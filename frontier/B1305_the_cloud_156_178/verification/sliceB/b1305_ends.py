"""B1305 slice B, Q1 -- the two ends of the colored Jones polynomial, re-derived with main's own code (DESIGN_B sealed fa793cf2).
J_n(4_1): GM eq. (166) (Habiro form), coded independently. J_n(3_1): two routes -- Habiro's cyclotomic expansion, and the U_q(sl2)
R-matrix eigenvalue formula for the closure of the 2-strand braid sigma^3 (T(2,3)) with the framing/orientation convention fixed ONLY
on n = 2 against the Jones polynomial; the two routes must agree at n = 3, 4. Then the ends at matched parity, the mirror, and the
B1227 reading: R(K) = top end / bottom end (constant term normalised to +1) obeys R(K*) = 1/R(K), so R^2 = 1 for an amphichiral knot.
Exact integer Laurent arithmetic (dicts); sympy only for the small-n R-matrix route."""
import json, sys
import sympy as sp
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
def lmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items(): r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}
def ladd(a, b, s=1):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) + s * c
    return {e: c for e, c in r.items() if c}
def factor(n, j):   # q^n + q^-n - q^j - q^-j
    f = {}
    for e, c in ((n, 1), (-n, 1), (j, -1), (-j, -1)): f[e] = f.get(e, 0) + c
    return {e: c for e, c in f.items() if c}
def J41(n):                                   # GM (166): 1 + sum_{m=1}^{n-1} prod_{j=1}^m (q^n + q^-n - q^j - q^-j)
    tot = {0: 1}; prod = {0: 1}
    for m in range(1, n):
        prod = lmul(prod, factor(n, m)); tot = ladd(tot, prod)
    return tot
def J31_habiro(n):                            # Habiro: sum_{k>=0} (-1)^k q^{-k(k+3)/2} prod_{j=1}^k (q^n + q^-n - q^j - q^-j)
    tot = {}; prod = {0: 1}
    for k in range(0, n):
        if k: prod = lmul(prod, factor(n, k))
        sh = -k * (k + 3) // 2
        tot = ladd(tot, {e + sh: c for e, c in prod.items()}, (-1) ** k)
    return tot
def mirror(d): return {-e: c for e, c in d.items()}
# ---- route 2 for the trefoil: R-matrix eigenvalues on V_{n-1} (x) V_{n-1} (spins j = (n-1)/2), sigma^3 closure, quantum dimensions
t = sp.symbols('t')                            # t = q^{1/4}
def qint(m): return (t ** (2 * m) - t ** (-2 * m)) / (t ** 2 - t ** -2)      # [m] with q = t^4, q^{1/2} = t^2
def J31_rmatrix(n, conv):
    """sum over J = 0..n-1 (integer spin of the summand V_J in V_{(n-1)/2}^{(x)2}) of eigenvalue^3 * [2J+1] / [n], eigenvalue
    lambda_J = (-1)^{(n-1)-J} q^{(C_J - 2 C_{(n-1)/2})/2 * s}, C_j = j(j+1), s = +-1 the orientation convention; times a framing
    factor q^{f * 3 * C_{(n-1)/2} * s} with f fixed on n = 2 -- conv = (s, f)"""
    s_, f_ = conv; jj = sp.Rational(n - 1, 2); C = lambda j: j * (j + 1)
    tot = 0
    for J in range(0, n):
        lam = (-1) ** ((n - 1) - J) * t ** (4 * sp.Rational(1, 2) * s_ * (C(J) - 2 * C(jj)))
        tot += lam ** 3 * qint(2 * J + 1)
    expr = sp.cancel(sp.together(tot / qint(n) * t ** (4 * f_ * 3 * C(jj) * s_)))
    expr = sp.expand(expr)
    d = {}
    for term in sp.Add.make_args(expr):
        c, e = term.as_coeff_exponent(t); assert c.is_integer and e.is_integer and e % 4 == 0, term
        d[int(e) // 4] = d.get(int(e) // 4, 0) + int(c)
    return {e: c for e, c in d.items() if c}
print("=== route 2 convention, fixed on n = 2 only (the Jones polynomial) ===")
target2 = J31_habiro(2); print("  Habiro J_2(3_1) =", dict(sorted(target2.items())))
conv = None
for s_ in (1, -1):
    for f_ in (sp.Rational(a, b) for a in range(-8, 9) for b in (1, 2, 3, 4, 6)):
        try: d = J31_rmatrix(2, (s_, f_))
        except AssertionError: continue
        if d == target2: conv = (s_, f_); break
    if conv: break
print("  convention found:", conv)
check("(a) an R-matrix convention reproduces J_2 exactly", conv is not None)
if conv:
    ok34 = all(J31_rmatrix(n, conv) == J31_habiro(n) for n in (3, 4))
    print("  n = 3:", dict(sorted(J31_rmatrix(3, conv).items())) == dict(sorted(J31_habiro(3).items())), " n = 4:", J31_rmatrix(4, conv) == J31_habiro(4))
    check("(a) the R-matrix route and the Habiro route agree exactly at n = 3 and n = 4 (independent formulas)", ok34)
# ---- the ends
L = 60; qq = [0] * (L + 1); qq[0] = 1
for n in range(1, L + 1):
    for i in range(L, n - 1, -1): qq[i] -= qq[i - n]         # (q;q)_inf
def bottom(d, N=24):
    lo = min(d); return [d.get(lo + i, 0) for i in range(N)]
def top(d, N=24):
    hi = max(d); return [d.get(hi - i, 0) for i in range(N)]
def stable(f, end, n1, n2, N=24):
    a, b = end(f(n1), N), end(f(n2), N); s = 0
    while s < N and a[s] == b[s]: s += 1
    return s, b[:s]
def name(v):
    if not v: return "?"
    sg = 1 if v[0] > 0 else -1; w = [sg * x for x in v]
    if w == qq[:len(w)]: return ("+" if sg > 0 else "-") + "(q;q)_inf"
    if w == [1] + [0] * (len(w) - 1): return ("+" if sg > 0 else "-") + "1"
    return "other"
print("=== the ends at matched parity ===")
res = {}
for knot, f in (("3_1 (Habiro's expansion)", J31_habiro), ("3_1 mirror (q -> 1/q)", lambda n: mirror(J31_habiro(n))), ("4_1", J41)):
    for end_name, end in (("bottom", bottom), ("top", top)):
        s, v = stable(f, end, 13, 15) if knot.startswith("3_1") else stable(f, end, 15, 16)
        res[(knot, end_name)] = (s, v); print(f"  {knot:<26} {end_name:<6} window {s:>2}  {v[:10]}  -> {name(v)}")
ok_b = name(res[("3_1 (Habiro's expansion)", "bottom")][1]).endswith("(q;q)_inf") and name(res[("3_1 (Habiro's expansion)", "top")][1]).endswith("1") \
    and res[("3_1 (Habiro's expansion)", "bottom")][0] >= 12 and res[("3_1 (Habiro's expansion)", "top")][0] >= 12
ok_41 = name(res[("4_1", "bottom")][1]) == "+(q;q)_inf" and name(res[("4_1", "top")][1]) == "+(q;q)_inf" and res[("4_1", "bottom")][0] >= 14
ok_m = name(res[("3_1 mirror (q -> 1/q)", "bottom")][1]).endswith("1") and name(res[("3_1 mirror (q -> 1/q)", "top")][1]).endswith("(q;q)_inf")
check("(b) 3_1: bottom end +-(q;q)_inf, top end trivial (windows >= 12); 4_1: (q;q)_inf at both ends (window >= 14)", ok_b and ok_41)
check("(c) the mirror trefoil has the ends swapped", ok_m)
# ---- (d) the B1227 reading: R = top / bottom as formal series on the stable window (constant terms normalised to +1)
def series_div(num, den, N):
    out = []
    for i in range(N):
        v = num[i] - sum(out[j] * den[i - j] for j in range(i)); out.append(v)   # den[0] = 1
    return out
def norm(v): return [x * (1 if v[0] > 0 else -1) for x in v]
def ratio(knot, N):
    top_v = norm(res[(knot, "top")][1][:N]); bot_v = norm(res[(knot, "bottom")][1][:N]); return series_div(top_v, bot_v, N)
N = 12
R41 = ratio("4_1", N); R31 = ratio("3_1 (Habiro's expansion)", N); R31m = ratio("3_1 mirror (q -> 1/q)", N)
part = series_div([1] + [0] * (N - 1), qq[:N], N)     # 1/(q;q)_inf = partition numbers
print(f"  R(4_1) = {R41}   R(3_1) = {R31}   R(3_1*) = {R31m}   partitions = {part}")
check("(d) R(4_1) = 1 exactly (2-torsion of a mirror-odd invariant on an amphichiral knot); R(3_1) = 1/(q;q)_inf and R(3_1*) = (q;q)_inf = 1/R(3_1)",
      R41 == [1] + [0] * (N - 1) and R31 == part and R31m == qq[:N])
json.dump(dict(convention=[str(x) for x in conv] if conv else None, ends={f"{k[0]} | {k[1]}": dict(window=v[0], series=v[1][:16]) for k, v in res.items()},
               R41=R41, R31=R31, R31m=R31m, fails=fails), open("b1305_ends.json", "w"), indent=1)
print("Q1:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)
