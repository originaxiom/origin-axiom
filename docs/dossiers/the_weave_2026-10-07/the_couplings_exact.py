"""W38's exact addendum: the weave's group on the matter triplet T in normal form, and main's B1615 and B1616 on the
whole residual-fixed spaces, in exact arithmetic. POST HOC (after W38's one run), answering the audit lane's two
verification requests of 2026-10-08 (relays NEUTRAL_HIGGS_AND_FULL_STABILITY and TWO_NEUTRAL_INDEX_AND_PHYSICAL_DICTIONARY):
  - B1615: an exact certificate for the sum rule m1 + m2 = m3 on the whole RRL family, not a numerical grid;
  - B1616: the degeneracy on the ENTIRE residual-fixed symmetric-matrix space, all irreducibles at once.

The argument.
  (1) Numerical, from W21's construction (as in W35 and W38). The group G on T has order 96. Its image in PGL(T) has
      order 24, with 9 involutions, 8 elements of order 3 and 6 of order 4: it is S4. A three-dimensional projective
      representation of S4 is linear (the faithful irreducibles of S4's double covers have dimensions 2 and 4), so
      T = c (x) R: c a character of G, R the rotation group of the cube. In the basis of the normal Klein group's three
      axes, with the phases fixed once by a 3-cycle, every element is c(g) S(g), S(g) a signed permutation matrix of
      determinant one. This is checked on all 96 elements, and c is checked to be a homomorphism.
  (2) Exact (sympy; integer matrices and the exact roots of unity c(g)), in that basis:
      - End(T) = T-bar (x) T, M -> g M g^dagger = S M S^T (c cancels): the identity (1), the traceless diagonal (2),
        the off-diagonal symmetric (3) and the antisymmetric (3') matrices, invariant and pairwise inequivalent;
      - for L, R, RL and RRL, each piece's fixed matrices and their singular values;
      - along RRL the off-diagonal symmetric piece's fixed space is two-dimensional. On it the polynomial
        (tr X)^2 - 2 tr(X^2), X = M^dagger M, vanishes identically. That is Heron's product
        (m1 + m2 + m3)(-m1 + m2 + m3)(m1 - m2 + m3)(m1 + m2 - m3) = (tr X)^2 - 2 tr X^2, so m1 + m2 = m3 on every member;
      - the whole fixed space of each residual (all pieces at once): its dimension and whether the masses are free;
      - Sym^2 T, M -> g M g^T = c(g)^2 S M S^T: each residual's whole fixed space, all pieces at once, and the
        discriminant of X's characteristic polynomial on it. If it vanishes identically, every member has an exactly
        degenerate pair of masses.

Run: python3 the_couplings_exact.py  ->  the_couplings_exact.json beside it.
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_couplings_verified as CV  # noqa: E402  (W38: the group on T from W21's construction)

OUT = HERE / "the_couplings_exact.json"
TOL = 1e-9


def pkey(g):
    f = g.ravel()
    k = int(np.argmax(abs(f) > 1e-6))
    h = g / (f[k] / abs(f[k]))
    return tuple(np.round(np.concatenate([h.real.ravel(), h.imag.ravel()]), 6))


def is_scalar(g):
    return np.allclose(g, g[0, 0] * np.eye(3), atol=1e-8)


def porder(g):
    h = g.copy()
    for n in range(1, 64):
        if is_scalar(h):
            return n
        h = h @ g
    return None


def normal_form(GT, el):
    """the basis in which every element is c(g) S(g), S(g) a signed permutation of determinant one"""
    P = {}
    for g in GT:
        P.setdefault(pkey(g), g)
    PG = list(P.values())
    orders = {}
    for g in PG:
        orders[porder(g)] = orders.get(porder(g), 0) + 1
    inv = [g for g in PG if porder(g) == 2]

    def conj_class(h):
        return {pkey(g @ h @ np.linalg.inv(g)) for g in PG}

    klein = [h for h in inv if len(conj_class(h)) == 3]
    assert len(klein) == 3
    axes = []
    for d in klein:
        w, V = np.linalg.eig(d)
        # the simple eigenvalue: d = lambda1 diag(1, -1, -1) in its axis basis
        i = [k for k in range(3) if sum(abs(w - w[k]) < 1e-6) == 1][0]
        v = V[:, i]
        axes.append(v / np.linalg.norm(v))
    E = np.array(axes).T
    assert np.allclose(E.conj().T @ E, np.eye(3), atol=1e-8)
    # fix the phases by RL (a 3-cycle): make it c times the cyclic permutation e1 -> e2 -> e3 -> e1
    g3 = E.conj().T @ el["RL"] @ E
    if abs(g3[1, 0]) < 0.5:                      # the other orientation: swap e2 and e3
        E = E[:, [0, 2, 1]]
        g3 = E.conj().T @ el["RL"] @ E
    beta, gamma, alpha = g3[1, 0], g3[2, 1], g3[0, 2]
    best = None
    for k in range(3):
        c = (alpha * beta * gamma) ** (1 / 3) * np.exp(2j * np.pi * k / 3)
        U = np.diag([1.0, np.conj(c) * beta, c * np.conj(alpha)])
        B = E @ U
        ok, data = True, []
        for g in GT:
            M = B.conj().T @ g @ B
            nz = np.argwhere(abs(M) > 1e-6)
            if len(nz) != 3:
                ok = False
                break
            z = M[tuple(nz[0])]
            S = M / z
            if not np.allclose(S.imag, 0, atol=1e-8) or not np.allclose(abs(S.real[abs(S.real) > 1e-6]), 1, atol=1e-8):
                ok = False
                break
            S = np.round(S.real).astype(int)
            if round(np.linalg.det(S)) == -1:
                S, z = -S, -z
            data.append((g, z, S))
        if ok:
            best = (B, data)
            break
    assert best is not None, "no phase choice gives c(g) S(g)"
    return PG, orders, klein, best


def root_of_unity(z, n=24):
    k = int(round(np.angle(z) / (2 * np.pi) * n)) % n
    assert abs(z - np.exp(2j * np.pi * k / n)) < 1e-8
    return k


def exact_root(k, n=24):
    return sp.nsimplify(sp.cos(2 * sp.pi * k / n)) + sp.I * sp.nsimplify(sp.sin(2 * sp.pi * k / n))


def main():
    GT, _, el = CV.the_group()
    PG, orders, klein, (B, data) = normal_form(GT, el)
    # c is a homomorphism and S a homomorphism into SO(3): checked on all 96 x 96 products
    def fkey(g):
        return tuple(np.round(np.concatenate([g.real.ravel(), g.imag.ravel()]), 6))

    dec = {fkey(g): (z, S) for g, z, S in data}
    hom_ok = True
    for (g, z, S), (h, w, T_) in itertools.product(data, data):
        zz, SS = dec[fkey(g @ h)]
        if abs(zz - z * w) > 1e-8 or not np.array_equal(SS, S @ T_):
            hom_ok = False
    res_g = {}
    for w in ("L", "R", "RL", "RRL"):
        M = B.conj().T @ el[w] @ B
        nz = np.argwhere(abs(M) > 1e-6)
        z = M[tuple(nz[0])]
        S = np.round((M / z).real).astype(int)
        if round(np.linalg.det(S)) == -1:
            S, z = -S, -z
        assert np.allclose(M, z * S, atol=1e-8)
        res_g[w] = (root_of_unity(z), sp.Matrix(S.tolist()))

    # ---- Dirac: End(T), M -> S M S^T, exact
    def unit(i, j):
        m = sp.zeros(3, 3)
        m[i, j] = 1
        return m

    pieces = {
        "1 (the identity)": [sp.eye(3)],
        "2 (traceless diagonal)": [unit(0, 0) - unit(1, 1), unit(1, 1) - unit(2, 2)],
        "3 (off-diagonal symmetric)": [unit(1, 2) + unit(2, 1), unit(0, 2) + unit(2, 0), unit(0, 1) + unit(1, 0)],
        "3' (antisymmetric)": [unit(1, 2) - unit(2, 1), unit(2, 0) - unit(0, 2), unit(0, 1) - unit(1, 0)],
    }

    def in_span(Mx, basis):
        A = sp.Matrix.hstack(*[b.reshape(9, 1) for b in basis])
        return A.rank() == sp.Matrix.hstack(A, Mx.reshape(9, 1)).rank()

    invariant = all(in_span(S * b * S.T, basis)
                    for (_, S) in res_g.values() for basis in pieces.values() for b in basis)

    def fixed(basis, act):
        n = len(basis)
        A = sp.zeros(9, n)
        for k, b in enumerate(basis):
            A[:, k] = (act(b) - b).reshape(9, 1)
        return [sum((v[k] * basis[k] for k in range(n)), sp.zeros(3, 3)) for v in A.nullspace()]

    def spectrum(Mx):
        X = (Mx.H * Mx).applyfunc(sp.nsimplify)
        ev = sorted((sp.nsimplify(sp.sqrt(e)) for e, m in X.eigenvals().items() for _ in range(m)), key=lambda e: float(e))
        top = ev[-1]
        return [str(sp.nsimplify(e / top)) for e in ev] if top != 0 else [str(e) for e in ev]

    dirac = []
    family = None
    for w, (_, S) in res_g.items():
        for name, basis in pieces.items():
            F = fixed(basis, lambda b, S=S: S * b * S.T)
            row = {"residual": w, "piece": name, "fixed dimension": len(F)}
            if len(F) == 1:
                row["masses (m/m3), exact"] = spectrum(F[0])
            if len(F) == 2:
                family = (w, name, F)
            dirac.append(row)

    # the RRL family: Heron's polynomial
    x, z, xb, zb = sp.symbols("x z xbar zbar")
    w_f, name_f, F = family
    M = x * F[0] + z * F[1]
    Mb = xb * F[0] + zb * F[1]               # the conjugate, with x-bar and z-bar independent symbols (F is real)
    X = Mb.T * M
    heron = sp.expand(X.trace() ** 2 - 2 * (X * X).trace())
    # closed-form masses on the family
    lam = sp.symbols("lam")
    charpoly = sp.factor(sp.expand((X - lam * sp.eye(3)).det()))
    fam = {"residual": w_f, "piece": name_f, "basis": [str(f.tolist()) for f in F],
           "(tr X)^2 - 2 tr X^2 on the family (X = M^dagger M)": str(heron),
           "det(X - lam) factored": str(charpoly)}
    # m1/m3 at the family's two ends and at its midpoint candidates
    samples = {}
    for (a, b) in ((1, 0), (0, 1), (1, 1), (1, -1), (1, 2), (2, 1), (1, sp.I)):
        Mi = M.subs({x: a, z: b})
        samples[str((a, b))] = spectrum(Mi)
    fam["masses (m/m3) at sample members, exact"] = samples

    # the whole fixed space of each residual in End(T) (the commutant of S): all pieces at once
    whole_dirac = {}
    for w, (_, S) in res_g.items():
        basis = [unit(i, j) for i in range(3) for j in range(3)]
        F = fixed(basis, lambda b, S=S: S * b * S.T)
        per_piece = sum(r["fixed dimension"] for r in dirac if r["residual"] == w)
        # a random matrix diagonal in S's (orthonormal) eigenbasis lies in the fixed space: three free masses
        Sn = np.array(S.tolist(), dtype=float)
        _, V = np.linalg.eig(Sn)
        Q, _ = np.linalg.qr(V)
        rng = np.random.default_rng(7)
        D = Q @ np.diag(rng.normal(size=3) + 1j * rng.normal(size=3)) @ Q.conj().T
        Fn = np.array([np.array(f.tolist(), dtype=complex).ravel() for f in F]).T
        coef = np.linalg.lstsq(Fn, D.ravel(), rcond=None)[0]
        whole_dirac[w] = {"dimension": len(F), "the pieces' fixed dimensions add up to it": per_piece == len(F),
                          "it holds every matrix diagonal in S's eigenbasis (three free masses)":
                              bool(np.allclose(Fn @ coef, D.ravel(), atol=1e-9))}

    # ---- Majorana: Sym^2 T, M -> c^2 S M S^T, exact; every residual's whole fixed space
    sym_basis = [unit(i, i) for i in range(3)] + [unit(i, j) + unit(j, i) for i, j in ((1, 2), (0, 2), (0, 1))]
    majorana = {}
    for w, (k, S) in res_g.items():
        c2 = sp.nsimplify(exact_root(2 * k))
        F = fixed(sym_basis, lambda b, S=S, c2=c2: sp.expand(c2 * S * b * S.T))
        row = {"c(g) = exp(2 pi i k/24), k": k, "fixed dimension (all pieces at once)": len(F)}
        if F:
            ts = sp.symbols("t0:%d" % len(F))
            tbs = sp.symbols("tb0:%d" % len(F))
            Mm = sum((ts[i] * F[i] for i in range(len(F))), sp.zeros(3, 3))
            Mmb = sum((tbs[i] * F[i].conjugate() for i in range(len(F))), sp.zeros(3, 3))
            Xm = (Mmb.T * Mm).applyfunc(sp.expand)
            cp = sp.Poly(sp.expand((Xm - lam * sp.eye(3)).det()), lam)
            disc = sp.expand(sp.discriminant(cp.as_expr(), lam))
            row["discriminant of det(X - lam) on the whole fixed space"] = str(sp.simplify(disc))
            row["every member has an exactly degenerate pair"] = sp.simplify(disc) == 0
            row["det(X - lam) factored"] = str(sp.factor(cp.as_expr()))
        majorana[w] = row

    res = {
        "status": ("POST HOC exact addendum to W38 (a verification of main's B1615 and B1616, not blind), answering the "
                   "audit lane's two verification requests"),
        "G's order on T": len(GT),
        "PGL(T) image: order and element orders": {"order": len(PG), "orders": {str(k): v for k, v in sorted(orders.items())}},
        "every element is c(g) S(g) in the Klein axes' basis (all 96)": len(data) == 96,
        "c and S are homomorphisms (checked on the projective group)": hom_ok,
        "the residual elements": {w: {"c = exp(2 pi i k/24), k": k, "S": str(S.tolist()),
                                      "S's order": next(n for n in range(1, 13) if S ** n == sp.eye(3))}
                                  for w, (k, S) in res_g.items()},
        "End(T)'s four pieces invariant under every residual": invariant,
        "Dirac: each piece's fixed vacua (exact)": dirac,
        "Dirac: the RRL family (exact)": fam,
        "Dirac: each residual's whole fixed space (all pieces at once)": whole_dirac,
        "Majorana: each residual's whole fixed space (all pieces at once)": majorana,
    }
    res["checks"] = {
        "the projective image is S4 (order 24; 9, 8, 6 elements of orders 2, 3, 4)":
            len(PG) == 24 and orders == {1: 1, 2: 9, 3: 8, 4: 6},
        "T = c (x) the cube's rotations, on all 96 elements": len(data) == 96 and hom_ok,
        "RL a 3-cycle, RRL an edge half-turn, L and R quarter-turns": (
            res["the residual elements"]["RL"]["S's order"] == 3 and res["the residual elements"]["RRL"]["S's order"] == 2
            and res["the residual elements"]["L"]["S's order"] == 4 and res["the residual elements"]["R"]["S's order"] == 4),
        "the RRL family lies in the off-diagonal symmetric piece and Heron's polynomial vanishes identically": (
            name_f.startswith("3 (off") and heron == 0),
        "the antisymmetric piece gives (0, 1, 1) wherever it is fixed": all(
            r.get("masses (m/m3), exact") == ["0", "1", "1"] for r in dirac
            if r["piece"].startswith("3'") and r["fixed dimension"] == 1),
        "every residual-fixed Majorana matrix, all pieces at once, has an exactly degenerate pair": all(
            r.get("every member has an exactly degenerate pair", True) for r in majorana.values()),
        "along RRL no Majorana matrix is fixed": majorana["RRL"]["fixed dimension (all pieces at once)"] == 0,
        "with Higgs fields in several pieces along one residual the Dirac masses are free": all(
            v["it holds every matrix diagonal in S's eigenbasis (three free masses)"]
            and v["the pieces' fixed dimensions add up to it"] for v in whole_dirac.values()),
    }
    res["every check holds"] = all(res["checks"].values())
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
