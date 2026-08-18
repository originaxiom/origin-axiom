#!/usr/bin/env python3
"""B1071b -- does the A2 orbit have REAL POINTS in e6(2)?

B1071 left its headline conditional: *if* A2 meets e6(2), its compact su(3)+su(3)
centraliser is available at 3 of 64 characters.  This closes the antecedent.

Kostant-Sekiguchi: real nilpotent G_R-orbits in g_R correspond bijectively to K_C-orbits
on nilpotent elements of p_C, and corresponding orbits lie in the SAME complex orbit.
So the complex orbit O meets g_R  <=>  some nilpotent of p_C lies in O.

With theta = theta_eps diagonal in the Cartan:
    k_C = h (+) span{e_r : eps(r) = +1}      p_C = span{e_r : eps(r) = -1}
Note eps(-r) = eps(r), so p_C is spanned by full root PAIRS and does contain semisimple
elements -- nilpotency is therefore CHECKED, never assumed.

Controls target the reported number.  Nothing is read until they pass.
"""
import itertools
import sys
from fractions import Fraction

sys.path.insert(0, "frontier/B1071_reality_gate")
sys.path.insert(0, "frontier/B1068_j2t_charge_field")
import e8_build as E                                              # noqa: E402
from reality_gate import (E6_ROOTS, RIDX, DIM6, BAS, brk, ad_matrix,   # noqa: E402
                          centralizer, span_dim, eps_of, NAMES, SIMPLE)

print("=" * 78)
print("SETUP -- p_C is spanned by root PAIRS, so nilpotency must be checked")
print("=" * 78)


def e_root(r):
    return {6 + RIDX[r]: Fraction(1)}


def pairing(r, s):
    """<r, s^vee> in the E8 Cartan matrix coordinates (roots are in simple-root coords)."""
    return sum(r[i] * E.A[i][j] * s[j] for i in range(8) for j in range(8)) // 1 if False else \
        sum(r[i] * E.A[i][j] * s[j] for i in range(8) for j in range(8))


def is_root(t):
    return any(t) and t in E.IDX


def ad_nilpotent(x, cap=40):
    M = ad_matrix(x)
    cur = [[M[j][i] for j in range(DIM6)] for i in range(DIM6)]
    acc = cur
    for k in range(1, cap + 1):
        if all(all(v == 0 for v in row) for row in acc):
            return True, k
        acc = [[sum(acc[r][t] * cur[t][c] for t in range(DIM6)) for c in range(DIM6)]
               for r in range(DIM6)]
    return False, None


print()
print("=" * 78)
print("CONTROLS")
print("=" * 78)

# CA -- the pairing routine must reproduce the E6 Cartan matrix on simple roots
okA = all(pairing(SIMPLE[i], SIMPLE[j]) == E.A[i][j] for i in range(6) for j in range(6))
print(f"  CA  pairing() reproduces the E6 Cartan matrix on simple roots: {okA}")

# CB -- a KNOWN A2 pair (adjacent simples) must give dim z = 36 and be nilpotent
e_known = {}
for k, c in e_root(SIMPLE[0]).items():
    e_known[k] = e_known.get(k, Fraction(0)) + c
for k, c in e_root(SIMPLE[2]).items():
    e_known[k] = e_known.get(k, Fraction(0)) + c
dz_known = span_dim(centralizer(e_known))
nil_known, pw = ad_nilpotent(e_known)
okB = dz_known == 36 and nil_known
print(f"  CB  known A2 rep (e_a1 + e_a3): dim z = {dz_known} (want 36), nilpotent ad^{pw}: "
      f"{nil_known} -> {okB}")

# CC -- a SEMISIMPLE element of a root pair must be REJECTED by the nilpotency check
e_ss = {}
for k, c in e_root(SIMPLE[0]).items():
    e_ss[k] = e_ss.get(k, Fraction(0)) + c
mr = tuple(-x for x in SIMPLE[0])
for k, c in e_root(mr).items():
    e_ss[k] = e_ss.get(k, Fraction(0)) + c
nil_ss, _ = ad_nilpotent(e_ss)
okC = not nil_ss
print(f"  CC  e_a1 + e_(-a1) rejected as non-nilpotent: {okC}  (guards p_C's root pairs)")

ok = okA and okB and okC
print(f"\n  ALL CONTROLS PASS: {ok}")
if not ok:
    raise SystemExit("controls failed -- nothing may be read")

print()
print("=" * 78)
print("THE RESULT -- which characters admit A2 (and 2A1) inside p_C")
print("=" * 78)

summary = {}
compact_chars = []
for signs in itertools.product([1, -1], repeat=6):
    ch = eps_of(signs)
    nplus = sum(1 for r in E6_ROOTS if ch(r) == 1)
    dimk = 6 + nplus
    proots = [r for r in E6_ROOTS if ch(r) == -1]

    # A2 inside p_C: a pair of p-roots spanning an A2 (pairing -1), sum a root
    a2_rep = None
    for r, s in itertools.combinations(proots, 2):
        if pairing(r, s) != -1:
            continue
        t = tuple(r[i] + s[i] for i in range(8))
        if not is_root(t):
            continue
        x = {}
        for k, c in e_root(r).items():
            x[k] = x.get(k, Fraction(0)) + c
        for k, c in e_root(s).items():
            x[k] = x.get(k, Fraction(0)) + c
        nil, _ = ad_nilpotent(x)
        if not nil:
            continue
        if span_dim(centralizer(x)) == 36:
            a2_rep = (r, s)
            break

    # 2A1 inside p_C: orthogonal p-roots, sum not a root
    a1_rep = None
    for r, s in itertools.combinations(proots, 2):
        if pairing(r, s) != 0:
            continue
        t = tuple(r[i] + s[i] for i in range(8))
        if is_root(t):
            continue
        x = {}
        for k, c in e_root(r).items():
            x[k] = x.get(k, Fraction(0)) + c
        for k, c in e_root(s).items():
            x[k] = x.get(k, Fraction(0)) + c
        nil, _ = ad_nilpotent(x)
        if not nil:
            continue
        if span_dim(centralizer(x)) == 46:
            a1_rep = (r, s)
            break

    key = (dimk, a2_rep is not None, a1_rep is not None)
    summary[key] = summary.get(key, 0) + 1
    if dimk == 38 and a2_rep is not None:
        compact_chars.append(signs)

print("  ambient form (dim k) | A2 meets p_C | 2A1 meets p_C | # characters")
for (dk, hasA2, hasA1), n in sorted(summary.items(), reverse=True):
    print(f"     dim k={dk:3d} [{NAMES.get(dk,'?'):16s}]  A2: {str(hasA2):5s}  "
          f"2A1: {str(hasA1):5s}   ({n})")

print()
print(f"  characters in e6(2) whose p_C contains an A2 nilpotent: {len(compact_chars)} of 36")
print()
print("  READING:")
print("   - compact e6 must show A2: False and 2A1: False -- a compact real form has NO")
print("     nonzero nilpotent.  If it shows True the method is broken.")
print("   - if A2 meets p_C for e6(2) characters, B1071's conditional headline is DISCHARGED:")
print("     the A2 orbit has real points in the object's sealed real form.")
