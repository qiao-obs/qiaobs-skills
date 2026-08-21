import unittest
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def test_validator_passes_repository(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skills.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("VALIDATION_PASS", result.stdout)

    def test_exact_skill_set(self):
        names = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
        self.assertEqual(names, {"trace-feature-chain", "run-autonomous-workpacks", "reason-from-reality"})


if __name__ == "__main__":
    unittest.main()
