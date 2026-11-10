# Ambiguity Patterns

Wording that almost always signals an under-specified requirement, with the
question it should trigger.

| Pattern | Examples | Ask |
|---|---|---|
| Vague quality adjectives | secure, fast, robust, user-friendly, scalable, reliable | Which measurable standard or threshold? |
| Unbounded sets | common, standard, various, etc., and so on, such as | Which exact items are in the list? |
| Weak modals | should, may, might, could, ideally | Mandatory or optional? Priority? |
| Unquantified | many, large, quickly, soon, frequently, small | What number, unit, and time frame? |
| Undefined actor | users, the system, admins, someone | Which role(s) and permissions? |
| Passive voice | is stored, is validated, is sent | Who or what does it, and when? |
| Implied but unstated | "upload" without size/limit; "delete" without retention | What are the limits, defaults, edge cases? |
| Comparatives | better, faster, easier, improved | Compared to what baseline? |
| Escape clauses | where possible, if needed, as appropriate, unless | Under which exact conditions? |
| Ambiguous scope | profile, account, content, data | What exactly is included? |
| Hidden conjunctions | "and/or", "or" | Both, either, or exclusive? |
| Missing failure path | no mention of errors | What happens when it fails? |
| Missing lifecycle | no mention of update/delete/expiry | Who can change/remove it, and what is retained? |

## Quick triage

- **Weak modal + vague adjective in one clause** = high-priority ambiguity.
- **Security, privacy, money, data deletion** wording = always flag, even if it
  looks fine.
- A one-line requirement with no acceptance criteria is itself an ambiguity:
  flag the missing success criteria.

## Example transformation

Clause: `"Uploaded files should be stored securely."`

- Pattern hits: weak modal ("should"), vague adjective ("securely"), passive voice.
- Reason: `[Security] "securely" has no standard (encryption at rest? access
  control? malware scanning?); "should" does not say if mandatory; the
  responsible component is unstated.`
- Question: `Q2: Which security controls are mandatory for stored files (encryption
  at rest, virus scanning, access control, compliance standard)?`
- Assumption: `(Q2) Files are encrypted at rest, scanned for malware, and
  accessible only to the owning user.`
