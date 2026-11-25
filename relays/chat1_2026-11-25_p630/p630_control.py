#!/usr/bin/env python3
"""P-630's positive control: the deviation spectrum of the golden chain at its critical point recovers the
tricritical Ising thermal dimensions h = 1/10 and h = 3/5. Sealed and dependency-free: standard library, numpy
and scipy; reads no file. Data-free.

    python3 -I p630_control.py

The critical object. N Fibonacci anyons on a ring (N even), fusion-path labels l_i in {0 = identity, 1 = tau}, no
two cyclically adjacent 0s; H_c = -sum_i P_i, with P_i the projector of anyons (i, i+1) onto the identity channel
(B220, B222: on l_i given (l_{i-1}, l_{i+1}) it is 1 for (0, 0), 0 for mixed neighbours, and the block
[[phi^-2, phi^-3/2], [phi^-3/2, phi^-1]] for (1, 1)). Its continuum limit is tricritical Ising, c = 7/10 (B220).
The chain is built here from that rule, independently of main's code. Momentum sectors k = 0 and k = pi.

The method (the one P-630 asks for, run where the answer is known). Deviate H_c -> H_c + g V along a
translation-invariant direction V and linearise at g = 0:
  A. the deviation's components. The component of V on the finite-size state of a scaling field phi is
     <phi| V |0> = N c_phi (2 pi / N)^{x_phi}, so it grows as N^{y - 1} with y = 2 - x_phi the field's eigenvalue
     in the flow away from criticality. Read off: h = x / 2 = (1 - s) / 2 from the slope s of ln|<phi|V|0>| in ln N.
  B. the size map (phenomenological renormalisation). The map g -> g' with N' Gap_N'(g') = N Gap_N(g),
     linearised at g = 0, has the eigenvalue (N'/N)^y, where d Gap / dg = <a|V|a> - <0|V|0> grows as N^{y - 1}
     with y set by the most relevant field phi whose coupling <a|phi|a> is non-zero. For the gap of sigma
     (the lowest k = pi level, h = 3/80) that field is epsilon (sigma x epsilon contains sigma); for the gap of
     epsilon it is epsilon' (epsilon x epsilon = 1 + epsilon').
Two directions:
  V_mu = sum_i (1 - l_i), the density of identity labels. It does not commute with the topological symmetry Y
         (Feiguin et al. 2007), so it can reach epsilon and epsilon', which sit in Y's tau-flux sector.
  V_Y  = sum_i (P_i P_{i+1} + P_{i+1} P_i). It commutes with Y, so its components on epsilon and epsilon' vanish:
         the selection-rule control.
Level labels at k = 0: level 0 the identity, level 1 epsilon (x = 1/5), level 2 epsilon' (x = 6/5). At k = pi:
level 0 sigma (x = 3/40). Checked by the gap ratios.

Fits (fixed here, before the run). Sizes N = 12, 14, ..., 30. For A and for sigma's gap in B: least squares of
ln|F(N)| = b + s ln N + c / N + d / N^2. For epsilon's gap in B, whose leading term N^(-1/5) carries a velocity
correction N^(-1): least squares of F(N) = a N^s + c / N, with s scanned on a grid of step 1e-4.

Cells and expectations, written before the run (probabilities are this seat's):
  G1 gate: at N = 10 and 12 the union of all momentum sectors' spectra equals the full spectrum to 1e-10, and
     every sector matrix is Hermitian to 1e-12 (99 %).
  G2 labels: at N = 30, (E_2 - E_0) / (E_1 - E_0) is within 0.3 of 6, and (E_pi,0 - E_0) / (E_1 - E_0) is
     within 0.03 of 3/8 (90 %).
  A1 epsilon: from <1| V_mu |0>, |h - 1/10| <= 0.01 (85 %).
  A2 epsilon': from <2| V_mu |0>, |h - 3/5| <= 0.03 (75 %).
  A3 selection rule: for N = 12 to 22 (dense diagonalisation), |<1| V_Y |0>| and |<2| V_Y |0>| are below 1e-10,
     while V_Y has a component above 1e-6 on at least one of the k = 0 levels 3 to 7 (95 %).
  B1 sigma's gap: from d(E_pi,0 - E_0)/d mu, |h - 1/10| <= 0.03 (75 %).
  B2 epsilon's gap: from d(E_1 - E_0)/d mu, |h - 3/5| <= 0.06 (55 %).
The control passes if G1, G2, A1, A2 and A3 hold. B1 and B2 are the literal map linearisation and are reported
whatever they give.
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

PHI = (1 + 5 ** 0.5) / 2
D0, D1, OFF = PHI ** -2, PHI ** -1, PHI ** -1.5
DENSE = 2000


def states(N):
    """All cyclic N-bit labellings with no two adjacent 0s, as integers (bit i = l_i), sorted."""
    X = np.array([0, 1], dtype=np.int64)
    for i in range(1, N):
        prev = (X >> (i - 1)) & 1
        X = np.concatenate([X[prev == 1], X | (1 << i)])
    X = X[((X & 1) | ((X >> (N - 1)) & 1)) == 1]
    return np.sort(X)


def rot(X, m, N):
    """T^m: the label at site i moves to site i + m."""
    m %= N
    if m == 0:
        return X.copy()
    return ((X << m) | (X >> (N - m))) & ((1 << N) - 1)


def orbits(X, N):
    """For every state: its representative (least rotation), the shift d with state = T^d rep, and its period."""
    rep = X.copy()
    for m in range(1, N):
        rep = np.minimum(rep, rot(X, m, N))
    shift = np.full(len(X), -1)
    for m in range(N):
        hit = (rot(rep, m, N) == X) & (shift < 0)
        shift[hit] = m
    per = np.full(len(X), N)
    for m in range(N - 1, 0, -1):
        per = np.where(rot(X, m, N) == X, m, per)
    return rep, shift, per


def apply_P(X, A, i, N):
    """P_i on states X (bits above N are carried untouched) with amplitudes A."""
    bm, bi, bp = (X >> ((i - 1) % N)) & 1, (X >> i) & 1, (X >> ((i + 1) % N)) & 1
    m00, m11 = (bm == 0) & (bp == 0), (bm == 1) & (bp == 1)
    Xs, As, bs = X[m11], A[m11], bi[m11]
    return (np.concatenate([X[m00], Xs, Xs ^ (1 << i)]),
            np.concatenate([A[m00], As * np.where(bs == 0, D0, D1), As * OFF]))


def op_H(X, A, i, N):
    return apply_P(X, -A, i, N)


def op_VY(X, A, i, N):
    j = (i + 1) % N
    X1, A1 = apply_P(*apply_P(X, A, j, N), i, N)
    X2, A2 = apply_P(*apply_P(X, A, i, N), j, N)
    return np.concatenate([X1, X2]), np.concatenate([A1, A2])


class Chain:
    def __init__(self, N):
        self.N = N
        self.X = states(N)
        assert len(self.X) == round(PHI ** N + (-PHI) ** (-N))          # the Lucas number L_N
        self.rep, self.shift, self.per = orbits(self.X, N)
        isrep = self.rep == self.X
        self.R, self.P = self.X[isrep], self.per[isrep]

    def sector(self, j):
        ok = (j * self.P) % self.N == 0
        return self.R[ok], self.P[ok]

    def matrix(self, j, op):
        """The k = 2 pi j / N block of sum_i op_i (or of V_mu when op is None): column = source representative,
        entry amp * exp(i k d) * sqrt(P_src / P_tgt) for an image T^d r'."""
        N = self.N
        R, P = self.sector(j)
        D = len(R)
        if op is None:
            M = sp.diags(np.array([N - bin(int(r)).count("1") for r in R], float)).tocsr()
        else:
            k = 2 * np.pi * j / N
            secpos = -np.ones(len(self.X), dtype=np.int64)
            secpos[np.searchsorted(self.X, R)] = np.arange(D)
            tagged = R | (np.arange(D, dtype=np.int64) << N)
            rows, cols, vals = [], [], []
            for i in range(N):
                Xt, At = op(tagged, np.ones(D), i, N)
                src, st = Xt >> N, Xt & ((1 << N) - 1)
                idx = np.searchsorted(self.X, st)
                assert np.all(self.X[idx] == st)                         # images stay in the constrained space
                tgt = secpos[np.searchsorted(self.X, self.rep[idx])]
                keep = tgt >= 0
                ph = np.exp(1j * k * self.shift[idx][keep])
                rows.append(tgt[keep])
                cols.append(src[keep])
                vals.append(At[keep] * ph * np.sqrt(P[src[keep]] / self.per[idx][keep]))
            M = sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                              shape=(D, D)).tocsr()
            if (2 * j) % N == 0:
                assert abs(M.imag).max() < 1e-12 if M.nnz else True
                M = M.real.tocsr()
        return M


def full_H(N):
    X = states(N)
    D = len(X)
    H = np.zeros((D, D))
    for i in range(N):
        tagged = X | (np.arange(D, dtype=np.int64) << N)
        Xt, At = op_H(tagged, np.ones(D), i, N)
        np.add.at(H, (np.searchsorted(X, Xt & ((1 << N) - 1)), Xt >> N), At)
    return H


def low(M, n):
    """The n lowest eigenpairs of a real symmetric block, dense below DENSE, else Lanczos to machine precision."""
    if M.shape[0] <= DENSE:
        w, v = np.linalg.eigh(M.toarray() if sp.issparse(M) else M)
        return w[:n], v[:, :n]
    w, v = eigsh(M, k=n, which="SA", tol=0)
    o = np.argsort(w)
    return w[o], v[:, o]


def fit_log(Ns, F):
    """ln|F| = b + s ln N + c/N + d/N^2; returns s."""
    Ns = np.asarray(Ns, float)
    A = np.stack([np.ones_like(Ns), np.log(Ns), 1 / Ns, 1 / Ns ** 2], 1)
    return np.linalg.lstsq(A, np.log(np.abs(F)), rcond=None)[0][1]


def fit_pow_plus_inv(Ns, F):
    """F = a N^s + c/N, s on a grid of step 1e-4 in [-1.5, 1.5]; returns s."""
    Ns, F = np.asarray(Ns, float), np.asarray(F, float)
    best = (np.inf, None)
    for s in np.arange(-1.5, 1.5, 1e-4):
        A = np.stack([Ns ** s, 1 / Ns], 1)
        r = F - A @ np.linalg.lstsq(A, F, rcond=None)[0]
        if r @ r < best[0]:
            best = (r @ r, s)
    return best[1]


def main():
    out = {}
    # G1: the gate
    g1 = True
    for N in (10, 12):
        ch = Chain(N)
        full = np.sort(np.linalg.eigvalsh(full_H(N)))
        pieces, herm = [], 0.0
        for j in range(N):
            M = ch.matrix(j, op_H)
            if M.shape[0] == 0:
                continue
            Md = M.toarray()
            herm = max(herm, np.abs(Md - Md.conj().T).max())
            pieces.append(np.linalg.eigvalsh(Md))
        union = np.sort(np.concatenate(pieces))
        diff = np.abs(union - full).max() if len(union) == len(full) else np.inf
        g1 &= diff < 1e-10 and herm < 1e-12
        print("G1 N=%d: dim %d, sectors' union vs full spectrum %.1e, worst non-Hermiticity %.1e"
              % (N, len(full), diff, herm))
    out["G1"] = g1

    sizes = list(range(12, 31, 2))
    rec = {k: [] for k in ("A_eps", "A_epsp", "D_sig", "D_eps", "r6", "rsig")}
    a3 = True
    for N in sizes:
        ch = Chain(N)
        H0, Hpi = ch.matrix(0, op_H), ch.matrix(N // 2, op_H)
        V0, Vpi = ch.matrix(0, None), ch.matrix(N // 2, None)
        E0, U0 = low(H0, 8)
        Ep, Up = low(Hpi, 2)
        g = U0[:, 0]
        Vg = V0 @ g
        a_eps, a_epsp = U0[:, 1] @ Vg, U0[:, 2] @ Vg
        d_eps = U0[:, 1] @ (V0 @ U0[:, 1]) - g @ Vg
        d_sig = Up[:, 0] @ (Vpi @ Up[:, 0]) - g @ Vg
        r6 = (E0[2] - E0[0]) / (E0[1] - E0[0])
        rsig = (Ep[0] - E0[0]) / (E0[1] - E0[0])
        for k_, v_ in zip(rec, (a_eps, a_epsp, d_sig, d_eps, r6, rsig)):
            rec[k_].append(v_)
        line = ("N=%2d dim0 %6d dimpi %6d | E1-E0 %.6f  r6 %.4f  rsig %.4f | <1|Vmu|0> %.6e <2|Vmu|0> %.6e"
                " | dGap_sig %.6e dGap_eps %.6e" % (N, H0.shape[0], Hpi.shape[0], E0[1] - E0[0], r6, rsig,
                                                    a_eps, a_epsp, d_sig, d_eps))
        if N <= 22:
            VY = ch.matrix(0, op_VY)
            assert np.abs((VY - VY.T)).max() < 1e-12
            VYg = VY @ g
            comps = [abs(U0[:, n] @ VYg) for n in range(1, 8)]
            ok = comps[0] < 1e-10 and comps[1] < 1e-10 and max(comps[2:]) > 1e-6
            a3 &= ok
            line += " | V_Y on levels 1..7: " + " ".join("%.1e" % c for c in comps)
        print(line)
    out["A3"] = a3
    out["G2"] = abs(rec["r6"][-1] - 6) <= 0.3 and abs(rec["rsig"][-1] - 3 / 8) <= 0.03

    h = {}
    h["A1"] = (1 - fit_log(sizes, rec["A_eps"])) / 2
    h["A2"] = (1 - fit_log(sizes, rec["A_epsp"])) / 2
    h["B1"] = (1 - fit_log(sizes, rec["D_sig"])) / 2
    h["B2"] = (1 - fit_pow_plus_inv(sizes, rec["D_eps"])) / 2
    target = {"A1": (0.1, 0.01), "A2": (0.6, 0.03), "B1": (0.1, 0.03), "B2": (0.6, 0.06)}
    print()
    for c in ("A1", "A2", "B1", "B2"):
        t, tol = target[c]
        out[c] = abs(h[c] - t) <= tol
        key = {"A1": "A_eps", "A2": "A_epsp", "B1": "D_sig", "B2": "D_eps"}[c]
        F = rec[key]
        loc = (1 - (np.log(abs(F[-1])) - np.log(abs(F[-2]))) / (np.log(sizes[-1]) - np.log(sizes[-2]))) / 2
        print("%s: h = %.5f (target %s, tolerance %.2f) -> %s; local h from N = %d, %d: %.5f"
              % (c, h[c], {0.1: "1/10", 0.6: "3/5"}[t], tol, "holds" if out[c] else "FAILS",
                 sizes[-2], sizes[-1], loc))
    print("G1 %s, G2 %s (r6 %.4f, rsig %.4f at N = %d), A3 %s"
          % (out["G1"], out["G2"], rec["r6"][-1], rec["rsig"][-1], sizes[-1], out["A3"]))
    passed = all(out[c] for c in ("G1", "G2", "A1", "A2", "A3"))
    print("the control passes (G1, G2, A1, A2, A3): %s; B1 %s, B2 %s" % (passed, out["B1"], out["B2"]))


if __name__ == "__main__":
    main()
