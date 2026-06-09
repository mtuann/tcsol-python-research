# Week 12 Readings

## Required Technical Reading

- Title: RapidFuzz Levenshtein distance
- Link: https://rapidfuzz.github.io/RapidFuzz/Usage/distance/Levenshtein.html
- Why it matters this week: the notebook uses `rapidfuzz.distance.Levenshtein.distance` to count visible edits between `vi_mt_output` and `vi_postedit`.
- Sections to read: function name, what `distance(s1, s2)` returns, and one short example.

## Required Research/Method Reading

- Citation: Sun, Y., Wang, M., & Jia, Y. (2025). Direction matters: Comparing post-editing and human translation effort and quality. PLOS ONE. DOI: `10.1371/journal.pone.0328511`.
- Link: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328511
- Research question: how post-editing and human translation differ in effort and quality.
- Method: empirical comparison of translation/post-editing workflows with effort and quality evidence.
- Dataset: article data and supporting files from the PLOS ONE publication.
- What we borrow this week: the habit of treating MTPE effort as measurable evidence, while keeping classroom data synthetic and limited.

## Required Concept Reference

- Title: ISO 18587:2017, Translation services, post-editing of machine translation output
- Link: https://www.iso.org/standard/62970.html
- Why it matters this week: it gives a professional reference point for full human post-editing requirements and post-editor competences.
- Beginner use: read only the scope/title. This course does not claim that the classroom workflow implements ISO 18587.
- Update note: the ISO page marks ISO 18587:2017 as “to be revised” and lists ISO/CD 18587.2 as replacement-in-progress.

## Optional / Instructor Source Menu

- Scarton et al. (2019), Estimating post-editing effort.
  https://arxiv.org/abs/1910.06204
- TAUS MT post-editing guidelines, practitioner context.
  https://www.taus.net/resources/reports/mt-post-editing-guidelines
- ViBidirectionMT-Eval (2025), Vietnamese bidirectional MT evaluation context.
  https://arxiv.org/abs/2501.08621

## Source Update Log

- Search date: 2026-06-04
- Search terms: `machine translation post-editing effort 2025`; `RapidFuzz Levenshtein distance documentation`; `ISO 18587 2017 post-editing machine translation`; `Vietnamese Chinese machine translation evaluation 2025`
- Sources checked: RapidFuzz docs, ISO 18587:2017, Sun/Wang/Jia 2025 PLOS ONE, Scarton et al. 2019, TAUS MTPE guidelines, ViBidirectionMT-Eval 2025.
- Source selected: RapidFuzz as technical source; Sun/Wang/Jia 2025 as method source; ISO 18587:2017 as concept reference.
- Why selected: official documentation for computation, open-access empirical MTPE source for method framing, and recognized MTPE standard for professional context.

| Source | Status | Last checked | Beginner use |
|---|---|---:|---|
| RapidFuzz Levenshtein docs | required technical | 2026-06-04 | read one function example |
| Sun, Wang, Jia 2025 PLOS ONE | required method | 2026-06-04 | read abstract and method idea |
| ISO 18587:2017 | required concept | 2026-06-04 | read scope/title only |
| Scarton et al. 2019 | optional | 2026-06-04 | instructor background |
| TAUS guidelines | optional practitioner source | 2026-06-04 | workflow vocabulary only |
| ViBidirectionMT-Eval 2025 | optional preprint | 2026-06-04 | language-pair context only |
