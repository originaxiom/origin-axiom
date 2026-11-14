#!/usr/bin/env python3
"""B862 -- the cascade selects the SM's GLOBAL FORM: S(U(3)xU(2)) = [SU(3)xSU(2)xU(1)]/Z6.

The SM's own data leaves the global group form ambiguous: Gamma in {1, Z2, Z3, Z6} all match
local physics (Tong, arXiv:1705.01853). The subalgebra su(3)+su(2)+u(1) selected at the
cascade's step 3 exponentiates INSIDE SU(5) to S(U(3)xU(2)), whose kernel from the naive
product is computed here to be exactly Z6. So the chain resolves a structural ambiguity the
SM itself cannot -- for free, and falsifiably in principle (the quotients differ in their
line-operator spectra).

Embedding: g(A,B,a) = diag(A e^{-2ia}, B e^{3ia}), A in SU(3), B in SU(2) -- the hypercharge
direction diag(2,2,2,-3,-3)/6 made explicit. Kernel = {(A,B,a): both blocks = 1}.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import math
import os

from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))


def kernel_exact(grid=6, charges=(-2, 3)):
    """The kernel of g(A, B, a) = diag(A e^{-2ia}, B e^{3ia}), computed from the map in exact arithmetic.

    Corrected 2026-11-10 (B1862; the advisor seat's audit, finding E6, reproduced on main). The function this replaces
    built no matrix and no map: it looped over twelve angles and tested exp(6ia) = 1, the six being a condition derived
    by hand in a comment. The fact was right; it was not computed.

    g(A, B, a) = 1 forces A = e^{2ia} 1 and B = e^{-3ia} 1, so a kernel element is a triple of scalars: A = e^{2 pi i alpha}
    with alpha in (1/3)Z (the centre of SU(3)), B = e^{2 pi i beta} with beta in (1/2)Z (the centre of SU(2)), a = 2 pi q.
    The five diagonal phases of g, as exact rationals mod 1, are alpha - 2q (three times) and beta + 3q (twice).
    From alpha - 2q = 0 and alpha in (1/3)Z, q lies in (1/6)Z: the grid of sixths is complete, and `grid` may be any
    multiple of 6 (a finer grid must find nothing more). Returns the kernel as triples (alpha, beta, q).

    `charges` (added 2026-11-12, Review 79) are the two exponents of the map, -2 and 3 for this one. They are a parameter so
    that a lock can run the same enumeration on another map and see another kernel: a function that returned six typed
    triples would pass every test of its values, and a planted one did.

    CORRECTED 2026-11-12 (Review 79's second round; found by two readings).  With the charges a parameter, "any multiple of 6"
    is true of (-2, 3) alone, and the guard still asked only for a multiple of 6.  For charges (c1, c2) a kernel element has
    c1 q in (1/3)Z and c2 q in (1/2)Z, so q lies in (1/g)Z with g = gcd(3|c1|, 2|c2|): 6 for (-2, 3), 1 for (-1, 1), 12 for
    (-4, 6).  A grid that is not a multiple of g would return a part of the kernel without a word.  It is refused now, and so
    are two zero charges, for which every a is in the kernel and no grid is complete."""
    c1, c2 = charges
    if c1 == 0 and c2 == 0:
        raise ValueError("both charges are zero: every a is in the kernel, which is infinite, and no grid is complete")
    need = math.gcd(3 * abs(c1), 2 * abs(c2))
    # ADDED 2026-11-12 (Review 80; a reader's finding F11, not checked by main, made again here).  A grid of zero, or a negative
    # grid that is a multiple of what the charges need, passed the guard below and enumerated no point: the kernel came back
    # empty, without a word, where it holds the identity at the least.  A grid has at least one point.
    if grid < 1:
        raise ValueError("a grid of %d has no point: the kernel holds the identity at the least, and an empty grid finds nothing" % grid)
    if grid % need:
        raise ValueError("a grid of %d is not complete for the charges %r: an element of the kernel has a in (1/%d) of a turn" % (grid, charges, need))
    ker = []
    for al in (Fr(0), Fr(1, 3), Fr(2, 3)):
        for be in (Fr(0), Fr(1, 2)):
            for n in range(grid):
                q = Fr(n, grid)
                phases = [(al + charges[0] * q) % 1] * 3 + [(be + charges[1] * q) % 1] * 2     # the diagonal of g(A, B, a), as exponents
                if all(x == 0 for x in phases):
                    ker.append((al, be, q))
    return ker


def _order(g):
    """the order of a kernel element under componentwise addition mod 1"""
    add = lambda x, y: tuple((u + v) % 1 for u, v in zip(x, y))
    o, e = 1, g
    while any(c != 0 for c in e):
        e = add(e, g)
        o += 1
    return o


def kernel_elements():
    """The kernel's elements as sixth-root indices of a (the form results.json has always held)."""
    ker = kernel_exact(6)
    assert len(ker) == len(kernel_exact(72)) == 6                 # the grid of sixths is complete
    assert max(_order(g) for g in ker) == 6                       # cyclic: an element of order 6 generates it
    assert all(al == (2 * q) % 1 and be == (-3 * q) % 1 for al, be, q in ker)   # A = e^{2ia} 1, B = e^{-3ia} 1
    return sorted(int(q * 6) for al, be, q in ker)


def main():
    ker = kernel_elements()
    res = dict(kernel_sixth_root_indices=ker, kernel_order=len(ker),
               global_form="S(U(3)xU(2)) = [SU(3)xSU(2)xU(1)]/Z6",
               ambiguity_resolved="Gamma in {1, Z2, Z3, Z6} all consistent with local SM "
                                  "physics (Tong 1705.01853); the SU(5) chain forces Z6.",
               falsifiable_in_principle="the four quotients differ in their line-operator "
                                        "spectra (one-form symmetry)")
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
    print(f"  kernel = Z_{len(ker)}  (sixth-root indices {ker})")
    print(f"  global form: {res['global_form']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
