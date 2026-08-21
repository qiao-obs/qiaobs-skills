# `run-autonomous-workpacks`: Complete Bounded Work

> 10-second definition: When a multi-stage mission is already authorized, turn it into bounded workpacks with explicit scope, dependencies, safe recovery, evidence, and a truthful closeout state.

- [简体中文说明](run-autonomous-workpacks.zh-CN.md)
- [Execution entrypoint](../../skills/run-autonomous-workpacks/SKILL.md)

## What this Skill is for

Large tasks often contain inspection, implementation, tests, documentation, build work, and repository closeout. Without a work structure, the agent may lose the original scope, repeat a failed command, mix unrelated edits into the diff, or call a local result a delivered result.

`run-autonomous-workpacks` provides a compact execution method:

1. establish the mission contract;
2. split the mission into independently verifiable workpacks;
3. order them by dependencies and side effects;
4. execute safe work inside the authorized boundary;
5. diagnose failures and retry only with a changed cause or input;
6. verify the complete result and record the real final state.

This Skill governs work organization, execution boundaries, and verification. It does not change Codex's native conversation, progress display, or subagent experience.

## When to use it

Use it when the request already contains enough authority and scope for several connected actions, such as:

- inspect a repository, implement a bounded change, run tests, update docs, and prepare a review;
- migrate a data shape with a rollback note, fixtures, validation, and a closeout record;
- prepare a release package while keeping publication or production actions explicitly separate;
- repair a cross-file issue where each work stage has a clear input and done condition.

Do not use it for:

- a one-line rewrite, translation, fact lookup, or isolated syntax explanation;
- analysis-only or diagnosis-only work where mutation is forbidden;
- an ambiguous task whose next mutation depends on a missing material fact;
- payment, deletion, production, publication, account changes, or other high-impact work without explicit authorization.

## Inputs and outputs

### Inputs

- objective and acceptance criteria;
- allowed and forbidden paths or systems;
- authoritative files, records, tests, and constraints;
- external actions that are explicitly allowed or must remain separate;
- existing user edits that must be preserved.

### Outputs

- mission contract;
- workpack cards and dependency board;
- per-pack changes, checks, failures, retries, and evidence;
- explicitly untouched scope;
- layered verification with `verified`, `unknown`, `skipped`, `failed`, or `blocked` states;
- `COMPLETE`, `PARTIAL`, or `BLOCKED` closeout.

## The workpack method

### 1. Write the mission contract

Record the objective, scope, non-goals, side-effect budget, authoritative inputs, acceptance criteria, and stop conditions before editing. A successful login is access evidence, not permission for every external action.

### 2. Define workpack cards

Every card needs one objective, exact allowed writes, untouched paths, inputs, dependencies, risk, done condition, checks, recovery route, status, and evidence. Keep documentation, implementation, installation, and publication scopes separate.

### 3. Execute in dependency order

Discover the baseline first. Prepare only required fixtures or temporary locations. Implement the smallest coherent change. Verify the focused behavior and then the repository-wide result. Perform external actions only after local evidence supports them and the request explicitly authorizes them.

### 4. Recover from failure

Capture the command and exit code. Classify the first relevant error. Make one diagnosed correction. Rerun the smallest decisive check. If the cause remains unexplained after bounded attempts, retain the failure as `PARTIAL` or `BLOCKED`; never turn an assumption into a pass.

### 5. Close with separate evidence

A source diff proves an intended edit. A test proves only the covered harness. A build proves artifact generation. A preview, upload, release, or user report proves its own layer. The closeout must not conflate these claims.

## An anonymized case

A public Skill repository refinement task contained baseline inspection, entrypoint edits, references, bilingual guides, image assets, deterministic validation, isolated installation, CI, pull request review, merge, and release. The safe decomposition was:

- WP-01: inspect the current branch, remote, release, and worktree;
- WP-02: refine Skill entrypoints and references;
- WP-03: generate and inspect assets and README rendering;
- WP-04: run static, unit, link, privacy, and installation checks;
- WP-05: enter review and release actions only after local evidence passes.

When an external permission was unavailable, the first four packs remained useful and the release pack stayed explicitly blocked. Local evidence was not presented as publication evidence.

## Copyable prompts

### Prompt 1: authorized implementation

> Execute this authorized multi-stage task across audit, implementation, regression tests, documentation, and closeout. Preserve existing edits, keep writes inside the named scope, avoid destructive commands, and distinguish local verification from external delivery.

### Prompt 2: diagnosis-only boundary

> Diagnose the issue without modifying, deploying, or uploading. Build an evidence-oriented workpack record, mark mutation work as unauthorized, and identify the smallest fact needed for a later implementation.

### Prompt 3: bounded retry

> A validation command failed. Preserve the command and exit code, classify the cause, make one diagnosed correction, rerun the decisive check, and leave the result `verified`, `unknown`, `partial`, or `blocked` according to evidence.

## Typical closeout record

```text
Outcome: PARTIAL
Completed workpacks:
- WP-01 baseline: verified
- WP-02 scoped implementation: verified
- WP-03 deterministic checks: verified
Changed artifacts:
- README.md: default narrative
- skills/<name>/SKILL.md: progressive disclosure
Verification:
- repository validation: PASS
- isolated install: PASS
- remote merge: SKIPPED — permission denied
Untouched scope:
- production systems and unrelated user edits
Open blockers:
- one maintainer action is required before merge
```

## Failure conditions

- treating a diagnosis request as implementation permission;
- creating a card without a done condition or exact write scope;
- repeating a failed command without a changed diagnosis;
- inferring publication from a local test or a successful login;
- overlapping temporary directories between independent checks;
- resetting or cleaning unknown user files;
- claiming `COMPLETE` while a required evidence layer is unknown.

## Composition

Use `trace-feature-chain` when the main problem is locating a cross-layer mismatch. Use `reason-from-reality` when the main problem is learning, planning, assessment, or belief update from evidence. Add this Skill only for the authorized execution portion, not as a replacement for the primary reasoning method.

## FAQ

### Does this Skill grant publication permission?

No. It organizes work that is already authorized. Publication, production changes, paid actions, deletion, account changes, and external messages require their own explicit authorization.

### Can it be used for diagnosis-only work?

It may help structure read-only evidence collection, but it must keep mutation packs out of scope and must not infer implementation permission.

### What is the difference between `PARTIAL` and `BLOCKED`?

`PARTIAL` means useful work is verified while a bounded gap remains. `BLOCKED` means a required next action cannot safely proceed without user input or an external state change.

### Why separate build, preview, upload, and release?

Each layer proves a different fact. Keeping them separate prevents a local source or test result from being presented as a result that a user can actually receive.

### Does it change the native Codex experience?

No. It defines work decomposition and evidence, while Codex retains its native interaction and presentation behavior.
