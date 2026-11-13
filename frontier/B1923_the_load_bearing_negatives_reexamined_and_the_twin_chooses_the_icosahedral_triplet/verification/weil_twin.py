"""The clue from W29/W31's wall, tested: does the line's twin (multiplication by 2 mod 5, B1914) choose between the two
Galois-conjugate icosahedral triplets of SL(2, F_5)?

The Weil representation of SL(2, F_5) on functions on F_5 (dimension 5) is built from an additive character
psi_a(x) = exp(2 pi i a x / 5): generators T = [[1,1],[0,1]] acts by f(x) -> psi_a(x^2 / 2) f(x), S = [[0,-1],[1,0]]
by the normalised Fourier transform with psi_a (up to the usual phase, fixed so that the relations hold projectively;
the characters are read up to the scalar). Written before the run: for a = 1 the five-dimensional representation splits
as an even part of dimension 3 and an odd part of dimension 2; for a = 2 (a non-square mod 5, the twin's scaling) the
parts are the Galois conjugates: the 3-part's character on an element of order 5 changes from (1 +- sqrt5)/2 to
(1 -+ sqrt5)/2. Main's code; a group computation, no data."""
import itertools, numpy as np
p = 5


def weil(a):
    w = np.exp(2j * np.pi * a / p)
    inv2 = pow(2, -1, p)
    T = np.diag([w ** ((a * 0 + 1) * 0) * np.exp(2j * np.pi * a * (x * x * inv2 % p) / p) for x in range(p)])
    F = np.array([[np.exp(2j * np.pi * a * (x * y % p) / p) for y in range(p)] for x in range(p)]) / np.sqrt(p)
    return T, F


def closure(gens, n_max=200000):
    """the group generated (as matrices up to scalars of modulus one), with a canonical key per projective class"""
    def key(M):
        i = np.argmax(np.abs(M.ravel()) > 1e-9); ph = M.ravel()[i] / abs(M.ravel()[i])
        return tuple(np.round((M / ph).ravel(), 6))
    G = {key(np.eye(p)): np.eye(p)}; frontier = [np.eye(p)]
    while frontier and len(G) < n_max:
        nxt = []
        for M in frontier:
            for g in gens:
                N = g @ M; k = key(N)
                if k not in G:
                    G[k] = N; nxt.append(N)
        frontier = nxt
    return list(G.values())


def parity_parts(M):
    """restrict to even (f(-x) = f(x)) and odd functions"""
    E = np.zeros((p, 3)); O = np.zeros((p, 2))
    E[0, 0] = 1; E[1, 1] = E[4, 1] = 1 / np.sqrt(2); E[2, 2] = E[3, 2] = 1 / np.sqrt(2)
    O[1, 0] = 1 / np.sqrt(2); O[4, 0] = -1 / np.sqrt(2); O[2, 1] = 1 / np.sqrt(2); O[3, 1] = -1 / np.sqrt(2)
    return E.T @ M @ E, O.T @ M @ O


if __name__ == "__main__":
    s5 = 5 ** 0.5
    for a in (1, 2):
        T, F = weil(a)
        G = closure([T, F])
        # elements of order 5 in the projective image: T itself is one; read the 3-part's trace up to the scalar's phase
        E3, O2 = parity_parts(T)
        tr3 = np.trace(E3)
        # remove the scalar ambiguity: compare |tr| and the real part after normalising T so that its eigenvalues are 5th roots
        ev = np.linalg.eigvals(E3)
        print("a = %d: projective image of order %d; the even part's eigenvalues under T (as 5th roots of unity, exponents):" % (a, len(G)),
              sorted(int(round((np.angle(e) / (2 * np.pi) * 5) % 5)) % 5 for e in ev),
              "| its trace %.6f%+.6fi; (1+sqrt5)/2 = %.6f, (1-sqrt5)/2 = %.6f" % (tr3.real, tr3.imag, (1 + s5) / 2, (1 - s5) / 2))
