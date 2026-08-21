# Workpack records

These are optional structured records for the work itself. They are not a required conversation format.

## Mission contract

```text
Objective: <observable outcome>
Scope: <allowed files, systems, and artifacts>
Non-goals: <explicit exclusions>
Acceptance criteria:
- <criterion>
- <criterion>
Constraints: <technical, privacy, compatibility, and authorization constraints>
Inputs: <authoritative sources>
Side-effect budget: <allowed | evidence-dependent | forbidden>
Stop conditions: <done, blocked, or escalation conditions>
```

## Workpack card

```text
ID: WP-<number>
Name: <imperative outcome>
Objective: <one independently verifiable result>
Allowed writes: <exact paths>
Untouched scope: <paths that must remain unchanged>
Inputs: <files, records, or prior outputs>
Dependencies: <prior IDs or none>
Risk: <low | medium | high>
Done when: <observable condition>
Checks: <commands, tests, preview, or inspection>
Recovery: <safe retry or route change>
Status: <queued | active | blocked | verified | failed | skipped>
Evidence: <result and artifact>
```

## Dependency board

```text
WP-01 <status> -> WP-02 <status> -> WP-03 <status>
Blocked by: <specific dependency or none>
Ready next: <workpack ID or none>
Untouched scope: <paths>
```

## Verification record

```text
Workpack: <ID>
Claim: <what is being proven>
Evidence: <command, test, artifact, or external record>
Observed: <actual result>
Status: <verified | unknown | failed | skipped>
Does not prove: <next layer that remains open>
```

## Failure and retry record

```text
Workpack: <ID>
Command: <exact command>
Exit code: <number>
First relevant error: <short factual excerpt>
Cause class: <content | environment | dependency | permission | external state>
Bounded correction: <one diagnosed change>
Decisive rerun: <command and result>
Final status: <verified | partial | blocked | failed>
```

## Blocker fact record

```text
Blocker: <specific missing input, permission, or external state>
Evidence: <proof>
Risk: <why guessing is unsafe>
Required input: <smallest non-secret action or fact>
Resume condition: <observable condition>
```

## Closeout record

```text
Outcome: <COMPLETE | PARTIAL | BLOCKED>
Completed workpacks: <IDs and evidence>
Changed artifacts: <paths and purpose>
Untouched scope: <paths>
Verification: <pass, unknown, skipped, or failed by layer>
External actions: <performed, skipped, or blocked with evidence>
Open blockers or follow-ups: <items or none>
```
