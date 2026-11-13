"""Decision 1 of the input budget: are positivity's side (GM5d as re-read in v1.48), the hand (the bundle's orientation)
and the line's twin one bit?

Main's reading, written before the run. GM5d (v1.48, B1662): step and pull-back are mirror images under D = diag(1, -1)
(D L D = L^-1, D R D = R^-1), and positivity is the choice of side: the forward word A = LR or the backward word
A' = L^-1 R^-1 = D A D. A placement is (side s, orientation o of the side's bundle, twin t of the line on the side's
eigenline mod 5). A map between bundles is an integer X, det +-1, with X A_s X^-1 = A_s'^e (e = +-1); it sends
(s, o, v) to (s', o * det X * e, X v). Expected: the eight placements fall into two orbits under every such X (one bit),
and into four under the maps that keep the orientation (o * det X * e = o), so the side, the hand and the twin are one
bit up to every identification, and the twin is a bit beyond the hand when only orientation-keeping maps identify.
PLANT: the orientation read from det X alone (forgetting e) must change the counts.
Not in this count: SE2 (orientable m004 over the non-orientable m000: a choice of manifold, not of a placement) and the
chiral premise (one block or both: a choice of kind, B1851, the scale card's design note). No data."""
import itertools, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent

def mul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def det(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]
def inv(X):
    d = det(X); return ((X[1][1] * d, -X[0][1] * d), (-X[1][0] * d, X[0][0] * d))
def act(X, v):
    return ((X[0][0] * v[0] + X[0][1] * v[1]) % 5, (X[1][0] * v[0] + X[1][1] * v[1]) % 5)

L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); D = ((1, 0), (0, -1))
A = {"+": mul(L, R), "-": mul(inv(L), inv(R))}
assert A["-"] == mul(mul(D, A["+"]), D)
BASE = {"+": (1, 2), "-": act(D, (1, 2))}                    # the forward line and its image under the side's mirror

def eigen_ok(s, v):
    Av = act(A[s], v); return Av == ((-v[0]) % 5, (-v[1]) % 5)
assert all(eigen_ok(s, BASE[s]) for s in "+-")

def twin(s, v):
    b = BASE[s]
    for lab, m in (("v", 1), ("2v", 2)):
        for sg in (1, -1):
            if v == ((sg * m * b[0]) % 5, (sg * m * b[1]) % 5):
                return lab
    return None

PLACES = [(s, o, t) for s in "+-" for o in (1, -1) for t in ("v", "2v")]
VEC = {(s, t): (BASE[s] if t == "v" else ((2 * BASE[s][0]) % 5, (2 * BASE[s][1]) % 5)) for s in "+-" for t in ("v", "2v")}

maps = []
B = 9
for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
    X = ((a, b), (c, d))
    if det(X) not in (1, -1):
        continue
    for s in "+-":
        XAXi = mul(mul(X, A[s]), inv(X))
        for s2 in "+-":
            for e in (1, -1):
                if XAXi == (A[s2] if e == 1 else inv(A[s2])):
                    maps.append((X, s, s2, e))

def orbits(rule):
    adj = {p: {p} for p in PLACES}
    for X, s, s2, e in maps:
        for (ss, o, t) in PLACES:
            if ss != s:
                continue
            w = act(X, VEC[(s, t)])
            t2 = twin(s2, w)
            assert t2 is not None, "a map left the eigenline"
            o2 = rule(o, X, e)
            if o2 is None:
                continue
            adj[(s, o, t)].add((s2, o2, t2)); adj[(s2, o2, t2)].add((s, o, t))
    seen, out = set(), []
    for p in PLACES:
        if p in seen:
            continue
        comp, st = set(), [p]
        while st:
            q = st.pop()
            if q in comp:
                continue
            comp.add(q); st.extend(adj[q])
        seen |= comp; out.append(sorted(comp))
    return out

every = orbits(lambda o, X, e: o * det(X) * e)
keeping = orbits(lambda o, X, e: o if det(X) * e == 1 else None)
planted = orbits(lambda o, X, e: o * det(X))
fmt = lambda orbs: [[f"{s} side, {'+' if o == 1 else '-'} hand, {t}" for s, o, t in orb] for orb in orbs]
cross = [m for m in maps if m[1] != m[2]]
res = {
    "maps_found": len(maps), "maps_between_the_sides": len(cross),
    "D_is_a_map_between_the_sides": any(m[0] == D and m[1] == "+" and m[2] == "-" and m[3] == 1 for m in maps),
    "orbits_under_every_map": fmt(every),
    "orbits_under_orientation_keeping_maps": fmt(keeping),
    "plant_orientation_from_det_alone": fmt(planted),
}
if __name__ == "__main__":
    print("maps found (entries <= %d): %d, of them between the two sides: %d; D among them: %s"
          % (B, res["maps_found"], res["maps_between_the_sides"], res["D_is_a_map_between_the_sides"]))
    for k in ("orbits_under_every_map", "orbits_under_orientation_keeping_maps", "plant_orientation_from_det_alone"):
        print(k, len(res[k]), res[k])
    (HERE / "the_hand_rows.json").write_text(json.dumps(res, indent=1))
