"""P-323, THE STRONG ANGLE IN THE MASS FRAME: the script of the sealed rule P323_RULE.md (this directory; sealed and pushed
at f53115e19 before this script existed).  Data-free.  Two stages:
    python3 -B p323_strong_angle.py --census [--workers 2] [--max-seconds 6300]
        the census, resumable: per task (line, centre) the 13 stencil points, and per calibration task one point; per point
        the residues R_s and the norms c_s of the up and down sectors (main's residues() and cA(), called as channels() calls
        them), L at both horocycles and the ten Higgs directions; at the end the read-out rows.  Chunks in chunks_p323/
        (git-ignored); when every task is done they are combined into p323_census.npz and p323_census_index.json.  Prints
        progress counts only.
    python3 -B p323_strong_angle.py --cells
        the cells, from p323_census.npz: writes p323_cells.json and prints the cells (redirect to p323_cells_run.txt).
The frame: main's B1720 instrument at 3412bf09d, unchanged, through this seat's route_b_scan.py and zero_free_census.py."""
import contextlib, importlib.util, io, json, math, os, sys, time, pathlib, subprocess
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
CH = HERE / "chunks_p323"
OUT_CENSUS, OUT_INDEX = HERE / "p323_census.npz", HERE / "p323_census_index.json"
_G = {}


def frame():
    """this seat's loader of main's instrument (as e20); importing it computes nothing"""
    if "zfc" not in _G:
        argv = sys.argv; sys.argv = ["x"]
        sp = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py"); zfc = importlib.util.module_from_spec(sp)
        with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(zfc)
        sys.argv = argv
        _G.update(zfc=zfc, rbs=zfc.rbs, B=zfc.B, tic=zfc.tic, TC=zfc.tic.TC)
    return _G


UNITS = ("1", "i", "j", "k")
HIGGS = ["dR"] + ["F_%d" % a for a in (-10, 14, 26, -6, 6, 18, -2, 10, 22)]
CAL_HIGGS = ["dR", "F_6", "F_22"]
CENTRES = [(0.15, 2.375), (0.15, 2.875), (0.15, 3.375), (0.65, 2.375), (0.65, 2.875), (0.65, 3.375)]
R1, R2 = 0.08, 0.04
HEX = [complex(math.cos(math.pi * k / 3), math.sin(math.pi * k / 3)) for k in range(6)]
HORS = ("L_max", "L_2")
READINGS = {"St,S": (1, 0), "S,St": (0, 1), "S,S": (0, 0), "St,St": (1, 1)}     # (up, down): 1 = S~ = S(conj h), 0 = S(h)
PHASE_FREE = ("St,S", "S,St")
SM = "St,S"
T_SHIFT = 19 * math.pi / 50
PERT, NPERT = 1e-12, 4


def stencil(c):
    z = complex(*c)
    return [z] + [z + R1 * e for e in HEX] + [z + R2 * e for e in HEX]


def lines():
    """B1713's 266 lines (tic.LINES) and the 30 lines of slope 2/5 at orders 25 and 30 (B1786's class)"""
    t = frame()["tic"]
    out = [(Fr(a), Fr(b)) for (_t, a, b) in t.LINES]
    assert len(out) == 266
    extra = [(Fr(2, 5), Fr(k, 25)) for k in range(1, 25) if k % 5 != 0]
    extra += [(Fr(2, 5), Fr(k, 30)) for k in range(1, 30) if math.gcd(k, 6) == 1]
    assert len(extra) == 30 and not set(extra) & set(out)
    return out + extra


def ten():
    """the ten (2/5, k/10) lines' indices in lines()"""
    L = lines()
    return [L.index((Fr(2, 5), Fr(k, 10))) for k in range(10)]


def point_data(a, b, tau):
    """per point: R and c of the up and down sectors (as channels() computes them), L at both horocycles, the Higgs"""
    g = frame(); B, TC, zfc = g["B"], g["TC"], g["zfc"]
    w = float(a) * tau + float(b)
    R = np.zeros((2, 4), complex); C = np.full((2, 4), np.nan)
    for i, (lf, rf) in enumerate((("Q", "u"), ("Q", "d"))):
        x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, tau); c = B.cA(x, yy, tau, Rr)
        for j, s in enumerate(UNITS):
            R[i, j] = Rr[s]
            if c[s] is not None: C[i, j] = c[s]
    L = np.array([TC.L_of(tau.imag, h) for h in HORS])
    H = np.array([zfc.direction(d, tau.real, tau.imag) for d in HIGGS], dtype=complex)
    return R, C, L, H


def chunk_path(tk):
    return CH / (("t_%03d_%d.npz" % tk[1:]) if tk[0] == "t" else ("c_%d_%d.npz" % tk[1:]))


def task(tk):
    p = chunk_path(tk)
    if p.exists(): return tk
    L = lines()
    if tk[0] == "t":
        _, li, ci = tk; a, b = L[li]; pts = stencil(CENTRES[ci])
    else:
        _, k, ci = tk; a, b0 = L[ten()[k]]; b = b0 - a; pts = [complex(*CENTRES[ci]) + 1]
    RR, CC, LL, HH = [], [], [], []
    for z in pts:
        R, C, Lh, H = point_data(a, b, z); RR.append(R); CC.append(C); LL.append(Lh); HH.append(H)
    tmp = p.with_suffix(".tmp.npz")
    np.savez(tmp, R=np.array(RR), C=np.array(CC), L=np.array(LL), H=np.array(HH))
    os.replace(tmp, p)
    return tk


def readout_rows():
    """the record's best six-rows (from main's committed files at 54cfec661)"""
    show = lambda rel: subprocess.run(["git", "show", "54cfec661:" + rel], cwd=ROOT, capture_output=True, check=True).stdout
    rows = [("B1726 best six-row", Fr(2, 5), Fr(1, 2), complex(0.55, 3.05))]
    b49 = json.loads(show("frontier/B1749_the_six_at_fresh_apexes/verification/comparison.json"))["best_six"]["seat"]
    L26 = lines()[:266]
    assert b49["horocycle"] == "L_max"
    rows.append(("B1749 best six-row", L26[b49["line"]][0], L26[b49["line"]][1], complex(b49["Re_tau"], b49["Im_tau"])))
    b86 = json.loads(show("frontier/B1786_the_slope_principle_out_of_sample/verification/comparison.json"))["best"]["a2/5"]["seat"]
    seen, L86 = set(), []
    for N in (25, 30):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1: continue
                aa, bb = Fr(j, N), Fr(k, N); key = min((aa, bb), ((-aa) % 1, (-bb) % 1))
                if key in seen: continue
                seen.add(key); L86.append(key)
    a86, bb86 = L86[b86["line"]]
    assert b86["horocycle"] == "L_max" and a86 == Fr(2, 5)
    rows.append(("B1786 best row", a86, bb86, complex(b86["Re_tau"], b86["Im_tau"])))
    rows.append(("B1786 best row's mirror", a86, (Fr(3, 5) - bb86) % 1, complex(1 - b86["Re_tau"], b86["Im_tau"])))
    return rows


def census(nw, max_s):
    CH.mkdir(exist_ok=True)
    L = lines(); ten()
    tasks = [("t", li, ci) for li in range(len(L)) for ci in range(len(CENTRES))] + [("c", k, ci) for k in range(10) for ci in range(len(CENTRES))]
    todo = [t for t in tasks if not chunk_path(t).exists()]
    print("census: %d stencil tasks (13 points each) and %d calibration points; %d tasks done; %d to do"
          % (len(L) * len(CENTRES), 60, len(tasks) - len(todo), len(todo)), flush=True)
    t0 = time.time(); n = 0
    if todo:
        from multiprocessing import Pool
        with Pool(nw) as P:
            for _ in P.imap_unordered(task, todo):
                n += 1
                if n % 50 == 0: print("tasks done this part %d (%.0f s)" % (n, time.time() - t0), flush=True)
                if time.time() - t0 > max_s:
                    print("census part stopped by its time limit after %d tasks this part" % n, flush=True); P.terminate(); break
    left = [t for t in tasks if not chunk_path(t).exists()]
    if left:
        print("census incomplete: %d tasks left" % len(left)); return
    ro = []
    for name, a, b, tau in readout_rows():
        R, C, Lh, H = point_data(a, b, tau); ro.append((name, str(a), str(b), tau, R, C, Lh, H))
    nl = len(L)
    Rs = np.zeros((nl, 6, 13, 2, 4), complex); Cs = np.zeros((nl, 6, 13, 2, 4)); Ls = np.zeros((nl, 6, 13, 2)); Hs = np.zeros((nl, 6, 13, len(HIGGS), 3), complex)
    for (_t, li, ci) in [t for t in tasks if t[0] == "t"]:
        d = np.load(chunk_path(("t", li, ci))); Rs[li, ci], Cs[li, ci], Ls[li, ci], Hs[li, ci] = d["R"], d["C"], d["L"], d["H"]
    cR = np.zeros((10, 6, 2, 4), complex); cC = np.zeros((10, 6, 2, 4)); cL = np.zeros((10, 6, 2)); cH = np.zeros((10, 6, len(HIGGS), 3), complex)
    for (_t, k, ci) in [t for t in tasks if t[0] == "c"]:
        d = np.load(chunk_path(("c", k, ci))); cR[k, ci], cC[k, ci], cL[k, ci], cH[k, ci] = d["R"][0], d["C"][0], d["L"][0], d["H"][0]
    np.savez_compressed(OUT_CENSUS, R=Rs, C=Cs, L=Ls, H=Hs, calR=cR, calC=cC, calL=cL, calH=cH,
                        roR=np.array([r[4] for r in ro]), roC=np.array([r[5] for r in ro]), roL=np.array([r[6] for r in ro]), roH=np.array([r[7] for r in ro]))
    OUT_INDEX.write_text(json.dumps({"lines": [[str(a), str(b)] for a, b in L], "centres": CENTRES, "r1": R1, "r2": R2, "higgs": HIGGS,
                                     "units": UNITS, "horocycles": HORS, "sectors": ["up", "down"], "ten": ten(),
                                     "readout_rows": [[r[0], r[1], r[2], [r[3].real, r[3].imag]] for r in ro]}, indent=1) + "\n")
    print("census complete: %s written" % OUT_CENSUS.name)


# ------------------------------------------------------------------------------------------------------------- the cells
def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def weights(R, C, L):
    """u_s = sqrt(2 pi L + c_s) R_s, and 0 where c_s is None or 2 pi L + c_s <= 0 (channels()' rule); returns u, clamp mask"""
    v = 2 * math.pi * L[..., None, None] + C
    ok = np.isfinite(C) & (v > 0)
    return np.where(ok, np.sqrt(np.where(ok, v, 1.0)) * R, 0), ~ok


def factors(u, H, cu, cd):
    """the six closed-form factors (each (..., nH)) and their scales, for a pairing (cu, cd); u (..., 2sec, 4), H (..., nH, 3)"""
    out = []
    for sec, cj in ((0, cu), (1, cd)):
        h = np.conj(H) if cj else H
        us = u[..., sec, :]
        Sig = (us ** 2).sum(-1)[..., None] * np.ones(H.shape[:-1]); Ssc = (np.abs(us) ** 2).sum(-1)[..., None] * np.ones(H.shape[:-1])
        uh = np.einsum("...k,...hk->...h", us[..., 1:], h); uhs = np.einsum("...k,...hk->...h", np.abs(us[..., 1:]), np.abs(h))
        hh = np.einsum("...hk,...hk->...h", h, h); hhs = np.einsum("...hk,...hk->...h", np.abs(h), np.abs(h))
        out.append({"hh": (hh, hhs), "Sig": (Sig, Ssc), "uh": (uh, uhs)})
    return out


def theta_of(fs, which):
    """the phase sum of a quantity: 'Y' all six factors, 'H' the two uh, 'M' the two Sigma"""
    keys = {"Y": ("hh", "Sig", "uh"), "H": ("uh",), "M": ("Sig",)}[which]
    return sum(np.angle(f[k][0]) for f in fs for k in keys)


def validity(fs, which, phase_free, clamp_ok):
    """the rule's four conditions on the factors of a quantity; arrays have the stencil point axis at position 2"""
    keys = {"Y": ("hh", "Sig", "uh"), "H": ("uh",), "M": ("Sig",)}[which]
    ok = clamp_ok.copy(); reasons = {}
    nonv = np.ones(ok.shape, bool); pi2 = np.ones(ok.shape, bool); wind = np.ones(ok.shape, bool)
    for f in fs:
        for k in keys:
            F, S = f[k]
            nonv &= (np.abs(F) > 1e-14 * S).all(axis=2)
            if k == "hh" and phase_free: continue                         # the pair (conj h . conj h)(h . h) cancels exactly
            ph = np.moveaxis(np.angle(F), 2, -1)
            d = wrap(ph[..., 1:] - ph[..., :1]); pi2 &= np.max(np.abs(d), axis=-1) < np.pi / 2
            for sl in (slice(1, 7), slice(7, 13)):
                hx = ph[..., sl]; wind &= np.abs(np.sum(wrap(np.roll(hx, -1, axis=-1) - hx), axis=-1)) < np.pi
    reasons = {"clamp mismatch": ~clamp_ok, "vanishing factor": clamp_ok & ~nonv, "winding": clamp_ok & nonv & ~wind,
               "difference past pi/2": clamp_ok & nonv & wind & ~pi2}
    return ok & nonv & pi2 & wind, reasons


def classify(th, sig):
    """th (..., 13) phases, sig (..., 13) per-point noise: D1, D2, sigma_D and the class (0 U, 1 N, 2 H, 3 H', 4 Un)"""
    d = wrap(th[..., 1:] - th[..., :1])
    D1, D2 = d[..., :6].mean(-1), d[..., 6:].mean(-1)
    sD = sig.max(-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = D1 / D2
    Un = sD > 1e-9
    N = ~Un & (np.abs(D1) > 1e-6) & (ratio >= 3) & (ratio <= 5)
    H = ~Un & ~N & (np.abs(D1) < 1e-8) & (sD <= 1e-10)
    Hp = ~Un & ~N & ~H & (ratio >= 30) & (ratio <= 250) & (np.abs(D2) >= 100 * sD)
    cls = np.where(Un, 4, np.where(N, 1, np.where(H, 2, np.where(Hp, 3, 0))))
    return D1, D2, sD, cls, ratio


def verdicts(valid, cls):
    """over the centres (last axis): the rule's verdicts"""
    vN = valid & (cls == 1); vnu = valid & (cls != 4)
    anyN = vN.any(-1); nnu = vnu.sum(-1); allH = (~vnu | (cls == 2) | (cls == 3)).all(-1)
    out = np.full(valid.shape[:-1], "NO READING", dtype=object)
    out[valid.any(-1)] = "NOISE-LIMITED"
    out[nnu > 0] = "UNDETERMINED"
    out[(~anyN) & (nnu >= 3) & allH] = "HARMONIC"
    out[anyN] = "NOT HARMONIC"
    return out


def all_quantities(R, C, L, H, keep=True):
    """theta (point axis 2) and factors (if keep) for every quantity of the rule, from one set of inputs"""
    Q = {}
    pack = (lambda th, fs: (th, fs)) if keep else (lambda th, fs: (th, None))
    for hr in range(2):
        u, clamp = weights(R, C, L[..., hr])
        vc = 2 * math.pi * L[:, :, :1, hr, None, None] + C[:, :, :1]
        okc = np.isfinite(C[:, :, :1]) & (vc > 0)
        uf = np.where(okc, np.sqrt(np.where(okc, vc, 1.0)), 0) * R
        for name, (cu, cd) in READINGS.items():
            fs = factors(u, H, cu, cd); Q[("Y", name, hr)] = pack(theta_of(fs, "Y"), fs)
            if name in (SM, "S,S"):
                ff = factors(uf, H, cu, cd); Q[("Yf", name, hr)] = pack(theta_of(ff, "Y"), ff)
            if name == SM:
                Q[("H", hr)] = pack(theta_of(fs, "H"), fs)
        Q[("clamp", hr)] = clamp
    fsM = factors(weights(R, C, L[..., 0])[0], H[..., :1, :], 0, 0)
    Q[("M",)] = pack(theta_of(fsM, "M")[..., 0], fsM)
    return Q


def perturbed(arrs, p):
    rng = np.random.default_rng(32300 + p); out = []
    for a in arrs:
        if np.iscomplexobj(a):
            z = rng.standard_normal(a.shape) + 1j * rng.standard_normal(a.shape)
        else:
            z = rng.standard_normal(a.shape)
        out.append(a * (1 + PERT * z))
    return out


def cells():
    g = frame(); B, tic = g["B"], g["tic"]
    d = np.load(OUT_CENSUS); idx = json.loads(OUT_INDEX.read_text())
    R, C, L, H = d["R"], d["C"], d["L"], d["H"]
    nl = R.shape[0]
    res = {"scope": {"lines": nl, "centres": len(CENTRES), "higgs": HIGGS, "readings": list(READINGS), "horocycles": list(HORS)}}
    Q = all_quantities(R, C, L, H)
    QP = [all_quantities(*perturbed((R, C, L, H), p), keep=False) for p in range(NPERT)]
    sig = {k: np.max([np.abs(wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    # the clamp pattern shared over the 13 points, per sector and horocycle
    clamp_ok = {}
    for hr in range(2):
        cm = Q[("clamp", hr)]                                                   # (nl, 6, 13, 2, 4)
        same = (cm == cm[:, :, :1]).all(axis=(2, 3, 4))                          # (nl, 6)
        clamp_ok[hr] = same
    res["clamps"] = {HORS[hr]: {"clamped channel-points": int(Q[("clamp", hr)].sum()), "centres with a clamp mismatch": int((~clamp_ok[hr]).sum())} for hr in range(2)}
    # J at the centres (LU coupling), per pairing and horocycle; sigma_1 and the LU determinant for C0(a)
    J = {}; c0a = {"checked": 0, "worst_ratio": 0.0, "fails": 0}
    for hr in range(2):
        u0, _ = weights(R[:, :, 0], C[:, :, 0], L[:, :, 0, hr])                  # (nl, 6, 2, 4)
        M0 = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s] for s in UNITS]))   # (nl, 6, 2, 2, 2)
        for name, (cu, cd) in READINGS.items():
            Ys = []
            for sec, cj in ((0, cu), (1, cd)):
                hv = np.conj(H[:, :, 0]) if cj else H[:, :, 0]                  # (nl, 6, 10, 3)
                S = hv[..., 0, None, None] * B.QI + hv[..., 1, None, None] * B.QJ + hv[..., 2, None, None] * B.QK
                Mx = M0[:, :, sec][:, :, None]
                Y = np.zeros(S.shape[:-2] + (3, 3), complex)
                for a_, Ca in enumerate(B.BLOCKS):
                    for b_, Cb in enumerate(B.BLOCKS):
                        Y[..., a_, b_] = np.einsum("...ij,...ij->...", Ca.T @ B.EPS @ S @ Cb, np.broadcast_to(Mx, S.shape))
                Ys.append(Y)
            JJ = np.zeros((nl, 6, len(HIGGS)))
            for li in range(nl):
                for ci in range(6):
                    for hi in range(len(HIGGS)):
                        JJ[li, ci, hi] = tic.ckm_left(Ys[0][li, ci, hi], Ys[1][li, ci, hi])[3]
            J[(name, hr)] = JJ
            if name == SM:
                th_, fs_ = Q[("Y", SM, hr)]
                validY, _ = validity(fs_, "Y", True, clamp_ok[hr][..., None] * np.ones((1, 1, len(HIGGS)), bool))
                good = validY & (np.moveaxis(sig[("Y", SM, hr)], 2, -1).max(-1) <= 1e-9)
                for sec in range(2):
                    det_lu = np.linalg.det(Ys[sec]); s1 = np.linalg.svd(Ys[sec], compute_uv=False)[..., 0]
                    f = fs_[sec]; cf = f["hh"][0][:, :, 0] * f["Sig"][0][:, :, 0] * f["uh"][0][:, :, 0]
                    ratio = np.abs(det_lu - cf) / (1e-12 * s1 ** 3)
                    c0a["checked"] += int(good.sum()); c0a["fails"] += int((good & (ratio > 1)).sum())
                    if good.any(): c0a["worst_ratio"] = max(c0a["worst_ratio"], float(ratio[good].max()))
    res["C0a"] = dict(c0a, holds=c0a["fails"] == 0 and c0a["checked"] > 0)
    # C0(b): rank one at every evaluated point
    rk = np.abs((R ** 2).sum(-1)) / (np.abs(R) ** 2).sum(-1)
    rkc = np.abs((d["calR"] ** 2).sum(-1)) / (np.abs(d["calR"]) ** 2).sum(-1)
    res["C0b"] = {"worst": float(max(rk.max(), rkc.max())), "holds": bool(max(rk.max(), rkc.max()) <= 1e-9)}
    # validity and classes per quantity
    def vc(key, phase_free, jcut, hr):
        th, fs = Q[key]
        if key[0] == "M":
            cok = clamp_ok[0][..., None]
        else:
            cok = clamp_ok[hr][..., None] * np.ones((1, 1, len(HIGGS)), bool)
        valid, reasons = validity(fs, "M" if key[0] == "M" else ("H" if key[0] == "H" else "Y"), phase_free, cok)
        if key[0] == "M":
            valid = valid[..., 0]; reasons = {k: v[..., 0] for k, v in reasons.items()}
        if jcut is not None:
            jl = np.abs(jcut) > 1e-9; reasons["|J| < 1e-9 at the centre"] = valid & ~jl; valid = valid & jl
        thm = np.moveaxis(th, 2, -1); sgm = np.moveaxis(sig[key], 2, -1)
        D1, D2, sD, cls, ratio = classify(thm, sgm)
        return valid, cls, D1, D2, sD, ratio, reasons
    V = {}
    for name in READINGS:
        for hr in range(2):
            V[("Y", name, hr)] = vc(("Y", name, hr), name in PHASE_FREE, J[(name, hr)], hr)
    for hr in range(2):
        V[("Yf", SM, hr)] = vc(("Yf", SM, hr), True, J[(SM, hr)], hr)
        V[("Yf", "S,S", hr)] = vc(("Yf", "S,S", hr), False, None, hr)
        V[("H", hr)] = vc(("H", hr), True, J[(SM, hr)], hr)
    V[("M",)] = vc(("M",), True, None, 0)
    def tally(keys):
        cnt = {"NOT HARMONIC": 0, "HARMONIC": 0, "UNDETERMINED": 0, "NOISE-LIMITED": 0, "NO READING": 0}; lst = {"HARMONIC": [], "UNDETERMINED": [], "NOISE-LIMITED": []}
        why = {}
        for key in keys:
            valid, cls, D1, D2, sD, ratio, reasons = V[key]
            vd = verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))         # (nl, nH)
            nr = (vd == "NO READING")
            for r, m in reasons.items():
                why[r] = why.get(r, 0) + int((np.moveaxis(m, 1, -1) & nr[..., None]).sum())
            for li in range(vd.shape[0]):
                for hi in range(vd.shape[1]):
                    v = vd[li, hi]; cnt[v] += 1
                    if v in lst: lst[v].append([key[1], HORS[key[2]], idx["lines"][li], HIGGS[hi]])
        return cnt, lst, why
    withr = lambda c: c["NOT HARMONIC"] + c["HARMONIC"] + c["UNDETERMINED"]
    c1, l1, w1 = tally([("Y", n, h) for n in PHASE_FREE for h in range(2)])
    c1b, l1b, w1b = tally([("Y", n, h) for n in ("S,S", "St,St") for h in range(2)])
    c3, l3, w3 = tally([("Yf", SM, h) for h in range(2)])
    cd_, ld_, wd_ = tally([("Yf", "S,S", h) for h in range(2)])
    # C0(d), C0(e)
    nN_floor = 0
    for h in range(2):
        valid, cls = V[("Yf", "S,S", h)][:2]; nN_floor += int((valid & (cls == 1)).sum())
    res["C0d"] = {"valid N cases with frozen weights in (S, S)": nN_floor, "holds": nN_floor == 0}
    res["C0e"] = {"counts": cd_, "harmonic_fraction": (cd_["HARMONIC"] / withr(cd_)) if withr(cd_) else None,
                  "holds": bool(withr(cd_) and cd_["HARMONIC"] >= 0.8 * withr(cd_))}
    first_ok = res["C0e"]["holds"]
    res["H1"] = {"counts": c1, "no_reading_reasons": w1, "first_clause_no_harmonic": (c1["HARMONIC"] == 0) if first_ok else "untested (C0(e) failed)",
                 "second_clause_undetermined_at_most_1pc": c1["UNDETERMINED"] <= 0.01 * withr(c1), "listed": l1}
    res["H1"]["holds"] = (res["H1"]["first_clause_no_harmonic"] is True) and res["H1"]["second_clause_undetermined_at_most_1pc"]
    res["H1b"] = {"counts": c1b, "no_reading_reasons": w1b, "first_clause_no_harmonic": (c1b["HARMONIC"] == 0) if first_ok else "untested (C0(e) failed)",
                  "second_clause_undetermined_at_most_1pc": c1b["UNDETERMINED"] <= 0.01 * withr(c1b), "listed": l1b}
    res["H1b"]["holds"] = (res["H1b"]["first_clause_no_harmonic"] is True) and res["H1b"]["second_clause_undetermined_at_most_1pc"]
    res["H3"] = {"counts": c3, "no_reading_reasons": w3, "holds": bool(withr(c3) and c3["NOT HARMONIC"] >= 0.9 * withr(c3))}
    # H4: theta_M per line at L_max
    valid, cls = V[("M",)][:2]
    vM = verdicts(valid, cls)
    cM = {k: int(np.sum(vM == k)) for k in ("NOT HARMONIC", "HARMONIC", "UNDETERMINED", "NOISE-LIMITED", "NO READING")}
    res["H4"] = {"counts": cM, "holds": bool(withr(cM) and cM["NOT HARMONIC"] >= 0.9 * withr(cM)),
                 "listed_other_than_not_harmonic": [[idx["lines"][li], str(vM[li])] for li in range(nl) if vM[li] != "NOT HARMONIC"]}
    # H2: the horocycle, SM reading, centres valid at both horocycles
    v0, v1 = V[("Y", SM, 0)][0], V[("Y", SM, 1)][0]                               # (nl, 6, 10)
    diff = np.abs(wrap(Q[("Y", SM, 0)][0][:, :, 0] - Q[("Y", SM, 1)][0][:, :, 0]))
    s2 = np.maximum(sig[("Y", SM, 0)][:, :, 0], sig[("Y", SM, 1)][:, :, 0])
    both = v0 & v1; has = both.any(axis=1); big = (both & (diff > np.maximum(1e-6, 1000 * s2))).any(axis=1)
    exc = [[idx["lines"][li], HIGGS[hi]] for li in range(nl) for hi in range(len(HIGGS)) if has[li, hi] and not big[li, hi]]
    res["H2"] = {"pairs_checked": int(has.sum()), "pairs_passing": int((has & big).sum()), "exceptions": exc,
                 "holds": bool(has.sum() and (has & big).sum() >= 0.95 * has.sum())}
    # C0(c): the Higgs's overall phase at the first valid centre of each line, per reading and Higgs, at L_max
    c0c = {"checked": 0, "fails": 0, "worst": 0.0}
    expect = {"St,S": 0.0, "S,St": 0.0, "S,S": 6.0, "St,St": -6.0}
    for name, (cu, cd) in READINGS.items():
        valid = V[("Y", name, 0)][0]
        # validity without the J cut for the control: recompute
        th, fs = Q[("Y", name, 0)]
        vnoJ, _ = validity(fs, "Y", name in PHASE_FREE, clamp_ok[0][..., None] * np.ones((1, 1, len(HIGGS)), bool))
        for phi in (0.3, 1.1, 2.0):
            u0, _ = weights(R[:, :, :1], C[:, :, :1], L[:, :, :1, 0])
            fsp = factors(u0, H[:, :, :1] * np.exp(1j * phi), cu, cd)
            thp = theta_of(fsp, "Y")[:, :, 0]                                      # (nl, 6, 10)
            dev = np.abs(wrap(thp - th[:, :, 0] - expect[name] * phi))
            tol = np.maximum(1e-9, 10 * sig[("Y", name, 0)][:, :, 0])
            for li in range(nl):
                for hi in range(len(HIGGS)):
                    cs = np.flatnonzero(vnoJ[li, :, hi])
                    if cs.size:
                        ci = cs[0]; c0c["checked"] += 1
                        c0c["worst"] = max(c0c["worst"], float(dev[li, ci, hi]))
                        if dev[li, ci, hi] > tol[li, ci, hi]: c0c["fails"] += 1
    res["C0c"] = dict(c0c, holds=c0c["fails"] == 0 and c0c["checked"] > 0)
    # C0(f): the T-step at the calibration points
    cR, cC, cL, cH = d["calR"], d["calC"], d["calL"], d["calH"]
    tl = idx["ten"]; c0f = {"checked": 0, "fails": 0, "worst_deviation": 0.0, "worst_ratio": 0.0}
    def theta_points(Rp, Cp, Lp, Hp, hr):
        u, _ = weights(Rp, Cp, Lp[..., hr]); return theta_of(factors(u, Hp, 1, 0), "Y")
    for hr in range(2):
        thc = theta_points(cR, cC, cL, cH, hr)                                         # (10, 6, 10)
        thb = Q[("Y", SM, hr)][0][tl][:, :, 0]                                           # (10, 6, 10)
        sc = np.max([np.abs(wrap(theta_points(*perturbed((cR, cC, cL, cH), p), hr) - thc)) for p in range(NPERT)], axis=0)
        sb = sig[("Y", SM, hr)][tl][:, :, 0]
        for hn in CAL_HIGGS:
            hi = HIGGS.index(hn)
            dev = np.abs(wrap(thc[:, :, hi] - thb[:, :, hi] - T_SHIFT))
            tol = 10 * np.maximum(sc[:, :, hi], sb[:, :, hi]) + 1e-12
            c0f["checked"] += dev.size; c0f["fails"] += int((dev > tol).sum())
            c0f["worst_deviation"] = max(c0f["worst_deviation"], float(dev.max())); c0f["worst_ratio"] = max(c0f["worst_ratio"], float((dev / tol).max()))
    res["C0f"] = dict(c0f, holds=c0f["fails"] == 0)
    res["C0"] = {"holds_stop_rule_controls": bool(res["C0a"]["holds"] and res["C0b"]["holds"] and res["C0c"]["holds"] and res["C0d"]["holds"] and res["C0f"]["holds"]),
                 "power_C0e": res["C0e"]["holds"]}
    # read-outs: the scaling diagnostic
    sc_n = sc_in = 0
    for hr in range(2):
        valid, cls, D1, D2, sD, ratio, _ = V[("Y", SM, hr)]
        m = valid & (sD <= 1e-9) & (np.abs(D1) > 1e-6)
        sc_n += int(m.sum()); sc_in += int((m & (ratio >= 3) & (ratio <= 5)).sum())
    res["readout_scaling"] = {"centres": sc_n, "ratio_in_3_5": sc_in}
    # read-outs: the median |Laplacian| over N centres by slope (SM, dR, L_max)
    slopes = sorted({a for a, b in idx["lines"]}, key=Fr); med = {}
    vY, cY, D1Y = V[("Y", SM, 0)][:3]; vH_, cH_, D1H = V[("H", 0)][:3]; vM_, cM_, D1M = V[("M",)][:3]
    for s in slopes:
        li = [i for i, (a, b) in enumerate(idx["lines"]) if a == s]
        def mm(v, c, D, hsel=True):
            if hsel: v, c, D = v[li, :, 0], c[li, :, 0], D[li, :, 0]
            else: v, c, D = v[li], c[li], D[li]
            x = np.abs(D[v & (c == 1)]) * 4 / R1 ** 2
            return float(np.median(x)) if x.size else None
        med[s] = {"theta_Y": mm(vY, cY, D1Y), "theta_H": mm(vH_, cH_, D1H), "theta_M": mm(vM_, cM_, D1M, False)}
    res["readout_median_abs_laplacian_over_N_centres"] = med
    # read-outs: the record's best six-rows (SM reading, dR, L_max)
    ro = []
    for k, (name, a, b, tz) in enumerate(idx["readout_rows"]):
        Rr, Cr, Lr, Hr = d["roR"][k], d["roC"][k], d["roL"][k], d["roH"][k]
        u, _ = weights(Rr, Cr, Lr[0]); fs = factors(u, Hr[:1], 1, 0)
        M = np.einsum("...s,sab->...ab", u, np.array([B.EDUAL[s] for s in UNITS]))
        S = lambda hv: hv[0] * B.QI + hv[1] * B.QJ + hv[2] * B.QK
        Yu = B.coupling(S(np.conj(Hr[0])), M[0]); Yd = B.coupling(S(Hr[0]), M[1])
        ro.append({"row": name, "line": [a, b], "tau": tz, "theta_Y_over_pi": float(wrap(theta_of(fs, "Y")[0]) / np.pi),
                   "theta_H_over_pi": float(wrap(theta_of(fs, "H")[0]) / np.pi), "theta_M_over_pi": float(wrap(theta_of(fs, "M")[0]) / np.pi),
                   "J": float(tic.ckm_left(Yu, Yd)[3])})
    res["readout_best_rows"] = ro
    (HERE / "p323_cells.json").write_text(json.dumps(res, indent=1, default=str) + "\n")
    # the printout
    print("C0 stop-rule controls (a, b, c, d, f) hold: %s; power C0(e): %s" % (res["C0"]["holds_stop_rule_controls"], res["C0"]["power_C0e"]))
    for k in ("C0a", "C0b", "C0c", "C0d", "C0f"):
        print("  %s: %s" % (k, res[k]))
    print("  C0e: counts %s, harmonic fraction %s" % (res["C0e"]["counts"], res["C0e"]["harmonic_fraction"]))
    print("  clamps: %s" % res["clamps"])
    for k in ("H1", "H1b"):
        r = res[k]
        print("%s holds: %s (no HARMONIC: %s; UNDETERMINED <= 1%%: %s); counts %s; no-reading reasons %s"
              % (k, r["holds"], r["first_clause_no_harmonic"], r["second_clause_undetermined_at_most_1pc"], r["counts"], r["no_reading_reasons"]))
    print("H2 holds: %s; pairs checked %d, passing %d; exceptions %d" % (res["H2"]["holds"], res["H2"]["pairs_checked"], res["H2"]["pairs_passing"], len(res["H2"]["exceptions"])))
    print("H3 holds: %s; counts %s" % (res["H3"]["holds"], res["H3"]["counts"]))
    print("H4 holds: %s; counts %s" % (res["H4"]["holds"], res["H4"]["counts"]))
    for k in ("H1", "H1b"):
        for v in ("HARMONIC", "UNDETERMINED", "NOISE-LIMITED"):
            L_ = res[k]["listed"][v]
            print("%s %s: %d%s" % (k, v, len(L_), (" (first 30): " + "; ".join("%s %s (%s, %s) %s" % (x[0], x[1], x[2][0], x[2][1], x[3]) for x in L_[:30])) if L_ else ""))
    print("H2 exceptions (first 30): %s" % "; ".join("(%s, %s) %s" % (x[0][0], x[0][1], x[1]) for x in res["H2"]["exceptions"][:30]))
    print("H4 lines other than NOT HARMONIC (first 40): %s" % "; ".join("(%s, %s) %s" % (x[0][0], x[0][1], x[1]) for x in res["H4"]["listed_other_than_not_harmonic"][:40]))
    print("read-out, the scaling: %s" % res["readout_scaling"])
    print("read-out, median 4|D(r1)|/r1^2 over N centres by slope (theta_Y SM dR L_max | theta_H | theta_M at L_max):")
    f = lambda x: "%.2e" % x if x is not None else "-"
    for s, v in med.items():
        print("  %-6s %s | %s | %s" % (s, f(v["theta_Y"]), f(v["theta_H"]), f(v["theta_M"])))
    print("read-out, the record's best six-rows (SM reading, dR, L_max), in units of pi:")
    for r in ro:
        print("  %-26s (%s, %s) at %.4f + %.4fi: theta_Y %+.4f, theta_H %+.4f, theta_M %+.4f, J %+.2e" % (r["row"], r["line"][0], r["line"][1], r["tau"][0], r["tau"][1], r["theta_Y_over_pi"], r["theta_H_over_pi"], r["theta_M_over_pi"], r["J"]))
    print("p323 cells exit 0")


if __name__ == "__main__":
    if "--census" in sys.argv:
        nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
        ms = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6300
        census(nw, ms)
    elif "--cells" in sys.argv:
        cells()
    else:
        print(__doc__)
