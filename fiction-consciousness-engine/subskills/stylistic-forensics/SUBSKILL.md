# Stylistic forensics

Works out how an author builds language: voice, vocabulary, sentences, rhythm, paragraphs, punctuation, imagery and devices. It explains what each choice does, not only that it occurs.

## Purpose

Surface imitation (archaic words, long sentences, ornate metaphor) is not style. Style is the relation between choices: why this sentence runs long here, why this image keeps returning. This subskill finds those relations and records the evidence for each.

## Activation

Reconstruct mode, and Absorb mode for corpora longer than one chapter. It runs after corpus intelligence and alongside contrast extraction.

## Procedure

Work through the layers in order. Each finding gets a location, a tier, and a function: what the choice does for the reader.

1. **Literary identity.** Period, tradition, genre, readership, the conventions the author follows and the ones they break. Facts and interpretation are kept apart.
2. **Authorial voice.** Narrative authority (certain, speculative, unreliable, self-questioning), relation to the reader (confiding, complicit, sceptical, confrontational), distance, moral stance, how emotion surfaces (stated, acted, displaced into image, buried in dialogue), and intellectual habit. Keep the author apart from the narrator, and both apart from the characters. A character's prejudice is not the author's.
3. **Lexical fingerprint.** Register and what makes it shift, concrete against abstract, verb classes, qualifying habits, unusual pairings, recurring semantic fields (bodies, buildings, weather, machinery, law), and what the author avoids. Absence counts, but one book cannot prove a prohibition.
4. **Sentence architecture.** Clause order, subordination, periodic and cumulative sentences, parallelism, antithesis, inversion, fragments, parenthesis, self-correction, openings and endings. For each pattern, say what it does: a long sentence can enact obsession, delay a revelation, build comic speed or pile up detail. Those are different findings even at the same length.
5. **Cadence.** Where stress falls, where the reader is made to pause, how prose speeds up in action and argument and slows in reflection, how sentences resolve (closure, reversal, ambiguity, interruption). Rhythm serves meaning. Variety alone is not a style.
6. **Paragraphs and transitions.** What paragraphs are for (movement, description, argument, psychology, delayed revelation, dramatic punctuation), whether an idea resolves inside one paragraph or migrates across several, how scenes and chapters hand over.
7. **Punctuation.** Semicolons, colons, dashes, ellipses, questions, italics, dialogue attribution. Separate the author's habits from house style and later editions. Do not exaggerate a quirk to make imitation look recognisable.
8. **Imagery and description.** For each significant device: when it appears, how it is built, what it connects, its effect, whether it recurs and whether it changes. Find the author's method of association (politics as illness, memory as architecture), never the images themselves for reuse. Note which details are chosen, which are left out, and whose eyes the description comes through.
9. **Devices.** Catalogue only what materially contributes: anaphora, chiasmus, polysyndeton, free indirect discourse, leitmotif and so on. A device found in the source does not become compulsory in new writing.

Send measurable hypotheses to stylometrics as they arise ("sentences shorten under pressure"). A hypothesis the numbers contradict is revised, not defended.

## Outputs

Findings for dossier sections C to F, K (signatures) and L (negative constraints), each with function, evidence, tier and confidence.

## Punctuation in generated prose

Generated prose follows the active profile's punctuation, dashes included, whatever house or personal preferences apply to notes and reports.

## Quality test

For each finding, answer: what should a writer do differently because of it? A finding with no answer is description, not forensics.

## Failure modes

- **Naming without function.** "Uses anaphora." Repair: say when and to what end.
- **Stereotype in place of evidence.** "Victorian, so ornate." Repair: cite the passages or drop it.
- **Narrator mistaken for author.** Repair: check the finding against a second narrator or work.

## Signals

- (+) Stylometrics confirms a hypothesis. A finding survives the clone test.
- (-) The dossier reports a contradiction between two findings. Re-read both locations.

## Contract

```contract
node: stylistic-forensics
sends: author-dossier | critical | voice, language, rhythm, imagery and device findings with evidence, for dossier sections C to F, K and L
sends: character-narrative-forensics | moderate | sentence and rhythm findings
sends: contrast-extraction | strong | hypotheses to put to a contrast pair
sends: corpus-intelligence | strong | sections to re-read where evidence is thin or the text may be editorial or a translator's
sends: form-specialist | moderate | prose-level findings that may carry across forms
sends: stylometrics | strong | hypotheses that can be measured
receives: author-dossier | strong | contradictions and gaps found in those sections
receives: character-narrative-forensics | moderate | scene-type labels, so rhythm findings can be tied to the scenes they occur in
receives: contrast-extraction | strong | difference statements: what the source does that the model's default does not
receives: corpus-intelligence | critical | primary-author text by section, with coverage and authorship status
receives: form-specialist | moderate | verse and drama features: metre, enjambment, speech rhetoric
receives: stylometrics | strong | computed distributions that confirm, qualify or contradict a hypothesis
```
