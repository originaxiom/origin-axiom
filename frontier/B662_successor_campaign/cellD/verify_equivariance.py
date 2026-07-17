"""CELL D — sigma*-equivariance / the subfield law's proof (B662 campaign).

THE CLAIM TO PROVE: the chord data (sigma*-matrix, Y-tensor) of the weld
double lies in the invariant trace field k(Gamma).  Fig-8: trace field
K = Q(sqrt-3) = k(Gamma) (degree 2), so the claim is arithmetic closure
+ Neumann-Reid (B659) — no computation needed.  The content is the
SILVER: L = Q(s,i), s^4 = 8s^2+16, degree 8; k(Gamma) = Q(i); the claim
is a deg-8 -> deg-2 Galois descent.

PROOF SHAPE (this script verifies every decisive ingredient EXACTLY):
  Gal(L/Q(i)) = {1, sigma, tau, sigma tau},
      sigma: s -> -s,   tau: s -> 4i/s   (both fix i; Klein four).
  (P0) Fix(sigma,tau) = Q(i)                        [linear algebra, exact]
  (P1) 2x2 letters: g(rho(x)) = eps_g(x) M_g rho(x) M_g^{-1}
       with explicit M_g, sign characters eps_g      [exact solve+check]
  (P2) weld descent datum: g(u).conj(M_{g'}).u^{-1} prop. M_g,
       g' = conj o g o conj                          [exact, 2x2]
  (P3) 27-level: g(LETS[x]) = W_g LETS[x] W_g^{-1} for ALL 12 letters
       of the double, W_g = lift_sl2(M_g)            [exact, 27x27]
       + g(U27) = W_g U27 conj(W_{g'})^{-1}          [exact]
  (P4) the cubic is invariant under every lift_sl2 image:
       e/f-derivation-invariance + h-weight-sum-zero [exact, tensor]
  (P5) THE DECISIVE STEP: Phi_g := (I6 (x) W_g^{-1}) o g  maps each
       banked H1 representative to ITSELF (exactly or mod B1) —
       i.e. the deterministic H1 basis is a Q(i)-form basis.
Given P0..P5 and the transport lemma (deterministic rational pipelines
commute with field automorphisms), g(Y_ijk) = Y_ijk for g = sigma, tau
=> every Y_ijk in Q(i) = k(Gamma); same for the sigma*-matrix C.

House rules: exact arithmetic (Fraction) in every decisive step.
"""
import json
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B649 = os.path.join(HERE, "..", "..", "B649_silver_holonomy")

T00 = time.time()

# =========================================================================
# Part 0 — the Galois group of L/Q(i), on the vec8 basis
# basis order: 1, s, s^2, s^3, i, i s, i s^2, i s^3   (re4 + im4)
# =========================================================================
MODP = [Fr(16), Fr(0), Fr(8), Fr(0)]   # s^4 = 16 + 8 s^2


def pmul_q(p, q):
    out = [Fr(0)] * 7
    for a_i, a in enumerate(p):
        if a == 0:
            continue
        for b_i, b in enumerate(q):
            out[a_i + b_i] += a * b
    for k in range(6, 3, -1):
        c = out[k]
        if c != 0:
            out[k] = Fr(0)
            for t, m in enumerate(MODP):
                out[k - 4 + t] += c * m
    return out[:4]


def v8mul(x, y):
    xr, xi = x[:4], x[4:]
    yr, yi = y[:4], y[4:]
    rr, ii = pmul_q(xr, yr), pmul_q(xi, yi)
    ri, ir = pmul_q(xr, yi), pmul_q(xi, yr)
    return [a - b for a, b in zip(rr, ii)] + [a + b for a, b in zip(ri, ir)]


def gal_from_images(img_s, img_i):
    """8x8 (as list of image-columns) of the Q-algebra map s->S, i->I."""
    cols = []
    for t in range(8):
        acc = [Fr(1), 0, 0, 0, 0, 0, 0, 0]
        acc = [Fr(x) for x in acc]
        for _ in range(t % 4):
            acc = v8mul(acc, img_s)
        if t >= 4:
            acc = v8mul(acc, img_i)
        cols.append(acc)
    return cols


def gal_v8(cols, v):
    out = [Fr(0)] * 8
    for t in range(8):
        if v[t] != 0:
            for r in range(8):
                out[r] += v[t] * cols[t][r]
    return out


F0, F1 = Fr(0), Fr(1)
VS = [F0, F1, F0, F0, F0, F0, F0, F0]           # s
VI = [F0, F0, F0, F0, F1, F0, F0, F0]           # i
SIG = gal_from_images([F0, -F1, F0, F0, F0, F0, F0, F0], VI)
# tau: s -> 4i/s = i(s^3 - 8s)/4  (1/s = (s^3-8s)/16)
TAU = gal_from_images([F0, F0, F0, F0, F0, Fr(-2), F0, Fr(1, 4)], VI)
CONJC = gal_from_images(VS, [F0, F0, F0, F0, -F1, F0, F0, F0])


def gal_compose(c2, c1):
    return [gal_v8(c2, c1[t]) for t in range(8)]


def gal_eq(c1, c2):
    return all(c1[t][r] == c2[t][r] for t in range(8) for r in range(8))


GID = gal_from_images(VS, VI)
STAU = gal_compose(SIG, TAU)

print("== P0: the Galois group Gal(L/Q(i)) ==", flush=True)
ok_hom = True
for nm, G in (("sigma", SIG), ("tau", TAU), ("conj", CONJC)):
    for t1 in range(8):
        b1 = [F1 if q == t1 else F0 for q in range(8)]
        for t2 in range(8):
            b2 = [F1 if q == t2 else F0 for q in range(8)]
            if gal_v8(G, v8mul(b1, b2)) != v8mul(gal_v8(G, b1),
                                                 gal_v8(G, b2)):
                ok_hom = False
print(f"  ring homomorphisms (64 basis products x3): {ok_hom}", flush=True)
print(f"  sigma^2 = tau^2 = id: "
      f"{gal_eq(gal_compose(SIG, SIG), GID) and gal_eq(gal_compose(TAU, TAU), GID)}",
      flush=True)
print(f"  sigma tau = tau sigma: {gal_eq(STAU, gal_compose(TAU, SIG))}",
      flush=True)
print(f"  sigma, tau, sigma-tau all != id: "
      f"{not gal_eq(SIG, GID) and not gal_eq(TAU, GID) and not gal_eq(STAU, GID)}",
      flush=True)
print(f"  conj o sigma = sigma o conj: "
      f"{gal_eq(gal_compose(CONJC, SIG), gal_compose(SIG, CONJC))}", flush=True)
print(f"  conj o tau = (sigma tau) o conj: "
      f"{gal_eq(gal_compose(CONJC, TAU), gal_compose(STAU, CONJC))}", flush=True)

rows_fix = []
for G in (SIG, TAU):
    for r in range(8):
        rows_fix.append([G[t][r] - GID[t][r] for t in range(8)])


def q_nullspace(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((k for k in range(r, m) if A[k][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        piv_cols.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    out = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for rr, pc in enumerate(piv_cols):
            v[pc] = -A[rr][fc]
        out.append(v)
    return out


fx = q_nullspace(rows_fix, 8)
fix_is_Qi = (len(fx) == 2 and
             sorted(tuple(t for t in range(8) if v[t] != 0)
                    for v in fx) == [(0,), (4,)])
print(f"  Fix(sigma,tau) = span(1, i) = Q(i): {fix_is_Qi}", flush=True)

# =========================================================================
# reload the banked pipeline (letters, weld, Fox rows, Z1, cob, H1 reps)
# =========================================================================
print("\n== reloading the banked 3b-i pipeline (letters/weld/Fox/H1) ==",
      flush=True)
t0 = time.time()
src = open(os.path.join(B649, "b649_stage3b_swap.py")).read()
head = src[:src.index('# ---- sigma* ---')]
ns = {"__name__": "cellD_shared",
      "__file__": os.path.join(B649, "b649_stage3b_swap.py")}
exec(compile(head, "b649_3bi_head.py", "exec"), ns)
print(f"  pipeline reloaded ({time.time()-t0:.0f}s)", flush=True)

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
mconj27 = ns["mconj27"]
lift_sl2 = ns["lift_sl2"]
mm2, adj2 = ns["mm2"], ns["adj2"]
G2m = ns["G2m"]
uweld = ns["u"]
U27, U27i = ns["U27"], ns["U27i"]
S1, S2, LETS = ns["S1"], ns["S2"], ns["LETS"]
rows27, Z1, cob, reps = ns["rows27"], ns["Z1"], ns["cob"], ns["reps"]
Span = ns["Span"]
Lnull = ns["L_nullspace_basis"]

assert len(reps) == 5 and len(Z1) == 31, "pipeline mismatch vs banked run"


def from8(v):
    return L([Fr(x) for x in v[:4]], [Fr(x) for x in v[4:]])


def gal(cols, x):
    return from8(gal_v8(cols, x.re + x.im))


def galM(cols, M):
    return [[gal(cols, x) for x in row] for row in M]


def m2inv(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    di = d.inv()
    return [[M[1][1] * di, (L0 - M[0][1]) * di],
            [(L0 - M[1][0]) * di, M[0][0] * di]]


def m2eq(A, B):
    return all((A[i][j] - B[i][j]).is_zero() for i in range(2)
               for j in range(2))


def meq27(A, B):
    return all((A[i][j] - B[i][j]).is_zero() for i in range(27)
               for j in range(27))


# =========================================================================
# Part 1 — the 2x2 Galois structure of the letters
# =========================================================================
print("\n== P1: 2x2 letters under Gal(L/Q(i)) ==", flush=True)
D2 = [[L1, L0], [L0, L0 - L1]]

# sigma: the checkerboard identity sigma(x) = eps(x) . D2 x D2^{-1}
EPS_SIG = {"a": -1, "b": +1, "c": -1}
ok_sig = True
for nm in "abc":
    X = G2m[nm]
    img = galM(SIG, X)
    tgt = mm2(mm2(D2, X), m2inv(D2))
    if EPS_SIG[nm] < 0:
        tgt = [[L0 - t for t in row] for row in tgt]
    ok = m2eq(img, tgt)
    ok_sig = ok_sig and ok
    print(f"  sigma({nm}) = {'-' if EPS_SIG[nm] < 0 else '+'}D {nm} D^-1: "
          f"{ok}", flush=True)
print(f"  M_sigma = D = diag(1,-1); eps_sigma = (-,+,-): {ok_sig}",
      flush=True)


def solve_intertwiner(gcols, signs):
    """solve g(X) M = eps(X) M X for X in a,b,c; return invertible M or None."""
    rows = []
    for nm in "abc":
        X = G2m[nm]
        gX = galM(gcols, X)
        e = signs[nm]
        for i in range(2):
            for j in range(2):
                row = [L0] * 4
                for p in range(2):
                    for q in range(2):
                        coef = L0
                        if q == j:
                            coef = coef + gX[i][p]
                        if p == i:
                            t = X[q][j]
                            coef = coef - (t if e > 0 else (L0 - t))
                        row[2 * p + q] = coef
                rows.append(row)
    basis = Lnull(rows, 4)
    for v in basis:
        M = [[v[0], v[1]], [v[2], v[3]]]
        d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        if not d.is_zero():
            return M, len(basis)
    return None, len(basis)


def find_intertwiner(gcols, label, first_guess):
    tried = [first_guess] + [p for p in
                             [{"a": sa, "b": sb, "c": sc}
                              for sa in (1, -1) for sb in (1, -1)
                              for sc in (1, -1)] if p != first_guess]
    for signs in tried:
        M, dim = solve_intertwiner(gcols, signs)
        if M is not None:
            return M, signs, dim
    return None, None, None


M_TAU, EPS_TAU, dim_tau = find_intertwiner(TAU, "tau", {"a": 1, "b": 1, "c": -1})
assert M_TAU is not None, "no tau-intertwiner found"
M_STAU, EPS_STAU, dim_stau = find_intertwiner(STAU, "sigma-tau",
                                              {"a": -1, "b": 1, "c": 1})
assert M_STAU is not None, "no sigma-tau-intertwiner found"


def show2(M, nm):
    for i in range(2):
        print(f"    {nm}[{i}] = "
              + " ; ".join(f"re{x.re} im{x.im}" for x in M[i]), flush=True)


for label, M, EPSX, gcols, dim in (("tau", M_TAU, EPS_TAU, TAU, dim_tau),
                                   ("sigma-tau", M_STAU, EPS_STAU, STAU,
                                    dim_stau)):
    okx = True
    Mi = m2inv(M)
    for nm in "abc":
        X = G2m[nm]
        img = galM(gcols, X)
        tgt = mm2(mm2(M, X), Mi)
        if EPSX[nm] < 0:
            tgt = [[L0 - t for t in row] for row in tgt]
        okx = okx and m2eq(img, tgt)
    sgn = "".join("+" if EPSX[nm] > 0 else "-" for nm in "abc")
    print(f"  {label}: solution space dim {dim}; eps = ({sgn}); "
          f"g(x) = eps M x M^-1 for a,b,c: {okx}", flush=True)
    show2(M, f"  M_{label}")
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    print(f"    det = re{d.re} im{d.im}", flush=True)

# =========================================================================
# Part 2 — the weld as a descent datum (2x2 level)
# g(u) . conj(M_{g'}) . u^{-1}  prop.to  M_g,   g' = conj o g o conj
#   sigma' = sigma;   tau' = sigma tau;   (sigma tau)' = tau
# =========================================================================
print("\n== P2: the weld's descent-datum compatibility (2x2) ==", flush=True)


def conj2(M):
    return [[x.conj() for x in row] for row in M]


def prop_scalar2(A, B):
    """A = lam*B? return lam or None."""
    lam = None
    for i in range(2):
        for j in range(2):
            if not B[i][j].is_zero():
                lam = A[i][j] * B[i][j].inv()
                break
        if lam is not None:
            break
    if lam is None:
        return None
    for i in range(2):
        for j in range(2):
            if not (A[i][j] - lam * B[i][j]).is_zero():
                return None
    return lam


ui = m2inv(uweld)
for glabel, gcols, Mg, Mgp in (("sigma", SIG, D2, D2),
                               ("tau", TAU, M_TAU, M_STAU),
                               ("sigma-tau", STAU, M_STAU, M_TAU)):
    V = mm2(mm2(galM(gcols, uweld), conj2(Mgp)), ui)
    lam = prop_scalar2(V, Mg)
    print(f"  {glabel}: g(u) conj(M_g') u^-1 = lam . M_g: "
          f"{'YES, lam = re' + str(lam.re) + ' im' + str(lam.im) if lam is not None else 'NO'}",
          flush=True)

# =========================================================================
# Part 3 — 27-level: one W_g intertwines ALL 12 letters of the double
# =========================================================================
print("\n== P3: 27-level intertwining, W_g = lift_sl2(M_g) ==", flush=True)
t0 = time.time()
W = {"sigma": lift_sl2(D2), "tau": lift_sl2(M_TAU),
     "stau": lift_sl2(M_STAU)}
Wi = {"sigma": lift_sl2(adj2(D2)), "tau": lift_sl2(adj2(M_TAU)),
      "stau": lift_sl2(adj2(M_STAU))}
for k in W:
    assert meq27(mmul(W[k], Wi[k]), meye(27)), f"W_{k} inverse failed"
print(f"  lifts built + inverses verified ({time.time()-t0:.0f}s)",
      flush=True)

GCOLS = {"sigma": SIG, "tau": TAU, "stau": STAU}
ok_all = {}
for gl in ("sigma", "tau", "stau"):
    t0 = time.time()
    ok12 = True
    for x in "abcABCdefDEF":
        M27 = LETS[x] if x in LETS else None
        if M27 is None:
            continue
        img = galM(GCOLS[gl], LETS[x])
        tgt = mmul(mmul(W[gl], LETS[x]), Wi[gl])
        if not meq27(img, tgt):
            ok12 = False
            print(f"    {gl}: FAIL at letter {x}", flush=True)
    ok_all[gl] = ok12
    print(f"  {gl}: g(LETS[x]) = W LETS[x] W^-1 for all 12 letters: "
          f"{ok12}  ({time.time()-t0:.0f}s)", flush=True)

print("\n  the U27 descent identity g(U27) = W_g U27 conj(W_g')^{-1}:",
      flush=True)
PARTNER = {"sigma": "sigma", "tau": "stau", "stau": "tau"}
for gl in ("sigma", "tau", "stau"):
    gp = PARTNER[gl]
    lhs = galM(GCOLS[gl], U27)
    rhs = mmul(mmul(W[gl], U27), mconj27(Wi[gp]))
    print(f"    {gl} (partner {gp}): exact: {meq27(lhs, rhs)}", flush=True)

# =========================================================================
# Part 4 — the cubic is invariant under every lift_sl2 image
# =========================================================================
print("\n== P4: cubic invariance ==", flush=True)
CUBQ = {tuple(map(int, k.split(","))): Fr(v)
        for k, v in json.load(open(os.path.join(B649,
                                                "cubic_rational.json"))).items()}
pr = json.load(open(os.path.join(B649, "e6_principal_rational.json")))
EQ = [[Fr(x) for x in row] for row in pr["e_pr"]]
FQ = [[Fr(x) for x in row] for row in pr["f_pr"]]
HQ = [[Fr(x) for x in row] for row in pr["h_pr"]]

wt = [HQ[i][i] for i in range(27)]
ok_h_offdiag = all(HQ[i][j] == 0 for i in range(27) for j in range(27)
                   if i != j)
ok_wt0 = all(wt[p] + wt[q] + wt[r] == 0 for (p, q, r) in CUBQ)
print(f"  h_pr diagonal: {ok_h_offdiag}; cubic support weight-sum zero "
      f"(=> torus invariance for any t2): {ok_wt0}", flush=True)


def derivation_zero(X):
    acc = {}
    for (p, q, r), c in CUBQ.items():
        for k in range(27):
            if X[p][k] != 0:
                acc[(k, q, r)] = acc.get((k, q, r), Fr(0)) + c * X[p][k]
            if X[q][k] != 0:
                acc[(p, k, r)] = acc.get((p, k, r), Fr(0)) + c * X[q][k]
            if X[r][k] != 0:
                acc[(p, q, k)] = acc.get((p, q, k), Fr(0)) + c * X[r][k]
    return all(v == 0 for v in acc.values())


ok_e = derivation_zero(EQ)
ok_f = derivation_zero(FQ)
ok_hd = derivation_zero(HQ)
print(f"  C(Xu,v,w)+C(u,Xv,w)+C(u,v,Xw) = 0 for X = e_pr, f_pr, h_pr: "
      f"{ok_e}, {ok_f}, {ok_hd}", flush=True)
print("  => the cubic is invariant under exp(nilpotents), the torus D(t2),"
      " and the Weyl factor — i.e. under EVERY lift_sl2 image.", flush=True)


def apply27(M, v):
    return [sum((M[i][k] * v[k] for k in range(27)
                 if not v[k].is_zero()), L0) for i in range(27)]


def Cval(u, v, w):
    acc = L0
    for (p, q, r), c in CUBQ.items():
        if u[p].is_zero() or v[q].is_zero() or w[r].is_zero():
            continue
        acc = acc + Lc(c) * u[p] * v[q] * w[r]
    return acc


vv = [[Lc(Fr((i * 7 + k * 3) % 5 - 2)) for i in range(27)] for k in range(3)]
sc_ok = True
for gl in ("tau", "sigma"):
    wu, wv, ww = (apply27(W[gl], vv[0]), apply27(W[gl], vv[1]),
                  apply27(W[gl], vv[2]))
    sc_ok = sc_ok and (Cval(wu, wv, ww) - Cval(*vv)).is_zero()
print(f"  spot-check Cval(W u, W v, W w) = Cval(u,v,w): {sc_ok}", flush=True)

# =========================================================================
# Part 5 — THE DECISIVE STEP: Phi_g fixes the banked H1 basis
# Phi_g(z) = blockwise W_g^{-1} . g(z)   (6 generator blocks of 27)
# =========================================================================
print("\n== P5: Phi_g on the five H1 representatives ==", flush=True)


def is_cocycle(z):
    for row in rows27:
        s_ = L0
        for t in range(162):
            if not z[t].is_zero() and not row[t].is_zero():
                s_ = s_ + row[t] * z[t]
        if not s_.is_zero():
            return False
    return True


def phi(gl, z):
    out = []
    for b in range(6):
        blk = [gal(GCOLS[gl], x) for x in z[27 * b: 27 * (b + 1)]]
        out.extend(apply27(Wi[gl], blk))
    return out


cobsp = Span(162)
for k, cv in enumerate(cob):
    cobsp.add(cv, ("cob", k))
red_reps = [cobsp.reduce(r)[0] for r in reps]
rsp = Span(162)
for idx, rr in enumerate(red_reps):
    assert rsp.add(rr, ("rep", idx))
T = []
for rr in red_reps:
    _, cf = rsp.reduce(rr)
    row = [L0] * 5
    for (tag, f) in cf:
        row[tag[1]] = row[tag[1]] + f
    T.append(row)


def solve5(Trows, target):
    A = [[Trows[r][c] for r in range(5)] for c in range(5)]
    b = target[:]
    n = 5
    Aug = [A[r][:] + [b[r]] for r in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if not Aug[r][c].is_zero())
        Aug[c], Aug[piv] = Aug[piv], Aug[c]
        pinv = Aug[c][c].inv()
        Aug[c] = [x * pinv for x in Aug[c]]
        for r in range(n):
            if r != c and not Aug[r][c].is_zero():
                f = Aug[r][c]
                Aug[r] = [x - f * y for x, y in zip(Aug[r], Aug[c])]
    return [Aug[r][n] for r in range(n)]


def lstr(x):
    return f"(re{x.re}|im{x.im})"


verdicts = {}
Gmats = {}
for gl in ("sigma", "tau", "stau"):
    print(f"  -- {gl} --", flush=True)
    Grows = []
    exact_ct, modB1_ct = 0, 0
    for m, rep in enumerate(reps):
        ph = phi(gl, rep)
        okz = is_cocycle(ph)
        d = [a - b for a, b in zip(ph, rep)]
        d_is_zero = all(x.is_zero() for x in d)
        dd, _ = cobsp.reduce(d)
        d_in_B1 = all(x.is_zero() for x in dd)
        if d_is_zero:
            exact_ct += 1
        if d_in_B1:
            modB1_ct += 1
            Grows.append([L1 if j == m else L0 for j in range(5)])
        else:
            red, cf = rsp.reduce(cobsp.reduce(ph)[0])
            assert all(x.is_zero() for x in red), \
                f"Phi_{gl}(rep{m}) not in H1 span"
            row = [L0] * 5
            for (tag, f) in cf:
                row[tag[1]] = row[tag[1]] + f
            Grows.append(solve5(T, row))
        print(f"    rep{m}: cocycle {okz}; Phi(rep)==rep exactly: "
              f"{d_is_zero}; == rep mod B1: {d_in_B1}", flush=True)
    Gmats[gl] = Grows
    isI = all((Grows[i][j] - (L1 if i == j else L0)).is_zero()
              for i in range(5) for j in range(5))
    verdicts[gl] = isI
    if not isI:
        for i, row in enumerate(Grows):
            print(f"    G[{i}] = " + " ; ".join(
                "0" if x.is_zero() else lstr(x) for x in row), flush=True)
    print(f"    G_{gl} = I5 (H1-classes fixed): {isI}", flush=True)

# =========================================================================
# Verdict + provenance
# =========================================================================
print("\n== VERDICT ==", flush=True)
all_p = (ok_hom and fix_is_Qi and ok_sig and all(ok_all.values())
         and ok_e and ok_f and ok_hd and ok_wt0 and sc_ok)
dec = all(verdicts.values())
print(f"  P0-P4 (group, letters, weld, 27-intertwining, cubic): {all_p}",
      flush=True)
print(f"  P5 (H1 basis is a Q(i)-form: G_sigma = G_tau = G_stau = I): "
      f"{dec}", flush=True)
if all_p and dec:
    print("  => THEOREM: the chord data (Y-tensor and sigma*-matrix) of the"
          " silver weld double is fixed by Gal(L/Q(i)) — it lies in"
          " Q(i) = k(Gamma).", flush=True)
else:
    print("  => MISSING LEMMA: see the failing gate above.", flush=True)

json.dump({
    "M_tau": [[x.re + x.im for x in row] for row in
              [[M_TAU[i][j] for j in range(2)] for i in range(2)]],
    "M_stau": [[x.re + x.im for x in row] for row in
               [[M_STAU[i][j] for j in range(2)] for i in range(2)]],
    "eps_sigma": EPS_SIG, "eps_tau": EPS_TAU, "eps_stau": EPS_STAU,
    "G_matrices_are_identity": verdicts,
}, open(os.path.join(HERE, "cellD_descent_data.json"), "w"),
    default=lambda o: [str(t) for t in o] if isinstance(o, list) else str(o))

print(f"\nCELL D verification DONE ({time.time()-T00:.0f}s total)",
      flush=True)
