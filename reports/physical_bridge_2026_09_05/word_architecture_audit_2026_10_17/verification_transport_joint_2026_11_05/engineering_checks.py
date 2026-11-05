"""Eight synthetic stdlib fixtures. Real science and production gates stay unloaded."""
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
SCIENTIFIC_FILES = ("verification_transport_end_2026_11_04", "verification_geometric_spin_sector_2026_11_04")


def literal_expected():
    assignments = [node for node in ast.parse(WRAPPER).body if isinstance(node, ast.Assign)
                   and any(isinstance(target, ast.Name) and target.id == "EXPECTED" for target in node.targets)]
    if len(assignments) != 1:
        raise ValueError("EXPECTED must have one literal declaration")
    return ast.literal_eval(assignments[0].value)


def metadata_population():
    population = []
    for directory in SCIENTIFIC_FILES:
        tree = ast.parse((HERE.parent / directory / "checks.py").read_text())
        population.extend(cls.name + "." + method.name for cls in tree.body if isinstance(cls, ast.ClassDef)
                          for method in cls.body if isinstance(method, ast.FunctionDef) and method.name.startswith("test_"))
    return tuple(population)


def load_fixture(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wrapper_fixture(directory, ending="return 0"):
    root = Path(directory).resolve()
    parent = root / "reports" / "physical" / "word"
    current = parent / "verification_transport_joint_2026_11_05"
    old = parent / "verification_v3"
    current.mkdir(parents=True)
    old.mkdir()
    sentinel = ("from pathlib import Path\nimport json\n"
                "ROOT=Path(__file__).resolve().parents[4]\n"
                "marker=ROOT/'imports'\n"
                "marker.write_text((marker.read_text() if marker.exists() else '')+'infrastructure\\n')\n"
                "def main():\n"
                "    counter=ROOT/'calls'\n"
                "    counter.write_text(str((int(counter.read_text()) if counter.exists() else 0)+1))\n"
                "    (ROOT/'binding.json').write_text(json.dumps({'here':str(HERE),'entry':ENTRY,'expected':list(EXPECTED)}))\n"
                "    " + ending + "\n")
    infrastructure = old / "run_checks.py"
    infrastructure.write_text(sentinel)
    if WRAPPER.count(FROZEN_HASH) != 1:
        raise ValueError("Synthetic infrastructure hash substitution is ambiguous")
    entry = current / "run_checks.py"
    entry.write_text(WRAPPER.replace(FROZEN_HASH, sha256(sentinel.encode()).hexdigest()))
    return root, infrastructure, entry, load_fixture("synthetic_joint_wrapper", entry)


def bridge_fixture(directory, missing=None):
    root = Path(directory).resolve()
    current = root / "verification_transport_joint_2026_11_05"
    other = root / "verification_geometric_spin_sector_2026_11_04"
    current.mkdir()
    other.mkdir()
    lines = ["from pathlib import Path", "import unittest", "from types import SimpleNamespace",
             "marker=Path(__file__).resolve().parents[1]/'science_imports'",
             "marker.write_text((marker.read_text() if marker.exists() else '')+'synthetic only\\n')"]
    groups = {}
    for identifier in literal_expected():
        classname, method = identifier.split(".")
        groups.setdefault(classname, []).append(method)
    for classname, methods in groups.items():
        if missing == classname:
            continue
        lines.append(f"class {classname}(unittest.TestCase):")
        for method in methods:
            lines.extend([f"    def {method}(self):", "        pass"])
    lines.extend(["class UnselectedChecks(unittest.TestCase):",
                  "    def test_must_not_be_exported(self):", "        pass"])
    if missing != "TRANSPORT":
        lines.append("TRANSPORT=SimpleNamespace(TransportEndChecks=TransportEndChecks)")
    (other / "checks.py").write_text("\n".join(lines)+"\n")
    entry = current / "checks.py"
    entry.write_text(BRIDGE)
    return root, entry


class JointWrapperEngineeringChecks(unittest.TestCase):
    def test_exact_wrapper_binds_and_delegates_once(self):
        with tempfile.TemporaryDirectory(prefix="joint-wrapper-") as directory:
            root, _, entry, wrapper = wrapper_fixture(directory)
            self.assertEqual(wrapper.main(), 0)
            record = json.loads((root / "binding.json").read_text())
            self.assertEqual(record["here"], str(entry.parent))
            self.assertEqual(record["entry"], entry.relative_to(root).as_posix())
            self.assertEqual(record["expected"], list(literal_expected()))
            self.assertEqual(len(record["expected"]), 13)
            self.assertEqual((root / "imports").read_text(), "infrastructure\n")
            self.assertEqual((root / "calls").read_text(), "1")

    def test_changed_infrastructure_rejects_before_import(self):
        with tempfile.TemporaryDirectory(prefix="joint-wrapper-") as directory:
            root, infrastructure, _, wrapper = wrapper_fixture(directory)
            infrastructure.write_text(infrastructure.read_text()+"# deliberate mutation\n")
            with self.assertRaisesRegex(ValueError, "source hash differs"):
                wrapper.main()
            self.assertFalse((root / "imports").exists())
            self.assertFalse((root / "binding.json").exists())

    def test_missing_infrastructure_rejects_before_delegation(self):
        with tempfile.TemporaryDirectory(prefix="joint-wrapper-") as directory:
            root, infrastructure, _, wrapper = wrapper_fixture(directory)
            infrastructure.unlink()
            with self.assertRaises(FileNotFoundError):
                wrapper.main()
            self.assertFalse((root / "imports").exists())

    def test_nonzero_delegation_propagates(self):
        with tempfile.TemporaryDirectory(prefix="joint-wrapper-") as directory:
            _, _, _, wrapper = wrapper_fixture(directory, "return 7")
            self.assertEqual(wrapper.main(), 7)

    def test_delegated_exception_propagates(self):
        with tempfile.TemporaryDirectory(prefix="joint-wrapper-") as directory:
            _, _, _, wrapper = wrapper_fixture(directory, "raise RuntimeError('synthetic rejection')")
            with self.assertRaisesRegex(RuntimeError, "synthetic rejection"):
                wrapper.main()

    def test_static_method_population_rejects_missing_extra_and_duplicate(self):
        actual, expected = metadata_population(), literal_expected()
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 13)
        self.assertEqual(len(set(actual)), 13)

        def require_population(population):
            if sorted(population) != sorted(actual):
                raise ValueError("Synthetic population differs")

        for wrong in (expected[:-1], expected+("Wrong.extra",), expected+(expected[0],)):
            with self.assertRaisesRegex(ValueError, "population differs"):
                require_population(wrong)

    def test_synthetic_bridge_has_one_source_and_exact_classes(self):
        with tempfile.TemporaryDirectory(prefix="joint-bridge-") as directory:
            root, entry = bridge_fixture(directory)
            bridge = load_fixture("synthetic_joint_bridge", entry)
            suite = unittest.defaultTestLoader.loadTestsFromModule(bridge)
            population = [".".join(test.id().split(".")[-2:]) for group in suite for test in group]
            self.assertEqual(sorted(population), sorted(literal_expected()))
            self.assertEqual(len(population), 13)
            self.assertIs(bridge.TransportEndChecks, bridge.science.TRANSPORT.TransportEndChecks)
            self.assertIs(bridge.GeometricSpinSectorChecks, bridge.science.GeometricSpinSectorChecks)
            self.assertEqual((root / "science_imports").read_text(), "synthetic only\n")

    def test_missing_bridge_attributes_fail(self):
        for missing in ("TRANSPORT", "GeometricSpinSectorChecks"):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory(prefix="joint-bridge-") as directory:
                _, entry = bridge_fixture(directory, missing)
                with self.assertRaises(AttributeError):
                    load_fixture("synthetic_broken_bridge", entry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
