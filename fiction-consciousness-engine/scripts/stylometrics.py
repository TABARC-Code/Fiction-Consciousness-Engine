#!/usr/bin/env python3
"""Measure prose so a profile quotes computed figures, never guesses.

    python3 stylometrics.py profile SOURCE.txt [--single-quotes] [--json]
    python3 stylometrics.py compare SOURCE.txt DRAFT.txt [--single-quotes] [--json]

Standard library only. Reports differences, never a similarity score:
none of these figures add up to "how like the author" a passage is.

Known limits, also printed with every report:
  - sentence splitting is a rule of thumb; abbreviations and verse confuse it
  - dialogue is found by quotation marks only
  - under about 2,000 words the figures are indicative, not stable
"""
import json
import re
import statistics
import sys
from collections import Counter

FUNCTION_WORDS = (
    "the a an and but or nor so yet for of in on at to from by with without "
    "into onto over under after before since until while though although "
    "because if unless as than that which who whom whose what when where why "
    "how not no never all some any each every this these those there then "
    "just only even still very quite rather perhaps"
).split()
PUNCT = {
    "comma": ",", "semicolon": ";", "colon": ":", "question": "?",
    "exclamation": "!", "ellipsis": "...", "em_dash": "—",
    "en_dash": "–", "parenthesis": "(",
}
ABBREV = r"(?:Mr|Mrs|Ms|Dr|St|Prof|Sr|Jr|vs|etc|e\.g|i\.e|No|Mt|Capt|Col|Gen|Lt|Sgt)"
WORD = re.compile(r"[A-Za-zÀ-ɏ]+(?:['’][A-Za-z]+)*")
CONTRACTION = re.compile(r"\b[A-Za-z]+['’](?:s|t|re|ve|ll|d|m)\b", re.I)
LIMITS = [
    "Sentence splitting is a rule of thumb. Check a sample of splits on unusual texts.",
    "Dialogue is found by quotation marks only. Unmarked or dashed dialogue is missed, and so is a speech whose closing quote is in a later paragraph.",
    "Line figures describe verse. For prose they just repeat paragraph structure, so ignore them. They show end-stopping, not metre: scan lines by reading them.",
    "Under about 2,000 words these figures are indicative, not stable.",
    "Three-word sequences are for spotting habits. Never reuse them as phrases.",
]


def sentences(text):
    protected = re.sub(ABBREV + r"\.", lambda m: m.group(0).replace(".", "\u0000"), text)
    protected = protected.replace("...", "\u0001")
    parts = re.split(r"(?<=[.!?\u0001])[\"'”’)]*\s+(?=[\"'“‘(]*[A-Z0-9])", protected)
    out = []
    for p in parts:
        p = p.replace("\u0000", ".").replace("\u0001", "...").strip()
        if WORD.search(p):
            out.append(p)
    return out


def dialogue_chars(text, single):
    pats = [r"“[^”]*”", r"\"[^\"]*\""]
    if single:
        pats.append(r"(?<![A-Za-z])‘[^’]*(?:’(?![A-Za-z]))")
        pats.append(r"(?<![A-Za-z])'[^']*'(?![A-Za-z])")
    return sum(len(m) for p in pats for m in re.findall(p, text))


def mattr(words, window=500):
    if not words:
        return 0.0
    if len(words) <= window:
        return len(set(words)) / len(words)
    vals = [len(set(words[i:i + window])) / window for i in range(0, len(words) - window + 1, 50)]
    return statistics.mean(vals)


def pct(values, p):
    if not values:
        return 0
    s = sorted(values)
    return s[min(len(s) - 1, int(round(p / 100 * (len(s) - 1))))]


def line_stats(text):
    """Line-based figures, for verse. Prose lines are paragraphs, so read these
    only when the text is set as verse (many short lines, one stanza per block)."""
    lines = [l for l in text.splitlines() if WORD.search(l)]
    if not lines:
        return {"count": 0}
    lens = [len(WORD.findall(l)) for l in lines]
    stopped = sum(1 for l in lines if l.rstrip().rstrip("\"'\u201d\u2019)").endswith((".", "!", "?", ";", ":", ",")))
    ends_period = sum(1 for l in lines if l.rstrip().rstrip("\"'\u201d\u2019)").endswith((".", "!", "?")))
    return {
        "count": len(lines),
        "mean_words": round(statistics.mean(lens), 1),
        "stdev_words": round(statistics.stdev(lens), 1) if len(lens) > 1 else 0,
        "share_end_stopped": round(stopped / len(lines), 3),
        "share_ending_full_stop": round(ends_period / len(lines), 3),
    }


def profile(text, single=False):
    paras = [p for p in re.split(r"\n\s*\n", text) if WORD.search(p)]
    sents = sentences(text)
    words = [w.lower() for w in WORD.findall(text)]
    n = len(words) or 1
    slen = [len(WORD.findall(s)) for s in sents]
    per_k = lambda c: round(c * 1000 / n, 2)
    para_s = [len(sentences(p)) for p in paras]
    para_w = [len(WORD.findall(p)) for p in paras]
    counts = Counter(words)
    trigrams = Counter(zip(words, words[1:], words[2:]))
    return {
        "words": len(words),
        "sentences": len(sents),
        "paragraphs": len(paras),
        "sentence_length": {
            "mean": round(statistics.mean(slen), 1) if slen else 0,
            "median": statistics.median(slen) if slen else 0,
            "stdev": round(statistics.stdev(slen), 1) if len(slen) > 1 else 0,
            "p10": pct(slen, 10), "p90": pct(slen, 90),
            "share_8_or_fewer": round(sum(1 for x in slen if x <= 8) / (len(slen) or 1), 3),
            "share_30_or_more": round(sum(1 for x in slen if x >= 30) / (len(slen) or 1), 3),
        },
        "paragraph_sentences": {
            "mean": round(statistics.mean(para_s), 1) if para_s else 0,
            "share_single_sentence": round(sum(1 for x in para_s if x == 1) / (len(para_s) or 1), 3),
        },
        "paragraph_words_mean": round(statistics.mean(para_w), 1) if para_w else 0,
        "dialogue_share_of_characters": round(dialogue_chars(text, single) / (len(text) or 1), 3),
        "lines": line_stats(text),
        "mattr_500": round(mattr(words), 3),
        "per_1000_words": {
            **{k: per_k(text.count(v)) for k, v in PUNCT.items()},
            "contractions": per_k(len(CONTRACTION.findall(text))),
        },
        "function_words_per_1000": {w: per_k(counts[w]) for w in FUNCTION_WORDS if counts[w]},
        "top_trigrams": [" ".join(t) + f" ({c})" for t, c in trigrams.most_common(10) if c > 1],
    }


def flat(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            out.update(flat(v, key + "."))
        elif isinstance(v, (int, float)):
            out[key] = v
    return out


def main(argv):
    single = "--single-quotes" in argv
    as_json = "--json" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args or args[0] not in ("profile", "compare") or len(args) < 2:
        print(__doc__)
        return 2
    def read(p):
        try:
            return open(p, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"Cannot read {p}: {e.strerror}", file=sys.stderr)
            sys.exit(1)
    if args[0] == "profile":
        res = profile(read(args[1]), single)
        if as_json:
            print(json.dumps({"file": args[1], "profile": res, "limits": LIMITS}, indent=2))
        else:
            print(f"# Stylometric profile: {args[1]}\n")
            for k, v in flat(res).items():
                print(f"- {k}: {v}")
            if res["top_trigrams"]:
                print("- top_trigrams: " + "; ".join(res["top_trigrams"]))
            print("\nLimits:\n" + "\n".join(f"- {l}" for l in LIMITS))
        return 0
    if len(args) < 3:
        print(__doc__)
        return 2
    a, b = profile(read(args[1]), single), profile(read(args[2]), single)
    fa, fb = flat(a), flat(b)
    rows = [(k, fa[k], fb.get(k, 0), round(fb.get(k, 0) - fa[k], 3)) for k in fa]
    if as_json:
        print(json.dumps({"source": args[1], "draft": args[2],
                          "rows": [dict(metric=k, source=x, draft=y, difference=d) for k, x, y, d in rows],
                          "limits": LIMITS}, indent=2))
    else:
        print(f"# Comparison\n\nSource: {args[1]} ({a['words']} words)\nDraft: {args[2]} ({b['words']} words)\n")
        print("| Metric | Source | Draft | Difference |\n|---|---|---|---|")
        for k, x, y, d in rows:
            print(f"| {k} | {x} | {y} | {d:+} |")
        print("\nDifferences only. No similarity score is given, by design.")
        print("Limits:\n" + "\n".join(f"- {l}" for l in LIMITS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
