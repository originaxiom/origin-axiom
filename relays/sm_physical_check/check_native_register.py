#!/usr/bin/env python3
"""The SM seat's check of the physical lane's NATIVE_SIGNED_ACTION_AND_INVARIANT_METRIC.md (audit/physical-bridge-2026-09-05
at 798281903): every review duty in its section 5, on this seat's own symbolic code.
    python3 check_native_register.py"""
import itertools
import json
import pathlib

import sympy as sp

out = {}
x, y, z = sp.symbols("x y z")
Lmap = sp.Matrix([x, z, x * z - y]); Rmap = sp.Matrix([z, y, y * z - x])
ell = Lmap.jacobian([x, y, z]).subs({x: 0, y: 0, z: 0}); r = Rmap.jacobian([x, y, z]).subs({x: 0, y: 0, z: 0})
out["(1) ell"] = str(ell.tolist()); out["(1) r"] = str(r.tolist())
out["(1) as displayed"] = ell == sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]) and r == sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
# (3): quaternion automorphisms from the forward substitutions, with a -> i, b -> j
Q = sp.Quaternion
qi, qj, qk = Q(0, 1, 0, 0), Q(0, 0, 1, 0), Q(0, 0, 0, 1)
def vec(q): return [q.b, q.c, q.d]
# alpha_L: a -> a, b -> ab  so  i -> i, j -> i j, and k = i j -> i (i j)
aL = {"i": qi, "j": qi * qj}; aL["k"] = aL["i"] * aL["j"]
aR = {"i": qi * qj, "j": qj}; aR["k"] = aR["i"] * aR["j"]
ML = sp.Matrix([vec(aL[c]) for c in "ijk"]).T; MR = sp.Matrix([vec(aR[c]) for c in "ijk"]).T
out["(3) alpha_L: i->i, j->k, k->-j"] = [vec(aL[c]) for c in "ijk"] == [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
out["(3) alpha_R: i->k, j->j, k->-i"] = [vec(aR[c]) for c in "ijk"] == [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
out["(3) ell = alpha_L^-1 and r = alpha_R^-1"] = (ell == ML.inv()) and (r == MR.inv())
# section 2: the group
def key(M): return tuple(M)
G = {key(sp.eye(3)): sp.eye(3)}; frontier = [sp.eye(3)]
while frontier:
    nxt = []
    for A in frontier:
        for g in (ell, r):
            B = A * g
            if key(B) not in G:
                G[key(B)] = B; nxt.append(B)
    frontier = nxt
allsp = [sp.Matrix(3, 3, lambda i, j: s[i] if p[i] == j else 0) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
proper = {key(M) for M in allsp if M.det() == 1}
out["(4) |G| = 24 and G = all det-1 signed permutations"] = len(G) == 24 and set(G) == proper
kernel = [M for M in G.values() if all(abs(M[i, j]) == (1 if i == j else 0) for i in range(3) for j in range(3))]
out["(5) kernel of the sign-forgetting map has 4 elements"] = len(kernel) == 4
X6 = [s * sp.eye(3)[:, i] for i in range(3) for s in (1, -1)]
orbit = {tuple(M * X6[0]) for M in G.values()}
out["G transitive on X6"] = len(orbit) == 6
stab = [M for M in G.values() if M * X6[0] == X6[0]]
powers = [ell ** n for n in range(4)]
out["the stabiliser of e1 is the powers of ell (size 4)"] = len(stab) == 4 and all(any(S == Pw for Pw in powers) for S in stab)
orbs = []
seen = set()
for v in X6:
    if tuple(v) in seen: continue
    o = {tuple(S * v) for S in stab}; seen |= o; orbs.append(sorted(o))
out["(6) stabiliser orbits on X6 (sizes)"] = sorted(len(o) for o in orbs)
# section 3: invariant symmetric forms
b = sp.symbols("b0:6"); B = sp.Matrix([[b[0], b[1], b[2]], [b[1], b[3], b[4]], [b[2], b[4], b[5]]])
sol = sp.solve(list(ell.T * B * ell - B) + list(r.T * B * r - B), b, dict=True)
out["(7) invariant symmetric B"] = str(B.subs(sol[0]))
c = sp.symbols("c0:9"); C = sp.Matrix(3, 3, c)
solc = sp.solve(list(ell * C - C * ell) + list(r * C - C * r), c, dict=True)
out["the commutant of G"] = str(C.subs(solc[0]))
# section 1 carrier warnings: axis vectors are not on the Markov surface nor its tangent cone
out["axis vectors on x^2+y^2+z^2 = xyz"] = any(sp.simplify(v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) == 0 for v in X6)
# section 4: the unsigned quotient's permutation module = constant line + sum-zero plane
perm = [sp.Matrix(3, 3, lambda i, j: abs(M[i, j])) for M in G.values()]
avg = sum(perm, sp.zeros(3, 3)) / len(perm)
out["(section 4) the invariant vectors of the permutation module (rank of the average)"] = avg.rank()
out["(section 4) the signed module has invariant vectors"] = (sum(G.values(), sp.zeros(3, 3)) / 24).rank()
print(json.dumps(out, indent=1, default=str))
pathlib.Path(__file__).with_name("check_native_register.json").write_text(json.dumps(out, indent=1, default=str))
