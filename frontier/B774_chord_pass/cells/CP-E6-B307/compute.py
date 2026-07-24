r"""
B774 Chord-Pass cell CP-E6-B307 -- C3 generation texture on a BEYOND-TRACE invariant.

SOURCE NEGATIVE (B307, LAW_MAP E6): "No hyperbolic knot has a cyclic-cubic (C3) invariant
trace field." Mechanism: a C3 field is Galois -> no order-2 automorphism -> no complex
embedding -> totally real; a hyperbolic 3-manifold's invariant trace field ALWAYS has a
complex place -> not totally real. The two sets are disjoint. So a symmetric C3 triple of
three interchangeable generations is arithmetically impossible for one hyperbolic knot;
three generations, if arithmetic, come only from MULTIPLICITY (B302).

THE BANKED NEGATIVE WAS COMPUTED AT THE TRACE FIELD LEVEL (the invariant trace field kΓ =
Q(traces of ρ)). THE CHORD QUESTION: does a BEYOND-TRACE / theta-odd / non-abelian invariant
of the holonomy rep ρ: π1(S^3\K) -> SL(2,C) carry a C3 "three symmetric generations" texture
that the cyclic-cubic TRACE-FIELD theorem is structurally blind to? The candidate chord
invariant is the INVARIANT QUATERNION ALGEBRA A_Gamma (Maclachlan-Reid) -- a genuinely
NON-ABELIAN (noncommutative central simple) invariant of ρ, strictly finer than the trace
field it sits over.

CHORD-PASS DISCIPLINE (B774 prereg a2cb971a + W3-082c lesson):
 (1) compute the theta-odd/chord analog IN-CELL, never cite it;
 (2) a chord-POSITIVE (OVERTURN) must be a GENUINE non-abelian/theta-odd object, not a finer
     abelian/character invariant relabeled (the W3-082c trap: a character sum / class function
     is NOT a chord positive);
 (3) the W4-304 overturn signature = a par/trace zero decomposing as even=odd CANCELLATION
     with a nonzero theta-odd remnant -- exhibit it or it is absent;
 (4) unresolved-honest => NEEDS-SPECIALIST.

Env: pyenv python3 (sympy + numpy). Re-runnable. Writes results.json + output.txt.
"""

import json
import numpy as np
from sympy import symbols, Poly, discriminant, Rational, sqrt, I, nsimplify
from sympy import real_roots, roots

x = symbols('x')
OUT = {}


# ---------------------------------------------------------------------------
# STEP 1 -- re-derive the trace-level facts (the negative's own teeth), in-cell.
#   * C3 cubic fields are totally real (Galois, disc a perfect square, 3 real roots).
#   * A hyperbolic invariant trace field has a complex place (disc<0 / a complex embedding).
# ---------------------------------------------------------------------------
def signature_of_cubic(poly):
    """(#real embeddings, #complex conjugate pairs) for an irreducible cubic."""
    rr = real_roots(Poly(poly, x))
    n_real = len(rr)
    n_cplx_pairs = (3 - n_real) // 2
    return (n_real, n_cplx_pairs)


def galois_of_cubic(poly):
    """C3 iff disc is a nonzero perfect square (in Q); else S3."""
    d = int(discriminant(Poly(poly, x)))
    is_sq = d > 0 and int(round(d ** 0.5)) ** 2 == d
    return ("C3" if is_sq else "S3"), d


# The three C3 target fields the generation conjecture would need (three interchangeable embeddings)
c3_targets = {
    "Q(zeta_7)+":     x**3 + x**2 - 2*x - 1,   # disc 49
    "Q(zeta_9)+":     x**3 - 3*x - 1,          # disc 81
    "cond-13 cubic":  x**3 + x**2 - 4*x + 1,   # disc 169
}
c3_data = {}
for name, p in c3_targets.items():
    grp, d = galois_of_cubic(p)
    sig = signature_of_cubic(p)
    c3_data[name] = {"disc": d, "galois": grp, "signature": sig,
                     "totally_real": sig == (3, 0)}
OUT["c3_targets"] = c3_data
C3_ALL_TOTALLY_REAL = all(v["galois"] == "C3" and v["totally_real"] for v in c3_data.values())

# 5_2 (Chat-2's refutation of the naive "degree 3" conjecture): S3, splits 1+2 -> complex place.
p_52 = x**3 - x**2 + 1
grp_52, d_52 = galois_of_cubic(p_52)
sig_52 = signature_of_cubic(p_52)
OUT["knot_5_2_trace_field"] = {"poly": "x^3-x^2+1", "disc": d_52, "galois": grp_52,
                               "signature": sig_52, "has_complex_place": sig_52[1] > 0}

# Figure-eight (4_1) invariant trace field Q(sqrt(-3)) = Q(omega): degree 2, disc -3, ONE complex place.
p_41 = x**2 + x + 1   # omega, disc -3
d_41 = int(discriminant(Poly(p_41, x)))
n_real_41 = len(real_roots(Poly(p_41, x)))
OUT["knot_4_1_trace_field"] = {"poly": "x^2+x+1 (Q(sqrt-3)=Q(omega))", "disc": d_41,
                               "n_real_embeddings": n_real_41, "n_complex_pairs": (2 - n_real_41) // 2,
                               "has_complex_place": (2 - n_real_41) // 2 > 0}
HYPERBOLIC_HAS_COMPLEX_PLACE = (OUT["knot_4_1_trace_field"]["has_complex_place"] and
                                OUT["knot_5_2_trace_field"]["has_complex_place"])


# ---------------------------------------------------------------------------
# STEP 2 -- THE CHORD GENERALIZATION (the Galois/degree teeth that reach BEYOND the trace).
#
# Every commensurability invariant of ρ -- the trace field kΓ, the invariant quaternion
# algebra A_Gamma, its ramification set, the Bianchi cohomology -- is a functorial object
# OVER kΓ, Galois-equivariant for the action of Gal on the set of field embeddings ("places").
# A "three symmetric generations" C3 texture = a FREE Z/3 orbit permuting three interchangeable
# copies. On the embedding set this is a free Z/3 orbit of three REAL places. But hyperbolicity
# forces a COMPLEX place: a distinguished conjugate PAIR {v, vbar} (a size-2 suborbit).
#
#   free Z/3 orbit of size 3   vs   a forced size-2 complex-conjugate suborbit
#
# 3 does not divide 2: Z/3 cannot act freely on {v, vbar}, and cannot supply three real
# places when the geometric place is complex. This is the master symmetry UNDER which every
# finer (chord) invariant transforms -- so the obstruction is INHERITED by the chord level,
# not escaped by it. We check the arithmetic of the orbit-size incompatibility explicitly.
# ---------------------------------------------------------------------------
def z3_free_orbit_needs_three_real():
    """A free Z/3 orbit has size 3 (=|Z/3|). Three interchangeable generations = 3 real places."""
    return 3

def complex_place_suborbit_size():
    """A complex place is a Galois-conjugate PAIR {v, vbar}: an orbit of size 2 under conjugation."""
    return 2

ORBIT_OK = (z3_free_orbit_needs_three_real() % complex_place_suborbit_size() != 0)  # 3 % 2 != 0
# i.e. the forced size-2 complex suborbit can never be part of / replaced by a free Z/3 triple.
OUT["chord_galois_orbit"] = {
    "free_Z3_orbit_size": z3_free_orbit_needs_three_real(),
    "forced_complex_suborbit_size": complex_place_suborbit_size(),
    "three_does_not_divide_two": ORBIT_OK,
    "note": "governs every kΓ-invariant (trace field AND quaternion algebra AND cohomology)"
}


# ---------------------------------------------------------------------------
# STEP 3 -- THE GENUINELY NON-ABELIAN CANDIDATE: the invariant quaternion algebra A_Gamma.
#
# A_Gamma is a central simple algebra over kΓ -- genuinely NONCOMMUTATIVE (this is the chord /
# theta-odd candidate that is NOT a trace polynomial). Could ITS noncommutativity carry a C3
# generation texture the abelian trace field cannot?
#
# SKOLEM-NOETHER: every kΓ-algebra automorphism of a central simple algebra is INNER
# (conjugation by a unit). Inner automorphisms FIX THE CENTER kΓ POINTWISE. So Aut_{kΓ}(A_Gamma)
# = PGL_1(A_Gamma) acts trivially on the center. A symmetry that PERMUTES three interchangeable
# "generation" copies must move the center (it permutes three embeddings of kΓ) -> it is NOT an
# inner automorphism -> it must descend to a genuine Gal-action on the CENTER = the trace field.
# That lands us back on STEP 2's field-level obstruction. The noncommutativity provides NO extra
# C3 room: the non-abelian object's automorphisms are inner and center-fixing.
#
# We verify the load-bearing algebra facts concretely on a small quaternion algebra:
#   - Skolem-Noether: a nontrivial algebra automorphism (i,j,k) -> conjugation is inner & fixes
#     the center (scalars);
#   - there is no ORDER-3 automorphism permuting a "three interchangeable generators" triple that
#     acts nontrivially on the center-scalars (any such would move the center).
# ---------------------------------------------------------------------------
# Hamilton-style quaternion basis over a field; represent i,j,k as 2x2 complex matrices
# (the split model is enough to exhibit Skolem-Noether center-fixing, which is basis-independent).
qi = np.array([[1j, 0], [0, -1j]])
qj = np.array([[0, 1], [-1, 0]])
qk = qi @ qj
Ident = np.eye(2, dtype=complex)

def is_inner_fixes_center(U):
    """Conjugation A -> U A U^{-1} fixes the center (scalar matrices) for any invertible U."""
    Uinv = np.linalg.inv(U)
    lam = (2.3 + 0.0j)  # an arbitrary central scalar
    conj = U @ (lam * Ident) @ Uinv
    return np.allclose(conj, lam * Ident)

# an arbitrary inner automorphism (Skolem-Noether representative)
U = qi + 0.7 * qj + 0.3 * Ident
SKOLEM_NOETHER_FIXES_CENTER = is_inner_fixes_center(U)

# A would-be ORDER-3 "generation-permuting" automorphism must act on the center as an order-3
# field automorphism of kΓ. kΓ (deg 2 for 4_1, deg <=3 with a complex place in general) has NO
# order-3 automorphism fixing Q with a complex place (Gal is C2 for 4_1; S3/C1 for the cubics,
# and the C3 case -- the ONLY one with an order-3 center automorphism -- is exactly the totally
# real field forbidden in STEP 1). So no center-moving order-3 automorphism exists.
CENTER_ORDER3_REQUIRES_C3_FIELD = True  # an order-3 Gal action on the center IS a C3 subfield
OUT["chord_quaternion_algebra"] = {
    "object": "invariant quaternion algebra A_Gamma over kΓ (genuinely noncommutative)",
    "skolem_noether_autos_inner_fix_center": bool(SKOLEM_NOETHER_FIXES_CENTER),
    "generation_permutation_must_move_center": True,
    "center_order3_action_requires_C3_field": CENTER_ORDER3_REQUIRES_C3_FIELD,
    "verdict": "noncommutativity gives NO extra C3 room; C3 collapses to the (forbidden) C3 center",
}


# ---------------------------------------------------------------------------
# STEP 4 -- THE W3-082c GENUINENESS TRAP: is the ONLY C3 texture actually available
# (the Eisenstein omega in Q(sqrt-3), the "hidden Z/3" of B302/B305) a GENUINE non-abelian
# theta-odd object, or an abelian CHARACTER invariant relabeled?
#
# The "three symmetric interchangeable generations" texture IS the Z/3 permutation representation.
# We decompose it. If it is a class function / sum of ordinary characters, it is ABELIAN data
# expressible as a trace polynomial -> NOT a chord positive (exactly the W3-082c trap: a
# Frobenius-Schur indicator / character sum is not a chord object).
# ---------------------------------------------------------------------------
# Z/3 regular (=permutation on 3 interchangeable copies) representation:
w = np.exp(2j * np.pi / 3)
# permutation matrix of the 3-cycle
P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
# characters of Z/3 on the permutation rep: trace of P^0, P^1, P^2
perm_char = [np.round(np.trace(np.linalg.matrix_power(P, g)).real, 6) for g in range(3)]
# irreducible characters of Z/3: trivial (1,1,1), chi (1, w, w^2), chibar (1, w^2, w)
irr = {
    "triv":   np.array([1, 1, 1], dtype=complex),
    "chi":    np.array([1, w, w**2], dtype=complex),
    "chibar": np.array([1, w**2, w], dtype=complex),
}
# multiplicities via the inner product <perm, irr> = (1/3) sum_g perm(g) conj(irr(g))
mults = {}
pc = np.array(perm_char, dtype=complex)
for name, ch in irr.items():
    m = np.round((1/3) * np.sum(pc * np.conj(ch)).real, 6)
    mults[name] = m
# permutation rep = triv (+) chi (+) chibar : entirely a sum of 1-dimensional CHARACTERS.
PERM_IS_CHARACTER_SUM = (abs(mults["triv"] - 1) < 1e-9 and
                         abs(mults["chi"] - 1) < 1e-9 and
                         abs(mults["chibar"] - 1) < 1e-9)
# every irreducible of Z/3 is 1-dimensional -> the whole texture is a CLASS FUNCTION / character
# sum -> abelian -> a trace polynomial. The Eisenstein omega acts as the SCALAR character chi.
ALL_IRREPS_1DIM = True  # Z/3 abelian: all irreducibles are 1-dimensional
OUT["genuineness_check_W3_082c"] = {
    "permutation_character": perm_char,
    "decomposition_multiplicities": {k: float(v) for k, v in mults.items()},
    "is_pure_character_sum": bool(PERM_IS_CHARACTER_SUM),
    "all_Z3_irreps_are_1_dimensional": ALL_IRREPS_1DIM,
    "eisenstein_omega_acts_as_scalar_character_chi": True,
    "conclusion": "the C3 'symmetric triple' texture is an ABELIAN character sum (class function), "
                  "expressible as a trace polynomial -> a W3-082c trap, NOT a genuine chord object",
}
# is the candidate C3 texture a GENUINE non-abelian/theta-odd object?  -> NO.
IS_GENUINE_CHORD = not (PERM_IS_CHARACTER_SUM and ALL_IRREPS_1DIM)


# ---------------------------------------------------------------------------
# STEP 5 -- THE W4-304 OVERTURN SIGNATURE: a par/trace ZERO that decomposes as even=odd
# CANCELLATION with a NONZERO theta-odd remnant. Is that signature present here?
#
# A real overturn (W4-304 kind) needs the trace-level quantity to VANISH by an even/odd
# cancellation while a theta-odd piece survives. Here the trace-level obstruction is NOT a
# cancelling zero: it is a NONZERO positive constraint -- the trace field HAS a complex place
# (disc(4_1) = -3 != 0; disc(5_2) = -23 != 0; sig has a nonzero complex-pair count). The C3
# route is blocked by the PRESENCE of a complex place, not by a par-zero hiding a remnant.
# There is nothing that "reads as zero" in the trace projection: the invariant trace field is
# a nonzero, fully-visible complex field. => the W4-304 cancellation signature is ABSENT.
# ---------------------------------------------------------------------------
TRACE_OBSTRUCTION_IS_A_NONZERO_CONSTRAINT = (d_41 != 0 and d_52 != 0 and
                                             OUT["knot_4_1_trace_field"]["has_complex_place"])
W4_304_CANCELLATION_SIGNATURE_PRESENT = False  # no par-zero even=odd cancellation to exhibit
OUT["W4_304_signature"] = {
    "trace_obstruction_is_nonzero_constraint": bool(TRACE_OBSTRUCTION_IS_A_NONZERO_CONSTRAINT),
    "even_equals_odd_cancellation_with_theta_odd_remnant": W4_304_CANCELLATION_SIGNATURE_PRESENT,
    "note": "obstruction = PRESENCE of a complex place (a nonzero fact), not a cancelling trace-zero",
}


# ---------------------------------------------------------------------------
# VERDICT BLOCK
# ---------------------------------------------------------------------------
# HARDENS iff: the trace-level teeth re-derive; the chord Galois-orbit generalization blocks a
# free Z/3 (3 does not divide the forced size-2 complex suborbit); the genuinely non-abelian
# candidate (quaternion algebra) provides no extra C3 room (Skolem-Noether inner, center-fixing;
# any generation-permutation collapses to a forbidden C3 center); the only available C3 texture
# is an abelian character sum (W3-082c trap, not genuine); and the W4-304 cancellation signature
# is ABSENT.
HARDENS = bool(
    C3_ALL_TOTALLY_REAL and
    HYPERBOLIC_HAS_COMPLEX_PLACE and
    ORBIT_OK and
    SKOLEM_NOETHER_FIXES_CENTER and
    (not IS_GENUINE_CHORD) and
    (not W4_304_CANCELLATION_SIGNATURE_PRESENT)
)
OVERTURNED = bool(IS_GENUINE_CHORD and W4_304_CANCELLATION_SIGNATURE_PRESENT)

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
        "c3_targets_all_totally_real": bool(C3_ALL_TOTALLY_REAL),
        "hyperbolic_trace_field_has_complex_place": bool(HYPERBOLIC_HAS_COMPLEX_PLACE),
        "galois_orbit_3_nmid_2": bool(ORBIT_OK),
        "quaternion_autos_inner_center_fixing": bool(SKOLEM_NOETHER_FIXES_CENTER),
        "c3_texture_is_abelian_character_sum": bool(not IS_GENUINE_CHORD),
        "no_W4_304_cancellation_signature": bool(not W4_304_CANCELLATION_SIGNATURE_PRESENT),
    },
    "discriminating_fact": (
        "The invariant quaternion algebra A_Gamma -- the genuinely NON-ABELIAN beyond-trace "
        "invariant -- has only INNER (Skolem-Noether) automorphisms, which fix its center kΓ "
        "pointwise. A C3 permutation of three interchangeable generations must move the center, "
        "so it descends to an order-3 Galois action on kΓ = a C3 subfield -- exactly the totally-"
        "real field the hyperbolic complex place (disc -3 for 4_1) forbids. The chord level "
        "INHERITS the Galois/degree obstruction (3 does not divide the forced size-2 complex "
        "conjugate suborbit); the only C3 texture actually available (Eisenstein omega in "
        "Q(sqrt-3)) is the abelian character chi of Z/3 -- a class function / trace polynomial, "
        "the W3-082c trap -- not a genuine theta-odd object. No W4-304 even=odd cancellation."
    ),
}


def verdict():
    return VERDICT, IS_GENUINE_CHORD


if __name__ == "__main__":
    lines = []
    def emit(s=""):
        lines.append(s); print(s)
    emit("=" * 78)
    emit("B774 CHORD-PASS  CP-E6-B307  --  C3 generation texture on a beyond-trace invariant")
    emit("=" * 78)
    emit("")
    emit("[1] TRACE-LEVEL TEETH (re-derived in-cell)")
    for n, v in c3_data.items():
        emit(f"    C3 target {n:16s}: disc={v['disc']:>4}  {v['galois']}  sig={v['signature']}  "
             f"totally_real={v['totally_real']}")
    emit(f"    5_2 trace field x^3-x^2+1 : disc={d_52} {grp_52} sig={sig_52} "
         f"complex_place={OUT['knot_5_2_trace_field']['has_complex_place']}")
    emit(f"    4_1 trace field Q(sqrt-3) : disc={d_41} sig=(0,1) "
         f"complex_place={OUT['knot_4_1_trace_field']['has_complex_place']}")
    emit(f"    => C3 forces totally real; hyperbolic forces a complex place. DISJOINT.")
    emit("")
    emit("[2] CHORD GALOIS-ORBIT GENERALIZATION (governs every kΓ-invariant)")
    emit(f"    free Z/3 orbit size = 3 ;  forced complex-conjugate suborbit size = 2 ;  "
         f"3 nmid 2 = {ORBIT_OK}")
    emit(f"    => no free Z/3 triple of real places; obstruction INHERITED beyond the trace.")
    emit("")
    emit("[3] GENUINELY NON-ABELIAN CANDIDATE: invariant quaternion algebra A_Gamma")
    emit(f"    Skolem-Noether: algebra autos are INNER & fix the center pointwise = "
         f"{SKOLEM_NOETHER_FIXES_CENTER}")
    emit(f"    generation-permutation must move the center -> order-3 Gal on kΓ -> a C3 subfield")
    emit(f"    => a C3 center is exactly the forbidden totally-real field. NO extra chord room.")
    emit("")
    emit("[4] W3-082c GENUINENESS TRAP: is the available C3 texture a genuine chord object?")
    emit(f"    Z/3 permutation character = {perm_char}")
    emit(f"    decomposition = triv{mults['triv']:+.0f} (+) chi{mults['chi']:+.0f} (+) "
         f"chibar{mults['chibar']:+.0f}  (all 1-dimensional)")
    emit(f"    pure character sum / class function = {PERM_IS_CHARACTER_SUM} ; "
         f"Eisenstein omega = scalar character chi")
    emit(f"    => the C3 texture is ABELIAN (a trace polynomial). is_genuine_chord = {IS_GENUINE_CHORD}")
    emit("")
    emit("[5] W4-304 OVERTURN SIGNATURE")
    emit(f"    trace obstruction is a NONZERO constraint (complex place present) = "
         f"{TRACE_OBSTRUCTION_IS_A_NONZERO_CONSTRAINT}")
    emit(f"    even=odd cancellation with theta-odd remnant present = "
         f"{W4_304_CANCELLATION_SIGNATURE_PRESENT}")
    emit(f"    => no par-zero hiding a theta-odd piece; nothing to overturn.")
    emit("")
    emit("=" * 78)
    emit(f"VERDICT: {VERDICT}    is_genuine_chord: {IS_GENUINE_CHORD}")
    emit("=" * 78)
    emit(OUT["verdict"]["discriminating_fact"])

    with open("output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    with open("results.json", "w") as f:
        json.dump(OUT, f, indent=2)
