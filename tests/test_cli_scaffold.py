"""Tests for configuration-sensitive scaffold guidance."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cli.triage import cmd_scaffold  # noqa: E402


class TestScaffold(unittest.TestCase):
    def test_manual_intake_config_omits_scout_setup_guidance(self):
        output = StringIO()
        args = type("Args", (), {"config": str(Path(__file__).resolve().parent.parent / "triage.yaml")})()

        with redirect_stdout(output):
            self.assertEqual(cmd_scaffold(args), 0)

        plan = output.getvalue()
        self.assertIn("No source profiles or scout crons are configured", plan)
        self.assertIn("manual intake template", plan)
        self.assertNotIn("triage-scout", plan)
        self.assertNotIn("Register scout crons", plan)


if __name__ == "__main__":
    unittest.main()
