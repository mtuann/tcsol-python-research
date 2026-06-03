# Translation QA Checklist

Copy this file into a week folder as `translation_qa.md`.

## Language Switch

- [ ] Page opens in Vietnamese by default.
- [ ] English switch changes all public learner-facing text.
- [ ] Switching language updates `<html lang>`.
- [ ] Language preference is saved only as a convenience; Vietnamese remains the no-JS default.

## Coverage

- [ ] Slide titles, body text, buttons, links, and navigation labels are bilingual.
- [ ] Interactive demo headings, buttons, chart titles, fallback text, tables, and accessibility labels are bilingual.
- [ ] Notebook Markdown instructions are Vietnamese-first.
- [ ] Assignment, exercises, rubric, readings, and data dictionary are Vietnamese-first.

## Terminology

- [ ] Week glossary is updated.
- [ ] Core terms match `resources/glossary/core_glossary.csv`.
- [ ] Code names, file names, library names, column names, and citation metadata remain in English.
- [ ] English anchor terms are included only where they help learning.

## Beginner Load

- [ ] No long Vietnamese-English parallel paragraphs in beginner-facing pages.
- [ ] Each slide has one main idea.
- [ ] Core task is still doable without programming background.
- [ ] Stretch content is clearly optional.

## Accessibility and Fallback

- [ ] Language buttons use `aria-pressed`.
- [ ] Interactive controls have accessible names.
- [ ] Keyboard navigation still works after adding the language switcher.
- [ ] No-JavaScript fallback remains understandable in Vietnamese.
