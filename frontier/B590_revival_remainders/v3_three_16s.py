"""B590-R2 — B572-V3: B299's triality orbits vs the three 16s (weight level, exact).

The three D5 (Spin(10)) decompositions of the 27 in the three triality frames
(charge = the coefficient of the deleted node's coweight; frames related by
B299's PHI), intersected with each other and with the PHI-orbit structure.
BLIND: the intersection pattern is the deliverable, whatever it is.

Run: python3 v3_three_16s.py (pyenv + sympy, ~10 s). Nothing to CLAIMS.md.
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B299_trinification_triality"))
import sympy as sp
from trinification_triality import PHI, THETA, _weights_27, _action_on_dynkin, E6_CARTAN

W27 = [tuple(int(x) for x in w) for w in _weights_27()]
assert len(W27) == 27
CINV = E6_CARTAN.inv()

# gates: PHI has order 3, preserves the weight set (Dynkin-label action)
assert PHI ** 3 == sp.eye(6)
PHI_D = _action_on_dynkin(PHI)
def act(M, w):
    v = M * sp.Matrix(w)
    return tuple(int(x) for x in v)
assert all(act(PHI_D, w) in set(W27) for w in W27), "PHI does not preserve the 27"

# PHI-orbit structure
orbits = []
seen = set()
for w in W27:
    if w in seen:
        continue
    orb = [w]
    x = act(PHI_D, w)
    while x != w:
        orb.append(x)
        x = act(PHI_D, x)
    seen.update(orb)
    orbits.append(orb)
print(f"PHI-orbit structure on the 27 weights: "
      f"{sorted((len(o) for o in orbits), reverse=True)}")

# the D5 charge in frame j: q_j(w) = coefficient of the node-1 coweight of PHI^{-j} w
# (node 1 in this Cartan-matrix ordering: removing it leaves D5)
def charge(w, node=0):
    lam = CINV * sp.Matrix(w)
    return lam[node]

# find which node gives the 1/10/16 split (gate)
def split_by_charge(frame_pow, node):
    vals = {}
    Pinv = PHI_D ** ((3 - frame_pow) % 3)
    for w in W27:
        q = charge(act(Pinv, w), node)
        vals.setdefault(q, []).append(w)
    return vals

NODE = None
for node in range(6):
    sizes = sorted(len(v) for v in split_by_charge(0, node).values())
    if sizes == [1, 10, 16]:
        NODE = node
        break
assert NODE is not None, "no node gives the 1/10/16 split"
print(f"charge node (removing it leaves D5): index {NODE}; split sizes 1/10/16  GATE PASS")

frames = []
for j in range(3):
    v = split_by_charge(j, NODE)
    by_size = {len(x): set(x) for x in v.values()}
    assert sorted(by_size) == [1, 10, 16]
    frames.append(by_size)

print("\nthe intersection tables (BLIND):")
print("  |16_i ∩ 16_j|:")
for i in range(3):
    print("   ", [len(frames[i][16] & frames[j][16]) for j in range(3)])
print("  |16_i ∩ 10_j|:")
for i in range(3):
    print("   ", [len(frames[i][16] & frames[j][10]) for j in range(3)])
print("  |10_i ∩ 10_j|:")
for i in range(3):
    print("   ", [len(frames[i][10] & frames[j][10]) for j in range(3)])
print("  the three singlets:", [sorted(frames[j][1]) for j in range(3)])
trip16 = frames[0][16] & frames[1][16] & frames[2][16]
print(f"  triple intersection 16∩16∩16: {len(trip16)}")

print("\nhow PHI-orbits distribute across frame-0's (16, 10, 1):")
from collections import Counter
profile = Counter()
for orb in orbits:
    key = tuple(sorted("16" if w in frames[0][16] else ("10" if w in frames[0][10] else "1")
                       for w in orb))
    profile[key] += 1
for k, v in sorted(profile.items()):
    print(f"  orbit profile {k}: x{v}")

print("\nDONE (the pattern above is the V3 deliverable, read blind)")
