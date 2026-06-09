# V2 Site Metadata

This folder stores lightweight metadata used to render the V2 website.

## Files

- `modules.json`: canonical list of the 16 planned modules, learning stages, gallery categories, and data categories.

## Design Rule

The homepage and future module index pages should read from metadata instead of duplicating module descriptions by hand.

Every module entry should answer:

- What research problem does this module solve?
- What dataset does the learner touch?
- What figure or visual decision does the learner practice?
- What paper-facing output does the learner produce?

## Public Deployment

The GitHub Pages workflow copies this folder into the static site. Keep metadata small and readable.
