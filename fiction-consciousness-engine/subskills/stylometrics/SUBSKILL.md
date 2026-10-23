# Stylometrics

Measures what can be measured, using a script, so numbers in a profile are computed, never estimated.

## Purpose

Interpretation finds the patterns. Measurement checks them. A claim such as "sentences shorten in action scenes" can be tested in seconds. A claim such as "95 per cent like the author" cannot be tested at all, and is never made.

## Activation

Whenever stylistic forensics has a measurable hypothesis, whenever a draft is compared with its source, and during the reconstruction validator's tests. Needs Python 3 and a text file. No extra packages.

## Procedure

1. Get clean primary-author text from corpus intelligence. Editorial matter skews every number.
2. Run the script:

       python3 scripts/stylometrics.py profile SOURCE.txt
       python3 scripts/stylometrics.py compare SOURCE.txt DRAFT.txt

   Add `--single-quotes` when the text marks dialogue with single quotation marks (common in British editions). Add `--json` for structured output.
3. Read the results against the hypothesis. Report what was measured, on how many words, and what it means for the hypothesis: confirmed, qualified or contradicted.
4. Record measured figures in the profile with tier A1 and the file and word count they came from.

## What the script measures

Words, sentences and paragraphs; sentence length (mean, median, spread, share of very short and very long sentences); paragraph length in sentences and words; line length and end-stopping (for verse); dialogue share; moving type-token ratio for vocabulary range; rates per thousand words for punctuation, contractions and a fixed set of function words; and the most frequent three-word sequences.

## Limits (say these when reporting)

- Sentence splitting is a rule of thumb. Abbreviations, ellipses and verse confuse it. Check a sample of splits on unusual texts.
- Dialogue detection relies on quotation marks. Unmarked or dashed dialogue is not counted.
- Under about 2,000 words, most figures are unstable. Report them as indicative.
- Frequent three-word sequences are for spotting habits. They are never a list of phrases to reuse.
- The comparison reports differences. It does not give a similarity score, because none of these figures add up to "how like the author" a passage is.

## Outputs

Measured figures with word counts, and a short note per hypothesis.

## Quality test

Could someone rerun the script on the same file and get the same numbers? Then the figure stands.

## Failure modes

- **False precision.** Two decimal places on a 400-word sample. Repair: round, and mark it indicative.
- **Numbers as style.** Writing to hit a sentence-length average. Repair: numbers check a profile entry. They never become a target.

## Signals

- (+) A measured figure confirms a forensic finding.
- (-) A figure is cited with no file or word count. Remove it until it is rerun.

## Contract

```contract
node: stylometrics
sends: corpus-intelligence | moderate | extraction faults the numbers expose: scanning noise, broken hyphenation, merged paragraphs
sends: reconstruction-validator | strong | side-by-side measurements of source and draft, never a similarity percentage
sends: stylistic-forensics | strong | computed distributions that confirm, qualify or contradict a hypothesis
receives: corpus-intelligence | critical | clean primary-author text only, with editorial matter removed
receives: reconstruction-validator | strong | draft passages and the matching source sections to measure
receives: stylistic-forensics | strong | hypotheses that can be measured
```
