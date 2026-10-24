"""Six synthetic software fixtures. Never import science or production gates."""
import ast
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
SOURCE = (HERE / "run_checks.py").read_text()


def literal_expected(source):
    tree = ast.parse(source)
    rows = [node for node in tree.body if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "EXPECTED"
                    for target in node.targets)]
    if len(rows) != 1:
        raise ValueError("EXPECTED declaration missing or ambiguous")
    return ast.literal_eval(rows[0].value)


def fixture(directory, mode="return 0"):
    # Match the production wrapper's resolved-path convention, including
    # macOS /var -> /private/var aliases; do not weaken its binding check.
    root = Path(directory).resolve()
    parent = root / "reports" / "physical" / "word"
    current = parent / "verification_p210"
    old = parent / "verification_v3"
    current.mkdir(parents=True)
    old.mkdir()
    sentinel = ('from pathlib import Path\nimport json\n'
                'ROOT = Path(__file__).resolve().parents[4]\n'
                'marker = ROOT / "imported"\n'
                'marker.write_text((marker.read_text() if marker.exists() else "") + "synthetic infrastructure only\\n")\n'
                'def main():\n'
                '    counter = ROOT / "calls"\n'
                '    counter.write_text(str((int(counter.read_text()) if counter.exists() else 0) + 1))\n'
                '    (ROOT / "binding.json").write_text(json.dumps({\n'
                '        "here": str(HERE), "entry": ENTRY, "expected": list(EXPECTED)}))\n'
                '    ' + mode + '\n')
    infrastructure = old / "run_checks.py"
    infrastructure.write_text(sentinel)
    original_hash = "1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0"
    if SOURCE.count(original_hash) != 1:
        raise ValueError("Synthetic hash substitution is not unique")
    copied = SOURCE.replace(original_hash, sha256(sentinel.encode()).hexdigest())
    entry = current / "run_checks.py"
    entry.write_text(copied)
    spec = importlib.util.spec_from_file_location("p210_synthetic_wrapper", entry)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return root, infrastructure, entry, module


class WrapperEngineeringChecks(unittest.TestCase):
    def test_exact_fixture_source_binds_once_and_only_to_its_packet(self):
        with tempfile.TemporaryDirectory(prefix="p210-engineering-") as directory:
            root, _, entry, wrapper = fixture(directory)
            self.assertEqual(wrapper.main(), 0)
            record = json.loads((root / "binding.json").read_text())
            self.assertEqual(record["here"], str(entry.parent))
            self.assertEqual(record["entry"], entry.relative_to(root).as_posix())
            self.assertEqual(record["expected"], list(literal_expected(SOURCE)))
            self.assertEqual(len(record["expected"]), 10)
            self.assertEqual((root / "imported").read_text(), "synthetic infrastructure only\n")
            self.assertEqual((root / "calls").read_text(), "1")

    def test_changed_source_refuses_before_sentinel_import(self):
        with tempfile.TemporaryDirectory(prefix="p210-engineering-") as directory:
            root, infrastructure, _, wrapper = fixture(directory)
            infrastructure.write_text(infrastructure.read_text() + "# deliberate mutation\n")
            with self.assertRaisesRegex(ValueError, "source hash differs"):
                wrapper.main()
            self.assertFalse((root / "imported").exists())
            self.assertFalse((root / "binding.json").exists())

    def test_missing_source_refuses_before_delegation(self):
        with tempfile.TemporaryDirectory(prefix="p210-engineering-") as directory:
            root, infrastructure, _, wrapper = fixture(directory)
            infrastructure.unlink()
            with self.assertRaises(FileNotFoundError):
                wrapper.main()
            self.assertFalse((root / "imported").exists())
            self.assertFalse((root / "binding.json").exists())

    def test_nonzero_return_is_not_converted_to_success(self):
        with tempfile.TemporaryDirectory(prefix="p210-engineering-") as directory:
            _, _, _, wrapper = fixture(directory, "return 7")
            self.assertEqual(wrapper.main(), 7)

    def test_exception_is_not_converted_to_success(self):
        with tempfile.TemporaryDirectory(prefix="p210-engineering-") as directory:
            _, _, _, wrapper = fixture(directory, 'raise RuntimeError("synthetic rejection")')
            with self.assertRaisesRegex(RuntimeError, "synthetic rejection"):
                wrapper.main()

    def test_static_population_matches_unimported_science_and_rejects_added_id(self):
        tree = ast.parse((HERE / "checks.py").read_text())
        actual = tuple(c.name + "." + method.name for c in tree.body
                       if isinstance(c, ast.ClassDef) for method in c.body
                       if isinstance(method, ast.FunctionDef) and method.name.startswith("test_"))
        expected = literal_expected(SOURCE)
        self.assertEqual(expected, actual)
        self.assertEqual(len(actual), 10)
        def verify(population):
            if population != actual:
                raise ValueError("Synthetic population mismatch")
        with self.assertRaisesRegex(ValueError, "population mismatch"):
            verify(expected + ("Wrong.extra_control",))


if __name__ == "__main__":
    unittest.main(verbosity=2)
