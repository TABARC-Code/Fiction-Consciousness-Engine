# Form specialist

Handles poetry, drama and non-fiction, where the prose-fiction rules do not fit as written.

## Purpose

A playwright's power lives in speech, entrances and asides. A poet's lives in the line. An essayist's lives in the argument. This subskill analyses those forms on their own terms, and says how their methods translate when the target is prose, or the other way round.

## Activation

Conditional: only when the corpus or the project includes verse, drama or non-fiction. Otherwise it stays idle.

## Procedure

**Poetry.** Metre and its variation (scan actual lines, never assert a metre; the stylometrics script reports line length and end-stopping, which supports an enjambment claim but cannot scan metre), stress, rhyme, stanza, enjambment and caesura, line breaks, sound, refrains, the turn, image density, compression, how form and meaning press on each other. Separate the convention from the author's handling of it.

**Drama.** Act and scene shape, soliloquy, aside, dramatic irony, ensemble, conflict carried in speech, stage directions, entrances and exits, each character's rhetoric, shifts between verse and prose, escalation, symmetry.

**Non-fiction.** Thesis, argument, choice of evidence, progression, persuasion, explanation, examples and analogies, handling of disagreement, digression, humour, closing moves. Keep the author's persuasive technique apart from the truth of their claims. A reconstruction never repeats an unsupported claim as fact.

**Translation between forms.** When a playwright's methods feed a novel, carry over the rhetoric, psychology and conflict structure, not stage directions or monologues. When a novelist's methods feed a play, carry over the information control and subtext, not interior narration.

## Auditor adjustment

The auditor's ten categories are written for prose fiction. For verse or drama, mark the categories that do not apply as "not applicable", with the reason (for example, free indirect discourse in a play written without a narrator). The auditor still runs on every substantial passage. Only the categories change. See `references/04-style-consistency-auditor.md`, B11.

## Outputs

Findings for dossier section J, form-specific segmentation rules for corpus intelligence, and the auditor adjustment for the project.

## Quality test

For a metrical claim, can the scansion of three cited lines be shown? For a dramatic claim, can it be shown in what the characters say rather than in a summary of the plot?

## Failure modes

- **Metre asserted, not scanned.** Repair: scan lines or withdraw the claim.
- **Theatrical prose.** Monologues and stage directions dropped into a novel. Repair: translate the method, not the format.

## Signals

- (+) The auditor runs cleanly with the adjusted categories.
- (-) An applicable auditor category keeps failing on a verse or drama passage. Check whether it should apply at all.

## Contract

```contract
node: form-specialist
sends: author-dossier | strong | form variation, for dossier section J
sends: corpus-intelligence | strong | segmentation rules that extraction must keep: line breaks, speaker labels, stage directions
sends: engine-auditor | contextual | which auditor categories do not apply to verse or drama, and why
sends: stylistic-forensics | moderate | verse and drama features: metre, enjambment, speech rhetoric
receives: author-dossier | moderate | the forms the profile must cover for this project
receives: corpus-intelligence | strong | form classification per work: prose, verse, drama or non-fiction
receives: engine-auditor | contextual | scores for the categories that do apply
receives: stylistic-forensics | moderate | prose-level findings that may carry across forms
```
