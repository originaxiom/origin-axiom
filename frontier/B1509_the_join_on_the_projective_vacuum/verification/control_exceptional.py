"""B1509 control, run before the seal.  It reproduces a received result and reads no sealed quantity.

The audit lane (codex's second lane, CANONICAL_CUSP_PROOF.md section 6) reports: for Ballas' convex-projective family on m004
with a central meridian twist mu in mu_4, the defining 4 and its dual each have exactly one H^1 class at q = 17 +- 12 sqrt2
(mu = -1) and at q = 7 +- 4 sqrt3 (mu = +i or -i), and none at generic q != 1.  Recomputed here with own Fox calculus:
  - Ballas' generators as the lane transcribes them (affine_background.py), t = q/2:
      m = [[1,0,1,t-1],[0,1,1,t],[0,0,1,t+1/2],[0,0,0,1]],  n = [[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]];
    relator r = m w n^-1 w^-1 with w = n m^-1 n^-1 m; longitude l = n m^-1 n^-1 m m n^-1 m^-1 n.
  - The twist s multiplies both meridians.  For s != 1, h^1(pi; 4 (x) s) = 4 - rank Phi_s(dr/dn): Phi_s(m) - 1 = s rho(m) - 1 is
    invertible (rho(m) unipotent), and the fundamental formula ties the dr/dm block to the dr/dn block.  So the exceptional q at a
    fixed twist mu are the zeros of D(q, mu) = det Phi_mu(dr/dn).
  - h^1 is also computed directly (dim Z^1 - dim B^1) at each exceptional point, for the defining 4 and the dual, over the exact
    number field (a second route).
Nothing here differentiates in the twist variable, computes a root multiplicity in it, or builds any extension (the sealed
quantities)."""
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

q, s = sp.symbols("q s")
WORD_R = "mnMNmNMnmN"
WORD_L = "nMNmmNMn"


def ballas(qq):
    t = qq / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


def rep(K, qq, mu, dual=False):
    m, n = ballas(qq)
    M = {"m": DomainMatrix.from_Matrix(mu * m).convert_to(K), "n": DomainMatrix.from_Matrix(mu * n).convert_to(K)}
    if dual:
        M = {k: v.inv().transpose() for k, v in M.items()}
    M["M"], M["N"] = M["m"].inv(), M["n"].inv()
    return M


def word(M, w):
    X = DomainMatrix.eye(M["m"].shape[0], M["m"].domain)
    for ch in w:
        X = X * M[ch]
    return X


def fox(M, w):
    d = M["m"].shape[0]
    K = M["m"].domain
    D = {"m": DomainMatrix.zeros((d, d), K), "n": DomainMatrix.zeros((d, d), K)}
    pre = DomainMatrix.eye(d, K)
    for ch in w:
        g = ch.lower()
        if ch.islower():
            D[g] = D[g] + pre
        else:
            D[g] = D[g] - pre * M[ch]
        pre = pre * M[ch]
    return D


def h1(M):
    d = M["m"].shape[0]
    K = M["m"].domain
    D = fox(M, WORD_R)
    J = D["m"].hstack(D["n"])
    d0 = (M["m"] - DomainMatrix.eye(d, K)).vstack(M["n"] - DomainMatrix.eye(d, K))
    return (2 * d - J.rank()) - d0.rank(), d - d0.rank()


def main():
    out = {}
    Kq = sp.QQ.frac_field(q)
    M1 = rep(Kq, q, 1)
    out["relator_holds"] = word(M1, WORD_R) == DomainMatrix.eye(4, Kq)
    ell = word(M1, WORD_L).to_Matrix()
    X = sp.symbols("X")
    out["longitude_charpoly_is_(X-q)^3(X-q^-3)"] = sp.cancel(ell.charpoly(X).as_expr() - (X - q) ** 3 * (X - q ** -3)) == 0
    Kqs = sp.QQ.frac_field(q, s)
    Ms = rep(Kqs, q, s)
    Dqs = Ms["m"].domain.to_sympy(fox(Ms, WORD_R)["n"].det())
    num = sp.factor(sp.numer(sp.together(Dqs)))
    out["D(q,s)_numerator_factored"] = str(num)
    exc = {}
    for label, mu, ext in (("-1", -1, [sp.sqrt(2), sp.sqrt(3)]), ("i", sp.I, [sp.sqrt(2), sp.sqrt(3)]), ("-i", -sp.I, [sp.sqrt(2), sp.sqrt(3)])):
        f = sp.expand(num.subs(s, mu))
        P = sp.Poly(f, q)
        re = sp.Poly([sp.re(c) for c in P.all_coeffs()], q)
        im = sp.Poly([sp.im(c) for c in P.all_coeffs()], q)
        g = sp.gcd(re, im) if not im.is_zero else re
        roots = [r for r in g.all_roots() if r.is_real and r > 0]
        cand = sorted({sp.nsimplify(sp.N(r, 80), ext) for r in roots}, key=lambda x: float(x))
        rows = []
        for r in cand:
            if r == 1:
                rows.append({"q": "1", "note": "q = 1 is the hyperbolic point, outside the family's q != 1"})
                continue
            assert sp.simplify(f.subs(q, r)) == 0, (label, r)
            K = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3), sp.I)
            hd, h0d = h1(rep(K, r, mu))
            hu, h0u = h1(rep(K, r, mu, dual=True))
            rows.append({"q": str(r), "h1_defining": hd, "h0_defining": h0d, "h1_dual": hu, "h0_dual": h0u})
        exc[label] = {"gcd_poly_in_q": str(g.as_expr()), "positive_real_roots": rows}
    out["exceptional"] = exc
    generic = []
    for qq in (sp.Rational(1, 3), sp.Rational(2), sp.Rational(5), sp.Rational(17)):
        K = sp.QQ.algebraic_field(sp.I)
        generic.append({"q": str(qq), **{f"mu={lab}": h1(rep(K, qq, mu))[0] for lab, mu in (("1", 1), ("-1", -1), ("i", sp.I), ("-i", -sp.I))}})
    out["generic_samples_h1"] = generic
    return out


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True)
    print(txt)
    if "--record" in sys.argv:
        Path(__file__).with_name("control_exceptional_run.txt").write_text(txt + "\n", encoding="utf-8")
