#!/usr/bin/env python3
"""W24 of the weave: THE SIX-DIMENSIONAL CENSUS. The owner's choice of 2026-10-08: is there a six-dimensional object the
weave forces, on which the heterotic dictionary (net generations = an index) applies? The rule is W24_RULE.md, committed
before this ran (d39778dd).

The candidates and what is read (exact where it can be: sympy, integers, fractions; the quaternion closures are numerical
on groups of at most 48 elements):
  A  the fibre's character variety X = C^3, (x, y, z) = (tr a, tr b, tr ab), with kappa = tr [a, b]:
     A1 every move acts by a polynomial map preserving kappa; the Jacobian determinants (L, R: +1; P: -1). Two routes
        for the maps: the record's table (the_common_point.TR) and traces of products of 2 x 2 matrices.
     A2 the points every move fixes.
     A3 the linear parts at the common point: their group, and its character at (S, L, SL) against W21's P (3').
     A4 the critical points of kappa, their Hessians, and the Euler characteristic of the level sets two ways.
  B  the local model at the common point:
     B1 each parity's fixed locus in X and on the Markov surface X_{-2};
     B2 the finite linear symmetries of X preserving kappa (signed permutations), and which moves give them;
     B3 the lifts to SU(2) of the parities, of A4 and of the moves' linear parts (orders; Du Val types by McKay);
     B4 the orbifold Euler numbers of E^3 / G for G = V4, A4, O, with and without discrete torsion.
  C  main's frame spaces: stated in the rule, nothing computed.
  D  the gauge side:
     D0 the moves' lifts on the six local solutions at the puncture: the commutant, the invariant subspaces and their
        indices; then with the parity grading added (the W22 audit);
     D1 the intertwiners chi_p (x) rho_Q = u rho_Q u^-1;
     D2, D3 the centraliser of W's holonomy Q8 in E8 and the multiplicities of its irreducibles in the 248, by
        characters, through two branchings (SU(3) x SU(2) x SU(6)' and G2 x F4).
  E  the verdict table against the criteria S1-S5.

    python3 the_six_dimensional_census.py   ->  the_six_dimensional_census.json beside it
"""
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the moves as automorphisms, 2O, the lifts of the common point)
import the_chiral_triplet as CT  # noqa: E402  (the parities as exponents of i on a, b; u_after)
import the_spin_room as SR  # noqa: E402  (quaternion units as 2 x 2 matrices)

x, y, z, t = sp.symbols("x y z t")
KAPPA = CP.KAPPA
INV = {"L": {1: [1], 2: [-1, 2]}, "R": {1: [1, -2], 2: [2]}}          # L^-1 and R^-1 as automorphisms


# ---------------------------------------------------------------------------------------------------------------- A
def trace_by_matrices(w):
    """tr of the word w (1 = a, 2 = b, negatives inverses) with A = [[x, -1], [1, 0]], B = [[0, t], [-1/t, y]], so that
    tr A = x, tr B = y, tr AB = t + 1/t =: z. Returned as a polynomial in x, y, z."""
    A = sp.Matrix([[x, -1], [1, 0]])
    B = sp.Matrix([[0, t], [-1 / t, y]])
    M = {1: A, 2: B, -1: A.inv(), -2: B.inv()}
    P = sp.eye(2)
    for g in w:
        P = P * M[g]
    f = sp.together(sp.expand(P.trace()))
    num, den = sp.fraction(f)
    # den is a power of t; the trace is symmetric under t -> 1/t; rewrite t^k + t^-k through z (Dickson polynomials)
    lau = sp.expand(num / den)
    poly = sp.Poly(sp.expand(lau * t ** 40), t)
    coeffs = {m[0] - 40: c for m, c in zip(poly.monoms(), poly.coeffs())}
    D = {0: sp.Integer(2), 1: z}
    for k in range(2, 41):
        D[k] = sp.expand(z * D[k - 1] - D[k - 2])
    out = coeffs.get(0, 0)
    for k in range(1, 41):
        ck, cmk = coeffs.get(k, 0), coeffs.get(-k, 0)
        assert sp.simplify(ck - cmk) == 0, "not symmetric in t"
        out += ck * D[k]
    return sp.expand(out)


def char_map(phi):
    """(tr phi(a), tr phi(b), tr phi(a)phi(b)) by matrices"""
    return (trace_by_matrices(phi[1]), trace_by_matrices(phi[2]), trace_by_matrices(CP.reduce(phi[1] + phi[2])))


def jac(F):
    return sp.Matrix([[sp.diff(f, v) for v in (x, y, z)] for f in F])


def cellA():
    res = {}
    maps = {}
    a1 = {}
    for m in ("L", "R", "P", "-I"):
        F = char_map(CP.AUT[m])
        same = all(sp.expand(F[i] - CP.TR[m][i]) == 0 for i in range(3))
        kap = sp.expand(KAPPA.subs({x: F[0], y: F[1], z: F[2]}, simultaneous=True) - KAPPA) == 0
        a1[m] = {"map (x, y, z) ->": [str(f) for f in F], "equals the record's table": bool(same),
                 "preserves kappa": bool(kap), "Jacobian determinant": str(sp.factor(jac(F).det()))}
        maps[m] = F
    res["A1 the moves on the character variety"] = a1
    res["A1 L and R preserve Omega = dx dy dz (Jacobian +1); P reverses it (-1)"] = bool(
        a1["L"]["Jacobian determinant"] == "1" and a1["R"]["Jacobian determinant"] == "1"
        and a1["P"]["Jacobian determinant"] == "-1")
    # A2: common fixed points of L, R (P and -I added after)
    eqs = [sp.expand(maps[m][i] - (x, y, z)[i]) for m in ("L", "R") for i in range(3)]
    sols = sp.solve(eqs, [x, y, z], dict=True)
    pts = sorted({(int(s[x]), int(s[y]), int(s[z])) for s in sols})
    res["A2 the points L and R both fix"] = [list(p) for p in pts]
    res["A2 ... and P fixes them too"] = all(maps["P"][0].subs({x: p[0], y: p[1], z: p[2]}) == p[0] and
                                             maps["P"][1].subs({x: p[0], y: p[1], z: p[2]}) == p[1] for p in pts)
    res["A2 kappa at them"] = {str(list(p)): int(KAPPA.subs({x: p[0], y: p[1], z: p[2]})) for p in pts}
    # A3: linear parts at the common point
    O0 = {x: 0, y: 0, z: 0}
    lin = {m: np.array(jac(maps[m]).subs(O0).tolist(), dtype=int) for m in ("L", "R", "P")}
    Linv = np.round(np.linalg.inv(lin["L"])).astype(int)
    Rinv = np.round(np.linalg.inv(lin["R"])).astype(int)
    grp = closure_int([lin["L"], lin["R"], Linv, Rinv])
    S0 = np.round(np.linalg.inv(lin["L"] @ Rinv @ lin["L"])).astype(int)
    res["A3 the linear parts of L and R at (0, 0, 0)"] = {"L": lin["L"].tolist(), "R": lin["R"].tolist()}
    res["A3 their group: order"] = len(grp)
    res["A3 every element a signed permutation of determinant 1 (a rotation of the cube)"] = all(
        is_signed_perm(g) and round(np.linalg.det(g)) == 1 for g in grp)
    trs = [int(np.trace(S0)), int(np.trace(lin["L"])), int(np.trace(S0 @ lin["L"]))]
    res["A3 character at (S, L, SL), S = (L R^-1 L)^-1"] = trs
    w21 = json.load(open(HERE / "the_holomorphic_triplet.json"))["read-out"]
    w21tr = w21["per braid-consistent lift choice"][0]["(4) traces of P at S, L, SL (a transposition, a 4-cycle, a 3-cycle)"]
    res["A3 W21's P at (S, L, SL)"] = w21tr
    res["A3 the same triplet (W21's flavour triplet is the tangent space at the common point)"] = bool(
        [float(v) for v in trs] == [float(v) for v in w21tr])
    # A4: critical points and Euler characteristics
    grad = [sp.diff(KAPPA, v) for v in (x, y, z)]
    crit = sp.solve(grad, [x, y, z], dict=True)
    crit_pts = sorted({(int(c[x]), int(c[y]), int(c[z])) for c in crit})
    H = sp.hessian(KAPPA, (x, y, z))
    res["A4 the critical points of kappa"] = {
        str(list(p)): {"kappa": int(KAPPA.subs({x: p[0], y: p[1], z: p[2]})),
                       "Hessian determinant (non-zero: a Morse point, an A1 node of its level)":
                           int(H.subs({x: p[0], y: p[1], z: p[2]}).det())} for p in crit_pts}
    # smoothness at infinity: F = w(x^2 + y^2 + z^2) - xyz - c w^3; at w = 0 the gradient vanishes nowhere on the surface
    w_, c_ = sp.symbols("w c")
    Fp = w_ * (x ** 2 + y ** 2 + z ** 2) - x * y * z - c_ * w_ ** 3
    eq_inf = [sp.diff(Fp, v).subs(w_, 0) for v in (x, y, z, w_)] + [Fp.subs(w_, 0)]
    G = sp.groebner(eq_inf, x, y, z, order="lex")
    # the ideal's only zero is x = y = z = 0 (no projective point): x^3, y^3, z^3 lie in it
    rad = all(G.contains(v ** 3) for v in (x, y, z))
    res["A4 the projective closures are smooth along the triangle at infinity, for every kappa"] = bool(rad)
    nodes = {}
    for p in crit_pts:
        k = int(KAPPA.subs({x: p[0], y: p[1], z: p[2]}))
        nodes[k] = nodes.get(k, 0) + 1
    chi_smooth_cubic, chi_triangle = 9, 3 * 2 - 3
    chis = {"generic": chi_smooth_cubic - chi_triangle}
    for k, n in sorted(nodes.items()):
        chis[str(k)] = chi_smooth_cubic - n - chi_triangle
    res["A4 nodes per singular level"] = {str(k): n for k, n in sorted(nodes.items())}
    res["A4 Euler characteristic of the level sets (9 - nodes - 3)"] = chis
    total = chis["generic"] * 1 + sum(chis[str(k)] - chis["generic"] for k in nodes)
    res["A4 chi(C^3) summed over the fibration by kappa (a consistency check: it must be 1)"] = total
    res["A4 consistent (no contribution from infinity)"] = bool(total == 1)
    res["A verdict"] = {
        "S1 forced": "yes: the fibre's characters, every move acting, no parameter",
        "S2 right kind": "yes: a complex threefold whose holomorphic volume form L and R preserve",
        "S3 a count exists": "no: contractible (chi = 1) and non-compact; the moves form an infinite group with a common "
                             "fixed point, so they do not act properly and give no compact quotient",
        "S4 a bundle with a hand": "no: the tangent bundle is trivial and no other bundle is forced",
        "passes": False}
    return res, maps, lin, grp


def closure_int(gens):
    seen = {tuple(np.eye(3, dtype=int).flatten())}
    out = [np.eye(3, dtype=int)]
    fr = list(out)
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                k = tuple(B.flatten())
                if k not in seen:
                    seen.add(k)
                    out.append(B)
                    nx.append(B)
        fr = nx
        assert len(out) <= 1000
    return out


def is_signed_perm(M):
    return all(sorted(abs(int(v)) for v in row) == [0, 0, 1] for row in M) and \
        all(sorted(abs(int(v)) for v in col) == [0, 0, 1] for col in M.T)


# ---------------------------------------------------------------------------------------------------------------- B
def signed_perms():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            out.append(M)
    return out


def pullback(M, f):
    v = M @ np.array([x, y, z])
    return sp.expand(f.subs({x: v[0], y: v[1], z: v[2]}, simultaneous=True))


def fix_count_torus(mats):
    """the number of points of R^3 / Z^3 fixed by the integer matrices (0 if the fixed set has positive dimension)"""
    S = sp.Matrix(np.vstack([m - np.eye(3, dtype=int) for m in mats]).tolist())
    if S.rank() < 3:
        return 0
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(S, domain=sp.ZZ)
    d = 1
    for i in range(3):
        d *= abs(int(D[i, i]))
    return d


def rot_of_quaternion(q):
    """the rotation of R^3 = span(i, j, k) by v -> q v q^-1"""
    R = np.zeros((3, 3))
    units = [(0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)]
    for c, e in enumerate(units):
        img = CP.qmul(CP.qmul(q, e), CP.qconj(q))
        R[:, c] = img[1:]
    return np.round(R).astype(int)


def orbifold_euler(G, torsion=False):
    """(1/|G|) sum over commuting pairs of eps(g, h) chi(Fix g cap Fix h) on E^3, E any elliptic curve; eps from the lift
    to SU(2) (the binary octahedral class): -1 when the lifts anticommute"""
    lift = {}
    for q in CP.TWO_O.values():
        R = rot_of_quaternion(q)
        lift.setdefault(tuple(R.flatten()), q)
    total = Fr(0)
    for g in G:
        for h in G:
            if not np.array_equal(g @ h, h @ g):
                continue
            n = fix_count_torus([g, h])
            chi = n * n                                 # E^3 = (R^3/Z^3) x (R^3/Z^3) as a real torus, factor-wise
            eps = 1
            if torsion and chi:
                qg, qh = lift[tuple(g.flatten())], lift[tuple(h.flatten())]
                comm = CP.qmul(CP.qmul(qg, qh), CP.qmul(CP.qconj(qg), CP.qconj(qh)))
                eps = 1 if CP.key(comm) == CP.key(CP.ONE) else -1
            total += eps * chi
    return total / len(G)


def cellB(lin, grp_O):
    res = {}
    parities = [np.diag(d) for d in ((1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
    # B1
    b1 = {}
    for P_ in parities:
        fx = [sp.expand(e) for e in (P_ @ np.array([x, y, z]) - np.array([x, y, z]))]
        line = sp.solve(fx, [x, y, z], dict=True)
        on_markov = sp.solve(fx + [x ** 2 + y ** 2 + z ** 2 - x * y * z], [x, y, z], dict=True)
        pts = [tuple(int(sol.get(v, v)) if sol.get(v, v).is_number else str(sol.get(v, v)) for v in (x, y, z))
               for sol in on_markov]
        b1[str(np.diag(P_).tolist())] = {"fixed locus in X": str(line), "fixed points on X_-2": [list(p) for p in pts]}
    res["B1 each parity's fixed locus"] = b1
    res["B1 on X_-2 each parity fixes only the common point"] = all(
        v["fixed points on X_-2"] == [[0, 0, 0]] for v in b1.values())
    # B2
    sym = [M for M in signed_perms() if pullback(M, KAPPA) == sp.expand(KAPPA)]
    det1 = [M for M in sym if round(np.linalg.det(M)) == 1]
    res["B2 signed permutations preserving kappa: order"] = len(sym)
    res["B2 ... with determinant 1: order"] = len(det1)
    three_cycle = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    gen = closure_int(parities + [three_cycle])
    res["B2 the parities and the 3-cycle generate the determinant-1 part"] = bool(
        len(gen) == len(det1) and all(any(np.array_equal(g, d) for d in det1) for g in gen))
    # which move gives the 3-cycle: the automorphism a -> b, b -> (ab)^-1, and the word L^-1 R L^-1 L^-1 of the moves,
    # which has the same matrix (Nielsen: automorphisms with one matrix differ by an inner one, trivial on traces)
    phi3 = {1: [2], 2: [-2, -1]}
    F3 = char_map(phi3)
    w3 = CP.compose(INV["L"], CP.compose(CP.AUT["R"], CP.compose(INV["L"], INV["L"])))
    F_w3 = char_map(w3)
    ab = lambda phi: [[sum((1 if g == 1 else -1 if g == -1 else 0) for g in phi[c]) for c in (1, 2)],
                      [sum((1 if g == 2 else -1 if g == -2 else 0) for g in phi[c]) for c in (1, 2)]]  # noqa: E731
    res["B2 a -> b, b -> (ab)^-1 acts on the characters as"] = [str(f) for f in F3]
    res["B2 the word L^-1 R L^-1 L^-1 of the moves: its matrix, and phi3's"] = [ab(w3), ab(phi3)]
    res["B2 the word acts on the characters as"] = [str(f) for f in F_w3]
    res["B2 ... the linear 3-cycle (x, y, z) -> (y, z, x)"] = bool([str(f) for f in F_w3] == ["y", "z", "x"]
                                                                   and [str(f) for f in F3] == ["y", "z", "x"])
    res["B2 the swap P is the transposition (x y), determinant -1"] = bool(
        [str(f) for f in CP.TR["P"]] == ["y", "x", "z"])
    res["B2 the linear symmetry group is not the moves' linear-part group (A4 = T is its intersection with O)"] = bool(
        len([g for g in det1 if any(np.array_equal(g, o) for o in grp_O)]) == len(det1) and len(grp_O) == 24)
    # B3: the lifts to SU(2)
    two_o = list(CP.TWO_O.values())
    rots = [(q, rot_of_quaternion(q)) for q in two_o]
    in_O = all(any(np.array_equal(R, o) for o in grp_O) for _, R in rots)

    def preimage(sub):
        return [q for q, R in rots if any(np.array_equal(R, s) for s in sub)]

    V4 = closure_int(parities)
    lifts = {"the parities V4 (order %d)" % len(V4): (preimage(V4), "Q8 -> D4"),
             "A4 (order %d)" % len(det1): (preimage(det1), "2T -> E6"),
             "the moves' linear parts O (order %d)" % len(grp_O): (preimage(grp_O), "2O -> E7")}
    res["B3 2O maps onto the moves' linear-part group"] = bool(in_O and len({tuple(R.flatten()) for _, R in rots}) == 24)
    res["B3 the lifts to SU(2) (order; Du Val type by McKay)"] = {k: [len(v[0]), v[1]] for k, v in lifts.items()}
    res["B3 the quaternion units i, j, k act on (x, y, z) as the three parities"] = all(
        any(np.array_equal(rot_of_quaternion(u), P_) for P_ in parities)
        for u in [(0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)])
    # B4
    b4 = {}
    for name, G in (("V4 (the parities)", V4), ("A4", det1), ("O (the moves' linear parts)", grp_O)):
        e0, e1 = orbifold_euler(G), orbifold_euler(G, torsion=True)
        b4[name] = {"order": len(G), "chi_orb": str(e0), "chi_orb with discrete torsion": str(e1),
                    "net generations, standard embedding (|chi| / 2)": [str(abs(e0) / 2), str(abs(e1) / 2)]}
    res["B4 E^3 / G, any elliptic curve E"] = b4
    res["B4 three among them"] = any(Fr(v["net generations, standard embedding (|chi| / 2)"][i]) == 3
                                    for v in b4.values() for i in (0, 1))
    res["B verdict"] = {
        "S1 forced": "no: the group is the weave's, but the compactification E^3 and its curve E are chosen",
        "S2 right kind": "yes: G lies in SU(3), a Calabi-Yau orbifold",
        "S3 a count exists": "yes: compact",
        "S4 a bundle with a hand": "yes for the standard embedding: the tangent bundle, with SU(3) holonomy at the "
                                   "fixed points",
        "S5 the count": "48, 16, 14 (the same with torsion): never three",
        "passes": False}
    return res


# ---------------------------------------------------------------------------------------------------------------- D
def blocks_action(phi, g):
    """the 6 x 6 lift on sum_u C^2_u (block basis): block (u o phi) -> block u by qmat(g)"""
    A = np.zeros((6, 6), dtype=complex)
    G = SR.qmat(g)
    for i, u in enumerate(CT.PAR):
        j = CT.PAR.index(CT.u_after(u, phi))
        A[2 * i:2 * i + 2, 2 * j:2 * j + 2] = G
    return A


def commutant(mats, n):
    rows = [np.kron(g.T, np.eye(n)) - np.kron(np.eye(n), g) for g in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    k = int(sum(s < 1e-9))
    _, _, Vh = np.linalg.svd(np.vstack(rows))
    basis = [Vh[-i - 1].conj().reshape(n, n, order="F") for i in range(k)]
    return k, basis


def W_of(w):
    """W(w) = sum_u chi_u(w) rho_Q(w), block basis"""
    rho = SR.QM["1"]
    for g in w:
        rho = rho @ ({1: SR.QM["i"], 2: SR.QM["j"]}[g] if g > 0 else np.linalg.inv({1: SR.QM["i"], 2: SR.QM["j"]}[-g]))
    A = np.zeros((6, 6), dtype=complex)
    for i, u in enumerate(CT.PAR):
        A[2 * i:2 * i + 2, 2 * i:2 * i + 2] = chi_word(u, w) * rho
    return A


def chi_word(u, w):
    v = 1
    for g in w:
        v *= SR.char_val(u, g)
    return v


def cellD():
    res = {}
    # D0
    lifts = [blocks_action(CP.AUT[m], g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    ok_intertwine = True
    for m in ("L", "R"):
        for g in CP.extend(CP.AUT[m]):
            A = blocks_action(CP.AUT[m], g)
            for gen in (1, 2):
                lhs = A @ W_of([gen]) @ np.linalg.inv(A)
                rhs = W_of(CP.AUT[m][gen])
                ok_intertwine &= bool(np.allclose(lhs, rhs, atol=1e-9))
    res["D0 the lifts intertwine: A W(x) A^-1 = W(phi(x)) for x = a, b"] = ok_intertwine
    k, basis = commutant(lifts, 6)
    res["D0 commutant of the moves' lifts on the six local solutions"] = k
    pieces = []
    if k == 2:
        rng = np.random.default_rng(7)
        C = sum(complex(rng.normal(), rng.normal()) * b for b in basis)
        ev, vec = np.linalg.eig(C)
        groups = []
        for i, e in enumerate(ev):
            for gr in groups:
                if abs(gr[0] - e) < 1e-6:
                    gr[1].append(i)
                    break
            else:
                groups.append([e, [i]])
        for e, idx in groups:
            Vsub = vec[:, idx]
            Q, _ = np.linalg.qr(Vsub)
            inv_ok = all(np.allclose(Q @ (Q.conj().T @ (A @ Q)), A @ Q, atol=1e-8) for A in lifts)
            per_block = [round(float(np.linalg.matrix_rank(Q[2 * b:2 * b + 2, :], tol=1e-8))) for b in range(3)]
            block_sum = all(np.allclose(Q @ Q.conj().T @ Pb(b) @ Q, Pb(b) @ Q, atol=1e-8) for b in range(3))
            pieces.append({"dimension": len(idx), "invariant under every lift": bool(inv_ok),
                           "a sum of parity blocks": bool(block_sum),
                           "index if it is Lambda_+ (dim - 3)": len(idx) - 3,
                           "rank of its projection to each block": per_block})
    res["D0 the invariant pieces"] = pieces
    res["D0 the conditions every move keeps and their indices"] = sorted(
        {0 - 3, 6 - 3} | {p["dimension"] - 3 for p in pieces} | (
            {sum(p["dimension"] for p in pieces) - 3} if pieces else set()))
    grading = [np.kron(np.diag([chi_word(u, [gen]) for u in CT.PAR]), np.eye(2)) for gen in (1, 2)]
    k2, _ = commutant(lifts + grading, 6)
    res["D0 with the parity grading added: commutant"] = k2
    res["D0 W22's +-3 needs the parity grading (block-diagonal conditions)"] = bool(k == 2 and k2 == 1)
    # D1
    units = {"i": (0.0, 1.0, 0.0, 0.0), "j": (0.0, 0.0, 1.0, 0.0), "k": (0.0, 0.0, 0.0, 1.0)}
    d1 = {}
    for u, name in zip(CT.PAR, CT.NAMES):
        found = []
        for nm, q in units.items():
            Q = SR.qmat(q)
            if all(np.allclose(Q @ SR.RHO[gen] @ np.linalg.inv(Q), SR.char_val(u, gen) * SR.RHO[gen]) for gen in (1, 2)):
                found.append(nm)
        d1[name] = found
    res["D1 the quaternion unit u_p with u_p rho_Q u_p^-1 = chi_p rho_Q"] = d1
    res["D1 every parity block is the spin doublet (W = rho_Q (x) C^3)"] = all(len(v) == 1 for v in d1.values())
    # D2, D3: characters of the 248 on Q8
    I = sp.I
    q8 = {"1": [1] * 6, "-1": [-1] * 6, "order 4": [I, -I] * 3}
    count = {"1": 1, "-1": 1, "order 4": 6}

    def e(k, lam):
        return sp.expand(sum(sp.prod(c) for c in itertools.combinations(lam, k)))

    route1 = {}
    for cls, lam in q8.items():
        c6 = sum(lam)
        c6b = sp.conjugate(c6)
        c15, c20 = e(2, lam), e(3, lam)
        c15b = sp.conjugate(c15)
        c35 = sp.expand(c6 * c6b - 1)
        route1[cls] = sp.simplify(8 + 3 + c35 + 3 * c15 + 3 * c15b + 6 * c6 + 6 * c6b + 2 * c20)
    spin = {"1": lambda j: 2 * j + 1, "-1": lambda j: (-1) ** int(2 * j) * (2 * j + 1),
            "order 4": lambda j: int(round(float(sp.sin((2 * j + 1) * sp.pi / 2))))}
    route2 = {}
    for cls in q8:
        ch = spin[cls]
        c14 = 3 + ch(1) + 2 * ch(Fr(3, 2))
        c7 = 2 * ch(Fr(1, 2)) + ch(1)
        route2[cls] = c14 + 52 + 26 * c7
    res["D2 chi_248 on Q8 via SU(3) x SU(2) x SU(6)' (W in the 6)"] = {k: str(v) for k, v in route1.items()}
    res["D2 chi_248 on Q8 via G2 x F4 (Q8 in G2's second SU(2))"] = {k: str(v) for k, v in route2.items()}
    res["D2 the two routes agree"] = all(sp.simplify(route1[k] - route2[k]) == 0 for k in q8)
    def mult(vals_by_cls):
        s = sum(count[c] * route1[c] * vals_by_cls[c] for c in q8)
        return sp.nsimplify(s / 8)

    m_triv = mult({"1": 1, "-1": 1, "order 4": 1})
    m_rho = mult({"1": 2, "-1": -2, "order 4": 0})
    # a parity character: +1 on one pair +-q, -1 on the other two pairs: sum over the six = -2
    s_par = (route1["1"] + route1["-1"] + route1["order 4"] * (2 - 4)) / 8
    res["D2 the centraliser's dimension (multiplicity of the trivial representation)"] = str(m_triv)
    res["D3 multiplicity of rho"] = str(m_rho)
    res["D3 multiplicity of each parity character"] = str(sp.nsimplify(s_par))
    res["D3 the check 55 + 2 x 56 + 3 x 27 = 248"] = bool(m_triv + 2 * m_rho + 3 * sp.nsimplify(s_par) == 248)
    res["D2 F4 x SU(2): 52 + 3"] = bool(m_triv == 55)
    res["D3 the numbers match F4 x SU(2): rho's 56 = (26, 2) + 2 (1, 2), each parity's 27 = (26, 1) + (1, 1)"] = bool(
        m_rho == 2 * 26 + 2 * 2 and sp.nsimplify(s_par) == 26 + 1)
    return res


def Pb(b):
    P = np.zeros((6, 6), dtype=complex)
    P[2 * b:2 * b + 2, 2 * b:2 * b + 2] = np.eye(2)
    return P


# ---------------------------------------------------------------------------------------------------------------- E
def cellE(A, B):
    return {
        "K1 the character variety": A["A verdict"],
        "K2 the local orbifolds E^3 / G": B["B verdict"],
        "K3 main's frame spaces": {
            "S1 forced": "yes, one per thread", "S2 right kind": "yes: complex parallelizable, K trivial; heterotic "
            "solutions exist on compact quotients (Fei-Yau, arXiv:1407.7641)",
            "S3 a count exists": "open: the threads' groups are not cocompact; only the cusp terms could count",
            "S4 a bundle with a hand": "no in the interior: TX is trivial and bundles from Gamma are flat, so ch = rank",
            "S5 the count": "0 on any compact quotient; the cusps are main's open cell (a)", "passes": False},
        "K4 the universal families": {
            "Kuga-Sato E x_M E": "S1 no: a free twist of the base (2026-10-08)",
            "the isomonodromic total space (H x X_-2) / SL(2, Z)": "S2 no: dtau has weight 2, so K is the weight-2 "
            "line bundle of the modular curve, not trivial; S3 no: the cusp and the surface's ends", "passes": False},
        "none passes": True}


def run():
    out = {"rule": "W24_RULE.md (committed d39778dd before this ran)"}
    A, maps, lin, grp = cellA()
    out["A the character variety"] = A
    B = cellB(lin, grp)
    out["B the local model at the common point"] = B
    out["C main's frame spaces"] = "stated in the rule; nothing computed here"
    out["D the gauge side"] = cellD()
    out["E the verdict"] = cellE(A, B)
    return out


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_six_dimensional_census.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))
