"""
REVIEW 80, the web seat: main's check_test_vacuity.py and two of its uses in scripts/gates/gates.py (at c40446392), on
constructed tests and on main's own locks.
Computed once; nothing here was sealed in advance.  Main's files are never changed: the checker is imported from the
seat's checkout of main, and its functions are run on constructed source text.

  V   constructed test functions, each passed through the checker's own functions (`cannot_fail`, and the NO-ASSERT and
      TAUTOLOGY tests as `read_locks` writes them).  Each of V1 to V4 has asserts none of which can fail when the test
      runs; V0 is a control the checker must report.
        V0  assert 1 == 1 as the only assert                      (a control: CANNOT-FAIL, and TAUTOLOGY is not it)
        V1  assert compute() or True                              (an `or` with a true literal)
        V2  assert (compute(), "a message")                       (a tuple, which is always true)
        V3  for x in (): assert compute(x)                        (a loop over nothing)
        V4  assert compute() == 3 or "it" == "it"                 (an `or` with a true comparison of literals)
  S   every assert in every tracked lock the checker reads (tests/*.py and test_*.py anywhere), at c40446392, whose
      test is a non-empty tuple, or an `or` one of whose operands the checker's own `_value` works out true with no
      names.  Printed as file, line and test; no file text is printed.

  G   the controls gate's reading of a control, `control_cannot_control(src, name)` in gates.py, on constructed files.  None
      means the control is accepted.
        G0  a module that calls pytest.importorskip at its top level        (a control: refused, "skip itself at import")
        G1  a module that skips itself at import under an `if`              (the test is real)
        G2  a module that skips itself at import in an `except` clause      (the test is real)
        G3  a control whose only assert is `gate_fails_on_the_plant() or True`
  H   the vacuity gate's sentence, `gate_test_vacuity()`, with the checker's reading replaced by one that finds no test in
      which no assert can fail: every one of the 26 held by name would then be mended.  The gate's own words say that a table
      of which some are mended or gone is to be shortened.  Printed: whether the gate passes, and whether its sentence asks for
      the table to be shortened.  The checkout's kind is set to 'full' in memory, since the seat's checkout is shallow and the
      history the gate reads begins after the cut.

Usage: code_probe.py <the seat's checkout of main, at c40446392>
"""
import ast
import importlib.util
import os
import subprocess
import sys

MAIN = sys.argv[1]
spec = importlib.util.spec_from_file_location('ctv_r80', os.path.join(MAIN, 'scripts/checks/check_test_vacuity.py'))
ctv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ctv)
print('main at', subprocess.run(['git', '-C', MAIN, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip())

CASES = {
    'V0': 'def test_v0():\n    assert 1 == 1\n',
    'V1': 'def test_v1():\n    assert compute() or True\n',
    'V2': 'def test_v2():\n    assert (compute(), "a message")\n',
    'V3': 'def test_v3():\n    for x in ():\n        assert compute(x)\n',
    'V4': 'def test_v4():\n    assert compute() == 3 or "it" == "it"\n',
}


def classes(fn):
    """the classes read_locks would put this function in, by its own tests"""
    out = []
    asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
    calls = {getattr(getattr(n, 'func', None), 'attr', None) for n in ast.walk(fn) if isinstance(n, ast.Call)}
    if not asserts and not (ctv._OK_CALLS & calls):
        return ['NO-ASSERT']
    if ctv.cannot_fail(fn):
        out.append('CANNOT-FAIL')
    for a in asserts:
        t = a.test
        if isinstance(t, ast.Constant) and bool(t.value):
            out.append('TAUTOLOGY')
        elif isinstance(t, ast.Compare) and len(t.ops) == 1 and isinstance(t.ops[0], ast.Eq) \
                and ast.dump(t.left) == ast.dump(t.comparators[0]):
            out.append('TAUTOLOGY')
    return out


for key, src in CASES.items():
    fn = ast.parse(src).body[0]
    got = classes(fn)
    print('V   %s: reported as %s' % (key, ', '.join(got) if got else 'nothing'))


def always_true(t):
    if isinstance(t, ast.Tuple) and t.elts:
        return 'a non-empty tuple'
    if isinstance(t, ast.BoolOp) and isinstance(t.op, ast.Or):
        for v in t.values:
            try:
                if ctv._value(v, {}):
                    return 'an `or` with an operand true by itself'
            except Exception:
                pass
    return None


hits = []
for rel in ctv._lock_files():
    try:
        tree = ast.parse(open(os.path.join(MAIN, rel), encoding='utf-8').read())
    except Exception:
        continue
    for fn in ast.walk(tree):
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name.startswith('test'):
            for a in ast.walk(fn):
                if isinstance(a, ast.Assert):
                    why = always_true(a.test)
                    if why:
                        hits.append((rel, a.lineno, fn.name, why))
print('S   locks read: %d; asserts that cannot fail by their own form: %d' % (len(ctv._lock_files()), len(hits)))
for h in hits:
    print('S   %s:%d %s -- %s' % h)


# --- G: the controls gate's reading of a control ------------------------------------------------------------------------
gspec = importlib.util.spec_from_file_location('gates_r80', os.path.join(MAIN, 'scripts/gates/gates.py'))
g = importlib.util.module_from_spec(gspec)
gspec.loader.exec_module(g)
REAL = "def test_the_gate_fails_on_a_planted_case():\n    assert sorted([2, 1])[0] == 1\n"
CONTROLS = {
    'G0': "import pytest\n\npytest.importorskip('a_package_nobody_has')\n\n\n" + REAL,
    'G1': "import os\nimport pytest\n\nif not os.path.exists('no_such_file'):\n    pytest.skip('not here', allow_module_level=True)\n\n\n" + REAL,
    'G2': "import pytest\n\ntry:\n    import a_package_nobody_has\nexcept ImportError:\n    pytest.skip('not here', allow_module_level=True)\n\n\n" + REAL,
    'G3': "def gate_fails_on_the_plant():\n    return False\n\n\ndef test_the_gate_fails_on_a_planted_case():\n    assert gate_fails_on_the_plant() or True\n",
}
for key, src in CONTROLS.items():
    print('G   %s: %s' % (key, g.control_cannot_control(src, 'test_the_gate_fails_on_a_planted_case') or 'accepted as a control'))

# --- H: the vacuity gate's sentence when every held test is mended ------------------------------------------------------
# The seat's checkout of main is shallow (history from 2026-09-10), and the gate is refused on a shallow clone.  The history
# it reads here starts at its anchor of 2026-11-11, which the checkout holds, so the gate is told the checkout is full.
g.checkout_state = lambda repo=None: 'full'
import types
real = ctv.read_locks()
fake = types.ModuleType('check_test_vacuity')
fake.read_locks = lambda: dict(real, **{'CANNOT-FAIL': []})
sys.modules['check_test_vacuity'] = fake
ok, detail = g.gate_test_vacuity()
print('H   the held table has %d names; the checker now finds none of them' % len(g.CANNOT_FAIL_AS_FOUND))
print('H   the gate passes: %s; its sentence asks for the table to be shortened: %s' % (ok, 'shorten the table' in str(detail)))
real_cf = [t for t in real['CANNOT-FAIL'] if t in g.CANNOT_FAIL_AS_FOUND]
fake.read_locks = lambda: dict(real, **{'CANNOT-FAIL': real_cf[:1]})
ok1, detail1 = g.gate_test_vacuity()
print('H   control, one of the 26 still found: the gate passes: %s; its sentence asks for the table to be shortened: %s'
      % (ok1, 'shorten the table' in str(detail1)))
