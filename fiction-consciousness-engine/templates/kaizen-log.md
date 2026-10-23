# Kaizen log

One entry per change to the profile, the anchors, the links or the skill itself. Dated, short, specific. Each entry names the signal that caused it.

Notation:
- (+) positive evidence: approved, accepted, praised
- (-) negative evidence: rejected, rewritten, complained about
- (?) unclear evidence: a signal that might mean either
- (=) reviewed and left unchanged

Rules:
- Log only what the user said or did, or a result the engine measured. Never log an inferred preference as the user's.
- A change is kept if the next two runs show a positive signal and no repeat of the same negative signal.
- A change that produces the same negative signal twice is reverted, and that revert is logged.

Format:

    YYYY-MM-DD | area | mark | signal | cause | change | metric before, then metric after | status (keep / pending / reverted)

Example (illustrative, not a real run):

    2026-10-23 | auditor cat 8 | (-) | author rejected a chapter for even rhythm | anchor allowed a repeated template | anchor note now asks for variation check across three paragraphs | none measured | pending

Write metrics as "before, then after". Do not use arrow glyphs anywhere in the skill.
