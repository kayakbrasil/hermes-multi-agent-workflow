"""Tests for generic item lifecycle transitions at the end of fulfillment."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import proposal_actions  # noqa: E402
from engine.item_vault import ItemVault  # noqa: E402


class TestFinalFulfillmentLifecycle(unittest.TestCase):
    def test_final_fulfillment_marks_approved_item_completed(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = ItemVault(Path(tmp))
            item = vault.create_item(
                slug="generic-item",
                title="Generic item",
                sources=[{"url": "manual"}],
                body="Approved work.",
            )
            item.frontmatter["status"] = "approved"
            item.frontmatter["path"] = "software_project"
            vault.save(item)

            with patch.object(proposal_actions, "vault_dir", return_value=Path(tmp)):
                result = proposal_actions.action_complete("generic-item")

            saved = vault.load("generic-item")
            self.assertTrue(result["ok"])
            self.assertEqual(saved.frontmatter["status"], "completed")
            self.assertIn("completed_at", saved.frontmatter)
            self.assertIn("Fulfillment completed", saved.body)


if __name__ == "__main__":
    unittest.main()
