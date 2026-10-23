"""B1739 (P-344): the frame's Higgs triplet is nearly null at hierarchy tau, and so the Standard Model's reading (S~ for the up
quarks, S for the down quarks and leptons) puts the lightest up and down states on nearly orthogonal lines.  No data.
  A  R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4) is exactly null, R.R = 0 (Jacobi's th3^4 = th2^4 + th4^4); the section the
     censuses use (B1691's components, DR) has h.h against eta^6/4 (P-308) and reality r = |h.h| / |h|^2 on a grid of tau
  B  the light state: at seeded points of B1726's grid, every sector and reading, the left singular vector of the smallest
     singular value of Y (B1736's closed form, checked against the frame) against conj(h) (reading S) and h (reading S~);
     and for u = 0 (Y = u1 [h]_x) the left null vector is conj(h) exactly
  D  why: rho(T)'s eigenlines (two of them null, (0, 1, +-i), one not, e_i), and the zero-free F_6 (B1731) on the same grid:
     F_6.F_6 = -48 eta^6 and its reality
  C  B1726's committed census: |V_ud| = sqrt(1 - |V_us|^2 - |V_ub|^2) by (up, down) reading and by Im tau, and its
     correlation with r(tau) under the mixed readings
    python3 -B the_higgs_is_nearly_null.py      # writes the_higgs_is_nearly_null.json beside itself
Importing computes nothing."""
import sys, io, json, math, random, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
_M = {}


def mods():
    if not _M:
        spec = importlib.util.spec_from_file_location("fg1739", ROOT / "frontier" / "B1736_the_family_group_is_the_frames_own" / "verification" / "the_family_group.py")
        FG = importlib.util.module_from_spec(spec); spec.loader.exec_module(FG); B = FG._b()
        P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"; sys.path.insert(0, str(P1691))
        s2 = importlib.util.spec_from_file_location("te1739", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(s2)
        with contextlib.redirect_stdout(io.StringIO()): s2.loader.exec_module(te)
        s3 = importlib.util.spec_from_file_location("c1739", ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.py")
        c26 = importlib.util.module_from_spec(s3); s3.loader.exec_module(c26)
        col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(encoding="utf-8"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
        _M.update(FG=FG, B=B, te=te, c26=c26, col=col)
    return _M


def higgs(t):
    import mpmath as mp
    te = mods()["te"]; return np.array([complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]])


def part_a():
    import mpmath as mp
    mp.mp.dps = 30
    q = lambda t: mp.exp(1j * mp.pi * t)
    th2 = lambda t: mp.jtheta(2, 0, q(t)); th3 = lambda t: mp.jtheta(3, 0, q(t)); th4 = lambda t: mp.jtheta(4, 0, q(t))
    eta = lambda t: mp.exp(2j * mp.pi * t / 24) * mp.nprod(lambda n: 1 - mp.exp(2j * mp.pi * n * t), [1, mp.inf])
    rows, rr = [], 0.0
    for re in (0.05, 0.35, 0.7):
        for im in (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0):
            t = complex(re, im); tm = mp.mpc(re, im)
            a, b, c = th2(tm), th3(tm), th4(tm); R = [-a * a, -c * c, 1j * b * b]
            rr = max(rr, float(abs(sum(x * x for x in R)) / sum(abs(x) ** 2 for x in R)))
            h = higgs(t); hh = complex(h @ h); e6 = complex(eta(tm) ** 6) / 4
            rows.append({"tau": [re, im], "reality_r": float(abs(hh) / np.vdot(h, h).real), "h.h_over_eta6/4": [abs(hh / e6), math.atan2((hh / e6).imag, (hh / e6).real) / (2 * math.pi)]})
    return {"R_reality_max_(Jacobi)": rr, "grid": rows}


def light_overlaps(n=24, seed=1739):
    M = mods(); FG, B, c26, col = M["FG"], M["B"], M["c26"], M["col"]
    rng = random.Random(seed); L = c26.lines(); P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    worst_closed, res = 0.0, {"S": [], "St": []}; null0 = 0.0
    for _ in range(n):
        re, im = rng.choice(c26.RE), rng.choice(c26.IM); a, b = rng.choice(L); t = complex(re, im); h = higgs(t)
        Lv = float(np.interp(im, [q[0] for q in col], [q[1] for q in col])); w = float(a) * t + float(b)
        for sec, (lf, rf) in {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}.items():
            x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
            u = np.array([(math.sqrt(2 * math.pi * Lv + c[s]) * R[s] if c[s] is not None and 2 * math.pi * Lv + c[s] > 0 else 0) for s in ("1", "i", "j", "k")])
            for rd, hh, target in (("S", h, np.conj(h)), ("St", np.conj(h), h)):
                Y = np.outer(u[1:], hh) + np.outer(hh, u[1:]) - (u[1:] @ hh) * np.eye(3) + u[0] * FG.cross(hh)
                S = hh[0] * B.QI + hh[1] * B.QJ + hh[2] * B.QK
                Yf = P @ B.coupling(S, B.weighted_M(dict(zip(("1", "i", "j", "k"), u)))) @ P.T
                worst_closed = max(worst_closed, float(np.abs(Y - Yf).max() / np.abs(Yf).max()))
                U = np.linalg.svd(Y)[0]
                res[rd].append(float(abs(np.vdot(target / np.linalg.norm(target), U[:, 2]))))
                if abs(u[0]) > 1e-12:                                   # u1 = 0 at B1716's residue zeros: Y0 = 0, no null line
                    Y0 = u[0] * FG.cross(hh); U0 = np.linalg.svd(Y0)[0]
                    null0 = max(null0, float(1 - abs(np.vdot(np.conj(hh) / np.linalg.norm(hh), U0[:, 2]))))
    return {"points": n, "closed_vs_frame_max_rel": worst_closed, "u=0: 1 - |<conj h, light>| max": null0,
            "overlap_light_with_conj_h_under_S": {q: float(np.quantile(res["S"], v)) for q, v in (("q10", 0.1), ("median", 0.5), ("q90", 0.9))},
            "overlap_light_with_h_under_St": {q: float(np.quantile(res["St"], v)) for q, v in (("q10", 0.1), ("median", 0.5), ("q90", 0.9))}}


def census_vud():
    V = ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.jsonl"
    acc = {}
    for l in V.read_text(encoding="utf-8").splitlines():
        if not l.strip(): continue
        r = json.loads(l)
        for h in ("L_max", "L_2"):
            for a in ("S", "St"):
                for b in ("S", "St"):
                    k = r["ckm|%s|%s|%s" % (h, a, b)]
                    acc.setdefault((a, b), []).append((math.sqrt(max(0.0, 1 - k[0] ** 2 - k[2] ** 2)), r["Im_tau"], r["Re_tau"]))
    out = {}
    for (a, b), v in acc.items():
        x = np.array([t[0] for t in v]); y = np.array([t[1] for t in v])
        bins = {f"{lo:.2f}-{lo + 0.5:.2f}": float(np.median(x[(y >= lo) & (y < lo + 0.5)])) for lo in (2.0, 2.5, 3.0)}
        out[f"up {a} / down {b}"] = {"rows": len(x), "median": float(np.median(x)), "fraction_above_0.9": float(np.mean(x > 0.9)), "median_by_Im_tau": bins}
    return out, acc


def part_d():
    import mpmath as mp
    mp.mp.dps = 30
    w = np.exp(1j * np.pi / 4); rT = w * np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    ev, V = np.linalg.eig(rT)
    lines = [{"phase/2pi": float(np.angle(ev[k]) / (2 * np.pi)), "v.v": float(abs(V[:, k] @ V[:, k]))} for k in range(3)]
    rows = []
    for im in (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0):
        t = mp.mpc(0.35, im); q = mp.exp(1j * mp.pi * t)
        a, b, c = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        eta = mp.exp(2j * mp.pi * t / 24) * mp.nprod(lambda n: 1 - mp.exp(2j * mp.pi * n * t), [1, mp.inf])
        F = [eta ** -3 * a ** 6, eta ** -3 * c ** 6, 1j * eta ** -3 * b ** 6]
        FF = sum(x * x for x in F)
        rows.append({"Im_tau": im, "F6_reality": float(abs(FF) / sum(abs(x) ** 2 for x in F)), "F6.F6/(-48 eta^6)": float(abs(FF / (-48 * eta ** 6)))})
    return {"rho_T_eigenlines": lines, "F6": rows}


def main():
    a = part_a(); print("A", json.dumps({k: v for k, v in a.items() if k != "grid"}))
    for r in a["grid"]: print("  ", r)
    b = light_overlaps(); print("B", json.dumps(b))
    c, acc = census_vud(); print("C", json.dumps(c, indent=1))
    # the correlation of the mixed readings' |V_ud| with r(tau) (r depends on tau only)
    taus = sorted({(t[2], t[1]) for t in acc[("St", "S")]}); rmap = {tt: float(abs(higgs(complex(*tt)) @ higgs(complex(*tt))) / np.vdot(higgs(complex(*tt)), higgs(complex(*tt))).real) for tt in taus}
    corr = {}
    for key in (("St", "S"), ("S", "St")):
        med = {tt: np.median([t[0] for t in acc[key] if (t[2], t[1]) == tt]) for tt in taus}
        xs = np.log([rmap[tt] for tt in taus]); ys = np.log([max(med[tt], 1e-6) for tt in taus])
        corr["up %s / down %s" % key] = {"log_correlation": float(np.corrcoef(xs, ys)[0, 1]), "slope_dlog_Vud_dlog_r": float(np.polyfit(xs, ys, 1)[0])}
    print("C-corr", corr)
    d = part_d(); print("D", json.dumps(d))
    json.dump({"A": a, "B": b, "C": c, "D": d, "C_log_correlation_median_Vud_vs_r": corr}, open(HERE / "the_higgs_is_nearly_null.json", "w"), indent=1)


if __name__ == "__main__":
    main()
