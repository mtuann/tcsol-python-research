# Week 13 Submission Text Model

## Timeline Caption

Figure 1 shows the timeline of 12 coded policy-source rows in the Week 13 classroom dataset. Color/labels distinguish publication dates from access-date placeholders; the figure describes source coverage rather than policy impact.

## Bar-Figure Caption

Figure 2 shows policy-area counts in the Week 13 classroom dataset. Counts describe the small synthetic coding sample and should not be interpreted as policy importance or implementation quality.

## Source Note

Source note: policy/source metadata were checked on 2026-06-04. Core sources include the PRC State Council education blueprint page, the PRC MOE 2024 statistical bulletin, UNESCO UIS SDG 4 indicators, and UNESCO GEM PEER. The classroom CSV is synthetic/paraphrased, SHA-256 cedbc768526aadf2ebfe41fdf08585ebe10963e5ba17adb1a78f93ca14d8aaa5, and should not be treated as a full policy corpus.

## Data/Methods Paragraph

The Week 13 classroom dataset contains 12 synthetic, paraphrased coded rows drawn from 6 policy or source documents. The unit of analysis is one coded source entry, not one learner, school, or full policy corpus. Each row records source metadata, including title, issuing body, source type, URL, access date, and a coder note, plus analytic fields such as policy_area, theme_code, and evidence_type. The source types include policy_plan, statistical_bulletin, metadata_standard, data_portal, coding_model, policy_dashboard, comparative_report, while the main coded policy areas include teacher_development, indicator_metadata, policy_coding_method, system_governance, digitalization. Dates are parsed with pd.to_datetime; 4 rows use access-date placeholders because the source pages are dynamic metadata, dashboard, or profile pages. Therefore, the timeline should be read as a source map for transparent paper writing, not as evidence of implementation sequence, learner outcomes, or causal policy effects.
