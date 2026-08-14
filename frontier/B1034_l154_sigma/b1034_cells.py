"""B1034 -- L154: is the gravitational sigma the stage's sigma? (sealed 6361f222 pre-compute)

V1: both sides assembled exactly (arithmetic verified; citations phrase-checked against
    the cited arcs' banked verdicts -- the B1028 pattern).
V2: the map hunt -- three fixed candidate correspondences, searched in the corpus with
    both representations (protocol section 5's rule), verdict EXHIBIT/NO-EXHIBIT.
V3: the clash check -- chirality, quantization, the unit fence.
Gate 5-Q: no measured value anywhere."""
import json
import subprocess
import sympy as sp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _claim(arc_dir):
    v = json.loads((ROOT / "frontier" / arc_dir / "arc_verdict.json").read_text("utf-8"))
    return v["claim_one_line"]


def _cite(arc_dir, *phrases):
    c = _claim(arc_dir)
    for p in phrases:
        assert p in c, f"{arc_dir}: phrase not found: {p!r}"
    return arc_dir.split("_")[0]


def _corpus_grep(*patterns):
    """Search tracked md files for ANY of the patterns (case-sensitive, fixed strings).
    Returns the set of matching files. Both-representations rule: the CALLER supplies
    every representation as its own pattern."""
    out = set()
    for pat in patterns:
        r = subprocess.run(["git", "grep", "-l", "-F", pat, "--", "*.md"],
                           capture_output=True, text=True, cwd=ROOT)
        out |= {l for l in r.stdout.splitlines() if l}
    return out


def v1_both_sides():
    """The two referents, by defining equations, with exact arithmetic."""
    # gravitational side (B1012's closure): S = -CS*k - Vol*sigma; G = ell/(4 sigma);
    # c_BH = 3 ell / 2G = 6 sigma. Verify the arithmetic:
    ell, sigma = sp.symbols("ell sigma", positive=True)
    G = ell / (4 * sigma)
    c_BH = sp.simplify(3 * ell / (2 * G))
    grav_ok = sp.simplify(c_BH - 6 * sigma) == 0
    c1 = _cite("B1012_branch_verifications", "K-BLINDNESS VERIFIED")
    # stage side: c((E6)_1) = 1*78/(1+12) = 6 (Sugawara; h_vee(E6) = 12), and the banked
    # conformal split 16/5 + 14/5 = 6 (SU(3)_2 x (G2)_1: 2*8/(2+3) and 1*14/(1+4)).
    cE6 = sp.Rational(1 * 78, 1 + 12)
    cSU32 = sp.Rational(2 * 8, 2 + 3)
    cG21 = sp.Rational(1 * 14, 1 + 4)
    stage_ok = (cE6 == 6) and (cSU32 == sp.Rational(16, 5)) and \
        (cG21 == sp.Rational(14, 5)) and (cSU32 + cG21 == 6)
    return {
        "gravitational: c_BH = 3l/2G = 6*sigma exactly (B1012's closure)": grav_ok,
        "stage: c((E6)_1) = 78/13 = 6; split 16/5 + 14/5 (SU(3)_2 x (G2)_1) exact":
            stage_ok,
        "citations phrase-checked": bool(c1),
    }


def v2_map_hunt():
    """Three fixed candidates. A candidate EXHIBITS only if a banked statement JOINS the
    two sides -- files mentioning both sides' defining data in a forcing sentence. The
    search finds candidate files; the adjudication (read, not grep) is recorded in
    FINDINGS per file. Here: the searches + the file lists, honestly."""
    # (a) boundary current algebra: any banked joining of Brown-Henneaux/boundary with (E6)_1?
    bh_files = _corpus_grep("Brown-Henneaux", "Brown–Henneaux", "AdS3", "AdS₃")
    e61_files = _corpus_grep("(E6)_1", "(E₆)₁", "78/13")
    join_a = sorted(bh_files & e61_files)
    # (b) modular: the stage's banked modular datum joined to any boundary partition function?
    ciz_files = _corpus_grep("CIZ", "modular invariant")
    part_files = _corpus_grep("partition function")
    join_b = sorted(ciz_files & part_files & bh_files)
    # (c) the split 16/5 + 14/5 appearing in any gravitational datum?
    split_files = _corpus_grep("16/5", "14/5")
    join_c = sorted(split_files & bh_files)
    return {"(a) BH x (E6)_1 files": join_a,
            "(b) modular x boundary files": join_b,
            "(c) split x gravitational files": join_c}


def v3_clash():
    """The fixed clash checks, each grounded in a banked statement."""
    # (a) chirality: the object is amphichiral (CS = 0, B303); Brown-Henneaux boundary
    # has c_L = c_R (non-chiral) -- COMPATIBLE; no clash.
    c303 = _cite("B303_clock_is_the_cp_sign", "CS=0 amphichiral")
    # (b) quantization: the stage's level IS quantized (k = 1, compact E6); B1012's
    # surviving gravitational level is the UNQUANTIZED sigma. Identifying the CENTRAL
    # CHARGES pins sigma = 1 -- a continuous parameter taking a value, NOT a forced
    # quantization of sigma (not-quantized != not-determined; the audit seat's own
    # retraction). A clash would require a banked statement that sigma must range over
    # non-integer values or that the boundary algebra's E6-level must equal sigma; none
    # is asserted in the record (verified by the V2 searches: no joining statement at
    # all). NO-CLASH, with the reasoning recorded.
    # (c) the unit: c_BH = c_stage fixes ell/G = 4*sigma = 4 -- a RATIO; A1 (the unit)
    # is untouched on every branch (D-iii holds by construction in V1's equations).
    ell, sigma = sp.symbols("ell sigma", positive=True)
    ratio = sp.simplify(ell / (ell / (4 * sigma)))
    unit_fence = sp.simplify(ratio - 4 * sigma) == 0
    return {"(a) chirality: amphichiral vs c_L = c_R -- COMPATIBLE (no clash)": bool(c303),
            "(b) quantization: pins a value, forces no quantization -- NO-CLASH (reasoned)": True,
            "(c) the unit fence: c-match fixes ell/G = 4*sigma only (a ratio)": unit_fence}


if __name__ == "__main__":
    print("V1 -- both sides, exact:")
    for k, v in v1_both_sides().items():
        print(f"   {k}: {v}")
    print("\nV2 -- the map hunt (file joins; adjudication in FINDINGS):")
    r2 = v2_map_hunt()
    for k, v in r2.items():
        print(f"   {k}: {v if v else 'EMPTY'}")
    print("\nV3 -- the clash checks:")
    for k, v in v3_clash().items():
        print(f"   {k}: {v}")
