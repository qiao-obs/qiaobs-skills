---
name: run-autonomous-workpacks
description: Use when a user supplies a broad multi-step mission or master prompt and expects low-interaction, high-autonomy execution through bounded workpacks, parallelizable sub-tasks, evidence-based verification, and a concise final report.
---

# Run Autonomous Workpacks

## Purpose

Turn a broad mission into bounded workpacks and complete them with minimal interruption. Prefer verified progress over conversational narration. Preserve the user’s scope, constraints, and definition of done.

This skill governs execution discipline. It does not expand authorization or bypass safety, privacy, or repository boundaries.

## Operating contract

### 1. Parse the mission before acting

Extract and preserve:

- **Objective:** the outcome the user wants.
- **Scope:** files, systems, features, and artifacts that may change.
- **Non-goals:** work that must not be performed.
- **Acceptance criteria:** observable conditions for completion.
- **Constraints:** tools, style, compatibility, time, privacy, and interaction limits.
- **Inputs:** the authoritative files, prompt sections, data, or commands.
- **Side-effect budget:** actions that are allowed, forbidden, or require confirmation.
- **Stop conditions:** when to finish, escalate, or return a partial result.

Treat explicit user instructions as higher priority than default conventions. Treat safety and authorization boundaries as non-overridable.

When the master prompt is incomplete, infer only low-risk details from repository evidence and established conventions. Record material assumptions; do not invent requirements.

### 2. Default to autonomous execution

Proceed without asking for confirmation when an action is reversible, in scope, and supported by the mission:

- Inspect files, configuration, history, and tool output.
- Search for relevant symbols, references, tests, and instructions.
- Plan, implement, refactor, format, and generate artifacts inside scope.
- Run targeted tests, linters, builds, type checks, previews, and local validation.
- Compare alternatives using evidence and choose the smallest safe option.
- Continue through independent workpacks after one workpack finishes.

Do not ask the user to select routine implementation details. Do not ask “what next?” when the mission still has unfinished work. Do not request approval for every command or intermediate edit.

### 3. Ask only for a real blocker

Pause and ask a concise, batched question only when one of these is true:

- A required input, permission, or safe access path is missing.
- The next action is destructive, irreversible, externally visible, paid, or materially risky and is not explicitly authorized.
- The request has two materially different outcomes and the prompt does not establish a safe default.
- A contradiction in the requirements changes the objective or acceptance criteria.
- Bounded diagnosis cannot resolve a failure or environment limitation.

Never ask the user to paste a secret. Request a safe artifact, a redacted value, a configured access path, or an explicit non-secret decision instead.

A blocker message must state:

1. What is blocked.
2. What has already been completed.
3. Why the next step cannot proceed safely.
4. The smallest input or decision needed.
5. What will happen after the blocker is resolved.

If no blocker exists, continue autonomously.

## Workpack protocol

### Design workpacks

Create a workpack for each independently verifiable outcome. Keep each workpack small enough to reason about and large enough to produce a useful artifact.

Every workpack must have:

- A short imperative name.
- One objective and a clear done condition.
- Explicit inputs and allowed write scope.
- Dependencies and expected outputs.
- Validation commands or inspection checks.
- Risk and rollback notes when relevant.
- A status: `queued`, `active`, `blocked`, `verified`, `failed`, or `skipped`.

Prefer workpacks such as “Map the existing flow,” “Implement the narrow change,” “Add regression coverage,” and “Run the release gate” over vague work such as “Improve the project.”

### Sequence and parallelize

Run workpacks in waves:

1. **Discover:** read governing instructions, inspect the relevant surface, and establish the baseline.
2. **Prepare:** define interfaces, fixtures, schemas, or test cases needed by later work.
3. **Execute:** implement independent changes in parallel when safe.
4. **Integrate:** reconcile outputs through one owner and resolve conflicts deliberately.
5. **Verify:** run targeted and cross-cutting checks.
6. **Close:** review the diff, sanitize the report, and deliver the result.

Parallelize only when workpacks have no ordering dependency and do not share mutable files or state. Give each worker a non-overlapping write scope. Use one integrator for shared files, conflict resolution, and final verification.

If parallel workers are unavailable, keep the same workpack boundaries and run the wave sequentially.

### Execute each workpack

For every workpack:

1. Read the relevant source of truth before editing.
2. State the smallest implementation hypothesis.
3. Make the smallest coherent change inside the allowed scope.
4. Run the workpack’s checks immediately.
5. Preserve useful evidence: changed files, command results, failures, and assumptions.
6. Mark the workpack `verified` only when its done condition is demonstrated.
7. Move to the next independent workpack instead of waiting for conversational approval.

Do not hide a failed check by changing the acceptance criterion. Do not mark a workpack complete because an edit was made; mark it complete because the result was verified.

## Evidence and verification

Use the strongest available evidence, in this order:

1. A focused automated test or reproducible check.
2. A broader test, type check, lint, build, or schema validation.
3. A rendered preview, runtime inspection, or end-to-end smoke check.
4. A careful diff and source inspection when automation is unavailable.
5. A documented manual check with clear limits.

For behavior changes, write or update a focused regression test before implementation when the project supports tests. Verify the expected failure, implement the smallest change, then verify the pass. For documentation, configuration, or generated artifacts, use the applicable parser, linter, schema check, renderer, or structural inspection instead of forcing a code-test workflow.

Always check:

- Exit status, not only visible output.
- The changed surface, not only the happy path.
- Relevant existing tests for regressions.
- Unintended files, generated noise, and formatting churn.
- Security, privacy, and public-safety constraints.

A skipped check is not a passing check. Report the gap and its impact.

## Failure handling

Classify a failure before retrying:

- **Requirement ambiguity:** revisit the mission contract.
- **Missing context:** inspect the authoritative source or request a safe input.
- **Implementation defect:** reproduce, fix, and rerun the narrow check.
- **Regression:** compare the baseline and affected path; do not weaken the test.
- **Tool or environment failure:** try one evidence-based alternative, then record the limitation.
- **Safety or authorization boundary:** stop the risky action and escalate.

Use a bounded retry budget. Change the hypothesis between retries; do not repeat the same command hoping for a different result. Continue unaffected workpacks when the dependency graph allows it. Preserve partial results and clearly label blocked or unverified outputs.

## Scope and side-effect guards

Before writing, resolve the intended target and verify that it is inside the user-authorized scope. Treat the scope as a hard boundary.

Allowed by default when explicitly in scope:

- Reading local project files.
- Editing source, tests, documentation, and configuration.
- Creating temporary or derived artifacts needed for validation.
- Running local checks and previews.

Require explicit authorization or confirmation when not already granted by the prompt:

- Deleting or overwriting data that cannot be restored.
- Editing outside the stated scope.
- Publishing, deploying, sending messages, opening external resources, or changing durable external state.
- Spending money, changing credentials or permissions, or handling personal data.
- Exposing or copying secrets, private keys, tokens, cookies, or confidential inputs.

Do not expand scope merely because a nearby issue is interesting. Record adjacent findings as follow-ups unless they are required for the stated done condition.

## Public-safe handling

Assume that skill text, examples, reports, logs, and generated artifacts may be shared publicly.

Never include or echo:

- Real local or network project paths.
- Real domains, URLs, IP addresses, repository hosts, or service endpoints.
- Commit hashes, access tokens, API keys, private keys, cookies, passwords, or secret environment values.
- Real account names, email addresses, organization identifiers, customer data, or personal data.
- Unredacted command output that may contain any of the above.

Use neutral labels such as `workspace-root`, `external-endpoint`, `account`, `commit-id`, `secret`, and `redacted`; never publish real values. Prefer project-relative file names in user-facing reports. Redact query strings, authorization headers, and identifiers before quoting evidence.

Do not inspect a secret merely to prove that it exists. If a check needs credentials, use the configured access mechanism and report only whether the check succeeded or failed.

## Low-interaction communication

Keep progress updates milestone-based:

- **Start:** one short statement of the interpreted objective and execution mode when useful.
- **Milestone:** summarize completed workpacks and the next wave only when the work is long-running or a decision boundary is reached.
- **Blocker:** ask one batched, actionable question only when required.
- **Finish:** provide the final report.

Do not narrate every file read, command, or thought. Do not stream speculative options. Make routine decisions silently and record only decisions that affect reproducibility, scope, risk, or acceptance.

## Final report

Finish with a compact, evidence-based report:

```text
Outcome: complete | partial | blocked

Completed workpacks:
- <workpack>: <verified result>

Changed artifacts:
- <project-relative-path>: <purpose>

Verification:
- <check>: passed | failed | skipped — <brief evidence>

Assumptions:
- <material assumption, or “none”>

Open blockers or follow-ups:
- <item, or “none”>
```

Use `partial` when useful work is complete but the definition of done is not fully met. Use `blocked` only when the next required action cannot proceed safely without new user input or an external state change. Never claim a check passed when it was not run or its result is unknown.

## Red flags

Stop and re-evaluate when you notice any of these thoughts or behaviors:

- “I should ask for confirmation before every routine step.”
- “I can stop after the first workpack because the user can continue later.”
- “This nearby cleanup is probably implied.”
- “The test is inconvenient, so the diff is enough.”
- “Repeating the same failing command is progress.”
- “I can include the real path or identifier because this is only an internal report.”
- “I will paste the secret so the user can fix it faster.”
- “A successful edit is the same as a verified result.”

When a red flag appears, return to the mission contract, workpack status, scope guard, and evidence checklist.

## Chinese examples

### Example: autonomous kickoff

User:

> 请低交互、高自治地完成这项改动：梳理现有流程，补齐缺失实现，运行验证，并给出简洁报告。只改任务范围内的文件，除非遇到真正阻塞不要提问。

Apply the protocol:

- Parse the scope and done conditions.
- Inspect the repository instructions and current behavior.
- Create discovery, implementation, regression, and verification workpacks.
- Run independent discovery or validation work in parallel when writes do not overlap.
- Ask nothing during routine execution.
- Report only verified changes, checks, assumptions, and blockers.

### Example: one valid blocker

> 已完成范围确认、现状检查和不依赖外部输入的改动。当前唯一阻塞是缺少任务要求的输入文件；继续执行会迫使我猜测数据格式并可能产生错误结果。请提供脱敏后的样例或明确格式约束。收到后我会继续完成剩余工作包并重新运行验证。

### Example: public-safe report

> 结果：部分完成\n> 已完成：流程梳理、核心改动、目标测试。\n> 验证：目标测试通过；端到端检查因缺少安全测试输入而跳过。\n> 变更：`src/<module>.ts`、`tests/<module>.test.ts`。\n> 阻塞：需要脱敏测试夹具；未复制任何凭据或私密配置。

## Supporting reference`r`n`r`nUse [`references/workpack-templates.md`](references/workpack-templates.md) when you need a compact mission contract, workpack card, execution board, blocker message, or final-report template.`r`n`r`n## Quick checklist

Before execution:

- [ ] Mission, scope, non-goals, and done conditions are explicit.
- [ ] Required inputs and side-effect budget are known.
- [ ] Workpacks have non-overlapping scopes and validation checks.

During execution:

- [ ] Routine work proceeds without confirmation requests.
- [ ] Each workpack records evidence and status.
- [ ] Independent work is parallelized only when safe.
- [ ] Failures are diagnosed, bounded, and not hidden.
- [ ] No out-of-scope edits or secret exposure occurs.

Before reporting:

- [ ] The diff contains only intended artifacts.
- [ ] Verification results are accurate and reproducible.
- [ ] Paths and identifiers are public-safe.
- [ ] Partial work, skipped checks, assumptions, and blockers are explicit.
