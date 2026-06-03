# Week 04 Instructor Notes

Week 04 is the first messy-data week. Keep it calm and procedural:

- "We are not fixing everything."
- "We are making a documented cleaned copy."
- "Every cleaning decision needs a reason."

## Teaching Sequence

1. Show the raw CSV.
2. Ask learners to point out suspicious cells before code.
3. Run the inspection cells.
4. Normalize one label column slowly.
5. Convert score columns.
6. Export cleaned data and cleaning log.
7. Write a cleaning note.

## Avoid

- Do not introduce imputation methods.
- Do not teach regex beyond literal replacement.
- Do not debate advanced missing-data mechanisms.
- Do not overwrite the raw CSV.
- Do not use real identifiable classroom data.

## Recommended Live Questions

- What would happen if `Measure Words` and `measure_words` were counted separately?
- Why is `eighty` safer as missing than as a guessed value?
- Why should the paper say how many rows had complete pre/post scores?
- What is the difference between correcting a label and changing a measurement?

## Pacing

If time is short, skip the stretch comparison and keep:

1. missing value count;
2. label normalization;
3. numeric conversion;
4. cleaning log;
5. cleaning note.

## Week 05 Bridge

Week 05 visualization should use the cleaned labels from Week 04. Preview this with one sentence only:

> A figure inherits the quality of its data labels.
