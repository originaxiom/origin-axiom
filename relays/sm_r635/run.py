#!/usr/bin/env python3
"""SM-R635 (P-635, M53): the boundary-free classes of H^1(fibre, ad Q8), exactly, by Fox calculus; an explicit
three-parameter family of flat SU(2) connections through the frame's Q8 point; and the monodromy's action on it.

Card: relays/cards/SM_R635_the-boundary-free-classes.md (sealed before any run on the Q8 point).
Data-free. No measured value is read or printed. Exact arithmetic (sympy) except one disclosed numerical sample (F4).

  python3 -B run.py <main checkout> run     # the sealed run: writes r635_run.txt and r635_results.json beside this file
  python3 -B run.py <main checkout> smoke   # plants only (P2, P4), outside the test population; prints 'smoke ok'

The frame's Q8 holonomies are read from main's own module (B1723's copy of B1656's functions: QI, QJ, QK, EPS,
BLOCKS); nothing of the frame is evaluated. Depends on the standard library, numpy, mpmath (through main's module),
sympy.
"""
import contextlib
import io
import itertools
import json
import pathlib
import random
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
LOG, OUT = [], {}


def say(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


# ---------------------------------------------------------------- the frame's Q8, read from main's module
def frame_q8(main_root):
    d = pathlib.Path(main_root) / "frontier" / "B1723_the_golden_valley" / "verification"
    sys.path.insert(0, str(d))
    argv = sys.argv
    sys.argv = ["x"]
    with contextlib.redirect_stdout(io.StringIO()):
        import b1656_funcs as B
    sys.argv = argv

    def ex(Mn):
        return sp.Matrix(2, 2, lambda i, j: sp.nsimplify(complex(Mn[i, j]).real, rational=True)
                         + sp.I * sp.nsimplify(complex(Mn[i, j]).imag, rational=True))
    return {"QI": ex(B.QI), "QJ": ex(B.QJ), "QK": ex(B.QK), "EPS": ex(B.EPS), "BLOCKS": [ex(c) for c in B.BLOCKS]}


# ---------------------------------------------------------------- quaternions and the adjoint
ONE = sp.eye(2)
QI0 = sp.Matrix([[sp.I, 0], [0, -sp.I]])
QJ0 = sp.Matrix([[0, 1], [-1, 0]])
QK0 = QI0 * QJ0
BASIS = [QI0, QJ0, QK0]


def quat(a, b, c, d):
    """a + b i + c j + d k as a 2 x 2 matrix in the frame's convention"""
    return a * ONE + b * QI0 + c * QJ0 + d * QK0


def ad(g):
    """Ad(g) on su(2) = R^3 in the basis (QI, QJ, QK); the inner product Re tr(X Y^H) / 2"""
    gi = g.inv()
    return sp.Matrix(3, 3, lambda r, c: sp.simplify(sp.re(sp.expand((g * BASIS[c] * gi * BASIS[r].H).trace() / 2))))


def to_vec(X):
    """an element of su(2) as its coordinates in (QI, QJ, QK)"""
    return sp.Matrix([sp.simplify(sp.re(sp.expand((X * Y.H).trace() / 2))) for Y in BASIS])


# ---------------------------------------------------------------- Fox calculus with coefficients Ad(rho)
def word_ad(word, AD):
    M = sp.eye(AD[word[0][0]].shape[0])
    for g, e in word:
        M = M * (AD[g] if e == 1 else AD[g].inv())
    return M


def fox(word, x, AD):
    """the Fox derivative d(word)/dx evaluated in Ad(rho), a 3 x 3 matrix"""
    dv = AD[x].shape[0]
    tot, pre = sp.zeros(dv), sp.eye(dv)
    for g, e in word:
        if g == x:
            tot += pre if e == 1 else -pre * AD[g].inv()
        pre = pre * (AD[g] if e == 1 else AD[g].inv())
    return tot


def fox_row(word, gens, AD):
    return sp.Matrix.hstack(*[fox(word, x, AD) for x in gens])


def cohomology(gens, rels, AD, boundary=None):
    """dims of H^0, Z^1, B^1, H^1; with a boundary word c also the restriction rank and dim H^1_par, where
    H^1_par = {u in Z^1 : u(c) in (Ad(c) - 1) V} / B^1 (the class held on the boundary)"""
    dv = AD[gens[0]].shape[0]
    n = dv * len(gens)
    d0 = sp.Matrix.vstack(*[AD[g] - sp.eye(dv) for g in gens])
    h0 = dv - d0.rank()
    b1 = d0.rank()
    if rels:
        J = sp.Matrix.vstack(*[fox_row(r, gens, AD) for r in rels])
        Zb = J.nullspace()
    else:
        Zb = [sp.eye(n)[:, i] for i in range(n)]
    z1 = len(Zb)
    res = dict(H0=h0, Z1=z1, B1=b1, H1=z1 - b1)
    if boundary is not None:
        Ac = word_ad(boundary, AD)
        Fc = fox_row(boundary, gens, AD)
        Zm = sp.Matrix.hstack(*Zb) if Zb else sp.zeros(n, 0)
        img = Ac - sp.eye(dv)
        # the class restricted to the boundary lives in V / (Ad(c) - 1) V; its rank on Z^1
        big = sp.Matrix.hstack(Fc * Zm, img)
        restr = big.rank() - img.rank()
        res.update(restriction_rank=restr, H1_par=(z1 - restr) - b1, H1_boundary=dv - img.rank())
    return res


A_, B_ = "a", "b"
TORUS_REL = [(A_, 1), (B_, 1), (A_, -1), (B_, -1)]          # c = a b a^-1 b^-1, the boundary loop of the fibre


def ad_pair(ga, gb):
    return {A_: ad(ga), B_: ad(gb)}


# ---------------------------------------------------------------- characters of Z2 x Z2 on the three axes
def per_character(AD):
    """on each axis where Ad(a), Ad(b) act by signs (a character of Z2 x Z2): dim H^1 on F2 and on Z^2"""
    out = {}
    for k, name in enumerate(("I", "J", "K")):
        AD1 = {A_: AD[A_][k:k + 1, k:k + 1], B_: AD[B_][k:k + 1, k:k + 1]}
        out[name] = dict(signs=(int(AD1[A_][0, 0]), int(AD1[B_][0, 0])),
                         H1_free=cohomology([A_, B_], [], AD1)["H1"],
                         H1_closed=cohomology([A_, B_], [TORUS_REL], AD1)["H1"])
    diag = all(AD[g][r, c] == 0 for g in (A_, B_) for r in range(3) for c in range(3) if r != c)
    out["Ad_diagonal"] = diag
    return out


# ---------------------------------------------------------------- the explicit family
s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
S = (s1, s2, s3)


def ex1(X, s):
    """exp(s X) for a unit pure quaternion X"""
    return sp.cos(s) * ONE + sp.sin(s) * X


def family(QI, QJ):
    QKl = QI * QJ
    A = QI * ex1(QI, s1) * ex1(QKl, s3)
    B = QJ * ex1(QJ, s2)
    return A, B


def tr(M):
    return sp.expand(M.trace())


def family_cells(QI, QJ):
    A, B = family(QI, QJ)
    x, y, z = tr(A), tr(B), tr(A * B)
    kap = tr(A * B * A.adjugate() * B.adjugate())          # det A = det B = 1
    at0 = {v: 0 for v in S}
    base = bool(sp.simplify(A.subs(at0) - QI) == sp.zeros(2)) and bool(sp.simplify(B.subs(at0) - QJ) == sp.zeros(2))
    Jac = sp.Matrix([[sp.diff(f, v).subs(at0) for v in S] for f in (x, y, z)])
    # the Fricke identity, checked at 20 seeded points to 40 digits (numerical, disclosed)
    fr = sp.lambdify(S, kap - (x**2 + y**2 + z**2 - x * y * z - 2), "mpmath")
    rf = random.Random(6350)
    import mpmath
    mpmath.mp.dps = 40
    fricke = max(abs(complex(fr(*[mpmath.mpf(rf.uniform(-1, 1)) for _ in range(3)]))) for _ in range(20))
    grad = [sp.nsimplify(sp.diff(kap, v).subs(at0)) for v in S]
    Hk = sp.Matrix(3, 3, lambda i, j: sp.nsimplify(sp.expand(sp.diff(kap, S[i], S[j]).subs(at0))))
    eig = sorted(Hk.eigenvals().keys(), key=lambda e: float(e))
    # tangent cocycles u_g = (d rho_s(g) / ds) rho(g)^-1 at s = 0, and their rank modulo B^1
    cols = []
    for v in S:
        ua = to_vec(sp.diff(A, v).subs(at0) * QI.inv())
        ub = to_vec(sp.diff(B, v).subs(at0) * QJ.inv())
        cols.append(sp.Matrix.vstack(ua, ub))
    AD = ad_pair(QI, QJ)
    d0 = sp.Matrix.vstack(*[AD[g] - sp.eye(3) for g in (A_, B_)])
    tang_mod_B = sp.Matrix.hstack(*cols, d0).rank() - d0.rank()
    # a disclosed numerical sample: kappa > -2 on 2000 points of the ball |s| <= 0.5 (seeded)
    f = sp.lambdify(S, sp.re(kap), "math")
    rng = random.Random(635)
    worst = None
    for _ in range(2000):
        while True:
            p = [rng.uniform(-0.5, 0.5) for _ in range(3)]
            if 1e-6 < sum(q * q for q in p) <= 0.25:
                break
        v = f(*p) + 2.0
        worst = v if worst is None else min(worst, v / sum(q * q for q in p))
    return dict(base_is_frame_q8=base, jacobian_rank=int(Jac.rank()), jacobian=str(Jac.tolist()),
                fricke_identity_residual=str(fricke), kappa_grad_at_0=[str(g) for g in grad],
                kappa_hessian=str(Hk.tolist()), kappa_hessian_eigs=[str(e) for e in eig],
                tangent_rank_mod_B1=int(tang_mod_B), sample_min_kappa_plus_2_over_s2=worst)


# ---------------------------------------------------------------- the monodromy
PHI = {A_: [(A_, 1), (B_, 1)], B_: [(B_, 1), (A_, 1), (B_, 1)]}   # a -> ab, b -> bab: abelianised [[1, 1], [1, 2]]


def phi_word(word):
    out = []
    for g, e in word:
        w = PHI[g]
        out += w if e == 1 else [(h, -f) for h, f in reversed(w)]
    return out


def abelianised_phi():
    return sp.Matrix([[sum(e for h, e in PHI[g] if h == x) for g in (A_, B_)] for x in (A_, B_)])


def monodromy_cells(AD):
    """phi* on H^1(F2, Ad rho): find P in SO(3) (signed permutations) with P Ad(rho(phi x)) P^-1 = Ad(rho(x)); the map
    u -> u', u'(x) = P u(phi(x)), on Z^1 = V^2; dim ker(phi* - 1) on H^1 = Z^1 / B^1, for every admissible P"""
    imgs = {g: word_ad(PHI[g], AD) for g in (A_, B_)}
    Ps = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            P = sp.zeros(3)
            for r, c in enumerate(perm):
                P[r, c] = sg[r]
            if P.det() != 1:
                continue
            if all(P * imgs[g] * P.inv() == AD[g] for g in (A_, B_)):
                Ps.append(P)
    d0 = sp.Matrix.vstack(*[AD[g] - sp.eye(3) for g in (A_, B_)])
    kers, charpolys = [], []
    lam = sp.symbols("lam")
    for P in Ps:
        Phi = sp.Matrix.vstack(*[P * fox_row(PHI[g], [A_, B_], AD) for g in (A_, B_)])   # 6 x 6 on Z^1 = V^2
        # dim{[u] : Phi u - u in B^1} - 0  (H^0 = 0 here; B^1 is Phi-stable)
        Mm = sp.Matrix.hstack(Phi - sp.eye(6), d0)
        ns = Mm.nullspace()
        U = sp.Matrix.hstack(*[v[:6, :] for v in ns]) if ns else sp.zeros(6, 0)
        kers.append(sp.Matrix.hstack(U, d0).rank() - d0.rank())
        # the induced 3 x 3 map on H^1: complement of B^1 spanned by coordinates, projected along B^1
        Bb = sp.Matrix.hstack(*d0.columnspace()) if d0.rank() else sp.zeros(6, 0)
        basis_cols = []
        cur = Bb
        for i in range(6):
            e = sp.eye(6)[:, i]
            if sp.Matrix.hstack(cur, e).rank() > cur.rank():
                basis_cols.append(i)
                cur = sp.Matrix.hstack(cur, e)
        Cm = sp.Matrix.hstack(*[sp.eye(6)[:, i] for i in basis_cols])
        full = sp.Matrix.hstack(Bb, Cm)
        H = (full.inv() * Phi * Cm)[Bb.shape[1]:, :]
        charpolys.append(str(sp.factor(H.charpoly(lam).as_expr())))
    return dict(n_conjugators=len(Ps), ker_dims=kers, charpolys=sorted(set(charpolys)))


def trace_route_monodromy(QI, QJ):
    """second route: D(phi) on trace coordinates (x, y, z) = (tr A, tr B, tr AB) at the Q8 point, through the family"""
    A, B = family(QI, QJ)
    at0 = {v: 0 for v in S}
    old = [tr(A), tr(B), tr(A * B)]
    new = [tr(A * B), tr(B * A * B), tr(A * B * B * A * B)]
    J0 = sp.Matrix([[sp.diff(f, v).subs(at0) for v in S] for f in old])
    J1 = sp.Matrix([[sp.diff(f, v).subs(at0) for v in S] for f in new])
    D = sp.simplify(J1 * J0.inv())
    return dict(Dphi=str(D.tolist()), ker_dim=3 - (D - sp.eye(3)).rank(),
                charpoly=str(sp.factor(D.charpoly(sp.symbols("lam")).as_expr())))


# ---------------------------------------------------------------- plants (outside the test population)
def plants():
    out = {}
    # P2: a generic irreducible pair (rational unit quaternions), the boundary free and held
    ga, gb = quat(sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7), 0), quat(sp.Rational(1, 3), 0,
                                                                                      sp.Rational(2, 3),
                                                                                      sp.Rational(2, 3))
    out["P2_generic_F2"] = cohomology([A_, B_], [], ad_pair(ga, gb), boundary=TORUS_REL)
    # P3: the trivial representation on F2 and on Z^2
    I2 = sp.eye(2)
    out["P3_trivial_F2"] = cohomology([A_, B_], [], ad_pair(I2, I2), boundary=TORUS_REL)
    out["P3_trivial_Z2"] = cohomology([A_, B_], [TORUS_REL], ad_pair(I2, I2))
    # P4: the monodromy on the trivial representation (phi* = abelianised phi (x) 1_3; no eigenvalue 1)
    out["P4_trivial_monodromy"] = monodromy_cells(ad_pair(I2, I2))
    out["P4_abelianised_phi"] = str(abelianised_phi().tolist())
    return out


def plant_P1(QI):
    # P1: a reducible pair (QI, QI) on the closed torus: H^1 must be positive
    return cohomology([A_, B_], [TORUS_REL], ad_pair(QI, QI))


# ---------------------------------------------------------------- the run
def main():
    if len(sys.argv) != 3 or sys.argv[2] not in ("run", "smoke"):
        raise SystemExit("usage: run.py <main checkout> run|smoke")
    mode = sys.argv[2]
    if mode == "smoke":
        p = plants()
        g = p["P2_generic_F2"]
        assert g["H0"] == 0 and g["H1"] == 3 and g["H1_par"] == 2, "P2 plant"
        assert p["P3_trivial_F2"]["H1"] == 6 and p["P3_trivial_Z2"]["H1"] == 6, "P3 plant"
        assert p["P4_trivial_monodromy"]["ker_dims"] and max(p["P4_trivial_monodromy"]["ker_dims"]) == 0, "P4"
        # callability on a non-Q8 base pair (two non-orthogonal pure unit quaternions); values discarded
        U = quat(0, sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3))
        V = quat(0, sp.Rational(1, 3), sp.Rational(-2, 3), sp.Rational(2, 3)) * ex1(U, sp.Rational(1, 5))
        with contextlib.redirect_stdout(io.StringIO()):
            fc = family_cells(U, V)
            trm = trace_route_monodromy(U, V)
            mg = monodromy_cells(ad_pair(U, V))
            Fq = frame_q8(sys.argv[1])
        assert "jacobian_rank" in fc and "ker_dim" in trm and "ker_dims" in mg and set(Fq) >= {"QI", "QJ", "EPS"}
        print("smoke ok")
        return
    F = frame_q8(sys.argv[1])
    QI, QJ, QK = F["QI"], F["QJ"], F["QK"]
    OUT["G0"] = dict(QI_sq=str((QI * QI).tolist()), QJ_sq=str((QJ * QJ).tolist()),
                     anticommute=bool(QI * QJ + QJ * QI == sp.zeros(2)), QK_is_QIQJ=bool(QK == QI * QJ),
                     EPS_is_QJ=bool(F["EPS"] == QJ),
                     BLOCKS_are_QJ_QI_QK=bool(F["BLOCKS"][0] == QJ and F["BLOCKS"][1] == QI and F["BLOCKS"][2] == QK),
                     commutator=str((QI * QJ * QI.inv() * QJ.inv()).tolist()))
    say("G0", OUT["G0"])
    AD = ad_pair(QI, QJ)
    OUT["Ad"] = {g: str(AD[g].tolist()) for g in AD}
    say("Ad", OUT["Ad"])
    OUT["F1_closed_torus"] = cohomology([A_, B_], [TORUS_REL], AD)
    say("F1 closed torus", OUT["F1_closed_torus"])
    OUT["F2_F3_punctured"] = cohomology([A_, B_], [], AD, boundary=TORUS_REL)
    say("F2/F3 punctured fibre, boundary free / held", OUT["F2_F3_punctured"])
    OUT["F4_per_character"] = per_character(AD)
    say("F4 per character", OUT["F4_per_character"])
    triv = {A_: sp.eye(1), B_: sp.eye(1)}
    OUT["F5_centre_lines"] = dict(closed=cohomology([A_, B_], [TORUS_REL], triv),
                                  punctured=cohomology([A_, B_], [], triv, boundary=TORUS_REL))
    say("F5 centre (the lines)", OUT["F5_centre_lines"])
    OUT["F6_family"] = family_cells(QI, QJ)
    say("F6 family", OUT["F6_family"])
    OUT["F7_monodromy_fox"] = monodromy_cells(AD)
    say("F7 monodromy (Fox route)", OUT["F7_monodromy_fox"])
    OUT["F7_monodromy_traces"] = trace_route_monodromy(QI, QJ)
    say("F7 monodromy (trace route)", OUT["F7_monodromy_traces"])
    OUT["P1_reducible_closed"] = plant_P1(QI)
    say("P1", OUT["P1_reducible_closed"])
    OUT["plants"] = plants()
    say("P2-P4", OUT["plants"])
    (HERE / "r635_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n", encoding="utf-8")
    (HERE / "r635_run.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
