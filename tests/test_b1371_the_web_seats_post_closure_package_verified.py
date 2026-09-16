"""B1371 lock (about a minute): the web seat's post-closure package re-derived -- Humbert's volume and the Bianchi
indices, the shape-field class membership, the four-property table with the 2T and 2I doors, the m + s and classic-census scans, the
Lefschetz numbers of the siblings' order-3 isometries, the non-semisimple Fox witnesses, the covering negative, the refutation of the
Sol-boundary claim (forty irreducible SU(2) representations of m004(0,1)), the Chern-Simons gate and slope law, kappa - 2 = omega."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1371_the_web_seats_post_closure_package_verified" / "verification"


def test_the_web_seats_package_verified_negatives_included():
    out = subprocess.run([sys.executable, str(VER / "verify_package.py")], capture_output=True, text=True, timeout=1800).stdout
    assert "vol(H^3/PSL(2,O_3)) = |D|^(3/2) zeta_K(2)/(4 pi^2) = 0.169156934402" in out
    assert "m202    vol 4.059766426  vol/v0 =   24.0000  integral" in out and "s959    vol 6.089649638  vol/v0 =   36.0000  integral" in out
    assert "v3461   vol 6.655154019  vol/v0 =   39.3431  not integral" in out
    assert "in the class: ['m004', 'm003', 'm202', 's959', 'v3551', 's596']; outside: ['v3461', 't10829', 't12582', 'm129']" in out
    assert "census manifolds of volume 12 v0 = 2 v_tet: ['m003', 'm004']" in out
    assert "m004        H_1              Z |Sym|   8 (  D4) amphicheiral True  order-3 elements 0  surjections onto 2T = SL(2,3): 48" in out
    assert "m003(-3,1)  H_1      Z/5 + Z/5 |Sym|  12 (  D6) amphicheiral False order-3 elements 2  surjections onto 2T = SL(2,3): 0  onto 2I = SL(2,5): 0" in out
    assert "m202        H_1          Z + Z |Sym|  12 (  D6) amphicheiral False order-3 elements 2  surjections onto 2T = SL(2,3): 96" in out
    assert "s959        H_1    Z/3 + Z + Z |Sym|  12 (  D6) amphicheiral False order-3 elements 2  surjections onto 2T = SL(2,3): 576" in out
    assert "3 (x) chi == 3 as characters: True; 2 (x) chi == 2: False" in out
    assert out.count("order-3 isometries: 2; their (tr H_1, tr H_2, L) = [(-1, 1, 3)]") == 2
    assert "m202 over F_3: 8 non-trivial homomorphisms pi_1 -> F_3; h^1 of the unipotent module U(t) over them: [2]; semisimplification (trivial 2-dim): 4" in out
    assert "(dim, h^1 unipotent, h^1 trivial) = [(2, 2, 4), (3, 2, 6), (4, 2, 8)]" in out
    assert "s959 over F_3: 26 non-trivial homomorphisms pi_1 -> F_3; h^1 of the unipotent module U(t) over them: [4, 5]; semisimplification (trivial 2-dim): 6" in out
    assert "m004 degree 2: 1 cover(s) [(1, 4.059766, 'Z/5 + Z')]; isometric to a target of that volume: {'m202': False}" in out
    assert "Dic_5 (order 20): homomorphisms with a non-abelian image 40, with an abelian image 20" in out
    assert "irreducible SU(2) representations of m004(0,1) found through binary dihedral images: 40" in out
    assert "slope law CS(p,-q) = -CS(p,q) mod 1 on the hyperbolic slopes: 8/8" in out
    assert "p = 5: all tetrahedra positively oriented vol  0.9813688" in out
    assert "a cube root of unity: True" in out
    assert "det(A - I) = 3 for a cusp-fixing order-3 isometry, first 4815: [('m202', 2, 24.0), ('s959', 2, 36.0), ('v3461', 2, 39.343), ('v3551', 2, 42.0)]; by number of cusps {2: 4}" in out
    assert "hexagonal manifolds (every cusp e^(i pi/3)) in the first 4815: 11; two-cusped among them: 5; of those with an order-3 isometry: 4" in out
    assert "m + s census (1263 manifolds): chiral + order-3 isometry + 2T door: [('m202', 96, [3]), ('s776', 1152, []), ('s784', 336, [0]), ('s959', 576, [3])]" in out
    assert "DONE" in out
