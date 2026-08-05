"""B907 completion: (a) the outer lift via the general F2-cocycle solve;
(b) the epsilon-pattern feasibility census on the C-weight system --
any C-stabilizing involution acts +-diagonally on the charges (B901),
so a pattern is realizable ONLY if it preserves the joint weight multiset.
"""
import io, os, contextlib, json, itertools
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
print("frame rebuilt", flush=True)

FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
def flip_root(r): return tuple(r[FLIP[i]] for i in range(6))

# ---- (a) solve d: ROOTS -> +-1 with d(a)d(b)d(a+b) = eps(a,b)*eps(fa,fb) ----
import numpy as np
ridx = {r: i for i, r in enumerate(ROOTS)}
rows = []; rhs = []
for a in ROOTS:
    for b in ROOTS:
        s = tuple(a[i]+b[i] for i in range(6))
        if s in ridx:
            row = [0]*72
            row[ridx[a]] ^= 1; row[ridx[b]] ^= 1; row[ridx[s]] ^= 1
            c = eps(a, b) * eps(flip_root(a), flip_root(b))
            rows.append(row); rhs.append(0 if c == 1 else 1)
A = np.array(rows, dtype=np.uint8); bv = np.array(rhs, dtype=np.uint8)
# GF(2) gaussian elimination
Aa = np.concatenate([A, bv[:, None]], axis=1)
r_ = 0
for c in range(72):
    piv = None
    for i in range(r_, Aa.shape[0]):
        if Aa[i, c]: piv = i; break
    if piv is None: continue
    Aa[[r_, piv]] = Aa[[piv, r_]]
    for i in range(Aa.shape[0]):
        if i != r_ and Aa[i, c]:
            Aa[i] ^= Aa[r_]
    r_ += 1
inconsistent = any(row[:72].sum() == 0 and row[72] for row in Aa)
print("F2 solve: rank", r_, "inconsistent:", bool(inconsistent), flush=True)
sol = [0]*72
if not inconsistent:
    for i in range(r_):
        c = next(cc for cc in range(72) if Aa[i, cc])
        sol[c] = int(Aa[i, 72])
    d = {ROOTS[i]: (-1)**sol[i] for i in range(72)}
    # verify tau is an automorphism on all bracket pairs incl. h-parts
    bad = 0
    for a in ROOTS:
        for b in ROOTS:
            s = tuple(a[i]+b[i] for i in range(6))
            if s in ridx:
                if d[a]*d[b]*eps(flip_root(a), flip_root(b)) != eps(a, b)*d[s]:
                    bad += 1
    print("tau cocycle verified, violations:", bad, flush=True)

# charges
CH = {n: [sp.Rational(c) for c in INV[n]] for n in ns}
def tau_sigma_action(signs, n):
    def chi(r):
        v = 1
        for i in range(6):
            if r[i] % 2: v *= signs[i]
        return v
    vec = CH[n]; img = [sp.Integer(0)]*78
    for i in range(6):
        if vec[i]: img[FLIP[i]] += vec[i]
    for r in ROOTS:
        c = vec[6 + IDX[r]]
        if c:
            fr = flip_root(r)
            img[6 + IDX[fr]] += c*d[r]*chi(fr)
    ev = None
    for k in range(78):
        if vec[k] == 0 and img[k] == 0: continue
        if vec[k] == 0: return None
        rt = sp.Rational(img[k])/sp.Rational(vec[k])
        if rt not in (1, -1): return None
        if ev is None: ev = int(rt)
        elif int(rt) != ev: return None
    return ev

def outer_fixed_dim(signs):
    def chi(r):
        v = 1
        for i in range(6):
            if r[i] % 2: v *= signs[i]
        return v
    dim = 4; seen = set()
    for r in ROOTS:
        if r in seen: continue
        fr = flip_root(r)
        if fr == r:
            if d[r]*chi(r) == 1: dim += 1
            seen.add(r)
        else:
            if d[r]*chi(fr)*d[fr]*chi(r) == 1: dim += 1
            seen.add(r); seen.add(fr)
    return dim

outer = []
if not inconsistent:
    for signs in itertools.product((1, -1), repeat=6):
        fd = outer_fixed_dim(signs)
        acts = {n: tau_sigma_action(signs, n) for n in ns}
        outer.append({"signs": list(signs), "fixed_dim": fd,
                      "eps": {str(n): acts[n] for n in ns},
                      "C_compatible": all(a is not None for a in acts.values())})
    from collections import Counter
    print("outer fixed-dim distribution:",
          dict(Counter(row["fixed_dim"] for row in outer)), flush=True)
    print("outer C-compatible:",
          [(row["fixed_dim"], row["eps"]) for row in outer
           if row["C_compatible"]][:8], flush=True)

# ---- (b) the epsilon-pattern feasibility census on the C-weight system ----
ADn = {}
for n in ns:
    M = mp.matrix(78, 78)
    S = sp.Matrix(ADS[n])
    for i in range(78):
        for j in range(78):
            v = S[i, j]
            if v != 0:
                M[i, j] = mp.mpf(sp.Rational(v).p)/mp.mpf(sp.Rational(v).q)
    ADn[n] = M
# generic combo for joint eigenvectors
combo = ADn[8]*mp.pi + ADn[14]*mp.e + ADn[16]*mp.sqrt(2) + ADn[22]*mp.sqrt(3)
E, ER = mp.eig(combo)
quads = []
for k in range(78):
    v = mp.matrix([ER[i, k] for i in range(78)])
    nrm = mp.sqrt(sum(abs(x)**2 for x in v))
    v = v*(1/nrm)
    q = []
    for n in ns:
        Av = ADn[n]*v
        lam = sum(Av[i]*mp.conj(v[i]) for i in range(78))
        q.append(lam)
    quads.append(tuple(q))
def close(x, y): return abs(x - y) < mp.mpf("1e-25")
def in_system(q):
    return any(all(close(q[t], p[t]) for t in range(4)) for p in quads)
feasible = {}
for pat in itertools.product((1, -1), repeat=4):
    ok = all(in_system(tuple(pat[t]*q[t] for t in range(4))) for q in quads)
    feasible[pat] = ok
print("pattern feasibility (eps8, eps14, eps16, eps22):", flush=True)
for pat, ok in feasible.items():
    tag = " WALL-REAL-CANDIDATE" if (pat[1] == 1 and pat[2] == -1 and ok) else ""
    if ok: print("  ", pat, "FEASIBLE" + tag, flush=True)
json.dump({"outer": outer, "tau_ok": not inconsistent,
           "pattern_feasibility": {str(k): v for k, v in feasible.items()}},
          open(os.path.join(HERE, "results_complete.json"), "w"), indent=1,
          default=str)
print("saved", flush=True)
