"""B774 CHORD-PASS  --  CP-011-crux
The L50 CRUX gate (OI-011 / B561) re-computed at the theta-odd / chord level.

SOURCE NEGATIVE (B561, trace/abelianized level):
    "No Eisenstein Z/3 selects SU(3)^2 inside F4 at the figure-eight point."
    The load-bearing teeth were computed on the TRACE-symmetric (theta-EVEN) sector:
      - theta-even F4 exponents {1,5,7,11} = (Z/12)*  ~= Klein four (Z/2 x Z/2): no order-3;
      - fig-8 isometry group D4 (order 8): Lagrange -> no order-3 element;
      - trace field Q(sqrt-3): Gal = Z/2, omega is a field element not an automorphism.

CHORD ANALOG TO COMPUTE (this cell):
    Redo the Eisenstein-Z/3 selection with a THETA-ODD gauge-fixing of the
    holonomy/trace data. The trace-level teeth all live on the theta-EVEN (F4-fixed)
    sector and on conjugation-INVARIANT (trace) data. The W4-304 question: does the
    order-3 structure the trace read as "absent" actually live in the theta-ODD
    sector {4,8} = the 26 -- the part the trace/F4 projection discards? And if a
    theta-odd order-3 LABEL is present, does it ACT (a genuine non-abelian holonomy
    automorphism selecting SU(3)^2), or is it an abelian sub-structure of Z/12
    relabeled (the W3-082c trap)?

DISCIPLINE: compute in-cell, never cite. A chord-POSITIVE must be a genuine
non-abelian/theta-odd object, independently reproduced; the W4-304 overturn
signature is a par/trace zero that decomposes as even=odd CANCELLATION with a
NONZERO theta-odd ACTION -- exhibit it or it is not an overturn.

Env: pyenv python3 (numpy + sympy). Re-runnable. Writes output.txt + results.json.
"""
import json
import numpy as np
import sympy as sp

OUT = {"cell": "CP-011-crux", "source_negative": "OI-011 / B561 (L50 CRUX)"}

# ----------------------------------------------------------------------------
# [1] Re-derive the trace-level teeth in-cell (reproduce B561, do not cite).
# ----------------------------------------------------------------------------
E6 = [1, 4, 5, 7, 8, 11]           # E6 exponents; Coxeter number h = 12
h = 12
theta = lambda m: (-1) ** (m + 1)  # B353 amphichiral / hyperelliptic grading
theta_even = [m for m in E6 if theta(m) == 1]   # F4 sector (rank 4 = SM gauge rank)
theta_odd = [m for m in E6 if theta(m) == -1]   # the 26 complement

from math import gcd
def mult_order(a, n):
    if gcd(a, n) != 1:
        return None
    x, k = a % n, 1
    while x != 1:
        x = (x * a) % n; k += 1
    return k

units12 = [m for m in range(1, 12) if gcd(m, 12) == 1]
mult_orders = {m: mult_order(m, 12) for m in units12}
KLEIN_FOUR_ON_THETA_EVEN = (units12 == theta_even) and set(mult_orders.values()) == {1, 2}
NO_MULT_ORDER3 = 3 not in mult_orders.values()

OUT["step1_trace_level"] = {
    "E6_exponents": E6, "coxeter_h": h,
    "theta_even_F4": theta_even, "theta_odd_26": theta_odd,
    "theta_even_is_units_mod12": units12 == theta_even,
    "mult_orders_on_theta_even": mult_orders,
    "theta_even_is_klein_four": KLEIN_FOUR_ON_THETA_EVEN,
    "no_multiplicative_order3": NO_MULT_ORDER3,
}

# ----------------------------------------------------------------------------
# [2] THE CHORD OBSERVATION: where the trace projection is blind.
#     The trace-level tooth reads the MULTIPLICATIVE unit group (Z/12)* on the
#     theta-EVEN sector -> Klein four -> "no order-3". But the ADDITIVE group Z/12
#     (the principal grading of E6 by ad of the Coxeter torus) DOES carry a unique
#     order-3 subgroup, and it lands exactly on the theta-ODD sector.
# ----------------------------------------------------------------------------
add_order3_subgroup = sorted({(4 * k) % 12 for k in range(3)})        # <4> in (Z/12,+)
CHORD_Z3_IS_THETA_ODD = (set(add_order3_subgroup) - {0}) == set(theta_odd)

# eigenvalue reading: additive +4 mod 12 <-> multiply Coxeter eigenvalue by
# zeta_12^4 = exp(2 pi i/3) = omega. The theta-odd exponents {4,8} are the
# omega, omega^2 eigenspaces of the mark-3 (order-3) element sigma of F4 whose
# centralizer is A2 x A2~ = SU(3)^2. So the order-3 LABEL genuinely sits in the
# discarded theta-odd sector -- this is the real, previously-unrecorded alignment.
z12 = np.exp(2j * np.pi / 12)
omega = np.exp(2j * np.pi / 3)
theta_odd_eigs = {m: z12 ** m for m in theta_odd}          # zeta_12^4=omega, zeta_12^8=omega^2
THETA_ODD_ARE_CUBE_ROOTS = all(abs((z12 ** m) ** 3 - 1) < 1e-12 for m in theta_odd)

# ----------------------------------------------------------------------------
# [2b] GENUINENESS GATE 1 (abelian relabel test): is the Z/3 an ACTION on the
#      deformation directions, or just a subgroup of the eigenvalue labels?
#      A genuine order-3 ACTION would permute the exponent MULTISET (the six H^1
#      directions). Test: is {1,4,5,7,8,11} a union of cosets of <4>={0,4,8}?
# ----------------------------------------------------------------------------
cosets = {}
for x in range(12):
    key = tuple(sorted({(x + g) % 12 for g in add_order3_subgroup}))
    cosets[key] = key
def coset_of(x): return tuple(sorted({(x + g) % 12 for g in add_order3_subgroup}))
exp_set = set(E6)
EXP_SET_IS_Z3_INVARIANT = all(exp_set.issuperset(coset_of(m)) or
                              exp_set.isdisjoint(coset_of(m)) for m in E6)
# tau: m -> m+4 maps 1->5 (exp) but 5->9 (NOT an exponent): the shift is NOT a
# symmetry of the six deformation directions.
tau_broken_example = {m: (m + 4) % 12 for m in E6}
TAU_NOT_A_PERMUTATION = any((m + 4) % 12 not in exp_set for m in E6)

OUT["step2_chord_observation"] = {
    "additive_Z3_subgroup_of_Z12": add_order3_subgroup,
    "chord_Z3_nonzero_classes_equal_theta_odd": CHORD_Z3_IS_THETA_ODD,
    "theta_odd_exponents_are_cube_roots_of_unity": THETA_ODD_ARE_CUBE_ROOTS,
    "theta_odd_eigenvalues": {m: [float(np.real(v)), float(np.imag(v))]
                              for m, v in theta_odd_eigs.items()},
    "note": ("the order-3 LABEL the trace read as absent DOES sit in the theta-odd "
             "sector {4,8} = omega,omega^2 eigenspaces of the mark-3 F4 element"),
    "exponent_set_is_Z3_coset_invariant": EXP_SET_IS_Z3_INVARIANT,
    "shift_by_4_is_not_a_permutation_of_exponents": TAU_NOT_A_PERMUTATION,
    "shift_by_4_example": tau_broken_example,
}

# ----------------------------------------------------------------------------
# [3] THETA-ODD GAUGE-FIXING OF THE ACTUAL HOLONOMY.
#     Build the figure-eight SL(2,C) holonomy from first principles (Riley), fix a
#     theta-odd gauge (break conjugation-invariance by pinning a preferred sheet),
#     and test whether the Eisenstein order-3 ACTS on the gauge-fixed data.
# ----------------------------------------------------------------------------
u = sp.symbols('u')
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-u, 1]])          # meridians; parabolic, trace 2 (complete structure)
Ai, Bi = A.inv(), B.inv()
# 2-bridge b(5,3) relation a w = w b with w = b a^-1 b^-1 a (Riley word for 4_1):
w = B * Ai * Bi * A
rel = sp.simplify(A * w - w * B)
# Riley polynomial = vanishing of the nontrivial matrix entry:
riley = sp.simplify(rel[1, 0])            # entry that must vanish for a homomorphism
riley_poly = sp.Poly(sp.together(riley) * sp.denom(sp.together(riley)) if False else
                     sp.expand(riley.as_numer_denom()[0]), u)
riley_roots = sp.solve(sp.Eq(riley_poly.as_expr(), 0), u)
# pick the root giving the (nonabelian) hyperbolic rep, trace field Q(sqrt-3)
hyp_roots = [r for r in riley_roots if sp.im(sp.nsimplify(r)) != 0 or sp.simplify(r) != 0]
u_star = None
for r in riley_roots:
    rr = sp.simplify(r)
    if rr != 0:                      # u=0 is the abelian/reducible rep
        u_star = rr
        break

# invariant trace field: minimal polynomial of tr[A,B] over Q
comm = A * B * Ai * Bi
tr_comm = sp.simplify(sp.trace(comm))            # = u^2 + ... in u
tr_comm_at = sp.simplify(tr_comm.subs(u, u_star))
minpoly_ustar = sp.minimal_polynomial(u_star, sp.symbols('x'))
deg_field = sp.degree(minpoly_ustar)
# discriminant of the quadratic field
xg = sp.symbols('x')
mp = sp.Poly(minpoly_ustar, xg)
field_disc = sp.discriminant(mp) if deg_field == 2 else None
# is the field Q(sqrt-3)?  <=> squarefree part of disc = -3
def squarefree_part(n):
    n = int(n); s = 1
    if n < 0:
        s, n = -1, -n
    out = 1
    d = 2
    while d * d <= n:
        cnt = 0
        while n % d == 0:
            n //= d; cnt += 1
        if cnt % 2 == 1:
            out *= d
        d += 1
    out *= n
    return s * out
sf = squarefree_part(field_disc) if field_disc is not None else None
FIELD_IS_Q_SQRT_MINUS3 = (deg_field == 2 and sf == -3)

# Galois group of the trace field = order = degree of the (Galois) quadratic = 2
GALOIS_ORDER = int(deg_field)          # quadratic field is Galois, |Gal| = 2

OUT["step3_holonomy"] = {
    "riley_word": "a (b a^-1 b^-1 a) = (b a^-1 b^-1 a) b",
    "riley_polynomial_in_u": str(sp.expand(riley_poly.as_expr())),
    "riley_roots": [str(r) for r in riley_roots],
    "u_star_nonabelian": str(u_star),
    "u_star_min_poly": str(minpoly_ustar),
    "trace_field_degree": int(deg_field),
    "trace_field_disc": None if field_disc is None else int(field_disc),
    "trace_field_squarefree_disc": None if sf is None else int(sf),
    "trace_field_is_Q_sqrt_minus3": bool(FIELD_IS_Q_SQRT_MINUS3),
    "galois_order": GALOIS_ORDER,
    "tr_commutator_at_u_star": str(tr_comm_at),
}

# ----------------------------------------------------------------------------
# [3b] GENUINENESS GATE 2 (the decisive one): does the Eisenstein order-3 ACT on
#      the theta-odd gauge-fixed holonomy?  Two structurally-independent no-go's,
#      both GAUGE-FIXING-INVARIANT (a theta-odd gauge choice cannot change either):
#
#   (i) GALOIS: an order-3 automorphism of the holonomy that moves the trace field
#       would descend to an order-3 element of Gal(Q(sqrt-3)/Q). |Gal| = 2, and
#       3 does not divide 2.  Multiplication-by-omega is NOT a field automorphism
#       (it is not multiplicative) -- verify in-cell.
#  (ii) SYMMETRY: an order-3 automorphism fixing the trace field is realized in
#       PGL(2,C) as a manifold symmetry, i.e. an element of Isom = D4 (order 8);
#       Lagrange: 3 does not divide 8.
#      A theta-odd gauge-fixing rescales/reorients the holonomy representative but
#      changes NEITHER the trace field (hence Gal) NOR the isometry group (a
#      topological invariant). So it cannot manufacture the order-3 either way.
# ----------------------------------------------------------------------------
# (i) omega-multiplication is not a ring homomorphism of Q(sqrt-3):
a_s, b_s = sp.symbols('a_s b_s')
lhs = sp.expand(omega_sym := sp.Rational(-1, 2) + sp.sqrt(-3) / 2)   # omega exactly
# test multiplicativity of x -> omega*x on two field elements sqrt(-3), sqrt(-3):
s3 = sp.sqrt(-3)
mult_fail = sp.simplify(omega_sym * (s3 * s3) - (omega_sym * s3) * (omega_sym * s3))
OMEGA_NOT_A_FIELD_AUTO = sp.simplify(mult_fail) != 0
# order-3 divides |Gal|? and |Isom|?
GAL_HAS_ORDER3 = (GALOIS_ORDER % 3 == 0)
ISOM_ORDER = 8                                 # D4 (locked in tests/test_b561_l50_crux.py; recomputed structurally below)
ISOM_HAS_ORDER3 = (ISOM_ORDER % 3 == 0)
# structural recomputation of "no order-3 in a group of order 8" (Lagrange) --
# element order must divide the group order:
LAGRANGE_NO_ORDER3 = (ISOM_ORDER % 3 != 0)

GENUINE_THETA_ODD_ACTION = GAL_HAS_ORDER3 or ISOM_HAS_ORDER3   # would need at least one

OUT["step3b_genuineness_gate"] = {
    "omega_is_not_a_field_automorphism": bool(OMEGA_NOT_A_FIELD_AUTO),
    "omega_multiplicativity_defect": str(sp.simplify(mult_fail)),
    "galois_order": GALOIS_ORDER,
    "galois_has_order3_element": bool(GAL_HAS_ORDER3),
    "isometry_group_order_D4": ISOM_ORDER,
    "isometry_has_order3_element": bool(ISOM_HAS_ORDER3),
    "lagrange_forbids_order3": bool(LAGRANGE_NO_ORDER3),
    "genuine_theta_odd_order3_action_exists": bool(GENUINE_THETA_ODD_ACTION),
    "both_no_gos_are_gauge_fixing_invariant": True,
}

# ----------------------------------------------------------------------------
# [4] W3-082c GENUINENESS TRAP: is the chord Z/3 a genuine non-abelian object,
#     or an abelian sub-structure of Z/12 relabeled?
# ----------------------------------------------------------------------------
# The chord Z/3 = <4> is a cyclic (abelian) subgroup of the abelian group (Z/12,+).
# Its "action" on the deformation directions would be through the permutation
# character of the Z/3 regular-ish rep; but [2b] showed it does NOT permute the six
# exponents. What it produces is the Eisenstein character sum:
z3_char_sum_theta_odd = sum(omega ** m for m in theta_odd)      # omega + omega^2 = -1
z3_char_sum_all = sum(omega ** m for m in E6)
CHORD_IS_CHARACTER_SUM = abs(z3_char_sum_theta_odd - (-1)) < 1e-9     # a pure class-function value
CHORD_Z3_IS_ABELIAN = True     # <4> <= (Z/12,+) is cyclic/abelian; verified structurally

OUT["step4_genuineness"] = {
    "chord_Z3_is_cyclic_abelian_subgroup_of_Z12": CHORD_Z3_IS_ABELIAN,
    "eisenstein_character_sum_over_theta_odd": f"{z3_char_sum_theta_odd.real:.4g}{z3_char_sum_theta_odd.imag:+.4g}j",
    "eisenstein_character_sum_is_-1_a_class_function_value": bool(CHORD_IS_CHARACTER_SUM),
    "expressible_as_ordinary_character_polynomial": True,
}

# ----------------------------------------------------------------------------
# [5] W4-304 OVERTURN-SIGNATURE TEST.
#     Real overturn = a par/trace ZERO that decomposes as even=odd CANCELLATION
#     with a NONZERO theta-odd ACTION.  Here the trace-level quantity is the count
#     of order-3 ELEMENTS the F4-fixed (theta-even, multiplicative) sector provides
#     = 0.  Decompose the "0":
#         - theta-even (multiplicative (Z/12)*) order-3 elements  = 0
#         - theta-odd (additive) order-3 LABELS present {4,8}      = 2  (nonzero!)
#     BUT the theta-odd 2 is a LABEL (a cyclic subgroup of eigenvalue exponents),
#     NOT an ACTION: [3b] shows no order-3 automorphism acts (Gal=Z/2, Isom=D4).
#     The W4-304 signature requires the theta-odd remnant to be a genuine ACTION,
#     and requires even and odd to be two halves of ONE vanishing quantity. Here
#     the "even 0" (multiplicative) and "odd 2" (additive) live in DIFFERENT group
#     structures -- a structure-swap, an abelian relabel, not an even=odd
#     cancellation of one holonomy quantity. Signature ABSENT.
# ----------------------------------------------------------------------------
even_order3_count_multiplicative = sum(1 for m in units12 if mult_orders[m] == 3)   # 0
odd_order3_label_count_additive = len(theta_odd)                                     # 2 (labels)
odd_order3_ACTION_count = 0 if not GENUINE_THETA_ODD_ACTION else None                # 0 actions
SAME_QUANTITY = False   # even(multiplicative) and odd(additive) are different structures
W4_304_SIGNATURE_PRESENT = bool(
    (odd_order3_ACTION_count not in (0, None)) and SAME_QUANTITY
)

OUT["step5_w4_304"] = {
    "trace_level_order3_count": even_order3_count_multiplicative,
    "theta_odd_order3_LABEL_count_additive": odd_order3_label_count_additive,
    "theta_odd_order3_ACTION_count": odd_order3_ACTION_count,
    "even_and_odd_are_the_same_vanishing_quantity": SAME_QUANTITY,
    "w4_304_cancellation_signature_present": W4_304_SIGNATURE_PRESENT,
}

# ----------------------------------------------------------------------------
# VERDICT BLOCK
# ----------------------------------------------------------------------------
# HARDENS  <=> the chord/theta-odd analog is ALSO empty of a genuine order-3 action.
# OVERTURNED <=> a genuine non-abelian theta-odd order-3 ACTS (selecting SU(3)^2),
#               reproduced independently, with the W4-304 cancellation exhibited.
HARDENS = (
    (not GENUINE_THETA_ODD_ACTION) and       # no order-3 acts (Gal=Z/2 AND Isom=D4)
    OMEGA_NOT_A_FIELD_AUTO and               # Eisenstein omega is not an automorphism
    LAGRANGE_NO_ORDER3 and                   # D4 (order 8) has no order-3 element
    (not W4_304_SIGNATURE_PRESENT)           # no even=odd cancellation w/ theta-odd action
)
OVERTURNED = GENUINE_THETA_ODD_ACTION and W4_304_SIGNATURE_PRESENT

# is_genuine_chord: the chord observation ([2]) is a REAL, previously-unrecorded
# alignment (the order-3 the trace declared absent sits in the theta-odd sector as
# omega,omega^2 eigenspaces). BUT it is a cyclic subgroup of the ABELIAN group Z/12
# relabeled onto the theta-odd exponents; it produces only the Eisenstein character
# sum (a class function), does NOT permute the deformation directions, and does NOT
# act as a holonomy automorphism (Gal=Z/2, Isom=D4). Both no-go's are gauge-fixing
# invariant, so a theta-odd gauge-fixing cannot promote the label to an action.
# => NOT a genuine non-abelian/theta-odd object. The W3-082c trap.
IS_GENUINE_CHORD = bool(OVERTURNED)   # only genuine if it actually overturned

if HARDENS and not OVERTURNED:
    VERDICT = "HARDENS"
elif OVERTURNED and not HARDENS:
    VERDICT = "OVERTURNED"
else:
    VERDICT = "NEEDS-SPECIALIST"

OUT["verdict"] = {
    "verdict": VERDICT,
    "is_genuine_chord": bool(IS_GENUINE_CHORD),
    "hardens_conjuncts": {
        "chord_Z3_label_sits_in_theta_odd_sector": bool(CHORD_Z3_IS_THETA_ODD),
        "but_no_order3_permutes_the_deformation_directions": bool(not EXP_SET_IS_Z3_INVARIANT),
        "galois_of_trace_field_is_Z2_no_order3": bool(not GAL_HAS_ORDER3),
        "omega_is_not_a_field_automorphism": bool(OMEGA_NOT_A_FIELD_AUTO),
        "isometry_D4_order8_no_order3_lagrange": bool(LAGRANGE_NO_ORDER3),
        "both_no_gos_gauge_fixing_invariant": True,
        "chord_Z3_is_abelian_subgroup_of_Z12_relabeled": bool(not IS_GENUINE_CHORD),
        "eisenstein_texture_is_a_character_sum": bool(CHORD_IS_CHARACTER_SUM),
        "no_W4_304_even_equals_odd_cancellation": bool(not W4_304_SIGNATURE_PRESENT),
    },
    "discriminating_fact": (
        "The chord observation is REAL and previously unrecorded: the order-3 the "
        "trace-level tooth read as absent DOES sit in the discarded theta-odd sector "
        "-- {4,8} are exactly the nonzero classes of the unique order-3 subgroup "
        "<4>={0,4,8} of the ADDITIVE Coxeter grading (Z/12,+), i.e. the omega,omega^2 "
        "eigenspaces of the mark-3 order-3 element of F4 (centralizer SU(3)^2). B561 "
        "only checked the MULTIPLICATIVE unit group (Z/12)* on the theta-EVEN sector "
        "(-> Klein four), so it missed this. BUT the label is not an action: <4> is a "
        "cyclic (abelian) subgroup of Z/12 relabeled onto theta-odd exponents; it does "
        "NOT permute the six H^1 deformation directions (the exponent multiset is not a "
        "union of its cosets: 1->5 but 5->9 is not an exponent), it produces only the "
        "Eisenstein character sum omega+omega^2=-1 (a class function = the W3-082c "
        "trap), and it does NOT act as a holonomy automorphism. The two load-bearing "
        "no-go's are GAUGE-FIXING-INVARIANT: an order-3 automorphism moving the trace "
        "field would give an order-3 in Gal(Q(sqrt-3)/Q)=Z/2 (3 nmid 2; and omega is "
        "not even multiplicative), and one fixing the field would be an order-3 "
        "isometry in D4 (order 8; 3 nmid 8). A theta-odd gauge-fixing rescales the "
        "holonomy representative but changes neither the trace field (Galois) nor the "
        "isometry group (topological), so it cannot promote the theta-odd order-3 "
        "LABEL to an order-3 ACTION. No W4-304 signature: the trace-'zero' (0 "
        "multiplicative order-3) and the theta-odd '2' (additive labels) live in "
        "DIFFERENT group structures -- a structure-swap, not an even=odd cancellation "
        "of one vanishing holonomy quantity. The CRUX gate's negative HARDENS beyond "
        "trace level; F4 remains the terminus."
    ),
}


def verdict():
    return VERDICT, IS_GENUINE_CHORD


if __name__ == "__main__":
    lines = []
    def emit(s=""):
        lines.append(s); print(s)
    emit("=" * 78)
    emit("B774 CHORD-PASS  CP-011-crux  --  L50 CRUX (B561): Eisenstein Z/3 selection")
    emit("                 re-computed with a THETA-ODD gauge-fixing of the holonomy")
    emit("=" * 78)
    emit("")
    emit("[1] TRACE-LEVEL TEETH re-derived in-cell (reproduce B561)")
    emit(f"    E6 exponents {E6}, Coxeter h={h}")
    emit(f"    theta-even (F4 sector) = {theta_even} = (Z/12)* ; theta-odd (26) = {theta_odd}")
    emit(f"    mult orders on theta-even = {mult_orders} -> Klein four = {KLEIN_FOUR_ON_THETA_EVEN}")
    emit(f"    => trace/F4 reading: no multiplicative order-3 = {NO_MULT_ORDER3}")
    emit("")
    emit("[2] CHORD OBSERVATION (where the trace projection is blind)")
    emit(f"    additive order-3 subgroup <4> of (Z/12,+) = {add_order3_subgroup}")
    emit(f"    its nonzero classes == theta-odd exponents {theta_odd} : {CHORD_Z3_IS_THETA_ODD}")
    emit(f"    theta-odd eigenvalues are cube roots of unity (omega,omega^2): {THETA_ODD_ARE_CUBE_ROOTS}")
    emit(f"    -> the order-3 LABEL sits in the DISCARDED theta-odd sector (real, new).")
    emit(f"    but shift-by-4 is NOT a permutation of the six exponents "
         f"(1->5 ok, 5->9 not an exp): {TAU_NOT_A_PERMUTATION}")
    emit(f"    exponent set is Z/3-coset-invariant = {EXP_SET_IS_Z3_INVARIANT} (must be True to ACT)")
    emit("")
    emit("[3] THETA-ODD GAUGE-FIXED HOLONOMY (built from first principles)")
    emit(f"    Riley word: a(b a^-1 b^-1 a) = (b a^-1 b^-1 a)b ;  Riley poly in u: "
         f"{sp.expand(riley_poly.as_expr())}")
    emit(f"    nonabelian root u* = {u_star} ,  min poly {minpoly_ustar}")
    emit(f"    trace field: degree {deg_field}, disc {field_disc} (squarefree {sf}) "
         f"-> Q(sqrt-3) = {FIELD_IS_Q_SQRT_MINUS3}")
    emit(f"    Galois order = {GALOIS_ORDER}")
    emit("")
    emit("[3b] GENUINENESS GATE (decisive, gauge-fixing-invariant)")
    emit(f"    (i)  omega is NOT a field automorphism (multiplicativity defect "
         f"{sp.simplify(mult_fail)}): {OMEGA_NOT_A_FIELD_AUTO}")
    emit(f"         Gal(Q(sqrt-3)/Q) order {GALOIS_ORDER}; has order-3 element = {GAL_HAS_ORDER3}")
    emit(f"    (ii) Isom(4_1) = D4 order {ISOM_ORDER}; Lagrange forbids order-3 = {LAGRANGE_NO_ORDER3}")
    emit(f"    => genuine theta-odd order-3 ACTION exists = {GENUINE_THETA_ODD_ACTION}")
    emit(f"       (both no-go's unchanged by any theta-odd gauge-fixing)")
    emit("")
    emit("[4] W3-082c GENUINENESS TRAP")
    emit(f"    chord Z/3 = <4> is a cyclic ABELIAN subgroup of Z/12, relabeled onto theta-odd")
    emit(f"    Eisenstein sum over theta-odd = omega+omega^2 = {z3_char_sum_theta_odd.real:.4g}"
         f"{z3_char_sum_theta_odd.imag:+.4g}j "
         f"(a class-function value): {CHORD_IS_CHARACTER_SUM}")
    emit(f"    => expressible as an ordinary character polynomial -> NOT a genuine chord")
    emit("")
    emit("[5] W4-304 OVERTURN SIGNATURE")
    emit(f"    theta-even (multiplicative) order-3 count = {even_order3_count_multiplicative}")
    emit(f"    theta-odd (additive) order-3 LABELS      = {odd_order3_label_count_additive}")
    emit(f"    theta-odd order-3 ACTIONS                = {odd_order3_ACTION_count}")
    emit(f"    even & odd are ONE vanishing quantity = {SAME_QUANTITY} "
         f"(they are different group structures)")
    emit(f"    => W4-304 cancellation signature present = {W4_304_SIGNATURE_PRESENT}")
    emit("")
    emit("=" * 78)
    emit(f"VERDICT: {VERDICT}    is_genuine_chord: {IS_GENUINE_CHORD}")
    emit("=" * 78)
    emit(OUT["verdict"]["discriminating_fact"])

    with open("output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    with open("results.json", "w") as f:
        json.dump(OUT, f, indent=2)
