"""B904 stage 3: fit the nine normalization scalars by Jacobi, then verify
Jacobi IN FULL (all 76076 unordered basis triples, exact rationals)."""
import itertools, os, pickle, json
from collections import defaultdict
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
VAR = os.environ.get("VARIANT", "cxcy_conj")
RAW = pickle.load(open(os.path.join(HERE, f"stage2_tensor_{VAR}.pkl"), "rb"))
DIM = 78
lam = sp.symbols("lam0 lam1 lam2")
mu = sp.symbols("mu0 mu1 mu2")
nu = sp.symbols("nu0 nu1 nu2")
kap = sp.symbols("kap0 kap1 kap2")
SYMS = list(lam) + list(mu) + list(nu) + list(kap)
loc = {s.name: s for s in SYMS}

BR = defaultdict(lambda: sp.Integer(0))
for k_str, v_str in RAW.items():
    a, b, k = eval(k_str)
    BR[(a, b, k)] = sp.sympify(v_str, locals=loc)

def br(a, b):
    """full antisymmetric bracket of basis elts -> dict k->coeff"""
    out = {}
    if a == b: return out
    s = 1
    if a > b: a, b, s = b, a, -1
    for (x, y, k), v in BRIDX.get((a, b), {}).items():
        out[k] = out.get(k, 0) + s*v
    return out

BRIDX = defaultdict(dict)
for (a, b, k), v in BR.items():
    if v != 0:
        BRIDX[(a, b)][(a, b, k)] = v

def jac(a, b, c):
    """[a,[b,c]] + [b,[c,a]] + [c,[a,b]] as dict k->sym coeff"""
    tot = defaultdict(lambda: sp.Integer(0))
    for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
        inner = br(y, z)
        for k, v in inner.items():
            for kk, vv in br(x, k).items():
                tot[kk] += v*vv
    return {k: sp.expand(v) for k, v in tot.items() if sp.expand(v) != 0}

# ---- probe fit: triples mixing summands and tri parts ----
probes = [(30, 47, 65), (0, 30, 46), (28, 30, 62), (30, 31, 46),
          (30, 46, 62), (31, 47, 63), (5, 33, 50), (28, 33, 50),
          (36, 52, 68), (30, 38, 46), (0, 5, 30), (34, 51, 66),
          (30, 40, 50), (32, 49, 64), (30, 45, 47)]
eqs = set()
for (a, b, c) in probes:
    for k, v in jac(a, b, c).items():
        eqs.add(sp.expand(v))
eqs = [e for e in eqs if e != 0]
print("probe equations:", len(eqs), flush=True)
sols = sp.solve(eqs, SYMS, dict=True)
print("VARIANT", VAR, "solution families:", len(sols), flush=True)
good = [s for s in sols if all(s.get(x, 1) != 0 for x in list(lam)+list(mu)+list(nu))]
print("nondegenerate families:", len(good), flush=True)
for s in good[:4]:
    print("  ", {str(k): v for k, v in s.items()}, flush=True)
if not good:
    json.dump({"fit": "FAILED", "families": len(sols)},
              open(os.path.join(HERE, "stage3_results.json"), "w"), indent=1)
    print("VARIANT", VAR, "FAILED"); raise SystemExit(0)
SUB = good[0]
# free symbols remaining -> set to 1 (scaling freedom)
SUBF = dict(SUB)
for x in SYMS:
    if x not in SUBF: SUBF[x] = 1
    else:
        rem = SUBF[x].free_symbols if hasattr(SUBF[x], "free_symbols") else set()
        for r in rem: SUBF[r] = 1
SUBF = {x: sp.Rational(sp.nsimplify(sp.sympify(v).subs(SUBF))) if hasattr(v, "subs") else sp.Rational(v)
        for x, v in SUBF.items()}
print("chosen scalars:", {str(k): v for k, v in SUBF.items()}, flush=True)

# numeric tensor
from fractions import Fraction as F
NBR = defaultdict(dict)
for (a, b, k), v in BR.items():
    val = sp.Rational(sp.expand(v.subs(SUBF)))
    if val != 0:
        NBR[(a, b)][k] = F(val.p, val.q)

def nbr(a, b):
    if a == b: return {}
    if a < b: return NBR.get((a, b), {})
    return {k: -v for k, v in NBR.get((b, a), {}).items()}

bad = 0; checked = 0
for a in range(DIM):
    for b in range(a+1, DIM):
        ab = nbr(a, b)
        for c in range(b+1, DIM):
            tot = defaultdict(lambda: F(0))
            for k, v in nbr(b, c).items():
                for kk, vv in nbr(a, k).items(): tot[kk] += v*vv
            for k, v in nbr(c, a).items():
                for kk, vv in nbr(b, k).items(): tot[kk] += v*vv
            for k, v in ab.items():
                for kk, vv in nbr(c, k).items(): tot[kk] += v*vv
            checked += 1
            if any(v != 0 for v in tot.values()):
                bad += 1
                if bad < 4: print("JACOBI FAIL at", (a, b, c), flush=True)
print(f"full Jacobi: {checked} triples, {bad} failures", flush=True)
pickle.dump({str(k): {kk: str(v) for kk, v in d.items()}
             for k, d in NBR.items()},
            open(os.path.join(HERE, "stage3_tensor.pkl"), "wb"))
json.dump({"fit": "OK", "scalars": {str(k): str(v) for k, v in SUBF.items()},
           "jacobi_triples": checked, "jacobi_failures": bad},
          open(os.path.join(HERE, "stage3_results.json"), "w"), indent=1)
print("saved", flush=True)
