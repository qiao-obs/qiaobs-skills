# Workpack lifecycle

Use this sequence for an authorized multi-stage mission. Keep each card independently checkable and keep the user informed without turning updates into approval requests.

## 1. Task contract

```text
Objective: observable outcome
Scope: allowed files, systems, and artifacts
Non-goals: explicit exclusions
Acceptance: facts that must be true at the end
Inputs: prompt, repository, tests, external records
Side-effect budget: allowed / evidence-dependent / forbidden
Mode: observable / quiet / high-visibility
Stops: USER_ONLY / EXTERNAL_WAIT / UNAUTHORIZED_HIGH_IMPACT / MISSING_FACT / FAILURE_UNRESOLVED
```

Write the contract before the first mutation. In the default `observable` mode, send a kickoff checkpoint before the first substantive command or subagent and continue without waiting.

## 2. Workpack card

```text
ID: WP-<number>
Name: imperative outcome
Objective: one independently verifiable result
Inputs: files, records, or prior outputs
Allowed writes: exact paths or path families
Dependencies: prior IDs or none
Risk: low / medium / high
Done when: observable condition
Checks: command, test, preview, or inspection
Recovery: safe retry or route change
Status: queued / active / blocked / verified / failed / skipped
Evidence: result after execution
```

Keep writes disjoint where possible. A documentation pack should not silently edit code; an installation smoke test should use a private temporary project.

## 3. Dependency waves

1. **Discover:** read instructions, audit the baseline, and freeze the boundary.
2. **Prepare:** create the branch and temporary locations; do not change behavior early.
3. **Implement:** make the smallest coherent change.
4. **Verify:** run narrow checks, then repository-wide checks and original-condition tests.
5. **Close:** inspect the diff, publish only after local gates, and record external results.

Send a checkpoint at the phase transitions and after each important wave. Parallelize only independent work with disjoint writes or read-only scopes.

## 4. Local failure handling

When a workpack fails:

1. preserve the command, exit code, and first relevant error;
2. classify content, environment, dependency, permission, or external-state failure;
3. make one bounded corrective change;
4. rerun the smallest decisive check;
5. send a checkpoint if the route, evidence quality, risk, or scope changes;
6. continue only when the workpack's done condition is supported.

Do not repeat the same command without changing the diagnosed cause. Do not hide skipped or unavailable checks behind a green summary.

## 5. Closeout

Before closeout, confirm the diff contains only in-scope artifacts, public-safe text, real evidence, and no temporary files. A final report can say `PARTIAL` even when local work is strong; use `COMPLETE` only when every required gate is fresh and observable.
