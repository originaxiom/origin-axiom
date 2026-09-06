"""B1291 — the parity theorem: 3 is EXCLUDED on a one-cusped manifold; the escape is >=2 cusps."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1291_the_parity_of_the_cusp"
V = ARC / "verification"


def _det_A_minus_I(a, b, c, d):
    return (a - 1) * (d - 1) - b * c


def test_the_algebraic_half_is_computed_not_asserted():
    """|Fix| = |det(A-I)|, and finite order in GL(2,Z) bounds it to {0,1,2,3,4}."""
    from itertools import product
    import numpy as np
    I = np.eye(2, dtype=int)
    vals, classes = set(), set()
    for a, b, c, d in product(range(-4, 5), repeat=4):
        if a * d - b * c not in (1, -1):
            continue
        A = np.array([[a, b], [c, d]]); P = I.copy()
        for _ in range(12):
            P = P @ A
            if (P == I).all():
                vals.add(abs(_det_A_minus_I(a, b, c, d)))
                classes.add((a * d - b * c, a + d, _det_A_minus_I(a, b, c, d)))
                break
    assert vals == {0, 1, 2, 3, 4}, vals
    assert (1, -1, 3) in classes, "3 must be ALGEBRAICALLY reachable — the geometry is what forbids it"


def test_the_parity_theorem_and_its_control_by_RUNNING_the_script():
    """Reds if any one-cusped manifold shows an odd |Fix|, or if >=2 cusps fails to realise 3."""
    r = subprocess.run([sys.executable, str(V / "parity.py")],
                       capture_output=True, text=True, cwd=str(V))
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.rstrip().endswith("SELFTEST: PASS"), out[-600:]
    assert "ODD |Fix| violations: 0" in out, out[-800:]
    # the control MUST fire: 3 realised with >=2 cusps, else the theorem is vacuous
    assert re.search(r"witnesses for the ODD/small values: .*3:", out), out[-800:]


def test_m004_is_one_cusped_and_its_fix_counts_are_even():
    import warnings; warnings.filterwarnings("ignore")
    snappy = __import__("snappy")
    M = snappy.Manifold("m004")
    assert M.num_cusps() == 1
    G = M.symmetry_group()
    assert G.order() == 8                                   # D4
    seen = set()
    for iso in G.isometries():
        for A in iso.cusp_maps():
            seen.add(abs(_det_A_minus_I(int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]))))
    assert seen == {0, 4}, seen
    assert all(v % 2 == 0 for v in seen), seen
    assert 3 not in seen


def test_the_other_two_closures_still_run():
    for script in ("dividing_set.py", "involutions.py"):
        r = subprocess.run([sys.executable, str(V / script)], capture_output=True, text=True, cwd=str(V))
        assert r.returncode == 0, script + ": " + r.stdout[-1500:]
        assert r.stdout.rstrip().endswith("SELFTEST: PASS"), script


def test_the_VACUOUS_closure_is_labelled_as_refuted_at_source():
    """B1291 §4: chi_orb(T^2/G) = 0 identically, so that criterion cannot fail. It must never be
    re-read as a closure — the label lives in the script, not only in the log (E53)."""
    src = (V / "orbifold.py").read_text(encoding="utf-8")
    assert "WITHDRAWN AS AN ARGUMENT" in src and "VACUOUS" in src
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "VACUOUS" in f and "MB12 vacuity failure" in f
    # and the vacuity must be stated as the *reason*, verifiable here
    from fractions import Fraction as F
    for n in (2, 3, 4, 6):
        assert F(0, n) == 0          # chi_orb(T^2/G) = chi(T^2)/|G| = 0 for EVERY finite G


def test_the_verdict_declares_the_law_and_the_registry_carries_it():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "NEGATIVE" and v["creates_law"] is True
    assert "B1291" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "EXCLUDED" in v["claim_one_line"] and "COMMENSURABILITY INVARIANT" in v["claim_one_line"]
