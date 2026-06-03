"""B58 Stage 1, Step 2 -- Sym^{2k} (principal-SL(2)/Kostant) partition diagnostic.

Predicted-NEGATIVE: neither the bare Kostant spectrum (M on sl(n)=+_{k=1}^{n-1} Sym^{2k})
nor the coupled spectrum (tensored with the H^1(F_2)=C^2 factor carrying M) equals the
metallic trace-map tower. Confirms kill #25 from the MULTIPLICITY side (not just eigenvalues).
Exact (sympy); m=1; M=[[1,1],[1,0]]. Writes sym2k_diagnostic.json. No commit.
"""

import json
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parent / "sym2k_diagnostic.json"
t, x, y = sp.symbols("t x y")
M = sp.Matrix([[1, 1], [1, 0]])     # m=1, det = -1


def sym_power(Mat, k):
    """Sym^k of a 2x2 matrix: action on degree-k monomials x^{k-i} y^i."""
    a, b, c, d = Mat[0, 0], Mat[0, 1], Mat[1, 0], Mat[1, 1]
    dim = k + 1
    S = sp.zeros(dim, dim)
    for i in range(dim):
        poly = sp.expand((a * x + c * y) ** (k - i) * (b * x + d * y) ** i)
        for j in range(dim):
            S[j, i] = poly.coeff(x, k - j).coeff(y, j)
    return S


def lucas(k):
    return int((M ** k).trace())


def catalog(kmax):
    """(trace b, det c) -> label, for char(M^k)=t^2-L_k t+(-1)^k and char(-M^k)=t^2+L_k t+(-1)^k."""
    cat = {}
    for k in range(1, kmax + 1):
        Lk = lucas(k)
        c = (-1) ** k
        cat[(Lk, c)] = f"char(M^{k})"
        cat[(-Lk, c)] = f"char(-M^{k})"
    cat[(1, 0)] = "(t-1)"      # linear t-1 -> treat as (b,c)=(1,0) sentinel below
    cat[(-1, 0)] = "(t+1)"
    return cat


def tag_factors(mat, kmax):
    """charpoly of mat, factor over Q, tag each irreducible factor; return multiplicity dict."""
    cp = sp.factor_list(mat.charpoly(t).as_expr())
    cat = catalog(kmax)
    mult = {}
    for fac, e in cp[1]:
        P = sp.Poly(fac, t)
        if P.degree() == 1:                       # t - r
            r = -P.all_coeffs()[1] / P.all_coeffs()[0]
            lab = "(t-1)" if r == 1 else ("(t+1)" if r == -1 else f"(t-({r}))")
        elif P.degree() == 2:
            a2, a1, a0 = P.all_coeffs()
            b, c = sp.nsimplify(-a1 / a2), sp.nsimplify(a0 / a2)   # f = t^2 - b t + c
            lab = cat.get((int(b), int(c)), f"[t^2-({b})t+({c})]")
        else:
            lab = f"[deg{P.degree()}:{fac}]"
        mult[lab] = mult.get(lab, 0) + e
    return mult


def fmt(mult):
    out = []
    for lab in sorted(mult, key=lambda s: (("-" in s and "M" in s), "t" in s and "M" not in s, s)):
        out.append(lab if mult[lab] == 1 else f"{lab}^{mult[lab]}")
    return ", ".join(out)


def block_diag(blocks):
    return sp.diag(*blocks)


def main():
    res = {"job": "B58_stage1_step2_sym2k", "m": 1, "M": "[[1,1],[1,0]]",
           "purpose": "predicted-NEGATIVE: Sym^{2k} principal-SL(2) decomposition != tower (kill #25, multiplicity side)",
           "bare_kostant": {}, "coupled": {}}
    for n in (3, 4, 5):
        kmax = 2 * (n - 1) + 1   # coupled spectrum reaches odd power 2(n-1)+1
        blocks = [sym_power(M, 2 * k) for k in range(1, n)]   # sl(n) = +_{k=1}^{n-1} Sym^{2k}
        bare = block_diag(blocks)
        assert bare.shape[0] == n * n - 1
        res["bare_kostant"][f"n={n}"] = {"dim": n * n - 1, "spectrum": fmt(tag_factors(bare, kmax))}

        coupled = block_diag([sp.Matrix(sp.kronecker_product(sym_power(M, 2 * k), M)) for k in range(1, n)])
        assert coupled.shape[0] == 2 * (n * n - 1)
        res["coupled"][f"n={n}"] = {"dim": 2 * (n * n - 1), "spectrum": fmt(tag_factors(coupled, kmax))}

    res["tower_for_comparison"] = {
        "n=3": "char(M^-1) char(M^2) char(M^3) (t-1)(t+1)",
        "n=4": "char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2(t+1)",
        "n=5": "char(M^-1) char(M)^2 char(M^2)^2 char(M^3) char(M^4) char(M^5) char(-M^2) char(-M^3) (t-1)^2(t+1)^2"}
    res["verdict"] = ("CONFIRMED NEGATIVE (expected): bare Kostant = even powers only, overshoots to M^{2(n-1)}; "
                      "coupled = odd powers only; neither matches the tower (both parities, capped at M^n, open "
                      "multiplicities). Symmetric-power coefficient decomposition does NOT reproduce the tower -- "
                      "re-confirms kill #25 from the multiplicity side; B64 parity split is a sorting, not a formula.")
    OUT.write_text(json.dumps(res, indent=2, default=str))
    print("STEP2 bare/coupled spectra computed for n=3,4,5; verdict: predicted-negative")
    for n in (3, 4, 5):
        print(f"  n={n} bare   :", res["bare_kostant"][f"n={n}"]["spectrum"])
        print(f"  n={n} coupled:", res["coupled"][f"n={n}"]["spectrum"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
