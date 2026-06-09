# Week 12 Submission Text Model

## Caption

Figure 1 compares mean post-editing time across three synthetic MT profiles for 10 Chinese-Vietnamese education-policy source segments (30 system-segment rows). Lower time indicates less observed post-editing time in this classroom dataset.

## Source Note

Source note: the synthetic dataset is data/raw/week12_mtpe_segments.csv, SHA-256 f4a22aed428056220b9617dd4259dbe7efa27a6f9308b525a4bd0032b19e3363, with raw GitHub download from the course repository. Edit distance was computed with RapidFuzz 3.13.0 Levenshtein distance. ISO 18587:2017 is used only as conceptual background for full human post-editing requirements, not as a claim that this classroom workflow implements the standard. For empirical MTPE context, see Sun, Wang, and Jia (2025), PLOS ONE, DOI 10.1371/journal.pone.0328511. Access date: 2026-06-04.

## Results Paragraph

In the synthetic Week 12 MTPE dataset, MT_B had the lowest observed mean post-editing time (36.4 seconds across 10 segments) and the lowest mean normalized edit distance (0.11). In contrast, MT_C had the highest mean time (111.4 seconds); its edit distance was higher than MT_B's but slightly lower than MT_A's. The revision-type table explains the pattern: lower-time rows often required no edit or only style repair, whereas higher-time rows often involved omission, terminology, or word-order repair. This is useful for a paper draft because it links a number to a visible revision reason and keeps the unit of analysis transparent. A cautious report should still avoid ranking real systems from this toy sample. However, the dataset is synthetic, the time values are classroom practice logs, and edit distance captures visible text change rather than all cognitive decisions made by a post-editor.
