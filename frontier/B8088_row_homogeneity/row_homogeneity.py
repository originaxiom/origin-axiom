#!/usr/bin/env python3
"""B8088 -- the Z/5 menu is homogeneous, but ARITHMETICALLY: W alone gives 25 orbits, not 9.

THE CLAIM UNDER TEST.  The owner's synthesis states, attributing it to B8086: "the Z/5 menu is
exactly one W x Galois orbit per row -- perfectly homogeneous; no counting rule can prefer a
point."  B8086 verified the nine ROWS, their COUNTS, and that every row has RANK 6.  It did NOT
compute orbits.  "One orbit per row" is strictly stronger than "one centraliser type per row":
a row is a FIBRE of the type map, and a fibre may be a union of several orbits of the same type.

WHY THE DISTINCTION IS LOAD-BEARING.  A single orbit forces a UNIQUE invariant measure.  A union
of k orbits admits a (k-1)-parameter family of invariant measures -- reweight the pieces freely.
So the "only object-consistent measure is uniform" step depends entirely on which is true, and on
WHICH GROUP is required to preserve it.

RESULT.  The claim holds -- but only for W x Galois.  Under W alone eight of the nine rows split.

QUANTIFIER (COMPUTE_THE_PROGRAM): the ALGEBRA -- the W-action on the 5-torsion of the E6 torus.
Nothing about the member, the class, the sisters or the rows of the manifold.  Gate 5 untouched.
"""
import itertools, collections, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]     # E6 Dynkin, as in B8086
N, P = 6, 5
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1

FAILED = []
def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILED.append(label)

# ------------------------------------------------------------------ the roots
simp = [tuple(1 if i == k else 0 for i in range(N)) for k in range(N)]
R, fr = set(simp), list(simp)
while fr:
    nx = []
    for r in fr:
        for j in range(N):
            pr = sum(r[i] * A[i][j] for i in range(N))
            s = tuple(r[i] - pr * (1 if i == j else 0) for i in range(N))
            if any(s) and s not in R:
                R.add(s); nx.append(s)
    fr = nx
ROOTS = sorted(R)

print("=" * 78)
print("CONTROLS")
print("=" * 78)
gate("E6 rebuilt by reflection closure: 72 roots", len(ROOTS) == 72, str(len(ROOTS)))

# ---------------------------------------------------------------- the actions
# B8086's convention: v in (Z/5)^6 pairs with a root by sum(r_i v_i) mod 5.  W therefore acts on
# v CONTRAGREDIENTLY.  From s_j(r)_i = r_i - delta_ij * sum_k r_k A_kj, transposing gives:
def refl(v, j):
    return tuple((v[k] - A[k][j] * v[j]) % P for k in range(N))

def vanish(v):
    return frozenset(r for r in ROOTS if sum(r[i] * v[i] for i in range(N)) % P == 0)

ALL = [v for v in itertools.product(range(P), repeat=N) if any(v)]
gate("sweep is exhaustive: 5^6 - 1", len(ALL) == P**N - 1, str(len(ALL)))
gate("each dual reflection is an involution",
     all(refl(refl(v, j), j) == v for v in ALL[::37] for j in range(N)))

# THE STRUCTURAL CONTROL, and it is what makes the bijection argument valid rather than numeric:
# the reflection carries the vanishing set to the reflected vanishing set, so the ISOMORPHISM TYPE
# of the centraliser is constant along a W-orbit -- no classifier needed to know that.
def refl_root(r, j):
    pr = sum(r[i] * A[i][j] for i in range(N))
    return tuple(r[i] - pr * (1 if i == j else 0) for i in range(N))

ok = True
for v in ALL[::53]:
    for j in range(N):
        if {refl_root(r, j) for r in vanish(v)} != set(vanish(refl(v, j))):
            ok = False; break
gate("W carries vanishing set to vanishing set -> type constant on W-orbits", ok)

# Galois v -> c*v scales every pairing by c, a unit, so it fixes each vanishing set POINTWISE.
# Hence Galois can only ever fuse orbits WITHIN a row -- it can never merge two rows.
gate("Galois fixes each vanishing set exactly -> it can only fuse within a row",
     all(vanish(tuple((c * x) % P for x in v)) == vanish(v) for v in ALL[::29] for c in (2, 3, 4)))

# ----------------------------------------------------------------- the orbits
seen, worbits = set(), []
for v0 in ALL:
    if v0 in seen:
        continue
    comp, st = {v0}, [v0]
    while st:
        u = st.pop()
        for j in range(N):
            w = refl(u, j)
            if w not in comp:
                comp.add(w); st.append(w)
    seen |= comp
    worbits.append(comp)

idx = {v: i for i, o in enumerate(worbits) for v in o}
parent = list(range(len(worbits)))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]; a = parent[a]
    return a
for oi, o in enumerate(worbits):
    v = next(iter(o))
    for c in range(2, P):
        ra, rb = find(oi), find(idx[tuple((c * x) % P for x in v)])
        if ra != rb:
            parent[ra] = rb
grp = collections.defaultdict(set)
for oi in range(len(worbits)):
    grp[find(oi)] |= worbits[oi]
GAL = sorted((len(g) for g in grp.values()), reverse=True)
WSZ = sorted((len(o) for o in worbits), reverse=True)

print()
print("=" * 78)
print("THE ORBITS")
print("=" * 78)
print(f"\n  W-orbits ...........: {len(worbits)}")
print(f"  W x Galois orbits ..: {len(grp)}")
print(f"  W x Galois sizes ...: {GAL}")

# ------------------------------------------- compare against B8086's banked rows
B8086 = os.path.join(HERE, "..", "B8086_wilson_menu", "results.json")
rows = sorted((r["count"] for r in json.load(open(B8086))["rows"]), reverse=True)
print(f"  B8086 row counts ...: {rows}")

gate("B8086 banked exactly 9 rows", len(rows) == 9, str(len(rows)))
gate("there are exactly 9 W x Galois orbits", len(grp) == 9, str(len(grp)))
gate("THE OWNER'S CLAIM: orbit sizes match the row counts exactly", GAL == rows)

# The bijection, argued rather than eyeballed: each row is a UNION of W x Galois orbits (type is
# constant on orbits, controlled above).  A partition into 9 parts refined by a partition into 9
# parts is the SAME partition.  Hence every row is exactly one orbit.
gate("=> every row is a SINGLE W x Galois orbit", len(rows) == len(grp) == 9 and GAL == rows)

# ---------------------------------------------- and the sharpening: W alone fails
per = collections.Counter()
for g in grp.values():
    per[len([1 for o in worbits if next(iter(o)) in g])] += 1
splits = sorted(((len(g), [len(o) for o in worbits if next(iter(o)) in g]) for g in grp.values()),
                key=lambda t: -t[0])
print("\n  W ALONE, per row:")
for tot, parts in splits:
    print(f"    row {tot:>5}  ->  {len(parts)} W-orbit(s) of {sorted(set(parts))}")
w_single = sum(1 for _, parts in splits if len(parts) == 1)
gate("W ALONE does NOT already give one orbit per row (the sharpening)",
     len(worbits) == 25 and w_single == 1, f"{len(worbits)} W-orbits; {w_single} of 9 rows single")

RES = {"n_elements": len(ALL), "n_W_orbits": len(worbits), "n_W_galois_orbits": len(grp),
       "W_galois_orbit_sizes": GAL, "b8086_row_counts": rows,
       "every_row_is_one_W_galois_orbit": GAL == rows and len(grp) == len(rows) == 9,
       "W_alone_rows_that_are_single_orbits": w_single,
       "W_orbit_sizes": WSZ,
       "splits": [{"row": t, "n_W_orbits": len(p), "W_orbit_size": sorted(set(p))}
                  for t, p in splits],
       "verdict": ("homogeneous, but ARITHMETICALLY: one W x Galois orbit per row, while W alone "
                   "gives 25 orbits and splits 8 of the 9 rows"),
       "scope": ("The W-action on the 5-torsion of the E6 torus. Establishes homogeneity of the "
                 "rows and therefore UNIQUENESS of the invariant measure ON EACH ROW -- but only "
                 "for the group W x Galois. Under W alone the invariant measures on a split row "
                 "form a multi-parameter family. Says NOTHING about the manifold, and nothing "
                 "about whether the Z/5 menu is this object's -- B8086 showed it is NOT "
                 "(H_1 = Z, torsion-free). Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")

if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
