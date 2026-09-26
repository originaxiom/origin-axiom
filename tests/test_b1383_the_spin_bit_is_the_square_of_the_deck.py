"""B1383 lock -- THE SPIN BIT IS THE SQUARE OF THE DECK.  On m004's spinors (spin structure sigma) the lifted Gieseking
deck squares to eps*sigma; paired with k reversed directions to eps^(k+1) (-1)^(k(k+1)/2) sigma; the Clifford half is
checked against Stiefel-Whitney classes on RP^2; on the mapping torus the double tick lifts to eps*sigma.  With physics'
eps = + the deck's role decides: gauged -> rho_1 (B1141's), the SM's CP (odd k) -> rho_2, the tick -> the double tick."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1383_the_spin_bit_is_the_square_of_the_deck" / "verification"
_spec = importlib.util.spec_from_file_location("b1383_deck_square", VER / "deck_square.py")
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)


def _W():
    W, d, mu = D.P.s2_intertwiner()
    assert d == D.P.ONE and mu == D.P.ONE
    return W


def test_clifford_and_the_stiefel_whitney_control():
    table = D.s1_clifford()
    assert table[(1, 3)] == -1 and table[(-1, 3)] == 1           # e1e2e3 squares to -eps: RP^2 is Pin- only
    rows = D.s2_rp2_control()
    assert rows[0] == ("unorientable", False, True)                # RP^2: Pin- only
    assert rows[1] == ("orientable", True, True)                   # the total space of L over RP^2 is spin
    assert rows[2] == ("unorientable", True, False)                # 2L: Pin+ only
    assert rows[3] == ("orientable", False, False)                 # 3L: orientable, not spin


def test_graded_product_and_the_sign_law():
    W = _W()
    assert D.s3_graded(W)
    law, eps_k = D.s4_sign_law(W)
    for eps in (1, -1):
        for sigma in (1, -1):
            assert law[(eps, sigma, 0)] == eps * sigma                                   # B1382 is k = 0
            for k in range(5):
                assert law[(eps, sigma, k)] == eps ** (k + 1) * (-1) ** (k * (k + 1) // 2) * sigma
            for k in (1, 3):
                assert eps_k[(eps, sigma, k)] == -sigma                                  # odd k: the factor sees -sigma


def test_mapping_torus_double_tick():
    diag, torus = D.s5_mapping_torus(_W())
    assert sorted(diag) == [0, 0, 1]                                                     # H_1(M_tau) = Z^2
    assert all(ok for ok, _ in torus.values()) and len(torus) == 8
    assert all(torus[(e, s, lam)][1] == e * s for e in (1, -1) for s in (1, -1) for lam in (1, -1))


def test_generation_parity_and_the_realizations():
    lemma = D.s6_generation_parity(trials=20)
    assert lemma["odd n admits X conj(X) = -1"] is False and lemma["U(1) supplies -1"] is False
    W = _W()
    law, eps_k = D.s4_sign_law(W)
    _, torus = D.s5_mapping_torus(W)
    table = D.s7_realizations(law, eps_k, torus)
    assert table["(a) parent as space / deck gauged (k = 0)"] == [1]                     # B1141's lift
    assert table["(c) deck inside the 4d CP/T/R, reflection type Pin+ (k = 1)"] == [-1]  # the other lift
    assert table["(b) B1104's mapping torus, double tick antiperiodic (NS, thermal)"] == [-1]


def test_mains_dirac_doubling_is_the_quaternionic_structure():
    assert D.s8_dirac_doubling(trials=20)
