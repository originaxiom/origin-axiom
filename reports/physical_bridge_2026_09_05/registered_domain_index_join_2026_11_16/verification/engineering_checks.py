"""Unrun infrastructure fixtures. These never import the mathematical checker."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


class RunnerRejectionChecks(unittest.TestCase):
    def run_fixture(self, kind, expected_message):
        specification = json.loads((HERE / "SPECIFICATION.json").read_text())
        paths = {row["path"] for row in [specification["design"], *specification["artifacts"]]}
        specification_path = (HERE / "SPECIFICATION.json").relative_to(ROOT).as_posix()
        paths.add(specification_path)
        entry = (HERE / "run_checks.py").relative_to(ROOT).as_posix()
        checks_path = (HERE / "checks.py").relative_to(ROOT).as_posix()
        with tempfile.TemporaryDirectory(prefix="pc3-runner-fixture-") as temporary:
            checkout = Path(temporary)
            for relative in sorted(paths):
                target = checkout / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / relative, target)
            marker = checkout / HERE.relative_to(ROOT) / "IMPORTED_SCIENCE"
            sentinel = ("from pathlib import Path\n"
                        "Path(__file__).with_name('IMPORTED_SCIENCE').write_text('imported')\n"
                        "raise RuntimeError('Scientific import escaped preflight')\n")
            (checkout / checks_path).write_text(sentinel)
            if kind != "changed_pin":
                # Make the fixture internally source-complete. Its dirty-file
                # rejection must occur after valid pins, before admission/import.
                for row in specification["artifacts"]:
                    if row["path"] == checks_path:
                        row["sha256"] = sha256(sentinel.encode()).hexdigest()
                (checkout / specification_path).write_text(json.dumps(specification, indent=2) + "\n")
            (checkout / ".gitignore").write_text("fixture.ignored\n")
            commands = (["git", "init", "--quiet", str(checkout)],
                        ["git", "-C", str(checkout), "add", "--all"],
                        ["git", "-C", str(checkout), "-c", "core.hooksPath=/dev/null",
                         "-c", "user.name=originaxiom", "-c", "user.email=fixture@example.invalid",
                         "commit", "--quiet", "-m", "Temporary runner rejection fixture"])
            for command in commands:
                subprocess.run(command, capture_output=True, check=True, timeout=30)
            if kind == "untracked":
                (checkout / "fixture.untracked").write_text("must reject\n")
            if kind == "ignored":
                (checkout / "fixture.ignored").write_text("must reject\n")
            result = subprocess.run([sys.executable, "-I", "-B", entry,
                                     "--admission", "NO_ADMISSION.json",
                                     "--output", "fixture-output.jsonl", "--log", "fixture-output.log"],
                                    cwd=checkout, capture_output=True, text=True, timeout=60)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_message, result.stderr)
            self.assertFalse(marker.exists())
            self.assertFalse((checkout / "fixture-output.jsonl").exists())
            self.assertFalse((checkout / "fixture-output.log").exists())

    def test_changed_pin_rejected_before_scientific_import(self):
        self.run_fixture("changed_pin", "Pinned source mismatch")

    def test_untracked_file_rejected_before_scientific_import(self):
        self.run_fixture("untracked", "Untracked or ignored files before admission")

    def test_ignored_file_rejected_before_scientific_import(self):
        self.run_fixture("ignored", "Untracked or ignored files before admission")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    path = Path(args.output)
    # Open before any fixture is attempted, retaining a collision as an error.
    with path.open("x", encoding="utf-8") as output:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(RunnerRejectionChecks)
        result = unittest.TextTestRunner(stream=output, verbosity=2, failfast=True).run(suite)
        return 0 if result.wasSuccessful() and result.testsRun == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
