# Bilingual Style Guide

Default learner-facing language is Vietnamese. English is available as an option for review, reuse, and future public sharing.

## Voice

- Vietnamese should be direct, calm, and beginner-friendly.
- English should be natural academic English, not word-for-word translation.
- Prefer short sentences in both languages.
- Use "bạn" for the learner in Vietnamese.

## Terminology

- First mention: Vietnamese term + English anchor, for example `biến (variable)`.
- Later mentions: Vietnamese term only, unless the English term is needed for software UI.
- Keep these in English: Python code, package names, function names, file names, column names, URLs, citation titles.
- Keep tool names in English: Word, Zotero, Quarto, Overleaf, LaTeX.
- Use `hỗ trợ viết paper (writing support)` when introducing the weekly writing layer.
- Use `mẫu câu viết học thuật (sentence frame)` for beginner writing scaffolds.

## Layout

- Website pages should show one language at a time.
- Avoid full paragraph-by-paragraph duplication on beginner pages.
- Slides should be concise: one main idea per slide, one small code block at most.
- Interactive demos should translate controls, labels, chart titles, fallback text, and screen-reader summaries.

## Translation QA

- Check Vietnamese first, because it is the default no-JavaScript experience.
- Then switch to English and check that no Vietnamese learner-facing labels remain.
- Verify that `<html lang>` changes with the selected language.
- Keep weekly glossary entries synchronized with the content.
