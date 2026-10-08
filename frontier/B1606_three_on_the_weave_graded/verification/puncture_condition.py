#!/usr/bin/env python3
"""B1606 -- main's check of the SM seat's W22 as qualified by its W24 cell D0: the puncture conditions the weave keeps.
At the puncture the holonomy of every parity block chi_p (x) rho_Q is -1 (central), so each block has a two-dimensional
space of local solutions and the six together carry the moves' lifts: g_m (in 2O, acting on rho_Q's C^2) tensored with
the move's permutation of the parities, twisted by the quaternion units u_p (j, i, k) that identify chi_p (x) rho_Q with
rho_Q (the seat's D1: chi_p (x) rho_Q = u_p rho_Q u_p^-1).  A self-adjoint condition that keeps the two-dimensional
chirality is a subspace Lambda_+ of the six local solutions; its index is dim Lambda_+ - 3 (Riemann-Roch, one block at a
time: the degree of the extension is dim - 1 per block).  Computed here: the commutant of the moves' lifts on C^6 and
its invariant subspaces (their dimensions, hence the kept indices); the same with the parity grading (the block-diagonal
signs chi_p, equivalently the flavour U(3) of W = rho_Q (x) C^3) added to the symmetry; whether -1 (the lift of the
sign) acts as -1 on all six (so every kept condition is a sum of 2O spinor representations, of even dimension, and the
index is odd).  Writes puncture_condition.json."""
import json, pathlib, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
I2 = np.eye(2, dtype=complex)
qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]]); qk = qi @ qj
s = 1 / np.sqrt(2)
LIFT = {"L": (I2 + qi) * s, "R": (I2 - qj) * s, "sign": qk}
PAR = [(1, 0), (0, 1), (1, 1)]
U = {(1, 0): qj, (0, 1): qi, (1, 1): qk}            # chi_p (x) rho_Q = u_p rho_Q u_p^-1 : the seat's D1 (checked below)
rho = {"a": qi, "b": qj}
MOVES = {"L": {"a": "a", "b": "ab"}, "R": {"a": "ab", "b": "b"}, "sign": {"a": "A", "b": "B"}}


def chi(p, letter):
    return (-1) ** (p[0] if letter == "a" else p[1])


def act_parity(m, p):
    sa = np.prod([chi(p, c.lower()) for c in m["a"]]); sb = np.prod([chi(p, c.lower()) for c in m["b"]])
    return (0 if sa == 1 else 1, 0 if sb == 1 else 1)


# D1: chi_p (x) rho_Q = u_p rho_Q u_p^-1 on the generators
d1 = all(np.allclose(chi(p, x) * rho[x], U[p] @ rho[x] @ np.linalg.inv(U[p])) for p in PAR for x in "ab")

# the lift of a move on the six local solutions: block p -> block q = p o m, by the matrix u_q^-1 g u_p (so that the
# identification with rho_Q is respected: g carries chi_p (x) rho_Q to chi_q (x) rho_Q (the pullback), and u's rewrite
# each block as rho_Q)
def six(m, g):
    M = np.zeros((6, 6), dtype=complex)
    for ip, p in enumerate(PAR):
        q = act_parity(MOVES[m], p); iq = PAR.index(q)
        M[2 * iq: 2 * iq + 2, 2 * ip: 2 * ip + 2] = np.linalg.inv(U[q]) @ g @ U[p]
    return M


GENS = {m: six(m, LIFT[m]) for m in LIFT}


def group(gens):
    G = [np.eye(6, dtype=complex)]; fr = [np.eye(6, dtype=complex)]
    while fr:
        M = fr.pop()
        for g in gens:
            N = M @ g
            if not any(np.allclose(N, E, atol=1e-7) for E in G):
                G.append(N); fr.append(N)
                if len(G) > 5000: raise RuntimeError("not finite")
    return G


def commutant(G):
    rows = [np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in G]
    A = np.vstack(rows); sv = np.linalg.svd(A, compute_uv=False)
    return int(sum(1 for x in sv if x < 1e-8)) + (36 - len(sv) if len(sv) < 36 else 0)


def invariant_subspace_dims(G):
    """the dimensions of the invariant subspaces, from the isotypic decomposition: with commutant c the irreducible
    constituents are found by the group's character; here: the eigenspaces of a generic element of the commutant"""
    rows = [np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in G]
    A = np.vstack(rows); U_, sv, Vh = np.linalg.svd(A); c = int(sum(1 for x in sv if x < 1e-8))
    null = Vh[-c:].conj() if c else []
    rng = np.random.default_rng(1606); X = sum(rng.normal() * v.reshape(6, 6, order="F") for v in null) if c else np.eye(6)
    ev = np.linalg.eigvals(X); groups = {}
    for e in ev:
        groups.setdefault(tuple(np.round([e.real, e.imag], 5)), 0); groups[tuple(np.round([e.real, e.imag], 5))] += 1
    dims = sorted(groups.values())
    # every sum of isotypic pieces is invariant; if the pieces are inequivalent irreducibles, the invariant subspaces
    # are exactly the sums of subsets
    subs = sorted({sum(c) for r in range(len(dims) + 1) for c in itertools.combinations(dims, r)})
    return dims, subs


out = {"D1_chi_p_rho_is_u_p_rho_u_p_inverse": bool(d1)}
G_moves = group([GENS["L"], GENS["R"]])
out["moves"] = {"order": len(G_moves), "commutant": commutant(G_moves)}
dims, subs = invariant_subspace_dims(G_moves)
out["moves"]["isotypic_dimensions"] = dims; out["moves"]["kept_dimensions"] = subs; out["moves"]["kept_indices"] = [d - 3 for d in subs]
out["moves"]["minus_one_in_group_acts_as_minus_one"] = bool(any(np.allclose(g, -np.eye(6), atol=1e-7) for g in G_moves))
out["moves"]["all_kept_indices_odd"] = all((d - 3) % 2 == 1 for d in subs)
# with the parity grading: the block-diagonal signs (+1 on one block, -1 on the others, and all sign patterns) added
grading = [np.diag(np.repeat([1 if k == j else -1 for k in range(3)], 2)).astype(complex) for j in range(3)]
G_graded = group([GENS["L"], GENS["R"]] + grading)
dims_g, subs_g = invariant_subspace_dims(G_graded)
out["moves_and_grading"] = {"order": len(G_graded), "commutant": commutant(G_graded), "isotypic_dimensions": dims_g, "kept_dimensions": subs_g, "kept_indices": [d - 3 for d in subs_g]}
# with the sign move as well
G_all = group([GENS["L"], GENS["R"], GENS["sign"]])
out["moves_and_sign"] = {"order": len(G_all), "commutant": commutant(G_all)}
json.dump(out, open(HERE / "puncture_condition.json", "w"), indent=1); print(json.dumps(out, indent=1))
