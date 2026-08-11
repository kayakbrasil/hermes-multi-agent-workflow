"""Tests for the standalone cost-report diagnostic."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class TestCostReport(unittest.TestCase):
    def test_help_runs_outside_repository_root(self):
        repo_root = Path(__file__).resolve().parent.parent
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(repo_root / "scripts" / "cost_report.py"), "--help"],
                cwd=tmp,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Per-item spend report", result.stdout)


if __name__ == "__main__":
    unittest.main()
