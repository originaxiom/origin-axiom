"""B1364 lock (seconds): c(SM) = su(2)_beta + u(1)^2 on the E6 root system, c(su(2)_beta) = su(6), an order-4 element of u(1)^2 killing
exactly the 8 SM roots, 24 surjections F(2,6) -> Q_8 deck-invariant up to 2T, and the descent's order-3 bound (>= 17)."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1364_the_level_mismatch_resolved" / "verification"


def test_y3_carries_a_flat_e6_connection_leaving_exactly_sm_times_u1():
    out = subprocess.run([sys.executable, str(VER / "sm_lines_on_y3.py")], capture_output=True, text=True, timeout=900).stdout
    assert "E6: 72 roots of norm 2 with integral pairings; rank 6" in out
    assert "roots commuting with the Standard Model (orthogonal to its roots, Y-neutral): 2 = +-beta with beta = (1/2)^5, psi = +c: True" in out
    assert "roots orthogonal to beta: 30 (the 30 roots of A5) -> c(su(2)_beta) = su(6), dimension 35" in out
    assert "killing exactly the 8 SM roots among the 30 of su(6): found -> unbroken algebra = 5 (Cartan) + 8 = 13" in out
    assert "roots of E6 commuting with both the Q_8 part (orthogonal to beta) and g: 8 (= the SM's 8: True)" in out
    assert "Y_3: homomorphisms F(2,6) -> Q_8 with image Q_8 (non-abelian): 24" in out
    assert "lines whose deck image is conjugate (in 2T) to themselves: 24 of 24" in out
    assert "the descent: an order-3 element of u(1)^2 kills at least 12 of the 30 roots of su(6)" in out
