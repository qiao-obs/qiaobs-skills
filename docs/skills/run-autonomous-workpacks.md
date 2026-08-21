# `run-autonomous-workpacks`: Complete Bounded Work with Visible Progress

> 10-second definition: When a multi-stage mission is already authorized, turn it into bounded workpacks with visible progress, dependencies, safe retries, and a truthful final state.

- [简体中文说明](run-autonomous-workpacks.zh-CN.md)
- [Execution entrypoint](../../skills/run-autonomous-workpacks/SKILL.md)

## Observable Autonomy Protocol

This method means **low interruption, not low visibility**.

```text
Low interruption, not low visibility.
High autonomy, not expanded authorization.
Continuous execution, not silent disappearance.
Progress updates, not approval requests.
Real blockers, not routine pauses.
```

Low interaction reduces mandatory user input, handoffs, and routine confirmation. It does not reduce the user’s awareness of the current phase, completed evidence, unverified work, risks, route changes, or release boundaries.

- `CHECKPOINT`: informational progress update; send it and continue;
- `GATE`: real authorization or input boundary; wait only for login/MFA, permission denial, unauthorized high-impact work, material missing facts, or a critical result that cannot be safely verified.

The default mode is `observable`. Use `quiet` only when the user explicitly requests silent execution. For work expected to exceed two minutes, report kickoff, phase transitions, meaningful failures or route changes, and a new-information heartbeat when no natural milestone occurs. Do not stream every command or send empty “still working” messages.

Example:

```text
CHECKPOINT (non-blocking): Scope and baseline are verified; implementation is active; local validation and release checks are not run yet. I will continue and report at the next phase boundary.
```
## The expensive failure mode it addresses

A broad mission often contains inspection, implementation, tests, documentation, build work, and closeout. If each stage becomes a separate confirmation loop, the agent spends the mission asking whether it may continue. If “autonomous” is interpreted as unlimited permission, it may instead edit, deploy, publish, or delete beyond the request.

This Skill manages the sequence without changing the authorization boundary.

## Use it / do not use it

Use it when the user has supplied an objective, scope, non-goals, and permission to carry out adjacent stages, for example:

> Inspect the repository, refine the three skills, run validation and install smoke tests, then open and merge the authorized release change. Preserve existing history and stop for MFA or permission denial.

Do not use it to turn “analysis only” into implementation, to infer permission from a successful login, or to perform unapproved production, paid, destructive, account, or publication actions. A small isolated task with no meaningful sequence does not need a workpack protocol.

## Four boundaries to keep distinct

```text
Low interaction ≠ no reporting
High autonomy ≠ expanded authorization
Continuous execution ≠ ignoring failure
Fewer questions ≠ guessing key facts
```

Routine, reversible, in-scope work can proceed without another confirmation. Login/MFA, external permission denial, human approval, a missing material fact, or an unauthorized high-impact action remains a real stop.

## Workpack lifecycle

```text
Task contract → verifiable workpacks → dependency order
→ diagnose/retry local failure → whole-result verification → COMPLETE/PARTIAL/BLOCKED
```

### 1. Write the task contract

Before the first mutation, extract:

- objective and observable done conditions;
- allowed files, systems, artifacts, and external actions;
- non-goals and forbidden side effects;
- authoritative inputs and assumptions;
- verification gates and final report shape;
- stop conditions: `USER_ONLY`, `EXTERNAL_WAIT`, `UNAUTHORIZED_HIGH_IMPACT`, `MISSING_FACT`, or `FAILURE_UNRESOLVED`.

### 2. Define workpack cards

Each card needs one independently verifiable objective, exact write scope, inputs, dependencies, risk, done condition, checks, recovery note, status, and evidence. Good names are “Map the baseline,” “Refine the entrypoint,” “Run the link gate,” and “Close the release.”

Keep write scopes disjoint where possible. A documentation pack should not silently edit code; an installation smoke test should use a private temporary destination.

### 3. Execute in dependency waves

1. **Discover:** read governing instructions and audit the baseline.
2. **Prepare:** create the branch and controlled temporary locations.
3. **Implement:** make the smallest coherent change.
4. **Verify:** run narrow checks, then full checks.
5. **Close:** review the diff and perform only the external actions explicitly authorized after local gates pass.

Parallelize only independent checks that do not share mutable state.

### 4. Diagnose and retry local failure

Capture the command, exit code, and first useful error. Classify the issue as content, environment, dependency, permission, or external state. Make one bounded correction, rerun the smallest decisive check, and mark the workpack verified only when its done condition is supported.

A safe retry of an idempotent network request may be reasonable. An authentication failure is not an invitation to keep retrying. An unresolved failure after bounded attempts becomes `PARTIAL` or `BLOCKED`, not an implied pass.

## Inputs and outputs

Inputs:

- user request, attached prompt, repository instructions, and current state;
- allowed write scope and side-effect budget;
- authoritative verification commands;
- external results needed for completion.

Outputs:

- task contract and execution board;
- changed artifacts and intentionally untouched scope;
- each workpack’s checks, failure evidence, and recovery;
- skipped, unknown, and blocked gates;
- final `COMPLETE`, `PARTIAL`, or `BLOCKED` state.

Minimum final report:

```text
Outcome: COMPLETE | PARTIAL | BLOCKED
Completed workpacks:
Changed artifacts:
Verification:
Assumptions:
Open blockers or follow-ups:
```

## Complete anonymized case

A public Skill repository refinement can include baseline audit, content restructuring, visual assets, six bilingual user guides, validators, installation smoke tests, CI, a pull request, merge, and a release. The method turns this into independent packs with controlled write scopes rather than one opaque stream of edits.

If local validation succeeds but GitHub rejects a push or merge, the local packs can still be verified. The external pack is `EXTERNAL_WAIT`; the report must not claim a release.

## Ordinary handling versus this Skill

| Ordinary handling | With `run-autonomous-workpacks` |
| --- | --- |
| Ask before each routine command | Continue through safe, authorized workpacks |
| Keep a vague to-do list | Give each pack a done condition and check |
| Retry a failure without diagnosis | Classify, correct once, and rerun the decisive check |
| Treat login as publication approval | Distinguish access from action authorization |
| Hide skipped external steps | Report `unknown`, `skipped`, `PARTIAL`, or `BLOCKED` honestly |

## Three copyable prompts

1. “Execute this authorized multi-stage mission with bounded workpacks. Preserve existing edits, avoid destructive commands, keep a short progress report, and stop only for real blockers.”
2. “Only analyze; do not modify, deploy, upload, publish, or delete. Build the workpack plan and evidence board, and mark mutation packs as not authorized.”
3. “A verification pack failed. Preserve the output, classify the failure, make one evidence-based correction, retry the smallest decisive check, and report the resulting state.”

## Typical output fragment

```text
Outcome: PARTIAL
Completed workpacks:
- WP-01 baseline audit: verified
- WP-02 scoped implementation: verified
- WP-03 deterministic checks: verified
Changed artifacts:
- README.md: default product narrative
- skills/<name>/SKILL.md: concise execution entrypoint
Verification:
- local validation: PASS
- external merge: SKIPPED — permission denied
Open blockers:
- maintainer action required before merge
```

## Boundaries, anti-patterns, and failure conditions

- Do not override an explicit “do not modify” instruction.
- Do not use low interaction to expand scope, bypass MFA, or infer publication permission.
- Do not overwrite user changes or rewrite history destructively.
- Do not mark a workpack `verified` without its listed check.
- Do not repeat the same failing command without changing the diagnosed cause.
- Do not omit progress at meaningful milestones; low interruption still requires transparent state.

## How to combine it

- Pair with `trace-feature-chain` when the first mismatch must be located before implementation.
- Pair with `reason-from-reality` when a long-term decision or learning loop must be executed and updated.
- Do not load all three for a simple syntax fix, translation, rewrite, or one-off fact.

## FAQ

**When can the agent continue?** When the work is reversible, in scope, supported by known inputs, and does not create an unapproved high-impact side effect.

**When must it stop?** For user-only authentication/MFA, external permission denial, unapproved production/paid/destructive work, a material missing fact, or unresolved failure after bounded retries.

**What is `PARTIAL`?** Useful work is verified, but a bounded nonessential or externally unobservable criterion remains open.

**What is `BLOCKED`?** The next required safe action cannot proceed without user input or an external state change.

**Why report milestones?** Fewer handoffs should reduce friction, not reduce transparency. A milestone tells the user what changed, which layer was verified, and whether the next step has external side effects.
