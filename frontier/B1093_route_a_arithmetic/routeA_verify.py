"""
Independent re-derivation, from scratch, of claims about
K = Q[x]/(f), f = x^3 - 12x - 5.

Everything here is original code written for this task (sympy + mpmath
only; no PARI/GP, no external number-theory calls). Algorithms
(Dedekind's criterion, Kummer-Dedekind factorization, norm form via
companion matrix, Minkowski bound, sign-map / narrow class number)
are implemented by hand from their mathematical definitions.
"""

import sympy as sp
from sympy import symbols, Poly, GF, ZZ, QQ, discriminant, resultant, gcd, Matrix, Rational
import mpmath as mp

mp.mp.dps = 50  # working precision

x = symbols('x')
f_expr = x**3 - 12*x - 5
f = Poly(f_expr, x, domain=ZZ)

print("="*100)
print("SETUP")
print("="*100)
print(f"f(x) = {f_expr}")

# ---------------------------------------------------------------------
# ITEM 5 (do first, it's a prerequisite sanity check): irreducibility,
# totally-real check, 30-digit roots
# ---------------------------------------------------------------------
print()
print("="*100)
print("ITEM 5: sanity anchors")
print("="*100)

is_irred = f.is_irreducible
print(f"f irreducible over Q: {is_irred}")

# real root count via Sturm's theorem (sympy's real_roots / count_roots),
# implemented by calling sympy's Sturm-sequence-based real root counter,
# which is a standard exact (no floating point) algorithm.
real_roots_exact = sp.real_roots(f_expr, x)
print(f"Number of real roots (Sturm/exact): {len(real_roots_exact)}")

# also cross-check total roots = 3 and none complex, via CRootOf (exact
# algebraic representation of each root, ordered) + evalf high precision
roots = [sp.CRootOf(f_expr, i) for i in range(3)]
print(f"CRootOf count: {len(roots)}")
roots_hp = [r.evalf(30) for r in roots]
for i, r in enumerate(roots_hp):
    print(f"  root[{i}] (30 digits) = {r}")

all_real = all(sp.im(r) == 0 for r in roots_hp)
print(f"All three CRootOf roots have zero imaginary part at 30 digits: {all_real}")
print(f"=> CONCLUSION: totally real cubic verified: {is_irred and len(real_roots_exact)==3 and all_real}")

# ---------------------------------------------------------------------
# ITEM 1: discriminant, factorization, Dedekind's criterion
# ---------------------------------------------------------------------
print()
print("="*100)
print("ITEM 1: discriminant + maximal order")
print("="*100)

disc_f = discriminant(f_expr, x)
print(f"disc(f) computed via sympy.discriminant = {disc_f}")

# cross-check via my own -4p^3-27q^2 formula for depressed cubic x^3+px+q
p_coeff = -12
q_coeff = -5
disc_formula = -4*p_coeff**3 - 27*q_coeff**2
print(f"cross-check via -4p^3-27q^2 (p={p_coeff}, q={q_coeff}) = {disc_formula}")
assert disc_f == disc_formula, "MISMATCH in discriminant formula cross-check!"

fac = sp.factorint(int(disc_f))
print(f"factorization of disc(f) = {disc_f}: {fac}")
fac_str = " * ".join(f"{b}^{e}" if e>1 else f"{b}" for b,e in fac.items())
print(f"  i.e. disc(f) = {fac_str}")

# candidate primes for non-maximality: p such that p^2 | disc(f)
candidates = [p for p,e in fac.items() if e >= 2]
print(f"primes p with p^2 | disc(f) (only candidates for [O_K:Z[theta]] > 1): {candidates}")

def dedekind_criterion(f_poly, p):
    """
    Dedekind's criterion at prime p for f (monic, integer coeffs).
    Returns (is_p_maximal: bool, details: dict)

    Implementation (Cohen, "A Course in Computational Algebraic Number
    Theory", Thm 6.1.4), written from the definition:

      1. Factor f mod p into irreducibles: fbar = prod gbar_i^{e_i}.
      2. Let g = prod g_i (lift, each factor taken once, "radical").
      3. Let h = prod g_i^{e_i - 1}, using the SAME lifts as in g, so
         that g*h ≡ f (mod p) as polynomials.
      4. Since g*h ≡ f mod p, T := (g*h - f)/p is an integer polynomial.
      5. Z[theta] is maximal at p  <=>  gcd( Tbar, gcd(gbar,hbar) ) = 1
         in F_p[x], where gcd(gbar,hbar) = prod_{e_i>=2} gbar_i
         (the "repeated part").
      p | [O_K:Z[theta]]  <=>  that gcd is non-trivial.
    """
    fp = Poly(f_poly.as_expr(), x, modulus=p)
    factors = fp.factor_list()[1]  # list of (poly, exponent) mod p

    # lift each irreducible factor to Z[x] using its GF(p) representative
    # coefficients taken as the standard 0..p-1 residues (sympy already
    # gives that representation under modulus=p).
    g_lift = Poly(1, x, domain=ZZ)
    h_lift = Poly(1, x, domain=ZZ)
    repeated_factors_mod_p = []
    for (gi_modp, ei) in factors:
        gi_int = Poly(gi_modp.as_expr(), x, domain=ZZ)  # lift, coeffs already in [0,p)
        g_lift = g_lift * gi_int
        if ei >= 2:
            h_lift = h_lift * gi_int**(ei-1)
            repeated_factors_mod_p.append((gi_modp, ei))

    prod_gh = g_lift * h_lift
    diff = prod_gh - f_poly
    diff_coeffs = diff.all_coeffs() if diff.degree() >= 0 else [0]
    # verify every coefficient of g*h - f is divisible by p (sanity check
    # of the construction itself)
    assert all(c % p == 0 for c in diff_coeffs), "g*h != f mod p -- construction bug"
    T = Poly([c // p for c in diff.all_coeffs()], x, domain=ZZ) if diff.degree() >= 0 else Poly(0, x, domain=ZZ)

    Tbar = Poly(T.as_expr(), x, modulus=p)
    gbar = Poly(g_lift.as_expr(), x, modulus=p)
    hbar = Poly(h_lift.as_expr(), x, modulus=p)

    D = sp.gcd(gbar, hbar)  # = product of repeated gbar_i's (up to unit)
    final_gcd = sp.gcd(D, Tbar)

    is_unit = final_gcd.degree() == 0  # constant (nonzero, since GF(p) field) => gcd is 1
    return (is_unit, {
        "factorization_mod_p": factors,
        "repeated_factors": repeated_factors_mod_p,
        "g": g_lift, "h": h_lift, "T": T,
        "gbar": gbar, "hbar": hbar, "D": D, "final_gcd": final_gcd,
    })

maximal_at_all_candidates = True
for p in candidates:
    ok, details = dedekind_criterion(f, p)
    print()
    print(f"--- Dedekind's criterion at p={p} ---")
    print(f"  f mod {p} factors as: {details['factorization_mod_p']}  (as (poly,mult) mod {p})")
    print(f"  repeated (mult>=2) irreducible factors mod {p}: {details['repeated_factors']}")
    print(f"  g (radical lift)   = {details['g'].as_expr()}")
    print(f"  h (lift of f/g)    = {details['h'].as_expr()}")
    print(f"  T = (g*h - f)/{p}  = {details['T'].as_expr()}")
    print(f"  gbar = {details['gbar'].as_expr()},  hbar = {details['hbar'].as_expr()}  (mod {p})")
    print(f"  D = gcd(gbar,hbar) = {details['D'].as_expr()}  (mod {p})")
    print(f"  gcd(D, Tbar)       = {details['final_gcd'].as_expr()}  (mod {p})")
    print(f"  => Z[theta] is {p}-maximal: {ok}   (p | index iff this is False)")
    maximal_at_all_candidates = maximal_at_all_candidates and ok

no_other_candidates = (len(candidates) == 0) or True  # by definition, only primes with p^2|disc can divide index
Z_theta_is_maximal_order = maximal_at_all_candidates
print()
print(f"Primes with p^2 | disc(f): {candidates}  (all other primes automatically cannot divide the index)")
print(f"Z[theta] maximal at every candidate prime: {maximal_at_all_candidates}")
print(f"=> CONCLUSION: Z[theta] = O_K : {Z_theta_is_maximal_order}")
if Z_theta_is_maximal_order:
    disc_K = disc_f
    print(f"=> disc(K) = disc(f) = {disc_K} = {fac_str}")
else:
    print("=> disc(K) != disc(f); would need index computation (NOT the case here per above).")

print()
print("SAVED FOR LATER SECTIONS:")
print(f"  disc_K = {disc_f}")

# ---------------------------------------------------------------------
# Norm form N(a + b*theta + c*theta^2), derived two independent ways:
#   (A) resultant(f(x), a+bx+cx^2, x)   [since f monic, Res(f,g) = prod g(alpha_i) = N(g(theta))]
#   (B) det(a*I + b*C + c*C^2), C = companion matrix of f
# ---------------------------------------------------------------------
print()
print("="*100)
print("NORM FORM  N(a + b*theta + c*theta^2)  -- derived two ways, cross-checked")
print("="*100)

a, b, c = symbols('a b c')

# (A) resultant
norm_form_res = sp.resultant(f_expr, a + b*x + c*x**2, x)
norm_form_res = sp.expand(norm_form_res)
print(f"(A) via resultant(f, a+bx+cx^2): N(a,b,c) = {norm_form_res}")

# (B) companion matrix
# f = x^3 - 12x - 5  => x^3 = 12x + 5, companion matrix in basis {1,theta,theta^2}
# C * (1,theta,theta^2)^T represents multiplication by theta:
#   theta*1       = theta
#   theta*theta   = theta^2
#   theta*theta^2 = theta^3 = 12*theta + 5
C = Matrix([[0, 0, 5],
            [1, 0, 12],
            [0, 1, 0]])
# sanity: char poly of C should be f
charpoly_C = C.charpoly(x).as_expr()
print(f"    char.poly(C) = {sp.expand(charpoly_C)}   (must equal f(x) = {f_expr})")
assert sp.expand(charpoly_C - f_expr) == 0, "companion matrix construction is wrong"

M = a*sp.eye(3) + b*C + c*C**2
norm_form_mat = sp.expand(M.det())
print(f"(B) via det(aI+bC+cC^2):        N(a,b,c) = {norm_form_mat}")

assert sp.expand(norm_form_res - norm_form_mat) == 0, "MISMATCH between the two norm-form derivations!"
print("Both derivations AGREE exactly.")

norm_form = norm_form_res

# Build a pure-Python exact-integer evaluator directly from the monomial
# dict (avoids lambdify's module-detection / float-casting entirely).
_norm_poly = Poly(norm_form, a, b, c, domain=ZZ)
_norm_monoms = list(zip(_norm_poly.monoms(), _norm_poly.coeffs()))  # [((ea,eb,ec), coeff), ...]
def norm_func(aa, bb, cc):
    total = 0
    for (ea, eb, ec), coeff in _norm_monoms:
        total += int(coeff) * (aa**ea) * (bb**eb) * (cc**ec)
    return total

# quick self-test: N(1,0,0) should be f(0)'s... actually N(1,0,0)=N(1)=1 (norm of the identity element 1)
print(f"self-test N(1,0,0) = {norm_func(1,0,0)}  (should be 1, the norm of the element '1')")
print(f"self-test N(0,1,0) = {norm_func(0,1,0)}  (should be N(theta) = (-1)^3 * f(0) = {(-1)**3 * f_expr.subs(x,0)})")

# ---------------------------------------------------------------------
# ITEM 2: class number via Minkowski bound + Kummer-Dedekind + principal
#         generator search
# ---------------------------------------------------------------------
print()
print("="*100)
print("ITEM 2: class number h(K)")
print("="*100)

n_deg = 3
r1, r2 = 3, 0  # totally real cubic
disc_K = disc_f

Mink_exact = Rational(sp.factorial(n_deg), n_deg**n_deg) * sp.sqrt(disc_K) * Rational(4,1)**r2 / sp.pi**r2
Mink_val = sp.nsimplify(Mink_exact)
Mink_numeric = float(Mink_exact.evalf(20))
print(f"Minkowski bound M_K = (n!/n^n)*sqrt(|disc_K|)*(4/pi)^r2 , n=3,r1=3,r2=0")
print(f"  = (3!/3^3) * sqrt({disc_K})  = (6/27)*sqrt({disc_K}) = (2/9)*sqrt({disc_K})")
print(f"  exact form: {sp.nsimplify(Rational(sp.factorial(n_deg), n_deg**n_deg))} * sqrt({disc_K})")
print(f"  numeric value = {Mink_numeric:.10f}")

import math
bound_floor = math.floor(Mink_numeric)
print(f"  => need to check all primes p <= {Mink_numeric:.6f}, i.e. p in {[pp for pp in sp.primerange(2, bound_floor+2) if pp<=Mink_numeric]}")

primes_to_check = [pp for pp in sp.primerange(2, bound_floor+2) if pp <= Mink_numeric]

def factor_mod_p_KD(p):
    """Kummer-Dedekind: factor f mod p (valid since Z[theta]=O_K globally,
       index=1, so this applies unconditionally at every prime)."""
    fp = Poly(f_expr, x, modulus=p)
    return fp.factor_list()[1]

def ideal_membership(elem_abc, p, g_factor):
    """Is a+b*theta+c*theta^2 (elem_abc=(a,b,c)) in the prime ideal
       (p, g_factor(theta))?  Test: (a+bx+cx^2) mod g_factor(x) == 0 in F_p[x]."""
    aa, bb, cc = elem_abc
    elem_poly = Poly(aa + bb*x + cc*x**2, x, modulus=p)
    gfac = Poly(g_factor.as_expr(), x, modulus=p)
    if elem_poly.degree() < 0:  # zero polynomial
        return True
    _, rem = sp.div(elem_poly, gfac)
    return rem == 0 or (hasattr(rem,'is_zero') and rem.is_zero)

print()
print("Kummer-Dedekind factorization of each rational prime p <= Minkowski bound:")
prime_ideals_needed = []  # list of dicts: p, factor poly, mult e, residue degree d, ideal norm
for p in primes_to_check:
    facs = factor_mod_p_KD(p)
    print(f"  p={p}:  f mod {p} = " + " * ".join(f"({gi.as_expr()})^{ei}" for gi,ei in facs))
    for gi, ei in facs:
        d = gi.degree()
        ideal_norm = p**d
        entry = {"p": p, "g": gi, "e": ei, "d": d, "norm": ideal_norm}
        if ideal_norm <= Mink_numeric + 1e-9:
            prime_ideals_needed.append(entry)
            print(f"      -> prime ideal from factor ({gi.as_expr()}), mult e={ei}, residue degree d={d}, "
                  f"Norm = {p}^{d} = {ideal_norm}   <= bound: NEEDS principality check")
        else:
            print(f"      -> prime ideal from factor ({gi.as_expr()}), mult e={ei}, residue degree d={d}, "
                  f"Norm = {p}^{d} = {ideal_norm}   > bound: no check needed")

print()
print(f"Total prime ideals with norm <= {Mink_numeric:.4f} requiring a principality check: {len(prime_ideals_needed)}")

def search_generator(target_norm, p, g_factor, box=8):
    """Search a,b,c in [-box,box]^3 for |N(a+b theta+c theta^2)| = target_norm
       AND membership in the ideal (p, g_factor(theta)). Returns list of
       valid (a,b,c) sorted by L1 'simplicity', or [] if none found."""
    found = []
    for aa in range(-box, box+1):
        for bb in range(-box, box+1):
            for cc in range(-box, box+1):
                if aa==0 and bb==0 and cc==0:
                    continue
                nv = norm_func(aa,bb,cc)
                if abs(nv) == target_norm:
                    if ideal_membership((aa,bb,cc), p, g_factor):
                        found.append((aa,bb,cc,nv))
    found.sort(key=lambda t: (abs(t[0])+abs(t[1])+abs(t[2]), max(abs(t[0]),abs(t[1]),abs(t[2]))))
    return found

print()
print("Searching for principal generators (box = [-8,8]^3 on (a,b,c), element = a+b*theta+c*theta^2):")
all_principal = True
generator_report = []
for entry in prime_ideals_needed:
    p, gi, ei, d, Nrm = entry["p"], entry["g"], entry["e"], entry["d"], entry["norm"]
    sols = search_generator(Nrm, p, gi, box=8)
    tag = f"p={p}, factor=({gi.as_expr()}), e={ei}, d={d}, Norm={Nrm}"
    if sols:
        best = sols[0]
        all_principal = all_principal and True
        print(f"  [{tag}]")
        print(f"      PRINCIPAL. generator alpha = {best[0]} + {best[1]}*theta + {best[2]}*theta^2 ,"
              f"  N(alpha) = {best[3]}   (# solutions found in box: {len(sols)})")
        generator_report.append((tag, best))
    else:
        all_principal = False
        print(f"  [{tag}]  NO GENERATOR FOUND in box [-8,8]^3 -- INCONCLUSIVE at this search radius")
        generator_report.append((tag, None))

print()
print(f"=> Every needed prime ideal principal (within search box): {all_principal}")
h_K = 1 if all_principal else None
print(f"=> class number h(K) = {h_K if h_K is not None else 'UNRESOLVED by this search (would need larger box or ideal-theoretic argument)'}")

# ---------------------------------------------------------------------
# ITEM 3: units u1, u2 -- norm verification + independence
# ---------------------------------------------------------------------
print()
print("="*100)
print("ITEM 3: units u1 = theta^2+2theta-4,  u2 = 3theta^2+6theta+2")
print("="*100)

# u1 = a+b*theta+c*theta^2 with (a,b,c) = (-4,2,1)
# u2 = a+b*theta+c*theta^2 with (a,b,c) = (2,6,3)
u1_abc = (-4, 2, 1)
u2_abc = (2, 6, 3)

N_u1 = norm_func(*u1_abc)
N_u2 = norm_func(*u2_abc)
print(f"u1 = -4 + 2*theta + theta^2   => N(u1) = {N_u1}   (claimed +1)")
print(f"u2 = 2 + 6*theta + 3*theta^2  => N(u2) = {N_u2}   (claimed -1)")

# cross-check independently via direct resultant substitution (not reusing norm_form machinery blindly)
u1_expr = -4 + 2*x + x**2
u2_expr = 2 + 6*x + 3*x**2
N_u1_direct = sp.resultant(f_expr, u1_expr, x)
N_u2_direct = sp.resultant(f_expr, u2_expr, x)
print(f"cross-check via direct resultant(f, u1) = {N_u1_direct}")
print(f"cross-check via direct resultant(f, u2) = {N_u2_direct}")

# also cross-check via literal product over the three high-precision roots
N_u1_numeric = mp.mpf(1)
N_u2_numeric = mp.mpf(1)
for r in roots_hp:
    rr = mp.mpf(str(sp.re(r)))
    N_u1_numeric *= (-4 + 2*rr + rr**2)
    N_u2_numeric *= (2 + 6*rr + 3*rr**2)
print(f"cross-check via product over 3 numeric embeddings: N(u1) ~ {N_u1_numeric}")
print(f"cross-check via product over 3 numeric embeddings: N(u2) ~ {N_u2_numeric}")

u1_is_unit = (N_u1 == 1)
u2_is_unit = (N_u2 == -1)
print(f"u1 is a unit (N=+1 exactly, as claimed): {u1_is_unit}")
print(f"u2 is a unit (N=-1 exactly, as claimed): {u2_is_unit}")

# independence check: rank-2 log-embedding matrix (using embeddings 1,2 of the
# 3 real embeddings; unit rank r1+r2-1 = 2 here). If u1^m u2^n were = +-1 for
# some non-trivial (m,n), the two log-vectors would be parallel (det=0).
print()
print("Independence check (multiplicative independence of u1,u2, via log-embedding rank):")
def eval_abc_at_root(abc, r):
    aa, bb, cc = abc
    return aa + bb*r + cc*r**2

log_rows = []
for i, r in enumerate(roots_hp):
    rr = mp.mpf(str(sp.re(r)))
    v1 = eval_abc_at_root(u1_abc, rr)
    v2 = eval_abc_at_root(u2_abc, rr)
    log_rows.append((mp.log(abs(v1)), mp.log(abs(v2))))
    print(f"  embedding {i} (theta={float(rr):.6f}): u1 -> {float(v1):.8f}, u2 -> {float(v2):.8f}, "
          f"log|u1|={float(log_rows[-1][0]):.8f}, log|u2|={float(log_rows[-1][1]):.8f}")

# sum of logs across all 3 embeddings should be 0 (since |N(u_i)|=1) -- sanity check
sum_log_u1 = sum(row[0] for row in log_rows)
sum_log_u2 = sum(row[1] for row in log_rows)
print(f"  sanity: sum of log|u1| over all 3 embeddings = {float(sum_log_u1):.2e}  (should be ~0)")
print(f"  sanity: sum of log|u2| over all 3 embeddings = {float(sum_log_u2):.2e}  (should be ~0)")

# 2x2 minor using embeddings 0,1 (any 2 of the 3 -- rank-2 lattice lives in the trace-zero plane)
M2 = mp.matrix([[log_rows[0][0], log_rows[0][1]],
                [log_rows[1][0], log_rows[1][1]]])
det2 = M2[0,0]*M2[1,1] - M2[0,1]*M2[1,0]
print(f"  2x2 log-determinant (embeddings 0,1) = {float(det2):.8f}")
independent = abs(det2) > mp.mpf('1e-10')
print(f"  => u1, u2 multiplicatively independent (nonzero log-determinant, hence not related by any "
      f"u1^m u2^n = root of unity): {independent}")
print(f"  (fundamentality of {{u1,u2}} as a full basis of O_K^* / torsion is ASSUMED-FROM-SOURCE; "
      f"NOT proved here -- only unit-ness (N=+-1) and rank-2 independence are verified.)")

# ---------------------------------------------------------------------
# ITEM 4: signature rank + narrow class number
# ---------------------------------------------------------------------
print()
print("="*100)
print("ITEM 4: signature rank / narrow class number h+")
print("="*100)

print("Sign vectors (sigma_1,sigma_2,sigma_3) of -1, u1, u2 at the 3 real embeddings")
print("(embeddings ordered as roots_hp[0],roots_hp[1],roots_hp[2] from item 5, 30-digit precision):")

def sign_vector(abc_or_const, roots_list):
    signs = []
    for r in roots_list:
        rr = mp.mpf(str(sp.re(r)))
        if abc_or_const == "minus_one":
            val = mp.mpf(-1)
        else:
            aa, bb, cc = abc_or_const
            val = aa + bb*rr + cc*rr**2
        signs.append(1 if val > 0 else -1)
    return signs

sv_minus1 = sign_vector("minus_one", roots_hp)
sv_u1 = sign_vector(u1_abc, roots_hp)
sv_u2 = sign_vector(u2_abc, roots_hp)

print(f"  sgn(-1) = {tuple(sv_minus1)}")
print(f"  sgn(u1) = {tuple(sv_u1)}")
print(f"  sgn(u2) = {tuple(sv_u2)}")

# map to F_2: -1 -> 1, +1 -> 0  (group hom ({+-1},*) -> (F_2,+))
def to_f2(v):
    return [0 if s == 1 else 1 for s in v]

row_minus1 = to_f2(sv_minus1)
row_u1 = to_f2(sv_u1)
row_u2 = to_f2(sv_u2)
print(f"  in F_2 (+1->0, -1->1):  sgn(-1)={row_minus1}, sgn(u1)={row_u1}, sgn(u2)={row_u2}")

def rank_mod2(rows):
    """Plain Gaussian elimination over F_2, written by hand (no library GF(2) dependency)."""
    M = [r[:] for r in rows]
    nrows = len(M)
    ncols = len(M[0]) if nrows else 0
    rank = 0
    for col in range(ncols):
        pivot = None
        for r in range(rank, nrows):
            if M[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        for r in range(nrows):
            if r != rank and M[r][col] == 1:
                M[r] = [(M[r][k] ^ M[rank][k]) for k in range(ncols)]
        rank += 1
    return rank, M

rk, reduced = rank_mod2([row_minus1, row_u1, row_u2])
print(f"  F_2-rank of {{sgn(-1), sgn(u1), sgn(u2)}} matrix = {rk}   (claim: 3, i.e. surjective onto (Z/2)^3)")
print(f"  row-reduced form: {reduced}")

surjective = (rk == 3)
print(f"  => sign map surjective onto {{+-1}}^3: {surjective}")

index_signgroup = 2**3 // (2**rk)  # [{+-1}^3 : image(sign map)]
print(f"  => [{{+-1}}^3 : image(sign-map)] = 2^3 / 2^{rk} = {index_signgroup}")

print()
print("Narrow class number:  h+ = h * [{+-1}^{r1} : image(sign map)]   (r1=3 here)")
if h_K is not None:
    h_plus = h_K * index_signgroup
    print(f"  h = {h_K}  (from item 2)")
    print(f"  h+ = {h_K} * {index_signgroup} = {h_plus}")
else:
    print(f"  h from item 2 was not conclusively pinned down by the search -- h+ cannot be finalized numerically, "
          f"but structurally h+ = h * {index_signgroup}.")

print()
print("Since h=1 (item 2) => Cl(K) is the trivial group => |Cl/Cl^2| = |Cl/Cl^3| = 1 trivially "
      "(quotient of the trivial group by anything is trivial).")

# ---------------------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------------------
print()
print("="*100)
print("FINAL SUMMARY")
print("="*100)
print(f"1. disc(f)=6237=3^4*7*11: {disc_f==6237 and fac=={3:4,7:1,11:1}}.  Dedekind @3 maximal: {maximal_at_all_candidates}."
      f"  => Z[theta]=O_K: {Z_theta_is_maximal_order}, disc(K)={disc_f}.")
print(f"2. Minkowski bound = {Mink_numeric:.6f}. All {len(prime_ideals_needed)} required prime ideals principal: {all_principal}."
      f"  => h(K) = {h_K}")
print(f"3. N(u1)={N_u1} (claim +1): {u1_is_unit}.  N(u2)={N_u2} (claim -1): {u2_is_unit}.  "
      f"Independent (log-det != 0): {independent}")
print(f"4. sgn(-1)={tuple(sv_minus1)}, sgn(u1)={tuple(sv_u1)}, sgn(u2)={tuple(sv_u2)}.  "
      f"F_2-rank = {rk} (claim 3): {rk==3}.  h+ = {h_plus if h_K is not None else 'N/A'}")
print(f"5. f irreducible: {is_irred}.  3 real roots: {len(real_roots_exact)==3}.  "
      f"Totally real confirmed: {is_irred and len(real_roots_exact)==3 and all_real}")

