"""The web seat's check for its note on the doublet index (data-free; no measured value is read; nothing is computed on
the candidate family's slope, a = 2/5 or 3/5; no D, no theta-bar, no inter-sector value).

What a doublet index would have to do: make the coupling itself enforce the hypercharge sign rule, S_X = H(v_X), with
v_X = -(q_L + q_R)_X w the twist sector X needs and H any Higgs section of the twist.  The note's argument is exact;
these checks verify its inputs on main's code (B1656's frame as B1821's module builds it, at main ac987e34b).

Notation: a line is (a, b), w = a tau + b (main's B.line_w(a, -b, tau)); N is w -> -w, the line (-a, -b), the
elliptic involution (P-626: a relabelling of the same point).  S = sigma 1 + h.(i, j, k) with the frame's matrices
B.QI, B.QJ, B.QK; S~ = EPS conj(S) EPS^T (B1790's reading); ||S||^2 = tr(S^dag S)/2.

(0) The instrument: on the band grid of (3), DR.DR against eta^6/4 (B1739) and R.R against 0 (Jacobi), R and DR from
    main's B1691 sections (cm_zero_line.direction).
(1) The algebra, with the frame's matrices:
    (a) the units 1, i, j, k are orthonormal: tr(U_a^dag U_b)/2 = delta_ab;
    (b) pseudoreality: EPS conj(U) EPS^T = U for each unit, so S~ = conj(sigma) + conj(h).Q;
    (c) the adjugate: EPS S^T EPS^T = sigma - h.Q;
    (d) det S = sigma^2 + h.h;
    (e) the readings' distance: min over phi of ||S~ - e^(i phi) S||^2 = 2(||S||^2 - |det S|), on 2000 seeded random S,
        against a 4096-point phi grid and at the closed-form minimiser phi* = -arg det S.
(2) The matter's parity at the puncture under N: on W183's census (orders 1-12, each line min((a, b), (-a, -b) mod 1);
    the family's slope removed) at three tau (0.2 + 2.5i, 0.45 + 3.1i, 0.05 + 1.7i), per sector and channel s: the
    residue R_s at -w against R_s at w (even), and main's a0_of (the kernel's Laurent constant) at -w against minus its
    value at w (odd), where main's residue is above its 1e-12 cut at both (the rest counted); for scale, each against
    the other parity.
(3) Where the reading is an input: rho = |det S|/||S||^2 for the record's Higgs directions (cm_zero_line's DIRS: DR,
    a0 (B1810's direction, not the singlet), R, t=-5/288, F_a for a in -10, -6, -2, 6, 10, 14, 18, 22, 26) on
    Im tau = 1.0, 1.5, ..., 4.0 and Re tau = 0, 0.05, ..., 0.5: per direction and Im tau, the smallest, median and largest
    rho over Re tau.  Then DR with the admissible singlet sigma = i r eta^3/2, r = 1/2, 1, 2 (det S = (1 - r^2) eta^6/4).
(4) The frame's own charge table (B.SIXY, B.SECTORS): each sector's net 6Y, the Higgs charge its pairing needs, and the
    reading each identification of S gives (S the flavour part of the field with 6Y = +3, B.SIXY's H, or of the field
    with 6Y = -3).

Usage: python3 doublet_index_check.py <main checkout>   (main at ac987e34b)
"""
import contextlib
import io
import math
import os
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd
from multiprocessing import Pool

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
os.chdir(ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]

PI = math.pi
SECS = (("up", 1, -4), ("down", 1, 2), ("lep", -3, 6))
FAMILY = (Fr(2, 5), Fr(3, 5))
PAR_TAUS = (complex(0.2, 2.5), complex(0.45, 3.1), complex(0.05, 1.7))
IM = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0)
RE = tuple(round(0.05 * k, 2) for k in range(11))
UNITS = (np.eye(2, dtype=complex), B.QI, B.QJ, B.QK)
CUT = 1e-12


def guard(a):
    if Fr(a) % 1 in FAMILY:
        raise SystemExit("refused: the candidate family's slope")


def eta(tau, n=80):
    q = np.exp(2j * PI * tau)
    return np.exp(2j * PI * tau / 24) * np.prod([1 - q ** k for k in range(1, n)])


def mat(sig, h):
    return sig * UNITS[0] + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK


def nrm2(A):
    return float(np.real(np.trace(A.conj().T @ A)) / 2)


def tilde(S):
    return B.EPS @ S.conj() @ B.EPS.T


def own_lines(orders):
    seen, out = set(), []
    for N in orders:
        for j in range(N):
            for k in range(N):
                if gcd(gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N)
                kk = min((a, b), ((-a) % 1, (-b) % 1))
                if kk in seen:
                    continue
                seen.add(kk); out.append(kk)
    return out


# ---------------------------------------------------------------------------------------------- (1)
def algebra():
    out = {}
    G = np.array([[np.trace(U.conj().T @ V) / 2 for V in UNITS] for U in UNITS])
    out["orth"] = float(np.max(np.abs(G - np.eye(4))))
    out["pseudo"] = [float(np.max(np.abs(B.EPS @ U.conj() @ B.EPS.T - U))) for U in UNITS]
    rng = np.random.default_rng(20261104)
    phis = np.linspace(0, 2 * PI, 4096, endpoint=False)
    e_t = e_adj = e_det = e_grid = e_star = 0.0
    lo = 1.0
    for _ in range(2000):
        sig = complex(*rng.normal(size=2)); h = rng.normal(size=3) + 1j * rng.normal(size=3)
        S = mat(sig, h)
        e_t = max(e_t, float(np.max(np.abs(tilde(S) - mat(np.conj(sig), np.conj(h))))))
        e_adj = max(e_adj, float(np.max(np.abs(B.EPS @ S.T @ B.EPS.T - mat(sig, -h)))))
        d = np.linalg.det(S)
        e_det = max(e_det, abs(d - (sig * sig + h @ h)) / (1 + abs(d)))
        closed = 2 * (nrm2(S) - abs(d))
        St = tilde(S)
        # ||St - e^{i phi} S||^2 = ||St||^2 + ||S||^2 - 2 Re(e^{i phi} <St, S>), <A, B> = tr(A^dag B)/2
        ip = np.trace(St.conj().T @ S) / 2
        grid = nrm2(St) + nrm2(S) - 2 * np.real(np.exp(1j * phis) * ip)
        e_grid = max(e_grid, abs(float(grid.min()) - closed) / nrm2(S))
        ps = -np.angle(d)
        e_star = max(e_star, abs(nrm2(St - np.exp(1j * ps) * S) - closed) / nrm2(S))
        lo = min(lo, closed / (2 * nrm2(S)))
    out.update(tilde=e_t, adj=e_adj, det=e_det, grid=e_grid, star=e_star, lo=lo)
    return out


# ---------------------------------------------------------------------------------------------- (2)
def parity(task):
    a, b, tau = task
    guard(a)
    rec = {"R": [], "a0": [], "cut": 0, "n": 0}
    for sn, ql, qr in SECS:
        got = []
        for sa, sb in ((a, b), (-a, -b)):
            w = B.line_w(float(sa), -float(sb), tau); x, y = B.sector_twists(w, tau, ql, qr)
            with contextlib.redirect_stdout(io.StringIO()):
                R = B.residues(x, y, tau); A0 = B.a0_of(x, y, tau, R)
            got.append((R, A0))
        (R1, A1), (R2, A2) = got
        for s in B.UNITS:
            rec["n"] += 1
            if abs(R1[s]) <= CUT or abs(R2[s]) <= CUT or A1[s] is None or A2[s] is None:
                rec["cut"] += 1
                continue
            rec["R"].append(abs(R2[s] - R1[s]) / abs(R1[s]))
            rec["a0"].append(abs(A2[s] + A1[s]) / (1 + abs(A1[s])))
            rec.setdefault("R_odd", []).append(abs(R2[s] + R1[s]) / abs(R1[s]))
            rec.setdefault("a0_rel", []).append((abs(A1[s]), abs(A2[s] + A1[s]), abs(A2[s] - A1[s])))
    return rec


# ---------------------------------------------------------------------------------------------- (3)
def band(tau):
    with contextlib.redirect_stdout(io.StringIO()):
        H = {d: np.array(Z.direction(d, tau)) for d in Z.DIRS}
    rho = {d: abs(h @ h) / float(np.real(np.vdot(h, h))) for d, h in H.items()}
    E3 = eta(tau) ** 3
    DR = H["DR"]; R = H["R"]
    inst = {"DR.DR": abs(DR @ DR - E3 ** 2 / 4) / abs(DR @ DR), "R.R": abs(R @ R) / float(np.real(np.vdot(R, R)))}
    sing = {}
    for r in (0.5, 1.0, 2.0):
        S = mat(1j * r * E3 / 2, DR)
        sing[r] = (abs(np.linalg.det(S)) / nrm2(S), abs(np.linalg.det(S) - (1 - r * r) * E3 ** 2 / 4) / (abs(E3) ** 2 / 4))
    return tau, rho, inst, sing


if __name__ == "__main__":
    census = own_lines(range(1, 13))
    keep = [l for l in census if l[0] % 1 not in FAMILY]
    ptasks = [(a, b, t) for (a, b) in keep for t in PAR_TAUS]
    btasks = [complex(x, y) for y in IM for x in RE]
    with Pool(4) as pool:
        RP = pool.map(parity, ptasks, chunksize=8)
        RB = pool.map(band, btasks, chunksize=1)

    print("(0) the instrument, on the band grid (%d tau: Im tau %s, Re tau %s)" % (len(RB), IM, RE))
    print("    DR.DR against eta^6/4: largest relative difference %.1e;  R.R/|R|^2 largest %.1e"
          % (max(r[2]["DR.DR"] for r in RB), max(r[2]["R.R"] for r in RB)))

    A = algebra()
    print("(1) the algebra, with the frame's matrices")
    print("    (a) tr(U_a^dag U_b)/2 - delta_ab: largest %.1e" % A["orth"])
    print("    (b) EPS conj(U) EPS^T - U for U = 1, i, j, k: %s" % ", ".join("%.1e" % v for v in A["pseudo"]))
    print("        S~ - (conj sigma + conj h.Q) on 2000 random S: largest %.1e" % A["tilde"])
    print("    (c) EPS S^T EPS^T - (sigma - h.Q): largest %.1e" % A["adj"])
    print("    (d) det S - (sigma^2 + h.h), relative: largest %.1e" % A["det"])
    print("    (e) min over phi of ||S~ - e^(i phi) S||^2 against 2(||S||^2 - |det S|), relative to ||S||^2: phi grid "
          "(4096 points) largest %.1e; at phi* = -arg det S largest %.1e" % (A["grid"], A["star"]))
    print("        the smallest (1 - rho) over the random S: %.3f" % A["lo"])

    rr = [v for r in RP for v in r["R"]]; aa = [v for r in RP for v in r["a0"]]
    print("(2) the matter's parity at the puncture under N (w -> -w): %d census lines (of %d; the family's slope removed) x %d tau"
          % (len(keep), len(census), len(PAR_TAUS)))
    print("    (sector, channel) pairs: %d; compared %d; residue below main's cut or a0_of None at w or -w: %d"
          % (sum(r["n"] for r in RP), len(rr), sum(r["cut"] for r in RP)))
    print("    R_s(-w) against R_s(w): largest relative difference %.1e, median %.1e" % (max(rr), float(np.median(rr))))
    print("    a0_s(-w) against -a0_s(w): largest |sum|/(1 + |a0|) %.1e, median %.1e" % (max(aa), float(np.median(aa))))
    ro = [v for r in RP for v in r.get("R_odd", [])]
    big = [t for r in RP for t in r.get("a0_rel", []) if t[0] > 1e-8]
    print("    for scale, the other parity: R_s(-w) against -R_s(w), relative: smallest %.3g, median %.3g" % (min(ro), float(np.median(ro))))
    print("    where |a0_s(w)| > 1e-8 (%d of %d compared; median |a0_s| %.3g): |a0_s(-w) + a0_s(w)|/|a0_s(w)| largest %.1e; "
          "|a0_s(-w) - a0_s(w)|/|a0_s(w)| smallest %.3g" % (len(big), len(rr), float(np.median([t[0] for t in big])),
                                                           max(t[1] / t[0] for t in big), min(t[2] / t[0] for t in big)))

    print("(3) where the reading is an input: rho = |det S|/||S||^2 (1 = the two readings coincide up to a phase; 0 = null)")
    for d in Z.DIRS:
        row = []
        for y in IM:
            v = sorted(r[1][d] for r in RB if abs(r[0].imag - y) < 1e-9)
            row.append("%.1f: %.2g / %.2g / %.2g" % (y, v[0], float(np.median(v)), v[-1]))
        print("    %-9s %s" % (d, ";  ".join(row)))
    print("    DR with the admissible singlet sigma = i r eta^3/2 (smallest / median / largest rho over Re tau; det against "
          "(1 - r^2) eta^6/4, largest relative to |eta^6|/4):")
    for r_ in (0.5, 1.0, 2.0):
        row = []
        for y in IM:
            v = sorted(r[3][r_][0] for r in RB if abs(r[0].imag - y) < 1e-9)
            row.append("%.1f: %.2g / %.2g / %.2g" % (y, v[0], float(np.median(v)), v[-1]))
        print("    r = %-4s %s;  det %.1e" % (r_, ";  ".join(row), max(r[3][r_][1] for r in RB)))

    print("(4) the frame's charge table: B.SIXY = %s" % B.SIXY)
    hq = B.SIXY["H"]
    pair = {}
    for sec, (l, r) in B.SECTORS.items():
        net = B.SIXY[l] + B.SIXY[r]; need = -net
        pair[sec] = "H" if need == hq else ("conj H" if need == -hq else "none")
        print("    %-5s (%s, %s) = (%+d, %+d): net 6Y %+d; its pairing needs a Higgs of 6Y %+d: %s"
              % (sec, l, r, B.SIXY[l], B.SIXY[r], net, need, pair[sec]))
    rd1 = tuple("S" if pair[s] == "H" else "S~" for s in ("up", "down", "lep"))
    rd2 = tuple("S~" if pair[s] == "H" else "S" for s in ("up", "down", "lep"))
    print("    S the flavour part of the field with 6Y = %+d (B.SIXY's H): reading (up, down, leptons) = (%s)" % (hq, ", ".join(rd1)))
    print("    S the flavour part of the field with 6Y = %+d: reading (up, down, leptons) = (%s)" % (-hq, ", ".join(rd2)))
