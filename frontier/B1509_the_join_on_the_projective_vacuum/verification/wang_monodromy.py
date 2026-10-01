"""B1509, post-run (computed after extension_index_run.txt): T3's mechanism checked directly on the fibre.

m004 fibres over the circle.  With u_k = m^k (n m^-1) m^-k, the Reidemeister-Schreier rewrite of the relator (level = exponent sum,
both generators weight 1) is  u1 u0^-2 u_-1 u0^-1,  so after conjugating by m:  u2 = u1 u0^-1 u1^2.  The fibre group F = <u0, u1> is
free of rank two; the monodromy is phi(u0) = u1, phi(u1) = u1 u0^-1 u1^2 (abelianised [[0,-1],[1,3]], char poly x^2 - 3x + 1, the
figure-eight's Alexander polynomial).

For A = mu rho_q (on F, A = rho_q: every u_k has exponent sum 0):  H^1(F; A) = Z^1/B^1, Z^1 = A^2 (the values on u0, u1; F is free),
B^1 = {((A(u0)-1)v, (A(u1)-1)v)}.  The stable letter acts by  (S z)(g) = A(m)^-1 z(m g m^-1) = A(m)^-1 z(phi(g)),  a map of cocycles
preserving B^1; S_A = mu^-1 S_rho.  With H^0(F; A) = 0, the Wang sequence gives H^1(M; A) = ker(S_A - 1), H^2(M; A) = coker(S_A - 1),
and cup with the fibration class is the natural map ker -> coker.  So e u c = 0 iff S_A has a Jordan block of size >= 2 at 1.

Checks:
  (a) the rewrite, letter by letter, and phi's relation in rho_q (exact, symbolic q);
  (b) the char poly of S_rho on Z^1 is (s-1)^4 times the monic Q(q, s) (Q from the control's printout), and on B^1 it is (s-1)^4;
  (c) at the six exceptional points: H^0(F; A) = 0, dim ker(S_A - 1) = 1 = h1(A), dim ker(S_A - 1)^2 = 2 at mu = -1 and 1 at +-i,
      and the Jordan block is present exactly where extension_index_run.txt has a1(W1) = 1 (e u c = 0);
  (d) a generic control (q = 2, all four central twists): ker(S_A - 1) = 0."""
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
WORD_R = "mnMNmNMnmN"
K = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3), sp.I)
POINTS = [("17-12sqrt2", 17 - 12 * sp.sqrt(2), -1, "-1"), ("17+12sqrt2", 17 + 12 * sp.sqrt(2), -1, "-1"),
          ("7-4sqrt3", 7 - 4 * sp.sqrt(3), sp.I, "i"), ("7+4sqrt3", 7 + 4 * sp.sqrt(3), sp.I, "i"),
          ("7-4sqrt3", 7 - 4 * sp.sqrt(3), -sp.I, "-i"), ("7+4sqrt3", 7 + 4 * sp.sqrt(3), -sp.I, "-i")]
U = {0: "nM", 1: "mnMM", 2: "mmnMMM"}          # u_k = m^k n m^-(k+1)
PHI = {"x": "y", "y": "yXyy"}                  # x = u0, y = u1;  phi(u0) = u1, phi(u1) = u1 u0^-1 u1^2


def rs_rewrite(word):
    """Reidemeister-Schreier over the transversal {m^k}: the relator as a word in the u_k, as (k, +-1) letters"""
    level, out = 0, []
    for ch in word:
        if ch == "m":
            level += 1
        elif ch == "M":
            level -= 1
        elif ch == "n":
            out.append((level, 1))
            level += 1
        elif ch == "N":
            out.append((level - 1, -1))
            level -= 1
    return out, level


def ballas(qq):
    t = qq / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


def word_matrix(mats, w):
    X = sp.eye(mats["m"].shape[0])
    for ch in w:
        X = X * (mats[ch] if ch.islower() else mats[ch.lower()].inv())
    return X


def fibre_data(mats_mn, dom):
    """rho on u0, u1, A(m)^-1, as DomainMatrices over dom"""
    conv = lambda M: DomainMatrix.from_Matrix(M).convert_to(dom)
    return conv(word_matrix(mats_mn, U[0])), conv(word_matrix(mats_mn, U[1])), conv(mats_mn["m"].inv())


def cocycle_value(word, g, z, dom, d):
    """z(word) for a cocycle on the free group <x, y> with values z['x'], z['y'] (Fox calculus)"""
    val = DomainMatrix.zeros((d, 1), dom)
    pre = DomainMatrix.eye(d, dom)
    for ch in word:
        if ch.islower():
            val = val + pre * z[ch]
            pre = pre * g[ch]
        else:
            ginv = g[ch.lower()].inv()
            val = val - pre * ginv * z[ch.lower()]
            pre = pre * ginv
    return val


def monodromy(u0, u1, minv, dom):
    """S on Z^1 = A^2 (coordinates (z_x, z_y)) and the coboundary map B: A -> Z^1"""
    d = u0.shape[0]
    g = {"x": u0, "y": u1}
    cols = []
    for j in range(2 * d):
        e = [DomainMatrix.zeros((d, 1), dom), DomainMatrix.zeros((d, 1), dom)]
        e[j // d] = DomainMatrix.from_list([[1 if i == j % d else 0] for i in range(d)], dom)
        z = {"x": e[0], "y": e[1]}
        top = minv * cocycle_value(PHI["x"], g, z, dom, d)
        bot = minv * cocycle_value(PHI["y"], g, z, dom, d)
        cols.append(top.vstack(bot))
    S = cols[0].hstack(*cols[1:])
    I = DomainMatrix.eye(d, dom)
    B = (u0 - I).vstack(u1 - I)
    return S, B


def rank(A):
    return A.rank()


def checks_symbolic():
    q, s = sp.symbols("q s")
    m, n = ballas(q)
    rw, lev = rs_rewrite(WORD_R)
    rel_ok = rw == [(1, 1), (0, -1), (0, -1), (-1, 1), (0, -1)] and lev == 0
    mats = {"m": m, "n": n}
    u = {k: word_matrix(mats, w) for k, w in U.items()}
    phi_rel = sp.simplify(u[2] - u[1] * u[0].inv() * u[1] * u[1]) == sp.zeros(4)
    dom = sp.QQ.frac_field(q)
    u0, u1, minv = fibre_data(mats, dom)
    S, B = monodromy(u0, u1, minv, dom)
    Q =-q * s ** 4 + 8 * q * s ** 3 + (q ** 2 - 16 * q + 1) * s ** 2 + 8 * q * s - q
    Qmonic = sp.expand(Q / (-q))
    char8_expr = sp.Poly([dom.to_sympy(c) for c in S.charpoly()], s).as_expr()
    quo, rem = sp.div(sp.Poly(char8_expr, s), sp.Poly((s - 1) ** 4, s))
    on_quotient_is_Q = rem.is_zero and sp.simplify(quo.as_expr() - Qmonic) == 0
    # S restricted to B^1 is A(m)^-1 (rho: unipotent): S B = B minv
    SB_is_Bminv = (S * B - B * minv).to_Matrix().applyfunc(sp.simplify) == sp.zeros(8, 4)
    abel = sp.Matrix([[0, -1], [1, 3]])
    return {"relator_rewrite_u1_u0^-2_u-1_u0^-1": rel_ok, "phi_relation_u2=u1_u0^-1_u1^2_in_rho_q": phi_rel,
            "abelianised_monodromy_charpoly": str(abel.charpoly(sp.Symbol("x")).as_expr()),
            "S_on_B1_equals_A(m)^-1": SB_is_Bminv,
            "charpoly_on_H1(F;rho_q)_equals_monic_Q": on_quotient_is_Q, "monic_Q": str(Qmonic),
            "charpoly_on_Z1_factored": str(sp.factor(char8_expr))}


def jordan_at_point(qq, mu):
    m, n = ballas(qq)
    mats = {"m": m, "n": n}
    u0, u1, minv_rho = fibre_data(mats, K)
    S_rho, B = monodromy(u0, u1, minv_rho, K)
    S = S_rho * K.from_sympy(1 / sp.sympify(mu))       # S_A = mu^-1 S_rho (A(m) = mu rho(m); A = rho on F)
    I8 = DomainMatrix.eye(8, K)
    N = S - I8
    h0F = 4 - rank(B)
    k1 = 8 - rank(N.hstack(B))
    k2 = 8 - rank((N * N).hstack(B))
    k3 = 8 - rank((N * N * N).hstack(B))
    return {"h0(F;A)": h0F, "dim ker(S_A-1) on H1(F;A)": k1, "dim ker(S_A-1)^2": k2, "dim ker(S_A-1)^3": k3}


def main():
    sym = checks_symbolic()
    run = json.loads((HERE / "extension_index_run.txt").read_text(encoding="utf-8"))
    a1 = {(r["q"], r["mu"]): r["W1 data (a0,a1,t0,r1)"][1] for r in run["exact"]}
    pts = []
    for label, qq, mu, ml in POINTS:
        j = jordan_at_point(qq, mu)
        block = j["dim ker(S_A-1)^2"] >= 2
        pts.append({"q": label, "mu": ml, **j, "jordan_block_at_1": block, "a1(W1) from the run": a1[(label, ml)],
                    "block_iff_a1(W1)=1": block == (a1[(label, ml)] == 1)})
    generic = []
    for mu, ml in ((1, "1"), (-1, "-1"), (sp.I, "i"), (-sp.I, "-i")):
        generic.append({"q": "2", "mu": ml, **jordan_at_point(sp.Integer(2), mu)})
    return {"symbolic": sym, "exceptional_points": pts, "generic_control": generic}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "wang_monodromy_run.txt").write_text(txt + "\n", encoding="utf-8")
