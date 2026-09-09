"""B1258 — 2T is blind to the embedding choice, and so is the SO(10) grading."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1258_2T_is_blind" / "verification" / "two_t_is_blind.py"


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import two_t_is_blind as B
    return B


def test_the_index_multisets_agree_mod_3_4_and_6():
    """The mechanism behind the blindness, as arithmetic."""
    P, S = [16, 8, 0], [12, 8, 4]
    for m in (3, 4, 6):
        assert sorted(n % m for n in P) == sorted(n % m for n in S), m
    assert all(n % 2 == 0 for n in P + S)
    assert sum(n + 1 for n in P) == sum(n + 1 for n in S) == 27


def test_the_naive_mod_12_claim_is_false():
    """This arc's own first mechanism, convicted: chi is NOT periodic at lambda = 1."""
    import sympy as sp
    B = _mod()
    assert sp.simplify(B.chi_n(0, sp.Integer(1)) - B.chi_n(12, sp.Integer(1))) != 0


def test_the_character_test_is_not_vacuous():
    import sympy as sp
    B = _mod()
    A, P = [10, 9, 5], [16, 8, 0]
    assert sum(n + 1 for n in A) == 27
    ra = [B.chi_sum(A, lam) for _, _, lam, _ in B.CLASSES]
    rb = [B.chi_sum(P, lam) for _, _, lam, _ in B.CLASSES]
    assert any(sp.simplify(x - y) != 0 for x, y in zip(ra, rb))
