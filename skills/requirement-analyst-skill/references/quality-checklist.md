# Quality Checklist

Run through this before writing the Summary. Fix problems with `edit_file`; if
everything passes, write the Summary and stop.

## Confirmed Facts
- [ ] Every bullet is stated in the document; nothing inferred.
- [ ] One fact per bullet.
- [ ] Modal verbs (shall/should) preserved.

## Ambiguities
- [ ] Each bullet uses the exact `**"clause"**` + `Reason:` shape.
- [ ] Each quoted clause appears verbatim in the document.
- [ ] Each Reason states what is missing and why it blocks work.
- [ ] Missing topics (limits, lifecycle, errors, security) are covered.
- [ ] All lenses in `analysis-framework.md` were considered.

## Clarification Questions
- [ ] Numbered `Q1..Qn`.
- [ ] Each is specific, answerable, and one question.
- [ ] Every ambiguity is covered by at least one question.
- [ ] Ordered by blocking impact.

## Assumptions
- [ ] Each cites a question `(Q#)`.
- [ ] Each is concrete and testable.
- [ ] Safer default chosen for security/data.
- [ ] No new scope introduced.

## Summary
- [ ] Two or three sentences only.
- [ ] States readiness verdict.

## File
- [ ] Only the five `AGENTS.md` sections, headings unchanged and in order.
- [ ] Written to the exact path the task named.
- [ ] Requirement document untouched.
