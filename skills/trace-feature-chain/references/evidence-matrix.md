# Evidence matrix

Use this reference after freezing the scenario. Keep the matrix small enough to review.

## Matrix

| Link | Expected | Observed | Evidence | Status |
| --- | --- | --- | --- | --- |
| Role and goal | Correct role can pursue the goal |  | User report or acceptance condition |  |
| Real entry and page state | Intended route and state are reached |  | Reproduction, route trace, screen state |  |
| Identity and permission | Action is applicable and authorized |  | Auth/policy facts |  |
| Command and API | Intended command has the right shape |  | Network trace, response, contract test |  |
| Backend, database, storage | Required facts are produced and persisted |  | Query, fixture, response, storage evidence |  |
| Shared contract | Producers and consumers agree |  | Type/schema test, source inspection |  |
| Runtime | Target runtime supports the behavior |  | Device log, exception, capability check |  |
| Build artifact | Fix is present in generated output |  | Build output, manifest, safe checksum |  |
| Preview/upload/release | Intended artifact reached the channel |  | Tool result, release record, user confirmation |  |
| Re-entry/recovery | Refresh, retry, or re-entry preserves result |  | Original-path regression |  |

`pass` proves only that row. It does not imply that later rows pass.

## First-mismatch test

1. What must be true before the symptom can occur?
2. Which prerequisite has direct evidence and which is assumed?
3. Where does `expected` first differ from `observed`?
4. Could the same path fail for a different role or non-empty data shape?
5. Is the proposed fix upstream of the symptom and inside scope?

Example:

```text
API returns a valid media address
→ shared client contract calls a browser-only constructor
→ real-device runtime throws
→ page displays “load failed”
```

The first mismatch is not necessarily the API or the page copy.
