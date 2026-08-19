#!/usr/bin/env python3
"""
Appendix B -- the geodir dimension count, computed; and the adjective it does not cover.

## WHY THIS SCRIPT EXISTS

Scope (geodirscope) recorded that Proposition (geodir) is stated without proof or citation:
"It is a deformation-cohomology statement -- which H^1 is six-dimensional, and why it is
unobstructed -- and this paper does not compute it."  This computes the first half.  The
second half is NOT computed, and the script says so rather than eliding it.

STRUCTURE.  rho_0 factors through SL(2), so as a pi_1-module e6 decomposes by
principal-sl2 exponent into Sym^{2m}(V_2) for m in {1,4,5,7,8,11}, of dimensions
3+9+11+15+17+23 = 78, and twisted cohomology follows the decomposition.

THE REPRESENTATION, AND ITS CONTROL.  pi_1(4_1) = <a,b | a w = w b> with
w = b^-1 a b^-1 a^-1.  The parabolic pair A = [[1,1],[0,1]], B = [[1,0],[t,1]] satisfies
the relator exactly when t^2 - t + 1 = 0 -- so t is a primitive sixth root of unity and the
trace field is Q(sqrt(-3)), the figure-eight's.  That is what identifies this as the
geometric representation rather than another solution of the relator.

METHOD.  Fox calculus on the one-relator presentation, block by block:
dim Z^1 = 2d - rank[rho(dr/da) | rho(dr/db)], dim B^1 = d - dim H^0, H^1 = Z^1 - B^1.
Exact over F_p at three primes with 6 | p-1.

WHAT IS NOT COMPUTED: unobstructedness.  The twisted Euler characteristic of a knot
exterior is zero and H^0 = H^3 = 0, so dim H^2 = dim H^1 = 6 -- the obstruction space is
NOT zero and unobstructedness follows from no dimension count here.

No third-party dependencies.
"""

EXPS = [1, 4, 5, 7, 8, 11]                 # the exponents of E6
PRIMES = [997, 1009, 1021]
W = "BabA"                                  # w = b^-1 a b^-1 a^-1
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


REL = "a" + W + "B" + inv_word(W)           # r = a w b^-1 w^-1


def symp(M, n, p):
    a, b, c, d = M
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(n + 1):
        co = [0] * (n + 1)
        co[0] = 1
        deg = 0
        for _ in range(n - k):
            nw = [0] * (n + 1)
            for j in range(deg + 1):
                nw[j] = (nw[j] + co[j] * a) % p
                nw[j + 1] = (nw[j + 1] + co[j] * b) % p
            co, deg = nw, deg + 1
        for _ in range(k):
            nw = [0] * (n + 1)
            for j in range(deg + 1):
                nw[j] = (nw[j] + co[j] * c) % p
                nw[j + 1] = (nw[j + 1] + co[j] * d) % p
            co, deg = nw, deg + 1
        for j in range(n + 1):
            out[j][k] = co[j]
    return out


def mm(X, Y, p):
    k = len(Y)
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) % p for j in range(len(Y[0]))]
            for i in range(len(X))]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def minv(X, p):
    n = len(X)
    M = [list(X[i]) + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        pr = next(i for i in range(r, n) if M[i][c] % p)
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [v * iv % p for v in M[r]]
        for i in range(n):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(2 * n)]
        r += 1
    return [row[n:] for row in M]


def rank(X, p):
    M = [row[:] for row in X]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if M[i][c] % p), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [v * iv % p for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def block(m, tv, p):
    n, d = 2 * m, 2 * m + 1
    Ma, Mb = symp((1, 1, 0, 1), n, p), symp((1, 0, tv, 1), n, p)
    M = {'a': Ma, 'A': minv(Ma, p), 'b': Mb, 'B': minv(Mb, p)}
    R = eye(d)
    for ch in REL:
        R = mm(R, M[ch], p)
    if R != eye(d):
        raise AssertionError(f"the relator does not act trivially at m={m}")
    Da = [[0] * d for _ in range(d)]
    Db = [[0] * d for _ in range(d)]
    P = eye(d)
    for ch in REL:
        if ch == 'a':
            Da = [[(Da[i][j] + P[i][j]) % p for j in range(d)] for i in range(d)]
        elif ch == 'A':
            T = mm(P, M['A'], p)
            Da = [[(Da[i][j] - T[i][j]) % p for j in range(d)] for i in range(d)]
        elif ch == 'b':
            Db = [[(Db[i][j] + P[i][j]) % p for j in range(d)] for i in range(d)]
        elif ch == 'B':
            T = mm(P, M['B'], p)
            Db = [[(Db[i][j] - T[i][j]) % p for j in range(d)] for i in range(d)]
        P = mm(P, M[ch], p)
    Z1 = 2 * d - rank([Da[i] + Db[i] for i in range(d)], p)
    st = [[(Ma[i][j] - (1 if i == j else 0)) % p for j in range(d)] for i in range(d)] + \
         [[(Mb[i][j] - (1 if i == j else 0)) % p for j in range(d)] for i in range(d)]
    H0 = d - rank(st, p)
    return d, H0, Z1, Z1 - (d - H0)


print("=" * 78)
print("CONTROLS -- is this the geometric representation?")
print("=" * 78)
print(f"\n  presentation: pi_1(4_1) = <a,b | a w = w b>, w = b^-1 a b^-1 a^-1")
print(f"  relator word: {REL}")
res = {}
for p in PRIMES:
    tv = next((x for x in range(p) if (x * x - x + 1) % p == 0), None)
    gate(f"p={p}: t^2 - t + 1 has a root, so the trace field Q(sqrt(-3)) embeds",
         tv is not None)
    res[p] = {m: block(m, tv, p) for m in EXPS + [2, 3, 6]}
gate("the parabolic pair satisfies the relator in every block "
     "(checked inside the block routine)", True)
gate("the exponent blocks account for e6 exactly: 3+9+11+15+17+23 = 78",
     sum(2 * m + 1 for m in EXPS) == 78)
if FAILED:
    raise SystemExit("controls failed -- nothing may be read")

print()
print("=" * 78)
print("THE DIMENSION COUNT")
print("=" * 78)
p0 = PRIMES[0]
print(f"\n  {'exponent m':>10} {'dim Sym^2m':>11} {'H^0':>5} {'Z^1':>5} {'B^1':>5} {'H^1':>5}")
for m in EXPS:
    d, H0, Z1, H1 = res[p0][m]
    print(f"  {m:>10} {d:>11} {H0:>5} {Z1:>5} {d-H0:>5} {H1:>5}")
tot = sum(res[p0][m][3] for m in EXPS)
print(f"  {'':>10} {'':>11} {'':>5} {'':>5} {'total':>5} {tot:>5}")
gate("dim H^1 = 6, as Prop (geodir) states", tot == 6, str(tot))
gate("every prime agrees", len({tuple(res[p][m][3] for m in EXPS) for p in PRIMES}) == 1)
gate("H^0 = 0 in every block, so B^1 is full and the count is clean",
     all(res[p0][m][1] == 0 for m in EXPS))
gate("the split is 1 + 5: the exponent-1 block contributes 1 and the other five "
     "contribute 1 each", res[p0][1][3] == 1 and sum(res[p0][m][3] for m in EXPS[1:]) == 5)
gate("the exponent-1 block IS the embedded principal sl2 -- Sym^2(V_2) is the adjoint "
     "of sl2, of dimension 3", res[p0][1][0] == 3)

print()
print("=" * 78)
print("WHAT THIS DOES NOT SETTLE, AND ONE THING THE PAPER DOES NOT SAY")
print("=" * 78)
extra = {m: res[p0][m][3] for m in (2, 3, 6)}
gate("m = 2, 3, 6 are NOT exponents of E6, and they give dim H^1 = 1 as well",
     all(v == 1 for v in extra.values()), str(extra))
print(f"""
  So the per-block contribution of 1 is a property of THIS MANIFOLD and Sym^{{2m}}, not
  of which exponents E6 happens to have.  The six is therefore the NUMBER of exponents --
  that is, rank(E6) = 6 -- and the "1+5 split by exponent" is a way of counting, not a
  discovery about E6.  Stating it the other way round would overclaim, and the paper
  currently invites that reading.

  NOT COMPUTED HERE: unobstructedness.  Prop (geodir) says "the UNOBSTRUCTED E6 moduli",
  and this arc computes H^1 only.  The twisted Euler characteristic of a knot exterior is
  zero and H^0 = H^3 = 0, so dim H^2 = dim H^1 = 6: the obstruction space is NOT zero, and
  unobstructedness does not follow from any dimension count here.  It needs either genuine
  obstruction theory or a citation.  Registered as owed, not asserted.

  ALSO UNCHANGED: the proposition still cannot select what it assumes.  rho_0 is DEFINED
  using the principal embedding, so a statement computed at that point cannot distinguish
  it from other sl2-subalgebras.  (C6) remains a fully priced choice, exactly as its own
  scope already says -- this arc verifies the count, and changes nothing about selection.""")

RES = {"exponents": EXPS, "primes": PRIMES,
       "H1_by_exponent": {str(m): res[p0][m][3] for m in EXPS},
       "H0_by_exponent": {str(m): res[p0][m][1] for m in EXPS},
       "block_dims": {str(m): res[p0][m][0] for m in EXPS},
       "total_H1": tot, "sum_block_dims": sum(2 * m + 1 for m in EXPS),
       "split": [1, 5],
       "non_exponents_also_one": {str(m): extra[m] for m in extra},
       "trace_field_poly": "t^2 - t + 1",
       "unobstructedness_computed": False,
       "dim_H2_by_euler_characteristic": tot,
       "scope": ("The H^1 dimension count is computed exactly, at three primes with "
                 "6 | p-1, from Fox calculus on the one-relator presentation, block by "
                 "block under the principal-sl2 decomposition. UNOBSTRUCTEDNESS IS NOT "
                 "COMPUTED: the twisted Euler characteristic is zero and H^0 = H^3 = 0, "
                 "so dim H^2 = 6 and the obstruction space is non-zero; that half needs "
                 "obstruction theory or a citation and is registered as owed. The "
                 "proposition also still cannot select what it assumes -- rho_0 is defined "
                 "using the principal embedding -- so (C6) remains a fully priced choice.")}
print()
if FAILED:
    raise SystemExit(f"FAIL: {len(FAILED)} check(s) did not reproduce: {FAILED}")
print("PASS: every check reproduced exactly.")
