"""B1957: the web seat's W-A1, lines 32-33: of the 32 candidate pairs rho(T) = diag(psi(k x^2)), rho(S) = c F_s
(k in F_5*, s = +-1, c in {1, -1, i, -i}; F_s the Fourier kernel psi(s x y)/sqrt 5), how many extend to a representation
of SL(2, F_5).  Main's own test: the assignment is carried along the group's Cayley graph on S = [[0, -1], [1, 0]] and
T = [[1, 1], [0, 1]] and must agree at every one of the 120 elements however reached; a second test by the relations
S^4 = 1, S^2 central, (S T)^3 = S^2, T^5 = 1 alone (which hold in SL(2, F_5) but do not present it)."""
import numpy as np
p = 5; X = np.arange(p); w = np.exp(2j * np.pi / p)
mul = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))
S, T, I = ((0, p - 1), (1, 0)), ((1, 1), (0, 1)), ((1, 0), (0, 1))


def extends(rS, rT):
    rho = {I: np.eye(p, dtype=complex)}; todo = [I]
    while todo:
        g = todo.pop()
        for h, M in ((mul(g, S), rho[g] @ rS), (mul(g, T), rho[g] @ rT)):
            if h in rho:
                if np.abs(rho[h] - M).max() > 1e-9: return None
            else: rho[h] = M; todo.append(h)
    return rho if len(rho) == 120 else None


if __name__ == "__main__":
    keep = []; rel = []
    for k in range(1, p):
        rT = np.diag(w ** ((k * X * X) % p))
        for s in (1, -1):
            F = w ** ((s * np.outer(X, X)) % p) / np.sqrt(p)
            for c in (1, -1, 1j, -1j):
                rS = c * F; rho = extends(rS, rT)
                if rho is not None: keep.append((k, s, c, len({np.round(M, 8).tobytes() for M in rho.values()})))
                S2 = rS @ rS; ok = all(np.abs(a - b).max() < 1e-9 for a, b in ((np.linalg.matrix_power(rS, 4), np.eye(p)), (S2 @ rT, rT @ S2), (np.linalg.matrix_power(rS @ rT, 3), S2), (np.linalg.matrix_power(rT, 5), np.eye(p))))
                if ok: rel.append((k, s, c))
    print("candidates: 32; extending to all 120 elements: %d: %s (the last entry: distinct matrices)" % (len(keep), [(k, s, complex(c), n) for k, s, c, n in keep]))
    print("passing the four relations alone: %d: %s" % (len(rel), [(k, s, complex(c)) for k, s, c in rel]))
    a = extends(keep[0][2] * w ** ((keep[0][1] * np.outer(X, X)) % p) / np.sqrt(p), np.diag(w ** ((keep[0][0] * X * X) % p))); b = extends(keep[1][2] * w ** ((keep[1][1] * np.outer(X, X)) % p) / np.sqrt(p), np.diag(w ** ((keep[1][0] * X * X) % p)))
    print("the two are complex conjugates of each other: %.1e; their characters agree on all 120 elements: %.1e (so they are one representation)" % (max(np.abs(a[g].conj() - b[g]).max() for g in a), max(abs(np.trace(a[g]) - np.trace(b[g])) for g in a)))
