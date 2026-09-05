"""B1257 — Brieskorn–Slodowy selects the subregular orbit, uniquely."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1257_brieskorn_selection" / "verification" / "brieskorn_selection.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import brieskorn_selection as B
    return B


def test_the_script_runs_and_selftests():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_exactly_one_orbit_has_a_surface_slice_and_it_is_the_subregular():
    B = _mod()
    rows, _ = B.table()
    surf = [r for r in rows if B.DIM_N - r[2] == 2]
    assert len(surf) == 1
    c, dims, dO = surf[0]
    assert c == B.SUBREGULAR and dO == 70 and dims == [13, 9, 5]


def test_the_principal_orbit_slice_is_a_point_and_forgets_2T():
    B = _mod()
    rows, _ = B.table()
    pt = [r for r in rows if B.DIM_N - r[2] == 0]
    assert len(pt) == 1 and pt[0][0] == B.PRINCIPAL and pt[0][1] == [17, 9, 1]


def test_the_criterion_discriminates():
    """MB12: 28 of 30 orbits give neither a point nor a surface — not a tautology."""
    B = _mod()
    rows, _ = B.table()
    neither = [r for r in rows if B.DIM_N - r[2] not in (0, 2)]
    assert len(neither) == 28 and len(rows) == 30


def test_the_selection_never_looked_at_the_27():
    """THE DECISIVE CONTROL: slice dimension depends only on dim O, not on the decomposition.

    Recompute the selection from orbit dimensions ALONE and require it to land on the same
    orbit — so the three-chiral reading cannot have been fitted to the answer.
    """
    B = _mod()
    rows, roots = B.table()
    by_dim_only = [c for c, _dims, dO in rows if B.DIM_N - dO == 2]
    assert by_dim_only == [B.SUBREGULAR]
    dims = next(d for c, d, _ in rows if c == B.SUBREGULAR)
    chiral = sum(1 for t in dims if t % 2 == 1 and t > 1)
    abelian = sum(1 for t in dims if t == 1)
    assert (chiral, abelian) == (3, 0)
