#!/usr/bin/env python3
"""W29 of the weave: THE Z6 TWIST-EATER (QUBIT x QUTRIT) IN E8. The rule is W29_RULE.md, committed before this ran
(37441028). The object is chosen, not forced (whether anything forces a qutrit flux is step 4 of the plan, open), so
every claim is conditional: if the shared fibre carried the Z6 flux.

  Z1 the group H6 = <A, B>, A = lambda C, B = lambda S in SU(6): order, centre, commutator, irreducibility, type; the
     Chinese-remainder factorisation into the qubit's Pauli pair and a qutrit pair; the lemma;
  Z2 centralisers in E8 by W25's chi248 (H6; the weave's qubit; the qutrit; the flux);
  Z3 the matter: the 6, Lambda^2 6, Lambda^3 6 and the adjoint under H6, with the qubit's and the qutrit's labels, and
     the multiplicities of each type in the 248 by characters;
  Z4 the flux as exp(2 pi i Y), and the orientation (the moves keep zeta; the swap has no intertwiner);
  Z5 the moves at the puncture: the lifts, their commutant on the 6 and on Lambda^2 6, the index sets;
  Z6 the anomalies (SU(3)^3; the doublet parity) under the moves and under locality;
  Z7 the verdict.

    python3 the_z6_twist_eater.py   ->  the_z6_twist_eater.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_six_dimensional_census as SC  # noqa: E402  (commutants)
import the_self_conjugate_weave as SW  # noqa: E402  (chi248, closure, Frobenius-Schur, averages)
import the_three_routes_and_the_qubit as TQ  # noqa: E402  (null spaces, index sets)

ZETA = np.exp(2j * np.pi / 6)
OMEGA = np.exp(2j * np.pi / 3)
LAM = np.exp(1j * np.pi / 6)
C6 = np.diag([ZETA ** k for k in range(6)])
S6 = np.zeros((6, 6), dtype=complex)
for _k in range(6):
    S6[(_k + 1) % 6, _k] = 1
A = LAM * C6
B = LAM * S6
I2, I3, I6 = np.eye(2, dtype=complex), np.eye(3, dtype=complex), np.eye(6, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
C3 = np.diag([OMEGA ** j for j in range(3)])
S3 = np.zeros((3, 3), dtype=complex)
for _j in range(3):
    S3[(_j + 1) % 3, _j] = 1
inv = np.linalg.inv


def close(P, Q, tol=1e-8):
    return bool(np.allclose(P, Q, atol=tol))


_CACHE = {}


def compound(M, k):
    """the k-th compound matrix (Lambda^k M), rows and columns the k-subsets in lexicographic order (cached by object
    for the group elements, which are averaged over several times)"""
    key = (id(M), k)
    if key in _CACHE and _CACHE[key][0] is M:
        return _CACHE[key][1]
    out = _compound(M, k)
    _CACHE[key] = (M, out)
    return out


def _compound(M, k):
    n = M.shape[0]
    subs = list(itertools.combinations(range(n), k))
    out = np.zeros((len(subs), len(subs)), dtype=complex)
    for a, I_ in enumerate(subs):
        for b, J_ in enumerate(subs):
            out[a, b] = np.linalg.det(M[np.ix_(I_, J_)])
    return out


def nullspace(M, tol=1e-9):
    """the null space of M; the thin SVD for tall M (its vh is already n x n), the full one only for wide M"""
    _, s, vh = np.linalg.svd(M, full_matrices=M.shape[0] < M.shape[1])
    rank = int(sum(s > tol))
    return vh[rank:].conj().T


def components(ops, n, seed=29):
    """the isotypic components of the algebra the operators generate on C^n: [(Q, d, m)], Q an orthonormal basis of
    the component, d the irreducible's dimension, m its multiplicity"""
    k, Bs = SC.commutant(ops, n)
    if k == 1:
        return [(np.eye(n, dtype=complex), n, 1)]
    blocks = [np.column_stack([(Bj @ Bk - Bk @ Bj).flatten() for Bj in Bs]) for Bk in Bs]
    N_ = nullspace(np.vstack(blocks))
    centre = [sum(c[j] * Bs[j] for j in range(k)) for c in N_.T]
    rng = np.random.default_rng(seed)
    Zc = sum(complex(rng.normal(), rng.normal()) * Cc for Cc in centre)
    ev, vec = np.linalg.eig(Zc)
    groups = []
    for i, e in enumerate(ev):
        for gr in groups:
            if abs(gr[0] - e) < 1e-6:
                gr[1].append(i)
                break
        else:
            groups.append([e, [i]])
    out = []
    for _, idx in groups:
        Q, _ = np.linalg.qr(vec[:, idx])
        kW = SC.commutant([Q.conj().T @ M @ Q for M in ops], len(idx))[0]
        m = int(round(kW ** 0.5))
        out.append((Q, len(idx) // m, m))
    return out


def scalar_on(Q, M):
    """the scalar by which M acts on the span of Q (None if it is not a scalar there)"""
    R = Q.conj().T @ M @ Q
    s = np.trace(R) / R.shape[0]
    return complex(s) if close(R, s * np.eye(R.shape[0]), 1e-7) else None


def root_label(s, n):
    """the exponent e with s = exp(2 pi i e / n), or None"""
    if s is None:
        return None
    e = np.angle(s) / (2 * np.pi) * n
    r = int(round(e)) % n
    return r if abs(e - round(e)) < 1e-6 and abs(abs(s) - 1) < 1e-6 else None


def intertwiners(phiA, phiB):
    """the solutions U of U A = phi(A) U, U B = phi(B) U"""
    M = np.vstack([np.kron(A.T, I6) - np.kron(I6, phiA), np.kron(B.T, I6) - np.kron(I6, phiB)])
    N_ = nullspace(M)
    return [N_[:, i].reshape(6, 6, order="F") for i in range(N_.shape[1])]


def subset_sums(structure):
    return sorted({sum(k * d for k, (d, _) in zip(ks, structure))
                   for ks in itertools.product(*[range(m + 1) for _, m in structure])})


def run():
    res = {"rule": "W29_RULE.md (committed 37441028 before this ran)",
           "the object": "chosen, not forced: every claim is conditional on the shared fibre carrying the Z6 flux"}
    # ---------------------------------------------------------------------------------------------------------- Z1
    H = SW.closure([A, B], 6, cap=1000)
    comm = A @ B @ inv(A) @ inv(B)
    scal = [h for h in H if close(h, h[0, 0] * I6)]
    perm = np.zeros((6, 6))
    for k in range(6):
        perm[(k % 2) * 3 + (k % 3), k] = 1
    crt_C = close(perm @ C6 @ perm.T, np.kron(Z, inv(C3)))
    crt_S = close(perm @ S6 @ perm.T, np.kron(X, S3))
    A3, B3 = np.linalg.matrix_power(A, 3), np.linalg.matrix_power(B, 3)
    qubit = close(perm @ A3 @ perm.T, np.kron(1j * Z, I3)) and close(perm @ B3 @ perm.T, np.kron(1j * X, I3))
    lemma = all(sp.simplify(sp.exp(2 * sp.pi * sp.I * w / 6) - 1) != 0 for w in range(1, 6))
    res["Z1 the group"] = {
        "det A, det B": [round(float(np.real(np.linalg.det(A))), 9), round(float(np.real(np.linalg.det(B))), 9)],
        "order of H6": len(H),
        "its scalars (the centre)": len(scal),
        "A B A^-1 B^-1 = zeta 1": close(comm, ZETA * I6),
        "commutant on C^6 (1 = irreducible)": SC.commutant([A, B], 6)[0],
        "Frobenius-Schur indicator of the 6 (0 = complex)": SW.fs(H),
        "Chinese remainder: C = Z (x) C3^-1 and S = X (x) S3 exactly": bool(crt_C and crt_S),
        "A^3, B^3 = iZ (x) 1, iX (x) 1: the weave's qubit units": bool(qubit),
        "lemma: zeta^w != 1 for w = 1..5, so an invariant subspace has dimension 0 or 6 (exact)": bool(lemma),
        "so no U(1) of SU(6)' commutes with H6 (Schur)": bool(lemma and SC.commutant([A, B], 6)[0] == 1)}
    # ---------------------------------------------------------------------------------------------------------- Z2
    Q8 = SW.closure([np.kron(1j * Z, I3), np.kron(1j * Y, I3)], 6)
    H3 = SW.closure([np.kron(I2, C3), np.kron(I2, S3)], 6)
    F6 = SW.closure([ZETA * I6], 6)
    cent = {"H6 (qubit x qutrit)": [len(H), SW.average(H)[0]],
            "the weave's qubit Q8 (rho_Q (x) 1_3)": [len(Q8), SW.average(Q8)[0]],
            "the qutrit alone (1_2 (x) H3)": [len(H3), SW.average(H3)[0]],
            "the flux <zeta 1> alone": [len(F6), SW.average(F6)[0]]}
    res["Z2 centralisers in E8 [order, dimension]"] = cent
    # ---------------------------------------------------------------------------------------------------------- Z3
    m6 = SW.average(H, lambda h: np.trace(h))
    m6b = SW.average(H, lambda h: np.conj(np.trace(h)))
    L2 = [compound(A, 2), compound(B, 2)]
    comp2 = components(L2, 15)
    rows2 = []
    labels2 = {}
    for Q, d, m in comp2:
        sA = scalar_on(Q, np.linalg.matrix_power(L2[0], 3))
        sB = scalar_on(Q, np.linalg.matrix_power(L2[1], 3))
        lab = (int(round(sA.real)) if sA is not None else None, int(round(sB.real)) if sB is not None else None)

        def chi(h, Q=Q, m=m):
            return np.trace(Q.conj().T @ compound(h, 2) @ Q) / m

        mult = SW.average(H, chi)[0]
        rows2.append({"dimension": d, "multiplicity in the 15": m, "signs of A^3, B^3 (iZ, iX on the qubit)": list(lab),
                      "multiplicity in the 248 (by characters)": mult})
        labels2[lab] = m
    parity_of = {(1, -1): "Z: the weave's (0, 1/2), kernel a", (-1, 1): "X: the weave's (1/2, 1/2), kernel ab",
                 (-1, -1): "Y: the weave's (1/2, 0), kernel b"}
    single2 = sorted(k for k, v in labels2.items() if v == 1)
    res["Z3 the 6"] = {"multiplicity of the 6 in the 248": m6[0], "of the 6-bar": m6b[0],
                       "so its multiplicity space has dimension 6, (3, 2)": bool(m6[0] == 6.0 and m6b[0] == 6.0)}
    res["Z3 the 15 = Lambda^2 6"] = {
        "types": rows2,
        "isotypic structure [(dimension, multiplicity)]": sorted((d, m) for _, d, m in comp2),
        "the doubly occurring type carries the qubit's trivial character": labels2.get((1, 1)) == 2,
        "the three single types carry the three non-trivial characters (the parities)": {
            str(k): parity_of.get(k) for k in single2},
        "as predicted": bool(sorted((d, m) for _, d, m in comp2) == [(3, 1), (3, 1), (3, 1), (3, 2)]
                             and labels2.get((1, 1)) == 2 and single2 == sorted(parity_of))}
    L3 = [compound(A, 3), compound(B, 3)]
    comp3 = components(L3, 20)
    rows3 = []
    labs3 = {}
    for Q, d, m in comp3:
        sA = scalar_on(Q, np.linalg.matrix_power(L3[0], 2))
        sB = scalar_on(Q, np.linalg.matrix_power(L3[1], 2))
        # A^2 = zeta C^2 and C^2 = 1 (x) C3 under the remainder ordering, so Lambda^3(A^2) = zeta^3 Lambda^3(C^2)
        la = root_label(sA / ZETA ** 3 if sA is not None else None, 3)
        lb = root_label(sB / ZETA ** 3 if sB is not None else None, 3)

        def chi3(h, Q=Q, m=m):
            return np.trace(Q.conj().T @ compound(h, 3) @ Q) / m

        rows3.append({"dimension": d, "multiplicity in the 20": m, "qutrit label (a, b) mod 3": [la, lb],
                      "multiplicity in the 248 (by characters)": SW.average(H, chi3)[0]})
        labs3[(la, lb)] = m
    nonzero = sorted(k for k in labs3 if k != (0, 0))
    pairs = {frozenset({k, ((-k[0]) % 3, (-k[1]) % 3)}) for k in nonzero}
    res["Z3 the 20 = Lambda^3 6"] = {
        "types": rows3,
        "isotypic structure [(dimension, multiplicity)]": sorted((d, m) for _, d, m in comp3),
        "the doubly occurring type is qutrit-blind": labs3.get((0, 0)) == 2,
        "the eight single types carry the eight non-zero qutrit labels": bool(len(nonzero) == 8 and all(
            labs3[k] == 1 for k in nonzero)),
        "in conjugate pairs: the four lines of P^1(F3)": len(pairs)}
    # the adjoint factors through H6 / centre = Z6 x Z6 (abelian): its two generators commute, and its characters are
    # the joint eigenvalue pairs (read from a generic combination of the two)
    ad = [np.kron(A, A.conj()), np.kron(B, B.conj())]
    commute = close(ad[0] @ ad[1], ad[1] @ ad[0])
    _, V = np.linalg.eig(ad[0] + np.pi * ad[1])
    Vi = inv(V)
    pairs_ad = {(root_label((Vi @ ad[0] @ V)[i, i], 6), root_label((Vi @ ad[1] @ V)[i, i], 6)) for i in range(36)}
    diag_ok = close(Vi @ ad[0] @ V, np.diag(np.diag(Vi @ ad[0] @ V)), 1e-7) and close(
        Vi @ ad[1] @ V, np.diag(np.diag(Vi @ ad[1] @ V)), 1e-7)
    res["Z3 the adjoint (End C^6 = 1 + 35)"] = {
        "the two generators commute (the adjoint is abelian)": bool(commute),
        "jointly diagonal in one basis": bool(diag_ok),
        "number of distinct characters (pairs of sixth-root exponents)": len(pairs_ad),
        "36 distinct characters, each once (so the 35 are the non-trivial ones)": bool(
            commute and diag_ok and len(pairs_ad) == 36 and None not in {x for pr in pairs_ad for x in pr})}
    # ---------------------------------------------------------------------------------------------------------- Z4
    yexact = sp.simplify(sp.exp(2 * sp.pi * sp.I * sp.Rational(1, 6)) - sp.exp(2 * sp.pi * sp.I * sp.Rational(-5, 6)))
    Ygen = np.diag([1 / 6] * 5 + [-5 / 6])
    moves = {"L": (A, A @ B), "R": (A @ B, B), "-I": (inv(A), inv(B)), "P": (B, A)}
    z4 = {}
    for nm, (pa, pb) in moves.items():
        cm = pa @ pb @ inv(pa) @ inv(pb)
        sols = intertwiners(pa, pb)
        z4[nm] = {"commutator of the image pair": "zeta" if close(cm, ZETA * I6) else (
            "zeta-bar" if close(cm, ZETA.conjugate() * I6) else "other"),
            "intertwiners U (dimension of the solution space)": len(sols)}
    res["Z4 the flux and the orientation"] = {
        "exp(2 pi i diag(1/6 x5, -5/6)) = zeta 1 (exact)": bool(yexact == 0 and close(
            np.diag(np.exp(2j * np.pi * np.diag(Ygen))), ZETA * I6)),
        "reading: with the 6 = 5_{1/6} + 1_{-5/6} under SU(5)' x U(1)_Y, the flux is exp(2 pi i Y)": "READING",
        "the moves": z4,
        "L, R and -I keep zeta and have one intertwiner each; the swap P sends zeta to zeta-bar and has none": bool(
            all(z4[m]["commutator of the image pair"] == "zeta" and z4[m][
                "intertwiners U (dimension of the solution space)"] == 1 for m in ("L", "R", "-I"))
            and z4["P"]["commutator of the image pair"] == "zeta-bar"
            and z4["P"]["intertwiners U (dimension of the solution space)"] == 0)}
    # ---------------------------------------------------------------------------------------------------------- Z5
    lifts = {m: intertwiners(*moves[m]) for m in ("L", "R", "-I")}
    if not all(lifts.values()):
        res["Z5 the moves at the puncture"] = {"a move has no lift on C^6": {m: len(v) for m, v in lifts.items()}}
        return res
    UL, UR, UI = lifts["L"][0], lifts["R"][0], lifts["-I"][0]
    par = np.zeros((6, 6))
    for k in range(6):
        par[(-k) % 6, k] = 1
    ui_is_parity = close(UI / UI[0, 0], par)
    kL, _ = SC.commutant([UL, UR], 6)
    st6 = sorted((d, m) for _, d, m in components([UL, UR], 6))
    Pplus = (I6 + par) / 2
    Pminus = (I6 - par) / 2
    pieces = all(close(U @ P, P @ U) for U in (UL, UR) for P in (Pplus, Pminus))
    D1 = subset_sums(st6)
    D1loc = [0, 6]
    L2lifts = [compound(UL, 2), compound(UR, 2)]
    st15 = sorted((d, m) for _, d, m in components(L2lifts, 15))
    D2 = subset_sums(st15)
    D2loc = [0, 15]
    res["Z5 the moves at the puncture"] = {
        "the lift of -I is the parity |k> -> |-k> up to a scalar": bool(ui_is_parity),
        "commutant of the lifts of L and R on the 6": kL,
        "their isotypic structure on the 6": st6,
        "the pieces are the parity's eigenspaces (dimensions 4 and 2)": bool(
            pieces and round(np.trace(Pplus).real) == 4 and round(np.trace(Pminus).real) == 2),
        "the 6-sector's index (-1 + d1): under the moves": [d - 1 for d in D1],
        "... under locality (the flux is central: U(6))": [d - 1 for d in D1loc],
        "the smooth E8 condition (traceless weights: d1 = 1, index 0) is move-invariant": bool(1 in D1),
        "the lifts' isotypic structure on Lambda^2 C^6 (the 15-sector)": st15,
        "the 15-sector's index (-5 + d2): under the moves": [d - 5 for d in D2],
        "... under locality": [d - 5 for d in D2loc]}
    # ---------------------------------------------------------------------------------------------------------- Z6
    def table(D1_, D2_):
        rows = []
        for d1 in D1_:
            for d2 in D2_:
                n32, n31 = d1 - 1, d2 - 5
                rows.append({"n(3,2)": n32, "n(3b,1)": n31, "SU(3)^3": 2 * n32 - n31})
        free = sorted({(r["n(3,2)"], r["n(3b,1)"]) for r in rows if r["SU(3)^3"] == 0})
        return rows, free

    rows_m, free_m = table(D1, D2)
    rows_l, free_l = table(D1loc, D2loc)
    res["Z6 the anomalies"] = {
        "SU(3)^3 = 2 n(3,2) - n(3b,1) = 3 + 2 d1 - d2": "the formula",
        "under the moves: the SU(3)^3-free (n(3,2), n(3b,1))": [list(f) for f in free_m],
        "... each has n(3b,1) = 2 n(3,2) (the Standard Model's ratio)": bool(all(b == 2 * a for a, b in free_m)),
        "... every n(3,2) the moves allow has a free completion": sorted({a for a, _ in free_m}) == [d - 1 for d in D1],
        "under locality: the four rows": rows_l,
        "under locality: the free ones": [list(f) for f in free_l],
        "the coloured doublets 3|n(3,2)| are odd for every move-invariant condition": bool(
            all((3 * abs(d - 1)) % 2 == 1 for d in D1)),
        "the doublet sector (1,2) (x) 20 is real, so its index is 0 (CPT): no chiral lepton doublets": "stated"}
    # ---------------------------------------------------------------------------------------------------------- Z7
    three_moves = 3 in [d - 1 for d in D1]
    res["Z7 the verdict"] = {
        "centraliser exactly SU(3) x SU(2) (11)": bool(cent["H6 (qubit x qutrit)"][1] == 11.0),
        "the quark doublets complex (the 6 has indicator 0, multiplicity 6)": bool(
            res["Z1 the group"]["Frobenius-Schur indicator of the 6 (0 = complex)"] == 0.0 and m6[0] == 6.0),
        "the flux is exp(2 pi i Y) (exact identity; the reading through SU(5)')": bool(
            res["Z4 the flux and the orientation"]["exp(2 pi i diag(1/6 x5, -5/6)) = zeta 1 (exact)"]),
        "(a) U(1)_Y broken (the lemma)": bool(res["Z1 the group"]["so no U(1) of SU(6)' commutes with H6 (Schur)"]),
        "(b) three allowed by the moves but not forced; locality with SU(3)^3 gives": [list(f) for f in free_l],
        "(b) three not forced": bool(three_moves and len([d for d in D1 if d - 1 != 3]) > 0
                                     and [5, 10] in [list(f) for f in free_l] and len(free_l) == 1),
        "(c) odd coloured doublets and no chiral leptons": bool(
            res["Z6 the anomalies"]["the coloured doublets 3|n(3,2)| are odd for every move-invariant condition"]),
        "(d) the flux is not forced": "step 4 of the plan, open; not computed here",
        "an echo, not a derivation": True}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_z6_twist_eater.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
