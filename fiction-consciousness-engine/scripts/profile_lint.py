#!/usr/bin/env python3
"""Reject style-profile entries that are generic, untiered or unlocated.

    python3 profile_lint.py fce-project/style-profile.md

An entry is any bullet line under the nine areas that says more than its
own label. Exit 0 when clean, 1 when there is something to fix.
"""
import re
import sys

# Phrases that fit half of all writers. An entry built on one of these says
# nothing a writer can act on. Extend the list from your own kaizen log.
GENERIC = [
    "varied sentence length", "uses varied sentence", "conversational tone",
    "balances formal and informal", "engages the reader", "creates a sense of",
    "vivid imagery", "rich prose", "rich description", "strong voice",
    "unique voice", "distinctive voice", "flows well", "flows naturally",
    "captures the essence", "writes beautifully", "evocative", "immersive",
    "compelling", "well-paced", "nuanced", "draws the reader in",
]
TIER = re.compile(r"\bA[1-4]\b")
LOCATION = re.compile(r"\b(?:S-\d+|U-\d+|ch(?:apter)?\.?\s*\d+|p\.?\s*\d+|para(?:graph)?\s*\d+|sample\s*\d+)", re.I)
# A form field: a label ending in a colon, left blank or "unclear". Labels may hold colons.
FIELD_ONLY = re.compile(r"^\s*-\s*.+:\s*(?:unclear)?\s*$", re.I)


def lint(text):
    problems = []
    in_areas = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## The nine calibration areas"):
            in_areas = True
            continue
        if in_areas and line.startswith("## "):
            in_areas = False
        if not in_areas or not line.lstrip().startswith("-") or FIELD_ONLY.match(line):
            continue
        low = line.lower()
        hits = [g for g in GENERIC if g in low]
        if hits:
            problems.append(f"line {n}: generic phrase '{hits[0]}': say what the writer does, when, and where it is seen")
        if not TIER.search(line):
            problems.append(f"line {n}: no tier (A1 to A4)")
        if not LOCATION.search(line):
            problems.append(f"line {n}: no location (source id, chapter, page, paragraph or sample)")
    return problems


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    problems = lint(open(argv[0], encoding="utf-8").read())
    if problems:
        print(f"{len(problems)} problem(s) in {argv[0]}:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"clean: {argv[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
