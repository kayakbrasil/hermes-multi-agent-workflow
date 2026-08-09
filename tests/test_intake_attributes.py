"""Tests for generic intake attributes flowing into persistent vault items."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.intake_parser import parse_intake_report  # noqa: E402
from engine.item_vault import ItemVault  # noqa: E402


class TestIntakeAttributes(unittest.TestCase):
    def test_parses_generic_attributes_block(self):
        report = """source: manual
captured_at: 2026-08-09T00:00:00Z

## Candidate: Personal project
Claim: Build a useful application
Sources:
  - url: manual intake
Why it may matter: Supports a personal goal
Attributes:
  objective: Track project work
  target_users: Me
  constraints: No production deployment
  project_type_hint: web_app
"""

        candidate = parse_intake_report(report).candidates[0]

        self.assertEqual(
            candidate.attributes,
            {
                "objective": "Track project work",
                "target_users": "Me",
                "constraints": "No production deployment",
                "project_type_hint": "web_app",
            },
        )

    def test_persists_allowed_attributes_to_item_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = ItemVault(Path(tmp))
            item = vault.create_item(
                slug="personal-project",
                title="Personal project",
                sources=[{"url": "manual intake"}],
                body="Project intake.",
                attributes={"objective": "Track project work"},
            )

            self.assertEqual(item.frontmatter["objective"], "Track project work")
            self.assertEqual(vault.load("personal-project").frontmatter["objective"], "Track project work")

    def test_does_not_allow_attributes_to_overwrite_engine_owned_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = ItemVault(Path(tmp))
            item = vault.create_item(
                slug="personal-project",
                title="Personal project",
                sources=[{"url": "manual intake"}],
                body="Project intake.",
                attributes={"status": "approved", "score": 100, "objective": "Track project work"},
            )

            self.assertEqual(item.frontmatter["status"], "triage")
            self.assertIsNone(item.frontmatter["score"])
            self.assertEqual(item.frontmatter["objective"], "Track project work")


if __name__ == "__main__":
    unittest.main()
