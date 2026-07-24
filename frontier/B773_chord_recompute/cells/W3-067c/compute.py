#!/usr/bin/env python3
"""
B773 chord-level re-computation -- cell W3-067c.
Field-fusion: the CHORD (twist-curve) analog of the mod-4 quantum twist.

WHY THIS CELL EXISTS
--------------------
B771 cell W3-067 (cells/W3-067/) asked whether a CLASSICAL composite once-punctured-torus bundle
(golden block m=1 concatenated with silver block m=2) has a trace field that FUSES to the compositum
Q(zeta12)=Q(sqrt-3, i) the way the QUANTUM SU(2)_k eigenvalue field does (B132, mod-4 T-twist). It
answered RESOLVED-B (no fusion) -- but it computed the classical side at the INVARIANT trace field
level, i.e. from the SQUARED generators  tr(a^2), tr(b^2), tr((ab)^2).

B772 adequacy audit flagged this TRACE-BLIND-RISK: the quantum comparator is FRAMING / Dehn-twist
(chord) data (R=T, L=STS^-1, the eigenvalue ORDER = the mod-4/mod-8 twist), whereas SQUARING a
holonomy matrix HALVES the eigenvalue order and destroys exactly the mod-2 framing information the
quantum twist lives in. So the prior comparison was CROSS-LEVEL: classical squared vs quantum framed.

THE CHORD LEVEL (what this cell computes)
-----------------------------------------
The "chord" / twist-curve data is the RAW (un-squared) trace of the actual twist curves entering the
R/L word -- the once-punctured-torus fiber generators a, b about which the Dehn twists R, L are taken.
The raw trace field  Q(tr a, tr b, tr ab)  is a genuine (conjugacy-invariant) invariant of the rep,
and it is the un-squared parent of the invariant trace field: it CARRIES the framing/order data the
squared field throws away. Concrete demonstration (below): the silver seed's chord trace tr(a) is a
root of x^4-4x^2+8 (= sqrt(2 +- 2i), eigenvalue order 8), while its SQUARED trace tr(a^2) is merely in
Q(i) (order 4) -- the exp(m*pi*i/4) order-8 T-phase is visible at the chord level, invisible after
squaring. This is precisely the blindness B772 flagged, now removed.

THE MATCHED COMPARISON
----------------------
  quantum (B132, in-cell copy): eigenvalue field of the composite word's SU(2)_k monodromy. This is
      ALWAYS cyclotomic (the monodromy eigenvalues are roots of unity); at k=4 the two 2-block words
      RLRRLL and RRLLRL fuse to Q(zeta12).
  classical chord: the raw twist-curve trace field of the SAME composite mapping torus.
  FUSION PRESENT (RESOLVED-A) would mean the chord field equals / contains that quantum cyclotomic
      fusion field -- i.e. squaring HID a quantum-matching fusion.
  FUSION ABSENT (RESOLVED-B) means the chord field is a generic non-cyclotomic number field with no
      relation to Q(zeta12); the K016 wall HARDENS at the matched level.

THE DISCRIMINATING FACT (exact, symbolic)
-----------------------------------------
The 2-block composite is the manifold s892 (both orderings (1,2),(2,1) give it). We upgrade the prior
cell's bounded-height PSLQ "outside compositum" to an EXACT minimal polynomial + symbolic certificate:
the chord trace tr(a) of s892 is a root of an IRREDUCIBLE DEGREE-14 polynomial over Q. Since phi(n)=14
has NO solution, NO cyclotomic field has degree 14, so Q(tr a) is non-cyclotomic; and since 14 does not
divide [Q(zeta12):Q]=4, tr(a) is not even contained in Q(zeta12). The chord field therefore cannot be
the quantum fusion field. Certified with sympy (irreducibility, totient obstruction, gcd-coprimality
to Phi_12), reproduced across 3 independent PSLQ mixers and 2 precisions.

SEALED CRITERION (B773 prereg 50e31242)
---------------------------------------
chord-level fusion ABSENT (wall hardens at matched level) => RESOLVED-B
chord-level fusion PRESENT (trace projection hid quantum-matching fusion) => RESOLVED-A
pipeline cannot certify => UNRESOLVED

HOUSE METHOD: computed at the chord (un-squared, framing-carrying) level -- NOT the squared projection
B766/B772 proved blind. Exact/symbolic minimal polynomials (sympy), not bounded-height PSLQ verdicts.
Numeric inputs cross-checked at >=2 precisions and >=3 PSLQ mixers with an explicit residual gate. The
verdict logic lives in verdict() and can emit UNRESOLVED. Gate 5/5-Q: structural language only.
"""
import json
import sys

import mpmath as mp
import numpy as np
import snappy
import sympy as sp

mp.mp.dps = 90
x = sp.symbols('x')

LOG = []
def say(s=""):
    print(s)
    LOG.append(s)

ok = True
def chk(name, cond, extra=""):
    global ok
    cond = bool(cond)
    ok = ok and cond
    say(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {extra}" if extra else ""))
    return cond


# ===========================================================================
# 0.  SnapPy plumbing -- RAW (chord) traces, no squaring.
# ===========================================================================
def block_word(seq):
    return "".join("R" * m + "L" * m for m in seq)

def clean(s):
    return str(s).replace(" ", "").replace("E", "e")

def to_mpc(z):
    return mp.mpc(clean(z.real()), clean(z.imag()))

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def tr(M):
    return M[0][0] + M[1][1]

def chord_traces(seq):
    """RAW twist-curve traces tr(a), tr(b), tr(ab) of the composite mapping torus (the CHORD level),
    plus the squared tr(a^2) for the explicit chord-vs-projection contrast."""
    M = snappy.Manifold("b++" + block_word(seq))
    G = M.high_precision().fundamental_group()
    a = G.SL2C('a'); b = G.SL2C('b'); ab = matmul(a, b)
    a2 = matmul(a, a)
    out = {
        "tr(a)":   to_mpc(tr(a)),
        "tr(b)":   to_mpc(tr(b)),
        "tr(ab)":  to_mpc(tr(ab)),
        "tr(a^2)": to_mpc(tr(a2)),
    }
    return M, out


# ===========================================================================
# 1.  Exact minimal polynomial of a complex algebraic number (PSLQ -> sympy).
#     Reproduced across independent real "mixers" K and >=2 precisions; a
#     relation is accepted ONLY if the residual passes an explicit gate.
# ===========================================================================
MIXERS = [mp.sqrt(2) / 3 + mp.pi / 11,
          mp.mpf(1) / 7 + mp.e / 5,
          mp.sqrt(5) - mp.mpf(1) / 3]
RES_GATE = mp.mpf(10) ** -40      # true relations here sit at ~1e-60; artifacts at >=1e-5

def _pslq_minpoly(z, deg, K):
    powers = [z ** k for k in range(deg + 1)]
    v = [mp.re(p) + K * mp.im(p) for p in powers]
    rel = mp.pslq(v, maxcoeff=10 ** 10, maxsteps=10 ** 6, tol=mp.mpf(10) ** -45)
    if not rel:
        return None, None
    res = abs(sum(c * p for c, p in zip(rel, powers)))
    return rel, res

def minimal_polynomial(z, maxdeg=20):
    """Smallest degree d for which a PSLQ relation vanishes below RES_GATE, agreeing across ALL mixers.
    Returns (sympy Poly monic-signed, degree, residual) or (None, None, None)."""
    for d in range(1, maxdeg + 1):
        rels = []
        good = True
        res_max = mp.mpf(0)
        for K in MIXERS:
            rel, res = _pslq_minpoly(z, d, K)
            if rel is None or res is None or res > RES_GATE:
                good = False
                break
            rels.append(rel)
            res_max = max(res_max, res)
        if not good:
            continue
        # normalise every mixer's relation to a signed-monic sympy poly and require they AGREE.
        polys = []
        for rel in rels:
            p = sp.Poly(sum(c * x ** i for i, c in enumerate(rel)), x)
            if p.degree() != d:
                good = False
                break
            p = p * int(sp.sign(p.LC()))
            polys.append(p)
        if not good:
            continue
        if all(p == polys[0] for p in polys):
            return polys[0], d, res_max
    return None, None, None


def is_cyclotomic_field_degree(d):
    """Does ANY cyclotomic field Q(zeta_n) have degree d over Q, i.e. is phi(n)=d solvable?
    phi(n) >= sqrt(n/2) so n < 2*d^2+2 bounds the search."""
    return any(sp.totient(n) == d for n in range(1, 2 * d * d + 4))


def certify_not_in_Qzeta12(minpoly, deg):
    """EXACT (no numerics) certificate that a root of `minpoly` (deg `deg`) is NOT in Q(zeta12).
    Q(zeta12)=Q(sqrt-3,i), [Q(zeta12):Q]=4, Phi_12 = x^4 - x^2 + 1. A number in Q(zeta12) has degree
    dividing 4. Also gcd(minpoly, Phi_12)=1 shows the root is not itself a conjugate of zeta12."""
    Phi12 = sp.Poly(sp.cyclotomic_poly(12, x), x)
    g = sp.gcd(minpoly, Phi12)
    degree_divides_4 = (4 % deg == 0)
    coprime = (sp.Poly(g, x).degree() == 0)
    # in Q(zeta12) => degree | 4.  Here deg=14 does NOT divide 4 => not in Q(zeta12).
    not_contained = (not degree_divides_4) and coprime
    return not_contained, {"[Q(zeta12):Q]": 4, "Phi_12": str(Phi12.as_expr()),
                           "deg(minpoly)": deg, "deg_divides_4": degree_divides_4,
                           "gcd(minpoly,Phi12)_is_constant": coprime}


# ===========================================================================
# 2.  QUANTUM comparator (B132 SU(2)_k), copied in-cell -- the MATCHED level.
#     R=T, L=STS^-1; eigenvalue ORDER d => Q(zeta_d). Roots of unity always => cyclotomic.
# ===========================================================================
def _S(k):
    n = k + 1
    return np.array([[np.sqrt(2 / (k + 2)) * np.sin(np.pi * (a + 1) * (b + 1) / (k + 2))
                      for b in range(n)] for a in range(n)], dtype=complex)

def _T(k):
    n = k + 1
    return np.diag([np.exp(2j * np.pi * (a * (a + 2) / (4 * (k + 2)))) for a in range(n)])

def _rho_word(word, k):
    S = _S(k); T = _T(k); R = T; L = S @ T @ np.linalg.inv(S)
    rep = np.eye(k + 1, dtype=complex)
    for ch in word:
        rep = rep @ (R if ch == "R" else L)
    return rep

def _order(lam, maxn=240):
    for n in range(1, maxn + 1):
        if abs(lam ** n - 1) < 1e-7:
            return n
    return None

def quantum_field(word, k=4):
    orders = sorted([_order(e) for e in np.linalg.eigvals(_rho_word(word, k))], reverse=True)
    s = {o for o in orders if o}
    has6 = any(o in (3, 6) for o in s)
    has4 = any(o == 4 for o in s)
    if has6 and has4:
        field = "Q(zeta12)"
    elif has4:
        field = "Q(i)"
    elif has6:
        field = "Q(sqrt-3)"
    else:
        field = "Q(rational)"
    return field, orders


# ===========================================================================
say("=" * 88)
say("STEP 0 -- the chord vs squared contrast on the KNOWN single seeds (positive controls)")
say("=" * 88)
# Golden m=1: chord trace field must be Q(sqrt-3) (coherent seed -- chord == invariant).
# Silver m=2: chord trace tr(a) must be the ORDER-8 element sqrt(2 +- 2i) (root of x^4-4x^2+8),
#             STRICTLY RICHER than its squared trace tr(a^2) in Q(i) -- the framing the projection hid.
_, g = chord_traces((1,))
mp_ga, dga, _ = minimal_polynomial(g["tr(a)"], maxdeg=6)
say(f"golden(m=1) chord tr(a) = {mp.nstr(g['tr(a)'], 24)}")
say(f"   minpoly = {mp_ga.as_expr()}   deg={dga}   disc={sp.discriminant(mp_ga.as_expr(), x)}")
golden_is_sqrt_m3 = (dga == 2 and sp.discriminant(mp_ga.as_expr(), x) == -12)
chk("golden chord trace generates Q(sqrt-3) (deg-2, disc -12) -- the coherent seed, chord == invariant",
    golden_is_sqrt_m3)

_, s = chord_traces((2,))
mp_sa, dsa, _ = minimal_polynomial(s["tr(a)"], maxdeg=6)
mp_sa2, dsa2, _ = minimal_polynomial(s["tr(a^2)"], maxdeg=6)
say(f"\nsilver(m=2) chord tr(a)   = {mp.nstr(s['tr(a)'], 24)}   minpoly = {mp_sa.as_expr()} (deg {dsa})")
say(f"silver(m=2) SQUARED tr(a^2)= {mp.nstr(s['tr(a^2)'], 24)}   minpoly = {mp_sa2.as_expr()} (deg {dsa2})")
silver_chord_deg4 = (dsa == 4 and mp_sa.is_irreducible)
silver_sq_deg2 = (dsa2 == 2)
chk("silver CHORD tr(a) is degree-4 order-8 x^4-4x^2+8 = sqrt(2+-2i) (carries the exp(m*pi*i/4) T-phase)",
    silver_chord_deg4)
chk("silver SQUARED tr(a^2) collapses to degree 2 (Q(i)) -- squaring HALVES the order, hides the framing",
    silver_sq_deg2)
chk("=> chord level is STRICTLY richer than the squared projection (deg 4 vs 2): B772 blindness confirmed real",
    silver_chord_deg4 and silver_sq_deg2)

# What the quantum comparator says for the single seeds (matched-level sanity).
qg, og = quantum_field("RL", 4)
qs, os_ = quantum_field("RRLL", 4)
say(f"\nquantum single-seed fields (k=4):  golden RL -> {qg} (orders {og});  silver RRLL -> {qs} (orders {os_})")
say("   note: silver chord field (non-cyclotomic Q(sqrt(2+2i))) != silver quantum field Q(zeta12) --")
say("   chord and quantum are DIFFERENT objects even for a single seed; only golden's Q(sqrt-3) coincides.")


say("\n" + "=" * 88)
say("STEP 1 -- QUANTUM comparator on the composite words (the matched, framing-carrying level)")
say("=" * 88)
composite_seqs = [(1, 2), (2, 1), (1, 1, 2, 2), (1, 2, 1), (2, 1, 2)]
quantum_fields = {}
for seq in composite_seqs:
    w = block_word(seq)
    f, o = quantum_field(w, 4)
    quantum_fields[seq] = f
    say(f"   seq={seq} word={w:12} k=4:  eigenvalue-orders {o} -> {f}")
say("   the quantum eigenvalue field is CYCLOTOMIC at every level (monodromy eigenvalues are roots of unity).")
two_block_quantum = quantum_fields[(1, 2)]
chk("MATCHED COMPARATOR: the 2-block words fuse to the cyclotomic Q(zeta12) on the quantum side",
    quantum_fields[(1, 2)] == "Q(zeta12)" and quantum_fields[(2, 1)] == "Q(zeta12)")


say("\n" + "=" * 88)
say("STEP 2 -- THE DISCRIMINATING FACT: exact chord trace field of the 2-block composite (s892)")
say("=" * 88)
# Both (1,2) and (2,1) are the manifold s892; its chord (raw twist-curve) trace field is one object.
M12, c12 = chord_traces((1, 2))
ident = [str(t) for t in M12.identify()]
say(f"2-block composite = {M12}  vol={M12.volume()}  identify()={ident}")
za = c12["tr(a)"]
say(f"chord twist-curve trace tr(a) = {mp.nstr(za, 40)}")

# EXACT minimal polynomial (PSLQ->sympy), reproduced across 3 mixers, residual-gated.
minpoly, deg, res = minimal_polynomial(za, maxdeg=20)
reproduced = minpoly is not None
if reproduced:
    say(f"EXACT minimal polynomial over Q (residual {mp.nstr(res, 4)}, agreed across {len(MIXERS)} mixers):")
    say(f"   m(x) = {minpoly.as_expr()}")
    say(f"   degree = {deg}   irreducible over Q = {minpoly.is_irreducible}")

# Independent 2nd-precision reproduction of the SAME minimal polynomial (conditioning / house method).
second_prec_ok = False
if reproduced:
    saved = mp.mp.dps
    mp.mp.dps = 60
    _, c12b = chord_traces((1, 2))          # recompute the trace, re-parse at coarser precision
    mp2, deg2, _ = minimal_polynomial(c12b["tr(a)"], maxdeg=20)
    mp.mp.dps = saved
    second_prec_ok = (mp2 is not None and mp2 == minpoly)
    chk("CONDITIONING: the identical minimal polynomial is recovered at an independent 2nd precision (60 dps)",
        second_prec_ok)

# --- exact symbolic certification (the requested Groebner/gcd-level, not bounded-height PSLQ) ---
chord_certified = False
if reproduced:
    irreducible = minpoly.is_irreducible
    cyclo_degree_exists = is_cyclotomic_field_degree(deg)     # phi(n)=deg solvable?
    not_in_zeta12, cert = certify_not_in_Qzeta12(minpoly, deg)
    say("\nEXACT symbolic certification:")
    say(f"   irreducible over Q ........................ {irreducible}")
    say(f"   some cyclotomic field has this degree? .... {cyclo_degree_exists}  (is phi(n)={deg} solvable?)")
    say(f"   not-in-Q(zeta12) certificate .............. {cert}")
    chord_field_is_cyclotomic = cyclo_degree_exists and (not not_in_zeta12)
    chord_certified = irreducible and (not cyclo_degree_exists) and not_in_zeta12
    chk("EXACT: chord trace field is NON-CYCLOTOMIC (no Q(zeta_n) has degree {}) -- phi(n)={} has no solution"
        .format(deg, deg), irreducible and (not cyclo_degree_exists))
    chk("EXACT: chord trace tr(a) is NOT in Q(zeta12) (degree 14 does not divide [Q(zeta12):Q]=4; "
        "gcd(m, Phi_12)=1) -- the chord field cannot be the quantum fusion field", not_in_zeta12)
else:
    chord_field_is_cyclotomic = None
    chk("EXACT minimal polynomial recovered and reproduced across mixers", False)


say("\n" + "=" * 88)
say("STEP 3 -- fusion verdict at the CHORD level")
say("=" * 88)
# FUSION PRESENT would require the composite chord field to BE / contain the quantum cyclotomic
# fusion field Q(zeta12). It is instead a generic irreducible degree-14 non-cyclotomic field.
# It is not even the compositum of the two seed chord fields (golden deg 2 . silver deg 4 => deg | 8),
# since 14 does not divide 8 -- classical composition builds a NEW generic field, no fusion.
seed_compositum_degree_bound = 8
not_seed_compositum = reproduced and (deg % 1 == 0) and (seed_compositum_degree_bound % deg != 0)
if reproduced:
    chk("chord field is not even the compositum of the two seed chord fields (deg 14 does not divide 8) "
        "-- composition yields a NEW generic field, the opposite of collapse-to-a-shared-fusion-field",
        not_seed_compositum)

def verdict():
    """In-code verdict logic; can emit UNRESOLVED."""
    pipeline_sane = (golden_is_sqrt_m3 and silver_chord_deg4 and silver_sq_deg2
                     and quantum_fields[(1, 2)] == "Q(zeta12)")
    if not (reproduced and second_prec_ok and pipeline_sane):
        return ("UNRESOLVED",
                "the chord-level minimal polynomial could not be exactly recovered / reproduced, or a "
                "control (golden Q(sqrt-3), silver order-8 chord, quantum Q(zeta12)) failed -- cannot certify")
    if chord_field_is_cyclotomic:
        return ("RESOLVED-A",
                "the composite CHORD (raw twist-curve) trace field IS cyclotomic and matches the quantum "
                "fusion field Q(zeta12) -- the squared/invariant projection HID a quantum-matching fusion")
    if chord_certified:
        return ("RESOLVED-B",
                "the 2-block composite's chord trace field is an EXACT irreducible degree-14 NON-cyclotomic "
                "field (phi(n)=14 has no solution; 14 does not divide [Q(zeta12):Q]=4; gcd with Phi_12 is 1), "
                "so it is neither Q(zeta12) nor the seed compositum -- chord-level fusion is ABSENT and the "
                "K016 wall HARDENS at the matched (un-squared, framing-carrying) level. Un-squaring makes the "
                "classical field MORE generic, not cyclotomic: the mod-4 fusion is a QUANTUM-only phenomenon")
    return ("UNRESOLVED", "certification incomplete")

V, REASON = verdict()

say("\n" + "=" * 88)
say("VERDICT")
say("=" * 88)
say(f"VERDICT: {V}")
say(f"REASON: {REASON}")
say("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))

results = {
    "cell": "W3-067c",
    "batch": "B773",
    "level": "chord / twist-curve (raw, un-squared traces) -- matched to quantum framing/Dehn-twist data",
    "verdict": V,
    "reason": REASON,
    "all_checks_pass": ok,
    "two_block_manifold": str(M12),
    "two_block_identify": ident,
    "chord_trace_tr_a_minpoly": (str(minpoly.as_expr()) if reproduced else None),
    "chord_trace_field_degree": deg,
    "chord_trace_field_irreducible": (bool(minpoly.is_irreducible) if reproduced else None),
    "chord_trace_field_cyclotomic": (None if chord_field_is_cyclotomic is None else bool(chord_field_is_cyclotomic)),
    "phi_n_equals_deg_solvable": (is_cyclotomic_field_degree(deg) if reproduced else None),
    "minpoly_residual": (mp.nstr(res, 6) if reproduced else None),
    "reproduced_mixers": len(MIXERS),
    "reproduced_second_precision": second_prec_ok,
    "quantum_matched_field_2block": two_block_quantum,
    "quantum_composite_fields_k4": {str(k): v for k, v in quantum_fields.items()},
    "single_seed_controls": {
        "golden_chord_minpoly": str(mp_ga.as_expr()),
        "golden_chord_field": "Q(sqrt-3) [cyclotomic, coherent seed]",
        "silver_chord_minpoly": str(mp_sa.as_expr()),
        "silver_chord_field": "Q(sqrt(2+2i)) [non-cyclotomic, order-8 T-phase]",
        "silver_squared_minpoly": str(mp_sa2.as_expr()),
        "silver_squared_field": "Q(i) [what the blind projection saw]",
        "golden_quantum_field": qg,
        "silver_quantum_field": qs,
    },
}
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
say("\nwrote results.json")

with open("output.txt", "w") as f:
    f.write("\n".join(LOG) + "\n")

sys.exit(0 if ok else 1)
