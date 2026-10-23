# Fiction Consciousness Engine: the description

The README says what the engine does and how to install it. This file explains why it is built the way it is, what state it is actually in, and what I'd want you to know before you change it.

## The short version

The engine writes fiction in close character consciousness. It can also study an author's books and turn what it finds into a style profile. The profile is only as good as the evidence under it, so most of the design is about refusing to pretend otherwise.

Most of the code is not clever. The interesting part is the set of rules that stop the clever-sounding output from being wrong.

## Why evidence tiers

A style note such as "varied sentence length" describes half of all writers. It sounds like an observation, but it tells a drafting model nothing it can act on.

So every profile line has to carry an evidence tier (A1 quoted, A2 paraphrased, A3 example, A4 inferred) and a location: a source, a chapter, a page or a sample. A line without both stays "unclear". The linter, `scripts/profile_lint.py`, rejects a list of generic phrases and any bullet that lacks a tier or a location. The phrase list is a starting list. It will grow, and it should.

## Why no similarity score

I considered a "how like the author" percentage and rejected it. Sentence length, function-word rate and trigram habits do not add up to a measure of voice, and a single number would look like one. The script reports differences only, and it prints its own limits with every run.

## Why the verbatim specification

Three of the reference files are the maintainer's specification, reproduced unchanged. Their hashes are stored in `validate.py`. If someone edits one of them, the validator fails. That looks fussy. It is also the only reliable way I found to stop a tidy-up pass quietly changing the rules the rest of the skill depends on.

Section A of the auditor and calibration files is held to the same standard, for the same reason.

## The contract graph

The subskills talk to each other. Each one has a contract block that names what it sends, what it receives, and how strongly the link matters. Every link has to run both ways, and the return has to be a real return rather than an echo. The validator enforces reciprocity, rejects a link that mirrors itself, and rejects a link to a node that does not exist.

I wanted the graph to be checked by a program. Describing it in prose and trusting it would have drifted within a week. The graph itself is in `references/lattice.md`, section 8.

## Design decisions

Four choices shaped the build.

One router, not seven skills. The modes share the same rules and the same profile. Splitting them would have meant keeping those rules in sync by hand.

Project data lives in `fce-project/`, not in the templates. An earlier build wrote project notes into the blank forms. That was a design flaw, and the validator now refuses template writes unless the line names `fce-project/`.

The auditor gates delivery. It runs on every substantial passage. I accepted the cost in tokens because a silent continuity error is the failure I'd least like to ship.

Scores stay out of prose. A delivered chapter is prose. Scores appear only when asked for, because the score itself changes how a draft reads.

## Current state

- Working: the router, the subskill wiring, the validator, both scripts, and the templates.
- Not yet tested: the auditor's anchors against any passage a real author or you have judged. Until that happens, the scores are a guide and nothing more.
- Planned: calibration against an author's approved passages, and a full run on a real manuscript.
- Unknown: whether the contrast step (describing the model's default next to the source, then recording only the differences) improves a profile. The idea is sound on paper. I have not measured it.

## Limitations and awkward bits

The thresholds are starting values I chose: three samples, 500 words, a recall of 0.8, and at most one in four passages where the auditor and the author disagree. I did not measure them. They are written down so they can be changed, and they should be.

Sentence splitting is a rule of thumb. It will misread abbreviations, verse and unusual punctuation. Dialogue is found by quotation marks only, so unmarked speech is missed.

Stylometrics says nothing useful about anything under about 2,000 words, and the lines figures are for verse only. For prose they only repeat the paragraph structure.

## Future direction

The next useful step is a real run: one author, one approved passage from the user, and a record of where the engine went wrong. That run will tell me more than another round of rereading.

After that, I would like to decide whether the contrast step earns its place, and to tune the thresholds from data rather than from my own sense of what seems reasonable.
