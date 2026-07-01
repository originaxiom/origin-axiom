"""B320 lock -- adjudication of Chat-1's three push-back points. (1) A+C fusion REFUTED: firewall A = Z/2 (Galois
conj sqrt-3->-sqrt-3), generations C = Z/3 (Eisenstein-unit omega / E6 center) -- different subgroups of the Z/6 units;
the democratic Yukawa rank-1 (3,0,0) needs S3, not Z/3 (a Z/3-circulant has rank 3). (2) the mod-7 -> Fano -> G2 chain
is real but FIBER-GENERIC: the 7 = the Heawood number of the torus (all bundles share it), and 168=7x|2T| is a
coincidence (2T=SL(2,3) has 1 involution, S4 has 9, so 2T != S4; the coset decomp is by S4). Exhaustion stands. (3)
observer=seam is a firewalled [HOOK], not a proven isomorphism. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B320_chat1_three_points" / "chat1_three_points.py"
_spec = importlib.util.spec_from_file_location("b320", _PATH)
b320 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b320)


def test_point1_fusion_refuted():
    assert b320.firewall_and_generation_group_orders() == (2, 3)   # A=Z/2, C=Z/3 -- different
    assert b320.allones_rank() == 1 and b320.generic_circulant_rank() == 3   # rank-1 needs S3 not Z/3
    assert b320.FUSION_REFUTED and b320.DEMOCRATIC_RANK1_NEEDS_S3_NOT_Z3


def test_point2_mod7_is_fiber_generic():
    assert b320.psl2_7_order() == 168                              # |PSL(2,7)| = |Aut(Fano)|
    assert b320.sl2_3_involutions() == 1 and b320.s4_involutions() == 9   # 2T != S4 -> 168=7x24 coincidence
    assert b320.heawood_torus() == 7                              # the 7 is fiber-generic
    assert b320.MOD7_CHAIN_IS_REAL_BUT_FIBER_GENERIC and b320.ONE_SIXTYEIGHT_EQ_7x24_IS_COINCIDENCE


def test_point3_observer_seam_firewalled():
    assert b320.OBSERVER_SEAM_IS_FIREWALLED_HOOK


def test_exhaustion_stands():
    assert b320.EXHAUSTION_STANDS                                  # the one unrun lead (mod-7) run -> generic
    assert b320.DERIVES_SM_VALUES is False
    assert b320.verdict()
