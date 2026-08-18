#!/usr/bin/env python3
"""B8071 -- the reality gate, in characteristic zero.

Two panels stopped at the same wall: mod-p Killing RANK is identical for every real form
of a given complex algebra.  A real form is named instead by dim k, the dimension of its
maximal compact subalgebra -- an exact integer.

Real forms of complex simple g <-> involutions theta of the compact form u, with
u = k (+) m the +-1 eigenspaces and g_R = k (+) i.m.  For a theta-stable complex
subalgebra c, the induced real form has maximal compact c ^ k, so dim(c ^ k_C) names it.

Criteria sealed in PREREG_reality_gate.md BEFORE this ran.  Controls target the measured
number itself, not its neighbourhood.
"""
import itertools
import os
import sys
from fractions import Fraction

sys.path.insert(0, "../B8068_j2t_charge_field")
sys.path.insert(0, "frontier/B8068_j2t_charge_field")
import e8_build as E                                    # noqa: E402

# ------------------------------------------------------------------ e6 inside e8
# Bourbaki: the first six nodes are E6.  E6 roots = E8 roots supported on nodes 0..5.
E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
NR = len(E6_ROOTS)
RIDX = {r: k for k, r in enumerate(E6_ROOTS)}
DIM6 = 6 + NR
# basis index: 0..5 = Cartan h_0..h_5 ; 6+k = e_{E6_ROOTS[k]}
E8_OF = [i for i in range(6)] + [E.N + E.IDX[r] for r in E6_ROOTS]
OF_E8 = {g: i for i, g in enumerate(E8_OF)}


def lift(vec):
    """e6-index vector (dict) -> e8-index vector."""
    return {E8_OF[i]: c for i, c in vec.items()}


def drop(vec8):
    """e8-index vector -> e6-index vector; raises if it leaves e6."""
    out = {}
    for g, c in vec8.items():
        if g not in OF_E8:
            raise ValueError("bracket left e6")
        out[OF_E8[g]] = c
    return out


def brk(u, v):
    return drop(E.br(lift(u), lift(v)))


BAS = [{i: Fraction(1)} for i in range(DIM6)]


def ad_matrix(x):
    """ad(x) as a DIM6 x DIM6 list-of-lists of Fractions (columns = images of basis)."""
    cols = []
    for b in BAS:
        img = brk(x, b)
        cols.append([img.get(i, Fraction(0)) for i in range(DIM6)])
    return cols                                        # cols[j][i] = coeff of basis i in ad(x)b_j


def rank_frac(rows):
    """exact rank of a list of row-vectors of Fractions."""
    rows = [list(r) for r in rows]
    n = len(rows[0]) if rows else 0
    piv = 0
    for c in range(n):
        pr = None
        for r in range(piv, len(rows)):
            if rows[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        piv += 1
        if piv == len(rows):
            break
    return piv


def nullspace(rows, n):
    """basis of the nullspace of the matrix whose ROWS are given, over Q."""
    rows = [list(r) for r in rows]
    piv_col = []
    piv = 0
    for c in range(n):
        pr = None
        for r in range(piv, len(rows)):
            if rows[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        piv_col.append(c)
        piv += 1
        if piv == len(rows):
            break
    free = [c for c in range(n) if c not in piv_col]
    out = []
    for fc in free:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv_col):
            v[pc] = -rows[i][fc]
        out.append(v)
    return out


def centralizer(x):
    """{y : [x,y] = 0} as a list of coordinate vectors."""
    cols = ad_matrix(x)                                # cols[j] = ad(x) b_j
    rows = [[cols[j][i] for j in range(DIM6)] for i in range(DIM6)]
    return nullspace(rows, DIM6)


def span_dim(vs):
    return rank_frac(vs) if vs else 0


print("=" * 78)
print("SETUP")
print("=" * 78)
print(f"  e6 roots: {NR}   dim e6 = {DIM6}   (want 72, 78)")
assert (NR, DIM6) == (72, 78)

# ------------------------------------------------------------------ CONTROLS
print()
print("=" * 78)
print("CONTROLS -- each aimed at the number this cell reports")
print("=" * 78)

# C1 -- the real-form census must reproduce E6 theory unprompted
SIMPLE = [tuple(1 if i == j else 0 for i in range(8)) for j in range(6)]


def eps_of(signs):
    """sign character on the root lattice from its values on the 6 simple roots."""
    def f(r):
        s = 1
        for j in range(6):
            if r[j] % 2:
                s *= signs[j]
        return s
    return f


census = {}
for signs in itertools.product([1, -1], repeat=6):
    ch = eps_of(signs)
    nplus = sum(1 for r in E6_ROOTS if ch(r) == 1)
    dimk = 6 + nplus
    census[dimk] = census.get(dimk, 0) + 1
print(f"  C1  inner sign-character census, dim k -> count: {dict(sorted(census.items()))}")
NAMES = {78: "compact e6(-78)", 46: "e6(-14)", 38: "e6(2)"}
c1 = set(census) == {78, 46, 38}
print(f"      identified: {[(d, NAMES.get(d,'?')) for d in sorted(census, reverse=True)]}")
print(f"      only {{78, 46, 38}} occur (B907 reports 78x1, 46x27, 38x36): {c1}")

# C2 -- theta is an automorphism, verified on brackets not assumed
def theta_apply(vec, ch):
    out = {}
    for i, c in vec.items():
        out[i] = c if i < 6 else c * ch(E6_ROOTS[i - 6])
    return out


import random                                          # noqa: E402
rnd = random.Random(20260817)
ch_test = eps_of((1, -1, 1, -1, 1, 1))                 # B907's wall-real character
bad = 0
for _ in range(300):
    i, j = rnd.randrange(DIM6), rnd.randrange(DIM6)
    lhs = theta_apply(brk(BAS[i], BAS[j]), ch_test)
    rhs = brk(theta_apply(BAS[i], ch_test), theta_apply(BAS[j], ch_test))
    if lhs != rhs:
        bad += 1
c2 = bad == 0
print(f"  C2  theta[x,y] == [theta x, theta y] on 300 random basis pairs: failures {bad} -> {c2}")

# C3/C4 -- nilpotent representatives, identified by centraliser dimension
def e_root(r):
    return {6 + RIDX[r]: Fraction(1)}


a = SIMPLE
# 2A1: two ORTHOGONAL simple roots (nodes 1 and 2 in Bourbaki E6 are non-adjacent)
# A2 : two ADJACENT simple roots
def cartan_entry(i, j):
    return E.A[i][j]


orth = [(i, j) for i in range(6) for j in range(i + 1, 6) if cartan_entry(i, j) == 0]
adj = [(i, j) for i in range(6) for j in range(i + 1, 6) if cartan_entry(i, j) == -1]
print(f"  C3  non-adjacent simple pairs: {len(orth)}   adjacent: {len(adj)}")

results = {}
for label, pairs, want_z, want_red in (("2A1", orth, 46, 22), ("A2", adj, 36, 16)):
    found = None
    for (i, j) in pairs:
        e = {}
        for k, c in e_root(a[i]).items():
            e[k] = e.get(k, Fraction(0)) + c
        for k, c in e_root(a[j]).items():
            e[k] = e.get(k, Fraction(0)) + c
        z = centralizer(e)
        dz = span_dim(z)
        if dz == want_z:
            found = (i, j, e, z, dz)
            break
    results[label] = found
    if found:
        i, j, e, z, dz = found
        # C4 nilpotency: ad(e)^k = 0 for some k
        M = ad_matrix(e)
        cur = [[M[j2][i2] for j2 in range(DIM6)] for i2 in range(DIM6)]
        pw, nilp = 1, False
        acc = cur
        while pw <= 40:
            if all(all(v == 0 for v in row) for row in acc):
                nilp = True
                break
            acc = [[sum(acc[r][k] * cur[k][c2] for k in range(DIM6)) for c2 in range(DIM6)]
                   for r in range(DIM6)]
            pw += 1
        print(f"  C3  orbit {label}: e = e_a{i+1} + e_a{j+1}   dim z(e) = {dz} (want {want_z}) "
              f"-> {dz == want_z}")
        print(f"  C4  ad(e) nilpotent (ad^{pw} = 0): {nilp}")
    else:
        print(f"  C3  orbit {label}: NO representative with dim z = {want_z} found -- STOP")

c3 = all(results[k] is not None for k in results)
ok = c1 and c2 and c3
print(f"\n  ALL CONTROLS PASS: {ok}")
if not ok:
    raise SystemExit("controls failed -- nothing may be read")

# ------------------------------------------------------------------ THE RESULT
print()
print("=" * 78)
print("THE RESULT -- which real forms are available to the rank-4 centralisers")
print("=" * 78)

SU3SU3 = {16: "su(3)+su(3) COMPACT", 12: "su(3)+su(2,1)", 11: "su(3)+sl(3,R)",
          8: "su(2,1)+su(2,1)", 7: "su(2,1)+sl(3,R)", 6: "sl(3,R)+sl(3,R)"}
SO7U1 = {22: "so(7)+u(1) COMPACT", 16: "so(6,1)+u(1)", 12: "so(5,2)+u(1)",
         10: "so(4,3)+u(1)", 15: "so(6,1)+R", 11: "so(5,2)+R", 9: "so(4,3)+R"}

RESULTS = {"census": {str(k): v for k, v in sorted(census.items())}, "orbits": {}}

for label, table in (("2A1", SO7U1), ("A2", SU3SU3)):
    i, j, e, z, dz = results[label]
    # reductive part: z(e) modulo its nilradical is hard; instead use z(e,h,f).
    # Build h from the sl2-triple: for e = e_ai + e_aj with the two roots in a Levi L,
    # h = sum of coroots of the positive roots of L (standard), f = e_{-ai} + e_{-aj} scaled.
    h = {}
    for nd in (i, j):
        for k2 in range(6):
            h[k2] = h.get(k2, Fraction(0)) + Fraction(2 * (1 if k2 == nd else 0))
    f = {}
    for nd in (i, j):
        nr = tuple(-x for x in a[nd])
        for k2, c in e_root(nr).items():
            f[k2] = f.get(k2, Fraction(0)) + c
    # z(e,h,f) = z(e) ^ z(h) ^ z(f)
    rows = []
    for x in (e, h, f):
        cols = ad_matrix(x)
        rows += [[cols[jj][ii] for jj in range(DIM6)] for ii in range(DIM6)]
    zred = nullspace(rows, DIM6)
    dred = span_dim(zred)
    print(f"\n  orbit {label}:  dim z(e) = {dz},  dim z(e,h,f) = {dred}")

    # for each real form, dim(zred ^ k_C)
    seen = {}
    for signs in itertools.product([1, -1], repeat=6):
        ch = eps_of(signs)
        nplus = sum(1 for r in E6_ROOTS if ch(r) == 1)
        dimk = 6 + nplus
        # k_C = +1 eigenspace of theta; intersect with span(zred)
        kept = []
        for v in zred:
            w = theta_apply({ii: c for ii, c in enumerate(v) if c != 0}, ch)
            wv = [w.get(ii, Fraction(0)) for ii in range(DIM6)]
            if wv == list(v):
                kept.append(v)
        # proper intersection: solve (theta - 1) x = 0 restricted to span(zred)
        M = []
        for v in zred:
            w = theta_apply({ii: c for ii, c in enumerate(v) if c != 0}, ch)
            M.append([w.get(ii, Fraction(0)) - v[ii] for ii in range(DIM6)])
        coef_ns = nullspace([[M[r][c2] for r in range(len(zred))] for c2 in range(DIM6)],
                            len(zred))
        dint = len(coef_ns) - (len(coef_ns) - rank_frac(coef_ns) if coef_ns else 0)
        dint = rank_frac(coef_ns) if coef_ns else 0
        seen.setdefault((dimk, dint), 0)
        seen[(dimk, dint)] += 1
    print(f"    ambient form (dim k) x dim(z_red ^ k) -> count:")
    for (dk, di), n in sorted(seen.items(), reverse=True):
        nm = table.get(di, f"dim k={di}: not in table")
        print(f"      e6 dim k={dk:3d} [{NAMES.get(dk,'?'):16s}]  z_red ^ k = {di:3d}  "
              f"[{nm}]   ({n} characters)")
    vary = len({di for (_, di) in seen}) > 1
    print(f"    C5 false-positive control -- dim(z_red ^ k) VARIES across characters: {vary}")
    RESULTS["orbits"][label] = {
        "dim_z_e": dz,
        "dim_z_ehf": dred,
        "by_form": {f"{dk}|{di}": n for (dk, di), n in sorted(seen.items(), reverse=True)},
        "compact_dim": max(table),
        "compact_in_e6_2": seen.get((38, max(table)), 0),
        "compact_in_e6_m14": seen.get((46, max(table)), 0),
        "varies": bool(vary),
    }

import json                                                                # noqa: E402
RESULTS["scope"] = ("computes which real forms are AVAILABLE to the centralisers; does NOT "
                    "verify the object OCCUPIES any. The compact-e6 row is vacuous by "
                    "construction (a compact form has no nonzero nilpotent) and is retained "
                    "as a visible marker of that gap.")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"), "w") as fh:
    json.dump(RESULTS, fh, indent=1, sort_keys=True)
print("\n  results.json written")
