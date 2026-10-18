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
sys.path.insert(0, str(ROOT / "scripts" / "gates"))
import tracked_state

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
    "ActualJoinChecks.test_retained_rank_match_span_and_determinant_countercontrols",
    "ActualJoinChecks.test_retained_algebra_and_root_instrument_controls",
    "LiftFamilyChecks.test_all_four_fixed_pairs_and_their_transported_boundaries",
    "LiftFamilyChecks.test_independent_lifts_add_inner_moves_and_the_old_loop_survives",
    "LiftFamilyChecks.test_relative_register_is_a_crossed_not_ordinary_product",
    "LiftFamilyChecks.test_chronological_register_reverses_algebraic_word_order",
    "LiftFamilyChecks.test_changing_frames_retains_both_path_endpoints",
    "InfiniteHistoryChecks.test_all_positive_prefixes_through_depth_nine_are_nested_cones",
    "InfiniteHistoryChecks.test_golden_recovery_and_constant_letter_endpoint_controls",
    "InfiniteHistoryChecks.test_chronological_blocks_have_opposite_endpoint_bounds",
    "InfiniteHistoryChecks.test_symmetric_stationary_laws_do_not_fix_history_correlations",
    "InfiniteHistoryChecks.test_complementary_coordinates_translate_intervals_and_bounds",
    "GraphJoiningChecks.test_edge_matching_preserves_nontrivial_loop_transport",
    "GraphJoiningChecks.test_finite_graph_cohomology_consequences_and_disconnected_control",
    "GraphJoiningChecks.test_cubic_sign_depends_on_the_fibre_tensor_not_its_name",
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


def capture_custody(pins, head):
    mismatches, errors = [], {}
    for row in pins:
        try:
            actual = sha256((ROOT / row["path"]).read_bytes()).hexdigest()
            if actual != row["sha256"]:
                mismatches.append(row["path"])
        except (OSError, ValueError) as error:
            errors[row["path"]] = type(error).__name__ + ": " + str(error)
    state = tracked_state.inspect(ROOT, expected_head=head)
    return {"pin_mismatches": mismatches, "pin_errors": errors,
            "tracked_state": state,
            "source_unchanged": not mismatches and not errors and state["clean"]}


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

    # Independently check the index before the unchanged base-policy gate.
    before = tracked_state.inspect(ROOT)
    require(before["clean"], "Strict tracked state is not clean before admission")
    # This strengthened checker performs no scientific import or execution.
    gate = subprocess.run([sys.executable, "-B", "scripts/gates/prospective_strict.py",
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
    head = before["head_after"]
    preimport = capture_custody(pins, head)
    require(preimport["source_unchanged"], "Sources or strict tracked state changed after admission")
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
              "preimport_custody": preimport,
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
        except BaseException as error:
            try:
                traceback.print_exc(file=log)
                emit({"stage": "halted", "error_type": type(error).__name__, "message": str(error)})
            except BaseException:
                # A reporting failure must not mask the original failure.
                pass
            raise
        finally:
            primary_error = sys.exc_info()[0] is not None
            try:
                custody = capture_custody(pins, head)
                emit({"stage": "custody", **custody})
            except BaseException as error:
                try:
                    emit({"stage": "custody_unavailable", "source_unchanged": False,
                          "error_type": type(error).__name__, "message": str(error)})
                except BaseException:
                    pass
                if not primary_error:
                    raise
        unchanged = custody["source_unchanged"]
        passed = (result.wasSuccessful() and result.testsRun == len(EXPECTED)
                  and not result.skipped and not result.expectedFailures
                  and not result.unexpectedSuccesses and unchanged)
        emit({"stage": "finished", "passed": passed, "tests_run": result.testsRun,
              "failures": len(result.failures), "errors": len(result.errors),
              "skips": len(result.skipped), "expected_failures": len(result.expectedFailures),
              "unexpected_successes": len(result.unexpectedSuccesses), "source_unchanged": unchanged,
              "scope": "Exact bounded controls and reviewed-proof safeguards, not physical realization or independent proof acceptance"})
        print(json.dumps({"passed": passed, "tests_run": result.testsRun}))
        return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
