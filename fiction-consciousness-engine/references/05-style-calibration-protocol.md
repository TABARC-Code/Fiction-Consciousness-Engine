PERMANENT STYLE CALIBRATION PROTOCOL

Status: permanent. Applies to every writing project this skill touches.

---

SECTION A: THE PROTOCOL (VERBATIM)

PERMANENT STYLE CALIBRATION PROTOCOL

At the beginning of a writing project, analyse approved reference material for transferable narrative characteristics, including:

- Narrative distance and viewpoint consistency.
- Typical sentence and paragraph variation.
- Balance of action, dialogue, reasoning and exposition.
- Frequency and purpose of internal questions.
- Methods of introducing character history.
- Transitions between physical action and reflection.
- Development of uncertainty and psychological tension.
- Degree of conversational informality.
- Handling of technical and environmental detail.

Create an internal style profile describing these craft characteristics without copying distinctive wording or story elements.

Treat original passages approved by the user as the primary calibration reference for subsequent writing.

For every substantial new chapter:

Draft: Apply the master instructions, subskills and story context.

Compare: Examine whether the chapter maintains the approved narrative characteristics. Look for genuine differences in technique, not just vocabulary.

Revise: Correct significant stylistic drift, inconsistencies and mechanical prose while preserving natural variation.

Preserve: Do not unnecessarily change passages that are already effective.

Do not force every chapter into identical structural proportions.

Maintain consistency at the level of narrative consciousness, characterisation and prose behaviour rather than through repeated formulas.

Output only original finished fiction unless the user requests a critique.

---

SECTION B: OPERATING NOTES

Section A is the law. Section B explains how to carry it out.

B1. Starting a project: build the style profile

1. Check for approved reference material. That means passages the user has approved, original passages they wrote, or reference fiction they named as a craft model.
2. If there is none, say so in one line and start from the Master System defaults. Do not invent a profile out of nothing and present it as calibrated.
3. If there is some, read it closely and fill the project's working copy of the profile (`fce-project/style-profile.md`, copied from `templates/`; see `06`, section 9), covering the nine areas listed above.
4. Describe behaviour, not wording. "Internal questions run in clusters of two or three when the character is cornered, then drop away for pages" is a profile entry. A quoted sentence is not. Never copy distinctive phrases, characters, technologies or plot beats from reference fiction (Master System section 28).
5. Where the evidence is thin, write "unclear" in that field. A blank is better than a guess. A wrong profile entry is worse than a missing one, because later chapters will be bent to fit it.
6. Keep the profile internal. Show it only if the user asks for a critique.

B2. Reference hierarchy

1. Passages the user has approved (primary calibration reference, per Section A), including approved chapters the engine wrote.
2. Established story facts and continuity.
3. The active reconstructed author profile, when the user has chosen to write in an author's manner (author dossier subskill).
4. The Master System and the twenty subskills.
5. External reference fiction, for broad craft principles only.

The generation contract (premise, characters, structure, length) governs what is written. This hierarchy governs how.

If an approved passage appears to break a Master System rule, the approved passage still sets the calibration, but flag the tension to the user once, briefly, when it matters for the work. Do not silently "fix" approved prose.

B3. The chapter loop

For every substantial new chapter, run these four steps in order.

Draft. Apply the Master System, the subskills that fit the scene type, the story context and the profile.

Compare. Hold the draft against the profile and against approved passages. Look for real technique differences: narrative distance creeping outward, internal reasoning turning tidy, exposition going encyclopaedic, dialogue tags multiplying, suspense turning formulaic. Vocabulary alone is not drift.

Revise. Fix significant drift and mechanical prose. Then run the Style Consistency Auditor (04-style-consistency-auditor.md) as the gate.

Preserve. Anything effective stays untouched.

Do not force chapters into matching proportions. A quiet dialogue chapter and a danger chapter should differ in density (Subskill 20). What stays constant is the consciousness, the characterisation and the way the prose behaves.

B4. Updating the profile

The profile is living, not fixed. When the user approves a new passage, check whether it shows a characteristic the profile missed or got wrong. If so, amend the entry. If the user rejects or heavily rewrites a passage, treat that as negative evidence about whichever entry produced it. See the feedback loops in lattice.md.

B5. Testing the profile

A profile is not trusted because it looks sensible. It is tested.

- **Clone test.** Write a neutral passage of about 400 to 600 words from a fresh scene plan, using only the profile. Compare it with the approved passages. Divergences are faults. Fix the profile entry and clone again. Method in `06`, stage C.
- **Rebuild test.** Ask for a fresh pass that reads only the approved passages and describes the nine areas. Compare it entry by entry with the current profile. Understanding score below 0.8 returns the profile to Stage B. Method in `06`, stage G.
- **Source register.** Every profile entry names its passage in `fce-project/source-register.md`. An entry with no passage is A4 and is not used to write prose.

B6. Output

Original finished fiction only. A critique only when the user asks for one.
