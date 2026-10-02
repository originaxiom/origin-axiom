#!/usr/bin/env python3
"""THE EARLY RECORD, INDEXED BY SUBJECT (Foundation Lock, Stage 1; WORKING_RULES, the rule of 2026-10-02).

A keyword sweep misses the early arcs: their verdict lines were written before the later vocabulary existed (the word
"grammar" is in none of the verdict lines of B1-B500, and the early multi-state constructions are called "gluing" and
"weaving", not "states").  So the early record was read line by line (2026-10-02, all of B1-B500) and every arc is
assigned here to the subjects it bears on.  The assignment is by hand; the text of each row is taken by code from
the arc's own verdict file, so nothing is retyped.

    python3 scripts/checks/early_record_index.py            # writes docs/EARLY_RECORD_INDEX.md
    python3 scripts/checks/early_record_index.py --check    # exit 1 if an early arc is in no subject, a listed arc
                                                            # does not exist, or the page is stale

Use: before a statement about what the record holds on one of these subjects, read the subject's rows.  The index
does not grade the arcs and does not replace reading them; it says where to look.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from topic_sweep import arcs, ROOT

LAST = 500
PAGE = os.path.join(ROOT, "docs", "EARLY_RECORD_INDEX.md")


def R(a, b):
    return list(range(a, b + 1))


# subject key -> (title, what a reader should know before saying anything on the subject, arc numbers)
SUBJECTS = [
 ("genesis", "The genesis: the seed A = LR, its half-step, the record-swap, what the axioms force and do not force",
  "The half-step F = LP is the unique GL(2,Z) square root of A (B14); the record-swap P is forced by (LX)^2 = A but "
  "NOT by A1-A6 (B16, B19); the trace map is the functorial lift of the half-step (B18) and is anti-Poisson (B21, "
  "B34); every word trace stays in Z[x,y,z] (B454); End(F2) on the character variety has four strata (B497); every "
  "metallic bundle double-covers a non-orientable one (B469).  The Omega strict-full theorems are re-derived in "
  "B156/B158/B159.",
  [13, 14, 16, 17, 18, 19, 21, 28, 30, 34, 35, 92, 93, 156, 158, 159, 179, 332, 454, 469, 471, 482, 485, 496, 497]),
 ("seed-selection", "What selects the golden seed (m = 1, the figure-eight) among its relatives, and what does not",
  "m is free under the axioms and m = 1 is selected only by the systole (B92); arithmeticity selects m = 1 AND m = 2 "
  "(B125, correcting B123); volume minimum among torsion-free positive words (B197); unique unitary anyon / unique "
  "superconformal chain (B218, B224, B228); only m = 1 is a knot complement (B251); the unique ramified prime selects "
  "E6 (B266); but almost everything in the E6 programme is generic to hyperbolic knots, only the arithmetic atom is "
  "specific (B282).",
  [92, 123, 125, 135, 197, 218, 224, 228, 231, 235, 238, 239, 240, 251, 258, 266, 282, 283, 316, 444, 445, 447]),
 ("coupling-selector", "The coupling I = 1/4, lambda/h = 1: conditional on an underived assumption (T1 -> S1)",
  "Ledger verdict B47: lambda/h = 1 is conditional, not derived; the strongest honest statement is T1 -> S1 with T1 "
  "underived (B32, B40).  Routes tried: period-3 return (B26, B31, B41), tangent integrality (B38, B39), variational "
  "(B42), Markov-Fricke discriminant (B43), torsion-one closure (B44), Lucas hierarchy (B29, B45), SL(3) (B46), "
  "renormalization (B36).  The figure-eight / I = 1/4 bridge is dead (B56).",
  [15, 24, 25, 26, 29, 31, 32, 36] + R(38, 47) + [56]),
 ("self-model", "Self-model, awareness, metabolism, behaviour catalogues: operational tests of the object",
  "The trace map has memory and feedback but never reads its invariant (B20, B37); kappa is conserved, the object is "
  "a horseshoe crystal, not a cell (B177, B455); the frozen ethogram's two preregistered gates fail (B456, B457); "
  "the Machian leap fails a random-base null (B170).",
  [20, 37, 170, 177, 452, 453, 455, 456, 457]),
 ("sln-tower", "The SL(n) tower: Dickson factors, degree = rank, the fixed-line spectra (era closed; capstones B153, B154)",
  "degree = rank is rank-stratified (B153) and the metallic exponent is order-determined, with no closed form (B154, "
  "B157, B199); the tower is one object, the Sym two-sequence (B117, B122); it is a trivial-representation "
  "phenomenon, absent at the geometric representation (B98, B99); climbing ranks acquires no new field (B129, B137).",
  [27, 33] + R(48, 52) + R(54, 55) + R(57, 66) + [74, 75] + R(77, 81) + R(83, 85) + [88, 89, 90, 94, 95, 98, 99]
  + R(103, 106) + [108] + R(110, 122) + [129, 137, 138, 141, 142, 149, 153, 154, 157, 198, 199, 201, 202, 203, 232]),
 ("character-variety", "The A-polynomial, the character varieties (SL(2), SL(3)), Painleve VI, the Coulomb branch",
  "The figure-eight A-polynomial is the trace map's fixed locus (B67); Fix(T1^2) on SL(3) is the SL(3) character "
  "variety, three components (B71, B100, B102); V0 is the Fuchsian locus of the Hitchin component (B101); kappa = "
  "4 I_FV + 2 (B148); the Schlesinger / Painleve VI flow is built (B164, B169) and the object is a transcendental "
  "positive-entropy solution (B317); the DGG elimination returns the A-polynomial (B433); the SL(3) sigma-story is "
  "the Gieseking deck action (B466); the periodic-orbit field tower on kappa = -2 (B448).",
  [2, 3, 67, 68, 69, 70, 71, 73, 87, 100, 101, 102, 148, 160, 164, 169, 179, 211, 213, 225, 317, 433, 448, 458, 465,
   466, 479, 485]),
 ("multi-state", "More than one object: gluing, weaving, composites, doubles, covers, children, mixed words",
  "The early record already builds on more than the root.  Gluing two metallic seeds along the cusp collapses the "
  "free kappa to a finite fork, never to a forced-unique value (B131, B174, B185, B190, B191); weaving two chains "
  "gives an interaction-born gap, rank 1 + number of fields, golden privileged (B172, B173, B175, B176, B178, B182); "
  "(golden, silver) is the unique metallic pair whose commutator is parabolic (B471, B472); composites are "
  "mirror-closed (B144) and concatenation makes the seam readout null (B369); covers create no new seam values "
  "(B349, B350, B368); the filled child and its controls (B434-B443, B453); the figure-eight double (B462); the "
  "Relation Campaign closes with no escaping invariant in any computed cell (B464); mixed words birth wild "
  "arithmetic (B498, B500).",
  [1, 130, 131, 144] + R(171, 176) + [178, 180, 182, 184, 185, 190, 191, 193, 319, 349, 350, 368, 369]
  + R(434, 443) + [453, 461, 462, 464, 470, 471, 472, 474, 477, 498, 499, 500]),
 ("chirality", "Chirality, orientation, mirror, the CP sign",
  "Amphichirality criterion for once-punctured-torus bundles (B134, B136); the chirality firewall (B139, B140, "
  "B143-B146) and its correction: arithmetic chiral bundles RRL/RLL exist (B147), sqrt(-7) is the chirality field "
  "(B316); amphichiral implies 2-torsion Chern-Simons (B152); every conjugation-odd invariant of the object vanishes "
  "or pairs (B252), corrected in B253; tau fixes both spin structures (B279); the CP sign is the sign of "
  "Chern-Simons (B289, B303, B340); every sampled hyperbolic filling makes the object chiral (B432), slope +-5 the "
  "minimal chirality input (B434); family, residue and wall converge on one orientation bit (B467, B469).",
  [22, 134, 136, 139, 140] + R(143, 147) + [152, 193, 252, 253, 271, 279, 285, 289, 303, 316, 318, 340, 348, 432,
                                               434, 467, 469]),
 ("scale", "Scale, dimensionful quantities, the cosmological constant, hierarchy",
  "Lambda = 2 pi^2 / Vol restates the problem (B5); the scale firewall: all dimensionful content is in hbar/k and "
  "squashing (B151), every emergent rate is dimensionless (B167, B168, B181, B188); the Mostow metric solves 3d "
  "vacuum Einstein (B259, with its withdrawn '122 orders'); no forced small number in the special geometry (B213); "
  "the seam envelope contracts up the tower (B408, B426); the tower measure is flat (B413).",
  [5, 96, 97, 126, 151, 167, 168, 181, 183, 187, 188, 189, 207, 213, 259, 408, 412, 413, 415, 426]),
 ("dynamics", "Dynamics, flows, time, potentials",
  "The derived potential and its inserted dynamics (B6, B7); the perturbation at (1,1,1) and the BKL observation "
  "(B4, B23); the void is a (2,1) saddle with Lyapunov rates +-4 log phi (B109, B416); the Painleve VI flow (B169, "
  "B317); the clock is the peripheral symplectic pairing, with no trajectory (B293); the cubic V(tau) is the wrong "
  "object for symmetry breaking (B295); the Dehn-filling flow, slope external (B338, B339); Ruelle resonance = "
  "escape rate (B451); opening the chain gives an irreversible spectrum at zero threshold (B183, B187); the "
  "QCA/Dirac route is null (B480).",
  [4, 6, 7, 23, 109, 169, 177, 183, 186, 187, 188, 293, 295, 317, 338, 339, 344, 416, 451, 480]),
 ("spectrum", "The spectral face: kappa, the Fibonacci Hamiltonian, quasicrystals, Cantor spectra",
  "The tower is the Kohmoto-Kadanoff-Tang trace map (B107, B127); kappa = 2 + lambda^2 and kappa = -2 is the "
  "parabolic cusp (B160); kappa = 2 is the unique fibre with positive-measure spectrum (B161, B162); kappa < 2 is "
  "Cantor and encodes no geometry (B163, B165, B186); SL(n >= 3) is non-Hermitian (B166); the symbolic face is "
  "Sturmian (B417); on-site is the unique Sturmian-preserving interaction (B200).",
  [25, 52, 107, 124, 148, 160, 161, 162, 163, 165, 166, 186, 192, 200, 417]),
 ("quantum", "Quantum invariants: WRT period laws, colored Jones, level-rank, anyons, the supersymmetric chain",
  "The WRT level-period law holds for all once-punctured-torus bundles and is elementary (B204, B208, B214, B215, "
  "B219; B216 withdrawn; generic by Jeffrey 1992, B283); the quantum trace map (B205); Lee-Yang / SU(2)_k layer "
  "(B132, B135); the golden chain is tricritical Ising = the first N=1 superconformal model, emergent only (B220-"
  "B224, B226-B231, B236); level-rank duality is conjugation, universal (B238, B242, B243, B245); colored Jones at "
  "roots of unity (B240, B261, B276, B314); the golden structure is a face of the Fibonacci TQFT, generic (B313, "
  "B483, B484, B492).",
  [9, 24, 76, 132, 135, 196] + R(204, 205) + [208, 212] + R(214, 224) + R(226, 231) + [236, 238]
  + R(240, 246) + [261, 276, 283, 312, 313, 314, 376, 384, 441, 483, 484, 492]),
 ("mckay-e6-e8", "The two ends: McKay E6 and E8, the E6 character variety, the E7 exclusion",
  "E8 from the monodromy field Q(sqrt 5), E6 from the trace field Q(sqrt -3) (B206, B210, B248, B249, B332); E7 "
  "excluded (B239, B256, B315); dim H^1(4_1, Ad rho_prin) = 6 graded by E6 exponents, unobstructed, smooth point "
  "(B264, B265, B270, B273, B274, B275, B347, B352, B357, B370); the involution is the E6 diagram involution "
  "(B353); the cascade is standard Slansky (B306, B310, B311); the E6 count is universal, not a fingerprint (B281, "
  "B445); two torsions, golden and Eisenstein (B423, B424, B425); the upstairs spin walls: E6 content is "
  "integer-spin, no fermions forced (B428, B429, B430); the centralizer of the principal sl2 is zero (B463).",
  [206, 207, 209, 210, 225, 233, 234, 235, 237, 247, 248, 249, 250] + R(254, 258) + R(263, 268) + R(270, 275)
  + [281, 282, 284, 301, 302, 304, 305, 306, 309, 310, 311, 312, 315, 320, 321, 332, 347, 351, 352, 353, 356, 357, 370,
     423, 424, 425, 428, 429, 430, 445, 463]),
 ("gauge-3d3d", "Gauge theory readings: 3d-3d, T[4_1], class S, S-duality, flavour versus gauge",
  "The trace-map action is the N=2* S-duality action (B150, B277); the character variety is the Coulomb branch of "
  "T[4_1] (B260, B433); T[4_1] is abelian, U(1) with two chirals, flavour only O(2) (B262, B269); the Gang-Yonekura "
  "SU(3) is a flavour symmetry, not a gauged colour group (B241, B487); metallic DGG laws (B488, B489); no gauge "
  "group is forced by the collective (B184).",
  [150, 184, 241, 260, 262, 269, 277, 433, 476, 487, 488, 489]),
 ("seam-fillings", "The seam: Dehn fillings, the forced closing A = LR, exceptional slopes, the child",
  "The ingredients live at the seam (B286); the fibre slope is the unique torus-bundle closing and its monodromy is "
  "A = LR (B287); closing destroys the E6-selecting arithmetic (B288, as amended by B1419); the Chern-Simons sign "
  "law (B289); selection is axis-stratified, no universally distinguished closing (B291, B294); adversarial re-run "
  "(B296); slope +-5 and the Meyerhoff child (B434-B443, B460); the wall maps v2-v4 (B268, B278, B297).",
  R(286, 297) + [338, 339, 432] + R(434, 443) + [460]),
 ("generations", "Generations, the Z/3, mixing textures",
  "The figure-eight cannot force three generations by its degree-2 field: multiplicity 1 or 2 on seven routes "
  "(B298); no hyperbolic knot has a cyclic-cubic trace field (B307); 2T spin-3/2 branches 2+2 (B280); the Z/3 lives "
  "in the commensurator as a hidden symmetry (B302) and as the deck group of the 3-fold cover, an isometry, hence "
  "exact degeneracy (B335, B337); n1 = n2 is forced (B327, B329, B331); textures: trimaximal / TBM (B342, B343), "
  "charge texture (B345, B346), circulant (B323-B326); the core multiplicity is Z/2, not Z/3 (B414); the cusp is "
  "rectangular, not hexagonal (B486).",
  [280, 298, 299, 300, 307, 308, 320] + R(323, 327) + R(329, 331) + [335, 337, 342, 343, 344, 345, 346, 400, 414, 486]),
 ("level-15", "The level-15 seam arithmetic: Q(sqrt -15), the Weil representation, pair tables, the value sector",
  "The compositum Q(sqrt -15) and its Hilbert class field (B333, B334, B336, B401, B449); the Weil representation "
  "at N = 3, 5, 15 and the pair tables (B354, B355, B358-B367, B379-B383, B386, B389, B390, B393, B395-B397); the "
  "seam is nonzero exactly with the half-characteristic twist (B381, B366); the level tower is the quantized golden "
  "cat map (B376); sector existence laws (B371-B374, B377, B391); the value sector and 1/12 = 1/16 + 1/48 (B382, "
  "B384, B386, B387, B394, B399); no canonical 3x3 frame (B400); the tower measure is flat (B412, B413, B415); "
  "commutator tables and selection rules (B472, B474, B478); float artifacts corrected (B481).",
  [155, 333, 334, 336, 354, 355] + R(358, 367) + R(371, 377) + R(379, 399) + R(401, 413) + [415, 418, 420, 422, 426,
                                                                                                 427, 431, 446, 447,
                                                                                                 449, 459, 468, 472,
                                                                                                 473, 474, 476, 478, 481]),
 ("sm-values", "Standard-Model values and structure: matches, null tests, the bars that were not cleared",
  "The null test: 6241 filling-invariant ratios match 12 SM parameters at chance level (B322); the PMNS ensemble is "
  "numerology-class (B398); forced kinematics and sin^2 theta_W = 3/8 (B304); the cascade's novelty killed (B310); "
  "six blind tracks, every destination is named pure mathematics (B416, B417, B419, B420, B421); the twelve "
  "refutations are one structural no-go with three scoped obstructions (B490).  Every one of these is a statement "
  "about the single root object and its family.",
  [8, 15, 139, 304, 322, 342, 398, 405, 406, 416, 417, 419, 420, 421, 476, 484, 490]),
 ("syntheses", "Syntheses, wall maps, closures of chapters, prior-art checks",
  "The physics chapter closed at the SL(n) era (B82, B86, B126, B127, B128); the five-wall map v2-v4 (B268, B272, "
  "B278, B297); the brave three-seat attempt: eight inputs compress to two walls (B300); the child programme "
  "(B443); the Relation Campaign (B464); the one structural no-go (B490); the prior-art harness (B491).",
  [82, 86, 126, 127, 128, 268, 272, 278, 296, 297, 300, 421, 443, 464, 490, 491]),
 ("spacetime", "Spacetime readings: Regge, Lorentzian signature, emergent dimension, Einstein",
  "The 3d layer is exact and the 4d Regge step undefined (B3); the Neumann-Zagier Hessian is negative definite, "
  "Lorentzian signature is only the sl(2,R) Killing form (B96, B97); the Omega cone's dimension 3.94 is a "
  "truncation artifact (B189); the Mostow metric solves 3d vacuum Einstein (B259); signature (1,3) appears in an "
  "explicit SL(4,Z) matrix (B155).",
  [3, 4, 96, 97, 155, 189, 259]),
]


def number(arc_id):
    m = re.match(r"B(\d+)", arc_id)
    return int(m.group(1)) if m else None


def first_heading(arc_dir):
    """an arc with neither a verdict file nor FINDINGS.md: the first heading of its first markdown file"""
    d = os.path.join(ROOT, "frontier", arc_dir)
    for f in sorted(os.listdir(d)):
        if f.endswith(".md"):
            line = open(os.path.join(d, f), errors="replace").readline().strip().lstrip("# ")
            if line: return "(no verdict file) " + line
    return ""


def early(rows=None):
    return [r for r in (rows or arcs()) if (number(r["id"]) or 10 ** 6) <= LAST and r["id"].startswith("B")]


def build(rows=None):
    rows = early(rows); by = {}
    for r in rows: by.setdefault(number(r["id"]), []).append(r)
    covered, missing = set(), []
    out = ["# The early record (B1–B%d), indexed by subject" % LAST, "",
           "Generated by `scripts/checks/early_record_index.py`; do not edit by hand.  The early arcs were read line by",
           "line on 2026-10-02 because a keyword sweep misses them: their verdict lines predate the later vocabulary.",
           "The assignment to subjects is by hand; each row's text is the arc's own verdict line.  **The index says",
           "where to look; it does not grade the arcs and it does not replace reading them.**  An arc may sit under",
           "several subjects.  The summaries under each heading are a reader's orientation, written from the verdict",
           "lines alone.", "",
           "| subject | arcs | PROVED | NEGATIVE | OPEN | RETRACTED | no verdict file |", "|---|---|---|---|---|---|---|"]
    body = []
    for key, title, note, nums in SUBJECTS:
        rs = []
        for n in sorted(set(nums)):
            if n not in by: missing.append((key, n)); continue
            covered.add(n); rs += by[n]
        c = lambda v: sum(1 for r in rs if r["verdict"] == v)
        out.append("| [%s](#%s) | %d | %d | %d | %d | %d | %d |" % (title.split(":")[0], key, len(rs), c("PROVED"), c("NEGATIVE"),
                                                                 c("OPEN"), c("RETRACTED"), c(None)))
        body += ["", '<a id="%s"></a>' % key, "## %s" % title, "", note, "",
                 "| arc | verdict | the arc's own line |", "|---|---|---|"]
        for r in rs:
            text = (r["claim"] or r["title"].lstrip("# ") or first_heading(r["dir"]) or "(no verdict file and no text: scripts only)").replace("|", "/").replace("\n", " ")
            body.append("| `%s` | %s | %s |" % (r["dir"], r["verdict"] or "—", text[:330] + ("…" if len(text) > 330 else "")))
    unassigned = sorted(n for n in by if n not in covered)
    out += ["", "%d arc directories from B1 to B%d, every one under at least one subject." % (len(rows), LAST)] + body + [""]
    return "\n".join(out), unassigned, missing


def main(argv):
    text, unassigned, missing = build()
    if unassigned: print("in no subject:", " ".join("B%d" % n for n in unassigned))
    if missing: print("listed but not in the record:", " ".join("%s:B%d" % m for m in missing))
    if "--check" in argv:
        stale = not os.path.exists(PAGE) or open(PAGE).read() != text
        if stale: print("docs/EARLY_RECORD_INDEX.md is stale: run scripts/checks/early_record_index.py")
        ok = not (unassigned or missing or stale)
        print("VERDICT early-record-index: %s (%d arc directories, %d subjects)" % ("PASS" if ok else "FAIL", len(early()), len(SUBJECTS)))
        return 0 if ok else 1
    if unassigned or missing: return 1
    open(PAGE, "w").write(text)
    print("wrote docs/EARLY_RECORD_INDEX.md: %d arc directories, %d subjects" % (len(early()), len(SUBJECTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
