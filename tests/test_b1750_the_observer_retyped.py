"""B1750 -- the observer re-typed (P-372) and GENESIS v1.55.  The amendment reproduces the root file from the hash-pinned
v1.54 (--check bites); every status cell as it was; the re-typing paragraph and the log entry in place above an
unrewritten v1.54 entry; WORKING_RULES' header annotated; the mirror's J sign recomputed live at B1741's tie pair."""
import importlib.util, pathlib, re, subprocess, sys
from fractions import Fraction as Fr
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1750_the_observer_retyped"


def _m():
    spec = importlib.util.spec_from_file_location("am55", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.55 · 2026-10-24 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_54_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    assert "**[v1.55] The observer re-typed**" in out and "maps every mass ratio" in out and "identification ledger (FK11)" in out
    i55, i54 = out.find("- **v1.55 · 2026-10-24 · main B1750.**"), out.find("- **v1.54 · 2026-10-22 · main B1721.**")
    assert 0 < i55 < i54


def test_working_rules_annotated():
    w = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert "values the observer's [superseded 2026-10-24, P-372" in w


def test_the_mirror_flips_j_live():
    sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
    import census as K
    L = K.lines(); im = 2.993325909
    x = K.compute(3.4, im, *L[153]); y = K.compute(3.6, im, *L[150])
    for k in x:
        if k.startswith("ckm"):
            assert abs(x[k][3] + y[k][3]) < 1e-12 * max(1.0, abs(x[k][3])) + 1e-15 and max(abs(p - q) for p, q in zip(x[k][:3], y[k][:3])) < 1e-9
        else:
            assert max(abs(p - q) for p, q in zip(x[k], y[k])) < 1e-9
