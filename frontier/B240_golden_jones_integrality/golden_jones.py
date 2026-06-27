"""B240 -- the golden integrality of the figure-eight's colored Jones (the one genuine keeper from the
chat1 physics hunt; both chat1 and chat2 agree it survives). Independently re-verified here. Nothing to
CLAIMS.md; firewall-clean (a dimensionless, object-specific quantum-invariant fact).

At the golden root q = e^{2pi i/5}, the figure-eight's colored Jones J_N weighted by the SU(2)_3 quantum
dimension [N] gives PURE INTEGERS:
    [N] * J_N(4_1; e^{2pi i/5}) = {1, -2, -2, 1}   (N=1..4),   Z = sum = -2.
The phi in [N]={1,phi,phi,1} cancels the 1/phi in J_N={1,-2/phi,-2/phi,1}: phi*(-2/phi)=-2 in Z.

MECHANISM (verified): J_2 = 1 + (q^{1/2}-q^{-1/2})(q^{3/2}-q^{-3/2}) = 1 - 4 sin(pi/5)sin(3pi/5), and the
identity sin(pi/5)sin(3pi/5) = sqrt5/4 (special to n=5: Q(cos 2pi/5)=Q(sqrt5)) gives J_2 = 1 - sqrt5 = -2/phi.

GOLDEN-SPECIFIC: at the other metallic roots n=8,13 the products are NOT integers (the cyclotomic field
does not collapse to a quadratic). FIGURE-EIGHT-vs-CHIRAL: the figure-eight is amphicheiral, so its J_N lies
in the real field Q(sqrt5) at this root; a chiral knot (trefoil) has J_N in the full cyclotomic field
Q(zeta_5) -- complex, not integer (corroborated below).

HONEST CAVEAT (both chats flag): the observation Z = -2 = -chi(Slavich 4-manifold) is UNVERIFIED -- the raw
sum Z is not the standard normalized WRT invariant, and chi appears in many formulas; held, not banked.

Run: python golden_jones.py (pyenv).
"""
import cmath

import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def colored_jones_fig8(N, q):
    """normalized colored Jones of 4_1 (Habiro/Masbaum): J_N = sum_{n=0}^{N-1} prod_{j=1}^n
    (q^{(N-j)/2}-q^{-(N-j)/2})(q^{(N+j)/2}-q^{-(N+j)/2}). J_N(unknot)=1."""
    tot = 0j
    for n in range(N):
        p = 1 + 0j
        for j in range(1, n + 1):
            p *= (q ** ((N - j) / 2) - q ** (-(N - j) / 2)) * (q ** ((N + j) / 2) - q ** (-(N + j) / 2))
        tot += p
    return tot


def qdim(N, k):
    """SU(2)_k quantum dimension of the N-dim rep: sin(N pi/(k+2))/sin(pi/(k+2))."""
    return np.sin(N * np.pi / (k + 2)) / np.sin(np.pi / (k + 2))


def products_at_root(n, knot=colored_jones_fig8):
    """[N]*J_N for N=1..k+1 at q=e^{2pi i/n}, level k=n-2."""
    q = cmath.exp(2j * np.pi / n); k = n - 2
    return [qdim(N, k) * knot(N, q) for N in range(1, k + 2)]


def is_integer_vector(v, tol=1e-9):
    return all(abs(z.imag) < tol and abs(z.real - round(z.real)) < tol for z in v)


def colored_jones_trefoil(N, q):
    """a colored Jones of the (chiral) trefoil 3_1 (one standard normalization); used only to show that a
    CHIRAL knot gives complex (non-real) values at the golden root."""
    tot = 0j
    for nn in range(N):
        p = q ** (-nn * (N - 1))
        for j in range(1, nn + 1):
            p *= (1 - q ** (-(N - j))) * (1 - q ** (-(N + j)))
        tot += p
    return tot


if __name__ == "__main__":
    print("=== golden integrality: [N]*J_N(4_1; e^{2pi i/5}) ===")
    pr5 = products_at_root(5)
    for N, p in enumerate(pr5, 1):
        print(f"  N={N}: [N]*J_N = {p:+.6f}")
    ints = [round(p.real) for p in pr5]
    assert is_integer_vector(pr5) and ints == [1, -2, -2, 1]
    print(f"  products = {ints}  (all integers)   Z = sum = {sum(ints)}")
    # the -2/phi values:
    q = cmath.exp(2j * np.pi / 5)
    assert abs(colored_jones_fig8(2, q) - (-2 / PHI)) < 1e-9
    assert abs(colored_jones_fig8(2, q) - (1 - 5 ** 0.5)) < 1e-9      # J_2 = 1 - sqrt5
    print("  J_2 = 1 - sqrt5 = -2/phi  (the sin(pi/5)sin(3pi/5)=sqrt5/4 mechanism)")

    print("\n=== golden-specific: other metallic roots are NOT integral ===")
    for n in (8, 13):
        prn = products_at_root(n)
        print(f"  n={n}: integer? {is_integer_vector(prn)}  ({[f'{p:+.3f}' for p in prn]})")
        assert not is_integer_vector(prn)

    print("\n=== figure-eight (amphicheiral) vs chiral knot (trefoil) at the golden root ===")
    tref = [qdim(N, 3) * colored_jones_trefoil(N, q) for N in range(1, 5)]
    print(f"  trefoil [N]*J_N = {[f'{p:+.3f}' for p in tref]}  -> real & integer? {is_integer_vector(tref)}")
    assert not is_integer_vector(tref)        # chiral -> complex -> not integer
    print("  (amphicheiral 4_1 -> J_N in Q(sqrt5) (real); chiral -> Q(zeta_5) (complex). Object-specific.)")

    print("\nVERIFIED: golden integrality is real, golden-specific, and figure-eight(amphicheiral)-specific.")
    print("The Z = -chi(Slavich) coincidence is HELD/unverified (raw sum != normalized WRT). Firewall-clean.")
    print("ALL CHECKS PASS")
