# Fiction Consciousness Engine

A Claude skill for writing fiction from inside a character's head. It can also learn how a particular author writes, so that a draft is built on a profile somebody has tested rather than on a vague impression of "the style".

Version 3.0.2. The skill itself lives in `fiction-consciousness-engine/`. Everything at the top level of this repository is about getting it into the right place.

## What it does

There are seven modes.

Write drafts scenes and chapters in close character consciousness, using the Master Fiction Writing System and twenty craft subskills. Every substantial passage goes past a Style Consistency Auditor before it is delivered.

Absorb learns your voice from passages you have approved. Reconstruct reads an author's books, separates their words from the editor's and translator's, and builds a research dossier and a style profile. Plan produces a writing specification, a book blueprint and a continuity ledger.

Compare sets two or more profiles side by side, and does not average them. Analyse writes a plain report on a book: the claim, the evidence, the gaps. Audit gives scores and located notes, if you ask for them.

## Status

- Working and tested: the two scripts, the validator, and the two-way contract wiring between the subskills.
- Not yet tested: the method end to end on a full manuscript, or on a real author's corpus. Expect rough edges.
- Self-assessed: the auditor's scores. It is checked against passages you have judged. Until a project has those, it runs on default anchors and the project is marked "judge uncalibrated".

## Installing

Copy the `fiction-consciousness-engine` folder into wherever your Claude setup loads skills from. Keep the folder name as it is. The validator checks that the `name` in `SKILL.md` matches the folder, so a renamed folder will fail on purpose.

Run the validator from inside the folder:

    python3 -I scripts/validate.py

It checks the verbatim specification files against stored hashes, the file references in the router, and the contract graph. It uses only the standard library. Run it after any change.

## Measuring text

    python3 scripts/stylometrics.py profile SOURCE.txt
    python3 scripts/stylometrics.py compare SOURCE.txt DRAFT.txt

Run these from inside `fiction-consciousness-engine/`, because the script paths are relative to it. Add `--single-quotes` for dialogue in single quotation marks, and `--json` for machine-readable output.

The script reports differences. It does not give a similarity score, and I don't plan to add one. Nothing it measures supports a figure like "94 per cent like the author", so I didn't write one. Under about 2,000 words the figures are indicative, and the output says so every time.

## Repository layout

    LICENSE                          MIT
    README.md                        this file
    description.md                   the reasoning behind the build
    fiction-consciousness-engine/    the skill

## Licence and credits

The engine is MIT licensed, see `LICENSE`. Several of the sources it draws on have their own status, some unclear. `fiction-consciousness-engine/LICENCE-NOTICE.md` sets out each one. One of them states MIT in its README but had no licence file in the copy I used, so check upstream before you redistribute anything taken from it.

Author: TABARC-Code.
