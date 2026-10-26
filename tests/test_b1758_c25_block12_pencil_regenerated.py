"""B1758 (P-301 / R70-1): lock test for the clean-checkout exact rational regeneration of the block-12 pencil
(R8, R14, R16, e(rho), det14(rho)) and the three exact proofs that det14(rho) > 0 and e(rho) > 0 at all three real roots
of mu(rho), confirming THEOREM_LEDGER C25 without b12_tower.pkl."""
import json, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1758_c25_block12_pencil_regenerated_from_scratch" / "verification"


def test_b12_tower_regenerated_and_exact_positivity():
    d = json.loads((A / "b12_tower_regenerated.json").read_text(encoding="utf-8"))
    rho, u = sp.symbols("rho u")
    mu = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)
    det14 = (sp.Rational(9084997258444800000, 28561)*rho**2
             + sp.Rational(77253378048000, 2197)*rho
             + sp.Rational(461060812800, 169))
    e_poly = (-sp.Rational(752150557025548369920000, 4826809)*rho**2
              + sp.Rational(159895951748628480000, 371293)*rho
              + sp.Rational(82022486586163200, 28561))
    assert sp.simplify(sp.sympify(d["det14_rho"]) - det14) == 0
    assert sp.simplify(sp.sympify(d["e_rho"]) - e_poly) == 0

    # Proof 1: Exact completing-the-square identity over Q
    sq = sp.Rational(9084997258444800000, 28561) * (rho + sp.Rational(13, 235200))**2 + sp.Integer(2727198720)
    assert sp.expand(det14 - sq) == 0
    assert d["completing_the_square"]["global_min"] == 2727198720
    assert d["completing_the_square"]["strictly_positive_for_all_real_rho"] is True

    # Proof 2: Exact resultant / minimal polynomial identity over Q
    minpoly_det14 = sp.Poly(sp.resultant(mu.as_expr(), u - det14, rho), u).monic()
    assert minpoly_det14.all_coeffs() == [
        1,
        -19856793600,
        98573063018250240000,
        -142198242829436706619392000000,
    ]
    minpoly_e = sp.Poly(sp.resultant(mu.as_expr(), u - e_poly, rho), u).monic()
    ce = minpoly_e.all_coeffs()
    assert ce[0] > 0 and ce[1] < 0 and ce[2] > 0 and ce[3] < 0

    # Proof 3: Exact rational interval certification at the 3 real roots of mu
    ivs = mu.intervals(eps=sp.Rational(1, 10**20))
    assert len(ivs) == 3
    for idx, ((lo, hi), _) in enumerate(ivs):
        d_lo = min(sp.Rational(det14.subs(rho, lo)), sp.Rational(det14.subs(rho, hi)))
        e_lo = min(sp.Rational(e_poly.subs(rho, lo)), sp.Rational(e_poly.subs(rho, hi)))
        assert d_lo > sp.Integer(2727198720) > 0
        assert e_lo > sp.Integer(283511130354) > 0
        assert d["interval_certifications"][idx]["det14_positive_exact"] is True
        assert d["interval_certifications"][idx]["e_positive_exact"] is True
        assert d["interval_certifications"][idx]["rel_diff_det14"] < 1e-12

    # Modular check at q = 40123 (B892 benchmark)
    m40123 = d["modular_checks"]["40123"]
    assert any(r["rq"] == 27063 and 13410 in r["gamma_q"] and 2675 in r["a_q"] for r in m40123)
    assert d["galois_invariance_b906"]["gamma_part_of_det14_zero"] is True
