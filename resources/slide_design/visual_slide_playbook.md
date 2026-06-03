# Visual Slide Playbook

Last audit: 2026-06-03

This playbook records slide-design patterns that can make the course website more vivid while staying beginner-friendly and original.

## Reference Audit

Reference observed:

- Source: https://uet-iai-course.github.io/image-processing-analysis/2526-2/lecture-9-intro-ML-DL-image-analysis.html
- Access date: 2026-06-03
- Local observation: HTML uses Reveal.js-style nested `<section>` slides, a white theme, a custom `lecture-style.css`, large image slides, inline SVG diagrams, two-column contrast layouts, callout boxes, color-coded concept cards, and a clear section-story structure.
- Prompt/source metadata: no explicit `prompt`, `Prompt`, `DALL`, `Midjourney`, or image-generation metadata was found in the HTML source during audit. Therefore, this deck is tracked as a visual-design reference, not as a reusable prompt source.

Do not copy the reference deck's images, content, or exact slide diagrams. Use the patterns below to build original visuals for this course.

## Patterns To Reuse

### 1. Visual Hook First

Start important lessons with a concrete visual, not a definition. For this course, use:

- a research workflow map;
- a tiny dataset preview;
- a paper-output mockup;
- a before/after contrast;
- a track chooser or mini decision tree.

### 2. One Slide, One Job

Each slide should do one of these jobs:

- introduce the research question;
- show the data unit;
- explain one Python concept;
- demonstrate one output;
- interpret one result;
- warn about one common mistake.

Avoid combining new code, new dataset structure, and new research method on the same slide in beginner weeks.

### 3. Diagram Instead Of Paragraph

Replace long text with original HTML/CSS/SVG diagrams:

- workflow: `question -> data -> code -> output -> interpretation -> paper`;
- table anatomy: rows, columns, unit of observation;
- notebook anatomy: Markdown cell vs code cell vs output;
- caption anatomy: source, N, variables, method, main reading, limitation.

### 4. Color Has Meaning

Use colors consistently:

- blue: Python/action;
- green: research evidence/output;
- amber: caution or limitation;
- red: common mistake;
- neutral gray: metadata/source.

Do not let the deck become a single-color theme.

### 5. Repeated Visual Grammar

Reuse a small set of components:

- `visual-grid`: two or three explanatory panels;
- `story-card`: compact concept card;
- `question-box`: key research question;
- `mini-table`: simplified dataset preview;
- `paper-card`: Methods/Results/caption mockup;
- `bridge-strip`: "we just learned / next problem / next step";
- `caption-card`: paper-ready caption example.

### 6. Track Prompt And Sources

Every visual artifact must be traceable:

- external reference URL;
- generated-image prompt, if any;
- AI-assisted diagram prompt, if any;
- human-authored note for original CSS/SVG;
- license/reuse note;
- access date.

Use `resources/templates/slide_prompt_sources_template.md` for each week and save the filled file as `slide_prompt_sources.md`.

## Beginner-Safe Rule

In Weeks 1-4, the learner should only read and interpret rich slides. They should not be asked to author HTML, CSS, JavaScript, SVG, Reveal.js, or Quarto internals.
