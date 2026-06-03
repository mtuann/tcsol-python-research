# Weekly Lesson Design Standard

Last source audit: 2026-06-03

This file is the design contract for every week in the course. Each week must follow this structure unless there is an explicit reason recorded in that week's `README.md`.

The course is not a generic Python course. Every week must connect Python to one of the learner's research directions:

- short-term Chinese teaching and TCSOL;
- Chinese-Vietnamese contrastive analysis;
- machine translation evaluation and MTPE;
- education policy analysis.

The weekly loop is:

```text
research question -> small dataset -> Python skill -> table/figure -> interpretation -> paper-ready writing -> paper-ready output
```

## Non-Negotiable Rules

Every week must include:

1. One main Python skill.
2. One small research question.
3. One dataset or data template.
4. One worked example.
5. One guided exercise.
6. One independent applied task.
7. One figure or table suitable for a paper draft.
8. One caption and interpretation paragraph.
9. One explicit writing-support block: paper section, writing output, tool support, sentence frame, and common writing risk.
10. One technical reading and one research/method reading.
11. One reproducibility checklist.

Do not add a hard dataset and a hard Python concept in the same week. If the Python skill is new, the dataset must be simple. If the dataset is messy or realistic, the Python skill must already be familiar.

## Canonical Week Pattern

Week 01 is the canonical beginner content pattern. Week 02 is the canonical visual slide pattern. Future weeks should reuse this combined structure unless the week's `README.md` records a clear reason to differ.

The canonical public path pattern is:

```text
course homepage
  -> weeks/week-XX-topic-slug/
    -> slides.html
    -> interactive_demo.html
    -> live_coding.html
    -> Colab link
    -> clearly labeled source .ipynb / Markdown links
```

Required learner-facing week surfaces:

- folder `index.html`: overview, research frame, writing support, notes, exercises, assignment, readings, rubric, and source links;
- `slides.html`: bilingual stage-first deck using `assets/css/lecture-slides.css`, language switcher, page-number jump, keyboard navigation, visible course exit links, and final-slide next-step CTAs;
- `live_coding.html`: rendered notebook with code/output, Colab action, source notebook download, and link back to the week overview;
- `interactive_demo.html`: included when interaction improves learning; if not included, record the reason in the week's `README.md`;
- homepage cards/links: point to public HTML pages first, not raw source files.

Required source surfaces:

- Markdown files remain editable source and may be exposed only in a clearly labeled instructor/source area;
- `.ipynb` remains the runnable source and may be exposed only as source/download or through Colab;
- generated/rendered HTML is the main learner reading experience.

Canonical Week 01 quality rules:

- If a rendered notebook page has a language switcher, notebook Markdown instructions must also be bilingual, not only the shell navigation.
- Advanced code cells in Weeks 1-2 must be labeled as run-only instructor code; learner tasks should say "run and read output" unless the learner has already practiced the construct.
- The research question, unit of observation, starter dataset, likely output, and beginner task must align in every track.
- Track examples must not claim learner-transfer evidence unless the dataset includes learner production or learner-error rows.
- MTPE labels used before the full MQM framework must be called simplified or MQM-inspired labels.
- Interactive demos must include exit links back to the homepage, week overview, slides, and notebook.
- Lecture slides must use `.inline-token` for short code/data terms inside prose and `.inline-token.value-token` or `.value-spotlight` for emphasized values such as `72`; do not leave raw Markdown backticks inside `data-i18n` strings.

## Beginner-First Layering

The standard is comprehensive for the instructor, but the learner is a complete programming beginner. Each weekly file must separate content into three levels:

| Level | Audience | Meaning |
|---|---|---|
| Core | learner | Required. Must be short, concrete, and doable in the week. |
| Stretch | learner, optional | Extra practice for curiosity or faster progress. |
| Instructor-only | instructor | Pedagogical notes, advanced explanation, source audit, and future expansion. |

For Weeks 1-4, the learner-facing Core must stay light:

- no more than one new Python concept;
- one dataset with 10-100 rows;
- one short table or figure;
- one 100-150 word interpretation;
- no regression, COMET, advanced Git, APIs, scraping, JavaScript authoring, or Overleaf/LaTeX authoring.

The instructor may prepare HTML slides, interactive visualizations, and source audits, but the learner only needs to use them, not build them, until later weeks.

## Bilingual Website Standard

All public website content must support Vietnamese and English.

Default language:

- Vietnamese is the default language for learner-facing website content.
- English is available through a clear language switcher.
- Use language codes `vi` and `en`; do not use `vn`.

Recommended delivery:

- Beginner weeks use one HTML page with a Vietnamese default and an English toggle.
- Larger future pages may use two route trees: Vietnamese unprefixed paths and English under `/en/`.
- Shared data, images, figures, and code examples must not be duplicated for each language.
- HTML files must set `<html lang="vi">` by default and update the language when the learner switches to English.
- Learner-facing navigation on GitHub Pages must link to `.html` pages or folder `index.html` pages, not raw `.md` or raw `.ipynb` files. Markdown and notebooks remain authoring/runnable sources and may be linked only as clearly labeled source material.

Content style:

- Use Vietnamese-first explanations with English anchor terms in parentheses when useful, such as `biến (variable)` or `đơn vị quan sát (unit of observation)`.
- Do not show full Vietnamese and full English paragraphs side by side in beginner weeks.
- Keep code, file names, column names, package names, function names, and citation metadata in English.
- Translate learner-facing instructions, slide text, labels, buttons, chart titles, captions, and accessibility labels.
- Instructor notes may be Vietnamese-first with concise English labels only when they help future reuse.

Production workflow:

```text
week brief -> content blocks -> glossary check -> bilingual draft -> artifact build -> translation QA -> learner release
```

Required support files for every week:

- `content_blocks.md`: bilingual source blocks for slide/demo text and key learner instructions.
- `glossary_weekXX.csv`: week-specific terms with Vietnamese, English, and notes.
- `translation_qa.md`: final checklist for language switch, terminology, accessibility, and learner load.
- `slide_prompt_sources.md`: source and prompt log for visual slide references, generated assets, and original diagrams.

Course-wide support files:

- `resources/style_guides/bilingual_style_guide.md`;
- `resources/glossary/core_glossary.csv`;
- `resources/templates/bilingual_content_blocks_template.md`;
- `resources/templates/translation_qa_checklist.md`.
- `resources/templates/slide_prompt_sources_template.md`;
- `resources/slide_design/visual_slide_playbook.md`.

## Standard Week Folder

Each week should use this structure:

```text
weeks/week-XX-topic-slug/
├── README.md
├── content_blocks.md
├── slides.qmd
├── slides.html
├── interactive_demo.qmd
├── interactive_demo.html
├── lecture_notes.md
├── live_coding.ipynb
├── live_coding.html
├── exercises.md
├── assignment.md
├── readings.md
├── data_dictionary.md
├── rubric.md
├── instructor_notes.md
├── glossary_weekXX.csv
├── translation_qa.md
├── slide_prompt_sources.md
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── interactive/
└── references/
```

Minimum submission from the learner:

```text
notebook + cleaned data or derived table + figure/table + caption + interpretation paragraph + paper-facing writing + source list
```

## Weekly README Template

Each week's `README.md` must contain:

```markdown
# Week XX: [Title]

## Research Frame

- Research area:
- Small research question:
- Why this matters for TCSOL / Chinese-Vietnamese contrastive research / MTPE / education policy:

## Python Skill

- Main skill:
- Supporting skills:
- Functions/libraries:

## Writing Support

- Paper section supported:
- Writing output:
- Tool support:
- Sentence frame:
- Common writing risk:

## Learning Objectives

By the end of this week, the learner can:

1. ...
2. ...
3. ...

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Dataset or data template follows the schema.
- [ ] One table or figure is exported.
- [ ] Caption explains N, variables, units, method, and main finding.
- [ ] Interpretation paragraph separates description, inference, and limitation.
- [ ] Writing output is ready to paste into Word, Quarto, or the final paper draft.
- [ ] Sources are cited with links and access date.

## Files

- Slides:
- Interactive demo:
- Lecture notes:
- Notebook:
- Exercises:
- Assignment:
- Data dictionary:
- Rubric:
```

## Weekly Rhythm

| Stage | Time | Required content |
|---|---:|---|
| Pre-class | 30-45 min | read short notes, inspect dataset, answer 2 warm-up questions |
| Lecture | 45-60 min | concept, research use case, common mistakes, mini demo |
| Live coding | 30-45 min | instructor codes from blank/skeleton notebook |
| Guided practice | 30-45 min | learner modifies and completes partially written code |
| Writing bridge | 10-15 min | turn the output into a caption, Results sentence, Methods note, or limitation |
| Debrief | 10-15 min | discuss bugs, research interpretation, figure/table choices, writing risk |
| Homework | 60-120 min | notebook + memo + figure/table/caption + paper-facing paragraph |

## Writing Support and Paper Tooling Standard

Every week must support paper writing, but tools must be layered gently.

Default progression:

| Stage | Weeks | Writing focus | Tool support |
|---|---:|---|---|
| Foundation | 1-2 | research question, data unit, source note | notebook Markdown; Word optional |
| Evidence | 3-5 | descriptive table, figure caption, figure note | Word + Zotero setup begins |
| Results | 6-8 | Results paragraph, limitation, teaching implication | Word + Zotero |
| Track writing | 9-13 | track-specific analysis paragraph | Word + Zotero; Quarto optional |
| Paper package | 14 | mini paper, appendix, references, reproducibility note | Word + Zotero by default; Overleaf/Quarto optional |

Required weekly writing block:

```markdown
## Writing Support

- Paper section supported:
- Writing output:
- Tool support:
- Sentence frame:
- Common writing risk:
```

Overleaf/LaTeX policy:

- Do not introduce Overleaf in Weeks 1-6.
- Do not require Overleaf unless the target journal, university, or template needs LaTeX.
- Introduce Overleaf in Week 14 as a packaging option after the learner already has draft sections, references, tables, and figures.
- Word + Zotero remains the default first writing workflow.
- Quarto is optional for reproducible reports after notebooks and figures are comfortable.

Course-wide roadmap: `resources/WRITING_AND_PAPER_TOOLING_ROADMAP.md`.

## Slide Deck Standard

Each week needs 10-18 slides. Use Quarto Reveal.js as the preferred source format:

```text
slides.qmd -> slides.html
```

If Quarto is not installed locally, still create `slides.qmd` as the source and provide a static `slides.html` fallback that can be opened in a browser or deployed to GitHub Pages.

Required slide sequence:

1. Title and research question.
2. Why this week's skill matters for paper writing.
3. Data preview: rows, columns, variables, source.
4. Conceptual explanation without code.
5. Python syntax or library concept.
6. Tiny worked example.
7. Research example using the week's dataset.
8. Common mistakes and debugging signs.
9. Figure/table target for the week.
10. Caption and interpretation example.
11. Assignment requirements.
12. Reproducibility checklist.

Optional slides:

- contrastive Chinese-Vietnamese examples;
- MT/MTPE error examples;
- education policy timeline or coding example;
- paper Methods/Results excerpt.

### Visual Slide Standard

Each deck should feel like a guided research explanation, not a text document broken into slides. Follow `resources/slide_design/visual_slide_playbook.md`.

Required visual rhythm:

1. Start with a concrete visual hook.
2. Use one slide for one conceptual job.
3. Prefer original HTML/CSS/SVG diagrams over long paragraphs.
4. Use color semantically: blue for Python/action, green for evidence/output, amber for caution/limitation, red for mistakes, gray for metadata/source.
5. Include at least three original visual components per week, such as workflow maps, dataset previews, paper-output mockups, before/after cards, or caption anatomy cards.
6. Track every external visual reference, generated-image prompt, or AI-assisted diagram in `slide_prompt_sources.md`.

Never copy images, diagrams, or exact CSS from an external slide deck unless the license explicitly allows reuse and the source is recorded.

### HTML Slide Requirements

The rendered `slides.html` should:

- run as a static file on GitHub Pages;
- not require a Python server;
- use Reveal.js through Quarto when available, or a documented standalone static HTML fallback;
- include the shared bilingual language switcher when published on the website;
- default to Vietnamese and allow English without duplicating the whole file in beginner weeks;
- include keyboard navigation, previous/next controls, page-number jump, and a visible slide counter;
- include persistent exit links to the course homepage and week overview;
- include final-slide next-step CTAs to the rendered notebook, interactive demo when available, week overview, and homepage;
- include speaker notes when useful;
- avoid heavy animation in beginner weeks;
- link to `interactive_demo.html` when interaction would distract from the main slide flow.

Do not require the learner to edit HTML, CSS, or JavaScript in Weeks 1-8.

## Public HTML Document Standard

Markdown files such as `README.md`, `lecture_notes.md`, `exercises.md`, `assignment.md`, `readings.md`, and `rubric.md` are source files. GitHub Pages serves direct `.md` URLs as text/markdown in this static deployment, so they are not appropriate as the main learner reading experience.

Every learner-facing Markdown source should have one of these public HTML paths:

- a folder `index.html` that collects the week's overview, notes, exercises, assignment, readings, and rubric;
- or a dedicated `.html` page when the document is long enough to stand alone.

Public HTML pages must:

- use the shared bilingual language switcher;
- preserve headings, tables, lists, code blocks, and links in rendered HTML;
- include clear actions to slides, rendered notebook, Colab, demo, and writing roadmap where relevant;
- include a small instructor/source section only when source access is useful;
- avoid sending learners directly to raw Markdown from homepage/course navigation.

## Notebook Publication Standard

Notebook files such as `live_coding.ipynb` are runnable source files. GitHub Pages may serve direct `.ipynb` URLs as raw notebook JSON, so they are not appropriate as the main learner reading experience.

Every week with a notebook must publish:

- `live_coding.ipynb`: runnable source notebook;
- `live_coding.html`: rendered notebook with code, output, and learner-facing action buttons;
- a Colab link for browser-based execution when the notebook can run without local setup.

Public links should use this order:

1. rendered notebook HTML for reading;
2. Colab for running;
3. raw `.ipynb` only as clearly labeled source/download.

For beginner weeks, make Colab notebooks self-contained: either commit the small CSV data needed for the lesson or add a fallback download from the public repository. For later weeks with rich plots or heavier dependencies, use `nbconvert` or Quarto to render notebooks, but keep the same public-link policy.

For simple beginner notebooks, the course renderer may be used:

```bash
./scripts/render_notebook.py weeks/week-XX-topic-slug/live_coding.ipynb weeks/week-XX-topic-slug/live_coding.html --execute --write-executed
```

Only use the lightweight renderer for notebooks with Markdown, code, stdout, and simple file outputs. Use `nbconvert` or Quarto for rich plots, images, math, widgets, or complex outputs.

## Interactive Demo Standard

Each week should include one lightweight interactive demo when it improves learning. The default path is:

```text
interactive_demo.qmd -> interactive_demo.html
```

Recommended tools:

| Tool | Use | Beginner suitability |
|---|---|---|
| Plotly | hover, zoom, dropdowns, interactive figures from Python | best default |
| Altair / Vega-Lite | concise statistical charts and selections | good after pandas basics |
| Observable Plot | rich web-native explanation | instructor-only unless learner knows JS |
| JupyterLite / Pyodide | run Python in browser | optional advanced, not default |

Avoid Dash and Streamlit for the public course site because they require a running server and are not suitable for plain GitHub Pages.

The interactive demo must include:

- a one-sentence learning goal;
- bilingual labels, chart titles, fallback text, and accessibility labels;
- a small dataset or embedded data sample;
- one interaction only in beginner weeks, such as hover, select, filter, or toggle;
- a plain-language interpretation guide;
- a non-interactive fallback table or summary in case JavaScript fails.

The learner's Week 1-6 task is to interpret the interactive visualization, not to build it from scratch.

## Lecture Notes Standard

Each `lecture_notes.md` must be 2-6 pages and include:

1. **Plain-language concept**
   Explain the Python idea without jargon first.

2. **Research use**
   Explain where the skill appears in a paper workflow.

3. **Annotated code**
   Include small code blocks with comments.

4. **Common mistakes**
   Show likely beginner errors and how to diagnose them.

5. **Mini cheat sheet**
   List the 5-10 commands/functions the learner should remember.

6. **Connection to final project**
   Explain which final project track can reuse this week's skill.

## Notebook Standard

The notebook must run from top to bottom with "Restart Kernel and Run All".

Required notebook sections:

1. **Title and research question**
2. **Paper connection**
   - target paper section;
   - writing output for this week;
   - sentence frame.
3. **Setup**
   - imports;
   - optional seed;
   - package versions if relevant.
4. **Load data**
   - file path;
   - source note;
   - first 5 rows.
5. **Inspect data**
   - dimensions;
   - column names;
   - missing values;
   - data types.
6. **Core Python skill**
   - one worked example;
   - one learner-editable example.
7. **Analysis**
   - summary table, metric, or transformation.
8. **Visualization or table**
   - export to `outputs/figures/` or `outputs/tables/`.
9. **Interpretation**
   - 100-200 words in Markdown.
10. **Paper-facing writing**
    - a caption, Methods note, Results paragraph, or Discussion/limitation paragraph ready to move into Word, Quarto, or the final paper draft.
11. **Limitations**
   - at least two limitations.
12. **Next step**
    - one possible improvement.

Do not leave hidden state. All variables needed by later cells must be created in earlier cells.

## Dataset Standard

Use CSV or Excel for beginner weeks. JSONL may be introduced only after the learner is comfortable with tables.

Minimum data documentation:

- source;
- access date;
- license or reuse note;
- unit of observation;
- column names;
- variable definitions;
- missing value codes;
- anonymization status.

Recommended dataset sizes:

| Stage | Rows | Data condition |
|---|---:|---|
| Weeks 1-4 | 10-100 | clean or almost clean |
| Weeks 5-8 | 50-500 | realistic missing values and labels |
| Weeks 9-12 | 100-1000 | multiple files, annotation, grouped data |
| Weeks 13-14 | project-sized | learner's selected final project data |

## Exercise Ladder

Every `exercises.md` must contain three levels.

### A. Copy and Modify

Learner changes variable names, column names, labels, or chart type in a worked example.

### B. Guided Problem

Learner follows a checklist but writes key lines independently.

### C. Research-Style Task

Learner answers a small research question with code and a short interpretation.

Example:

```text
A. Change the pre-test score chart into a post-test score chart.
B. Compute gain score and plot it by group.
C. Which group improved more, and what limitation prevents a causal claim?
```

## Assignment Standard

Each `assignment.md` must use this template:

```markdown
# Assignment: [Research Task]

## Goal

- Python skill:
- Research skill:
- Paper section supported:
- Writing output:

## Data

- File:
- Unit of observation:
- Key variables:

## Tasks

1. Load and inspect the dataset.
2. Clean or transform at least one variable.
3. Produce one table or figure.
4. Write a caption.
5. Write a 150-300 word interpretation.
6. Write one paper-facing paragraph or sentence frame.
7. Record one debugging note or limitation.

## Submission

- `.ipynb` notebook;
- exported table or figure;
- short memo or paper-facing paragraph in Markdown/Word;
- source list.
```

## Rubric Standard

Use a 100-point rubric every week.

| Criterion | Points | What to look for |
|---|---:|---|
| Code correctness | 25 | notebook runs, tasks answered, no hidden state |
| Code clarity | 15 | readable names, organized sections, minimal clutter |
| Data handling | 15 | schema followed, missing values handled, source recorded |
| Figure/table quality | 15 | labels, units, N, scale, export quality |
| Research writing and interpretation | 20 | meaningful claim, limitation, link to research question, usable paper-facing sentence/paragraph |
| Reproducibility | 10 | paths, package notes, source links, no manual output edits |

Track-specific rubric points may replace up to 20 points:

- TCSOL: learner-error coding consistency, teaching implication.
- Contrastive analysis: quality of Chinese-Vietnamese explanation.
- MTPE: error typology, human evaluation, post-editing rationale.
- Education policy: document coding transparency, policy context.

## Figure and Table Standard

Each week must produce at least one paper-facing figure or table.

### Required Figure Checklist

- Descriptive title or caption.
- X and Y labels with units.
- N or sample size visible in caption.
- Clear color palette; no unnecessary decoration.
- Axis scale does not distort the claim.
- Exported as `.png` for quick viewing and `.svg` or `.pdf` when needed for publication.
- If uncertainty is shown, caption states what it means: SD, SE, CI, bootstrap interval, etc.

### Required Table Checklist

- Clear title.
- Unit of observation.
- N and missing values.
- Rounded numbers consistently.
- Notes explain abbreviations.
- Statistics are not repeated redundantly in the text.

### Caption Formula

Use this formula:

```text
Figure/Table X. [Main finding in words]. Data are from [source], N = [sample size].
[Variables/units]. [Method/statistic]. [One limitation or reading note if needed].
```

Weak caption:

```text
Figure 1. Pre-test and post-test scores.
```

Better caption:

```text
Figure 1. Learners improved after the short result-complement lesson, but gains varied by initial proficiency. Data include 28 Vietnamese beginner learners, with scores measured on a 100-point classroom test. Points show individual learners and lines connect pre-test to post-test scores; the figure is descriptive and does not by itself establish causality.
```

## Research Track Standards

### TCSOL and Short-Term Chinese Teaching

Weekly artifacts should often include:

- `participant_profile.csv`;
- `course_context.md`;
- `lesson_log.csv`;
- `pretest_items.csv`;
- `posttest_scores.csv`;
- `learner_errors.csv`;
- `error_taxonomy.md`;
- `rubric_guidelines.md`.

Core schemas:

```csv
learner_id,age_range,L1,other_languages,prior_chinese_months,course_level,attendance_rate
S001,18-24,Vietnamese,English,6,beginner,0.92
```

```csv
learner_id,item_id,target_structure,learner_output,correct_form,error_type,severity,feedback_given
S001,Q03,result_complement,他写错了字,他把字写错了,complement_order,minor,recast
```

Required research habit:

- Always connect the Python output to a teaching decision.
- Do not stop at "this error is frequent"; explain how it changes lesson design.

### Chinese-Vietnamese Contrastive Analysis

Weekly artifacts should often include:

- `hv_contrastive_examples.csv`;
- `contrastive_codebook.md`;
- `teaching_notes.md`;
- `example_selection_log.md`.

Core schema:

```csv
example_id,zh_sentence,pinyin,vi_equivalent,feature,contrast_type,pedagogical_note
C001,我把书放在桌子上,wo3 ba3 shu1 fang4 zai4 zhuo1zi shang,Tôi đặt sách lên bàn,把-construction,word_order,Explain why 把 marks a disposal-like structure before comparing Vietnamese word order
```

Required research habit:

- Every contrastive claim needs examples.
- Every example needs a teaching or translation implication.

### MT Evaluation and MTPE

Weekly artifacts should often include:

- `mt_eval.csv`;
- `mtpe_guidelines.md`;
- `mqm_lite_error_typology.md`;
- `human_scores.csv`;
- `metric_results.csv`.

Core schema:

```csv
segment_id,domain,genre,zh_source,vi_reference,mt_system,vi_mt,vi_postedit,pe_time_seconds,error_type,severity,contrastive_note
M001,policy,paragraph,教育数字化推动资源共享,Giáo dục số thúc đẩy chia sẻ tài nguyên,system_a,...,...,42,terminology,major,...
```

Minimum human evaluation:

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Adequacy | serious meaning error | main idea preserved with gaps | meaning complete |
| Fluency | unnatural Vietnamese | understandable but awkward | natural Vietnamese |
| Terminology | wrong terms | partly inconsistent | consistent terms |
| Style/register | wrong register | acceptable | fits genre |

Simplified MQM-inspired labels:

- `accuracy`;
- `fluency`;
- `terminology`;
- `style`;
- `omission`;
- `addition`;
- `word_order`;
- `literal_translation`;
- `collocation`;
- `named_entity`;
- `sino_vietnamese_interference`.

Required research habit:

- Automatic metrics do not replace human evaluation.
- Always compare metric scores with at least 3 qualitative examples.

### Education Policy

Weekly artifacts should often include:

- `policy_docs.csv`;
- `policy_codebook.md`;
- `timeline.csv`;
- `theme_counts.csv`;
- `policy_excerpt_notes.md`.

Core schema:

```csv
doc_id,title,issuing_body,date,policy_area,target_group,theme,excerpt,url,access_date
P001,教育强国建设规划纲要（2024—2035年）,中共中央 国务院,2025-01-19,education reform,national,digitalization,...,https://...,2026-06-03
```

Required research habit:

- Separate policy description from policy evaluation.
- Quote short excerpts only when needed, and always preserve citation metadata.

## Reading and Source Update Protocol

Each week must include two kinds of reading:

1. **Technical reading**
   Official documentation when available.

2. **Research/method reading**
   A peer-reviewed paper, official report, standard, or major research guide.

Each `readings.md` must include:

```markdown
## Required Technical Reading

- Title:
- Link:
- Why it matters this week:
- Sections to read:

## Required Research/Method Reading

- Citation:
- Link:
- Research question:
- Method:
- Dataset:
- What we borrow this week:

## Source Update Log

- Search date:
- Search terms:
- Sources checked:
- Source selected:
- Why selected:
```

### Source Quality Tiers

Use this priority order:

1. Official documentation or official statistics.
2. Peer-reviewed journal/conference paper.
3. Academic preprint with clear authorship and methods.
4. University library or research guide.
5. Blog/tutorial only when it explains implementation better than official docs.

Do not rely on unattributed blog posts for methods, statistics, or policy claims.

### Suggested Search Queries

For TCSOL:

```text
Chinese as a second language learner error Vietnamese learners Mandarin 2024 2025
TCSOL short-term Chinese course pretest posttest study
Chinese proficiency grading standards international Chinese language education
```

For contrastive Chinese-Vietnamese:

```text
Chinese Vietnamese contrastive analysis measure words word order
Vietnamese learners Chinese result complement error analysis
Sino-Vietnamese words Chinese learning error analysis
```

For MT/MTPE:

```text
machine translation post-editing effort 2025
Chinese Vietnamese machine translation evaluation BLEU chrF COMET
WMT 2025 machine translation metrics human evaluation
MQM error typology machine translation evaluation
```

For education policy:

```text
site:moe.gov.cn 教育统计 2025 教育部
site:moe.gov.cn 教育强国建设规划纲要 2024 2035
OECD Education Policy Outlook 2025
UNESCO education policy strategy 2025
```

## Current Source Starter Pack

Use these as starting points, then update readings when building each week.

### Technical Documentation

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [JupyterLab User Guide](https://jupyterlab.readthedocs.io/en/stable/user/)
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [NumPy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [seaborn documentation](https://seaborn.pydata.org/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)
- [statsmodels User Guide](https://www.statsmodels.org/stable/user-guide.html)
- [Pingouin documentation](https://pingouin-stats.org/)
- [RapidFuzz documentation](https://rapidfuzz.github.io/RapidFuzz/)
- [sacreBLEU on PyPI](https://pypi.org/pypi/sacrebleu)
- [COMET documentation](https://unbabel.github.io/COMET/html/index.html)

### HTML Slides and Interactive Visualization

- [Quarto Reveal.js presentations](https://quarto.org/docs/presentations/revealjs/)
- [Quarto presenting slides](https://quarto.org/docs/presentations/revealjs/presenting.html)
- [Quarto GitHub Pages publishing](https://quarto.org/docs/publishing/github-pages.html)
- [Quarto interactive documents](https://quarto.org/docs/interactive/)
- [Plotly Python getting started](https://plotly.com/python/getting-started/)
- [Plotly `write_html`](https://plotly.com/python-api-reference/generated/plotly.io.write_html.html)
- [JupyterLite documentation](https://jupyterlite.readthedocs.io/)

### Writing, Citation, and Paper Packaging

- [Zotero Word processor plugin](https://www.zotero.org/support/word_processor_plugin_usage)
- [Zotero word processor integration](https://www.zotero.org/support/word_processor_integration)
- [Quarto citations](https://quarto.org/docs/authoring/citations.html)
- [Overleaf Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- [Overleaf bibliography management in LaTeX](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)
- [Overleaf `.bib` file documentation](https://docs.overleaf.com/citing-and-references/working-with-.bib-files)
- [Overleaf and Zotero](https://www.overleaf.com/learn/how-to/How_to_link_your_Overleaf_account_to_Mendeley_and_Zotero)

### Research Design, Tables, Figures, Reproducibility

- [Tidy Data](https://vita.had.co.nz/papers/tidy-data.html)
- [APA tables and figures guide, Purdue OWL](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/apa_tables_and_figures.html)
- [Ten Simple Rules for Better Figures](https://journals.plos.org/plosone/doi?id=10.1371/journal.pcbi.1003833)
- [The Turing Way](https://book.the-turing-way.org/)
- [FAIR Principles](https://www.nature.com/articles/sdata201618)
- [Equator Network reporting guidelines](https://www.equator-network.org/)

### TCSOL and Chinese as a Second Language

- [Chinese as a Second Language journal](https://www.benjamins.com/catalog/csl)
- [MOE: Chinese Proficiency Grading Standards launch](https://en.moe.gov.cn/news/press_releases/202104/t20210428_528917.html)
- [Chinese Proficiency Grading Standards overview](https://www.chinese.cn/zhuanti/202207/en/)
- [A Framework of Multilingual Conversion Errors, 2025](https://journals.sagepub.com/doi/full/10.1177/21582440251385737)
- [Mandarin tonal errors by Vietnamese learners](https://scholars.lib.ntu.edu.tw/handle/123456789/637277)
- [Chinese connectives error types in CSL learners](https://pmc.ncbi.nlm.nih.gov/articles/PMC8819010/)

### MT, MTPE, and Translation Evaluation

- [sacreBLEU GitHub repository](https://github.com/mjpost/sacrebleu)
- [COMET GitHub repository](https://github.com/Unbabel/COMET)
- [MQM error typology](https://themqm.org/error-types-2/typology/)
- [ISO 18587:2017 MTPE standard](https://www.iso.org/standard/62970.html)
- [Direction matters: post-editing and human translation effort, 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328511)
- [ViBidirectionMT-Eval: Vietnamese-Chinese MT evaluation](https://arxiv.org/abs/2501.08621)
- [WMT25 automated translation evaluation findings](https://aclanthology.org/2025.wmt-1.24.pdf)

### Education Policy

- [2024 National Education Development Statistical Bulletin, PRC MOE](https://www.moe.gov.cn/jyb_sjzl/sjzl_fztjgb/202506/t20250611_1193760.html)
- [Education Powerhouse Plan 2024-2035, PRC MOE](https://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/202501/t20250119_1176193.html)
- [Education Powerhouse Plan topic page, PRC MOE](https://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2025/2025_zt02/)
- [UNESCO education policies and strategies](https://www.unesco.org/en/education-policies)
- [OECD Education Policy Outlook 2025](https://www.oecd.org/en/publications/education-policy-outlook-2025_c3f402ba-en.html)

## 14-Week Artifact and Writing Progression

This table does not replace the syllabus. It defines the artifact emphasis for each week.

| Week | Main build | Required paper-facing output | Writing/tool output |
|---|---|---|---|
| 1 | research notebook basics + HTML slide demo | reproducible notebook with source note | research question + 100-150 word memo |
| 2 | data table and data dictionary | clean CSV template + codebook | data description paragraph |
| 3 | pandas summaries | descriptive table | table caption; Word + Zotero setup begins |
| 4 | data cleaning log | before/after cleaning table | cleaning decision note |
| 5 | visualization basics | bar/line/boxplot with caption | figure caption + figure note |
| 6 | basic statistics | test result table + interpretation | Results paragraph with limitation |
| 7 | TCSOL design | pre/post-test or rubric artifact | short teaching-study Methods draft |
| 8 | learner error analysis | error frequency chart + examples | learner-error Results paragraph |
| 9 | Chinese-Vietnamese contrastive analysis | contrastive examples table | contrastive example interpretation |
| 10 | teaching adaptation | data-driven teaching recommendation | pedagogical adaptation paragraph |
| 11 | MT evaluation | metric table + human score comparison | MT evaluation Results paragraph |
| 12 | MTPE analysis | post-editing effort chart + error table | MTPE workflow discussion paragraph |
| 13 | education policy coding | policy timeline or theme table | policy coding Methods paragraph; Quarto optional |
| 14 | final project | mini paper package + reproducibility checklist | Word + Zotero by default; optional Overleaf/Quarto package |

## Definition of Done

A week is complete only when all are true:

- `README.md` states the research question and Python skill.
- `README.md` states the weekly writing support block and tool support.
- Learner-facing website content opens in Vietnamese by default and can switch to English.
- `content_blocks.md`, `glossary_weekXX.csv`, `translation_qa.md`, and `slide_prompt_sources.md` are updated.
- `slides.qmd` and `slides.html` exist and follow the slide deck standard.
- `interactive_demo.html` exists or the week explicitly explains why no interaction is useful.
- Lecture notes explain the concept, code, mistakes, and research use.
- Notebook runs from top to bottom.
- Dataset is documented.
- Exercises include copy-modify, guided, and research-style levels.
- Assignment has clear deliverables.
- At least one figure or table is exported.
- Caption, interpretation, and paper-facing writing output are included.
- Readings include links and source audit notes.
- Rubric is present.
- Learner-facing Core is clearly separated from Stretch and Instructor-only content.
- Language switch, keyboard navigation, and no-JavaScript fallback are tested for public HTML.
- Slide visuals are original or properly sourced, and all prompts/sources are logged.
- No private learner data is exposed.
- Overleaf is not required before Week 14.

## Design Smell Checklist

Revise the week if any of these are true:

- The week teaches more than two new Python concepts.
- The dataset has no research context.
- The assignment only asks for code and no interpretation.
- The assignment only asks for interpretation and no paper-facing writing output.
- The HTML slide/demo requires the learner to understand JavaScript in beginner weeks.
- Overleaf or LaTeX is introduced before the learner has paper materials to format.
- The interactive demo has no plain-language fallback summary.
- The figure has no caption or N.
- The reading list has no current source or official documentation.
- MT metrics are treated as final truth.
- Education policy analysis quotes documents without metadata.
- Learner data is identifiable.
- The notebook only works if cells are run manually in a special order.
