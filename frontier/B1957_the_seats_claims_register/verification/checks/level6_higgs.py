"""B1957: the selection of the Higgs's mode among the six of flux 6, as agy-002's gate 2 defines it, recomputed by main on
main's own overlap (cim_overlap.py).  Data-free; no mass enters.
The definition is the seat's (read in its card and its script's text, not run): on the six Higgs modes,
  B(tau) = sum over the 24 points w of order 5 and the three sectors (weights 3, 3, 1) of  sum_ij conj(Y_ijk) Y_ijl,
averaged over one period of the closed geodesic of M = [[2, 1], [1, 1]] and projected on what commutes with M's matrix U_M
on the six modes; K = (theta_m / L)^2 on the eigenvector of U_M with eigenphase theta_m, L = 4 ln(phi); M_H^2 = K - c B, c > 0.
What main tests: U_M's order and eigenphases, and that it is the modes' own transport along M (H1, H3); the seat's result
as defined (H5, first two lines); and whether B is a function of the point w on the torus (H2, H4, H5, H6).
It is not.  The Higgs's Wilson line is (q_L + q_R) w / 2 = +-3 w / 2, and a point w of the torus is defined up to the
lattice, so the Wilson line is defined only up to half the lattice, which acts on the six modes by the clock and the shift
of order two, Z^3 and X^3.  The seat evaluates each point at one lift (a, b in [0, 1)).
The reason the lift-invariant B selects nothing (H6), in three lines:
  (1) Y_ijk vanishes unless k = i + j + 1 mod 3, so B joins only k with k + 3; averaging over Z^3 removes that entry and
      averaging over X^3 equalises B_kk with B_(k+3)(k+3): the average is diag(b_0, b_1, b_2, b_0, b_1, b_2);
  (2) the product of two sections of flux 3 is a section of flux 6, so sum_k |Y_ijk|^2 = integral |psi_i|^2 |psi_j|^2;
  (3) moving z by tau/3 carries psi_i to psi_(i+1) for both matter fields, so that integral depends on i - j only, and
      the three b_k, each a sum over i + j + 1 = k mod 3, are equal.
So for every point, every sector and every modulus the lift-invariant B is a multiple of the identity."""
import sys, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import cim_overlap as C
PTS5 = [(a / 5, b / 5) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
SECT = ((1, -4, 3), (1, 2, 3), (-3, 6, 1))
k = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k ** 2 / 6)); S6 = np.exp(-1j * np.pi / 4) * np.exp(-2j * np.pi * np.outer(k, k) / 6) / np.sqrt(6)
UM = T6 @ (S6.conj().T @ T6.conj().T @ S6)                       # M = R L with R = T and L = S^-1 T^-1 S
PHI = (1 + 5 ** 0.5) / 2; LM = 4 * np.log(PHI)


def bubble(tau, n=48):
    B = np.zeros((6, 6), complex)
    for a, b in PTS5:
        w = a * tau + b
        for qL, qR, nc in SECT:
            Y = C.overlap(tau, qL * w, qR * w, (qL + qR) * w / 2, n=n); B += nc * np.einsum("ijk,ijl->kl", Y.conj(), Y)
    return B


def geod(s): w = 1j * np.exp(s); return (PHI * w - 1 / PHI) / (w + 1)


def transport_g(Mf, sp, tau, zeta, g, n=48):
    """<new mode a | old mode b>: new = the mode at g.tau in the variable z / (c tau + d), g = (a, b, c, d)"""
    a, b, c, d = g; j = c * tau + d; z = C.cell(tau, n)
    new = C.psi(Mf, *sp, z / j, (a * tau + b) / j, zeta / j); old = C.psi(Mf, *sp, z, tau, zeta)
    return np.einsum("axy,bxy->ab", new, old.conj()) / n ** 2


Z3 = np.diag((-1.0) ** k); X3 = np.roll(np.eye(6), 3, axis=0); KLEIN = (np.eye(6), Z3, X3, Z3 @ X3)
lifted = lambda B: sum(g @ B @ g.conj().T for g in KLEIN) / 4
upto = lambda A, Bm: min(np.abs(A - ph * Bm).max() for ph in [A.ravel()[np.abs(Bm).argmax()] / Bm.ravel()[np.abs(Bm).argmax()]])


def one(tau, w, n=48):
    B = np.zeros((6, 6), complex)
    for qL, qR, nc in SECT:
        Y = C.overlap(tau, qL * w, qR * w, (qL + qR) * w / 2, n=n); B += nc * np.einsum("ijk,ijl->kl", Y.conj(), Y)
    return B


if __name__ == "__main__":
    ev, V = np.linalg.eig(UM); o = np.argsort(np.angle(ev)); ev, V = ev[o], V[:, o] / np.linalg.norm(V[:, o], axis=0)
    print("H1: U_M^12 = 1 to %.1e, and no lower power; eigenphases over pi: %s (the seat: -5/6, -1/3, -1/6, 1/6, 1/3, 5/6)" % (np.abs(np.linalg.matrix_power(UM, 12) - np.eye(6)).max(), np.round(np.angle(ev) / np.pi, 6).tolist()))
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4; B1 = one(tau, w)
    print("H2: one point w of order 5, moved by a lattice vector: B(w + 1) against Z^3 B Z^-3: %.1e (against B itself: %.2f); B(w + tau) against X^3 B X^-3: %.1e (against B itself: %.2f); scale %.1f" % (
        np.abs(one(tau, w + 1) - Z3 @ B1 @ Z3).max(), np.abs(one(tau, w + 1) - B1).max(), np.abs(one(tau, w + tau) - X3 @ B1 @ X3.T).max(), np.abs(one(tau, w + tau) - B1).max(), np.abs(B1).max()))
    print("    so the Higgs's Wilson line (q_L + q_R) w / 2 = +-3 w / 2 is not a function of the point w on the torus: the four lifts of w differ by the clock and shift of order two on the six modes")
    W = transport_g(6, (0.0, 0.0), tau, 0.0, (2, 1, 1, 1))
    cands = {"T L (the seat's U_M)": UM, "L T": (S6.conj().T @ T6.conj().T @ S6) @ T6, "conj(T L)": UM.conj(), "conj(L T)": ((S6.conj().T @ T6.conj().T @ S6) @ T6).conj()}
    print("H3: the six modes' own transport along M = [[2, 1], [1, 1]] (unitary to %.1e), against, up to a phase: %s" % (C.unit_err(W), "; ".join("%s %.1e" % (kk, upto(W, vv)) for kk, vv in cands.items())))
    B0 = bubble(tau); BT = bubble(tau + 1); BS = bubble(-1 / tau); BM = bubble((2 * tau + 1) / (tau + 1))
    print("H4: the sum over the 24 points with representatives in the unit cell (the seat's), at tau + 1, -1/tau and M.tau, against B conjugated by the modes' transport: %.1e, %.1e, %.1e (scale %.1f)" % (np.abs(BT - T6 @ B0 @ T6.conj().T).max(), np.abs(BS - S6 @ B0 @ S6.conj().T).max(), np.abs(BM - W @ B0 @ W.conj().T).max(), np.abs(B0).max()))
    print("    the same sum averaged over the four lifts of each point: %.1e, %.1e, %.1e" % (np.abs(lifted(BT) - T6 @ lifted(B0) @ T6.conj().T).max(), np.abs(lifted(BS) - S6 @ lifted(B0) @ S6.conj().T).max(), np.abs(lifted(BM) - W @ lifted(B0) @ W.conj().T).max()))
    ns = 16; Braw = sum(bubble(geod(LM * (i + 0.5) / ns)) for i in range(ns)) / ns
    for lab, Bx in (("representatives in the unit cell (the seat's)", Braw), ("averaged over the lifts", lifted(Braw))):
        for lab2, Wm in (("U_M", UM), ("conj U_M", UM.conj())):
            e2, V2 = np.linalg.eig(Wm); o2 = np.argsort(np.angle(e2)); e2, V2 = e2[o2], V2[:, o2] / np.linalg.norm(V2[:, o2], axis=0)
            Bp = sum(np.linalg.matrix_power(Wm.conj().T, n) @ Bx @ np.linalg.matrix_power(Wm, n) for n in range(12)) / 12
            d = np.real(np.einsum("am,ab,bm->m", V2.conj(), Bp, V2)); Kd = (np.angle(e2) / LM) ** 2
            gs = [np.angle(e2[np.argsort(Kd - c * d)[0]]) / np.pi for c in (1e-4, (4 * np.pi / 50) / (16 * np.pi ** 2), 1e-2)]
            m = Kd - (4 * np.pi / 50) / (16 * np.pi ** 2) * d; g = np.sort(m)
            print("H5: %s, projected on the commutant of %-8s: B on the eigenvectors (phases/pi %s): %s; ground mode's phase/pi for three values of c: %s; least gap at the seat's c %.2e" % (lab, lab2, np.round(np.angle(e2) / np.pi, 3).tolist(), np.round(d, 4).tolist(), np.round(gs, 3).tolist(), np.diff(g).min()))
    # H6: the reason, tested piece by piece at one point
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4; worst_sel = worst_par = 0.0; z = C.cell(tau, 48)
    for qL, qR, nc in SECT:
        zL, zR, zH = qL * w, qR * w, (qL + qR) * w / 2; Y = C.overlap(tau, zL, zR, zH)
        pL = C.psi(3, 0.5, 0.5, z, tau, zL); pR = C.psi(3, 0.5, 0.5, z, tau, zR)
        N = np.einsum("ixy,jxy->ij", np.abs(pL) ** 2, np.abs(pR) ** 2) / 48 ** 2
        worst_par = max(worst_par, np.abs((np.abs(Y) ** 2).sum(axis=2) - N).max())
        worst_sel = max(worst_sel, max(abs(Y[i, j, kk]) for i in range(3) for j in range(3) for kk in range(6) if (kk - i - j - 1) % 3))
        circ = max(abs(N[i, j] - N[(i + 1) % 3, (j + 1) % 3]) for i in range(3) for j in range(3))
        b1 = lifted(np.einsum("ijk,ijl->kl", Y.conj(), Y))
        print("H6: sector (%d, %d), one point: selection rule %.1e; sum_k |Y_ijk|^2 = integral |psi_i|^2 |psi_j|^2 to %.1e; that integral depends on i - j only to %.1e; the four lifts averaged: distance from a multiple of the identity %.1e" % (qL, qR, worst_sel, worst_par, circ, np.abs(b1 - np.trace(b1) / 6 * np.eye(6)).max()))
    for tau in (0.23 + 1.37j, -0.31 + 0.83j):
        Bq = bubble(tau); BL = lifted(Bq)
        print("H6: tau = %s: the seat's sum has eigenvalues %s; averaged over the lifts %s" % (tau, np.round(np.linalg.eigvalsh((Bq + Bq.conj().T) / 2), 4).tolist(), np.round(np.linalg.eigvalsh((BL + BL.conj().T) / 2), 4).tolist()))
    print("So: with B a function of the torus's points, M_H^2 = K - c B is K up to a constant: its ground space is the pair of modes with phases +-pi/6 (dimension 2, one bit), for every c.")
    # Corrected 2026-11-18 (the physical lane's finding C8-02; checks/physical_c8_tick_higgs.py): 'one bit' in the line above says too much.
    # The ground space is a complex plane and every unit vector of it is a ground direction; it is one bit only on the two eigenlines.
    # The printed line is left as it ran; the run file is the record of that run.
