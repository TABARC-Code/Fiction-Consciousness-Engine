# Author dossier

Turns the forensic findings into two documents: a research dossier, and the operational profile the engine writes from.

## Purpose

Analysis and instruction are different jobs. The dossier explains the author. The profile tells the engine what to do. Keeping them apart stops a book report from posing as a writing guide, and stops a writing guide from claiming more than the evidence allows.

## Activation

Reconstruct mode, after the forensic subskills. Updated whenever approved chapters return evidence.

## Procedure

1. **Build the dossier** (form in `templates/author-dossier.md`, working copy in `fce-project/author-dossier.md`), sections A to M:
   A corpus and provenance, B literary identity, C core voice, D linguistic architecture, E cadence, F imagery and description, G character and dialogue, H narrative architecture, I themes, J variation by form, genre, period and narrator, K signatures, L negative constraints, M confidence and limits.
   Every signature in K needs evidence. Every constraint in L needs a reason. Section M separates well supported traits from tentative ones and names conflicting evidence.
2. **Build the operational profile.** Map the dossier onto the nine calibration areas of the engine's style profile (`references/05-style-calibration-protocol.md`), which stay the mandatory core. Put anything that does not fit the nine areas under extensions: imagery principles, tonal principles, structural principles, exclusions.
3. **Write registers.** One register per distinct mode the author uses: each narrator, letters within a novel, verse sections. Each register states only how it departs from the core profile.
4. **Write actionable entries.** Each entry names a mechanism a writer can follow. "Write dramatically" fails. "Builds opposition through parallel clauses, then breaks the pattern with a short reversal" passes.
5. **Lint the profile.** Run `python3 scripts/profile_lint.py fce-project/style-profile.md`. Fix every generic phrase and every entry without a tier or location before the profile is used.
6. **Blending several authors.** Build a separate dossier for each author first. Then name a dominant voice, list compatible and incompatible traits, and set an explicit order of precedence. Never average the authors together.

## Outputs

- The author dossier (research).
- The operational profile and registers (instruction), written to `fce-project/style-profile.md` and `.json`.
- A one-paragraph confidence statement: coverage, evidence strength, open limits.

## Quality test

Hide the author's name. Could a writer use the profile alone to draft a scene this author would recognise as using their methods, without copying a sentence? If the profile would leave them guessing, it is not finished.

## Failure modes

- **Dossier copied into the profile.** Repair: the profile keeps only what changes behaviour.
- **Unsupported signature.** Repair: find the evidence or move it to section M.
- **Blend by average.** Repair: set the hierarchy.

## Signals

- (+) An approved chapter confirms a profile entry.
- (-) The validator fails a test that traces to a profile entry. Mark the entry doubtful and return to the forensic subskill that produced it.

## Contract

```contract
node: author-dossier
sends: character-narrative-forensics | strong | gaps found in those sections
sends: contrast-extraction | moderate | entries flagged as generic, to be contrasted again
sends: corpus-intelligence | strong | open questions that need more of the corpus read
sends: engine-profile | critical | operational profile mapped onto the nine calibration areas, plus extensions and registers
sends: form-specialist | moderate | the forms the profile must cover for this project
sends: manuscript-architect | critical | active profile, contextual rules and negative constraints
sends: reconstruction-validator | strong | signatures and constraints to test
sends: stylistic-forensics | strong | contradictions and gaps found in those sections
receives: character-narrative-forensics | critical | character, dialogue, psychology, plot, time, scene and theme findings, for dossier sections G to I
receives: contrast-extraction | strong | specific, followable difference statements for the profile
receives: corpus-intelligence | strong | coverage record and provenance for dossier section A
receives: engine-profile | critical | evidence from approved chapters, and entries marked doubtful
receives: form-specialist | strong | form variation, for dossier section J
receives: manuscript-architect | strong | situations the profile gives no guidance for, and planned departures from it
receives: reconstruction-validator | strong | failed tests that point to profile entries
receives: stylistic-forensics | critical | voice, language, rhythm, imagery and device findings with evidence, for dossier sections C to F, K and L
```
