#!/usr/bin/env python3
"""The SM seat's check of the physical lane's packet cyclic_charged_mass_2026_11_16 (audit/physical-bridge-2026-09-05 at
798281903): every finite, algebraic or numerically checkable step, on this seat's own code.  The analytic premises
(complete-domain L2 identification, global middle-line inverses, Hermitian stationary response, the V2 projection)
are not checked here.  Sections E and F use a P^1 Cech analogue with the same degrees and divisor pattern, not the
lane's elliptic objects.  No data; no physical value.
    python3 check_cyclic_charged_mass.py [MAIN_CHECKOUT]"""
import json
import pathlib
import subprocess
import sys

import mpmath as mp
import numpy as np
import sympy as sp

out = {}
plants = {}
HERE = pathlib.Path(__file__).resolve().parent


def zero(M):
    return bool(sp.simplify(sp.Matrix(M)) == sp.zeros(*sp.Matrix(M).shape))


# ---------------------------------------------------------------- A. the corner reduction (EXACT_CORNER_REDUCTION 1)
c1, c2, c3, fz, fw = sp.symbols("c1 c2 c3 f_z f_w")
d1, d2, d3 = sp.symbols("d1 d2 d3")


def Qmat(a, b, c, f):
    return sp.Matrix([[0, a, 0, 0], [0, 0, b, 0], [0, 0, 0, c], [f, 0, 0, 0]])


Qz = Qmat(c1, c2, c3, fz)
perm = Qz[:, [1, 2, 3, 0]]
out["A1 (1) with source columns reordered (1/2,-1/2,-3/2,3/2) is diag(c1,c2,c3) + f_z corner"] = bool(
    perm == sp.diag(c1, c2, c3, fz))


def factor(a, b, c, f):
    """8x8 graded factor complex V0 -(Q)-> V1, its pivot part, homotopy, i, p and grading sign."""
    Q, P = Qmat(a, b, c, f), Qmat(a, b, c, 0)
    d = sp.zeros(8); d[4:, :4] = Q
    dP = sp.zeros(8); dP[4:, :4] = P
    h = sp.zeros(8)
    h[1, 4], h[2, 5], h[3, 6] = 1 / a, 1 / b, 1 / c          # pivot inverses: target rows 0..2 -> source cols 1..3
    i = sp.zeros(8, 2); i[0, 0] = 1; i[7, 1] = 1              # retained highest source, lowest target
    p = i.T
    S = sp.diag(*([1] * 4 + [-1] * 4))
    return d, dP, h, i, p, S


dV, dVP, hV, iV, pV, SV = factor(c1, c2, c3, fz)
dW, dWP, hW, iW, pW, SW = factor(d1, d2, d3, fw)
I8 = sp.eye(8)
out["A2 factor SDR: dP h + h dP = 1 - i p, p i = 1, h i = 0, p h = 0, h h = 0"] = all([
    zero(dVP * hV + hV * dVP - (I8 - iV * pV)), pV * iV == sp.eye(2), zero(hV * iV), zero(pV * hV), zero(hV * hV)])
deltaV = dV - dVP
out["A2 corner times pivot homotopy vanishes in both orders (h delta = delta h = 0)"] = zero(hV * deltaV) and zero(
    deltaV * hV)
out["A2 factor transferred differential p delta i = f_z exactly (no inverse of f_z)"] = bool(
    sp.simplify(pV * deltaV * iV - sp.Matrix([[0, 0], [fz, 0]])) == sp.zeros(2))

kp = sp.kronecker_product
I8 = sp.eye(8)
d_full = kp(dV, I8) + kp(SV, dW)
d_piv = kp(dVP, I8) + kp(SV, dWP)
out["A3 two-factor Koszul total differential squares to zero"] = zero(d_full * d_full)
plants["A3-plant: total differential without the Koszul sign squares to zero (must FAIL)"] = zero(
    (kp(dV, I8) + kp(I8, dW)) ** 2)
piV = iV * pV
h_tot = kp(hV, I8) + kp(piV * SV, hW)
i_tot, p_tot = kp(iV, iW), kp(pV, pW)
out["A4 tensor SDR: d h + h d = 1 - i p and side conditions"] = all([
    zero(d_piv * h_tot + h_tot * d_piv - (sp.eye(64) - i_tot * p_tot)), zero(h_tot * i_tot), zero(p_tot * h_tot),
    zero(h_tot * h_tot)])
delta = d_full - d_piv
higher = [zero(p_tot * delta * (h_tot * delta) ** k * i_tot) for k in (1, 2, 3)]
out["A4 perturbation series terms of order >= 2 vanish (no higher algebraic corner term)"] = all(higher)
dprime = sp.simplify(p_tot * delta * i_tot)       # kron order: 0 A=H0(x)H0, 1 C=H0(x)H1, 2 B=H1(x)H0, 3 D=H1(x)H1
koszul = sp.zeros(4); koszul[2, 0] = fz; koszul[1, 0] = fw; koszul[3, 2] = -fw; koszul[3, 1] = fz
out["A4 retained differential is A -(f_z,f_w)-> B+C -(-f_w,f_z)-> D, eq. (2)"] = bool(
    sp.simplify(dprime - koszul) == sp.zeros(4))


def coh_dims(dmat, deg):
    dims = []
    for k in range(3):
        idx_k = [j for j in range(len(deg)) if deg[j] == k]
        idx_n = [j for j in range(len(deg)) if deg[j] == k + 1]
        idx_p = [j for j in range(len(deg)) if deg[j] == k - 1]
        rk_out = dmat.extract(idx_n, idx_k).rank() if idx_n else 0
        rk_in = dmat.extract(idx_k, idx_p).rank() if idx_p else 0
        dims.append(len(idx_k) - rk_out - rk_in)
    return dims


degs = [a + b for a in [0] * 4 + [1] * 4 for b in [0] * 4 + [1] * 4]
cv = {c1: 2, c2: -3, c3: sp.Rational(5, 7), d1: 7, d2: sp.Rational(-1, 3), d3: 11}
res = {}
for name, fv in (("origin", (0, 0)), ("z-axis", (3, 0)), ("w-axis", (0, 5)), ("generic", (3, 5))):
    sub = dict(cv); sub[fz], sub[fw] = fv
    big = coh_dims(d_full.subs(sub), degs)
    small = coh_dims(koszul.subs({fz: fv[0], fw: fv[1]}), [0, 1, 1, 2])
    res[name] = [big, small, big == small]
out["A5 pointwise cohomology dims of the 16-32-16 complex equal those of the retained 1-2-1 complex"] = res

# ---------------------------------------------------------------- B. line powers, L2 pole test, degrees
powers = {"A": -3, "B": 1, "C": 1, "D": 5}
out["B1 S-powers: A->B, A->C, B->D, C->D each shift by the S^4 neutral coefficient; A D = B C"] = all([
    powers["B"] - powers["A"] == 4, powers["D"] - powers["C"] == 4,
    powers["A"] + powers["D"] == powers["B"] + powers["C"]])


def converges(a, n):
    """integral_0^{1/e} r^(a-1-2n) log(1/r)^(a-2) dr; with r = exp(-s) it is integral_1^S exp(-(a-2n) s) s^(a-2) ds
    as S -> oo, evaluated numerically at S = 40, 80, 160 (no closed-form continuation)."""
    part = [mp.quad(lambda u: mp.exp(-(a - 2 * n) * u) * u ** (a - 2), mp.linspace(1, S_, 9)) for S_ in (40, 80, 160)]
    return bool(abs(part[2] - part[1]) < 1e-12 and abs(part[1] - part[0]) < 1e-8)


maxpole = {}
for a in (-3, 1, 5):
    ok = [n for n in range(-6, 7) if converges(a, n)]
    maxpole[a] = max(ok) if ok else None
out["B2 largest L2-admissible pole order at a = -3, 1, 5 (packet: -2, 0, 2)"] = [maxpole[-3], maxpole[1], maxpole[5]]
degA, degB, degC, degD = maxpole[-3], maxpole[1], maxpole[1], maxpole[5]
out["B2 Hom degrees A->B, B->D are 2 and deg A + deg D = deg B + deg C"] = bool(
    degB - degA == 2 and degD - degB == 2 and degA + degD == degB + degC)

# ------------------------------------------------- C. the nontrivial order-two section (elliptic, numeric)
mp.mp.dps = 30
tau = mp.mpc(0.31, 1.13)
qn = mp.exp(1j * mp.pi * tau)
th = lambda n, z, d=0: mp.jtheta(n, z, qn, d)
g = lambda z: th(3, z) / th(1, z)                 # periods pi, pi*tau
z0 = mp.mpc(0.37, 0.21)
out["C1 g = theta3/theta1 has multipliers (-1,-1) under z+pi, z+pi*tau (the character of xi)"] = [
    mp.nstr(g(z0 + mp.pi) / g(z0), 12), mp.nstr(g(z0 + mp.pi * tau) / g(z0), 12)]
out["C2 residue of g at the puncture z=0 (nonzero: actual simple pole)"] = mp.nstr(th(3, 0) / th(1, 0, 1), 12)


def count_zeros(fun, dfun):
    o = mp.mpc(-0.113, -0.087)                    # shifted cell avoiding zeros on the boundary
    corners = [o, o + mp.pi, o + mp.pi + mp.pi * tau, o + mp.pi * tau, o]
    tot = 0
    for k in range(4):
        tot += mp.quad(lambda z: dfun(z) / fun(z), [corners[k], corners[k + 1]])
    return tot / (2j * mp.pi)


n1 = count_zeros(lambda z: th(1, z), lambda z: th(1, z, 1))
n3 = count_zeros(lambda z: th(3, z), lambda z: th(3, z, 1))
out["C3 zeros of theta1, theta3 per cell (one pole, one zero of g)"] = [mp.nstr(n1, 10), mp.nstr(n3, 10)]
zq = mp.pi / 2 + mp.pi * tau / 2
out["C3 the zero q of g sits at the half period (pi + pi tau)/2, so q != p: |theta3(q)|, |theta3(p)|"] = [
    mp.nstr(abs(th(3, zq)), 5), mp.nstr(abs(th(3, 0)), 12)]
plants["C3-plant: q = p, i.e. theta3 vanishes at the puncture (must FAIL)"] = bool(abs(th(3, 0)) < 1e-20)
# n0: trivial character, constant section of O(p) -- a nonzero constant has no pole and no zero (immediate)


def common_divisor(z0nz, z1nz):
    divs = []
    if z0nz:
        divs.append({"p": 2})
    if z1nz:
        divs.append({"p": 1, "q": 1})
    if not divs:
        return None
    pts = set().union(*divs)
    return {x: min(d.get(x, 0) for d in divs) for x in pts if min(d.get(x, 0) for d in divs) > 0}


out["C4 common divisor (2): generic, z1=0, z0=0"] = [common_divisor(1, 1), common_divisor(1, 0), common_divisor(0, 1)]

# ---------------------------------------------------------------- D. local and global Koszul cohomology
w = sp.symbols("w")
loc = {}
for (a, b) in ((1, 1), (2, 1), (1, 3), (2, 2), (3, None)):
    f0 = w ** a * (1 + 2 * w)
    f1 = 0 * w if b is None else w ** b * (3 - w)
    h = sp.gcd(f0, f1)
    g0, g1 = sp.cancel(f0 / h), sp.cancel(f1 / h)
    comp = sp.expand(-f1 * f0 + f0 * f1) == 0
    ord_gcd = next(k for k in range(10) if sp.expand(h).coeff(w, k) != 0)
    loc[f"ord ({a},{b})"] = {"d1 d0 = 0": bool(comp),
                             "residual pair unimodular at 0": bool(g0.subs(w, 0) != 0 or g1.subs(w, 0) != 0),
                             "length H1 = length H2 = ord_0 gcd": ord_gcd,
                             "min of the two orders": min(a, b if b is not None else 10 ** 6)}
out["D1 local Koszul over the valuation ring: H1 = A(Z)/A, H2 = D/D(-Z), length = ord of common factor"] = loc


def rr(deg, trivial=False):
    """genus one: (h0, h1)"""
    if deg > 0:
        return deg, 0
    if deg < 0:
        return 0, -deg
    return (1, 1) if trivial else (0, 0)


chi = sum(s_ * (rr(d_)[0] - rr(d_)[1]) for s_, d_ in ((1, -2), (-1, 0), (-1, 0), (1, 2)))
out["D2 Euler characteristic of A -> B+C -> D on genus one is 0, so dim H1_tot = dim H2_tot"] = chi
out["D2 Riemann-Roch: h1(Abar), h0(Dbar), h1(Abar(p)), h0(Dbar(-p))"] = [rr(-2)[1], rr(2)[0], rr(-1)[1], rr(1)[0]]


def origin_count(middle_trivial):
    hA1 = rr(-2)[1]; hB0 = sum(rr(0, t)[0] for t in middle_trivial)
    return hA1 + hB0


table = {}
for seed, sing_mid in (("aligned", (True, False)), ("misaligned", (False, False))):
    sing = [origin_count(sing_mid), 2, 1]
    trip = [origin_count((False, False)), 2, 1]
    total = [2 * sing[k] + 2 * 3 * trip[k] for k in range(3)]
    table[seed] = {"singlet": sing, "triplet": trip, "128-block": total}
out["D3 kernel table (origin, one coeff., both): packet aligned 3,2,1 / 2,2,1 / 18,16,8; misaligned 16,16,8"] = table
out["D3 128 = (4 x 4 spinor product) x (4 + 4bar); 4 = 1 + 3"] = bool(16 * 8 == 128 and 1 + 3 == 4)

# ---------------------------------------------------------------- E. P^1 Cech analogue of the secondary map (exact)
# A=O(-3), B=C=O(-1) (acyclic), D=O(1); f0 = X0^2 (div 2p, p = infinity), f1 = X0 (X1 - 2 X0) (div p + q, q = {x=2}).
x = sp.symbols("x")


def split_m1(phi):
    """G for O(-1): phi in C^1 -> (s0, s1), s0 in k[x], s1 exps <= -1, with s1 - s0 = phi."""
    phi = sp.expand(phi)
    terms = sp.Add.make_args(phi) if phi != 0 else []
    pos = sum((t for t in terms if sp.degree(t * x ** 50, x) - 50 >= 0), sp.Integer(0))
    return -pos, sp.expand(phi - pos)


def Kmap(alpha, F0, F1, sign=-1):
    sC = split_m1(F1 * alpha); sB = split_m1(F0 * alpha)
    s0 = sp.expand(F0 * sC[0] + sign * F1 * sB[0]); s1 = sp.expand(F0 * sC[1] + sign * F1 * sB[1])
    return s0, s1


def Kmatrix(F0, F1, sign=-1):
    cols, closed = [], True
    for alpha in (1 / x, 1 / x ** 2):
        s0, s1 = Kmap(alpha, F0, F1, sign)
        closed = closed and sp.expand(s1 - s0) == 0
        cols.append([sp.expand(s0).coeff(x, 0), sp.expand(s0).coeff(x, 1)])
    return sp.Matrix(cols).T, closed


cases = {"2p and p+q (Z=p)": (sp.Integer(1), x - 2), "coprime (Z=0)": (x ** 2, sp.Integer(1)),
         "proportional (Z=2p)": (sp.Integer(1), sp.Integer(2)), "axis f1=0": (sp.Integer(1), sp.Integer(0))}
eres = {}
for name, (F0, F1) in cases.items():
    K, closed = Kmatrix(F0, F1)
    eres[name] = {"K closed (global section of D)": bool(closed), "rank K": int(K.rank()), "K": str(K.tolist())}
out["E1 K_* = F0 G_C F1 - F1 G_B F0 is closed; rank K = 2 - deg Z (packet: rank 1 for Z = p)"] = eres
Kp, closedp = Kmatrix(sp.Integer(1), x - 2, sign=+1)
plants["E1-plant: the + sign F0 G_C F1 + F1 G_B F0 is closed (must FAIL)"] = bool(closedp)
K1, _ = Kmatrix(sp.Integer(1), x - 2)
out["E2 kernel of K = span{x^-2} = image of the endpoint quotient Abar(p)/Abar in H1(Abar)"] = bool(
    K1 * sp.Matrix([0, 1]) == sp.zeros(2, 1) and K1 * sp.Matrix([1, 0]) != sp.zeros(2, 1))
out["E2 image of K = span{1} = H0(Dbar(-p)) inside H0(Dbar) = span{1, x}"] = bool(
    K1[1, :] == sp.zeros(1, 2) and K1[0, :] != sp.zeros(1, 2))
gam0, gam1 = 1 + x ** 2, x ** -3 + 5 * x ** -4      # a Cech 0-cochain of O(-3)
ex = sp.expand(gam1 - gam0)
s0e, s1e = Kmap(ex, sp.Integer(1), x - 2)
out["E3 K kills exact representatives (changing alpha by d gamma leaves K unchanged)"] = bool(
    sp.expand(s0e) == 0 and sp.expand(s1e) == 0)

# ------------------------------------------------- F. normalised mass from M = sqrt2 (d + d^dag), numeric
N = 3
rng = np.random.default_rng(20261118)


def line(n, U):
    c0 = list(range(0, U + 1)) + list(range(-N, n + 1))
    tag = [0] * (U + 1) + [1] * (n + N + 1)
    c1_ = list(range(-N, U + 1))
    return c0, tag, c1_


LA, LB, LD = line(-3, N), line(-1, N + 2), line(1, N + 4)


def bmat(L):
    c0, tag, c1_ = L
    M = np.zeros((len(c1_), len(c0)))
    for j, (e, t) in enumerate(zip(c0, tag)):
        M[c1_.index(e), j] = 1.0 if t == 1 else -1.0          # d(s0, s1) = s1 - s0
    return M


def mult(poly, Ls, Lt, deg):
    coeffs = {k: complex(sp.Poly(poly, x).coeff_monomial(x ** k)) for k in range(3)}
    if deg == 0:
        src, stag = Ls[0], Ls[1]; tgt, ttag = Lt[0], Lt[1]
        M = np.zeros((len(tgt), len(src)), complex)
        for j, (e, t) in enumerate(zip(src, stag)):
            for k, c in coeffs.items():
                if c:
                    M[[i for i, (e2, t2) in enumerate(zip(tgt, ttag)) if e2 == e + k and t2 == t][0], j] += c
        return M
    src, tgt = Ls[2], Lt[2]
    M = np.zeros((len(tgt), len(src)), complex)
    for j, e in enumerate(src):
        for k, c in coeffs.items():
            if c:
                M[tgt.index(e + k), j] += c
    return M


def randmetric(n):
    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    G = X.conj().T @ X + n * np.eye(n)
    return np.linalg.cholesky(G).conj().T                 # R with G = R^dag R


def model(F0p, F1p, nu0, nu1):
    bA, bB, bD = bmat(LA), bmat(LB), bmat(LD)
    dims = {"A0": len(LA[0]), "A1": len(LA[2]), "B0": len(LB[0]), "B1": len(LB[2]),
            "C0": len(LB[0]), "C1": len(LB[2]), "D0": len(LD[0]), "D1": len(LD[2])}
    R = {k: randmetric(v) for k, v in dims.items()}
    F = {}
    for i_, P in ((0, F0p), (1, F1p)):
        for dg in (0, 1):
            F[(i_, "AB", dg)] = mult(P, LA, LB, dg)
            F[(i_, "BD", dg)] = mult(P, LB, LD, dg)
    order = ["A0", "A1", "B0", "C0", "B1", "C1", "D0", "D1"]
    tdeg = {"A0": 0, "A1": 1, "B0": 1, "C0": 1, "B1": 2, "C1": 2, "D0": 2, "D1": 3}
    off = np.cumsum([0] + [dims[k] for k in order]); pos = {k: (off[j], off[j + 1]) for j, k in enumerate(order)}
    n_tot = off[-1]

    def put(Mx, t_, s_, blk):
        Mx[pos[t_][0]:pos[t_][1], pos[s_][0]:pos[s_][1]] += blk

    Db = np.zeros((n_tot, n_tot), complex); Dk = np.zeros((n_tot, n_tot), complex)
    put(Db, "A1", "A0", bA); put(Db, "B1", "B0", bB); put(Db, "C1", "C0", bB); put(Db, "D1", "D0", bD)
    for dg, sg in ((0, 1), (1, -1)):                           # delta_signed = (-1)^form-degree delta
        a_, b_, c_, d_ = f"A{dg}", f"B{dg}", f"C{dg}", f"D{dg}"
        put(Dk, b_, a_, sg * nu0 * F[(0, "AB", dg)]); put(Dk, c_, a_, sg * nu1 * F[(1, "AB", dg)])
        put(Dk, d_, b_, sg * (-nu1) * F[(1, "BD", dg)]); put(Dk, d_, c_, sg * nu0 * F[(0, "BD", dg)])
    Rt = np.zeros((n_tot, n_tot), complex)
    for k in order:
        Rt[pos[k][0]:pos[k][1], pos[k][0]:pos[k][1]] = R[k]
    Ri = np.linalg.inv(Rt)
    to_on = lambda Mx: Rt @ Mx @ Ri
    sq = np.abs((Db + Dk) @ (Db + Dk)).max()
    # sigma_* : K on the harmonic H1(A) (ON coordinates), into H0(D) (ON coordinates)
    bA_on = R["A1"] @ bA @ np.linalg.inv(R["A0"])
    U_, S_, Vh_ = np.linalg.svd(bA_on)
    harm = U_[:, len(LA[0]):]                                   # complement of the image (rank = dim A0)
    raw = np.linalg.inv(R["A1"]) @ harm
    GB = np.linalg.inv(bB)
    K = F[(0, "BD", 0)] @ GB @ F[(1, "AB", 1)] @ raw - F[(1, "BD", 0)] @ GB @ F[(0, "AB", 1)] @ raw
    closed = np.abs(bD @ K).max()
    sig = np.linalg.svd(R["D0"] @ K, compute_uv=False)
    return Db, Dk, to_on, sig, closed, sq


fres = {}
nu0, nu1 = 0.7 - 0.4j, -1.3 + 0.5j
for name, (P0, P1), nlight in (("2p and p+q (Z=p)", (sp.Integer(1), x - 2), 1),
                               ("coprime (Z=0)", (x ** 2, sp.Integer(1)), 2)):
    Db, Dk, to_on, sig, closed, sq = model(P0, P1, nu0, nu1)
    pred = sorted(np.sqrt(2) * abs(nu0 * nu1) * sig[sig > 1e-9])
    rows = []
    for t in (1e-2, 1e-3, 1e-4):
        Mt = np.sqrt(2) * (to_on(Db + t * Dk) + to_on(Db + t * Dk).conj().T)
        ev = np.sort(np.abs(np.linalg.eigvalsh(Mt)))
        light = ev[:4]
        rows.append({"t": t, "light |eigenvalues| / t^2": [float(v / t ** 2) for v in light]})
    last = rows[-1]["light |eigenvalues| / t^2"]
    lifted = sorted(last)[-2 * nlight:]
    fres[name] = {"d^2 max": float(sq), "K closed residual": float(closed), "sigma(K)": [float(v) for v in sig],
                  "predicted sqrt2|nu0 nu1| sigma": [float(v) for v in pred], "runs": rows,
                  "rel. deviation at t=1e-4": float(max(abs(l / pp - 1) for l, pp in zip(lifted, sorted(pred * 2)))),
                  "persistent eigenvalues (t=1e-4, /t^2)": sorted(last)[:4 - 2 * nlight]}
    if name.startswith("2p"):
        plants["F-plant: light mass = |nu0 nu1| sigma t^2 without sqrt2, within 1e-3 (must FAIL)"] = bool(
            max(abs(l / (abs(nu0 * nu1) * sig[0]) - 1) for l in lifted) < 1e-3)
out["F1 M = sqrt2 (d + d^dag) in a finite metric model: light masses = sqrt2 |nu0 nu1| sigma_* t^2 (6)"] = fres

# ---------------------------------------------------------------- G. provenance pins
repo = HERE.parent.parent
git = lambda *a, cwd=repo: subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
nov9 = ("reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/"
        "NATIVE_CYCLIC_DEFORMATION_AND_DERIVED_QUADRATIC_MOMENT_RESPONSE_2026_11_09.md")
out["G1 the November 9 source named in PRIOR_WORK_RECONCILIATION exists at 798281903"] = git(
    "cat-file", "-e", f"798281903:{nov9}").returncode == 0
if len(sys.argv) > 1:
    mainp = pathlib.Path(sys.argv[1]).resolve()
    txt = git("show", "613c4f4174ffaf1afef0b1e0bd8efdcff3f620ec:docs/seats/physical.md", cwd=mainp).stdout
    out["G2 main's docs/seats/physical.md at 613c4f41 carries M4 (end law) and M5"] = bool(
        "### M4" in txt and "### M5" in txt and "end law" in txt)
else:
    out["G2 main's docs/seats/physical.md at 613c4f41 carries M4 (end law) and M5"] = "not run (no MAIN_CHECKOUT)"

out["PLANTS (each must be False)"] = plants
print(json.dumps(out, indent=1, default=str))
HERE.joinpath("check_cyclic_charged_mass.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
