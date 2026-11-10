# Section-by-Section Instructions

Section headings must match the `AGENTS.md` skeleton exactly:
`Confirmed Facts`, `Ambiguities`, `Clarification Questions`, `Assumptions`, `Summary`.

## 1. Confirmed Facts

- One bullet per fact. One fact per bullet; split compound sentences.
- Record only what the document **directly states**. If you have to reason to get
  there, it is not a fact; it belongs in Assumptions.
- Keep the document's wording (including "shall" / "should" / "may"). The modal verb
  is itself a fact: `shall` = mandatory, `should` = recommended/unclear priority.
- Include the requirement title/ID and any stated actors, constraints, numbers,
  dates, and dependencies.
- If the document states nothing about a topic, say nothing here.

Good: `- Users shall be able to upload files to their profile. (mandatory: "shall")`
Bad:  `- Files are stored in S3.` (not stated)

## 2. Ambiguities

Exact shape required by `AGENTS.md`:

```
- **"the exact clause"**
  Reason: why it is under-specified
```

- Quote verbatim, in quotes, inside the bold.
- One bullet per clause. If one clause hides several gaps, list the gaps in the
  Reason, separated by semicolons.
- The Reason must say **what is missing and why it blocks a developer**, and may be
  prefixed with a tag: `[Business]`, `[Technical]`, `[Security]`, `[Data]`, `[NFR]`.
- Use [analysis-framework.md](analysis-framework.md) to find gaps and
  [ambiguity-patterns.md](ambiguity-patterns.md) to recognise vague wording.
- Also flag **absent** topics that the document should have addressed
  (e.g. no size limit). Quote the nearest clause and say what is absent.
- Do not flag a clause that is already precise.

## 3. Clarification Questions

- One bullet each. Written for the product owner/stakeholder, not the developer.
- Specific and closed where possible ("What is the maximum size per file?"), not
  "Can you tell me more about uploads?".
- One question per bullet. Number them `Q1`, `Q2`, ... so Assumptions can cite them.
- Order by **blocking impact**: questions that stop work first.
- Offer options when it speeds an answer ("Which of: a) images only b) ...?").
- Cover every ambiguity at least once. No question without a matching ambiguity.

## 4. Assumptions

- One bullet each, format: `- (Q#) Assumption statement.`
- State what a developer would end up assuming if nobody answered: the most
  conventional, lowest-risk default.
- Prefer the safer default for security and data questions.
- Make each assumption testable and concrete (numbers, lists), not "reasonable limits".
- Do not smuggle in new scope. An assumption fills a gap; it does not add a feature.

## 5. Summary

- Two or three sentences. No more.
- Sentence 1: what the requirement asks for. Sentence 2: how complete it is and the
  biggest gaps. Optional sentence 3: readiness verdict
  (`Ready` / `Ready with assumptions` / `Blocked pending answers`).

## Style

- Plain, neutral, concise. No filler, no marketing words.
- No sections beyond the five. No extra headings, tables, or preamble in the file.
- Never rewrite the requirement document.
