"""B1384 lock -- THE GENERATED STATE SPACE: the corrective handoff's load-bearing mathematics re-derived with own code.
S0 the signed state (-I = (L^2 R^-1)^2); S1 the common SL5 in E8 (the SM centraliser is exactly the structure A4 + u1_Y);
S2 the parabolic lemma; S3 one versus three is Shapiro plus Mackey on Gamma6 normal in Gamma2; S4 the Sym^4 control and its
order-5 twists on M2 (one prime here; the run record has three); S5 the M6 physical gate (added 2026-09-28): on a generation-
shaped background every cross-block coupling is boundary-active and the rank-2 completion loses the cusp-fixed vector (one prime and
one background here; the run record has three primes and four backgrounds)."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1384_the_generated_state_space" / "verification"
_spec = importlib.util.spec_from_file_location("b1384_handoff_checks", VER / "handoff_checks.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)


def test_signed_state_and_common_sl5():
    assert H.s0_signed_state() == "(L^2 R^-1)^2 = -I"
    assert H.s0b_the_swap_and_the_orientation_fork() == {"sigma": "RP", "sigma^2": "RL", "(P sigma P)^2": "LR"}
    out = H.s1_common_sl5()
    assert out == {"centraliser_roots": 20, "e6_roots": 72, "family": 6, "mixed": 12}


def test_parabolic_lemma():
    out = H.s2_parabolic_lemma(trials=20)
    assert out["X cancels"] is True


def test_one_versus_three_is_shapiro_and_mackey():
    out = H.s3_shapiro_mackey(want_firing=2, want_quiet=6)
    assert out["with I != 0"] >= 2 and out["unipotent T^3 != 1 with (T^3-1)^2 = 0"] >= 1


def test_sym4_order5_twists_have_index_zero():
    H.PRIMES = (601,)
    rows = H.s4_sym4_twists()
    assert rows[601]["Sym4 untwisted I"] == 0
    assert rows[601]["twists"] == [((0, 1, 1, 2, 1), (0, 1, 1, 2, 1), 0)]


def test_m6_gate_every_cross_block_coupling_moves_the_cusp():
    spec = importlib.util.spec_from_file_location("b1384_s5_m6_gate", VER / "s5_m6_gate.py")
    S5 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S5)
    out = S5.run(601, per_locus=1, want_loci=1)
    assert out["loci"] == 639 and out["backgrounds"]
    rows = out["rows"]
    assert len(rows) == 5                                          # one background, its five charged sectors
    for r in rows:
        assert r["deck_indices"] == [r["I"]] * 3 and r["I"] in (1, -1) and r["distinct_blocks"]
        assert r["six_cusp_trivial"]
        assert r["arrows"] == {"(1, 1, 0)": 30}                    # h1 = 1, restriction rank 1, interior 0, for all 30 arrows
        assert r["lam_product"] not in (0, None) and r["upper"][0] * r["lower"][0] % 601 != 0
