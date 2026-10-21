#!/usr/bin/env python3
"""W114 -- the tuned layer's fit: can theta-bar = 0 at every tau and the observed quarks coexist in the record's
frame at all, at the cost of one tuned number per tuned sector?  The rule is W114_RULE.md, committed and pushed
before this script.  One run; its output (the_tuned_fit.json, the_tuned_fit_run.txt) is committed before it is read.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the exact cubic tensor against a direct determinant on random integer vectors, the root parametrization's
landing on the variety (and its 30-digit refinement), the objective's evaluation at random points (whether it
returns, with no value printed), and its timing.  One dead block was removed.  No fit was run before the run.

It reuses W113's code (the_strong_angle.py, imported): the exact spaces and real bases, the fast evaluation, the
observables, the data and the chi-squared.  On a tuned sector, alpha(c) -- the E4^3 part of det Y / eta^a -- is a
real cubic form, built exactly as a tensor by multilinearity in the rows; a free vector v maps to c = v + s* e, with
s* the real root of alpha(v + s e) of least |s| along a fixed direction e, so every point lies on the variety.
"""
import itertools
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_strong_angle as SA  # noqa: E402

mp.mp.dps = 30
T0 = time.time()
P, M_ = 1, -1
TT, BB, MQT, MQB = (P, P), (M_, M_), (P, M_), (M_, P)
# (number, hand, (up type, up weight), (down type, down weight)) in the rule's order; tuned weights 5, 7, 4
ASSIGN = [
    (1, (P, P, P), (TT, 1), (TT, 5)), (2, (P, P, P), (TT, 5), (TT, 1)), (3, (P, P, P), (TT, 5), (TT, 5)),
    (4, (P, P, M_), (TT, 1), (MQT, 4)), (5, (P, P, M_), (TT, 5), (MQT, 4)),
    (6, (P, M_, P), (MQT, 4), (TT, 1)), (7, (P, M_, P), (MQT, 4), (TT, 5)),
    (8, (P, M_, M_), (MQT, 4), (MQT, 4)), (9, (M_, P, P), (MQB, 4), (MQB, 4)),
    (10, (M_, P, M_), (MQB, 4), (BB, 3)), (11, (M_, P, M_), (MQB, 4), (BB, 7)),
    (12, (M_, M_, P), (BB, 3), (MQB, 4)), (13, (M_, M_, P), (BB, 7), (MQB, 4)),
    (14, (M_, M_, M_), (BB, 3), (BB, 7)), (15, (M_, M_, M_), (BB, 7), (BB, 3)), (16, (M_, M_, M_), (BB, 7), (BB, 7)),
]
PASS = {4: 9.49, 2: 5.99, 1: 3.84}
COMPAT = 3.84


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


def perm_sign(perm):
    s = 1
    for x in range(3):
        for y in range(x + 1, 3):
            if perm[x] > perm[y]:
                s = -s
    return s


def exact_series(rb, p0):
    return [[[[sum((x * SA.mon_series(mon)[p] for mon, x in B[i][j].items()), Fraction(0)) for p in range(p0 + 1)]
              for j in range(3)] for i in range(3)] for B in rb]


def det_coeff(rows, p0):
    """the t^p0 coefficient of the determinant whose row i is rows[i] (3 lists of series)"""
    tot = Fraction(0)
    for perm in itertools.permutations(range(3)):
        sg = perm_sign(perm)
        A_, B_, C_ = rows[0][perm[0]], rows[1][perm[1]], rows[2][perm[2]]
        for p1 in range(p0 + 1):
            if A_[p1] == 0:
                continue
            for p2 in range(p0 + 1 - p1):
                if B_[p2] == 0:
                    continue
                tot += sg * A_[p1] * B_[p2] * C_[p0 - p1 - p2]
    return tot


class SectorParam:
    def __init__(self, typ, k, rng):
        basis, d = SA.space(typ[0], typ[1], k)
        closed, rb = SA.real_basis(basis, d)
        self.typ, self.k, self.rb, self.dim = typ, k, rb, len(rb)
        self.label = f"{SA.NAME[typ]} k={k}"
        self.S = SA.Sector(rb, SA.M_ETA[typ], self.label)
        self.tuned = (k == SA.K_TUNED[typ])
        self.nfree = 0 if self.dim == 1 else self.dim
        self.check = None
        if self.tuned:
            m, a = SA.M_ETA[typ], SA.A_CHAR[typ]
            self.p0 = m + a // 3
            ser = exact_series(rb, self.p0)
            n = self.dim
            D = {}
            for b1, b2, b3 in itertools.product(range(n), repeat=3):
                D[(b1, b2, b3)] = det_coeff([ser[b1][0], ser[b2][1], ser[b3][2]], self.p0)
            # the symmetric tensor (floats) with alpha(c) = sum_ijk As[i,j,k] c_i c_j c_k
            As = np.zeros((n, n, n))
            for idx in itertools.product(range(n), repeat=3):
                perms = list(itertools.permutations(idx))
                As[idx] = float(sum((D[q] for q in perms), Fraction(0)) / len(perms))
            self.As = As
            self.Dexact = D
            # the self-check: the tensor against a direct determinant on random integer vectors
            ok = True
            for _ in range(3):
                c = [Fraction(int(x)) for x in rng.integers(-7, 8, size=n)]
                rows = [[[sum((c[b] * ser[b][i][j][p] for b in range(n)), Fraction(0)) for p in range(self.p0 + 1)]
                         for j in range(3)] for i in range(3)]
                direct = det_coeff(rows, self.p0)
                via = sum((D[idx] * c[idx[0]] * c[idx[1]] * c[idx[2]] for idx in D), Fraction(0))
                ok = ok and (direct == via)
            self.check = ok
            scale = float(np.max(np.abs(As))) if np.max(np.abs(As)) > 0 else 1.0
            while True:
                e = rng.normal(size=n)
                e = e / np.linalg.norm(e)
                if abs(self.alpha(e)) > 1e-3 * scale:
                    break
            self.e = e

    def alpha(self, c):
        return float(np.einsum("ijk,i,j,k->", self.As, c, c, c))

    def cubic(self, v):
        A, e = self.As, self.e
        a3 = np.einsum("ijk,i,j,k->", A, e, e, e)
        a2 = 3 * np.einsum("ijk,i,j,k->", A, v, e, e)
        a1 = 3 * np.einsum("ijk,i,j,k->", A, v, v, e)
        a0 = np.einsum("ijk,i,j,k->", A, v, v, v)
        return np.array([a3, a2, a1, a0])

    def coeffs(self, v):
        if self.dim == 1:
            return np.array([1.0])
        v = np.asarray(v, dtype=float)
        if not self.tuned:
            nv = np.linalg.norm(v)
            return v / nv if nv > 1e-12 else None
        co = self.cubic(v)
        r = np.roots(co)
        scale = max(1.0, float(np.max(np.abs(r)))) if r.size else 1.0
        real = [x.real for x in r if abs(x.imag) <= 1e-9 * scale]
        if not real:
            return None
        s = min(real, key=abs)
        c = v + s * self.e
        nc = np.linalg.norm(c)
        return c / nc if nc > 1e-12 else None

    def coeffs_mp(self, v):
        """the same root refined at 30 digits from the exact tensor (for the read-outs)"""
        if not self.tuned:
            return [mp.mpf(float(x)) for x in self.coeffs(v)]
        n = self.dim
        vv = [mp.mpf(float(x)) for x in v]
        ee = [mp.mpf(float(x)) for x in self.e]

        def form(x, y, z):
            return sum(mp.mpf(Dv.numerator) / Dv.denominator * x[i] * y[j] * z[k]
                       for (i, j, k), Dv in self.Dexact.items())

        a3, a0 = form(ee, ee, ee), form(vv, vv, vv)
        a2 = form(vv, ee, ee) + form(ee, vv, ee) + form(ee, ee, vv)
        a1 = form(vv, vv, ee) + form(vv, ee, vv) + form(ee, vv, vv)
        roots = mp.polyroots([a3, a2, a1, a0], maxsteps=2000, extraprec=120)
        real = [mp.re(x) for x in roots if abs(mp.im(x)) < mp.mpf(10) ** -20 * max(1, max(abs(y) for y in roots))]
        s = min(real, key=abs)
        c = [vv[i] + s * ee[i] for i in range(n)]
        nc = mp.sqrt(sum(x * x for x in c))
        return [x / nc for x in c]


class Model:
    def __init__(self, up, dn):
        self.up, self.dn = up, dn
        self.npar = 2 + up.nfree + dn.nfree
        self.nfit = 2 + (up.dim - 1 - int(up.tuned)) + (dn.dim - 1 - int(dn.tuned))
        self.dof = 8 - self.nfit

    def split(self, p):
        return complex(p[0], p[1]), p[2:2 + self.up.nfree], p[2 + self.up.nfree:]

    def evaluate(self, p, ycap=8.0):
        tau, vu, vd = self.split(p)
        if tau.imag <= 0.05:
            return None
        tf = SA.to_fd(tau)
        if tf.imag > ycap:
            return None
        cu, cd = self.up.coeffs(vu), self.dn.coeffs(vd)
        if cu is None or cd is None:
            return None
        U, E = SA.u_eta_np(np.array([tf]))
        Yu, Yd = self.up.S.Y(U, E, cu), self.dn.S.Y(U, E, cd)
        return tf, cu, cd, SA.observables(Yu, Yd)

    def chi2(self, p, logd, a):
        r = self.evaluate(p)
        if r is None:
            return 1e30
        c = SA.chi2_many(r[3][0][0], logd, a)
        return float(c) if np.isfinite(c) else 1e30


def nm(f, p0, maxfev):
    r = minimize(f, p0, method="Nelder-Mead",
                 options={"maxfev": maxfev, "maxiter": maxfev, "xatol": 1e-10, "fatol": 1e-12, "adaptive": True})
    return r.x, float(r.fun)


def random_starts(model, rng, n):
    taus = SA.random_tau_F(rng, n, 6.0)
    VU = rng.normal(size=(n, model.up.nfree)) if model.up.nfree else np.zeros((n, 0))
    VD = rng.normal(size=(n, model.dn.nfree)) if model.dn.nfree else np.zeros((n, 0))
    return np.concatenate([taus.real[:, None], taus.imag[:, None], VU, VD], 1)


def stage1(model, P1, logd, a):
    vals = np.full(len(P1), np.inf)
    U, E = SA.u_eta_np(P1[:, 0] + 1j * P1[:, 1])
    CU = np.array([model.up.coeffs(p[2:2 + model.up.nfree]) if model.up.nfree else np.array([1.0]) for p in P1],
                  dtype=object)
    CD = np.array([model.dn.coeffs(p[2 + model.up.nfree:]) if model.dn.nfree else np.array([1.0]) for p in P1],
                  dtype=object)
    good = np.array([cu is not None and cd is not None for cu, cd in zip(CU, CD)])
    idx = np.where(good)[0]
    cu = np.stack([CU[i] for i in idx])
    cd = np.stack([CD[i] for i in idx])
    for s in range(0, len(idx), 5000):
        j = idx[s:s + 5000]
        Yu = model.up.S.Y(U[j], E[j], cu[s:s + 5000])
        Yd = model.dn.S.Y(U[j], E[j], cd[s:s + 5000])
        obs = SA.observables(Yu, Yd)[0]
        vals[j] = SA.chi2_many(obs, logd, a)
    return vals


def search(model, logd, rng, a=0.10, n1=20000, n2=50, n3=5, maxfev=8000):
    P1 = random_starts(model, rng, n1)
    v1 = stage1(model, P1, logd, a)
    order = np.argsort(v1)
    starts = [P1[i] for i in order[:n2]]

    def f(p):
        return model.chi2(p, logd, a)

    s2 = sorted((nm(f, p0, maxfev) for p0 in starts), key=lambda t: t[1])
    s3 = sorted((nm(f, p, maxfev) for p, _ in s2[:n3]), key=lambda t: t[1])
    return s3[0], float(v1[order[0]]), [v for _, v in s2[:5]], starts


def readout(model, p, K):
    tf, cu, cd, (obs, J, su, sd, V) = model.evaluate(p, ycap=1e9)
    obs = obs[0]
    pulls = ((np.log(obs) - SA.LOGD) / np.hypot(SA.REL, 0.10)).tolist()
    tau, vu, vd = model.split(p)
    cu_mp = model.up.coeffs_mp(vu) if model.up.nfree else [mp.mpf(1)]
    cd_mp = model.dn.coeffs_mp(vd) if model.dn.nfree else [mp.mpf(1)]

    def W_of(sec, c):
        W = [[{} for _ in range(3)] for _ in range(3)]
        for b, B in enumerate(sec.rb):
            for i in range(3):
                for j in range(3):
                    for mon, x in B[i][j].items():
                        W[i][j][mon] = W[i][j].get(mon, 0) + c[b] * (mp.mpf(x.numerator) / x.denominator)
        return W

    Wu, Wd = W_of(model.up, cu_mp), W_of(model.dn, cd_mp)
    rs = []
    for t in SA.GENERIC5[:3]:
        u, eta = SA.u_mp(t), SA.eta_mp(t)

        def Ym(W, m):
            return mp.matrix([[sum((x * u[0] ** mo[0] * u[1] ** mo[1] * u[2] ** mo[2] for mo, x in W[i][j].items()),
                                   mp.mpc(0)) / eta ** m for j in range(3)] for i in range(3)])
        rs.append(mp.det(Ym(Wu, model.up.S.m)) * mp.det(Ym(Wd, model.dn.S.m)) / eta ** (6 * K))
    imag = float(max(abs(r.imag) / abs(r) for r in rs))
    spread = float(max(abs(r - rs[0]) for r in rs) / abs(rs[0]))
    return {"tau_in_F": [tf.real, tf.imag], "delta_to_nearest_elliptic_point": float(min(abs(tf - e)
                                                                                          for e in SA.ELLIPTIC)),
            "observables": dict(zip(SA.LABELS, obs.tolist())), "pulls": dict(zip(SA.LABELS, pulls)),
            "J": float(J[0]), "m_u/m_t": float(obs[0] * obs[1]), "m_d/m_b": float(obs[2] * obs[3]),
            "U1: max |Im r|/|r| at three tau": imag, "U1: spread of r across three tau": spread,
            "U1 holds": bool(imag < 1e-12 and spread < 1e-12), "theta-bar": "0" if rs[0].real > 0 else "pi"}


def main():
    out = {"rule": "W114_RULE.md", "script": "the_tuned_fit.py", "status": "one run"}
    rng = np.random.default_rng(114)
    secs = {}
    for _, _, up, dn in ASSIGN:
        for typ, k in (up, dn):
            if (typ, k) not in secs:
                t = time.time()
                secs[(typ, k)] = SectorParam(typ, k, rng)
                s = secs[(typ, k)]
                log(f"sector {s.label}: dim {s.dim}, tuned {s.tuned}, tensor check {s.check} ({time.time() - t:.1f}s)")
    out["sectors"] = {s.label: {"dim": s.dim, "tuned": s.tuned, "exact tensor equals the direct determinant": s.check}
                      for s in secs.values()}

    # U0, the control, on assignment 12
    n12 = next(a for a in ASSIGN if a[0] == 12)
    model12 = Model(secs[n12[2]], secs[n12[3]])
    rc = np.random.default_rng(1140)
    ostar, pstar = None, None
    for _ in range(5000):
        p = random_starts(model12, rc, 1)[0]
        if p[1] < 1.0 or p[1] > 3.0:
            continue
        r = model12.evaluate(p)
        if r is None:
            continue
        o = r[3][0][0]
        if np.all((o > 1e-6) & (o < 0.9)):
            ostar, pstar = o, p
            break
    (pb, vb), s1, top, _ = search(model12, np.log(ostar), np.random.default_rng(1141))
    out["U0"] = {"synthetic point": pstar.tolist(), "synthetic observables": ostar.tolist(), "chi2_min": vb,
                 "stage-1 best": s1, "holds": bool(vb <= 0.01)}
    log("U0", out["U0"]["chi2_min"], out["U0"]["holds"])

    rows = {}
    for num, hand, up, dn in ASSIGN:
        t = time.time()
        model = Model(secs[up], secs[dn])
        K = up[1] + dn[1]
        (pb, vb), s1, top, starts = search(model, SA.LOGD, np.random.default_rng(1150 + num))
        rec = {"hand": str(hand), "up": secs[up].label, "down": secs[dn].label, "fitted parameters": model.nfit,
               "dof": model.dof, "chi2_min (a = 0.10)": vb, "stage-1 best": s1, "stage-2 best five": top}
        for a2 in (0.05, 0.20):
            rr = [nm(lambda p, a2=a2: model.chi2(p, SA.LOGD, a2), q, 8000) for q in starts[:5]]
            rr.append(nm(lambda p, a2=a2: model.chi2(p, SA.LOGD, a2), pb, 8000))
            rec[f"chi2_min (a = {a2})"] = min(v for _, v in rr)
        if vb < 1e29:
            rec["best point"] = readout(model, pb, K)
        if model.dof >= 1:
            rec["pass mark"] = PASS[model.dof]
            rec["passes"] = bool(vb <= PASS[model.dof])
        else:
            rec["pass mark"] = f"{COMPAT} (compatibility only)"
            rec["compatible"] = bool(vb <= COMPAT)
        rec["seconds"] = time.time() - t
        rows[str(num)] = rec
        log(f"assignment {num}", hand, secs[up].label, "/", secs[dn].label, "dof", model.dof, "chi2_min", vb)
    out["assignments"] = rows

    u1 = all(r.get("best point", {}).get("U1 holds", False) for r in rows.values())
    u2 = all(not rows[str(n)].get("passes", True) for n in (1, 2, 4, 6))
    u3 = all(not r["passes"] for r in rows.values() if "passes" in r)
    u4 = all(not r["compatible"] for r in rows.values() if "compatible" in r)
    out["cells"] = {"U0": out["U0"]["holds"], "U1": bool(u1), "U2": bool(u2), "U3": bool(u3), "U4": bool(u4)}
    out["seconds"] = time.time() - T0
    (HERE / "the_tuned_fit.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    log("cells", out["cells"])
    log("written the_tuned_fit.json")


if __name__ == "__main__":
    main()
