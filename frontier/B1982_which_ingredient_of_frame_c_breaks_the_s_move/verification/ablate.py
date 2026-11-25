"""B1982 (main, 2026-11-25; data-free): which ingredient of frame C breaks the S move. Frame C (determinant_law.parts, copied
in B1980's duality_cov.parts_L) with switches: the norm factor, kappa's point-dependent phase, the a0 term, the Higgs. Each
variant is tested under S with the covariant end, plain matching, at 1.5/(2/3) and 2.5/0.4. See ../CARD.md.
    python3 -B ablate.py > ablate_run.txt"""
import sys, pathlib, json, time, math
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1980_*")) / "verification"))
import duality_cov as D
DL = D.DL; FM = D.FM; mp = D.mp; B = D.B; H = D.H; f2m = D.f2m; CM = D.CM
VARIANTS = {"V0": dict(norm=True, phase=True, a0=True, higgs="frame"), "V1": dict(norm=False, phase=True, a0=True, higgs="frame"),
            "V2": dict(norm=False, phase=False, a0=True, higgs="frame"), "V3": dict(norm=True, phase=True, a0=False, higgs="frame"),
            "V4": dict(norm=True, phase=False, a0=True, higgs="frame"), "V5": dict(norm=False, phase=False, a0=True, higgs="const"),
            "V6": dict(norm=True, phase=True, a0=True, higgs="const")}
def Y_variant(tx, ty, a, b, sec, L, v):
    mp.mp.dps = int(30 + 2 * ty)
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty)); y = mp.im(t); L = mp.mpf(L)
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    th1 = lambda z: B.th_mp(1, z, t)
    c3 = [DL.te.ev(cc, t) for cc in DL.te.B[1]] if v["higgs"] == "frame" else [mp.mpf(1)] * 3
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])) if v["phase"] else mp.mpf(1)
    kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    u = {}
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): u[s] = 0; continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
        if not v["norm"]:
            u[s] = R; continue
        al, be = cs[s][0] - H, cs[s][1] - H; z = f2m(al) * t + f2m(be)
        c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        if v["a0"]:
            a0 = 2 * I * mp.pi * f2m(al) + mp.diff(th1, z) / th1(z); c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
        arg = 2 * mp.pi * L + c
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    Mw = sum((u[s] * ED[s] for s in FM.UNITS), mp.zeros(2, 2))
    return mp.matrix([[sum(((Ca.T * EPS * S * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
def outputs(arg):
    x, y, a, b, L, vname = arg; v = VARIANTS[vname]
    Y = {s: Y_variant(x, y, a, b, s, L, v) for s in ("up", "down", "lep")}
    o = []
    for s in ("up", "down", "lep"):
        sv = sorted(abs(w) for w in mp.svd_c(Y[s], compute_uv=False))
        o += [mp.log(sv[1] / sv[2]) if sv[1] > 0 else None, mp.log(sv[0] / sv[2]) if sv[0] > 0 else None]
    V = CM.U_of(Y["up"]).H * CM.U_of(Y["down"])
    o += [mp.log(abs(V[i, j])) if abs(V[i, j]) > 0 else None for (i, j) in ((0, 1), (1, 2), (0, 2))]
    return [None if w is None else float(w) for w in o]
if __name__ == "__main__":
    t0 = time.time(); res = {}
    with Pool(6) as pool:
        for vname in VARIANTS:
            r = []
            for (y, yp) in ((1.5, 1 / 1.5), (2.5, 0.4)):
                Ls, Lp = D.L_cov("0", y), D.L_cov("0", yp)
                src = dict(zip(D.P96, pool.map(outputs, [("0", y, a, b, Ls, vname) for (a, b) in D.P96], chunksize=8)))
                par = dict(zip(D.E30, pool.map(outputs, [("0", yp, a, b, Lp, vname) for (a, b) in D.E30], chunksize=8)))
                big, med = D.match(src, par); r.append(big)
                print("%s %s: S move %.4f against %.4f: largest d %.1e, median %.1e  [%.0f s]" % (vname, VARIANTS[vname], y, yp, big, med, time.time() - t0), flush=True)
            res[vname] = r
    print("SUMMARY E0: V0 reproduces B1980 (0.18 and 0.32 within 1e-2): %s %s" % (abs(res["V0"][0] - 0.18) < 1e-2 and abs(res["V0"][1] - 0.32) < 1.5e-2, ["%.4f" % x for x in res["V0"]]))
    print("SUMMARY variants passing S (largest d < 1e-8 at both pairs): %s" % [k for k in VARIANTS if all(x < 1e-8 for x in res[k])])
    print("SUMMARY the variants ranked by their worse distance: %s" % sorted((round(max(res[k]), 4), k) for k in VARIANTS))
