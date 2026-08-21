# Origins and method

## Public-safe origin

These skills were distilled from a long-running, anonymized campus information mini-program. The source experience included role-specific failures, simulator-versus-real-device differences, shared data-contract bugs, build/release confusion, and repeated handoff cost. This repository keeps only the transferable method. It does not publish private logs, identifiers, credentials, infrastructure details, real domains, account data, or commit identifiers.

## The reusable method

A useful diagnosis starts by freezing a **scenario predicate**: role or account class, device/runtime, real entry point, data shape, unique failure, and expected result. It then traces:

```text
role → business goal → real entry → page state → identity/permission facts
→ user command → API → backend/database facts → object storage
→ shared contract → runtime → build artifact → preview/upload/release
→ result after re-entry → recovery/retry
```

For every link, record expected, actual, evidence, and status. Stop at the first mismatch. A shared contract defect belongs in the shared layer, not in an account-specific exception. A front-end runtime defect does not justify redeploying an unrelated server. A changed file is not the same thing as a changed build, preview, upload, deployment, or user-accepted release.

## What was deliberately removed

The public materials use generic roles such as “operator” and “member,” generic media URLs, and an anonymized campus platform. They omit real people, schools, account IDs, URLs, tokens, logs, screenshots, storage keys, server addresses, and private worktree paths.
