# Decision and authorization boundaries

Use this reference before a mutation, external action, or user interruption. Communication and authorization are different layers.

## CHECKPOINT versus GATE

- `CHECKPOINT` is an informational progress message. Send it and continue without waiting.
- `GATE` is a real authorization or input boundary. State the smallest user action and wait.

A checkpoint must never end with “should I continue?” A low-interaction request defaults to visible `CHECKPOINT` updates, not silent execution.

## Decision table

| Situation | Default action | Report state |
| --- | --- | --- |
| Read, inspect, search, or compare in scope | Continue | evidence collected; checkpoint when the phase changes |
| Reversible edit inside explicit scope | Continue | workpack active or verified |
| Deterministic test/build/preview | Continue | verification evidence |
| Failed routine command with a bounded diagnosis | Repair and retry | local failure handled; checkpoint if route changes |
| Browser login, MFA, or missing human approval | Stop and ask once | `USER_ONLY` / `GATE` |
| Permission denied by an external service | Stop external step | `EXTERNAL_WAIT` / `GATE` |
| Paid, destructive, production, or irreversible action not explicitly authorized | Do not perform | `UNAUTHORIZED_HIGH_IMPACT` / `GATE` |
| Missing fact changes the safe implementation or target | Gather safe evidence or stop | `MISSING_FACT` / `GATE` |
| Repeated failure remains unexplained | Stop after bounded attempts | `FAILURE_UNRESOLVED` / `BLOCKED` |

## Authorization is not transitive

Approval to edit a repository does not authorize production deployment, publishing a package, changing an account, sending an external message, or deleting data. A successful login proves access, not that a particular action is approved.

Low-interaction execution also does not authorize:

- revealing credentials or private records;
- overwriting user modifications;
- force-pushing or rewriting history;
- deploying a server or uploading a client artifact outside the requested scope;
- changing a neighboring feature because it looks related.

When the mission explicitly authorizes a public branch, pull request, merge, or release, perform those actions only after the stated local and CI gates pass. If GitHub settings, review requirements, or another external state blocks the sequence, report the exact remaining action instead of claiming completion.

## User-only gate message

```text
需要你处理｜GATE：<specific boundary>
已完成：<safe work already finished>
为什么必须停：<evidence-based reason>
请只做：<smallest safe action; never paste a secret>
完成标准：<observable result>
你回复后我将：<next workpack and verification>
```
