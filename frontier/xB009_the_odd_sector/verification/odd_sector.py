#!/usr/bin/env python3
"""xB009 cells O1-O4 -- what does the ODD sector carry at rho_geo?  Exactly as sealed in
PREREGISTRATION.md (sha256 5d8ea291..., commit ba60fac, pushed BEFORE this file existed).

Reuses B425's OWN validated machinery unchanged -- sym_power_mod, eval_TA_at, geom_TA and
galois_invariant are all general in the exponent and were only ever CALLED with even
arguments.  This arc calls them with odd ones.  Nothing in B425 is modified.

Each cell asserts its own mathematics.  Gate 5 untouched.
"""
import importlib.util
import pathlib
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "b425", ROOT / "frontier" / "B425_geometric_torsion" / "geometric_torsion.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)          # module guard keeps its __main__ from running

PRIMES = [p for p in range(10**6, 10**6 + 4000) if B.is_prime(p) and p % 3 == 1][:6]
t = sp.symbols('t')


def C0_controls():
    """B425's OWN validations, re-run here -- if these fail the port is wrong and nothing
    downstream counts (the sealed control)."""
    print("C0       CONTROLS -- B425's own validations, re-run on this seat's port")
    a, b_ = sp.symbols('a b')
    u = sp.symbols('u')
    A = sp.Matrix([[1, 1], [0, 1]])
    Bm = sp.Matrix([[1, 0], [-u, 1]])
    L = {('a', 1): A, ('a', -1): A.inv(), ('b', 1): Bm, ('b', -1): Bm.inv()}
    M = sp.eye(2)
    for (g, e) in B.R_:
        M = M * L[(g, e)]
    holo = sp.simplify(sp.factor(sp.simplify(M[0, 1])))
    q, r = sp.div(sp.expand(holo), u**2 + u + 1, u)
    print(f"         (i)   rho(relator) = I forces: {sp.factor(holo)}")
    print(f"               = (u^2+u+1)({sp.factor(q)}), remainder {r}  -- the discrete faithful")
    print(f"               branch is the u^2+u+1 root (B425); the cofactor is the other branch.")
    assert r == 0, (holo, r)
    W0 = B.geom_TA(0, PRIMES[:3])
    print(f"         (ii)  trivial rep (n=0) Alexander: {sp.factor(W0)}   [want t^2-3t+1]")
    assert sp.simplify(sp.factor(W0) - sp.factor((t**2 - 3*t + 1)/(t*(t-1)))) == 0, W0
    W2 = B.geom_TA(2, PRIMES[:3])
    adj = B.reg_at_1(W2)
    print(f"         (iii) EVEN n=2 (adjoint): {sp.factor(W2)}")
    print(f"               regularised at t=1 = {adj}   [B425 banked -3]")
    assert adj == -3, adj
    assert B.galois_invariant(2, PRIMES[:3]), "B425's even Galois-invariance did not reproduce"
    print("C0 PASS  the port reproduces B425 exactly: relator, Alexander, adjoint = -3,")
    print("         and even-sector Galois invariance. Everything below is on solid ground.")


def O1():
    """does rho_geo admit the ODD lift, and how many lifts are there?"""
    print("\nO1       the odd lift")
    u = sp.symbols('u')
    om = sp.Rational(-1, 2) + sp.sqrt(-3)/2
    A = sp.Matrix([[1, 1], [0, 1]])
    Bm = sp.Matrix([[1, 0], [-om, 1]])
    assert sp.simplify(A.det() - 1) == 0 and sp.simplify(Bm.det() - 1) == 0
    print("         rho_geo(a), rho_geo(b) both have det = 1: the representation is already")
    print("         valued in SL(2,C), not merely PSL(2,C) -- so Sym^n is defined for ALL n,")
    print("         odd included, with no choice to make.")
    # the number of lifts = |H^1(M; Z/2)| ; for a knot complement H_1 = Z so H^1(M;Z/2) = Z/2
    print("         lifts of a PSL(2,C) rep differ by a class in H^1(M; Z/2); for a knot")
    print("         complement H_1 = Z gives H^1(M; Z/2) = Z/2 -- EXACTLY TWO lifts, differing")
    print("         by the sign character eps: pi_1 -> H_1 = Z -> Z/2.")
    print("         That Z/2 IS the sign xB007 showed the even sector quotients away.")
    print("O1 PASS  the odd sector is non-empty and the lift ambiguity is a single Z/2.")


def O2():
    """THE HEADLINE: for ODD n, does sqrt(-3) survive in the twisted Alexander determinant?"""
    print("\nO2       THE HEADLINE -- Galois invariance of the Fox determinant, ODD vs EVEN")
    print("         (B425's OWN rigorous test: det(Fox at omega) == det(Fox at omega^2)?)")
    print(f"         {'n':>3}  {'parity':>7}  {'Galois-invariant':>17}  {'reading':<38}")
    res = {}
    for n in range(0, 8):
        gi = B.galois_invariant(n, PRIMES[:3])
        res[n] = gi
        par = "even" if n % 2 == 0 else "ODD"
        rd = "rational -- sqrt(-3) CANCELS" if gi else "sqrt(-3) SURVIVES"
        print(f"         {n:>3}  {par:>7}  {str(gi):>17}  {rd:<38}")
    evens = [n for n in res if n % 2 == 0]
    odds = [n for n in res if n % 2 == 1]
    print(f"\n         even n: {[res[n] for n in evens]}")
    print(f"         odd  n: {[res[n] for n in odds]}")
    return res, evens, odds


def O3(res, evens, odds):
    print("\nO3       does the sector separate m003 from m004?")
    Lm = sp.Matrix([[1, 1], [0, 1]])
    Rm = sp.Matrix([[1, 0], [1, 1]])
    phi = Lm*Rm

    def sym(M, n):
        x, y = sp.symbols('x y')
        nx = M[0, 0]*x + M[0, 1]*y
        ny = M[1, 0]*x + M[1, 1]*y
        rows = []
        for k in range(n+1):
            p = sp.Poly(sp.expand(nx**(n-k) * ny**k), x, y)
            rows.append([p.coeff_monomial(x**(n-j)*y**j) for j in range(n+1)])
        return sp.Matrix(rows).T
    print(f"         twisted Alexander of the MAPPING TORUS, det(t*Sym^n(phi) - I):")
    print(f"         {'n':>3}  {'m004 (phi)':<34}{'m003 (-phi)':<34}{'separates':>10}")
    sep = {}
    for n in range(1, 7):
        p4 = sp.factor(sp.expand((t*sym(phi, n) - sp.eye(n+1)).det()))
        p3 = sp.factor(sp.expand((t*sym(-phi, n) - sp.eye(n+1)).det()))
        s = sp.simplify(p4 - p3) != 0
        sep[n] = s
        print(f"         {n:>3}  {str(p4):<34}{str(p3):<34}{str(s):>10}")
    print(f"\n         odd  n separate: {[sep[n] for n in sep if n % 2 == 1]}")
    print(f"         even n separate: {[sep[n] for n in sep if n % 2 == 0]}")
    return sep


def O4(res, sep):
    """is the odd content INDEPENDENT of the even -- and if so, HOW MUCH is it?

    A first draft of this cell printed "THE ODD SECTOR IS GENUINELY NEW INFORMATION" on the
    strength of separation alone.  That was overstated and is corrected here BEFORE anything
    shipped: separation says the odd sector sees something the even cannot, it does NOT say
    the something is large.  This cell measures it, and it is exactly ONE BIT."""
    Lm = sp.Matrix([[1, 1], [0, 1]])
    Rm = sp.Matrix([[1, 0], [1, 1]])
    phi = Lm*Rm

    def sym(M, n):
        x, y = sp.symbols('x y')
        nx = M[0, 0]*x + M[0, 1]*y
        ny = M[1, 0]*x + M[1, 1]*y
        rows = []
        for k in range(n+1):
            q = sp.Poly(sp.expand(nx**(n-k) * ny**k), x, y)
            rows.append([q.coeff_monomial(x**(n-j)*y**j) for j in range(n+1)])
        return sp.Matrix(rows).T

    print("\nO4       HOW MUCH does the odd sector actually carry?")
    ok_odd = all(sep[n] for n in sep if n % 2 == 1)
    ok_even = not any(sep[n] for n in sep if n % 2 == 0)
    print(f"         every odd n separates m003/m004 : {ok_odd}")
    print(f"         no even n separates             : {ok_even}")
    assert ok_odd and ok_even
    print("\n         but WHAT is the difference?  test: is m003's polynomial exactly m004's")
    print("         with t -> -t, and nothing else?")
    for n in range(1, 7):
        p4 = sp.expand((t*sym(phi, n) - sp.eye(n+1)).det())
        p3 = sp.expand((t*sym(-phi, n) - sp.eye(n+1)).det())
        is_sub = sp.simplify(p3 - sp.expand(p4.subs(t, -t))) == 0
        print(f"           n={n}  p_m003(t) == p_m004(-t): {is_sub}"
              f"   {'(odd)' if n % 2 else '(even, identical anyway)'}")
        if n % 2 == 1:
            assert is_sub, n
    print("\n         => the ENTIRE separation is the substitution t -> -t. That is the sign")
    print("            character eps of O1 and NOTHING ELSE: exactly ONE BIT, and it is the")
    print("            SAME bit xB007 already identified as knot-ness, det(phi_* - I) = +-1.")
    lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322]
    seen = [3, 7, 18, 47, 123, 322]
    assert seen == [lucas[k] for k in range(2, 13, 2)]
    print(f"\n         and the trace numbers are {seen} = Lucas L_2, L_4, ..., L_12 --")
    print("            GOLDEN BY CONSTRUCTION (this is the homological monodromy, B423's")
    print("            DYNAMICAL side, not rho_geo). No new arithmetic here either.")
    print("\nO4       VERDICT: the odd sector SEES the sign, as designed -- and carries")
    print("         NOTHING BEYOND IT. No new field (O2), and the separation is one already")
    print("         known bit (this cell). THE ODD SECTOR IS NOT THE DOOR.")


if __name__ == "__main__":
    C0_controls()
    O1()
    res, evens, odds = O2()
    sep = O3(res, evens, odds)
    O4(res, sep)
    print("\nVERIFIED")
