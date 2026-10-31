#!/usr/bin/env python3
"""Structural checks for fiction-consciousness-engine.

Run from anywhere:  python3 scripts/validate.py
Exit code 0 means every check passed. Anything else lists what broke.

It checks structure, not prose quality. A pass here says the skill is
wired correctly. It says nothing about whether the fiction is any good.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The author's specification text. If any of these change, someone edited
# the verbatim files, which the skill forbids. Update the hash only on a
# deliberate, logged change of specification.
VERBATIM = {
    "references/01-master-system.md":
        "8ff5c2a19e76ef8f5be363419f93f47b69d8f4fe8d179dee497d9de8eb1b8d0d",
    "references/02-subskills-01-12.md":
        "5b5f693f3ee3c9d752e6d27b1021d7e21f62f233d176919ff81dc1fda6158127",
    "references/03-subskills-13-20.md":
        "fd6a57c61f6f37873429cc868f0e87fc5ac44f9f6fad8f1bd3a5b5e2452132c6",
}
SECTION_A = {
    "references/04-style-consistency-auditor.md":
        "eba169e5a21a0d413689fbda8ce20a9bc3ea0be8a54d6eadf01cdeed6a1f8849",
    "references/05-style-calibration-protocol.md":
        "9b10a22f1c604ac32254c9e8449f8760e4797dd6fba38b3d9ea2372acd422b38",
}
ARROWS = re.compile("[←-⇿⟰-⟿⤀-⥿▶►]|->|=>")
PROFILE_AREAS = 9
AUDIT_CATEGORIES = 10
SUBSKILLS = 20

failures = []


def fail(msg):
    failures.append(msg)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


# 1. Verbatim specification unchanged.
for rel, want in VERBATIM.items():
    if sha((ROOT / rel).read_bytes()) != want:
        fail(f"verbatim file changed: {rel}")
for rel, want in SECTION_A.items():
    if sha(read(rel).split("SECTION B:")[0].encode()) != want:
        fail(f"section A changed: {rel}")

# 2. Every file the router names exists.
skill = read("SKILL.md")
for ref in sorted(set(re.findall(r"`((?:references|templates|scripts)/[^`]+)`", skill))):
    if not (ROOT / ref).exists():
        fail(f"SKILL.md names a missing file: {ref}")

# 3. Frontmatter: name matches folder, description within limit.
fm = skill.split("---")[1]
name = re.search(r"^name:\s*(\S+)", fm, re.M)
if not name or name.group(1) != ROOT.name:
    fail("frontmatter name does not match folder name")
desc = " ".join(fm.split("description:", 1)[1].replace(">", "", 1).split())
desc = desc.split(" version:")[0]
if len(desc) > 1024:
    fail(f"description is {len(desc)} characters, limit 1024")

# 4. No arrow glyphs outside the verbatim files.
for path in ROOT.rglob("*"):
    rel = path.relative_to(ROOT).as_posix()
    if path.is_dir() or rel in VERBATIM or rel.startswith("scripts/"):
        continue
    text = path.read_text(encoding="utf-8")
    if rel in SECTION_A:
        text = text.split("SECTION B:", 1)[1]
    for n, line in enumerate(text.splitlines(), 1):
        if ARROWS.search(line):
            fail(f"arrow glyph in {rel} line {n}")

# 5. Counts that must hold.
subs = len(set(re.findall(r"SUBSKILL (\d+) ", read("references/02-subskills-01-12.md")
                          + read("references/03-subskills-13-20.md"))))
if subs != SUBSKILLS:
    fail(f"found {subs} subskill headings, expected {SUBSKILLS}")
index_rows = re.findall(r"^\| (\d+) \|", skill, re.M)
if len(index_rows) != SUBSKILLS:
    fail(f"SKILL.md subskill index has {len(index_rows)} rows, expected {SUBSKILLS}")
card = re.findall(r"^\| (\d+) \|", read("templates/audit-scorecard.md"), re.M)
if len(card) != AUDIT_CATEGORIES:
    fail(f"scorecard has {len(card)} categories, expected {AUDIT_CATEGORIES}")

# 6. Profile: JSON valid and the same nine areas as the Markdown form.
try:
    prof = json.loads(read("templates/style-profile.json"))
    if len(prof["calibration_areas"]) != PROFILE_AREAS:
        fail("style-profile.json does not have nine areas")
except (ValueError, KeyError) as exc:
    fail(f"style-profile.json invalid: {exc}")
md_areas = re.findall(r"^\d\. \*\*", read("templates/style-profile.md"), re.M)
if len(md_areas) != PROFILE_AREAS:
    fail(f"style-profile.md has {len(md_areas)} areas, expected {PROFILE_AREAS}")

# 7. Neighbour table and patches agree.
lattice = read("references/lattice.md")
patches = read("references/neighbour-patches.md")
for pid in sorted(set(re.findall(r"\| (P-[A-Z]+) \|", lattice))):
    if f"## {pid}:" not in patches:
        fail(f"lattice names patch {pid} but neighbour-patches.md has no entry")
for pid in re.findall(r"^## (P-[A-Z]+):", patches, re.M):
    if f"| {pid} |" not in lattice:
        fail(f"neighbour-patches.md has {pid} but the lattice table does not")

# 8. Project data must never be written into the skill's blank forms.
WRITE_TO_FORM = re.compile(
    r"(?:in|into|to) `templates/(?:style-profile|source-register|kaizen-log"
    r"|author-dossier|book-blueprint|manuscript-continuity-ledger)")
for path in (list(ROOT.glob("*.md")) + list((ROOT / "references").glob("*.md"))
             + list((ROOT / "subskills").rglob("*.md"))):
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        # Naming the blank form is fine when the same line names its project copy.
        if WRITE_TO_FORM.search(line) and "Never write" not in line and "fce-project/" not in line:
            fail(f"writes project data into a blank form: "
                 f"{path.relative_to(ROOT).as_posix()} line {n}")

# 9. No personal identity in shipped documentation.
for rel in ["SKILL.md", "README.md", "description.md"]:
    if re.search(r"TABARC|Blackwood|@gmail", read(rel), re.I):
        fail(f"identity string in {rel}")

# 10. Subskills: required sections, and every one registered in SKILL.md.
SUB = ROOT / "subskills"
REQUIRED = ["## Purpose", "## Activation", "## Procedure", "## Outputs",
            "## Quality test", "## Failure modes", "## Signals", "## Contract"]
sub_dirs = sorted(p for p in SUB.iterdir() if p.is_dir()) if SUB.exists() else []
for d in sub_dirs:
    f = d / "SUBSKILL.md"
    if not f.exists():
        fail(f"subskill folder without SUBSKILL.md: {d.name}")
        continue
    body = f.read_text(encoding="utf-8")
    for h in REQUIRED:
        if h not in body:
            fail(f"{d.name}: missing section '{h}'")
    if f"`subskills/{d.name}/SUBSKILL.md`" not in skill:
        fail(f"{d.name} is not registered in SKILL.md")

# 11. Contracts: reciprocal, bidirectional, not mirrored, known nodes only.
STRENGTHS = {"critical", "strong", "moderate", "weak", "contextual", "optional"}
nodes, sends, recvs = {}, {}, {}
contract_files = [d / "SUBSKILL.md" for d in sub_dirs] + [SUB / "_engine-nodes.md"]
for f in contract_files:
    if not f.exists():
        fail(f"missing contract file: {f.relative_to(ROOT).as_posix()}")
        continue
    for blockm in re.finditer(r"```contract\n(.*?)```", f.read_text(encoding="utf-8"), re.S):
        lines = blockm.group(1).strip().splitlines()
        if not lines or not lines[0].startswith("node: "):
            fail(f"contract block without a node line in {f.name}")
            continue
        node = lines[0][6:].strip()
        if node in nodes:
            fail(f"node declared twice: {node}")
        nodes[node] = f
        for ln in lines[1:]:
            m = re.match(r"(sends|receives): ([a-z-]+) \| ([a-z]+) \| (.+)$", ln)
            if not m:
                fail(f"{node}: malformed contract line: {ln}")
                continue
            kind, other, strength, what = m.groups()
            if strength not in STRENGTHS:
                fail(f"{node}: unknown strength '{strength}'")
            (sends if kind == "sends" else recvs)[(node, other)] = (strength, what.strip())
for d in sub_dirs:
    if d.name not in nodes:
        fail(f"subskill {d.name} has no contract block")
for (a, b), (st, what) in sends.items():
    if b not in nodes:
        fail(f"{a} sends to unknown node {b}")
        continue
    got = recvs.get((b, a))
    if not got:
        fail(f"one-way link: {a} sends to {b}, but {b} does not list it as received")
    elif got != (st, what):
        fail(f"contract mismatch: {a} to {b} differs between sender and receiver")
    back = sends.get((b, a))
    if not back:
        fail(f"no return path: {a} sends to {b}, {b} sends nothing back")
    elif back[1] == what:
        fail(f"mirrored contract: {a} and {b} send each other the same thing")
for (b, a) in recvs:
    if (a, b) not in sends:
        fail(f"{b} claims to receive from {a}, but {a} sends nothing")

# 13. Section references such as "04, B11" point at notes that exist.
NOTE_FILES = {"04": "references/04-style-consistency-auditor.md",
              "05": "references/05-style-calibration-protocol.md"}
CITE = re.compile(r"`(?:references/)?(0[45])(?:-[a-z-]+\.md)?`,? (?:B|section B)(\d+)")
for path in [ROOT / "SKILL.md"] + list((ROOT / "references").glob("*.md")) + list(SUB.rglob("*.md")):
    for num, b in CITE.findall(path.read_text(encoding="utf-8")):
        if not re.search(rf"^B{b}\. ", read(NOTE_FILES[num]), re.M):
            fail(f"{path.relative_to(ROOT).as_posix()} cites {num} B{b}, which does not exist")

# 12. Scripts run.
import subprocess
import tempfile
sample = ('"You\'re early," said Dev. He did not open the door. '
          'Mara waited on the step, and the rain ran off the roof.\n\nShe left.\n')
with tempfile.TemporaryDirectory() as tmp:
    src = Path(tmp) / "s.txt"
    src.write_text(sample, encoding="utf-8")
    prof = Path(tmp) / "p.md"
    prof.write_text("## The nine calibration areas\n   - P-001 Vivid imagery throughout.\n",
                    encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-I", *a], capture_output=True, text=True)
    r = run(str(ROOT / "scripts/stylometrics.py"), "compare", str(src), str(src), "--json")
    try:
        if r.returncode or json.loads(r.stdout)["rows"][0]["difference"] != 0:
            fail("stylometrics.py compare did not run cleanly")
    except (ValueError, KeyError, IndexError):
        fail("stylometrics.py produced unreadable output")
    if run(str(ROOT / "scripts/profile_lint.py"), str(prof)).returncode != 1:
        fail("profile_lint.py did not flag a generic, untiered entry")
    good = Path(tmp) / "g.md"
    good.write_text("## The nine calibration areas\n   - P-001 Distance closes to immediate when a lie is "
                    "suspected, and reflective clauses drop out. A2, S-001 para 4.\n", encoding="utf-8")
    if run(str(ROOT / "scripts/profile_lint.py"), str(good)).returncode != 0:
        fail("profile_lint.py rejected a specific, tiered, located entry")
    verse = Path(tmp) / "v.txt"
    verse.write_text("Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\n"
                     "Rough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date.\n",
                     encoding="utf-8")
    rv = run(str(ROOT / "scripts/stylometrics.py"), "profile", str(verse), "--json")
    try:
        if json.loads(rv.stdout)["profile"]["lines"]["count"] != 4:
            fail("stylometrics.py miscounted verse lines")
    except (ValueError, KeyError):
        fail("stylometrics.py gave no line statistics")
    dashes = Path(tmp) / "d.txt"
    dashes.write_text("He waited--and then he spoke----slowly.\n\n---\n\nNothing more was said.\n", encoding="utf-8")
    rd = run(str(ROOT / "scripts/stylometrics.py"), "profile", str(dashes), "--json")
    try:
        pd = json.loads(rd.stdout)["profile"]
        # two hyphen runs in the prose, the rule line left out: 2 dashes in 11 words = 181.82 per 1,000
        if pd["per_1000_words"]["hyphen_run_dash"] != 181.82 or pd["per_1000_words"]["em_dash"] != 0:
            fail("stylometrics.py miscounted hyphen-run dashes")
    except (ValueError, KeyError):
        fail("stylometrics.py gave no hyphen-run dash figure")
    if run(str(ROOT / "scripts/profile_lint.py"), str(ROOT / "templates/style-profile.md")).returncode != 0:
        fail("the blank profile form does not lint clean: form and linter have drifted")

if failures:
    print(f"FAILED: {len(failures)} problem(s)")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("PASSED: all structural checks")
