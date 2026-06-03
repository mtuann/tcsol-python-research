# Python for TCSOL, Chinese-Vietnamese Contrastive Research, MTPE, and Education Policy

> Working syllabus and project hub for teaching Python to a beginner graduate student in Applied Linguistics, TCSOL, Contrastive Linguistics, Translation Studies, and Education Policy.

Last source check: 2026-06-03

## Project Purpose

This project designs a Python learning path for a student who is preparing for graduate study in education policy and whose research interests include:

- **Applied Linguistics and TCSOL**: short-term Chinese language teaching, learner progress, classroom intervention, second language acquisition, and pedagogical design.
- **Chinese-Vietnamese Contrastive Linguistics**: contrastive analysis for teaching, translation, and cross-cultural communication.
- **Translation Studies**: machine translation evaluation, machine translation post-editing (MTPE), translation quality annotation, and modern translation workflows.
- **Education Policy**: policy document analysis, education statistics, institutional comparison, and evidence-based policy discussion.

The course does **not** treat Python as a general programming course or an NLP engineering course. Python is taught as a research instrument:

```text
research question -> data design -> cleaning -> analysis -> visualization -> interpretation -> paper
```

## Target Learner

This syllabus assumes the learner:

- has no previous programming background;
- can read academic Chinese and Vietnamese;
- needs Python mainly for paper writing and research evidence;
- may work in China, so local/offline tools should be preferred over tools that rely heavily on blocked or unstable cloud access;
- is more likely to use Word/Zotero at first than a full LaTeX workflow;
- should meet Overleaf only after she has real tables, figures, captions, and draft sections to package.

## Learning Outcomes

By the end of the course, the learner should be able to:

- build clean research datasets in CSV/Excel format;
- analyze pre-test/post-test, survey, classroom observation, and learner-error data;
- create Chinese-Vietnamese contrastive datasets with explicit coding categories;
- evaluate MT/MTPE outputs with both human annotation and light automatic metrics;
- produce publication-ready tables and figures;
- write clear Methods and Results sections;
- build a paper-facing writing habit through weekly captions, paragraphs, limitations, and source notes;
- choose an appropriate writing workflow: Word + Zotero by default, Quarto or Overleaf when the project needs reproducible publishing or LaTeX formatting;
- keep a reproducible research folder with data, notebooks, outputs, and references.

## Recommended Tool Stack

### Core Environment

- **Miniconda or Anaconda** for Python environment management.
- **JupyterLab** for lessons, exploratory analysis, and combining code with explanation.
- **VS Code** for project organization, notebooks, Markdown, and later Git work.
- **Git + GitHub** for version control and publishing.
- **Gitee** as a practical mirror/backup option in China if GitHub access is unstable.

### Python Libraries

| Area | Libraries | Use |
|---|---|---|
| Data tables | `pandas`, `numpy`, `openpyxl` | CSV/Excel, cleaning, grouping, summary tables |
| Visualization | `matplotlib`, `seaborn` | bar charts, line charts, boxplots, heatmaps |
| Statistics | `scipy`, `pingouin`, `statsmodels` | t-test, correlation, regression, ANOVA, effect size |
| Text patterns | `re`, `regex` | search linguistic patterns, annotate examples |
| Similarity/editing | `rapidfuzz` | fuzzy matching, edit distance, MTPE effort proxies |
| MT metrics | `sacreBLEU` | BLEU, chrF, TER for MT evaluation |
| Advanced MT metric | `unbabel-comet` | optional only; stronger but heavier and harder to explain |

### Writing and Citation

- **Zotero + Word** for the first writing workflow.
- **Quarto** for a later reproducible report workflow that combines text, code, figures, and citations.
- **Overleaf** as a Week 14 optional paper-packaging workflow when the learner needs LaTeX, a journal/university template, or collaborative LaTeX editing.
- **Markdown** for README, notes, and simple GitHub Pages content.

Writing is not saved for the end of the course. Every week must include a small paper-facing writing task. Overleaf should not be introduced as a separate early burden; it is a final packaging option after the learner has enough paper material.

Detailed policy: [`resources/WRITING_AND_PAPER_TOOLING_ROADMAP.md`](resources/WRITING_AND_PAPER_TOOLING_ROADMAP.md).

## Course Design Standard

All weekly lessons must follow the contract in [`resources/WEEKLY_LESSON_DESIGN_STANDARD.md`](resources/WEEKLY_LESSON_DESIGN_STANDARD.md). That file defines the required weekly artifacts: slides, lecture notes, live-coding notebook, dataset/data dictionary, exercises, assignment, readings, figure/table output, caption, interpretation paragraph, rubric, and reproducibility checklist.

Each week must also follow the writing-support policy in [`resources/WRITING_AND_PAPER_TOOLING_ROADMAP.md`](resources/WRITING_AND_PAPER_TOOLING_ROADMAP.md): paper connection, writing output, tool support, sentence frame, and common writing risk.

The current design supports both Markdown/Quarto sources and deployable HTML:

- `slides.qmd` and `slides.html` for each week;
- `interactive_demo.qmd` and `interactive_demo.html` when interaction improves learning;
- static HTML files that can be served by GitHub Pages.

Public learner-facing navigation should target HTML pages or folder `index.html` pages. Markdown files remain authoring sources; direct `.md` links on GitHub Pages render as raw text in this static deployment and should not be the main learner experience.

Notebook files follow the same rule. Direct `.ipynb` links on GitHub Pages may render as raw notebook JSON, so public navigation should point to a rendered notebook HTML page such as `live_coding.html`. Keep the `.ipynb` as downloadable/runnable source, and add a Colab link when the notebook should be executed without local setup.

## Bilingual Website Policy

Public learner-facing HTML defaults to Vietnamese and provides an English option through a language switcher. The course uses Vietnamese-first explanations with English anchor terms, rather than long side-by-side duplicate paragraphs, so a beginner can focus on the concept without extra reading load.

For future weeks, start from:

- [`resources/style_guides/bilingual_style_guide.md`](resources/style_guides/bilingual_style_guide.md)
- [`resources/templates/bilingual_content_blocks_template.md`](resources/templates/bilingual_content_blocks_template.md)
- [`resources/templates/translation_qa_checklist.md`](resources/templates/translation_qa_checklist.md)
- [`resources/glossary/core_glossary.csv`](resources/glossary/core_glossary.csv)

## Visual Slide And Source Tracking Policy

Slides should use original visual explanations: workflow maps, dataset previews, paper-output mockups, caption anatomy cards, and research-track comparison panels. External decks may be used as design references, but their images, diagrams, and exact CSS should not be copied unless the license explicitly allows reuse.

For future slide work, use:

- [`resources/slide_design/visual_slide_playbook.md`](resources/slide_design/visual_slide_playbook.md)
- [`resources/templates/slide_prompt_sources_template.md`](resources/templates/slide_prompt_sources_template.md)

## Current Lesson Packages

- [`Tuần 01: Python như một quy trình nghiên cứu`](weeks/week-01-python-research-workflow/)

## Suggested Repository Structure

```text
tcsol-python-research-syllabus/
├── README.md
├── docs/                  # future GitHub Pages site
├── weeks/                 # week-by-week lesson packages
├── notebooks/             # lesson notebooks and student exercises
├── data/
│   ├── raw/               # original data, usually not public
│   └── processed/         # cleaned/anonymized data
├── outputs/
│   └── figures/           # charts exported from notebooks
├── paper/                 # drafts, outline, tables, citation files
├── resources/             # rubrics, coding schemes, reading notes
└── assets/                # images for GitHub Pages or README
```

Important: do not publish identifiable student data. If this repository becomes public, keep raw classroom data outside the repo or anonymize it thoroughly.

## Course Design Principles

- Teach one or two new technical concepts per week.
- Every coding task must serve a real research task.
- Prefer small datasets first: 20 sentences, 30 survey rows, 50 translations, then scale up.
- Use Excel/CSV as the bridge from familiar research habits to Python.
- Treat visualization as argument-building, not decoration.
- Treat automatic MT metrics as supporting evidence, not final judgment.
- Treat writing as a weekly output, not a final-week clean-up task.
- Keep Overleaf optional and late: Week 14 paper packaging, not Week 1-6 concept load.
- Make the final notebook runnable from top to bottom.
- Publish a rendered notebook HTML page for the website; use Colab as the default browser-based run option.

## 14-Week Syllabus

| Week | Theme | Python Skills | Research Practice | Deliverable |
|---|---|---|---|---|
| 1 | Python as a research tool | Jupyter, cells, variables, strings, Markdown | Turn a broad interest into a researchable question | research question + 100-150 word memo |
| 2 | Research data as tables | lists, dictionaries, CSV/Excel structure | Design columns for learners, tests, errors, translations, or policies | dataset template + data description |
| 3 | pandas basics | `DataFrame`, select columns, filter rows, `groupby` | Summarize class or survey data | descriptive table + caption |
| 4 | Cleaning data | missing values, type conversion, label normalization | Clean survey/pre-test/post-test data | cleaned dataset + cleaning note |
| 5 | Visualization for papers | `matplotlib`, `seaborn` | Choose chart types that match research claims | 2 draft figures + captions |
| 6 | Intro statistics | mean, SD, confidence interval, t-test, correlation | Compare pre-test vs post-test or two teaching groups | Results paragraph with limitation |
| 7 | TCSOL short-course research | rubric design, classroom variables | Analyze learner gains and learning difficulties | mini teaching-study design |
| 8 | Learner error analysis | frequency tables, cross-tabulation | Code errors: tones, measure words, aspect, word order, complements | learner error report |
| 9 | Chinese-Vietnamese contrastive data | string matching, regex, coding categories | Build bilingual examples and classify phenomena | contrastive analysis table |
| 10 | Pedagogical adaptation | grouping, ranking, visualization | Convert contrastive findings into teaching priorities | short lesson adaptation |
| 11 | MT evaluation | source/MT/reference tables, BLEU/chrF/TER | Compare MT systems on Chinese-Vietnamese examples | MT evaluation table |
| 12 | MTPE workflow | edit distance, time logs, error annotation | Measure post-editing effort and classify errors | MTPE analysis memo |
| 13 | Education policy data | policy metadata, timeline, coding scheme | Analyze policy documents and education statistics | policy coding table |
| 14 | Paper package and Overleaf option | clean notebook, README, Zotero, Word, optional Quarto/Overleaf | Combine question, data, method, results, limitations | mini paper + notebook + optional Overleaf project |

## Writing and Paper Tooling Progression

| Stage | Weeks | Writing focus | Tool support |
|---|---:|---|---|
| Foundation | 1-2 | research question, data unit, source note | notebook Markdown; Word optional |
| Evidence | 3-5 | descriptive table, figure caption, figure note | Word + Zotero setup begins |
| Results | 6-8 | Results paragraph, limitation, teaching implication | Word + Zotero |
| Track writing | 9-13 | track-specific analysis paragraph | Word + Zotero; Quarto optional |
| Paper package | 14 | mini paper, appendix, references, reproducibility note | Word + Zotero by default; Overleaf/Quarto optional |

## Project Tracks

The learner should choose one main track by Week 4.

### Track A: Short-Term Chinese Teaching / TCSOL

Possible research question:

> Does a short focused intervention on Chinese result complements improve Vietnamese learners' accuracy in sentence production?

Data:

- learner ID, anonymized;
- class group;
- pre-test and post-test scores;
- item-level responses;
- error category;
- brief classroom observation notes.

Python analysis:

- score gain by learner and by item;
- most frequent error categories;
- paired t-test or Wilcoxon test;
- effect size;
- boxplot or line chart of learner progress.

Paper contribution:

- evidence-based teaching recommendation for a short course;
- clear connection between linguistic difficulty and classroom intervention.

### Track B: Chinese-Vietnamese Contrastive Linguistics

Possible research question:

> How do Vietnamese learners transfer Vietnamese word order patterns when using Chinese complements or disposal constructions?

Data:

- Chinese example;
- Vietnamese equivalent;
- grammatical feature;
- learner translation or learner production;
- error type;
- pedagogical note.

Python analysis:

- frequency of contrastive phenomena;
- error distribution by structure;
- examples selected for qualitative interpretation;
- charts showing high-priority teaching points.

Paper contribution:

- a contrastive analysis that directly supports teaching material design.

### Track C: MT Evaluation and MTPE

Possible research question:

> How reliable is machine translation for Chinese-Vietnamese education-policy texts, and what types of errors require human post-editing?

Data:

- source sentence;
- MT system name;
- MT output;
- human reference or post-edited version;
- post-editing time;
- error category;
- severity.

Python analysis:

- BLEU, chrF, TER with `sacreBLEU`;
- edit distance or similarity with `rapidfuzz`;
- error frequency by MT system;
- post-editing time by text type;
- qualitative examples of major errors.

Human evaluation categories can start simple:

- accuracy;
- fluency;
- terminology;
- style/register;
- omission/addition;
- mistranslation;
- punctuation/formatting.

Paper contribution:

- balanced evaluation of MT usefulness and limits;
- MTPE workflow recommendations for Chinese-Vietnamese translation contexts.

### Track D: Education Policy

Possible research question:

> How do recent Chinese education policy documents frame digitalization, internationalization, and teacher development?

Data:

- policy title;
- issuing body;
- date;
- policy level;
- target population;
- keywords;
- coded theme;
- short excerpt;
- analytic memo.

Python analysis:

- policy timeline;
- frequency of themes;
- comparison across policy areas;
- tables of policy targets and implementation measures.

Paper contribution:

- systematic mapping of policy discourse;
- evidence for a literature review or policy analysis paper.

## Data Templates

### `students_scores.csv`

```csv
student_id,group,level,pre_score,post_score,attendance_hours,notes
S001,A,beginner,62,78,18,"anonymized"
```

### `learner_errors.csv`

```csv
student_id,item_id,target_structure,learner_answer,error_category,severity,comment
S001,Q03,result_complement,他写错了字,complement_order,minor,"needs more input examples"
```

### `contrastive_examples.csv`

```csv
example_id,zh_sentence,vi_equivalent,feature,contrast_type,pedagogical_note
C001,我把书放在桌子上,Tôi đặt sách lên bàn,把-construction,word_order,"Vietnamese learners may omit 把"
```

### `mt_eval.csv`

```csv
segment_id,source_text,system,mt_output,reference,post_edited,pe_time_seconds,error_type,severity
M001,教育数字化推动资源共享,system_a,...,...,...,42,terminology,major
```

### `policy_docs.csv`

```csv
doc_id,title,issuing_body,date,policy_area,target_group,theme,excerpt,url
P001,教育强国建设规划纲要（2024—2035年）,中共中央 国务院,2025-01-19,education reform,national,digitalization,...,https://...
```

## Installation Draft

Recommended local setup:

```bash
conda create -n tcsol-python python=3.12
conda activate tcsol-python

pip install jupyterlab pandas numpy openpyxl matplotlib seaborn scipy statsmodels pingouin rapidfuzz sacrebleu
```

For students in China, a temporary PyPI mirror can help:

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

Optional advanced MT evaluation:

```bash
pip install unbabel-comet
```

Only add COMET after the learner understands reference-based metrics and human error annotation. COMET is useful, but it can shift the course too far toward NLP if introduced too early.

## GitHub Pages Plan

This repository can later become a GitHub Pages site.

Recommended path:

1. Keep `README.md` as the main repository overview.
2. Put public-facing website pages in `docs/`.
3. Configure GitHub Pages to publish from the `main` branch and `/docs` folder.
4. Keep raw or private research data out of `docs/`.
5. Add an `index.md` in `docs/` when the syllabus is ready to publish.

## Assessment Plan

| Component | Weight | Evidence |
|---|---:|---|
| Weekly exercises | 25% | short notebooks, cleaned datasets |
| Research data design | 15% | data dictionary, coding scheme |
| Visualization and statistics | 20% | figures, tables, interpretation |
| Final notebook | 20% | reproducible notebook, clean outputs |
| Mini paper | 20% | Introduction, Data, Methods, Results, Limitations |

## Reproducibility Checklist

Before submitting a project, check:

- The dataset has a data dictionary.
- Student or participant data is anonymized.
- Raw data is preserved separately and not edited by hand.
- Cleaned data is generated from documented steps.
- The notebook runs from top to bottom.
- Figures and tables are generated by code.
- Package versions are recorded.
- MT systems and access dates are recorded.
- Zotero bibliography is complete.
- Methods section explains data, coding, tools, and limitations.

## What Not to Teach First

Avoid these in the first version of the course:

- object-oriented programming;
- web scraping at scale;
- deep learning;
- training NLP models;
- Docker;
- Git branching and merge conflict workflows;
- advanced LaTeX;
- topic modeling and sentiment analysis unless the learner's actual paper requires them.

These topics are useful later, but they are not the shortest path to a good Applied Linguistics or Education Policy paper.

## Source Map and Current Documentation

### Python and Research Computing

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [JupyterLab User Guide](https://jupyterlab.readthedocs.io/en/stable/user/)
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [Miniconda documentation](https://www.anaconda.com/docs/getting-started/miniconda/main)
- [Conda: managing environments](https://docs.conda.io/en/latest/user-guide/tasks/manage-environments.html)
- [Tsinghua PyPI mirror help](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

### Data, Visualization, and Statistics

- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [NumPy documentation](https://numpy.org/doc/)
- [openpyxl documentation](https://openpyxl.readthedocs.io/en/stable/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [seaborn documentation](https://seaborn.pydata.org/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)
- [statsmodels User Guide](https://www.statsmodels.org/stable/user-guide.html)
- [Pingouin documentation](https://pingouin-stats.org/)

### Translation, MT, and MTPE

- [sacreBLEU on PyPI](https://pypi.org/pypi/sacrebleu)
- [sacreBLEU GitHub repository](https://github.com/mjpost/sacrebleu)
- [COMET documentation](https://unbabel.github.io/COMET/html/index.html)
- [COMET GitHub repository](https://github.com/Unbabel/COMET)
- [RapidFuzz documentation](https://rapidfuzz.github.io/RapidFuzz/)
- [MQM error typology](https://themqm.org/error-types-2/typology/)
- [ISO 18587:2017 MTPE standard](https://www.iso.org/standard/62970.html)

### Writing, Citation, and Publishing

- [Zotero Word plugin documentation](https://www.zotero.org/support/word_processor_plugin_usage/)
- [Zotero word processor integration](https://www.zotero.org/support/word_processor_integration)
- [Quarto authoring in VS Code](https://quarto.org/docs/get-started/authoring/vscode.html)
- [Quarto citations](https://quarto.org/docs/authoring/citations.html)
- [Overleaf Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- [Overleaf bibliography management in LaTeX](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)
- [Overleaf: working with `.bib` files](https://docs.overleaf.com/citing-and-references/working-with-.bib-files)
- [Overleaf and Zotero](https://www.overleaf.com/learn/how-to/How_to_link_your_Overleaf_account_to_Mendeley_and_Zotero)
- [GitHub Pages quickstart](https://docs.github.com/pages/quickstart)
- [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Git documentation](https://git.github.io/htmldocs/git.html)
- [Gitee Help Center](https://gitee.com/help)

### TCSOL and Chinese Education Policy

- [MOE: Chinese Proficiency Grading Standards launch](https://en.moe.gov.cn/news/press_releases/202104/t20210428_528917.html)
- [Chinese Proficiency Grading Standards overview](https://www.chinese.cn/zhuanti/202207/en/)
- [2024 National Education Development Statistical Bulletin, PRC MOE](https://www.moe.gov.cn/jyb_sjzl/sjzl_fztjgb/202506/t20250611_1193760.html)
- [Education Powerhouse Plan 2024-2035, PRC MOE](https://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/202501/t20250119_1176193.html)
- [Education Powerhouse Plan topic page, PRC MOE](https://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2025/2025_zt02/)
- [UNESCO education policies and strategies](https://www.unesco.org/en/education-policies)
- [OECD Education Policy Outlook 2025](https://www.oecd.org/en/publications/education-policy-outlook-2025_c3f402ba-en.html)

## Next Content Tasks

- Create `docs/index.md` as a public landing page.
- Review and refine `weeks/week-01-python-research-workflow/`.
- Create `weeks/week-02-data-tables-and-codebooks/`.
- Create blank CSV templates in `resources/templates/`.
- Add a one-page learner setup guide in Vietnamese.
- Add a Zotero + Word workflow guide.
- Add a Week 14 Word/Zotero/Overleaf paper package template.
- Add a simple MTPE annotation rubric.
- Add a short policy document coding rubric.
