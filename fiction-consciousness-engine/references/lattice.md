LATTICE: LINKS, FEEDBACK LOOPS AND IMPROVEMENT NOTATION

Purpose: record how the parts of this skill depend on one another, how information moves between them in both directions, how ideas from one subskill feed another, and how the skill gets better with use. This file is engineering, not instruction to the prose. Nothing here changes the Master System or the twenty subskills. It only wires them together.

---

1. DESIGN PRINCIPLES

Sequential thinking. The workflow in SKILL.md runs in order, each step reading what the previous one produced.

Bidirectional information flow. Every forward link has a named return path. A scene that fails the auditor sends information back to the ledger or to the scene plan, not just to a rewrite.

Cross-fertilisation. Subskills are not silos. Several share evidence and inform each other's quality tests. The pairs are listed below.

Constant improvement through feedback loops. Positive and negative feedback both change what the skill does next time. The loops are written out in section 4.

---

2. FORWARD AND RETURN LINKS (WORKFLOW)

Forward means "this step feeds that step". Return means "this step may send information back".

| From | Forward to | Return path from the later step |
|---|---|---|
| Intake | Calibrate | Calibrate reports missing reference material back to intake, so the user can be asked once |
| Calibrate (profile) | Draft | Compare step reports technique drift back to the profile, to amend or confirm entries |
| Scene state (ledger) | Draft | Auditor category 10 failures return to the ledger: the ledger was wrong or stale, not just the prose |
| Subskill selection | Draft | Craft review returns "this subskill did not belong here" so the selection can shrink |
| Draft | Craft review | Craft review returns specific passages, not general notes |
| Craft review | Auditor | Auditor returns scores below 4 as targeted revision tasks |
| Auditor | Delivery | User reaction returns through Step 8 into the profile |

---

3. CROSS-FERTILISATION BETWEEN SUBSKILLS

Each pair below is a two-way edge. Evidence or technique flows both directions. Weight is a rough guide to how often the pair should be considered together: strong, medium, light.

| Pair | Weight | What flows A to B | What flows B to A |
|---|---|---|---|
| 1 Consciousness and 2 Inference | strong | The character's expertise decides what they notice | The inference chain shows what the character does and does not know |
| 1 Consciousness and 3 Association | strong | Background decides which memory fires | The memory reveals fears and worldview, refining the character model |
| 1 Consciousness and 16 Self-deception | strong | What the character avoids thinking about | Self-deception explains selective attention |
| 1 Consciousness and 13 Distance | strong | The character's attention sets the distance | Distance level shows how much of the consciousness is exposed |
| 2 Inference and 14 Belief tracking | strong | Each conclusion is logged as belief, not fact | The ledger tells inference what the character may legitimately conclude |
| 2 Inference and 5 Object intelligence | medium | Reasoning needs a concrete physical detail | Practical knowledge generates the anomaly that starts reasoning |
| 3 Association and 18 Recurring detail | medium | Memories can seed a recurring detail | A recurring detail changes the memory's meaning later |
| 4 Exposition and 10 Institutional subtext | medium | Exposition carries social attitude | Institutional detail gives exposition a reason to exist |
| 4 Exposition and 14 Belief tracking | medium | Exposition marks what the character is sure of and unsure of | The ledger stops exposition overclaiming |
| 5 Object intelligence and 8 Suspense | strong | Wrong-looking equipment supplies practical dread | Rising pressure decides which object details matter |
| 6 Dialogue agendas and 16 Self-deception | strong | What a speaker will not say | Self-justification shows up in how they talk |
| 6 Dialogue agendas and 7 Interruption | light | Interruptions are agenda moves | Interrupted thoughts leave dialogue unresolved |
| 7 Interruption and 9 Pressure | medium | Interruption pattern shows stress | Stress level changes how thoughts break |
| 8 Suspense and 15 Revelation | strong | Escalation steps decide when clues land | Revealed information resets escalation |
| 8 Suspense and 9 Pressure | strong | Danger level sets cognitive mode | Cognitive state limits what escalation the character can process |
| 11 Rhythm and 19 Transitions | strong | Rhythm shapes where thought shifts occur | Smooth transitions stop rhythm turning into a template |
| 11 Rhythm and 20 Density | medium | Sentence length follows density | Density decides how long paragraphs run |
| 12 Continuity and 14 Belief tracking | strong | Physical facts feed the confirmed-facts list | Beliefs explain odd but consistent character actions |
| 12 Continuity and 17 Causality | strong | State of the world constrains possible actions | Consequences update the state |
| 15 Revelation and 18 Recurring detail | medium | Clues can recur | Meaning evolution re-reads old clues |
| 17 Causality and 16 Self-deception | medium | Decisions have consequences | Consequences pressure self-deception |
| 9 Pressure and 20 Density | medium | Stress level selects density | Density constraints show how much the character can process |

Master System links. Each numbered Master System section maps to subskills that implement it in more detail. The mapping is deliberately loose, because the specification itself says these are tendencies, not formulas.

- Part I (voice): Subskills 1, 13, 19.
- Part II (cognition): Subskills 2, 3, 14, 16.
- Part III (prose and rhythm): Subskills 11, 20.
- Part IV (world-building): Subskills 4, 5, 10.
- Part V (dialogue and relationships): Subskills 6, 16.
- Part VI (suspense and horror): Subskills 7, 8, 9, 15.
- Part VII (pacing and structure): Subskills 12, 17, 20.
- Part VIII (originality and anti-formula): Subskills 11, 18, 19 and the calibration protocol.
- Part IX (quality control): the Style Consistency Auditor.

---

4. FEEDBACK LOOPS

4.1 Positive loop (reinforcement)

Trigger: the user approves a passage, accepts a draft without edits, or says something specific worked.

1. Identify which characteristics the passage shows: distance level, rhythm behaviour, reasoning pattern, exposition handling, dialogue differentiation, and so on.
2. Compare against the style profile. If the profile already records it, mark the entry as confirmed. If not, add it.
3. Treat the approved passage as primary calibration reference (protocol, Section A).
4. Note which subskills were leading in the scene. Record the pairing as (+) in `fce-project/kaizen-log.md`. A pairing with three (+) marks on one project is treated as strong for that project, whatever the table above says. The table itself is not edited for one project.

4.2 Negative loop (correction)

Trigger: the user rejects a passage, rewrites heavily, says it "doesn't sound right", or flags drift.

1. Find the cause in the data, not in guesswork. Ask the user only if the passage gives no clue. One short question.
2. Ask why, up to five times, and stop at the first answer that names a step the engine can change. Example:
   - The author rewrote the chapter. Why? It "didn't sound like her".
   - Why? The narration explained the character's feelings.
   - Why? Distance drifted to reflective during the argument scene.
   - Why? The ledger set pressure to "calm", so subskill 13 allowed distance.
   - Why? The ledger was not updated after the previous scene's injury.
   - Stop: the ledger is a step the engine can change. That is the fix, not the prose.
3. Name the auditor category the fault would show in (voice, rhythm, exposition, continuity, and so on). If the auditor scored that category 4 or above, the auditor missed it: run judge calibration (`04`, B7) on that passage.
4. Fix the step the why-chain found, for this project. Do not just patch the prose.
5. Mark the offending profile entry as doubtful or amend it.
6. Log the chain and the fix in `fce-project/kaizen-log.md`.
7. If the same fault appears twice, note it as a recurring failure and check the auditor's anchors for that category.

4.3 Drift loop (automatic)

Trigger: every substantial new chapter (protocol B3).

Draft, compare against profile and approved passages, revise, preserve. Information returns to the profile if the comparison finds an approved technique has legitimately evolved.

4.4 Audit-calibration loop

Trigger: the auditor scores a long run of passages at the same high or low value.

Re-read more slowly. A scorer that never varies is not scoring. See B6 in the auditor file.

4.5 Verification loop (plan, do, check, act)

Every change made by loops 4.1 to 4.4 is a hypothesis until the next chapters test it. A fix that is never checked is a guess that has been written down.

- **Plan.** Write the change and the signal it should produce. Example: "Ledger now updated after every scene that changes injuries. Expect: no continuity rewrites from the author in the next two chapters."
- **Do.** Apply the change to the next chapter only.
- **Check.** After each of the next two chapters, record whether the expected signal appeared.
- **Act.** Two positive results with no repeat of the original fault: keep, and mark it (+) in the log. The same fault twice: revert the change, mark it (-), and run the why-chain again from the start. Mixed or no signal: keep it as pending and say so if asked. Do not claim a fix worked without the check.

One change at a time per area. Two changes to the same profile area in the same chapter make the check impossible, because a good or bad result cannot be traced to either.

---

5. IMPROVEMENT NOTATION

Every skill in this family is treated as constantly improving. Notation used when the skill itself is revised:

- (+) positive evidence: approved, accepted, praised
- (-) negative evidence: rejected, rewritten, complained about
- (?) unclear evidence: a signal that might mean either
- (=) unchanged: reviewed and left alone

Log lines are short, dated and specific:

    2026-10-17 | Auditor cat 8 | (=) | anchors unchanged, first build
    2026-10-17 | Calibration | (=) | first build, no approved passages yet

Never log inferred preferences as facts. Only what the user said or did goes in with a (+) or (-).

---

6. NEIGHBOURS: DISCOVERED AT RUNTIME, LINKED BOTH WAYS

6.1 Discovery rule

The engine does not assume which neighbours exist. At Step 0 it checks the installed skill list in the current environment. It links only to skills that are present. A missing neighbour is not an error. It is recorded as "not present" and the link is skipped. This keeps the skill portable: on another person's system, the same rules apply to whatever they have installed.

6.2 Two-way rule

Every active link has a forward contract (this skill to the neighbour) and a reciprocal contract (the neighbour to this skill). This skill can write its own side. The neighbour's side needs its own skill file to be changed. Where the engine cannot change a neighbour, it writes the reciprocal text into `references/neighbour-patches.md`, labelled with the link's status. The link is one-way until the patch is applied. The engine says so when the link matters, and never claims a two-way link that has not been written on both sides.

6.3 Neighbour table

Status key: present means it appeared in the installed skill list checked when this version was built. Not present means it did not. Re-check on each new system.

| Neighbour | Status at 2.0.0 | Overlap | Forward (this to neighbour) | Return (neighbour to this) | Weight | Patch id |
|---|---|---|---|---|---|---|
| narrative-voice-engine | present | Part I, subskills 1 and 13 | This is the stricter gate on voice | Supplies voice principles to absorb (`06`) | strong | P-NVE |
| prose-style-voice-engine | present | Calibration area 1, 8 | Profile comparison only, never overrides the profile | Supplies style vocabulary for the profile to test against | moderate | P-PSV |
| scene-writing-engine | present | Scene development, subskill 17 | Scene plan can come from it | This engine returns craft review on its scenes | moderate | P-SWE |
| dialogue-subtext-engine | present | Subskill 6 | Supplies dialogue technique for scenes with competing agendas | This engine returns agenda findings | moderate | P-DSE |
| suspense-horror-engine | present | Subskills 8 and 9 | Supplies escalation patterns | This engine returns cognitive-state limits | moderate | P-SHE |
| pacing-time-engine | present | Subskills 11 and 20 | Supplies pacing for long scenes | This engine returns density findings | light | P-PTE |
| character-psychology-engine | present | Subskills 3 and 16 | Supplies character models for the ledger | This engine returns self-deception findings | moderate | P-CPE |
| fiction-structure-engine | present | Sits above this engine | Structure is decided first | This engine returns scene-level constraints | strong | P-FSE |
| master-drafting-orchestrator | present | Could call this as its prose gate | Calls this engine for the gate | Receives scene results | moderate | P-MDO |
| humanizer | present | AI-tell detection after the auditor | Runs after the auditor, only if the author wants it | Returns tells it found; never overrides continuity rules | light | P-HUM |
| book-knowledge-extraction | present | Absorption method (`06`) and analysis (`07`) derive from it | Receives reference sources for fiction | Supplies stage method | strong | P-BKE |
| golden-age-author, military-gothic-voice, historical-fiction-master, western-fiction, speculative-fiction-writer | present | Genre neighbours | Consulted for period or genre texture only, if the project needs it | Receives scene requests | contextual | none needed |
| anti-slop-engine, overwatch-prose-audit, weird-prose-forensics, pulp-autopsy, plot-paradigms-engine | not present in the list checked | Several | Not linked | Not linked | none | none |

Rules for the table:
- The engine links to a neighbour only when its row says present for the current system.
- A genre neighbour never sets the profile. It is consulted for texture only, when the project asks.
- If a neighbour's advice conflicts with the Master System or the auditor, the Master System and the auditor win.

6.4 Patch application

`references/neighbour-patches.md` holds the reciprocal text for each patch id. The user applies it to the neighbour's own skill. The engine does not edit another skill unless the user asks, and only then after reading that skill in full.

---

8. SUBSKILL GRAPH

8.1 What the graph is

Nine subskills (`subskills/`) and seven engine nodes (`subskills/_engine-nodes.md`). Each node's file holds a contract block listing everything it sends and receives. There is no separate edge list to drift out of date: the contract blocks are the graph.

8.2 Rules

- **Every link runs both ways.** If A sends to B, B lists it as received, and B sends something back to A.
- **The reciprocal is not a mirror.** What comes back is what the receiver learned, not an echo. Corpus intelligence sends text to stylometrics; stylometrics sends back the extraction faults its numbers exposed.
- **Strength can differ by direction.** Text into stylometrics is critical. Fault reports back are moderate.
- **Enforced, not trusted.** `scripts/validate.py` fails on a one-way link, a missing return, a mirrored reciprocal, a sender and receiver that disagree, or an unknown node.

8.3 The four flows

**Reconstruction.** Corpus intelligence feeds contrast extraction, both forensic subskills, the form specialist and stylometrics. They feed the author dossier, which writes the profile. The validator tests it. Return paths: the dossier sends gaps back to the forensic subskills, they send re-read requests back to corpus intelligence, and stylometrics sends extraction faults back to the corpus. A weak profile is traced back to the text, not patched at the top.

**Writing.** The manuscript architect hands canon to the scene ledger and the contract to drafting. Drafting goes to the auditor, then the validator. Return paths: the ledger's end state goes back into canon, the auditor sends revision tasks back to drafting, and the validator sends drift reports back to the architect.

**Feedback.** The author's verdict reaches the profile and the validator. Return paths: the profile names the entries behind a rejected passage, the dossier sends those back to the forensic subskill that produced them, and the validator logs every passage it passed that the author rejected.

**Measurement.** Forensics and stylometrics, and the validator and stylometrics, exchange hypotheses and measurements. A hypothesis the numbers contradict is revised, not defended.

8.4 Cross-fertilisation worth knowing

- Character and narrative forensics tunes drafting subskills 1, 3, 6 and 13 to 18 for one author, and drafting reports back which tuned quality tests failed. This is how a reconstructed voice reaches the engine without editing the specification.
- The form specialist changes which auditor categories apply, and the auditor's scores show whether the change was right.
- Book analysis and corpus intelligence share inventory and coverage, so an analysis report and a later reconstruction start from the same record.
- Contrast extraction and stylistic forensics trade hypotheses and differences. Each makes the other more specific.

8.5 Adding or changing a subskill

1. Write `subskills/<name>/SUBSKILL.md` with the eight required sections.
2. Write its contract block. For every send, add the matching receive, and a return, in the other node's file.
3. Register it in the subskill table in `SKILL.md`.
4. Run `scripts/validate.py` until it passes.
5. Log the change in section 9, with the signal that justified it.

8.6 Pruning (just in time)

An edge that carries nothing during a whole project is noted in `fce-project/kaizen-log.md` as idle. An edge idle across two projects is a candidate for removal, both sides together. A subskill earns its place by the signals it produces, not by being written down.

---

9. CHANGE LOG

    2026-10-17 | v1.0.0 | First build from the three supplied specification documents plus the Style Consistency Auditor and Permanent Style Calibration Protocol.
    2026-10-23 | v2.0.0 | Merged with the book-knowledge-extraction method (absorption, clone and rebuild tests, source register, unknowns). Added craft source analysis (07), a companion JSON profile, a six-layer style analysis mapped to the nine calibration areas (writing-style-extractor, MIT, credited in LICENCE-NOTICE.md), judge calibration for the auditor, runtime neighbour discovery with two-way contracts, and neighbour patches. Removed the author byline and personal anecdotes from README and description. Verbatim specification files unchanged.
    2026-10-23 | v2.1.0 | Kaizen pass. Added scripts/validate.py (verbatim hashes, file references, arrows, counts, patch table, identity, template writes), tested against injected faults. Project data now lives in fce-project/, never in the skill's blank forms. Clone test runs only when the profile changes. Absorb mode reports a short status. Uncalibrated judge has a defined fallback. Negative loop gains a why-chain; new verification loop (4.5) checks each fix over two chapters. One changelog, here.
    2026-10-23 | v3.0.0 | Author reconstruction and manuscript system. Nine subskills with two-way contract blocks, enforced by validate.py (one-way links, missing returns, mirrored reciprocals, unknown nodes, dangling section citations). Built from the user's expanded book-intelligence specification, rewritten and restructured, and a contrast method from a voice-extraction skill. Added stylometrics.py (computed measures, differences only) and profile_lint.py (generic-phrase gate). New templates: author dossier, book blueprint, continuity ledger. Auditor B11 (verse and drama) and B12 (reconstructed voices). Source hierarchy extended in 05 B2. Frame D in 07. Router rewritten with seven modes. Thin-evidence threshold now three samples and 500 words.
    2026-10-23 | v3.0.1 | Test and script gaps. profile_lint.py now has a positive test (a specific, tiered, located entry must pass), proved by mutation: a linter that rejects everything is caught. stylometrics.py gains line statistics for verse (line length, end-stopping) with notes that it cannot scan metre. Dialogue limit widened to name speeches that run across paragraphs. SICO citation made exact in LICENCE-NOTICE.md after checking the source. Earlier claim that stylometrics figures were hand-checked was made before the check; checked afterwards on one 132-word passage (words, sentences, paragraphs, commas all agree).
    2026-10-23 | v3.0.2 | Kaizen pass on the packaged build. stylometrics.py now reports a missing or unreadable file in one line with exit 1, not a traceback. Versions aligned. No change to verbatim specification, auditor, protocol or subskill contracts.
    2026-10-23 | v3.0.3 | Double-check pass. Corrected two false statements: that one arrow in the specification had been replaced (none had; files 01 to 03 are byte-identical to the upload, checked against the uploaded zip), and the router's note on that. Section A of 04 and 05 confirmed byte-identical to the upload. Versions aligned.
