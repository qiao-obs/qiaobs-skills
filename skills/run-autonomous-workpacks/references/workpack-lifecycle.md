# Workpack lifecycle

Use this sequence for an authorized multi-stage mission. Keep each card independently checkable and make the artifact status precise.

## 1. Task contract

```text
Objective: observable outcome
Scope: allowed files, systems, and artifacts
Non-goals: explicit exclusions
Acceptance: facts that must be true at the end
Inputs: prompt, repository, tests, and external records
Side-effect budget: allowed / evidence-dependent / forbidden
Stops: USER_ONLY / EXTERNAL_WAIT / UNAUTHORIZED_HIGH_IMPACT / MISSING_FACT / FAILURE_UNRESOLVED
```

Write the contract before the first mutation. Resolve safe facts first; do not turn an ambiguity into an implementation guess.

## 2. Workpack card

```text
ID: WP-<number>
Name: imperative outcome
Objective: one independently verifiable result
Inputs: files, records, or prior outputs
Allowed writes: exact paths or path families
Untouched scope: paths that must not change
Dependencies: prior IDs or none
Risk: low / medium / high
Done when: observable condition
Checks: command, test, preview, or inspection
Recovery: safe retry or route change
Status: queued / active / blocked / verified / failed / skipped
Evidence: result after execution
```

Keep writes disjoint where possible. A documentation pack must not silently edit code; an installation smoke test must use a private temporary project.

## 3. Dependency waves

1. **Discover:** read instructions, audit the baseline, and freeze the boundary.
2. **Prepare:** create only the required branch, fixtures, and temporary locations.
3. **Implement:** make the smallest coherent change.
4. **Verify:** run focused checks, then repository-wide checks and original-condition tests.
5. **Close:** inspect the diff, perform only authorized external actions, and record the result.

A dependency board should show which pack is ready, active, blocked, verified, failed, or skipped and why.

## 4. Local failure handling

When a workpack fails:

1. preserve the command, exit code, and first relevant error;
2. classify content, environment, dependency, permission, or external-state cause;
3. make one bounded corrective change;
4. rerun the smallest decisive check;
5. continue only when the done condition is supported.

Do not repeat the same command without changing the diagnosed cause. Record an unresolved failure rather than converting a likely result into a pass.

## 5. Closeout

Before closeout, confirm the diff contains only in-scope artifacts, public-safe text, real evidence, and no temporary files. Distinguish edited, tested, built, previewed, uploaded, merged, released, and accepted states. Use `COMPLETE`, `PARTIAL`, or `BLOCKED` only according to the evidence rules in [verification-and-failure-handling.md](verification-and-failure-handling.md).
