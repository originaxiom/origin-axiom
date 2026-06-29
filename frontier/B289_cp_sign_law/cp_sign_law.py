"""B289 -- IS THE CP SIGN FORCED? The CS sign law of the closings, and its Q(sqrt-3) Galois meaning.
Run with sage-python (SnapPy). Phase II of the seam arc (wall #3, chirality/CP).

B286 found the cusped object amphichiral (CS=0) and generic closings chiral, with CS(p,-q)=-CS(p,q) on a sample.
This makes it robust and reads its meaning:

  1. FORCED SIGN LAW (mechanism). Over every hyperbolic closing (p,q), |p|,|q|<=8: the closed manifold is CHIRAL
     (CS not in {0,1/2} mod 1) and obeys  CS(p,-q) = -CS(p,q)  EXACTLY. The ORIENTED slope forces the CP sign.
     Verified two ways: chern_simons() and Im(complex_volume)/(2*pi^2) agree.

  2. AMPHICHIRAL LOCUS EMPTY. No hyperbolic closing has CS in {0,1/2} -- closing ALWAYS breaks amphichirality/CP.

  3. HANDEDNESS = Q(sqrt-3) GALOIS CONJUGATION. The mirror slope (p,-q) realises complex conjugation of the
     geometric holonomy (orientation reversal -> CS -> -CS). At the cusp this complex conjugation is the nontrivial
     element of Gal(Q(sqrt-3)/Q): it swaps the two Riley roots u <-> u^2, which is EXACTLY the involution that flips
     B285's commutator phase kappa = u^2+2 = sqrt(3) e^{-+ i pi/6} between +pi/6 and -pi/6 (= the tau/amphichirality
     swap). So the closing's CS sign and the cusp's +-pi/6 sign are TWO FACES of the same Q(sqrt-3) involution.

  4. BUT THE SIGN IS NOT OBJECT-DERIVABLE. The object is amphichiral (CS=0) and CP-symmetric (it delivers +-pi/6
     symmetrically, B252/B285). The closing forces A sign; WHICH sign is the external/seam choice (the tau-fork).
     PHYSICS (CP -> baryon) FIREWALLED -- see verdict.py.
"""
import snappy
from math import pi, gcd


def cs(p, q):
    M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((p, q))
    if 'positively' not in M.solution_type():
        return None
    return float(M.chern_simons())


def cs_via_complex_volume(p, q):
    M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((p, q))
    if 'positively' not in M.solution_type():
        return None
    return complex(M.complex_volume()).imag / (2 * pi**2)        # method 2: Im(complex volume)/(2 pi^2)


def is_chiral(c):
    c = c % 1.0
    return min(c, abs(c - 0.5), abs(c - 1.0)) > 1e-4


if __name__ == "__main__":
    print("cusped m004: CS =", cs(0, 0) if False else float(snappy.Manifold('m004').chern_simons()), "(amphichiral)")
    n = n_chiral = n_signlaw = n_twoway = 0
    amphichiral = []
    for p in range(-8, 9):
        for q in range(1, 9):
            if gcd(abs(p), q) != 1:
                continue
            c = cs(p, q)
            if c is None:
                continue
            n += 1
            if is_chiral(c):
                n_chiral += 1
            else:
                amphichiral.append((p, q))
            c2 = cs_via_complex_volume(p, q)            # complex-volume CS is defined mod 1/2 (normalization)
            if c2 is not None and min(((c - c2) % 0.5), 0.5 - ((c - c2) % 0.5)) < 1e-4:
                n_twoway += 1
            cm = cs(p, -q)
            if cm is not None and min(((c + cm) % 1.0), 1 - ((c + cm) % 1.0)) < 1e-4:
                n_signlaw += 1
    print(f"\nhyperbolic closings: {n}")
    print(f"chiral: {n_chiral}/{n}   |   CS two methods agree (mod 1/2): {n_twoway}/{n}")
    print(f"forced sign law CS(p,-q)=-CS(p,q): {n_signlaw}/{n}")
    print(f"amphichiral-preserving closings (CS in {{0,1/2}}): {amphichiral if amphichiral else 'NONE'}")
    assert n_chiral == n and n_signlaw == n and not amphichiral
    print("\nVERDICT: closing forces a CP sign (the oriented slope), via the Q(sqrt-3) complex-conjugation involution")
    print("(= the B285 +-pi/6 / tau swap); WHICH sign is not object-derivable (the object is CP-symmetric). Firewalled.")
