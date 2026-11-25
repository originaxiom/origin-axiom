"""B1980 part B rerun (main, 2026-11-25; data-free): the duality matching with the canonical end read covariantly, L at tau
carried into the fundamental domain (B1927), instead of frame C's code's Re-tau-only reduction. See ../CORRECTION_CARD.md.
    python3 -B duality_cov.py > duality_cov_run.txt"""
import sys, pathlib, json, time, math
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
FM = DL.FM; mp = DL.mp; B = DL.B; H = DL.H; f2m = DL.f2m
P96 = sorted((Fr(r["a"]), Fr(r["b"])) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text()))
E30 = [(Fr(j, 30), Fr(k, 30)) for j in range(30) for k in range(30) if (j, k) != (0, 0)]
KS = (2, 3, 5, 6, 10, 15, 30, 60, 900)

def parts_L(tx, ty, a, b, sec, L):
    """determinant_law.parts with the end L given (copied line for line; only L's source changed)"""
    mp.mp.dps = int(30 + 2 * ty)
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty)); y = mp.im(t); L = mp.mpf(L)
    eta = mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t)); t1p = 2 * mp.pi * eta ** 3
    th1 = lambda z: B.th_mp(1, z, t)
    c3 = [DL.te.ev(cc, t) for cc in DL.te.B[1]]; S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b); yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]; bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0])); kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    u = {}
    for s in FM.UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]): u[s] = 0; continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / t1p
        al, be = cs[s][0] - H, cs[s][1] - H; z = f2m(al) * t + f2m(be)
        a0 = 2 * I * mp.pi * f2m(al) + mp.diff(th1, z) / th1(z)
        c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L); arg = 2 * mp.pi * L + c
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    Mw = sum((u[s] * ED[s] for s in FM.UNITS), mp.zeros(2, 2))
    Ys = {}
    for rn, Sr in RD.items():
        Ys[rn] = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
    return RD, Mw, Ys, u, cs, ds

def fd(tx, ty):
    t = complex(float(tx), float(ty))
    for _ in range(200):
        t = complex(((t.real + 0.5) % 1.0) - 0.5, t.imag)
        if abs(t) < 1 - 1e-15: t = -1 / t
        else: break
    return t
def L_cov(tx, ty): return FM.CR.canon(fd(tx, ty))["L_2"]
def L_code(tx, ty): return FM.CR.canon(complex(((float(tx) + 0.5) % 1.0) - 0.5, float(ty)))["L_2"]

def outputs(arg):
    x, y, a, b, L = arg
    Y = {s: parts_L(x, y, a, b, s, L)[2]["S"] for s in ("up", "down", "lep")}
    o = []
    for s in ("up", "down", "lep"):
        sv = sorted(abs(v) for v in mp.svd_c(Y[s], compute_uv=False))
        o += [mp.log(sv[1] / sv[2]) if sv[1] > 0 else None, mp.log(sv[0] / sv[2]) if sv[0] > 0 else None]
    V = CM.U_of(Y["up"]).H * CM.U_of(Y["down"])
    o += [mp.log(abs(V[i, j])) if abs(V[i, j]) > 0 else None for (i, j) in ((0, 1), (1, 2), (0, 2))]
    return [None if v is None else float(v) for v in o]
def table(y, pts, pool):
    L = L_cov("0", y)
    return dict(zip(pts, pool.map(outputs, [("0", y, a, b, L) for (a, b) in pts], chunksize=8)))
def dist(u, v):
    m = 0.0
    for p, q in zip(u, v):
        if (p is None) != (q is None): return math.inf
        if p is not None: m = max(m, abs(p - q) / max(1.0, abs(p)))
    return m
def match(src, par):
    ds = sorted(min(dist(u, v) for v in par.values()) for u in src.values())
    return ds[-1], ds[len(ds) // 2]
if __name__ == "__main__":
    t0 = time.time()
    worst = 0
    for (a, b) in P96[:12]:
        for s in ("up", "down", "lep"):
            for y in (1.5, 0.4):
                A = DL.parts("0", y, a, b, s)[2]["S"]; Bm = parts_L("0", y, a, b, s, L_code("0", y))[2]["S"]
                worst = max(worst, max(abs(A[i, j] - Bm[i, j]) for i in range(3) for j in range(3)))
    print("K0 (the copied frame against parts, same end, 12 points x 3 sectors x 2 heights): largest difference %.1e" % worst, flush=True)
    print("the end on the axis: L_code(0.4i) = %.6f, L_cov(0.4i) = %.6f, L(2.5i) = %.6f" % (L_code("0", 0.4), L_cov("0", 0.4), L_code("0", 2.5)), flush=True)
    res = {}
    with Pool(6) as pool:
        for (y, yp) in ((1.25, 0.8), (1.5, 1 / 1.5), (2.5, 0.4)):
            big, med = match(table(y, P96, pool), table(yp, E30, pool)); res[("S", y)] = big
            print("S move, covariant end: height %.4f against %.4f: largest d %.1e, median %.1e  [%.0f s]" % (y, yp, big, med, time.time() - t0), flush=True)
        for K in KS:
            for f in (1.5, 2.5):
                y = f * math.sqrt(K); yp = K / y
                big, med = match(table(y, P96, pool), table(yp, E30, pool)); res[(K, f)] = big
                print("K = %d, covariant end: height %.4f against %.4f: largest d %.1e, median %.1e  [%.0f s]" % (K, y, yp, big, med, time.time() - t0), flush=True)
    print("SUMMARY K0 passes: %s" % (worst < 1e-25))
    print("SUMMARY S-cov (plain matching) passes: %s" % all(res[("S", y)] < 1e-8 for y in (1.25, 1.5, 2.5)))
    print("SUMMARY F-cov: K passing with the covariant end: %s" % [K for K in KS if all(res[(K, f)] < 1e-8 for f in (1.5, 2.5))])
