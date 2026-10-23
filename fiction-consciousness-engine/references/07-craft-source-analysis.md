# Craft source analysis

Status: method. Used when the user supplies a book, essay, manual or reference passage and wants it analysed, not only absorbed. Absorption (`06`) turns approved prose into a profile. This file says how to read the source itself, what to report, and how confident to be.

Sources adapted for this file are credited in `LICENCE-NOTICE.md`. No wording was copied. Analysis is a report about a book. It is never the same thing as the operational profile used to write: keep the two apart (see the author dossier subskill).

---

## 1. Read the source before analysing it

1. Confirm the source is text. For a PDF, check the page count and whether the text layer is real. A scanned book returns empty or garbled text. Rasterise representative pages and read them visually, and say that the reading is visual.
2. For a long book (over about 400 pages), read the front matter, the contents, the introduction, the conclusion, and the opening of each chapter. Sample the middle. Record every skipped section in the coverage record (`fce-project/source-register.md`).
3. Do not reproduce long passages. Quote at most one short phrase per point, and only where the exact words are the point. Describe the rest.
4. Note extraction problems in the output: missing pages, broken tables, footnotes that were lost.

Budget: a 300-page book is roughly 60,000 to 120,000 tokens of text. Start with the highest-value sections and stop when the question is answered.

---

## 2. Identify the source type and the analysis frame

Decide before writing anything:

- **Genre and subgenre.** For example: literary fiction, science fiction, psychological suspense, craft manual, narrative non-fiction, history, memoir, essay collection.
- **Context.** Who wrote it, when, for what readers, from what position. A writer's own craft book carries a different weight from a critic's.
- **Hybrid status.** Some books need two frames. A fictionalised memoir needs fiction and memoir frames. Blend them, and say which frame leads.

Then pick a frame:

| Source | Frame | Core question |
|---|---|---|
| Argument, craft manual, self-help, essay | Frame A: argument | What is the claim, and how well is it held up? |
| Novel or story collection | Frame B: fiction | How does the narrative make the reader feel and understand what it does? |
| History, biography, memoir | Frame C: lived or documented account | What is the account claiming, and whose view does it come from? |
| Poetry or drama | Frame D: verse and stage | How does the form itself make the meaning? |

---

## 3. Frame A: argument and craft texts

Report in this order. Each section is prose unless a list genuinely helps.

**Central claim.** One or two sentences, stated as a claim someone could disagree with. Avoid "the author argues that craft matters".

**Main moves.** Three to six logical steps that build the claim. Say what each depends on. These are not chapter summaries.

**Evidence and its quality.** For each important piece of support, say what kind it is: controlled study, case, anecdote, expert opinion, the author's own experience. Flag where a general claim rests on one anecdote or a single secondhand source. Flag overstatement.

**Models and named concepts.** Any framework the author introduces: what it is, what it explains, where it breaks down.

**Usable technique.** Specific, practical methods, reproduced as the author's logic. Each one must be stated in the source's own terms, not generalised into advice the source does not give. Each one carries a tier (`06`, section 2).

**Counterarguments.** The objections the author raises and answers. An objection the author ignores is a gap, not a neutral omission.

**Gaps and blind spots.** Where the argument is weakest, where evidence is thin, what the author avoids addressing. This section needs judgement. Leave out minor quibbles. If nothing structural is wrong, say so.

**Quotes.** At most three, each short, each located (chapter or page). Do not invent quotes. If a quote cannot be checked, describe the passage instead.

---

## 4. Frame B: fiction

Written for reference novels and stories the author wants to learn from. The aim is craft, not plot summary.

**Central themes.** Separate surface subject from what the author seems to be interrogating. Mark interpretation as inference.

**Plot architecture.** Setup, central conflict, turning points, climax, resolution. Trace what drives the story forward. Spoiler-aware: say so if the summary reveals an ending.

**Consciousness and distance.** Whose mind is in the narration, how close it sits, how it moves in and out. This is the most useful section for this engine. Map it onto subskills 1 and 13.

**Character.** For each major character: wants, fears, and whether they change. Map belief and self-deception onto subskills 14 and 16.

**Technique.** Point of view, tense, structure, pacing, time handling, unreliable narration. Explain what each choice does. Do not just name it.

**Dialogue and subtext.** How speakers differ, what they avoid saying, how talk carries conflict. Map onto subskill 6.

**Suspense and information.** How the book releases information, when it withholds it, how tension is built and relieved. Map onto subskills 8, 9 and 15.

**Recurring detail.** Images, objects or lines that gather meaning. Do not manufacture symbolism the text does not support.

**Tone and register.** The emotional texture, and whether the effects are earned or strained.

**Passages.** At most three short passages, each located. Use them to show a technique, not to show off the prose.

---

## 5. Frame C: history, biography, memoir

**Central account.** What the book claims happened, or what this life is ultimately about.

**Arc and structure.** Chronological, thematic, or argument-led. Say which.

**Key figures.** Who drives events, and how the author weights individual agency against structure and chance.

**Causes and consequences.** Individual, structural or contingent. Say which the author relies on.

**Perspective.** The author's lens: political, disciplinary, personal. Name what the lens makes clear and what it may miss. No author is neutral.

**Lessons.** Only the ones the text supports, stated as conditional claims ("X leads to Y under conditions Z"). Vague moralising is not a lesson.

**Revelations.** Facts or documents that reframe the subject. Give the location.

---

## 5a. Frame D: poetry and drama

**Formal structure.** For verse: metre (scan actual lines), rhyme, stanza, lineation, the turn. For drama: acts and scenes, entrances and exits, verse and prose shifts.

**Language and rhetoric.** Sound, compression, image density for verse. Each character's rhetoric, soliloquy and aside for drama.

**Progression.** How the poem or play moves: argument, accumulation, reversal, escalation.

**Voice and character.** The speaker of a poem is not the poet. A character's speech is not the playwright's view.

**Themes.** As in Frame B, with interpretation marked.

Detail on both forms is in `subskills/form-specialist/SUBSKILL.md`.

## 6. Confidence and separation

Every finding is marked by what kind of claim it is:

- **Author's claim.** What the source says.
- **Supported.** The evidence in the source supports it, with a location.
- **Engine's judgement.** The engine's reading. Always labelled.

Never blend the three into one sentence without a marker. An author's claim that the evidence does not support is reported as a claim that lacks support.

Confidence is separate from tier. A finding can be high confidence and still rest on an A4 inference, if it is labelled as one.

---

## 7. Reader verdict (optional, on request)

Four to six sentences. Who will get most from the source, its greatest strength, its most significant weakness, and whether it delivers on its own stated purpose. A verdict that could apply to any book in the genre fails and must be rewritten.

For this engine, the verdict also says how useful the source is for the calibration profile: whether it has passages worth absorbing, and what it would add to the nine areas.

---

## 8. What not to do

- Do not present a craft manual's rules as laws of fiction. They are the author's rules, and the Master System already decides which ones this engine follows.
- Do not analyse a book the user has not supplied. Do not work from memory of a book and present the result as a reading of the text.
- Do not turn analysis into absorption without the user's say-so. Analysis is a report. Absorption changes the profile.
