"""B1805 -- matter parity from the tower above, tested (P-414).  The committed runs: Spin(10)'s centre is matter parity; the
fillings' order-2 line breaks Spin(10) to (connected) Pati-Salam; no flat connection gives exactly the SM (U(1)_X stays);
only 1, 10, 16, 16bar, 45 localise (no 126); Witten's conditions with real Higgs 10's have no solution for exponent-2 F'."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1805_matter_parity_from_the_tower_above" / "verification"


def test_the_centre_is_matter_parity_and_w_gives_pati_salam():
    c1 = (V / "c1_run.txt").read_text(encoding="utf-8")
    assert "centraliser of W in su(5): 12" in c1 and "centraliser of W in so(10): 21" in c1
    assert "-> z2 = exp(i pi Q_X) = matter parity" in c1 and "solutions [] -> matter parity is not in S(U(3)xU(2))" in c1
    r1 = (V / "referee" / "r1_run.txt").read_text(encoding="utf-8")
    assert "CONNECTED" in r1


def test_the_parity_does_not_reach_the_sm_and_witten_fails():
    r4 = (V / "referee" / "r4_run.txt").read_text(encoding="utf-8")
    assert "commutant of su(3)+su(2)+u(1)_Y in so(10): dim 2 ; abelian: True" in r4
    r2 = (V / "referee" / "r2_run.txt").read_text(encoding="utf-8")
    assert "'126': 5.0" in r2 and "so(12) adj -> so(10): max norm^2 of restricted weights 2" in r2
    r3 = (V / "referee" / "r3_run.txt").read_text(encoding="utf-8")
    assert "(C0) Higgs as real 10s, twist of order <= 2, sigma, tau free, all conditions:              groups with solutions: NONE" in r3
    assert "cases where H_u's 10 self-mass (charge 2 h_u) is forbidden: 0" in r3
