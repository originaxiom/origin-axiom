"""B1957: the physical lane's package 'registered domain index join' (2026-11-16), its two continuation notes
NORMALIZED_WILSON_CROSSING_VERTEX.md and ACTUAL_SLOT_VERTEX_AND_HIGHER_MASS.md: their finite algebra, on main.
The notes are hand derivations conditional on the lane's supplied parent, its mode and domain theorem and its Wilson
and spin state; none of that analysis is here.
 V1  the normalisation algebra (sympy): with Z_a = h A_w/(2G), Z_u = k c+ I_w/G, Z_v = k c- I_w/G (c+ c- = 1),
     Z_H = h A_g/G, e_H = |q|/sqrt(Z_H) and |Y_raw| = |q| k A_w/G, the normalised coupling obeys
     |y|^2/e_H^2 = 2 A_w A_g/I_w^2, in which G, h, k, q and the frame constants cancel.
 V2  the bound: I_w^2 <= A_w A_g (Cauchy-Schwarz), so |y|/e_H >= sqrt 2, with equality when the conformal factor is
     proportional to |f|: on a grid, a constant factor gives exactly 2 and a non-constant one gives more.
 V3  in SU(5) with H = diag(-2, -2, -2, 3, 3): [H, E] = 5 E for a root vector between a weak and a colour index.
 V4  a matrix of the block form [[0 (2 x 2), x], [y, z]] has rank at most 2 (random draws).
 V5  the second-order reduction in a finite model: M(t) = M0 + t V1 + t^2 V2 with a 3-dimensional kernel on each
     side; Y1 = P_L V1 P_R of rank 2 by the slot rule; Y2 = P_L V2 P_R - P_L V1 Q_R C^-1 Q_L V1 P_R; the three smallest
     singular values of M(t) are t s_1(Y1), t s_2(Y1) and t^2 |l^dagger Y2 r| to leading order.
 V6  the five-coefficient stabiliser: L^T E_ij R = E_ij for (i, j) in {13, 23, 31, 32, 33} forces L = c, R = 1/c
     (the linear system for (L^T, R^-1) has a one-dimensional solution space); with E_33 left out it has more.
 V7  the canonical current: if R preserves the Gram G (R^dagger G R = G) then G^(1/2) R G^(-1/2) is unitary."""
import functools
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    rng = np.random.default_rng(21)
    G, h, k, cp, Aw, Ag, Iw, q = sp.symbols("G h k c_plus A_w A_g I_w q", positive=True)
    Za, Zu, Zv, ZH = h * Aw / (2 * G), k * cp * Iw / G, k * (1 / cp) * Iw / G, h * Ag / G
    y = (q * k * Aw / G) / sp.sqrt(Za * Zu * Zv); eH = q / sp.sqrt(ZH)
    print("V1: |y| = %s; |y|^2/e_H^2 - 2 A_w A_g/I_w^2 = %s" % (sp.simplify(y), sp.simplify(y ** 2 / eH ** 2 - 2 * Aw * Ag / Iw ** 2)))
    n = 400; xs = (np.arange(n) + 0.5) / n; X, Yg = np.meshgrid(xs, xs); f = np.ones_like(X)
    for name, Om in (("a constant conformal factor", np.full_like(X, 1.7)), ("a non-constant one", 1.0 + 0.8 * np.cos(2 * np.pi * X) * np.sin(2 * np.pi * Yg) ** 2), ("one that decays", np.exp(-3 * Yg))):
        A_w = np.mean(np.abs(f) ** 2); A_g = np.mean(Om ** 2); I_w = np.mean(Om * np.abs(f)); print("V2: %s: 2 A_w A_g/I_w^2 = %.6f" % (name, 2 * A_w * A_g / I_w ** 2))
    H = np.diag([-2.0, -2, -2, 3, 3]); E = np.zeros((5, 5)); E[3, 0] = 1.0
    print("V3: [H, E] = 5 E for E between a weak and a colour index: %s; the charge over six: 5/6" % np.allclose(H @ E - E @ H, 5 * E))
    worst = 0
    for _ in range(1000):
        Y = np.zeros((3, 3), dtype=complex); Y[:2, 2] = rng.normal(size=2) + 1j * rng.normal(size=2); Y[2, :] = rng.normal(size=3) + 1j * rng.normal(size=3); worst = max(worst, np.linalg.matrix_rank(Y))
    print("V4: the largest rank over 1,000 random matrices of the block form: %d" % worst)
    # V5
    N = 9; U, _ = np.linalg.qr(rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))); W, _ = np.linalg.qr(rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)))
    sv0 = np.array([0, 0, 0, 1.3, 1.7, 2.1, 2.6, 3.0, 3.4]); M0 = U @ np.diag(sv0) @ W.conj().T
    PL = U[:, :3] @ U[:, :3].conj().T; PR = W[:, :3] @ W[:, :3].conj().T; QL = np.eye(N) - PL; QR = np.eye(N) - PR
    V1 = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); V2 = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    # impose the slot rule on the kernel block: the 2 x 2 form/form corner of U^dagger V1 W vanishes
    blk = U.conj().T @ V1 @ W; blk[:2, :2] = 0; V1 = U @ blk @ W.conj().T
    y1 = (U.conj().T @ V1 @ W)[:3, :3]; Cinv = W[:, 3:] @ np.diag(1 / sv0[3:]) @ U[:, 3:].conj().T
    y2 = (U.conj().T @ (V2 - V1 @ Cinv @ V1) @ W)[:3, :3]
    s1 = np.linalg.svd(y1, compute_uv=False); uu, ss, vh = np.linalg.svd(y1); l = uu[:, 2]; r = vh[2, :].conj(); m2 = abs(l.conj() @ y2 @ r)
    rows = []
    for t in (1e-2, 1e-3, 1e-4):
        s = np.sort(np.linalg.svd(M0 + t * V1 + t * t * V2, compute_uv=False))[:3]; rows.append((t, s[2] / (t * s1[0]), s[1] / (t * s1[1]), s[0] / (t * t * m2)))
    print("V5: rank of Y1: %d; at t = 1e-2, 1e-3, 1e-4 the three smallest singular values over (t s_1, t s_2, t^2 |m2|): %s" % (np.linalg.matrix_rank(y1), [tuple(round(float(x), 4) for x in row[1:]) for row in rows]))
    # V6
    def stab(pairs):
        rows = []
        for i, j in pairs:
            Eij = np.zeros((3, 3)); Eij[i, j] = 1.0
            # unknowns X = L^T (9), Z = R^-1 (9): X E - E Z = 0
            A = np.zeros((9, 18))
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        A[3 * a + b, 3 * a + c] += Eij[c, b]            # (X E)_ab = sum_c X_ac E_cb
                        A[3 * a + b, 9 + 3 * c + b] -= Eij[a, c]        # (E Z)_ab = sum_c E_ac Z_cb
            rows.append(A)
        return 18 - np.linalg.matrix_rank(np.vstack(rows))
    five = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
    print("V6: the solution space of L^T E_ij = E_ij R^-1 over the five matrices has dimension %d (L = c, R = 1/c); with E_33 left out: %d; with all nine: %d" % (stab(five), stab(five[:4]), stab([(i, j) for i in range(3) for j in range(3)])))
    # V7
    Bm = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Gm = Bm.conj().T @ Bm + np.eye(3); w, Vv = np.linalg.eigh(Gm); Gh = Vv @ np.diag(np.sqrt(w)) @ Vv.conj().T; Ghi = np.linalg.inv(Gh)
    Uu, _ = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); R = Ghi @ Uu @ Gh; J = Gh @ R @ Ghi
    print("V7: R preserves the Gram: %s; G^(1/2) R G^(-1/2) is unitary: %s" % (np.allclose(R.conj().T @ Gm @ R, Gm), np.allclose(J.conj().T @ J, np.eye(3))))
