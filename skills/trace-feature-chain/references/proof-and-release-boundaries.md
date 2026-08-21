# Proof and release boundaries

Treat each delivery step as a separate claim. A successful earlier layer never proves a later one.

| Claim | What it proves | What it does not prove |
| --- | --- | --- |
| File changed | Source differs from baseline | Tests, build, delivery, or user result |
| Focused test passes | Covered behavior passes in that harness | Untested roles, runtimes, data, or artifacts |
| Full test suite passes | Suite passes under its configured environment | Real-device behavior or current upload |
| Build succeeds | An artifact was generated | That artifact contains the intended fix or reached a user |
| Preview works | A preview channel renders the artifact | Uploaded version or user acceptance |
| Upload succeeds | A package reached the upload service | Review, release, or user entry into that version |
| Release exists | A named version is published | The user has installed or re-entered it |
| User accepts | The stated scenario works for that user | Unrelated scenarios or future regressions |

## Verification order

1. Run the narrow regression that preserves the original predicate.
2. Run repository validation and unit tests.
3. Rebuild generated artifacts when source-to-artifact generation exists.
4. Test the target runtime or preview channel if it is in scope.
5. Confirm upload, release, or acceptance only when the tool result or user report is available.
6. Re-enter through the original path and exercise retry/recovery.

Use `unknown` for a missing layer. Do not rewrite a release claim from `source changed` to `released` by implication.
