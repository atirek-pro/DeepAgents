---
name: requirement-analyst-skill
description: Analyzes a raw business or technical requirement document and produces a structured, developer-ready analyst report (confirmed facts, ambiguities, clarification questions, assumptions, summary). Use when asked to review, analyze, or break down a requirement (e.g. requirements/REQ001.txt) before a developer builds a feature or system from it.
license: MIT
compatibility: Works with the deepagents FilesystemBackend (virtual_mode=True); needs only read_file, write_file and edit_file. No scripts are executed.
metadata:
  author: loop-engineering
  version: "1.0"
---

# Requirement Analyst Skill

Turns a raw requirement into a report a developer can build from without guessing.
The report is a **review**, not a design: it records what is known, what is
missing, what to ask, and what would be assumed if nobody answers.

## Precedence

`AGENTS.md` (persistent memory) is the contract for **procedure, section skeleton,
retry behaviour and completion rule**. This skill adds **depth and quality** inside
that contract. If the two ever disagree, `AGENTS.md` wins. Never change the
requirement document. Never edit `AGENTS.md`.

## Workflow

Follow the stage order from `AGENTS.md`, one tool call per turn:

1. Read the requirement document (path comes from the task, e.g. `requirements/<id>.txt`).
2. Write the report file with the six-section skeleton; fill only **Confirmed Facts**.
3. Edit in **Ambiguities**.
4. Edit in **Clarification Questions**.
5. Edit in **Assumptions**.
6. Edit in **Summary**, then reply with one short sentence and stop.

Output path: use the exact path the task names (normally `output/analysis_draft.md`).
Do not invent alternative filenames.

## What to read, and when

Read these only at the stage that needs them (progressive disclosure):

| Stage | Read |
|---|---|
| Before writing Confirmed Facts | [references/instructions.md](references/instructions.md) – rules for each section |
| Before writing Ambiguities / Questions | [references/analysis-framework.md](references/analysis-framework.md) – the lenses to probe (business and technical) |
| Spotting vague wording | [references/ambiguity-patterns.md](references/ambiguity-patterns.md) – vague-term catalogue |
| Before the Summary | [references/quality-checklist.md](references/quality-checklist.md) – self-check |
| Unsure of the shape | [assets/report-template.md](assets/report-template.md) and [assets/example-report.md](assets/example-report.md) |

## Non-negotiables

- **Facts are quoted or tightly paraphrased from the document. Never inferred.**
- Every ambiguity quotes the **exact clause** and gives a reason.
- Every clarification question is answerable, specific, and unblocks real work.
- Every assumption is what a developer would *actually do* if unanswered, and it
  maps back to a question.
- Tag business vs technical concerns (`[Business]`, `[Technical]`, `[Security]`,
  `[Data]`, `[NFR]`) so the developer can route them.
- Do not design the solution, pick a stack, or add requirements the document lacks.
