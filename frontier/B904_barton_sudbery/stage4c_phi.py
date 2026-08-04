"""B904 stage 4c: the explicit isomorphism phi: L(O_split, C'_split) -> the build.

Chevalley generators on both sides (BS: from stage4b's simple system in the
E6-matched order; build: the frame's unit-tuple simple roots). Parallel
extension by identical bracket words to full rank; phi = change of basis;
FULL verification phi([a,b]) = [phi a, phi b] on all 78x78 basis pairs.
Sign freedom: search over f_i sign flips (2^6) if the direct choice fails.
"""
import io, os, json, pickle, contextlib, itertools
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DIM = 78
RAW = pickle.load(open(os.path.join(HERE, "stage2c_tensor.pkl"), "rb"))
NBR = defaultdict(dict)
for kstr, d in RAW.items():
    key = eval(kstr)
    if len(key) == 2:
        for kk, vv in d.items(): NBR[key][int(kk)] = F(vv)
    else:
        NBR[(key[0], key[1])][key[2]] = F(d)
def nbr(a, b):
    if a == b: return {}
    if a < b: return NBR.get((a, b), {})
    return {k: -v for k, v in NBR.get((b, a), {}).items()}
def brv_bs(u, v):
    out = [F(0)]*DIM
    for i, cu in enumerate(u):
        if not cu: continue
        for j, cv in enumerate(v):
            if not cv: continue
            for k, w in nbr(i, j).items():
                out[k] += cu*cv*w
    return out

with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
# build bracket via BB table: BB[p][q] = coeff list
def brv_bd(u, v):
    out = [F(0)]*DIM
    for i, cu in enumerate(u):
        if not cu: continue
        for j, cv in enumerate(v):
            if not cv: continue
            w = BB[i][j]
            for k, c in enumerate(w):
                if c:
                    r = sp.Rational(c)
                    out[k] += cu*cv*F(r.p, r.q)
    return out

# ---- BS simple generators ----
RJ = json.load(open(os.path.join(HERE, "stage4_roots.json")))
CJ = json.load(open(os.path.join(HERE, "stage4b_cartan.json")))
perm = CJ["e6_permutation"]
ROOTS_BS = [tuple(sp.Rational(x) for x in r) for r in RJ["roots"]
            if any(sp.Rational(x) != 0 for x in r)]
# rebuild H and root vectors (as in 4b)
D1 = pickle.load(open(os.path.join(HERE, "stage1_tri.pkl"), "rb"))
SO_ = D1["SO"]; TRI_ = [tuple([F(x) for x in comp] for comp in t) for t in D1["TRI"]]
nso = 28
import numpy as _np
def somat(coeffs):
    M = [[F(0)]*8 for _ in range(8)]
    for a, c in enumerate(coeffs):
        if c:
            for i in range(8):
                for j in range(8):
                    M[i][j] += F(SO_[a][i][j])*c
    return M
rows = []
for a in range(nso):
    A1 = somat(TRI_[a][0])
    rows.append([A1[i][j] for i in range(8) for j in range(8) if i != j])
Mo = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r]
                for r in rows]).T
NSo = Mo.nullspace()
Hvecs = []
for v in NSo:
    vec = [F(0)]*DIM
    for a in range(nso):
        r = sp.Rational(v[a]); vec[a] = F(r.p, r.q)
    Hvecs.append(vec)
for g in (28, 29):
    vec = [F(0)]*DIM; vec[g] = F(1); Hvecs.append(vec)
ADH = []
for h in Hvecs:
    M = sp.zeros(DIM, DIM)
    for i, c in enumerate(h):
        if not c: continue
        for b in range(DIM):
            for k, v in nbr(i, b).items():
                M[k, b] += sp.Rational(c.numerator, c.denominator) \
                           * sp.Rational(v.numerator, v.denominator)
    ADH.append(M)
def rootvec(al):
    M = sp.Matrix.vstack(*[ADH[i] - al[i]*sp.eye(DIM) for i in range(6)])
    ns = M.nullspace()
    v = ns[0]
    den = sp.lcm([sp.Rational(x).q for x in v if x != 0])
    v = v*den
    return [F(sp.Rational(x).p, sp.Rational(x).q) for x in v]
f_ = [sp.Rational(97, 7), sp.Rational(31, 5), sp.Rational(11, 3),
      sp.Rational(7, 11), sp.Rational(3, 13), sp.Rational(1, 17)]
def height(al): return sum(f_[i]*al[i] for i in range(6))
POS = [al for al in ROOTS_BS if height(al) > 0]
setPOS = set(POS)
def is_sum(al):
    for be in POS:
        ga = tuple(al[k] - be[k] for k in range(6))
        if ga in setPOS: return True
    return False
SIMPLE = [al for al in POS if not is_sum(al)]
SIMPLE_ORD = [SIMPLE[perm[i]] for i in range(6)]  # E6-order
E_bs, Fv_bs, H_bs = [], [], []
for al in SIMPLE_ORD:
    e = rootvec(al)
    fneg = rootvec(tuple(-x for x in al))
    h = brv_bs(e, fneg)
    # normalize: want [h, e] = 2e
    he = brv_bs(h, e)
    nz = next(i for i in range(DIM) if e[i])
    c = he[nz] / e[nz] / 2      # [h,e] = 2c e  => scale fneg by 1/c
    fneg = [x / c for x in fneg]
    h = brv_bs(e, fneg)
    E_bs.append(e); Fv_bs.append(fneg); H_bs.append(h)
print("BS Chevalley generators normalized", flush=True)

# ---- build simple generators ----
def unit(i): return tuple(1 if j == i else 0 for j in range(6))
E_bd, F_bd, H_bd = [], [], []
for i in range(6):
    al = unit(i)
    p = 6 + IDX[al]; n = 6 + IDX[tuple(-x for x in al)]
    e = [F(0)]*DIM; e[p] = F(1)
    fn = [F(0)]*DIM; fn[n] = F(1)
    h = brv_bd(e, fn)
    he = brv_bd(h, e)
    nz = next(k for k in range(DIM) if e[k])
    c = he[nz] / e[nz] / 2
    fn = [x / c for x in fn]
    h = brv_bd(e, fn)
    E_bd.append(e); F_bd.append(fn); H_bd.append(h)
print("build Chevalley generators normalized", flush=True)

def try_signs(signs):
    gens_bs = [(E_bs[i], [x*signs[i] for x in Fv_bs[i]]) for i in range(6)]
    gens_bd = [(E_bd[i], F_bd[i]) for i in range(6)]
    basis_bs, basis_bd = [], []
    Mrref = sp.zeros(0, DIM)
    def rank_add(vec):
        nonlocal Mrref
        M2 = sp.Matrix.vstack(Mrref, sp.Matrix([[sp.Rational(x.numerator,
                              x.denominator) for x in vec]]))
        if M2.rank() > Mrref.shape[0]:
            Mrref = M2.rref()[0][:M2.rank(), :]
            return True
        return False
    queue = []
    for i in range(6):
        for v_bs, v_bd in ((gens_bs[i][0], gens_bd[i][0]),
                           (gens_bs[i][1], gens_bd[i][1])):
            if rank_add(v_bs):
                basis_bs.append(v_bs); basis_bd.append(v_bd)
                queue.append((v_bs, v_bd))
    idx = 0
    while len(basis_bs) < DIM and idx < len(basis_bs):
        for g in range(len(queue[:12])):
            a_bs, a_bd = basis_bs[idx], basis_bd[idx]
            g_bs, g_bd = queue[g]
            w_bs = brv_bs(g_bs, a_bs)
            if any(w_bs) and rank_add(w_bs):
                w_bd = brv_bd(g_bd, a_bd)
                basis_bs.append(w_bs); basis_bd.append(w_bd)
        idx += 1
    if len(basis_bs) < DIM:
        return None, f"span stalled at {len(basis_bs)}"
    B_bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in v]
                      for v in basis_bs]).T
    B_bd = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in v]
                      for v in basis_bd]).T
    PHI = B_bd * B_bs.inv()
    return PHI, "ok"

PHI, msg = try_signs([1]*6)
print("direct sign choice:", msg, flush=True)
if PHI is None:
    for signs in itertools.product((1, -1), repeat=6):
        PHI, msg = try_signs(list(signs))
        if PHI is not None:
            print("signs", signs, msg, flush=True); break
assert PHI is not None

# FULL verification on all basis pairs
def col(v): return [F(sp.Rational(PHI[k, v]).p, sp.Rational(PHI[k, v]).q)
                    for k in range(DIM)]
PHIcols = [col(v) for v in range(DIM)]
bad = 0
for a in range(DIM):
    ea = [F(0)]*DIM; ea[a] = F(1)
    for b in range(a+1, DIM):
        eb = [F(0)]*DIM; eb[b] = F(1)
        lhs_vec = brv_bs(ea, eb)
        # phi(lhs)
        lhs = [F(0)]*DIM
        for i, c in enumerate(lhs_vec):
            if c:
                for k in range(DIM):
                    lhs[k] += c*PHIcols[i][k]
        rhs = brv_bd(PHIcols[a], PHIcols[b])
        if lhs != rhs:
            bad += 1
            if bad < 4: print("MISMATCH at", (a, b), flush=True)
print(f"HOMOMORPHISM CHECK: {DIM*(DIM-1)//2} pairs, {bad} mismatches", flush=True)
if bad == 0:
    pickle.dump([[str(PHI[i, j]) for j in range(DIM)] for i in range(DIM)],
                open(os.path.join(HERE, "stage4c_phi.pkl"), "wb"))
    det = PHI.det()
    print("phi det:", det, "-> ISOMORPHISM" if det != 0 else "", flush=True)
json.dump({"mismatches": bad,
           "verdict": "ISOMORPHISM" if bad == 0 else "FAILED"},
          open(os.path.join(HERE, "stage4c_results.json"), "w"), indent=1)
print("saved", flush=True)
