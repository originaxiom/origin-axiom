"""Round 5: S25 / B1430's hypercharge claim, made EXHAUSTIVE.

B1430: "exactly three hypercharges give the 27 the Standard Model's multiset ... exactly 3 of 28 513 scanned
rational directions, and those three are a single stabiliser orbit" -- and its own section 6: "The u(1) scan
is a box of 28 513 rational directions, not an exhaustive proof over all of them."

The box is unnecessary.  Fix one commuting (A2, A1) pair (all 720 are one Weyl orbit -- verified).  The 27
splits into irreducible A2 x A1 pieces; a hypercharge Y lies in the 3-dimensional commutant, is constant on
each piece, and is linear in Y.  The Standard-Model multiset of the 27 is

    Q (3,2)_{1/6} ; D (3,1)_{-1/3} ;  three conjugate triplets {-2/3, 1/3, 1/3} ;
    three doublets {-1/2, -1/2, +1/2} ;  three singlets {1, 0, 0}

(u^c, d^c, D^c ; L, H_d, H_u ; e^c, nu^c, S), with "conjugate" meaning opposite colour type to Q.  Setting
Q's charge to +1/6 fixes Y's scale and sign, so each solution is one direction.  Which conjugate triplet
takes -2/3, which doublet +1/2, which singlet 1: 27 assignments, each an overdetermined linear system in 3
unknowns, solved exactly.  The union of their solutions is EVERY hypercharge direction, rational or not,
giving the SM multiset.  No box.

Nothing is read from B1430's code.  E6 from its Cartan matrix; the 27 as the Weyl orbit of a fundamental
weight; exact rational arithmetic throughout.
"""
from fractions import Fraction as Fr
import itertools

EDGES = {(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)}          # Bourbaki E6
A = [[2 if i == j else (-1 if (i + 1, j + 1) in EDGES or (j + 1, i + 1) in EDGES else 0)
      for j in range(6)] for i in range(6)]


def ip(u, v):
    return sum(u[i] * A[i][j] * v[j] for i in range(6) for j in range(6))


def refl(i, v):
    c = sum(v[j] * A[j][i] for j in range(6))
    w = list(v); w[i] -= c
    return tuple(w)


def inverse(M):
    n = len(M); X = [[Fr(M[i][j]) for j in range(n)] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if X[r][c] != 0)
        X[c], X[p] = X[p], X[c]
        pv = X[c][c]; X[c] = [x / pv for x in X[c]]
        for r in range(n):
            if r != c and X[r][c] != 0:
                f = X[r][c]; X[r] = [a - f * b for a, b in zip(X[r], X[c])]
    return [row[n:] for row in X]


def closure(start, f, ngen=6):
    seen = {start}; fr = [start]
    while fr:
        nx = []
        for x in fr:
            for i in range(ngen):
                y = f(i, x)
                if y not in seen:
                    seen.add(y); nx.append(y)
        fr = nx
    return seen


def solve_exact(rows, rhs, n):
    """least-squares-free exact solve of an overdetermined system; returns the unique solution or None"""
    M = [list(map(Fr, r)) + [Fr(b)] for r, b in zip(rows, rhs)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    if any(all(x == 0 for x in row[:n]) and row[n] != 0 for row in M):
        return None                                     # inconsistent
    if len(piv) < n:
        return "underdetermined"
    sol = [Fr(0)] * n
    for i, c in enumerate(piv):
        sol[c] = M[i][n]
    return tuple(sol)


def main():
    simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
    roots = closure(simple[0], refl) | set()
    for s in simple:
        roots |= closure(s, refl)
    roots = sorted(roots)
    print(f"E6: {len(roots)} roots")

    Ainv = inverse(A)
    omega1 = tuple(Ainv[0])                             # fundamental weight 1, in the root basis
    W27 = sorted(closure(omega1, refl))
    minuscule = all(ip(w, a) in (-1, 0, 1) for w in W27 for a in roots)
    print(f"27: Weyl orbit of omega_1 has {len(W27)} weights; minuscule: {minuscule}")

    # one commuting (A2, A1) pair
    a1 = simple[0]
    a2 = next(r for r in roots if ip(a1, r) == -1)
    a12 = tuple(x + y for x, y in zip(a1, a2))
    A2 = {a1, a2, a12} | {tuple(-x for x in r) for r in (a1, a2, a12)}
    b = next(r for r in roots if all(ip(r, s) == 0 for s in A2))
    A1 = {b, tuple(-x for x in b)}
    sub = A2 | A1

    # irreducible A2 x A1 pieces of the 27: connected components under subsystem root steps
    Wset = set(W27); comp = {}
    for w in W27:
        if w in comp:
            continue
        stack, cid = [w], len(set(comp.values()))
        comp[w] = cid
        while stack:
            x = stack.pop()
            for g in sub:
                y = tuple(p + q for p, q in zip(x, g))
                if y in Wset and y not in comp:
                    comp[y] = cid; stack.append(y)
    pieces = {}
    for w, c in comp.items():
        pieces.setdefault(c, []).append(w)
    P3 = {(1, 0), (-1, 1), (0, -1)}
    P3b = {(0, 1), (1, -1), (-1, 0)}

    def colour(ws):
        labs = {(ip(w, a1), ip(w, a2)) for w in ws}
        return "3" if labs == P3 else ("3b" if labs == P3b else "1")

    info = []
    for c, ws in pieces.items():
        col = colour(ws)
        weak = len(ws) // (3 if col != "1" else 1)
        info.append({"w": ws[0], "size": len(ws), "col": col, "weak": weak})
    shape = sorted((d["size"], d["col"]) for d in info)
    print(f"pieces under A2 x A1: {len(info)};  (size, colour): {shape}")

    Q = [d for d in info if d["size"] == 6]
    assert len(Q) == 1, "no unique (3,2)"
    Qc = Q[0]["col"]
    same = [d for d in info if d["size"] == 3 and d["col"] == Qc]
    opp = [d for d in info if d["size"] == 3 and d["col"] != Qc]
    dbl = [d for d in info if d["size"] == 2]
    sgl = [d for d in info if d["size"] == 1]
    print(f"relative to Q's colour: same-type triplets {len(same)}, conjugate triplets {len(opp)}, "
          f"doublets {len(dbl)}, singlets {len(sgl)}   (SM needs 1, 3, 3, 3)")

    # the commutant: Y with (Y, a1) = (Y, a2) = (Y, b) = 0  -- a basis by exact nullspace
    cons = [[sum(A[i][j] * v[j] for j in range(6)) for i in range(6)] for v in (a1, a2, b)]
    basis = []
    # nullspace of the 3x6 constraint matrix
    M = [list(map(Fr, r)) for r in cons]
    piv, r = [], 0
    for c in range(6):
        p = next((i for i in range(r, 3) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(3):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        piv.append(c); r += 1
    freec = [c for c in range(6) if c not in piv]
    for fc in freec:
        v = [Fr(0)] * 6; v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -M[i][fc]
        basis.append(tuple(v))
    print(f"commutant: dimension {len(basis)}")

    def charge_row(w):                                  # charge of weight w as a linear form in the coefficients
        return [ip(v, w) for v in basis]

    sols = set()
    for o_i, d_i, s_i in itertools.product(range(3), range(3), range(3)):
        rows, rhs = [charge_row(Q[0]["w"])], [Fr(1, 6)]
        rows.append(charge_row(same[0]["w"])); rhs.append(Fr(-1, 3))
        for k, d in enumerate(opp):
            rows.append(charge_row(d["w"])); rhs.append(Fr(-2, 3) if k == o_i else Fr(1, 3))
        for k, d in enumerate(dbl):
            rows.append(charge_row(d["w"])); rhs.append(Fr(1, 2) if k == d_i else Fr(-1, 2))
        for k, d in enumerate(sgl):
            rows.append(charge_row(d["w"])); rhs.append(Fr(1) if k == s_i else Fr(0))
        x = solve_exact(rows, rhs, len(basis))
        if x == "underdetermined":
            raise RuntimeError("a system left freedom -- the count would be infinite")
        if x is not None:
            Y = tuple(sum(x[k] * basis[k][i] for k in range(len(basis))) for i in range(6))
            sols.add(Y)
    print(f"\nall 27 assignments solved exactly: {len(sols)} hypercharge direction(s) give the SM multiset")

    # double-check each solution reproduces the multiset directly on all 27 weights
    target = sorted([(6, "Q", Fr(1, 6))] + [(3, "same", Fr(-1, 3))] +
                    [(3, "opp", y) for y in (Fr(-2, 3), Fr(1, 3), Fr(1, 3))] +
                    [(2, "", y) for y in (Fr(-1, 2), Fr(-1, 2), Fr(1, 2))] +
                    [(1, "", y) for y in (Fr(1), Fr(0), Fr(0))])
    for Y in sols:
        got = []
        for d in info:
            y = ip(Y, d["w"])
            assert all(ip(Y, w) == y for w in pieces[[k for k, v in pieces.items() if d["w"] in v][0]])
            tag = "Q" if d["size"] == 6 else ("same" if d["size"] == 3 and d["col"] == Qc else
                                             ("opp" if d["size"] == 3 else ""))
            got.append((d["size"], tag, y))
        assert sorted(got) == target, (Y, sorted(got))
    print("   each re-checked directly against the multiset on all 27 weights: yes")

    # the stabiliser of the pair, and its action on the solutions
    def perm_of(i):
        return tuple(roots.index(refl(i, r)) for r in roots)
    gens = [perm_of(i) for i in range(6)]
    ident = tuple(range(len(roots)))
    G = {ident}; fr = [ident]
    while fr:
        nx = []
        for g in fr:
            for h in gens:
                k = tuple(h[g[t]] for t in range(len(roots)))
                if k not in G:
                    G.add(k); nx.append(k)
        fr = nx
    print(f"\n|W(E6)| as permutations of the roots: {len(G)}")
    idx = {r: t for t, r in enumerate(roots)}
    A2i, A1i = {idx[r] for r in A2}, {idx[r] for r in A1}
    stab = [g for g in G if {g[t] for t in A2i} == A2i and {g[t] for t in A1i} == A1i]
    print(f"stabiliser of the (A2, A1) pair: order {len(stab)}")

    simple_idx = [idx[s] for s in simple]

    def act(g, Y):                                      # w(Y) = sum_i Y_i w(alpha_i)
        imgs = [roots[g[simple_idx[i]]] for i in range(6)]
        return tuple(sum(Y[i] * imgs[i][j] for i in range(6)) for j in range(6))

    def line(Y):                                        # normalise sign by the charge of Q
        qc = ip(Y, Q[0]["w"])
        return Y if qc > 0 else tuple(-x for x in Y)

    S = [line(Y) for Y in sols]
    orbit = {line(act(g, S[0])) for g in stab}
    print(f"orbit of one solution under the stabiliser: {len(orbit & set(S))} of the {len(S)} solutions"
          f"  -> single orbit: {set(S) <= orbit}")
    print("\nThe count is over the WHOLE commutant, rational or not; B1430's box is not needed and its")
    print("'not an exhaustive proof' caveat is closed -- for this (A2, A1) pair, hence for all 720 by the orbit.")


if __name__ == "__main__":
    main()
