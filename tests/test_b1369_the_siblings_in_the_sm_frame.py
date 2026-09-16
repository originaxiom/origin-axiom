"""B1369 lock (about a minute): the free-cusp census of the figure-eight family (83 free cusps on 35 of 112 members;
77 members without one, m202 and s959 among them); m202's peripheral subgroups of index 7 and its spin-1/2 half cusp-fixed only with
finite-order characters; the isometries' exact action on H_1 from the canonical retriangulation (|Aut| = |Isom| on every candidate,
73 cusp-map cross-checks); the region-swap parity closing 79 of the 83 free cusps; the four residual cusps and their unique shortest
cusp modes; 108 of 112 members closed."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1369_the_siblings_in_the_sm_frame" / "verification"


def test_the_family_in_the_sm_frame_needs_a_free_cusp_and_parity_closes_all_but_four():
    out = subprocess.run([sys.executable, str(VER / "siblings_in_the_sm_frame.py")], capture_output=True, text=True, timeout=3600).stdout
    assert "the only cusps that can host a non-unitary cusp-fixed spin-0 sector: 83 cusps on 35 members" in out
    assert "one-cusped members: 60: 54 have b_1 = 1 = the peripheral rank (no free cusp); 6 have b_1 = 2 with a peripheral image of rank 1 (a free cusp): ['t06828', 'o10_150688', 'o10_150713', 'o10_150714', 'o10_150716', 'o10_150724']" in out
    assert "multi-cusped members (52): 23 have every peripheral rank equal to b_1 (no free cusp; m202 and s959 among them: [[2, 2], [2, 2]]), 29 have a free cusp" in out
    assert "members without a free cusp: 77 of 112; with a free cusp: 35" in out
    assert "cusp 0: mu = bbAbA -> [-2, 3], lambda = bba -> [1, 2]; peripheral rank 2, index of P_0 in H_1 = 7; lift traces (mu, lambda) = (+2.000, +2.000)" in out
    assert "isometries: 12 (D6), cusp-swapping: 6, cusp-fixing with |det(A - I)| = 3 on both cusps (the order-3 rotation of B1321): 2" in out
    assert "characters with the whole 10 cusp-fixed on cusp 0 (a grid of 1225 solutions): 266 keep all 22 non-SM roots non-trivial (Standard Model unbroken)" in out
    assert "P_0 + P_1 = H_1: index of the sum = 1" in out
    assert "free cusps: 83; closed by parity: 79 (of which 75 already by an isometry acting on the torus by +-I, R71's form; 4 need the general lemma); parity silent: 4: [('o10_150688', 0), ('o10_150708', 0), ('o10_150716', 0), ('o10_150725', 1)]" in out
    assert "cross-checks of the direct action against the cusp-map inference: 73 cusps, all agree" in out
    assert out.count("agree with SnapPy's cusp maps: True") == 10          # the ten free cusps of members whose peripheral classes do not span H_1
    assert "o10_150725 cusp 1: free classes 2, a fixer negates a subspace of dimension 1" in out
    assert out.count("shortest dual vector unique: True") == 4
    assert "members fully closed (no free cusp, or every free cusp closed by parity): 108 of 112; members with an open cusp: ['o10_150688', 'o10_150708', 'o10_150716', 'o10_150725']" in out
    assert "DONE" in out


def test_the_isometry_instrument_matches_snappy_on_m412_and_closes_its_free_cusps():
    out = subprocess.run([sys.executable, str(VER / "family_isometries.py"), "m412", "o10_150684"], capture_output=True, text=True, timeout=900).stdout
    assert "m412 tets 12 b_1 2 cusps 2 |Aut| 8 |Isom| (SnapPy) 8 ranks [1, 1]" in out
    assert out.count("-> closed (general) True, closed (+-I only) True") == 2
    assert "o10_150684 tets 24 b_1 2 cusps 2 |Aut| 2 |Isom| (SnapPy) 2 ranks [1, 1]" in out
    assert out.count("-> closed (general) True, closed (+-I only) False") == 2


def test_the_instrument_reproduces_theory_predicted_ranks_on_the_whitehead_link_and_the_borromean_rings():
    out = subprocess.run([sys.executable, str(VER / "controls.py")], capture_output=True, text=True, timeout=900).stdout
    assert "m129  H_1 =        Z + Z: instrument (b_1, ranks) (2, [1, 1]), SnapPy (2, [1, 1]), predicted (2, [1, 1]); |Aut| 8 = |Isom| 8: OK" in out
    assert "L6a4  H_1 =    Z + Z + Z: instrument (b_1, ranks) (3, [1, 1, 1]), SnapPy (3, [1, 1, 1]), predicted (3, [1, 1, 1]); |Aut| 48 = |Isom| 48: OK" in out
    assert "CONTROLS PASS" in out
