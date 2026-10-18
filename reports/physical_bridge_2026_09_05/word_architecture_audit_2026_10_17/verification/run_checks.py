"""Prospective-gated entrypoint; no science imports before real admission.

This is a proposed wrapper, not a replacement for repository policy.
Missing acceptance, dirty tracked state or incomplete test coverage fails.
"""
import argparse
from contextlib import ExitStack
from hashlib import sha256
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback
import unittest


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ENTRY = Path(__file__).resolve().relative_to(ROOT).as_posix()
EXPECTED = (
    "PartialRecordChecks.test_definedness_is_observable_even_with_constant_output",
    "PartialRecordChecks.test_later_output_and_later_definedness_are_both_checked",
    "PartialRecordChecks.test_all_two_state_two_update_binary_output_machines",
    "PartialRecordChecks.test_malformed_domains_fail_closed",
    "WordLiftChecks.test_inverses_and_boundary_fixing_on_actual_word_generators",
    "WordLiftChecks.test_same_homology_sign_different_based_boundary_action",
    "RelativePlacementChecks.test_polynomial_family_and_commutator_identity",
    "RelativePlacementChecks.test_double_coset_changes_preserve_product_class",
    "RelativePlacementChecks.test_additive_commutator_formula_before_specialization",
    "RelativePlacementChecks.test_all_three_nondegenerate_integral_branches",
    "RelativePlacementChecks.test_degenerate_locus_does_not_have_a_universal_sign_or_rank",
    "RelativePlacementChecks.test_complex_trace_equivalence_does_not_erase_integral_orientation",
    "RelativePlacementChecks.test_literal_mirror_gluing_inequality_is_not_a_chirality_certificate",
    "ActualJoinChecks.test_actual_field_and_all_three_retained_joins",
    "ActualJoinChecks.test_separate_frame_change_needs_its_intertwiner",
    "ActualJoinChecks.test_compatible_bend_is_not_automatically_a_common_frame_change",
    "ActualJoinChecks.test_interface_roster_and_singular_frame_are_rejected",
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def ids(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from ids(item)
        else:
            yield ".".join(item.id().split(".")[-2:])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log", required=True)
    args = parser.parse_args()
    require(Path.cwd().resolve() == ROOT, "Run from the repository root")
    require(sys.dont_write_bytecode and not sys.flags.optimize, "Use -B, without -O")
    env = json.loads((HERE / "ENVIRONMENT.json").read_text())
    require(platform.python_version() == env["python"] and
            platform.python_implementation() == env["implementation"], "Runtime differs from the design")
    for name, value in env["required_environment"].items():
        require(os.environ.get(name) == value, "Required environment differs: " + name)
    for name, value in env["packages"].items():
        require(importlib.metadata.version(name) == value, "Dependency version differs: " + name)

    # This checker performs no scientific import or execution.
    gate = subprocess.run([sys.executable, "-B", "scripts/gates/prospective.py",
                           "--admission", args.admission], cwd=ROOT, capture_output=True, text=True)
    if gate.returncode != 0:
        print(gate.stdout, end="")
        print(gate.stderr, end="", file=sys.stderr)
        return 2
    report = json.loads(gate.stdout)
    require(report.get("prospective_admissible") is True, "Prospective admission missing")
    packet = report["packet"]
    command = {"entrypoint": ENTRY, "argv": ["python3", "-B", ENTRY, "--admission", args.admission,
                                             "--output", args.output, "--log", args.log]}
    require(command in packet["commands"], "This exact command was not admitted")
    require(set(packet["outputs"]) == {args.output, args.log}, "Output population differs")
    admission = json.loads((ROOT / args.admission).read_text())
    specification = json.loads((ROOT / admission["specification"]["path"]).read_text())
    pins = [admission["specification"], specification["design"]] + specification["artifacts"]
    def pinned_now():
        return all(sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"] for row in pins)
    require(pinned_now(), "Input changed after admission")
    head = git("rev-parse", "HEAD")
    outputs = [ROOT / args.output, ROOT / args.log]
    for path in outputs:
        require(not path.exists(), "Output collision; preserve prior attempt")
        path.parent.mkdir(parents=True, exist_ok=True)
    with ExitStack() as stack:
        output = stack.enter_context(outputs[0].open("x", encoding="utf-8"))
        log = stack.enter_context(outputs[1].open("x", encoding="utf-8"))
        def emit(row):
            output.write(json.dumps(row, sort_keys=True) + "\n")
            output.flush()
        emit({"stage": "admitted_start", "head": head, "admission_report": report,
              "expected_tests": list(EXPECTED), "time": time.time()})
        try:
            # Imports and collection occur only after the accepted gate.
            sys.path.insert(0, str(HERE))
            module_spec = importlib.util.spec_from_file_location("word_join_checks", HERE / "checks.py")
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            suite = unittest.defaultTestLoader.loadTestsFromModule(module)
            population = list(ids(suite))
            require(sorted(population) == sorted(EXPECTED), "Incomplete or changed control population")
            class RecordedResult(unittest.TextTestResult):
                def startTest(self, test):
                    super().startTest(test)
                    emit({"stage": "test_start", "test": test.id()})
                def addSuccess(self, test):
                    super().addSuccess(test)
                    emit({"stage": "test_pass", "test": test.id()})
            result = unittest.TextTestRunner(stream=log, verbosity=2, failfast=True,
                                            resultclass=RecordedResult).run(suite)
            unchanged = pinned_now() and git("rev-parse", "HEAD") == head and not git("diff", "--name-only", "HEAD", "--")
            passed = (result.wasSuccessful() and result.testsRun == len(EXPECTED)
                      and not result.skipped and not result.expectedFailures
                      and not result.unexpectedSuccesses and unchanged)
            emit({"stage": "finished", "passed": passed, "tests_run": result.testsRun,
                  "failures": len(result.failures), "errors": len(result.errors),
                  "skips": len(result.skipped), "expected_failures": len(result.expectedFailures),
                  "unexpected_successes": len(result.unexpectedSuccesses), "source_unchanged": unchanged,
                  "scope": "Exact bounded controls and received-proof checks, not physical selection or independent proof acceptance"})
            print(json.dumps({"passed": passed, "tests_run": result.testsRun}))
            return 0 if passed else 1
        except BaseException as error:
            traceback.print_exc(file=log)
            emit({"stage": "halted", "error_type": type(error).__name__, "message": str(error)})
            raise


if __name__ == "__main__":
    raise SystemExit(main())
