"""B1357 lock (about two minutes): the Hurwitz torus T^4/2T has 48 singular points in orbits E6 + D4 + A1 + 4A2 with chi = 5 and
resolution chi = 24; the cover orbifold has E6, D4, A1 loci on Hantzsche-Wendt and an A2 locus on T^3, one invariant spinor,
b2 = 0, b3 = 4 (descent b3 = 2, deck eigenvalues 1,1,omega,omega-bar); the local groups along the descent's cone circles have ages
1/15/5 (E6), 1/4/1 (A1), 1/5/1 (D4: seven classes, folded), 1/7/1 (A2); the order-6 coset elements fix 2-tori in two classes."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1357_the_objects_own_joyce_orbifold" / "verification"


def test_the_objects_own_joyce_orbifold_census_betti_numbers_and_the_descents_local_groups():
    out = subprocess.run([sys.executable, str(VER / "joyce_orbifold.py")], capture_output=True, text=True, timeout=2400).stdout
    assert "|Fix(g)| = N(g - 1)^2 for every g (Lefschetz): True" in out
    assert "chi(T^4/2T) = (1/24) sum_g chi(Fix g) = 5" in out
    assert "singular points of T^4 (non-identity fixed points): 48; 2T-orbits: 7: {'2T (E6)': 1, 'Z2 (A1)': 1, 'Q8 (D4)': 1, 'Z3 (A2)': 4}" in out
    assert "= 5 + 19 = 24  (K3: True)" in out
    assert "type A2: orbit of singular orbits [3, 4, 5, 6] (covering degree 4 over Y_3), holonomy image ['1'] -> locus = T^3 (b_1 = 3)" in out
    assert "cover: invariant 1-forms 0 (invariant spinors = 1 + 0 = 1: N = 1), b_2 = 0, b_3 = 4" in out
    assert "descent: invariant 1-forms 0 (invariant spinors = 1 + 0 = 1: N = 1), b_2 = 0, b_3 = 2" in out
    assert "locus E6 (holonomy image of order 4): (R^3)^hol has dimension 0 -> RIGID" in out
    assert "locus A2 (holonomy image of order 1): (R^3)^hol has dimension 3 -> resolvable" in out
    assert "g of order 6: fixed subspace of the linear part of dimension 2; fixed set on T^4: 1 tori  (8 elements)" in out
    assert "crepant b_2 = 15, b_4 = 5, non-compact divisors 10" in out
    assert "local group order 6 (= 3|Gamma_y|: True" in out and "crepant b_2 = 4, b_4 = 1, non-compact divisors 3" in out
    assert "conjugacy classes 7, ages" in out and "crepant b_2 = 5, b_4 = 1, non-compact divisors 4" in out
    assert "crepant b_2 = 7, b_4 = 1, non-compact divisors 6" in out
    assert "the order-6 elements form 2 conjugacy classes of [4, 4]" in out
    assert "singular points on it by type {'E6': 1, 'A1': 12, 'A2': 8}" in out
    assert "singular points on it by type {'E6': 1, 'D4': 3, 'A2': 8}" in out
