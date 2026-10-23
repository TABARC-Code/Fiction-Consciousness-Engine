# Contrast extraction

Finds what a writer does by comparing them with what the model does by default on the same material.

## Purpose

Asked to describe a style cold, a model reaches for phrases that fit half of all writers: "varied sentence lengths", "conversational tone". Contrast fixes that. The model writes its own default version of the same moment, then describes only the differences. A difference is specific by construction.

The comparison step is adapted from a voice-extraction skill shared with this build (see `LICENCE-NOTICE.md`). Its detector-evasion aims are not used.

## Activation

- Absorb and Reconstruct modes, after corpus intelligence has supplied anonymised samples.
- Again whenever profile-lint or the dossier flags an entry as generic.

## Procedure

1. **Take the samples.** Numbered, anonymised, at least three, at least 500 words in total, each at least 100 words. Fewer than that, and the profile is marked thin. Variety helps more than volume: three scenes of different kinds teach more than six of the same kind.
2. **Write the baselines.** For each sample, write the model's plain default version of the same moment: same situation, same characters, same length, no attempt at any particular voice. Baselines are working material only. They are never shown as prose and never delivered.
3. **Pass 1: describe the differences.** For each pair, say what the source does that the baseline does not, under: structure of paragraphs and scenes, how thought moves, where it commits and where it hedges, sentence technique, vocabulary (concrete or abstract, technical or plain), and habits (parentheses, fragments, questions, interruptions). Describe behaviour a writer could follow. Do not report averages here. Stylometrics does that.
4. **Pass 2: pressure test.** For each statement ask three questions. Could it describe half of all writers? Then sharpen it or drop it. Could someone follow it as an instruction? If not, add a trigger ("when cornered") and a located example. Is there a habit seen but not yet named? Name it.
5. **Reject generic statements.** Anything matching the generic list in `scripts/profile_lint.py` is rewritten or dropped.
6. **Find what stays constant.** A statement that holds across different scene types is a stable trait. One that holds in only one type is contextual and is filed as a register rule, not a core trait.

## Outputs

- Difference statements with sample number, location and tier (A2 when seen directly, A4 when inferred).
- Register candidates, one per distinct mode (for example, each viewpoint character, or narration as against letters within the novel).

## Quality test

Hand a difference statement to a writer who has never seen the samples. Can they act on it? If they would have to guess, it is not finished.

## Failure modes

- **Baseline leakage.** The baseline is written badly on purpose, so every difference looks like a virtue. Repair: the baseline is the model's honest default, not a straw man.
- **Topic anchoring.** Differences describe subject matter, not style. Repair: re-anonymise and re-pair.
- **Content copying.** A difference statement quotes the source to make its point. One short located phrase is allowed. More is not.

## Signals

- (+) Statements survive the clone test unchanged.
- (-) Profile-lint flags a contrast statement as generic. Log it and rerun pass 2.

## Contract

```contract
node: contrast-extraction
sends: author-dossier | strong | specific, followable difference statements for the profile
sends: corpus-intelligence | moderate | samples too short, or too alike in topic, to contrast
sends: stylistic-forensics | strong | difference statements: what the source does that the model's default does not
receives: author-dossier | moderate | entries flagged as generic, to be contrasted again
receives: corpus-intelligence | strong | anonymised samples, with topic notes held apart
receives: stylistic-forensics | strong | hypotheses to put to a contrast pair
```
