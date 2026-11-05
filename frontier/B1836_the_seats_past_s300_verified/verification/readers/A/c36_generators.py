"""S301-A check c36 (value-free; MAIN's code only: b1656_funcs via B1821's cm_zero_line, B1691's DR, B1667's radius column).
Theorem 36 (agy, c5c9236df) claims: (1) DR(tau + 1) = e^{i pi/4} (h_I, h_K, -h_J) (in main's (I, J, K) order) and
(1/2) eta^3 gains e^{i pi/4}; (2) DR.DR = (eta^3/2)^2; (3) with the singlet sigma = i r eta^3 / 2 every mass ratio and |V_CKM|
is invariant under A, P, N, T, M and J is invariant under A, P, N, T and odd under M, "for all real r".
Main's B1832 S300 bullet 'T^2, not T, at the residue level' compared |R_s| channel by channel (c8b_tshift.py); here the
same comparison is repeated with channels j and k exchanged, and the full outputs are compared directly.
Main's line convention: w = p1 tau - p2.  T: (tau, p2) -> (tau + 1, p2 + p1) keeps w.  A: p2 -> p2 + 1.  P: p1 -> p1 + 1.
N: (p1, p2) -> -(p1, p2).  M: (p2, tau) -> (-p2, -conj tau).  Prints deviations only (no output value)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import cmath, math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
SECT = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]


def eta(tau):
    q = cmath.exp(2j * math.pi * tau)
    p = 1.0 + 0j
    for k in range(1, 400):
        p *= 1 - q ** k
    return cmath.exp(2j * math.pi * tau / 24) * p


def S_of(a0, h):
    return a0 * np.eye(2) + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK


def adj(S):
    return B.EPS @ S.T @ B.EPS.T


def tilde(S):
    return B.EPS @ S.conj() @ B.EPS.T


_CACHE = {}


def Ms(tau, w, L):
    key = (round(tau.real, 12), round(tau.imag, 12), round(w.real, 12), round(w.imag, 12), round(L, 12))
    if key in _CACHE:
        return _CACHE[key]
    out = {}
    for sn, ql, qr in SECT:
        x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau)
        c = B.cA(x, yy, tau, R)
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        out[sn] = (B.weighted_M(u), R)
    _CACHE[key] = out
    return out


def outputs(tau, p1, p2, L, direction, r, reading):
    w = B.line_w(p1, p2, tau)
    h = np.array(Z.direction(direction, tau))
    a0 = 1j * r * eta(tau) ** 3 / 2
    S = S_of(a0, h)
    rd = {"lane36": (adj(tilde(S)), S, S), "FR-FIB": (tilde(S_of(0, h)), S_of(0, h), S_of(0, h)),
          "FR-COV": (-adj(S), S, S)}[reading]
    M = Ms(tau, w, L)
    Y = {sn: B.coupling(Sx, M[sn][0]) for (sn, _, _), Sx in zip(SECT, rd)}
    out = []
    U = {}
    for sn in ("up", "down", "lepton"):
        u_, s_, _ = np.linalg.svd(Y[sn])
        out += [s_[1] / s_[0], s_[2] / s_[0]]
        U[sn] = u_[:, ::-1]
    V = U["up"].conj().T @ U["down"]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return np.array(out), np.abs(V), J, M


if __name__ == "__main__":
    print("c36: Theorem 36's claims on main's code")
    taus = (complex(0.21, 2.3), complex(0.37, 3.05), complex(-0.12, 1.6))
    # (1) T multipliers
    wt = 0.0; we = 0.0; wd = 0.0
    for t in taus:
        h0 = np.array(Z.direction("DR", t)); h1 = np.array(Z.direction("DR", t + 1))
        wt = max(wt, np.abs(h1 - cmath.exp(1j * math.pi / 4) * np.array([h0[0], h0[2], -h0[1]])).max() / np.abs(h0).max())
        we = max(we, abs(eta(t + 1) ** 3 - cmath.exp(1j * math.pi / 4) * eta(t) ** 3) / abs(eta(t) ** 3))
        wd = max(wd, abs(h0 @ h0 - (eta(t) ** 3 / 2) ** 2) / abs(eta(t) ** 3 / 2) ** 2)
    print("  (1) DR(tau+1) vs e^{i pi/4}(h_I, h_K, -h_J): rel dev %.1e;  eta^3(tau+1) vs e^{i pi/4} eta^3: %.1e" % (wt, we))
    print("  (2) DR.DR vs (eta^3/2)^2: rel dev %.1e  (already on main: LAW_MAP B1732 row, P-308)" % wd)
    # F_10 under T: is it a uniform phase times the same signed permutation?
    wf = 0.0
    for t in taus:
        f0 = np.array(Z.direction("F_10", t)); f1 = np.array(Z.direction("F_10", t + 1))
        perm = np.array([f0[0], f0[2], -f0[1]])
        ph = f1[0] / perm[0]
        wf = max(wf, np.abs(f1 - ph * perm).max() / np.abs(f0).max())
    print("      F_10(tau+1) = (phase) x (h_I, h_K, -h_J): rel dev %.1e" % wf)

    # residues: channel-by-channel vs j<->k exchanged, tau -> tau + 1 with w fixed, every sector
    cbc = 0.0; swp = 0.0
    for t in taus:
        for (p1, p2) in ((0.4, 0.1), (0.4, 0.5), (0.4, 0.2), (1 / 3, 1 / 7)):
            w = B.line_w(p1, p2, t)
            for sn, ql, qr in SECT:
                R0 = B.residues(*B.sector_twists(w, t, ql, qr), t)
                R1 = B.residues(*B.sector_twists(w, t + 1, ql, qr), t + 1)
                mx = max(abs(v) for v in R0.values())
                cbc = max(cbc, max(abs(abs(R1[s]) - abs(R0[s])) for s in B.UNITS) / mx)
                sw = {"1": "1", "i": "i", "j": "k", "k": "j"}
                swp = max(swp, max(abs(abs(R1[s]) - abs(R0[sw[s]])) for s in B.UNITS) / mx)
    print("  residues under T (w fixed): |R_s(tau+1)| - |R_s(tau)| channel by channel: %.2e;  with j <-> k exchanged: %.1e" % (cbc, swp))

    # (3) the generators on the full outputs
    lines = ((0.4, 0.1), (0.4, 0.5), (0.4, 0.2), (1 / 3, 1 / 7))
    for direction in ("DR", "F_10"):
        for reading in ("lane36", "FR-FIB", "FR-COV"):
            for r in ((0.0, 0.3, 0.7, 1.4) if reading != "FR-FIB" else (0.0,)):
                worst = {g: 0.0 for g in "APNTM"}
                for t in taus[:2]:
                    L = Z.radii(t)[0]
                    for (p1, p2) in lines:
                        o0, v0, j0, _ = outputs(t, p1, p2, L, direction, r, reading)
                        gens = {"A": (t, p1, p2 + 1, +1), "P": (t, p1 + 1, p2, +1), "N": (t, -p1, -p2, +1),
                                "T": (t + 1, p1, p2 + p1, +1), "M": (-t.conjugate(), p1, -p2, -1)}
                        for g, (tg, a_, b_, js) in gens.items():
                            o, vv, jj, _ = outputs(tg, a_, b_, L, direction, r, reading)
                            dev = max(np.abs(o - o0).max() / max(np.abs(o0).max(), 1e-300), np.abs(vv - v0).max(), abs(jj - js * j0) / max(abs(j0), 1e-12))
                            worst[g] = max(worst[g], dev)
                print("  %-5s %-7s r=%.1f: worst relative deviation  A %.1e  P %.1e  N %.1e  T %.1e  M(J odd) %.1e"
                      % (direction, reading, r, worst["A"], worst["P"], worst["N"], worst["T"], worst["M"]), flush=True)
