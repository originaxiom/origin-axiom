#!/usr/bin/env python3
"""B8091 -- what the FIRST STEP throws away: the monodromy is the SQUARE of the substitution
matrix, and squaring erases exactly the two things the ledger prices as bits.

The owner's question: does the founding rule a->ab, b->a already encode arrow, chirality,
dynamics and selection, so that the recurring bottlenecks are one loss with several shadows?

This computes the destruction. It does NOT prove the identification (which loss carries which
bit) -- that is registered as the sharpened L169 and explicitly left unproved here.

QUANTIFIER (COMPUTE_THE_PROGRAM): 2x2 integer matrices and word combinatorics. Nothing about
E6, no SM content, no values. Gate 5 untouched.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def det(A):   return A[0][0]*A[1][1] - A[0][1]*A[1][0]
def tr(A):    return A[0][0] + A[1][1]
def incidence(sub, L="ab"):
    """M[i][j] = number of occurrences of letter i in sub(letter j) -- counts, never order."""
    return [[sub[c].count(r) for c in L] for r in L]

SIGMA  = {"a": "ab", "b": "a"}     # the founding rule
MIRROR = {"a": "ba", "b": "a"}     # its mirror -- the other chirality
M, Mm = incidence(SIGMA), incidence(MIRROR)

print("=" * 74); print("1. THE RULE AND ITS MATRIX"); print("=" * 74)
gate("sigma's incidence matrix is the Fibonacci matrix [[1,1],[1,0]]", M == [[1,1],[1,0]], str(M))
gate("char poly of M is t^2 - t - 1 (so the slope is GOLDEN)",
     (tr(M), det(M)) == (1, -1), f"trace {tr(M)}, det {det(M)}")

print(); print("=" * 74); print("2. LOSS ONE -- ORDER"); print("=" * 74)
gate("a->ab and a->ba are DIFFERENT rules", SIGMA != MIRROR)
gate("but their incidence matrices are IDENTICAL -> the mirror is invisible downstream", M == Mm,
     f"{M} == {Mm}")
# BITE: order-blindness must not be vacuous -- a genuinely different rule must differ
BITE = {"a": "aab", "b": "a"}
gate("BITE: a genuinely different rule DOES change the matrix (blindness is not vacuous)",
     incidence(BITE) != M, str(incidence(BITE)))

print(); print("=" * 74); print("3. LOSS TWO -- SIGN, AND WHY SQUARING IS FORCED"); print("=" * 74)
M2 = mul(M, M)
gate("det M = -1 (orientation-REVERSING)", det(M) == -1)
gate("det M^2 = +1 (orientation-preserving) -> squaring ERASES the sign", det(M2) == 1)
# A punctured-torus bundle is orientable iff its monodromy is orientation-preserving.
gate("so M itself is INADMISSIBLE as the monodromy of an ORIENTABLE bundle", det(M) != 1)
gate("and M^2 is admissible -- the square is FORCED, not chosen", det(M2) == 1)

print(); print("=" * 74); print("4. THE MONODROMY IS THE SQUARE"); print("=" * 74)
gate("M^2 = [[2,1],[1,1]]", M2 == [[2,1],[1,1]], str(M2))
gate("its trace is 3 and det 1 -- the figure-eight monodromy phi_1",
     tr(M2) == 3 and det(M2) == 1)
# the banked family: phi_m - I = [[m^2, m],[m, 0]]  (paper's check_homology)
phi1_minus_I = [[M2[0][0]-1, M2[0][1]], [M2[1][0], M2[1][1]-1]]
gate("OBSERVATION (unweighted, B888 discipline): phi_1 - I equals M itself",
     phi1_minus_I == M, f"{phi1_minus_I} == {M}")

print(); print("=" * 74); print("5. WHAT SURVIVES, AND WHAT DOES NOT"); print("=" * 74)
print("""    survives: the SLOPE (the eigenvalue ratio -- golden), because it is a property of M^2 too
    lost    : the ORDER inside sigma(a)   -> the incidence matrix counts, never arranges
    lost    : the SIGN of det             -> squaring, and squaring is forced by orientability
    never present: the INTERCEPT          -> the slope fixes the hull, not the point on it
    never present: the eigenvalue's UNIT  -> only ratios of eigenvalues are scale-free""")

RES = {"M": M, "M_mirror": Mm, "M2": M2,
       "det_M": det(M), "det_M2": det(M2), "trace_M2": tr(M2),
       "order_is_invisible": M == Mm,
       "bite_nonvacuous": incidence(BITE) != M,
       "squaring_forced_by_orientability": det(M) == -1 and det(M2) == 1,
       "monodromy_is_the_square": M2 == [[2,1],[1,1]] and tr(M2) == 3,
       "phi1_minus_I_equals_M": phi1_minus_I == M,
       "losses": {"order": "chirality (IDENTIFICATION UNPROVED)",
                  "sign":  "arrow/orientation (IDENTIFICATION UNPROVED)",
                  "intercept": "phase (never present, not lost)",
                  "unit": "scale (never present, not lost)"},
       "scope": ("2x2 integer matrices and word combinatorics. PROVES the destruction -- "
                 "order-blindness and sign-erasure -- and PROVES the square is forced by "
                 "orientability. Does NOT prove the IDENTIFICATION of which loss carries which "
                 "bit; that is the sharpened L169 and is registered UNPROVED. Nothing about E6, "
                 "no SM content, no values. Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED: raise SystemExit(f"FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
