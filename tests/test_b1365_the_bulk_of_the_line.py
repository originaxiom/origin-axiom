"""B1365 lock (seconds): the 27's charge table under SM x U(1)' reproduces B1283's (beta, gamma) on all eleven field types and gamma is
the eta model's U(1); the 4-torsion census of exp(u(1)^2) (12 order-4 points, four reaching exactly the SM); H^1(Y_3; 78_rho) by Fox
calculus (three neutral moduli, one vector-like colour-triplet pair, the (2,20) sector empty; controls b_1 = 0 and the alphabet);
the D-term sign theorem; the deck test (288 of 288 combined lines differ from their deck images); the three explicit deformation families."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1365_the_bulk_of_the_line" / "verification"


def test_the_line_leaves_u1_eta_three_moduli_one_triplet_pair_and_no_seesaw():
    out = subprocess.run([sys.executable, str(VER / "bulk_of_the_line.py")], capture_output=True, text=True, timeout=900).stdout
    assert "all eleven field types agree with B1283's identification, and gamma = -(5 psi - 3 chi)/12 on every weight: True" in out
    assert "gamma = (2 sqrt 15 / 3) Q_eta on every field type (U(1)' is the eta model's U(1)): True" in out
    assert "non-trivial 4-torsion points of T^2: 15; orders: {4: 12, 2: 3}" in out
    assert "order-4 points killing exactly the SM's eight among the 30 (B1364's condition): 4 -> [(1, 0), (1, 2), (3, 0), (3, 2)]" in out
    assert "controls: b_1(Y_3) = h^1(trivial) = 0" in out
    assert "order 2: [1, 1, 1], order 4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" in out
    assert "h^1 of the adjoint (3,1) = Ad o rho_Q8 over the 24 lines: [3]; of the doublet (2) alone: [0]" in out
    assert "the spectrum depends only on the point g: 1 distinct outcomes" in out
    assert "(3, ((\'(1,35)\', (3, 1, Fraction(-1, 3), Fraction(-2, 1)), 3), (\'(1,35)\', (3, 1, Fraction(1, 3), Fraction(2, 1)), 3)))" in out
    assert "it vanishes only at N_i = nu^c_i = 0" in out
    assert "differs from their deck image's on some word of length <= 6: 288 of 288" in out
    assert "{(True, True, True): 24}" in out
