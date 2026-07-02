"""B352 lock -- the cup-product obstruction machinery + the banked verdict.

Always-on tier (fast, ~15 s): the exact chain skeleton, the verified intertwiners, the
block representation (relator identity + exact-bracket automorphism at dps 100), the
block cohomology dimensions (dim H^1 = 1 per exponent, 1-dim coker with a >20-order
rank cliff), and the MB12 positive control (the H^2 pairing is not vacuous).

Gated tier (OA_SLOW=1, ~15-30 min): the full second-order obstruction evaluation for
all six exponent directions + the coboundary/curve controls -- the banked B352 verdict
(every class vanishes; the {4,8} escape directions are unobstructed at second order).
Reproducer: OA_SLOW=1 pytest tests/test_b352_cup_product_obstruction.py, or
python frontier/B352_cup_product_obstruction/cup_product.py. Nothing to CLAIMS.md."""
import importlib.util
import os
import pathlib

import pytest

_PATH = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
         / "B352_cup_product_obstruction" / "cup_product.py")
_spec = importlib.util.spec_from_file_location("b352", _PATH)
b352 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b352)


def test_representation_is_valid():
    # X(rel) = I per block and X_root preserves the EXACT integer bracket -- the
    # load-bearing validation of the module identification Ad rho = (+) Sym^{2m}.
    worst_rel, worst_auto = b352.rep_checks(n_pairs=2)
    assert float(worst_rel) < 1e-40
    assert float(worst_auto) < 1e-55


def test_block_cohomology_dimensions():
    # dim H^1(4_1, Sym^{2m}) = 1 for every exponent (B347's tangent, re-derived by
    # this machinery), through the >20-order rank cliff assertions inside.
    for m in b352.EXPONENTS:
        za, zb = b352.h1_line(m)
        import mpmath as mp
        n = sum(1 for k in range(b352.DIM) if za[k] != 0 or zb[k] != 0)
        assert n > 0                       # a genuine nonzero representative
        u = b352.h2_functional(m)          # 1-dim coker, cliff-asserted inside
        assert u.rows == b352.N_OF[m]


def test_h2_pairing_is_not_vacuous():
    # MB12 positive control: the functionals pair O(1) with random vectors, so a
    # vanishing obstruction class is information, not a degenerate pairing.
    pc = b352.control_pairing_not_vacuous()
    for m, v in pc.items():
        assert v > 1e-3, (m, v)


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full second-order obstruction sweep (~15-30 min); "
                           "set OA_SLOW=1 to run -- the banked verdict is recorded "
                           "in FINDINGS.md with this reproducer")
def test_full_obstruction_sweep_all_directions_unobstructed():
    r = b352.run_all(full=True)
    assert r["relator_residual"] < 1e-40
    assert r["automorphism_residual"] < 1e-55
    # controls: the m=1 curve direction and gauge invariance
    for key in ("control_m1", "control_coboundary"):
        comps, diag = r[key]
        assert all(v < 1e-40 for v in comps.values()), (key, comps)
    # the verdict: every exponent direction (and the {4,8} mix) has vanishing
    # obstruction class, while the raw second-order cochain is large (so the
    # vanishing is exactness, not triviality)
    for key in [k for k in r if k.startswith("obstruction")]:
        comps, diag = r[key]
        assert all(v < 1e-40 for v in comps.values()), (key, comps)
        assert diag["q_norm"] > 1.0, (key, diag)
        assert diag["first_order_residual"] < 1e-40, (key, diag)
