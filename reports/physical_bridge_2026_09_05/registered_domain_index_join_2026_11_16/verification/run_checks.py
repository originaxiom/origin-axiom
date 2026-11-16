"""P-C3 runner. Admission and source/checkout checks precede scientific imports."""

import argparse
from contextlib import ExitStack
from hashlib import sha256
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import signal
import subprocess
import sys
import time
import traceback
import unittest


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ENTRY = Path(__file__).resolve().relative_to(ROOT).as_posix()
BASE = (ROOT / "reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17"
        / "verification_v3/run_checks.py")
BASE_SHA256 = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def extra_files():
    entries = set()
    for flags in (("--others", "--exclude-standard"),
                  ("--others", "--ignored", "--exclude-standard")):
        result = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", *flags],
                                capture_output=True, check=True, timeout=30)
        entries.update(path.decode("utf-8", "strict") for path in result.stdout.split(b"\0") if path)
    return entries


def verify_pins(pins):
    for pin in pins:
        relative = Path(pin["path"])
        require(not relative.is_absolute() and ".." not in relative.parts, "Unsafe source pin")
        path = ROOT / relative
        require(path.is_file() and not path.is_symlink(), "Missing regular pinned source: " + str(relative))
        require(sha256(path.read_bytes()).hexdigest() == pin["sha256"],
                "Pinned source mismatch: " + str(relative))


def load_infrastructure():
    require(sha256(BASE.read_bytes()).hexdigest() == BASE_SHA256, "Frozen runner infrastructure differs")
    spec = importlib.util.spec_from_file_location("pc3_custody_infrastructure", BASE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.ROOT == ROOT, "Infrastructure root differs")
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log", required=True)
    args = parser.parse_args()
    require(Path.cwd().resolve() == ROOT, "Run from the repository root")
    require(sys.flags.isolated and sys.dont_write_bytecode and not sys.flags.optimize,
            "Use isolated Python with -I -B, without -O")
    environment = json.loads((HERE / "ENVIRONMENT.json").read_text())
    require(platform.python_implementation() == environment["implementation"] and
            platform.python_version() == environment["python"], "Runtime differs")
    for package, version in environment["packages"].items():
        require(importlib.metadata.version(package) == version, "Runtime dependency differs: " + package)

    specification_path = HERE / "SPECIFICATION.json"
    specification = json.loads(specification_path.read_text())
    pins = [specification["design"], *specification["artifacts"]]
    verify_pins(pins)
    require(not extra_files(), "Untracked or ignored files before admission")
    infrastructure = load_infrastructure()
    before = infrastructure.tracked_state.inspect(ROOT)
    require(before["clean"], "Tracked checkout or index is dirty before admission")

    # Isolated mode removes the script directory. Add only the pinned gate
    # directory explicitly, so its existing sibling imports remain available.
    bootstrap = ("import runpy,sys\n"
                 "sys.path.insert(0,sys.argv.pop(1))\n"
                 "script=sys.argv.pop(1)\n"
                 "runpy.run_path(script,run_name='__main__')\n")
    gate = subprocess.run([sys.executable, "-I", "-B", "-c", bootstrap,
                           str(ROOT / "scripts/gates"), "scripts/gates/prospective_strict.py",
                           "--admission", args.admission], cwd=ROOT, capture_output=True,
                          text=True, timeout=60)
    if gate.returncode:
        print(gate.stdout, end="")
        print(gate.stderr, end="", file=sys.stderr)
        return 2
    report = json.loads(gate.stdout)
    require(report.get("prospective_admissible") is True, "Prospective admission missing")
    admission = json.loads((ROOT / args.admission).read_text())
    expected_specification = {"path": specification_path.relative_to(ROOT).as_posix(),
                              "sha256": sha256(specification_path.read_bytes()).hexdigest()}
    require(admission["specification"] == expected_specification, "Admission binds a different specification")
    command = {"entrypoint": ENTRY,
               "argv": ["python3", "-I", "-B", ENTRY, "--admission", args.admission,
                        "--output", args.output, "--log", args.log]}
    packet = report["packet"]
    require(command in packet["commands"], "This exact command was not admitted")
    require(set(packet["outputs"]) == {args.output, args.log}, "Admitted outputs differ")

    all_pins = [expected_specification, *pins]
    custody = infrastructure.capture_custody(all_pins, before["head_after"])
    require(custody["source_unchanged"] and not extra_files(), "Sources or checkout changed before import")
    outputs = [ROOT / args.output, ROOT / args.log]
    require(outputs[0] != outputs[1], "Output and log paths coincide")
    for relative, path in zip((args.output, args.log), outputs):
        require(not Path(relative).is_absolute() and ".." not in Path(relative).parts,
                "Output path leaves checkout")
        require(not path.exists(), "Output collision; preserve the earlier attempt")
        path.parent.mkdir(parents=True, exist_ok=True)

    expected = json.loads((HERE / "EXPECTED.json").read_text())
    def timeout(signum, frame):
        raise TimeoutError("P-C3 two-minute scientific run limit exceeded")

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(120)
    started = time.monotonic()
    with ExitStack() as stack:
        output = stack.enter_context(outputs[0].open("x", encoding="utf-8"))
        log = stack.enter_context(outputs[1].open("x", encoding="utf-8"))
        def emit(row):
            output.write(json.dumps(row, sort_keys=True) + "\n")
            output.flush()

        emit({"stage": "admitted_start", "admission": report, "custody": custody,
              "expected_tests": expected, "scope": "bounded author controls, independently reviewed execution"})
        try:
            # All scientific imports and test collection occur after the strict gate.
            spec = importlib.util.spec_from_file_location("pc3_exact_checks", HERE / "checks.py")
            checks = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(checks)
            suite = unittest.defaultTestLoader.loadTestsFromModule(checks)
            require(sorted(infrastructure.ids(suite)) == sorted(expected), "Check population differs")
            class RecordedResult(unittest.TextTestResult):
                def startTest(self, test):
                    super().startTest(test)
                    emit({"stage": "test_start", "test": test.id()})

                def addSuccess(self, test):
                    super().addSuccess(test)
                    emit({"stage": "test_pass", "test": test.id()})

            result = unittest.TextTestRunner(stream=log, verbosity=2, failfast=True,
                                            resultclass=RecordedResult).run(suite)
        except BaseException as error:
            traceback.print_exc(file=log)
            emit({"stage": "first_exception", "type": type(error).__name__, "message": str(error)})
            raise
        finally:
            signal.alarm(0)
            primary_error = sys.exc_info()[0] is not None
            try:
                after = infrastructure.capture_custody(all_pins, before["head_after"])
                unexpected = sorted(extra_files() - {args.output, args.log})
                emit({"stage": "final_custody", **after, "unexpected_files": unexpected,
                      "seconds": time.monotonic() - started})
            except BaseException as error:
                try:
                    emit({"stage": "custody_unavailable", "source_unchanged": False,
                          "type": type(error).__name__, "message": str(error)})
                except BaseException:
                    pass
                if not primary_error:
                    raise
        passed = (result.wasSuccessful() and result.testsRun == len(expected)
                  and not result.skipped and not result.expectedFailures
                  and not result.unexpectedSuccesses and after["source_unchanged"] and not unexpected)
        emit({"stage": "finished", "passed": passed, "tests_run": result.testsRun,
              "failures": len(result.failures), "errors": len(result.errors),
              "evidence": "computed once, tested against the specified planted errors if passed",
              "limits": "Finite conditional controls. Physical domains, full spectrum and foundational selection remain separate."})
        return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
