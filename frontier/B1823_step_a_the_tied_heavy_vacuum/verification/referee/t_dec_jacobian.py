"""The decoupling-limit vacuum (lambda v -> 0; analysis_leading.py's object): tau0* = argmin V0 (singlets only) and
S0* = the lowest eigenvector of Q(tau0*) = sum_i c_i conj(W_i) W_i^T, c_i = (G(a_i^2) - G(d_i^2))/(a_i^2 - d_i^2).
The draft: it moves with mu^2/M^2 alone at leading order ('one leading free number').  Here: its Jacobian with respect to
log mu^2 AND the 3n normalisation constants the tie fixes by convention (2n singlets, n triplets), by central differences
(each perturbed vacuum re-solved: Newton on V0 in mpmath, then the eigenvector), in hyperbolic (tau) and Fubini-Study (S)
units.  rank(mu column) = 1 by construction; rank(all) = how many numbers move the leading-order vacuum once the
convention is free.  Referee's forms (ref_model.py), the draft's constants.  -> t_dec_jacobian.json"""
import sys, pathlib, json, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import mpmath as mp
import ref_model as rm
from ref_helpers import draft_norms

mp.mp.dps = 25


def G(x, mu2, m02):
    return x * rm.Fprime(x, mu2, m02)


def c_coef(a2, d2, mu2, m02):
    if abs(a2 - d2) < mp.mpf(10) ** -15 * max(a2, d2):
        h = a2 * mp.mpf(10) ** -8
        return (G(a2 + h, mu2, m02) - G(a2 - h, mu2, m02)) / (2 * h)
    return (G(a2, mu2, m02) - G(d2, mu2, m02)) / (a2 - d2)


class Dec:
    def __init__(self, menu, n, mu2, m02, sc, tc):
        self.menu, self.n = menu, n
        self.mu2, self.m02 = mp.mpf(mu2), mp.mpf(m02)
        self.sc, self.tc = [mp.mpf(c) for c in sc], [mp.mpf(c) for c in tc]
        self.cache = {}

    def sing(self, tau):
        key = ("s", mp.nstr(mp.re(tau), 30), mp.nstr(mp.im(tau), 30))
        if key not in self.cache:
            et = rm.eta(tau); E = rm.eisenstein(tau); y2 = 2 * mp.im(tau)
            vals = []
            for i in range(2 * self.n):
                spr = rm.SINGLETS[i]
                vals.append(y2 ** rm.sweight(*spr) * abs(rm.singlet(*spr, tau, et, E)) ** 2)
            self.cache[key] = vals
        return self.cache[key]

    def trip(self, tau):
        key = ("t", mp.nstr(mp.re(tau), 30), mp.nstr(mp.im(tau), 30))
        if key not in self.cache:
            et = rm.eta(tau); y2 = 2 * mp.im(tau); out = []
            for i in range(self.n):
                kind, a = rm.MENU[self.menu][i]
                v = rm.triplet_value(kind, a, tau, et)
                out.append([y2 ** (mp.mpf(3) / 4) * c for c in v])
            self.cache[key] = out
        return self.cache[key]

    def V0(self, tau, dmu, dS):
        mu2 = self.mu2 * mp.exp(dmu); s = self.sing(tau); v = mp.mpf(0)
        for i in range(self.n):
            a2 = s[2 * i] * (self.sc[2 * i] * mp.exp(dS[2 * i])) ** 2
            d2 = s[2 * i + 1] * (self.sc[2 * i + 1] * mp.exp(dS[2 * i + 1])) ** 2
            v += 2 * rm.Ffun(a2, mu2, self.m02) + rm.Ffun(d2, mu2, self.m02)
        return v

    def tau0(self, start, dmu, dS, it=30, h=mp.mpf("1e-7")):
        t = mp.mpc(start)
        for _ in range(it):
            f = lambda x, y: self.V0(t + x + 1j * y, dmu, dS)
            f0 = f(0, 0)
            gx = (f(h, 0) - f(-h, 0)) / (2 * h); gy = (f(0, h) - f(0, -h)) / (2 * h)
            hxx = (f(h, 0) - 2 * f0 + f(-h, 0)) / h ** 2; hyy = (f(0, h) - 2 * f0 + f(0, -h)) / h ** 2
            hxy = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
            det = hxx * hyy - hxy ** 2
            dx = -(hyy * gx - hxy * gy) / det; dy = -(-hxy * gx + hxx * gy) / det
            t = t + dx + 1j * dy
            if max(abs(dx), abs(dy)) < mp.mpf("1e-17"):
                break
        return t, (hxx, hyy, hxy)

    def S0(self, tau, dmu, dS, dT):
        mu2 = self.mu2 * mp.exp(dmu); s = self.sing(tau); W = self.trip(tau)
        Q = mp.matrix(3, 3)
        for i in range(self.n):
            a2 = s[2 * i] * (self.sc[2 * i] * mp.exp(dS[2 * i])) ** 2
            d2 = s[2 * i + 1] * (self.sc[2 * i + 1] * mp.exp(dS[2 * i + 1])) ** 2
            c = c_coef(a2, d2, mu2, self.m02) * (self.tc[i] * mp.exp(dT[i])) ** 2
            for j in range(3):
                for k in range(3):
                    Q[j, k] += c * mp.conj(W[i][j]) * W[i][k]
        E, U = mp.eighe(Q)
        order = sorted(range(3), key=lambda k: mp.re(E[k]))
        k0 = order[0]
        v = [U[j, k0] for j in range(3)]
        kk = max(range(3), key=lambda j: abs(v[j])); ph = abs(v[kk]) / v[kk]
        return [ph * c for c in v], [mp.re(E[k]) for k in order]


def tangent(S0, S1):
    """S1 - S0 projected on T_{S0} CP^2 (phases aligned), as 4 real numbers in an orthonormal basis"""
    ov = mp.fsum(mp.conj(S0[k]) * S1[k] for k in range(3))
    S1 = [S1[k] * abs(ov) / ov for k in range(3)]
    d = [S1[k] - S0[k] for k in range(3)]
    ov2 = mp.fsum(mp.conj(S0[k]) * d[k] for k in range(3))
    d = [d[k] - ov2 * S0[k] for k in range(3)]
    basis = []
    for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        v = [mp.mpc(c) for c in e]
        for b in [S0] + basis:
            o = mp.fsum(mp.conj(b[k]) * v[k] for k in range(3)); v = [v[k] - o * b[k] for k in range(3)]
        nv = mp.sqrt(mp.fsum(abs(c) ** 2 for c in v))
        if nv > mp.mpf("1e-8"):
            basis.append([c / nv for c in v])
        if len(basis) == 2:
            break
    out = []
    for b in basis:
        z = mp.fsum(mp.conj(b[k]) * d[k] for k in range(3)); out += [mp.re(z), mp.im(z)]
    return out


if __name__ == "__main__":
    lead = {m: json.loads((HERE.parent / ("analysis_leading_%s.json" % m)).read_text())["menu_" + m] for m in ("Z", "H")}
    rows = []
    eps = mp.mpf("1e-5")
    for menu in ("Z", "H"):
        for n in range(2, 9):
            t0c = time.time()
            sc, tc = draft_norms(menu, n, "N", "sup")
            dec = Dec(menu, n, 0.5, 0.005, sc, tc)
            start = mp.mpc(*lead["Z"][str(n)]["tau0"])            # the menus share their singlets: one tau0* per n
            zS = [mp.mpf(0)] * (2 * n); zT = [mp.mpf(0)] * n
            tb, hs = dec.tau0(start, 0, zS)
            Sb, Eb = dec.S0(tb, 0, zS, zT)
            y = mp.im(tb)
            cols = []; labels = []
            def solve(dmu, dS, dT):
                t, _ = dec.tau0(tb, dmu, dS); S, _ = dec.S0(t, dmu, dS, dT); return t, S
            perts = [("log mu2", (eps, zS, zT), (-eps, zS, zT))]
            for j in range(2 * n):
                p = list(zS); m_ = list(zS); p[j] = eps; m_[j] = -eps
                perts.append(("singlet %d" % j, (0, p, zT), (0, m_, zT)))
            for j in range(n):
                p = list(zT); m_ = list(zT); p[j] = eps; m_[j] = -eps
                perts.append(("triplet %d" % j, (0, zS, p), (0, zS, m_)))
            for lab, pp, pm in perts:
                tp, Sp = solve(*pp); tm, Sm = solve(*pm)
                dtau = (tp - tm) / (2 * eps) / y
                dS = [(a - b) / (2 * eps) for a, b in zip(tangent(Sb, Sp), tangent(Sb, Sm))]
                cols.append([mp.re(dtau), mp.im(dtau)] + dS); labels.append(lab)
            J = mp.matrix([[cols[j][a] for j in range(len(cols))] for a in range(6)])
            sv = sorted([float(abs(v)) for v in mp.svd_r(J, compute_uv=False)], reverse=True)
            rk = sum(1 for v in sv if v > 1e-6 * sv[0])
            Jn = mp.matrix([[cols[j][a] for j in range(1, len(cols))] for a in range(6)])
            svn = sorted([float(abs(v)) for v in mp.svd_r(Jn, compute_uv=False)], reverse=True)
            rkn = sum(1 for v in svn if v > 1e-6 * svn[0])
            sp = {lab: float(mp.sqrt(mp.fsum(c ** 2 for c in col))) for lab, col in zip(labels, cols)}
            row = dict(menu=menu, n=n, tau0=[float(mp.re(tb)), float(mp.im(tb))], Q_eigs=[float(e) for e in Eb],
                       on_mirror_line=bool(abs(mp.re(tb)) < 1e-9 or abs(abs(mp.re(tb)) - 0.5) < 1e-9 or abs(abs(tb) - 1) < 1e-9),
                       rank_mu_only=1, rank_normalisations=rkn, rank_all=rk, svals_all=sv, svals_normalisations=svn,
                       speed_per_efold=sp, seconds=round(time.time() - t0c, 1))
            rows.append(row)
            print("%s n=%d tau0*=%.6f%+.6fi on-line=%s | rank: mu 1, normalisations %d, all %d | svals %s | speeds mu %.3f, "
                  "singlets max %.3f, triplets max %.3f [%.0fs]" % (menu, n, row["tau0"][0], row["tau0"][1], row["on_mirror_line"],
                  rkn, rk, ["%.2g" % v for v in sv], sp["log mu2"], max(v for k, v in sp.items() if k.startswith("singlet")),
                  max(v for k, v in sp.items() if k.startswith("triplet")), row["seconds"]), flush=True)
    (HERE / "t_dec_jacobian.json").write_text(json.dumps(dict(rows=rows), indent=1))
