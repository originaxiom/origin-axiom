"""F3 — the swap-twisted triality (prereg addendum 9320e6f9). Gate: straight solves
load-bearing steps; the commutant diagnostic is float-labeled.
reproduce D5 dim-0; then the twisted system X A = A X, X B = C X, X C = B X.
"""
import os, pickle, sys, time
import numpy as np

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
B575 = "<seat-workdir>/origin-axiom/frontier/B575_bridge_obstruction/l51_obstruction.py"
B299 = "<seat-workdir>/origin-axiom/frontier/B299_trinification_triality/trinification_triality.py"
PKL = "<seat-workdir>/seat-work/cell3_double/stage1_classes.pkl"
LAM = "abABaaBAbA"

src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
print("exec B575 stages 0-3...", flush=True)
t0 = time.time()
exec(compile(src[:cut], B575, "exec"), ns)
print(f"  done {time.time()-t0:.0f}s", flush=True)

K0, K1 = ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
mmul, meye, rref = ns["mmul"], ns["meye"], ns["rref"]
d = 27

def mt(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]

def is_eye(M):
    return all((M[i][j] - (K1 if i == j else K0)).is_zero() for i in range(d) for j in range(d))

def minv(M):
    aug = [list(M[i]) + [K1 if k == i else K0 for k in range(d)] for i in range(d)]
    Rr, piv = rref(aug)
    assert len(piv) == d
    return [[Rr[i][d + j] for j in range(d)] for i in range(d)]

def word_mat(word, acts):
    P = meye(d)
    for ch in word:
        P = mmul(P, acts[ch])
    return P

def inv_word(w):
    return ''.join(ch.swapcase() for ch in reversed(w))

pk = pickle.load(open(PKL, "rb"))
Kc = ns["K"]
J = [[Kc(*pk["J"][i][j]) for j in range(d)] for i in range(d)]
raw_classes = pk["classes"]
h1 = pk["h1"]
assert all(len(c) == 3 * d for c in raw_classes), \
    f"class layout: expected 81 = 3x27, got {[len(c) for c in raw_classes]}"
classes = [{g: [Kc(*c[gi * d + i]) for i in range(d)]
            for gi, g in enumerate(('a', 'b', 'c'))} for c in raw_classes]
print(f"pkl rehydrated: h1 = {h1}, classes = {len(classes)} (81-vectors -> a/b/c)",
      flush=True)
Jinv = minv(J)
C27 = mmul(mmul(J, mt(B27i)), Jinv)
C27i = mmul(mmul(J, mt(B27)), Jinv)
assert is_eye(mmul(C27, C27i))
acts = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i, 'c': C27, 'C': C27i}
REL = ns["REL"]
for name, w in (("R1", REL), ("R2", REL.replace('b', 'c').replace('B', 'C')),
                ("R3", LAM.replace('b', 'c').replace('B', 'C') + inv_word(LAM))):
    assert is_eye(word_mat(w, acts)), f"relator gate {name}"
print("relator gates pass (C27 rebuilt from banked J)", flush=True)

# ---- weight bridge ----
w575 = None
for k, v in ns.items():
    if isinstance(v, (list, tuple)) and len(v) == 27:
        try:
            if all(len(x) == 6 and all(isinstance(int(y), int) for y in x) for x in v):
                w575 = [tuple(int(y) for y in x) for x in v]
                print(f"  weight list found in ns['{k}']", flush=True)
                break
        except Exception:
            continue
if w575 is None:
    print("VERDICT: OBSTRUCTED-AT-BRIDGE — no 27 weight-label list in the B575 "
          "namespace; fix: rerun B575 with label capture.", flush=True)
    sys.exit(0)

nb = {"__name__": "b299"}
exec(compile(open(B299).read(), B299, "exec"), nb)
w299 = [tuple(int(y) for y in x) for x in nb["_weights_27"]()]
import sympy as sp
TH, PH = nb["THETA"], nb["PHI"]
I6 = sp.eye(6)
assert TH**3 == I6 and PH**3 == I6 and TH * PH == PH * TH, "B299 Z3xZ3 sanity"
tri6 = []
for i in range(3):
    for j in range(3):
        m = TH**i * PH**j
        if m != I6 and not any(m == x for x in tri6):
            tri6.append(m)
print(f"order-3 Dynkin actions found: {len(tri6)} (the 8 nontrivial Z3xZ3 elements)",
      flush=True)

from itertools import permutations
w575set = set(w575)
patterns = []
for perm in permutations(range(6)):
    relab = [tuple(x[perm[i]] for i in range(6)) for x in w299]
    if set(relab) != w575set:
        continue
    idx299_to_575 = {}
    for j, lw in enumerate(relab):
        idx299_to_575[j] = w575.index(lw)
    for m in tri6:
        A = nb["_action_on_dynkin"](m)
        pperm = [None] * 27
        ok = True
        for j, mu in enumerate(w299):
            img = tuple(int(sum(A[i, l] * mu[l] for l in range(6))) for i in range(6))
            if img not in set(w299):
                ok = False
                break
            pperm[idx299_to_575[j]] = idx299_to_575[w299.index(img)]
        if ok and all(p is not None for p in pperm):
            key = tuple(pperm)
            if key not in [p[0] for p in patterns]:
                patterns.append((key, perm))
print(f"candidate 27-permutation patterns: {len(patterns)}", flush=True)

# ---- pattern solves (exact; unknowns d_j; X[pperm[j]][j] = d_j) ----
def pattern_solve(pperm, pairs_lr):
    rows = []
    for Ml, Mr in pairs_lr:
        # X Ml - Mr X = 0: X Ml term: d_k Ml[k][j] at i = pperm[k];
        # Mr X term: Mr[i][pperm[j]] d_j
        for i in range(d):
            for j in range(d):
                coef = [K0] * d
                for k in range(d):
                    if pperm[k] == i:
                        coef[k] = coef[k] + Ml[k][j]
                coef[j] = coef[j] - Mr[i][pperm[j]]
                if not all(c.is_zero() for c in coef):
                    rows.append(coef)
    Rr, piv = rref([list(r) for r in rows])
    free = [j for j in range(d) if j not in piv]
    return len(free), Rr, piv

STRAIGHT = ((A27, A27), (B27, B27), (C27, C27))
TWISTED = ((A27, A27), (B27, C27), (C27, B27))

print("GATE: straight solves must reproduce D5's dim-0...", flush=True)
for pi, (pperm, perm) in enumerate(patterns):
    ker, _, _ = pattern_solve(pperm, STRAIGHT)
    assert ker == 0, f"gate: straight pattern {pi} changed (dim {ker})"
print("gate PASS: 8/8 straight dims = 0 (D5 reproduced)", flush=True)

results = []
for pi, (pperm, perm) in enumerate(patterns):
    ker, Rr, piv = pattern_solve(pperm, TWISTED)
    print(f"TWISTED pattern {pi} (relabel {perm}): solution dim = {ker}", flush=True)
    results.append((pi, pperm, ker, Rr, piv))

found = [r for r in results if r[2] > 0]
if not found:
    # float commutant diagnostic (labeled non-exact)
    import math
    def fl(M):
        return np.array([[complex(float(x.a), float(x.b) * math.sqrt(3)) for x in row]
                         for row in M])
    Af, Bf, Cf = fl(A27), fl(B27), fl(C27)
    I27 = np.eye(27)
    rowsf = []
    for Mf in (Af, Bf, Cf):
        rowsf.append(np.kron(I27, Mf.T) - np.kron(Mf, I27))
    sv = np.linalg.svd(np.vstack(rowsf), compute_uv=False)
    dimc = int((sv < 1e-8 * sv[0]).sum())
    print(f"VERDICT: NO-PATTERN-SOLUTION at all {len(patterns)} patterns. "
          f"Float commutant dim = {dimc} (SVD gap diagnostic, non-exact): "
          f"{'Schur-forced (irreducible)' if dimc == 1 else 'reducible — genuine pattern obstruction'}",
          flush=True)
    sys.exit(0)

# ---- ACTION-FOUND: grade H1 ----
pi, pperm, ker, Rr, piv = found[0]
free = [j for j in range(d) if j not in piv]
sol = [K0] * d
sol[free[0]] = K1
for r_i, p_j in enumerate(piv):
    sol[p_j] = K0 - sum((Rr[r_i][f] * sol[f] for f in free), K0)
X = [[K0] * d for _ in range(d)]
for j in range(d):
    X[pperm[j]][j] = sol[j]
XM = mmul(X, mmul(X, X))
lam = XM[0][0]
x3scalar = all((XM[i][j] - (lam if i == j else K0)).is_zero()
               for i in range(d) for j in range(d))
print(f"TWISTED-ACTION-FOUND at pattern {pi}: X^3 scalar = {x3scalar} "
      f"(twisted X need not be order 3; X^2 is a straight intertwiner). "
      f"Grading H1 via the sigma*-twisted class action...", flush=True)

SIG = {'a': 'a', 'b': 'c', 'c': 'b'}
def act_on_class(u):
    # twisted action: (X.u)(g) = X u(sigma^{-1} g); sigma = the deck swap (involution)
    return {g: [sum((X[i][k] * u[SIG[g]][k] for k in range(d)), K0) for i in range(d)]
            for g in u}
# express X.u in span(classes) + coboundaries: coboundary basis delta_v(g) = rho(g)v - v
cob = []
for v_idx in range(d):
    v = [K1 if i == v_idx else K0 for i in range(d)]
    cob.append({g: [ (sum((acts[g][i][k] * v[k] for k in range(d)), K0) - v[i])
                     for i in range(d)] for g in ('a', 'b', 'c')})
gens3 = ('a', 'b', 'c')
def flat(u):
    return [u[g][i] for g in gens3 for i in range(d)]
basis = [flat(u) for u in classes] + [flat(u) for u in cob]
Tmat = []
for u in classes:
    tgt = flat(act_on_class(u))
    aug = [list(col) + [tgt[r]] for r, col in enumerate(zip(*basis))]
    Rr2, piv2 = rref([row[:] for row in aug])
    coeff = [K0] * len(basis)
    for r_i, p_j in enumerate(piv2):
        if p_j < len(basis):
            coeff[p_j] = Rr2[r_i][len(basis)]
    Tmat.append(coeff[:len(classes)])
print("T (action on the 5 classes, rows = images):", flush=True)
for row in Tmat:
    print("  ", [str(x) for x in row], flush=True)
print("DONE — grade multiplicities from T's eigenstructure (analyze in FINDINGS).", flush=True)
