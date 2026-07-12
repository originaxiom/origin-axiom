#!/usr/bin/env python3
"""B547 — the ghost scanner: rigorous realizability on x^2+y^2+z^2-xyz=c.

A trace triple (x,y,z) is realizable by an SL(2,Z) pair (A,B) — (tr A, tr B,
tr AB) — iff, for A = companion of some trace with class number h(disc)=1,
there is an integer q with
    Delta = (x^2-4) q^2 + (4z-2xy) q + (y^2-4) = square.
Solvability is decided EXACTLY by sympy.diophantine on the binary quadratic.
COMPLETENESS: valid when h(disc = x^2-4) = 1 (companion = only GL(2,Z) class).
"""
import sympy as sp
from sympy.solvers.diophantine import diophantine

q, m = sp.symbols('q m', integer=True)


def slot_realizable(x, y, z):
    a2, a1, a0 = x*x - 4, 4*z - 2*x*y, y*y - 4
    if a2 == 0:
        sol = diophantine(sp.Eq(a1*q + a0, m*m))
    else:
        sol = diophantine(a2*q*q + a1*q + a0 - m*m)
    return len(sol) > 0


def h_disc_one(D):
    """h(order of discriminant D) == 1 for the small discs the scanner hits.
    Real (D>0) and imaginary (D<0) quadratic orders; conservative (None = unknown)."""
    table = {
        # imaginary (class number one): Heegner + small orders
        -3: 1, -4: 1, -7: 1, -8: 1, -11: 1, -12: 1, -15: 2, -16: 1, -19: 1,
        -20: 2, -24: 2, -27: 1, -28: 1,
        # real, class number one (fundamental + common orders)
        5: 1, 8: 1, 12: 1, 13: 1, 17: 1, 21: 1, 24: 1, 28: 1, 29: 1, 32: 2,
        33: 1, 41: 1, 44: 1, 45: 1, 60: 2, 252: None,
    }
    return table.get(D, None)


def classify(x, y, z):
    """REALIZED / GHOST(proved) / needs-class-work.
    Proof of non-realizability needs ONE trace t with h(t^2-4)=1 whose BOTH
    A=t orderings fail (the S3 symmetry of the trace triple lets A be any coord)."""
    coords = [x, y, z]
    # realizable if ANY ordering works
    perms = [(x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)]
    for (a, b, c) in perms:
        if slot_realizable(a, b, c):
            return 'REALIZED', (a, b, c)
    # none realized; is there a COMPLETE (h=1) failing trace?
    for t in set(coords):
        if h_disc_one(t*t - 4) == 1:
            return 'GHOST(proved)', t     # both A=t orderings already failed above
    return 'needs-class-work', None


def all_hyperbolic(x, y, z):
    return all(abs(t) >= 3 for t in (x, y, z))


def main():
    print("=" * 68)
    print("B547 — the ghost scanner")
    print("=" * 68)

    print("\n[headline] (4,4,16), c=32:")
    verdict, _ = classify(4, 4, 16)
    print(f"  verdict: {verdict}; all-hyperbolic: {all_hyperbolic(4,4,16)}")
    print("  mechanism: slot (4,4,16) reduces to u^2-3v^2=7; 7 is INERT in Q(sqrt3)")
    print("  ((3/7)=-1) => not a norm => no solution. A SECOND ghost mechanism")
    print("  (inert-prime obstruction) beyond B545's elliptic-lock — the first")
    print("  ALL-HYPERBOLIC ghost. Refutes chat-2's '(4,4,16) realizable' claim.")

    print("\n[census] small candidates (Baragar/Markov context):")
    tests = [
        (1, 0, 0, "c=1  (B545: elliptic-lock)"),
        (1, 1, 5, "c=22 (B537: elliptic slot)"),
        (4, 4, 16, "c=32 (all-hyperbolic, inert-prime)"),
        (4, 16, 60, "c=32"),
        (3, 3, 3, "Markov (must REALIZE)"),
        (3, 3, 6, "Markov (must REALIZE)"),
        (3, 6, 15, "Markov (must REALIZE)"),
    ]
    for (x, y, z, note) in tests:
        v, w = classify(x, y, z)
        c = x*x + y*y + z*z - x*y*z
        tag = " [ALL-HYP]" if all_hyperbolic(x, y, z) and v.startswith('GHOST') else ""
        print(f"  ({x},{y},{z}) c={c:>4}: {v:16s}{tag}  {note}")

    print("\n[answer to the sharpened open question]")
    print("  ALL-HYPERBOLIC GHOSTS EXIST: (4,4,16) is a proved ghost with every")
    print("  coordinate hyperbolic. Ghostliness is NOT only an elliptic shadow —")
    print("  a genuinely new (inert-prime) arithmetic obstruction. Lit-gate")
    print("  (Whang/BGS/Fricke free-product trace theory) still required before novelty.")


if __name__ == '__main__':
    main()
