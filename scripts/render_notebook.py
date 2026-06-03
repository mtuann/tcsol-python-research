#!/usr/bin/env python3
"""Render a simple Jupyter notebook to learner-facing HTML.

This project is published as a static GitHub Pages site. Direct `.ipynb`
URLs render as raw JSON there, so weekly notebooks should be rendered to an
HTML companion page and linked from the learner-facing site.

The renderer intentionally uses only Python standard library modules. It is
enough for early-course notebooks that use Markdown, code, stdout, and simple
CSV/file operations. For later notebooks with rich plots, use nbconvert or
Quarto and keep the same public-link policy.
"""

from __future__ import annotations

import argparse
import contextlib
import html
import io
import json
import os
import re
import traceback
from pathlib import Path
from typing import Any


REPO_NAME = "tcsol-python-research"
REPO_OWNER = "mtuann"


def source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def render_markdown(markdown: str) -> str:
    blocks: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            blocks.append(f"<p>{inline_markdown(text)}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_type, list_items
        if list_type and list_items:
            items = "".join(f"<li>{inline_markdown(item)}</li>" for item in list_items)
            blocks.append(f"<{list_type}>{items}</{list_type}>")
        list_type = None
        list_items = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        unordered = re.match(r"^-\s+(.+)$", line)
        quote = re.match(r"^>\s+(.+)$", line)

        if heading:
            flush_paragraph()
            flush_list()
            level = min(len(heading.group(1)) + 1, 4)
            blocks.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
        elif ordered:
            flush_paragraph()
            if list_type != "ol":
                flush_list()
                list_type = "ol"
            list_items.append(ordered.group(1))
        elif unordered:
            flush_paragraph()
            if list_type != "ul":
                flush_list()
                list_type = "ul"
            list_items.append(unordered.group(1))
        elif quote:
            flush_paragraph()
            flush_list()
            blocks.append(f"<blockquote>{inline_markdown(quote.group(1))}</blockquote>")
        else:
            paragraph.append(line)

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def execute_notebook(nb: dict[str, Any], repo_root: Path) -> dict[str, Any]:
    namespace: dict[str, Any] = {"__name__": "__main__"}
    original_cwd = Path.cwd()
    os.chdir(repo_root)
    try:
        execution_count = 1
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "code":
                continue

            cell["execution_count"] = execution_count
            execution_count += 1
            stdout = io.StringIO()
            source = source_text(cell)
            outputs: list[dict[str, Any]] = []

            try:
                with contextlib.redirect_stdout(stdout):
                    exec(compile(source, "<notebook-cell>", "exec"), namespace)
            except Exception:
                text = stdout.getvalue()
                if text:
                    outputs.append({"name": "stdout", "output_type": "stream", "text": text})
                outputs.append(
                    {
                        "ename": "ExecutionError",
                        "evalue": "Cell failed while rendering",
                        "output_type": "error",
                        "traceback": traceback.format_exc().splitlines(),
                    }
                )
                cell["outputs"] = outputs
                raise

            text = stdout.getvalue()
            if text:
                outputs.append({"name": "stdout", "output_type": "stream", "text": text})
            cell["outputs"] = outputs
    finally:
        os.chdir(original_cwd)

    return nb


def render_outputs(cell: dict[str, Any]) -> str:
    rendered: list[str] = []
    for output in cell.get("outputs", []):
        output_type = output.get("output_type")
        if output_type == "stream":
            text = output.get("text", "")
            if isinstance(text, list):
                text = "".join(text)
            rendered.append(
                '<div class="nb-output">'
                '<div class="nb-output-label">Output</div>'
                f"<pre><code>{html.escape(str(text).rstrip())}</code></pre>"
                "</div>"
            )
        elif output_type == "error":
            trace = "\n".join(output.get("traceback", []))
            rendered.append(
                '<div class="nb-output nb-error">'
                '<div class="nb-output-label">Error</div>'
                f"<pre><code>{html.escape(trace)}</code></pre>"
                "</div>"
            )
    return "\n".join(rendered)


def render_cells(nb: dict[str, Any]) -> str:
    parts: list[str] = []
    code_count = 0
    for index, cell in enumerate(nb.get("cells", []), start=1):
        cell_type = cell.get("cell_type")
        if cell_type == "markdown":
            parts.append(
                '<article class="nb-cell nb-markdown" data-cell-type="markdown">'
                f"{render_markdown(source_text(cell))}"
                "</article>"
            )
        elif cell_type == "code":
            code_count += 1
            code = html.escape(source_text(cell).rstrip())
            outputs = render_outputs(cell)
            parts.append(
                '<article class="nb-cell nb-code" data-cell-type="code">'
                f'<div class="nb-input-label">In [{code_count}]</div>'
                f"<pre><code>{code}</code></pre>"
                f"{outputs}"
                "</article>"
            )
        else:
            parts.append(
                '<article class="nb-cell nb-unknown">'
                f"<p>Unsupported cell {index}: {html.escape(str(cell_type))}</p>"
                "</article>"
            )
    return "\n".join(parts)


def notebook_title(nb: dict[str, Any]) -> str:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in source_text(cell).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return "Rendered Notebook"


def build_html(nb: dict[str, Any], notebook_path: Path, repo_root: Path) -> str:
    rel_path = notebook_path.relative_to(repo_root).as_posix()
    title = notebook_title(nb)
    colab_url = (
        f"https://colab.research.google.com/github/{REPO_OWNER}/{REPO_NAME}/blob/main/{rel_path}"
    )
    source_name = notebook_path.name
    rendered_cells = render_cells(nb)

    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | Rendered Notebook</title>
  <link rel="stylesheet" href="../../assets/css/bilingual.css">
  <link rel="stylesheet" href="../../assets/css/course-doc.css">
</head>
<body>
  <header class="doc-topbar">
    <a class="doc-brand" href="../../" data-i18n="brand">Python Research Hub</a>
    <nav class="doc-nav" aria-label="Điều hướng notebook" data-i18n-aria-label="nav.aria">
      <a href="./" data-i18n="nav.week">Week 01</a>
      <a href="slides.html" data-i18n="nav.slides">Slides</a>
      <a href="interactive_demo.html" data-i18n="nav.demo">Demo</a>
      <a href="{html.escape(source_name)}" download data-i18n="nav.source">Source .ipynb</a>
      <nav class="language-switcher" aria-label="Ngôn ngữ / Language" data-i18n-aria-label="nav.language">
        <button type="button" data-lang-option="vi" aria-pressed="true">Tiếng Việt</button>
        <button type="button" data-lang-option="en" aria-pressed="false">English</button>
      </nav>
    </nav>
  </header>

  <main class="doc-shell notebook-shell">
    <aside class="doc-sidebar">
      <strong data-i18n="side.title">Notebook</strong>
      <a href="./" data-i18n="side.week">Tổng quan tuần</a>
      <a href="{html.escape(colab_url)}" data-i18n="side.colab">Chạy bằng Colab</a>
      <a href="{html.escape(source_name)}" download data-i18n="side.source">Tải source .ipynb</a>
      <a href="data/raw/week01_research_tracks.csv" data-i18n="side.csv">CSV dữ liệu</a>
    </aside>

    <div class="doc-main">
      <section class="doc-hero">
        <span class="doc-eyebrow" data-i18n="hero.tag">Rendered notebook</span>
        <h1>{html.escape(title)}</h1>
        <p class="doc-lead" data-i18n="hero.body">Đây là bản HTML đã chạy sẵn để đọc trên GitHub Pages. Muốn thực hành, mở notebook trong Colab hoặc tải file .ipynb.</p>
        <div class="doc-actions">
          <a class="doc-button" href="{html.escape(colab_url)}" data-i18n="action.colab">Chạy trong Colab</a>
          <a class="doc-button secondary" href="{html.escape(source_name)}" download data-i18n="action.source">Tải .ipynb</a>
          <a class="doc-button secondary" href="./" data-i18n="action.week">Quay lại Week 01</a>
        </div>
      </section>

      <section class="doc-card notebook-note">
        <h2 data-i18n="note.title">Cách dùng trang này</h2>
        <div class="doc-grid three">
          <article class="mini-card"><span class="swatch blue"></span><h3 data-i18n="note.read.title">Đọc</h3><p data-i18n="note.read.body">Bản HTML giữ code và output cạnh nhau, phù hợp để ôn lại sau buổi học.</p></article>
          <article class="mini-card"><span class="swatch green"></span><h3 data-i18n="note.run.title">Chạy</h3><p data-i18n="note.run.body">Nút Colab mở notebook có thể chạy từng cell và tự tải CSV nếu không có file local.</p></article>
          <article class="mini-card"><span class="swatch amber"></span><h3 data-i18n="note.source.title">Source</h3><p data-i18n="note.source.body">File .ipynb vẫn được giữ để tải, nộp bài hoặc chỉnh trong JupyterLab/VS Code.</p></article>
        </div>
      </section>

      <section class="notebook-document" aria-label="Rendered notebook cells">
        {rendered_cells}
      </section>
    </div>
  </main>

  <script src="../../assets/js/bilingual.js"></script>
  <script>
    window.Bilingual.init({{
      defaultLang: "vi",
      translations: {{
        vi: {{
          "brand": "Python Research Hub",
          "nav.aria": "Điều hướng notebook",
          "nav.week": "Week 01",
          "nav.slides": "Slides",
          "nav.demo": "Demo",
          "nav.source": "Source .ipynb",
          "nav.language": "Ngôn ngữ / Language",
          "side.title": "Notebook",
          "side.week": "Tổng quan tuần",
          "side.colab": "Chạy bằng Colab",
          "side.source": "Tải source .ipynb",
          "side.csv": "CSV dữ liệu",
          "hero.tag": "Rendered notebook",
          "hero.body": "Đây là bản HTML đã chạy sẵn để đọc trên GitHub Pages. Muốn thực hành, mở notebook trong Colab hoặc tải file .ipynb.",
          "action.colab": "Chạy trong Colab",
          "action.source": "Tải .ipynb",
          "action.week": "Quay lại Week 01",
          "note.title": "Cách dùng trang này",
          "note.read.title": "Đọc",
          "note.read.body": "Bản HTML giữ code và output cạnh nhau, phù hợp để ôn lại sau buổi học.",
          "note.run.title": "Chạy",
          "note.run.body": "Nút Colab mở notebook có thể chạy từng cell và tự tải CSV nếu không có file local.",
          "note.source.title": "Source",
          "note.source.body": "File .ipynb vẫn được giữ để tải, nộp bài hoặc chỉnh trong JupyterLab/VS Code."
        }},
        en: {{
          "brand": "Python Research Hub",
          "nav.aria": "Notebook navigation",
          "nav.week": "Week 01",
          "nav.slides": "Slides",
          "nav.demo": "Demo",
          "nav.source": "Source .ipynb",
          "nav.language": "Language",
          "side.title": "Notebook",
          "side.week": "Week overview",
          "side.colab": "Run in Colab",
          "side.source": "Download source .ipynb",
          "side.csv": "Data CSV",
          "hero.tag": "Rendered notebook",
          "hero.body": "This is the pre-run HTML version for GitHub Pages. To practice, open the notebook in Colab or download the .ipynb file.",
          "action.colab": "Run in Colab",
          "action.source": "Download .ipynb",
          "action.week": "Back to Week 01",
          "note.title": "How to use this page",
          "note.read.title": "Read",
          "note.read.body": "The HTML version keeps code and output together, useful for review after class.",
          "note.run.title": "Run",
          "note.run.body": "The Colab button opens a runnable notebook and downloads the CSV automatically when local files are unavailable.",
          "note.source.title": "Source",
          "note.source.body": "The .ipynb file remains available for download, submission, or editing in JupyterLab/VS Code."
        }}
      }}
    }});
  </script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--write-executed", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    notebook_path = args.notebook.resolve()
    output_path = args.output.resolve()
    nb = json.loads(notebook_path.read_text(encoding="utf-8"))

    if args.execute:
        nb = execute_notebook(nb, repo_root)

    output_path.write_text(build_html(nb, notebook_path, repo_root), encoding="utf-8")

    if args.write_executed:
        notebook_path.write_text(
            json.dumps(nb, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
