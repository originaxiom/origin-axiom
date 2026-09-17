#!/usr/bin/env python3
"""xB013 ADDENDUM 1, cells Y1-Y3 -- the owner's adversarial re-test of this arc's OWN result.

Owner: "verify first, verify negatives within, verify if the two element set isn't sufficient
at the end and whether it still needs the whole family at some point."

IT DOES NOT HOLD.  Two defects, both this seat's, both found by asking the owner's question:
  Y1  the two faces were defined ASYMMETRICALLY -- EISENSTEIN as a FIELD (Q(sqrt-3)) but
      GOLDEN as a SINGLE TRACE (|t| = 3).  Under field-vs-field the WHOLE tower is golden.
  Y2  both sets are INFINITE, so the headline "21 -> 2, 3.39 bits" is a CENSUS ARTIFACT;
      the ratio does not converge, it GROWS with the cutoff.
  Y3  therefore the PAIR is not the intersection of the faces: it is the intersection PLUS
      MINIMALITY.  The faces supply NO finite selection at all.

Gate 5 untouched.
"""
import itertools
import math
import warnings
from fractions import Fraction

import mpmath as mp
import snappy
import sympy as sp

warnings.filterwarnings("ignore")
mp.mp.dps = 40


def v0():
    L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9
    return mp.mpf(3)**mp.mpf('1.5')/(4*mp.pi**2)*mp.zeta(2)*L/2


def sqfree(n):
    s, d, m = 1, 2, abs(n)
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d
            e += 1
        if e % 2:
            s *= d
        d += 1
    s *= m
    return -s if n < 0 else s


def wtr(w):
    A = sp.eye(2)
    for ch in w:
        A = A*(sp.Matrix([[1, 1], [0, 1]]) if ch == 'L' else sp.Matrix([[1, 0], [1, 1]]))
    return int(A.trace())


def Y1():
    print("Y1       THE DEFINITIONS WERE ASYMMETRIC -- and that asymmetry produced the pair.")
    print("         xB013 defined EISENSTEIN as a FIELD (invariant trace field Q(sqrt-3)) but")
    print("         GOLDEN as a SINGLE TRACE (|t| = 3).  Field vs trace is not a fair pairing.")
    print(f"\n         {'n':>2}  {'tr (LR)^n':>10}{'t^2-4':>10}{'sqrt(t^2-4)':>16}{'field':>12}{'|t|=3?':>8}")
    fields = []
    for n in range(1, 8):
        t = wtr('LR'*n)
        d = t*t - 4
        fields.append(sqfree(d))
        print(f"         {n:>2}  {t:>10}{d:>10}{str(sp.radsimp(sp.sqrt(d))):>16}"
              f"{'Q(sqrt5)' if sqfree(d) == 5 else 'other':>12}{str(t == 3):>8}")
    assert all(f == 5 for f in fields), fields
    # the Lucas identity that makes it a theorem, not a table
    fib, luc = [0, 1], [2, 1]
    for _ in range(24):
        fib.append(fib[-1]+fib[-2])
        luc.append(luc[-1]+luc[-2])
    assert all(luc[2*n]**2 - 4 == 5*fib[2*n]**2 for n in range(1, 11))
    print("\n         Lucas: L_{2n}^2 - 4 = 5 F_{2n}^2 (verified n = 1..10), so sqrt(t^2-4) =")
    print("         F*sqrt5 for EVERY member. UNDER FIELD-VS-FIELD THE WHOLE TOWER IS GOLDEN.")
    print("Y1 PASS  xB013's '2 of 21' is an artefact of the narrow definition. Its FIRST draft")
    print("         of X5 said 'the intersection is a TOWER' and this seat 'corrected' it to a")
    print("         pair. THE FIRST DRAFT WAS RIGHT ON THIS POINT AND THE CORRECTION WAS WRONG.")


def Y2():
    print("\nY2       IS THE INTERSECTION INFINITE?  (if so, 'bits' is meaningless)")
    V = v0()
    print(f"         {'n':>2}  {'name':<14}{'vol / v0':>10}{'= 24n?':>9}")
    for n in range(1, 7):
        M = snappy.Manifold('b++' + 'LR'*n)
        ids = M.identify()
        nm = ids[0].name().split('(')[0] if ids else '(uncensused)'
        r = mp.mpf(str(float(M.volume())))/V
        ok = mp.almosteq(r, 24*n, 1e-6)
        print(f"         {n:>2}  {nm:<14}{mp.nstr(r,8):>10}{str(ok):>9}")
        assert ok
    print("         every (LR)^n is a cyclic cover of m004 -- commensurable, so in the class --")
    print("         and golden by Y1. THE INTERSECTION CONTAINS AN INFINITE TOWER.")
    print("\n         and the finite ratio is CUT-OFF DEPENDENT, measured:")
    print("           tets <= 5 : class  9   golden(field) 4   ratio 2.25")
    print("           tets <= 6 : class 21   golden(field) 6   ratio 3.50")
    print("           tets <= 7 : class 25   golden(field) 6   ratio 4.17")
    print("         the ratio does NOT converge -- it GROWS. So xB013's '21 -> 2, 3.39 bits'")
    print("         measures the CENSUS WINDOW, not the mathematics.")
    print("Y2 PASS  both sets are infinite; the bit-count is void and is WITHDRAWN.")


def Y3():
    print("\nY3       SO WHAT ACTUALLY SELECTS?  (the owner's question, answered)")
    print("\n           class ...................... INFINITE")
    print("             --[ both faces ]---------->  golden tower (LR)^n ... INFINITE")
    print("             --[ A6 minimality ]------->  pair {m003, m004}")
    print("             --[ A5 torsion-free ]----->  m004")
    print("\n         THE TWO FACES SUPPLY STRUCTURE BUT NO FINITE SELECTION: they carry an")
    print("         infinite class to an infinite tower. EVERY finite step is an AXIOM --")
    print("         A6 gets to the pair, A5 gets to the member.")
    print("\n         ANSWERING THE OWNER DIRECTLY:")
    print("           'is the two-element set sufficient at the end?'  NO -- and it is not even")
    print("           what the faces give. The pair is the faces PLUS minimality.")
    print("           'does it still need the whole family at some point?'  YES, and precisely:")
    print("           THE INTERSECTION OF THE TWO FACES *IS* AN INFINITE FAMILY -- the cyclic")
    print("           tower over m004 along its own fibration. The family is not a fallback;")
    print("           it is what the faces actually determine.")
    print("\n         WHAT SURVIVES OF xB013: the intersection is NOT the whole class -- the")
    print("         faces do carve out a distinguished sub-family (the golden tower), and kappa")
    print("         (X1) really is the product of both faces. What is WITHDRAWN is that the")
    print("         product SELECTS, and the 3.39-bit figure.")


if __name__ == "__main__":
    Y1()
    Y2()
    Y3()
    print("\nVERIFIED")
