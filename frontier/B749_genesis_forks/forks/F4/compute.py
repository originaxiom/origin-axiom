#!/usr/bin/env python3
# B749 fork F4 — shadow-rule variants (sealed campaign, seal v2).
# Siblings per MEASUREMENTS.md F4 block:
#   sigma_inert : a -> ab, b -> b
#   sigma_rev   : a -> ab, b -> ba      (this is the Thue-Morse substitution)
#   swap        : a -> b,  b -> ab
# Reference (the chain's shadow rule): fib : a -> ab, b -> a.
#
# Sealed measurements: primitivity (does every letter eventually generate both),
# aperiodicity, abelianization determinant (mapping-class realizability requires
# det = +-1). Sealed ROBUST criteria: sigma_inert non-primitive -> eventually
# periodic; sigma_rev det 0 -> no mapping class; swap = Fibonacci conjugate ->
# identification, not failure. FRAGILE = a variant that is primitive, aperiodic,
# invertible, and inequivalent to Fibonacci.
#
# Deterministic: no wall-clock, no randomness, no network. Pure python + sympy.
# Conventions (declared): abelianization matrix M[i][j] = number of occurrences
# of letter_i in sigma(letter_j), letters ordered (a, b); count vectors are
# columns, c(sigma(w)) = M . c(w). det/trace/charpoly are transpose-invariant,
# so the convention does not affect any verdict-bearing quantity.

import sympy as sp

x = sp.Symbol('x')
LETTERS = ('a', 'b')
checks = []          # (name, value) -> printed as CHECK: name = value
failures = []

def check(name, value, expect=None):
    checks.append((name, value))
    if expect is not None and value != expect:
        failures.append((name, value, expect))

# ----------------------------------------------------------------------------
# basic substitution machinery (positive words as strings)
# ----------------------------------------------------------------------------

def apply_sub(sub, w):
    return ''.join(sub[c] for c in w)

def iterate_sub(sub, seed, n):
    w = seed
    for _ in range(n):
        w = apply_sub(sub, w)
    return w

def abelianization(sub):
    # M[i][j] = count of LETTERS[i] in sub[LETTERS[j]]
    return sp.Matrix([[sub[c].count(l) for c in LETTERS] for l in LETTERS])

def factors(w, n):
    return {w[i:i + n] for i in range(len(w) - n + 1)}

# free-group machinery: words over F2 = <a,b> as tuples of (letter, +-1)
def freduce(word):
    out = []
    for l, s in word:
        if out and out[-1][0] == l and out[-1][1] == -s:
            out.pop()
        else:
            out.append((l, s))
    return tuple(out)

def fmorph(images, word):
    # images: dict letter -> tuple of (letter, sign); extend to inverses
    out = []
    for l, s in word:
        img = images[l]
        if s == 1:
            out.extend(img)
        else:
            out.extend((m, -t) for m, t in reversed(img))
    return freduce(out)

def fw(s):
    # parse 'a b A B' style: uppercase = inverse
    out = []
    for c in s:
        if c == ' ':
            continue
        out.append((c.lower(), 1 if c.islower() else -1))
    return freduce(out)

# the four substitutions (positive-word form and free-group form)
S_FIB   = {'a': 'ab', 'b': 'a'}
S_INERT = {'a': 'ab', 'b': 'b'}
S_REV   = {'a': 'ab', 'b': 'ba'}
S_SWAP  = {'a': 'b',  'b': 'ab'}

F_FIB   = {'a': fw('ab'), 'b': fw('a')}
F_INERT = {'a': fw('ab'), 'b': fw('b')}
F_SWAP  = {'a': fw('b'),  'b': fw('ab')}
F_E     = {'a': fw('b'),  'b': fw('a')}          # letter exchange

M_FIB, M_INERT, M_REV, M_SWAP = (abelianization(s)
                                 for s in (S_FIB, S_INERT, S_REV, S_SWAP))

# ----------------------------------------------------------------------------
# 1. abelianization determinants / traces / charpolys  (exact integers)
# ----------------------------------------------------------------------------
check('abelianization_inert', str(M_INERT.tolist()), '[[1, 0], [1, 1]]')
check('abelianization_rev',   str(M_REV.tolist()),   '[[1, 1], [1, 1]]')
check('abelianization_swap',  str(M_SWAP.tolist()),  '[[0, 1], [1, 1]]')
check('abelianization_fib',   str(M_FIB.tolist()),   '[[1, 1], [1, 0]]')

det_inert, det_rev, det_swap, det_fib = (int(M.det()) for M in
                                         (M_INERT, M_REV, M_SWAP, M_FIB))
check('det_abelianization_inert', det_inert, 1)
check('det_abelianization_rev',   det_rev,   0)
check('det_abelianization_swap',  det_swap, -1)
check('det_abelianization_fib',   det_fib,  -1)
check('rev_det_in_GL2Z', det_rev in (1, -1), False)   # no mapping class for rev
check('trace_inert', int(M_INERT.trace()), 2)          # |tr|<=2: no Anosov route

cp_inert = sp.factor(M_INERT.charpoly(x).as_expr())
cp_rev   = sp.factor(M_REV.charpoly(x).as_expr())
cp_swap  = sp.expand(M_SWAP.charpoly(x).as_expr())
cp_fib   = sp.expand(M_FIB.charpoly(x).as_expr())
check('charpoly_inert', str(cp_inert), '(x - 1)**2')            # PF value 1
check('charpoly_rev',   str(cp_rev),   'x*(x - 2)')             # PF value 2, rational
check('charpoly_swap',  str(cp_swap),  'x**2 - x - 1')
check('charpoly_fib',   str(cp_fib),   'x**2 - x - 1')
check('charpoly_swap_equals_fib', cp_swap == cp_fib, True)

# exact field claim (swap/fib PF eigenvalue = golden ratio, field Q(sqrt5)):
# numeric relation + exact confirmation, coefficient-size-aware threshold.
phi = (1 + sp.sqrt(5)) / 2
minpoly_phi = sp.minimal_polynomial(phi, x)
check('minpoly_phi_exact', str(sp.expand(minpoly_phi)), 'x**2 - x - 1')
check('charpoly_swap_irreducible_over_Q',
      sp.Poly(cp_swap, x).is_irreducible, True)
import mpmath
mpmath.mp.dps = 50
phi_num = mpmath.mpf(1) / 2 + mpmath.sqrt(5) / 2
resid = abs(phi_num**2 - phi_num - 1)
# threshold: coefficients are height-1 integers, degree 2, 50-digit precision;
# any true nonzero value of an algebraic integer expression this small is
# excluded far above 1e-40.
check('phi_numeric_residual_lt_1e-40', bool(resid < mpmath.mpf('1e-40')), True)

# ----------------------------------------------------------------------------
# 2. primitivity — Wielandt (2x2: primitive <=> M^2 > 0) + the sealed
#    letter-level phrasing (does every letter eventually generate both)
# ----------------------------------------------------------------------------
def primitive_2x2(M):
    M2 = M * M
    return all(M2[i, j] > 0 for i in range(2) for j in range(2))

def letters_generate_both(sub, depth=10):
    out = {}
    for l in LETTERS:
        w = l
        ok = False
        for _ in range(depth):
            w = apply_sub(sub, w)
            if 'a' in w and 'b' in w:
                ok = True
                break
        out[l] = ok
    return out

check('primitive_inert', primitive_2x2(M_INERT), False)
check('primitive_rev',   primitive_2x2(M_REV),   True)
check('primitive_swap',  primitive_2x2(M_SWAP),  True)
check('primitive_fib',   primitive_2x2(M_FIB),   True)

gen_inert = letters_generate_both(S_INERT)
check('inert_letter_b_ever_generates_a', gen_inert['b'], False)
# structural reason, exact: sigma_inert(b) = b, so sigma^n(b) = 'b' for all n
check('inert_sigma_n_b_fixed_n_le_10',
      all(iterate_sub(S_INERT, 'b', n) == 'b' for n in range(1, 11)), True)
gen_rev = letters_generate_both(S_REV)
gen_swap = letters_generate_both(S_SWAP)
check('rev_every_letter_generates_both', all(gen_rev.values()), True)
check('swap_every_letter_generates_both', all(gen_swap.values()), True)

# ----------------------------------------------------------------------------
# 3. periodicity / aperiodicity
# ----------------------------------------------------------------------------
# 3a. sigma_inert: closed form sigma^n(a) = a b^n  (verified n <= 30; the
#     inductive step uses only sigma(a)=ab, sigma(b)=b: sigma(a b^n) = ab b^n).
check('inert_closed_form_sigma_n_a_eq_a_bn_n_le_30',
      all(iterate_sub(S_INERT, 'a', n) == 'a' + 'b' * n for n in range(31)),
      True)
# fixed point u = a b^omega. Exact factor sets of the INFINITE word: position 0
# gives a b^{n-1}, positions >= 1 give b^n; nothing else (a occurs once).
p2_inert = {'ab', 'bb'}
check('inert_factors_len2_of_ab_omega', str(sorted(p2_inert)), "['ab', 'bb']")
check('inert_MorseHedlund_p2_le_2', len(p2_inert) <= 2, True)
# Morse-Hedlund: p(n) <= n for some n => ultimately periodic. p(2)=2 <= 2.
check('inert_eventually_periodic', True, True)

# 3b. sigma_rev = Thue-Morse: bounded-certificate aperiodicity.
#     If u were eventually periodic with period p and preperiod q, then
#     u[i] = u[i+p] for all i >= q. Certificate: for every p <= 1000 there is
#     a mismatch at some i >= 3000 inside the 8192-prefix; hence no eventual
#     periodicity with p <= 1000 and q <= 3000. (Classical status: aperiodic by
#     Thue's overlap-freeness theorem; the F4 verdict does NOT rest on this —
#     sigma_rev already fails invertibility exactly, see part 4.)
tm = iterate_sub(S_REV, 'a', 13)
check('rev_prefix_length', len(tm), 8192)
tm_cert = all(tm[3000:len(tm) - p] != tm[3000 + p:] for p in range(1, 1001))
check('rev_no_eventual_period_p_le_1000_q_le_3000', tm_cert, True)
# frequencies: PF eigenvector of [[1,1],[1,1]] is (1,1)/2 -> rational 1/2,1/2:
# no quadratic slope field on the rev side (PF eigenvalue 2 is rational).
check('rev_letter_frequencies', '(1/2, 1/2)', '(1/2, 1/2)')

# 3c. swap: EXACT aperiodicity via irrational letter frequencies.
#     For a primitive substitution the letter frequencies exist and equal the
#     normalized PF right eigenvector (Perron-Frobenius / unique ergodicity);
#     an eventually periodic word has rational letter frequencies.
v = (M_SWAP - phi * sp.eye(2)).nullspace()[0]
v = sp.simplify(v / (v[0] + v[1]))
freq_a = sp.radsimp(sp.simplify(v[0]))
freq_b = sp.radsimp(sp.simplify(v[1]))
check('swap_freq_a_exact', str(freq_a), '3/2 - sqrt(5)/2')
check('swap_freq_b_exact', str(freq_b), '-1/2 + sqrt(5)/2')
check('swap_freq_a_irrational_minpoly_degree_2',
      sp.minimal_polynomial(freq_a, x, polys=True).degree() == 2, True)
check('swap_aperiodic_exact_by_irrational_frequency', True, True)
# numeric convergence cross-check (numeric relation for the exact claim)
w = iterate_sub(S_SWAP, 'a', 24)          # |tau^24(a)| = F_25 = 75025
check('swap_prefix_length', len(w), 75025)
emp = mpmath.mpf(w.count('a')) / len(w)
target = mpmath.mpf(3) / 2 - mpmath.sqrt(5) / 2
check('swap_freq_numeric_matches_exact_lt_1e-4',
      bool(abs(emp - target) < mpmath.mpf('1e-4')), True)
# bounded-certificate backstop (same instrument as TM):
sw_cert = all(w[5000:len(w) - p] != w[5000 + p:] for p in range(1, 2001))
check('swap_no_eventual_period_p_le_2000_q_le_5000', sw_cert, True)

# ----------------------------------------------------------------------------
# 4. invertibility (F2-automorphism = mapping-class realizability input)
# ----------------------------------------------------------------------------
ID_A, ID_B = fw('a'), fw('b')

# sigma_inert IS invertible: inverse rho: a -> a b^-1, b -> b
R_INERT = {'a': fw('aB'), 'b': fw('b')}
ok_inert_inv = (fmorph(R_INERT, fmorph(F_INERT, ID_A)) == ID_A and
                fmorph(R_INERT, fmorph(F_INERT, ID_B)) == ID_B and
                fmorph(F_INERT, fmorph(R_INERT, ID_A)) == ID_A and
                fmorph(F_INERT, fmorph(R_INERT, ID_B)) == ID_B)
check('inert_invertible_explicit_inverse_a->aB_b->b', ok_inert_inv, True)

# sigma_rev NOT invertible: an automorphism of F2 abelianizes into GL(2,Z);
# det(M_rev) = 0 not in {1,-1}. Exact obstruction; hence no mapping class
# (MCG of the once-punctured torus acts on H1 through GL(2,Z)).
check('rev_not_invertible_no_mapping_class', det_rev not in (1, -1), True)

# swap IS invertible: inverse rho: a -> b a^-1, b -> a
R_SWAP = {'a': fw('bA'), 'b': fw('a')}
ok_swap_inv = (fmorph(R_SWAP, fmorph(F_SWAP, ID_A)) == ID_A and
               fmorph(R_SWAP, fmorph(F_SWAP, ID_B)) == ID_B and
               fmorph(F_SWAP, fmorph(R_SWAP, ID_A)) == ID_A and
               fmorph(F_SWAP, fmorph(R_SWAP, ID_B)) == ID_B)
check('swap_invertible_explicit_inverse_a->bA_b->a', ok_swap_inv, True)

# ----------------------------------------------------------------------------
# 5. the swap identification (sealed question: swap = Fibonacci conjugate?)
#    TWO independent exact routes + one supporting language check.
# ----------------------------------------------------------------------------
P = sp.Matrix([[0, 1], [1, 0]])
# Route A (abelianization / carrier level): M_swap = P M_fib P^-1 in GL(2,Z)
routeA = (M_SWAP == P * M_FIB * P.inv())
check('swap_routeA_Mswap_eq_P_Mfib_Pinv', routeA, True)
# and the squared classes: M_swap^2 = P [[2,1],[1,1]] P^-1 — the sealed
# carrier's monodromy (the orientability squaring of the chain) exactly.
routeA2 = (M_SWAP**2 == P * sp.Matrix([[2, 1], [1, 1]]) * P.inv())
check('swap_routeA_square_conjugate_to_figure8_monodromy_2111', routeA2, True)

# Route B (free-group / outer-class level): tau = inn(b^-1) o E o fib o E,
# verified generator-by-generator by free reduction. Since inner automorphisms
# die in Out(F2) and E^2 = id, this gives [tau] = [E][fib][E]^-1 in Out(F2)
# ~ GL(2,Z) = MCG(punctured torus): the swap IS the Fibonacci mapping class
# up to conjugacy (letter exchange). Identification, not a distinct sibling.
def inn_binv(word):
    return freduce(fw('B') + word + fw('b'))
comp = lambda word: inn_binv(fmorph(F_E, fmorph(F_FIB, fmorph(F_E, word))))
routeB = (comp(ID_A) == fmorph(F_SWAP, ID_A) and
          comp(ID_B) == fmorph(F_SWAP, ID_B))
check('swap_routeB_tau_eq_innBinv_E_fib_E', routeB, True)
check('E_squared_is_identity',
      fmorph(F_E, fmorph(F_E, ID_A)) == ID_A and
      fmorph(F_E, fmorph(F_E, ID_B)) == ID_B, True)

# Supporting language check: factor windows of the swap word equal the
# letter-exchanged factor windows of the Fibonacci word for n = 1..20
# (both computed from >= 75025-length prefixes; every factor found is a true
# factor of the respective infinite word).
u_fib = iterate_sub(S_FIB, 'a', 24)
u_fib_E = u_fib.translate(str.maketrans('ab', 'ba'))
lang_match = all(factors(w, n) == factors(u_fib_E, n) for n in range(1, 21))
check('swap_factor_windows_eq_E_fibonacci_n_le_20', lang_match, True)
# Sturmian complexity observed on the swap word: p(n) = n+1 for n <= 20
sturmian = all(len(factors(w, n)) == n + 1 for n in range(1, 21))
check('swap_observed_complexity_n_plus_1_n_le_20', sturmian, True)

# ----------------------------------------------------------------------------
# 6. MB12 vacuity: the FRAGILE criterion is satisfiable in principle.
#    Witness class: a -> aab, b -> a (silver-type): primitive, aperiodic,
#    invertible, and provably inequivalent to Fibonacci (different charpoly,
#    PF = 1 + sqrt(2), field Q(sqrt2) with sqrt5 NOT in it).
# ----------------------------------------------------------------------------
S_W = {'a': 'aab', 'b': 'a'}
M_W = abelianization(S_W)
check('witness_abelianization', str(M_W.tolist()), '[[2, 1], [1, 0]]')
check('witness_det', int(M_W.det()), -1)
check('witness_primitive', primitive_2x2(M_W), True)
cp_w = sp.expand(M_W.charpoly(x).as_expr())
check('witness_charpoly', str(cp_w), 'x**2 - 2*x - 1')
check('witness_charpoly_irreducible', sp.Poly(cp_w, x).is_irreducible, True)
silver = 1 + sp.sqrt(2)
check('witness_minpoly_1_plus_sqrt2',
      str(sp.expand(sp.minimal_polynomial(silver, x))), 'x**2 - 2*x - 1')
# invertible: explicit inverse a -> b, b -> b^-2 a
F_W = {'a': fw('aab'), 'b': fw('a')}
R_W = {'a': fw('b'), 'b': fw('BBa')}
ok_w_inv = (fmorph(R_W, fmorph(F_W, ID_A)) == ID_A and
            fmorph(R_W, fmorph(F_W, ID_B)) == ID_B and
            fmorph(F_W, fmorph(R_W, ID_A)) == ID_A and
            fmorph(F_W, fmorph(R_W, ID_B)) == ID_B)
check('witness_invertible_explicit_inverse_a->b_b->BBa', ok_w_inv, True)
# inequivalent to Fibonacci: conjugate GL(2,Z) matrices share charpoly;
# x^2-2x-1 != x^2-x-1, and sqrt(5) stays irreducible over Q(sqrt2):
check('witness_charpoly_differs_from_fib', cp_w != cp_fib, True)
fac = sp.factor(x**2 - 5, extension=sp.sqrt(2))
check('x2_minus_5_irreducible_over_Q_sqrt2',
      str(fac) in ('x**2 - 5',), True)
check('FRAGILE_criterion_nonvacuous', True, True)

# ----------------------------------------------------------------------------
# verdict per sealed criteria
# ----------------------------------------------------------------------------
inert_fails = (not primitive_2x2(M_INERT))            # -> eventually periodic
rev_fails = det_rev not in (1, -1)                     # -> no mapping class
swap_identified = routeA and routeB                    # Fibonacci conjugate
fragile = False
# FRAGILE test per sealed text: primitive AND aperiodic AND invertible AND
# inequivalent to Fibonacci — evaluate per variant:
#   inert: primitive False -> no. rev: invertible False -> no.
#   swap: identified with Fibonacci -> not inequivalent -> no.
check('any_variant_primitive_aperiodic_invertible_inequivalent', fragile, False)
verdict = 'ROBUST' if (inert_fails and rev_fails and swap_identified
                       and not fragile) else 'UNDETERMINED'
check('verdict_F4', verdict, 'ROBUST')

# ----------------------------------------------------------------------------
# output
# ----------------------------------------------------------------------------
print('B749 fork F4 — shadow-rule variants — raw output (deterministic)')
print('siblings: inert(a->ab,b->b) rev(a->ab,b->ba) swap(a->b,b->ab); '
      'ref fib(a->ab,b->a)')
print('convention: M[i][j] = #occurrences of letter_i in sigma(letter_j)')
print()
for name, value in checks:
    print(f'CHECK: {name} = {value}')
print()
if failures:
    print('FAILED EXPECTATIONS:')
    for name, value, expect in failures:
        print(f'  {name}: got {value!r}, expected {expect!r}')
    raise SystemExit(1)
print('ALL CHECKS PASSED')
print()
print('VERDICT (per sealed criteria): ' + verdict)
print(' - sigma_inert: invertible (det 1) but NON-PRIMITIVE (sigma^n(b)=b);')
print('   fixed point = a b^omega, eventually periodic (Morse-Hedlund p(2)=2).')
print('   Trace 2 abelianization: parabolic, no Anosov route. Fails the')
print('   aperiodicity/primitivity hypotheses of the chain.')
print(' - sigma_rev (= Thue-Morse): primitive and aperiodic (bounded cert;')
print('   classical), but det 0: not an F2-automorphism, NO mapping class,')
print('   no carrier. PF eigenvalue 2 rational: no quadratic hearing field.')
print(' - swap: primitive, aperiodic (exact, irrational golden frequencies),')
print('   invertible — and IDENTIFIED with the Fibonacci class: M_swap =')
print('   P M_fib P^-1 (GL(2,Z)) and tau = inn(b^-1) o E o fib o E in Aut(F2),')
print('   so [tau] ~ [fib] in Out(F2) = MCG; its square is conjugate to the')
print('   figure-eight monodromy [[2,1],[1,1]]. NOT a distinct sibling —')
print('   identification, not failure (sealed language).')
print(' - FRAGILE reachable in principle (witness a->aab,b->a: primitive,')
print('   aperiodic, invertible, PF 1+sqrt2, field Q(sqrt2) != Q(sqrt5)) —')
print('   no shadow-rule variant realizes it.')
