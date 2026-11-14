"""B1934 (main, 2026-11-14): three exact checks in the programme's terms.
(1) Both Weil representations of SL(2, F5) on C^5 (T = diag(e(k x^2 / 5)), k a residue or not; S the normalised Fourier
    transform, its eighth-root phase fixed by requiring <S, T> to have order 120) split invariantly as an even 3 plus an
    odd 2; both blocks have determinant 1; the 3 has real character and golden traces on the elements of order 5 (an
    icosahedral triplet, one of the two Galois conjugates by k), the 2 has -I acting as -1 (the spinor doublet).
(2) The hand (-1)^(n+e) of +-J^n K^e at the mark (1, 2) mod 5 equals the Legendre symbol mod 5 of its eigenvalue there,
    the quadratic character of Q(sqrt 5), in all 32 cases.
(3) With the frame's charges (6Y: Q 1, u -4, d 2, L -3, e 6), the lepton pair (L, e) is the down pair (Q, d) transposed
    modulo N exactly when N divides 5.
    python3 -B level_five_structure.py      # prints its checks; writes nothing"""
import cmath, itertools, math
import numpy as np
P = 5; W = cmath.exp(2j * math.pi / P)
LEG = {1: 1, 4: 1, 2: -1, 3: -1}
E = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0]], dtype=complex) / np.array([1, math.sqrt(2), math.sqrt(2)])
O = np.array([[0, 0], [1, 0], [0, 1], [0, -1], [-1, 0]], dtype=complex) / math.sqrt(2)


def generate(gens, cap=400):
    key = lambda M: tuple(np.round(np.concatenate([M.real.flatten(), M.imag.flatten()]), 6))
    I = np.eye(5, dtype=complex); seen = {key(I): I}; frontier = [I]
    while frontier and len(seen) <= cap:
        nxt = []
        for A in frontier:
            for G in gens:
                B = G @ A; k = key(B)
                if k not in seen:
                    seen[k] = B; nxt.append(B)
        frontier = nxt
    return list(seen.values())


def weil(k):
    T = np.diag([W ** (k * x * x) for x in range(P)])
    for m, j in itertools.product(range(1, 5), range(8)):
        S = np.array([[W ** (m * x * y) for y in range(P)] for x in range(P)]) / math.sqrt(P) * cmath.exp(2j * math.pi * j / 8)
        G = generate([S, T])
        if len(G) == 120:
            return S, T, G
    return None


def order(g):
    n, A = 1, g.copy()
    while not np.allclose(A, np.eye(5)):
        A = A @ g; n += 1
    return n


def check_weil(k):
    S, T, G = weil(k)
    blocks_invariant = all(np.allclose(E.conj().T @ g @ O, 0) for g in G)
    dets = {round(float(np.linalg.det(E.conj().T @ g @ E).real), 9) for g in G} | {round(float(np.linalg.det(O.conj().T @ g @ O).real), 9) for g in G}
    real3 = all(abs(np.trace(E.conj().T @ g @ E).imag) < 1e-9 for g in G)
    tr5 = sorted({round(float(np.trace(E.conj().T @ g @ E).real), 9) for g in G if order(g) == 5})
    mI = S @ S
    sgn_odd = round(float(np.trace(O.conj().T @ mI @ O).real) / 2)
    texp = sorted({round((cmath.phase(W ** (k * x * x)) / (2 * math.pi)) * P) % P for x in (0, 1, 2)})
    return {"order": len(G), "blocks_invariant": blocks_invariant, "dets": dets, "real_triplet": real3, "traces_order5": tr5,
            "minus_I_on_odd": sgn_odd, "T_exponents_on_triplet": texp}


def hand_is_legendre(mark=(1, 2)):
    J = np.array([[1, 1], [1, 0]]); K = np.array([[0, 1], [-1, 0]]); v = np.array(mark)
    for sgn, n, e in itertools.product((1, -1), range(8), (0, 1)):
        M = sgn * np.linalg.matrix_power(J, n) @ np.linalg.matrix_power(K, e) % P
        lam = next((l for l in range(1, P) if np.array_equal(M @ v % P, l * v % P)), None)
        if lam is None or LEG[lam] != (-1) ** (n + e):
            return False
    return True


Y6 = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}


def transposed_orders(Nmax=60, y=Y6):
    return [N for N in range(2, Nmax + 1) if (y["Q"] - y["e"]) % N == 0 and (y["d"] - y["L"]) % N == 0]


if __name__ == "__main__":
    for k in (1, 2):
        print("Weil representation, k = %d:" % k, check_weil(k))
    print("the hand is the Legendre symbol of the eigenvalue at the mark (32 cases):", hand_is_legendre())
    print("line orders N <= 60 at which the lepton pair is the down pair transposed:", transposed_orders())
