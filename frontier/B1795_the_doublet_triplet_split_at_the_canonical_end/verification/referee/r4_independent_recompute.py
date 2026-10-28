"""Referee B1795, r4: an independent re-implementation (no b1656_funcs function is called except the Higgs section S, which
is pair-independent and checked by split.py's control).  Own theta sums; residues ANALYTIC (theta1'(0) and the derivative
of theta1(u + t) at 0), not circle means; the regularised norm c_s by a POLAR Gauss-Legendre quadrature on [0, rmax(theta)]
of (|K|^2 - 1/r^2) r plus the closed term int log rmax dtheta (cA integrates in log r from eps = 1e-5 with a disc
correction); own dual basis by solving the 4x4 pairing system; own coupling as a trace.  Twists exact from fractions.
Compares Dn, |det M| and sv3/sv1, sv2/sv1 with split_rows.jsonl on a sample of lines, all three points, all four pairs.
    python3 -B r4_independent_recompute.py [nth nr]"""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
V = ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification"
NTH = int(sys.argv[1]) if len(sys.argv) > 1 else 48
NR = int(sys.argv[2]) if len(sys.argv) > 2 else 48
K = np.arange(-30, 31)
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UN = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}; BL = [QJ, QI, QK]


def thchar(a, b, u, T):                    # sum_n exp(i pi T (n+a)^2 + 2 pi i (n+a)(u+b))
    n = K + a; u = np.asarray(u, dtype=complex)[..., None]
    return np.exp(1j * np.pi * T * n * n + 2j * np.pi * n * (u + b)).sum(-1)


def theta1(u, t):                           # -i sum_k (-1)^k exp(i pi t (k+1/2)^2 + i pi (2k+1) u)
    h = K + 0.5; u = np.asarray(u, dtype=complex)[..., None]
    return (-1j * ((-1.0) ** K) * np.exp(1j * np.pi * t * h * h + 1j * np.pi * (2 * K + 1) * u)).sum(-1)


def dtheta1(u, t):                          # d/du theta1(u, t)
    h = K + 0.5; u = np.asarray(u, dtype=complex)[..., None]
    return (-1j * ((-1.0) ** K) * (1j * np.pi * (2 * K + 1)) * np.exp(1j * np.pi * t * h * h + 1j * np.pi * (2 * K + 1) * u)).sum(-1)


def bilinear(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2 * t
    t1 = theta1(u, t); t1s = theta1(u + t, t); den = 1j * np.exp(-1j * np.pi * t / 2) * np.exp(-1j * np.pi * u) * t1
    X0, X1, Y0, Y1 = thchar(ax, bx, u, T), thchar(ax, bx, u + t, T), thchar(ay, by, u, T), thchar(ay, by, u + t, T)
    return np.array([[X0 * Y0 / t1, np.exp(1j * np.pi * by) * X0 * Y1 / den], [np.exp(1j * np.pi * bx) * X1 * Y0 / den, np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / t1s]])


def residue_matrix(x, y, t):               # analytic: all four entries have a simple pole at u = 0
    (ax, bx), (ay, by) = x, y; T = 2 * t
    X0, X1, Y0, Y1 = (complex(thchar(ax, bx, 0, T)), complex(thchar(ax, bx, t, T)), complex(thchar(ay, by, 0, T)), complex(thchar(ay, by, t, T)))
    d1 = complex(dtheta1(0, t)); d1s = complex(dtheta1(t, t)); dden = 1j * np.exp(-1j * np.pi * t / 2) * d1
    return np.array([[X0 * Y0 / d1, np.exp(1j * np.pi * by) * X0 * Y1 / dden], [np.exp(1j * np.pi * bx) * X1 * Y0 / dden, np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / d1s]])


def chan(Mlist, s):                         # P_s = sum_{mn} (eps C_s)_{mn} M_{mn}
    E = EPS @ UN[s]; return sum(E[m, n] * Mlist[m][n] for m in range(2) for n in range(2))


def rmax(th, t):
    d = np.exp(1j * th); y1 = d.imag / t.imag; x1 = d.real - y1 * t.real; return 0.5 / np.maximum(abs(x1), abs(y1))


def norms(x, y, t, R):
    """c_s = int_P (|P_s/R_s|^2 - 1/|z|^2) dA + int_0^{2pi} log rmax(theta) dtheta, polar GL on [0, rmax]"""
    v = [0.5 + 0.5 * t, -0.5 + 0.5 * t, -0.5 - 0.5 * t, 0.5 - 0.5 * t]
    br = sorted(float(np.mod(np.angle(z), 2 * np.pi)) for z in v); br.append(br[0] + 2 * np.pi)
    xg, wg = np.polynomial.legendre.leggauss(NTH); xr, wr = np.polynomial.legendre.leggauss(NR)
    tot = {s: 0.0 for s in UN}; logint = 0.0
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a); wt = 0.5 * (b - a) * wg; rm = rmax(th, t)
        logint += float(np.sum(wt * np.log(rm)))
        r = 0.5 * rm[:, None] * (xr[None, :] + 1); w2 = 0.5 * rm[:, None] * wr[None, :]
        z = r * np.exp(1j * th)[:, None]; Mz = bilinear(x, y, z, t)
        for s in UN:
            if abs(R[s]) < 1e-12: continue
            Ps = chan(Mz, s); f = (np.abs(Ps / R[s]) ** 2 - 1 / r ** 2) * r
            tot[s] += float(np.sum(wt[:, None] * w2 * f))
    return {s: (tot[s] + logint if abs(R[s]) >= 1e-12 else None) for s in UN}


# own dual basis: E_s with sum_{mn} (eps C_t)_{mn} (E_s)_{mn} = delta_st
keys = list(UN); A = np.array([[(EPS @ UN[tk]).ravel() @ UN[sk].ravel() for sk in keys] for tk in keys])  # A[t][s] = pair(C_s, C_t)
Ainv = np.linalg.inv(A); EDU = {keys[s]: sum(Ainv[b, s] * UN[keys[b]] for b in range(4)) for s in range(4)}
for tk in keys:
    for sk in keys: assert abs((EPS @ UN[tk]).ravel() @ EDU[sk].ravel() - (tk == sk)) < 1e-12
def Ycoup(S, M): return np.array([[np.trace(Ca.T @ EPS @ S @ Cb @ M.T) for Cb in BL] for Ca in BL])


spec = importlib.util.spec_from_file_location("split", V / "split.py"); SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
rows = {(r["a"], r["b"], r["point"]): r for r in (json.loads(l) for l in (V / "split_rows.jsonl").read_text().splitlines() if l.strip())}
SAMPLE = [("0", "1/11"), ("0", "4/11"), ("1/6", "1/12"), ("1/4", "3/8"), ("1/7", "3/7"), ("1/5", "2/5"), ("2/5", "7/60"), ("2/5", "49/60"), ("2/5", "11/12"), ("5/12", "1/3"), ("1/3", "1/2")]
SAMPLE = [s for s in SAMPLE if (s[0], s[1], "g1") in rows]
print("sample lines:", SAMPLE, "| quadrature nth %d nr %d per segment" % (NTH, NR))
worst = {"Dn": 0.0, "detM": 0.0, "sv": 0.0, "R": 0.0, "c": 0.0}
for a, b in SAMPLE:
    for pk, (re_t, im_t) in SP.POINTS.items():
        t = complex(re_t, im_t); ref = rows[(a, b, pk)]
        Ls = {"L_max": float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])), "L_2": float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))}
        Sx = SP.higgs(t)
        line = []
        for p, (ql, qr) in SP.PAIRS.items():
            x = (float(ql * Fr(a)), float(2 * ql * Fr(b))); y = (float(qr * Fr(a)), float(2 * qr * Fr(b)))
            Rm = residue_matrix(x, y, t); R = {s: complex(chan([[Rm[0, 0], Rm[0, 1]], [Rm[1, 0], Rm[1, 1]]], s)) for s in UN}
            c = norms(x, y, t, R)
            D = sum(c[s] * R[s] ** 2 for s in UN if c[s] is not None); nR = sum(abs(R[s]) ** 2 for s in UN)
            Dn = abs(D) / (max(abs(v) for v in c.values() if v is not None) * nR)
            rr = ref[p]
            worst["Dn"] = max(worst["Dn"], abs(Dn - rr["Dn"]) / rr["Dn"])
            worst["R"] = max(worst["R"], max(abs(R[s] - complex(*rr["R"][s])) for s in UN) / math.sqrt(nR))
            worst["c"] = max(worst["c"], max(abs(c[s] - rr["c"][s]) for s in UN if c[s] is not None and rr["c"][s] is not None))
            for h, L in Ls.items():
                u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None else 0) for s in UN}
                M = sum(u[s] * EDU[s] for s in UN)
                worst["detM"] = max(worst["detM"], abs(abs(np.linalg.det(M)) - rr["detM|" + h]) / rr["detM|" + h])
                for rn, S in Sx.items():
                    sv = np.linalg.svd(Ycoup(S, M), compute_uv=False); sr = rr["sv|%s|%s" % (h, rn)]
                    worst["sv"] = max(worst["sv"], abs(sv[2] / sv[0] - sr[2] / sr[0]) / (sr[2] / sr[0]), abs(sv[1] / sv[0] - sr[1] / sr[0]) / (sr[1] / sr[0]))
            line.append("%s Dn %.4e (row %.4e)" % (p, Dn, rr["Dn"]))
        print("(%s, %s) %-5s " % (a, b, pk) + " | ".join(line[::2]))
print("WORST over the sample: rel Dn %.2e | rel |det M| %.2e | rel sv2/sv1, sv3/sv1 %.2e | residues (rel to |R|) %.2e | abs c_s %.2e" % (worst["Dn"], worst["detM"], worst["sv"], worst["R"], worst["c"]))
