---
name: run-autonomous-workpacks
description: Use for authorized multi-step work that should continue with few user decisions while remaining visibly trackable. Organize bounded workpacks, send concise non-blocking progress at kickoff, phase transitions, and bounded heartbeats, verify outcomes with evidence, and pause only for real blockers or new authorization. Do not use for analysis-only, diagnosis-only, or trivial one-step requests.
---

# Autonomous Workpacks

Complete authorized multi-stage work as bounded, inspectable workpacks. The method is **Observable Autonomy Protocol**: reduce forced user input without reducing the user's awareness of state, evidence, risk, or boundaries.

## Observable autonomy contract

- **Minimize mandatory user input, not user awareness. A progress checkpoint is informational: send it and continue. Wait only at a real gate.**
- Low interaction means fewer confirmations, handoffs, and routine implementation questions; it does not mean silence.
- High autonomy means continuous execution inside the authorized scope; it does not expand authorization.
- Progress reports are not approvals. Use `CHECKPOINT` for non-blocking information and `GATE` for a real wait.
- Default to `observable` mode. Use `quiet` only when the user explicitly asks for silent execution. Use `high-visibility` only when explicitly requested.
- Do not stream commands, expose internal reasoning, manufacture percentages, or ask “should I continue?” after a routine checkpoint.

Read [communication-and-progress-contract.md](references/communication-and-progress-contract.md) for mode rules, timing, templates, status queries, long commands, and optional subagent visibility.

## Mission contract

Before the first mutation, extract and preserve:

- objective and observable done condition;
- allowed files, systems, artifacts, and external actions;
- non-goals and forbidden side effects;
- authoritative inputs, assumptions, and required facts;
- verification gates and final report shape;
- stop conditions: `USER_ONLY`, `EXTERNAL_WAIT`, `UNAUTHORIZED_HIGH_IMPACT`, `MISSING_FACT`, or `FAILURE_UNRESOLVED`.

Send a short kickoff `CHECKPOINT` before the first substantive tool call or subagent. It is informational and must not wait for a reply.

## Workpack lifecycle

Use the lifecycle in [workpack-lifecycle.md](references/workpack-lifecycle.md):

```text
Task contract → verifiable workpacks → dependency order
→ execute and checkpoint → diagnose/retry local failure
→ validate the whole result → COMPLETE / PARTIAL / BLOCKED
```

Each workpack needs one objective, non-overlapping write scope, inputs, dependencies, done condition, checks, risk, recovery note, and status. Use `queued`, `active`, `blocked`, `verified`, `failed`, or `skipped` precisely.

Report `CHECKPOINT` when baseline discovery is frozen, when implementation begins, when a workpack or wave completes, when verification begins, when a key assumption changes, or when local gates finish before external actions. Include completed, active, unverified, blocked, release status, and next step. Do not report every file or command.

## Execute in dependency waves

1. **Discover:** read instructions, audit the baseline, and name the scope boundary.
2. **Prepare:** create the branch and controlled temporary locations; do not change behavior early.
3. **Implement:** make the smallest coherent change inside the allowed write scope.
4. **Verify:** run narrow checks, then repository-wide checks and original-condition tests.
5. **Close:** inspect the diff, perform only explicitly authorized external actions after local gates, and report the actual result.

Parallelize only independent checks with disjoint writes or read-only scopes. Subagents are optional optimization, not part of the Skill's definition. Use them only when the work is independent, coordination is worthwhile, and the main thread can summarize and verify the batch. Default to no more than three at once; read [communication-and-progress-contract.md](references/communication-and-progress-contract.md) before using them.

## Authorization and stopping

Continue safe, reversible, in-scope work without another confirmation. Establish a `GATE` and wait only for:

- login, MFA, private credentials, or a security access path the user must provide;
- external permission denial or formal approval;
- an unapproved irreversible, production, public, paid, destructive, or high-impact action;
- a material ambiguity with no safe default;
- a key fact whose absence makes the next mutation unsafe;
- a critical result that cannot be verified and has no trustworthy substitute;
- a legal, compliance, or safety decision that requires a human.

Before a `GATE`, finish all independent safe work and state the smallest user action without requesting a secret. A `CHECKPOINT` never asks for confirmation; a `GATE` explicitly waits.

Use [decision-and-authorization-boundaries.md](references/decision-and-authorization-boundaries.md) for the blocker format.

## Failure, retries, and evidence

Do not stop or repeat blindly when a routine check fails:

1. preserve the command, exit code, and relevant error;
2. classify content, environment, dependency, permission, or external-state failure;
3. make one bounded correction;
4. rerun the smallest decisive check;
5. continue only when the workpack's done condition is supported.

For long commands, announce the target and success criterion before starting. If there is no natural milestone after roughly 90 seconds, send a concise heartbeat; do not let a normal task go about two minutes without human-readable status. These timing values are this repository's collaboration design, not a platform guarantee.

A changed file is not a test; a passing test is not CI; CI is not a build, preview, upload, release, or user acceptance. Use [verification-and-failure-handling.md](references/verification-and-failure-handling.md) and mark missing proof `unknown`.

## Required final state

Use one of:

- `COMPLETE`: every acceptance criterion has fresh, direct evidence;
- `PARTIAL`: useful work is verified, but a bounded nonessential or externally unobservable criterion remains open;
- `BLOCKED`: the next required safe action needs user input or an external state change.

The final report must distinguish local edits, tests, CI, build, preview, upload, merge, release, and user acceptance. Include changed artifacts, intentionally untouched scope, skipped checks, assumptions, risks, blockers, and the one user action if any. Use [workpack-templates.md](references/workpack-templates.md) when a structured report helps.

## Chinese operating example

> 请低交互、高自治地完成这项多阶段改动。
>
> **CHECKPOINT（不等待回复）：** 已完成范围确认和基线审计；正在进入实现；静态验证和安装冒烟尚未运行；当前未提交、未推送。下一次在实施完成或进入验证时汇报。我会继续执行。
>
> 随后直接完成安全工作。只有登录/MFA、权限拒绝、未授权高影响动作或关键事实缺失才建立 `GATE`。

## Red flags

Stop and re-evaluate if you notice:

- a long ordinary task has no human-readable update for about two minutes;
- a checkpoint ends with “reply to continue” even though no gate exists;
- a command log or subagent lifecycle is being used as a progress report;
- a report uses a fake stage denominator or percentage;
- edited, tested, CI, published, or accepted states are conflated;
- repeated subagents produce no bounded batch summary;
- a quiet mode was inferred from “direct execution” or “low interaction”;
- a diagnosis-only request is being changed, deployed, uploaded, or published;
- a failure is repeated without a changed diagnosis;
- user changes, secrets, or private identifiers are exposed.

## Quick checklist

Before execution:

- [ ] Mission, scope, non-goals, side-effect budget, and done conditions are explicit.
- [ ] Observable mode is selected unless quiet is explicitly requested.
- [ ] Kickoff checkpoint is ready; it will not ask for confirmation.
- [ ] Workpacks have disjoint scopes, dependencies, and checks.

During execution:

- [ ] Stage transitions and meaningful failures are reported with new information.
- [ ] Long commands have a preflight note and a bounded heartbeat when needed.
- [ ] Routine work continues after checkpoints.
- [ ] Subagents, if any, have independent roles, bounded count, and a main-thread summary.
- [ ] No out-of-scope edits, secret exposure, or silent authorization expansion occurs.

Before reporting:

- [ ] Edited, tested, built, previewed, uploaded, merged, released, and accepted states are separate.
- [ ] Every claimed check has fresh evidence; unknowns remain visible.
- [ ] The final report is public-safe, concise, and accurate.
