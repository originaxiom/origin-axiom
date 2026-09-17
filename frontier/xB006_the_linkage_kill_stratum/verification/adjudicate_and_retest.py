#!/usr/bin/env python3
"""xB006 cells S2b and S3 - the HAND ADJUDICATION of S2's raw candidates, and the
re-test of the primary one, exactly as sealed in PREREGISTRATION.md (sha256 94b1f14c...,
commit 504d6bd, pushed BEFORE any of this existed).

S2's regex returns 30 arcs on the sealed lexicon.  REPORTING 30 AS THE ANSWER WOULD BE
THE VERY OVER-REACH THIS ARC AUDITS.  Every one is read and adjudicated here, with its
reason recorded, and the count that matters is the adjudicated one.

Each cell asserts its own mathematics.  Gate 5 untouched.
"""
import itertools
import sys
import warnings

import snappy

warnings.filterwarnings("ignore")

# --- S2b: every raw candidate, read and adjudicated -------------------------------------
# BASE_RATE   the "not evidence" is a base-rate / look-elsewhere argument WITH the rate
#             computed -- a different and sound kind of argument
# LINK_NAMED  the link IS supplied (a definition, a named theorem, a specific named fact);
#             S2's 600-char window missed it
# NOT_A_KILL  the phrase sits in a PROVED arc's convergence or description, doing no kill work
# PROSE       ordinary English use of "one fact" / "not evidence"
# MODEL       the arc TESTED its own linkage assumption -- the behaviour E82 asks for
# E82         no link exhibited, and the sameness does evidential work in a kill
ADJUDICATION = {
 "B1006_lambda2_pslq":              ("BASE_RATE",  "'absence of evidence, not evidence of absence' -- a PSLQ exclusion-power argument with the digit envelope computed"),
 "B1009_verification_pass":         ("BASE_RATE",  "'reaching E6 is not evidence IF a third of entry points reach E6 too' -- rate cited from B993/B996; and the arc is WITHDRAWING an overreach, not making one"),
 "B1035_receipts_and_register":     ("PROSE",      "'massive neutrinos are not evidence for nu_R' -- a physics clause in the falsifier register, no sameness claimed"),
 "B1096_anomaly_layer":             ("E82",        "'completeness of content and emptiness of layer are THE SAME FACT' -- a reason is offered ('a layer that vanishes identically cannot supply a ratio') but no map between the two statements; SECONDARY candidate"),
 "B1146_seam_b":                    ("NOT_A_KILL", "'SEAM-B is the same fact seen head-on' -- a cross-bench convergence note in a PROVED arc"),
 "B1208_cross_seat_harvest":        ("LINK_NAMED", "'the same fact seen from the covering's definition' -- the link IS the definition of the orientation double cover, and the arc says so"),
 "B1222_symmetry_vanishing_thesis": ("BASE_RATE",  "'65 vanishings are a real pattern; they are not evidence for the first story that explains them' -- a methodological point, and the arc declared its kill conditions in advance and met them"),
 "B1223_triality_correspondence":   ("MODEL",      "'the value of a small-group coincidence is not zero, but it is not evidence, and the difference is one computation: check whether the action matches' -- this IS the discriminator E82 restates"),
 "B1234_a6_built_the_walls":        ("BASE_RATE",  "'surjecting onto 2T is generic at ~1/3, so the equal counts are not evidence of distinction' -- the rate is computed"),
 "B1239_quarter_class_is_cusp_local":("PROSE",     "'re-graded from one fact read in CGHN p.14' -- ordinary English"),
 "B1244_gate5_audit":               ("BASE_RATE",  "'two scales in one decade is not evidence, the base-rate discipline covers this shape' -- explicitly pre-dismissed at zero weight"),
 "B1276_legs_are_faces":            ("LINK_NAMED", "'two derivations of one fact, from arithmetic and from representation theory' -- BOTH derivations are named and given"),
 "B1340_the_joker_priced":          ("BASE_RATE",  "'anomaly-free on the 19624 vacua is not evidence; the check cannot fail' -- a VACUITY finding, computed (all six coefficients vanish identically as polynomials)"),
 "B1346_the_chat1_handoff_intake":  ("LINK_NAMED", "'predicted by B1297's own theorem -- a confirmation, not evidence' -- the theorem is named"),
 "B142_klein4_and_magic_cartography":("E82",       "'the kappa equality is the S_3 cusp symmetry restated (automatic), not independent evidence' -- S_3 is named but the restatement is not exhibited; SECONDARY candidate. NOTE its decisive arm is elsewhere (trace field Q(sqrt-7) or Q(i), not Q(sqrt-3)), so the kill does not rest on this line"),
 "B146_b145_calibration":           ("E82",        "'the near-tautological volume-minimality / palindromic-period arms (ONE FACT: short word ~ low volume ~ palindromic period)' -- three properties chained by '~' with no map, and the 'near-tautological' is the evidential downgrade. PRIMARY candidate: re-tested in S3"),
 "B333_compositum_seam":            ("LINK_NAMED", "'tautological (it is WHY sqrt-15 is the compositum's third subfield; it carries no new information)' -- the link is the definition of the compositum"),
 "B414_generation_structure":       ("BASE_RATE",  "'every nontrivial object has small cyclic subgroups; a 3-2 presence is a HOOK, not evidence'"),
 "B559_blackhole_probes":           ("LINK_NAMED", "'CS = 0 for the figure-eight IS its amphichirality' -- a theorem, and the section is flagged HINT and firewalled"),
 "B572_eleven_clauses":             ("PROSE",      "'the SnapPy-generator convention of the same fact' -- a convention restatement, named as such"),
 "B660_structure_campaign":         ("LINK_NAMED", "'FORCED A PRIORI (integer-polynomial invariants are Galois-stable); the C-orbit match carries no information' -- the theorem is named"),
 "B687_sm_atlas_koide":             ("BASE_RATE",  "22 of 23 invariants graded unreachable or base-rate-dead; the h(27)=2/3 match is explicitly not evidence"),
 "B703_koide_sigma_distance":       ("BASE_RATE",  "'NOT evidence: not derived, convention-framed, a post-hoc fit atop a tautology' -- the arc names its own fit as post-hoc"),
 "B706_rung2_sm_freedom":           ("LINK_NAMED", "'FIELD MISMATCH -- 9/40 is in Q, it does NOT use sqrt5' -- a specific named reason, and the arc says the base rate is NOT the kill"),
 "B724_seeing_readjudication":      ("BASE_RATE",  "torsion-spectrum density computed (~2.3 signed-combos/decade), so a factor-3 near-hit is EXPECTED"),
 "B772_negatives_adequacy":         ("MODEL",      "'we are NOT re-confirming one fact many times (MY HYPOTHESIS WAS WRONG: 12/14 negatives are object-native and genuinely seam-independent)' -- the arc TESTED its own linkage hypothesis and refuted it"),
 "B808_empty_cells":                ("BASE_RATE",  "multiple comparisons: 3.5 expected below threshold by chance, 1 observed"),
 "B978_phaseA_bank":                ("LINK_NAMED", "'it is the SAME fact (omega_1 not in Q)' -- the shared fact is named explicitly"),
 "B986_b500_stragglers":            ("PROSE",      "'(a proof, not evidence)' -- the arc is saying its argument IS a proof"),
 "B995_separating_and_rare":        ("MODEL",      "'RARE AND SEPARATING ARE NOT INDEPENDENT -- for population rate r the chance all five differ is about (1-r)^5' -- the dependence is COMPUTED, and it voids the arc's own instrument"),
}


def S2b(raw_names):
    missing = set(raw_names) - set(ADJUDICATION)
    extra = set(ADJUDICATION) - set(raw_names)
    assert not missing, f"S2 returned arcs this adjudication does not cover: {sorted(missing)}"
    assert not extra, f"adjudication covers arcs S2 did not return: {sorted(extra)}"
    counts = {}
    for k, (cls, _) in ADJUDICATION.items():
        counts[cls] = counts.get(cls, 0) + 1
    print(f"S2b      every one of S2's {len(raw_names)} raw candidates read and adjudicated")
    for cls in ("BASE_RATE", "LINK_NAMED", "PROSE", "NOT_A_KILL", "MODEL", "E82"):
        n = counts.get(cls, 0)
        note = {"BASE_RATE": "a base-rate / look-elsewhere argument, WITH the rate computed",
                "LINK_NAMED": "the link IS supplied; S2's window missed it",
                "PROSE": "ordinary English, no sameness claimed",
                "NOT_A_KILL": "the phrase does no kill work",
                "MODEL": "the arc TESTED its own linkage assumption -- the behaviour E82 asks for",
                "E82": "NO LINK EXHIBITED, and the sameness does evidential work"}[cls]
        print(f"           {cls:<11} {n:>3}   {note}")
    e82 = sorted(k for k, (c, _) in ADJUDICATION.items() if c == "E82")
    print(f"\n         ADJUDICATED E82 CANDIDATES: {len(e82)}")
    for k in e82:
        print(f"           {k}\n             {ADJUDICATION[k][1]}")
    assert len(e82) >= 1, "OUTCOME B: no adjudicated candidate -- E82 is not a class"
    assert len(e82) <= 8, "beyond the sealed prior's range 1-8; report that, do not hide it"
    print(f"\nS2b PASS |C_adjudicated| = {len(e82)}, inside the SEALED PRIOR's range 1-8.")
    print("         The raw 30 was instrument over-firing, not 30 wrong kills. Reporting 30")
    print("         would have been the exact over-reach this arc audits.")
    return e82


# --- S3: the primary candidate, re-tested -----------------------------------------------
def cyclic_words(nmax):
    out = []
    for n in range(2, nmax + 1):
        for t in itertools.product('LR', repeat=n):
            w = ''.join(t)
            if 'L' not in w or 'R' not in w:
                continue
            if min(w[i:] + w[:i] for i in range(n)) == w:
                out.append(w)
    return out


def is_palindromic(w):
    """cyclically palindromic: some rotation of w equals its reverse."""
    r = w[::-1]
    return any(w[i:] + w[:i] == r for i in range(len(w)))


def S3(nmax=9):
    """B146: 'the near-tautological volume-minimality / palindromic-period arms
    (ONE FACT: short word ~ low volume ~ palindromic period)'.  Are they one fact?"""
    rows = [(w, len(w), float(snappy.Manifold('b++' + w).volume()), is_palindromic(w))
            for w in cyclic_words(nmax)]
    print(f"\nS3       B146's chain re-tested on {len(rows)} once-punctured-torus bundles"
          f" (words of length 2..{nmax})")

    # (i) short word ~ low volume ?
    inv = [(a, b) for a in rows for b in rows if a[1] < b[1] and a[2] > b[2]]
    print(f"\n         (i) 'short word ~ low volume': {len(inv)} pairs where the SHORTER word has"
          f" the LARGER volume")
    a, b = min(inv, key=lambda p: p[0][1])
    print(f"             e.g. |{a[0]}| = {a[1]}, vol {a[2]:.4f}   >   |{b[0]}| = {b[1]},"
          f" vol {b[2]:.4f}")
    assert inv, "no inversion: word length really does order volume"

    # (ii) does word length carry volume information at all?
    print(f"\n         (ii) volume spread WITHIN a fixed word length:")
    spreads = []
    for n in range(4, nmax + 1):
        same = [r for r in rows if r[1] == n]
        lo, hi = min(r[2] for r in same), max(r[2] for r in same)
        spreads.append(hi/lo)
        print(f"             length {n}: {len(same):>3} bundles, vol {lo:.4f} .. {hi:.4f}"
              f"  (ratio {hi/lo:.2f}x)")
    assert max(spreads) > 2.0, "volume is nearly determined by length after all"

    # (iii) low volume ~ palindromic ?
    pal = [r for r in rows if r[3]]
    npal = [r for r in rows if not r[3]]
    cross = [(x, y) for x in npal for y in pal if x[2] < y[2]]
    print(f"\n         (iii) 'low volume ~ palindromic': {len(pal)} palindromic,"
          f" {len(npal)} not; {len(cross)} pairs where a NON-palindromic bundle has")
    print(f"              LOWER volume than a palindromic one"
          f"  (e.g. {cross[0][0][0]} at {cross[0][0][2]:.4f} < {cross[0][1][0]} at"
          f" {cross[0][1][2]:.4f})")
    assert cross

    print("\n         => the three are NOT one fact. The chain B146 wrote is FALSE AS STATED.")

    # (iv) ...BUT the extremal regime, which is where B146 applies it.  The honest half.
    lo12 = sorted(rows, key=lambda r: r[2])[:12]
    print(f"\n         (iv) AND NOW THE OTHER HALF, which the headline must carry: at the BOTTOM")
    print(f"              of the volume spectrum the coupling is REAL and it is STRUCTURAL.")
    print(f"              lowest palindromic volume     : {min(r[2] for r in pal):.4f}")
    print(f"              lowest NON-palindromic volume : {min(r[2] for r in npal):.4f}")
    assert all(r[3] for r in lo12), "a non-palindromic bundle is among the 12 lowest volumes"
    print(f"              all 12 lowest-volume bundles are palindromic: True")
    mono = []
    for n in range(2, nmax + 1):
        same = [r for r in rows if r[1] == n]
        m = min(same, key=lambda r: r[2])
        mono.append((n, m[0], m[2], m[3]))
    print(f"\n              and the volume MINIMISER at each length is the MONOTONE word:")
    for n, w, v, p in mono:
        assert w in ('L'*(n-1) + 'R', 'L' + 'R'*(n-1)), (n, w)
        assert p, (w, "monotone word not palindromic")
        print(f"                length {n}: {w:<10} vol {v:.4f}   palindromic: {p}")
    print("\n              L^(n-1)R reversed is R L^(n-1), a rotation of itself -- so it is")
    print("              CYCLICALLY PALINDROMIC BY INSPECTION. That is the map B146 never wrote.")
    print("\nS3 PASS  B146's KILL SURVIVES, and its missing link is now supplied. What is")
    print("         corrected is the JUSTIFICATION: the three are not one fact in general")
    print("         (i-iii), but volume-minimality DOES force palindromicity in the extremal")
    print("         regime where B146 applies it, via the explicit monotone family (iv).")
    print("         A scoping note, not a revival. Reported to cc; nothing retracted here.")


if __name__ == "__main__":
    sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
    import linkage_sweep as LS
    raw = []
    for name, d, txt in LS.arcs():
        if not LS.is_kill(d, txt):
            continue
        hits, k, _ = LS.classify(name, d, txt)
        if hits and k == "C":
            raw.append(name)
    S2b(raw)
    S3()
    print("\nVERIFIED")
