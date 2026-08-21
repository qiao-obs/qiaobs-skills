# Verification and failure handling

## Layered evidence

| Evidence | Supports | Does not support |
| --- | --- | --- |
| Source diff | intended source changed | tests or delivery |
| Focused test | covered behavior in that harness | untested inputs or runtime |
| Repository test | configured suite passes | real-device or user acceptance |
| Build result | artifact generated | artifact delivered |
| Preview result | preview channel renders | uploaded or released version |
| Upload result | package accepted by service | review or user entry |
| Release record | named version published | installed result |
| User report | original scenario works for that user | unrelated cases |

## Retry loop

For each failed check:

1. capture the complete command, exit code, and first relevant error;
2. map it to the smallest workpack and the earliest unproven layer;
3. change one diagnosed cause or input;
4. rerun the decisive check;
5. mark `verified` only when the done condition is supported.

A network timeout can be retried once with the same safe request if the operation is idempotent. An authentication or permission failure is not a retry invitation. An ambiguous product decision is not an environment failure.

## Final status rules

- `COMPLETE`: all acceptance criteria have direct evidence.
- `PARTIAL`: the remaining gap is known, bounded, and does not make the verified artifacts misleading.
- `BLOCKED`: the next required action cannot proceed without user input or external state.

Record `unknown` for a check that was not run or cannot be observed. Never turn a likely outcome into a pass.
