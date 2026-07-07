#!/usr/bin/env python3
"""B462 R3b — the silver (m=2) control for the kappa-diagonal.

Identical machinery to kappa_diagonal.py with the silver curve f2(t) = t^2 - 6
(B69, exact). Predictions fixed BEFORE the run (burden-inversion):
  P1: kappa = -2 appears in every fork (the parabolic law — class-generic).
  P2: if Q(sqrt5) / the conductor-7 cubic recur here, they are gluing-word
      arithmetic; if not, they are the fig-8's own (derived) curve data.
Outcome (banked): P1 CONFIRMED (kappa=-2 in all six forks); P2 — neither field
recurs (silver gets Q(sqrt21), a disc -59 cubic, two sextics) => the fig-8
fields are object-derived, not word-forced. LAUNDERS/derived; no H1.
"""
import sys

import sympy as sp

p, r, x = sp.symbols("p r x")


def f(t):
    return t**2 - 6


def act(word, P, Q, R):
    for g in word:
        if g == "S":
            P, Q, R = Q, P, R
        elif g == "T":
            P, Q, R = P, R, P*R - Q
    return P, Q, R


RQUAD = r**2 - p*f(p)*r + p**2 + f(p)**2 - 4


def fork_poly(word):
    P, Q, R = act(word, p, f(p), r)
    cond = sp.expand(sp.numer(sp.together(Q - f(P))))
    if cond == 0:
        return None
    if cond.has(r):
        return sp.factor(sp.resultant(sp.Poly(cond, r), sp.Poly(RQUAD, r), r))
    return sp.factor(cond)


def main():
    p1 = True
    p2_recurrence = []
    fig8_fields = {sp.expand(x**2 - 2*x - 4), sp.expand(x**3 - 2*x**2 - x + 1)}
    for word in ("T", "TT", "S", "ST", "TS", "STS"):
        fp = fork_poly(word)
        assert fp is not None, f"unexpected continuum at phi={word}"
        deg = sp.Poly(sp.expand(fp), p).degree()
        kf = {}
        for g, mult in sp.factor_list(fp)[1]:
            kp = sp.factor(sp.resultant(sp.Poly(g, p), sp.Poly(x - f(p), p), p))
            for kg, km in sp.factor_list(kp)[1]:
                kf[sp.expand(kg)] = kf.get(sp.expand(kg), 0) + km * mult
        print(f"phi={word}: fork size {deg}")
        has_minus2 = False
        for kg, m in sorted(kf.items(), key=lambda t: sp.Poly(t[0], x).degree()):
            d = sp.Poly(kg, x).degree()
            tag = f"disc {sp.discriminant(kg, x)}" if d > 1 else f"kappa={sp.solve(kg, x)[0]}"
            print(f"   (x{m}) {kg}   [{tag}]")
            if sp.expand(kg) == sp.expand(x + 2):
                has_minus2 = True
            if sp.expand(kg) in fig8_fields:
                p2_recurrence.append((word, kg))
        p1 &= has_minus2
    print(f"\nP1 (parabolic law, kappa=-2 in every fork): {'CONFIRMED' if p1 else 'REFUTED'}")
    print(f"P2 (fig-8 fields recur at m=2): {p2_recurrence if p2_recurrence else 'NO RECURRENCE'}")
    ok = p1 and not p2_recurrence
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
