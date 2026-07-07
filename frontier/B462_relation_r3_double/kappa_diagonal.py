#!/usr/bin/env python3
"""B462 R3b — the self-gluing kappa-diagonal of the B174 landscape (m1 = m2 = 1).

B174 banked the fork SIZES (T:9, T^2:10, S:16, ST/TS/STS:32) of the fig-8
self-glue under gluing maps phi; the actual kappa-VALUE sets (the fork's
contents, as exact algebraic numbers) were never extracted. On the fig-8 curve
q = f(p) = p^4 - 5p^2 + 2 (B67), kappa = tr(longitude) = f(p), so each fork
point's kappa is f(p) reduced mod the fork polynomial: the kappa-set's minimal
polynomials come from Res_p(g(p), x - f(p)) per irreducible factor g.

Gate: per-phi degree totals must reproduce B174's banked fork sizes exactly.
Reading: field IDs of the kappa values vs the frozen whitelist
(Q, Q(sqrt5), Q(sqrt-3), Q(sqrt-7), Q(sqrt-15), ...) + the Markov value -2.
"""
import sys

import sympy as sp

p, r, x = sp.symbols("p r x")


def f(t):
    return t**4 - 5*t**2 + 2


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


def field_id(g):
    """name the field of an irreducible factor if it's small/recognizable."""
    d = sp.Poly(g, x).degree()
    if d == 1:
        root = sp.Rational(-sp.Poly(g, x).all_coeffs()[1], sp.Poly(g, x).all_coeffs()[0])
        return f"Q (kappa = {root})"
    if d == 2:
        disc = sp.discriminant(g, x)
        core = sp.factorint(sp.Integer(disc))
        sf = sp.Integer(1)
        for prime, e in core.items():
            if e % 2:
                sf *= prime
        return f"Q(sqrt({sf})) [disc {disc}]"
    return f"degree-{d} field [disc {sp.discriminant(g, x)}]"


BANKED_SIZES = {"T": 9, "TT": 10, "S": 16, "ST": 32, "TS": 32, "STS": 32}


def main():
    ok = True
    for word in ("T", "TT", "S", "ST", "TS", "STS"):
        fp = fork_poly(word)
        assert fp is not None
        total_deg = sp.Poly(sp.expand(fp), p).degree()
        gate = total_deg == BANKED_SIZES[word]
        ok &= gate
        print(f"\n== phi = {word}: fork size {total_deg} "
              f"[gate vs B174 banked {BANKED_SIZES[word]}: {'PASS' if gate else 'FAIL'}] ==")
        kappa_factors = {}
        for g, mult in sp.factor_list(fp)[1]:
            kp = sp.factor(sp.resultant(sp.Poly(g, p), sp.Poly(x - f(p), p), p))
            for kg, kmult in sp.factor_list(kp)[1]:
                kappa_factors[sp.expand(kg)] = kappa_factors.get(sp.expand(kg), 0) + kmult * mult
        for kg, m in sorted(kappa_factors.items(), key=lambda t: sp.Poly(t[0], x).degree()):
            print(f"   kappa-factor (x{m}): {kg}")
            print(f"      -> {field_id(kg)}")
            # flag the Markov value and rational kappas on the whitelist boundary
            if sp.Poly(kg, x).degree() == 1:
                val = sp.Rational(-sp.Poly(kg, x).all_coeffs()[1], sp.Poly(kg, x).all_coeffs()[0])
                if val == -2:
                    print("      ** kappa = -2: the MARKOV surface (the banked heartbeat locus, B448)")
                if val == 2:
                    print("      ** kappa = 2: the reducible/parabolic boundary")
    print("\n" + ("ALL GATES PASS" if ok else "GATE FAILURE"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
