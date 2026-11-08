"""Eight synthetic fixtures; no real scientific module or production gate is imported."""
import ast
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
WRAPPER = (HERE / "run_checks.py").read_text()
BRIDGE = (HERE / "checks.py").read_text()
FROZEN_HASH = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"


def expected_literal():
    matches = [node for node in ast.parse(WRAPPER).body if isinstance(node, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == "EXPECTED" for t in node.targets)]
    if len(matches) != 1:
        raise ValueError("Expected exactly one literal method population")
    return ast.literal_eval(matches[0].value)


def source_population():
    tree = ast.parse((HERE / "test_register_architecture.py").read_text())
    return tuple(cls.name + "." + method.name for cls in tree.body
                 if isinstance(cls, ast.ClassDef) for method in cls.body
                 if isinstance(method, ast.FunctionDef) and method.name.startswith("test_"))


def load_fixture(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wrapper_fixture(directory, ending="return 0"):
    root = Path(directory).resolve()
    physical = root / "reports" / "physical_bridge_2026_09_05"
    current = physical / "foundation_selection_2026_11_07" / "verification_architecture_2026_11_08"
    old = physical / "word_architecture_audit_2026_10_17" / "verification_v3"
    current.mkdir(parents=True)
    old.mkdir(parents=True)
    sentinel = ("from pathlib import Path\nimport json\n"
                "ROOT=Path(__file__).resolve().parents[4]\n"
                "marker=ROOT/'imports'\n"
                "marker.write_text((marker.read_text() if marker.exists() else '')+'sentinel\\n')\n"
                "def main():\n"
                "    counter=ROOT/'calls'\n"
                "    counter.write_text(str((int(counter.read_text()) if counter.exists() else 0)+1))\n"
                "    (ROOT/'binding.json').write_text(json.dumps({'here':str(HERE),'entry':ENTRY,'expected':list(EXPECTED)}))\n"
                "    " + ending + "\n")
    infrastructure = old / "run_checks.py"
    infrastructure.write_text(sentinel)
    if WRAPPER.count(FROZEN_HASH) != 1:
        raise ValueError("Ambiguous synthetic hash substitution")
    entry = current / "run_checks.py"
    entry.write_text(WRAPPER.replace(FROZEN_HASH, sha256(sentinel.encode()).hexdigest()))
    return root, infrastructure, entry, load_fixture("synthetic_architecture_wrapper", entry)


def bridge_fixture(directory, missing=False):
    root = Path(directory).resolve()
    current = root / "verification_architecture_2026_11_08"
    current.mkdir()
    lines = ["from pathlib import Path", "import unittest",
             "marker=Path(__file__).resolve().parents[1]/'sentinel_imports'",
             "marker.write_text((marker.read_text() if marker.exists() else '')+'sentinel only\\n')"]
    if not missing:
        lines.append("class RegisterArchitectureControls(unittest.TestCase):")
        for identifier in expected_literal():
            classname, method = identifier.split(".")
            if classname != "RegisterArchitectureControls":
                raise ValueError("Undeclared fixture class")
            lines.extend([f"    def {method}(self):", "        pass"])
    lines.extend(["class UnselectedControls(unittest.TestCase):",
                  "    def test_must_not_be_exported(self):", "        pass"])
    (current / "test_register_architecture.py").write_text("\n".join(lines)+"\n")
    entry = current / "checks.py"
    entry.write_text(BRIDGE)
    return root, entry


class ArchitectureWrapperEngineeringChecks(unittest.TestCase):
    def test_01_deep_path_exact_population_and_one_delegation(self):
        with tempfile.TemporaryDirectory(prefix="architecture-wrapper-") as directory:
            root, _, entry, wrapper = wrapper_fixture(directory)
            self.assertEqual(wrapper.main(), 0)
            record = json.loads((root / "binding.json").read_text())
            self.assertEqual(record["here"], str(entry.parent))
            self.assertEqual(record["entry"], entry.relative_to(root).as_posix())
            self.assertEqual(record["expected"], list(expected_literal()))
            self.assertEqual(len(record["expected"]), 7)
            self.assertEqual((root / "imports").read_text(), "sentinel\n")
            self.assertEqual((root / "calls").read_text(), "1")

    def test_02_changed_infrastructure_rejects_before_import(self):
        with tempfile.TemporaryDirectory(prefix="architecture-wrapper-") as directory:
            root, infrastructure, _, wrapper = wrapper_fixture(directory)
            infrastructure.write_text(infrastructure.read_text()+"# deliberate mutation\n")
            with self.assertRaisesRegex(ValueError, "source hash differs"):
                wrapper.main()
            self.assertFalse((root / "imports").exists())
            self.assertFalse((root / "calls").exists())
            self.assertFalse((root / "binding.json").exists())

    def test_03_missing_infrastructure_rejects_before_import(self):
        with tempfile.TemporaryDirectory(prefix="architecture-wrapper-") as directory:
            root, infrastructure, _, wrapper = wrapper_fixture(directory)
            infrastructure.unlink()
            with self.assertRaises(FileNotFoundError):
                wrapper.main()
            self.assertFalse((root / "imports").exists())
            self.assertFalse((root / "calls").exists())
            self.assertFalse((root / "binding.json").exists())

    def test_04_delegated_nonzero_exit_preserved(self):
        with tempfile.TemporaryDirectory(prefix="architecture-wrapper-") as directory:
            root, _, _, wrapper = wrapper_fixture(directory, "return 7")
            self.assertEqual(wrapper.main(), 7)
            self.assertEqual((root / "calls").read_text(), "1")

    def test_05_delegated_exception_preserved(self):
        with tempfile.TemporaryDirectory(prefix="architecture-wrapper-") as directory:
            root, _, _, wrapper = wrapper_fixture(directory, "raise RuntimeError('sentinel rejection')")
            with self.assertRaisesRegex(RuntimeError, "sentinel rejection"):
                wrapper.main()
            self.assertEqual((root / "calls").read_text(), "1")

    def test_06_static_population_rejects_missing_extra_duplicate(self):
        actual, expected = source_population(), expected_literal()
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 7)
        self.assertEqual(len(set(actual)), 7)

        def require_population(population):
            if sorted(population) != sorted(actual):
                raise ValueError("Sentinel population differs")

        for wrong in (expected[:-1], expected+("Wrong.extra",), expected+(expected[0],)):
            with self.assertRaisesRegex(ValueError, "population differs"):
                require_population(wrong)

    def test_07_synthetic_bridge_exact_class_and_one_import(self):
        with tempfile.TemporaryDirectory(prefix="architecture-bridge-") as directory:
            root, entry = bridge_fixture(directory)
            bridge = load_fixture("synthetic_architecture_bridge", entry)
            suite = unittest.defaultTestLoader.loadTestsFromModule(bridge)
            population = [".".join(test.id().split(".")[-2:]) for group in suite for test in group]
            self.assertEqual(sorted(population), sorted(expected_literal()))
            self.assertEqual(len(population), 7)
            self.assertIs(bridge.RegisterArchitectureControls, bridge.science.RegisterArchitectureControls)
            self.assertEqual((root / "sentinel_imports").read_text(), "sentinel only\n")

    def test_08_missing_bridge_class_rejects(self):
        with tempfile.TemporaryDirectory(prefix="architecture-bridge-") as directory:
            root, entry = bridge_fixture(directory, missing=True)
            with self.assertRaises(AttributeError):
                load_fixture("synthetic_architecture_missing_class", entry)
            self.assertEqual((root / "sentinel_imports").read_text(), "sentinel only\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
