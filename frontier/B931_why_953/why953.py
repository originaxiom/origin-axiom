#!/usr/bin/env python3
"""B931 -- WHY 953 (the decode's residue).  LANE 2.

B928 derived the twist arithmetic down to one residue: 953 and 2304 = 2^8 3^2
enter through the K-norm of d = 1 - 2*(flip mass) on the banked atom lines
(N_{K/Q}(d) = -(953/2304)^2 on both colorless families), and the derivation
stopped at the eigenline coordinates.  This cell traces WHERE the two integers
are born.  Attack lines, declared:

(ii) THE ATOM-LINE TRACE.  The colorless eigenline solve is re-done
  SYMBOLICALLY over Q[x]/(h(x)): the eigenvector is an adjugate column of
  (C - x), every downstream quantity (the H+-form value q, the H+D2-twisted
  value q', the flip-restricted value q_f) is a POLYNOMIAL in x, and field
  norms become resultants with h.  Factoring the resultants -- and the
  form-polynomials themselves -- pins the exact site where 953 and 2304 are
  born.  On the A-family the H-norm is sesquilinear: the conjugation of
  L = Q[x]/(h_A) over K is computed as a polynomial t(x) (the odd-charge
  flip theta -> theta - 2*o(theta)) and the form pairs v(t(x)) with v(x).
  Per-coordinate and per-minor resultants are recorded (which minor births
  the prime).

(new) THE RATIONAL BLOCK GRAMS.  The three rational charge blocks W3 (h_S),
  W6 (h_A), W18 (h_col) as saturated integer lattices; the H- and H'-Gram
  determinants, their ratios, the cross-block pairings under both forms, and
  the pencil operators X = G^-1 G'.  (Outcome: the rational/bilinear world is
  953-blind; D2 recouples W3 with W6.)

(i)+(iii) THE WHITELIST (declared BEFORE compute; each candidate is a named
  structural evaluation of banked objects):
  W-A  discriminants/leads/consts: mu13, h_S, h_A, h_col, HIER, the two
       d-minpolys, the two flip-mass minpolys, the colored e1/e3 minpolys.
  W-B  pairwise resultants among {mu13, h_S, h_A, h_col, HIER}.
  W-C  values of {mu13, h_S, h_A, h_col} at distinguished small rationals.
  W-D  the 27-rep trace Gram of the four charges G_mn = tr(R_m R_n).
  W-E  (in W-A) coefficient contents -- where the {2,3}-parts live.
  W-F  Res(mp_dS, mp_dA), Res(mp_mS, mp_mA).
  W-G  the field K itself: disc(K) by round_two, the index of Z[theta_S],
       splitting in K of the declared prime list {2,3,5,7,11,13,17,19,29,
       953,1129,421493,72869,20417473} (every prime that appears in a banked
       value-layer invariant), and the quadratic-resolvent symbols.

(vii) THE DIVISOR MAP (the deliverable's core).  In a monic integral model of
  K the exact prime-ideal divisors of d_S, d_A, m_S, m_A -- every valuation
  at every place over {2, 3, 953} (and the flip-mass primes) -- computed with
  sympy round_two + prime_decomp + PrimeIdeal.valuation, and compared with
  the banked B918 divisor of the hierarchy element V (den(V) = P1(953)^4,
  the observer's place).

HOUSE RULES: exact arithmetic for all verdicts (no numerics anywhere);
verify-don't-trust (Mc, h_S, h_A re-derived from the frame; every derived
minpoly must equal its banked B916/B928 counterpart before it is used;
banked K-coordinates are cross-checked through an independent model);
e6_centralizer.py exec'd in an isolated namespace with chdir to scratch and
__file__ set; failures reported honestly.

Output: results.json (exact data + checks).
"""
import io
import os
import json
import time
import pickle
import tempfile
import itertools
import contextlib
from fractions import Fraction as Fr

import sympy as sp
from sympy import Symbol, Poly, Rational, factorint, resultant, discriminant

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b931_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B931 why 953", "checks": {}, "notes": []}
x = Symbol("x")
y = Symbol("y")


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def dump():
    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        dump()
        raise SystemExit(f"UNSTABLE at {name}")


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


def ffac(n):
    """factor an integer: trial division to 10^6, provable primality on
    leftovers (BPSW), full factorization only below 10^24 -- larger
    composite leftovers are honestly marked C<digits>:<value>.  Every prime
    below 10^6 (in particular 953) is ALWAYS found by the trial stage."""
    n = int(n)
    if n == 0:
        return {"0": 1}
    out = {}
    if n < 0:
        out["-1"] = 1
        n = -n
    f = factorint(n, limit=10 ** 6)
    comp = []
    for p, e in sorted(f.items()):
        if p < 10 ** 12 or sp.isprime(p):
            out[str(p)] = out.get(str(p), 0) + int(e)
        else:
            comp.append((p, e))
    for p, e in comp:
        if p < 10 ** 24:
            try:
                for q_, e2 in sorted(factorint(p).items()):
                    out[str(q_)] = out.get(str(q_), 0) + int(e2) * int(e)
                continue
            except Exception:
                pass
        out[f"C{len(str(p))}:{p}"] = out.get(f"C{len(str(p))}:{p}", 0) \
            + int(e)
    return out


def has953(fac):
    return "953" in fac


# ================================================================ [0] inputs
log("[0] banked inputs ...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27",
                                   "rep27.json")))
REP = [[[int(v) for v in row] for row in REPJ["rep"][str(k)]]
       for k in range(78)]
WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diag_27_weights", len(set(WT)) == 27)

B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
piW_banked = list(B912["H_plus_support_pi"])
cbP = [int(v) for v in B912["H_plus_entries_c_b"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2 = [int(v) for v in B916["H_prime_diag_vs_H_plus"]["D2"]]
MPS_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["S0"]]
MPA_banked = [int(c) for c in B916["d_ratio_minpolys_desc"]["A0p"]]
B914 = json.load(open(os.path.join(REPO, "frontier", "B914_ratio_table",
                                   "results.json")))
hS_banked = [int(c) for c in B914["h_S_B883"]]
B918 = json.load(open(os.path.join(REPO, "frontier", "B918_v_kummer",
                                   "results.json")))
HIER = [int(c) for c in B918["hier_cubic"]["coeffs"]]
B928 = json.load(open(os.path.join(REPO, "frontier", "B928_d2_decode",
                                   "results.json")))
mpmS_banked = [int(c) for c in B928["Q2_colorless"]["minpoly_m_S"]]
mpmA_banked = [int(c) for c in B928["Q2_colorless"]["minpoly_m_A"]]
mS_K = [Fr(c) for c in B928["Q2_colorless"]["m_S_K_coords"]]
mA_K = [Fr(c) for c in B928["Q2_colorless"]["m_A_K_coords"]]
V_K = [Fr(1084447130452992, 139398566318089),
       Fr(2399403349337702400, 1812181362135157),
       Fr(3020358603911646412800, 23558357707757041)]      # banked B918 root
E1MP = [256, -768, -828, 2859]                      # B928 Q3 (colored e1)
E3MP = [12230590464, -10239934464, 255728448, 865523177]   # B928 Q3 (det X)
MU = [500716339200, -2075673600, -4769856, 2197]    # mu13, descending (banked)

FLIP6 = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
negflip = {tuple(-w[FLIP6[i]] for i in range(6)): b
           for b, w in enumerate(WT)}
piW = [negflip[WT[b]] for b in range(27)]
CHK("weight_pairing_recomputed_matches_banked", piW == piW_banked)
CHK("D2_has_11_flips", sum(1 for v in D2 if v == -1) == 11)

# ================================================================ [1] frame
log("[1] B854 frame (isolated exec, chdir scratch, __file__ set) ...")
cache = os.path.join(SCRATCH, "b931_frame_cache.pkl")
if os.path.exists(cache):
    FR = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
          "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    FR = {"ns": list(g6["ns"]),
          "INV": {n: [Fr(c) for c in g6["INV"][n]] for n in g6["ns"]}}
    pickle.dump(FR, open(cache, "wb"))
ns = FR["ns"]
INV = FR["INV"]
CHK("frame_ns_8_14_16_22", sorted(ns) == [8, 14, 16, 22])

Rex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV[n]):
        if c:
            Rk = REP[k]
            for a in range(27):
                ra = Rk[a]
                for b in range(27):
                    if ra[b]:
                        M[a][b] += c * ra[b]
    Rex[n] = M
CHK("four_charges_commute",
    all(all(sum(Rex[m_][i][t] * Rex[n_][t][j] for t in range(27))
            == sum(Rex[n_][i][t] * Rex[m_][t][j] for t in range(27))
            for i in range(27) for j in range(27))
        for m_, n_ in itertools.combinations(ns, 2)))

# ================================================================ [2] Mc
log("[2] Mc = 3 R8 + 7 R14 + 13 R16 + 17 R22; charpoly factors ...")
CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
      for i in range(27)]
Me = [[Fr(3) * Rex[8][i][j] + Fr(13) * Rex[16][i][j] for j in range(27)]
      for i in range(27)]
Mo = [[Fr(7) * Rex[14][i][j] + Fr(17) * Rex[22][i][j] for j in range(27)]
      for i in range(27)]
McS = sp.Matrix(27, 27, lambda i, j: Rational(Mc[i][j].numerator,
                                              Mc[i][j].denominator))
cp = McS.charpoly(x)
fl = sp.factor_list(cp.as_expr())
facs = sorted([(sp.degree(f, x), m, Poly(f, x)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])
h_S, h_A, h_col = facs[0][2], facs[1][2], facs[2][2]
if h_S.LC() < 0:
    h_S = Poly(-h_S.as_expr(), x)
if h_A.LC() < 0:
    h_A = Poly(-h_A.as_expr(), x)
if h_col.LC() < 0:
    h_col = Poly(-h_col.as_expr(), x)
CHK("h_S_equals_banked_B914",
    [int(c) for c in h_S.all_coeffs()] == hS_banked, str(hS_banked))
REC("h_A_coeffs", [str(c) for c in h_A.all_coeffs()])
REC("h_col_coeffs", [str(c) for c in h_col.all_coeffs()])
mu_poly = Poly(MU, x)
hier_poly = Poly(HIER, x)


def matmulQ(Xm, Ym):
    n_ = len(Xm)
    Yt = [[Ym[j][i] for j in range(n_)] for i in range(n_)]
    return [[sum(a * b for a, b in zip(row, col) if a and b)
             for col in Yt] for row in Xm]


def poly_mat(coeffs):
    Acc = [[coeffs[0] if i == j else Fr(0) for j in range(27)]
           for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        for i in range(27):
            Acc[i][i] += c
    return Acc


def qkernel(M):
    m, n_ = len(M), len(M[0])
    A2 = [row[:] for row in M]
    piv = []
    rr = 0
    for c in range(n_):
        pr = next((r for r in range(rr, m) if A2[r][c] != 0), None)
        if pr is None:
            continue
        A2[rr], A2[pr] = A2[pr], A2[rr]
        iv = A2[rr][c]
        A2[rr] = [e / iv for e in A2[rr]]
        for r in range(m):
            if r != rr and A2[r][c]:
                f = A2[r][c]
                A2[r] = [A2[r][j] - f * A2[rr][j] for j in range(n_)]
        piv.append(c)
        rr += 1
    ker = []
    for fc in [c for c in range(n_) if c not in piv]:
        v = [Fr(0)] * n_
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A2[i][fc]
        ker.append(v)
    return ker


def qsolve_span(basis, vec):
    k, n_ = len(basis), len(basis[0])
    Aug = [[basis[j][i] for j in range(k)] + [vec[i]] for i in range(n_)]
    piv = []
    rr = 0
    for c in range(k):
        pr = next((r for r in range(rr, n_) if Aug[r][c] != 0), None)
        if pr is None:
            continue
        Aug[rr], Aug[pr] = Aug[pr], Aug[rr]
        iv = Aug[rr][c]
        Aug[rr] = [e / iv for e in Aug[rr]]
        for r in range(n_):
            if r != rr and Aug[r][c]:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[rr][j] for j in range(k + 1)]
        piv.append(c)
        rr += 1
    sol = [Fr(0)] * k
    for i, c in enumerate(piv):
        sol[c] = Aug[i][k]
    for i in range(n_):
        if sum(basis[j][i] * sol[j] for j in range(k)) != vec[i]:
            return None
    return sol


def restrict(Mbig, W):
    Crows = []
    for w in W:
        img = [sum(Mbig[i][j] * w[j] for j in range(27) if w[j])
               for i in range(27)]
        solv = qsolve_span(W, img)
        assert solv is not None
        Crows.append(solv)
    return [[Crows[b][a] for b in range(len(W))] for a in range(len(W))]


hS_fr = [Fr(int(c)) for c in h_S.all_coeffs()]
hA_fr = [Fr(sp.Rational(c).p, sp.Rational(c).q) for c in h_A.all_coeffs()]
W3 = qkernel(poly_mat(hS_fr))
W6 = qkernel(poly_mat(hA_fr))
CHK("rational_blocks_dim_3_and_6", len(W3) == 3 and len(W6) == 6)
C_S = restrict(Mc, W3)
C_A = restrict(Mc, W6)
CO3 = restrict(Mo, W3)
CHK("Mo_restricted_to_W3_is_zero",
    all(CO3[i][j] == 0 for i in range(3) for j in range(3)),
    "the vacuum 3-space is odd-charge-free: the S-side H-norm is bilinear")
CE6 = restrict(Me, W6)
CO6 = restrict(Mo, W6)


def sym_trace(Cmat, hpoly, W, tag, conj_data=None, normalize=False):
    """the symbolic eigenline trace over Q[x]/(hpoly) for one block.

    conj_data = (C_even, C_odd) when the H-norm needs the sesquilinear
    pairing v(t(x)) vs v(x), t = the odd-flip conjugation of L over K.
    normalize: divide the lifted 27-vector by its rational content (a
    declared gauge choice; ratios d, m are gauge-free either way)."""
    n_ = len(Cmat)
    hx = hpoly.as_expr()
    log(f"[{tag}] adjugate of (C - x I) ({n_}x{n_}) over Q[x] ...")
    Mx = sp.Matrix(n_, n_, lambda i, j:
                   Rational(Cmat[i][j].numerator, Cmat[i][j].denominator)
                   - (x if i == j else 0))
    adj = Mx.adjugate()
    det = Mx.det()
    CHK(f"{tag}_adjugate_identity_det",
        sp.expand(det * hpoly.LC() - (-1) ** n_ * hx) == 0)
    col, colj = None, None
    for j in range(n_):
        cj = [Poly(adj[i, j], x) for i in range(n_)]
        if any(sp.rem(p.as_expr(), hx, x) != 0 for p in cj):
            col = cj
            colj = j
            break
    CHK(f"{tag}_adjugate_column_found", col is not None, f"column {colj}")
    eig_ok = all(
        sp.rem(sp.expand(sum(Mx[i, k] * col[k].as_expr()
                             for k in range(n_))), hx, x) == 0
        for i in range(n_))
    CHK(f"{tag}_eigenline_all_rows_mod_h", eig_ok)

    # the conjugation t(x) of L over K (A-side): theta -> theta - 2 o(theta)
    tpoly = x
    if conj_data is not None:
        C_ev, C_od = conj_data
        i0 = next(i for i in range(n_)
                  if sp.rem(col[i].as_expr(), hx, x) != 0
                  and sp.gcd(Poly(sp.rem(col[i].as_expr(), hx, x), x),
                             hpoly).degree() == 0)
        vi0_inv = sp.invert(sp.rem(col[i0].as_expr(), hx, x), hx, x)
        ox = sp.rem(sp.expand(
            sum(Rational(C_od[i0][j].numerator, C_od[i0][j].denominator)
                * col[j].as_expr() for j in range(n_)) * vi0_inv), hx, x)
        # certificates: C_od v = o v, C_ev v = (x - o) v, all rows, mod h
        CHK(f"{tag}_odd_eigenvalue_all_rows",
            all(sp.rem(sp.expand(
                sum(Rational(C_od[i][j].numerator, C_od[i][j].denominator)
                    * col[j].as_expr() for j in range(n_))
                - ox * col[i].as_expr()), hx, x) == 0 for i in range(n_)))
        CHK(f"{tag}_even_eigenvalue_all_rows",
            all(sp.rem(sp.expand(
                sum(Rational(C_ev[i][j].numerator, C_ev[i][j].denominator)
                    * col[j].as_expr() for j in range(n_))
                - (x - ox) * col[i].as_expr()), hx, x) == 0
                for i in range(n_)))
        tpoly = sp.rem(sp.expand(x - 2 * ox), hx, x)
        CHK(f"{tag}_conjugation_is_root_of_h",
            sp.rem(sp.expand(hx.subs(x, tpoly)), hx, x) == 0)
        tpow = [sp.Integer(1)]
        for _ in range(1, hpoly.degree()):
            tpow.append(sp.rem(sp.expand(tpow[-1] * tpoly), hx, x))

        def compose_t(p):
            cs = list(reversed(p.all_coeffs()))
            return Poly(sp.rem(sp.expand(
                sum(sp.Rational(cs[k]) * tpow[k]
                    for k in range(len(cs)))), hx, x), x)

        tt = compose_t(Poly(tpoly, x))
        CHK(f"{tag}_conjugation_is_involution",
            sp.expand(tt.as_expr() - x) == 0)
        CHK(f"{tag}_conjugation_nontrivial",
            sp.rem(sp.expand(tpoly - x), hx, x) != 0)

    # lift to the 27 coordinates (optionally content-normalized gauge)
    v27 = []
    for i in range(27):
        e = sum(Rational(W[a][i].numerator, W[a][i].denominator)
                * col[a].as_expr() for a in range(len(W)) if W[a][i])
        v27.append(Poly(sp.rem(sp.expand(e), hx, x), x))
    gauge_scale = sp.Integer(1)
    if normalize:
        allc = [sp.Rational(c) for p in v27 for c in p.all_coeffs()
                if c != 0]
        den = 1
        for c in allc:
            den = sp.ilcm(den, c.q)
        num = 0
        for c in allc:
            num = sp.igcd(num, abs((c * den).p))
        gauge_scale = sp.Rational(den, num)
        v27 = [Poly(sp.expand(p.as_expr() * gauge_scale), x) for p in v27]
    if conj_data is not None:
        vbar27 = [compose_t(p) for p in v27]
    else:
        vbar27 = v27

    def form(cb):
        e = 0
        for b in range(27):
            a = piW[b]
            if cb[b] == 0:
                continue
            pa, pb = vbar27[a], v27[b]
            if pa.is_zero or pb.is_zero:
                continue
            e += cb[b] * pa.as_expr() * pb.as_expr()
        return Poly(sp.rem(sp.expand(e), hx, x), x)

    cb_tw = [cbP[b] * D2[b] for b in range(27)]
    cb_fl = [cbP[b] if D2[b] == -1 else 0 for b in range(27)]
    Q = form(cbP)
    Qtw = form(cb_tw)
    Qfl = form(cb_fl)
    CHK(f"{tag}_Qtw_equals_Q_minus_2Qflip",
        sp.expand(Qtw.as_expr() - Q.as_expr() + 2 * Qfl.as_expr()) == 0)
    rec = {"column": colj, "h": [str(c) for c in hpoly.all_coeffs()],
           "conjugation_t": str(tpoly), "gauge_scale": str(gauge_scale)}

    out = {}
    for nm, P in (("Q", Q), ("Qtw", Qtw), ("Qflip", Qfl)):
        cont, prim = P.primitive()
        flist = sp.factor_list(prim.as_expr())
        facs_ = []
        for f, m in flist[1]:
            fp = Poly(f, x)
            rf = sp.Rational(resultant(hx, fp.as_expr(), x))
            facs_.append({
                "factor": str(fp.as_expr()), "mult": int(m),
                "disc": ffac(sp.Rational(discriminant(fp.as_expr(), x)).p)
                if fp.degree() >= 2 else None,
                "Res_h_factor": {"num": ffac(rf.p), "den": ffac(rf.q)}})
        rq = sp.Rational(resultant(hx, P.as_expr(), x))
        out[nm] = {"poly": str(P.as_expr()), "content": str(cont),
                   "content_num_fac": ffac(sp.Rational(cont).p),
                   "content_den_fac": ffac(sp.Rational(cont).q),
                   "primitive_factors": facs_,
                   "Res_num_fac": ffac(rq.p), "Res_den_fac": ffac(rq.q)}
    rec["forms"] = out

    lc = int(hpoly.LC())

    def NK(P):
        r = sp.Rational(resultant(hx, P.as_expr(), x))
        return r / sp.Integer(lc) ** P.degree()

    Nq, Nqtw, Nqfl = NK(Q), NK(Qtw), NK(Qfl)
    rec["N_q"] = {"num": ffac(Nq.p), "den": ffac(Nq.q)}
    rec["N_qtw"] = {"num": ffac(Nqtw.p), "den": ffac(Nqtw.q)}
    rec["N_qflip"] = {"num": ffac(Nqfl.p), "den": ffac(Nqfl.q)}
    Nd = Nqtw / Nq
    rec["N_d"] = str(Nd)

    # per-coordinate resultants; per-minor only on the 3x3 block (which
    # minor births what -- the A-side raw minors are astronomically tall
    # and the coordinate resultants already answer the question there)
    coords = {}
    for b in range(27):
        if v27[b].is_zero:
            continue
        rb = sp.Rational(resultant(hx, v27[b].as_expr(), x))
        coords[str(b)] = {"num": ffac(rb.p), "den": ffac(rb.q),
                          "has953": has953(ffac(rb.p)) or has953(ffac(rb.q))}
    rec["coordinate_resultants"] = coords
    if n_ <= 3:
        minors = {}
        for i in range(n_):
            for j in range(n_):
                pij = Poly(adj[i, j], x)
                if pij.is_zero:
                    continue
                rij = sp.Rational(resultant(hx, pij.as_expr(), x))
                minors[f"{i},{j}"] = {"num": ffac(rij.p),
                                      "den": ffac(rij.q),
                                      "has953": has953(ffac(rij.p))}
        rec["adjugate_minor_resultants"] = minors

    dinv = sp.invert(Q.as_expr(), hx, x)
    dx = sp.rem(sp.expand(Qtw.as_expr() * dinv), hx, x)
    mx = sp.rem(sp.expand(Qfl.as_expr() * dinv), hx, x)

    def minpoly_of(px):
        """minpoly via the multiplication matrix of px in Q[x]/(h)."""
        deg = hpoly.degree()
        cols = []
        for k in range(deg):
            w = Poly(sp.rem(sp.expand(px * x ** k), hx, x), x)
            cc = [sp.Rational(0)] * deg
            for k2, c in enumerate(reversed(w.all_coeffs())):
                cc[k2] = sp.Rational(c)
            cols.append(cc)
        Mm = sp.Matrix(deg, deg, lambda i, j: cols[j][i])
        cpz = Mm.charpoly(y).as_expr()
        cand = None
        for f, m in sp.factor_list(cpz)[1]:
            fp = Poly(f, y)
            if fp.degree() >= 1 and (cand is None
                                     or fp.degree() < cand.degree()):
                cand = fp
        # certificate: cand(px) = 0 mod h
        csc = list(reversed(cand.all_coeffs()))
        acc = sp.Integer(0)
        pw = sp.Integer(1)
        for c in csc:
            acc = acc + sp.Rational(c) * pw
            pw = sp.rem(sp.expand(pw * px), hx, x)
        if sp.rem(sp.expand(acc), hx, x) != 0:
            raise RuntimeError("minpoly certificate failed")
        ints = [sp.Rational(c) for c in cand.all_coeffs()]
        den = 1
        for c in ints:
            den = sp.ilcm(den, c.q)
        ints = [int(c * den) for c in ints]
        g = 0
        for c in ints:
            g = sp.igcd(g, abs(c))
        ints = [c // g for c in ints]
        if ints[0] < 0:
            ints = [-c for c in ints]
        return ints

    rec["d_minpoly"] = minpoly_of(dx)
    rec["m_minpoly"] = minpoly_of(mx)
    return rec, Nd, dx, mx


# ================================================================ [3] S trace
log("[3] the S-family trace over Q[x]/(h_S) ...")
recS, NdS, dxS, mxS = sym_trace(C_S, h_S, W3, "S")
CHK("S_d_minpoly_equals_banked_B916", recS["d_minpoly"] == MPS_banked,
    str(recS["d_minpoly"]))
CHK("S_m_minpoly_equals_banked_B928", recS["m_minpoly"] == mpmS_banked,
    str(recS["m_minpoly"]))
CHK("S_norm_law", NdS == -Rational(953, 2304) ** 2, str(NdS))
# the junk identification: N(q_S) = -disc(h_S)^2 in the adjugate gauge
dscS = sp.Rational(discriminant(h_S.as_expr(), x))
NqS = sp.Rational(1)
for p_, e_ in recS["N_q"]["num"].items():
    NqS *= sp.Integer(p_) ** e_
CHK("S_Nq_equals_minus_disc_hS_squared", NqS == -dscS ** 2,
    "the adjugate-gauge norm of the H+-value is the discriminant squared")
RES["S_trace"] = recS
dump()

# ================================================================ [4] A trace
log("[4] the A-family trace over Q[x]/(h_A), sesquilinear ...")
recA, NdA, dxA, mxA = sym_trace(C_A, h_A, W6, "A", conj_data=(CE6, CO6),
                                normalize=True)
CHK("A_d_minpoly_equals_banked_B916", recA["d_minpoly"] == MPA_banked,
    str(recA["d_minpoly"]))
CHK("A_m_minpoly_equals_banked_B928", recA["m_minpoly"] == mpmA_banked,
    str(recA["m_minpoly"]))
CHK("A_norm_law_L_over_Q_is_square_of_K_norm",
    NdA == Rational(953, 2304) ** 4, str(NdA))
# junk-structure probe: is N(q_A) = (2304-part) * (rational square) *
# disc-related content?  record |N(q_A)| / disc(h_A)^2 square-ness
NqA = sp.Rational(1)
for p_, e_ in recA["N_q"]["num"].items():
    if p_ == "-1":
        NqA *= -1
    elif p_.startswith("C"):
        NqA *= sp.Integer(p_.split(":")[1]) ** e_
    else:
        NqA *= sp.Integer(p_) ** e_
for p_, e_ in recA["N_q"]["den"].items():
    if p_.startswith("C"):
        NqA /= sp.Integer(p_.split(":")[1]) ** e_
    else:
        NqA /= sp.Integer(p_) ** e_
dscA = sp.Rational(discriminant(h_A.as_expr(), x))
ratio_junk = sp.Rational(abs(NqA)) / dscA ** 2
REC("A_Nq_over_discA_sq_is_square",
    bool(sp.integer_nthroot(abs(sp.Rational(ratio_junk).p), 2)[1]
         and sp.integer_nthroot(abs(sp.Rational(ratio_junk).q), 2)[1]),
    "the A-side junk = disc(h_A)^2 x a rational square (gauge^2)")
RES["A_trace"] = recA
dump()

# ================================================================ [5] blocks
log("[5] the rational block lattices and their H/H' Grams ...")
Hm = sp.zeros(27, 27)
Hpm = sp.zeros(27, 27)
for b in range(27):
    Hm[piW[b], b] = cbP[b]
    Hpm[piW[b], b] = cbP[b] * D2[b]
CHK("H_and_Hprime_symmetric", Hm.T == Hm and Hpm.T == Hpm)


def latt(P):
    cs = [Fr(sp.Rational(c).p, sp.Rational(c).q) for c in P.all_coeffs()]
    ker = qkernel(poly_mat(cs))
    Bm = sp.Matrix([[Rational(e.numerator, e.denominator) for e in v]
                    for v in ker])
    Rr, _ = Bm.rref()
    rows = []
    for i in range(Rr.rows):
        r = list(Rr.row(i))
        den = sp.ilcm(*[sp.Rational(e).q for e in r])
        r = [sp.Integer(sp.Rational(e) * den) for e in r]
        g = 0
        for e in r:
            g = sp.igcd(g, abs(e))
        rows.append([e // g for e in r])
    return sp.Matrix(rows)


L3 = latt(h_S)
L6 = latt(h_A)
L18 = latt(h_col)
CHK("lattice_dims", L3.rows == 3 and L6.rows == 6 and L18.rows == 18)
blocks = {}
for nm, L in (("L3", L3), ("L6", L6), ("L18", L18)):
    G = L * Hm * L.T
    Gp = L * Hpm * L.T
    dG, dGp = G.det(), Gp.det()
    ent = {"detG_fac": ffac(dG), "detGp_fac": ffac(dGp),
           "ratio": str(sp.Rational(dGp, dG))}
    if nm == "L3":
        ent["G"] = [[str(G[i, j]) for j in range(3)] for i in range(3)]
        ent["Gp"] = [[str(Gp[i, j]) for j in range(3)] for i in range(3)]
        X3 = G.inv() * Gp
        ent["X3_charpoly"] = str(X3.charpoly(x).as_expr())
    if nm == "L6":
        X6 = G.inv() * Gp
        ent["X6_charpoly"] = str(X6.charpoly(x).as_expr())
    blocks[nm] = ent
cross = {}
for (na, La), (nb, Lb) in itertools.combinations(
        [("L3", L3), ("L6", L6), ("L18", L18)], 2):
    cross[f"{na}-{nb}"] = {
        "H_orthogonal": bool((La * Hm * Lb.T).is_zero_matrix),
        "Hprime_orthogonal": bool((La * Hpm * Lb.T).is_zero_matrix)}
blocks["cross_pairings"] = cross
CHK("H_blocks_mutually_orthogonal",
    all(v["H_orthogonal"] for v in cross.values()))
CHK("Hprime_recouples_W3_W6",
    not cross["L3-L6"]["Hprime_orthogonal"]
    and cross["L3-L18"]["Hprime_orthogonal"]
    and cross["L6-L18"]["Hprime_orthogonal"],
    "the D2 twist connects the vacuum 3-space to the A-block -- "
    "rationally, the colorless 9-space is the twist's smallest closed world")
# the colorless 9-lattice: det ratio must be exactly -1 (D2 det = -1,
# W18 ratio = +1, W9 perp W18 in both forms)
L9 = latt(Poly(sp.expand(h_S.as_expr() * h_A.as_expr()), x))
G9 = L9 * Hm * L9.T
G9p = L9 * Hpm * L9.T
blocks["L9"] = {"detG_fac": ffac(G9.det()), "detGp_fac": ffac(G9p.det()),
                "ratio": str(sp.Rational(G9p.det(), G9.det()))}
CHK("L9_det_ratio_minus_1", sp.Rational(G9p.det(), G9.det()) == -1)
CHK("L18_det_ratio_plus_1",
    sp.Rational(sp.Integer(1), 1)
    == sp.Rational((L18 * Hpm * L18.T).det(), (L18 * Hm * L18.T).det()))
CHK("no_953_in_any_block_gram_det",
    not any(has953(blocks[nm]["detG_fac"]) or has953(blocks[nm]["detGp_fac"])
            for nm in ("L3", "L6", "L18", "L9")),
    "the rational/bilinear world is 953-blind")
RES["rational_blocks"] = blocks
dump()

# ================================================================ [6] whitelist
log("[6] the declared whitelist sweep (W-A .. W-G) ...")
mpdS = Poly(MPS_banked, x)
mpdA = Poly(MPA_banked, x)
mpmS = Poly(mpmS_banked, x)
mpmA = Poly(mpmA_banked, x)
POLYS = {"mu13": mu_poly, "h_S": h_S, "h_A": h_A, "h_col": h_col,
         "HIER": hier_poly, "mp_dS": mpdS, "mp_dA": mpdA,
         "mp_mS": mpmS, "mp_mA": mpmA, "e1_colored": Poly(E1MP, x),
         "e3_colored": Poly(E3MP, x)}
WA = {}
for nm, P in POLYS.items():
    d_ = sp.Rational(discriminant(P.as_expr(), x))
    WA[nm] = {"disc_num_fac": ffac(d_.p), "disc_den_fac": ffac(d_.q),
              "lead_fac": ffac(int(sp.Rational(P.LC()))),
              "const_fac": ffac(sp.Rational(P.all_coeffs()[-1]).p),
              "disc_has_953": has953(ffac(d_.p)) or has953(ffac(d_.q))}
RES["W_A_discriminants"] = WA
CORE = ["mu13", "h_S", "h_A", "h_col", "HIER"]
WB = {}
for a_, b_ in itertools.combinations(CORE, 2):
    r = sp.Rational(resultant(POLYS[a_].as_expr(), POLYS[b_].as_expr(), x))
    WB[f"Res({a_},{b_})"] = {"num": ffac(r.p), "den": ffac(r.q),
                             "has_953": has953(ffac(r.p))}
RES["W_B_pairwise_resultants"] = WB
PTS = [0, 1, -1, 2, -2, 3, -3, Rational(1, 2), Rational(-1, 2),
       Rational(1, 3), Rational(-1, 3), Rational(2, 3), Rational(-2, 3),
       Rational(3, 2), Rational(-3, 2), 6, -6, Rational(1, 6),
       Rational(-1, 6), 13, -13, Rational(1, 13), Rational(-1, 13)]
WC = {}
for nm in ["mu13", "h_S", "h_A", "h_col"]:
    P = POLYS[nm]
    hits = {}
    for t in PTS:
        val = sp.Rational(P.as_expr().subs(x, t))
        if val == 0:
            continue
        fac = {"num": ffac(val.p), "den": ffac(val.q)}
        if has953(fac["num"]) or has953(fac["den"]):
            hits[str(t)] = fac
    WC[nm] = hits if hits else "no 953 at any declared point"
RES["W_C_distinguished_values"] = WC
G4 = [[sum(Rex[m_][i][j] * Rex[n_][j][i] for i in range(27)
           for j in range(27)) for n_ in ns] for m_ in ns]
detG4 = sp.Matrix(4, 4, lambda i, j: Rational(G4[i][j].numerator,
                                              G4[i][j].denominator)).det()
RES["W_D_trace_gram"] = {
    "entries": [[str(G4[i][j]) for j in range(4)] for i in range(4)],
    "det": str(detG4),
    "det_num_fac": ffac(sp.Rational(detG4).p),
    "det_den_fac": ffac(sp.Rational(detG4).q),
    "has_953": "953" in json.dumps(
        [ffac(sp.Rational(detG4).p)]
        + [ffac(Fr(G4[i][j]).numerator) for i in range(4) for j in range(4)
           if Fr(G4[i][j]).denominator == 1])}
WF = {}
for a_, b_ in [("mp_dS", "mp_dA"), ("mp_mS", "mp_mA")]:
    r = sp.Rational(resultant(POLYS[a_].as_expr(), POLYS[b_].as_expr(), x))
    WF[f"Res({a_},{b_})"] = {"num": ffac(r.p), "den": ffac(r.q),
                             "has_953": has953(ffac(r.p))}
RES["W_F_twist_separations"] = WF
dump()

# ---- W-G: the field K, its discriminant, index, and the declared primes
log("[6b] W-G: disc(K), index, splitting of the declared primes ...")
from sympy.polys.numberfields.basis import round_two
ZK_S, dK = round_two(h_S)
idx2 = sp.Rational(dscS, dK)
CHK("disc_K_times_index_sq_is_disc_hS", idx2.q == 1
    and sp.sqrt(idx2).is_integer, f"disc(K) = {dK} = {ffac(dK)}")
REC("disc_K", f"{dK} = {ffac(dK)}",
    "the field discriminant of K (round_two on monic h_S)")
REC("index_Z_thetaS_in_OK", str(sp.sqrt(idx2)),
    str(ffac(int(sp.sqrt(idx2)))))
KF = sp.QQ.alg_field_from_poly(h_S)
# the monic mu13 model (also used in [7]); built here for the fallback
A_mu = MU[0]
T_mu = Poly([1, MU[1], MU[0] * MU[2], MU[0] ** 2 * MU[3]], y)
KFmu = sp.QQ.alg_field_from_poly(T_mu)
PRIMES_DECL = [2, 3, 5, 7, 11, 13, 17, 19, 29, 953, 1129, 421493,
               72869, 20417473]
CHK("flip_mass_primes_are_prime",
    sp.isprime(20417473) and sp.isprime(72869) and sp.isprime(29)
    and 29 * 72869 == 2113201,
    "N(m_S)-numerator 20417473 prime; N(m_A)-numerator = 29 * 72869")
WG = {}
for p_ in PRIMES_DECL:
    pat = None
    for Kmodel in (KF, KFmu):
        try:
            pat = sorted([(P.e, P.f) for P in Kmodel.primes_above(p_)])
            break
        except Exception:
            continue
    if pat is None:
        # sympy prime_decomp edge case (both models); for UNRAMIFIED p
        # the S3-resolvent theorem decides: jacobi(dK, p) = -1 <=> the
        # Frobenius is a transposition <=> pattern [1,2]
        if p_ % 2 == 1 and dK % p_ != 0 \
                and sp.jacobi_symbol(dK, p_) == -1:
            pat = [(1, 1), (1, 2)]
            pat = {"pattern": str(pat),
                   "method": "resolvent theorem (jacobi(dK,p) = -1 => "
                             "transposition Frobenius => [1,2]); sympy "
                             "prime_decomp edge case in both models"}
        else:
            pat = "sympy prime_decomp failed in both models; " \
                  "pattern not determined by the resolvent alone"
    WG[str(p_)] = pat
RES["W_G_splitting_in_K"] = {k: str(v) for k, v in WG.items()}
REC("W_G_splitting", RES["W_G_splitting_in_K"])
# quadratic-resolvent symbols: the [1,2] pattern <=> kronecker(dK, p) = -1
import sympy.ntheory as nt
RES["W_G_resolvent_symbols"] = {
    str(p_): int(sp.jacobi_symbol(dK, p_))
    for p_ in [953, 2, 1129, 421493, 20417473] if p_ % 2 == 1}
dump()

# ================================================================ [7] divisors
log("[7] the divisor map: valuations of d and m at every place over "
    "{2,3,953} (+ flip-mass primes), h_S model + mu13 cross-model gate ...")
ZKmod = KF.maximal_order()
PB = ZKmod.parent


def elt_from_coeffs(cs):
    """cs = rational coeffs of 1, theta, theta^2 -> (integral elt, den)."""
    den = 1
    for c in cs:
        den = sp.ilcm(den, sp.Rational(c).q)
    ints = [int(sp.Rational(c) * den) for c in cs]
    pol = Poly(list(reversed(ints)), x)   # ascending -> Poly descending
    return PB.element_from_poly(pol), den


def divisor_of(px, label, primes):
    """px = polynomial rep (in theta_S) of an element z of K; full
    valuation table of z at every place over the given primes."""
    cs = [0, 0, 0]
    pp = Poly(sp.expand(px), x)
    for k, c in enumerate(reversed(pp.all_coeffs())):
        cs[k] = sp.Rational(c)
    elt, den = elt_from_coeffs(cs)
    I = elt * ZKmod
    tab = {}
    vsum = {}
    for p_ in primes:
        for i_, P in enumerate(KF.primes_above(p_)):
            vP = int(P.valuation(I) - P.e * sp.multiplicity(p_, den))
            tab[f"p={p_}#{i_} (e={P.e},f={P.f})"] = vP
            vsum[p_] = vsum.get(p_, 0) + P.f * vP
    # norm cross-check: multiplication matrix of z mod h_S
    cols = []
    for k in range(3):
        w = sp.rem(sp.expand(pp.as_expr() * x ** k), h_S.as_expr(), x)
        wp = Poly(w, x)
        cc = [0, 0, 0]
        for k2, c in enumerate(reversed(wp.all_coeffs())):
            cc[k2] = sp.Rational(c)
        cols.append(cc)
    Nz = sp.Matrix(3, 3, lambda i, j: cols[j][i]).det()
    ok = all(vsum[p_] == sp.multiplicity(p_, sp.Rational(Nz).p)
             - sp.multiplicity(p_, sp.Rational(Nz).q) for p_ in primes)
    CHK(f"divisor_{label}_norm_consistency", ok,
        f"N({label}) = {sp.Rational(Nz)}")
    return tab, sp.Rational(Nz)


DIV = {}
tab, Nd_ = divisor_of(dxS, "d_S", [2, 3, 953])
DIV["d_S"] = {"valuations": tab, "norm": str(Nd_)}
CHK("d_S_norm_recheck", Nd_ == -Rational(953, 2304) ** 2)
tab, Nm_ = divisor_of(mxS, "m_S", [2, 3, 953, 20417473])
DIV["m_S"] = {"valuations": tab, "norm": str(Nm_)}
# d_A, m_A live in K too but were computed in the h_A model; bring them in
# through the banked B928 K-coordinates (mu13/rho basis), cross-model gated:
# rho as an element of the h_S model is NOT needed -- instead verify the
# banked coords reproduce the SAME minpolys my trace derived, then use the
# monic mu13 model (y = lc*rho) for their valuations.
A_mu = MU[0]
T_mu = Poly([1, MU[1], MU[0] * MU[2], MU[0] ** 2 * MU[3]], y)
CHK("monic_mu_model_correct",
    sp.expand(T_mu.as_expr().subs(y, A_mu * x) - A_mu ** 2
              * mu_poly.as_expr()) == 0,
    "T_mu(y) = y^3 + B y^2 + A C y + A^2 D, y = A rho")
KFmu = sp.QQ.alg_field_from_poly(T_mu)
ZKmu = KFmu.maximal_order()
PBmu = ZKmu.parent
_, dKmu = round_two(T_mu)
CHK("mu_model_same_field_disc", dKmu == dK,
    f"disc = {dKmu} in both models -- same field K")


def kcoords_to_mupoly(kc):
    """(c0,c1,c2) in basis 1,rho,rho^2 -> polynomial in y (rho = y/A)."""
    return sp.expand(sp.Rational(kc[0]) + sp.Rational(kc[1]) * y / A_mu
                     + sp.Rational(kc[2]) * y ** 2 / A_mu ** 2)


def divisor_mu(py, label, primes):
    pp = Poly(sp.rem(sp.expand(py), T_mu.as_expr(), y), y)
    cs = [0, 0, 0]
    for k, c in enumerate(reversed(pp.all_coeffs())):
        cs[k] = sp.Rational(c)
    den = 1
    for c in cs:
        den = sp.ilcm(den, c.q)
    ints = [int(c * den) for c in cs]
    elt = PBmu.element_from_poly(Poly(list(reversed(ints)), y))
    I = elt * ZKmu
    tab = {}
    vsum = {}
    for p_ in primes:
        for i_, P in enumerate(KFmu.primes_above(p_)):
            vP = int(P.valuation(I) - P.e * sp.multiplicity(p_, den))
            tab[f"p={p_}#{i_} (e={P.e},f={P.f})"] = vP
            vsum[p_] = vsum.get(p_, 0) + P.f * vP
    cols = []
    for k in range(3):
        w = sp.rem(sp.expand(pp.as_expr() * y ** k), T_mu.as_expr(), y)
        wp = Poly(w, y)
        cc = [0, 0, 0]
        for k2, c in enumerate(reversed(wp.all_coeffs())):
            cc[k2] = sp.Rational(c)
        cols.append(cc)
    Nz = sp.Matrix(3, 3, lambda i, j: cols[j][i]).det()
    ok = all(vsum[p_] == sp.multiplicity(p_, sp.Rational(Nz).p)
             - sp.multiplicity(p_, sp.Rational(Nz).q) for p_ in primes)
    CHK(f"divisor_{label}_norm_consistency", ok,
        f"N({label}) = {sp.Rational(Nz)}")
    return tab, sp.Rational(Nz)


def minpoly_mu(py):
    pp = sp.rem(sp.expand(py), T_mu.as_expr(), y)
    Rz = Poly(resultant(T_mu.as_expr(), x - pp, y), x)
    cand = None
    for f, m in sp.factor_list(Rz.as_expr())[1]:
        fp = Poly(f, x)
        if fp.degree() >= 1 and (cand is None
                                 or fp.degree() < cand.degree()):
            cand = fp
    ints = [sp.Rational(c) for c in cand.all_coeffs()]
    den = 1
    for c in ints:
        den = sp.ilcm(den, c.q)
    ints = [int(c * den) for c in ints]
    g = 0
    for c in ints:
        g = sp.igcd(g, abs(c))
    ints = [c // g for c in ints]
    if ints[0] < 0:
        ints = [-c for c in ints]
    return ints


mS_mu = kcoords_to_mupoly(mS_K)
mA_mu = kcoords_to_mupoly(mA_K)
V_mu = kcoords_to_mupoly(V_K)
CHK("cross_model_gate_mS", minpoly_mu(mS_mu) == mpmS_banked,
    "banked B928 K-coords reproduce THIS cell's independently derived "
    "flip-mass minpoly -- the coordinates are trusted after this gate")
CHK("cross_model_gate_mA", minpoly_mu(mA_mu) == mpmA_banked)
dS_mu = sp.expand(1 - 2 * mS_mu)
dA_mu = sp.expand(1 - 2 * mA_mu)
CHK("cross_model_gate_dS", minpoly_mu(dS_mu) == MPS_banked)
CHK("cross_model_gate_dA", minpoly_mu(dA_mu) == MPA_banked)
tab, Nz = divisor_mu(dS_mu, "d_S_mu_model", [2, 3, 953])
DIV["d_S_mu_model"] = {"valuations": tab, "norm": str(Nz)}
tab, Nz = divisor_mu(dA_mu, "d_A", [2, 3, 953])
DIV["d_A"] = {"valuations": tab, "norm": str(Nz)}
CHK("d_A_norm_recheck", Nz == -Rational(953, 2304) ** 2)
tab, Nz = divisor_mu(mA_mu, "m_A", [2, 3, 29, 72869])
DIV["m_A"] = {"valuations": tab, "norm": str(Nz)}
tab, Nz = divisor_mu(V_mu, "V_hierarchy", [2, 3, 953, 1129, 421493])
DIV["V_hierarchy"] = {"valuations": tab, "norm": str(Nz)}
v953 = {k: v for k, v in tab.items() if k.startswith("p=953")}
CHK("V_pole_reproduces_B918_observer_place",
    sorted((int(k.split("f=")[1].rstrip(")")), v)
           for k, v in v953.items()) == [(1, -4), (2, 0)],
    "den(V) = P1(953)^4, deg-1 place only -- B918 banked, re-derived here")
RES["divisor_map"] = DIV
dump()

# ================================================================ [8] synthesis
log("[8] synthesis: the 953/2304 provenance map ...")
sites = []
for side in ("S_trace", "A_trace"):
    for nm, f in RES[side]["forms"].items():
        for key in ("Res_num_fac", "Res_den_fac",
                    "content_num_fac", "content_den_fac"):
            if has953(f[key]):
                sites.append(f"{side}.{nm}.{key}")
        for fa in f["primitive_factors"]:
            rf = fa["Res_h_factor"]
            if has953(rf["num"]) or has953(rf["den"]):
                sites.append(f"{side}.{nm}.Res(h, {fa['factor'][:48]}...)")
    coord_hits = [b for b, v in RES[side]["coordinate_resultants"].items()
                  if v["has953"]]
    minor_hits = [k for k, v in RES[side]
                  .get("adjugate_minor_resultants", {}).items()
                  if v["has953"]]
    sites += [f"{side}.coordinate[{b}]" for b in coord_hits]
    sites += [f"{side}.adjugate_minor[{k}]" for k in minor_hits]
for grp in ("W_A_discriminants", "W_B_pairwise_resultants",
            "W_C_distinguished_values", "W_D_trace_gram",
            "W_F_twist_separations"):
    blob = json.dumps(RES[grp])
    if '"953"' in blob:
        sites.append(grp + " (see detail)")
RES["sites_953"] = sites
REC("sites_where_953_appears", sites)
REC("verdict_2304",
    "2304^2 = 2^16 3^4 = the exact {2,3}-part of lc(mu13) "
    "(lc = 2304^2 * 5^2 * 7^3 * 11); at ideal level the 2304-denominator "
    "of d is the divisor table's negative part over 2 and 3")
RES["verdict"] = "COMPLETE (see DRAFT_FINDINGS.md)"
dump()
log("done.")
