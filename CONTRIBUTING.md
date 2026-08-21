# Contributing

Thanks for helping improve `qiaobs-skills`.

## Before opening a pull request

1. Keep each Skill a coherent task unit with a precise trigger boundary.
2. Do not add credentials, private paths, real user data, telemetry, hidden network calls, or copied third-party text.
3. Update references and examples when behavior changes.
4. Run:

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

5. Explain what evidence changed and which claims remain unknown.

## Pull requests

Use the template. Keep changes focused, describe trigger-boundary changes explicitly, and include a validation transcript or explain why a check could not run.
