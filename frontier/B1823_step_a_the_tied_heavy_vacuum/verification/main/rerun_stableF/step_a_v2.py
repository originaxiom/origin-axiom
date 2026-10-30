"""STEP A v2 -- the computation (P-518, P-519; THE FINAL ATTACK's Step A).  Data-free: no measured number is read or
compared; the script reads no file.

    nice -n 10 env OMP_NUM_THREADS=1 python3 -I step_a_v2.py [A B C D F G H] [--workers 3]
    -> step_a_v2.json beside itself (sections merged), stdout to step_a_v2_run.txt

 A  modular invariance of every copy's three heavy eigenvalues under T and S (30 digits), with controls that must fail
 B  the overall phase of S drops out (30 digits); control: B1818's additive coupling depends on it
 C  the rank of d(log m^2) on the six coordinates at random points, n = 1..8, both menus; control: one shared triplet
 D  the vacua: seeded multistart on the six coordinates, clustering mod the group, mpmath Newton refinement, the 6x6
    Hessian at two steps (isolated / flat), the Jacobian rank at the vacuum, the free numbers (implicit-function theorem)
 F  the leading order in lambda v: tau0* = argmin V0, S* = lowest eigenvector of Q(tau0*); n = 2: S* = Y1 x Y2
 G  the untied control: per-copy levels planted at a point
 H  the symmetric configurations (i, (1,-1,0)/sqrt2), (omega, eigenvectors of P L^-1): stationarity and Hessians
"""
import sys, json, time, pathlib, platform, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
import scipy
import mpmath as mp
from model import (Singlet, Triplet, Copy, form_values, eigs_from, Ffun, unit, reduce_to_F, frame_at, LINV, LMAT, PMAT,
                   mp_form_values, mp_triplet, mp_eigs_from, mp_F, mp_unit)
from search import (SINGLET_LIST, MENU_Z, MENU_H, NSinglet, NTriplet, make_copies, Model, local_min, fs_dist, sup_norm)

OUT = HERE / "step_a_v2.json"
DPS = 34
mp.mp.dps = DPS
DMAT = np.diag([1.0, 1.0, -1.0])          # the mirror: (tau, S) -> (-conj tau, D conj S)
f6 = lambda v: float(v)


def env():
    return dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, mpmath=mp.__version__,
                mp_dps=DPS, platform=platform.platform())


# =============================================================================================== mpmath model (local chart)
class MPModel:
    """the numpy Model's potential at DPS digits, in a local chart at (tau0, S0)"""
    def __init__(self, model, tau0, S0):
        self.model = model
        self.mu2, self.m02, self.lv = mp.mpf(model.mu2), mp.mpf(model.m02), mp.mpf(model.lv)
        self.recenter(tau0, S0)

    def recenter(self, tau0, S0):
        S0 = unit(np.array([complex(c) for c in S0]))
        e1, e2 = frame_at(S0)
        self.tau0 = mp.mpc(tau0) if not isinstance(tau0, mp.mpc) else tau0
        self.S0 = [mp.mpc(c) for c in S0]; self.e1 = [mp.mpc(c) for c in e1]; self.e2 = [mp.mpc(c) for c in e2]
        self.cache = {}

    def pieces(self, tau):
        key = (mp.nstr(mp.re(tau), 40), mp.nstr(mp.im(tau), 40))
        if key in self.cache:
            return self.cache[key]
        fv = mp_form_values(tau); th, dth, ddth, E4, E6, ae = fv
        y2 = 2 * mp.im(tau); A, D, W = [], [], []
        for c in self.model.copies:
            def sabs(Y):
                return mp.mpf(Y.c) * mp.power(ae, Y.s) * mp.power(abs(E4), Y.p) * mp.power(abs(E6), Y.r)
            A.append(mp.power(y2, mp.mpf(c.YL.w)) * sabs(c.YL) ** 2)
            D.append(mp.power(y2, mp.mpf(c.YE.w)) * sabs(c.YE) ** 2)
            vec, fac = mp_triplet(c.Y3, fv)
            if c.Y3.kind == "DR":
                fac = fac * mp.mpf(c.Y3.scale)
            g = mp.power(y2, mp.mpf(c.Y3.w) / 2) * fac
            W.append([g * v for v in vec])                                       # b^2 = (lambda v)^2 |S . W|^2
        self.cache[key] = (A, D, W)
        return A, D, W

    def point(self, x):
        tau = self.tau0 + x[0] + 1j * x[1]
        S = [self.S0[k] + mp.mpc(x[2], x[3]) * self.e1[k] + mp.mpc(x[4], x[5]) * self.e2[k] for k in range(3)]
        return tau, mp_unit(S)

    def eigs(self, x, lv=None):
        lv = self.lv if lv is None else lv
        tau, S = self.point(x); A, D, W = self.pieces(tau); out = []
        for a2, d2, w in zip(A, D, W):
            b2 = lv ** 2 * abs(sum(S[k] * w[k] for k in range(3))) ** 2
            out.extend(mp_eigs_from(a2, d2, b2))
        return out

    def eigs_at(self, tau, S):
        """eigenvalues at an explicit (tau, S) given in mpmath numbers (no chart, no conversion)"""
        S = mp_unit(S); A, D, W = self.pieces(tau); out = []
        for a2, d2, w in zip(A, D, W):
            b2 = self.lv ** 2 * abs(sum(S[k] * w[k] for k in range(3))) ** 2
            out.extend(mp_eigs_from(a2, d2, b2))
        return out

    def V(self, x, mu2=None, m02=None, lv=None):
        mu2 = self.mu2 if mu2 is None else mu2; m02 = self.m02 if m02 is None else m02
        mus = getattr(self.model, "mu2s", None)
        if mus is None:
            return mp.fsum(mp_F(u, mu2, m02) for u in self.eigs(x, lv))
        e = self.eigs(x, lv); r = mp.mpf(self.model.m0_ratio)
        return mp.fsum(mp_F(e[k], mp.mpf(mus[k // 3]), r * mp.mpf(mus[k // 3])) for k in range(len(e)))

    def grad(self, h, **kw):
        g = []
        for a in range(6):
            xp = [mp.mpf(0)] * 6; xm = [mp.mpf(0)] * 6; xp[a] = h; xm[a] = -h
            g.append((self.V(xp, **kw) - self.V(xm, **kw)) / (2 * h))
        return g

    def hess(self, h):
        H = mp.matrix(6, 6); z = [mp.mpf(0)] * 6; v0 = self.V(z)
        for a in range(6):
            xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
            H[a, a] = (self.V(xp) - 2 * v0 + self.V(xm)) / h ** 2
        for a in range(6):
            for b in range(a + 1, 6):
                vals = []
                for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                    x = list(z); x[a] = sa * h; x[b] = sb * h; vals.append(self.V(x))
                H[a, b] = H[b, a] = (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h * h)
        return H

    def newton(self, it=12, h=mp.mpf("1e-12"), tol=mp.mpf("1e-20")):
        gn = None
        for _ in range(it):
            g = self.grad(h); gn = max(abs(v) for v in g)
            if gn < tol:
                break
            H = self.hess(mp.mpf("1e-8"))
            E, Q = mp.eigsy(H)
            # pseudo-inverse step (flat directions are not moved)
            emax = max(abs(e) for e in E); dx = [mp.mpf(0)] * 6
            for k in range(6):
                if abs(E[k]) > emax * mp.mpf("1e-12"):
                    coef = sum(Q[a, k] * g[a] for a in range(6)) / E[k]
                    for a in range(6):
                        dx[a] -= coef * Q[a, k]
            step = max(abs(v) for v in dx)
            if step > mp.mpf("0.02"):
                dx = [v * mp.mpf("0.02") / step for v in dx]
            tau, S = self.point(dx)
            self.recenter(tau, [complex(c) for c in S]); self.tau0 = tau
            self.S0 = S                                                          # keep full precision of S
        g = self.grad(h); return max(abs(v) for v in g)

    def invariants(self, x):
        """the smooth per-copy invariants (a^2, d^2, beta_hat = b^2 / max_S b^2 in [0, 1]), scale-free"""
        tau, S = self.point(x); A, D, W = self.pieces(tau); out = []
        for a2, d2, w in zip(A, D, W):
            ww = mp.fsum(abs(c) ** 2 for c in w)
            out.extend([mp.log(a2), mp.log(d2), abs(sum(S[k] * w[k] for k in range(3))) ** 2 / ww])
        return out

    def jac_inv(self, h):
        z = [mp.mpf(0)] * 6; J = mp.matrix(3 * len(self.model.copies), 6)
        for a in range(6):
            xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
            up, um = self.invariants(xp), self.invariants(xm)
            for i in range(len(up)):
                J[i, a] = (up[i] - um[i]) / (2 * h)
        return J

    def jac_logm2(self, h):
        z = [mp.mpf(0)] * 6; u0 = self.eigs(z); J = mp.matrix(len(u0), 6)
        for a in range(6):
            xp = list(z); xm = list(z); xp[a] = h; xm[a] = -h
            up, um = self.eigs(xp), self.eigs(xm)
            for i in range(len(u0)):
                J[i, a] = (mp.log(up[i]) - mp.log(um[i])) / (2 * h)
        return J


def svals(J):
    s = mp.svd_r(J, compute_uv=False)
    return sorted([abs(v) for v in s], reverse=True)


# =============================================================================================== A  invariance
def sec_A():
    import random
    rng = random.Random(1818 + 2)
    out = {}
    Lm = np.array(LINV); Pm = np.array(PMAT)
    def mpS(S): return [mp.mpc(c) for c in S]
    pts = []
    for _ in range(3):
        tau = mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 1.7))
        S = unit(np.array([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]))
        pts.append((tau, S))
    for menu in ("Z", "H"):
        model = Model(make_copies(8, menu), 0.5, 0.005, 0.3)
        worst = 0.0; per = []
        for c in model.copies:
            mm = Model([c], 0.5, 0.005, 0.3); wc = 0.0
            for tau, S in pts:
                def eig(t, s):
                    return MPModel(mm, t, s).eigs([mp.mpf(0)] * 6)
                e0 = eig(tau, S); eT = eig(tau + 1, Lm @ S); eS = eig(-1 / tau, Pm @ S)
                wc = max(wc, max(abs(a / b - 1) for a, b in zip(eT, e0)), max(abs(a / b - 1) for a, b in zip(eS, e0)))
            per.append(dict(copy=c.name, weights=(c.YL.w, c.YE.w, c.Y3.w), max_rel_dev=f6(wc)))
            worst = max(worst, wc)
        out["menu_" + menu] = dict(per_copy=per, worst=f6(worst), pass_lt_1e20=bool(worst < 1e-20))
    # the frame's matrices: F_a(tau+1) ~ L^-1 F_a(tau), F_a(-1/tau) ~ P F_a(tau) projectively -- implied by the above;
    # the controls that must FAIL
    tau, S = pts[0]
    def ctrl_inv(ufun):
        u0 = ufun(tau, S); uT = ufun(tau + 1, Lm @ S); uS = ufun(-1 / tau, Pm @ S)
        return f6(max(abs(uT / u0 - 1), abs(uS / u0 - 1)))
    def th(t):
        return mp_form_values(t)[0]
    def ae(t):
        return mp_form_values(t)[5]
    # (i) B1818's singlet theta3^(2m) with exponent 2m (m = 2): not a singlet (theta3(tau+1) = theta4(tau))
    c1 = ctrl_inv(lambda t, s: mp.power(2 * mp.im(t), 4) * abs(th(t)[1] ** 4) ** 2)
    # (ii) a triplet with its components permuted: (eps th2^a, eps th3^a, i th4^a) eta^(3-a), a = 6 (not rho_R-equivariant)
    def perm(t, s):
        t2, t3, t4 = th(t); a = 6
        v = [t2 ** a, t3 ** a, 1j * t4 ** a]
        return mp.power(2 * mp.im(t), mp.mpf(3) / 2) * mp.power(ae(t), 2 * (3 - a)) * abs(sum(mp.mpc(s[k]) * v[k] for k in range(3))) ** 2
    c2 = ctrl_inv(perm)
    # (iii) the right form F_6 with a wrong exponent (2 instead of 3/2)
    def wrongexp(t, s):
        vec, fac = mp_triplet(Triplet("F", 6), mp_form_values(t))
        return mp.power(2 * mp.im(t), 2) * fac ** 2 * abs(sum(mp.mpc(s[k]) * vec[k] for k in range(3))) ** 2
    c3 = ctrl_inv(wrongexp)
    # (iv) B1818's additive coupling: u = (2y)^k |M theta3^(2m) + lam S . Fdir_a|^2 (m = 2, a = 6, k = 4)
    def additive(t, s):
        t2, t3, t4 = th(t); a = 6; eps = 1
        v = [eps * t2 ** a, eps * t4 ** a, 1j * t3 ** a]
        amp = t3 ** 4 + mp.mpf("0.6") * sum(mp.mpc(s[k]) * v[k] for k in range(3))
        return mp.power(2 * mp.im(t), 4) * abs(amp) ** 2
    c4 = ctrl_inv(additive)
    # positive control: W150's eta^12 E4 with exponent 10
    def w150(t, s):
        fv = mp_form_values(t); return mp.power(2 * mp.im(t), 10) * (mp.power(fv[5], 12) * abs(fv[3])) ** 2
    c0 = ctrl_inv(w150)
    out["controls"] = dict(positive_W150_eta12E4_w10=c0, B1818_theta3_singlet=c1, permuted_triplet=c2,
                           wrong_exponent=c3, B1818_additive_coupling=c4,
                           controls_fail_gt_1e3=bool(min(c1, c2, c3, c4) > 1e-3), positive_passes=bool(c0 < 1e-20))
    # the mirror: (tau, S) -> (-conj tau, D conj S) preserves every eigenvalue (real q-coefficients)
    model = Model(make_copies(8, "H"), 0.5, 0.005, 0.3)
    e0 = MPModel(model, tau, S).eigs([mp.mpf(0)] * 6)
    eM = MPModel(model, -mp.conj(tau), DMAT @ S.conj()).eigs([mp.mpf(0)] * 6)
    out["mirror_max_rel_dev"] = f6(max(abs(a / b - 1) for a, b in zip(eM, e0)))
    return out


# =============================================================================================== B  phase
def sec_B():
    import random
    rng = random.Random(7)
    worst = 0.0
    model = Model(make_copies(8, "H"), 0.5, 0.005, 0.3)
    for _ in range(4):
        tau = mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 1.7))
        S = [mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]
        mm = MPModel(model, tau, [complex(c) for c in S])
        e0 = mm.eigs_at(tau, S)
        for al in ("0.3", "1.1", "2.9"):
            ph = mp.exp(1j * mp.mpf(al))
            e1 = mm.eigs_at(tau, [ph * c for c in S])
            worst = max(worst, max(abs(a / b - 1) for a, b in zip(e1, e0)))
    # control: B1818's additive coupling (one bilinear carrying a mass and the Higgs) moves with the phase
    tau = mp.mpc("0.1", "1.3"); S = unit(np.array([1, 0.4 + 0.2j, -0.3j]))
    def additive(s):
        fv = mp_form_values(tau); t2, t3, t4 = fv[0]; a = 6
        v = [t2 ** a, t4 ** a, 1j * t3 ** a]
        amp = t3 ** 4 + mp.mpf("0.6") * sum(mp.mpc(s[k]) * v[k] for k in range(3))
        return mp.power(2 * mp.im(tau), 4) * abs(amp) ** 2
    ctrl = [f6(additive(np.exp(1j * al) * S) / additive(S) - 1) for al in (0.3, 1.1, 2.9)]
    return dict(max_rel_dev_eigs_under_phase=f6(worst), pass_lt_1e25=bool(worst < 1e-25),
                control_B1818_additive_rel_change=ctrl,
                reading="the heavy mass matrix [[a, b], [0, d]] has singular values depending on |a|, |b|, |d| only; "
                        "S -> e^{i alpha} S is a hypercharge rotation absorbed by rephasing L and Ebar")


# =============================================================================================== C  rank at random points
def rank_at(model, tau, S, hs=("1e-12", "1e-10"), thr=mp.mpf("1e-9")):
    res = []
    for h in hs:
        J = MPModel(model, tau, S).jac_logm2(mp.mpf(h))
        s = svals(J); res.append((sum(1 for v in s if v > thr), s))
    return res


def sec_C():
    rng = np.random.default_rng(2026)
    pts = [(complex(rng.uniform(-0.5, 0.5), rng.uniform(0.95, 2.2)), unit(rng.normal(size=3) + 1j * rng.normal(size=3)))
           for _ in range(12)]
    out = {}
    for menu in ("Z", "H"):
        ranks = {}; smin = {}; agree = True
        for n in range(1, 9):
            model = Model(make_copies(n, menu), 0.5, 0.005, 0.3)
            rr = []; ss = []
            for tau, S in pts:
                r = rank_at(model, mp.mpc(tau), S)
                agree = agree and (r[0][0] == r[1][0]); rr.append(r[0][0])
                ss.append(f6(r[0][1][min(r[0][0], len(r[0][1])) - 1]))
            ranks[n] = rr; smin[n] = min(ss)
        out["menu_" + menu] = dict(ranks=ranks, smallest_kept_sval=smin, two_steps_agree=bool(agree),
                                   generic_min_n_plus_2_6=bool(all(all(r == min(n + 2, 6) for r in ranks[n]) for n in ranks)))
    # control: one shared triplet form (F_2) for every copy caps the S-rank at 1: total rank 3
    rr = {}
    for n in (1, 2, 4, 8):
        cps = make_copies(n, "Z")
        for c in cps:
            c.Y3 = NTriplet("F", 2, "N")
        model = Model(cps, 0.5, 0.005, 0.3)
        rr[n] = [rank_at(model, mp.mpc(tau), S, hs=("1e-12",))[0][0] for tau, S in pts[:6]]
    out["control_shared_triplet"] = dict(ranks=rr, caps_at_3=bool(all(all(r == 3 for r in v) for v in rr.values())))
    return out


# =============================================================================================== D  vacua
def canon(tau, S):
    """reduce to F, then mirror to Re tau >= 0; phase: largest component real positive"""
    tau, S = reduce_to_F(tau, unit(S))
    if tau.real < 0:
        tau, S = -tau.conjugate(), DMAT @ S.conj()
        tau, S = reduce_to_F(tau, S)
    k = int(np.argmax(np.abs(S))); S = S * (abs(S[k]) / S[k])
    return tau, S


def mirror_fixed(tau, S, tol=1e-7):
    """is (tau, S) fixed by a reflection of the extended group? returns the line's name or None"""
    S = unit(S)
    cands = []
    if abs(tau.real) < 1e-6:
        cands.append(("Re tau = 0", DMAT @ S.conj()))
    if abs(tau.real - 0.5) < 1e-6:
        cands.append(("Re tau = 1/2", LINV @ DMAT @ S.conj()))         # T o mirror: tau -> 1 - conj tau
    if abs(tau.real + 0.5) < 1e-6:
        cands.append(("Re tau = -1/2", LMAT @ DMAT @ S.conj()))        # T^-1 o mirror: tau -> -1 - conj tau
    if abs(abs(tau) - 1) < 1e-6:
        cands.append(("|tau| = 1", PMAT @ DMAT @ S.conj()))
    for name, S2 in cands:
        if fs_dist(S, S2) < tol:
            return name
    return None


def symmetric_point(tau, tol=1e-6):
    if abs(tau - 1j) < tol:
        return "i"
    if abs(tau - complex(0.5, np.sqrt(3) / 2)) < tol or abs(tau - complex(-0.5, np.sqrt(3) / 2)) < tol:
        return "omega"
    return None


def classify(mpm, h1="1e-8", h2="1e-7"):
    Hs = [mpm.hess(mp.mpf(h)) for h in (h1, h2)]
    E1 = sorted([f6(e) for e in mp.eigsy(Hs[0])[0]]); E2 = sorted([f6(e) for e in mp.eigsy(Hs[1])[0]])
    emax = max(abs(e) for e in E1)
    stable = all(abs(a - b) <= 1e-6 * emax + 1e-3 * abs(a) for a, b in zip(E1, E2))
    nflat = sum(1 for e in E1 if abs(e) < 1e-9 * emax)
    nneg = sum(1 for e in E1 if e < -1e-9 * emax)
    iso = (nflat == 0 and nneg == 0 and min(E1) > 1e-6 * emax)
    return dict(hess_eigs=E1, hess_eigs_step2=E2, stable=bool(stable), n_flat=nflat, n_negative=nneg,
                isolated=bool(iso), min_over_max=E1[0] / emax)


def free_numbers(mpm, H):
    """dx*/d(log mu^2, log m0^2, log lambda v) = -H^-1 d_p grad V; rows tau scaled by 1/Im tau (hyperbolic), S rows are
    already Fubini-Study-orthonormal at first order"""
    h = mp.mpf("1e-12"); dl = mp.mpf("1e-6")
    cols = []
    for which in ("mu2", "m02", "lv"):
        base = dict(mu2=mpm.mu2, m02=mpm.m02, lv=mpm.lv)
        gp = mpm.grad(h, **{**base, which: base[which] * mp.exp(dl)})
        gm = mpm.grad(h, **{**base, which: base[which] * mp.exp(-dl)})
        dg = mp.matrix([(a - b) / (2 * dl) for a, b in zip(gp, gm)])
        cols.append(-(mp.inverse(H) * dg))
    y = mp.im(mpm.tau0)
    M = mp.matrix(6, 3)
    for j in range(3):
        for a in range(6):
            M[a, j] = cols[j][a] / (y if a < 2 else 1)
    s = svals(M)
    per = [f6(mp.sqrt(sum(M[a, j] ** 2 for a in range(6)))) for j in range(3)]
    per_S = [f6(mp.sqrt(sum(M[a, j] ** 2 for a in range(2, 6)))) for j in range(3)]
    return dict(svals=[f6(v) for v in s], rank=sum(1 for v in s if v > 1e-6 * s[0]),
                speed_per_param=dict(zip(("log mu2", "log m02", "log lv"), per)),
                direction_speed_FS_per_param=dict(zip(("log mu2", "log m02", "log lv"), per_S)))


def refine_and_classify(model, cand):
    """mpmath Newton from a candidate, then the Hessian classification, mixings, ranks and free numbers"""
    out = {}
    mpm = MPModel(model, mp.mpc(cand["tau"]), cand["S"])
    gnorm = mpm.newton()
    tau = complex(mpm.tau0); S = np.array([complex(c) for c in mpm.S0])
    tau_c, S_c = canon(tau, S)
    if abs(tau_c - tau) > 1e-12 or fs_dist(S_c, S) > 1e-12:
        mpm = MPModel(model, mp.mpc(tau_c), S_c); gnorm = mpm.newton(it=3)
        tau = complex(mpm.tau0); S = np.array([complex(c) for c in mpm.S0])
    cl = classify(mpm)
    k = int(np.argmax(np.abs(S))); S = S * (abs(S[k]) / S[k])
    A, D, W = model.pieces(tau)
    cs = [model.c_coef(a, d) for a, d in zip(A, D)]
    bs = list(np.abs(W @ S) ** 2)                                                   # b_i^2 (W carries lambda v)
    J = mpm.jac_logm2(mp.mpf("1e-12")); sv = svals(J)
    Ji = mpm.jac_inv(mp.mpf("1e-12")); svi = svals(Ji)
    Ji2 = mpm.jac_inv(mp.mpf("1e-10")); svi2 = svals(Ji2)
    out["best"] = dict(V=f6(mpm.V([mp.mpf(0)] * 6)), tau=[tau.real, tau.imag],
                       S=[[c.real, c.imag] for c in S], grad_inf_after_newton=f6(gnorm),
                       mirror_fixed=mirror_fixed(tau, S), symmetric_point=symmetric_point(tau),
                       cusp=bool(tau.imag > 6), c_coefs=[f6(c) for c in cs], b2=[f6(b) for b in bs],
                       jac_rank_eigs=sum(1 for v in sv if v > 1e-9), jac_svals_eigs=[f6(v) for v in sv],
                       jac_rank_invariants=sum(1 for v in svi if v > 1e-9),
                       jac_rank_invariants_step2=sum(1 for v in svi2 if v > 1e-9),
                       jac_svals_invariants=[f6(v) for v in svi], **cl)
    if cl["n_flat"] > 0:
        H = mpm.hess(mp.mpf("1e-8")); E, Qv = mp.eigsy(H)
        k0 = min(range(6), key=lambda k: abs(E[k]))
        v0 = mpm.V([mp.mpf(0)] * 6); follow = []
        for step in ("0.05", "0.2"):
            x = [Qv[a, k0] * mp.mpf(step) for a in range(6)]
            tau2, S2 = mpm.point(x)
            m2 = MPModel(model, tau2, [complex(c) for c in S2]); m2.newton(it=6)
            t3, S3 = complex(m2.tau0), np.array([complex(c) for c in m2.S0])
            follow.append(dict(step=float(step), dV=f6(m2.V([mp.mpf(0)] * 6) - v0), tau_moved=abs(t3 - tau),
                               fs_moved=fs_dist(S3, S)))
        out["valley_follow"] = follow
    if cl["isolated"]:
        H = mpm.hess(mp.mpf("1e-8"))
        out["free_numbers"] = free_numbers(mpm, H)
    return out


def one_config(args):
    menu, n, mu2, m02, lv, nstart, seed, tnorm, snorm = args
    t0 = time.time()
    model = Model(make_copies(n, menu, tnorm, snorm), mu2, m02, lv)
    rng = np.random.default_rng(seed)
    found = []; failed = 0
    rng2 = np.random.default_rng(seed + 100000)
    for k in range(2 * nstart):
        g = rng if k < nstart else rng2
        x = g.uniform(-0.5, 0.5); y = g.uniform(np.sqrt(1 - x * x), 3.5) if k < nstart else g.uniform(3.5, 16.0)
        S = g.normal(size=3) + 1j * g.normal(size=3)
        try:
            tau, Sf, v, r = local_min(model, complex(x, y), S)
            tau, Sf = canon(tau, Sf)
            if not np.isfinite(v) or v >= 1e29:
                failed += 1; continue
            found.append((v, tau, Sf))
        except Exception:
            failed += 1
    found.sort(key=lambda t: t[0])
    # cluster by the invariant fingerprint (the sorted eigenvalues per copy)
    clusters = []
    for v, tau, S in found:
        fp = np.concatenate([np.sort(eigs_from(*_masses(model, tau, S, c))) for c in range(n)])
        for cl in clusters:
            if np.max(np.abs(cl["fp"] - fp) / (np.abs(cl["fp"]) + 1e-12)) < 1e-5 and abs(cl["V"] - v) < 1e-9 * (1 + abs(v)):
                cl["count"] += 1; break
        else:
            clusters.append(dict(V=v, tau=tau, S=S, fp=fp, count=1))
    clusters.sort(key=lambda c: c["V"])
    res = dict(menu=menu, n=n, mu2=mu2, m02=m02, lv=lv, tnorm=tnorm, snorm=snorm, n_starts=nstart, n_failed_starts=failed,
               n_distinct_minima=len(clusters),
               minima=[dict(V=c["V"], tau=[c["tau"].real, c["tau"].imag], count=c["count"]) for c in clusters[:6]])
    interior = [c for c in clusters if c["tau"].imag <= 6]
    cuspy = [c for c in clusters if c["tau"].imag > 6]
    if interior and cuspy:
        from model import mp_V
        cps = model.copies
        vi = mp_V(cps, mp.mpc(interior[0]["tau"]), [mp.mpc(z) for z in interior[0]["S"]], mp.mpf(mu2), mp.mpf(m02), 1, mp.mpf(lv))
        vc = mp_V(cps, mp.mpc(cuspy[0]["tau"]), [mp.mpc(z) for z in cuspy[0]["S"]], mp.mpf(mu2), mp.mpf(m02), 1, mp.mpf(lv))
        res_arb = dict(interior_numpy=interior[0]["V"], interior_mp=float(vi), cusp_numpy=cuspy[0]["V"], cusp_mp=float(vc),
                       cusp_tau=[cuspy[0]["tau"].real, cuspy[0]["tau"].imag], cusp_lower_mp=bool(vc < vi))
    else:
        res_arb = None
    if cuspy and (not interior or cuspy[0]["V"] < interior[0]["V"]):
        res["runaway"] = dict(V=cuspy[0]["V"], tau=[cuspy[0]["tau"].real, cuspy[0]["tau"].imag],
                              note="the lowest point found lies deep in the cusp (Im tau > 6): no interior global minimum")
    if interior:
        res.update(refine_and_classify(model, interior[0]))
        best = interior[0]
        if len(interior) > 1 and interior[1]["V"] - best["V"] < 1e-7 * (1 + abs(best["V"])):
            res["near_degenerate_second"] = dict(V=interior[1]["V"], tau=[interior[1]["tau"].real, interior[1]["tau"].imag])
    res["arbiter"] = res_arb
    res["seconds"] = round(time.time() - t0, 1)
    return res


def _masses(model, tau, S, c):
    A, D, W = model.pieces(tau)
    return A[c], D[c], float(np.abs(W[c] @ unit(S)) ** 2)


def grid_D():
    jobs = []; seed = 100
    for menu in ("Z", "H"):
        for n in range(1, 9):
            for mu2 in (0.3, 0.5, 0.8):
                for lv in (0.1, 0.3, 1.0):
                    seed += 1; jobs.append((menu, n, mu2, 0.01 * mu2, lv, 24, seed, "N", "sup"))
            seed += 1; jobs.append((menu, n, 0.5, 0.1 * 0.5, 0.3, 24, seed, "N", "sup"))          # m0 check
            seed += 1; jobs.append((menu, n, 0.5, 0.01 * 0.5, 0.3, 24, seed, "cusp", "cusp"))    # convention check
    return jobs


def sec_D(workers=1):
    jobs = grid_D()
    if workers > 1:
        import multiprocessing as mpr
        with mpr.get_context("spawn").Pool(workers) as pool:
            results = []
            for r in pool.imap_unordered(one_config, jobs):
                results.append(r); _log_cfg(r)
    else:
        results = []
        for j in jobs:
            r = one_config(j); results.append(r); _log_cfg(r)
    results.sort(key=lambda r: (r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"], r["lv"]))
    return dict(configs=results, summary=_summ_D(results))


def _log_cfg(r):
    if "best" not in r:
        print("  D %s n=%d mu2=%.2f lv=%.1f %s: no interior minimum; runaway %s" % (r["menu"], r["n"], r["mu2"], r["lv"], r["tnorm"],
              r.get("runaway")), flush=True)
        return
    b = r["best"]
    print("  D %s n=%d mu2=%.2f m02=%.4f lv=%.1f %s/%s: V=%.10f tau=%.6f+%.6fi iso=%s flat=%d neg=%d mirror=%s sym=%s "
          "free=%s [%d minima, %.0fs]%s" % (r["menu"], r["n"], r["mu2"], r["m02"], r["lv"], r["tnorm"], r["snorm"], b["V"],
          b["tau"][0], b["tau"][1], b["isolated"], b["n_flat"], b["n_negative"], b["mirror_fixed"], b["symmetric_point"],
          r.get("free_numbers", {}).get("rank"), r["n_distinct_minima"], r["seconds"],
          (" RUNAWAY below (V=%.6f at Im tau %.1f)" % (r["runaway"]["V"], r["runaway"]["tau"][1])) if "runaway" in r else ""), flush=True)


def _summ_D(results):
    summ = {}
    for r in results:
        key = "%s_%s_n%d" % (r["menu"], r["tnorm"], r["n"])
        s = summ.setdefault(key, dict(isolated=[], n_flat=[], mirror=[], sym=[], free_rank=[], runaway=[]))
        s["runaway"].append("runaway" in r)
        if "best" not in r:
            continue
        b = r["best"]
        s["isolated"].append(b["isolated"]); s["n_flat"].append(b["n_flat"]); s["mirror"].append(b["mirror_fixed"])
        s["sym"].append(b["symmetric_point"]); s["free_rank"].append(r.get("free_numbers", {}).get("rank"))
    return summ


# =============================================================================================== F  leading order
def sec_F():
    out = {}
    rng = np.random.default_rng(55)
    from scipy.optimize import minimize
    for menu in ("Z", "H"):
        rows = {}
        for n in range(1, 9):
            model = Model(make_copies(n, menu), 0.5, 0.005, 0.3)
            best = None
            for _ in range(16):
                x = rng.uniform(-0.5, 0.5); y = rng.uniform(np.sqrt(1 - x * x), 3.5)
                f = lambda p: model.V0(reduce_to_F(complex(p[0], p[1]), np.ones(3))[0]) if p[1] > 0.05 else 1e30
                r = minimize(f, [x, y], method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-16, maxiter=8000))
                if best is None or r.fun < best[0]:
                    best = (r.fun, r.x)
            t0 = reduce_to_F(complex(*best[1]), np.ones(3))[0]
            if t0.real < 0:
                t0 = -t0.conjugate()
            Qm = model.Q(t0) / model.lv ** 2
            ev, U = np.linalg.eigh(Qm)
            Sstar = U[:, 0]
            row = dict(tau0=[t0.real, t0.imag], V0=float(best[0]), Q_eigs=[float(e) for e in ev], S_star=[[c.real, c.imag] for c in Sstar])
            if n == 2:
                A, D, W = model.pieces(t0)
                cr = np.cross(W[0], W[1]); row["fs_S_star_vs_cross"] = fs_dist(Sstar, cr)
                row["c_coefs"] = [float(model.c_coef(a, d)) for a, d in zip(A, D)]
            # the exact vacua at small lambda v converge to it
            conv = []
            for lv in (0.1, 0.03, 0.01):
                mm = Model(make_copies(n, menu), 0.5, 0.005, lv)
                tau, S, v, r = local_min(mm, t0, Sstar)
                tau, S = canon(tau, S)
                conv.append(dict(lv=lv, dist_tau_hyp=float(abs(tau - t0) / t0.imag), fs_dist_S=fs_dist(S, Sstar),
                                 V_minus_V0=float(v - best[0])))
            row["exact_vs_leading"] = conv
            rows[n] = row
            print("  F %s n=%d tau0=%.6f+%.6fi Q eigs %s conv %s" % (menu, n, t0.real, t0.imag,
                  np.round(ev, 6), [(c["lv"], "%.1e" % c["dist_tau_hyp"], "%.1e" % c["fs_dist_S"]) for c in conv]), flush=True)
        out["menu_" + menu] = rows
    return out


# =============================================================================================== G  untied control
def sec_G():
    """the untied control: per-copy levels mu_i^2 and per-copy M_L, M_E chosen so that every singlet sits at its own
    exact minimiser u_i* at a planted tau_p (the joint level set then contains tau_p x {S : S^T Y3_i(tau_p) = 0})"""
    from search import u_star
    rng = np.random.default_rng(909)
    out = {}
    for n in (1, 2, 3):
        rows = []
        for trial in range(2):
            tau_p = complex(rng.uniform(-0.4, 0.4), rng.uniform(1.05, 1.8))
            cps = make_copies(n, "Z")
            base = Model(cps, 0.5, 0.005, 0.3)
            A, D, W = base.pieces(tau_p)
            mu2s = [float(v) for v in rng.uniform(0.3, 0.8, size=n)]
            us = [u_star(m, 0.01 * m) for m in mu2s]
            for i, c in enumerate(cps):                                         # per-copy M_L, M_E (untied)
                c.YL.c *= np.sqrt(us[i] / A[i]); c.YE.c *= np.sqrt(us[i] / D[i])
            um = Model(cps, 0.5, 0.005, 0.3); um.mu2s = mu2s; um.m0_ratio = 0.01
            bound = sum(3 * Ffun(u, m, 0.01 * m) for u, m in zip(us, mu2s))
            sols = []
            for _ in range(16):
                x = rng.uniform(-0.5, 0.5); y = rng.uniform(np.sqrt(1 - x * x), 3.0)
                tau, S, v, r = local_min(um, complex(x, y), rng.normal(size=3) + 1j * rng.normal(size=3))
                sols.append((v, tau, S))
            sols.sort(key=lambda t: t[0])
            v, tau, S = sols[0]
            mpm = MPModel(um, mp.mpc(tau), S); g = mpm.newton(it=8)
            cl = classify(mpm)
            tau = complex(mpm.tau0); S = np.array([complex(c) for c in mpm.S0])
            ta, Sa = canon(tau, S); tp_c = canon(tau_p, np.ones(3))[0]
            Vmp = f6(mpm.V([mp.mpf(0)] * 6))
            A2, D2, W2 = um.pieces(tau)
            rows.append(dict(tau_planted=[tau_p.real, tau_p.imag], V=Vmp, bound_all_at_level=bound,
                             V_minus_bound=Vmp - bound, at_joint_level_set=bool(abs(Vmp - bound) < 1e-12),
                             tau=[ta.real, ta.imag],
                             hyp_dist_to_planted=float(min(abs(ta - tp_c), abs(ta + tp_c.conjugate())) / tp_c.imag),
                             b2=[float(b) for b in np.abs(W2 @ unit(S)) ** 2], grad_inf=f6(g), **cl))
            print("  G n=%d trial %d: V-bound=%.3e at-level=%s n_flat=%d iso=%s hess=%s" % (n, trial, Vmp - bound,
                  rows[-1]["at_joint_level_set"], cl["n_flat"], cl["isolated"], np.round(cl["hess_eigs"], 10)), flush=True)
        out["n%d" % n] = rows
    out["reading"] = ("untied (per-copy levels): where the joint level set is non-empty it is the vacuum; its singlet "
                      "conditions cost one level each (two fix tau), its zero-mixing conditions S^T Y3_i(tau) = 0 cost none: "
                      "n = 1 leaves a CP^1 of directions (two flat directions), n = 2 a point; n = 3 is empty at a generic "
                      "planted tau (the three triplets' determinant does not vanish there) and the minimum is a compromise")
    return out


# =============================================================================================== H  symmetric configurations
def sec_H():
    out = {}
    w = complex(-0.5, np.sqrt(3) / 2)
    M3 = PMAT @ LINV
    ev, U = np.linalg.eig(M3)
    for menu in ("Z", "H"):
        rows = {}
        for n in range(1, 9):
            model = Model(make_copies(n, menu), 0.5, 0.005, 0.3)
            pts = [("i", 1j, np.array([1, -1, 0]) / np.sqrt(2))] + [("omega_%d" % k, w, U[:, k]) for k in range(3)]
            rr = []
            for name, tau, S in pts:
                mpm = MPModel(model, mp.mpc(tau), S)
                g = mpm.grad(mp.mpf("1e-10")); gn = max(abs(v) for v in g)
                cl = classify(mpm)
                rr.append(dict(point=name, S=[[c.real, c.imag] for c in unit(S)], V=f6(mpm.V([mp.mpf(0)] * 6)),
                               grad_inf=f6(gn), minimum=bool(cl["n_negative"] == 0 and cl["n_flat"] == 0),
                               hess_eigs=cl["hess_eigs"]))
            rows[n] = rr
            print("  H %s n=%d: %s" % (menu, n, [(r["point"], "%.9f" % r["V"], "%.0e" % r["grad_inf"], r["minimum"]) for r in rr]),
                  flush=True)
        out["menu_" + menu] = rows
    out["omega_stabiliser_action_P_Linv_eigenvalues"] = [[complex(e).real, complex(e).imag] for e in ev]
    return out


SECTIONS = dict(A=sec_A, B=sec_B, C=sec_C, D=sec_D, F=sec_F, G=sec_G, H=sec_H)

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    workers = 1
    if "--workers" in sys.argv:
        workers = int(sys.argv[sys.argv.index("--workers") + 1]); args = [a for a in args if a != str(workers)]
    want = args or list("ABCDFGH")
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    res["environment"] = env()
    res["data_free"] = "no measured number is read or compared; the script reads no file"
    for key in want:
        t0 = time.time(); print("== section", key, flush=True)
        r = SECTIONS[key](workers) if key == "D" else SECTIONS[key]()
        r["seconds"] = round(time.time() - t0, 1); res[key] = r
        OUT.write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
        print("== section %s done in %.0fs" % (key, r["seconds"]), flush=True)
    print("written", OUT.name)
