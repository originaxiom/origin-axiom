"""B1306 slice B, Q6 -- Park arXiv:2004.02087v2 eq (32) against its own F^+_{m(5_2)}, from the arXiv LaTeX SOURCE, with main's own series code.
The five a_i(x,q) are transcribed from FKexamples.tex (lines 655-670 of the e-print, fetched 2026-09-09); the blocks f_0, f_1 from the paper's
closed forms (same lines), f_2, f_3 from the paper's Q(q)-formulas -- controlled against its printed truncations. Convention A (the cloud's memo 183
section 3): y-hat acts on the right as F(x) -> F(qx), so the coefficient of x^{n+1/2} in A-hat F^+ is sum_i sum_d a_{i,d}(q) q^{i(n-d+1/2)} f_{n-d}(q).
Exact integer arithmetic in Q = q^{1/2}. Pre-registered PASS (branch (i) of the DESIGN): the x^{1/2}, x^{3/2} rows vanish identically, x^{5/2}
vanishes on the series, and the x^{7/2} coefficient equals q^13 f_0 (the cloud's defect), so the recursion's f_3 differs from Park's printed f_3."""
import sympy as sp, json, sys
q, x = sp.symbols('q x')
# --- eq (32) as typed in the source (Q = q^{1/2}; the prefactors q^{11/2}, q^{1/2} are written as Q^11, Q) ---
a0 = -q**9*x**7*(q**3*x+1)*(q**5*x**2-1)*(q**7*x**2-1)
a1_poly = (q**9*x**6+q**8*x**6-q**8*x**4-3*q**7*x**5-q**7*x**4-q**6*x**5+2*q**6*x**4+2*q**6*x**3+q**5*x**4-q**5*x**2-q**4*x**3-q**3*x**4-q**3*x**3+q**3*x**2+2*q**2*x**3+2*q**2*x**2-q*x**2-2*q*x+1)
a1 = x**2*(q*x+1)*(q**3*x+1)*(q**7*x-1)*a1_poly            # times q^{11/2}
a2_poly = (q**12*x**6+q**11*x**5-2*q**10*x**5-3*q**9*x**4+2*q**8*x**4-q**8*x**3+2*q**7*x**3-q**6*x**4-4*q**6*x**3-q**5*x**3-3*q**5*x**2+q**4*x**3+2*q**4*x**2+q**3*x-q**2*x**2-2*q**2*x+1)
a2 = -q**2*(q**2*x-1)*(q**2*x+1)*(q*x**2-1)*(q**7*x**2-1)*a2_poly
a3_poly = (q**16*x**6-2*q**13*x**5-q**13*x**4+q**11*x**4+2*q**10*x**4+2*q**10*x**3-q**9*x**4-q**8*x**3-q**8*x**2-q**7*x**3-q**7*x**2+2*q**6*x**3+2*q**6*x**2+q**5*x**2-q**3*x**2-3*q**3*x-q**2*x+q+1)
a3 = (q*x**2-1)*(q*x+1)*(q**3*x+1)*a3_poly                  # times q^{1/2}
a4 = (q*x+1)*(q*x**2-1)*(q**3*x**2-1)
HALF = {0: 0, 1: 11, 2: 0, 3: 1, 4: 0}                        # extra Q-exponent of the prefactor (Q^11 = q^{11/2}, Q = q^{1/2})
A = {}                                                        # A[i][d] = dict {Q-exponent: int}  (coefficient of x^d in a_i, in Q)
for i, ai in enumerate((a0, a1, a2, a3, a4)):
    P = sp.Poly(sp.expand(ai), x)
    A[i] = {}
    for (d,), cq in zip(P.monoms(), P.coeffs()):
        cp = sp.Poly(sp.expand(cq), q); A[i][d] = {2 * e[0] + HALF[i]: int(c) for e, c in zip(cp.monoms(), cp.coeffs())}
# --- series in Q (dict exp->int), truncated at Q^TOP ---
TOP = 2 * 60
def sadd(a, b, s=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + s * c
        if r[e] == 0: del r[e]
    return r
def smul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1 + e2
            if e <= TOP: r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}
def shift(a, k): return {e + k: c for e, c in a.items()}
def qpoly(expr):                                              # a Laurent polynomial in q -> series dict in Q
    expr = sp.expand(expr); out = {}
    for term in sp.Add.make_args(expr):
        c, e = term.as_coeff_exponent(q); out[2 * int(e)] = out.get(2 * int(e), 0) + int(c)
    return out
def sdiv(num, den):                                           # exact power-series division num/den in Q (den's lowest coefficient +-1)
    lo = min(den); c0 = den[lo]; assert abs(c0) == 1
    num = shift(num, -lo); den = shift(den, -lo); out = {}; rem = dict(num)
    while rem:
        e = min(rem)
        if e > TOP: break
        c = rem[e] * c0; out[e] = c; rem = sadd(rem, shift(den, e), -c)
        rem = {k: v for k, v in rem.items() if k <= TOP}
    return out
# --- the blocks from Park's own text ---
f0 = {}; f1 = {}
for j in range(0, 40):
    t = j * (j + 1) // 2
    f0 = sadd(f0, {2 * (t - 1): -((-1) ** j)})                                    # -q^{-1} sum (-1)^j q^{j(j+1)/2}
    for s in range(0, j + 1): f1 = sadd(f1, {2 * (t - 1 + s): -((-1) ** j)})     # -q^{-1} sum (-1)^j q^{j(j+1)/2} (1-q^{j+1})/(1-q)
f0 = {e: c for e, c in f0.items() if e <= TOP}; f1 = {e: c for e, c in f1.items() if e <= TOP}
f2 = sadd(smul(sdiv(qpoly(1 + q - q**2), qpoly(-q + q**3)), f0), smul(sdiv(qpoly(-1 - 2*q + q**2), qpoly(-q + q**3)), f1))
f3 = sadd(smul(sdiv(qpoly(-2 - q - q**2 + 2*q**3 + q**4 - q**5), qpoly(q**2 - q**4 - q**5 + q**7)), f0),
          smul(sdiv(qpoly(2 + q + 3*q**2 - q**3 - q**6), qpoly(q**2 - q**4 - q**5 + q**7)), f1))
F = {0: f0, 1: f1, 2: f2, 3: f3}
def show(s, lo=None, hi=None):
    ks = sorted(k for k in s if (lo is None or k >= lo) and (hi is None or k <= hi)); return " ".join(f"{s[k]:+d}q^{k/2:g}" for k in ks) or "0"
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label); fails.append(label) if not ok else None
# C1/C2: the printed truncations
printed = {0: {-1: -1, 0: 1, 2: -1, 5: 1, 9: -1, 14: 1, 20: -1, 27: 1}, 1: {-1: -1, 0: 1, 1: 1, 2: -1, 3: -1, 4: -1, 5: 1, 6: 1, 7: 1, 8: 1},
           2: {-1: -1, 0: 2, 1: 1, 2: -1, 3: -2, 4: -2, 5: 1, 6: 1, 7: 3, 8: 2, 10: -1}, 3: {0: 2, 1: 1, 2: -2, 3: -2, 4: -3, 6: 2, 7: 4, 8: 4, 9: 2, 11: -3}}
lim = {0: 35, 1: 9, 2: 11, 3: 12}
for j in range(4):
    mine = {e // 2: c for e, c in F[j].items() if e % 2 == 0 and e // 2 < lim[j]}
    check(f"f_{j}: the closed form / Q(q)-formula reproduces Park's printed series below O(q^{lim[j]})", mine == printed[j])
# the operator rows: coefficient of x^{n+1/2} = sum_d Row_n(d) f_{n-d},  Row_n(d) = sum_i a_{i,d} Q^{2i(n-d)+i}
def row(n, d):
    r = {}
    for i in range(5):
        if d in A[i]: r = sadd(r, shift(A[i][d], 2 * i * (n - d) + i))
    return r
for n in (0, 1):
    ok = all(row(n, d) == {} for d in range(0, n + 1)); check(f"x^{n}+1/2 equation vanishes IDENTICALLY as an operator (rows {list(range(n+1))} all zero)", ok)
def lhs(n):
    tot = {}
    for d in range(0, n + 1):
        tot = sadd(tot, smul(row(n, d), F[n - d]))
    return tot
l2 = lhs(2); check("x^{5/2} equation satisfied EXACTLY by Park's f_0, f_1, f_2 (all coefficients through Q^%d)" % TOP, {e: c for e, c in l2.items() if e <= TOP - 20} == {})
l3 = lhs(3); target = shift(f0, 26)
print("   [A-hat F+]_{x^{7/2}} =", show(l3, hi=70)); print("   q^13 f_0             =", show(target, hi=70))
check("x^{7/2} coefficient equals q^13 f_0 (the cloud's defect), through Q^%d" % (TOP - 20), {e: c for e, c in l3.items() if e <= TOP - 20} == {e: c for e, c in target.items() if e <= TOP - 20})
check("and it is NOT zero", bool(l3))
# the recursion's f_3 vs Park's: solve Row_3(0) f_3 = -(Row_3(1) f_2 + Row_3(2) f_1 + Row_3(3) f_0)
rhs = {}
for d in (1, 2, 3): rhs = sadd(rhs, smul(row(3, d), F[3 - d]), -1)
f3_rec = sdiv(rhs, row(3, 0)); diff = sadd(f3_rec, f3, -1)
print("   f_3(recursion) - f_3(Park) =", show(diff, hi=30))
check("the recursion's f_3 differs from Park's printed/rational f_3, first at q^3", diff and min(diff) == 6)
json.dump(dict(fails=fails, x72=show(l3, hi=90), target=show(target, hi=90), f3_diff=show(diff, hi=40)), open("b1306_park_eq32.json", "w"), indent=1)
print("Q6:", "PASS" if not fails else "FAIL"); sys.exit(1 if fails else 0)
