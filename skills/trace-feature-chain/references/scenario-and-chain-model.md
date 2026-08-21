# Scenario and chain model

Use this reference before opening a large evidence search. The point is to name the smallest real-world predicate that distinguishes the failure from the working case.

## Scenario predicate

```text
Role/account class: generic class, never an identifier
Business goal: the user-visible outcome
Device/runtime: simulator, real device, browser, worker, or other target
Environment: local, test, preview, or released
Real entry: screen/route → control → action
Page state: loading, empty, populated, stale, permission-gated, or error
Identity/permission facts: authenticated identity, role, applicability, visibility, authorization
Data conditions: empty/non-empty, media present, state, network
Observed failure: one reproducible predicate
Expected result: observable success
Non-goals: excluded work
```

If a field is unknown, record `unknown` and the cheapest safe way to obtain proof. Do not ask for a private identifier when a role class is sufficient.

## Chain questions

| Link | Question | Useful evidence |
| --- | --- | --- |
| Role → goal | Is this the right actor pursuing the right outcome? | User report, acceptance condition |
| Entry → state | Did the real route reach the expected page state? | Route trace, screen state, reproduction |
| Identity → permission | Is the action applicable and authorized? | Auth facts, policy result, not UI labels |
| Command → API | Did the intended command send the expected shape? | Request/response or contract test |
| API → data | Did the producer return the facts the UI needs? | Response, query, fixture, storage metadata |
| Data → contract | Do producer and consumer agree on semantics? | Type/schema test, source inspection |
| Contract → runtime | Does the target runtime support the behavior? | Device log, capability check, exception |
| Runtime → artifact | Is the fix present in generated output? | Build output, manifest, safe checksum |
| Artifact → delivery | Did the intended artifact reach the stated channel? | Preview/upload/release record |
| Delivery → re-entry | Does a fresh entry, retry, or refresh project the result? | Original-path regression |

The chain is a reasoning order, not a demand to inspect every file. Skip a link only after evidence shows it cannot change the answer.

## Boundary contrasts

Select a small contrast set:

- **Data:** empty versus populated or media present.
- **Role:** ordinary member versus another authorized class.
- **Runtime:** simulator versus target device.
- **Entry:** fresh entry versus re-entry or retry.
- **Delivery:** source/build versus preview/upload/release.

Keep only contrasts connected to the original failure predicate. More combinations are not automatically more evidence.
