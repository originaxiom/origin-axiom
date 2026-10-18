"""Non-scientific runner tests with temporary files and a sentinel module.

Never imports controls.py, checks.py, SymPy or the retained producers.
Admission and Git are mocked ONLY here. This is infrastructure validation,
not a way to admit, execute or certify the mathematical experiment.
"""
from contextlib import ExitStack, redirect_stderr, redirect_stdout
from hashlib import sha256
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("runner_policy_subject", HERE / "run_checks.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class RunnerPolicyChecks(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(self.stack.enter_context(tempfile.TemporaryDirectory(prefix="word-runner-policy-"))).resolve()
        self.loaded = 0
        self.started = 0
        self.dirty = False
        self.module_kind = "pass"
        self.env = {"python": "sentinel-version", "implementation": "sentinel-runtime",
                    "required_environment": {}, "packages": {}}
        self.write("ENVIRONMENT.json", self.env)
        self.design = self.root / "DESIGN.txt"
        self.design.write_text("Non-scientific test fixture, not an experiment design.\n")
        self.spec = {"design": self.pin(self.design), "artifacts": []}
        self.write("SPECIFICATION.json", self.spec)
        self.write("ADMISSION.json", {"specification": self.pin(self.root / "SPECIFICATION.json")})
        self.argv = ["sentinel-entry.py", "--admission", "ADMISSION.json",
                     "--output", "result.jsonl", "--log", "result.log"]
        self.report = {"prospective_admissible": True,
                       "packet": {"experiment_id": "NON_SCIENTIFIC_POLICY_SENTINEL",
                                  "commands": [{"entrypoint": "sentinel-entry.py",
                                                "argv": ["python3", "-B", *self.argv]}],
                                  "outputs": ["result.jsonl", "result.log"]}}
        self.gate = types.SimpleNamespace(returncode=0, stdout=json.dumps(self.report), stderr="")
        self.stack.enter_context(patch.object(runner, "ROOT", self.root))
        self.stack.enter_context(patch.object(runner, "HERE", self.root))
        self.stack.enter_context(patch.object(runner, "ENTRY", "sentinel-entry.py"))
        self.stack.enter_context(patch.object(runner, "EXPECTED", ("Sentinel.test_marker",)))
        self.stack.enter_context(patch.object(runner.platform, "python_version", return_value="sentinel-version"))
        self.stack.enter_context(patch.object(runner.platform, "python_implementation", return_value="sentinel-runtime"))
        self.stack.enter_context(patch.object(runner.sys, "dont_write_bytecode", True))
        self.stack.enter_context(patch.object(runner.sys, "argv", self.argv))
        self.stack.enter_context(patch.object(runner.sys, "path", list(runner.sys.path)))
        self.stack.enter_context(patch.object(runner.subprocess, "run", return_value=self.gate))
        self.stack.enter_context(patch.object(runner, "git", side_effect=self.git))
        loader = types.SimpleNamespace(exec_module=self.load_sentinel)
        self.stack.enter_context(patch.object(runner.importlib.util, "spec_from_file_location",
                                             return_value=types.SimpleNamespace(loader=loader)))
        self.stack.enter_context(patch.object(runner.importlib.util, "module_from_spec",
                                             return_value=types.ModuleType("sentinel_only")))
        original_cwd = Path.cwd()
        self.stack.callback(os.chdir, original_cwd)
        os.chdir(self.root)

    def write(self, name, value):
        (self.root / name).write_text(json.dumps(value))

    def pin(self, path):
        return {"path": path.relative_to(self.root).as_posix(),
                "sha256": sha256(path.read_bytes()).hexdigest()}

    def git(self, *args):
        if args == ("rev-parse", "HEAD"):
            return "non-scientific-sentinel-head"
        if args == ("diff", "--name-only", "HEAD", "--"):
            return "changed.txt" if self.dirty else ""
        raise AssertionError("Undeclared Git call in runner")

    def refresh_gate(self):
        self.gate.stdout = json.dumps(self.report)

    def load_sentinel(self, module):
        self.loaded += 1
        owner = self
        def marker(test):
            owner.started += 1
            if owner.module_kind == "source_change":
                owner.design.write_text("Altered non-scientific fixture.\n")
            if owner.module_kind == "dirty":
                owner.dirty = True
            if owner.module_kind == "expected_failure":
                test.fail("Expected failure must not count as a passing control")
            test.assertEqual(owner.loaded, 1)
        if self.module_kind == "expected_failure":
            marker = unittest.expectedFailure(marker)
        if self.module_kind == "skip":
            marker = unittest.skip("Sentinel deliberately skipped")(marker)
        name = "test_wrong_population" if self.module_kind == "wrong_population" else "test_marker"
        module.Sentinel = type("Sentinel", (unittest.TestCase,), {name: marker})

    def run_subject(self):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return runner.main()

    def assert_no_science_stage(self):
        self.assertEqual(self.loaded, 0)
        self.assertEqual(self.started, 0)
        self.assertFalse((self.root / "result.jsonl").exists())
        self.assertFalse((self.root / "result.log").exists())

    def final_row(self):
        return json.loads((self.root / "result.jsonl").read_text().splitlines()[-1])

    def test_rejected_admission_never_imports(self):
        self.gate.returncode = 1
        self.assertEqual(self.run_subject(), 2)
        self.assert_no_science_stage()

    def test_malformed_report_never_imports(self):
        self.gate.stdout = "not JSON"
        with self.assertRaises(json.JSONDecodeError):
            self.run_subject()
        self.assert_no_science_stage()

    def test_missing_positive_admission_never_imports(self):
        self.report["prospective_admissible"] = False
        self.refresh_gate()
        with self.assertRaisesRegex(ValueError, "Prospective admission missing"):
            self.run_subject()
        self.assert_no_science_stage()

    def test_unadmitted_command_never_imports(self):
        self.report["packet"]["commands"][0]["argv"].append("changed-command")
        self.refresh_gate()
        with self.assertRaisesRegex(ValueError, "exact command"):
            self.run_subject()
        self.assert_no_science_stage()

    def test_unadmitted_output_never_imports(self):
        self.report["packet"]["outputs"].append("extra-output")
        self.refresh_gate()
        with self.assertRaisesRegex(ValueError, "Output population"):
            self.run_subject()
        self.assert_no_science_stage()

    def test_preexisting_output_is_preserved(self):
        previous = "Preserve this prior output.\n"
        (self.root / "result.jsonl").write_text(previous)
        with self.assertRaisesRegex(ValueError, "Output collision"):
            self.run_subject()
        self.assertEqual((self.root / "result.jsonl").read_text(), previous)
        self.assertEqual(self.loaded, 0)
        self.assertFalse((self.root / "result.log").exists())

    def test_changed_pin_never_imports(self):
        self.design.write_text("Changed before admission capture.\n")
        with self.assertRaisesRegex(ValueError, "Input changed"):
            self.run_subject()
        self.assert_no_science_stage()

    def test_changed_runtime_never_imports(self):
        self.env["python"] = "another-version"
        self.write("ENVIRONMENT.json", self.env)
        with self.assertRaisesRegex(ValueError, "Runtime differs"):
            self.run_subject()
        self.assert_no_science_stage()

    def test_wrong_population_halts_before_any_test(self):
        self.module_kind = "wrong_population"
        with self.assertRaisesRegex(ValueError, "control population"):
            self.run_subject()
        self.assertEqual(self.loaded, 1)
        self.assertEqual(self.started, 0)
        self.assertEqual(self.final_row()["stage"], "halted")

    def test_skip_is_not_a_pass(self):
        self.module_kind = "skip"
        self.assertEqual(self.run_subject(), 1)
        self.assertEqual(self.final_row()["skips"], 1)
        self.assertFalse(self.final_row()["passed"])

    def test_expected_failure_is_not_a_pass(self):
        self.module_kind = "expected_failure"
        self.assertEqual(self.run_subject(), 1)
        self.assertEqual(self.final_row()["expected_failures"], 1)
        self.assertFalse(self.final_row()["passed"])

    def test_during_run_source_change_is_not_a_pass(self):
        self.module_kind = "source_change"
        self.assertEqual(self.run_subject(), 1)
        self.assertFalse(self.final_row()["source_unchanged"])
        self.assertFalse(self.final_row()["passed"])

    def test_during_run_tracked_change_is_not_a_pass(self):
        self.module_kind = "dirty"
        self.assertEqual(self.run_subject(), 1)
        self.assertFalse(self.final_row()["source_unchanged"])
        self.assertFalse(self.final_row()["passed"])

    def test_complete_sentinel_run_records_success_without_science(self):
        self.assertEqual(self.run_subject(), 0)
        self.assertEqual((self.loaded, self.started), (1, 1))
        self.assertTrue(self.final_row()["passed"])
        self.assertEqual(self.final_row()["tests_run"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
