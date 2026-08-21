"""F4b + F5 of the finalization wave.

F4b — what separates the 18's two orbits: test the ideal-swap explicitly
  (swap(t) in S?), find which composed moves preserve S, and if the swap
  exchanges the orbits the residual price is ZERO new bits (the bit is
  'which ideal is color', already a named physical assignment).

F5 — L175, the h = 0 locus: compute the vanishing word-sets of the B593
  coupling in SIX channels (odd u3, odd u6, even-sym 10+01, even-sym 20+02,
  fixed 00, fixed 11) over all 1364 free-group words to length 5, float
  census at 1e-10 with the odd-u3 set cross-checked against B1103's exact
  count (28). Outcome: WORD-PROPERTY (identical sets) / CHANNEL-DEPENDENT.
"""
import itertools
import json
from fractions import Fraction as F

import numpy as np

ST = "."
REPO = "."

# ---------------- F4b ----------------
res = json.load(open(f"{REPO}/frontier/B1102_exact_hypercharge_solve/"
                     "b1102_results.json"))
sols = [tuple(F(x) for x in t) for t in res["all_solving_directions"]]
S = set(sols)
swap = lambda t: (t[2], t[3], t[0], t[1])
swap_in = [swap(t) in S for t in sols]
print(f"F4b: swap(t) in S for {sum(swap_in)}/18")

# rebuild the two orbits under the set-preserving group from f1_f4 run:
prev = json.load(open(f"{ST}/b1109_results.json"))
# recompute orbits quickly (same construction) to get orbit membership:
W3 = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]
def mat_from_perm(p):
    a, b = W3[p[0]], W3[p[1]]
    return ((a[0], b[0]), (a[1], b[1]))
MATS = [mat_from_perm(p) for p in itertools.permutations(range(3))]
def contr(M, v):
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    inv = ((M[1][1]/det, -M[0][1]/det), (-M[1][0]/det, M[0][0]/det))
    return (inv[0][0]*v[0] + inv[1][0]*v[1], inv[0][1]*v[0] + inv[1][1]*v[1])
def act(t, gA, gB, sw):
    tA, tB = contr(gA, (t[0], t[1])), contr(gB, (t[2], t[3]))
    out = (tA[0], tA[1], tB[0], tB[1])
    return (out[2], out[3], out[0], out[1]) if sw else out
group = [(gA, gB, sw) for gA in MATS for gB in MATS for sw in (False, True)]
pres = [g for g in group if all(act(t, *g) in S for t in sols)]
pres_swap = [g for g in pres if g[2]]
print(f"F4b: preserving moves {len(pres)} (with swap: {len(pres_swap)})")
seen, orbits = set(), []
for t in sols:
    if t in seen: continue
    orb, fr = {t}, [t]
    while fr:
        x = fr.pop()
        for g in pres:
            y = act(x, *g)
            if y in S and y not in orb:
                orb.add(y); fr.append(y)
    seen |= orb; orbits.append(orb)
print(f"F4b: orbits {[len(o) for o in orbits]}")
if len(orbits) == 2:
    o1, o2 = orbits
    cross = any(swap(t) in o2 for t in o1)
    print(f"F4b: swap maps orbit1 -> orbit2: {cross}")
    # a separating invariant candidate: the value assigned to the pure
    # +e_i basis classes is not invariant; instead report canonical reps:
    r1 = sorted(o1)[0]; r2 = sorted(o2)[0]
    print("F4b: orbit reps:", [str(x) for x in r1], "|", [str(x) for x in r2])

# ---------------- F5 ----------------
import importlib.util, os, math, cmath
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(REPO, "frontier/B238_su32_levelrank/su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b238)
w, Smat, Tmat, cc = b238.su3_data(2)
n = len(w)
Si, Ti = np.linalg.inv(Smat), np.linalg.inv(Tmat)
R, L = Tmat, Si @ Ti @ Smat
MAT = {"a": R, "A": np.linalg.inv(R), "b": L, "B": np.linalg.inv(L)}
idx = {wt: w.index(wt) for wt in w}
def vec(pairs):
    v = np.zeros(n, dtype=complex)
    for wt, c in pairs: v[idx[wt]] = c
    return v
s2 = 1/math.sqrt(2)
CH = {
  "odd_u3":   vec([((1,0),  s2), ((0,1), -s2)]),
  "odd_u6":   vec([((2,0),  s2), ((0,2), -s2)]),
  "even_s3":  vec([((1,0),  s2), ((0,1),  s2)]),
  "even_s6":  vec([((2,0),  s2), ((0,2),  s2)]),
  "fixed_00": vec([((0,0), 1.0)]),
  "fixed_11": vec([((1,1), 1.0)]),
}
letters = "aAbB"
CACHE = {"": np.eye(n, dtype=complex)}
words = []
for ln in range(1, 6):
    for tup in itertools.product(letters, repeat=ln):
        s = "".join(tup)
        CACHE[s] = CACHE[s[:-1]] @ MAT[s[-1]]
        words.append(s)
zero_sets = {}
for name, u in CH.items():
    zs = frozenset(s for s in words
                   if abs(np.conj(u) @ CACHE[s] @ u) < 1e-10)
    zero_sets[name] = zs
    print(f"F5: channel {name}: {len(zs)} vanishing words")
ref = zero_sets["odd_u3"]
same = {name: zs == ref for name, zs in zero_sets.items()}
print(f"F5: odd_u3 count vs B1103's exact 28: {len(ref)} "
      f"{'OK' if len(ref) == 28 else 'MISMATCH'}")
print("F5: identical to odd_u3 zero-set:", same)
verdict = ("WORD-PROPERTY" if all(same.values()) else
           "CHANNEL-DEPENDENT: " + ",".join(k for k, v in same.items() if not v))
print("F5 VERDICT:", verdict)
json.dump({"F4b_swap_in_S": sum(swap_in), "F4b_preserving": len(pres),
           "F4b_preserving_with_swap": len(pres_swap),
           "F4b_orbits": [len(o) for o in orbits],
           "F5_counts": {k: len(v) for k, v in zero_sets.items()},
           "F5_same_as_odd_u3": same, "F5_verdict": verdict},
          open(f"{ST}/b1110_results.json", "w"), indent=1)
