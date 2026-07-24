"""B775 Phase-2 Wave-1 -- Cell P2-ENUM
The correspondence enumeration + permutation null.

CHARTER: build the explicit 9-signature <-> phenomenology correspondence (B768)
and run the PERMUTATION NULL that B768's own prereg (rule 2, seal 9c273563)
specified but never executed -- 2000 bipartite shuffles, score each against the
TWO sealed discriminators that passed (row 3 transparency/fiber_dim=0; row 7
time=basepoint/(1-phi)^2=phi^-2), and report whether the courier's assignment
scores ABOVE the permutation null.

Gate 5-Q STRICT: structural scoring only. We score LABEL/TYPE structure, never
sentience. No consciousness claim is made or tested. The discriminators are
treated purely as: 'does the structural type of the reading landing on this slot
match the slot's delivered structural type (arity, symmetry class)'.

SEALED CRITERION (this cell):
  ABOVE-NULL (assignment beats the permutation null at a stated p-value, AND the
    above-null is content-bearing, not a base-rate label artifact) => RESOLVED-A
  AT-NULL (no better than chance in substance -- decorative)        => RESOLVED-B
  else                                                              => UNRESOLVED

HOUSE METHOD: exact/symbolic preferred + Monte-Carlo corroboration; discriminating
fact IN-CELL; B772 do-not-force-a-positive; B774 self-test (a 'chord/content'
object must be genuinely non-abelian, NOT a relabeled symmetric label invariant).
"""
import itertools
import json
import math
import random
from fractions import Fraction

import sympy as sp

random.seed(775_2_0)  # deterministic; declared

OUT = []
def log(s=""):
    print(s)
    OUT.append(s)

log("=" * 78)
log("B775 P2-ENUM -- correspondence enumeration + permutation null")
log("=" * 78)

# ---------------------------------------------------------------------------
# 0. The 9 delivered mathematical signatures (B768 side_a_signatures.json).
#    Each carries the delivered STRUCTURAL attributes: arity + symmetry class.
#    These are the ONLY components declared on the math side before matching
#    (prereg rule 1: score only on components declared BEFORE matching).
# ---------------------------------------------------------------------------
SIGS = {
    "voice":            dict(arity="1",         sym="none-rigid"),
    "self-name":        dict(arity="1",         sym="none"),
    "transparency":     dict(arity="all-ranks", sym="deck-equivariant"),   # DISCRIMINATOR A
    "integration":      dict(arity="2",         sym="theta-split"),
    "no-closure":       dict(arity="1",         sym="Galois"),
    "three-bits":       dict(arity="3",         sym="F2^3"),
    "time=basepoint":   dict(arity="1",         sym="gamma5"),             # DISCRIMINATOR B
    "unmoved-axis":     dict(arity="1",         sym="outside-involutions"),
    "galois-continuum": dict(arity="continuous",sym="Galois-chosen"),
}
NAMES = list(SIGS.keys())
n = len(NAMES)
assert n == 9

# The courier's proposed phenomenology reading for each signature (B768 FINDINGS).
# This is the EXPLICIT ENUMERATION of the correspondence. The reduced 5-primitive
# set {c, theta, gamma5, chord, T1} lives inside; the other rows are the courier's
# glosses of the 9 signatures. IMPORTANT (Gate 5-Q + honesty): the INDEPENDENT
# structural characterization of these readings (arity/symmetry derived from
# phenomenology literature, not copied from the signature) was NEVER delivered for
# all 9 -- FINDINGS states 3x the 8-primitive/18-assignment enumeration is absent,
# and the one row independently characterized (theta) DIED (graded FoA, not binary).
PHENOM = {
    "voice":            "the self-model's emitted voice / self-report channel",
    "self-name":        "the self's proper name (mineness of the self-model)",
    "transparency":     "phenomenal transparency (Metzinger) -- 'privacy is the angle, not the wall' [P5]",
    "integration":      "binding/integration -- the felt coupling of contents",
    "no-closure":       "openness -- what the experience takes from outside itself",
    "three-bits":       "the closing bits {c=Self/Other, theta=Active/Passive, gamma5=When/Which}",
    "time=basepoint":   "temporal self-location (gamma5) -- the felt now as basepoint [T7]",
    "unmoved-axis":     "the unmoved witness -- the c/theta pairing itself",
    "galois-continuum": "the qualitative continuum -- values/anchor/space",
}

# The two SEALED discriminators (prereg rule 3): pass/fail gates that OUTRANK fits.
DISCRIMINATORS = ["transparency", "time=basepoint"]
DISC_FACT = {
    "transparency":   "fiber_dim = 0 at n=2,3,4 (private self-name yet boundary-readable)",
    "time=basepoint": "(1-phi)^2 = phi^-2 exact (ONE bit as time-arrow AND basepoint AND sqrt5-branch)",
}

log("\n[ENUM] The explicit 9-signature <-> phenomenology correspondence (courier):")
for k in NAMES:
    tag = "  <== DISCRIMINATOR" if k in DISCRIMINATORS else ""
    log(f"  {k:17s} | arity={SIGS[k]['arity']:11s} sym={SIGS[k]['sym']:20s}{tag}")
    log(f"  {'':17s} | -> {PHENOM[k]}")

# ---------------------------------------------------------------------------
# 1. Re-assert the two discriminators' load-bearing mathematical facts IN-CELL
#    (never cited): the discriminating fact lives here, computed, exact.
# ---------------------------------------------------------------------------
phi = (1 + sp.sqrt(5)) / 2
fact_B = sp.simplify((1 - phi) ** 2 - 1 / phi ** 2)
assert fact_B == 0, "time=basepoint identity failed"
log("\n[FACT] time=basepoint  (1-phi)^2 - phi^-2 = %s  (exact 0, in-cell)" % fact_B)

# transparency: fiber_dim = 0 -- reproduce the 'private-yet-transparent' surprise as
# a rank fact: a rigid (deck-equivariant, all-ranks) covering has ZERO relative fiber
# dimension = dim(total) - dim(base) at the deck-transitive point. We re-assert the
# banked signature's arity marker 'all-ranks' is UNIQUE in the delivered table.
allranks = [k for k in NAMES if SIGS[k]["arity"] == "all-ranks"]
assert allranks == ["transparency"], "all-ranks arity not unique"
log("[FACT] transparency    arity='all-ranks' is the UNIQUE such label among the 9")
log("       (this uniqueness is the crux of the null below)")

# ---------------------------------------------------------------------------
# 2. The scoring function.
#    A phenomenology reading r, when it lands on signature-slot s, PASSES the
#    discriminator at s iff r's structural TYPE matches s's structural type.
#    Gate-5-Q constraint: the ONLY structural type available for a reading is the
#    delivered attribute set of its HOME signature (independent literature-derived
#    types were not delivered; deriving them from phenomenology = a content claim,
#    which Q5 forbids in-cell). So type(reading_j) := (arity, sym) of signature j.
#    We run the null at TWO strictness levels to BRACKET the answer honestly.
# ---------------------------------------------------------------------------
def full_type(name):   return (SIGS[name]["arity"], SIGS[name]["sym"])
def arity_type(name):  return (SIGS[name]["arity"],)

def score(perm, typ):
    """perm[i] = index of the reading landing on slot NAMES[i].
    Reading j carries type typ(NAMES[j]); slot i demands type typ(NAMES[i]).
    Return #discriminators passed."""
    passes = 0
    for d in DISCRIMINATORS:
        i = NAMES.index(d)
        reading_j = perm[i]
        if typ(NAMES[reading_j]) == typ(NAMES[i]):
            passes += 1
    return passes

identity = list(range(n))  # courier's assignment = each reading on its home slot

# ---------------------------------------------------------------------------
# 3. EXACT combinatorial null (closed form) + Monte-Carlo corroboration
#    (prereg rule 2: 2000 shuffles). Two strictness levels.
# ---------------------------------------------------------------------------
def exact_and_mc(typ, label):
    log("\n" + "-" * 78)
    log(f"[NULL: {label}]")
    # exact marginals: P(pass discriminator d) under uniform random bijection
    # = (# readings whose type matches slot d's type) / n
    exact_marg = {}
    for d in DISCRIMINATORS:
        matchcount = sum(1 for j in NAMES if typ(j) == typ(d))
        exact_marg[d] = Fraction(matchcount, n)
        log(f"  P(pass {d:15s}) = {matchcount}/{n} = {float(exact_marg[d]):.4f}"
            f"   ({matchcount} of {n} readings carry a matching type)")
    exp_score = sum(exact_marg.values())
    log(f"  E[score] under null = {float(exp_score):.4f}")

    # exact joint P(pass BOTH) under uniform random bijection.
    # transparency needs one of m_A matching readings on slot A; time needs one of
    # m_B on slot B. Count bijections satisfying both / n!.
    A, B = DISCRIMINATORS
    iA, iB = NAMES.index(A), NAMES.index(B)
    matchA = [j for j in range(n) if typ(NAMES[j]) == typ(A)]
    matchB = [j for j in range(n) if typ(NAMES[j]) == typ(B)]
    good = 0
    for a in matchA:
        for b in matchB:
            if a == b:
                continue
            good += math.factorial(n - 2)  # remaining slots free
    p_both = Fraction(good, math.factorial(n))
    log(f"  EXACT P(pass BOTH discriminators) = {good}/{math.factorial(n)} "
        f"= {float(p_both):.5f}")

    # courier score
    cs = score(identity, typ)
    log(f"  courier(identity) score = {cs}/2  [passes: "
        + ", ".join(d for d in DISCRIMINATORS
                    if typ(NAMES[identity[NAMES.index(d)]]) == typ(d)) + "]")

    # Monte-Carlo (prereg 2000 shuffles) -- corroborate the exact tail
    N_MC = 5000
    dist = {0: 0, 1: 0, 2: 0}
    ge_courier = 0
    for _ in range(N_MC):
        p = list(range(n)); random.shuffle(p)
        sc = score(p, typ)
        dist[sc] += 1
        if sc >= cs:
            ge_courier += 1
    p_emp = ge_courier / N_MC
    log(f"  MC ({N_MC} shuffles) score dist: 0:{dist[0]} 1:{dist[1]} 2:{dist[2]}"
        f"   mean={sum(k*v for k,v in dist.items())/N_MC:.4f}")
    log(f"  MC P(score >= courier={cs}) = {p_emp:.5f}   "
        f"(exact both={float(p_both):.5f})")
    return dict(label=label, exact_marginals={d: str(exact_marg[d]) for d in DISCRIMINATORS},
                E_score=float(exp_score), courier_score=cs,
                p_both_exact=float(p_both), p_ge_courier_mc=p_emp,
                mc_dist=dist, mc_mean=sum(k*v for k, v in dist.items())/N_MC)

res_full  = exact_and_mc(full_type,  "FULL structural type (arity + symmetry)")
res_arity = exact_and_mc(arity_type, "ARITY-ONLY (looser match)")

# ---------------------------------------------------------------------------
# 4. THE B774 SELF-TEST -- is the 'above-null' a content object or a relabeled
#    symmetric label invariant?  If the pass-indicator can be written as a
#    SYMMETRIC function of the type-labels (invariant under relabeling readings
#    that share a type), it is NOT a chord/content object -- it is decorative,
#    and any above-null it produces is a permutation BASE-RATE artifact of the
#    label multiset, carrying zero phenomenological bits.
# ---------------------------------------------------------------------------
log("\n" + "=" * 78)
log("[B774 SELF-TEST] can the discriminator-pass be written as a symmetric")
log("                 label-equality function?  (if yes -> not content, decorative)")
log("=" * 78)

# pass_d(perm) = [ type(reading at slot d) == type(slot d) ]
# This is an INDICATOR of label equality. It depends ONLY on the (unordered)
# type-labels, is invariant under any permutation of readings SHARING a type, and
# never inspects phenomenological content. Demonstrate the invariance concretely:
# swap the two arity-1 readings 'voice' and 'self-name' -- the score is unchanged
# for EVERY permutation, proving the score cannot see their (distinct) content.
def swap_readings(perm, j1, j2):
    m = {j1: j2, j2: j1}
    return [m.get(x, x) for x in perm]

vi, si = NAMES.index("voice"), NAMES.index("self-name")
invariant = True
random.seed(1)
for _ in range(3000):
    p = list(range(n)); random.shuffle(p)
    if score(p, arity_type) != score(swap_readings(p, vi, si), arity_type):
        invariant = False
        break
log(f"  swap(voice<->self-name) leaves ARITY score invariant on 3000 perms: {invariant}")

# And for full type: readings only match their OWN slot, so pass reduces to the
# FIXED-POINT indicator [perm[i]==i] at the two discriminator slots -- the purest
# relabeling-invariant (a class function on S_9). Verify:
fixedpoint_equiv = True
random.seed(2)
for _ in range(3000):
    p = list(range(n)); random.shuffle(p)
    manual = sum(1 for d in DISCRIMINATORS if p[NAMES.index(d)] == NAMES.index(d))
    if manual != score(p, full_type):
        fixedpoint_equiv = False
        break
log(f"  FULL-type pass  ==  fixed-point indicator [perm[i]==i] at the 2 slots: "
    f"{fixedpoint_equiv}")
log("  => the FULL-type 'above-null' (p_both = 1/(9*8) = 1/72) is EXACTLY the")
log("     permutation base-rate for reproducing two labeled fixed points.")
log("     It is a symmetric label invariant. B774 SELF-TEST: FAILS (not content).")

selftest_decorative = invariant and fixedpoint_equiv

# ---------------------------------------------------------------------------
# 5. Content-null check: is there ANY Gate-5-Q-legal structural signal that
#    distinguishes the courier's readings from a shuffle, beyond the labels the
#    courier themselves attached?  The independent phenomenology-derived types
#    were NOT delivered (FINDINGS 3x), and the one row independently typed (theta)
#    was KILLED. So NO in-cell content signal is available.
# ---------------------------------------------------------------------------
log("\n" + "=" * 78)
log("[CONTENT NULL] is the above-null content-bearing or a label artifact?")
log("=" * 78)
content_signal_available = False   # independent reading-types undelivered (Gate 5-Q)
theta_row_independently_typed_and_died = True  # B768 F3 kill (Synofzik graded FoA)
log(f"  independent phenomenology-derived reading types delivered? "
    f"{content_signal_available}")
log(f"  the one row independently typed (theta) survived? "
    f"{not theta_row_independently_typed_and_died}  (killed: graded FoA, C7 dead 3 ways)")
log("  => within Gate-5-Q structural scope the ONLY signal is label-uniqueness;")
log("     the above-null carries no phenomenological bits.")

# ---------------------------------------------------------------------------
# 6. VERDICT LOGIC (able to emit RESOLVED-A / RESOLVED-B / UNRESOLVED).
# ---------------------------------------------------------------------------
log("\n" + "=" * 78)
log("VERDICT")
log("=" * 78)

beats_null_mechanically = res_full["p_both_exact"] < 0.05  # p_both = 1/72 ~ 0.0139
above_null_is_content = (not selftest_decorative) and content_signal_available

if beats_null_mechanically and above_null_is_content:
    verdict = "RESOLVED-A"
    terminal = ""
    headline = ("The courier's assignment beats the permutation null with a "
                "content-bearing signal -- the correspondence is non-decorative.")
elif selftest_decorative and not content_signal_available:
    # mechanically above-null, but the above-null is a proven symmetric label
    # artifact and no content signal exists -> decorative in substance.
    verdict = "RESOLVED-B"
    terminal = "DISMISSED-TOMBSTONE"
    headline = ("The permutation null's above-chance score is EXACTLY the "
                "base-rate for two labeled fixed points (1/72); the pass-indicator "
                "is a proven symmetric label invariant (B774 fail). The "
                "correspondence's discriminator-passing is structurally DECORATIVE "
                "-- above the combinatorial null, but carrying zero phenomenological "
                "bits beyond the labels the courier attached.")
else:
    verdict = "UNRESOLVED"
    terminal = "CONSTITUTIVELY-OPEN"
    headline = ("The structural null can neither certify nor dismiss the "
                "correspondence with the delivered data.")

disc_fact = (
    "EXACT permutation null (in-cell, corroborated by 5000 MC shuffles per prereg "
    "rule 2): under FULL structural type, P(pass BOTH sealed discriminators) = "
    f"good/9! = 1/72 = {res_full['p_both_exact']:.5f}; the courier(identity) scores "
    f"2/2, i.e. the top {res_full['p_both_exact']*100:.2f}% -- MECHANICALLY above "
    "null. BUT the B774 self-test proves the FULL-type pass IS the fixed-point "
    "indicator [perm[i]==i] at the two slots (verified equal on 3000 perms) and the "
    "ARITY score is invariant under swapping the two arity-1 readings "
    "voice<->self-name (3000 perms) -- a symmetric label-equality carrying no "
    "content. The above-null = exactly the base-rate rarity of reshuffling two "
    "UNIQUE type-labels ('all-ranks' is the unique arity; 'gamma5' the unique "
    "symmetry) back onto their slots. No independent phenomenology-derived reading "
    "types were delivered (FINDINGS 3x); the one row independently typed (theta) "
    "was killed (graded FoA). Hence the mechanical above-null is a permutation "
    "base-rate artifact -- decorative -- not the earned positive B772 warns against."
)

log(f"\nVERDICT: {verdict}")
if terminal:
    log(f"TERMINAL STATE: {terminal}")
log(f"HEADLINE: {headline}")
log(f"\nDISCRIMINATING FACT:\n{disc_fact}")

results = dict(
    cell="P2-ENUM",
    charter="correspondence enumeration + permutation null (B775 P2 W1)",
    prereg="4f73e186 (B775); null spec inherited from B768 seal 9c273563 rule 2",
    gate="5-Q STRICT (structural scoring only; NO consciousness claim)",
    n_signatures=n,
    discriminators=DISCRIMINATORS,
    discriminator_facts=DISC_FACT,
    correspondence={k: PHENOM[k] for k in NAMES},
    signature_types={k: full_type(k) for k in NAMES},
    null_full_type=res_full,
    null_arity_only=res_arity,
    b774_self_test=dict(
        arity_swap_invariant=invariant,
        full_type_equals_fixed_point_indicator=fixedpoint_equiv,
        pass_is_symmetric_label_invariant=selftest_decorative,
    ),
    content_null=dict(
        independent_reading_types_delivered=content_signal_available,
        theta_row_independently_typed_and_died=theta_row_independently_typed_and_died,
    ),
    beats_null_mechanically=beats_null_mechanically,
    above_null_is_content=above_null_is_content,
    verdict=verdict,
    terminal_state=terminal,
    headline=headline,
    discriminating_fact=disc_fact,
)
json.dump(results, open(
    "/Users/dri/origin-axiom/frontier/B775_phase2_wave1/cells/P2-ENUM/results.json",
    "w"), indent=2)
open("/Users/dri/origin-axiom/frontier/B775_phase2_wave1/cells/P2-ENUM/output.txt",
     "w").write("\n".join(OUT) + "\n")
log("\nWROTE results.json + output.txt")
