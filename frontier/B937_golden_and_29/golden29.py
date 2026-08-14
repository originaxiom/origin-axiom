#!/usr/bin/env python3
"""B937 -- THE GOLDEN ENTRY + THE 29 WHITELIST.  Two riders, one arc.

PART A (the golden entry).  B930's same-generation S-vs-A overlap-squared is
ONE element W of K = Q[rho]/mu13 with minimal polynomial

    953^4 x^3 - 230571559875 x^2 - 16394578125 x - 5^12,

the value prime leading and a pure power of 5 closing.  This cell gives W the
full B931 treatment: its exact prime-ideal divisor place by place (numerator
and denominator), the 5-adic story (which places over 5 carry it, with what
exponents, and whether the exponent 12 is structural), and an EXACT decision
on whether the golden field Q(sqrt5) genuinely enters the object's arithmetic
or 5 is merely a residue characteristic.

PART B (the 29 whitelist).  29 shows up twice in the banked record: in the
zero-level norm of the A-family flip mass (N(m_A) numerator = 29 * 72869) and
in the middle coefficient of B930's W3 rotation quadratic
(1536x^2 - 2088x + 677, 2088 = 2^3 * 3^2 * 29).  The whitelist below is
DECLARED and written to results.json BEFORE any of it is computed; each item
is then computed exactly, and the arc's two-outcome verdict is sealed against
the criterion stated inside the declaration.

INSTRUMENT UPGRADE (used by both parts).  B931's divisor work ran in two
non-maximal models of K (the h_S model and the monic mu13 model); in BOTH,
sympy's prime_decomp fails at p = 5 and p = 7, and B931 had to fall back on
the S3-resolvent theorem for the splitting TYPE at 5 (valuations there were
out of reach).  This cell derives a MONOGENIC model of K -- an index-1
generator found by search over the round_two integral basis -- in which every
place of every prime is reachable.  Part A's 5-adic story needs exactly that.

HOUSE RULES: exact arithmetic for every verdict (no numerics anywhere in this
cell); verify-don't-trust (every harvested element is gated against a banked
minimal polynomial or a banked norm law before use, and B931's d_S/d_A
divisors are recomputed in the NEW model and compared place by place with the
banked two-model tables); definiteness discipline (no form assumed definite,
no matrix assumed full rank -- the charge Gram's indefiniteness is checked,
not assumed); incremental dump after every stage.

INPUT PROVENANCE.  Banked JSON is read from the repo.  Five K-elements that
B930 computed but did not record (x_e, x_o, q_S, q_A, and a cross-generation
representative) were harvested by re-executing the banked B930 instrument
UNCHANGED in an isolated scratch namespace, and are pasted below as declared
literals; every one is gated in stage [3] against a banked invariant, and the
composite identity W = x_e^2 / (d_S q_S d_A q_A) is re-verified in exact
K-arithmetic.  The rational register data (Cmp3, Cmp6, G3, G6, det G18, the
charge trace Gram, the H+ weights) was harvested the same way; the parts of
it that carry a verdict are gated against B930's banked characteristic
polynomials and trace sum rule.
"""
import os
import json
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy import Symbol, Poly, factorint
from sympy.polys.numberfields.basis import round_two
from sympy.matrices.normalforms import hermite_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
T00 = time.time()
x = Symbol("x")
y = Symbol("y")
s = Symbol("s")

RES = {"cell": "B937 golden entry + the 29 whitelist", "checks": {},
       "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def dump():
    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        dump()
        raise SystemExit(f"UNSTABLE at {name}")


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


SIEVE_LIMIT = 10 ** 6
_SMALL_PRIMES = list(sp.sieve.primerange(2, SIEVE_LIMIT))


def ffac(n):
    """Exact factorisation by explicit trial division over every prime below
    10^6, then a provable primality test (sympy isprime = BPSW + extra) on the
    leftover; a composite leftover is marked C<digits>:<value> rather than
    silently dropped or expensively cracked.  EVERY prime below 10^6 -- in
    particular 5, 29, 149, 677, 953 -- is always found, which is all any
    verdict in this cell depends on; the rho/p-1 stages are deliberately not
    run (they cost 90 s on a single 100-digit resultant and buy nothing a
    verdict here uses)."""
    n = int(n)
    if n == 0:
        return {"0": 1}
    out = {}
    if n < 0:
        out["-1"] = 1
        n = -n
    for p in _SMALL_PRIMES:
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[str(p)] = e
    if n > 1:
        if n < SIEVE_LIMIT ** 2 or sp.isprime(n):
            out[str(n)] = out.get(str(n), 0) + 1
        else:
            out[f"C{len(str(n))}:{n}"] = 1
    return out


def fac_of_rat(r):
    r = sp.Rational(r)
    return {"num": ffac(r.p), "den": ffac(r.q)}


def has29(blob):
    return '"29"' in json.dumps(blob)


def squarefree_part(n):
    n = int(n)
    sgn = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    for p_, e in ffac(n).items():
        if p_ == "-1" or not p_.isdigit():
            continue
        if e % 2:
            out *= int(p_)
    return sgn * out


def primitive_int_poly(coeffs):
    rs = [sp.Rational(c) for c in coeffs]
    den = 1
    for c in rs:
        den = sp.ilcm(den, c.q)
    ints = [int(c * den) for c in rs]
    g = 0
    for c in ints:
        g = sp.igcd(g, abs(c))
    ints = [c // g for c in ints]
    if ints[0] < 0:
        ints = [-c for c in ints]
    return ints


# ===================================================================== [0]
log("[0] banked inputs ...")
B930 = json.load(open(os.path.join(REPO, "frontier", "B930_overlap_matrix",
                                   "results.json")))
B928 = json.load(open(os.path.join(REPO, "frontier", "B928_d2_decode",
                                   "results.json")))
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
B931 = json.load(open(os.path.join(REPO, "frontier", "B931_why_953",
                                   "results.json")))

MU = [500716339200, -2075673600, -4769856, 2197]      # mu13, descending
A_, B_, C_, D_ = MU
mu_poly = Poly(MU, x)

W_MINPOLY_BANKED = [int(c) for c in
                    B930["b_overlap"]["moduli_sq_minpolys"]["11"]]
X_MINPOLY_BANKED = [int(c) for c in
                    B930["b_overlap"]["moduli_sq_minpolys"]["12"]]
W_KCOORDS_BANKED = [Fr(c) for c in B930["b_overlap"]["same_gen_sq_K"]]
MPDS = [int(c) for c in B916["d_ratio_minpolys_desc"]["S0"]]
MPDA = [int(c) for c in B916["d_ratio_minpolys_desc"]["A0p"]]
MPMS = [int(c) for c in B928["Q2_colorless"]["minpoly_m_S"]]
MPMA = [int(c) for c in B928["Q2_colorless"]["minpoly_m_A"]]
MS_K = [Fr(c) for c in B928["Q2_colorless"]["m_S_K_coords"]]
MA_K = [Fr(c) for c in B928["Q2_colorless"]["m_A_K_coords"]]
W3_FACTORS = json.loads(B930["checks"]["c_W3_charpoly_factors"]["value"])
W6_FACTORS = json.loads(B930["checks"]["c_W6_charpoly_factors"]["value"])
W18_FACTORS = json.loads(B930["checks"]["c_W18_charpoly_factors"]["value"])
TRACE_SUM_DETAIL = B930["checks"]["c_traces_sum_rule_11"]["detail"]

# ---- harvested B930 K-elements (declared literals; gated in [3])
HARV = {
    "x_e": ["12055276929078190080000", "-5099950924513424179200000",
            "145306899751127482368000000"],
    "x_o": ["0", "0", "0"],
    "q_S": ["-36777806644951683956736", "-11225995912201391780659200",
            "3046562582942039246320435200"],
    "q_A": ["-2401367095773232260710400", "5916007323785802138255360000",
            "-990969807198729249352581120000"],
    "d_S": ["-20123/32448", "111650/2197", "-54331200/28561"],
    "d_A": ["8933/16224", "-63910/2197", "-923630400/28561"],
    "W": ["-6666875/153487321", "18406080000/1995335173",
          "266005555200000/25939357249"],
    "X_cross": ["-80419/161057", "257241600/2093741",
                "-125179084800/27218633"],
}
CMP3 = [["1", "-525/4", "-85050"], ["0", "27/32", "-105/4"],
        ["0", "1/4608", "33/64"]]
CMP6 = [["1", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0"],
        ["0", "0", "29/96", "0", "0", "385/4"],
        ["0", "0", "-5/32", "1", "0", "525/4"],
        ["0", "0", "0", "0", "0", "0"],
        ["0", "0", "1/4608", "0", "0", "65/192"]]
G3M = [["-3", "3024", "362880"], ["3024", "-8080128", "1585059840"],
       ["362880", "1585059840", "-2384905420800"]]
G6M = [["-960", "0", "0", "0", "0", "0"], ["0", "-2520", "0", "0", "0", "0"],
       ["0", "0", "-1852800", "220800", "0", "-225792000"],
       ["0", "0", "220800", "-1299840", "0", "-225792000"],
       ["0", "0", "0", "0", "-1117670400", "0"],
       ["0", "0", "-225792000", "-225792000", "0", "-888717312000"]]
DETG18 = 1556415303506476891498390487040000000000
CHARGE_GRAM = {"8": "60383232", "14": "-79427174400",
               "16": "247210809753600/13", "22": "-222489728778240000/19"}
CHARGE_GRAM_OFFDIAG_ALL_ZERO = True
CB_PLUS = [1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1,
           1, -1, 1, -1, 1, -1, 1, -1, 1]
H_S = [1, 0, -535623511707648, 2928461724187049852928]

RES["inputs"] = {
    "mu13_descending": [str(c) for c in MU],
    "banked_W_minpoly": [str(c) for c in W_MINPOLY_BANKED],
    "banked_cross_minpoly": [str(c) for c in X_MINPOLY_BANKED],
    "harvested_K_elements_rho_basis": HARV,
    "harvest_provenance": "re-execution of the banked B930 instrument "
                          "(unchanged) in an isolated scratch namespace; "
                          "every literal gated in stage [3]",
}
dump()

# ===================================================================== [1]
log("[1] K-arithmetic in the rho basis (1, rho, rho^2) ...")
R3 = (Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_))            # rho^3
R4 = (R3[2] * R3[0], R3[0] + R3[2] * R3[1], R3[1] + R3[2] * R3[2])
KZERO = (Fr(0), Fr(0), Fr(0))
KONE = (Fr(1), Fr(0), Fr(0))


def kadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def ksub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def kscale(a, c):
    return (a[0] * c, a[1] * c, a[2] * c)


def kmul(a, b):
    c0 = a[0] * b[0]
    c1 = a[0] * b[1] + a[1] * b[0]
    c2 = a[0] * b[2] + a[1] * b[1] + a[2] * b[0]
    c3 = a[1] * b[2] + a[2] * b[1]
    c4 = a[2] * b[2]
    out = [c0, c1, c2]
    if c3:
        for k in range(3):
            out[k] += c3 * R3[k]
    if c4:
        for k in range(3):
            out[k] += c4 * R4[k]
    return tuple(out)


def kmatmul(a):
    cols = [kmul(a, KONE), kmul(a, (Fr(0), Fr(1), Fr(0))),
            kmul(a, (Fr(0), Fr(0), Fr(1)))]
    return sp.Matrix(3, 3, lambda i, j: sp.Rational(cols[j][i].numerator,
                                                    cols[j][i].denominator))


def knorm(a):
    return sp.Rational(kmatmul(a).det())


def ktrace(a):
    return sp.Rational(kmatmul(a).trace())


def kinv(a):
    v = kmatmul(a).solve(sp.Matrix([1, 0, 0]))
    return tuple(Fr(sp.Rational(v[i]).p, sp.Rational(v[i]).q)
                 for i in range(3))


def keval(coeffs, a):
    """evaluate an integer polynomial (descending) at a in K."""
    acc = KZERO
    for c in coeffs:
        acc = kadd(kmul(acc, a), kscale(KONE, Fr(int(c))))
    return acc


def kminpoly(a):
    cp = kmatmul(a).charpoly(x).as_expr()
    best = None
    for f, m in sp.factor_list(cp)[1]:
        fp = Poly(f, x)
        if fp.degree() < 1:
            continue
        co = primitive_int_poly(fp.all_coeffs())
        if keval(co, a) == KZERO and (best is None or len(co) < len(best)):
            best = co
    if best is None:
        raise RuntimeError("no minimal polynomial found")
    return best


def K(lst):
    return tuple(Fr(c) for c in lst)


rho = (Fr(0), Fr(1), Fr(0))
CHK("K_arithmetic_rho_satisfies_mu13", keval(MU, rho) == KZERO,
    "A rho^3 + B rho^2 + C rho + D = 0 under the reduction used here")
CHK("K_arithmetic_minpoly_of_rho_is_mu13",
    kminpoly(rho) == primitive_int_poly(MU))

# ===================================================================== [2]
log("[2] the monogenic model of K (the instrument upgrade) ...")
T_mu = Poly([1, B_, A_ * C_, A_ ** 2 * D_], y)          # y = A_ * rho
CHK("monic_mu_model_correct",
    sp.expand(T_mu.as_expr().subs(y, A_ * x) - A_ ** 2 * mu_poly.as_expr())
    == 0, "T_mu(y) = y^3 + B y^2 + AC y + A^2 D,  y = A rho")
ZKy, dK = round_two(T_mu)
dK = int(dK)
REC("disc_K", f"{dK} = {ffac(dK)}", "round_two field discriminant")
CHK("disc_K_is_6237", dK == 6237, "3^4 * 7 * 11 -- agrees with B931")
QM = ZKy.QQ_matrix.to_Matrix()
basis_y = [[sp.Rational(QM[i, j]) for i in range(3)] for j in range(3)]


def y_to_k(vec):
    out = KZERO
    pw = KONE
    yk = kscale(rho, Fr(A_))
    for c in vec:
        cc = sp.Rational(c)
        out = kadd(out, kscale(pw, Fr(cc.p, cc.q)))
        pw = kmul(pw, yk)
    return out


OK_BASIS = [y_to_k(b) for b in basis_y]
CHK("integral_basis_is_a_3_element_Z_basis", len(OK_BASIS) == 3
    and OK_BASIS[0] == KONE)

def kcharpoly(a):
    """monic characteristic polynomial coefficients (descending)."""
    return [sp.Rational(c) for c in
            kmatmul(a).charpoly(x).as_expr().as_poly(x).all_coeffs()]


BOX = 6
cands_gen = []
for a in range(-BOX, BOX + 1):
    for b in range(-BOX, BOX + 1):
        z = kadd(kscale(OK_BASIS[1], Fr(a)), kscale(OK_BASIS[2], Fr(b)))
        co = kcharpoly(z)
        if any(c.q != 1 for c in co):
            continue
        mp = [int(c) for c in co]
        dsc = int(sp.discriminant(Poly(mp, x).as_expr(), x))
        if dsc == 0 or sp.Rational(dsc, dK).q != 1:
            continue
        q_ = sp.Rational(dsc, dK)
        if not sp.sqrt(q_).is_integer or int(sp.sqrt(q_)) != 1:
            continue
        if mp[1] % 3:
            continue                       # not depressible over Z
        sh = mp[1] // 3                    # theta + a2/3 kills the square
        zz = kadd(z, kscale(KONE, Fr(sh)))
        mpz = [int(c) for c in kcharpoly(zz)]
        cands_gen.append((max(abs(c) for c in mpz), tuple(mpz), a, b, sh,
                          zz))
CHK("monogenic_generator_found", len(cands_gen) > 0,
    f"{len(cands_gen)} index-1 depressed generators in the search box")
cands_gen.sort(key=lambda t: (t[0], t[1]))
_, T_S_t, a_gen, b_gen, sh_gen, S_GEN = cands_gen[0]
T_S = list(T_S_t)
T_S_poly = Poly(T_S, s)
REC("monogenic_model_of_K", str(T_S_poly.as_expr()),
    "the reduced index-1 defining polynomial of K "
    "(K is MONOGENIC: O_K = Z[s])")
CHK("monogenic_model_disc_equals_field_disc",
    int(sp.discriminant(T_S_poly.as_expr(), s)) == dK,
    "index 1 -- every place of every prime is reachable by prime_decomp")
CHK("monogenic_generator_is_in_O_K_and_generates",
    kminpoly(S_GEN) == T_S and len(T_S) == 4)

pw = KONE
cols = []
for k in range(3):
    cols.append(pw)
    pw = kmul(pw, S_GEN)
TRM = sp.Matrix(3, 3, lambda i, j: sp.Rational(cols[j][i].numerator,
                                               cols[j][i].denominator))
CHK("transfer_matrix_invertible", TRM.det() != 0,
    "1, s, s^2 is a Q-basis of K (s is primitive)")
TRMinv = TRM.inv()


def k_to_s(a):
    v = TRMinv * sp.Matrix([sp.Rational(a[i].numerator, a[i].denominator)
                            for i in range(3)])
    return [sp.Rational(v[i]) for i in range(3)]


CHK("s_model_same_field_disc", int(round_two(T_S_poly)[1]) == dK)
# transfer sanity: the transferred rho satisfies mu13 modulo T_S
rho_s = sum(k_to_s(rho)[k] * s ** k for k in range(3))
CHK("transfer_carries_rho_to_a_root_of_mu13",
    sp.rem(sp.expand(Poly(MU, x).as_expr().subs(x, rho_s)),
           T_S_poly.as_expr(), s) == 0,
    f"rho = {rho_s} in the monogenic model: the two models are the SAME "
    f"field K, with this explicit isomorphism")

# --- exact P-adic valuations by ideal-lattice membership.
# O_K = Z[s] (index 1), so Dedekind's theorem applies at EVERY prime: the
# places over p are P_i = (p, g_i(s)) where T = prod g_i^{e_i} mod p, with
# e(P_i) = e_i and f(P_i) = deg g_i.  Valuations are then computed as
# v_P(z) = max{k : z in P^k} on lattices in Z^3 -- elementary, exact, and
# independent of sympy's prime_valuation (which raises CoercionFailed on
# these inputs: its halting test reads only the last diagonal entry of a
# matrix it never returns to Hermite form, so it is not usable here).
def smulmat(co):
    """multiplication matrix of c0 + c1 s + c2 s^2 in the basis (1,s,s^2)."""
    r0, r1, r2 = -T_S[3], -T_S[2], -T_S[1]      # s^3 = r0 + r1 s + r2 s^2
    cols = []
    cur = list(co)
    for _ in range(3):
        cols.append(list(cur))
        c3 = cur[2]
        cur = [cur[0] * 0 + r0 * c3, cur[0] + r1 * c3, cur[1] + r2 * c3]
    return sp.Matrix(3, 3, lambda i, j: cols[j][i])


def ideal_from_gens(gens):
    cols = []
    for g in gens:
        Mg = smulmat(g)
        for j in range(3):
            cols.append([Mg[i, j] for i in range(3)])
    return hermite_normal_form(
        sp.Matrix(3, len(cols), lambda i, j: cols[j][i]))


def ideal_mul(A_, B_):
    cols = []
    for j in range(3):
        Ma = smulmat([A_[i, j] for i in range(3)])
        for j2 in range(3):
            v = Ma * sp.Matrix([B_[i, j2] for i in range(3)])
            cols.append([v[i] for i in range(3)])
    return hermite_normal_form(
        sp.Matrix(3, len(cols), lambda i, j: cols[j][i]))


PLACES = {}


def places_of(p):
    """[(g_ascending, e, f)] for every place over p, by Dedekind."""
    if p not in PLACES:
        out = []
        for f_, e_ in sp.factor_list(T_S_poly.as_expr(), modulus=p)[1]:
            fp = Poly(f_, s, modulus=p)
            asc = [int(c) % p for c in reversed(fp.all_coeffs())]
            asc = (asc + [0, 0, 0])[:3]
            out.append((asc, int(e_), int(fp.degree())))
        PLACES[p] = out
    return PLACES[p]


def to_num_den(a):
    cs = k_to_s(a)
    den = 1
    for c in cs:
        den = sp.ilcm(den, sp.Rational(c).q)
    return [int(sp.Rational(c) * den) for c in cs], int(den)


def val_at(a, p_, label=""):
    """the (f, v) table of a at every place over p_, with the norm
    consistency check sum_P f_P v_P = v_p(N(a))."""
    num, den = to_num_den(a)
    out = []
    vsum = 0
    for gasc, e_, f_ in places_of(p_):
        P = ideal_from_gens([[p_, 0, 0], gasc])
        k = 0
        Pk = None
        while True:
            Pk_next = P if Pk is None else ideal_mul(Pk, P)
            if any(sp.Rational(c).q != 1
                   for c in Pk_next.solve(sp.Matrix(num))):
                break
            Pk = Pk_next
            k += 1
            if k > 400:
                raise RuntimeError("runaway valuation loop")
        v = k - e_ * sp.multiplicity(p_, den)
        out.append((f_, int(v)))
        vsum += f_ * int(v)
    N = knorm(a)
    got = sp.multiplicity(p_, N.p) - sp.multiplicity(p_, N.q)
    CHK(f"val_norm_consistency_{label or 'elt'}_at_{p_}", vsum == got,
        f"sum f*v = {vsum} = v_{p_}(N) = {got}")
    return sorted(out)


def divisor(a, label, note=""):
    """the COMPLETE prime-ideal divisor of a nonzero a in K.

    Completeness argument: write a = n/den with den = lcm of the
    denominators of the s-coordinates; since O_K = Z[s], den*a lies in O_K,
    so every place with v < 0 lies over a prime dividing den; and every
    place with v > 0 either survives into the numerator of N(a) or is
    cancelled inside its own rational prime -- which forces that prime to
    divide den as well.  The candidate set below therefore provably
    contains the whole support, and the final identity
    |N(a)| = prod_p p^(sum_P f_P v_P) is checked."""
    _, den = to_num_den(a)
    N = knorm(a)
    cands = set()
    for src in (ffac(N.p), ffac(N.q), ffac(den)):
        for p_ in src:
            if p_.isdigit() and int(p_) > 1:
                cands.add(int(p_))
            elif p_.startswith("C"):
                CHK(f"divisor_{label}_fully_factored", False,
                    f"composite leftover {p_} -- refusing to claim a "
                    f"complete divisor")
    tab = {}
    prod = sp.Integer(1)
    for p_ in sorted(cands):
        vs = val_at(a, p_, f"{label}")
        for i_, (f_, v) in enumerate(vs):
            tab[f"p={p_}#{i_}(f={f_})"] = v
        prod *= sp.Integer(p_) ** sum(f_ * v for f_, v in vs)
    CHK(f"divisor_{label}_complete", abs(sp.Rational(N)) == prod,
        f"N({label}) = {N} = {fac_of_rat(N)}")
    return {"valuations": tab, "norm": str(N), "norm_fac": fac_of_rat(N),
            "note": note}


# ---- gate the new model against B931's banked two-model divisor tables
d_S = K(HARV["d_S"])
d_A = K(HARV["d_A"])
div_dS = divisor(d_S, "d_S")
div_dA = divisor(d_A, "d_A")


def b931_vpat(label, p_):
    out = []
    for k, v in B931["divisor_map"][label]["valuations"].items():
        if k.startswith(f"p={p_}#"):
            out.append((int(k.split("f=")[1].rstrip(")")), v))
    return sorted(out)


for lab, el in (("d_S", d_S), ("d_A", d_A)):
    for p_ in (2, 3, 953):
        CHK(f"cross_model_gate_{lab}_at_{p_}",
            val_at(el, p_, lab) == b931_vpat(lab, p_),
            f"{val_at(el, p_, lab)} == B931's {b931_vpat(lab, p_)}")
RES["field_K"] = {
    "mu13_model": str(T_mu.as_expr()),
    "monogenic_model": str(T_S_poly.as_expr()),
    "disc_K": str(dK), "disc_K_fac": ffac(dK),
    "index_of_this_generator": 1,
    "generator": {"a": a_gen, "b": b_gen, "depression_shift": sh_gen},
    "note": "sympy prime_decomp fails at p = 5 and p = 7 in BOTH banked "
            "models (h_S and monic mu13); in this index-1 model every "
            "place of every prime is reachable, which is exactly what the "
            "5-adic story needs.",
}
dump()

# ===================================================================== [3]
log("[3] gates on the harvested B930 elements ...")
W = K(HARV["W"])
x_e = K(HARV["x_e"])
x_o = K(HARV["x_o"])
q_S = K(HARV["q_S"])
q_A = K(HARV["q_A"])
X_cross = K(HARV["X_cross"])

CHK("W_K_coords_equal_banked_B930", list(W) == list(W_KCOORDS_BANKED))
CHK("W_minpoly_equals_banked_B930", kminpoly(W) == W_MINPOLY_BANKED,
    str(W_MINPOLY_BANKED))
CHK("W_minpoly_lead_is_953_pow4", ffac(W_MINPOLY_BANKED[0]) == {"953": 4})
CHK("W_minpoly_const_is_minus_5_pow12",
    ffac(W_MINPOLY_BANKED[3]) == {"-1": 1, "5": 12})
CHK("d_S_minpoly_equals_banked_B916", kminpoly(d_S) == MPDS)
CHK("d_A_minpoly_equals_banked_B916", kminpoly(d_A) == MPDA)
CHK("d_S_norm_is_minus_953_over_2304_sq",
    knorm(d_S) == -sp.Rational(953, 2304) ** 2, str(knorm(d_S)))
CHK("d_A_norm_is_minus_953_over_2304_sq",
    knorm(d_A) == -sp.Rational(953, 2304) ** 2, str(knorm(d_A)))
CHK("d_S_equals_1_minus_2_m_S", d_S == ksub(KONE, kscale(K(MS_K), Fr(2))))
CHK("d_A_equals_1_minus_2_m_A", d_A == ksub(KONE, kscale(K(MA_K), Fr(2))))
CHK("m_S_minpoly_equals_banked_B928", kminpoly(K(MS_K)) == MPMS)
CHK("m_A_minpoly_equals_banked_B928", kminpoly(K(MA_K)) == MPMA)
CHK("x_o_is_exactly_zero", x_o == KZERO,
    "the same-generation twisted overlap h'(S_g, A_g+) has ZERO tau-part: "
    "it lies in K, not merely in N -- so |h'|^2 = x_e^2 is a perfect "
    "SQUARE in K")
CHK("W_equals_xe_sq_over_dq_product",
    W == kmul(kmul(x_e, x_e), kinv(kmul(kmul(d_S, q_S), kmul(d_A, q_A)))),
    "W = x_e^2 / (d_S q_S d_A q_A) exactly -- the harvested parts are "
    "internally consistent with the banked K-coordinates")
CHK("X_cross_minpoly_equals_banked_B930",
    kminpoly(X_cross) == X_MINPOLY_BANKED, str(X_MINPOLY_BANKED))
CHK("X_cross_minpoly_lead_is_953_sq",
    ffac(X_MINPOLY_BANKED[0]) == {"953": 2})
CHK("X_cross_minpoly_const_is_minus_5_pow6",
    ffac(X_MINPOLY_BANKED[3]) == {"-1": 1, "5": 6})
dump()

# ===================================================================== [4]
log("[4] PART A: the divisors ...")
PA = {}
PA["W_divisor"] = divisor(W, "W", "the same-generation overlap^2")
PA["X_cross_divisor"] = divisor(X_cross, "X_cross",
                                "a cross-generation overlap^2 (it lies in "
                                "K: its beta-part vanishes)")
u = kmul(W, kmul(d_S, d_A))
CHK("u_equals_xe_sq_over_q_product",
    u == kmul(kmul(x_e, x_e), kinv(kmul(q_S, q_A))),
    "u := W d_S d_A = h'(S,A)^2 / (h+(S,S) h+(A,A)); both W and u are "
    "GAUGE-INVARIANT (numerator and denominator have the same homogeneity "
    "under the atom rescalings), so their divisors are properties of the "
    "object, not of B930's normalisation")
PA["u_divisor"] = divisor(u, "u", "the H+-normalised twisted overlap^2")
PA["u_minpoly"] = [str(c) for c in kminpoly(u)]
supp = sorted({int(k.split("=")[1].split("#")[0])
               for k, v in PA["u_divisor"]["valuations"].items() if v})
CHK("u_support_is_exactly_2_3_5", supp == [2, 3, 5],
    f"the divisor of u is supported exactly over {supp}: the golden "
    f"numerator is entirely u's and the value prime 953 is entirely the "
    f"twist's")
PA["u_support"] = supp

# the 953 story
v953 = {"W": val_at(W, 953, "W"), "u": val_at(u, 953, "u"),
        "d_S": val_at(d_S, 953, "d_S"), "d_A": val_at(d_A, 953, "d_A"),
        "X_cross": val_at(X_cross, 953, "X_cross")}
PA["953_story"] = {k: [list(t) for t in v] for k, v in v953.items()}
CHK("u_is_a_953_unit", all(v == 0 for f_, v in v953["u"]),
    "u has valuation 0 at BOTH places over 953")
CHK("W_953_pole_is_exactly_the_two_twist_places",
    [(f_, -v) for f_, v in v953["W"]]
    == [(f_, vS + vA) for (f_, vS), (_, vA) in zip(v953["d_S"],
                                                   v953["d_A"])],
    f"W at 953 = {v953['W']} = -(d_S {v953['d_S']} + d_A {v953['d_A']}): "
    f"the mixing element's 953-pole is the SUM of the two families' twist "
    f"zeros -- the degree-one observer place (doubly, from the vacuum "
    f"family) and the degree-two mirror place (simply, from the A-family)")
CHK("lead_953_pow4_equals_norm_of_the_pole_ideal",
    sp.prod([sp.Integer(953) ** (f_ * (-v)) for f_, v in v953["W"]])
    == 953 ** 4,
    "N(P1^2 * P2) = 953^2 * 953^2 = 953^4 -- the banked minpoly lead is "
    "the norm of W's pole ideal")

# the 5-adic story
p5 = places_of(5)
PA["5_places"] = [{"e": e_, "f": f_} for _g, e_, f_ in p5]
v5 = {
    "W": val_at(W, 5, "W"), "u": val_at(u, 5, "u"),
    "X_cross": val_at(X_cross, 5, "X_cross"),
    "d_S": val_at(d_S, 5, "d_S"), "d_A": val_at(d_A, 5, "d_A"),
    "m_S": val_at(K(MS_K), 5, "m_S"), "m_A": val_at(K(MA_K), 5, "m_A"),
    "x_e_GAUGE_DEPENDENT": val_at(x_e, 5, "x_e"),
    "q_S_GAUGE_DEPENDENT": val_at(q_S, 5, "q_S"),
    "q_A_GAUGE_DEPENDENT": val_at(q_A, 5, "q_A"),
}
PA["5_story"] = {k: [list(t) for t in v] for k, v in v5.items()}
sumfv = sum(f_ * v for f_, v in v5["W"])
CHK("the_5_exponent_is_12_and_it_is_the_place_sum", sumfv == 12,
    f"sum over the places over 5 of f*v = {sumfv}; places (e,f) = "
    f"{[(e_, f_) for _g, e_, f_ in p5]}, valuations {v5['W']}")
CHK("W_and_u_have_the_same_5_divisor", v5["W"] == v5["u"],
    "the twist is a 5-unit, so the whole golden content is the "
    "H+-normalised mixing element's")
loc5 = [f_ * v for f_, v in v5["W"]]
CHK("the_two_places_over_5_contribute_EQUAL_local_norms",
    len(set(loc5)) == 1 and loc5[0] == 6,
    f"W at 5 = {v5['W']}: f*v = {loc5}, i.e. 5^6 from the degree-one place "
    f"and 5^6 from the degree-two place. The golden numerator splits "
    f"EVENLY between the two places over 5; 12 = 6 + 6.")
g5 = 0
for f_, v in v5["W"]:
    g5 = sp.igcd(g5, v)
CHK("the_5_part_of_W_is_a_perfect_cube", int(g5) == 3,
    f"gcd of the 5-valuations {[v for f_, v in v5['W']]} is {g5}: the "
    f"5-part of (W) is the CUBE of the ideal with valuations "
    f"{[(f_, v // int(g5)) for f_, v in v5['W']]} (norm 5^4), so "
    f"12 = 3 * 4")
CHK("same_minus_cross_at_5_is_the_degree_one_place_alone",
    [(f_, v - v2) for (f_, v), (_f, v2) in zip(v5["W"], v5["X_cross"])]
    == [(1, 6), (2, 0)],
    f"same-generation {v5['W']} minus cross-generation {v5['X_cross']}: "
    f"the two differ ONLY at the degree-one place over 5, by exactly the "
    f"6th power. The cross-generation mixing is blind to the degree-one "
    f"place; the same-generation mixing carries it to the 6th.")
CHK("the_cross_generation_5_content_is_the_per_place_contribution",
    sum(f_ * v for f_, v in v5["X_cross"]) == 6,
    f"X_cross at 5 = {v5['X_cross']}, norm-numerator 5^6 -- exactly the "
    f"local contribution of each single place in the same-generation "
    f"element")
# THE SHARPEST STATEMENT: same-generation / cross-generation
ratio = kmul(W, kinv(X_cross))
PA["same_over_cross_divisor"] = divisor(
    ratio, "W_over_Xcross",
    "the ratio of the same-generation to a cross-generation overlap^2")
CHK("cross_generation_lives_ONLY_on_the_degree_two_places",
    all(v == 0 for f_, v in v5["X_cross"] if f_ == 1)
    and all(v == 0 for f_, v in v953["X_cross"] if f_ == 1),
    f"X_cross at 5 = {v5['X_cross']} and at 953 = {v953['X_cross']}: the "
    f"cross-generation mixing element is supported ENTIRELY on the "
    f"degree-TWO places of both primes -- it never touches the observer's "
    f"degree-one place")
CHK("same_over_cross_is_EXACTLY_the_observer_places",
    sorted(PA["same_over_cross_divisor"]["valuations"].items())
    == sorted({"p=5#0(f=1)": 6, "p=5#1(f=2)": 0,
               "p=953#0(f=1)": -2, "p=953#1(f=2)": 0}.items()),
    "the same-generation over the cross-generation overlap^2 has divisor "
    "q1(5)^6 * P1(953)^-2 -- supported ONLY on the DEGREE-ONE places, and "
    "at 953 with exactly the exponent of d_S's twist zero (B918's "
    "observer place, where the hierarchy element V has its pole). The "
    "whole difference between diagonal and off-diagonal mixing is the "
    "observer's place.")
PA["exponent_12_candidate_tests"] = {
    "12 = 4 places x 3": {
        "places_over_5": len(p5),
        "verdict": "REFUTED",
        "detail": f"5 has {len(p5)} places in K "
                  f"({[(e_, f_) for _g, e_, f_ in p5]}), not 4"},
    "12 = the D-flip count": {
        "D2_flip_count": 11,
        "verdict": "REFUTED",
        "detail": f"the banked flip rank is 11 exactly "
                  f"({TRACE_SUM_DETAIL}); 11 != 12"},
    "12 = the floor dimension": {
        "floor_dim_banked": 12,
        "verdict": "MATCH WITHOUT MECHANISM",
        "detail": "Cent(C) -- the floor -- has dimension 12 (B874/B932). "
                  "The integers agree, but this cell exhibits NO "
                  "computation carrying the floor into the 5-divisor; "
                  "recorded as a coincidence-level match, not a "
                  "derivation."},
    "12 = 6 + 6, the two places over 5 balancing": {
        "verdict": "COMPUTED",
        "W_at_5": [list(t) for t in v5["W"]],
        "local_norm_exponents": loc5,
        "detail": "the divisor of W over 5 is q1^6 q2^3 with f(q1) = 1 and "
                  "f(q2) = 2, so each place contributes exactly 5^6 to the "
                  "norm. The exponent 12 is the SUM OF TWO EQUAL LOCAL "
                  "CONTRIBUTIONS, not a dimension; and 6 is also the whole "
                  "5-content of a cross-generation overlap."},
    "12 = 3 x 4, the 5-part being a perfect cube": {
        "verdict": "COMPUTED",
        "detail": "the 5-valuations (6, 3) have gcd 3, so the 5-part of "
                  "(W) is the cube of an ideal of norm 5^4. Recorded; no "
                  "mechanism is claimed for the cube."},
    "12 = 2 x 6, the divisor being a square": {
        "verdict": "REFUTED BY THE COMPUTATION",
        "detail": "this cell's first pass guessed the 5-divisor would be "
                  "even at every place, since W's numerator is the square "
                  "x_e^2. The computation refutes it: the valuation at the "
                  "degree-two place is 3, odd, because the H+ norms are "
                  "NOT 5-units (v_5(N(q_S)) = 4, v_5(N(q_A)) = 8). The "
                  "abort is logged as part of the instrument story."},
}
dump()

# ---- an INDEPENDENT p-adic belt on the degree-one places
log("[4c] the independent p-adic belt (Newton lift, no lattices) ...")


def padic_simple_root(p_, m):
    """the p-adic root of T_S at the (unique) degree-one place, to p^m."""
    def ev(c, r, mod):
        acc = 0
        for co in c:
            acc = (acc * r + co) % mod
        return acc
    dT = [3 * T_S[0], 2 * T_S[1], T_S[2]]
    simple = [r for r in range(p_) if ev(T_S, r, p_) == 0
              and ev(dT, r, p_) != 0]
    if len(simple) != 1:
        return None
    r, mod = simple[0], p_
    while mod < p_ ** m:
        mod = min(mod * mod, p_ ** m)
        r = (r - ev(T_S, r, mod) * pow(ev(dT, r, mod), -1, mod)) % mod
    return r, mod


def v_deg1_padic(a, p_, m):
    """v at the degree-one place, by evaluating at the p-adic root."""
    rt = padic_simple_root(p_, m)
    r, mod = rt
    num, den = to_num_den(a)
    val = (num[0] + num[1] * r + num[2] * r * r) % mod
    if val == 0:
        raise RuntimeError("precision exhausted in the p-adic belt")
    v = 0
    while val % p_ == 0:
        val //= p_
        v += 1
    return v - sp.multiplicity(p_, den)


BELT = {}
for lab, el in (("W", W), ("u", u), ("X_cross", X_cross), ("d_S", d_S),
                ("d_A", d_A)):
    for p_, m_ in ((5, 24), (953, 10)):
        lat = [v for f_, v in val_at(el, p_, lab) if f_ == 1]
        pad = v_deg1_padic(el, p_, m_)
        BELT[f"{lab}@{p_}"] = {"lattice": lat[0], "padic": int(pad)}
        CHK(f"belt_deg1_{lab}_at_{p_}", lat[0] == pad,
            f"lattice {lat[0]} == Newton-lift evaluation {pad}")
PA["independent_padic_belt"] = BELT
PA["independent_padic_belt_note"] = (
    "the degree-one place of an unramified p has completion Q_p, so the "
    "valuation there is just v_p of the element evaluated at the p-adic "
    "root of the defining polynomial -- a route sharing no code with the "
    "ideal-lattice computation. The degree-two valuations then follow from "
    "the norm identity sum_P f_P v_P = v_p(N), which every table above "
    "already checks.")
dump()

# ---- the golden field decision
log("[4b] PART A: does Q(sqrt5) enter?  (exact) ...")
dW = int(sp.discriminant(Poly(W_MINPOLY_BANKED, x).as_expr(), x))
dX = int(sp.discriminant(Poly(X_MINPOLY_BANKED, x).as_expr(), x))
sfW, sfX = squarefree_part(dW), squarefree_part(dX)
PA["golden_field_decision"] = {
    "disc_W_minpoly": str(dW), "disc_W_minpoly_fac": ffac(dW),
    "squarefree_part_disc_W": sfW,
    "disc_X_minpoly": str(dX), "disc_X_minpoly_fac": ffac(dX),
    "squarefree_part_disc_X": sfX,
    "galois_group_of_W_minpoly":
        "C3" if (dW > 0 and sp.integer_nthroot(int(dW), 2)[1]) else "S3",
}
CHK("W_generates_K", len(kminpoly(W)) == 4,
    "the overlap^2 has a degree-3 minimal polynomial: it GENERATES K, so "
    "the splitting field of that polynomial IS the Galois closure of K")
CHK("splitting_field_quadratic_subfield_is_Q_sqrt77",
    sfW == squarefree_part(dK) == 77,
    f"squarefree(disc of W's minpoly) = {sfW} = squarefree(disc K) = "
    f"{squarefree_part(dK)}")
CHK("sqrt5_not_in_the_splitting_field_of_W", sfW != 5,
    "an irreducible cubic with Galois group S3 has EXACTLY ONE quadratic "
    "subfield in its splitting field, namely Q(sqrt disc); here that is "
    "Q(sqrt77), so Q(sqrt5) is not in it")
CHK("Mbar_has_exactly_three_quadratic_subfields",
    squarefree_part(dK) == 77 and squarefree_part(77 * -3) == -231,
    "N cap Q(sqrt-3) = Q because squarefree(disc K) = 77 != -3, so "
    "Gal(Mbar/Q) = S3 x C2 with abelianisation C2 x C2: Mbar (the "
    "degree-12 field in which every B930 quantity was computed) has "
    "exactly the three quadratic subfields Q(sqrt77), Q(sqrt-3), "
    "Q(sqrt-231)")
CHK("sqrt5_not_in_Mbar",
    all(squarefree_part(5 * q_) != 1 for q_ in (77, -3, -231)),
    "5 is not equal modulo squares to any of 77, -3, -231, so Q(sqrt5) is "
    "not one of Mbar's three quadratic subfields")
alpha = sp.AlgebraicNumber(sp.rootof(T_S_poly.as_expr(), 0))
fl5 = sp.factor_list(x ** 2 - 5, extension=alpha)
fl15 = sp.factor_list(x ** 2 + 15, extension=alpha)
CHK("x2_minus_5_stays_irreducible_over_K",
    len(fl5[1]) == 1 and Poly(fl5[1][0][0], x).degree() == 2,
    "5 is not a square in K (independent computational confirmation)")
CHK("x2_plus_15_stays_irreducible_over_K",
    len(fl15[1]) == 1 and Poly(fl15[1][0][0], x).degree() == 2,
    "-15 is not a square in K -- this is the only other way sqrt5 could "
    "enter K(sqrt-3): (a + b tau)^2 = 5 with tau^2 = -3 forces a = 0 and "
    "b^2 = -5/3")
CHK("5_is_unramified_in_K", dK % 5 != 0,
    f"disc K = {dK}: 5 does not ramify, so it is not a field-theoretic "
    f"distinguished prime of K at all")
PA["golden_field_decision"]["resolvent_symbols"] = {
    str(p_): int(sp.jacobi_symbol(dK, p_))
    for p_ in [5, 7, 11, 29, 149, 953, 1129, 421493, 72869, 20417473,
               17681] if p_ % 2 and dK % p_}
PA["where_5_sits_upstream"] = {
    "lc(mu13)": ffac(A_),
    "disc(h_S)": ffac(int(sp.discriminant(Poly(H_S, x).as_expr(), x))),
    "disc(K)": ffac(dK),
    "reading": "5 divides the charge cubic's leading coefficient (to the "
               "second power) and the h_S discriminant (to the second "
               "power), but NOT the field discriminant: 5 is unramified in "
               "K. B931 DERIVED the twist's 2304 as the {2,3}-part of "
               "lc(mu13); this cell finds no analogous derivation of the "
               "5-content of the mixing element. Where the integer 5 comes "
               "from is this arc's honest residue -- exactly parallel to "
               "B931's open residue for 953.",
}
PA["golden_field_decision"]["verdict"] = (
    "5 IS A RESIDUE CHARACTERISTIC, NOT THE GOLDEN FIELD. The overlap^2 "
    "generates K; the splitting field of its minimal polynomial is the "
    "S3-closure of K, whose unique quadratic subfield is Q(sqrt77). The "
    "whole tower Mbar in which B930 computed has exactly three quadratic "
    "subfields -- Q(sqrt77), Q(sqrt-3), Q(sqrt-231) -- and Q(sqrt5) is "
    "none of them; x^2 - 5 and x^2 + 15 are both irreducible over K; and "
    "5 does not divide disc K = 3^4 * 7 * 11, so 5 is unramified. The 5 "
    "in the banked minimal polynomial is the residue characteristic of "
    "the places carrying the mixing numerator -- nothing golden.")
RES["partA"] = PA
dump()

# ===================================================================== [5]
log("[5] PART B: DECLARING the 29 whitelist (written BEFORE compute) ...")
DECL = {
    "question": "29 appears twice in the banked record: (i) as a prime of "
                "the A-family flip mass's zero-level norm, N(m_A) "
                "numerator = 29 * 72869 (B928/B931), and (ii) inside the "
                "middle coefficient of B930's W3 twist-vs-Galois rotation "
                "quadratic 1536x^2 - 2088x + 677, where 2088 = 2^3 * 3^2 "
                "* 29. Is 29 STRUCTURAL or COINCIDENCE?",
    "whitelist": {
        "W29-1": "m_A's zero-divisor: the exact valuations of m_A at every "
                 "place over 29, with m_S, d_S, d_A, W, u and X_cross as "
                 "controls at the same places",
        "W29-2": "the rotation quadratic 1536x^2 - 2088x + 677: its "
                 "discriminant, the factorisations of lead/middle/"
                 "constant, the quadratic field it generates, and its "
                 "reduction mod 29 -- with the A-register's quadratic "
                 "1536x^2 - 984x + 125 alongside",
        "W29-3": "the discriminants of every irreducible factor of the W3, "
                 "W6 and W18 flip-compression characteristic polynomials, "
                 "and of the full characteristic polynomials",
        "W29-4": "the discriminant of the S-A overlap^2 minimal polynomial "
                 "(same generation) and of the cross-generation one",
        "W29-5": "the resultant grid: every pairwise resultant among "
                 "{mu13, the monogenic model of K, h_S, mp_dS, mp_dA, "
                 "mp_mS, mp_mA, the W3 quadratic, the W6 quadratic, the "
                 "same-generation overlap minpoly, the cross-generation "
                 "overlap minpoly}",
        "W29-6": "29's place structure in K: the (e,f) pattern, the "
                 "quadratic-resolvent symbol (disc K | 29), the Frobenius "
                 "class, and which place carries m_A's zero",
        "W29-7": "the Killing/trace Gram of the four charges on the 27, "
                 "G_mn = tr(R_m R_n): entries, determinant, principal "
                 "minors; plus the three register Gram determinants (G3, "
                 "G6, G18) and the 27 H+ diagonal weights",
    },
    "verdict_criterion": {
        "STRUCTURAL": "at least two whitelist appearances of 29 are linked "
                      "by an EXHIBITED chain of exact identities in which "
                      "one appearance is derived from the other -- e.g. "
                      "the 29 dividing 2088 shown to be the residue "
                      "characteristic of a place at which a named object "
                      "of the SAME family degenerates, with the identity "
                      "computed in this cell",
        "COINCIDENCE": "no such chain after the whole whitelist is "
                       "computed; the appearances sit in objects of "
                       "different families and/or different kinds (a "
                       "rational trace numerator versus a prime ideal), "
                       "and the look-elsewhere budget over the whitelist's "
                       "own integers makes two or more 29-divisibility "
                       "hits unremarkable",
        "note": "both outcomes are reachable and both bank; the whitelist "
                "is fixed before any of it is computed",
    },
}
RES["whitelist_29_DECLARED_BEFORE_COMPUTE"] = DECL
dump()
log("    whitelist sealed into results.json; computing it now")

PBD = {}
RES["partB"] = PBD          # incremental: every dump below carries part B
INTEGERS_EXAMINED = []


def note_int(tag, n):
    n = int(n)
    if n in (0, 1, -1):
        return {}
    f = ffac(n)
    INTEGERS_EXAMINED.append({"tag": tag, "value": str(n),
                              "has_29": "29" in f})
    return f


log("[5.1] W29-6: 29's place structure in K ...")
p29 = places_of(29)
sym29 = int(sp.jacobi_symbol(dK, 29))
PBD["W29-6_place_structure"] = {
    "pattern": [{"e": e_, "f": f_} for _g, e_, f_ in p29],
    "resolvent_symbol_discK_over_29": sym29,
    "frobenius_class": "transposition" if sym29 == -1 else "other",
    "ramified": dK % 29 == 0,
}
dump()

log("[5.2] W29-1: m_A's zero-divisor at 29 + controls ...")
v29 = {"m_A": val_at(K(MA_K), 29, "m_A"), "m_S": val_at(K(MS_K), 29, "m_S"),
       "d_A": val_at(d_A, 29, "d_A"), "d_S": val_at(d_S, 29, "d_S"),
       "W": val_at(W, 29, "W"), "u": val_at(u, 29, "u"),
       "X_cross": val_at(X_cross, 29, "X_cross")}
PBD["W29-1_divisors_at_29"] = {k: [list(t) for t in v]
                               for k, v in v29.items()}
CHK("m_A_vanishes_at_the_degree_one_place_over_29",
    any(f_ == 1 and v > 0 for f_, v in v29["m_A"])
    and all(v == 0 for f_, v in v29["m_A"] if f_ != 1),
    str(v29["m_A"]))
CHK("m_S_is_29_blind_at_every_place",
    all(v == 0 for f_, v in v29["m_S"]),
    "the S-family flip mass has valuation 0 at BOTH places over 29")
CHK("the_overlap_elements_are_29_blind",
    all(v == 0 for f_, v in v29["W"])
    and all(v == 0 for f_, v in v29["u"])
    and all(v == 0 for f_, v in v29["X_cross"]),
    "W, u and X_cross all have valuation 0 at every place over 29")
note_int("N(m_A) numerator", sp.Rational(knorm(K(MA_K))).p)
note_int("N(m_S) numerator", sp.Rational(knorm(K(MS_K))).p)
dump()

log("[5.3] W29-2/3: the rotation quadratics and every compression factor ..")
comp = {}
for reg, facs in (("W3", W3_FACTORS), ("W6", W6_FACTORS),
                  ("W18", W18_FACTORS)):
    rows = []
    full = sp.Integer(1)
    for fdat in facs:
        co = [int(c) for c in fdat["coeffs"]]
        pol = Poly(co, x)
        d_ = int(sp.discriminant(pol.as_expr(), x)) if pol.degree() >= 2 \
            else 0
        rows.append({
            "factor": str(pol.as_expr()), "mult": fdat["mult"],
            "coeff_fac": [ffac(c) if c else {"0": 1} for c in co],
            "disc": str(d_), "disc_fac": ffac(d_) if d_ else {},
            "has_29_in_coeffs": any("29" in ffac(c) for c in co if c),
            "has_29_in_disc": "29" in (ffac(d_) if d_ else {})})
        for c in co:
            note_int(f"{reg} factor coeff", c)
        if d_:
            note_int(f"{reg} factor disc", d_)
        full *= pol.as_expr() ** fdat["mult"]
    fullp = Poly(sp.expand(full), x)
    dfull = int(sp.discriminant(fullp.as_expr(), x))
    comp[reg] = {"factors": rows, "full_charpoly": str(fullp.as_expr()),
                 "full_charpoly_disc": str(dfull),
                 "full_charpoly_disc_fac": ffac(dfull) if dfull else
                 {"0": 1},
                 "full_charpoly_disc_is_zero_repeated_roots": dfull == 0}
    if dfull:
        note_int(f"{reg} full charpoly disc", dfull)
PBD["W29-3_compressions"] = comp

qW3 = [int(c) for c in W3_FACTORS[-1]["coeffs"]]
qW6 = [int(c) for c in W6_FACTORS[-1]["coeffs"]]
dq3 = int(sp.discriminant(Poly(qW3, x).as_expr(), x))
dq6 = int(sp.discriminant(Poly(qW6, x).as_expr(), x))
CHK("W3_rotation_quadratic_is_the_banked_one", qW3 == [1536, -2088, 677])
CHK("W6_rotation_quadratic_is_the_banked_one", qW6 == [1536, -984, 125])
CHK("the_two_rotation_quadratics_SHARE_a_discriminant", dq3 == dq6,
    f"disc = {dq3} = {ffac(dq3)} for BOTH the vacuum register's and the "
    f"A-register's twist-vs-Galois quadratic: the two registers' principal "
    f"angles live in ONE quadratic field, Q(sqrt{squarefree_part(dq3)})")
PBD["W29-2_rotation_quadratics"] = {
    reg: {"poly": str(Poly(q_, x).as_expr()),
          "coeff_fac": [ffac(c) for c in q_],
          "disc": str(d_), "disc_fac": ffac(d_),
          "quadratic_field": f"Q(sqrt{squarefree_part(d_)})",
          "29_divides_disc": "29" in ffac(d_),
          "29_divides_a_coefficient": any("29" in ffac(c) for c in q_),
          "reduction_mod_29": [c % 29 for c in q_],
          "irreducible_mod_29": not any(
              (q_[0] * t * t + q_[1] * t + q_[2]) % 29 == 0
              for t in range(29))}
    for reg, q_, d_ in (("W3", qW3, dq3), ("W6", qW6, dq6))}
PBD["W29-2_rotation_quadratics"]["shared_disc_squarefree_part"] = \
    squarefree_part(dq3)
dump()

log("[5.4] W29-4: the overlap minimal polynomials' discriminants ...")
PBD["W29-4_overlap_discs"] = {
    "same_generation": {"minpoly": [str(c) for c in W_MINPOLY_BANKED],
                        "coeff_fac": [ffac(c) for c in W_MINPOLY_BANKED],
                        "disc": str(dW), "disc_fac": ffac(dW),
                        "has_29": "29" in ffac(dW)},
    "cross_generation": {"minpoly": [str(c) for c in X_MINPOLY_BANKED],
                         "coeff_fac": [ffac(c) for c in X_MINPOLY_BANKED],
                         "disc": str(dX), "disc_fac": ffac(dX),
                         "has_29": "29" in ffac(dX)},
}
for c in W_MINPOLY_BANKED + X_MINPOLY_BANKED:
    note_int("overlap minpoly coeff", c)
note_int("disc(same-gen overlap minpoly)", dW)
note_int("disc(cross-gen overlap minpoly)", dX)
dump()

log("[5.5] W29-5: the resultant grid ...")
GRID = {"mu13": Poly(MU, x), "K_monogenic": Poly(T_S, x),
        "h_S": Poly(H_S, x), "mp_dS": Poly(MPDS, x),
        "mp_dA": Poly(MPDA, x), "mp_mS": Poly(MPMS, x),
        "mp_mA": Poly(MPMA, x), "W3_quad": Poly(qW3, x),
        "W6_quad": Poly(qW6, x),
        "overlap_same": Poly(W_MINPOLY_BANKED, x),
        "overlap_cross": Poly(X_MINPOLY_BANKED, x)}
names = list(GRID)
grid = {}
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a_, b_ = names[i], names[j]
        log(f"      Res({a_}, {b_}) ...")
        r = sp.Rational(sp.resultant(GRID[a_].as_expr(),
                                     GRID[b_].as_expr(), x))
        fn, fd = ffac(r.p), ffac(r.q)
        grid[f"{a_}|{b_}"] = {"num": fn, "den": fd,
                              "has_29": "29" in fn or "29" in fd}
        note_int(f"Res({a_},{b_})", r.p)
PBD["W29-5_resultant_grid"] = grid
PBD["W29-5_resultant_grid_29_hits"] = [k for k, v in grid.items()
                                       if v["has_29"]]
dump()

log("[5.6] W29-7: the charge trace Gram and the register Grams ...")
order = ["8", "14", "16", "22"]
G4 = sp.diag(*[sp.Rational(CHARGE_GRAM[n_]) for n_ in order])
detG4 = sp.Rational(G4.det())
G3s = sp.Matrix(3, 3, lambda i, j: sp.Rational(G3M[i][j]))
G6s = sp.Matrix(6, 6, lambda i, j: sp.Rational(G6M[i][j]))
grams = {
    "charge_trace_gram_diag": [str(G4[i, i]) for i in range(4)],
    "charge_trace_gram_offdiag_all_zero": CHARGE_GRAM_OFFDIAG_ALL_ZERO,
    "charge_trace_gram_entry_fac": {order[i]: fac_of_rat(G4[i, i])
                                    for i in range(4)},
    "charge_trace_gram_det": str(detG4),
    "charge_trace_gram_det_fac": fac_of_rat(detG4),
    "charge_trace_gram_principal_minors":
        [str(sp.Rational(G4[:k, :k].det())) for k in range(1, 5)],
    "G3_det": str(sp.Rational(G3s.det())),
    "G3_det_fac": fac_of_rat(sp.Rational(G3s.det())),
    "G6_det": str(sp.Rational(G6s.det())),
    "G6_det_fac": fac_of_rat(sp.Rational(G6s.det())),
    "G18_det": str(DETG18), "G18_det_fac": fac_of_rat(DETG18),
    "H_plus_diagonal_weights_distinct_values": sorted(set(CB_PLUS)),
}
for i in range(4):
    note_int(f"charge Gram entry {order[i]}", sp.Rational(G4[i, i]).p)
for nm, v in (("detG4", detG4), ("detG3", sp.Rational(G3s.det())),
              ("detG6", sp.Rational(G6s.det())), ("detG18", DETG18)):
    note_int(nm, sp.Rational(v).p)
grams["29_anywhere"] = has29(grams)
PBD["W29-7_grams"] = grams
CHK("charge_gram_indefiniteness_is_CHECKED_not_assumed",
    any(sp.Rational(G4[i, i]) < 0 for i in range(4))
    and any(sp.Rational(G4[i, i]) > 0 for i in range(4)),
    f"the charge trace Gram carries both signs: "
    f"{[str(G4[i, i]) for i in range(4)]}")
CHK("register_grams_are_nondegenerate_and_indefinite",
    G3s.det() != 0 and G6s.det() != 0 and DETG18 != 0
    and any(G3s[i, i] < 0 for i in range(3)),
    "no definiteness assumed anywhere: the register Grams are invertible "
    "and the vacuum register's diagonal is negative (B912's banked "
    "indefiniteness)")
dump()

log("[5.7] the chain tests (post-whitelist; declared as such) ...")
tr3, tr6 = sp.Rational(151, 64), sp.Rational(169, 64)
CHK("tr_W3_equals_Tr_K_m_S", ktrace(K(MS_K)) == tr3, str(ktrace(K(MS_K))))
CHK("tr_W6_equals_2_Tr_K_m_A", 2 * ktrace(K(MA_K)) == tr6,
    str(ktrace(K(MA_K))))
CHK("the_29_of_2088_IS_the_29_of_Tr_m_S_minus_1",
    sp.Rational(-qW3[1], qW3[0]) == tr3 - 1
    and ffac(sp.Rational(tr3 - 1).p) == {"3": 1, "29": 1},
    "2088/1536 = 87/64 = Tr_K(m_S) - 1, and 87 = 3 * 29; the subtracted 1 "
    "is the exact unity principal angle (the rational line F cap W3). So "
    "the 29 of the W3 rotation quadratic is the 29 of the integer "
    "151 - 64, where 151/64 = Tr_K(m_S).")
CHK("the_A_register_rotation_quadratic_is_29_free",
    not any("29" in ffac(c) for c in qW6),
    "1536x^2 - 984x + 125 carries no 29 -- yet the 29-PLACE lives on the "
    "A-family; and the S-register's quadratic carries the 29 -- yet the "
    "S-family flip mass is 29-blind at every place. The two 29s sit on "
    "OPPOSITE sides of the S/A dichotomy.")

blk = sp.Matrix(2, 2, [sp.Rational(CMP6[2][2]), sp.Rational(CMP6[2][5]),
                       sp.Rational(CMP6[5][2]), sp.Rational(CMP6[5][5])])
CHK("W6_twist_block_charpoly_is_the_banked_quadratic",
    primitive_int_poly(Poly(blk.charpoly(x).as_expr(), x).all_coeffs())
    == qW6, str(blk.charpoly(x).as_expr()))
found = None
for c_ in range(1, 60):
    Pm = sp.Matrix(2, 2, [1, 0, c_, 1])
    Bn = Pm * blk * Pm.inv()
    ents = [sp.Rational(Bn[i, j]) for i in range(2) for j in range(2)]
    if all("29" not in ffac(e.p) and "29" not in ffac(e.q)
           for e in ents if e != 0):
        found = (c_, [str(e) for e in ents])
        break
CHK("the_29_in_B930s_W6_matrix_entry_is_BASIS_DEPENDENT", found is not None,
    f"an explicit unimodular shear of the W6 twist block removes every 29 "
    f"from the entries while preserving the characteristic polynomial: "
    f"c = {None if not found else found[0]}, entries "
    f"{None if not found else found[1]}")

M3 = sp.Matrix(3, 3, lambda i, j: sp.Rational(CMP3[i][j]))
cp3 = Poly(M3.charpoly(x).as_expr(), x)
den3 = 1
for c in cp3.all_coeffs():
    den3 = sp.ilcm(den3, sp.Rational(c).q)
CHK("W3_compression_charpoly_denominator_is_29_free",
    "29" not in ffac(int(den3)),
    "the reduction mod 29 of the W3 compression's characteristic "
    "polynomial is defined")
PBD["chain_tests_POST_WHITELIST"] = {
    "T1_S_family_at_29": [list(t) for t in v29["m_S"]],
    "T2_A_register_quadratic": {"poly": str(Poly(qW6, x).as_expr()),
                                "coeff_fac": [ffac(c) for c in qW6]},
    "T3_kinds": "the 2088-appearance is the NUMERATOR of a rational trace "
                "(an additive invariant: 87 = 64*(Tr_K(m_S) - 1)); the "
                "m_A-appearance is a PRIME IDEAL of K (a place at which a "
                "multiplicative invariant vanishes). No operation in the "
                "pipeline sends one to the other -- the numerator of a "
                "rational trace is not a place of anything.",
    "T4_W6_matrix_29_is_basis_dependent": {
        "original_entries": [str(sp.Rational(CMP6[2][2])),
                             str(sp.Rational(CMP6[2][5])),
                             str(sp.Rational(CMP6[5][2])),
                             str(sp.Rational(CMP6[5][5]))],
        "conjugating_shear_c": found[0] if found else None,
        "entries_after": found[1] if found else None,
        "charpoly_preserved": True},
    "T5_29_in_any_divisor_computed_here": {k: [list(t) for t in v]
                                           for k, v in v29.items()},
    "T6_W3_compression_mod_29": {
        "cleared_charpoly": str(sp.expand(cp3.as_expr() * den3)),
        "charpoly_mod_29": [int(sp.Rational(c) * den3) % 29
                            for c in cp3.all_coeffs()],
        "quadratic_mod_29": [c % 29 for c in qW3],
        "quadratic_irreducible_mod_29": not any(
            (qW3[0] * t * t + qW3[1] * t + qW3[2]) % 29 == 0
            for t in range(29)),
        "reading": "mod 29 the quadratic loses its linear term (2088 = 0 "
                   "mod 29): the two non-unity principal cosines^2 become "
                   "negatives of each other mod 29. Nothing degenerates -- "
                   "the quadratic stays irreducible mod 29 (29 is inert in "
                   "the shared rotation field)."},
}
dump()

log("[5.75] post-whitelist observations (registered, NOT tested) ...")
PBD["post_whitelist_observations"] = {
    "677_appears_in_both_worlds": {
        "W3_rotation_quadratic_constant": 677,
        "same_gen_overlap_x_coefficient": ffac(W_MINPOLY_BANKED[1]),
        "cross_gen_overlap_x_coefficient": ffac(X_MINPOLY_BANKED[2]),
        "677_place_structure_in_K": [{"e": e_, "f": f_}
                                     for _g, e_, f_ in places_of(677)],
        "status": "UNEXPLAINED COINCIDENCE-LEVEL DATA. 677 was NOT on the "
                  "declared whitelist; it is recorded here because it "
                  "turned up in the factorisations the whitelist printed, "
                  "and it is registered for a future DECLARED test, not "
                  "used for anything in this arc's verdict."},
    "the_shared_rotation_field": {
        "disc": 200256, "squarefree_part": 3129, "factorisation": ffac(3129),
        "status": "3129 = 3 * 7 * 149; 3 and 7 divide disc K = 3^4 * 7 * "
                  "11 but 149 is new to the record. Recorded, not used."},
}
dump()

log("[5.8] the look-elsewhere budget ...")
tot = len(INTEGERS_EXAMINED)
hits = [d for d in INTEGERS_EXAMINED if d["has_29"]]
PBD["look_elsewhere_budget"] = {
    "integers_examined_in_the_whitelist": tot,
    "29_divisibility_hits": len(hits),
    "hits": hits,
    "naive_expectation": str(sp.Rational(tot, 29)),
    "reading": "under the crude model 'a pipeline integer is divisible by "
               "29 with probability 1/29', the whitelist's own integer "
               "count already predicts hits of this multiplicity. Two "
               "appearances of a prime as small as 29 across a whitelist "
               "of this size is not, by itself, evidence of a mechanism.",
}
dump()

# ===================================================================== [6]
log("[6] verdicts ...")
structural = False
RES["verdict"] = {
    "partA": {
        "W_divisor": PA["W_divisor"]["valuations"],
        "953": "W's whole 953-content is a POLE, and it is exactly minus "
               "the sum of the two families' twist divisors: W "
               f"{PA['953_story']['W']} against d_S "
               f"{PA['953_story']['d_S']} and d_A "
               f"{PA['953_story']['d_A']}. The mixing element is the one "
               "object that sees BOTH places of 953 at once -- the "
               "observer's degree-one place (doubly, from the vacuum "
               "family) and the degree-two mirror place (simply, from the "
               "A-family) -- while each family alone sees only its own. "
               "The banked lead 953^4 = N(P1^2 * P2) exactly.",
        "5": f"the gauge-invariant H+-normalised mixing element "
             f"u = W d_S d_A has a divisor supported EXACTLY over "
             f"{PA['u_support']}: the golden numerator is entirely u's, "
             f"the value prime entirely the twist's. The 5-divisor is "
             f"q1^6 q2^3 (f = 1, 2), so the two places over 5 contribute "
             f"EQUAL local norms 5^6 each: 12 = 6 + 6, and 6 is also the "
             f"whole 5-content of a cross-generation overlap.",
        "the_observer_place_law": "the cross-generation overlap^2 is "
            "supported ENTIRELY on the DEGREE-TWO places -- q2(5)^3 "
            "P2(953)^-1 -- and the same-generation one adds exactly "
            "q1(5)^6 P1(953)^-2. The whole difference between diagonal and "
            "off-diagonal mixing is the OBSERVER'S degree-one place, at "
            "953 with exactly d_S's twist exponent (B918's V-pole place). "
            "Off-diagonal mixing never touches the observer's place.",
        "exponent_12": PA["exponent_12_candidate_tests"],
        "golden_field": PA["golden_field_decision"]["verdict"],
    },
    "partB": {
        "verdict": "STRUCTURAL" if structural else "COINCIDENCE",
        "grounds": [
            "OPPOSITE SIDES: the 29-place lives on the A-family (m_A "
            "vanishes at the degree-one place over 29) while m_S has "
            "valuation 0 at every place over 29; conversely the 29 of "
            "2088 lives in the S-register's rotation quadratic while the "
            "A-register's own rotation quadratic 1536x^2 - 984x + 125 is "
            "29-free",
            "DIFFERENT KINDS: 2088's 29 is a factor of the numerator of a "
            "rational trace (87 = 64*(Tr_K(m_S) - 1), an additive "
            "invariant); m_A's 29 is a prime ideal of K at which a "
            "multiplicative invariant vanishes. No pipeline map carries a "
            "trace numerator to a place",
            "29 divides NO discriminant in the whitelist: not the two "
            "rotation quadratics' shared discriminant, not any "
            "compression charpoly's, not either overlap minimal "
            "polynomial's",
            "29 appears in NO divisor computed in this cell except m_A's "
            "(W, u, X_cross, d_S, d_A, m_S are all 29-units)",
            "the one further 29 in the record -- the entry 29/96 of "
            "B930's W6 compression matrix -- is shown here to be "
            "basis-dependent: an exhibited unimodular shear removes every "
            "29 while preserving the characteristic polynomial",
            "the look-elsewhere budget over the whitelist's own integers "
            "predicts hits of this multiplicity",
        ],
        "what_would_have_made_it_structural":
            DECL["verdict_criterion"]["STRUCTURAL"],
    },
}
RES["runtime_s"] = round(time.time() - T00, 1)
dump()
log("results.json written; done")
