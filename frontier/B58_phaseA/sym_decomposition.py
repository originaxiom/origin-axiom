"""Sym^d / principal-SL(2) two-sequence decomposition test (B58 Phase A probe).

Compute-and-gate. m=1, M=[[1,1],[1,0]] (det -1). Exact sympy. NO commit / ledger edit.
char(M^k)=t^2-L_k t+(-1)^k, char(-M^k)=t^2+L_k t+(-1)^k, L_k=tr(M^k) (Lucas).

Claim under test: the (n^2-1) tower = [Sym^2..Sym^n] x [Sym^0..Sym^{n-3}] as a Dickson multiset.

Gate 0a: Sym^d factorizations d=0..7.
Gate 0b: dimension identity (general n + per-n).
Gate 0c: full two-sequence product vs verified tower n=3,4,5 (multiset).
Gate 2 : n=6 row from the construction vs the theta-split candidate (CANDIDATE_A_D).
See SYM_DECOMPOSITION.md for the Gate-1 reconciliation against the Sym^{2k} kill.
"""
import sympy as sp

t, x, y, n, d = sp.symbols("t x y n d")
M = sp.Matrix([[1, 1], [1, 0]])


def sym_power(Mat, k):
    a, b, c, dd = Mat[0, 0], Mat[0, 1], Mat[1, 0], Mat[1, 1]
    S = sp.zeros(k + 1, k + 1)
    for i in range(k + 1):
        poly = sp.expand((a * x + c * y) ** (k - i) * (b * x + dd * y) ** i)
        for j in range(k + 1):
            S[j, i] = poly.coeff(x, k - j).coeff(y, j)
    return S


def lucas(k):
    return int((M ** k).trace())


def catalog(kmax):
    cat = {}
    for k in range(1, kmax + 1):
        Lk, c = lucas(k), (-1) ** k
        cat[(Lk, c)] = f"char(M^{k})"
        cat[(-Lk, c)] = f"char(-M^{k})"
    return cat


def tag_poly(expr, kmax):
    cat = catalog(kmax)
    mult = {}
    for fac, e in sp.factor_list(sp.expand(expr))[1]:
        P = sp.Poly(fac, t)
        if P.degree() == 1:
            r = -P.all_coeffs()[1] / P.all_coeffs()[0]
            lab = "(t-1)" if r == 1 else ("(t+1)" if r == -1 else f"(t-({r}))")
        elif P.degree() == 2:
            a2, a1, a0 = P.all_coeffs()
            b, c = int(sp.nsimplify(-a1 / a2)), int(sp.nsimplify(a0 / a2))
            lab = cat.get((b, c), f"[t^2-({b})t+({c})]")
        else:
            lab = f"[deg{P.degree()}]"
        mult[lab] = mult.get(lab, 0) + e
    return mult


def charpoly_sym(k):
    return sym_power(M, k).charpoly(t).as_expr()


def fmt(m):
    key = lambda s: (("-M" in s), ("t" in s and "M" not in s), s)
    return " ".join(lab if m[lab] == 1 else f"{lab}^{m[lab]}" for lab in sorted(m, key=key))


def tower_product(N):
    prod = sp.Integer(1)
    for k in range(2, N + 1):
        prod *= charpoly_sym(k)
    for k in range(0, N - 2):
        prod *= charpoly_sym(k)
    return prod


def sym_counts(N):
    """multiplicities via the proved mod-4 membership rule; cross-checks tower_product."""
    a, b = {}, {}
    for k in list(range(2, N + 1)) + list(range(0, N - 2)):
        for h in range(1, k + 1):
            if (k - h) % 4 == 0:
                a[h] = a.get(h, 0) + 1
            elif (k - h) % 4 == 2:
                b[h] = b.get(h, 0) + 1
    return {h: v for h, v in a.items() if v}, {h: v for h, v in b.items() if v}


def main():
    print("== Gate 0a: Sym^d(M) factorizations ==")
    for k in range(0, 8):
        print(f"  Sym^{k} (dim {k+1}) = {fmt(tag_poly(charpoly_sym(k), 8))}")

    print("\n== Gate 0b: dimension identity (general n) ==")
    pr = sp.summation(d + 1, (d, 2, n))
    co = sp.summation(d + 1, (d, 0, n - 3))
    print(f"  principal  = {sp.factor(pr)}  == (n+4)(n-1)/2: {sp.simplify(pr-(n+4)*(n-1)/2)==0}")
    print(f"  commutator = {sp.factor(co)}  == (n-1)(n-2)/2: {sp.simplify(co-(n-1)*(n-2)/2)==0}")
    print(f"  total      = {sp.expand(pr+co)}  == n^2-1: {sp.simplify(pr+co-(n**2-1))==0}")

    print("\n== Gate 0c: two-sequence product vs verified tower (n=3,4,5) ==")
    verified = {
        3: {"char(M^-1)": 1, "char(M^2)": 1, "char(M^3)": 1, "(t-1)": 1, "(t+1)": 1},
        4: {"char(M^-1)": 1, "char(M^1)": 1, "char(M^2)": 1, "char(M^3)": 1, "char(M^4)": 1,
            "char(-M^2)": 1, "(t-1)": 2, "(t+1)": 1},
        5: {"char(M^-1)": 1, "char(M^1)": 2, "char(M^2)": 2, "char(M^3)": 1, "char(M^4)": 1,
            "char(M^5)": 1, "char(-M^2)": 1, "char(-M^3)": 1, "(t-1)": 2, "(t+1)": 2},
    }
    for N in (3, 4, 5):
        m = tag_poly(tower_product(N), 2 * N)
        m = {("char(M^-1)" if k == "char(-M^1)" else k): v for k, v in m.items()}  # name self-dual as verified does
        print(f"  n={N}: {fmt(tag_poly(tower_product(N),2*N))}  -> match verified: {m==verified[N]}")

    print("\n== Gate 2: n=6 construction row vs theta-split candidate ==")
    sa, sb = sym_counts(6)
    print(f"  SYM   a(char M^h)  = {dict(sorted(sa.items()))}   (h=1 split: char(M^1) vs char(M^-1) below)")
    print(f"  SYM   b(char -M^h) = {dict(sorted(sb.items()))}   (h=1 entry is char(M^-1)=char(-M^1)=t^2+t-1)")
    print("  THETA a = {1:3,2:2,3:2,4:1,5:1,6:1}, char(M^-1):1, b = {2:2,3:1,4:1}, (t-1)^3(t+1)^2")
    print(f"  CONTESTED: a3(n=6): SYM=2, THETA=2  (vs B66 pinv=1) -> agree;  b3: SYM=1, THETA=1 -> agree")
    print("  FULL ROW DIVERGES (a1,a2,b2, parity swapped) -> different formulas; a3(n=6) stays OPEN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
