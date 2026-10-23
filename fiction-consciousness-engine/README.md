# Fiction Consciousness Engine

Version 3.0.3. A Claude skill for writing fiction from inside a character's head, in a voice built from evidence, and keeping it that way across a whole book.

It started as a close-third prose engine for science fiction, suspense and horror. It still is one. Version 3 adds the other half: reading an author's books properly, working out how they write, and turning that into a profile the engine can draft from, tested before it's trusted.

## What it does

- **Write.** Scenes and chapters, drafted through the Master Fiction Writing System and twenty craft subskills, with a ten-category auditor gate before anything is delivered.
- **Absorb.** Learns your own voice from passages you've approved.
- **Reconstruct.** Reads an author's corpus (novels, plays, poems, essays), separates their words from editors' and translators', and builds a research dossier and an operational style profile.
- **Plan.** Writing specification, book blueprint, character dossiers, and a continuity canon that every chapter reads from and writes back to.
- **Compare.** Separate profiles for several authors, then a deliberate blend with a stated hierarchy. No averaging.
- **Analyse.** A plain report on a book: claim, evidence, gaps, technique.
- **Audit.** Scores and located notes, when you ask.

## How the parts talk to each other

Nine subskills sit in `subskills/`. Each one has a contract block saying exactly what it sends to its neighbours and what it gets back. Every link runs both ways, and the thing that comes back isn't an echo. Corpus intelligence hands text to stylometrics; stylometrics hands back the scanning faults its numbers turned up. The validator refuses to pass a one-way link, a mirrored one, or a link to a node that doesn't exist. `references/lattice.md`, section 8, walks through the four flows.

## Folder

    fiction-consciousness-engine/
      SKILL.md                     router: rules, modes, workflow
      README.md  description.md  LICENCE-NOTICE.md
      references/
        01 to 03                   specification (verbatim)
        04-style-consistency-auditor.md
        05-style-calibration-protocol.md
        06-absorption-and-extraction.md
        07-craft-source-analysis.md
        lattice.md                 links, loops, subskill graph, changelog
        neighbour-patches.md
      subskills/
        corpus-intelligence/  contrast-extraction/  stylistic-forensics/
        character-narrative-forensics/  form-specialist/  stylometrics/
        author-dossier/  manuscript-architect/  reconstruction-validator/
        _engine-nodes.md           the engine's own side of each contract
      templates/                   blank forms, copied into fce-project/
      scripts/
        stylometrics.py            measures text, compares source and draft
        profile_lint.py            rejects generic or unsourced profile entries
        validate.py                checks the skill's own wiring

## Things to know

- **The scoring is still self-assessed.** The auditor and validator are calibrated against passages you've judged, and your reading outranks both. When you reject something they passed, it gets logged and they get recalibrated.
- **Numbers are computed or absent.** Stylometrics runs a script on real text. There's no "94 per cent like the author" anywhere, because nothing measured supports a figure like that.
- **Thin material gives thin profiles.** Fewer than three samples or 500 words and most entries stay "unclear". That's deliberate.
- **Full reading for reconstruction.** A profile built from samples is labelled provisional until the whole corpus has been read, in chunks if it has to be.
- **Methods, not copies.** It learns how an author builds sentences and scenes. It doesn't reuse their sentences, images or plots, and it won't present new writing as the author's own.
- **Your project lives in `fce-project/`.** The templates stay blank. Back up that folder with the manuscript.
- **Not yet run on a full manuscript.** The scripts and the wiring are tested. The method hasn't been run end to end on a real book yet, so expect rough edges and say where you find them.

## Installing

Put the `fiction-consciousness-engine` folder where your skills live. The folder name has to stay as it is. Run `python3 scripts/validate.py` after any change.

## Credits

See `LICENCE-NOTICE.md`.
