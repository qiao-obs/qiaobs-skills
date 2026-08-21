# Communication and progress contract

This reference defines the public communication layer of Observable Autonomy Protocol. It is a repository collaboration design, not an OpenAI platform SLA. The purpose is to reduce interruption without making the work invisible.

## Modes

| Mode | How selected | Normal reporting | Continue? |
| --- | --- | --- | --- |
| `observable` | Default; also triggered by “direct execution,” “low interaction,” or “finish it” | Kickoff, phase checkpoints, meaningful failure/route changes, bounded heartbeat, blockers, final | Continue unless a real `GATE` exists |
| `quiet` | Only when the user explicitly requests silent execution | Required warnings, real blockers, final; no routine heartbeat | Continue unless a real `GATE` exists |
| `high-visibility` | Only when the user asks to follow progress closely | More detailed phase updates, still not every command | Continue unless a real `GATE` exists |

“Direct execution” means do not return routine work to the user. “Do not ask at every step” means do not request approval after each action. Neither phrase means “say nothing.”

## CHECKPOINT versus GATE

| Type | Meaning | Wait for user? | Example |
| --- | --- | --- | --- |
| `CHECKPOINT` | Informational state update | No; send and continue | Baseline frozen, implementation complete, verification starting |
| `GATE` | Blocking authorization or input boundary | Yes | MFA, permission denial, unapproved production action, material missing fact |

Never write a checkpoint as “please confirm whether to continue.” Never suppress a checkpoint merely to avoid creating a gate.

## Required update triggers

### Kickoff

Before the first substantive tool call or subagent, send:

```text
开始｜<任务名>
目标：<one-sentence done condition>
路径：<3–6 real phases>
当前：<first phase>
用户操作：无；除真实阻塞外我会继续执行。
下次汇报：<first milestone or bounded heartbeat>
```

For a task that takes less than about two minutes and has only one or two actions, kickoff plus final is enough.

### Phase checkpoint

Send a `CHECKPOINT` when baseline discovery is frozen, work moves from discovery to implementation, a workpack or wave completes, verification starts, a key assumption is disproven, a plan denominator changes, local gates finish before an external action, or an external action completes.

Every meaningful checkpoint states:

- what is verified complete;
- what is active;
- what is not yet verified;
- the real commit/push/PR/merge/release state;
- the next action and whether user input is needed.

### Heartbeat

For an interactive task expected to run beyond two minutes:

- target a new-information heartbeat if no natural milestone occurs for roughly 90 seconds;
- do not normally exceed about two minutes without a human-readable state;
- before a command likely to take more than about 60 seconds, state what is running, why, the success criterion, and the next status point;
- when a session can yield and be polled, keep the polling interval within the visibility budget.

The 90-second target and two-minute ceiling are design guidance for this repository, not a guaranteed timer exposed by the host.

A heartbeat must add information. “Still working” alone is not a heartbeat.

## User asks for status

Prioritize the request at the next safe boundary. Answer before starting another long command. Include:

- current phase and frozen total, or explain why the denominator changed;
- verified workpacks, active work, and queued work;
- changed artifacts or change scale;
- checks already run and checks not run;
- commit, push, PR, CI, merge, release, and acceptance state;
- blockers and required user action;
- next step.

Do not answer only “still running,” and do not make the user infer status from tool events.

## Long commands, failures, and route changes

Before a long build, test, render, install, or web check, announce the target and success criterion. After it returns, report the actual exit result promptly.

Send a checkpoint when:

- the first key assumption is disproven;
- the same route fails repeatedly and a new route is chosen;
- a check cannot run and evidence quality drops;
- a local blocker leaves independent work possible;
- the scope, risk, denominator, or completion definition changes.

State the failure fact, diagnosis, new route, and effect on scope or evidence. Do not repeat an unchanged command and do not hide a skipped check.

## Subagent visibility

Subagents are optional optimization, not a default behavior. Use them only when tasks are independent, the speed or independent review value justifies coordination, write scopes do not conflict, and the main thread can integrate and verify the output.

- Default to no more than three active subagents.
- Before starting a batch, send a checkpoint with count, roles, write boundaries, and main-thread work.
- Report a batch summary, not each creation or shutdown event.
- State how many returned, which findings were adopted, which were rejected or unresolved, and how the main thread will integrate them.
- The main thread owns final verification and communication.

Example:

```text
进度 2/5｜并行审计完成 2/3
已返回：文档审计、评测审计；发现 4 个需整合项。
仍在运行：视觉资产检查。
主线程正在：合并不冲突结论，尚未进入发布。
用户操作：无；我会继续。
```

## Templates

### Milestone checkpoint

```text
进度 <phase>/<total>｜<phase name>
已完成：<verified result>
正在进行：<active work and purpose>
验证：<passed checks>; <unrun or unknown checks>
发布状态：<edited / tested / committed / pushed / PR / CI / merged / released>
接下来：<next action>
用户操作：无，我会继续；或 <one real gate action>
```

### Heartbeat

```text
仍在 <phase>/<total>｜<phase name>
新增进展：<new evidence since last update>
当前问题：<none, or bounded failure and route change>
验证：<current evidence>; <remaining unknown>
接下来：<next action>
用户操作：无；最迟约两分钟后或下个里程碑再次更新。
```

### Status on request

```text
当前：<phase>/<total>, <workpack statuses>
已验证：<completed evidence>
正在进行：<active item>
尚未验证：<specific checks>
发布状态：<real VCS/PR/CI/release state>
阻塞：<none, or GATE reason>
下一步：<specific action>
用户操作：<none, or one smallest action>
```

### GATE

```text
需要你处理｜GATE：<specific boundary>
已完成：<safe work independent of the gate>
为什么必须停：<evidence and risk>
请只做：<one smallest safe action; never request a secret in chat>
完成标准：<observable result>
你回复后我将：<next workpack and verification>
```

### Final report

```text
Outcome: COMPLETE | PARTIAL | BLOCKED
Completed workpacks:
Changed artifacts:
Verification:
Commit / push / PR / CI / merge / release:
Assumptions:
Open blockers or follow-ups:
User action required:
```

## Anti-patterns

- A routine long task has no human-readable state for about two minutes.
- Every checkpoint waits for a “continue” reply.
- A command log, progress spinner, or subagent lifecycle is presented as the update.
- A fake denominator or percentage is used without an objective basis.
- “Still working” is sent without new information.
- Edited, tested, CI, published, or accepted are conflated.
- Quiet mode is inferred from ordinary low-interaction wording.
- Several subagents are started and stopped without a batch summary.
- The final report is the first human-readable state after a long task.
