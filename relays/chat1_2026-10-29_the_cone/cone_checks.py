"""THE CONE AND THE SIGN: the exact checks of THE_CONE_RULE.md (sealed aabd77104).

Classical facts on the record's object, checked so that a relay can cite them:
  S1a  Riley's representation of the figure-eight knot group satisfies its relator (exact, Z[omega]);
  S1b  each holonomy generator acts on Hermitian 2x2 matrices X -> A X A^dagger as an element of SO+(3,1);
  S2   the Minkowski metric in hyperbolic-slicing coordinates is the cone over H^3 (the Milne metric);
  S3   the arrow: X -> -X swaps the two halves of the light cone; complex conjugation (orientation-reversing on H^3)
       keeps each half;
  S4   the moves L, R keep the discriminant b^2 - 4ac of binary quadratic forms, a form of signature (2,1);
  S5   that form is B97's Killing form, through sl(2,R) -> symmetric matrices, X -> X J;
  S6   sl(2,C) as a real Lie algebra has Killing form of signature (3,3);
  S7   the control: m003's holonomy also lands in SO+(3,1).

Run from this folder:  python3 cone_checks.py --selftest   (synthetic inputs only)
                       python3 cone_checks.py              (writes cone_checks_out.txt and cone_checks.json)
"""
import json
import sys

import sympy as sp

I2 = sp.eye(2)
SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
ETA = sp.diag(1, -1, -1, -1)
OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # e^(2 pi i/3)


def lorentz_of(A):
    """The 4x4 real matrix of X -> A X A^dagger in the basis (I, s1, s2, s3); Lambda[mu, nu] = tr(s_mu A s_nu A^+)/2."""
    Ad = A.H
    return sp.Matrix(4, 4, lambda m, n: sp.simplify(sp.expand((SIG[m] * A * SIG[n] * Ad).trace() / 2)))


def is_so31_exact(L):
    gram = sp.simplify(L.T * ETA * L - ETA)
    det = sp.simplify(L.det())
    l00 = sp.simplify(L[0, 0])
    return {"gram_zero": bool(gram == sp.zeros(4, 4)), "det": str(det), "Lambda00": str(l00),
            "Lambda00_ge_1": (bool(sp.N(l00) >= 1) if l00.is_number else None),
            "all_real": bool(all(sp.simplify(sp.im(v)) == 0 for v in L))}


def lorentz_numeric(A):
    import numpy as np
    s = [np.eye(2), np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    Ad = A.conj().T
    return np.array([[np.trace(s[m] @ A @ s[n] @ Ad) / 2 for n in range(4)] for m in range(4)])


def is_so31_numeric(Lc):
    import numpy as np
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    L = Lc.real
    return {"max_imag": float(abs(Lc.imag).max()), "gram_resid": float(abs(L.T @ eta @ L - eta).max()),
            "det": float(np.linalg.det(L)), "Lambda00": float(L[0, 0])}


def snappy_holonomy(name):
    import numpy as np
    import snappy
    G = snappy.Manifold(name).fundamental_group()
    out = {}
    for g in G.generators():
        M = G.SL2C(g)
        out[g] = np.array([[complex(M[0, 0]), complex(M[0, 1])], [complex(M[1, 0]), complex(M[1, 1])]])
    return out, [str(r) for r in G.relators()]


def form_action(M, abc):
    """f(x, y) = a x^2 + b x y + c y^2  ->  f(p x + q y, r x + s y) for M = [[p, q], [r, s]]."""
    x, y = sp.symbols("x y")
    a, b, c = abc
    p, q, r, s = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    f = sp.expand(a * (p * x + q * y) ** 2 + b * (p * x + q * y) * (r * x + s * y) + c * (r * x + s * y) ** 2)
    P = sp.Poly(f, x, y)
    return (P.coeff_monomial(x ** 2), P.coeff_monomial(x * y), P.coeff_monomial(y ** 2))


def selftest():
    a = sp.symbols("a", real=True)
    # identity -> identity; a diagonal boost -> cosh/sinh in the (0, 3) block; a rotation keeps Lambda00 = 1
    assert lorentz_of(sp.eye(2)) == sp.eye(4)
    B = sp.diag(sp.exp(a / 2), sp.exp(-a / 2))
    LB = lorentz_of(B)
    assert sp.simplify(LB[0, 0] - sp.cosh(a)) == 0 and sp.simplify(LB[0, 3] - sp.sinh(a)) == 0
    th = sp.symbols("th", real=True)
    Rz = sp.diag(sp.exp(sp.I * th / 2), sp.exp(-sp.I * th / 2))
    assert sp.simplify(lorentz_of(Rz)[0, 0] - 1) == 0
    assert is_so31_exact(LB)["gram_zero"]
    # forms: the identity substitution changes nothing; the discriminant of x^2 - y^2 is 4
    assert form_action(sp.eye(2), (1, 0, -1)) == (1, 0, -1)
    print("selftest: helpers pass on synthetic inputs (identity, a boost, a rotation, the forms' identity)")


def main():
    lines, out = [], {"rule": "aabd77104"}

    def say(s=""):
        print(s)
        lines.append(s)

    say("THE CONE AND THE SIGN: the checks of THE_CONE_RULE.md (sealed aabd77104)")
    say()

    # S1a -- Riley's relator
    x = sp.Matrix([[1, 1], [0, 1]])
    y = sp.Matrix([[1, 0], [-OMEGA, 1]])
    w = x.inv() * y * x * y.inv()
    diff = sp.simplify(sp.expand(w * x - y * w))
    diffm = sp.simplify(sp.expand(w * x + y * w))
    s1a = bool(diff == sp.zeros(2, 2)) or bool(diffm == sp.zeros(2, 2))
    out["S1a"] = {"wx_minus_yw_zero": bool(diff == sp.zeros(2, 2)), "wx_plus_yw_zero": bool(diffm == sp.zeros(2, 2)),
                  "holds": s1a}
    say("S1a Riley's relator w x = y w (w = x^-1 y x y^-1), omega = e^(2 pi i/3): wx - yw = 0: %s; wx + yw = 0: %s  -> %s"
        % (out["S1a"]["wx_minus_yw_zero"], out["S1a"]["wx_plus_yw_zero"], s1a))
    say("    tr(x y^-1) = %s, tr(x y) = %s" % (sp.simplify((x * y.inv()).trace()), sp.simplify((x * y).trace())))

    # S1b -- exact on Riley's generators, numeric on SnapPy's
    s1b_ok = True
    out["S1b"] = {"riley": {}, "snappy_m004": {}}
    for nm, A in (("x", x), ("y", y)):
        L = lorentz_of(A)
        r = is_so31_exact(L)
        out["S1b"]["riley"][nm] = dict(r, Lambda=[[str(v) for v in L.row(i)] for i in range(4)])
        ok = r["gram_zero"] and r["det"] == "1" and r["Lambda00_ge_1"] and r["all_real"]
        s1b_ok &= ok
        say("S1b Riley %s: Lambda^T eta Lambda = eta exactly: %s; det %s; Lambda00 %s (>= 1: %s); real: %s"
            % (nm, r["gram_zero"], r["det"], r["Lambda00"], r["Lambda00_ge_1"], r["all_real"]))
        say("      Lambda = %s" % [[str(v) for v in L.row(i)] for i in range(4)])
    hol, rel = snappy_holonomy("m004")
    out["S1b"]["snappy_m004_relators"] = rel
    for g, A in hol.items():
        r = is_so31_numeric(lorentz_numeric(A))
        out["S1b"]["snappy_m004"][g] = r
        ok = r["max_imag"] < 1e-9 and r["gram_resid"] < 1e-9 and abs(r["det"] - 1) < 1e-9 and r["Lambda00"] >= 1 - 1e-9
        s1b_ok &= ok
        say("S1b SnapPy m004 %s: max imag %.1e; gram residual %.1e; det %.12f; Lambda00 %.6f" % (
            g, r["max_imag"], r["gram_resid"], r["det"], r["Lambda00"]))
    say("    m004 relators (SnapPy): %s" % rel)
    out["S1b"]["holds"] = s1b_ok
    say("S1b -> %s" % s1b_ok)
    say()

    # S2 -- the Milne metric
    t, r_, th, ph = sp.symbols("t r theta phi", positive=True)
    X = sp.Matrix([t * sp.cosh(r_), t * sp.sinh(r_) * sp.sin(th) * sp.cos(ph),
                   t * sp.sinh(r_) * sp.sin(th) * sp.sin(ph), t * sp.sinh(r_) * sp.cos(th)])
    J = X.jacobian([t, r_, th, ph])
    g = sp.simplify(J.T * ETA * J)
    target = sp.diag(1, -t ** 2, -t ** 2 * sp.sinh(r_) ** 2, -t ** 2 * sp.sinh(r_) ** 2 * sp.sin(th) ** 2)
    s2_metric = bool(sp.simplify(g - target) == sp.zeros(4, 4))
    s2_det = bool(sp.simplify((X.T * ETA * X)[0] - t ** 2) == 0)
    out["S2"] = {"metric_is_cone": s2_metric, "detX_is_t2": s2_det, "holds": s2_metric and s2_det,
                 "metric": [[str(v) for v in g.row(i)] for i in range(4)]}
    say("S2 the pull-back of eta in (t, r, theta, phi): %s" % [[str(v) for v in g.row(i)] for i in range(4)])
    say("    = dt^2 - t^2 (dr^2 + sinh^2 r dOmega^2) exactly: %s; det X = t^2: %s  -> %s" % (s2_metric, s2_det, out["S2"]["holds"]))
    say()

    # S3 -- the arrow
    T = -sp.eye(4)
    comm = all(sp.simplify(T * lorentz_of(A) - lorentz_of(A) * T) == sp.zeros(4, 4) for A in (x, y))
    e0 = sp.Matrix([1, 0, 0, 0])
    swaps = bool((T * e0)[0] < 0)
    # complex conjugation of entries: X -> conj(X) on Hermitian X (= X^T): in (I, s1, s2, s3) it flips s2
    C = sp.diag(1, 1, -1, 1)
    conj_is_conj = all(sp.simplify((SIG[m].conjugate() - (C[m, m] * SIG[m]))) == sp.zeros(2, 2) for m in range(4))
    c_det, c00 = C.det(), C[0, 0]
    # conjugation maps Riley's group to its complex conjugate: Lambda(conj A) = C Lambda(A) C
    conj_intertwines = all(sp.simplify(lorentz_of(A.conjugate()) - C * lorentz_of(A) * C) == sp.zeros(4, 4) for A in (x, y))
    s3 = comm and swaps and conj_is_conj and c_det == -1 and c00 == 1 and conj_intertwines
    out["S3"] = {"time_reversal_commutes": comm, "time_reversal_swaps_halves": swaps,
                 "conjugation_is_diag(1,1,-1,1)": conj_is_conj, "conjugation_det": str(c_det),
                 "conjugation_Lambda00": str(c00), "conjugation_intertwines": conj_intertwines, "holds": s3}
    say("S3 X -> -X commutes with both generators: %s; swaps the halves (e0 -> -e0): %s" % (comm, swaps))
    say("    complex conjugation of entries = diag(1, 1, -1, 1) on (I, s1, s2, s3): %s; det %s; Lambda00 %s;"
        " Lambda(conj A) = C Lambda(A) C: %s  -> %s" % (conj_is_conj, c_det, c00, conj_intertwines, s3))
    say()

    # S4 -- the 2+1 half: forms and the discriminant
    a, b, c = sp.symbols("a b c")
    Lm = sp.Matrix([[1, 0], [1, 1]])
    Rm = sp.Matrix([[1, 1], [0, 1]])
    disc = lambda abc: sp.expand(abc[1] ** 2 - 4 * abc[0] * abc[2])
    keeps = {nm: bool(sp.expand(disc(form_action(M, (a, b, c))) - disc((a, b, c))) == 0) for nm, M in (("L", Lm), ("R", Rm))}
    gram = sp.Matrix([[0, 0, -2], [0, 1, 0], [-2, 0, 0]])           # b^2 - 4ac in (a, b, c)
    ev = gram.eigenvals()
    pos = sum(m for v, m in ev.items() if v > 0)
    neg = sum(m for v, m in ev.items() if v < 0)
    LR = Lm * Rm
    act = sp.Matrix(3, 3, lambda i, j: form_action(LR, tuple(1 if k == j else 0 for k in range(3)))[i])
    ns = (act - sp.eye(3)).nullspace()
    inv_forms = [list(v) for v in ns]
    inv_disc = [disc(tuple(v)) for v in ns]
    cusp_null = disc((1, 0, 0)) == 0 and disc((0, 0, 1)) == 0
    Lfix = (sp.Matrix(3, 3, lambda i, j: form_action(Lm, tuple(1 if k == j else 0 for k in range(3)))[i]) - sp.eye(3)).nullspace()
    Lfix_disc = [disc(tuple(v)) for v in Lfix]
    s4 = all(keeps.values()) and (pos, neg) == (2, 1) and len(ns) == 1 and inv_disc[0] > 0 and cusp_null \
        and all(d == 0 for d in Lfix_disc)
    out["S4"] = {"keeps_disc": keeps, "signature": [pos, neg], "LR": [[int(v) for v in LR.row(i)] for i in range(2)],
                 "LR_invariant_forms": [[str(u) for u in v] for v in inv_forms], "their_disc": [str(d) for d in inv_disc],
                 "L_invariant_forms": [[str(u) for u in v] for v in Lfix], "their_disc_L": [str(d) for d in Lfix_disc],
                 "holds": s4}
    say("S4 L, R keep b^2 - 4ac: %s; its signature (pos, neg) = (%d, %d)" % (keeps, pos, neg))
    say("    LR = %s; its invariant forms (a, b, c): %s, discriminant %s (> 0: spacelike)" % (
        out["S4"]["LR"], out["S4"]["LR_invariant_forms"], out["S4"]["their_disc"]))
    say("    L's invariant forms: %s, discriminant %s (null, the cusp)  -> %s" % (
        out["S4"]["L_invariant_forms"], out["S4"]["their_disc_L"], s4))
    say()

    # S5 -- B97's Killing form is the discriminant
    h, e, f = sp.symbols("h e f")
    Xs = sp.Matrix([[h, e], [f, -h]])
    Jm = sp.Matrix([[0, 1], [-1, 0]])
    S = Xs * Jm
    sym = bool(sp.simplify(S - S.T) == sp.zeros(2, 2))
    abc = (S[0, 0], 2 * S[0, 1], S[1, 1])
    killing = sp.expand(4 * (Xs * Xs).trace())
    ratio = sp.simplify(killing / disc(abc))
    inter = all(sp.simplify(M * S * M.T - (M * Xs * M.inv()) * Jm) == sp.zeros(2, 2) for M in (Lm, Rm))
    s5 = sym and inter and ratio.is_number
    out["S5"] = {"XJ_symmetric": sym, "Killing_over_disc": str(ratio), "intertwines_Ad": inter, "holds": bool(s5)}
    say("S5 X J symmetric: %s; Killing(X, X)/disc = %s; M (XJ) M^T = (M X M^-1) J for L, R: %s  -> %s" % (
        sym, ratio, inter, bool(s5)))
    say()

    # S6 -- the real Killing form of sl(2, C)
    E = sp.Matrix([[0, 1], [0, 0]]); F = sp.Matrix([[0, 0], [1, 0]]); H = sp.Matrix([[1, 0], [0, -1]])
    basis = [E, F, H, sp.I * E, sp.I * F, sp.I * H]

    def coords(Z):
        # Z = sum c_k basis_k with real c_k: entries Z = [[u, v], [w, -u]]
        u, v, w = Z[0, 0], Z[0, 1], Z[1, 0]
        return [sp.re(v), sp.re(w), sp.re(u), sp.im(v), sp.im(w), sp.im(u)]

    ad = [sp.Matrix(6, 6, lambda i, j: coords(B * basis[j] - basis[j] * B)[i]) for B in basis]
    K = sp.Matrix(6, 6, lambda i, j: (ad[i] * ad[j]).trace())
    evK = K.eigenvals()
    posK = sum(m for v, m in evK.items() if v > 0)
    negK = sum(m for v, m in evK.items() if v < 0)
    s6 = (posK, negK) == (3, 3)
    out["S6"] = {"signature": [posK, negK], "holds": s6}
    say("S6 the Killing form of sl(2, C) as a real Lie algebra: signature (pos, neg) = (%d, %d)  -> %s" % (posK, negK, s6))
    say()

    # S7 -- the control: m003
    hol3, rel3 = snappy_holonomy("m003")
    s7 = True
    out["S7"] = {"relators": rel3, "gens": {}}
    for g3, A in hol3.items():
        r = is_so31_numeric(lorentz_numeric(A))
        out["S7"]["gens"][g3] = r
        s7 &= r["max_imag"] < 1e-9 and r["gram_resid"] < 1e-9 and abs(r["det"] - 1) < 1e-9 and r["Lambda00"] >= 1 - 1e-9
        say("S7 SnapPy m003 %s: gram residual %.1e; det %.12f; Lambda00 %.6f" % (g3, r["gram_resid"], r["det"], r["Lambda00"]))
    out["S7"]["holds"] = s7
    say("S7 -> %s" % s7)
    say()

    cells = {k: out[k]["holds"] for k in ("S1a", "S1b", "S2", "S3", "S4", "S5", "S6", "S7")}
    out["cells"] = cells
    say("CELLS: " + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in cells.items()))
    with open("cone_checks_out.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open("cone_checks.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
        fh.write("\n")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
