"""W93: main's B1658 (the twisted half bound, P-163; sealed b6542d300, output 04d64c2ff) checked on this seat's own code.
The rule (W93_RULE.md) was committed before this script; the predictions and priors are there. Not blind: B1658's
preregistration and output were read first. A fibre-frame result at one tau (tau = omega): a frozen piece.

  K1  the factorisation: ||adj Y|| = 2 |det S| ||M||^2, adj Y / det S free of S, rank Y <= 2 (random null M, random S)
  K2  the Gram spectrum of S -> Y(S, M): {1, 2, 2, 4} ||M||^2 for null M; a non-null control misses
  K3  the null residues at omega on W59's 18 lines, three sectors (analytic theta sums, 40 digits); leptons' R_1 = 0
  K4  on the actual residues: sigma1 sigma2 = 2 |det S| ||M||^2, sigma1^2 + sigma2^2 = ||Y||^2, sigma3 = 0 (40 digits);
      every two sectors' (t + 1/t) within a factor 4 for 1000 random S per line (double precision)
  K5  the census on this seat's HZ2021 file
  read-out: the pairs the bound constrains if the up sector's Higgs is not the down quarks' and the leptons'

The objects (from B1658's text, implemented here): QI = diag(i, -i), QJ = [[0, 1], [-1, 0]], QK = QI QJ, eps = QJ,
C = (1, QI, QJ, QK); the generations' blocks (QJ, QI, QK); <A, B> = sum A_mn B_mn; the dual basis E^s with
<eps C_t, E^s> = delta_st; M = sum_s R_s E^s; Y_ab(S, M) = <C_a^T eps S C_b, M>; R_s = c_s theta_s(ub) theta_s(delta),
c = (-i, -1, -1, i) on (1, i, j, k) <-> theta (1, 2, 4, 3), ub = (qL + qR) w, delta = (qL - qR) w, w = p1 tau - p2.

Run: python3 the_twisted_half_bound_checked.py  ->  the_twisted_half_bound_checked.json beside it.
"""
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_twisted_half_bound_checked.json"
HZ = HERE / "received" / "HZ2021_running_masses_MZ.json"
mp.mp.dps = 40
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
LINES18 = [(b + Fr(i, 3), b + Fr(j, 3)) for b in (Fr(1, 9), Fr(2, 9)) for i in range(3) for j in range(3)]
KEYS = ("1", "i", "j", "k")
CH = {"1": (mp.mpf(1) / 2, mp.mpf(1) / 2), "i": (mp.mpf(1) / 2, mp.mpf(0)), "j": (mp.mpf(0), mp.mpf(1) / 2),
      "k": (mp.mpf(0), mp.mpf(0))}
CS = {"1": mp.mpc(0, -1), "i": mp.mpc(-1), "j": mp.mpc(-1), "k": mp.mpc(0, 1)}


def units(lib):
    """the quaternion units, the generations' blocks, eps and the dual basis, in numpy (lib = 'np') or mpmath"""
    if lib == "np":
        I2 = np.eye(2, dtype=complex)
        QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ
        C = {"1": I2, "i": QI, "j": QJ, "k": QK}
        EC = {s: QJ @ C[s] for s in KEYS}
        G = np.array([[np.sum(EC[t] * C[s]) for s in KEYS] for t in KEYS])
        Gi = np.linalg.inv(G)
        E = {KEYS[a]: sum(Gi[b, a] * C[KEYS[b]] for b in range(4)) for a in range(4)}
        return C, QJ, [QJ, QI, QK], E
    I2 = mp.eye(2)
    QI = mp.matrix([[1j, 0], [0, -1j]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ
    C = {"1": I2, "i": QI, "j": QJ, "k": QK}
    EC = {s: QJ * C[s] for s in KEYS}
    pair = lambda A, Bm: mp.fsum(A[m, n] * Bm[m, n] for m in range(2) for n in range(2))
    G = mp.matrix([[pair(EC[t], C[s]) for s in KEYS] for t in KEYS])
    Gi = G ** -1
    E = {}
    for a in range(4):
        X = mp.zeros(2, 2)
        for b in range(4):
            X += Gi[b, a] * C[KEYS[b]]
        E[KEYS[a]] = X
    return C, QJ, [QJ, QI, QK], E


CN, EPSN, BLKN, EN = units("np")
CM, EPSM, BLKM, EM = units("mp")


def coupling_np(S, M):
    return np.array([[np.sum((Ca.T @ EPSN @ S @ Cb) * M) for Cb in BLKN] for Ca in BLKN])


def coupling_mp(S, M):
    Y = mp.zeros(3, 3)
    for a, Ca in enumerate(BLKM):
        for b, Cb in enumerate(BLKM):
            X = Ca.T * EPSM * S * Cb
            Y[a, b] = mp.fsum(X[m, n] * M[m, n] for m in range(2) for n in range(2))
    return Y


def adjugate(Y):
    return np.array([[(-1) ** (i + j) * np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1)) for j in range(3)]
                     for i in range(3)])


# ------------------------------------------------------------------------------------------- K1, K2
def K1_K2():
    rng = np.random.default_rng(93)
    rn = lambda *sh: rng.normal(size=sh) + 1j * rng.normal(size=sh)
    w_norm, w_free, w_rank = 0.0, 0.0, 0.0
    spec_dev, nonnull = 0.0, []
    basis = [np.array(b, dtype=complex).reshape(2, 2) for b in np.eye(4)]
    for _ in range(200):
        M = np.outer(rn(2), rn(2))
        A = []
        for _s in range(2):
            S = rn(2, 2)
            Y = coupling_np(S, M)
            adj = adjugate(Y)
            w_norm = max(w_norm, abs(np.linalg.norm(adj) / (abs(np.linalg.det(S)) * np.linalg.norm(M) ** 2) - 2))
            sv = np.linalg.svd(Y, compute_uv=False)
            w_rank = max(w_rank, sv[2] / sv[0])
            A.append(adj / np.linalg.det(S))
        w_free = max(w_free, np.linalg.norm(A[0] - A[1]) / np.linalg.norm(A[0]))
        Mn = M / np.linalg.norm(M)
        L = np.array([coupling_np(Bm, Mn).ravel() for Bm in basis]).T
        spec_dev = max(spec_dev, float(np.abs(np.linalg.eigvalsh(L.conj().T @ L) - np.array([1, 2, 2, 4])).max()))
    for _ in range(20):
        Mn = rn(2, 2); Mn = Mn / np.linalg.norm(Mn)
        L = np.array([coupling_np(Bm, Mn).ravel() for Bm in basis]).T
        nonnull.append(float(np.abs(np.linalg.eigvalsh(L.conj().T @ L) - np.array([1, 2, 2, 4])).max()))
    k1 = {"| ||adj Y|| / (|det S| ||M||^2) - 2 | max": w_norm, "adj Y / det S spread between two S": w_free,
          "sigma3 / sigma1 max": w_rank, "holds": bool(w_norm < 1e-10 and w_free < 1e-10 and w_rank < 1e-12)}
    k2 = {"null M: spectrum deviation max": spec_dev, "non-null control: smallest deviation": min(nonnull),
          "holds": bool(spec_dev < 1e-12 and min(nonnull) > 1e-3)}
    return k1, k2


# ------------------------------------------------------------------------------------------- the residues
def theta(s, z, t, M=40):
    """the z-form theta with characteristic CH[s]; theta_1 = -theta[1/2, 1/2]"""
    a, b = CH[s]
    v = mp.fsum(mp.exp(1j * mp.pi * ((n + a) ** 2 * t + 2 * (n + a) * (z + b))) for n in range(-M, M + 1))
    return -v if s == "1" else v


OMEGA = mp.mpc(-0.5, mp.sqrt(3) / 2)


def residues(line, sec, t=OMEGA):
    p1, p2 = (mp.mpf(x.numerator) / x.denominator for x in line)
    w = p1 * t - p2
    qL, qR = SIXY[SECTORS[sec][0]], SIXY[SECTORS[sec][1]]
    ub, dl = (qL + qR) * w, (qL - qR) * w
    return {s: CS[s] * theta(s, ub, t) * theta(s, dl, t) for s in KEYS}


def M_of(R):
    X = mp.zeros(2, 2)
    for s in KEYS:
        X += R[s] * EM[s]
    return X


def fro(X):
    return mp.sqrt(mp.fsum(abs(X[i, j]) ** 2 for i in range(X.rows) for j in range(X.cols)))


def det2(X):
    return X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]


# ------------------------------------------------------------------------------------------- K3, K4
def K3_K4():
    rng = np.random.default_rng(1658 + 93)
    rn = lambda *sh: rng.normal(size=sh) + 1j * rng.normal(size=sh)
    null_max, lep_R1 = mp.mpf(0), mp.mpf(0)
    id_max, s3_max = mp.mpf(0), mp.mpf(0)
    ratio_max = 0.0
    Ms = {}
    for line in LINES18:
        for sec in SECTORS:
            R = residues(line, sec)
            M = M_of(R)
            null_max = max(null_max, abs(det2(M)) / fro(M) ** 2)
            if sec == "lep":
                lep_R1 = max(lep_R1, abs(R["1"]) / mp.sqrt(mp.fsum(abs(R[s]) ** 2 for s in KEYS)))
            Ms[(line, sec)] = M
            for _ in range(20):
                Sn = rn(2, 2)
                S = mp.matrix([[mp.mpc(complex(Sn[i, j])) for j in range(2)] for i in range(2)])
                Y = coupling_mp(S, M)
                U, sv, V = mp.svd_c(Y)
                svs = sorted([abs(sv[i]) for i in range(3)], reverse=True)
                a = abs(svs[0] * svs[1] / (2 * abs(det2(S)) * fro(M) ** 2) - 1)
                b = abs((svs[0] ** 2 + svs[1] ** 2) / fro(Y) ** 2 - 1)
                id_max = max(id_max, a, b)
                s3_max = max(s3_max, svs[2] / svs[0])
        Mn = {sec: np.array([[complex(Ms[(line, sec)][i, j]) for j in range(2)] for i in range(2)]) for sec in SECTORS}
        for _ in range(1000):
            S = rn(2, 2)
            T = {}
            for sec in SECTORS:
                sv = np.linalg.svd(coupling_np(S, Mn[sec]), compute_uv=False)
                t = sv[1] / sv[0]
                T[sec] = t + 1 / t
            for a_, b_ in (("up", "down"), ("up", "lep"), ("down", "lep")):
                r = T[a_] / T[b_]
                ratio_max = max(ratio_max, r, 1 / r)
    k3 = {"|det M| / ||M||^2 max": float(null_max), "leptons' |R_1| / |R| max": float(lep_R1),
          "holds": bool(null_max < mp.mpf(10) ** -25 and lep_R1 < mp.mpf(10) ** -25)}
    k4 = {"spectrum identities, max relative": float(id_max), "sigma3 / sigma1 max": float(s3_max),
          "largest (t + 1/t) ratio over 18 000 one-Higgs draws": ratio_max,
          "holds": bool(id_max < mp.mpf(10) ** -20 and s3_max < mp.mpf(10) ** -20 and ratio_max <= 4 + 1e-9)}
    return k3, k4


# ------------------------------------------------------------------------------------------- K5 and the read-out
def K5():
    hz = json.loads(HZ.read_text(encoding="utf-8"))["masses_GeV"]
    v, s = hz["value"], hz["sigma"]
    pair = {"up": ("c", "t"), "down": ("s", "b"), "lep": ("mu", "tau")}
    T = {}
    for sec, (a, b) in pair.items():
        t = v[a] / v[b]
        dt = t * math.hypot(s[a] / v[a], s[b] / v[b])
        T[sec] = (t + 1 / t, (1 / t ** 2 - 1) * dt)                # d(t + 1/t) = (1 - 1/t^2) dt, in magnitude
    out = {}
    for a, b in (("up", "down"), ("up", "lep"), ("down", "lep")):
        r = T[a][0] / T[b][0]
        rr = max(r, 1 / r)
        rel = math.hypot(T[a][1] / T[a][0], T[b][1] / T[b][0])
        out[f"{a}/{b}"] = {"ratio": r, "sigma": rr * rel, "z against 4": (rr - 4) / (rr * rel)}
    refuted = any(x["z against 4"] > 3 for x in out.values())
    rounded = {k: round(x["ratio"], 2) for k, x in out.items()}
    holds = rounded == {"up/down": 5.08, "up/lep": 15.92, "down/lep": 3.13} and out["up/lep"]["z against 4"] > 3
    readout = {"if the up sector has its own Higgs, the pairs constrained": ["down/lep"],
               "down/lep ratio": out["down/lep"]["ratio"], "down/lep z against 4": out["down/lep"]["z against 4"],
               "within the bound": bool(out["down/lep"]["z against 4"] < 0)}
    return {"pairs": out, "refuted at 3 sigma": refuted, "holds": bool(holds)}, readout


def main():
    out = {"rule": "W93_RULE.md", "status": "one run; not blind (B1658's output read first)"}
    out["K1"], out["K2"] = K1_K2()
    out["K3"], out["K4"] = K3_K4()
    out["K5"], out["read-out: two Higgs fields (up; down and leptons)"] = K5()
    out["all cells hold"] = all(out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5"))
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print({k: out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5")}, "all", out["all cells hold"])


if __name__ == "__main__":
    main()
