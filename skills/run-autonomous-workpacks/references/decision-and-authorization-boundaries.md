# Decision and authorization boundaries

Use this reference before a mutation, external action, or status change. Work organization and authorization are separate concerns.

## Decision table

| Situation | Default action | Record state |
| --- | --- | --- |
| Read, inspect, search, or compare in scope | Continue | evidence collected |
| Reversible edit inside explicit scope | Continue | workpack active or verified |
| Deterministic test, build, preview, or isolated install | Continue | verification evidence |
| Failed routine command with a bounded diagnosis | Repair and retry | local failure handled |
| Browser login, MFA, or missing human approval | Stop and request the smallest required input | `USER_ONLY` |
| Permission denied by an external service | Stop the external step | `EXTERNAL_WAIT` |
| Paid, destructive, production, public, or irreversible action not explicitly authorized | Do not perform | `UNAUTHORIZED_HIGH_IMPACT` |
| Missing fact changes the safe implementation or target | Gather safe evidence or stop | `MISSING_FACT` |
| Repeated failure remains unexplained | Stop after bounded attempts | `FAILURE_UNRESOLVED` |

## Authorization is not transitive

Approval to edit a repository does not authorize production deployment, publishing a package, changing an account, sending an external message, or deleting data. A successful login proves access, not approval for a particular action.

Workpack execution also does not authorize:

- revealing credentials or private records;
- overwriting unrelated user modifications;
- widening a diagnosis-only request into implementation;
- treating a passing local check as proof of delivery or acceptance;
- hiding an unknown result behind a likely assumption.

## Factual blocker record

When a required input is unavailable, record only facts:

```text
Blocker: <specific missing input, permission, or external state>
Evidence: <command, response, or inspection that proves it>
Risk: <why guessing or proceeding is unsafe>
Required input: <smallest non-secret action or fact needed>
Resume condition: <observable condition for the next workpack>
```

Never paste a secret into this record. Keep the record attached to the affected workpack rather than turning it into a general conversation script.
