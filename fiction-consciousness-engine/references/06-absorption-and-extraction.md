# Absorption and extraction for fiction

Status: method. Adapted from book-knowledge-extraction v3.1.0 for the work this skill does. Nothing here changes the Master System or the twenty subskills. It governs how reference material is turned into a style profile, how that profile is tested, and how it is kept honest.

Use it when the user supplies new material to learn from: approved passages, their own earlier chapters, a craft book, or a reference novel named as a model. It runs before the style profile is relied on for a new chapter.

---

## 1. Source types and what each may do

| Source | What it is for | Limits |
|---|---|---|
| Approved passage (the user's own, or one they have marked approved) | Primary calibration. Sets the profile. | Behaviour is extracted, never wording. The text stays in the project. |
| Rejected or heavily rewritten passage | Negative evidence. Shows what the profile must not produce. | Used only to find the faulty profile entry. |
| Craft text (non-fiction on prose, character, suspense) | Technique candidates. | Principles only. Each technique is tested against approved passages before it enters the profile. |
| Reference fiction named as a model | Broad craft principles only. | Never sentences, characters, technologies or scene beats (Master System section 28). |

A craft text can suggest a technique. It cannot define the user's style. Only approved passages do that.

---

## 2. Evidence tiers for fiction

Authority is separate from confidence. A tier says where a fact about the style comes from. Confidence says how sure the entry is.

| Tier | Meaning | Example |
|---|---|---|
| A1 quoted | Located in an approved passage, checked against the text | "Paragraph 4 of chapter 2 ends on the action, not the thought." |
| A2 paraphrased | Behaviour seen in an approved passage, described in the engine's words, with location | "Internal questions appear in clusters of two when the character is cornered." |
| A3 example | A worked case from a craft text or approved passage that illustrates a technique without generalising | A craft text's scene used to show a distance shift |
| A4 inferred | The engine's deduction. Not in any source. Always labelled. Never presented to the user as their style. | "Probably prefers short paragraphs in action." |

Rules:
- Every profile entry carries a tier.
- A4 entries are not used to write prose until they are confirmed by an approved passage or by the user.
- A1 quotes are for the project file only. They are never reproduced in delivered prose.

---

## 3. The seven stages, adapted

The stage names match book-knowledge-extraction so the two skills can be run together. The work is the same. The outputs are fiction-specific.

### Stage A: Absorb

Read every approved passage in full. Write a short gist for each: whose consciousness is in play, what distance it holds, what the passage is doing (reasoning, dialogue, suspense, reflection). Classify each source using section 1.

Coverage record for each source, kept in `fce-project/source-register.md`:
- passage id, description, word count
- read fully: yes or no
- where it is thin (fewer than three samples, under 500 words in total, a sample under 100 words, or one scene only): flagged, because thin evidence gives unclear entries

Check: can the gist be written in one sentence per passage? If not, read again.

### Stage B: Extract

Fill the nine calibration areas in `fce-project/style-profile.md` from the approved passages. For each entry:
- describe behaviour, not wording
- write a trigger where there is one ("when the character is cornered, X happens")
- give the tier and the passage location
- write "unclear" where the evidence does not decide

Run contrast extraction (`subskills/contrast-extraction/SUBSKILL.md`) on the anonymised samples: write the model's own default version of each moment, then record only what the approved passage does differently. Then the pressure test: could the entry describe half of all writers, and could a writer follow it as an instruction? Sharpen or drop. Finally run `python3 scripts/profile_lint.py fce-project/style-profile.md` and fix everything it reports.

Technique candidates from craft texts are written as observable behaviour with a trigger. A technique that cannot be written that way is parked, not promoted.

### Stage C: Clone

This is the test that the profile holds. Write a neutral test passage of about 400 to 600 words, using only the profile and a scene plan with no approved text in it. The scene plan should come from the project, not from the approved passages, so the passage cannot simply copy them.

Compare the clone with the approved passages on the nine areas. Log every divergence:

- **Missing:** an approved behaviour the clone does not show (for example, free indirect discourse drops out under pressure).
- **Lost condition:** a trigger the profile dropped (the internal questions cluster only when cornered, but the clone uses them everywhere).
- **Softened threshold:** a degree that became vaguer ("often" where the approved text shows a pattern of two in a page).
- **Invented:** a clone feature that the approved text does not show. The profile entry behind it is A4 and must be removed or confirmed.

Each divergence is a fault. Fix the profile entry, then clone again. Stop when the divergence list is empty or each remaining item is recorded as a known limit.

The clone is a test, not a chapter. Do not deliver it.

### Stage D: Synthesise

Across the approved passages and any craft texts:

1. **Agreement, conflict, complement.** Where sources agree, the entry strengthens. Where they conflict, classify the conflict as scope, emphasis, method or fact. A common conflict is density: a quiet dialogue chapter and a dangerous chapter should differ. That is scope, not contradiction (protocol section B3).
2. **Governance.** The user's approved passages govern their project. A craft text never overrides them, however respected it is.
3. **Bridge concepts.** Name a concept only when at least two passages support it. Example: a pattern where pressure narrows the sentence length and the thought range at the same time. A bridge concept links subskills 9 and 20 for this project, and it must cite its passages.

### Stage E: Plan

List the profile entries that are ready (tiered A1 or A2, passed the clone test) and the blocked ones (A4, unclear, or failed). List candidate project extensions. A candidate that duplicates subskills 1 to 20 is not added as a new subskill. It becomes a project extension that refines an existing one. The verbatim specification files are never edited to fit a project.

### Stage F: Build

Write the results into the project folder, never into the skill's own `templates/` folder (see section 9):
- `fce-project/style-profile.md` and `style-profile.json` (the profile)
- `fce-project/source-register.md` (sources, coverage, unknowns)
- `fce-project/kaizen-log.md` (what changed, and why)
- project extensions, if any, in `fce-project/extensions.md`

Never edit `references/01-master-system.md`, `02-subskills-01-12.md` or `03-subskills-13-20.md`. Never edit sections A of `04` or `05`.

### Stage G: Rebuild

The final test. Ask for a fresh pass, which can be the user or, if the user asks for one, a fresh agent that has not seen the current profile. Give it only the approved passages and the nine areas, and ask it to describe the style behaviour in the same form.

Compare the rebuilt profile with the current one, entry by entry. Score each entry as:
- reconstructed correctly
- reconstructed with altered meaning
- missing
- invented

Understanding score = entries reconstructed correctly / total entries. Threshold 0.8. Below it, return to Stage B for the misses, then rebuild again. Each altered or invented entry is a negative Kaizen signal.

---

## 4. Recall and precision for absorption

Run both after Stage B.

- **Recall sample.** Take one passage in three, or every passage when there are fewer than three. Count the behaviours in the sample that the profile should capture. Recall = behaviours found in the profile divided by behaviours in the sample. Below 0.8 means Stage B is not finished.
- **Precision sample.** Take five profile entries at random. Check each against its location in the approved text. A mismatch, or an entry the text does not show, is an extraction fault.

---

## 5. Unknowns

Gaps are tracked in `fce-project/source-register.md` with an id (U-001 and so on). Each gap has the question, what evidence would close it, and its status. A gap is closed only with evidence at equal or higher tier than the entry it would settle. A gap the user has not answered stays open. It is not filled with a guess.

---

## 6. Limits of this method

- Two approved passages give a weak profile. Say so, and keep most entries at unclear until a third passage confirms them.
- A profile built from one author's own work reflects that work. If the user wants a change of voice for a new book, that is a new profile, not an edit to this one.
- The clone and rebuild tests are checks on consistency. They do not measure whether the prose is good. The user's reading does that.

---

## 7. Input formats

Accept what the user has. Note the format in the source register.

- **Pasted text.** Use directly. Record the word count.
- **Plain text, Markdown or Word files.** Read the file. Confirm the approved passage boundaries with the user if they are unclear.
- **PDF manuscript or book.** Check the text layer first (see `07`, section 1). For long files, read in chunks and record the chunks. A scanned PDF is read visually and the register says so.
- **URL.** Fetch only if the user supplies it. A page that cannot be fetched is recorded as unavailable, not guessed at.

Approved material should always be pasted or supplied as a file, never recalled. The engine does not reconstruct approved prose from memory.

---

## 8. Layer mapping from the six-layer style analysis

A six-layer style method is useful here, but several of its layers serve persuasion, which is out of scope for fiction. The mapping below keeps what fits and drops what does not.

| Style-analysis layer | Used for | Maps to calibration area | Left out |
|---|---|---|---|
| Surface patterns (formatting, punctuation, vocabulary, sentence length) | Sentence and paragraph behaviour, informality | 2, 8, 9 | Hard word counts. Count only to check a claim, never as the finding. |
| Psychological architecture (emotional arc, motives) | Internal questions, uncertainty, tension | 4, 7 | Persuasion frameworks (AIDA, PAS), scarcity and social-proof triggers, calls to action |
| Subconscious rhythms (short and long alternation, cadence) | Rhythm and paragraph endings | 2, 6 | Alliteration counts, unless a passage shows a pattern a reader would notice |
| Linguistic fingerprints (openers, transitions, fragments, voice) | Person, tense, transitions between action and thought | 1, 6, 8 | Opener tallies as a rule. Use only where the approved text shows a habit. |
| Influence mechanisms (hooks, open loops, callbacks) | Revelation, chapter endings, returning details | 3, 7, 9 (subskills 15, 18) | Marketing hooks |
| Replication blueprint (dos and don'ts) | Profile constraints | All, once tiered | Any rule that copies wording. Rules describe behaviour only. |

The writing-style analysis aims at a reproduction indistinguishable from the original author. This engine's aim is narrower: the profile must describe behaviour well enough to write new scenes that a reader familiar with the approved passages would recognise. It must not copy wording, characters, technologies or scene beats (Master System section 28). Where the two aims conflict, this engine's rule wins.

---

## 9. Project files

The skill's `templates/` folder holds blank forms only. It is never written to during a project. Installed skill folders can be synced or replaced, and a profile stored there would be lost on the next sync, or leak one project's voice into another.

At the first Absorb or Calibrate of a project, copy the four forms into a folder called `fce-project/` beside the manuscript (or in the working directory if there is no manuscript folder), and work only on the copies:

| Form in `templates/` | Working copy | Holds |
|---|---|---|
| `style-profile.md` | `fce-project/style-profile.md` | The human-readable profile |
| `style-profile.json` | `fce-project/style-profile.json` | The same profile, structured, for comparing chapters |
| `source-register.md` | `fce-project/source-register.md` | Sources, coverage, unknowns |
| `kaizen-log.md` | `fce-project/kaizen-log.md` | Every change to the profile, anchors or links |

If `fce-project/` already exists, read it before doing anything else. That is the project's memory.

The JSON file must always match the Markdown file. If they differ, the Markdown file is the one the author last approved, and the JSON is rebuilt from it.

If no folder can be written (a chat with no file access), keep the profile in the conversation, say so, and offer the files at the end for the author to keep.

