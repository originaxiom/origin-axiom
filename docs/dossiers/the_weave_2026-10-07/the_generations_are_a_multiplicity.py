"""W49 (the rule: W49_RULE.md, committed before this script). The generations are a multiplicity: three or split.

The weave's local system is W = sum over the parities p of chi_p (x) rho_Q. The quaternion units u_p, with
u_p rho_Q u_p^-1 = chi_p rho_Q (W24 D1; W28's units_of_parities), identify it with rho_Q (x) M, M = C^3 the multiplicity:
Psi(v (x) e_p) = u_p v in parity p's block. On the twisted cohomology V = H1(F2; W) the same units give
Phi_p(z) = u_p^-1 z, from parity p's block of V to D = H1(F2; rho_Q), the doublet. (W21's code calls D "M"; here M is the
multiplicity.)

  controls  the identification on the fibre: Psi^-1 W(x) Psi = 1 (x) rho_Q(x) for x = a, b; every lift of L and R on the
            six local solutions (W24's blocks_action) is S (x) g, S a signed permutation of the three blocks.
  M1  T (W21's holomorphic triplet) meets each parity block of V in a line. Phi_p sends the three lines to one line l of
      D. l is invariant under every lift of L and R on D, Q(l, l) > 0 (W21's Hodge-Riemann form at the zero parity), and
      the other invariant line, l's Q-orthogonal complement, is Q-negative.
  M2  In the basis t_p (T's line in block p, scaled so that Phi_p(t_p) = l^): each lift of L and R acts on T as c times a
      signed permutation, c its eigenvalue on l; each lift of the inner automorphisms acts as its sign on l times the
      parity signs; the group the lifts of L and R generate on T is W42's {z S : S a rotation of the cube, z^8 = 1,
      z^4 = sgn S}, 96 elements, and it contains the inner automorphisms' lifts (W42's K and E).
  M3  The Hodge-Riemann form on T in the basis t_p is Q(l^, l^) times the identity.
  M4  The four puncture conditions (W28 E2; W46's Q2 and Q4) in rho_Q (x) M coordinates, each vector a 2 x 3 matrix:
      the generic rank of V2's and V4's vectors; the support test (a subspace W is a product X (x) Y iff
      dim W = dim X_W * dim Y_W, X_W and Y_W the spans of its matrices' columns and rows; W lies in X_W (x) Y_W always);
      flavour-blind (W = X (x) M) iff dim W = 3 dim X_W.

  Extra read-outs, reported and not predicted (no prior was set):
      E1  the signed permutation of M2 is the lift's conjugation of the three units: g^-1 u_p g = sum_q P_qp u_q.
      E2  T-bar meets each block in a line, and Phi_p sends the three to l's Q-orthogonal complement.
      E3  the singular values of V2's vectors, as 2 x 3 matrices, for random vectors.
      E4  the fibre index of each puncture condition (W46's table, recomputed) beside its type.

Run: python3 the_generations_are_a_multiplicity.py  ->  the_generations_are_a_multiplicity.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_end_conditions_on_the_weaves_surface as EC  # noqa: E402  (W46: Q2, Q4, CONDITIONS, frame, reps, table)
import the_six_dimensional_census as SC  # noqa: E402  (W24: blocks_action, W_of)
import the_spin_room as SR  # noqa: E402  (QM, RHO, qmat, char_val, cocycle_on_word)
import the_three_routes_and_the_qubit as TQ  # noqa: E402  (W28: units_of_parities)

CP, CT, H = EC.CP, EC.CT, EC.H
OUT = HERE / "the_generations_are_a_multiplicity.json"
TOL = 1e-8
ZERO = H.ZERO
INNER = {"inner by a": (CP.inner([1]), 1), "inner by b": (CP.inner([2]), 2)}


def close(A, B, tol=TOL):
    return bool(np.allclose(A, B, atol=tol))


def cx(z):
    z = complex(z)
    return [round(z.real, 9), round(z.imag, 9)]


def mat(M):
    return [[cx(x) for x in row] for row in np.array(M)]


def turns(z):
    return round(float(np.angle(z) / (2 * np.pi)) % 1.0, 9) % 1.0


def null_space(A, tol=1e-9):
    _, s, vh = np.linalg.svd(A)
    r = int(sum(s > tol * max(1.0, s[0])))
    return vh[r:].conj().T, [round(float(x), 12) for x in s]


def units():
    names = TQ.units_of_parities()
    return names, [SR.QM[names[u]] for u in CT.PAR]


def on_D(phi, g):
    """a lift on D = H1(F2; rho_Q) in CT.basis(ZERO)'s H1 coordinates: z -> g^-1 (z o phi), as CT.on_V's blocks"""
    assert CT.u_after(ZERO, phi) == ZERO
    gi = np.linalg.inv(SR.qmat(g))
    B = CT.basis(ZERO)
    cols = []
    for k in (2, 3):
        e = B[:, k]
        img = np.concatenate([gi @ SR.cocycle_on_word([e[0:2], e[2:4]], ZERO, phi[x]) for x in (1, 2)])
        cols.append(np.linalg.solve(B, img)[2:4])
    return np.array(cols).T


def to_D(c, p, U):
    """Phi_p on the class with H1 coordinates c in block p: the cocycle u_p^-1 z, in CT.basis(ZERO)'s H1 coordinates"""
    z = CT.basis(CT.PAR[p])[:, 2:4] @ c
    Ui = np.linalg.inv(U[p])
    w = np.concatenate([Ui @ z[0:2], Ui @ z[2:4]])
    return np.linalg.solve(CT.basis(ZERO), w)[2:4]


def block_lines(C):
    """for each parity block p: the coefficient vector x_p with C x_p inside block p (None unless a line), and the
    singular values of C's rows off the block"""
    xs, sv, dims = [], [], []
    for p in range(3):
        off = [r for r in range(6) if r // 2 != p]
        N, s = null_space(C[off, :])
        dims.append(int(N.shape[1]))
        sv.append(s)
        xs.append(N[:, 0] if N.shape[1] == 1 else None)
    return xs, sv, dims


def images_in_D(C, xs, U):
    return [to_D(C[2 * p:2 * p + 2, :] @ xs[p], p, U) if xs[p] is not None else np.zeros(2, dtype=complex)
            for p in range(3)]


def lifts_of(m):
    return [(g, CT.on_V(CP.AUT[m], g), on_D(CP.AUT[m], g)) for g in CP.extend(CP.AUT[m])]


def eigen_on(A, v):
    """(the eigenvalue of A on the line of the unit vector v, the residual |A v - c v|)"""
    w = A @ v
    c = complex(v.conj() @ w)
    return c, float(np.linalg.norm(w - c * v))


def on_T(Ct, X):
    Y = np.linalg.lstsq(Ct, X @ Ct, rcond=None)[0]
    return Y, float(np.linalg.norm(Ct @ Y - X @ Ct))


def signed_perm(P, tol=TOL):
    """P is a signed permutation matrix: entries 0 or +-1, one nonzero in each row and column"""
    R = np.round(np.real(P))
    if not (np.allclose(P, R, atol=tol) and set(np.unique(np.abs(R)).tolist()) <= {0.0, 1.0}):
        return False
    return bool(all(np.sum(np.abs(R), axis=0) == 1) and all(np.sum(np.abs(R), axis=1) == 1))


def conj_units(G, U):
    """P with G^-1 u_p G = sum_q P_qp u_q (tr(u_q u_p) = -2 delta_qp), and whether the expansion is exact"""
    Gi = np.linalg.inv(G)
    P = np.zeros((3, 3), dtype=complex)
    exact = True
    for p in range(3):
        X = Gi @ U[p] @ G
        for q in range(3):
            P[q, p] = -np.trace(U[q] @ X) / 2
        exact &= close(sum(P[q, p] * U[q] for q in range(3)), X)
    return P, bool(exact)


def perm_sign(S):
    perm = [int(np.argmax(np.abs(S[:, i]))) for i in range(3)]
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return 1 if inv % 2 == 0 else -1


def normal_form(Y):
    """(z, S) with Y = z S, S a signed permutation of determinant 1, or None"""
    nz = np.argwhere(np.abs(Y) > 1e-6)
    if not len(nz):
        return None
    z = complex(Y[tuple(nz[0])])
    S = Y / z
    if not signed_perm(S):
        return None
    S = np.round(np.real(S))
    if round(np.linalg.det(S)) == -1:
        S, z = -S, -z
    return z, S


def key3(M):
    return tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 6))


def closure3(gens, cap=4096):
    key = key3
    G = {key(np.eye(3)): np.eye(3, dtype=complex)}
    fr = list(G.values())
    while fr and len(G) <= cap:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                k = key(B)
                if k not in G:
                    G[k] = B
                    nx.append(B)
        fr = nx
    return list(G.values())


def as_matrix(w):
    """a vector of rho_Q (x) M in block layout (block p = the coefficient of e_p) as the 2 x 3 matrix [w_1 w_2 w_3]"""
    return np.array([w[2 * p:2 * p + 2] for p in range(3)]).T


def rank(M, tol=1e-9):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(sum(s > tol * max(1.0, s[0])))


# ------------------------------------------------------------------------------------------------------------- controls
def controls(U):
    Psi = np.zeros((6, 6), dtype=complex)
    for p in range(3):
        Psi[2 * p:2 * p + 2, 2 * p:2 * p + 2] = U[p]
    Pi = np.linalg.inv(Psi)
    hol = {x: close(Pi @ SC.W_of([x]) @ Psi, np.kron(np.eye(3), SR.RHO[x])) for x in (1, 2)}
    fact = {}
    for m in ("L", "R"):
        for i, g in enumerate(CP.extend(CP.AUT[m])):
            A = Pi @ SC.blocks_action(CP.AUT[m], g) @ Psi
            G = SR.qmat(g)
            S = np.array([[np.trace(G.conj().T @ A[2 * r:2 * r + 2, 2 * c:2 * c + 2]) / 2 for c in range(3)]
                          for r in range(3)])
            fact["%s, lift %d" % (m, i)] = bool(close(A, np.kron(S, G)) and signed_perm(S))
    return Psi, Pi, {"Psi^-1 W(a) Psi = 1 (x) rho_Q(a)": hol[1], "Psi^-1 W(b) Psi = 1 (x) rho_Q(b)": hol[2],
                     "every lift of L and R on the six is S (x) g, S a signed permutation": all(fact.values()),
                     "by lift": fact}


# ------------------------------------------------------------------------------------------------------------------ M1
def M1(C, U):
    xs, sv, dims = block_lines(C)
    ell = images_in_D(C, xs, U)
    L = np.array(ell).T
    s = np.linalg.svd(L, compute_uv=False)
    n0 = np.linalg.norm(ell[0])
    lhat = ell[0] / n0 if n0 > 1e-12 else np.array([1, 0], dtype=complex)
    G0 = H.block_gram(ZERO)
    q = complex(lhat.conj() @ G0 @ lhat)
    perp, _ = null_space((G0 @ lhat).conj()[None, :])
    lperp = perp[:, 0] / np.linalg.norm(perp[:, 0])
    qperp = complex(lperp.conj() @ G0 @ lperp)
    inv, chars = {}, {}
    for m in ("L", "R"):
        for i, (g, _, A) in enumerate(lifts_of(m)):
            c, r = eigen_on(A, lhat)
            c2, r2 = eigen_on(A, lperp)
            inv["%s, lift %d" % (m, i)] = bool(r < TOL and r2 < TOL)
            chars["%s, lift %d" % (m, i)] = {"on l (turns)": turns(c), "on l's complement (turns)": turns(c2)}
    out = {"the dimension of T's intersection with each parity block": dims,
           "the singular values of T's rows off each block": sv,
           "Phi_p of the three lines (D's H1 coordinates)": [[cx(x) for x in v] for v in ell],
           "the singular values of the 2 x 3 matrix of the three images": [round(float(x), 12) for x in s],
           "the three images span one line": bool(s[1] < 1e-9 * s[0]),
           "Q(l^, l^)": cx(q), "Q on l's Q-orthogonal complement": cx(qperp),
           "l and its complement are invariant under every lift of L and R": bool(all(inv.values())),
           "the lifts' eigenvalues on l and on its complement": chars,
           "the Gram matrix of Q on D": mat(G0)}
    ok = (dims == [1, 1, 1] and out["the three images span one line"] and q.real > 1e-9 and abs(q.imag) < TOL
          and out["l and its complement are invariant under every lift of L and R"] and qperp.real < -1e-9)
    return out, bool(ok), xs, ell, lhat, lperp, q


# ------------------------------------------------------------------------------------------------------------------ M2
def t_basis(C, xs, ell, lhat):
    cols = []
    for p in range(3):
        beta = complex(lhat.conj() @ ell[p])
        alpha = 1 / beta if abs(beta) > 1e-12 else 1.0
        cols.append(alpha * (C @ xs[p]) if xs[p] is not None else np.zeros(6, dtype=complex))
    return np.array(cols).T


def M2(Ct, U, lhat):
    sanity = all(close(to_D(Ct[2 * p:2 * p + 2, p], p, U), lhat) for p in range(3))
    moves, extra, gens = {}, {}, []
    for m in ("L", "R"):
        for i, (g, X, A) in enumerate(lifts_of(m)):
            Y, res = on_T(Ct, X)
            c, r = eigen_on(A, lhat)
            P = Y / c
            Pu, exact = conj_units(SR.qmat(g), U)
            nm = "%s, lift %d" % (m, i)
            moves[nm] = {"T invariant (residual)": res, "c on l (turns)": turns(c), "Y / c": mat(P),
                         "Y / c is a signed permutation": signed_perm(P), "det(Y / c)": cx(np.linalg.det(P))}
            extra[nm] = bool(exact and close(P, Pu))
            gens.append(Y)
    group = closure3(gens)
    keys = {key3(Y) for Y in group}
    inner = {}
    for nm, (phi, gen) in INNER.items():
        for i, g in enumerate(CP.extend(phi)):
            X, A = CT.on_V(phi, g), on_D(phi, g)
            Y, res = on_T(Ct, X)
            eps, r = eigen_on(A, lhat)
            signs = np.diag([SR.char_val(u, gen) for u in CT.PAR])
            Pu, exact = conj_units(SR.qmat(g), U)
            lab = "%s, lift %d" % (nm, i)
            inner[lab] = {"T invariant (residual)": res, "on D": mat(A), "its sign on l": cx(eps),
                          "the parity signs": [cx(x) for x in np.diag(signs)], "Y": mat(Y),
                          "Y lies in the group of L and R": key3(Y) in keys,
                          "Y = sign * parity signs": bool(abs(abs(eps) - 1) < TOL and abs(eps.imag) < TOL
                                                          and close(Y, eps * signs) and close(A, eps * np.eye(2)))}
            extra[lab] = bool(exact and close(Y / eps, Pu))
    forms = [normal_form(Y) for Y in group]
    good = [f is not None and abs(f[0] ** 8 - 1) < TOL and abs(f[0] ** 4 - perm_sign(f[1])) < TOL for f in forms]
    out = {"Phi_p(t_p) = l^ for each p": bool(sanity), "the lifts of L and R on T": moves,
           "the lifts of the inner automorphisms on T": inner,
           "the group the lifts of L and R generate on T: elements": len(group),
           "every element is z S with S a rotation of the cube, z^8 = 1, z^4 = sgn S": bool(all(good))}
    ok = (sanity and all(v["Y / c is a signed permutation"] and v["T invariant (residual)"] < TOL
                         for v in moves.values())
          and all(v["Y = sign * parity signs"] and v["Y lies in the group of L and R"]
                  and v["T invariant (residual)"] < TOL for v in inner.values())
          and len(group) == 96 and all(good))
    return out, bool(ok), extra


# ------------------------------------------------------------------------------------------------------------------ M3
def M3(Ct, q):
    Gram = Ct.conj().T @ H.gram_V() @ Ct
    ok = close(Gram, q * np.eye(3)) and q.real > 1e-9
    return {"the Gram matrix of Q on T in the basis t_p": mat(Gram), "Q(l^, l^)": cx(q)}, bool(ok)


# ------------------------------------------------------------------------------------------------------------------ M4
def M4(Pi, rng):
    conds = {"0": np.zeros((6, 0)), "V2": EC.Q2, "V4": EC.Q4, "L6": np.eye(6)}
    out = {}
    for name, B in conds.items():
        W = Pi @ B
        d = W.shape[1]
        cols = np.hstack([as_matrix(W[:, k]) for k in range(d)]) if d else np.zeros((2, 0))
        rows = np.hstack([as_matrix(W[:, k]).T for k in range(d)]) if d else np.zeros((3, 0))
        dx, dy = rank(cols), rank(rows)
        gen = [rank(as_matrix(W @ (rng.normal(size=d) + 1j * rng.normal(size=d)))) for _ in range(5)] if d else []
        out[name] = {"dimension": d, "dim X_W (the columns' span in C^2)": dx, "dim Y_W (the rows' span in M)": dy,
                     "a product X (x) Y": bool(d == dx * dy), "flavour-blind, X (x) M": bool(d == 3 * dx),
                     "the ranks of five random vectors": gen}
    ok = (all(out[n]["a product X (x) Y"] and out[n]["flavour-blind, X (x) M"] for n in ("0", "L6"))
          and all(not out[n]["a product X (x) Y"] and out[n]["the ranks of five random vectors"] == [2] * 5
                  for n in ("V2", "V4")))
    return out, bool(ok)


def E3(Pi, rng):
    W = Pi @ EC.Q2
    ratios = []
    for _ in range(200):
        s = np.linalg.svd(as_matrix(W @ (rng.normal(size=2) + 1j * rng.normal(size=2))), compute_uv=False)
        ratios.append(float(s[0] / s[1]))
    return {"s1 / s2 over 200 random vectors of V2: min, max": [round(min(ratios), 12), round(max(ratios), 12)]}


def E4(m4):
    C, K = EC.frame()
    (_, gL, gR) = H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    tab = EC.table(R)
    f = {c: round(tab[c]["1"] - tab[c]["0"], 9) for c in EC.CONDITIONS}
    blind = {c: m4[c]["flavour-blind, X (x) M"] for c in EC.CONDITIONS}
    return {"the fibre index f = I(n = 1) - I(n = 0), by condition": f, "flavour-blind, by condition": blind,
            "|f| = 3 exactly at the flavour-blind conditions": bool(
                all((abs(abs(f[c]) - 3) < 1e-9) == blind[c] for c in EC.CONDITIONS))}


def main():
    rng = np.random.default_rng(49)
    names, U = units()
    named, order = H.triplets()
    C = named["T"]
    Psi, Pi, ctl = controls(U)
    m1, ok1, xs, ell, lhat, lperp, q = M1(C, U)
    Ct = t_basis(C, xs, ell, lhat)
    m2, ok2, e1 = M2(Ct, U, lhat)
    m3, ok3 = M3(Ct, q)
    m4, ok4 = M4(Pi, rng)
    xb, _, dimb = block_lines(named["T-bar"])
    ellb = images_in_D(named["T-bar"], xb, U)
    e2 = {"the dimension of T-bar's intersection with each block": dimb,
          "each image lies on l's Q-orthogonal complement": bool(
              dimb == [1, 1, 1] and all(abs(complex(lhat.conj() @ H.block_gram(ZERO) @ v)) < TOL
                                        and np.linalg.norm(v) > 1e-9 for v in ellb))}
    e3 = E3(Pi, rng)
    e4 = E4(m4)
    control_ok = bool(ctl["Psi^-1 W(a) Psi = 1 (x) rho_Q(a)"] and ctl["Psi^-1 W(b) Psi = 1 (x) rho_Q(b)"]
                      and ctl["every lift of L and R on the six is S (x) g, S a signed permutation"])
    checks = {
        "M1: T meets each parity block in a line; Phi_p sends the three to one line l of D; l is invariant under every "
        "lift and Q-positive, its complement Q-negative": ok1,
        "M2: the lifts of L and R act on T as c (on l) times a signed permutation; the inner automorphisms' lifts as a "
        "sign times the parity signs; the group on T is W42's z S, 96 elements": ok2,
        "M3: the Hodge-Riemann form on T in the basis t_p is Q(l^, l^) times the identity": ok3,
        "M4: V2 and V4 are entangled (generic rank 2; not X (x) Y); 0 and L6 are products and flavour-blind": ok4,
    }
    out = {"status": "W49: the generations are a multiplicity, three or split (the rule first)",
           "the unit of each parity (W28)": {str(u): names[u] for u in CT.PAR},
           "the order of the moves' group on V (W21)": order,
           "controls": ctl, "every control holds": control_ok,
           "M1: one line": m1, "M2: the lifts in the basis t_p": m2, "M3: the Hodge-Riemann form on T": m3,
           "M4: the puncture conditions in rho_Q (x) M": m4,
           "extra read-outs (not predicted)": {
               "E1: the signed permutation is the lift's conjugation of the three units, for every lift": bool(
                   all(e1.values())),
               "E1: by lift": e1, "E2: T-bar": e2, "E3: V2's singular values": e3, "E4: the fibre index by type": e4},
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("every control holds:", control_ok)
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
