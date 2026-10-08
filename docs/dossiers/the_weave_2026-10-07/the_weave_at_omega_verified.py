"""Main's B1617 (the weave at tau = omega, given the owner's tagged postulate) verified with this seat's code. A
VERIFICATION, not blind: B1617's read-out was read first (main @ 5658257a). B1617 is "given tau = omega".

The residual symmetry at omega is built from W21's construction, as in W35 and W38:
  - U, the automorphism a -> b, b -> a^-1 b (main's "L^-1 then R"); its H1 matrix [[0, -1], [1, 1]] has order 6 and
    fixes omega;
  - the inner automorphisms (conjugation by a and by b), which fix every tau;
  - the sign -I.
The fixed-point convention is CONVENTIONS.md section 3: under the period rule (the geometric action on W21's period
ratio) U fixes omega + 1, the same torus, and L U L^-1 fixes omega; the group-level results are computed for both.
Each is lifted to V through every element of 2O that realises it at the common point (the_common_point.extend), and
restricted to the matter triplet T in the Hodge-Riemann form's orthonormal basis (the_mixing_patterns_verified.on_T).
Then: the group's order on T; T's commutant under it; U's eigen-turns on T; the inner automorphisms and U in W38's
normal form (the Klein axes' basis, every element c(g) S(g)); the invariants in T-bar (x) T, T (x) T and Sym^2 T.

Run: python3 the_weave_at_omega_verified.py  ->  the_weave_at_omega_verified.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_couplings_exact as CE  # noqa: E402  (W38's normal form)
import the_couplings_verified as CV  # noqa: E402  (W38: the group on T)
import the_mixing_patterns_verified as MV  # noqa: E402  (W35: T and its basis)

OUT = HERE / "the_weave_at_omega_verified.json"
CP, CT, H = MV.CP, MV.CT, MV.H
OMEGA = np.exp(2j * np.pi / 3)


def h1(phi):
    """the abelianised automorphism: columns are the images of a and b"""
    cols = []
    for g in (1, 2):
        v = [0, 0]
        for x in phi[g]:
            v[abs(x) - 1] += 1 if x > 0 else -1
        cols.append(v)
    return np.array(cols).T


def mobius(M, t):
    (a, b), (c, d) = M
    return (a * t + b) / (c * t + d)


def closure(gens, cap=5000):
    G = {}
    fr = [np.eye(gens[0].shape[0], dtype=complex)]
    k = lambda M: tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 6))
    G[k(fr[0])] = fr[0]
    while fr:
        if len(G) > cap:
            raise RuntimeError("closure exceeded %d elements" % cap)
        nx = []
        for X in fr:
            for g in gens:
                Y = X @ g
                if k(Y) not in G:
                    G[k(Y)] = Y
                    nx.append(Y)
        fr = nx
    return list(G.values())


def commutant_dim(ops, dim):
    M = np.vstack([np.kron(np.eye(dim), A) - np.kron(A.T, np.eye(dim)) for A in ops])
    s = np.linalg.svd(M, compute_uv=False)
    return int(sum(s < 1e-8 * max(1.0, s[0]))) + max(0, dim * dim - len(s))


def invariants(G, f):
    return round(float(np.real(sum(f(g) for g in G)) / len(G)), 6)


def main():
    named, _ = H.triplets()
    C = named["T"]
    G0 = H.gram_V()
    Qt = C.conj().T @ G0 @ C
    K = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T

    U = {1: [2], 2: [-1, 2]}
    autos = {"U": U, "inner by a": CP.inner([1]), "inner by b": CP.inner([2]), "-I": CP.AUT["-I"]}
    MU = h1(U)
    # the geometric action on W21's period ratio is the period rule tau -> (delta tau + beta)/(gamma tau + alpha)
    # (CONVENTIONS.md section 3): U fixes omega + 1 there, and L U L^-1 fixes omega; under the standard rule U fixes omega
    period = lambda M, t: (M[1][1] * t + M[0][1]) / (M[1][0] * t + M[0][0])
    L_inv = {1: [1], 2: [-1, 2]}
    LUL = CP.compose(CP.compose(CP.AUT["L"], U), L_inv)
    MLUL = h1(LUL)
    fixes = {"standard rule: U fixes omega": bool(abs(mobius(MU, OMEGA) - OMEGA) < 1e-12),
             "period rule: U fixes omega + 1": bool(abs(period(MU, OMEGA + 1) - (OMEGA + 1)) < 1e-12),
             "period rule: L U L^-1 fixes omega": bool(abs(period(MLUL, OMEGA) - OMEGA) < 1e-12)}
    lifts = {n: [MV.on_T(C, K, CT.on_V(phi, g)) for g in CP.extend(phi)] for n, phi in autos.items()}
    gens = [x for v in lifts.values() for x in v]
    R = closure(gens)
    order = len(R)
    comm = commutant_dim(gens, 3)

    # U's eigen-turns on T (the lift and its negative)
    turns = {}
    for i, gU in enumerate(lifts["U"]):
        ev = np.linalg.eigvals(gU)
        turns["lift %d" % i] = sorted(round(round(float(np.angle(e) / (2 * np.pi)), 6) % 1, 6) for e in ev)
    uorder = next(n for n in range(1, 100) if np.allclose(np.linalg.matrix_power(lifts["U"][0], n), np.eye(3), atol=1e-8))

    # W38's normal form: B, the Klein axes' basis; each element c S with S a signed permutation of determinant one
    GT, _, el = CV.the_group()
    _, _, _, (B, _) = CE.normal_form(GT, el)

    def nf(g):
        M = B.conj().T @ g @ B
        nz = np.argwhere(abs(M) > 1e-6)
        if len(nz) != 3:
            return None
        z = M[tuple(nz[0])]
        S = M / z
        if not np.allclose(S.imag, 0, atol=1e-8):
            return None
        S = np.round(S.real).astype(int)
        if round(np.linalg.det(S)) == -1:
            S, z = -S, -z
        if not np.allclose(M, z * S, atol=1e-8):
            return None
        return {"c = exp(2 pi i k/24), k": CE.root_of_unity(z), "S": S.tolist()}

    normal = {n: [nf(g) for g in v] for n, v in lifts.items()}
    in_G = {n: [bool(any(np.allclose(g, h, atol=1e-8) for h in GT)) for g in v] for n, v in lifts.items()}

    # the same residual group built with the period rule's stabiliser of omega (L U L^-1): conjugate, so the same results
    autos_p = dict(autos)
    autos_p["U"] = LUL
    lifts_p = {n: [MV.on_T(C, K, CT.on_V(phi, g)) for g in CP.extend(phi)] for n, phi in autos_p.items()}
    gens_p = [x for v in lifts_p.values() for x in v]
    turns_p = sorted(sorted(round(round(float(np.angle(e) / (2 * np.pi)), 6) % 1, 6) for e in np.linalg.eigvals(g))
                     for g in lifts_p["U"])
    period_stabiliser = {"its H1 matrix": MLUL.tolist(), "the residual group's order on T": len(closure(gens_p)),
                         "T's commutant under it": commutant_dim(gens_p, 3), "its eigen-turns on T (both lifts)": turns_p}

    inv = {
        "T-bar (x) T (Dirac, B1615's tensor)": invariants(R, lambda g: abs(np.trace(g)) ** 2),
        "T (x) T (W39's tensor given Lambda)": invariants(R, lambda g: np.trace(g) ** 2),
        "Sym^2 T": invariants(R, lambda g: (np.trace(g) ** 2 + np.trace(g @ g)) / 2),
    }
    res = {
        "status": "VERIFICATION of main's B1617 (read first), with this seat's code; given tau = omega",
        "U's H1 matrix": MU.tolist(),
        "U's order in SL(2, Z)": next(n for n in range(1, 13) if np.array_equal(np.linalg.matrix_power(MU, n), np.eye(2, dtype=int))),
        "which fixes omega (both rules)": fixes,
        "the period rule's stabiliser of omega, L U L^-1": period_stabiliser,
        "the residual group's order on T": order,
        "T's commutant under it (1 = irreducible)": comm,
        "U's order on T": uorder,
        "U's eigen-turns on T": turns,
        "in W38's normal form": normal,
        "inside the L, R group of order 96": in_G,
        "invariants under the residual group": inv,
    }
    inner_klein = all(x is not None and all(row.count(0) == 2 for row in x["S"]) and
                      all(x["S"][i][i] != 0 for i in range(3))
                      for n in ("inner by a", "inner by b") for x in normal[n])
    u_cycle = all(x is not None and all(x["S"][i][i] == 0 for i in range(3)) for x in normal["U"])
    res["checks"] = {
        "U has order 6; under the period rule U fixes omega + 1 and L U L^-1 fixes omega": (
            res["U's order in SL(2, Z)"] == 6 and fixes["period rule: U fixes omega + 1"]
            and fixes["period rule: L U L^-1 fixes omega"]),
        "the period rule's stabiliser gives the same order, irreducibility and eigen-turns": (
            period_stabiliser["the residual group's order on T"] == order and period_stabiliser["T's commutant under it"] == comm
            and sorted(turns.values()) == turns_p),
        "the residual group has order 48 on T": order == 48,
        "T is irreducible under it (B1617's Z2 fails)": comm == 1,
        "U has order 12 on T with eigen-turns 1/4, 7/12, 11/12 (one lift)": uorder == 12 and any(
            t == [0.25, 0.583333, 0.916667] for t in turns.values()),
        "the inner automorphisms act as diagonal signs (the Klein group, the parity grading)": inner_klein,
        "U acts as a 3-cycle of the axes": u_cycle,
        "one invariant in T-bar (x) T (three equal masses), none in T (x) T or Sym^2 T": (
            inv["T-bar (x) T (Dirac, B1615's tensor)"] == 1 and inv["T (x) T (W39's tensor given Lambda)"] == 0
            and inv["Sym^2 T"] == 0),
    }
    res["every check holds"] = all(res["checks"].values())
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
