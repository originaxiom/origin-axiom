"""Post-science metadata detector calibration, not a physics certificate."""
import ast
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "scripts/checks/check_test_vacuity.py"
SPEC = importlib.util.spec_from_file_location("carrier_vacuity_detector", PATH)
detector = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(detector)


def lowered(body, base="unittest.TestCase", override=""):
    source = "import unittest\nclass Case(" + base + "):\n" + override + "    def test_math(self):\n        " + body + "\n"
    tree = ast.parse(source)
    fn = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "test_math")
    return source, detector._unittest_assertions(tree, fn)


def test_genuine_methods_lower_to_dynamic_expressions():
    for method, args in (("assertTrue", "compute()"), ("assertFalse", "compute()"),
                         ("assertEqual", "compute(), 2"), ("assertNotEqual", "compute(), 2")):
        _, nodes = lowered("self." + method + "(" + args + ")")
        assert len(nodes) == 1
        assert isinstance(nodes[0], ast.Assert)
        assert not detector._is_literal(nodes[0].test, set())


def test_corrupted_actual_unittest_execution_fails():
    source, nodes = lowered("self.assertEqual(sum([1, 1]), 3)")
    assert len(nodes) == 1
    namespace = {}
    exec(compile(source, "<calibration>", "exec"), namespace)
    result = unittest.TestResult()
    namespace["Case"]("test_math").run(result)
    assert result.testsRun == 1
    assert len(result.failures) == 1
    assert not result.wasSuccessful()


def test_constant_and_syntactic_tautologies_are_not_exempted():
    _, true_nodes = lowered("self.assertTrue(True)")
    _, false_nodes = lowered("self.assertFalse(False)")
    _, eq_nodes = lowered("self.assertEqual(compute(), compute())")
    assert isinstance(true_nodes[0].test, ast.Constant) and true_nodes[0].test.value is True
    assert isinstance(false_nodes[0].test, ast.Constant) and false_nodes[0].test.value is True
    t = eq_nodes[0].test
    assert isinstance(t, ast.Compare) and isinstance(t.ops[0], ast.Eq)
    assert ast.dump(t.left) == ast.dump(t.comparators[0])


def test_arbitrary_and_overridden_methods_stay_outside():
    _, dummy = lowered("self.assertEqual(compute(), 2)", base="object")
    _, overridden = lowered("self.assertEqual(compute(), 2)", override="    def assertEqual(self, *args):\n        pass\n")
    assert dummy == []
    assert overridden == []


def test_original_science_has_eight_nonliteral_asserting_methods():
    science = Path(__file__).with_name("test_physical_bridge_carrier_periphery.py")
    tree = ast.parse(science.read_text())
    funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
    assert len(funcs) == 8
    for fn in funcs:
        nodes = detector._unittest_assertions(tree, fn)
        assert nodes
        assert any(not detector._is_literal(n.test, set()) for n in nodes)
