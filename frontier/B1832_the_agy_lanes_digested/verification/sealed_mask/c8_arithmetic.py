"""SEALED-DIGEST CHECK c8 (value-free arithmetic and one residue identity on main's code).
 (a) Q2 = qL^2 + qR^2 per sector (Theorem 20 B.2; Theorem 25): (17, 5, 45); lepton/down = 9 because (qL, qR)_lepton = 3 (-1, 2).
 (b) lam = -exp(-i pi (2j+1)/5) = exp(2 pi i (2-j)/5) (Theorem 18 C.1).
 (c) T: tau -> tau+1 maps the order-10 strip lines (2/5, (2j+1)/10) by j -> j-2 mod 5 (a single 5-cycle; Theorem 23 Step 3);
     on main's residues |R_s(tau+1; line j)| = |R_s(tau; line j-2)| in every sector and channel.
 (d) the spin-flavour lock (sm_19_gate step 4): U = ((LR)^3 - I)/4 = [[3,2],[2,1]], det -1, U = I mod 2, so each of the four
     spin characters locks exactly 16 of the 64 8-torsion points.
 (e) D(eta) = e^{2 eta} D_raw for a light-generation split diag(e^-eta, e^eta, 1) on the lepton masses (Theorem 20 A.2)."""
import cmath, math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
Q2 = {s: ql * ql + qr * qr for s, ql, qr in Z.SECTORS}
print("(a) Q2:", Q2, "; lepton/down =", Q2["lepton"] / Q2["down"], "; up/down =", Q2["up"] / Q2["down"])
print("(b) max |-exp(-i pi(2j+1)/5) - exp(2 pi i(2-j)/5)| over j:", max(abs(-cmath.exp(-1j * math.pi * (2 * j + 1) / 5) - cmath.exp(2j * math.pi * (2 - j) / 5)) for j in range(5)))
perm = {j: next(k for k in range(5) if abs(((2 * j + 1) / 10 - 0.4 - (2 * k + 1) / 10) % 1) < 1e-12 or abs(((2 * j + 1) / 10 - 0.4 - (2 * k + 1) / 10) % 1 - 1) < 1e-12) for j in range(5)}
print("(c) T on the order-10 lines (line_w(p1, p2, tau+1) = line_w(p1, p2 - p1, tau)):", perm)
worst = 0.0
for tau in (0.21 + 1.8j, 0.37 + 2.5j):
    for j in range(5):
        k = perm[j]
        for sn, ql, qr in Z.SECTORS:
            R1 = B.residues(*B.sector_twists(B.line_w(0.4, (2 * j + 1) / 10, tau + 1), tau + 1, ql, qr), tau + 1)
            R0 = B.residues(*B.sector_twists(B.line_w(0.4, (2 * k + 1) / 10, tau), tau, ql, qr), tau)
            m = max(abs(v) for v in R0.values())
            worst = max(worst, max(abs(abs(R1[s]) - abs(R0[s])) / m for s in B.UNITS))
print("    max | |R(tau+1; j)| - |R(tau; T j)| | / max|R| :", worst)
U = (np.linalg.matrix_power(np.array([[2, 1], [1, 1]]), 3) - np.eye(2, dtype=int)) // 4
print("(d) (LR)^3 =", np.linalg.matrix_power(np.array([[2, 1], [1, 1]]), 3).tolist(), "; U =", U.tolist(), "; det U =", round(np.linalg.det(U)),
      "; U mod 2 =", (U % 2).tolist(), "; locked points per spin character:",
      [sum(1 for a in range(8) for b in range(8) if tuple((U @ np.array([a, b])) % 2) == es) for es in ((0, 0), (1, 0), (0, 1), (1, 1))])
me = np.array([1.0, 7.0, 50.0]); md = np.array([2.0, 5.0, 60.0]); eta = 0.37
Draw = (me[1] / me[0]) * (md[0] / md[1]); me2 = me * np.array([math.exp(-eta), math.exp(eta), 1])
print("(e) D(eta)/D_raw =", (me2[1] / me2[0]) * (md[0] / md[1]) / Draw, " e^{2 eta} =", math.exp(2 * eta), "(illustrative numbers, not frame values)")
