"""B1354 -- the maximal persistence.  Fast (~2 minutes): the obstruction-class tower climbed to order 6 modulo one prime -- at order 4
the second-order class must drop V4, V8, V16 and tie V6 to V14 (a linear solution family), the higher orders are affine and free,
and the branch found keeps all three cusp-fixed vectors of rho_0 through order 6 (Toeplitz kernel dimensions 3m).  Slow: the full
tower (two primes, four directions, every target vector, the kappa-terms) and the climb to order 8 modulo both primes."""
import sys, subprocess
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1354_the_maximal_persistence" / "verification"
pytest.importorskip("sympy")


def test_a_formal_branch_tangent_to_v10_keeps_the_three_cusp_fixed_vectors_through_order_six():
    out = subprocess.run([sys.executable, str(VER / "continuation.py"), "6", "67108819"], capture_output=True, text=True, timeout=1800).stdout
    assert "Groebner basis: 4 elements, all linear: True" in out
    assert "V4 = 0, V8 = 0, V16 = 0 (must vanish)" in out
    assert "Toeplitz kernel dimensions kd(1..7) = [3, 6, 9, 12, 15, 18, 21]" in out
    assert "the climb continued through order 6" in out


@pytest.mark.slow
def test_the_tower_finds_candidates_for_every_target_and_the_climb_reaches_order_eight_modulo_two_primes():
    out = subprocess.run([sys.executable, str(VER / "persistence_tower.py")], capture_output=True, text=True, timeout=7200).stdout
    assert out.count("Groebner basis {1}") == 0
    assert out.count("candidate branches keeping") >= 32
    out2 = subprocess.run([sys.executable, str(VER / "continuation.py"), "8"], capture_output=True, text=True, timeout=7200).stdout
    assert out2.count("the climb continued through order 8") == 2
    assert out2.count("kd(1..9) = [3, 6, 9, 12, 15, 18, 21, 24, 27]") == 2


@pytest.mark.slow
def test_the_tuned_branch_is_formally_self_dual_and_the_greedy_one_is_not():
    for prime in ("67108819", "67108837"):
        out = subprocess.run([sys.executable, str(VER / "trace_series.py"), "8", prime], capture_output=True, text=True, timeout=3600).stdout
        greedy, tuned = out.split("=== the tuned branch")
        assert greedy.count("self-duality defect at orders [4, 5, 6, 7, 8]") == 6
        assert tuned.count("self-duality defect at orders none") == 8 and "moves first at order 1" in tuned
