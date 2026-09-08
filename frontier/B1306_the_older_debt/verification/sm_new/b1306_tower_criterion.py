"""B1306 slice A, Q1-Q3 -- the SM seat's 2x2 criterion (sm:B1303) re-derived with main's own code (DESIGN_A sealed 815f34be).
Independent route: the words phi^n(a), phi^n(b) for phi: a -> aab, b -> ab are built explicitly; the FULL Fox Jacobian of the relators
phi^n(a) a^-1, phi^n(b) b^-1 is evaluated at every non-trivial character of H_1(Y_n) = coker(Phi^n - I) exactly modulo a prime q = 1 (mod m)
(own 2x2 Smith parametrisation); h^1(Y_n; psi) = 1 - rank J(psi). Controls: the support counts of B1301/B1303, rank J <= 1, det(J + I) = 1
(sm:B1304's unipotent lemma) and, coded separately, the seat's factorised product A(x_{n-1})...A(x_0) compared with J + I at every character
(the chain rule, both orders tested at n = 3). Q2: Y_20's order-41 characters (predicted h^1 = 0 on all 1680) and its order-11 ones (20 at 1) via
the product form, two primes. Q3: Y_24's 2-primary subgroup (1024 characters): support 123 = 3 + 24 + 96, no order 32; Y_12's as control."""
import json, sys, math
from collections import Counter
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
# ---------- words ----------
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
PHI = {'a': 'aab', 'b': 'ab'}; PHI['A'] = ''.join(INV[c] for c in reversed(PHI['a'])); PHI['B'] = ''.join(INV[c] for c in reversed(PHI['b']))
def phi_word(w): return ''.join(PHI[c] for c in w)
def phi_n(w, n):
    for _ in range(n): w = phi_word(w)
    return w
# ---------- integer 2x2 helpers ----------
def matmul(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def matpow(X, n):
    R = [[1, 0], [0, 1]]
    for _ in range(n): R = matmul(R, X)
    return R
PHIM = [[2, 1], [1, 1]]
def smith2(A):
    """Smith normal form of an integer 2x2 matrix: returns (d1, d2, U, V) with U A V = diag(d1, d2), d1 | d2, U, V unimodular"""
    A = [row[:] for row in A]; U = [[1, 0], [0, 1]]; V = [[1, 0], [0, 1]]
    def swap_rows(M, i, j): M[i], M[j] = M[j], M[i]
    def swap_cols(M, i, j):
        for r in M: r[i], r[j] = r[j], r[i]
    def add_row(M, i, j, c):   # row_i += c * row_j
        M[i] = [x + c * y for x, y in zip(M[i], M[j])]
    def add_col(M, i, j, c):   # col_i += c * col_j
        for r in M: r[i] += c * r[j]
    while True:
        # bring the smallest non-zero |entry| to (0,0)
        entries = [(abs(A[i][j]), i, j) for i in range(2) for j in range(2) if A[i][j]]
        if not entries: break
        _, i, j = min(entries)
        if i: swap_rows(A, 0, 1); swap_rows(U, 0, 1)
        if j: swap_cols(A, 0, 1); swap_cols(V, 0, 1)
        done = True
        if A[1][0]:
            c = A[1][0] // A[0][0]; add_row(A, 1, 0, -c); add_row(U, 1, 0, -c); done = done and A[1][0] == 0
        if A[0][1]:
            c = A[0][1] // A[0][0]; add_col(A, 1, 0, -c); add_col(V, 1, 0, -c); done = done and A[0][1] == 0
        if done and A[1][0] == 0 and A[0][1] == 0:
            if A[1][1] % A[0][0] != 0:      # enforce divisibility
                add_row(A, 0, 1, 1); add_row(U, 0, 1, 1); continue
            break
    d1, d2 = abs(A[0][0]), abs(A[1][1])
    return d1, d2, U, V
def modinv(a, q): return pow(a % q, q - 2, q)
def prime_1_mod(m, skip=()):
    q = m + 1
    while True:
        if q not in skip and all(q % p for p in range(2, int(q ** 0.5) + 1)): return q
        q += m
def prim_root_of_unity(m, q):
    # a primitive m-th root of unity in F_q (q = 1 mod m)
    for g in range(2, q):
        z = pow(g, (q - 1) // m, q)
        if all(pow(z, m // p, q) != 1 for p in set(factor(m))): return z
def factor(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f
def coker_matrix(n):
    A = matpow(PHIM, n); return [[A[0][0] - 1, A[0][1]], [A[1][0], A[1][1] - 1]]
def characters(n):
    """H_1(Y_n) = coker(Phi^n - I): (d1, d2) from the Smith form (invariant factors only) and the list of ALL non-trivial characters as
    exponent pairs (eu, ev) of a primitive m-th root of unity, m = d2 = the exponent: (u, v) = (eu, ev)/m with A^T (u, v) integral --
    enumerated by the defining condition, not by a transform"""
    A = coker_matrix(n); d1, d2, _, _ = smith2([[A[0][0], A[1][0]], [A[0][1], A[1][1]]]); m = d2
    out = []
    for eu in range(m):
        for ev in range(m):
            if eu == 0 and ev == 0: continue
            if (A[0][0] * eu + A[1][0] * ev) % m == 0 and (A[0][1] * eu + A[1][1] * ev) % m == 0: out.append((eu, ev))
    assert len(out) == d1 * d2 - 1, (n, len(out), d1 * d2)
    return d1, d2, out
def fox_eval(word, x, pa, pb, q):
    """d(word)/d x under psi (psi(a) = pa, psi(b) = pb in F_q); returns the scalar in F_q"""
    val = {'a': pa, 'A': modinv(pa, q), 'b': pb, 'B': modinv(pb, q)}
    tot = 0; prefix = 1
    for c in word:
        if c == x: tot = (tot + prefix) % q
        elif c == INV[x]: tot = (tot - prefix * val[c]) % q
        prefix = prefix * val[c] % q
    return tot
def analyse_level(n, verbose=True):
    d1, d2, chars = characters(n); m = d2
    q1 = prime_1_mod(m); q2 = prime_1_mod(m, skip=(q1,)); primes = [(q1, prim_root_of_unity(m, q1)), (q2, prim_root_of_unity(m, q2))]
    wa, wb = phi_n('a', n), phi_n('b', n)
    FIB = [0, 1]
    while len(FIB) < 2 * n + 3: FIB.append(FIB[-1] + FIB[-2])
    support = []; bad_rank = 0; bad_det = 0; bad_chain = 0; single_prime_false = 0
    for eu, ev in chars:
        zeros = []; ranks = []
        for q, z in primes:
            pa, pb = pow(z, eu, q), pow(z, ev, q)
            M = [[fox_eval(wa, 'a', pa, pb, q), fox_eval(wa, 'b', pa, pb, q)], [fox_eval(wb, 'a', pa, pb, q), fox_eval(wb, 'b', pa, pb, q)]]
            J = [[(M[0][0] - 1) % q, M[0][1] % q], [M[1][0] % q, (M[1][1] - 1) % q]]
            zero = all(v == 0 for r in J for v in r); zeros.append(zero)
            ranks.append(0 if zero else (1 if (J[0][0] * J[1][1] - J[0][1] * J[1][0]) % q == 0 else 2))
            if (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % q != 1: bad_det += 1
            P = [[1, 0], [0, 1]]
            for k in range(n):
                x = pow(pa, FIB[2 * k + 1], q) * pow(pb, FIB[2 * k], q) % q
                Ak = [[(1 + x) % q, x * x % q], [1, x]]
                P = [[sum(Ak[i][t] * P[t][j] for t in range(2)) % q for j in range(2)] for i in range(2)]
            if P != [[r[0] % q, r[1] % q] for r in M]: bad_chain += 1
        if max(ranks) == 2: bad_rank += 1
        if all(zeros): support.append((eu, ev))
        elif any(zeros): single_prime_false += 1
    orders = Counter(m // math.gcd(m, math.gcd(eu, ev)) for eu, ev in support)
    if verbose: print(f"  Y_{n}: H_1 = Z/{d1} + Z/{d2} ({d1 * d2} characters, primes {q1}, {q2}); |phi^n(a)| = {len(wa)}; support {len(support)} by order {dict(sorted(orders.items()))}; rank J = 2 (both primes agree): {bad_rank}; det(J + I) != 1: {bad_det}; product != J + I: {bad_chain}; zero modulo ONE prime only (false positives caught): {single_prime_false}")
    return dict(n=n, d=(d1, d2), primes=(q1, q2), support=len(support), orders={str(k): v for k, v in sorted(orders.items())}, bad_rank=bad_rank, bad_det=bad_det, bad_chain=bad_chain, single_prime_false=single_prime_false)
print("=== Q1: the full Fox Jacobian vs the criterion, n = 3 .. 9 ===")
res = {n: analyse_level(n) for n in range(3, 10)}
pred = {3: 3, 4: 0, 5: 20, 6: 27, 7: 56, 8: 0, 9: 147}
check("(a) support counts 3, 0, 20, 27, 56, 0, 147 at n = 3..9 (B1301/B1303)", all(res[n]["support"] == pred[n] for n in pred))
check("(b) rank J <= 1 on every non-trivial character (no h^1 >= 2)", all(res[n]["bad_rank"] == 0 for n in res))
check("(c) det(J + I) = 1 on every non-trivial character (sm:B1304's unipotent lemma, on the full Jacobian)", all(res[n]["bad_det"] == 0 for n in res))
check("(d) the seat's factorised product A(x_{n-1})...A(x_0) equals J + I at every character (the chain rule, left-multiplied)", all(res[n]["bad_chain"] == 0 for n in res))
check("(a') H_1 structures Y_3 (4,4), Y_5 (11,11), Y_6 (8,40), Y_7 (29,29), Y_8 (21,105), Y_9 (76,76)", all(res[n]["d"] == d for n, d in {3: (4, 4), 5: (11, 11), 6: (8, 40), 7: (29, 29), 8: (21, 105), 9: (76, 76)}.items()))
# ---------- Q2 / Q3: the product form on selected characters of large levels ----------
def product_h1(n, pa_exp, pb_exp, m, q, z):
    """h^1 via the factorised product for the character psi(a) = z^pa_exp, psi(b) = z^pb_exp (z a primitive m-th root in F_q)"""
    FIB = [0, 1]
    while len(FIB) < 2 * n + 3: FIB.append(FIB[-1] + FIB[-2])
    pa, pb = pow(z, pa_exp % m, q), pow(z, pb_exp % m, q); P = [[1, 0], [0, 1]]
    for k in range(n):
        x = pow(pa, FIB[2 * k + 1], q) * pow(pb, FIB[2 * k], q) % q
        Ak = [[(1 + x) % q, x * x % q], [1, x]]
        P = [[sum(Ak[i][t] * P[t][j] for t in range(2)) % q for j in range(2)] for i in range(2)]
    return 1 if P == [[1, 0], [0, 1]] else 0
def torsion_characters(n, p_order):
    """the characters of H_1(Y_n) of order dividing p_order, as exponent pairs relative to a primitive p_order-th root; via the defining condition"""
    A = coker_matrix(n); out = []
    for eu in range(p_order):
        for ev in range(p_order):
            if eu == 0 and ev == 0: continue
            if (A[0][0] * eu + A[1][0] * ev) % p_order == 0 and (A[0][1] * eu + A[1][1] * ev) % p_order == 0:
                g = math.gcd(p_order, math.gcd(eu, ev)); out.append((eu, ev, p_order // g))
    d1, d2, _, _ = smith2([[A[0][0], A[1][0]], [A[0][1], A[1][1]]]); return out, (d1, d2)
def count_support(n, chars, order, p_order):
    """characters of exact order `order` among chars (exponents relative to a primitive p_order-th root): h^1 = 1 iff P = I modulo BOTH primes"""
    q1 = prime_1_mod(p_order); q2 = prime_1_mod(p_order, skip=(q1,)); zs = [(q, prim_root_of_unity(p_order, q)) for q in (q1, q2)]
    c = 0
    for eu, ev, o in chars:
        if o != order: continue
        if all(product_h1(n, eu, ev, p_order, q, z) for q, z in zs): c += 1
    return c
print("=== Q2: Y_20's order-41 and order-11 characters (the even-level correction) ===")
chars41, d20 = torsion_characters(20, 41); chars11, _ = torsion_characters(20, 11)
print(f"  H_1(Y_20) = Z/{d20[0]} + Z/{d20[1]}; order-41 characters: {sum(1 for c in chars41 if c[2] == 41)}; order-11: {sum(1 for c in chars11 if c[2] == 11)}")
s41 = count_support(20, chars41, 41, 41); s11 = count_support(20, chars11, 11, 11)
print(f"  Y_20: h^1 = 1 on {s41} of the order-41 characters (zero modulo both primes); on {s11} of the order-11 characters")
check("Q2: nothing at 41 (0 of 1680) and Y_5's 20 at 11 -- sm:B1303's correction of B1301's forward list, reproduced", s41 == 0 and s11 == 20 and sum(1 for c in chars41 if c[2] == 41) == 1680)
print("=== Q3: the 2-primary subgroups of Y_12 (control) and Y_24 ===")
def two_primary_support(n):
    A = coker_matrix(n); d1, d2, _, _ = smith2([[A[0][0], A[1][0]], [A[0][1], A[1][1]]]); p2 = 1
    while d2 % (2 * p2) == 0: p2 *= 2
    chars, _ = torsion_characters(n, p2)
    q1 = prime_1_mod(p2); q2 = prime_1_mod(p2, skip=(q1,)); zs = [(q, prim_root_of_unity(p2, q)) for q in (q1, q2)]
    by_order = Counter()
    for eu, ev, o in chars:
        if all(product_h1(n, eu, ev, p2, q, z) for q, z in zs): by_order[o] += 1
    return len(chars), dict(sorted(by_order.items())), (d1, d2)
n12, s12, d12 = two_primary_support(12); n24, s24, d24 = two_primary_support(24)
print(f"  Y_12: H_1 = Z/{d12[0]} + Z/{d12[1]}; 2-primary characters {n12}; support by order {s12}")
print(f"  Y_24: H_1 = Z/{d24[0]} + Z/{d24[1]}; 2-primary characters {n24}; support by order {s24}")
check("Q3: Y_12's 2-primary support 123 = {2: 3, 8: 24, 16: 96} (control) and Y_24's is the same with no order-32 character", s12 == {2: 3, 8: 24, 16: 96} and s24 == {2: 3, 8: 24, 16: 96} and n24 == 1023)
json.dump(dict(levels={str(k): v for k, v in res.items()}, Y20=dict(order41_support=s41, order11_support=s11, H1=d20), Y12_2adic=s12, Y24_2adic=s24, fails=fails), open("b1306_tower_criterion.json", "w"), indent=1)
print("Q1-Q3:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)
