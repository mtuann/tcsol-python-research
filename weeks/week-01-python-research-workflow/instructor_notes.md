# Week 01 Instructor Notes

## Teaching Goal

The learner has no programming background. Week 01 should reduce fear, not maximize technical coverage.

The main message:

```text
Python helps you make a paper workflow reproducible.
You do not need to become a software engineer.
```

## Keep Core Very Light

Required learner-facing concepts:

- notebook cells;
- Markdown vs code;
- variables;
- strings;
- CSV as a table;
- one row = one observation.

Avoid:

- pandas;
- statistics;
- installation troubleshooting during the main lesson;
- COMET, BLEU, regression, APIs, scraping;
- asking the learner to write HTML, CSS, or JavaScript.

## Suggested Teaching Script

1. Start with a familiar academic task: "I need to write a Methods section."
2. Show that Methods needs data source, rows, columns, and procedure.
3. Open `slides.html`.
4. Open `interactive_demo.html` and show that a dataset can become a table or figure.
5. Open `live_coding.ipynb`.
6. Let the learner edit variables only.
7. Run the CSV cells together.
8. Ask the learner to choose one future track.

## Common Learner Reactions

| Reaction | Instructor response |
|---|---|
| "I don't understand all the code." | "You do not need to yet. Today you only need to run it and identify what changed." |
| "Can Python write my paper?" | "Python can produce evidence and transparent methods; you still interpret the result." |
| "Why not use Excel?" | "Excel is useful. Python helps when the workflow must be repeated, checked, and documented." |
| "Do I need machine learning?" | "No. Most useful research starts with clean data, tables, figures, and careful interpretation." |

## Optional Demonstration

If the learner is curious, show the HTML interactive demo. Do not explain JavaScript. Say:

```text
Later, Python can export interactive figures like this. For now, your job is to read and interpret them.
```

## Success Criteria

The week is successful if the learner says:

- "I can run a notebook."
- "I know what kind of data my question needs."
- "I can write a short interpretation of a simple output."

