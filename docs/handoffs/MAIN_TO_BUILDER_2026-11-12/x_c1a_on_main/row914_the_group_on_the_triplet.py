#!/usr/bin/env python3
"""Harvest row 914, its computed part only: the group that the weave's moves generate on the triplet.

Main's own code, exact integer matrices.  The linear parts at the origin of the Fricke maps
    L: (x, y, z) -> (x, z, xz - y)        R: (x, y, z) -> (z, y, yz - x)
are dL: (x, y, z) -> (x, z, -y) and dR: (x, y, z) -> (z, y, -x) (main's B1601, section 2).  The group they generate, and
the group with the sign -1 added, are enumerated; orders of elements and determinants are counted.

NOT COMPUTED, and not read: anything of the seat's file after its first block.  The rest of that file is a reading about
mixing, which is behind the firewall."""
import itertools, json, pathlib, subprocess, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
def mul(a, b): return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
dL = ((1, 0, 0), (0, 0, 1), (0, -1, 0))        # (x, y, z) -> (x, z, -y)
dR = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))        # (x, y, z) -> (z, y, -x)
NEG = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))
def det(m): return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
def order(m):
    p, n = m, 1
    while p != I3: p = mul(p, m); n += 1
    return n
def generate(gens):
    seen, frontier = {I3}, [I3]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h)
                if x not in seen: seen.add(x); nxt.append(x)
        frontier = nxt
    return seen
def facts(G):
    return {"order": len(G), "determinants": dict(sorted(collections.Counter(det(m) for m in G).items())),
            "element orders": dict(sorted(collections.Counter(order(m) for m in G).items())),
            "rotations (determinant 1)": sum(1 for m in G if det(m) == 1), "-1 in the group": NEG in G}
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % detail) if detail else ""))
# the linear parts, from the maps themselves: the Jacobian at the origin by exact differences of the polynomial maps
Lmap = lambda x, y, z: (x, z, x * z - y); Rmap = lambda x, y, z: (z, y, y * z - x)
def jac(f):
    cols = [f(*e) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]            # the maps have no constant term and their quadratic terms vanish on the axes
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
check("the linear part of L at the origin is (x, y, z) -> (x, z, -y)", jac(Lmap) == dL)
check("the linear part of R at the origin is (x, y, z) -> (z, y, -x)", jac(Rmap) == dR)
fixes = lambda m, k: all(m[i][k] == (1 if i == k else 0) for i in range(3)) and all(m[k][j] == (1 if j == k else 0) for j in range(3))
check("each is a quarter turn: of order 4 and determinant 1, dL fixing the first axis and dR the second", order(dL) == 4 == order(dR) and det(dL) == 1 == det(dR) and fixes(dL, 0) and fixes(dR, 1) and not fixes(dL, 1))
rot = generate([dL, dR]); full = generate([dL, dR, NEG])
fr, ff = facts(rot), facts(full)
check("the two quarter turns generate a group of order 24, all of determinant 1", fr["order"] == 24 and fr["determinants"] == {1: 24}, fr)
check("its elements have the orders of the rotations of a cube: 1, 9, 8, 6 of orders 1, 2, 3, 4", fr["element orders"] == {1: 1, 2: 9, 3: 8, 4: 6}, fr["element orders"])
check("it is the group of signed permutation matrices of determinant 1", rot == {m for m in (tuple(tuple(s[i] if p[i] == j else 0 for j in range(3)) for i in range(3)) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)) if det(m) == 1})
check("with the sign it has order 48, half of each determinant, and -1 is in it", ff["order"] == 48 and ff["determinants"] == {-1: 24, 1: 24} and ff["-1 in the group"], ff)
check("-1 is not in the group of the two moves alone", NEG not in rot)
# the seat's first block, read as data at its commit
raw = subprocess.run(["git", "show", "c0ff37644:docs/dossiers/the_weave_2026-10-07/the_mixing.json"], capture_output=True, text=True, cwd=str(HERE.parents[1])).stdout
seat = json.loads(raw)["(1) the weave's group on the triplet"]
norm = lambda d: {str(k): v for k, v in d.items()}
same = {k: (norm(seat[k]) == norm(ff[k]) if isinstance(seat[k], dict) else seat[k] == ff[k]) for k in ("order", "determinants", "element orders", "rotations (determinant 1)", "-1 in the group")}
check("the seat's first block gives the same five facts for the group with the sign", all(same.values()), same)
# planted: a wrong generator must change the count
bad = generate([dL, ((1, 0, 0), (0, 1, 0), (0, 0, 1))])
check("planted: with the second move replaced by the identity the group has order 4", len(bad) == 4)
res = {"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]], "the rotations": fr, "with the sign": ff}
(HERE / "row914_the_group_on_the_triplet.json").write_text(json.dumps(res, indent=1, default=str) + "\n", encoding="utf-8")
print("\n%d checks, %d failing" % (len(CHECKS), len(res["failing"])))
