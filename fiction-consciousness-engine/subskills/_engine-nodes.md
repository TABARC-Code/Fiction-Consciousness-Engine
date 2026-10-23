# Engine nodes

The subskills above link to parts of the core engine. Those parts are not subskill folders, so their side of each contract is recorded here. Reading down any node shows everything it gives and everything it takes.

A node's text in `references/` is not changed by these contracts. In particular `engine-drafting` stands for the verbatim Master System and subskills 1 to 20 at work. It receives findings as project-specific tuning, never as edits to the specification.

## engine-drafting

Steps 2 to 7 of the workflow in `SKILL.md`: the Master System and subskills 1 to 20 drafting a scene.

```contract
node: engine-drafting
sends: character-narrative-forensics | moderate | subskill quality tests that failed under the author's profile
sends: engine-auditor | critical | the drafted passage
sends: engine-scene-ledger | critical | state changes the draft caused
sends: manuscript-architect | strong | conflicts between the chapter plan and the instruction priority
receives: character-narrative-forensics | strong | author-specific calibration for subskills 1, 3, 6 and 13 to 18
receives: engine-auditor | critical | categories scoring below 4, as targeted revision tasks
receives: engine-scene-ledger | critical | scene state before drafting
receives: manuscript-architect | critical | generation contract and chapter purpose
```

## engine-auditor

The Style Consistency Auditor, `references/04-style-consistency-auditor.md`.

```contract
node: engine-auditor
sends: engine-drafting | critical | categories scoring below 4, as targeted revision tasks
sends: form-specialist | contextual | scores for the categories that do apply
sends: reconstruction-validator | strong | the ten category scores for the same passage
receives: engine-drafting | critical | the drafted passage
receives: form-specialist | contextual | which auditor categories do not apply to verse or drama, and why
receives: reconstruction-validator | strong | fidelity findings on five dimensions, mapped to auditor categories
```

## engine-calibration

The calibration protocol and absorption method, `references/05` and `06`.

```contract
node: engine-calibration
sends: engine-profile | critical | tiered, located entries from absorption
sends: reconstruction-validator | strong | profile status after each test
receives: engine-profile | critical | entries to re-test after a change
receives: reconstruction-validator | strong | situation test passages, used as clone tests
```

## engine-profile

The project's style profile, `fce-project/style-profile.md` and `.json`.

```contract
node: engine-profile
sends: author-dossier | critical | evidence from approved chapters, and entries marked doubtful
sends: engine-calibration | critical | entries to re-test after a change
sends: engine-feedback | strong | the profile entries behind a rejected passage
receives: author-dossier | critical | operational profile mapped onto the nine calibration areas, plus extensions and registers
receives: engine-calibration | critical | tiered, located entries from absorption
receives: engine-feedback | critical | the author's approvals and rejections
```

## engine-scene-ledger

The silent scene state ledger, `templates/scene-state-ledger.md`.

```contract
node: engine-scene-ledger
sends: engine-drafting | critical | scene state before drafting
sends: manuscript-architect | critical | the scene's end state, to update canon
receives: engine-drafting | critical | state changes the draft caused
receives: manuscript-architect | critical | canon from the manuscript continuity ledger for the coming scene
```

## engine-book-analysis

Analyse mode, `references/07-craft-source-analysis.md`.

```contract
node: engine-book-analysis
sends: corpus-intelligence | moderate | coverage gaps met while reporting
receives: corpus-intelligence | moderate | source inventory and coverage
```

## engine-feedback

The author's reactions, routed through the loops in `references/lattice.md`, section 4.

```contract
node: engine-feedback
sends: engine-profile | critical | the author's approvals and rejections
sends: reconstruction-validator | critical | the author's verdict, which outranks the validator
receives: engine-profile | strong | the profile entries behind a rejected passage
receives: reconstruction-validator | moderate | passages the validator passed but the author rejected
```
