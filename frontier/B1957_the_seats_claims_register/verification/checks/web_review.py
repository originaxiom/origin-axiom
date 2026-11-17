"""B1957: the items the web seat names, in its harvest review, as computed only by its referee read or stated in main's
record without a recomputation on main.  Each is recomputed here on main's own code (no data; nothing of the seat's run).
R1  W-A1, lines 32-33: of the 32 candidate pairs, the two that are representations (web_wa1_reps.py does the count).
R2  W-A2, part B: conjugation by each Weil representation moves the Weyl operators X^a Z^b by a linear map of F_5^2; the
    identification with W-A1's map is diag(1, 4) for the conjugate, diag(1, 2) for the other class, and a swap for the
    labelling Z^a X^b: both halves (T and S), and uniqueness up to a scalar.
R3  W-A2, part C: the five flux-5 zero modes of the fibre: T^2 acts as diag(zeta^(j^2)) and S by the kernel psi(-jk)/sqrt 5.
R4  W-A3, lines 76-77: one relabelling by a power of zeta^(ab) removes both phases of frame C's down coupling's law
    (B1953: zeta^(-a^2) under T, zeta^(2ab) under S), so the down lines move as a permutation of the 24 points."""
import sys, pathlib, itertools, functools
import numpy as np
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])


def weil(c):
    T = np.diag([psi(c * x * x) for x in range(5)])
    for k in (1, 2, 3, 4):
        Fk = np.array([[psi(k * x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
        for s in (1, -1, 1j, -1j):
            S = s * Fk
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12 and np.abs(np.linalg.matrix_power(S, 4) - np.eye(5)).max() < 1e-12: return T, S


def moves(U, op):
    """the 2 x 2 matrix over F_5 by which conjugation with U moves the labels of op(a, b), and whether it is linear on all 25"""
    def im(a, b):
        M = U @ op(a, b) @ U.conj().T; v = max(itertools.product(range(5), repeat=2), key=lambda v: abs(np.trace(op(*v).conj().T @ M)))
        return v, abs(abs(np.trace(op(*v).conj().T @ M)) / 5 - 1)
    (c1, e1), (c2, e2) = im(1, 0), im(0, 1); Mx = np.array([[c1[0], c2[0]], [c1[1], c2[1]]])
    lin = all(tuple((Mx @ np.array([a, b])) % 5) == im(a, b)[0] for a in range(5) for b in range(5)); return Mx, lin, max(e1, e2)


if __name__ == "__main__":
    # R2
    XZ = lambda a, b: np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5); ZX = lambda a, b: np.linalg.matrix_power(Z, a % 5) @ np.linalg.matrix_power(X, b % 5)
    ref = {g: moves(U, XZ)[0] for g, U in zip("TS", weil(2))}
    print("R2: W-A1's representation (class 2): conjugation moves X^a Z^b by M_T = %s, M_S = %s (the seat: [[1, 0], [4, 1]] and [[0, 4], [1, 0]])" % (ref["T"].tolist(), ref["S"].tolist()))
    inv5 = lambda d: pow(int(d) % 5, -1, 5)
    def identifications(MT, MS):
        out = []
        for e in itertools.product(range(5), repeat=4):
            D = np.array(e).reshape(2, 2); det = (D[0, 0] * D[1, 1] - D[0, 1] * D[1, 0]) % 5
            if det and all(((D @ ref[g]) % 5 == (M @ D) % 5).all() for g, M in (("T", MT), ("S", MS))): out.append((D, det))
        return out
    for lab, c, op in (("the conjugate (class 3), labelling X^a Z^b", 3, XZ), ("the other class (class 1), labelling X^a Z^b", 1, XZ), ("the other class's conjugate (class 4)", 4, XZ), ("W-A1's representation, labelling Z^a X^b", 2, ZX)):
        T, S = weil(c); (MT, lt, _), (MS, ls, _) = moves(T, op), moves(S, op); ids = identifications(MT, MS)
        scal = {tuple(((D * inv5(D.ravel()[np.flatnonzero(D.ravel())[0]])) % 5).ravel()) for D, _ in ids}
        print("    %s: M_T = %s, M_S = %s, linear on all 25: %s; identifications D with D M = M' D for both T and S: %d, one up to a scalar: %s, namely %s; its determinant is a square mod 5: %s" % (
            lab, MT.tolist(), MS.tolist(), lt and ls, len(ids), len(scal) == 1, np.array(sorted(scal)[0]).reshape(2, 2).tolist() if scal else None, sorted({int(d) in (1, 4) for _, d in ids})))
    # R3
    def modes(u, tau, nw=30):
        n = np.arange(-nw, nw + 1); return np.array([np.exp(5j * np.pi * tau * (n + j / 5) ** 2 + 10j * np.pi * u * (n + j / 5)).sum() for j in range(5)])
    tau = 0.21 + 1.13j; us = [0.137 + 0.071j, -0.31 + 0.22j, 0.05 - 0.4j, 0.44 + 0.3j, -0.2 - 0.15j, 0.3 + 0.05j, 0.11 + 0.37j]
    t2 = max(np.abs(modes(u, tau + 2) - np.array([psi(j * j) for j in range(5)]) * modes(u, tau)).max() / np.abs(modes(u, tau)).max() for u in us)
    A = np.array([modes(u, tau) for u in us]); B = np.array([np.exp(-5j * np.pi * u * u / tau) * modes(u / tau, -1 / tau) for u in us])
    K = np.linalg.lstsq(A, B, rcond=None)[0].T; res = np.abs(A @ K.T - B).max() / np.abs(B).max()
    ker = np.array([[psi(-j * k) for k in range(5)] for j in range(5)]) / np.sqrt(5); c = K[0, 0] / ker[0, 0]
    print("R3: the five flux-5 modes: under tau + 2 they pick up zeta^(j^2): %.1e; under -1/tau (with the factor exp(-5 pi i u^2/tau)) they mix by a matrix (fit residual %.1e) equal to a constant times psi(-jk)/sqrt 5: %.1e, the constant sqrt(-i tau): %.1e" % (t2, res, np.abs(K - c * ker).max() / abs(c), abs(c - np.sqrt(-1j * tau))))
    print("    under tau + 1 alone they do not return to their span: the odd flux needs the square (zeta^(j^2) = psi(k j^2) with 2k = 1, k = 3: a non-residue, W-A1's class)")
    # R4
    sys.path.insert(0, str(next((ROOT / "frontier").glob("B1953_*")) / "verification")); import weyl_operator as W
    for tx, ty in (("0.13", 1.7),):
        Ys, _ = W.images(tx, ty, "down")
        for rd in ("S", "St"):
            for gen in "TS":
                lw = W.law(Ys["t"][rd], Ys[gen][rd], gen); phi = lw["phi"]; tr = next(t for t in W.TRANS[gen] if True)
                best = None
                for trf in W.TRANS[gen]:
                    for eps in (1, -1):
                        ph = {w: phi[w] * psi(eps * (w[0] * w[1] - trf(*w)[0] * trf(*w)[1])) for w in W.PTS}; r0 = ph[(0, 1)]
                        dev = max(abs(np.angle(ph[w] / r0)) for w in W.PTS) / (2 * np.pi)
                        if best is None or dev < best[0]: best = (dev, eps)
                raw = max(abs(np.angle(phi[w] / phi[(0, 1)])) for w in W.PTS) / (2 * np.pi)
                print("R4: down, reading %-2s, %s: the law's residual %.1e; its phases vary over the 24 points by %.3f of a turn; after the relabelling Y(a, b) -> zeta^(%+d ab) Y(a, b) they vary by %.1e" % (rd, gen, lw["residual"], raw, best[1], best[0]))
