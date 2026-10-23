# Character and narrative forensics

Works out how an author makes people and stories: consciousness, dialogue, psychology, plot, time, scenes and themes. Its findings calibrate the engine's own subskills for this author.

## Purpose

The engine already knows how to write a mind (subskills 1 to 20). This subskill learns how this particular author does it, so the engine's machinery is tuned to the author, not replaced.

## Activation

Reconstruct mode, and Absorb mode for corpora with several scenes. Runs on the same sections as stylistic forensics.

## Procedure

1. **Character construction.** Through action and inaction, speech and silence, contradiction, self-deception, relationships, habits, gestures, repeated choices, memory, the gap between intention and consequence. Does the author explain motive or leave it to inference?
2. **Dialogue.** How speakers differ in vocabulary, grammar, rhythm, confidence and class. What goes unsaid. How talk carries power and resistance. Interruption and silence. How exposition gets into speech. Attribution and movement. Long speeches or rapid exchange. How speech changes under pressure. Keep the author's principles of dialogue apart from any one character's speech.
3. **Psychology.** Restraint, introspection, obsession, repression, shifts in self-image, the gap between what a character believes about themselves and what the narrative shows. How the reader learns of it.
4. **Plot.** Openings and their promises, information control, inciting events, reversals, discoveries, subplots, climaxes, endings (closed, ambiguous, refused). What drives the story: character, circumstance, causality, coincidence, investigation, association. The author's relation to suspense, inevitability and surprise. Do not assume a three-act shape.
5. **Time and perspective.** Person, tense, focalisation, omniscience or restriction, jumps, retrospection, embedded stories, parallel timelines, foreshadowing, unreliability, intrusion. What each does to the reader's knowledge.
6. **Scenes.** How scenes open, establish place, bring in conflict, control information and end (reversal, question, shift, discovery, quiet close). The balance of action, dialogue, description and reflection.
7. **Pacing.** How the author speeds and slows the story, and how characters move it on.
8. **Themes.** Separate explicit narrator argument, characters' beliefs, patterns supported by structure, readings the text suggests, and speculation about the author's own views. Not every recurring image is a symbol.

Label each scene by type (investigative, dialogue, exploration, horror, reflective, action, or the author's own types) and pass the labels to stylistic forensics so rhythm findings can be tied to scene type.

## Engine calibration

Map findings onto the engine's subskills as project-specific tuning, never as edits to `references/02` or `03`:

| Finding | Tunes subskill |
|---|---|
| How thought and memory surface | 1, 3 |
| Dialogue principles | 6 |
| Distance and focalisation | 13 |
| Knowledge and belief handling | 14 |
| Information release | 15 |
| Self-deception | 16 |
| Scene causality | 17 |
| Recurring detail | 18 |

## Outputs

Findings for dossier sections G to I, scene-type labels, and the calibration table above, filled for this author.

## Quality test

Could the engine's ledger for a new scene be filled in the way this author would fill it? If a field would be a guess, the finding is not yet usable.

## Failure modes

- **Plot summary posing as analysis.** Repair: trace structural logic, not events.
- **Every character in the narrator's voice.** Repair: check dialogue findings with tags stripped.
- **Theme inflation.** Repair: demand two or more structural supports per theme.

## Signals

- (+) A tuned subskill passes its quality test on the first draft.
- (-) A tuned subskill's quality test fails under the profile. The finding behind it is marked doubtful.

## Contract

```contract
node: character-narrative-forensics
sends: author-dossier | critical | character, dialogue, psychology, plot, time, scene and theme findings, for dossier sections G to I
sends: corpus-intelligence | moderate | re-chunk requests where a scene was split across chunks
sends: engine-drafting | strong | author-specific calibration for subskills 1, 3, 6 and 13 to 18
sends: stylistic-forensics | moderate | scene-type labels, so rhythm findings can be tied to the scenes they occur in
receives: author-dossier | strong | gaps found in those sections
receives: corpus-intelligence | critical | the same sections with chapter and scene boundaries intact
receives: engine-drafting | moderate | subskill quality tests that failed under the author's profile
receives: stylistic-forensics | moderate | sentence and rhythm findings
```
