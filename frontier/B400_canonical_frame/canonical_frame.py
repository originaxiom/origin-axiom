"""B400 -- F1-F4: exact frame geometry in the shared W2-label space (Z12)."""
import json, os
from fractions import Fraction as Fr
import math
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))

def vec12_from_23_col(b):
    """(2,3): a = W2-exp mod 12 -> the column at W3-exp b, as a Z12 vector."""
    v = [Fr(0)]*12
    for k, val in T["2,3"].items():
        a, bb = map(int, k.split(","))
        if bb == b: v[a] = Fr(val[3])
    return v

def vec12_from_12_row(a):
    """(1,2): b = W2-exp mod 12 -> the row at W1-exp a, as a Z12 vector."""
    v = [Fr(0)]*12
    for k, val in T["1,2"].items():
        aa, b = map(int, k.split(","))
        if aa == a: v[b] = Fr(val[3])
    return v

def dot(u, v): return sum(x*y for x, y in zip(u, v))

# F1: the Mercedes triple
M = [vec12_from_23_col(b) for b in (0, 2, 4)]
G = [[dot(M[i], M[j]) for j in range(3)] for i in range(3)]
n = G[0][0]
mercedes_ok = all(G[i][i] == n for i in range(3)) and all(G[i][j] == -n/2 for i in range(3) for j in range(3) if i != j)
ksum = [sum(M[i][k] for i in range(3)) for k in range(12)]
kernel_zero = all(x == 0 for x in ksum)
print("F1 Mercedes: Gram prop to [[1,-1/2,-1/2],...]:", mercedes_ok, " columns sum to zero:", kernel_zero, " n =", n)

# F2: the golden slot rows
g6, g14 = vec12_from_12_row(6), vec12_from_12_row(14)
n6, n14, i614 = dot(g6, g6), dot(g14, g14), dot(g6, g14)
print("F2 golden rows: |g6|^2 =", n6, " |g14|^2 =", n14, " <g6,g14> =", i614)

# F3: relative geometry -- project golden vectors onto the Mercedes plane
# plane basis: e1 = M0 - M1, e2 = M0 + M1 - 2*M2 (orthogonal in the triple geometry)
e1 = [M[0][k]-M[1][k] for k in range(12)]
e2 = [M[0][k]+M[1][k]-2*M[2][k] for k in range(12)]
print("F3 plane-basis norms:", dot(e1,e1), dot(e2,e2), " cross:", dot(e1,e2))
rel = {}
for name, g in (("g6", g6), ("g14", g14)):
    c1, c2 = dot(g, e1), dot(g, e2)
    rel[name] = dict(onto_e1=str(c1), onto_e2=str(c2),
                     norm2=str(dot(g, g)))
    # squared cosine of the angle to the plane:
    if dot(g,g) != 0:
        proj2 = (c1*c1/dot(e1,e1) if dot(e1,e1) else 0) + (c2*c2/dot(e2,e2) if dot(e2,e2) else 0)
        rel[name]["cos2_to_plane"] = str(proj2 / dot(g, g))
    print(f"   {name}: <g,e1> = {c1}, <g,e2> = {c2}, cos^2(angle to plane) = {rel[name].get('cos2_to_plane')}")
json.dump(dict(mercedes=bool(mercedes_ok), kernel_zero=bool(kernel_zero), n=str(n),
               g6=dict(norm2=str(n6)), g14=dict(norm2=str(n14)), inner=str(i614),
               rel=rel), open(os.path.join(HERE, "canonical_frame.json"), "w"), indent=1)
print("DONE")
