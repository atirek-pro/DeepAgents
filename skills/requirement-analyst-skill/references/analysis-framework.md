# Analysis Framework: Lenses to Probe

For each requirement, run it through every lens. A lens that yields nothing is
fine; a lens that was skipped is how gaps reach production.
Use the tag in brackets on ambiguities and questions.

## Business lenses

- **[Business] Actor & permissions** – Who exactly? Roles, tiers, anonymous vs
  authenticated, admin override?
- **[Business] Goal & value** – Why is this needed? What outcome defines success?
- **[Business] Scope boundaries** – What is explicitly in and out? Which
  platforms/channels (web, mobile, API)?
- **[Business] Rules & policy** – Limits, quotas, approval flows, retention,
  deletion rights, pricing impact.
- **[Business] Priority & dependencies** – MoSCoW level, deadline, related
  requirements, external teams or vendors.
- **[Business] Acceptance** – How will anyone decide it is done? Measurable criteria?

## Technical lenses

- **[Technical] Inputs / outputs** – Exact formats, fields, encodings, limits,
  validation rules.
- **[Technical] Behaviour & states** – Happy path, replace/overwrite, duplicate,
  partial failure, cancel, resume, concurrency.
- **[Technical] Error handling** – What does the user see on failure? Retries?
  Messages? Logging?
- **[Technical] Integration** – Existing services, APIs, auth system, storage,
  third parties, migrations.
- **[Data] Data model & lifecycle** – What is stored, where, for how long, who
  owns it, how it is deleted/exported, PII involved?
- **[Security] Security & privacy** – AuthN/AuthZ, encryption in transit/at
  rest, malware scanning, access control, audit trail, compliance
  (GDPR, HIPAA, SOC2...).
- **[NFR] Non-functional** – Performance (latency, throughput), scalability,
  availability, accessibility, i18n, browser/device support, observability.
- **[Technical] Testability** – Can each statement become a pass/fail test as written?

## Cross-check questions

1. Could two developers read this and build different things? If yes, ambiguity.
2. Is there a number, list, or name where the text says an adjective? Ask for it.
3. Does anything contradict anything else in the document?
4. Is something implied by the title but not described in the body?
5. What happens at the edges: zero, one, maximum, over maximum, invalid, concurrent?

## Mapping to the report

| Finding | Goes to |
|---|---|
| Directly stated | Confirmed Facts |
| Vague / missing / contradictory | Ambiguities |
| Answer needed from stakeholder | Clarification Questions |
| Default a developer would pick | Assumptions |
