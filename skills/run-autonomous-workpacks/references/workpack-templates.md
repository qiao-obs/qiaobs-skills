# Workpack Templates

Use these templates to keep autonomous execution bounded, inspectable, and low-interaction. Replace template fields; do not insert real secrets or private identifiers.

## Mission contract

```text
Objective: <observable outcome>
Scope: <allowed files, systems, or artifacts>
Non-goals: <explicit exclusions>
Acceptance criteria:
- <criterion>
- <criterion>
Constraints: <technical, privacy, compatibility, and interaction constraints>
Inputs: <authoritative sources>
Side-effect budget: <allowed | confirmation required | forbidden>
Stop conditions: <done, blocked, or escalation conditions>
```

## Workpack card

```text
ID: WP-<number>
Name: <imperative name>
Objective: <one independently verifiable outcome>
Inputs: <files, outputs, or decisions required>
Allowed writes: <non-overlapping scope>
Dependencies: <workpack IDs or none>
Risk: low | medium | high
Done when:
- <observable condition>
Checks:
- <command, test, inspection, or preview>
Rollback or recovery: <safe recovery note>
Status: queued | active | blocked | verified | failed | skipped
Evidence: <short result after execution>
```

## Execution board

| ID | Workpack | Depends on | Write scope | Status | Evidence |
|---|---|---|---|---|---|
| WP-01 | <name> | — | <scope> | queued | — |
| WP-02 | <name> | WP-01 | <scope> | queued | — |

Use one row per workpack. Do not mark `verified` until the listed check has run and supports the done condition.

## Blocker message

```text
Blocked: <specific next action>
Completed: <work already finished>
Reason: <evidence-based safety, access, or ambiguity reason>
Needed: <smallest safe input or decision>
After unblock: <next workpack and verification>
```

## Final report

```text
Outcome: complete | partial | blocked
Completed workpacks:
- <ID>: <verified result>
Changed artifacts:
- <project-relative-path>: <purpose>
Verification:
- <check>: passed | failed | skipped — <evidence>
Assumptions:
- <material assumption, or none>
Open blockers or follow-ups:
- <item, or none>
```

## Chinese micro-example

```text
WP-02 名称：补齐登录态校验
完成条件：未登录请求得到明确错误；已登录请求保持原行为
验证：运行目标测试，并检查一条未登录和一条已登录路径
写入范围：src/<module>.ts、tests/<module>.test.ts
```
