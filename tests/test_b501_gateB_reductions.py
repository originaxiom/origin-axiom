"""B501 lock -- CL-3B Gate B in-sandbox reductions (three pieces, banked JSONs + recompute).

Always-on tier (fast, <60 s):
  piece 1 -- the exact E6 lattice toolkit is RE-DERIVED (Weyl dims, the three tensor
             decompositions) and the full sieve is RE-RUN for 2T and A4 (window counts
             gated against B356's banked values, attrition + survivors against the
             banked b501_piece1.json, the two REALIZED canonical controls must pass);
  piece 2 -- banked locks from b501_piece2.json (gates, controls, verdict separations);
  piece 3 -- banked locks from b501_piece3.json (exact theta-block check, the
             sl2-commutant lemma Z/2, per-line intertwining floors).
Gated tier (OA_SLOW=1): piece-3 exact recompute (theta on all 78 chain vectors +
the commutant SNF + the m=1 line residual at dps 100, ~1 min) and a piece-2 single
direction re-run (m=1 base jets, ~10 min).
Nothing to CLAIMS.md."""
import importlib.util
import json
import os
import pathlib

import pytest

HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B501_gateB_reductions"
_spec = importlib.util.spec_from_file_location("b501_probe", HERE / "probe.py")
probe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(probe)

P1 = json.load(open(HERE / "b501_piece1.json"))
P2 = json.load(open(HERE / "b501_piece2.json"))
P3 = json.load(open(HERE / "b501_piece3.json"))


# ------------------------------------------------------------------ piece 1 ----------
def test_e6_toolkit_rederives_exactly():
    assert probe.weyl_dim((1, 0, 0, 0, 0, 0)) == 27
    assert probe.weyl_dim((0, 1, 0, 0, 0, 0)) == 78
    assert probe.weyl_dim((2, 0, 0, 0, 0, 0)) == 351
    assert probe.weyl_dim((1, 0, 0, 0, 0, 1)) == 650
    assert probe.weyl_dim((3, 0, 0, 0, 0, 0)) == 3003
    facts, W27, W78, W650 = probe.e6_tensor_facts()
    assert [d for _, __, d in facts["27_tensor_27bar"]] == [1, 78, 650]
    assert [d for _, __, d in facts["sym2_27"]] == [27, 351]
    assert [d for _, __, d in facts["sym3_27"]] == [1, 650, 3003]
    assert sum(W78.values()) == 78 and W78[(0,) * 6] == 6
    assert sum(W650.values()) == 650


def test_piece1_sieve_recomputes_to_banked_verdict():
    facts, W27, W78, W650 = probe.e6_tensor_facts()
    for name, banked_window in (("2T", (71192, 70262)), ("A4", (1089, 1028))):
        gs = probe._group_side(name)
        orders_needed = sorted({o for o in gs["orders"] if o >= 2})
        ach = probe.torsion_profiles(orders_needed, W27, W78, W650)
        chiral, real, conj_of = probe._enumerate_window(gs)
        assert (len(chiral) + len(real), len(chiral)) == banked_window
        att_c, surv_c = probe._sieve(gs, chiral, conj_of, ach)
        att_r, _ = probe._sieve(gs, real, conj_of, ach)
        g = P1["groups"][name]
        assert att_c == g["attrition_chiral"]
        assert att_r == g["attrition_real"]
        if name == "2T":
            assert att_c["pass_all"] == 28 and att_r["pass_all"] == 17
            assert sorted(map(list, surv_c)) == sorted(g["chiral_survivors"])
            # the realized canonical embeddings must pass every layer (controls)
            ctl = probe._canonical_controls(gs, ach)
            assert ctl["principal"]["passes_all"] and ctl["trinification"]["passes_all"]
        if name == "A4":
            assert att_c["pass_all"] == 2


def test_piece1_survivors_are_conjugate_pairs():
    surv = [tuple(v) for v in P1["groups"]["2T"]["chiral_survivors"]]
    assert len(surv) == 28
    # irrep order (B356-derived): dims [1,1,1,2,3,2,2] with the conjugation pairing
    # 1'<->1'' at positions 1,2 and 2'<->2'' at positions 5,6
    def conj(v):
        return (v[0], v[2], v[1], v[3], v[4], v[6], v[5])
    assert set(surv) == {conj(v) for v in surv}
    assert all(conj(v) != v for v in surv)


def test_piece1_torsion_achievable_sets_lock():
    assert P1["groups"]["2T"]["achievable_sizes"] == {"2": 3, "3": 7, "4": 14, "6": 47}


# ------------------------------------------------------------------ piece 2 ----------
DIRS2 = {r["label"]: r for r in P2["directions"]}


def test_piece2_parameters_and_rep_checks():
    assert P2["dps"] == 100
    assert P2["rep_checks"]["relator"] < 1e-50
    assert P2["rep_checks"]["automorphism"] < 1e-60
    assert set(DIRS2) == {"coboundary", "m=1", "m=4", "m=8", "m=4+m=8"}


def test_piece2_controls():
    cob = DIRS2["coboundary"]
    assert cob["class_norm"] < 1e-80                       # exact-tier zero at order 4
    m1 = DIRS2["m=1"]
    assert max(m1["gate_P1"], m1["gate_P2"], m1["gate_P3"]) < 1e-45
    assert m1["class_norm"] < 1e-55                        # the integrable control
    assert m1["order3_class_norm"] < 1e-55


def test_piece2_escape_sector_order4():
    """The verdict criterion: every direction's order-4 class sits >= 3 orders below
    the direction's own expansion-floor gates (the absolute criterion -- valid whether
    or not the z3-shift span quotient is informative). Where the span saturates C^6
    (m=8, mix: deltas at q4-scale against a floor-level class) MB12 goes vacuous and
    the span readout is NOT used; where it is informative (m=4) MB12 must hold."""
    for lbl in ("m=4", "m=8", "m=4+m=8"):
        r = DIRS2[lbl]
        gates = max(r["gate_P1"], r["gate_P2"], r["gate_P3"])
        assert gates < 1e-35                               # expansion floors hold
        assert r["class_norm"] < 1e-3 * gates              # >= 3 orders below own floor
        # the order-3 stage was healthy before order 4 was read
        if r.get("order3_gauge"):
            assert r["order3_gauge"]["corrected_class_norm"] < gates
        else:
            assert r["order3_class_norm"] < gates
    m4 = DIRS2["m=4"]
    if m4.get("mb12_random_residuals"):
        assert min(m4["mb12_random_residuals"]) > 0.1      # informative span: MB12 holds


def test_piece2_theta_parity_signature():
    """q4 is theta-even for the {4,8}-sector directions (odd z1, z3; even z2, q4):
    the {4,8}-block components sit below the leading F4-block component."""
    for lbl in ("m=4", "m=8", "m=4+m=8"):
        c = DIRS2[lbl]["class_abs"]                        # block order [1, 4, 5, 7, 8, 11]
        lead_f4 = max(c[0], c[2], c[3], c[5])
        assert max(c[1], c[4]) < 0.5 * lead_f4


# ------------------------------------------------------------------ piece 3 ----------
def test_piece3_exact_facts():
    assert P3["theta_blockwise_scalar_exact"] is True
    lem = P3["commutant_lemma"]
    assert lem["invariant_factors"] == [1, 1, 1, 1, 1, 2]
    assert lem["free_rank"] == 0 and lem["n_solutions"] == 2
    assert lem["theta_pattern_is_solution"] is True


def test_piece3_lines_lock():
    for m in (1, 4, 5, 7, 8, 11):
        r = P3["lines"][str(m)]
        assert r["eps_expected"] == (-1) ** (m + 1)
        assert r["r_theta_match"] < 1e-60                  # Psi z = eps z mod B^1
        assert r["r_wrong_sign"] > 1.0                     # the wrong-sign control
        assert abs(r["z0_noncoboundary"] - 1.0) < 1e-6     # non-vacuity: |z0 mod B^1| = 1
        assert r["r_J2"] < 1e-55                           # amphichiral J^2 = +1
    assert P3["sl2_intertwiner_residuals"]["hyperelliptic"] < 1e-65
    assert P3["sl2_intertwiner_residuals"]["amphichiral"] < 1e-65


# ------------------------------------------------------------------ slow tier --------
@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="piece-3 exact recompute ~1 min; set OA_SLOW=1")
def test_slow_piece3_recompute():
    CP = probe.load_cp()
    CP._guard()
    eps = {m: (-1) ** (m + 1) for m in CP.EXPONENTS}
    th = CP.E6.theta_map()
    for (m, k) in CP.COLS:
        v = CP.CHAINS[m][k]
        tv = CP.E6._apply(th, v)
        assert CP.E6._vec_eq(tv, {i: eps[m] * c for i, c in v.items()})
    lem = probe._commutant_lemma(CP)
    assert lem["free_rank"] == 0 and lem["n_solutions"] == 2
    assert lem["theta_pattern_is_solution"]


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="piece-2 m=1 base re-run ~10 min; set OA_SLOW=1")
def test_slow_piece2_m1_rerun():
    CP = probe.load_cp()
    probe.load_massey()
    za, zb = CP.h1_line(1)
    r = probe.depth3_direction("m=1", za, zb, [], gauge_fix=False, do_deltas=False)
    assert max(r["gate_P1"], r["gate_P2"], r["gate_P3"]) < 1e-45
    assert r["class_norm"] < 1e-55
