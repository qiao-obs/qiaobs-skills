# Anonymized case study

## Predicate

An authorized operator can edit a public profile in a simulator. On a real phone, the edit page fails only when the account already has an avatar or background image. The API returns normally. The requested scope is the edit flow; unrelated server deployment is excluded.

## Chain result

- Role and goal: pass; the role is authorized for the setting.
- Real entry and page state: pass until media parsing.
- Permission and API: pass; the expected setting response is returned.
- Shared contract: fail conditionally; the image URL helper assumes a browser constructor.
- Target runtime: fail; the constructor is not guaranteed by the mini-program runtime.
- Build and delivery: unknown until regenerated and uploaded.

The first actionable mismatch is the shared contract/runtime boundary, not an account exception and not the API status.

## Minimal repair

Remove the browser-only dependency from the shared URL validation helper while preserving its security checks. Add a regression case with a real-looking signed media address and a runtime without that constructor. Leave the backend and unrelated pages untouched.

## Evidence record

The original project recorded one repair touching one shared source file and one regression file, with 31 focused checks passing before a front-end upload. Those figures describe that anonymized case only; they are not a performance benchmark or a promise for every project.

## What remains separate

A passing source test does not prove a phone preview, an uploaded package, re-entry, or user acceptance. Each needs its own evidence. If a later layer fails, return to the chain rather than widening the patch.
