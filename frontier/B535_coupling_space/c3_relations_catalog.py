#!/usr/bin/env python3
"""B535 C3: the relations catalog — measure one number, compute all others.

Exact Perron eigenvectors for all 6 coupling types (adjugate over Q(tau),
tau = sqrt(phi), tau^4 = tau^2 + 1). For every distinct component x:
  - degree of x over Q (4 = complete measurement, <4 = degenerate)
  - for complete x: the explicit cubic g with tau = g(x) — the dictionary
    entry that turns one measured number into every other read-out.

Also: the algebraic verification that the second C2 language-survivor is
EXACTLY the conjugate a^-1 sigma(.) a.
"""
import sys
import os
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system,
)

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1
TAU_R = sp.sqrt((1 + sp.sqrt(5)) / 2)
BETA_T = t**2 + t**3


def red(e):
    return sp.rem(sp.expand(e), MIN, t)


def inv(e):
    p = sp.Poly(red(e), t, domain='QQ')
    m = sp.Poly(MIN, t, domain='QQ')
    s, _, h = sp.gcdex(p, m)
    return red(s.as_expr() / h.as_expr())


def analyze_matrix(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    rws = standard_return_words_from_positions(host, fpm[factor], trim=trim)
    return sp.Matrix(canonical_induced_system(rws, max_power=2)['matrix'])


BETA_SQ_T = red(BETA_T**2)      # beta^2 = 2 + 2t + 3t^2 + 2t^3


def exact_perron(A):
    """Handles both induction powers: A_u ~ M^q + 0 with q in {1,2}
    (the banked B530 law); Perron eigenvalue beta or beta^2."""
    n = A.rows
    Af = np.array([[float(A[i, j]) for j in range(n)] for i in range(n)])
    pf = max(abs(np.linalg.eigvals(Af)))
    beta_num = float(sp.expand(BETA_T).evalf(30, subs={t: TAU_R}))
    if abs(pf - beta_num) < 1e-6:
        lam = BETA_T
    elif abs(pf - beta_num**2) < 1e-4:
        lam = BETA_SQ_T
    else:
        raise ValueError(f"Perron {pf} is neither beta nor beta^2")
    N = (A - sp.expand(lam) * sp.eye(n)).applyfunc(sp.expand)
    adj = N.adjugate().applyfunc(red)
    col = None
    for j in range(n):
        c = [adj[i, j] for i in range(n)]
        vals = [float(sp.expand(e).evalf(30, subs={t: TAU_R})) for e in c]
        if all(abs(x) > 1e-12 for x in vals):
            col = c
            break
    vcol = sp.Matrix(col)
    resid = (A * vcol - sp.expand(lam) * vcol).applyfunc(red)
    assert all(e == 0 for e in resid)
    s_inv = inv(red(sum(col)))
    out = [red(e * s_inv) for e in col]
    vals = [float(sp.expand(e).evalf(30, subs={t: TAU_R})) for e in out]
    if any(v < 0 for v in vals):
        out = [red(-e) for e in out]
        vals = [-v for v in vals]
    assert all(v > 0 for v in vals)
    return out, vals


def coeffs(e):
    p = sp.Poly(red(e), t, domain='QQ')
    return tuple(p.coeff_monomial(t**k) for k in range(4))


def tau_in_terms_of(e):
    """If Q(e) = Q(tau): the cubic g with tau = g(e). Else None."""
    powers = [red(e**k) for k in range(4)]     # 1, e, e^2, e^3 in tau-basis
    B = sp.Matrix([[sp.Poly(pw, t, domain='QQ').coeff_monomial(t**k)
                    for pw in powers] for k in range(4)])
    if B.det() == 0:
        return None
    c = B.solve(sp.Matrix([0, 1, 0, 0]))       # coords of tau
    return c


def main():
    print("=" * 76)
    print("B535 C3 — the relations catalog")
    print("=" * 76)

    # ── conjugacy proof for the second C2 survivor ──
    SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
    SURV = {'a': 'bAABa', 'b': 'ABa', 'A': 'bABa', 'B': 'Aa'}
    conj_ok = all(SURV[g] == SUB[g][1:] + SUB[g][0] for g in 'abAB') and \
              all(SUB[g][0] == 'a' for g in 'abAB')
    print(f"\nC2 survivor #2 == a^-1 sigma(.) a exactly "
          f"(every image starts with 'a', rotate by one): {conj_ok}")

    # ── exact Perron vectors for the 6 types ──
    host = grow(10)
    reps = {'T1': 'a', 'T2': 'B', 'T3': 'A', 'T4': 'aA', 'T5': 'Bab',
            'T6': 'bABab'}
    all_components = {}   # coeff-tuple -> (float, type list)
    for label, factor in reps.items():
        A = analyze_matrix(factor, host)
        vec, vals = exact_perron(A)
        print(f"\n{label} (u='{factor}', rc={A.rows}):")
        for e, x in sorted(zip(vec, vals), key=lambda p: -p[1]):
            key = coeffs(e)
            all_components.setdefault(key, [x, []])[1].append(label)
            c0, c1, c2, c3 = key
            print(f"  {x:.10f} = ({c0}) + ({c1})t + ({c2})phi + ({c3})t^3")

    # ── the dictionary ──
    print(f"\n{'='*76}\nTHE READ-OUT DICTIONARY "
          f"({len(all_components)} distinct components)\n{'='*76}")
    print(f"\n{'value':>14} {'deg':>4} {'types':>12}   tau = g(x)")
    n_complete = n_degenerate = 0
    degen = []
    for key, (x, labels) in sorted(all_components.items(), key=lambda kv: -kv[1][0]):
        e = sum(c * t**k for k, c in enumerate(key))
        g = tau_in_terms_of(e)
        if g is not None:
            n_complete += 1
            gs = " + ".join(f"({sp.nsimplify(g[k])})x^{k}" for k in range(4)
                            if g[k] != 0)
            # exact check: g(e) == tau
            check = red(sum(g[k] * e**k for k in range(4)) - t) == 0
            assert check
            print(f"{x:14.10f} {4:>4} {'/'.join(sorted(set(labels))):>12}   {gs}")
        else:
            n_degenerate += 1
            expr = sum(c * TAU_R**k for k, c in enumerate(key))
            mp = sp.minimal_polynomial(expr, t)
            degen.append((x, labels, mp))
            print(f"{x:14.10f} {sp.degree(mp):>4} "
                  f"{'/'.join(sorted(set(labels))):>12}   DEGENERATE: minpoly {mp}")

    print(f"\ncomplete (degree-4) measurements: {n_complete}")
    print(f"degenerate measurements: {n_degenerate}")
    print(f"""
VERDICT:
  every degree-4 component is a COMPLETE measurement: the explicit cubic
  g recovers tau = g(x) exactly, and every other read-out of every coupling
  type is then a known element of Q(tau). One number in, all numbers out.
""")


if __name__ == '__main__':
    main()
