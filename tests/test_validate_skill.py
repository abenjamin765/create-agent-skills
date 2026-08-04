from __future__ import annotations

import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "skills/create-agent-skill/scripts/validate_skill.py"
SPEC = importlib.util.spec_from_file_location("validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidateSkillTests(unittest.TestCase):
    def test_valid_minimal_skill(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = pathlib.Path(temp) / "sample-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: sample-skill\n"
                "description: Reviews samples. Use when a sample review is requested.\n"
                "---\n\n# Workflow\n\nReview the sample.\n",
                encoding="utf-8",
            )
            self.assertEqual([], VALIDATOR.validate(skill))

    def test_rejects_bad_name_and_missing_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = pathlib.Path(temp) / "Bad_Name"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: Bad_Name\n"
                "description: Use when testing invalid packages.\n"
                "---\n\nRead [missing](references/missing.md).\n",
                encoding="utf-8",
            )
            errors = VALIDATOR.validate(skill)
            self.assertTrue(any("name must" in error for error in errors))
            self.assertTrue(any("missing referenced file" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
