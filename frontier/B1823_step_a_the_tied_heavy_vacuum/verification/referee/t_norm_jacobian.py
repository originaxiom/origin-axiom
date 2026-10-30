"""How many free numbers move the vacuum once the tie's normalisation convention is not taken as given?
At an isolated vacuum x* (6 real coordinates: tau, and an exponential chart on CP^2), the implicit-function theorem gives
dx*/dp = -H^-1 d_p grad V for every continuous input p.  Inputs: the draft's three (log mu^2 at fixed m0^2, log m0^2,
log lambda v) and the 3n normalisation constants of the forms (log c of each singlet: a^2 or d^2 scale by c^2; log s of each
triplet: b^2 scales by s^2) -- exactly the ratios the tie fixes by convention.  The rank of the 6 x (3 + 3n) Jacobian is
the number of independent ways the vacuum moves when the convention is free; the draft's count is the rank of its first
three columns.  tau rows in hyperbolic units (/Im tau), S rows Fubini-Study (the exponential chart is orthonormal).
Referee's independent forms (ref_model.py) with the draft's constants.  -> t_norm_jacobian.json"""
import sys, pathlib, json, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import mpmath as mp
import ref_model as rm
from ref_helpers import draft_norms, exp_chart

mp.mp.dps = 30


def eig_closed(a2, d2, b2):
    s = a2 + b2 + d2
    disc = (a2 - d2) ** 2 + b2 * (2 * a2 + 2 * d2 + b2)
    sp = (s + mp.sqrt(disc)) / 2
    return a2, sp, (a2 * d2 / sp if sp > 0 else mp.mpf(0))


class Evaluator:
    def __init__(self, model, tau0, S0):
        self.m, self.tau0, self.S0 = model, tau0, rm.unit(S0)

    def V(self, x, p):
        """p = [dlog mu2, dlog m02, dlog lv] + [delta_singlet x 2n] + [delta_triplet x n]"""
        n = self.m.n
        tau = self.tau0 + x[0] + 1j * x[1]
        S = exp_chart(self.S0, x[2:6])
        A, D, W = self.m.pieces(tau)
        mu2 = self.m.mu2 * mp.exp(p[0]); m02 = self.m.m02 * mp.exp(p[1]); lvf = mp.exp(p[2])
        v = mp.mpf(0)
        for i in range(n):
            a2 = A[i] * mp.exp(2 * p[3 + 2 * i]); d2 = D[i] * mp.exp(2 * p[3 + 2 * i + 1])
            sfac = lvf * mp.exp(p[3 + 2 * n + i])
            b2 = abs(sfac * mp.fsum(W[i][k] * S[k] for k in range(3))) ** 2
            for u in eig_closed(a2, d2, b2):
                v += rm.Ffun(u, mu2, m02)
        return v


def jac(ev, npar, h=mp.mpf("1e-8"), k=mp.mpf("1e-6")):
    z6 = [mp.mpf(0)] * 6; zp = [mp.mpf(0)] * npar
    v0 = ev.V(z6, zp)
    H = mp.matrix(6, 6)
    for a in range(6):
        xp = list(z6); xm = list(z6); xp[a] = h; xm[a] = -h
        H[a, a] = (ev.V(xp, zp) - 2 * v0 + ev.V(xm, zp)) / h ** 2
        for b in range(a + 1, 6):
            vals = []
            for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                x = list(z6); x[a] = sa * h; x[b] = sb * h; vals.append(ev.V(x, zp))
            H[a, b] = H[b, a] = (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h * h)
    g = []
    for a in range(6):
        xp = list(z6); xm = list(z6); xp[a] = h; xm[a] = -h
        g.append((ev.V(xp, zp) - ev.V(xm, zp)) / (2 * h))
    M = mp.matrix(6, npar)
    for a in range(6):
        for j in range(npar):
            vals = []
            for sa, sb in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                x = list(z6); x[a] = sa * h; p = list(zp); p[j] = sb * k; vals.append(ev.V(x, p))
            M[a, j] = (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h * k)
    J = -(mp.inverse(H) * M)
    return H, J, g


def svals(J):
    s = mp.svd_r(J, compute_uv=False)
    return sorted([float(abs(v)) for v in s], reverse=True)


def rank(sv, rel=1e-6):
    return sum(1 for v in sv if v > rel * sv[0]) if sv and sv[0] > 0 else 0


if __name__ == "__main__":
    D = json.loads((HERE.parent / "step_a_v2.json").read_text())["D"]["configs"]
    sel = []
    for r in D:
        if "best" not in r or not r["best"]["isolated"] or r["tnorm"] != "N" or abs(r["m02"] / r["mu2"] - 0.01) > 1e-9:
            continue
        if r["n"] == 2 or (r["mu2"] == 0.5 and r["lv"] in (0.1, 0.3) and r["n"] in (3, 4, 5, 6, 8)):
            if "runaway" in r:
                continue
            sel.append(r)
    rows = []
    for r in sel:
        t0 = time.time()
        n = r["n"]; b = r["best"]
        sc, tc = draft_norms(r["menu"], n, r["tnorm"], r["snorm"])
        model = rm.RefModel(r["menu"], n, r["mu2"], r["m02"], r["lv"], sc, tc)
        ev = Evaluator(model, mp.mpc(*b["tau"]), [mp.mpc(*c) for c in b["S"]])
        npar = 3 + 3 * n
        H, J, g = jac(ev, npar)
        y = mp.mpf(b["tau"][1])
        Jg = mp.matrix(6, npar)
        for a in range(6):
            for j in range(npar):
                Jg[a, j] = J[a, j] / (y if a < 2 else 1)
        cols = lambda idx: mp.matrix([[Jg[a, j] for j in idx] for a in range(6)])
        sv_par = svals(cols(range(3))); sv_norm = svals(cols(range(3, npar))); sv_all = svals(Jg)
        sv_singlets = svals(cols(range(3, 3 + 2 * n))); sv_triplets = svals(cols(range(3 + 2 * n, npar)))
        speeds = [float(mp.sqrt(mp.fsum(Jg[a, j] ** 2 for a in range(6)))) for j in range(npar)]
        Sspeeds = [float(mp.sqrt(mp.fsum(Jg[a, j] ** 2 for a in range(2, 6)))) for j in range(npar)]
        Heig = sorted([float(e) for e in mp.eigsy(H)[0]])
        row = dict(menu=r["menu"], n=n, mu2=r["mu2"], lv=r["lv"], tau=b["tau"], mirror=b["mirror_fixed"],
                   grad_inf=float(max(abs(v) for v in g)), hess_eigs=Heig,
                   rank_draft_params=rank(sv_par), rank_normalisations=rank(sv_norm), rank_singlet_norms=rank(sv_singlets),
                   rank_triplet_norms=rank(sv_triplets), rank_all=rank(sv_all),
                   svals_draft_params=sv_par, svals_normalisations=sv_norm, svals_all=sv_all,
                   speed_per_efold=dict(log_mu2=speeds[0], log_m02=speeds[1], log_lv=speeds[2],
                                        singlets=speeds[3:3 + 2 * n], triplets=speeds[3 + 2 * n:]),
                   S_speed_per_efold=dict(log_mu2=Sspeeds[0], singlets=Sspeeds[3:3 + 2 * n], triplets=Sspeeds[3 + 2 * n:]),
                   draft_free_rank=r.get("free_numbers", {}).get("rank"),
                   draft_speed=r.get("free_numbers", {}).get("speed_per_param"),
                   seconds=round(time.time() - t0, 1))
        rows.append(row)
        print("%s n=%d mu2=%.1f lv=%.1f mirror=%s | grad %.1e | rank: draft params %d (draft %s), normalisations %d "
              "(singlets %d, triplets %d), all %d | svals_all %s | mu2 speed %.3f, max singlet %.3f, max triplet %.3f [%.0fs]" % (
                  r["menu"], n, r["mu2"], r["lv"], b["mirror_fixed"], row["grad_inf"], row["rank_draft_params"],
                  row["draft_free_rank"], row["rank_normalisations"], row["rank_singlet_norms"], row["rank_triplet_norms"],
                  row["rank_all"], ["%.2g" % v for v in sv_all], speeds[0], max(speeds[3:3 + 2 * n]),
                  max(speeds[3 + 2 * n:]), row["seconds"]), flush=True)
    (HERE / "t_norm_jacobian.json").write_text(json.dumps(dict(rows=rows), indent=1))
