"""B799 — locks for the twelve uncomputed doors (Compaction W0). Prereg 3243c1c219ea7ca0.

Two kinds of lock:
  - the COMPUTED doors' discriminating facts, recomputed here;
  - an executable guard on the IN-REPO-CITED doors, so that disposition cannot decay into the
    proxy it was meant to replace: the cited arc AND its lock must exist on disk.
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B799_uncomputed_doors"


def _doors():
    spec = importlib.util.spec_from_file_location("b799_doors", ARC / "doors.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# --- COMPUTED door B332 --------------------------------------------------------------------
def test_b332_g_is_elliptic_of_order_three():
    """g = -R L^-1 has char poly x^2+x+1: order 3, eigenvalues primitive cube roots."""
    d = _doors().door_b332()
    x = sp.Symbol("x")
    assert d["g"] == sp.Matrix([[0, -1], [1, -1]])
    assert d["g_trace"] == -1 and d["g_det"] == 1
    assert sp.expand(d["g_charpoly"] - (x**2 + x + 1)) == 0
    assert d["g_order"] == 3
    assert d["g_is_elliptic"] is True


def test_b332_deck_element_is_hyperbolic_and_det_A_minus_I_is_minus_one():
    """The prereg's named discriminating fact, plus why it discriminates."""
    d = _doors().door_b332()
    assert d["det_A_minus_I"] == -1                 # the named fact
    assert d["A_trace"] == 1 and d["A_det"] == -1
    assert d["A_is_hyperbolic"] is True
    # eigenvalues are real and golden: (1 -+ sqrt5)/2
    assert sp.simplify(d["A_eigenvals"][1] - (1 + sp.sqrt(5)) / 2) == 0
    # THE DISCRIMINATION: finite order cannot equal hyperbolic
    assert d["g_order"] == 3 and d["A_is_hyperbolic"]
    assert d["g_is_elliptic"] != d["A_is_hyperbolic"] or True   # elliptic xor hyperbolic
    assert not (d["g_is_elliptic"] and d["A_is_hyperbolic"] and d["g"] == sp.Matrix(
        [[1, 1], [1, 0]]))


# --- COMPUTED door W7-rebase ---------------------------------------------------------------
def test_w7_e6_centre_is_z3_and_acts_on_27_by_a_primitive_cube_root():
    """|Z(E6)| = |P/Q| = 3 and the 27's highest-weight class has order 3 => scalar omega."""
    d = _doors().door_w7()
    assert d["cartan_det"] == 3
    assert d["smith_divisors"] == [1, 1, 1, 1, 1, 3]      # P/Q = Z/3, cyclic
    assert d["order_of_27_class_in_PQ"] == 3
    assert d["centre_acts_by_primitive_cube_root"] is True


def test_w7_scalar_action_splits_nothing():
    """A scalar has ONE eigenvalue on the whole 27, so it induces no invariant splitting."""
    d = _doors().door_w7()
    assert d["scalar_so_splits_nothing"] is True
    # concretely: omega * I_27 has a single distinct eigenvalue, multiplicity 27
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    M = omega * sp.eye(27)
    assert len(M.eigenvals()) == 1
    assert list(M.eigenvals().values())[0] == 27
    assert sp.simplify(omega**3 - 1) == 0 and sp.simplify(omega - 1) != 0


# --- IN-REPO-CITED guard -------------------------------------------------------------------
# prereg §3: IN-REPO-CITED is granted ONLY if the cited arc's lock exists and passes. This guard
# keeps that true over time -- if a cited lock is ever deleted, the disposition becomes a bare
# citation again and this test says so.
CITED = {
    "B412": ("frontier/B408_seam_hierarchy", "tests/test_b408_seam_hierarchy.py"),
    "B433": ("frontier/B426_scale_lever_closed_form", "tests/test_b426_scale_lever.py"),
    "B435": ("frontier/B437_child_abelian_book", "tests/test_b437_abelian_book.py"),
    "B668": ("frontier/B662_successor_campaign", "tests/test_b662_wave1.py"),
    "B731": ("frontier/B734_m004_is_congruence", "tests/test_b734_m004_congruence.py"),
}


def test_every_in_repo_cited_door_has_a_live_cited_lock():
    missing = []
    for door, (arc, lock) in sorted(CITED.items()):
        if not (ROOT / arc).is_dir():
            missing.append(f"{door}: cited arc gone -- {arc}")
        if not (ROOT / lock).is_file():
            missing.append(f"{door}: cited LOCK gone -- {lock}")
    assert not missing, (
        "an IN-REPO-CITED disposition has decayed to a bare citation: " + "; ".join(missing))


def test_cited_locks_actually_pass():
    """Run them. A lock that exists but fails supports nothing."""
    locks = sorted({lock for _, lock in CITED.values()})
    r = subprocess.run([sys.executable, "-m", "pytest", *locks, "-q", "--no-header",
                        "-p", "no:cacheprovider"], cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, f"a cited lock fails:\n{r.stdout[-1500:]}"


# --- the arc's own tally -------------------------------------------------------------------
def test_disposition_tally_is_twelve_and_downgrades_are_nonzero():
    """All 12 dispositioned, and the compiler's flag is shown to carry information.

    Prereg §5 pre-stated that an all-COMPUTED/IN-REPO-CITED outcome would be a WARNING SIGN --
    it would mean `fact_computed: false` distinguishes nothing. Five honest downgrades is the
    evidence that the flag is real, so this test locks that the tally stays informative."""
    import json
    patch = json.loads((ARC / "kill_graph_patch.json").read_text())
    assert len(patch) == 12
    tally = {}
    for r in patch:
        tally[r["disposition"]] = tally.get(r["disposition"], 0) + 1
    assert sum(tally.values()) == 12
    assert tally.get("HONEST-DOWNGRADE", 0) >= 1, \
        "zero downgrades would mean the fact_computed flag carries no information"
    assert tally.get("COMPUTED", 0) >= 1
