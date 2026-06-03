# Week 01 Translation QA

Status: locally validated on 2026-06-03.

## Language Switch

- [x] `slides.html` opens with Vietnamese text and `<html lang="vi">`.
- [x] `interactive_demo.html` opens with Vietnamese text and `<html lang="vi">`.
- [x] Both pages include a Tiếng Việt / English switcher.
- [x] Shared helper stores the selected language but Vietnamese remains the no-JavaScript default.

## Coverage

- [x] Slide titles, body text, navigation buttons, workflow labels, tables, and captions are bilingual.
- [x] Interactive demo headings, track buttons, detail labels, chart titles, fallback table, and accessibility labels are bilingual.
- [x] Notebook Markdown instructions are revised Vietnamese-first.
- [x] README, lecture notes, exercises, assignment, readings, data dictionary, rubric, and instructor notes are revised Vietnamese-first.

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
