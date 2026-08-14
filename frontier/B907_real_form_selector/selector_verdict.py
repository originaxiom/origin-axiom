"""B907 final: oblique-rule-compliant census + the FORM identification.

(1) Pattern census fixed: joint eigenvalues read componentwise (A v = lam v
    at the max component), never Rayleigh quotients (non-normal!).
(2) For each C-compatible wall-real phi (pattern eps14=+1, eps16=-1), the
    REAL FORM realized by sigma = phi o sigma_split has holomorphic
    involution class [phi o omega], omega = the frame's Chevalley involution
    (B893: omega(e_a) = e_{-a}, omega|_h = -1, d == 1). Its fixed dim names
    the form: 36 sp(4)->e6(6), 38 su(6)+su(2)->e6(2),
    46 so(10)+u(1)->e6(-14), 52 f4->e6(-26), 78 -> compact.
"""
import io, os, contextlib, json, itertools
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
print("frame rebuilt", flush=True)

FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
def flip_root(r): return tuple(r[FLIP[i]] for i in range(6))
ridx = {r: i for i, r in enumerate(ROOTS)}

# ---- rebuild tau's d (F2 solve, as before) ----
rows = []; rhs = []
for a in ROOTS:
    for b in ROOTS:
        s = tuple(a[i]+b[i] for i in range(6))
        if s in ridx:
            row = [0]*72
            row[ridx[a]] ^= 1; row[ridx[b]] ^= 1; row[ridx[s]] ^= 1
            c = eps(a, b) * eps(flip_root(a), flip_root(b))
            rows.append(row); rhs.append(0 if c == 1 else 1)
Aa = np.concatenate([np.array(rows, dtype=np.uint8),
                     np.array(rhs, dtype=np.uint8)[:, None]], axis=1)
r_ = 0
for c in range(72):
    piv = next((i for i in range(r_, Aa.shape[0]) if Aa[i, c]), None)
    if piv is None: continue
    Aa[[r_, piv]] = Aa[[piv, r_]]
    for i in range(Aa.shape[0]):
        if i != r_ and Aa[i, c]: Aa[i] ^= Aa[r_]
    r_ += 1
sol = [0]*72
for i in range(r_):
    c = next(cc for cc in range(72) if Aa[i, cc])
    sol[c] = int(Aa[i, 72])
d = {ROOTS[i]: (-1)**sol[i] for i in range(72)}

CH = {n: [sp.Rational(c) for c in INV[n]] for n in ns}

def apply_auto(vec, kind, signs):
    """apply sigma_chi (inner) or tau o sigma_chi (outer) to a 78-vector."""
    def chi(r):
        v = 1
        for i in range(6):
            if r[i] % 2: v *= signs[i]
        return v
    img = [sp.Integer(0)]*78
    if kind == "inner":
        for i in range(6):
            if vec[i]: img[i] += vec[i]
        for r in ROOTS:
            c = vec[6 + IDX[r]]
            if c: img[6 + IDX[r]] += c*chi(r)
    else:
        for i in range(6):
            if vec[i]: img[FLIP[i]] += vec[i]
        for r in ROOTS:
            c = vec[6 + IDX[r]]
            if c:
                fr = flip_root(r)
                img[6 + IDX[fr]] += c*d[r]*chi(fr)
    return img

def omega_vec(vec):
    """B893's Chevalley involution: h -> -h, e_a -> e_{-a} (d == 1)."""
    img = [sp.Integer(0)]*78
    for i in range(6):
        if vec[i]: img[i] -= vec[i]
    for r in ROOTS:
        c = vec[6 + IDX[r]]
        if c:
            nr = tuple(-x for x in r)
            img[6 + IDX[nr]] += c
    return img

def basis_vec(k):
    v = [sp.Integer(0)]*78; v[k] = sp.Integer(1); return v

def fixed_dim_of(mapfun):
    M = sp.zeros(78, 78)
    for k in range(78):
        img = mapfun(basis_vec(k))
        for i in range(78):
            M[i, k] = img[i]
    return int((M - sp.eye(78)).rank()), M   # fixed dim = 78 - rank(M - I)

def charge_eps(kind, signs):
    out = {}
    for n in ns:
        vec = CH[n]; img = apply_auto(vec, kind, signs)
        ev = None
        for k in range(78):
            if vec[k] == 0 and img[k] == 0: continue
            if vec[k] == 0: return None
            rt = sp.Rational(img[k])/sp.Rational(vec[k])
            if rt not in (1, -1): return None
            if ev is None: ev = int(rt)
            elif int(rt) != ev: return None
        out[n] = ev
    return out

FORM = {36: "e6(6) split", 38: "e6(2)", 46: "e6(-14)", 52: "e6(-26)",
        78: "compact"}
findings = []
for kind in ("inner", "outer"):
    for signs in itertools.product((1, -1), repeat=6):
        ce = charge_eps(kind, signs)
        if ce is None: continue
        wall_real = (ce[14] == 1 and ce[16] == -1)
        if not wall_real: continue
        # verify phi is an involution: phi^2 = id
        def phi(v, kind=kind, signs=signs): return apply_auto(v, kind, signs)
        sq_ok = all(phi(phi(basis_vec(k))) == basis_vec(k)
                    for k in (0, 6, 20, 50, 77))
        # the composite phi o omega -> the form class
        def comp(v): return phi(omega_vec(v))
        fd, M = fixed_dim_of(comp)
        fdim = 78 - fd
        # involution check for the composite on samples
        findings.append({"kind": kind, "signs": list(signs),
                         "eps": {str(n): ce[n] for n in ns},
                         "phi_involution_samples": bool(sq_ok),
                         "composite_fixed_dim": fdim,
                         "form": FORM.get(fdim, f"dim {fdim} (check)")})
        print(kind, signs, "eps", ce, "phi^2=id:", sq_ok,
              "-> composite fixed dim", fdim, "=", FORM.get(fdim, "?"),
              flush=True)
json.dump(findings, open(os.path.join(HERE, "verdict.json"), "w"), indent=1)
print("saved;", len(findings), "wall-real C-compatible involutions", flush=True)
