# Neighbour patches

Reciprocal link text for other skills. This engine cannot make a link two-way on its own: the other skill's file has to be changed. Each patch below is the text to add to that skill's own SKILL.md, under a heading such as "Related skills". Apply a patch only when that neighbour is present and the user has asked for the change.

Each patch has an id (matches the table in `lattice.md`, section 6.3), a direction, and a status. Status stays "one-way" until the patch is applied, and changes to "two-way" only after the user confirms.

---

## P-NVE: narrative-voice-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: that skill is the stricter gate on close-third voice and free indirect discourse. Use its auditor when a project needs a per-passage score. Do not override its voice rules on a project that has its own style profile.
    Return path: send voice findings from this skill's auditor back here as candidate techniques, not as rules.

## P-PSV: prose-style-voice-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: use this skill's style vocabulary to describe a passage, then test the description against the author's approved passages through the calibration protocol. The approved passages decide, not the vocabulary.

## P-SWE: scene-writing-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: a scene plan from this skill can feed the drafting step. Scene-level continuity and causal checks are handled by subskills 12 and 17 of the consciousness engine.

## P-DSE: dialogue-subtext-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: for dialogue with competing agendas, consult this skill's technique after the consciousness engine has set each speaker's agenda (subskill 6, scene state ledger).

## P-SHE: suspense-horror-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: escalation patterns from this skill can be used, provided they are checked against the cognitive state the consciousness engine sets for the viewpoint character (subskills 8 and 9).

## P-PTE: pacing-time-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: pacing for long scenes can be informed by this skill, within the density target set by subskill 20.

## P-CPE: character-psychology-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: character models from this skill feed the belief ledger (subskill 14) and self-deception (subskill 16). Keep the character model in the ledger, not in the prose.

## P-FSE: fiction-structure-engine

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: structure is decided here first. The consciousness engine then governs each scene inside that structure.

## P-MDO: master-drafting-orchestrator

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: this skill can be called as the prose gate. It returns the revised scene only, with no scores, unless the author asks for them.

## P-HUM: humanizer

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: run only after the consciousness engine's auditor, and only if the author asks for AI-tell detection. It must not change events, facts, dialogue intent or continuity.

## P-BKE: book-knowledge-extraction

Status: one-way until applied.

    Related: fiction-consciousness-engine (present).
    Relationship: when a source is fiction or a craft text on fiction, route it here for the absorption method (references/06) and the craft source analysis (references/07). Return to the extraction routing table any profile the fiction engine builds.
