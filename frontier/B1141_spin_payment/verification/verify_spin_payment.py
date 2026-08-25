"""
HOSTILE, independent (compute-not-cite) verification of:
  - THE BEAT (cloud memos 16/17/18): an antiholomorphic intertwiner W
    implementing "Galois conjugation (.) Fibonacci step" on the figure-eight
    knot complement m004's discrete faithful holonomy.
  - THE SPIN PAYMENT (cloud memo 28): the Gieseking extension exists over
    EXACTLY ONE of the two SL(2,C) lifts (spin structures) of m004 -- the
    object's own Z/2 beat SELECTS the lift.

Everything below is derived from scratch in-sandbox: no cloud-memo numbers
are assumed, only the CONSTRUCTION (generators, target beat-words, the four
intertwining equations) as specified in the verification brief. SnapPy is
used only as an INDEPENDENT cross-check of the geometric input (that m004
really is the figure-eight, with the expected volume/homology/trace field),
never as a source of the algebra itself.

Pure topology/algebra. No SM value enters anywhere (Gate 5 n/a).

Run: python3 verify_spin_payment.py
Requires: sympy, mpmath, snappy  (all confirmed present in the environment)
"""
import itertools
import json

import sympy as sp

RESULTS = {}

# =====================================================================
# PART 0 -- SnapPy ground truth: confirm m004 is really the figure-eight
# =====================================================================
print("="*78)
print("PART 0 -- independent geometric ground truth (SnapPy)")
print("="*78)
import snappy
M = snappy.Manifold('m004')
ids = [str(x) for x in M.identify()]
vol = float(M.volume())
homology = str(M.homology())
print("SnapPy identify(m004):", ids)
print("SnapPy volume:", vol, " (known figure-8 volume = 2.029883212819...)")
print("SnapPy H_1:", homology)
assert '4_1(0,0)' in ids
assert abs(vol - 2.0298832128193) < 1e-9
assert homology == 'Z'
RESULTS['snappy_identify'] = ids
RESULTS['snappy_volume'] = vol
RESULTS['snappy_H1'] = homology
RESULTS['n_spin_structures'] = 2   # H^1(M;Z/2) = Z/2, forced by H_1=Z

# =====================================================================
# PART 1 -- build the Riley parabolic holonomy EXACTLY, find + verify the
# relator by independent brute-force search (not citing any prior arc)
# =====================================================================
print("\n" + "="*78)
print("PART 1 -- the holonomy representation and its relator (exact)")
print("="*78)

u = sp.symbols('u')
Asym = sp.Matrix([[1, 1], [0, 1]])
Bsym = sp.Matrix([[1, 0], [-u, 1]])
Ainv_s, Binv_s = Asym.inv(), Bsym.inv()
gens_s = {'a': Asym, 'b': Bsym, 'A': Ainv_s, 'B': Binv_s}


def word_matrix_sym(word):
    Mm = sp.eye(2)
    for ch in word:
        Mm = Mm * gens_s[ch]
    return Mm


def reduced(word):
    pairs = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    return all(word[i + 1] != pairs[word[i]] for i in range(len(word) - 1))


print("brute-force search over words w (length 1..6), classical 2-bridge ansatz a*w = w*b:")
found_u2u1 = []
for length in range(1, 7):
    for tup in itertools.product('abAB', repeat=length):
        w = ''.join(tup)
        if not reduced(w):
            continue
        W = word_matrix_sym(w)
        D = Asym * W - W * Bsym
        entries = [sp.expand(sp.fraction(sp.together(D[i, j]))[0]) for i in range(2) for j in range(2)]
        entries = [e for e in entries if e != 0]
        if not entries:
            continue
        g = sp.Poly(entries[0], u)
        for e in entries[1:]:
            g = g.gcd(sp.Poly(e, u))
        if g.degree() >= 1 and sp.expand(g.monic().as_expr() - (u**2 + u + 1)) == 0:
            found_u2u1.append(w)
print(f"  {len(found_u2u1)} words of length<=6 independently reproduce u^2+u+1=0; shortest: "
      f"{sorted(found_u2u1, key=len)[:4]}")
assert len(found_u2u1) > 0

omega = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2   # e^{2 pi i /3}
print("\nomega := e^(2 pi i/3). Minimal polynomial check:")
print("  omega^2 + omega + 1 =", sp.simplify(omega**2 + omega + 1), " <- holds (0)")
print("  omega^2 - omega + 1 =", sp.simplify(omega**2 - omega + 1),
      " <- does NOT hold (this is the polynomial for e^(i pi/3) instead, a different")
print("     though related generator of the same field Q(sqrt(-3)) -- the task brief's stated")
print("     defining polynomial 'omega^2-omega+1=0' for omega=e^(2pi i/3) is WRONG; the VALUE")
print("     e^(2pi i/3) is right, confirmed independently by the search above.")
RESULTS['omega_minpoly_x2+x+1_holds'] = True
RESULTS['omega_minpoly_x2-x+1_holds'] = False
RESULTS['erratum_1'] = ("task brief states omega=e^{2pi i/3} is 'a root of omega^2-omega+1=0'; "
                         "independently confirmed FALSE. omega^2+omega+1=0 is the correct minimal "
                         "polynomial for e^{2pi i/3}; x^2-x+1=0 is instead satisfied by e^{i pi/3} "
                         "(the figure-eight's ideal-tetrahedron shape parameter, a related but "
                         "distinct generator of the same field Q(sqrt(-3))). Non-load-bearing.")

A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-omega, 1]])
w0 = 'bABa'
W0word = word_matrix_sym(w0).subs(u, omega)
relator_word = 'a' + w0 + 'B' + ''.join({'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}[c] for c in reversed(w0))
print(f"\nfull relator word (from w='{w0}'): R = {relator_word!r}")

gens = {'a': A, 'b': B, 'A': A.inv(), 'B': B.inv()}


def word_matrix(word, g=gens):
    Mm = sp.eye(2)
    for ch in word:
        Mm = Mm * g[ch]
    return sp.simplify(Mm)


Rmat = word_matrix(relator_word)
print("R(A,B) exactly =", Rmat.tolist(), " == I:", Rmat == sp.eye(2))
assert Rmat == sp.eye(2)
print("det A =", A.det(), " det B =", sp.simplify(B.det()), " trace A =", A.trace(),
      " trace B =", sp.simplify(B.trace()), " trace AB =", sp.simplify((A * B).trace()))
RESULTS['relator_word'] = relator_word
RESULTS['relator_holds_exactly'] = True

# cross-check trace field against SnapPy's own (independently-computed) holonomy
import numpy as np
G = M.fundamental_group()


def to_np(m):
    return np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])


Asn, Bsn = to_np(G.SL2C('a')), to_np(G.SL2C('b'))
tf_check = [2 * np.trace(Asn @ Bsn).imag / np.sqrt(3)]
print("SnapPy holonomy trace(AB): 2*Im/sqrt(3) =", tf_check[0], "(near-integer confirms trace field Q(sqrt(-3)) independently)")
RESULTS['snappy_trace_field_crosscheck_near_integer'] = abs(tf_check[0] - round(tf_check[0])) < 1e-6

# =====================================================================
# PART 2 -- THE RELATOR CENSUS (the two SL(2,C) lifts / two spin structures)
# =====================================================================
print("\n" + "="*78)
print("PART 2 -- the relator census (two spin structures)")
print("="*78)
census = {}
for sA, sB, label in [(1, 1, "R(A,B)"), (-1, -1, "R(-A,-B)"), (-1, 1, "R(-A,B)"), (1, -1, "R(A,-B)")]:
    Rm = word_matrix(relator_word, {'a': sA * A, 'b': sB * B, 'A': (sA * A).inv(), 'B': (sB * B).inv()})
    verdict = "+I" if Rm == sp.eye(2) else ("-I" if Rm == -sp.eye(2) else "NEITHER")
    census[label] = verdict
    print(f"  {label:12s} = {verdict}")
assert census == {"R(A,B)": "+I", "R(-A,-B)": "+I", "R(-A,B)": "-I", "R(A,-B)": "-I"}
RESULTS['relator_census'] = census

na = sum(1 for c in relator_word if c in 'aA')
nb = sum(1 for c in relator_word if c in 'bB')
print(f"(mechanism: relator has {na} a-letters (odd={na % 2 == 1}), {nb} b-letters (odd={nb % 2 == 1}) "
      f"=> flipping one generator's sign flips the relator's sign, flipping both restores it)")

# =====================================================================
# PART 3 -- the beat map and its compatibility with the presentation
# =====================================================================
print("\n" + "="*78)
print("PART 3 -- the beat map: rho(beat(a))=A, rho(beat(b))=B^-1 A B A^-1 B")
print("="*78)
Ab = A
Bb = B.inv() * A * B * A.inv() * B
print("det(rho(beat(b))) =", sp.simplify(Bb.det()), " trace =", sp.simplify(Bb.trace()))
Rbeat = word_matrix(relator_word, {'a': Ab, 'b': Bb, 'A': Ab.inv(), 'B': Bb.inv()})
print("R(rho(beat(a)), rho(beat(b))) =", Rbeat.tolist(), " == I:", Rbeat == sp.eye(2))
assert Rbeat == sp.eye(2)
print(" => beat DOES respect the presentation: rho o beat is a genuine representation of pi_1(m004).")
RESULTS['beat_respects_relator'] = True

beat_b_word = 'BabAb'  # = b^-1 a b a^-1 b, translating B^-1 A B A^-1 B into group-word letters
print(f"beat(a) word length = 1 (odd);  beat(b) word = {beat_b_word!r}, length = {len(beat_b_word)} (odd)")
assert len(beat_b_word) == 5
RESULTS['beat_word_lengths'] = {'beat_a': 1, 'beat_b': len(beat_b_word)}

ea = sum(1 if c == 'a' else (-1 if c == 'A' else 0) for c in relator_word)
eb = sum(1 if c == 'b' else (-1 if c == 'B' else 0) for c in relator_word)
print(f"H_1 check: relator abelianizes to ({ea})[a] + ({eb})[b] = 0  =>  [a]=[b] in H_1(M;Z)=Z")
print("  => chi(a) = chi(b) = -1 is FORCED for the nontrivial character (both are meridians).")
assert (ea, eb) == (1, -1)
RESULTS['H1_abelianized_relator'] = {'e_a': ea, 'e_b': eb}


def chi(word):
    return (-1) ** len(word)


def beat_word_map(word):
    beat_a, beat_A, beat_b = 'a', 'A', beat_b_word
    beat_B = ''.join({'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}[c] for c in reversed(beat_b))
    m = {'a': beat_a, 'A': beat_A, 'b': beat_b, 'B': beat_B}
    return ''.join(m[c] for c in word)


print("General proof: len(beat(w)) = na(w)*1 + nb(w)*5 == na(w)+nb(w) (mod 2) == len(w) (mod 2)")
print("  => chi(beat(w)) = chi(w) for EVERY w in pi_1(M), not just the two generators.")
import random
random.seed(2028)
mismatches = 0
for _ in range(20):
    n = random.randint(2, 10)
    w, last = '', ''
    inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    while len(w) < n:
        c = random.choice('abAB')
        if last and c == inv[last]:
            continue
        w += c
        last = c
    if chi(w) != chi(beat_word_map(w)):
        mismatches += 1
print(f"  spot-checked on 20 random words: {20-mismatches}/20 match chi(beat(w))=chi(w)")
assert mismatches == 0
RESULTS['chi_beat_invariance_spotcheck'] = f"{20-mismatches}/20"

# =====================================================================
# PART 4 -- THE CRUX: the full linear intertwining system, exact rank
# =====================================================================
print("\n" + "="*78)
print("PART 4 -- CLAIM 1: intertwiner space dimension (full linear system)")
print("="*78)
omega_bar = sp.conjugate(omega)
conjA = A.conjugate()          # A real => conj(A) = A
conjB = sp.Matrix([[1, 0], [-omega_bar, 1]])

p, q, r, s = sp.symbols('p q r s')
W = sp.Matrix([[p, q], [r, s]])
Eq_a = W * conjA - Ab * W
Eq_b = W * conjB - Bb * W
scalar_eqs = list(Eq_a) + list(Eq_b)
unknowns = [p, q, r, s]
Mcoeff = sp.simplify(sp.Matrix([[sp.expand(e).coeff(v) for v in unknowns] for e in scalar_eqs]))
rank = Mcoeff.rank()
ns = Mcoeff.nullspace()
print(f"8 scalar equations (W*conj(a)=rho(beat(a))*W ; W*conj(b)=rho(beat(b))*W) in 4 unknowns (p,q,r,s).")
print(f"EXACT rank (sympy, algebraic-number entries) = {rank}  =>  solution-space dimension = {4-rank}")
print("nullspace basis:", [sp.simplify(v).T.tolist() for v in ns])
assert rank == 3 and len(ns) == 1
RESULTS['intertwiner_system_rank'] = rank
RESULTS['intertwiner_space_dimension'] = 4 - rank

W0 = sp.simplify(ns[0].reshape(2, 2))
print("base solution W0 =", W0.tolist())

# independent numeric cross-check via complex SVD (mpmath, 50 digits) -- see stage8 script for the
# full standalone version (incl. a deliberately-kept record of a first-attempt methodology bug).
import mpmath as mp
mp.mp.dps = 50
omega_mp = mp.e**(2j * mp.pi / 3)


def mat(a, b, c, d):
    return mp.matrix([[a, b], [c, d]])


def conjM(Mm):
    return mat(*[mp.conj(x) for x in Mm])


A_mp, B_mp = mat(1, 1, 0, 1), mat(1, 0, -omega_mp, 1)
Ab_mp = A_mp
Bb_mp = B_mp**-1 * A_mp * B_mp * A_mp**-1 * B_mp
conjA_mp, conjB_mp = conjM(A_mp), conjM(B_mp)


def eqs_from_W(pqrs):
    pp, qq, rr, ss = pqrs
    Wm = mat(pp, qq, rr, ss)
    E1 = Wm * conjA_mp - Ab_mp * Wm
    E2 = Wm * conjB_mp - Bb_mp * Wm
    return [E1[0, 0], E1[0, 1], E1[1, 0], E1[1, 1], E2[0, 0], E2[0, 1], E2[1, 0], E2[1, 1]]


basis = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
Mcplx = mp.matrix(8, 4)
for j, b_ in enumerate(basis):
    for i, val in enumerate(eqs_from_W(b_)):
        Mcplx[i, j] = val
_, Sc, _ = mp.svd_c(Mcplx)
numeric_rank = sum(1 for sv in Sc if sv > mp.mpf('1e-30'))
print(f"independent numeric cross-check (mpmath, 50-digit complex SVD): rank = {numeric_rank}, "
      f"4th singular value = {mp.nstr(Sc[3], 6)} (~0) => nullspace dim = {4-numeric_rank}")
assert numeric_rank == 3
RESULTS['intertwiner_rank_numeric_crosscheck'] = numeric_rank

# =====================================================================
# PART 5 -- CLAIM 2: eqs (i)-(iv) hold for W0; N(lambda) positivity
# =====================================================================
print("\n" + "="*78)
print("PART 5 -- CLAIM 2: eqs (i)-(iv) for W0, and the norm-positivity argument")
print("="*78)
eqs_ok = {
    'W0 conj(A) W0^-1 == +A': sp.simplify(W0 * conjA * W0.inv() - A) == sp.zeros(2, 2),
    'W0 conj(B) W0^-1 == +rho(beat(b))': sp.simplify(W0 * conjB * W0.inv() - Bb) == sp.zeros(2, 2),
    'W0 conj(W0) == +A': sp.simplify(W0 * W0.conjugate() - A) == sp.zeros(2, 2),
    'det(W0) == 1': sp.simplify(W0.det() - 1) == 0,
}
for k, v in eqs_ok.items():
    print(f"  {k}: {v}")
assert all(eqs_ok.values())
RESULTS['beat_closure_equations'] = eqs_ok

x, y = sp.symbols('x y', real=True)
lam_C = x + sp.I * y
sqC = sp.expand(sp.simplify((lam_C * W0 * (lam_C * W0).conjugate())[0, 0]))
print(f"\nfor GENERAL lambda=x+iy in C (the full 1-dim solution space): "
      f"(lambda W0)(conj(lambda W0)) = {sqC} * A")
assert sp.simplify(sqC - (x**2 + y**2)) == 0
print("  = |lambda|^2 * A, literally x^2+y^2 -- nonnegative for EVERY complex lambda, =0 only at lambda=0.")
print("  => N(lambda) = -1 is impossible for ANY lambda in C (a stronger, fully general statement).")

X, Y = sp.symbols('X Y', real=True)
lam_arith = X + Y * omega
sqA_ = sp.expand(sp.simplify((lam_arith * W0 * (lam_arith * W0).conjugate())[0, 0]))
print(f"\non the arithmetic lattice lambda=X+Y*omega (X,Y in Q): N(X,Y) = {sqA_}")
print("  task brief's claimed closed form was X^2+XY+Y^2; ACTUAL closed form is X^2-XY+Y^2")
print("  (the standard Eisenstein-integer norm) -- differs by the cross-term sign, same erratum")
print("  family as the omega-polynomial mislabel in Part 1. Still positive definite either way:")
disc = sp.expand((-1)**2 - 4 * 1 * 1)
print(f"  discriminant of X^2-XY+Y^2 = (-1)^2-4(1)(1) = {disc} < 0, leading coeff 1>0 => positive definite.")
assert sp.simplify(sqA_ - (X**2 - X * Y + Y**2)) == 0
RESULTS['N_lambda_general'] = "x^2+y^2 (|lambda|^2), lambda in C -- exact"
RESULTS['N_XY_arithmetic_lattice'] = "X^2-XY+Y^2 (NOT X^2+XY+Y^2 as stated in brief -- erratum, non-load-bearing)"
RESULTS['N_positive_definite'] = True
RESULTS['erratum_2'] = ("task brief claims N(lambda)=X^2+XY+Y^2 for lambda=X+Y*omega; independently "
                         "computed exact value is X^2-XY+Y^2 (the standard Eisenstein norm for "
                         "omega=e^{2pi i/3}). Same sign-convention family as erratum_1. Both forms "
                         "are positive definite (disc=-3); does not affect the conclusion.")

# =====================================================================
# PART 6 -- the MECHANISM: why the twisted lift fails self-consistency
# =====================================================================
print("\n" + "="*78)
print("PART 6 -- the mechanism: twisted lift shares eqs (i,ii) but fails (iii)")
print("="*78)
lhs_i = sp.simplify(W0 * (-conjA) * W0.inv())
lhs_ii = sp.simplify(W0 * (-conjB) * W0.inv())
twisted_shares_eqs = (sp.simplify(lhs_i - (-A)) == sp.zeros(2, 2) and
                       sp.simplify(lhs_ii - (-Bb)) == sp.zeros(2, 2))
print("Because chi(beat(g))=chi(g) for g=a,b, the SAME W0 intertwines the twisted lift's (i,ii) too:")
print(f"  W0 conj(-A) W0^-1 == -A: {sp.simplify(lhs_i-(-A))==sp.zeros(2,2)}   "
      f"W0 conj(-B) W0^-1 == -rho(beat(b)): {sp.simplify(lhs_ii-(-Bb))==sp.zeros(2,2)}")
print("  => (i,ii) alone cannot distinguish the lifts, exactly as chi-invariance predicts.")
print("The obstruction lives ONLY in the self-consistent square: twisted lift needs W*conj(W)=-A,")
print("but every W in the (exactly 1-dim) solution space gives W*conj(W)=(x^2+y^2)*A >= 0. No solution:")
sol = sp.solve(sp.Eq(x**2 + y**2, -1), (x, y))
print("  solve(x^2+y^2=-1) over R:", sol, " (empty, confirmed)")
assert twisted_shares_eqs and sol == []
RESULTS['twisted_lift_shares_i_ii'] = twisted_shares_eqs
RESULTS['twisted_lift_square_unsatisfiable'] = True

# =====================================================================
# FINAL SUMMARY
# =====================================================================
print("\n" + "="*78)
print("SUMMARY")
print("="*78)
RESULTS['verdict'] = "CONFIRMED: the spin payment holds. Two non-load-bearing documentation errata found."
# (side-effect-free: the full RESULTS dict is emitted on stdout below; no file written,
#  so the in-lock reproduction never clobbers a tracked file — the pinned copy is b1141_results.json)
print(json.dumps(RESULTS, indent=2, default=str))
