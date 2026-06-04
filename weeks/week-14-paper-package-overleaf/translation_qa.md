# Week 14 Translation QA

## Terms To Keep Bilingual

| English term | Vietnamese support | QA note |
|---|---|---|
| paper package | gói paper / bộ hồ sơ paper | Keep English anchor because it maps to final deliverable. |
| reproducibility note | ghi chú tái lập | Explain as a file map + rerun note. |
| Zotero | Zotero | Tool name; do not translate. |
| Word + Zotero | Word + Zotero | Default route for beginner paper writing. |
| Quarto | Quarto | Optional reproducible report route. |
| Overleaf | Overleaf | Optional LaTeX route, not required core. |
| `.bib` file | file `.bib` | Explain as bibliography database for Quarto/Overleaf. |
| tool route | lộ trình công cụ | Means chosen writing/citation workflow. |

## Common Bilingual Risks

- "Package" should not sound like software installation; here it means a paper-ready folder.
- "Overleaf option" must be translated as optional, not required.
- "Reproducibility" should be practical: where files are and how to rerun, not a philosophy lecture.
- "Word + Zotero" should be presented as academically valid, not a lower-status choice.

## QA Report

| Surface | Status | Notes |
|---|---|---|
| `index.html` | Pass after revision | Vietnamese default frames Week 14 as consolidation; English aggregate translation keys were removed. |
| `slides.html` | Pass after revision | Learner-facing labels, figure alt text, and sentence frames have bilingual support. |
| `interactive_demo.html` | Pass after revision | Tool-route scale has visible explanation and screen-reader support. |
| `live_coding.html` | Pass after revision | Vietnamese notebook headings are no longer English-only; Colab fallback is explained. |

## Final Check

- [x] Vietnamese default makes clear that Week 14 is consolidation.
- [x] English mode does not leave Vietnamese-only tool instructions in learner-facing controls.
- [x] The learner is not pushed into LaTeX if Word + Zotero fits the target.
- [x] `.bib`, Quarto, and Overleaf are framed as optional routes.
