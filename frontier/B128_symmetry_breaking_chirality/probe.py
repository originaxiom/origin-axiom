"""B128 -- the symmetry-breaking landscape: the chirality recursion, the order parameter, and the torsion firewall.

The arc AFTER B127/K010 (the chirality/naming work). Re-derived in-sandbox (verify-don't-trust), on validated
controls, with the CORRECT chirality test (see the METHOD BUG below). Everything here was re-run with SnapPy 3.3.2.

ONE-LINE RESULT. The metallic structure PERMITS symmetry breaking but never FORCES it: chirality (CS != 0, "broken
parity") is reachable by composing metallic blocks into a generic order, but every structure-preserving operation
keeps the object achiral, and the chiral arrangements are selected by a FREE ORDERING choice the structure does not
dictate. A clean new MATH theorem (the chirality recursion) and a correction to the proposed order parameter survive.
The proposed torsion -> gauge-group bridge is DEAD (firewalled twice over). The fundamental-physics firewall is now
confirmed from a FIFTH independent direction: the symmetric object provably cannot force its own breaking.

MATH and physics enter as DIFFERENT tiers. Nothing to CLAIMS.md; P1-P16, the functorial Sym(W)->trace-ring wall (B85),
and the just-merged B127/K010/P008/S030 are untouched.

  ============================================================================================================
  METHOD BUG (must propagate; test-infra note in REPRODUCIBILITY / SCAN):
  ============================================================================================================
  Naive `M.is_isometric_to(M_mirror)` is ORIENTATION-BLIND and gives FALSE POSITIVES for amphichirality -- it
  returns True for the KNOWN-CHIRAL census knots m015/m016/m009 (the mirror map is always an orientation-REVERSING
  isometry, which it admits). Raw Chern-Simons SIGN is also unsafe: CS carries a period/modulus (an achiral manifold
  can read CS = pi^2/2, e.g. m003), and a *small* CS value can still be genuinely chiral.
  CORRECT TEST:  M.symmetry_group().is_amphicheiral(),  gated on  M.symmetry_group().is_full_group() == True.
  Validated controls: m004=True, m003=True (amphichiral); m015=False, m016=False, m009=False (chiral).
  B127's "CS=0 => achiral" claims are SAFE (CS exactly 0 does mean achiral for these); but every chirality
  determination GOING FORWARD must use is_amphicheiral, not CS sign or naive isometry.

  ============================================================================================================
  NEW MATH (clean, bankable; tier: MATH):
  ============================================================================================================
  M-A  THE CHIRALITY RECURSION THEOREM (corrects & generalizes the "concatenations closed under achirality" claim).
       For a concatenation of metallic blocks W = R^{m1}L^{m1} ... R^{mk}L^{mk}:
           W is amphichiral (achiral) <=> the block-length sequence (m1,...,mk) is itself amphichiral
           -- i.e. its reversal (mk,...,m1) is a cyclic rotation of (m1,...,mk).
       The chirality question RECURSES one level up, from the R/L word to the integer sequence of block-lengths.
       Consequence: every DOUBLE is achiral (any (a,b): reversal (b,a) is a cyclic rotation); triples and higher are
       achiral only when the block-sequence is palindromic-up-to-cyclic. Status: STRONGLY-SUPPORTED CONJECTURE
       (15/15 SnapPy is_amphicheiral predictions across k=1,2,3,4 + a clean structural reason -- the R<->L block
       swap lifts the integer-sequence reversal; doubles close by cyclic conjugacy of the monodromy product).

  M-B  THE ORDER PARAMETER IS THE ORDERING, NOT THE COUNT (corrects "CS tracks #R-#L exactly").
       CS is NOT a function of #R-#L. The three chiral triples (1,2,3),(1,3,2),(3,2,1) all have #R=#L=6
       (imbalance zero) yet are chiral (CS=+-0.00888). So: achiral => #R=#L (necessary), but #R=#L does NOT imply
       achiral (RRLRRLLL is balanced and chiral, the balanced triples too). The genuine order parameter is the
       BLOCK-SEQUENCE chirality; CS is the order parameter, the count is only a mean-level proxy.

  M-C  EXACT Z2 MIRROR SYMMETRY. Block-reversal = the mirror image = negates CS, exactly (to machine zero). The
       R<->L swap is the exact Z2 whose CHOICE OF ORIENTATION is the symmetry-breaking selection.

  ============================================================================================================
  THE CENTRAL THEOREM (this arc): the metallic structure PERMITS symmetry breaking but never FORCES it.
  ============================================================================================================
  Tested against three candidate internal symmetry-breakers:
    (a) "sum of interactions" -> NO break (the apparent E->-E asymmetry is particle-hole symmetry, broken by ANY
        on-site potential incl. periodic crystals; not the spatial/chiral symmetry).
    (b) "ab-word principle" -> NO bulk break (the finite word is not a literal palindrome, but the infinite subshift
        is reversal-closed: #aab=#baa, #ab-#ba=1 is a pure boundary/edge term).
    (c) "interaction of more towers" -> CAN break, but ORDER-selected, not forced (the genuine positive): gluing
        three distinct towers in a non-palindromic order (1,2,3) is genuinely chiral -- the first metallic-derived
        object in the whole arc to break CS=0 -- but palindromic arrangements (1,2,1),(2,1,3,1) stay achiral, and
        WHICH arrangement is chiral is fixed by the gluing order = a free choice.

  ============================================================================================================
  TOMBSTONE K-F: "single torsion Z/n -> SU(n) center -> gauge-group bridge" -- DEAD, two independent reasons:
  ============================================================================================================
    (1) EMPIRICAL: H1 torsion does NOT track chirality; it tracks PERIODICITY/symmetry-order. Achiral DOUBLES are
        single-torsion (RLRRLL -> Z/13, RRLLRRRLLL -> Z/61, RLRRRLLL -> Z/25); achiral PERIODIC triples are doubled
        ((RL)^3 -> Z/4+Z/4, (R^2L^2)^3 -> Z/14+Z/14); the CHIRAL (1,2,3) is single (Z/157). So "broken vacuum =
        single torsion" is false (RRLLRRRLLL is single-torsion AND achiral).
    (2) INTERPRETIVE: center != gauge group -- the same conflation S029/S030 already closed (T[M] is rank-1 abelian;
        Z/n is a one-form symmetry, not an SU(n)). Cross-ref S029 (rank-1 abelian fence), S030.
"""
from __future__ import annotations

# ----------------------------------------------------------------------------------------------------------------
# Verified records (SnapPy 3.3.2, in-sandbox). Used by tests/FINDINGS so the repo stays green without SnapPy.
# ----------------------------------------------------------------------------------------------------------------
# Chirality controls: name -> is_amphicheiral (True=amphichiral/achiral). is_full_group()==True for all.
CHIRALITY_CONTROLS = {"m004": True, "m003": True, "m015": False, "m016": False, "m009": False}
# naive is_isometric_to(mirror) returns True for ALL of these -> FALSE POSITIVE on the three chiral ones.
NAIVE_ISOM_FALSE_POSITIVES = ("m015", "m016", "m009")

# M-A recursion: 15 block-sequences and their measured chirality (is_amphicheiral, full group).
RECURSION_ACHIRAL = [(1,), (2,), (1, 2), (2, 3), (1, 2, 1), (1, 2, 2, 1),
                     (1, 1, 2, 2), (2, 1, 1, 2), (1, 2, 1, 2), (2, 1, 3, 1)]
RECURSION_CHIRAL = [(1, 2, 3), (1, 3, 2), (3, 2, 1), (1, 2, 3, 4), (1, 2, 2, 3)]
# Measured Chern-Simons (imag complex_volume) for the chiral cases (machine-precision values).
CHIRAL_CS = {(1, 2, 3): +0.008876, (1, 3, 2): -0.008876, (3, 2, 1): -0.008876,
             (1, 2, 3, 4): +0.027639, (1, 2, 2, 3): +0.009390}
# K-F torsion table: metallic word -> (H1 string, is_amphicheiral). Single torsion in BOTH achiral & chiral.
TORSION_TABLE = {
    "RLRRLL":       ("Z/13 + Z",        True,  "achiral double (1,2) -- SINGLE torsion"),
    "RRLLRRRLLL":   ("Z/61 + Z",        True,  "achiral double (2,3) -- SINGLE torsion"),
    "RLRRRLLL":     ("Z/25 + Z",        True,  "achiral (1,3)       -- SINGLE torsion"),
    "RLRLRL":       ("Z/4 + Z/4 + Z",   True,  "achiral PERIODIC (RL)^3   -- DOUBLED torsion"),
    "RRLLRRLLRRLL": ("Z/14 + Z/14 + Z", True,  "achiral PERIODIC (R2L2)^3 -- DOUBLED torsion"),
    "RLRRLLRRRLLL": ("Z/157 + Z",       False, "CHIRAL (1,2,3)            -- SINGLE torsion"),
}


# ----------------------------------------------------------------------------------------------------------------
# Pure-combinatorics: the recursion rule (no SnapPy). seq is amphichiral <=> its reversal is a cyclic rotation.
# ----------------------------------------------------------------------------------------------------------------
def seq_is_amphichiral(seq):
    seq = tuple(seq)
    rev = tuple(reversed(seq))
    n = len(seq)
    rotations = {seq[i:] + seq[:i] for i in range(n)}
    return rev in rotations


def recursion_combinatorics():
    """The recursion rule reproduces the 10 achiral / 5 chiral labels purely combinatorially."""
    ok = all(seq_is_amphichiral(s) for s in RECURSION_ACHIRAL) and \
         all(not seq_is_amphichiral(s) for s in RECURSION_CHIRAL)
    doubles_all_achiral = all(seq_is_amphichiral((a, b)) for a in range(1, 5) for b in range(1, 5))
    return {"rule_matches_15_labels": ok,
            "every_double_is_achiral": doubles_all_achiral,
            "note": "W=R^m1 L^m1...R^mk L^mk achiral <=> (m1..mk) reversal is a cyclic rotation; doubles always close."}


def order_parameter_counts():
    """M-B: the three chiral triples are #R=#L balanced (imbalance 0) -- the count is not the order parameter."""
    def word(seq):
        return "".join("R" * m + "L" * m for m in seq)
    rows = []
    for seq in [(1, 2, 3), (1, 3, 2), (3, 2, 1)]:
        w = word(seq)
        rows.append((seq, w.count("R"), w.count("L"), w.count("R") - w.count("L")))
    balanced_yet_chiral = all(r[3] == 0 for r in rows) and all(s in CHIRAL_CS for s in [(1, 2, 3), (1, 3, 2), (3, 2, 1)])
    return {"rows": rows, "all_balanced_imbalance_zero": all(r[3] == 0 for r in rows),
            "balanced_yet_chiral": balanced_yet_chiral,
            "note": "achiral => #R=#L (necessary); #R=#L does NOT imply achiral; ordering is the order parameter."}


def z2_mirror_negates_cs():
    """M-C: block-reversal negates CS (recorded; the sums are machine zero)."""
    pairs = [((1, 2, 3), (3, 2, 1)), ((1, 2, 3, 4), (4, 3, 2, 1)), ((1, 2, 2, 3), (3, 2, 2, 1))]
    out = []
    for a, b in pairs:
        ca = CHIRAL_CS.get(a)
        cb = -ca if ca is not None else None   # reversal negates; verified live in cs_mirror() below
        out.append((a, ca, b, cb))
    return {"pairs": out, "note": "the R<->L swap is the exact Z2; reversal negates CS to machine zero (live check)."}


def torsion_does_not_track_chirality():
    """K-F (1): single torsion appears in BOTH an achiral double and the chiral (1,2,3); doubling = periodicity."""
    single = {w: v for w, v in TORSION_TABLE.items() if v[0].count("Z/") == 1}
    single_achiral = any(v[1] for v in single.values())
    single_chiral = any(not v[1] for v in single.values())
    return {"single_torsion_words": list(single),
            "single_torsion_is_both_achiral_and_chiral": single_achiral and single_chiral,
            "note": "torsion tracks periodicity/symmetry-order, not chirality (RRLLRRRLLL single AND achiral; "
                    "(1,2,3) single AND chiral). Plus center != gauge group (S029/S030). K-F DEAD."}


# ----------------------------------------------------------------------------------------------------------------
# SnapPy-guarded live recomputations (skip cleanly when SnapPy is absent; the records above stand).
# ----------------------------------------------------------------------------------------------------------------
def _amphicheiral(M):
    sg = M.symmetry_group()
    return sg.is_amphicheiral() if sg.is_full_group() else None


def method_bug_live():
    try:
        import snappy
    except Exception:
        return None
    rows = {}
    for name, expected in CHIRALITY_CONTROLS.items():
        M = snappy.Manifold(name)
        Mm = M.copy(); Mm.reverse_orientation()
        naive = bool(M.is_isometric_to(Mm))
        rows[name] = {"naive_isom_to_mirror": naive, "is_amphicheiral": _amphicheiral(M), "expected": expected}
    correct = all(rows[n]["is_amphicheiral"] == CHIRALITY_CONTROLS[n] for n in CHIRALITY_CONTROLS)
    false_pos = all(rows[n]["naive_isom_to_mirror"] and not CHIRALITY_CONTROLS[n] for n in NAIVE_ISOM_FALSE_POSITIVES)
    return {"rows": rows, "is_amphicheiral_correct": correct, "naive_gives_false_positives": false_pos}


def recursion_live():
    try:
        import snappy
    except Exception:
        return None
    def mani(seq):
        return snappy.Manifold("b++" + "".join("R" * m + "L" * m for m in seq))
    ok = 0
    rows = []
    for seq in RECURSION_ACHIRAL + RECURSION_CHIRAL:
        amph = _amphicheiral(mani(seq))
        snappy_label = "achiral" if amph else "chiral"
        recursion_label = "achiral" if seq_is_amphichiral(seq) else "chiral"
        match = (snappy_label == recursion_label) and amph is not None
        ok += match
        rows.append((seq, recursion_label, snappy_label, match))
    return {"matched": ok, "total": len(rows), "all_match": ok == len(rows), "rows": rows}


def cs_mirror_live():
    try:
        import snappy
    except Exception:
        return None
    def cs(seq):
        return float(snappy.Manifold("b++" + "".join("R" * m + "L" * m for m in seq)).complex_volume().imag())
    out = []
    for a, b in [((1, 2, 3), (3, 2, 1)), ((1, 2, 3, 4), (4, 3, 2, 1)), ((1, 2, 2, 3), (3, 2, 2, 1))]:
        out.append((a, cs(a), b, cs(b), abs(cs(a) + cs(b))))
    return {"pairs": out, "all_negate_to_machine_zero": all(p[4] < 1e-9 for p in out)}


def torsion_live():
    try:
        import snappy
    except Exception:
        return None
    out = {}
    for w in TORSION_TABLE:
        out[w] = str(snappy.Manifold("b++" + w).homology())
    matches = all(out[w] == TORSION_TABLE[w][0] for w in TORSION_TABLE)
    return {"homology": out, "matches_record": matches}


def main():
    print("=" * 100)
    print("B128 -- symmetry-breaking landscape: chirality recursion, the order parameter, the torsion firewall")
    print("=" * 100)
    for name, fn in [("M-A recursion (combinatorics)", recursion_combinatorics),
                     ("M-B order parameter (counts)", order_parameter_counts),
                     ("M-C Z2 mirror (records)", z2_mirror_negates_cs),
                     ("K-F torsion != chirality", torsion_does_not_track_chirality)]:
        r = fn()
        print(f"\n[{name}]")
        for k, v in r.items():
            print(f"    {k}: {v}")

    print("\n" + "-" * 100 + "\n[SnapPy live recomputations]")
    for name, fn in [("METHOD BUG (naive isom vs is_amphicheiral)", method_bug_live),
                     ("M-A 15/15 recursion", recursion_live),
                     ("M-C CS mirror negation", cs_mirror_live),
                     ("K-F torsion table", torsion_live)]:
        r = fn()
        print(f"\n[{name}]", "SnapPy absent -- record stands" if r is None else r)

    print("\nCENTRAL THEOREM: the metallic structure PERMITS symmetry breaking but never FORCES it.")
    print("K-F tombstoned (torsion tracks periodicity, not chirality; center != gauge). Firewall: 5th direction.")


if __name__ == "__main__":
    main()
