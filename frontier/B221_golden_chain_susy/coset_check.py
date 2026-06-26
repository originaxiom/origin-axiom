"""B221 -- the golden (Fibonacci anyon) chain's emergent SUSY: the EXACT anchor. Nothing to CLAIMS.md.

What B220 reproduced as "c=7/10" is the tricritical Ising model M(4,5) = the FIRST member of the N=1
SUPERCONFORMAL minimal series. So the golden chain's emergent CFT is SUPERSYMMETRIC. This file proves the
identity by exact arithmetic, and records the structural facts that were hiding in plain sight:

  (1) c = 7/10 by THREE exact derivations that agree:
        - the GKO coset  M(4,5) = (SU(2)_2 x SU(2)_1)/SU(2)_3 :  c_2 + c_1 - c_3 = 3/2 + 1 - 9/5 = 7/10
        - the Virasoro minimal model     c(p) = 1 - 6/(p(p+1)),  p=4  -> 7/10
        - the N=1 SUPERCONFORMAL series  c(m) = (3/2)(1 - 8/(m(m+2))),  m=3 -> 7/10   <-- the SUSY identity
      and SU(2)_3 is exactly the FIBONACCI / GOLDEN level (the golden anyon = the spin-1 primary of SU(2)_3),
      so multiplicity (golden, B218) -> emergent N=1 superconformal SUSY.

  (2) the 6 tricritical-Ising primaries h_{r,s} = ((5r-4s)^2 - 1)/80 = {0, 1/10, 3/5, 3/2, 7/16, 3/80},
      and the coset weights h2(j1)+h1(j2)-h3(j3) (mod 1) reproduce them mod 1 (the coset structure). The
      h=3/2 primary is the SUPERCURRENT G -- the SUSY generator Act I (B222) will hunt in the spectrum.

  (3) the GOLDEN quantum dimension  d_1(SU(2)_3) = 2 cos(pi/5) = (1+sqrt5)/2 = phi  (exact; ties to B218).

  (4) content = MULTIPLICITY: for the metallic family content(R^m L^m) = gcd(b,c,a-d) = m, and R^m L^m == I
      (mod m). So L39's period-controlling "content" IS the multiplicity m (= B212's congruence-trivialization
      modulus = B204's gcd(a,b)); golden (m=1) has WRT period 5; t-2 = det(gamma-I) = |H_1| of the closed bundle.

Firewall: dimensionless CFT / representation-theory facts only; the SUSY here is a 2d superCONFORMAL symmetry of
the emergent critical chain, NOT a scale or spacetime SUSY (see speculations/S040). Nothing to CLAIMS.md;
P1-P16 untouched. Physics classical (Friedan-Qiu-Shenker; Feiguin et al 2007). Run: python coset_check.py (pyenv).
"""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp


# ---- central charges (exact, Fraction) ----
def c_su2(k):
    """affine SU(2)_k Sugawara central charge c = 3k/(k+2)."""
    return Fr(3 * k, k + 2)


def coset_central_charge():
    """M(4,5) = (SU(2)_2 x SU(2)_1)/SU(2)_3  =>  c = c_2 + c_1 - c_3."""
    return c_su2(2) + c_su2(1) - c_su2(3)


def minimal_model_c(p):
    """unitary Virasoro minimal model M(p,p+1): c = 1 - 6/(p(p+1))."""
    return Fr(1) - Fr(6, p * (p + 1))


def superconformal_c(m):
    """N=1 superconformal minimal series: c = (3/2)(1 - 8/(m(m+2)))."""
    return Fr(3, 2) * (Fr(1) - Fr(8, m * (m + 2)))


# ---- tricritical Ising operator content (exact, Kac formula for M(4,5)) ----
def kac_weights_m45():
    """h_{r,s} = ((5r - 4s)^2 - 1)/80, 1<=r<=3, 1<=s<=4, modulo (r,s)~(4-r,5-s). Returns the distinct set."""
    out = set()
    for r in range(1, 4):
        for s in range(1, 5):
            out.add(Fr((5 * r - 4 * s) ** 2 - 1, 80))
    return sorted(out)


def h_su2(j, k):
    """primary conformal weight of spin-j in SU(2)_k: h = j(j+1)/(k+2). j is a Fraction (0,1/2,1,...,k/2)."""
    return j * (j + 1) / (k + 2)


def coset_weights_mod1():
    """coset weights (mod 1) of M(4,5) = (SU(2)_2 x SU(2)_1)/SU(2)_3 via the GKO branching:
    labels l=2j1 in {0,1,2} (SU(2)_2), l'=2j3 in {0,1,2,3} (SU(2)_3), the SU(2)_1 label eps fixed by
    eps = (l+l') mod 2 (the level-1 Z2 selection rule). h = h2(j1)+h1(eps/2)-h3(j3) (mod 1); the field
    identification (l,l')~(2-l,3-l') makes pairs coincide. r=l+1, s=l'+1 are the minimal-model labels."""
    out = set()
    for ll in range(0, 3):        # l = 2*j1, spin j1 = l/2 in SU(2)_2
        for lp in range(0, 4):    # l' = 2*j3, spin j3 = l'/2 in SU(2)_3
            eps = (ll + lp) % 2   # SU(2)_1 label fixed by parity
            h = h_su2(Fr(ll, 2), 2) + h_su2(Fr(eps, 2), 1) - h_su2(Fr(lp, 2), 3)
            out.add(h % 1)
    return sorted(out)


# ---- the golden quantum dimension (exact, sympy) ----
def golden_quantum_dim_check():
    """d_1(SU(2)_3) = sin(3 pi/5)/sin(pi/5) = 2 cos(pi/5) = (1+sqrt5)/2 = phi, exactly."""
    d1 = sp.sin(3 * sp.pi / 5) / sp.sin(sp.pi / 5)
    phi = (1 + sp.sqrt(5)) / 2
    return sp.simplify(d1 - phi) == 0, sp.nsimplify(sp.simplify(d1))


# ---- content = multiplicity (exact integer arithmetic) ----
def content(a, b, c, d):
    """content of gamma=[[a,b],[c,d]] = gcd(b,c,a-d) = largest modulus where gamma reduces to a scalar (B219)."""
    return gcd(gcd(abs(b), abs(c)), abs(a - d))


def metallic_word(m):
    """R^m L^m = [[1+m^2, m],[m, 1]] (trace 2+m^2)."""
    return (1 + m * m, m, m, 1)


if __name__ == "__main__":
    print("(1) c = 7/10 by three exact derivations (the SUSY identity):")
    cc = coset_central_charge()
    print(f"    coset (SU(2)_2 x SU(2)_1)/SU(2)_3:  c_2+c_1-c_3 = {c_su2(2)}+{c_su2(1)}-{c_su2(3)} = {cc}")
    print(f"    Virasoro minimal M(4,5):            c(p=4) = {minimal_model_c(4)}")
    print(f"    N=1 superconformal (m=3):           c(m=3) = {superconformal_c(3)}   <- SUSY")
    assert cc == minimal_model_c(4) == superconformal_c(3) == Fr(7, 10)
    print(f"    all equal 7/10: {cc == minimal_model_c(4) == superconformal_c(3) == Fr(7,10)}")
    print(f"    SU(2)_3 is the Fibonacci/golden level (c_su2(3)={c_su2(3)} = the SU(2)_3 WZW central charge).")

    print("\n(2) tricritical-Ising operator content (the SUSY primaries):")
    kac = kac_weights_m45()
    print(f"    Kac h_{{r,s}} for M(4,5): {[str(h) for h in kac]}")
    assert kac == sorted([Fr(0), Fr(1, 10), Fr(3, 5), Fr(3, 2), Fr(7, 16), Fr(3, 80)])
    print(f"    = {{0,1/10,3/5,3/2,7/16,3/80}}: {kac == sorted([Fr(0),Fr(1,10),Fr(3,5),Fr(3,2),Fr(7,16),Fr(3,80)])}")
    print(f"    the h=3/2 primary = the SUPERCURRENT G (the SUSY generator; B222 hunts it in the spectrum).")
    cw = coset_weights_mod1()
    kac_mod1 = sorted(set(h % 1 for h in kac))
    print(f"    coset weights (mod 1): {[str(h) for h in cw]}")
    print(f"    Kac weights  (mod 1): {[str(h) for h in kac_mod1]}")
    assert cw == kac_mod1
    print(f"    coset reproduces the TCI weights mod 1: {cw == kac_mod1}  (golden SU(2)_3 -> TCI structure)")

    print("\n(3) the golden quantum dimension:")
    ok, val = golden_quantum_dim_check()
    print(f"    d_1(SU(2)_3) = sin(3pi/5)/sin(pi/5) = {val} = phi (= 2cos(pi/5)): exact {ok}")
    assert ok

    print("\n(4) content = multiplicity m (L39's invariant IS the multiplicity):")
    for m in range(1, 7):
        a, b, c, d = metallic_word(m)
        ct = content(a, b, c, d)
        modI = all(x % m == (1 if i in (0, 3) else 0) for i, x in enumerate((a, b, c, d))) if m > 1 else True
        print(f"    m={m}: R^mL^m={[a,b,c,d]} content={ct} (==m? {ct==m})  R^mL^m==I mod m? {modI}")
        assert ct == m and modI
    print("    => content(R^mL^m)=m = B212 congruence modulus = B204 gcd(a,b); golden (m=1) WRT period 5.")
    print("\nALL CHECKS PASS")
