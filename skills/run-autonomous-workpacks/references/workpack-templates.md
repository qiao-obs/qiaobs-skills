# Workpack templates

## Kickoff checkpoint

```text
开始｜<任务名>
目标：<一句话完成定义>
路径：<3—6 个真实阶段>
当前：<第一个阶段>
用户操作：无；除真实阻塞外我会继续执行。
下次汇报：<第一个里程碑或有界心跳>
```

A kickoff is an informational `CHECKPOINT`, not a request to continue.

## Mission contract

```text
Objective: <observable outcome>
Scope: <allowed files, systems, and artifacts>
Non-goals: <explicit exclusions>
Acceptance criteria:
- <criterion>
- <criterion>
Constraints: <technical, privacy, compatibility, and interaction constraints>
Inputs: <authoritative sources>
Mode: observable | quiet | high-visibility
Side-effect budget: <allowed | evidence-dependent | forbidden>
Stop conditions: <done, blocked, or escalation conditions>
```

## Milestone checkpoint

```text
进度 <phase>/<total>｜<phase name>
已完成：<verified result>
正在进行：<active work and purpose>
验证：<passed checks>; <unrun or unknown checks>
发布状态：<edited / tested / committed / pushed / PR / CI / merged / released>
接下来：<next action>
用户操作：无，我会继续；或 <one real gate action>
```

## Heartbeat

```text
仍在 <phase>/<total>｜<phase name>
新增进展：<new information>
当前问题：<none, or bounded failure and route change>
验证：<current evidence>; <remaining unknown>
接下来：<next action>
用户操作：无；最迟约两分钟后或下个里程碑再次更新。
```

## Subagent batch checkpoint

```text
进度 <phase>/<total>｜并行审计完成 <returned>/<total>
已返回：<roles and useful findings>
仍在运行：<roles, or none>
主线程正在：<integration and final verification>
用户操作：无，我会继续。
```

Use a batch summary, not a stream of creation and shutdown events. Keep the default active count at three or fewer.

## Status on request

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

## Blocker gate

```text
需要你处理｜GATE：<具体门槛>
已完成：<不依赖该门槛的安全工作>
为什么必须停：<证据与风险>
请只做：<一个最短、可执行动作；不要索取秘密>
完成标准：<可观察结果>
你回复后我将：<继续的工作包和验证>
```

## Final report

```text
Outcome: COMPLETE | PARTIAL | BLOCKED
Completed workpacks:
- <ID>: <verified result>
Changed artifacts:
- <path>: <purpose>
Verification:
- <check>: PASS | FAIL | SKIPPED — <evidence>
Commit / push / PR / CI / merge / release:
- <real status for each layer>
Assumptions:
- <material assumption, or none>
Open blockers or follow-ups:
- <item, or none>
User action required: <none, or one unavoidable action>
```

Use generic labels in public examples. Never place secrets, private paths, account IDs, or real infrastructure identifiers in a card.
