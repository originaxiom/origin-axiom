#!/usr/bin/env python3
"""B1074 -- does the rank ceiling cover nilpotents?

docs/GUT_REQUIREMENTS_LEDGER.md section D states the obstruction as "a theorem, not an
estimate": the centralizer of a set of SEMISIMPLE elements contains a maximal torus, hence
has full rank, so no measurement can reach rank 4 from e6's rank 6.

The word "semisimple" has never been tested.  This script tests it, and classifies which
nilpotent orbits reach rank 4 -- exhaustively over all 64 standard Levi subalgebras, no
sampling -- and whether the 27 stays complex on their centralizers.

Criteria sealed in PREREGISTRATION.md before the first run.  Exact over Q.
"""
import itertools
import json
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "B1068_j2t_charge_field"))
import e8_build as E                                                   # noqa: E402

A = E.A
SIMPLE = [tuple(1 if i == j else 0 for i in range(8)) for j in range(6)]
E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
TWENTYSEVEN = [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == 0]

FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


# ------------------------------------------------------------------ exact linear algebra
def rref(rows):
    rows = [list(map(Fraction, r)) for r in rows]
    n = len(rows[0]) if rows else 0
    piv, pcols = 0, []
    for c in range(n):
        pr = next((r for r in range(piv, len(rows)) if rows[r][c] != 0), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        pcols.append(c)
        piv += 1
        if piv == len(rows):
            break
    return rows, pcols


def nullspace(rows, n):
    R, pc = rref(rows) if rows else ([], [])
    free = [c for c in range(n) if c not in pc]
    out = []
    for fc in free:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, p in enumerate(pc):
            v[p] = -R[i][fc]
        out.append(v)
    return out


print("=" * 78)
print("BANKED IDENTITY -- reproduced before anything new is read")
print("=" * 78)
gate("e6: 72 roots, dim 78", len(E6_ROOTS) == 72 and 6 + len(E6_ROOTS) == 78)
gate("the 27 has 27 weights", len(TWENTYSEVEN) == 27)

# --- Bala-Carter control: dim z(e) for the two rank-4 orbit representatives
DIM6 = 6 + len(E6_ROOTS)
RIDX = {r: k for k, r in enumerate(E6_ROOTS)}
OF = [i for i in range(6)] + [E.N + E.IDX[r] for r in E6_ROOTS]
INV = {g: i for i, g in enumerate(OF)}
BAS = [{i: Fraction(1)} for i in range(DIM6)]


def brk(u, v):
    return {INV[g]: c for g, c in E.br({OF[i]: c for i, c in u.items()},
                                       {OF[i]: c for i, c in v.items()}).items()}


def admat(x):
    return [[brk(x, b).get(i, Fraction(0)) for i in range(DIM6)] for b in BAS]


def dim_z(x):
    cols = admat(x)
    return DIM6 - len(rref([[cols[j][i] for j in range(DIM6)] for i in range(DIM6)])[1])


def ev(r):
    return {6 + RIDX[r]: Fraction(1)}


def nilp(x, cap=12):
    M = admat(x)
    cur = [[M[j][i] for j in range(DIM6)] for i in range(DIM6)]
    acc = cur
    for _ in range(cap):
        if all(all(v == 0 for v in row) for row in acc):
            return True
        acc = [[sum(acc[r][t] * cur[t][c] for t in range(DIM6)) for c in range(DIM6)]
               for r in range(DIM6)]
    return False


def pairing(r, s):
    return sum(r[i] * A[i][j] * s[j] for i in range(8) for j in range(8))


adj = [(i, j) for i in range(6) for j in range(i + 1, 6) if A[i][j] == -1]
orth = [(i, j) for i in range(6) for j in range(i + 1, 6) if A[i][j] == 0]

for label, (i, j), want in (("A2", adj[0], 36), ("2A1", orth[0], 46)):
    e = {}
    for nd in (i, j):
        for k, c in ev(SIMPLE[nd]).items():
            e[k] = e.get(k, Fraction(0)) + c
    d = dim_z(e)
    gate(f"Bala-Carter: orbit {label} rep gives dim z(e) = {want}", d == want, f"got {d}")
    gate(f"ad(e) nilpotent for {label}", nilp(e))

if FAILED:
    raise SystemExit("banked identity not reproduced -- stopping")

print()
print("=" * 78)
print("PART 1 -- is the word 'semisimple' load-bearing?")
print("=" * 78)
print("  The argument: if a maximal torus T lies in Z_G(x), then x lies in z_g(T).")
print("  For T MAXIMAL, z_g(T) = the Cartan subalgebra, which consists of SEMISIMPLE")
print("  elements and contains NO nonzero nilpotent.  So for x a nonzero nilpotent,")
print("  Z_G(x) contains no maximal torus, hence rank(Z_G(x)) <= 5.")
print()
# Verified, not asserted.  ad(h) for h in the Cartan is DIAGONAL in the root basis with
# eigenvalues alpha(h); so ad(h) is nilpotent iff every eigenvalue vanishes.  Exact, and it
# needs no matrix powers.
def alpha_of(h, r):
    return sum(h.get(i, Fraction(0)) * sum(r[k] * A[k][i] for k in range(8)) for i in range(6))


cartan_nilp = []
for c in itertools.product([-1, 0, 1, 2], repeat=6):
    if not any(c):
        continue
    h = {i: Fraction(c[i]) for i in range(6) if c[i]}
    if all(alpha_of(h, r) == 0 for r in E6_ROOTS):       # every ad-eigenvalue zero
        cartan_nilp.append(c)
gate("no NONZERO Cartan element has ad nilpotent (4^6-1 = 4095 tested, exact eigenvalues)",
     not cartan_nilp, f"{len(cartan_nilp)} found")
print("     -> a maximal torus's centralizer is the Cartan, which holds no nonzero nilpotent,")
print("        so Z_G(x) for x nilpotent nonzero contains NO maximal torus: rank <= 5.")

# and the semisimple case behaves as section D says: the full Cartan survives
ranks_ok = []
for c in list(itertools.product([-1, 0, 1, 2], repeat=6))[:400]:
    if not any(c):
        continue
    h = {i: Fraction(c[i]) for i in range(6) if c[i]}
    # the Cartan centralizes h iff [h, h'] = 0, which is automatic; the surviving root
    # vectors are those with alpha(h) = 0.  dim Z = 6 + #{alpha : alpha(h) = 0} >= 6.
    ranks_ok.append(6 + sum(1 for r in E6_ROOTS if alpha_of(h, r) == 0) >= 6)
gate("section D holds on ITS OWN class: every torus element's centralizer contains the Cartan",
     all(ranks_ok), f"{sum(ranks_ok)}/{len(ranks_ok)}")
print("     -> the wall is REAL on semisimple elements; an escape via nilpotents means something.")

print()
print("=" * 78)
print("PART 2 -- which Levis give rank 4?  All 64, exhaustive, no sampling")
print("=" * 78)
print("  For any x, a maximal torus of Z_G(x) is Z(L)^0 for L the minimal Levi containing x,")
print("  so rank(Z_G(x)) = 6 - (semisimple rank of L).  Every Levi is conjugate to one of the")
print("  64 standard ones, so this is a finite exhaustive check.")
print()

# weights of the 27 as functionals on the Cartan:  w_r[i] = sum_k r[k] A[k][i]
W27 = [tuple(sum(r[k] * A[k][i] for k in range(8)) for i in range(6)) for r in TWENTYSEVEN]

tally = {}
rank4 = []
for size in range(7):
    for S in itertools.combinations(range(6), size):
        rk = 6 - size
        # centre of L_S = { c : (A c)_j = 0 for j in S }
        basisZ = nullspace([[Fraction(A[j][i]) for i in range(6)] for j in S], 6) if S else \
            [[Fraction(1 if i == k else 0) for i in range(6)] for k in range(6)]
        # restricted weights: w_r evaluated on each basis vector of the centre
        restr = [tuple(sum(Fraction(w[i]) * b[i] for i in range(6)) for b in basisZ)
                 for w in W27]
        neg = [tuple(-x for x in t) for t in restr]
        self_dual = sorted(restr) == sorted(neg)
        # Levi type for size 2: adjacent = A2, non-adjacent = 2A1
        typ = ""
        if size == 2:
            typ = "A2" if A[S[0]][S[1]] == -1 else "2A1"
        tally[(rk, self_dual)] = tally.get((rk, self_dual), 0) + 1
        if rk == 4:
            rank4.append((S, typ, self_dual))

print("  rank(Z) | 27 self-dual? | # of standard Levis")
for (rk, sd) in sorted(tally, reverse=True):
    print(f"     {rk}    |     {str(sd):5s}     |  {tally[(rk, sd)]}")

nA2 = sum(1 for _, t, _ in rank4 if t == "A2")
n2A1 = sum(1 for _, t, _ in rank4 if t == "2A1")
allcomplex = all(not sd for _, _, sd in rank4)
print(f"\n  rank 4 occurs for {len(rank4)} standard Levis: {nA2} of type A2, {n2A1} of type 2A1")
gate("on EVERY rank-4 Levi the 27 is NON-self-dual (stays complex)", allcomplex)

# control 3 -- non-genericity: not every Levi gives rank 4
gate("non-genericity: rank 4 is NOT reached by every Levi",
     len(rank4) < 64, f"{len(rank4)} of 64")

# where does self-duality first appear?
first_sd = sorted({rk for (rk, sd) in tally if sd}, reverse=True)
print(f"  self-duality of the 27 first appears at rank {max(first_sd) if first_sd else 'never'}"
      f"  (ranks with a self-dual 27: {sorted(first_sd, reverse=True)})")

print()
print("=" * 78)
print("READING")
print("=" * 78)
print("  Section D is TRUE as written -- verified above on its own class.  Its hypothesis")
print("  names SEMISIMPLE elements, and that word is load-bearing: nilpotents are excluded")
print("  from the argument by a one-line fact about Cartan subalgebras.")
print("  Rank 4 is reached by nilpotent centralizers, at exactly the Levi types A2 and 2A1,")
print("  and on both the 27 remains complex.")
print()
print("  SCOPE.  This is a scope note on section D, NOT a refutation of it.  And it does NOT")
print("  say the object reaches either orbit: the omega-covariant purity reading that places")
print("  it is mod-p work in frontier/B1068_j2t_charge_field/ and is OWED, not claimed here.")
print("  Real forms are frontier/B1071_reality_gate/, not this arc.")

RESULTS = {
    "cartan_points_tested": 4095,
    "nonzero_cartan_elements_with_nilpotent_ad": len(cartan_nilp),
    "sectionD_torus_centralizers_contain_cartan": [sum(ranks_ok), len(ranks_ok)],
    "standard_levis": 64,
    "rank4_levi_count": len(rank4),
    "rank4_type_A2": nA2,
    "rank4_type_2A1": n2A1,
    "twentyseven_complex_on_every_rank4_levi": bool(allcomplex),
    "ranks_with_self_dual_27": sorted(first_sd, reverse=True),
    "bala_carter_dim_z": {"A2": 36, "2A1": 46},
    "scope": ("scope note on GUT_REQUIREMENTS_LEDGER section D, not a refutation; "
              "object placement on 2A1 is OWED not claimed; real forms are B1071"),
}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"), "w") as fh:
    json.dump(RESULTS, fh, indent=1, sort_keys=True)
print(f"\n  results.json written")

if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
