#!/usr/bin/env python3
"""B1523 -- route F (the fibration), a post-run check written after the seal: the bundle rebuilt from its word, no SnapPy holonomy.

For a word state (sign, w) the group is Gamma = F_2 x| <t>, F_2 = <a, b>, t x t^-1 = phi(x), with phi = phi_{w_1} o ... o phi_{w_n}
(phi_L: a -> ab, b -> b; phi_R: a -> a, b -> ba; both fix the fibre boundary [a, b] = a b a^-1 b^-1 exactly), composed with
iota: a -> a^-1, b -> b^-1 for the sign -. Its induced matrix on H_1(F) is the word's product of L = [[1,0],[1,1]], R = [[1,1],[0,1]].
  - The fibre representation is a fixed point of phi's trace map on (x, y, z) = (tr a, tr b, tr ab) with tr[a, b] = -2. The map is
    iterated letter by letter (Fricke: L sends (x, y, z) to (z, y, yz - x), R to (x, z, xz - y), iota is the identity on traces),
    and solved by Newton at 60 digits from random starts; the solution whose cusp shape matches SnapPy's (up to the conventions:
    mod 1, sign, conjugation) is the hyperbolic structure. SnapPy enters only there.
  - rho(phi(a)), rho(phi(b)) and the action c -> c o phi on cocycles are accumulated the same way, one letter at a time
    (iota: c(a) -> -Ad(a)^-1 c(a); L: c(a) -> c(a) + Ad(a) c(b); R: c(b) -> c(b) + Ad(b) c(a)), so no long word is formed.
  - rho(t) solves T rho(x) T^-1 = rho(phi(x)) (a 1-dimensional linear problem, Schur), normalised to det 1.
  - H^1(Gamma; V) = H^1(F_2; V)^t (Lyndon-Hochschild-Serre, H^0(F_2; V) = 0 for the irreducible fibre representation): a cocycle on
    F_2 is free, (c(a), c(b)) in V^2; t acts by (t.c)(x) = Ad(rho(t))^-1 c(phi(x)), computed by the Fox calculus of the words phi(x);
    dim H^1(Gamma; V) = dim {c : t.c - c in B^1} - dim H^0(F; V) - dim B^1 + dim H^1(Z; H^0(F; V)).
  - The modules: V = R (trivial), so(3,1) and v, built here from the 4-dimensional representation X -> A X A^* on 2 x 2 Hermitian
    matrices in the basis of the identity and the Pauli matrices (route R uses the same model; nothing else is shared: this file has
    its own module bases, adjoint action, Fox calculus and rank decisions).
  - The fibre boundary's rigidity (Heusener-Porti Def. 7.1): the fixed class restricted to [a, b], against the image of Ad[a, b] - 1.
Usage: python3 route_f.py SIGN WORD [SIGN WORD ...]   e.g. python3 route_f.py + LR - LLRLRR"""
import cmath
import json
import random
import sys

import mpmath as mp

mp.mp.dps = 60
EPS = mp.mpf(10) ** -30

INV = {"a": "A", "b": "B", "A": "a", "B": "b"}


def inv_word(w):
    return "".join(INV[c] for c in reversed(w))


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] == INV[c]:
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def substitute(w, img):
    """the image of the word w under the endomorphism with img['a'], img['b']"""
    s = []
    for c in w:
        s.append(img[c] if c in "ab" else inv_word(img[c.lower()]))
    return free_reduce("".join(s))


def automorphism(sign, word):
    """phi as the images of a and b (words in a, b, A, B)"""
    img = {"a": "a", "b": "b"}
    # phi_w = phi_{w_1} o ... o phi_{w_n}: apply the last letter first
    for letter in reversed(word):
        step = {"a": "ab", "b": "b"} if letter == "L" else {"a": "a", "b": "ba"}
        img = {"a": substitute(img["a"], step), "b": substitute(img["b"], step)}
    if sign == "-":
        img = {"a": substitute(img["a"], {"a": "A", "b": "B"}), "b": substitute(img["b"], {"a": "A", "b": "B"})}
    return img


def rep_from_traces(x, y, z):
    A = mp.matrix([[x, 1], [-1, 0]])
    beta = (-z + mp.sqrt(z * z - 4)) / 2
    B = mp.matrix([[0, beta], [-1 / beta, y]])
    return A, B


def word_matrix(w, A, B):
    Ai, Bi = mp.inverse(A), mp.inverse(B)
    M = {"a": A, "b": B, "A": Ai, "B": Bi}
    X = mp.eye(2)
    for c in w:
        X = X * M[c]
    return X


def tr2(X):
    return X[0, 0] + X[1, 1]


def fixed_point_equations(img):
    def F(x, y, z):
        A, B = rep_from_traces(x, y, z)
        return [tr2(word_matrix(img["a"], A, B)) - x,
                tr2(word_matrix(img["b"], A, B)) - y,
                x * x + y * y + z * z - x * y * z]
    return F


def solve_fibre(img, starts=60, seed=1):
    """trace-map fixed points with tr[a, b] = -2, by Newton from random starts; each returned once (up to 1e-25)"""
    rng = random.Random(seed)
    F = fixed_point_equations(img)
    sols = []
    for _ in range(starts):
        x0 = [mp.mpc(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(3)]
        try:
            s = mp.findroot(F, x0, tol=mp.mpf(10) ** -50, maxsteps=200)
        except (ZeroDivisionError, ValueError):
            continue
        x, y, z = s[0], s[1], s[2]
        if max(abs(v) for v in F(x, y, z)) > mp.mpf(10) ** -40:
            continue
        A, B = rep_from_traces(x, y, z)
        # the third equation, not imposed: tr rho(phi(ab)) = z
        if abs(tr2(word_matrix(free_reduce(img["a"] + img["b"]), A, B)) - z) > mp.mpf(10) ** -35:
            continue
        if abs(mp.im(x)) + abs(mp.im(y)) + abs(mp.im(z)) < mp.mpf(10) ** -20:
            continue      # real characters are not the complete structure
        if not any(abs(x - u[0]) + abs(y - u[1]) + abs(z - u[2]) < mp.mpf(10) ** -25 for u in sols):
            sols.append((x, y, z))
    return sols


def monodromy_matrix(img, A, B):
    """T in SL(2, C) with T rho(x) T^-1 = rho(phi(x)), x = a, b (the null space of a 8 x 4 linear system), det T = 1"""
    Ap, Bp = word_matrix(img["a"], A, B), word_matrix(img["b"], A, B)
    rows = []
    for X, Y in ((A, Ap), (B, Bp)):
        # T X - Y T = 0, unknowns T00, T01, T10, T11
        for i in range(2):
            for j in range(2):
                row = [mp.mpc(0)] * 4
                for k in range(2):
                    row[2 * i + k] += X[k, j]          # (T X)_ij = sum_k T_ik X_kj
                    row[2 * k + j] -= Y[i, k]          # (Y T)_ij = sum_k Y_ik T_kj
                rows.append(row)
    M = mp.matrix(rows)
    U, S, V = mp.svd_c(M)
    t = [mp.conj(V[3, j]) for j in range(4)]
    T = mp.matrix([[t[0], t[1]], [t[2], t[3]]])
    d = mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
    T = T / d
    resid = max(mp.mnorm(T * A * mp.inverse(T) - Ap, 1), mp.mnorm(T * B * mp.inverse(T) - Bp, 1))
    return T, resid, S[2]


def cusp_shape(sign, A, B, T):
    """the fibre boundary mu = [a, b] and the section (t for +, ab t for -) commute; their translations at the common fixed point"""
    mu = word_matrix("abAB", A, B)
    sec = T if sign == "+" else word_matrix("ab", A, B) * T
    # the fixed point of mu: the kernel of mu - s 1 (s = +-1), from the larger row
    s = 1 if mp.re(tr2(mu)) > 0 else -1
    N = mu - s * mp.eye(2)
    if abs(N[0, 0]) + abs(N[0, 1]) >= abs(N[1, 0]) + abs(N[1, 1]):
        u, v = N[0, 1], -N[0, 0]
    else:
        u, v = -N[1, 1], N[1, 0]
    n = abs(u) ** 2 + abs(v) ** 2
    S = mp.matrix([[u, -mp.conj(v) / n], [v, mp.conj(u) / n]])
    Si = mp.inverse(S)
    out = []
    for X in (mu, sec):
        Y = Si * X * S
        if abs(Y[1, 0]) > mp.mpf(10) ** -25:
            return None, "not upper-triangular"
        out.append(Y[0, 1] / Y[0, 0])
    return out[1] / out[0], mp.mnorm(mu * sec - sec * mu, 1)


# ------------------------------------------------------------------ the modules, built here: own bases, own coordinates
PAULI = [mp.matrix([[1, 0], [0, 1]]), mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -1j], [1j, 0]]), mp.matrix([[1, 0], [0, -1]])]
JF = mp.diag([1, -1, -1, -1])


def hermitian_rep(A):
    """X -> A X A^* on Hermitian 2 x 2 matrices, in the basis (1, sigma_x, sigma_y, sigma_z): a real 4 x 4 matrix in SO(3,1)"""
    Ad = A.H
    L = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            M = PAULI[i] * A * PAULI[j] * Ad
            L[i, j] = mp.re(M[0, 0] + M[1, 1]) / 2
    return L


def module_basis(kind, seed=7):
    """a basis of v = {J S : S symmetric, tr J S = 0} or so(3,1) = {J K : K antisymmetric}, orthonormal in the flattened Euclidean
    product, obtained by Gram-Schmidt from a random spanning set (a basis that shares nothing with route R's)"""
    rng = random.Random(seed)
    cands = []
    for _ in range(40):
        M = mp.matrix(4, 4)
        for i in range(4):
            for j in range(4):
                M[i, j] = mp.mpf(rng.uniform(-1, 1))
        if kind == "v":
            S = (M + M.T) / 2
            Y = JF * S
            t = sum(Y[i, i] for i in range(4)) / 4
            # remove the trace inside the constraint: J S with tr(J S) = 0, using J * (t J) = t 1
            Y = Y - t * mp.eye(4)
        else:
            K = (M - M.T) / 2
            Y = JF * K
        cands.append(Y)
    basis = []
    for Y in cands:
        y = mp.matrix([Y[i, j] for i in range(4) for j in range(4)])
        for b in basis:
            y = y - b * mp.fdot(b, y)
        nrm = mp.norm(y)
        if nrm > mp.mpf(10) ** -20:
            basis.append(y / nrm)
    want = {"v": 9, "so": 6}[kind]
    assert len(basis) == want, (kind, len(basis))
    return basis


BASES = {k: module_basis(k) for k in ("v", "so")}


def adjoint(L, kind):
    """Y -> L Y L^-1 in the module's orthonormal basis (coordinates by Euclidean projection, the basis being orthonormal and the
    module invariant)"""
    if kind == "triv":
        return mp.matrix([[1]])
    B = BASES[kind]
    Li = JF * L.T * JF
    n = len(B)
    M = mp.matrix(n, n)
    for j, b in enumerate(B):
        Y = mp.matrix(4, 4)
        for i in range(16):
            Y[i // 4, i % 4] = b[i]
        Z = L * Y * Li
        z = mp.matrix([Z[i, k] for i in range(4) for k in range(4)])
        for i, bi in enumerate(B):
            M[i, j] = mp.fdot(bi, z)
        # invariance check: the image lies in the module
        back = sum((bi * M[i, j] for i, bi in enumerate(B)), mp.matrix(16, 1))
        assert mp.norm(back - z) < mp.mpf(10) ** -40
    return M


def cocycle_on_word(w, ca, cb, Ad):
    """c(w) for the free-group cocycle with c(a) = ca, c(b) = cb; Ad[x] the module action of x in {a, b, A, B}"""
    n = ca.rows
    acc = mp.matrix(n, 1)
    P = mp.eye(n)
    for ch in w:
        if ch == "a":
            acc += P * ca
        elif ch == "b":
            acc += P * cb
        elif ch == "A":
            acc -= P * Ad["A"] * ca
        else:
            acc -= P * Ad["B"] * cb
        P = P * Ad[ch]
    return acc


def rank_with_margin(M):
    s = sorted([abs(x) for x in mp.svd_c(M, compute_uv=False)], reverse=True)
    r = sum(1 for x in s if x > EPS)
    return r, (min([x for x in s if x > EPS], default=None)), max([x for x in s if x <= EPS], default=mp.mpf(0))


def fibre_cohomology(img, A, B, T, kind):
    """dim H^1(Gamma; V) = dim H^1(F; V)^t + dim H^1(Z; H^0(F; V)) (Lyndon-Hochschild-Serre)"""
    LA, LB, LT = hermitian_rep(A), hermitian_rep(B), hermitian_rep(T)
    Ad = {"a": adjoint(LA, kind), "b": adjoint(LB, kind)}
    Ad["A"], Ad["B"] = mp.inverse(Ad["a"]), mp.inverse(Ad["b"])
    AdTi = mp.inverse(adjoint(LT, kind))
    n = Ad["a"].rows
    # Phi on V^2: column k is Phi applied to the k-th basis cocycle
    Phi = mp.matrix(2 * n, 2 * n)
    for k in range(2 * n):
        e = mp.matrix(2 * n, 1)
        e[k] = 1
        ca, cb = mp.matrix([e[i] for i in range(n)]), mp.matrix([e[n + i] for i in range(n)])
        ia = AdTi * cocycle_on_word(img["a"], ca, cb, Ad)
        ib = AdTi * cocycle_on_word(img["b"], ca, cb, Ad)
        for i in range(n):
            Phi[i, k], Phi[n + i, k] = ia[i], ib[i]
    delta = mp.matrix(2 * n, n)
    for i in range(n):
        for j in range(n):
            delta[i, j] = Ad["a"][i, j] - (1 if i == j else 0)
            delta[n + i, j] = Ad["b"][i, j] - (1 if i == j else 0)
    rb, bk, bd = rank_with_margin(delta)
    # (Phi - 1) c - delta u = 0 in (c, u)
    Sys = mp.matrix(2 * n, 3 * n)
    for i in range(2 * n):
        for j in range(2 * n):
            Sys[i, j] = Phi[i, j] - (1 if i == j else 0)
        for j in range(n):
            Sys[i, 2 * n + j] = -delta[i, j]
    r, k_, d_ = rank_with_margin(Sys)
    dim_S = 3 * n - r
    # (c, u) -> c has kernel {(0, u) : delta u = 0} = H^0(F; V), of dimension n - rb; so the fixed part of H^1(F; V) is
    # dim_S - (n - rb) - rb = dim_S - n, and LHS adds H^1(Z; H^0(F; V)): 1 for the trivial module, 0 for so and v (H^0 = 0)
    dim = dim_S - n + (1 if kind == "triv" else 0)
    return {"dim": int(dim), "B1": rb, "margin": [float(k_) if k_ is not None else None, float(d_)],
            "coboundary margin": [float(bk) if bk is not None else None, float(bd)]}, (Phi, delta, Sys, Ad, n)


def fibre_boundary_residual(img, A, B, T):
    """the fixed class's restriction to the fibre boundary [a, b]: zero iff [a, b] is not a rigid slope"""
    info, (Phi, delta, Sys, Ad, n) = fibre_cohomology(img, A, B, T, "v")
    if info["dim"] != 1:
        return None
    # the kernel of the 2n x 3n system is (dim B^1 + 1)-dimensional; an economy SVD would not return it, so pad to square
    Sq = mp.matrix(3 * n, 3 * n)
    for i in range(2 * n):
        for j in range(3 * n):
            Sq[i, j] = Sys[i, j]
    U, S, V = mp.svd_c(Sq)
    assert all(abs(S[i]) < EPS for i in range(2 * n - 1, 3 * n)) and abs(S[2 * n - 2]) > EPS, "kernel dimension is not n + 1"
    # the class: project each kernel vector's c-part off im(delta) and keep the largest
    ker = [mp.matrix([mp.conj(V[i, j]) for j in range(3 * n)]) for i in range(2 * n - 1, 3 * n)]
    Ub, Sb, Vb = mp.svd_c(delta)
    cols = [mp.matrix([Ub[i, k] for i in range(2 * n)]) for k in range(n)]
    best = None
    for kv in ker:
        c = mp.matrix([kv[i] for i in range(2 * n)])
        for col in cols:
            c = c - col * (col.H * c)[0]
        if best is None or mp.norm(c) > mp.norm(best):
            best = c
    ca, cb = mp.matrix([best[i] for i in range(n)]), mp.matrix([best[n + i] for i in range(n)])
    cmu = cocycle_on_word("abAB", ca, cb, Ad)
    Amu = Ad["a"] * Ad["b"] * Ad["A"] * Ad["B"]
    Bm = Amu - mp.eye(n)
    Uu, Su, Vu = mp.svd_c(Bm)
    rank = sum(1 for i in range(n) if abs(Su[i]) > EPS)
    proj = mp.matrix(n, 1)
    for k in range(rank):
        col = mp.matrix([Uu[i, k] for i in range(n)])
        proj += col * (col.H * cmu)[0]
    return float(mp.norm(cmu - proj) / mp.norm(cmu))


def record(sign, word, snappy_shape=None, starts=60):
    img = automorphism(sign, word)
    sols = solve_fibre(img, starts=starts)
    cands = []
    for (x, y, z) in sols:
        A, B = rep_from_traces(x, y, z)
        T, tres, sgap = monodromy_matrix(img, A, B)
        shape, comm = cusp_shape(sign, A, B, T)
        if shape is None:
            continue
        cands.append({"traces": (x, y, z), "A": A, "B": B, "T": T, "T residual": tres, "shape": complex(shape), "commutation": comm})
    out = {"state": sign + word, "automorphism": img, "fixed points found": len(sols), "with a parabolic cusp": len(cands)}
    if snappy_shape is None:
        return out, cands
    # the hyperbolic one: |Im shape| equal to SnapPy's, Re shape +- Re SnapPy's an integer (the section is defined up to mu^k,
    # the orientation and the mirror up to sign and conjugation)
    def matches(sh):
        if abs(abs(sh.imag) - abs(snappy_shape.imag)) > 1e-9:
            return False
        return any(abs((sh.real + e * snappy_shape.real) - round(sh.real + e * snappy_shape.real)) < 1e-9 for e in (1, -1))
    geo = [c for c in cands if matches(c["shape"])]
    out["matching SnapPy's cusp shape"] = len(geo)
    if not geo:
        return out, cands
    g = geo[0]
    for kind in ("triv", "so", "v"):
        info, _ = fibre_cohomology(img, g["A"], g["B"], g["T"], kind)
        out["H1 " + kind] = info
    out["fibre boundary residual"] = fibre_boundary_residual(img, g["A"], g["B"], g["T"])
    out["T residual"] = float(g["T residual"])
    out["shape"] = [g["shape"].real, g["shape"].imag]
    return out, cands


if __name__ == "__main__" and not (len(sys.argv) > 1 and sys.argv[1] == "--fast"):
    import snappy
    args = sys.argv[1:]
    for sign, word in zip(args[0::2], args[1::2]):
        sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
        rec, _ = record(sign, word, sh)
        print(json.dumps({k: v for k, v in rec.items() if k != "automorphism"}, default=str))


# ------------------------------------------------------------------ the recursion (letter by letter; supersedes the word forms above)
def letters(sign, word):
    """the steps of c -> c o phi for phi = iota^[sign -] o phi_{w_1} o ... o phi_{w_n}: iota first, then w_1, ..., w_n"""
    return (["i"] if sign == "-" else []) + list(word)


def trace_map(steps, x, y, z):
    for st in steps:
        if st == "L":
            x, y, z = z, y, y * z - x
        elif st == "R":
            x, y, z = x, z, x * z - y
    return x, y, z


def solve_fibre_fast(steps, starts=400, seed=1, accept=None):
    """Newton on T_phi(x, y, z) = (x, y, z), x^2 + y^2 + z^2 = x y z; returns the distinct non-real solutions (or the first one
    `accept` takes, if given)"""
    rng = random.Random(seed)

    def F(x, y, z):
        X, Y, Z = trace_map(steps, x, y, z)
        return [X - x, Y - y, x * x + y * y + z * z - x * y * z]
    sols = []
    for _ in range(starts):
        # log-scaled magnitudes (0.3 to 300) with random phases: the fibre traces grow with the word
        x0 = [mp.mpc(10 ** rng.uniform(-0.5, 2.5)) * mp.expjpi(rng.uniform(0, 2)) for _ in range(3)]
        try:
            r = mp.findroot(F, x0, tol=mp.mpf(10) ** -50, maxsteps=100)
        except (ZeroDivisionError, ValueError):
            continue
        x, y, z = r[0], r[1], r[2]
        if max(abs(v) for v in F(x, y, z)) > mp.mpf(10) ** -40:
            continue
        if abs(trace_map(steps, x, y, z)[2] - z) > mp.mpf(10) ** -35:
            continue
        if abs(mp.im(x)) + abs(mp.im(y)) + abs(mp.im(z)) < mp.mpf(10) ** -20:
            continue
        if any(abs(x - u[0]) + abs(y - u[1]) + abs(z - u[2]) < mp.mpf(10) ** -25 for u in sols):
            continue
        sols.append((x, y, z))
        if accept is not None and accept(x, y, z):
            return sols, (x, y, z)
    return sols, None


def image_reps(steps, A, B):
    for st in steps:
        if st == "i":
            A, B = mp.inverse(A), mp.inverse(B)
        elif st == "L":
            A, B = A * B, B
        else:
            A, B = A, B * A
    return A, B


def monodromy_fast(steps, A, B):
    Ap, Bp = image_reps(steps, A, B)
    rows = []
    for X, Y in ((A, Ap), (B, Bp)):
        for i in range(2):
            for j in range(2):
                row = [mp.mpc(0)] * 4
                for k in range(2):
                    row[2 * i + k] += X[k, j]
                    row[2 * k + j] -= Y[i, k]
                rows.append(row)
    U, S, V = mp.svd_c(mp.matrix(rows))
    t = [mp.conj(V[3, j]) for j in range(4)]
    T = mp.matrix([[t[0], t[1]], [t[2], t[3]]])
    T = T / mp.sqrt(T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0])
    resid = max(mp.mnorm(T * A * mp.inverse(T) - Ap, 1), mp.mnorm(T * B * mp.inverse(T) - Bp, 1))
    return T, resid


def phi_on_cocycles(steps, A, B, kind):
    """the 2n x 2n matrix of c -> c o phi in the coordinates (c(a), c(b)), with the current representation updated per letter"""
    n = 1 if kind == "triv" else len(BASES[kind])
    P = mp.eye(2 * n)
    for st in steps:
        Ada, Adb = adjoint(hermitian_rep(A), kind), adjoint(hermitian_rep(B), kind)
        Sm = mp.eye(2 * n)
        if st == "i":
            Ia, Ib = mp.inverse(Ada), mp.inverse(Adb)
            for i in range(n):
                for j in range(n):
                    Sm[i, j] = -Ia[i, j]
                    Sm[n + i, n + j] = -Ib[i, j]
            A, B = mp.inverse(A), mp.inverse(B)
        elif st == "L":
            for i in range(n):
                for j in range(n):
                    Sm[i, n + j] = Ada[i, j]
            A, B = A * B, B
        else:
            for i in range(n):
                for j in range(n):
                    Sm[n + i, j] = Adb[i, j]
            A, B = A, B * A
        P = Sm * P
    return P


def cohomology_fast(steps, A, B, T, kind):
    n = 1 if kind == "triv" else len(BASES[kind])
    Ad = {"a": adjoint(hermitian_rep(A), kind), "b": adjoint(hermitian_rep(B), kind)}
    Ad["A"], Ad["B"] = mp.inverse(Ad["a"]), mp.inverse(Ad["b"])
    AdTi = mp.inverse(adjoint(hermitian_rep(T), kind))
    P = phi_on_cocycles(steps, A, B, kind)
    Phi = mp.matrix(2 * n, 2 * n)
    for i in range(n):
        for j in range(2 * n):
            Phi[i, j] = mp.fsum(AdTi[i, k] * P[k, j] for k in range(n))
            Phi[n + i, j] = mp.fsum(AdTi[i, k] * P[n + k, j] for k in range(n))
    delta = mp.matrix(2 * n, n)
    for i in range(n):
        for j in range(n):
            delta[i, j] = Ad["a"][i, j] - (1 if i == j else 0)
            delta[n + i, j] = Ad["b"][i, j] - (1 if i == j else 0)
    rb, bk, bd = rank_with_margin(delta)
    Sys = mp.matrix(2 * n, 3 * n)
    for i in range(2 * n):
        for j in range(2 * n):
            Sys[i, j] = Phi[i, j] - (1 if i == j else 0)
        for j in range(n):
            Sys[i, 2 * n + j] = -delta[i, j]
    r, k_, d_ = rank_with_margin(Sys)
    dim = (3 * n - r) - n + (1 if kind == "triv" else 0)
    return {"dim": int(dim), "B1": rb, "margin": [float(k_) if k_ is not None else None, float(d_)],
            "coboundary margin": [float(bk) if bk is not None else None, float(bd)]}, (Sys, delta, Ad, n)


def fibre_boundary_fast(steps, A, B, T):
    info, (Sys, delta, Ad, n) = cohomology_fast(steps, A, B, T, "v")
    if info["dim"] != 1:
        return None, info
    Sq = mp.matrix(3 * n, 3 * n)
    for i in range(2 * n):
        for j in range(3 * n):
            Sq[i, j] = Sys[i, j]
    U, S, V = mp.svd_c(Sq)
    assert all(abs(S[i]) < EPS for i in range(2 * n - 1, 3 * n)) and abs(S[2 * n - 2]) > EPS, "kernel dimension is not n + 1"
    ker = [mp.matrix([mp.conj(V[i, j]) for j in range(3 * n)]) for i in range(2 * n - 1, 3 * n)]
    Ub, Sb, Vb = mp.svd_c(delta)
    cols = [mp.matrix([Ub[i, k] for i in range(2 * n)]) for k in range(n)]
    best = None
    for kv in ker:
        c = mp.matrix([kv[i] for i in range(2 * n)])
        for col in cols:
            c = c - col * (col.H * c)[0]
        if best is None or mp.norm(c) > mp.norm(best):
            best = c
    ca, cb = mp.matrix([best[i] for i in range(n)]), mp.matrix([best[n + i] for i in range(n)])
    cmu = cocycle_on_word("abAB", ca, cb, Ad)
    Bm = Ad["a"] * Ad["b"] * Ad["A"] * Ad["B"] - mp.eye(n)
    Uu, Su, Vu = mp.svd_c(Bm)
    rank = sum(1 for i in range(n) if abs(Su[i]) > EPS)
    proj = mp.matrix(n, 1)
    for k in range(rank):
        col = mp.matrix([Uu[i, k] for i in range(n)])
        proj += col * (col.H * cmu)[0]
    return float(mp.norm(cmu - proj) / mp.norm(cmu)), info


def record_fast(sign, word, snappy_shape, starts=400):
    steps = letters(sign, word)

    def matches(sh):
        if abs(abs(sh.imag) - abs(snappy_shape.imag)) > 1e-9:
            return False
        return any(abs((sh.real + e * snappy_shape.real) - round(sh.real + e * snappy_shape.real)) < 1e-9 for e in (1, -1))

    def accept(x, y, z):
        A, B = rep_from_traces(x, y, z)
        T, _ = monodromy_fast(steps, A, B)
        sh, _ = cusp_shape(sign, A, B, T)
        return sh is not None and matches(complex(sh))
    sols, geo = solve_fibre_fast(steps, starts=starts, accept=accept)
    out = {"state": sign + word, "non-real fixed points seen": len(sols), "hyperbolic found": geo is not None}
    if geo is None:
        return out
    A, B = rep_from_traces(*geo)
    T, tres = monodromy_fast(steps, A, B)
    sh, comm = cusp_shape(sign, A, B, T)
    out["shape"] = [complex(sh).real, complex(sh).imag]
    out["T residual"] = float(tres)
    out["commutation"] = float(comm)
    for kind in ("triv", "so"):
        info, _ = cohomology_fast(steps, A, B, T, kind)
        out["H1 " + kind] = info
    res, info = fibre_boundary_fast(steps, A, B, T)
    out["H1 v"] = info
    out["fibre boundary residual"] = res
    return out


def main_fast(pairs):
    import snappy
    for sign, word in pairs:
        sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
        print(json.dumps(record_fast(sign, word, sh), default=str), flush=True)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "--fast":
    args = sys.argv[2:]
    main_fast(list(zip(args[0::2], args[1::2])))
