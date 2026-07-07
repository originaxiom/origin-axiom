#!/usr/bin/env python3
"""B448 — the trace-map periodic-orbit field tower (Chat-1's decisive open question), EXACT.

Repo convention (B416): T1(x,y,z) = (z, x, xz−y); the figure-eight monodromy = T1^2;
kappa = x^2+y^2+z^2−xyz−2 conserved.

Key reduction (verified against T1 numerically below): writing the orbit as a sequence,
T1-orbits are exactly the solutions of the cyclic quadratic recursion

    a_{n+2} = a_n * a_{n+1} − a_{n−1}        (indices mod k for a period-k orbit),

with the state at time n being (x,y,z) = (a_n, a_{n−1}, a_{n+1}). The cusp locus is
kappa = −2  <=>  a_n^2 + a_{n−1}^2 + a_{n+1}^2 − a_n a_{n−1} a_{n+1} = 0 (any one n).

So period-k orbits on kappa=−2 form an exact ideal: k quadrics + 1 cubic in k unknowns.
We solve by Groebner elimination over QQ, factor the univariate eliminant, mark
lower-period factors, and read off each orbit's field. Sanity anchors: k=1 -> a=0
(the (0,0,0) fixed point; a=2 is the void, kappa=+2, excluded); k=2 -> x^2−3x+3
(disc −3: the discrete-faithful pair — the trace field Q(sqrt−3)).

Run: python3 orbit_fields.py     (prints the field tower, k = 1..7)
"""
import sympy as sp


def sanity_recursion_matches_T1():
    import random
    random.seed(1)
    for _ in range(20):
        x, y, z = [random.uniform(-2, 2) for _ in range(3)]
        states = [(x, y, z)]
        for _ in range(6):
            X, Y, Z = states[-1]
            states.append((Z, X, X * Z - Y))
        a = [y, x, z]                       # a_{n-1}, a_n, a_{n+1} at n=1
        for n in range(1, 6):
            a.append(a[n] * a[n + 1] - a[n - 1])
        for i, (X, Y, Z) in enumerate(states[:5]):
            n = i + 1
            assert abs(a[n] - X) + abs(a[n - 1] - Y) + abs(a[n + 1] - Z) < 1e-9
    return True


def orbit_eliminant(k):
    """Factored univariate eliminant for period-k orbits on kappa=-2."""
    A = sp.symbols(f'a0:{k}')

    def a(n):
        return A[n % k]

    eqs = [sp.expand(a(n + 2) - a(n) * a(n + 1) + a(n - 1)) for n in range(k)]
    eqs.append(sp.expand(a(0) ** 2 + a(k - 1) ** 2 + a(1) ** 2
                         - a(0) * a(k - 1) * a(1)))
    G = sp.groebner(eqs, *A, order='lex')
    last = A[-1]
    uni = [g for g in G.exprs if g.free_symbols <= {last}]
    if not uni:
        return None
    return sp.factor_list(sp.Poly(uni[0], last).as_expr())


def field_label(fac, var):
    p = sp.Poly(fac, var)
    d = p.degree()
    if d == 1:
        return "Q"
    disc = sp.discriminant(fac, var)
    if d == 2:
        sf = sp.factorint(sp.Integer(disc))
        sq = sp.Integer(1)
        for q, e in sf.items():
            if q == -1:
                if e % 2:
                    sq *= -1
                continue
            if e % 2:
                sq *= q
        return f"Q(sqrt({sq}))  [disc {disc}]"
    return f"deg-{d}, disc = {disc} = {sp.factorint(sp.Integer(disc))}"


def main():
    assert sanity_recursion_matches_T1()
    print("recursion == T1 dynamics: verified numerically (20 random states)")
    print()
    seen = set()
    for k in range(1, 8):
        fl = orbit_eliminant(k)
        if fl is None:
            print(f"period {k}: (no univariate eliminant — inspect)")
            continue
        _, factors = fl
        print(f"== period {k}: eliminant factors on kappa=-2 ==")
        for fac, mult in factors:
            fs = list(fac.free_symbols)
            if not fs:
                continue
            var = fs[0]
            key = sp.srepr(sp.expand(fac.subs(var, sp.Symbol('t'))))
            tag = "" if key not in seen else "   [seen at lower period]"
            seen.add(key)
            print(f"   {sp.expand(fac)}   -> {field_label(fac, var)}{tag}")
        print(flush=True)


if __name__ == '__main__':
    main()
