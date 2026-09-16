#!/usr/bin/env python3
"""B1369's instrument on cases it was not built on: manifolds whose peripheral ranks are predicted by theory.
  * m004, m003 (one cusp, b_1 = 1): the peripheral image has rank 1 (half of H_1 of the torus dies).
  * m129, the Whitehead link complement: linking number 0, so each longitude is null-homologous and each cusp's peripheral image has
    rank 1 while b_1 = 2 -- both cusps free.
  * L6a4, the Borromean rings complement: pairwise linking numbers 0, so all three longitudes are null-homologous: ranks [1, 1, 1],
    b_1 = 3.
The instrument's b_1 and ranks must equal these predictions and SnapPy's fundamental-group computation, and its automorphism count
must equal SnapPy's isometry count.  With --all, the same agreement is checked on every member of B1186's family (about four minutes).
Usage: python3 controls.py [--all]"""
import sys, os, json, warnings, time
warnings.filterwarnings("ignore")
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family_isometries import FamilyMember


def abelianise(word, gens):
    v = [0] * len(gens)
    for ch in word:
        i = gens.index(ch.lower()); v[i] += 1 if ch.islower() else -1
    return v


def snappy_ranks(M):
    G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    rR = R.rank() if rels else 0
    out = []
    for (mu, lam) in G.peripheral_curves():
        P = sp.Matrix([abelianise(mu, gens), abelianise(lam, gens)])
        out.append((sp.Matrix.vstack(R, P) if rels else P).rank() - rR)
    return len(gens) - rR, out


CONTROLS = [("m004", (1, [1])), ("m003", (1, [1])), ("m129", (2, [1, 1])), ("L6a4", (3, [1, 1, 1]))]
print("=== controls: theory-predicted peripheral ranks ===")
for name, expect in CONTROLS:
    FM = FamilyMember(name)
    mine = (FM.b1, [FM.cusp[c]['rankP'] for c in range(FM.num_cusps)])
    sn = snappy_ranks(FM.M); iso = FM.M.symmetry_group().order()
    ok = mine == expect == sn and len(FM.auts) == iso
    print(f"  {name:5s} H_1 = {FM.M.homology()!s:>12s}: instrument (b_1, ranks) {mine}, SnapPy {sn}, predicted {expect}; |Aut| {len(FM.auts)} = |Isom| {iso}: {'OK' if ok else 'MISMATCH'}")
    assert ok, name
if "--all" in sys.argv:
    fam = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1186_family_is_112", "verification", "family_census.json")))
    t0 = time.time(); bad = []
    for name in fam['members_B']:
        FM = FamilyMember(name); sn = snappy_ranks(FM.M)
        mine = (FM.b1, [FM.cusp[c]['rankP'] for c in range(FM.num_cusps)])
        if mine != sn or len(FM.auts) != FM.M.symmetry_group().order(): bad.append(name)
    print(f"=== all {len(fam['members_B'])} members: b_1, peripheral ranks and |Aut| = |Isom| against SnapPy ({time.time() - t0:.0f} s): disagreements {bad if bad else 'none'} ===")
    assert not bad
print("CONTROLS PASS")
