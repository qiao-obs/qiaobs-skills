# Evidence Matrix and Report Template

Use this reference after the scenario predicate is frozen. Keep the matrix small: include every link that can change the answer, not every file in the repository.

## 1. Scenario predicate

```text
Role/account class: [generic class; no identifier]
Device/runtime: [simulator, real device, browser, worker, etc.]
Environment: [local, test, preview, released; use a safe label]
Real entry: [screen/route → control → action]
Data conditions: [empty/non-empty, media present, state, network]
Observed failure: [one reproducible predicate]
Expected result: [observable success]
Scope: [requested feature]
Non-goals: [explicitly excluded work]
```

If a field is unknown, write `unknown` and explain how to obtain proof. Ask for clarification only when the missing fact blocks safe diagnosis or execution.

## 2. Evidence matrix

| Link | Expected | Observed | Evidence | Status |
| --- | --- | --- | --- | --- |
| Role and goal | Correct role can perform the goal |  | User report or acceptance condition |  |
| Real entry and state | Intended route and control are reachable |  | Reproduction, screen state, route trace |  |
| Identity and permission | The request is authorized and applicable |  | Auth/permission facts, not assumptions |  |
| Command and API | The intended command is sent with the right shape |  | Network trace, request/response contract |  |
| Backend, database, storage | Required data is stored and returned correctly |  | Server log, query, fixture, or response |  |
| Shared contract | Producers and consumers agree on shape and semantics |  | Type/schema test, source inspection |  |
| Runtime | The target runtime supports the executed behavior |  | Device log, exception, capability check |  |
| Build artifact | The fix is present in the generated artifact |  | Build output, manifest, checksum if safe |  |
| Preview/upload/release | The intended artifact reached the stated channel |  | Tool result, release record, or user confirmation |  |
| Re-entry/recovery | Refresh, retry, or re-entry preserves the expected result |  | Original-path regression |  |

`pass` means the listed evidence proves that link only. It does not imply that later links pass.

## 3. First-mismatch test

For each failed scenario, ask:

1. What must be true before this symptom can occur?
2. Which prerequisite has direct evidence, and which is only assumed?
3. Where does `expected` first differ from `observed`?
4. Could the same code path fail for another role or non-empty data shape?
5. Is the proposed fix upstream of the symptom and limited to the requested feature?

Do not stop at a generic UI message. Example reasoning:

```text
API returns a valid media address
→ shared client contract invokes a browser-only constructor
→ real-device runtime throws
→ page shows “load failed”
```

The first mismatch is the runtime/contract boundary, not the page copy and not necessarily the API.

## 4. Boundary checks

Choose a small comparison matrix rather than testing every combination:

| Dimension | Baseline | Contrast | Why it matters |
| --- | --- | --- | --- |
| Data | empty | non-empty or media present | Reveals conditional parsing and rendering paths |
| Role | ordinary member | operator or other authorized class | Reveals shared versus role-specific logic |
| Runtime | simulator | real device | Reveals capability and API differences |
| Entry | fresh entry | re-entry/retry | Reveals stale state and recovery defects |
| Delivery | source/build | preview/upload/release | Reveals artifact and channel mismatch |

Record only contrasts that relate to the original predicate. Do not use the matrix to expand scope.

## 5. Minimal-fix decision rules

- **Shared contract defect:** fix the shared contract and add a regression case for the affected data shape.
- **Role-specific policy defect:** fix policy or permission evaluation; do not hide it with a UI exception.
- **Frontend runtime defect:** fix the client-compatible code and verify the target runtime; do not redeploy an unrelated backend.
- **Backend/data defect:** fix the producing layer and verify the returned shape before changing consumers.
- **Build/release defect:** rebuild or republish the intended artifact; do not claim a source edit reached users without proof.
- **Unknown cause:** gather the cheapest decisive evidence before making a speculative change.

## 6. Final report template

```text
Scenario predicate:
- Role/device/entry:
- Data and permission conditions:
- Unique failure and expected result:

Scope and non-goals:

Chain summary:
- PASS:
- FAIL:
- UNKNOWN:

First mismatch:
- Link:
- Expected:
- Observed:
- Evidence:

Root cause:

Minimal safe fix:
- Changed:
- Intentionally untouched:

Verification:
- Automated/local:
- Original scenario:
- Build/artifact:
- Preview/upload/release:
- Re-entry/recovery:

Release boundary:

Remaining risks and user checks:
```

For public examples, replace all project-specific names, paths, domains, identifiers, hashes, logs, and secrets with generic placeholders.
