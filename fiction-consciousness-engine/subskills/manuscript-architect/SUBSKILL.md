# Manuscript architect

Plans a book and keeps it whole: the generation contract, the blueprint, the chapter loop and the manuscript's canon.

## Purpose

A long manuscript fails in two ways. It drifts in voice, which the auditor and calibration catch. Or it drifts in fact: a wound heals between chapters, a letter is opened twice. This subskill holds the canon so the engine cannot quietly forget what it wrote.

## Activation

Plan mode, and Write mode for any work longer than one chapter.

## Procedure

1. **Settle the generation contract.** Target author or profile, genre, form, period, setting, premise, audience, length, structure, number of chapters, viewpoint, themes, characters, plot direction, degree of fidelity (historical reconstruction, contemporary adaptation, genre transfer or blend), and readability needs. Use what the user gave. Fill a missing item with a sensible default only where the request does not hang on it, and record that it was a default. The user's premise, characters and structure always beat traits inferred from the source author's books.
2. **Build the blueprint** (form in `templates/book-blueprint.md`, working copy in `fce-project/book-blueprint.md`): title and premise, form, active profile, perspective, central conflict, thematic questions, character dossiers (wants, contradictions, relationships, how each one speaks), setting and world rules, structure, chapter outline (purpose, developments, consequence), continuity requirements, length and pacing, and the ending and what makes it earn itself. If the user has a blueprint already, use theirs. Do not impose a modern three-act shape on a form that needs another.
3. **Run the chapter loop,** one substantial chapter or scene at a time unless asked otherwise:
   - read the canon for the chapter from the continuity ledger
   - set the chapter's purpose, characters, conflicts, viewpoint, register and ending
   - pass the canon to the scene state ledger and the contract to drafting
   - draft through the engine's workflow (Steps 2 to 7), auditor included
   - send the chapter to the reconstruction validator
   - write the scene's end state back to the continuity ledger
4. **Keep the canon** in `fce-project/continuity-ledger.md` (form in `templates/manuscript-continuity-ledger.md`). After each chapter, record events, new character facts, relationship changes, places and chronology, world details, objects and injuries, promises, questions opened and closed, character knowledge, open tensions, foreshadowing, departures from the outline, and changes to stylistic decisions. Never rewrite an established fact silently. If a new idea conflicts with canon, name the conflict and resolve it, and list any earlier chapters that would need revision.
5. **Review the whole manuscript** only when all of it is available: larger patterns, drift, repeated images, character arcs, pacing, structure. Never claim a whole-manuscript review over a partial manuscript.

## Outputs

The writing specification, the blueprint, the canon, and complete chapters in prose. Chapters are prose only. Planning documents are kept apart and shown on request.

## Quality test

Pick any established fact from chapter 2. Can the ledger say where it was set up, and confirm it still holds in the latest chapter?

## Failure modes

- **Outline instead of chapter.** Repair: write the scene unless the user asked for an outline.
- **Source premise replacing the user's.** Repair: the contract governs subject, the profile governs method.
- **Canon drift.** Repair: the scene ledger reads from canon before every scene and writes back after.

## Signals

- (+) The validator reports no continuity faults across several chapters.
- (-) The author spots a continuity error the ledger should have caught. Run the why-chain (`references/lattice.md`, 4.2) on the ledger, not the prose.

## Contract

```contract
node: manuscript-architect
sends: author-dossier | strong | situations the profile gives no guidance for, and planned departures from it
sends: engine-drafting | critical | generation contract and chapter purpose
sends: engine-scene-ledger | critical | canon from the manuscript continuity ledger for the coming scene
sends: reconstruction-validator | strong | finished chapters and, when available, the whole manuscript
receives: author-dossier | critical | active profile, contextual rules and negative constraints
receives: engine-drafting | strong | conflicts between the chapter plan and the instruction priority
receives: engine-scene-ledger | critical | the scene's end state, to update canon
receives: reconstruction-validator | strong | drift reports that need a blueprint or continuity change
```
