"""B1256 addendum — h^1(m004; Sym^n): the even-dimensional case, computed not cited.

Pins the answer to the arc's one open item: Sym^even contributes 1 to h^1 (reproducing
Menal-Ferrer-Porti on this bench), Sym^ODD contributes 0. Three of B1256's four candidate
sl2 embeddings carried even-dimensional summands and depended on this.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1256_sl2_embedding" / "verification" / "h1_symmetric_powers.py"


def _table():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    rows = {}
    for line in r.stdout.splitlines():
        m = re.match(r"\s*(\d+)\s+(\d+)\s+\S+-dim\s+\(Sym\^\w+\)\s+(\d+)\s+(\d+)\s+(yes|NO)", line)
        if m:
            n, dimV, h0, h1, agree = int(m[1]), int(m[2]), int(m[3]), int(m[4]), m[5]
            rows[n] = (dimV, h0, h1, agree)
    assert len(rows) == 17, f"expected n=0..16, got {sorted(rows)}"
    return rows


def test_two_independent_primes_agree_on_every_row():
    for n, (_, _, _, agree) in _table().items():
        assert agree == "yes", f"primes disagree at n={n}"


def test_MFP_reproduced_on_bench_for_the_object():
    """dim H^1 = 1 for every nontrivial ODD-dimensional symmetric power."""
    rows = _table()
    for n in range(2, 17, 2):
        assert rows[n][2] == 1, f"Sym^{n} (dim {n+1}) gave h^1 = {rows[n][2]}"
    assert rows[0][1] == 1 and rows[0][2] == 1          # trivial: h^0 = h^1 = 1


def test_the_open_half_answered_even_dimensional_reps_contribute_zero():
    """THE ADDENDUM'S RESULT: Sym^odd (even-dimensional) gives h^1 = 0, every one."""
    rows = _table()
    for n in range(1, 17, 2):
        assert rows[n][2] == 0, f"Sym^{n} (dim {n+1}) gave h^1 = {rows[n][2]}, expected 0"


def test_the_subregular_decomposition_is_all_odd_dimensional():
    """Why uniqueness survives under the CANONICAL PSL(2,C) holonomy: 13+9+5 are all odd."""
    assert all(d % 2 == 1 for d in (13, 9, 5)) and sum((13, 9, 5)) == 27
    # and the other three candidates each carry at least one even-dimensional summand
    for cand in ([8, 7, 5, 4, 3], [7, 6, 5, 4, 3, 2], [6, 5, 4, 4, 3, 3, 2]):
        assert sum(cand) == 27 and any(d % 2 == 0 for d in cand)
