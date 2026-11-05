"""agy digest, Theorem 10's frame identities, main's code only (frame_common).  Data-free.
  T10e  c_s(3/5, 4/5; tau) = c_s(2/5, 1/5; tau)  (the involution partner -w_eig mod Z^2), three sectors, two tau
  T10f  Y_s(3/5, 4/5) = lambda_s Y_s(2/5, 1/5) with lambda_u = e^{-4 pi i/5}, lambda_d = lambda_e = 1 (the lane's claim),
        in FR-COV (the lane's scalar a0 = c_s b) and in FR-FIB (a0 = 0)
  T10g  T^8: Y_s((2/5, j/5), tau + 8) = e^{i phi_s} Y_s((2/5, j-1/5), tau), phi = (2 pi/25, -4 pi/5, 4 pi/5) claimed,
        all five j, one tau; the fitted common phase is printed; the det-phase shift 3(phi_u + phi_d) computed from det
  T10h  the five lines (2/5, j/5) at the SAME tau are distinct (the relabelling selects nothing): spread of m2/m3 per sector
L = 2.36 as the lane's Theorem 10 uses (the identities are L-independent: u is scaled channel by channel)."""
import cmath, json, math, pathlib
import numpy as np
from frame_common import B, norms, matter, higgs, yukawa, phase_ratio, CHARS

OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v, flush=True)
L = 2.36
SEC = ("up", "down", "lepton")
def Ys(line, tau, frcov=True, cache=None):
    out = {}
    for s in SEC:
        R, c = norms(line, tau, s)
        S, _, _ = higgs(tau, CHARS[s] if frcov else None)
        out[s] = (yukawa(S, matter(R, c, L)), c)
    return out

claimed = {"up": cmath.exp(-4j * math.pi / 5), "down": 1, "lepton": 1}
for tau in (complex(0.17, 2.05), complex(-0.31, 2.83)):
    A = Ys((0.4, 0.2), tau); Bm = Ys((0.6, 0.8), tau); A0 = Ys((0.4, 0.2), tau, False); B0 = Ys((0.6, 0.8), tau, False)
    rec("T10e tau %s max|c(3/5,4/5) - c(2/5,1/5)| over channels, by sector" % tau,
        {s: max(abs(A[s][1][k] - Bm[s][1][k]) for k in B.UNITS if A[s][1][k] is not None) for s in SEC})
    for nm, X, Z in (("FR-COV", A, Bm), ("FR-FIB", A0, B0)):
        res = {}
        for s in SEC:
            lam, r = phase_ratio(Z[s][0], X[s][0])
            res[s] = {"lambda/claimed": complex(np.round(lam / claimed[s], 12)), "residual": r}
        rec("T10f tau %s %s Y(3/5,4/5) = lambda Y(2/5,1/5)" % (tau, nm), res)

tau = complex(0.23, 2.15)
phi_claim = {"up": 2 * math.pi / 25, "down": -4 * math.pi / 5, "lepton": 4 * math.pi / 5}
t8 = {}; dets = {}
for j in range(5):
    Ysh = Ys((0.4, j / 5), tau + 8); Y0 = Ys((0.4, (j - 1) / 5), tau)
    row = {}
    for s in SEC:
        lam, r = phase_ratio(Ysh[s][0], Y0[s][0])
        row[s] = {"phase/pi": round(cmath.phase(lam) / math.pi, 10), "|lambda|": round(abs(lam), 12), "residual": r,
                  "c spread": max(abs(Ysh[s][1][k] - Y0[s][1][k]) for k in B.UNITS if Y0[s][1][k] is not None)}
    t8["j=%d" % j] = row
    du = np.angle(np.linalg.det(Ysh["up"][0]) * np.linalg.det(Ysh["down"][0])) - np.angle(np.linalg.det(Y0["up"][0]) * np.linalg.det(Y0["down"][0]))
    dets["j=%d" % j] = round(((du + math.pi) % (2 * math.pi) - math.pi) / math.pi, 10)
rec("T10g T^8 at tau = %s: Y((2/5,j/5), tau+8) vs Y((2/5,(j-1)/5), tau)" % tau, t8)
rec("T10g claimed phases / pi", {s: phi_claim[s] / math.pi for s in SEC})
rec("T10g det-phase shift of arg det(Y_u Y_d) under T^8, /pi mod 2 (claimed -4/25 = -0.16)", dets)
# the inversion's det-phase shift directly
for tau_ in (complex(0.17, 2.05),):
    A = Ys((0.4, 0.2), tau_); Bm = Ys((0.6, 0.8), tau_)
    dd = np.angle(np.linalg.det(Bm["up"][0]) * np.linalg.det(Bm["down"][0])) - np.angle(np.linalg.det(A["up"][0]) * np.linalg.det(A["down"][0]))
    rec("T10g det-phase shift under w -> -w_eig, /pi mod 2 (claimed -2/5)", round(((dd + math.pi) % (2 * math.pi) - math.pi) / math.pi, 10))
# T10h
spread = {}
Yl = {j: Ys((0.4, j / 5), tau) for j in range(5)}
for s in SEC:
    r = []
    for j in range(5):
        sv = np.sort(np.linalg.svd(Yl[j][s][0], compute_uv=False)); r.append(float(sv[1] / sv[2]))
    spread[s] = [round(v, 6) for v in r]
rec("T10h m2/m3 per sector on the five lines (2/5, j/5), j = 0..4, at the same tau (FR-COV)", spread)
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
