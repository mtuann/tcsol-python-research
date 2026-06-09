# Week 01 Translation QA

Status: locally validated on 2026-06-03.

## Language Switch

- [x] `slides.html` opens with Vietnamese text and `<html lang="vi">`.
- [x] `interactive_demo.html` opens with Vietnamese text and `<html lang="vi">`.
- [x] `index.html` and `live_coding.html` open with Vietnamese text and `<html lang="vi">`.
- [x] Both pages include a Tiếng Việt / English switcher.
- [x] Shared helper stores the selected language but Vietnamese remains the no-JavaScript default.

## Coverage

- [x] Slide titles, body text, navigation buttons, workflow labels, tables, and captions are bilingual.
- [x] Interactive demo headings, track buttons, detail labels, chart titles, fallback table, and accessibility labels are bilingual.
- [x] Week overview sidebar/actions are bilingual and link to rendered HTML pages first.
- [x] Rendered notebook page has bilingual action labels for Colab, source notebook download, and week overview.
- [x] Notebook Markdown instructions are revised Vietnamese-first.
- [x] README, lecture notes, exercises, assignment, readings, data dictionary, rubric, and instructor notes are revised Vietnamese-first.

## Public Navigation

- [x] Homepage Week 01 notebook link points to `live_coding.html`, with Colab as a separate run option.
- [x] Week overview links to `slides.html`, `interactive_demo.html`, `live_coding.html`, Colab, and source `.ipynb` download.
- [x] Slides include persistent homepage/week links, previous/next controls, slide counter, page-number jump, and final-slide next-step CTAs.
- [x] Rendered notebook HTML includes Colab, source `.ipynb` download, and a link back to Week 01.
- [x] Raw Markdown and `.ipynb` links are labeled as source/download rather than learner-facing reading links.

## Terminology

- [x] Week glossary exists as `glossary_week01.csv`.
- [x] Core terms align with `resources/glossary/core_glossary.csv`.
- [x] Code, file names, column names, library names, and citation metadata remain in English.
- [x] English anchor terms are used where useful: notebook, Markdown, code, variable, CSV, unit of observation.

## Beginner Load

- [x] Website shows one language at a time instead of long side-by-side paragraphs.
- [x] Week 01 keeps one core Python idea: variables/text values.
- [x] CSV/path/export cells are still instructor-provided sample code.
- [x] Stretch task is clearly optional.

## Accessibility and Fallback

- [x] Language buttons and track buttons use `aria-pressed`.
- [x] Interactive demo has a screen-reader chart summary.
- [x] Slide keyboard navigation ignores focused buttons/links.
- [x] Local browser test confirms language switch and track interaction.
- [x] Visual slide refresh checked in local browser: workflow cards, mini tables, notebook visual, and caption mockup render without overlap on desktop.
- [x] Live slide exit navigation checked after deploy: no overflow, no overlap, and links route back to the week overview/home.
- [x] Rendered notebook HTML checked after deploy: no overflow, code/output blocks render, and source links are clearly labeled.
