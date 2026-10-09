"""W50 (the rule: W50_RULE.md, committed before this script). Is the parity grading a symmetry at a fixed tau on the
owner's ruled branch, the weave <L, R>? Do couplings in tau alone then give mixing that is not a permutation? Which
modular object is T?

  N1  six word identities in Aut(F2), exact: the braid relation; Delta^4 = conj(a b^-1 a^-1 b) with Delta = L R^-1 L;
      sigma L sigma L^-1 = conj(a^-1), sigma R sigma R^-1 = conj(b) (sigma the sign); P L P R^-1 = conj(b),
      P R P L^-1 = conj(a^-1) (P the swap). Composition is right to left (CP.compose(f, g) = f o g).
  N2  every reduced word of length <= 12 in L^+-1, R^+-1 whose H1 matrix is I, read as an automorphism (the identity,
      conj(u)^+-1 or another). The rule's wording forgot the braid relators; its correction, committed before the run,
      is tested, and the original wording is recorded beside it.
  N3  the residuals on T (W21's construction, W49's basis t_p) at a generic tau, at i and at omega, on the ruled branch
      and with the inner automorphisms and -I added (W40's frame): orders, eigenvalues, commutants. A move fixes tau
      when its Moebius image (the period rule, CONVENTIONS.md section 3) does.
  N4  the couplings in tau alone for T (x) T: vector-valued modular forms for rho_T^v (x) rho_T^v, rho_T = (Delta, L^-1)
      in the basis t_p, split into D (diagonal), O+ (symmetric off-diagonal) and O- (antisymmetric); their dimensions
      by q-expansion (W45's method, returning the forms) at k = 1, 3, ..., 11, and the six-dimensional symmetric
      couplings at k = 3 read directly.
  N5  the mixing at tau0 = 0.17 + 1.13i: (a) O+ at k = 3 against D at k = 5; (b) generic symmetric couplings at k = 5
      against k = 7; (c) D alone at k = 5 against k = 7. V = U_1^H U_2 from the left singular vectors; its distance
      from the permutations is the smallest, over the six permutations P, of the largest ||V_ij| - P_ij|.
  N6  eta^21 (theta_2^2, theta_3^2, theta_4^2) against rho_T: its T- and S-matrices by least squares, and the
      intertwiners B with B M = rho_T B.

  Extra read-outs (no prior): N5's couplings at i and at omega; the singular-value ratios at tau0.

Run: python3 the_parity_grading_at_a_fixed_tau.py  ->  the_parity_grading_at_a_fixed_tau.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_generations_are_a_multiplicity as GM  # noqa: E402  (W49: the basis t_p, restrictions, closure)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: chi, allowed, dims)

CP, CT, H, SR, SC = GM.CP, GM.CT, GM.H, GM.SR, GM.SC
OUT = HERE / "the_parity_grading_at_a_fixed_tau.json"
TOL = 1e-8
ID = {1: [1], 2: [2]}
A_ = {"L": CP.AUT["L"], "Li": SC.INV["L"], "R": CP.AUT["R"], "Ri": SC.INV["R"], "s": CP.AUT["-I"], "P": CP.AUT["P"]}
U_WORD = [1, -2, -1, 2]                                   # u = a b^-1 a^-1 b (W45)
TAU0 = 0.17 + 1.13j
OMEGA = np.exp(2j * np.pi / 3)
WEIGHTS = [1, 3, 5, 7, 9, 11]
PREDICTED = {"D": [0, 0, 1, 1, 2, 2], "O+": [1, 1, 2, 2, 3, 3], "O-": [0, 1, 1, 2, 2, 3]}


def comp(*auts):
    out = ID
    for a in auts:
        out = CP.compose(out, a)
    return out


def ab(word):
    return (sum(1 if x == 1 else -1 if x == -1 else 0 for x in word),
            sum(1 if x == 2 else -1 if x == -2 else 0 for x in word))


def h1(phi):
    """the H1 matrix, the images of a and b as columns"""
    (al, ga), (be, de) = ab(phi[1]), ab(phi[2])
    return ((al, be), (ga, de))


def moebius(phi, tau):
    """the period rule (CONVENTIONS.md section 3): [[al, be], [ga, de]] acts by tau -> (de tau + be)/(ga tau + al)"""
    (al, be), (ga, de) = h1(phi)
    return (de * tau + be) / (ga * tau + al)


def cx(z):
    z = complex(z)
    return [round(z.real, 9), round(z.imag, 9)]


def mat(M):
    return [[cx(x) for x in row] for row in np.array(M)]


def turns(z):
    return round(float(np.angle(z) / (2 * np.pi)) % 1.0, 9) % 1.0


# ------------------------------------------------------------------------------------------------------------------ N1
def N1():
    L, Li, R, Ri, s, P = (A_[k] for k in ("L", "Li", "R", "Ri", "s", "P"))
    D = comp(L, Ri, L)
    rows = {
        "L R^-1 L = R^-1 L R^-1": comp(L, Ri, L) == comp(Ri, L, Ri),
        "Delta^4 = conj(a b^-1 a^-1 b)": comp(D, D, D, D) == CP.inner(U_WORD),
        "sigma L sigma L^-1 = conj(a^-1)": comp(s, L, s, Li) == CP.inner([-1]),
        "sigma R sigma R^-1 = conj(b)": comp(s, R, s, Ri) == CP.inner([2]),
        "P L P R^-1 = conj(b)": comp(P, L, P, Ri) == CP.inner([2]),
        "P R P L^-1 = conj(a^-1)": comp(P, R, P, Li) == CP.inner([-1]),
    }
    return {k: bool(v) for k, v in rows.items()}


# ------------------------------------------------------------------------------------------------------------------ N2
def N2(nmax=12):
    letters = ["L", "Li", "R", "Ri"]
    inverse = {"L": "Li", "Li": "L", "R": "Ri", "Ri": "R"}
    M = {x: h1(A_[x]) for x in letters}

    def mul(X, Y):
        return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
                (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))

    I2 = ((1, 0), (0, 1))
    found, count = [], 0
    stack = [((), I2)]
    while stack:
        word, X = stack.pop()
        if word and X == I2:
            found.append(word)
        if len(word) == nmax:
            continue
        for x in letters:
            if word and inverse[x] == word[-1]:
                continue
            count += 1
            stack.append((word + (x,), mul(X, M[x])))
    named = {"the identity": ID, "conj(u)": CP.inner(U_WORD), "conj(u^-1)": CP.inner(CP.inv(U_WORD)),
             "conj(a)": CP.inner([1]), "conj(a^-1)": CP.inner([-1]),
             "conj(b)": CP.inner([2]), "conj(b^-1)": CP.inner([-2])}
    tally, lengths, positive = {}, {}, True
    for w in found:
        phi = comp(*(A_[x] for x in w))
        name = next((n for n, v in named.items() if v == phi), "other")
        tally[name] = tally.get(name, 0) + 1
        lengths.setdefault(name, set()).add(len(w))
        if name in ("conj(u)", "conj(u^-1)"):
            positive &= set(w) <= {"L", "Ri"} or set(w) <= {"Li", "R"}
    return {"reduced words searched": count, "words with H1 matrix I": len(found),
            "their automorphisms": tally, "their lengths, by automorphism": {n: sorted(v) for n, v in lengths.items()},
            "each word for conj(u)^+-1 uses only L and R^-1, or only L^-1 and R": bool(positive)}


# ------------------------------------------------------------------------------------------------------------------ N3
def lifts_on_T(Ct, phi):
    return [GM.on_T(Ct, CT.on_V(phi, g))[0] for g in CP.extend(phi)]


def commutant_dim(mats):
    rows = [np.kron(g.T, np.eye(3)) - np.kron(np.eye(3), g) for g in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(sum(s < 1e-9 * max(1.0, s[0])))


def residual(Ct, gens):
    mats = [Y for phi in gens for Y in lifts_on_T(Ct, phi)]
    G = GM.closure3(mats)
    return {"order": len(G), "commutant dimension": commutant_dim(mats)}, mats


def N3(Ct):
    L, Ri = A_["L"], A_["Ri"]
    D = comp(L, Ri, L)
    D2 = comp(D, D)
    U = {1: [2], 2: [-1, 2]}
    w = comp(L, U, A_["Li"])
    inner = [CP.inner([1]), CP.inner([2]), A_["s"]]
    mob = {"Delta^2 has H1 matrix -I": h1(D2) == ((-1, 0), (0, -1)),
           "U = L^-1 o R (so U lies in <L, R>)": comp(A_["Li"], A_["R"]) == U,
           "Delta fixes i": bool(abs(moebius(D, 1j) - 1j) < 1e-12),
           "L U L^-1 fixes omega": bool(abs(moebius(w, OMEGA) - OMEGA) < 1e-12),
           "the H1 matrix of L U L^-1": [list(r) for r in h1(w)]}
    gen, _ = residual(Ct, [D2])
    at_i, mi = residual(Ct, [D, D2])
    at_w, mw = residual(Ct, [w, D2])
    w40_gen, _ = residual(Ct, [D2] + inner)
    w40_w, _ = residual(Ct, [w, D2] + inner)

    def eig_mult(Y):
        ev = np.linalg.eigvals(Y)
        groups = []
        for z in ev:
            for gp in groups:
                if abs(gp[0] - z) < 1e-7:
                    gp.append(z)
                    break
            else:
                groups.append([z])
        return sorted(len(gp) for gp in groups), sorted(turns(z) for z in ev)

    D_lifts = lifts_on_T(Ct, D)
    w_lifts = lifts_on_T(Ct, w)
    out = {"the Moebius checks": mob,
           "the ruled branch: generic tau (Delta^2)": gen,
           "the ruled branch: i (Delta)": dict(at_i, **{"Delta's eigenvalue multiplicities and turns, by lift":
                                                        [eig_mult(Y) for Y in D_lifts]}),
           "the ruled branch: omega (L U L^-1)": dict(at_w, **{"w's eigenvalue multiplicities and turns, by lift":
                                                               [eig_mult(Y) for Y in w_lifts],
                                                               "w^3 is a scalar, for each lift": [
                                                                   GM.close(np.linalg.matrix_power(Y, 3),
                                                                            np.linalg.matrix_power(Y, 3)[0, 0]
                                                                            * np.eye(3)) for Y in w_lifts]}),
           "W40's frame (with the inner automorphisms and -I): generic tau": w40_gen,
           "W40's frame (with the inner automorphisms and -I): omega": w40_w}
    D2_lifts = lifts_on_T(Ct, D2)
    scal = all(GM.close(Y, Y[0, 0] * np.eye(3)) for Y in D2_lifts)
    ok = (all(v for k, v in mob.items() if k != "the H1 matrix of L U L^-1")
          and scal and (gen["order"], gen["commutant dimension"]) == (4, 9)
          and (at_i["order"], at_i["commutant dimension"]) == (8, 5)
          and all(eig_mult(Y)[0] == [1, 2] for Y in D_lifts)
          and (at_w["order"], at_w["commutant dimension"]) == (12, 3)
          and all(eig_mult(Y)[0] == [1, 1, 1] for Y in w_lifts)
          and all(out["the ruled branch: omega (L U L^-1)"]["w^3 is a scalar, for each lift"])
          and (w40_gen["order"], w40_gen["commutant dimension"]) == (16, 3)
          and (w40_w["order"], w40_w["commutant dimension"]) == (48, 1))
    out["Delta^2 acts on T as a scalar"] = bool(scal)
    return out, bool(ok)


# ------------------------------------------------------------------------------------------------------------------ N4
def rho_T(Ct):
    (_, gL, gR) = H.lift_choices()[0]
    tL = GM.on_T(Ct, CT.on_V(CP.AUT["L"], gL))[0]
    tR = GM.on_T(Ct, CT.on_V(CP.AUT["R"], gR))[0]
    A = tL @ np.linalg.inv(tR) @ tL
    return A, np.linalg.inv(tL)


def pieces():
    E = lambda p, q: np.eye(9)[:, 3 * p + q]
    r = 1 / np.sqrt(2)
    D = np.array([E(p, p) for p in range(3)]).T
    Op = np.array([r * (E(p, q) + E(q, p)) for p, q in ((0, 1), (0, 2), (1, 2))]).T
    Om = np.array([r * (E(p, q) - E(q, p)) for p, q in ((0, 1), (0, 2), (1, 2))]).T
    Sym = np.hstack([D, Op])
    return {"D": D, "O+": Op, "O-": Om, "Sym": Sym}


def forms(rS, rT, k, N=24, M=120):
    """W45's dims, returning the forms: (null count, gap, coefficient columns, the evaluator)"""
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    w, P = np.linalg.eig(rT)
    P = np.linalg.qr(P)[0] if np.allclose(rT @ rT.conj().T, np.eye(d)) else P
    lam = [float(np.angle(z) / (2 * np.pi)) % 1.0 for z in w]
    lam = [0.0 if abs(x - 1) < 1e-9 or abs(x) < 1e-9 else x for x in lam]
    cols = [(j, n) for j in range(d) for n in range(N)]
    h0 = np.sqrt(3) / 2

    def phi(j, n, t):
        e = n + lam[j]
        return np.exp(2j * np.pi * e * t) * np.exp(2 * np.pi * e * h0)

    thetas = np.linspace(np.pi / 3 + 0.02, 2 * np.pi / 3 - 0.02, M)
    rows = []
    for th in thetas:
        t = np.exp(1j * th)
        ts = -1 / t
        tk = np.exp(float(k) * np.log(t))
        block = np.zeros((d, len(cols)), dtype=complex)
        for c, (j, n) in enumerate(cols):
            block[:, c] = P[:, j] * phi(j, n, ts) - tk * (rS @ P[:, j]) * phi(j, n, t)
        rows.append(block)
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A)
    s = s / s[0]
    null = int(sum(s < 1e-9))
    gap = [float(s[len(s) - null - 1]) if null < len(s) else None, float(s[-null]) if null else None]
    Z = vh[len(s) - null:].conj().T if null else np.zeros((len(cols), 0))

    def evaluate(c, t):
        return sum(c[i] * P[:, j] * phi(j, n, t) for i, (j, n) in enumerate(cols))

    return null, gap, Z, evaluate


def as_matrix(v, basis):
    return (basis @ v).reshape(3, 3)


def couplings(rS9, rT9, B, k):
    rS, rT = B.conj().T @ rS9 @ B, B.conj().T @ rT9 @ B
    return forms(rS, rT, k), (rS, rT)


def N4(A, Tm):
    rS9, rT9 = np.kron(A.conj(), A.conj()), np.kron(Tm.conj(), Tm.conj())
    pcs = pieces()
    inv = {n: bool(GM.close((np.eye(9) - B @ B.conj().T) @ X @ B, np.zeros_like(B))) for n, B in pcs.items()
           for X in (rS9, rT9)}
    dims, store, check_iw, s_test = {}, {}, True, {}
    t_test = 0.31 + 0.97j
    for name in ("D", "O+", "O-"):
        B = pcs[name]
        row = {}
        for k in WEIGHTS:
            (null, gap, Z, ev), (rS, rT) = couplings(rS9, rT9, B, k)
            row[str(k)] = {"dimension (null count)": null, "gap": gap}
            iw = IW.dims(rS, rT, Fraction(k))[0]
            check_iw &= iw == null
            store[(name, k)] = (Z, ev, B)
            for i in range(null):
                lhs = ev(Z[:, i], -1 / t_test)
                rhs = np.exp(k * np.log(t_test)) * (rS @ ev(Z[:, i], t_test))
                s_test[(name, k, i)] = float(np.linalg.norm(lhs - rhs) / max(1e-300, np.linalg.norm(rhs)))
        dims[name] = row
    (null6, gap6, Z6, ev6), _ = couplings(rS9, rT9, pcs["Sym"], 3)
    sym3 = []
    for i in range(null6):
        Y = as_matrix(ev6(Z6[:, i], TAU0), pcs["Sym"])
        sym3.append(float(np.max(np.abs(np.diag(Y))) / np.max(np.abs(Y))))
    got = {n: [dims[n][str(k)]["dimension (null count)"] for k in WEIGHTS] for n in dims}
    table_ok = all(got[n][1:] == PREDICTED[n][1:] and got[n][0] >= PREDICTED[n][0] for n in PREDICTED)
    out = {"the pieces are invariant": all(inv.values()), "dimensions by piece and weight": dims,
           "dimensions, as lists over k = 1, 3, ..., 11": got,
           "W45's dims agrees on every piece and weight": bool(check_iw),
           "the largest relative S-relation residual at tau = 0.31 + 0.97i": max(s_test.values()) if s_test else None,
           "the six-dimensional symmetric couplings at k = 3: count": null6,
           "their largest diagonal entry over their largest entry, at tau0": sym3}
    res = out["the largest relative S-relation residual at tau = 0.31 + 0.97i"]
    ok = (out["the pieces are invariant"] and table_ok and check_iw and null6 == 1 and bool(sym3) and sym3[0] < 1e-8
          and res is not None and res < 1e-6)
    return out, bool(ok), store, pcs


# ------------------------------------------------------------------------------------------------------------------ N5
def perm_distance(V):
    a = np.abs(V)
    best = None
    for p in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for i, j in enumerate(p):
            P[i, j] = 1.0
        dist = float(np.max(np.abs(a - P)))
        best = dist if best is None else min(best, dist)
    return best


def left_basis(Y):
    U, s, _ = np.linalg.svd(Y)
    return U, s


def mixing(Y1, Y2):
    U1, s1 = left_basis(Y1)
    U2, s2 = left_basis(Y2)
    V = U1.conj().T @ U2
    rel = lambda s: [round(float(x / s[0]), 9) for x in s]
    gap = lambda s: float(min(abs(s[0] - s[1]), abs(s[1] - s[2])) / s[0])
    return {"distance from the permutations": round(perm_distance(V), 9), "|V|": np.round(np.abs(V), 6).tolist(),
            "singular values over the largest: first, second": [rel(s1), rel(s2)],
            "the smallest relative gap between singular values: first, second": [round(gap(s1), 9),
                                                                                  round(gap(s2), 9)]}


def coupling_at(store, pcs, name, k, coeffs, tau):
    Z, ev, B = store[(name, k)]
    v = Z @ coeffs
    return as_matrix(ev(v, tau), B)


def N5(store, pcs, rng):
    def rnd(n):
        return rng.normal(size=n) + 1j * rng.normal(size=n)

    def dim(name, k):
        return store[(name, k)][0].shape[1]

    def sym_generic(k, cD, cO, tau):
        Y = np.zeros((3, 3), dtype=complex)
        if dim("D", k):
            Y += coupling_at(store, pcs, "D", k, cD, tau)
        if dim("O+", k):
            Y += coupling_at(store, pcs, "O+", k, cO, tau)
        return Y

    have = dim("O+", 3) >= 1 and dim("D", 5) >= 1 and dim("D", 7) >= 1
    cO3 = np.eye(max(1, dim("O+", 3)))[:, 0]
    cD5, cD7 = np.eye(max(1, dim("D", 5)))[:, 0], np.eye(max(1, dim("D", 7)))[:, 0]
    c5 = (rnd(dim("D", 5)), rnd(dim("O+", 5)))
    c7 = (rnd(dim("D", 7)), rnd(dim("O+", 7)))
    out, extra = {}, {}
    for label, tau in (("tau0", TAU0), ("i", 1j), ("omega", OMEGA)):
        if not have:
            break
        a = mixing(coupling_at(store, pcs, "O+", 3, cO3, tau), coupling_at(store, pcs, "D", 5, cD5, tau))
        b = mixing(sym_generic(5, *c5, tau), sym_generic(7, *c7, tau))
        c = mixing(coupling_at(store, pcs, "D", 5, cD5, tau), coupling_at(store, pcs, "D", 7, cD7, tau))
        row = {"(a) O+ at k = 3 against D at k = 5": a, "(b) generic symmetric, k = 5 against k = 7": b,
               "(c) D alone, k = 5 against k = 7": c}
        (out if label == "tau0" else extra)[label] = row
    ok = bool(have and out["tau0"]["(a) O+ at k = 3 against D at k = 5"]["distance from the permutations"] > 0.05
              and out["tau0"]["(b) generic symmetric, k = 5 against k = 7"]["distance from the permutations"] > 0.05
              and out["tau0"]["(c) D alone, k = 5 against k = 7"]["distance from the permutations"] < 1e-8)
    return out, ok, extra


# ------------------------------------------------------------------------------------------------------------------ N6
def theta(tau, K=40):
    n = np.arange(-K, K + 1)
    t2 = np.sum(np.exp(1j * np.pi * (n + 0.5) ** 2 * tau))
    t3 = np.sum(np.exp(1j * np.pi * n ** 2 * tau))
    t4 = np.sum((-1.0) ** n * np.exp(1j * np.pi * n ** 2 * tau))
    return t2, t3, t4


def eta(tau, N=200):
    q = np.exp(2j * np.pi * tau)
    p = 1.0 + 0j
    for m in range(1, N):
        p *= 1 - q ** m
    return np.exp(1j * np.pi * tau / 12) * p


def F(tau):
    t2, t3, t4 = theta(tau)
    return eta(tau) ** 21 * np.array([t2 ** 2, t3 ** 2, t4 ** 2])


def N6(A, Tm):
    pts = [0.11 + 0.93j, -0.27 + 1.02j, 0.38 + 0.98j, -0.05 + 1.21j, 0.22 + 1.4j]
    X = np.array([F(t) for t in pts]).T
    XT = np.array([F(t + 1) for t in pts]).T
    XS = np.array([F(-1 / t) / np.exp(11.5 * np.log(t)) for t in pts]).T
    MT = XT @ np.linalg.pinv(X)
    MS = XS @ np.linalg.pinv(X)
    resT = float(np.linalg.norm(MT @ X - XT) / np.linalg.norm(XT))
    resS = float(np.linalg.norm(MS @ X - XS) / np.linalg.norm(XS))
    I3 = np.eye(3)
    sysm = np.vstack([np.kron(MT.T, I3) - np.kron(I3, Tm), np.kron(MS.T, I3) - np.kron(I3, A)])
    _, s, vh = np.linalg.svd(sysm)
    s = s / s[0]
    null = int(sum(s < 1e-9))
    out = {"the fitted T- and S-matrices (relative residuals)": [resT, resS],
           "the T-matrix's eigen-turns": sorted(turns(z) for z in np.linalg.eigvals(MT)),
           "tr of the S-matrix": cx(np.trace(MS)), "the intertwiners' dimension": null,
           "the smallest singular values": [float(x) for x in s[-3:]]}
    ok = False
    if null == 1:
        B = vh[-1].conj().reshape(3, 3, order="F")
        B = B / B[np.unravel_index(np.argmax(np.abs(B)), B.shape)]
        big = np.abs(B) > 1e-6
        mono = bool(all(big.sum(axis=0) == 1) and all(big.sum(axis=1) == 1))
        names = ["theta_2^2", "theta_3^2", "theta_4^2"]
        pairing = {CT.NAMES[p]: names[int(np.argmax(np.abs(B[p])))] for p in range(3)}
        t = 0.29 + 1.07j
        f1, f0 = B @ F(t + 1), B @ F(t)
        fs = B @ F(-1 / t)
        law = bool(GM.close(f1, Tm @ f0, 1e-6 * np.linalg.norm(f0))
                   and GM.close(fs, np.exp(11.5 * np.log(t)) * (A @ f0), 1e-6 * np.linalg.norm(fs)))
        out.update({"B (scaled)": mat(B), "B is invertible": bool(abs(np.linalg.det(B)) > 1e-6), "B is monomial": mono,
                    "the parity carried by each even theta constant": pairing,
                    "B F obeys rho_T's laws at tau = 0.29 + 1.07i": law})
        ok = bool(out["B is invertible"] and mono and law and resT < 1e-9 and resS < 1e-9)
    return out, ok


def main():
    rng = np.random.default_rng(50)
    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    A, Tm = rho_T(Ct)
    ctl = {"rho_T(S) and rho_T(T) are unitary in the basis t_p": bool(
               GM.close(A @ A.conj().T, np.eye(3)) and GM.close(Tm @ Tm.conj().T, np.eye(3))),
           "tr rho_T(S)": cx(np.trace(A)), "rho_T(S)^2 = i": bool(GM.close(A @ A, 1j * np.eye(3))),
           "rho_T(T)'s eigen-turns (W45: 1/8, 3/8, 7/8)": sorted(turns(z) for z in np.linalg.eigvals(Tm)),
           "tr rho_T(ST)": cx(np.trace(A @ Tm))}
    ctl_ok = bool(ctl["rho_T(S) and rho_T(T) are unitary in the basis t_p"] and ctl["rho_T(S)^2 = i"]
                  and abs(complex(*ctl["tr rho_T(S)"]) - np.exp(1j * np.pi / 4)) < 1e-9
                  and ctl["rho_T(T)'s eigen-turns (W45: 1/8, 3/8, 7/8)"] == [0.125, 0.375, 0.875]
                  and abs(complex(*ctl["tr rho_T(ST)"])) < 1e-9)
    inner_lifts = [Y for phi in (CP.inner([1]), CP.inner([2])) for Y in lifts_on_T(Ct, phi)]
    pcs = pieces()
    kact = []
    for Y in inner_lifts:
        K9 = np.kron(Y.conj(), Y.conj())
        kact.append([bool(GM.close(K9 @ pcs["D"], pcs["D"])),
                     [complex(x).real for x in np.diag(pcs["O+"].conj().T @ K9 @ pcs["O+"])]])
    ctl["the inner automorphisms' lifts: trivial on D; their characters on O+"] = kact
    ctl_ok &= all(a for a, _ in kact) and all(any(abs(x + 1) < 1e-9 for x in c) for _, c in kact)
    n1 = N1()
    n2 = N2()
    n3, ok3 = N3(Ct)
    n4, ok4, store, pcs = N4(A, Tm)
    n5, ok5, extra5 = N5(store, pcs, rng)
    n6, ok6 = N6(A, Tm)
    checks = {
        "N1: the six word identities hold exactly": all(n1.values()),
        "N2 (as corrected before the run): up to length 12 every word with H1 matrix I is the identity or conj(u)^+-1, "
        "those of length 12 and of one sign; no conj(a), conj(b)": bool(
            set(n2["their automorphisms"]) <= {"the identity", "conj(u)", "conj(u^-1)"}
            and n2["their automorphisms"].get("conj(u)", 0) > 0 and n2["their automorphisms"].get("conj(u^-1)", 0) > 0
            and all(n2["their lengths, by automorphism"].get(n) == [12] for n in ("conj(u)", "conj(u^-1)"))
            and n2["each word for conj(u)^+-1 uses only L and R^-1, or only L^-1 and R"]),
        "N3: the residuals on T (ruled branch: 4, 8, 12; W40's frame: 16, 48) with their commutants": ok3,
        "N4: the coupling spaces' dimensions by piece and weight; the symmetric couplings at k = 3 are off-diagonal": ok4,
        "N5: at tau0 the mixings (a) and (b) are not permutations; with D alone every mixing is": ok5,
        "N6: rho_T is eta^21 (theta_2^2, theta_3^2, theta_4^2)'s representation, through a monomial intertwiner": ok6,
    }
    out = {"status": "W50: is the parity grading a symmetry at a fixed tau on the ruled branch? (the rule first)",
           "controls": ctl, "every control holds": ctl_ok,
           "N1: the word identities": n1, "N2: the words with H1 matrix I": n2, "N3: the residuals on T": n3,
           "N4: the couplings in tau alone": n4, "N5: the mixing at tau0": n5, "N6: the theta constants": n6,
           "extra read-outs (not predicted)": {"N5's couplings at i and at omega": extra5},
           "the rule's original N2 wording (every such word empty or for conj(u)^+-1), corrected before the run": bool(
               set(n2["their automorphisms"]) <= {"conj(u)", "conj(u^-1)"}),
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("every control holds:", ctl_ok)
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
