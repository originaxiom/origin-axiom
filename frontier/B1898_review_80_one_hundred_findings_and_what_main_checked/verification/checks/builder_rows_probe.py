#!/usr/bin/env python3
"""Review 80: main's reproduction of the rows of agy-002's file that are in the enforcement package's code.

Each case is a constructed source or page given to the package's OWN function, in memory or in a temporary folder.
Nothing in the repository is changed.  A banned phrase is never written here as a literal: where one is needed it is
put together from pieces at run time.  Main wrote these from the reader's descriptions and ran none of its code.

    python3 builder_rows_probe.py        # prints each case and what the function answered
"""
import ast, importlib.util, json, os, pathlib, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m


g = load("gates_probe", "scripts/gates/gates.py")
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import check_test_vacuity as ctv

OUT = []


def say(row, case, answer, reproduced):
    OUT.append({"row": row, "case": case, "the function answered": str(answer)[:160], "reproduced": bool(reproduced)})
    print("row %-3s %-88s -> %-46s %s" % (row, case[:88], str(answer)[:46], "REPRODUCED" if reproduced else "not reproduced"))


def classes(src, name="test_x"):
    """the classes the vacuity checker gives the test `name` of `src`, by the same steps as its read_locks"""
    tree = ast.parse(src)
    fn = next(n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name)
    asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
    calls = {getattr(getattr(n, "func", None), "attr", None) for n in ast.walk(fn) if isinstance(n, ast.Call)}
    out = []
    if not asserts and not (ctv._OK_CALLS & calls):
        out.append("NO-ASSERT")
    elif ctv.cannot_fail(fn):
        out.append("CANNOT-FAIL")
    return out


# ---------------------------------------------------------------------------------------------- row 41: the controls gate
honest = "import pytest\n\ndef compute():\n    return 1\n"
c41 = {
    "(a) the module's mark written with an annotation": "import pytest\npytestmark: object = pytest.mark.skip(reason='never')\n\ndef test_control():\n    assert compute() == 1\n\ndef compute():\n    return 1\n",
    "(b) a skip inside a helper that the control calls": honest + "\ndef _bail():\n    pytest.skip('never')\n\ndef test_control():\n    _bail()\n    assert compute() == 1\n",
    "(c) a control with no assert and a bare approx": honest + "\ndef test_control():\n    pytest.approx(compute())\n",
    "the control of the probe: the same mark written plainly": "import pytest\npytestmark = pytest.mark.skip(reason='never')\n\ndef test_control():\n    assert compute() == 1\n\ndef compute():\n    return 1\n",
}
for k, src in c41.items():
    a = g.control_cannot_control(src, "test_control")
    say(41, k, a, (a is None) != k.startswith("the control"))

# ------------------------------------------------------------------------------------------- rows 42 and 43: the checker
c42 = {
    "(a) no assert, a bare approx": "import pytest\ndef test_x():\n    pytest.approx(1.0)\n",
    "(b) a no-op call before a comparison of literals": "def noop():\n    pass\ndef test_x():\n    noop()\n    assert 2 + 2 == 4\n",
    "(c) the only assert inside an inner function never called": "def test_x():\n    def inner():\n        assert compute() == 1\n    x = 1\n",
    "the control: a comparison of literals alone": "def test_x():\n    assert 2 + 2 == 4\n",
    "the control: no assert at all": "def test_x():\n    x = 1\n",
}
for k, src in c42.items():
    a = classes(src)
    say(42, k, a or "no class", (a == []) != k.startswith("the control"))
c43 = {
    "a shift of literals": "def test_x():\n    assert 1 << 3 == 8\n",
    "a subscript of a literal list": "def test_x():\n    assert [1, 2, 3][0] == 1\n",
    "a repeated tuple": "def test_x():\n    assert (1, 2) * 2 == (1, 2, 1, 2)\n",
    "a dict unpacked into a dict": "def test_x():\n    assert {**{'a': 1}} == {'a': 1}\n",
    "an f-string of literals": "def test_x():\n    assert f\"{1}\" == '1'\n",
    "an annotated binding": "def test_x():\n    x: int = 3\n    assert x == 3\n",
    "two names bound at once": "def test_x():\n    x = y = 3\n    assert x == y\n",
    "the control: a sum of literals": "def test_x():\n    assert 1 + 2 == 3\n",
}
for k, src in c43.items():
    a = classes(src)
    say(43, k, a or "no class", (a == []) != k.startswith("the control"))

# ------------------------------------------------------------------------------------------------- row 44: by the code
src = (ROOT / "scripts/checks/check_test_vacuity.py").read_text(encoding="utf-8")
say(44, "(a) a lock that does not parse is passed over before it is counted", "except Exception: continue" if "        except Exception:\n            continue\n        for fn in ast.walk(tree):" in src else "the lines differ",
    "        except Exception:\n            continue\n        for fn in ast.walk(tree):" in src)
say(44, "(b) the key of a test is the file and the function's name, with no class", 'f"{rel}::{fn.name}"' if 'f"{rel}::{fn.name}"' in src else "differs", 'f"{rel}::{fn.name}"' in src and "ClassDef" not in src)
say(44, "(c) only files named test_*.py are collected outside tests/", '":(glob)**/test_*.py"' if '":(glob)**/test_*.py"' in src else "differs", '":(glob)**/test_*.py"' in src and "_test.py" not in src.replace("test_*.py", ""))

# ------------------------------------------------------------------------------------------- row 45: the framing gate
def seen(page_text):
    plain = g._framing_plain(page_text)
    return any(g._framing_plain(ph) in plain for ph in g.BANNED)
ph = next(x for x in g.BANNED if len(x.split()) >= 3)           # one of the gate's own phrases; never printed
w = ph.split(); mid = len(w) // 2
wrap = lambda l, r: " ".join(w[:mid] + [l + w[mid] + r] + w[mid + 1:])
c45 = {
    "the control: one of the gate's phrases written plainly": ph,
    "the control: asterisks around one word (the gate strips them)": wrap("*", "*"),
    "(a) underscores around one word": wrap("_", "_"),
    "(a) double underscores around one word": wrap("__", "__"),
    "(a) an emphasis command around one word": wrap("\\emph{", "}"),
    "(a) a link around one word": wrap("[", "](http://x)"),
    "(a) a tilde in place of one space": " ".join(w[:mid]) + "~" + " ".join(w[mid:]),
    "(a) a quoted block broken before one word": "> " + " ".join(w[:mid]) + "\n> " + " ".join(w[mid:]),
}
for k, s_ in c45.items():
    a_ = seen("It is said here that " + s_ + ".")
    say(45, k, "seen" if a_ else "not seen", (not a_) if k.startswith("(a)") else a_)
gsrc = (ROOT / "scripts/gates/gates.py").read_text(encoding="utf-8")
say(45, "(b) the walk skips a folder when '.git' is anywhere in its full path", 'if ".git" in dirpath' if 'if ".git" in dirpath or "__pycache__" in dirpath' in gsrc else "differs", 'if ".git" in dirpath or "__pycache__" in dirpath' in gsrc)

# ------------------------------------------------------------------------------- rows 42 (b) and 43 again, other forms
for k, src_ in {"42 (b) again: a bare approx before a comparison of literals": "import pytest\ndef test_x():\n    pytest.approx(1.0)\n    assert 2 + 2 == 4\n",
                "42 (b) again: a call of a helper's attribute before it": "import helpers\ndef test_x():\n    helpers.noop()\n    assert 2 + 2 == 4\n",
                "43 again: a slice of a literal list": "def test_x():\n    assert [1, 2, 3][0:2] == [1, 2]\n",
                "43 again: a subscript of a literal dict": "def test_x():\n    assert {'a': 1}['a'] == 1\n"}.items():
    a_ = classes(src_)
    say(k[:2], k, a_ or "no class", a_ == [])

json.dump(OUT, open(pathlib.Path(__file__).with_name("builder_rows_probe.json"), "w"), indent=1)
rows = sorted({o["row"] for o in OUT})
print("\nrows probed:", rows, "| cases: %d | reproduced: %d" % (len(OUT), sum(o["reproduced"] for o in OUT)))
