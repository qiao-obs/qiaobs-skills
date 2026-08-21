---
name: trace-feature-chain
description: Traces a feature from a real user scenario to its release artifact, identifies the first broken link, and defines the smallest safe repair and proof. Use when a role, device, entry point, data shape, permission, runtime, build, preview, upload, or release result does not match expectations.
---

# Trace Feature Chain

## Purpose

Find where reality first diverges from the intended feature contract. Diagnose the cause before editing, keep the change within the requested scope, and prove each claimed layer separately.

## Trigger conditions

Use this skill when:

- A feature works for one role, device, entry point, or data state but fails for another.
- A page error hides whether the fault is in state, identity, permission, API, data, a shared contract, runtime, build, or release.
- Source code changed but the user may still be running an old preview or uploaded artifact.
- The user asks for root-cause tracing, a minimal safe fix, or an honest release boundary.

Do not turn a focused diagnosis into general cleanup or an unrelated deployment.

## Chain to trace

Trace this chain in order, skipping a link only when evidence proves it is irrelevant:

```text
role/account class → business goal → real entry → page state
→ identity/permission/visibility → user command → API
→ backend/database/object storage → shared contract → runtime
→ build artifact → preview/upload/release → re-entry/retry/recovery
```

## Operating procedure

1. **Freeze the scenario predicate.** Record the role or account class, device/runtime, environment, exact entry and action, data/permission/network conditions, unique failure, expected result, and non-goals. Use classes and placeholders; never expose private identifiers.
2. **Reproduce the original path.** Keep the original role, device, entry point, data shape, and failure condition. Do not substitute an easier account, simulator, empty record, or alternate route and call the issue fixed.
3. **Build an evidence matrix.** For every relevant link, record `expected`, `observed`, `evidence`, and `status` (`pass`, `fail`, or `unknown`). See [references/evidence-matrix.md](references/evidence-matrix.md).
4. **Trace upstream from the symptom.** Verify prerequisites one link at a time. Stop at the first observed mismatch; treat later error text, loading states, and retries as consequences until proven otherwise.
5. **Separate facts that are often conflated.** Distinguish identity, permission, visibility, applicability, and authorization. Distinguish frontend, backend, database, object storage, runtime, build, preview, upload, release, and user acceptance.
6. **Probe meaningful boundaries.** Compare only dimensions relevant to the predicate: empty versus non-empty data, ordinary versus special role, simulator versus real device, fresh entry versus re-entry, and online versus degraded network. Check shared contracts when several roles or data shapes can reach the same code.
7. **Choose the smallest safe repair.** Patch the first mismatched layer. Fix shared behavior in the shared layer; never add an account-ID exception for a shared defect. Avoid unrelated refactors, speculative fallbacks, destructive operations, or redeploying an unaffected layer.
8. **Verify in layers.** Run the narrowest useful checks, then re-test the original scenario with the original conditions. Verify generated dependencies/artifacts, preview or upload operations, re-entry, retry, and recovery separately when they are in scope.
9. **Report the boundary honestly.** State what the evidence proves, what it does not prove, what changed, what stayed untouched, and what still requires user or real-device confirmation. Mark missing proof as `unknown`, never as `pass`.

## Guardrails

- Diagnose before editing. Edit only when the user authorizes implementation.
- Return to the original feature path immediately when investigation drifts to an unrelated symptom.
- Do not infer end-to-end success from a reachable page, a successful API response, a passing test, a changed file, a successful build, or a successful preview alone.
- Do not claim that a fix is released until the relevant artifact and release evidence are confirmed.
- Redact secrets, tokens, personal data, private paths, real domains, account identifiers, and commit hashes from public-facing reports and examples.

## Required output

Use this compact structure:

```text
Scenario predicate:
Scope and non-goals:
Chain status:
First mismatch:
Root cause and affected layer:
Minimal safe fix:
Evidence and verification:
Release boundary:
Remaining risks or user checks:
```

Chinese example:

> 平台运营角色在真机上从主界面进入公开资料页并点击编辑；仅在头像或背景图非空时失败，模拟器正常。请找第一处逻辑不匹配，不要只改错误文案，也不要顺手部署无关服务。
