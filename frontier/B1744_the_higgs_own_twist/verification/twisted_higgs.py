"""B1744 (P-324), POST HOC look (labelled): the Higgs as the frame's residue quaternion at its own hypercharge twist.
T0 = residues(twist_of(3w), (0, 0), tau) of B1656's pairing (at zero twist the channel triplet R; the twist's sign does
not matter, the frame being even: the_twist.py, part A).  The Higgs matrix S = s R_1 * 1 + R_i Q_I + R_j Q_J + R_k Q_K with
the scalar channel dropped (s = 0) or kept with either sign (s = +1, -1: the twist in the left or the right slot), read S
or S~ = eps conj(S) eps^T in every sector (H_u = H_d: no pair), c = 3.  B1742's grid (ten (2/5, k/10) lines, 1 280 points,
both horocycles); per variant the minimum chi2_nine and chi2_six and where.  Six variants, chosen before any of them was
compared with data; a hit is a hypothesis for a sealed test on fresh points, never a result."""
import sys, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
import pencils as P      # noqa: E402

VARIANTS = [(s, rd) for s in (0, 1, -1) for rd in ("S", "St")]


def nine_S(S, M, hor, B):
    Y = {sec: B.coupling(S, M[(sec, hor)]) for sec in ("up", "down", "lep")}
    six = []
    for sec in ("up", "down", "lep"):
        sv = np.maximum(np.linalg.svd(Y[sec], compute_uv=False), 1e-300); six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, P.LC, -P.LC])
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    ck = np.log(np.maximum([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])], 1e-300))
    r = (np.concatenate([six, ck]) - P.T9) / P.S9
    return float((r ** 2).sum()), float((r[:6] ** 2).sum())


def point(task):
    k, re_t, im_t = task; a, b = P.LINES[k]; t = complex(re_t, im_t); B = P.R.CEN._modules()["B"]
    M = P.SC.channels(re_t, im_t, a, b); w = float(a) * t + float(b)
    R = B.residues(B.twist_of(3 * w, t), (0.0, 0.0), t)
    out = []
    for s, rd in VARIANTS:
        S = s * R["1"] * B.UNITS["1"] + R["i"] * B.QI + R["j"] * B.QJ + R["k"] * B.QK
        if rd == "St": S = B.EPS @ np.conj(S) @ B.EPS.T
        for hor in ("L_max", "L_2"):
            c9, c6 = nine_S(S, M, hor, B); out.append((s, rd, k, re_t, im_t, hor, c9, c6))
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    HERE = pathlib.Path(__file__).resolve().parent
    RES = [0.0625 + 0.125 * i for i in range(8)]; IMS = [round(2.0 + 0.1 * j, 10) for j in range(16)]
    tasks = [(k, r, y) for k in range(10) for r in RES for y in IMS]; rows = []
    with Pool(8) as Pp:
        for i, o in enumerate(Pp.imap_unordered(point, tasks, chunksize=4)):
            rows += o
            if i % 320 == 0: print("points", i, flush=True)
    (HERE / "twisted_higgs.json").write_text(json.dumps(rows) + "\n")
    for s, rd in VARIANTS:
        rr = [r for r in rows if r[0] == s and r[1] == rd]; b9 = min(rr, key=lambda r: r[6]); b6 = min(rr, key=lambda r: r[7])
        print("R1 x %+d, read %-2s: min chi2_nine %9.2f at line %d, %.4f + %.2fi, %s; min chi2_six %8.2f; nine < 21.67: %d, six < 16.75: %d" % (
            s, rd, b9[6], b9[2], b9[3], b9[4], b9[5], b6[7], sum(r[6] < 21.67 for r in rr), sum(r[7] < 16.75 for r in rr)))
