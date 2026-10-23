# Reconstruction validator

Tests whether new writing applies the author's methods, works as writing in its own right, and stays original.

## Purpose

Two failures look like success. A passage can resemble the author and still fail as a scene. A passage can work as a scene and ignore the requested style. The validator checks both, and checks for copying, before a profile is trusted or a chapter is accepted.

## Activation

- After a new or changed profile, before a manuscript starts: situation tests.
- After each chapter in Plan or Write mode on a reconstructed voice.
- Whenever the author reports that the voice is wrong.

## Procedure

1. **Situation tests.** Write five short original passages from the profile, one each: description, dialogue, reflection, action or escalation, irony or reversal. Use a fresh scene plan, never the source's plot. These are clone tests for the calibration protocol. They are working material and are not delivered unless the user asks for them.
2. **Score five fidelity dimensions** by close reading, each with located notes:

   | Dimension | Question | Overlaps auditor category |
   |---|---|---|
   | Linguistic | Do vocabulary, syntax, rhythm and rhetoric match the profile? | 1, 8 |
   | Narrative | Do scene development, information control, viewpoint and movement match? | 2, 9, 10 |
   | Character | Are characters built and differentiated by the author's principles? | 3, 5, 7 |
   | Tonal | Is the register held without caricature? | 1, 9 |
   | Literary | Does the passage succeed on its own as writing? | 4, 6, 10 |

   The auditor's ten scores and these five are read together. A passage that passes the auditor but fails linguistic fidelity has the right engine and the wrong voice. One that passes fidelity but fails the auditor has the voice and broken craft.
3. **Measure.** Run `scripts/stylometrics.py compare` on the source section and the draft. Report differences. Never convert them into a percentage likeness.
4. **Check originality.** No sentence, image sequence, character or plot taken from the source. Any phrase of four or more distinctive words matching the source is rewritten. Recognisable vocabulary is not a pass. Weak syntax with the right words is caricature.
5. **Revise in order:** narrative function, continuity and character, sentence and rhythm, vocabulary and description, dialogue and tone, then exaggerated imitation, then originality, then a final read for natural movement. Never add spelling errors, odd punctuation or clumsy grammar to look human. Individual style comes from consistent decisions, not manufactured mistakes.

## Outputs

Pass or revise for each test, located notes per dimension, measured differences, and the profile entries behind each failure.

## Quality test

Could the author read the notes and agree on where each failure is, without the scores?

## Failure modes

- **Invented precision.** "92 per cent faithful." Repair: name the dimensions and the evidence instead.
- **Self-approval.** The validator passes its own drafts. Repair: the author's verdict outranks it, and every disagreement is logged.
- **Caricature passing.** Signature devices on every page. Repair: check device frequency against the source with stylometrics.

## Signals

- (+) The author approves a chapter the validator passed.
- (-) The author rejects a chapter the validator passed. Log it, and recalibrate the validator the same way the auditor is recalibrated (`references/04-style-consistency-auditor.md`, B7).

## Contract

```contract
node: reconstruction-validator
sends: author-dossier | strong | failed tests that point to profile entries
sends: engine-auditor | strong | fidelity findings on five dimensions, mapped to auditor categories
sends: engine-calibration | strong | situation test passages, used as clone tests
sends: engine-feedback | moderate | passages the validator passed but the author rejected
sends: manuscript-architect | strong | drift reports that need a blueprint or continuity change
sends: stylometrics | strong | draft passages and the matching source sections to measure
receives: author-dossier | strong | signatures and constraints to test
receives: engine-auditor | strong | the ten category scores for the same passage
receives: engine-calibration | strong | profile status after each test
receives: engine-feedback | critical | the author's verdict, which outranks the validator
receives: manuscript-architect | strong | finished chapters and, when available, the whole manuscript
receives: stylometrics | strong | side-by-side measurements of source and draft, never a similarity percentage
```
