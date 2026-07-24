"""P2W3-L53 (OI-014) -- E6 all-orders local smoothness / Goldman-Millson formality at rho_prin.
B775 Phase-2 Wave-3 structural cell. FIREWALLED (deformation theory of flat connections, NOT physics).
Nothing to CLAIMS.md. Gate 5/5-Q: structural only, no SM values, one-number pin untouched.

THE OPEN ISSUE (OI-014/L53). B273 proved the quadratic cup obstruction H^1 x H^1 -> H^2(e6) vanishes
identically (Phi_2 = 0, integration to 2nd order); B274 added the cubic Phi_3 = 0 (3rd order) and CITED the
Menal-Ferrer--Porti smoothness criterion. The genuinely-open residual: is rho_prin an ALL-ORDERS smooth point
(a Goldman--Millson formality statement), or is there a computable obstruction at some finite order?

RESULT -- RESOLVED-A by reduction to named theorems, with every finite certificate reproduced IN-CELL in pure
python (no sage), a second and independent way, via the Kostant-exponent sl(2) block decomposition:

  e6 = (+)_{m in {1,4,5,7,8,11}} Sym^{2m}   under the principal sl(2)      (dims 3+9+11+15+17+23 = 78)

The figure-eight geometric rep is a = [[1,1],[0,1]], b = [[1,0],[t,1]], t = e^{i pi/3} (root of z^2 - z + 1);
it satisfies the relator abABaBAbaB (verified). rho_prin acts on each Sym^{2m} by this SL(2) rep, so Ad(a) =
exp(ad e), Ad(b) = exp(t ad f) -- exactly B273/B274's principal rep, now block by block.

  (C1) Twisted cohomology (both primes p = 99991, 100003):  per exponent block  h^0 = 0, h^1 = 1, h^2 = 1;
       totals  dim H^0(M) = 0,  dim H^1(M) = 6,  dim H^2(M) = 6.   [reproduces B264/B273/B274, pure python]
  (C2) Meridian mu = a is REGULAR unipotent: on each Sym^{2m} it is a SINGLE Jordan block, ker(mu - I) = 1;
       total ker = 6 = rank(E6).  (One Cartan direction per Kostant exponent.)
  (C3) Nonlinear check (in-cell, explicit sl(2) bracket): the m=1 = adjoint-sl(2) cup product H^1 x H^1 -> H^2
       is NON-vacuous (obstruction cochain q != 0) yet [q] = 0 in H^2 -- the smoothness witness, both primes.
       (The coupled full-e6 orders 2 and 3 are B273/B274, sage; reproduced here in the rank-1 shadow.)

THE REDUCTION (all-orders smoothness = formality), each arrow a named theorem or an in-cell integer identity:
  1. mu regular (C2)  ==Kostant 1963==>  the centralizer z(e) of the regular nilpotent is ABELIAN, dim = rank = 6.
     The longitude lambda commutes with mu, so lambda in exp(z(e)); an abelian algebra acts trivially on itself,
     so lambda fixes ker(mu - I) = z(e).  Hence  H^0(dM) = ker(mu-I) cap ker(lambda-I) = 6,  and on T^2 (chi = 0,
     Poincare duality H^0 = H^2)  dim H^1(dM) = 2 * H^0(dM) = 12 = 2 * rank.
  2. Poincare--Lefschetz "half-lives-half-dies" (named): for the compact 3-manifold M with torus boundary the
     image of H^1(M) -> H^1(dM) is a LAGRANGIAN, dim = (1/2) dim H^1(dM) = 6.
  3. dim H^1(M) = 6 (C1) = 6 = dim image  ==>  restriction H^1(M) -> H^1(dM) is INJECTIVE (rank = dim domain).
     [Injectivity is FORCED by the two computed 6's + half-lives-half-dies; not separately assumed.]
  4. Menal-Ferrer--Porti / Heusener--Porti smoothness (named): injective restriction + boundary variety smooth at
     rho|_dM (guaranteed by mu regular, z(e) abelian) ==> rho_prin is a SMOOTH point of X(M), dim = (1/2)dim H^1(dM) = 6.
  5. DIMENSION FORCING (the L53 payoff -- why smooth => formal). H^0(M) = 0 (C1) => rho_prin has finite centralizer
     => H^1(M) is the honest Zariski tangent space and the Goldman--Millson/Kuranishi map Phi = Phi_2 + Phi_3 + ...
     : H^1 -> H^2 cuts the germ as Phi^{-1}(0). A smooth point of dim 6 sitting inside H^1 of dim 6 means
     Phi^{-1}(0) is smooth of FULL ambient dimension, i.e. Phi^{-1}(0) = H^1 near 0, i.e. Phi == 0 to ALL ORDERS.
     Every higher Massey product <xi,...,xi> in H^2 is therefore cohomologically trivial: the controlling DGLA
     C^*(pi_1(4_1), Ad rho) is FORMAL at rho_prin, and the germ is the (identically-zero) quadratic cone = H^1.

So all-orders local smoothness / formality is REDUCED to {Kostant, Poincare-Lefschetz half-lives-half-dies,
Menal-Ferrer--Porti} + the in-cell certificates C1/C2, with the dimension-forcing step (5) supplying the missing
"smooth => all Massey products vanish" that B274 asserted but did not articulate. DISCRIMINATING FACT: the single
numerical coincidence dim H^1(M) = 6 = (1/2) dim H^1(dM) = (1/2)*12 with mu regular -- the exact MFP smoothness
signature -- which via half-lives-half-dies forces injectivity and hence (by dimension) Phi == 0 at every order.

FALSIFICATION GATES (the verdict block can emit RESOLVED-A / RESOLVED-B / UNRESOLVED):
  * any block h^1 != 1, or total (h0,h1,h2) != (0,6,6)                          -> reduction void -> UNRESOLVED
  * meridian not regular (some block ker(mu-I) != 1)                            -> reduction void -> UNRESOLVED
  * dim H^1(M) != (1/2) dim H^1(dM)  (i.e. 6 != 6)                              -> not a smooth pt -> UNRESOLVED
  * the nonlinear cup obstruction NONzero ([q] != 0 in H^2)                     -> obstruction at order 2 -> RESOLVED-B
  * the cup obstruction VACUOUS (q == 0, nothing tested)                        -> vacuity -> UNRESOLVED
  * all gates pass                                                              -> RESOLVED-A (formality reduced)

Env: pyenv python3 (NOT sage). Exact arithmetic mod two primes p = 1 mod 3 (so z^2 - z + 1 splits, t = e^{i pi/3}).
Run: python3 compute.py   (~5 s).
"""
import json, os
from math import comb

EXPO = [1, 4, 5, 7, 8, 11]
REL = "abABaBAbaB"
PRIMES = [99991, 100003]


# ---------- mod-p linear algebra (pure python) ----------
def froot(p):
    for t in range(p):
        if (t * t - t + 1) % p == 0:
            return t


def matmul(X, Y, p):
    k = len(Y)
    return [[sum(X[i][s] * Y[s][j] for s in range(k)) % p for j in range(len(Y[0]))] for i in range(len(X))]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def scal(c, X, p):
    return [[(c * X[i][j]) % p for j in range(len(X[0]))] for i in range(len(X))]


def madd(X, Y, p):
    return [[(X[i][j] + Y[i][j]) % p for j in range(len(X[0]))] for i in range(len(X))]


def matvec(X, v, p):
    return [sum(X[i][s] * v[s] for s in range(len(v))) % p for i in range(len(X))]


def expnil(M, p):
    n = len(M); R = eye(n); term = eye(n); k = 1
    while any(x % p for row in term for x in row) and k < 60:
        term = scal(pow(k, p - 2, p), matmul(term, M, p), p); R = madd(R, term, p); k += 1
    return R


def rank_mod(rows, p):
    rows = [r[:] for r in rows]; nr = len(rows); nc = len(rows[0]) if rows else 0; r = 0
    for col in range(nc):
        piv = next((i for i in range(r, nr) if rows[i][col] % p), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]; inv = pow(rows[r][col], p - 2, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(nr):
            if i != r and rows[i][col] % p:
                f = rows[i][col]; rows[i] = [(rows[i][j] - f * rows[r][j]) % p for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def cols_rank(colvecs, dim_out, p):
    """rank of the map whose columns are colvecs (each length dim_out)."""
    return rank_mod([[colvecs[c][r] for c in range(len(colvecs))] for r in range(dim_out)], p)


def in_span(colvecs, target, dim_out, p):
    base = cols_rank(colvecs, dim_out, p)
    return cols_rank(colvecs + [target], dim_out, p) == base


def kernel(colvecs, dim_in, dim_out, p):
    M = [[colvecs[c][r] for c in range(dim_in)] for r in range(dim_out)]
    M = [row[:] for row in M]; nr = len(M); nc = dim_in; pivc = []; r = 0
    for col in range(nc):
        piv = next((i for i in range(r, nr) if M[i][col] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][col], p - 2, p); M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nr):
            if i != r and M[i][col] % p:
                f = M[i][col]; M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(nc)]
        pivc.append(col); r += 1
        if r == nr:
            break
    free = [c for c in range(nc) if c not in pivc]; basis = []
    for fc in free:
        v = [0] * nc; v[fc] = 1
        for ri, pc in enumerate(pivc):
            v[pc] = (-M[ri][fc]) % p
        basis.append(v)
    return basis


def solve(A, b, p):
    nr = len(A); nc = len(A[0]); M = [A[i][:] + [b[i]] for i in range(nr)]; r = 0; pivc = []
    for col in range(nc):
        piv = next((i for i in range(r, nr) if M[i][col] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][col], p - 2, p); M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nr):
            if i != r and M[i][col] % p:
                f = M[i][col]; M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(nc + 1)]
        pivc.append(col); r += 1
    q = [0] * nc
    for ri, pc in enumerate(pivc):
        q[pc] = M[ri][nc]
    return q


# ---------- Sym^{2m} of a 2x2 matrix (basis x^{2m-k} y^k) ----------
def sym_power(g, twom, p):
    a, b, c, dd = g[0][0], g[0][1], g[1][0], g[1][1]; d = twom + 1
    M = [[0] * d for _ in range(d)]
    for k in range(d):
        coeff = {}
        for i in range(twom - k + 1):
            ci = comb(twom - k, i) * pow(a, i, p) * pow(c, twom - k - i, p) % p
            for j in range(k + 1):
                cj = comb(k, j) * pow(b, j, p) * pow(dd, k - j, p) % p
                xp = i + j; coeff[xp] = (coeff.get(xp, 0) + ci * cj) % p
        for xp, val in coeff.items():
            M[twom - xp][k] = val
    return M


# ---------- (C1)/(C2) block cohomology + meridian regularity ----------
def block_data(m, p):
    t = froot(p); d = 2 * m + 1
    a = [[1, 1], [0, 1]]; A = [[1, p - 1], [0, 1]]; b = [[1, 0], [t, 1]]; B = [[1, 0], [(p - t) % p, 1]]
    R = {ch: sym_power(g, 2 * m, p) for ch, g in [('a', a), ('A', A), ('b', b), ('B', B)]}
    P = eye(d)
    for ch in REL:
        P = matmul(P, R[ch], p)
    assert P == eye(d), f"relator fails on Sym^{2 * m}"
    I = eye(d)
    amI = [[(R['a'][i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    bmI = [[(R['b'][i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    d0 = [[amI[r][i] for r in range(d)] + [bmI[r][i] for r in range(d)] for i in range(d)]
    r0 = cols_rank(d0, 2 * d, p)

    def u_r(xa, xb):
        pref = eye(d); ur = [0] * d
        for ch in REL:
            xi = xa if ch.lower() == 'a' else xb
            term = matvec(pref, xi, p) if ch.islower() else matvec(pref, [(-x) % p for x in matvec(R[ch], xi, p)], p)
            ur = [(ur[i] + term[i]) % p for i in range(d)]; pref = matmul(pref, R[ch], p)
        return ur

    z = [0] * d
    d1 = [u_r([1 if j == i else 0 for j in range(d)], z) for i in range(d)] + \
         [u_r(z, [1 if j == i else 0 for j in range(d)]) for i in range(d)]
    r1 = cols_rank(d1, d, p)
    h0 = d - r0; h2 = d - r1; h1 = (2 * d - r1) - r0
    # meridian mu = a regular <=> ker(a - I) on Sym^{2m} is 1-dimensional (single Jordan block)
    ker_mu = d - cols_rank([[amI[r][i] for r in range(d)] for i in range(d)], d, p)
    return dict(m=m, dim=d, h0=h0, h1=h1, h2=h2, ker_mu=ker_mu)


# ---------- (C3) nonlinear sl(2)=adjoint (m=1) cup-product obstruction, explicit bracket ----------
def sl2_cup_obstruction(p):
    t = froot(p)
    ade = [[r % p for r in row] for row in [[0, -2, 0], [0, 0, 1], [0, 0, 0]]]
    adh = [[r % p for r in row] for row in [[2, 0, 0], [0, 0, 0], [0, 0, -2]]]
    adf = [[r % p for r in row] for row in [[0, 0, 0], [-1, 0, 0], [0, 2, 0]]]
    Ad = {'a': expnil(ade, p), 'A': expnil(scal(p - 1, ade, p), p),
          'b': expnil(scal(t, adf, p), p), 'B': expnil(scal((p - t) % p, adf, p), p)}
    P = eye(3)
    for ch in REL:
        P = matmul(P, Ad[ch], p)
    assert P == eye(3), "sl2 relator"
    adbasis = [ade, adh, adf]

    def adof(v):
        M = [[0] * 3 for _ in range(3)]
        for c, adm in zip(v, adbasis):
            if c % p:
                M = madd(M, scal(c, adm, p), p)
        return M

    def u_r(xa, xb):
        pref = eye(3); ur = [0, 0, 0]
        for ch in REL:
            xi = xa if ch.lower() == 'a' else xb
            term = matvec(pref, xi, p) if ch.islower() else matvec(pref, [(-x) % p for x in matvec(Ad[ch], xi, p)], p)
            ur = [(ur[i] + term[i]) % p for i in range(3)]; pref = matmul(pref, Ad[ch], p)
        return ur

    z = [0, 0, 0]
    d1 = [u_r([1 if j == i else 0 for j in range(3)], z) for i in range(3)] + \
         [u_r(z, [1 if j == i else 0 for j in range(3)]) for i in range(3)]
    Z1 = kernel(d1, 6, 3, p)
    I = eye(3)
    amI = [[(Ad['a'][i][j] - I[i][j]) % p for j in range(3)] for i in range(3)]
    bmI = [[(Ad['b'][i][j] - I[i][j]) % p for j in range(3)] for i in range(3)]
    B1 = [[amI[r][i] for r in range(3)] + [bmI[r][i] for r in range(3)] for i in range(3)]
    xi = next(zc for zc in Z1 if not in_span(B1, zc, 6, p))
    xa, xb = xi[:3], xi[3:]
    adxa, adxb = adof(xa), adof(xb)

    def factor(ch):
        axi = adxa if ch.lower() == 'a' else adxb; Mx = Ad[ch]; inv2 = pow(2, p - 2, p)
        if ch.islower():
            return [Mx, matmul(axi, Mx, p), scal(inv2, matmul(matmul(axi, axi, p), Mx, p), p)]
        return [Mx, scal(p - 1, matmul(Mx, axi, p), p), scal(inv2, matmul(Mx, matmul(axi, axi, p), p), p)]

    prod = [eye(3), [[0] * 3 for _ in range(3)], [[0] * 3 for _ in range(3)]]
    for ch in REL:
        Ff = factor(ch); N = [[[0] * 3 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if i + j <= 2:
                    N[i + j] = madd(N[i + j], matmul(prod[i], Ff[j], p), p)
        prod = N
    Aflat = [[adbasis[k][i][j] for k in range(3)] for i in range(3) for j in range(3)]
    tvec = [prod[2][i][j] for i in range(3) for j in range(3)]
    q = solve(Aflat, tvec, p)
    return dict(p=p, o1_zero=all(x % p == 0 for row in prod[1] for x in row),
                q_nonzero=any(x % p for x in q), cup_vanishes=in_span(d1, q, 3, p))


# ---------- driver + verdict ----------
def run(p):
    blocks = [block_data(m, p) for m in EXPO]
    H0 = sum(b['h0'] for b in blocks); H1 = sum(b['h1'] for b in blocks); H2 = sum(b['h2'] for b in blocks)
    ker_total = sum(b['ker_mu'] for b in blocks)
    merid_regular = all(b['ker_mu'] == 1 for b in blocks)
    H1_boundary = 2 * ker_total  # H^0(dM)=ker(mu-I)=6 (Kostant abelian z(e)); T^2 chi=0 => H^1(dM)=2*H^0
    cup = sl2_cup_obstruction(p)
    return dict(p=p, blocks=blocks, H0_M=H0, H1_M=H1, H2_M=H2, ker_mu_total=ker_total,
                merid_regular=merid_regular, H1_boundary=H1_boundary, cup=cup)


def verdict(runs):
    ok_cert = all(r['H0_M'] == 0 and r['H1_M'] == 6 and r['H2_M'] == 6 for r in runs)
    ok_merid = all(r['merid_regular'] and r['ker_mu_total'] == 6 for r in runs)
    ok_lag = all(r['H1_M'] == r['H1_boundary'] // 2 for r in runs)          # 6 == 12/2  (half-lives-half-dies)
    cup_vac = any(not r['cup']['q_nonzero'] for r in runs)                  # vacuity guard
    cup_nonzero = any(not r['cup']['cup_vanishes'] for r in runs)           # a real obstruction found
    cup_ok = all(r['cup']['cup_vanishes'] and r['cup']['q_nonzero'] and r['cup']['o1_zero'] for r in runs)
    if cup_nonzero:
        return "RESOLVED-B", "nonlinear cup obstruction [q]!=0 in H^2: a genuine obstruction at order 2"
    if not (ok_cert and ok_merid and ok_lag):
        return "UNRESOLVED", "MFP certificate failed (dims / meridian regularity / half-lives identity)"
    if cup_vac:
        return "UNRESOLVED", "cup obstruction vacuous (q==0), smoothness witness not exercised"
    if ok_cert and ok_merid and ok_lag and cup_ok:
        return ("RESOLVED-A",
                "all-orders local smoothness = formality: reduced to Menal-Ferrer--Porti + Poincare-Lefschetz "
                "half-lives-half-dies + Kostant, with in-cell certificates dim H^1(M)=6=(1/2)dim H^1(dM), meridian "
                "regular, and the dimension-forcing Phi==0 (H^1 dim 6 = smooth-germ dim 6 => all Massey products vanish)")
    return "UNRESOLVED", "unexpected certificate state"


if __name__ == "__main__":
    lines = []

    def out(s=""):
        print(s); lines.append(s)

    out("=== P2W3-L53 (OI-014): E6 all-orders local smoothness / Goldman-Millson formality at rho_prin ===")
    out("    FIREWALLED (deformation theory of flat connections, not physics). Pure python, exact mod p.\n")
    runs = []
    for p in PRIMES:
        r = run(p); runs.append(r)
        out(f"p = {p}")
        out("  block cohomology H^*(4_1, Sym^{2m}) per Kostant exponent m:")
        for b in r['blocks']:
            out(f"    m={b['m']:2d}  dim Sym={b['dim']:2d}   h0={b['h0']} h1={b['h1']} h2={b['h2']}   "
                f"ker(mu-I)={b['ker_mu']} ({'regular' if b['ker_mu'] == 1 else 'NOT regular'})")
        out(f"  totals: dim H^0(M)={r['H0_M']}, dim H^1(M)={r['H1_M']}, dim H^2(M)={r['H2_M']}   "
            f"| meridian regular: {r['merid_regular']} (ker total={r['ker_mu_total']}=rank E6)")
        out(f"  boundary: dim H^0(dM)=ker(mu-I)=6 (Kostant z(e) abelian) => dim H^1(dM)={r['H1_boundary']}=2*rank")
        out(f"  half-lives-half-dies: (1/2)dim H^1(dM)={r['H1_boundary'] // 2} = dim H^1(M)={r['H1_M']} "
            f"=> restriction injective, image Lagrangian")
        c = r['cup']
        out(f"  nonlinear sl(2)=adjoint(m=1) cup obstruction: cocycle o1=0:{c['o1_zero']}  "
            f"q nonzero (non-vacuous):{c['q_nonzero']}  [q]=0 in H^2:{c['cup_vanishes']}\n")

    v, reason = verdict(runs)
    out(f"VERDICT: {v}")
    out(f"  {reason}")
    out("  discriminating fact: dim H^1(M)=6=(1/2)dim H^1(dM)=(1/2)*12 with meridian regular -- the MFP smoothness")
    out("  signature; via half-lives-half-dies it forces injectivity, and the smooth 6-dim germ filling H^1 (dim 6)")
    out("  forces the Goldman-Millson map Phi==0 to all orders (all higher Massey products cohomologically vanish).")

    res = dict(
        cell="P2W3-L53", oi="OI-014", topic="E6 all-orders local smoothness / GM formality at rho_prin",
        firewalled=True, env="pyenv python3 (no sage)", primes=PRIMES,
        certificates=dict(
            dim_H0_M=runs[0]['H0_M'], dim_H1_M=runs[0]['H1_M'], dim_H2_M=runs[0]['H2_M'],
            meridian_regular=all(r['merid_regular'] for r in runs), ker_mu_total=runs[0]['ker_mu_total'],
            dim_H1_boundary=runs[0]['H1_boundary'],
            half_lives_identity=(runs[0]['H1_M'] == runs[0]['H1_boundary'] // 2),
            per_block_h1={b['m']: b['h1'] for b in runs[0]['blocks']}),
        nonlinear_cup=dict(non_vacuous=all(r['cup']['q_nonzero'] for r in runs),
                           vanishes=all(r['cup']['cup_vanishes'] for r in runs)),
        reduction=["Kostant 1963 (regular nilpotent centralizer abelian, dim=rank)",
                   "Poincare-Lefschetz half-lives-half-dies",
                   "Menal-Ferrer--Porti / Heusener--Porti smoothness criterion",
                   "dimension forcing: smooth dim6 germ in H^1 dim6 => Phi==0 all orders => DGLA formal"],
        both_primes_agree=(runs[0]['H1_M'] == runs[1]['H1_M'] == 6 and
                           runs[0]['cup']['cup_vanishes'] == runs[1]['cup']['cup_vanishes'] is True),
        verdict=v, reason=reason)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
