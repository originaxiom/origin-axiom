"""B1025 locks — no test module may require an OPTIONAL dependency at import time.

The defect this prevents (measured 2026-08-10, on a clone following `requirements.txt`):

    $ python3 -m pytest -q
    ERROR tests/test_b461.py            ModuleNotFoundError: No module named 'snappy'
    ERROR tests/test_b719_scale.py      ModuleNotFoundError: No module named 'snappy'
    ERROR tests/test_b849_order_parameter.py
    !!!!!! Interrupted: 3 errors during collection !!!!!!
    22 skipped, 1 warning, 3 errors in 218.33s

pytest aborts the ENTIRE run on a collection error, so three unguarded imports meant **zero
tests executed** — not "three modules skipped". `REPRODUCIBILITY.md` declares SnapPy optional
("The verified figure-eight constants are hard-coded and tested without it"), so the suite is
supposed to stay green without it. It could not run at all.

The rule these locks enforce is the one the repo already used correctly in 37 other modules:
reach an optional dependency through `pytest.importorskip`, never a bare module-level import.

Scope: an INSTRUMENT lock. It asserts a structural property of the test suite, not a
mathematical fact about the object — the honest kind for a repair arc (WORKING_RULES 7).
"""
import ast
import pathlib
import re

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_TESTS = _ROOT / "tests"

# Frozen constant, amended only by a logged change (the GOVERNANCE house rule for whitelists).
# These are the dependencies `requirements.txt` does NOT install: importing one at module scope
# is what breaks collection on a conforming clone.
OPTIONAL_DEPS = frozenset({"snappy", "cypari", "cypari2", "sage", "flint", "python_flint"})


def module_level_optional_imports(source: str) -> set:
    """Optional deps imported as a DIRECT child of the module body.

    Direct children only, by design: an import nested in `try:`/`if:`/a function is already
    guarded (or lazily reached) and does not break collection. `pytest.importorskip(...)` is a
    Call, not an Import node, so it is correctly invisible here.
    """
    found = set()
    for node in ast.parse(source).body:
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or ""]
        else:
            continue
        for name in names:
            root = name.split(".")[0]
            if root in OPTIONAL_DEPS:
                found.add(root)
    return found


def any_bare_optional_import(source: str) -> set:
    """Optional deps imported bare ANYWHERE in a test module — module scope OR inside a function.

    Module scope aborts collection (locks 1–2). An in-function bare import is milder but still
    wrong: the test **FAILS** instead of **SKIPPING** on a clone without the dependency, which
    violates the same `REPRODUCIBILITY.md` contract one level down. Measured 2026-08-10: 23 such
    failures across nine modules, after the collection abort was repaired.

    Imports inside `try:` are exempt — that form handles absence deliberately.
    """
    tree = ast.parse(source)

    # Every `importorskip("dep")` call, with the line it sits on. An import of `dep` is guarded
    # if such a call appears EARLIER in the file (module preamble, an enclosing decorator, or
    # the same function body). Line order is the honest proxy for "runs before".
    guards = {}
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "importorskip"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            dep = node.args[0].value.split(".")[0]
            guards[dep] = min(guards.get(dep, 10**9), node.lineno)

    # Imports inside `try:` handle absence deliberately.
    in_try = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            for sub in ast.walk(node):
                if isinstance(sub, (ast.Import, ast.ImportFrom)):
                    in_try.add(id(sub))

    found = set()
    for node in ast.walk(tree):
        if id(node) in in_try:
            continue
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or ""]
        else:
            continue
        for name in names:
            root = name.split(".")[0]
            if root in OPTIONAL_DEPS and guards.get(root, 10**9) > node.lineno:
                found.add(root)
    return found


def _test_files():
    return sorted(p for p in _TESTS.glob("test_*.py"))


def test_no_test_module_imports_an_optional_dep_at_module_scope():
    """The invariant: collection must succeed with only `requirements.txt` installed."""
    offenders = {}
    for path in _test_files():
        bad = module_level_optional_imports(path.read_text(encoding="utf-8"))
        if bad:
            offenders[path.name] = sorted(bad)
    assert not offenders, (
        "these test modules import an optional dependency at module scope, which aborts "
        f"COLLECTION of the whole suite on a clone without it: {offenders}. "
        "Use `pytest.importorskip(...)` instead."
    )


def test_modules_that_exec_a_frontier_script_guard_it_first():
    """The indirect form of the same defect — the one that broke `test_b849_order_parameter`.

    A test may load a frontier script via `spec_from_file_location` + `exec_module`. That runs
    the script's module-level imports at COLLECTION time, so if the script needs an optional
    dep the loading test must `importorskip` BEFORE the exec.
    """
    offenders = {}
    for path in _test_files():
        src = path.read_text(encoding="utf-8")
        if "exec_module" not in src:
            continue
        targets = re.findall(r'"([^"]*?/[^"]*?\.py)"|frontier"\s*/\s*"([^"]+)"', src)
        # Resolve the frontier scripts this test executes, by path fragments it names.
        for frag in re.findall(r'"(B\d+[A-Za-z0-9_]*)"\s*/\s*"([A-Za-z0-9_]+\.py)"', src):
            script = _ROOT / "frontier" / frag[0] / frag[1]
            if not script.is_file():
                continue
            needs = module_level_optional_imports(script.read_text(encoding="utf-8"))
            if not needs:
                continue
            exec_at = src.index("exec_module")
            guard = re.search(r"importorskip", src[:exec_at])
            if guard is None:
                offenders[path.name] = f"execs {script.name} needing {sorted(needs)}, unguarded"
    assert not offenders, (
        "these tests exec a frontier script that imports an optional dependency, without an "
        f"`importorskip` before the exec: {offenders}"
    )


def test_no_test_module_reaches_an_optional_dep_bare_anywhere():
    """The FAIL-instead-of-SKIP class (B1025 follow-on, measured 2026-08-10).

    23 tests across nine modules failed with `ModuleNotFoundError: snappy` AFTER the collection
    abort was fixed, because they imported it bare inside a test function. `REPRODUCIBILITY.md`
    promises the suite stays green without SnapPy; a failure is not green.
    """
    offenders = {}
    for path in _test_files():
        bad = any_bare_optional_import(path.read_text(encoding="utf-8"))
        if bad:
            offenders[path.name] = sorted(bad)
    assert not offenders, (
        "these test modules import an optional dependency bare (module or function scope), so "
        f"they FAIL rather than SKIP without it: {offenders}. Use `pytest.importorskip(...)`."
    )


# --- the positive control (MB12): the criterion must be able to FAIL --------------------------
# Without this, a detector that always returned the empty set would pass the two locks above and
# have measured nothing. Same discipline the arcs apply to their own sealed criteria.

def test_detector_flags_a_bare_module_level_import():
    assert module_level_optional_imports("import snappy\n") == {"snappy"}
    assert module_level_optional_imports("from snappy import Manifold\n") == {"snappy"}
    assert module_level_optional_imports("import snappy.foo\n") == {"snappy"}


def test_detector_does_not_flag_the_guarded_forms():
    guarded = (
        "import pytest\n"
        'snappy = pytest.importorskip("snappy")\n'
    )
    assert module_level_optional_imports(guarded) == set()

    try_wrapped = "try:\n    import snappy\nexcept ImportError:\n    snappy = None\n"
    assert module_level_optional_imports(try_wrapped) == set()

    in_function = "def f():\n    import snappy\n    return snappy\n"
    assert module_level_optional_imports(in_function) == set()


def test_required_dependencies_are_not_treated_as_optional():
    """A guard on the guard: sympy/numpy/pytest are in requirements.txt and must stay importable
    at module scope, or this lock would push the suite toward skipping its own mathematics."""
    for required in ("sympy", "numpy", "scipy", "pytest"):
        assert required not in OPTIONAL_DEPS
    assert module_level_optional_imports("import sympy\nimport numpy\n") == set()


def test_the_three_repaired_modules_are_clean_and_still_reference_snappy():
    """Regression-pins the specific repair: the modules still USE SnapPy (the fix must not have
    been "delete the test"), but reach it through importorskip."""
    for name in ("test_b461.py", "test_b719_scale.py", "test_b849_order_parameter.py"):
        src = (_TESTS / name).read_text(encoding="utf-8")
        assert module_level_optional_imports(src) == set(), f"{name} regressed"
        assert "snappy" in src, f"{name} no longer references snappy — repair became deletion"
        assert "importorskip" in src, f"{name} lost its guard"
