"""Main's own check of the referee's B2 (Step A v2), on the DRAFT's code (step_a_v2.MPModel.pieces: the sup/N-normalised
forms at 30 digits), not the referee's: the decoupling-limit vacuum (tau0* = argmin V0 by Newton in mpmath; S* = the
lowest eigenvector of Q(tau0*)) differentiated with respect to log mu^2 (m0^2/mu^2 held), the 2n singlet constants and
the n triplet constants that the 'tie' fixes by convention.  Central differences (h = 1e-8), tau in hyperbolic units
(d tau / Im tau), S in Fubini-Study tangent coordinates; 40 digits, Newton's finite-difference step 1e-13.  Ranks at a relative threshold of 1e-6.  Menu Z: n = 2 (on the
mirror line Re tau = 1/2) and n = 5 (off the mirror lines), at mu^2 = 0.5, m0^2 = 0.005 (the draft's decoupling point).
A first version minimised with Nelder-Mead in double precision; it stalled at the iteration cap (about 1e-9 in tau, too
coarse for the rank) and was stopped before printing anything.  Data-free."""
import sys, pathlib, json
import numpy as np
import mpmath as mp
D = pathlib.Path(__file__).resolve().parents[1]          # the arc's verification/: the draft's code
sys.path.insert(0, str(D))
import step_a_v2 as sa                       # importing runs nothing (its sections sit under __main__)
from model import mp_F
from search import Model, make_copies
mp.mp.dps = 40


def Fp(u, mu2, m02):
    return 2 * (u + m02) * mp.log((u + m02) / mu2) - 2 * u * mp.log(u / mu2) - 2 * m02


def c_coef(a2, d2, mu2, m02):
    G = lambda x: x * Fp(x, mu2, m02)
    if abs(a2 - d2) < mp.mpf(10) ** -20 * max(a2, d2):
        h = a2 * mp.mpf(10) ** -10
        return (G(a2 + h) - G(a2 - h)) / (2 * h)
    return (G(a2) - G(d2)) / (a2 - d2)


class Dec:
    def __init__(self, copies, n, guess):
        self.n = n
        self.mpm = sa.MPModel(Model(copies, 0.5, 0.005, 0.3), guess, np.ones(3, dtype=complex) / np.sqrt(3))

    def V0(self, tau, dmu, dS):
        mu2 = mp.mpf("0.5") * mp.exp(dmu); m02 = mp.mpf("0.005") * mp.exp(dmu)
        A, Dd, W = self.mpm.pieces(tau)
        return mp.fsum(2 * mp_F(A[i] * mp.exp(2 * dS[2 * i]), mu2, m02) + mp_F(Dd[i] * mp.exp(2 * dS[2 * i + 1]), mu2, m02)
                       for i in range(self.n))

    def tau0(self, start, dmu, dS, h=mp.mpf("1e-13")):
        t = mp.mpc(start); last = None
        for _ in range(60):
            f = lambda x, y: self.V0(t + x + 1j * y, dmu, dS)
            f0 = f(0, 0); fx1, fx2, fy1, fy2 = f(h, 0), f(-h, 0), f(0, h), f(0, -h)
            gx = (fx1 - fx2) / (2 * h); gy = (fy1 - fy2) / (2 * h)
            hxx = (fx1 - 2 * f0 + fx2) / h ** 2; hyy = (fy1 - 2 * f0 + fy2) / h ** 2
            hxy = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
            det = hxx * hyy - hxy ** 2
            dx = -(hyy * gx - hxy * gy) / det; dy = -(-hxy * gx + hxx * gy) / det
            t = t + dx + 1j * dy
            last = max(abs(dx), abs(dy))
            if last < mp.mpf(10) ** -24:
                return t, (hxx, hyy, det)
        if last < mp.mpf(10) ** -20:          # the floor of the finite-difference gradient at 40 digits
            return t, (hxx, hyy, det)
        raise RuntimeError("Newton did not converge: last step %s" % mp.nstr(last, 3))

    def S_low(self, tau, dmu, dS, dT):
        mu2 = mp.mpf("0.5") * mp.exp(dmu); m02 = mp.mpf("0.005") * mp.exp(dmu)
        A, Dd, W = self.mpm.pieces(tau); Q = mp.zeros(3, 3)
        for i in range(self.n):
            c = c_coef(A[i] * mp.exp(2 * dS[2 * i]), Dd[i] * mp.exp(2 * dS[2 * i + 1]), mu2, m02)
            w = [W[i][k] * mp.exp(dT[i]) for k in range(3)]
            for a in range(3):
                for b in range(3):
                    Q[a, b] += c * mp.conj(w[a]) * w[b]
        E, U = mp.eighe(Q)
        k = min(range(3), key=lambda j: mp.re(E[j]))
        return [U[a, k] for a in range(3)], [mp.re(E[j]) for j in range(3)]


def coords(t, S, t0, S0, e1, e2):
    ov = sum(mp.conj(S0[k]) * S[k] for k in range(3)); S = [S[k] * mp.conj(ov) / abs(ov) for k in range(3)]
    d = [S[k] - S0[k] for k in range(3)]
    p1 = sum(mp.conj(e1[k]) * d[k] for k in range(3)); p2 = sum(mp.conj(e2[k]) * d[k] for k in range(3))
    return [mp.re(t - t0) / mp.im(t0), mp.im(t - t0) / mp.im(t0), mp.re(p1), mp.im(p1), mp.re(p2), mp.im(p2)]


def complement(S0):
    basis = []
    for v in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        v = [mp.mpc(x) for x in v]
        pr = sum(mp.conj(S0[k]) * v[k] for k in range(3)); v = [v[k] - pr * S0[k] for k in range(3)]
        for b in basis:
            pr = sum(mp.conj(b[k]) * v[k] for k in range(3)); v = [v[k] - pr * b[k] for k in range(3)]
        nv = mp.sqrt(sum(abs(x) ** 2 for x in v))
        if nv > mp.mpf("1e-6"):
            basis.append([x / nv for x in v])
    return basis[:2]


out = {}
for n, guess in ((2, complex(0.5, 1.244)), (5, complex(0.3262, 1.3187))):
    copies = make_copies(n, "Z", "N", "sup"); dec = Dec(copies, n, guess)
    z = [mp.mpf(0)] * (2 * n); zT = [mp.mpf(0)] * n
    t0, hes = dec.tau0(guess, mp.mpf(0), z)
    S0, ev0 = dec.S_low(t0, mp.mpf(0), z, zT); e1, e2 = complement(S0)
    v_np = Model(copies, 0.5, 0.005, 0.3).V0(complex(t0))
    h = mp.mpf("1e-8"); cols = []; names = ["log mu2"] + ["singlet %d" % k for k in range(2 * n)] + ["triplet %d" % k for k in range(n)]
    for name in names:
        xs = []
        for sg in (1, -1):
            dmu, dS, dT = mp.mpf(0), list(z), list(zT)
            if name == "log mu2":
                dmu = sg * h
            elif name.startswith("singlet"):
                dS[int(name.split()[1])] = sg * h
            else:
                dT[int(name.split()[1])] = sg * h
            t, _ = dec.tau0(t0, dmu, dS)
            S, _ = dec.S_low(t, dmu, dS, dT)
            xs.append(coords(t, S, t0, S0, e1, e2))
        cols.append([float((xs[0][k] - xs[1][k]) / (2 * h)) for k in range(6)])
    J = np.array(cols).T
    sv_mu = np.linalg.svd(J[:, :1], compute_uv=False); sv = np.linalg.svd(J, compute_uv=False)
    rank = lambda s: int((s > 1e-6 * s[0]).sum())
    row = dict(tau0=[float(mp.re(t0)), float(mp.im(t0))], V0_mp=float(dec.V0(t0, 0, z)), V0_numpy=float(v_np),
               Q_eigs=[float(x) for x in ev0], sv_all=[float(x) for x in sv], rank_mu=rank(sv_mu), rank_all=rank(sv))
    if n == 2:
        A, Dd, W = dec.mpm.pieces(t0)
        cr = [W[0][1] * W[1][2] - W[0][2] * W[1][1], W[0][2] * W[1][0] - W[0][0] * W[1][2], W[0][0] * W[1][1] - W[0][1] * W[1][0]]
        ncr = mp.sqrt(sum(abs(x) ** 2 for x in cr)); ov = abs(sum(mp.conj(S0[k]) * cr[k] for k in range(3))) / ncr
        row["one_minus_overlap_S_with_W1xW2"] = float(1 - ov)   # W_i^T S = 0 (bilinear) for both copies: S is W1 x W2 itself
    out["Z n=%d" % n] = row
    print("Z n=%d tau0* = %.6f%+.6fi  V0 mp %.12f numpy %.12f  rank(mu) %d  rank(all) %d  svals %s %s" % (
        n, row["tau0"][0], row["tau0"][1], row["V0_mp"], row["V0_numpy"], row["rank_mu"], row["rank_all"],
        " ".join("%.2g" % x for x in sv), ("  1-|<S*, W1 x W2>| = %.1e" % row["one_minus_overlap_S_with_W1xW2"]) if n == 2 else ""), flush=True)
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
