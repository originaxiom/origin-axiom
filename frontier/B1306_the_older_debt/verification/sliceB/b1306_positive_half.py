"""B1306 slice B, Q1 -- T-TOWER-LAW-POSITIVE-HALF (sm:B1304 addendum @ ca850d6b) re-derived with main's own Fox calculus of the half-deck.
h: a -> ab, b -> a (Psi on H_1; Psi^2 = the deck Phi). pi_1(Y_n) = <a, b | h^{2n}(x) = x> (the seat's proved presentation identity; B1306 A verified the
phi-presentation's supports 3, 0, 20, 27, 56, 0, 147 at n = 3..9, and the seat showed all three presentations agree on every character).
A Psi-eigencharacter class (m, u): u^2 = u + 1 mod m, u^{2n} = 1 mod m; psi(a) = zeta^u, psi(b) = zeta (a <-> phi, b <-> 1 in Z[phi]/(phi^{2n} - 1)).
Own computations (exact modulo two primes q = 1 mod m, agreement required):
 (a) P_n = Fox matrix of h^{2n} at psi from the WORDS h^{2n}(a), h^{2n}(b) (no factorisation assumed); N_0 = Fox matrix of h^e at psi from the words
     h^e(a), h^e(b), e = ord_m(u); checks: P_n = N_0^{2n/e}; tr N_0 = 1 + (-1)^e; N_0 fixes the coboundary vector; e odd => N_0^2 = I and P_n = I.
 (b) the conductor form <=> the odd-order form on every root u of x^2 - x - 1 mod m, m <= 4000 (own enumeration).
 (c) the converse's content at n <= NMAX: both orders even => P_n != I.  PASS = every class obeys (a)-(c) and the theorem's prediction."""
import sys, json
from sympy import Matrix, isprime, factorint
from sympy.matrices.normalforms import smith_normal_form
from sympy.ntheory import n_order
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 13
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
H = {'a': 'ab', 'b': 'a'}; H['A'] = ''.join(INV[c] for c in reversed(H['a'])); H['B'] = ''.join(INV[c] for c in reversed(H['b']))
def h_word(w): return ''.join(H[c] for c in w)
def h_n(w, n):
    for _ in range(n): w = h_word(w)
    return w
def modinv(a, q): return pow(a % q, q - 2, q)
def prime_1_mod(m, skip=()):
    q = m + 1
    while True:
        if q not in skip and isprime(q): return q
        q += m
def prim_root_of_unity(m, q):
    ps = list(factorint(m))
    for g in range(2, q):
        z = pow(g, (q - 1) // m, q)
        if all(pow(z, m // p, q) != 1 for p in ps): return z
def fox(word, x, val, q):
    """d(word)/dx at the character val (dict a,A,b,B -> F_q)"""
    tot = 0; prefix = 1
    for c in word:
        if c == x: tot = (tot + prefix) % q
        elif c == INV[x]: tot = (tot - prefix * val[c]) % q
        prefix = prefix * val[c] % q
    return tot
def evalw(word, val, q):
    r = 1
    for c in word: r = r * val[c] % q
    return r
def jac(k, val, q):           # Fox matrix of h^k at the character: rows = images of a, b; cols = d/da, d/db
    wa, wb = h_n('a', k), h_n('b', k)
    return [[fox(wa, 'a', val, q), fox(wa, 'b', val, q)], [fox(wb, 'a', val, q), fox(wb, 'b', val, q)]]
def mm(X, Y, q): return [[sum(X[i][k] * Y[k][j] for k in range(2)) % q for j in range(2)] for i in range(2)]
def mpow(X, n, q):
    R = [[1, 0], [0, 1]]
    for _ in range(n): R = mm(R, X, q)
    return R
def torsion_exponent(n):
    Phi = Matrix([[2, 1], [1, 1]]); A = Phi ** n - Matrix.eye(2); D = smith_normal_form(A); return abs(int(D[1, 1])), abs(int(D[0, 0]))
def divisors(m):
    out = [1]
    for p, k in factorint(m).items(): out = [d * p ** i for d in out for i in range(k + 1)]
    return sorted(out)
def classes(n):
    d2, d1 = torsion_exponent(n); out = []
    for m in divisors(d2):
        if m == 1: continue
        for u in range(m):
            if (u * u - u - 1) % m == 0 and pow(u, 2 * n, m) == 1: out.append((m, u))
    return d1, d2, out
fails = []
def check(label, ok):
    if not ok: fails.append(label)
    return ok
table = {}
print(f"(a),(c): Psi-eigencharacter classes of every level n <= {NMAX}, exact modulo two primes")
for n in range(2, NMAX + 1):
    d1, d2, cls = classes(n); rows = []
    for (m, u) in cls:
        e = n_order(u, m); e2 = n_order((-u) % m, m); assert (2 * n) % e == 0
        res = []
        for skip in ((), None):
            q = prime_1_mod(m) if skip == () else prime_1_mod(m, skip=(prime_1_mod(m),)); z = prim_root_of_unity(m, q)
            pa, pb = pow(z, u, q), z; val = {'a': pa, 'A': modinv(pa, q), 'b': pb, 'B': modinv(pb, q)}
            # psi is a character of Y_n: psi(h^{2n}(x)) = psi(x)
            ok_char = evalw(h_n('a', 2 * n), val, q) == pa and evalw(h_n('b', 2 * n), val, q) == pb
            P = jac(2 * n, val, q); N0 = jac(e, val, q); I = [[1, 0], [0, 1]]
            vcol = [(pa - 1) % q, (pb - 1) % q]
            fix_col = [(N0[0][0] * vcol[0] + N0[0][1] * vcol[1]) % q, (N0[1][0] * vcol[0] + N0[1][1] * vcol[1]) % q] == vcol
            fix_row = [(vcol[0] * N0[0][0] + vcol[1] * N0[1][0]) % q, (vcol[0] * N0[0][1] + vcol[1] * N0[1][1]) % q] == vcol
            res.append(dict(ok_char=ok_char, PI=(P == I), P_is_N0pow=(P == mpow(N0, 2 * n // e, q)), tr=(N0[0][0] + N0[1][1]) % q,
                            tr_ok=((N0[0][0] + N0[1][1] - (1 + (-1) ** e)) % q == 0), fix=(fix_col or fix_row), fixside=("col" if fix_col else "row" if fix_row else "-"),
                            N0sq=(mm(N0, N0, q) == I)))
        agree = all(res[0][k] == res[1][k] for k in ("ok_char", "PI", "P_is_N0pow", "tr_ok", "fix", "N0sq"))
        r = res[0]; pred = (e % 2 == 1) or (e2 % 2 == 1)
        rows.append(dict(m=m, u=u, e=e, e2=e2, predicted=pred, h1=int(r["PI"]), P_is_N0pow=r["P_is_N0pow"], tr_ok=r["tr_ok"], fix=r["fix"], fixside=r["fixside"],
                         N0sq_when_e_odd=(r["N0sq"] if e % 2 == 1 else None), agree=agree, ok_char=r["ok_char"]))
        check(f"n={n} (m={m},u={u}): psi is a character of Y_n", r["ok_char"]); check(f"n={n} (m={m},u={u}): two primes agree", agree)
        check(f"n={n} (m={m},u={u}): P_n = N_0^(2n/e)", r["P_is_N0pow"]); check(f"n={n} (m={m},u={u}): tr N_0 = 1 + (-1)^e", r["tr_ok"])
        check(f"n={n} (m={m},u={u}): N_0 fixes the coboundary vector", r["fix"])
        if e % 2 == 1: check(f"n={n} (m={m},u={u}): e odd => N_0^2 = I", r["N0sq"])
        check(f"n={n} (m={m},u={u}): theorem prediction {pred} matches h^1 = {int(r['PI'])}", pred == r["PI"])
    npred = sum(1 for r in rows if r["predicted"]); ncarry = sum(r["h1"] for r in rows); nboth = sum(1 for r in rows if not r["predicted"])
    nboth_carry = sum(r["h1"] for r in rows if not r["predicted"])
    table[n] = dict(H1=(d1, d2), classes=len(rows), predicted=npred, carry=ncarry, both_even=nboth, both_even_carry=nboth_carry, rows=rows)
    print(f"  n={n:2d}: H1=({d1},{d2}) classes {len(rows)} | theorem predicts h1=1 for {npred}, carry {ncarry} | both orders even {nboth}, of which carry {nboth_carry} | "
          + ", ".join(f"({r['m']},{r['u']}):e={r['e']},e'={r['e2']},h1={r['h1']},fix={r['fixside']}" for r in rows))
# (b) conductor form <=> odd-order form, m <= 4000
print("(b): conductor form <=> odd-order form on every root of x^2 - x - 1 mod m, m <= 4000")
pairs = 0; mism = []
for m in range(2, 4001):
    for u in range(m):
        if (u * u - u - 1) % m: continue
        pairs += 1; e = n_order(u, m); e2 = n_order((-u) % m, m)
        odd_form = (e % 2 == 1) or (e2 % 2 == 1)
        d = e if e % 2 == 1 else e // 2                       # the conductor: smallest d with u^{2d} = 1
        cond_form = (d % 2 == 1) and (pow(u, d, m) in (1, m - 1)) and (m % 5 != 0)
        if odd_form != cond_form: mism.append((m, u, e, e2, d))
print(f"  pairs (m, u): {pairs}; mismatches: {len(mism)} {mism[:5]}")
check("(b) the two forms are equivalent on all pairs with m <= 4000", not mism)
out = dict(NMAX=NMAX, fails=fails, table={n: {k: v for k, v in t.items() if k != 'rows'} for n, t in table.items()}, pairs_m_le_4000=pairs, mismatches=mism[:20])
json.dump(out, open("b1306_positive_half.json", "w"), indent=1)
print("FAILS:", len(fails)); [print("   ", f) for f in fails[:12]]
print("Q1:", "PASS" if not fails else "FAIL"); sys.exit(1 if fails else 0)
