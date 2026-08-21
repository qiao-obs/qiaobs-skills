# `trace-feature-chain`: Trace the First Mismatch

> 10-second definition: When a feature fails only for a particular role, device, entry point, data shape, or release artifact, trace the real path to the first mismatch and repair only that layer.

- [简体中文说明](trace-feature-chain.zh-CN.md)
- [Execution entrypoint](../../skills/trace-feature-chain/SKILL.md)

## The expensive failure mode it addresses

A page can say “load failed” while the API is healthy, permissions are correct, and the actual defect is a shared client contract that the target runtime cannot execute. The opposite can also happen: a policy or data producer is wrong while the UI looks like the culprit.

Use this Skill to keep these distinctions visible:

- identity, permission, visibility, applicability, and authorization are different facts;
- frontend, backend, database, object storage, shared contract, runtime, build, preview, upload, release, and acceptance are different layers;
- source changed, test passed, build succeeded, preview worked, upload succeeded, and the user accepted the result are different claims.

## Use it / do not use it

Use it when a user gives a reproducible scenario such as:

> An authorized operator can edit a public profile in the simulator, but a real phone fails only when an avatar URL is present.

Do not load it for ordinary interface polish, a standalone syntax fix, translation, one-off factual help, or a routine deployment whose failure chain is already understood.

## The chain

```text
role → business goal → real entry → page state → identity/permission facts
→ command → API → backend/database facts → object storage
→ shared contract → runtime → build artifact → preview/upload/release
→ re-entry projection → recovery and retry
```

This is a reasoning order, not a demand to inspect every file. Skip a link only after evidence shows it cannot change the answer.

## Workflow

### 1. Freeze the scenario predicate

Record the generic role class, business goal, device/runtime, environment, exact entry and action, page state, identity and permission facts, data and network conditions, unique failure, expected result, and non-goals. Redact identifiers and use classes rather than accounts.

### 2. Reproduce the original path

Keep the original role, device, entry, data shape, and failure condition. An empty fixture, a simulator, an easier account, or a direct route can be a useful contrast, but none replaces the original scenario.

### 3. Build an evidence matrix

For each relevant link, write:

```text
Expected:
Observed:
Evidence:
Status: pass | fail | unknown
```

The [evidence matrix](../../skills/trace-feature-chain/references/evidence-matrix.md) provides a compact format and boundary contrasts.

### 4. Stop at the first mismatch

Ask what must be true before the symptom can appear, then compare expected and observed values from upstream to downstream. The first actionable mismatch is the earliest directly evidenced difference that explains the later symptom.

### 5. Pick the minimum safe repair

Repair a shared defect in the shared layer, a policy defect in policy evaluation, a data defect in its producer, and an artifact defect in the build or delivery path. Avoid account-ID exceptions, speculative fallback behavior, unrelated refactors, and redeploying an unaffected service.

### 6. Verify by layer

Run the original-condition regression, repository checks, generation/build checks, target-runtime or preview checks, delivery evidence, and re-entry/recovery checks as separate gates. Read [proof and release boundaries](../../skills/trace-feature-chain/references/proof-and-release-boundaries.md) before writing a release claim.

## Inputs and outputs

Inputs:

- role class, device/runtime, environment, and release channel;
- real entry and action sequence;
- minimum data condition that distinguishes failure from success;
- expected result, actual failure, and non-goals;
- safe access to relevant code, responses, tests, logs, artifacts, or tool results.

Output:

```text
Scenario predicate:
Scope and non-goals:
Chain status:
First mismatch:
Root cause and affected layer:
Minimal safe fix:
Evidence and verification:
Release boundary:
Remaining risks or user checks:
```

## Complete anonymized case

In an anonymized campus information mini-program, an authorized operator could edit public information in the simulator. A real phone failed only when the account already had an avatar or background image. The backend response was normal.

A conventional response might add an account-specific branch, relabel the error as a network failure, add retries, or redeploy the backend. The chain method instead kept the non-empty media condition, verified permission and API facts, and found that a shared image helper depended on a browser API not guaranteed by the target runtime.

The repair removed that runtime dependency in the shared helper and added a regression for a signed-looking media address under the target capability constraint. The original case recorded one shared source file, one regression file, and 31 focused checks before a front-end upload. Those numbers describe one anonymized case, not a benchmark.

## Ordinary handling versus this Skill

| Ordinary handling | With `trace-feature-chain` |
| --- | --- |
| Start from the final error text | Freeze the original role, route, data, and device predicate |
| Treat HTTP 200 as feature success | Verify the producer/consumer contract and runtime behavior separately |
| Add a special case for a named account | Fix the shared layer when the path is shared |
| Treat tests or a build as release proof | State each artifact and delivery boundary explicitly |
| Substitute a simple fixture | Preserve the data condition that triggers the defect |

## Three copyable prompts

1. “Trace this role-specific real-device failure from the actual entry through permissions, API, data, shared contract, runtime, build, and release. Find the first mismatch before editing.”
2. “The source fix passes tests but the phone still shows the old behavior. Check generated output, preview/upload version, re-entry, and recovery as separate claims.”
3. “This failure appears only with non-empty media. Compare the relevant data and runtime boundaries, and do not add an account-specific exception for a shared defect.”

## Typical output fragment

```text
First mismatch:
- Link: shared contract → target runtime
- Expected: media validation runs on the real device
- Observed: the helper calls a browser-only constructor when media is present
- Evidence: API shape is valid; device failure is conditional; helper is shared

Release boundary:
- Focused regression: pass
- Build artifact: unknown until regenerated
- Preview/upload: unknown
- User acceptance: unknown
```

## Boundaries, anti-patterns, and failure conditions

- Do not expose account identifiers, signed URLs, private paths, credentials, or infrastructure details.
- Do not use a passing page load, API status, or test suite as end-to-end proof.
- Do not widen the patch because a later symptom is noisy.
- Do not redeploy a server merely because a client runtime failure is confusing.
- If the first mismatch remains unknown, gather the cheapest decisive evidence rather than making a speculative edit.

## How to combine it

- Use `run-autonomous-workpacks` after the mismatch is known when the authorized work includes implementation, tests, build, docs, and closeout.
- Use `reason-from-reality` when software evidence must update a longer plan, capability decision, or learning loop.
- Do not load all three for a simple syntax fix, translation, rewrite, or isolated fact.

## FAQ

**Why not start with the error message?** It may be a downstream projection. The chain keeps upstream prerequisites visible.

**Why preserve non-empty data?** Parsing, rendering, storage, and serialization paths often differ between empty and populated states.

**Why separate build, preview, upload, and acceptance?** Each is a different artifact or observation boundary.

**What if evidence is incomplete?** Mark the link `unknown`, state the cheapest next check, and avoid a stronger claim.
