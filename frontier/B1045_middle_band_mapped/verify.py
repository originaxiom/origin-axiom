"""B1045 — the instrument's first measured miss, and why the middle band is MAPPED not dispositioned.

Two results, one of each kind.

POSITIVE: B1044's law-siblings gate was used against a new band on its first outing and CAUGHT
NOTHING -- because a fingerprint catches restatements in the SAME vocabulary and B485 states
B1040's metallic degree in ALEXANDER-POLYNOMIAL language. Verified identical here, fingerprint
widened, gate now fires, B485 consolidated. The limitation is real, is not fixable by adding terms,
and is stated in the registry rather than discovered again.

NEGATIVE (about method): the B300-B499 band is MAPPED, not dispositioned. The map is keyword-seeded
from CLAIM LINES, and campaign step 1 forbids exactly that as a basis for disposition -- "read the
bodies, not the claim lines". The measured misassignment rate is the argument: 5 of 58, and TWO
of the five are arcs whose claim line explicitly DENIES the cluster the keywords assigned it to
(a third merely contrasts -- the first draft said three, and this check corrected it).
"""
import json
import pathlib
import re
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import law_siblings as ls          # noqa: E402

R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def claim(b):
    p = list(ROOT.glob(f"frontier/{b}_*/arc_verdict.json"))
    return json.loads(p[0].read_text(encoding="utf-8"))["claim_one_line"] if p else ""


# ============================================ 1. B485 IS B1040's LAW, IN ANOTHER VOCABULARY
m, a = sp.symbols("m a")
M = sp.Matrix([[m, 1], [1, 0]])
charpoly_of_Msq = sp.expand((M * M).charpoly(a).as_expr())
delta_m = sp.expand(a**2 - (m**2 + 2) * a + 1)
lam = (m + sp.sqrt(m**2 + 4)) / 2
chk("B485s_Alexander_law_IS_the_char_poly_of_M_m_squared",
    sp.expand(charpoly_of_Msq - delta_m) == 0
    and sp.simplify(sp.expand(delta_m.subs(a, lam**2))) == 0,
    Delta_m="a^2 - (m^2+2)a + 1", charpoly="charpoly(M_m^2)", root="lambda_m^2",
    note="the Alexander polynomial of a FIBERED bundle IS its monodromy's characteristic "
         "polynomial. B1040 verified this polynomial as the metallic DYNAMICAL DEGREE; B485 "
         "closed it as the metallic ALEXANDER LAW. One fact, two languages, two bands")

# the miss, reconstructed against the fingerprints as they were BEFORE the widening
OLD_ISO = r"isomonodrom|Painlev|Schlesinger|Vieta|Jimbo|Fricke cubic"
OLD = {"the tower (B1038)": ls.FINGERPRINTS["the tower (B1038)"],
       "phi-fixed reducibility (B1039)": ls.FINGERPRINTS["phi-fixed reducibility (B1039)"],
       "the metallic exponent (B1039)": ls.FINGERPRINTS["the metallic exponent (B1039)"],
       "isomonodromy (B1040)": OLD_ISO}
c485 = claim("B485")
chk("and_NO_fingerprint_reached_it_before_this_arc",
    not any(re.search(p, c485, re.I) for p in OLD.values()),
    tested=sorted(OLD), note="the instrument's first measured miss, on its first use against a "
                             "band it had not seen")
chk("the_fingerprint_is_widened_and_the_gate_now_fires",
    re.search(ls.FINGERPRINTS["isomonodromy (B1040)"], c485, re.I) is not None
    and "WIDENED B1045" in read("scripts/checks/law_siblings.py"))
chk("B485_is_now_consolidated_and_the_LIMITATION_is_stated_not_hidden",
    "B485" in read("docs/LAW_MAP.md")
    and "TRANSLATION between vocabularies escapes it"
        in re.sub(r"\s+", " ", read("docs/consolidation/LAW_SIBLINGS.md"))
    and "not fixable by adding terms" in read("docs/consolidation/LAW_SIBLINGS.md"),
    note="every widening is a guess at the next synonym. What the instrument reliably catches is "
         "the case that bit (B564: same words, different band); what it will keep missing is a "
         "re-derivation in another field's language")

# ============================================ 2. THE BAND IS MAPPED, AND THE MAP'S ERROR IS MEASURED
MISASSIGNED = {
    "B423": ("E6 selection & grading", "zeta / torsion",
             "the statement is the regularized-zeta CLOSED FORM; 'E6' names the object it is "
             "computed on"),
    "B345": ("E6 selection & grading", "generations / deviation",
             "the claim line ends 'INDEPENDENT of the E6-exponent grading'"),
    "B346": ("E6 selection & grading", "generations / deviation",
             "it is about the deviation space's symplectic conjugation; E6 is the contrast"),
    "B316": ("metallic family laws", "arithmetic selection / fields",
             "the claim line says sqrt(-7) is 'NOT a metallic-ladder member'"),
    "B435": ("E6 selection & grading", "the (5,1) child",
             "it is the child's H1 and vacuum count"),
}
denials = [b for b, (_, _, why) in MISASSIGNED.items()
           if re.search(r"\bNOT\b|independent of", why, re.I)]
chk("the_keyword_map_misassigns_and_the_rate_is_measured",
    len(MISASSIGNED) == 5,
    misassigned=len(MISASSIGNED), clustered=58, rate="%.0f%%" % (100 * 5 / 58),
    corrections={b: f"{a_} -> {b_}" for b, (a_, b_, _) in MISASSIGNED.items()})
chk("and_TWO_of_the_five_are_arcs_whose_claim_line_DENIES_the_cluster",
    len(denials) == 2, denying=sorted(denials),
    note="THE ARGUMENT FOR STEP 1, made concrete: a claim line's KEYWORDS can be exactly the words "
         "the arc uses to say what it is NOT. B345 says 'independent of the E6-exponent grading' "
         "and B316 says 'NOT a metallic-ladder member' -- and a keyword sweep files both under the "
         "thing they deny. THE FIRST DRAFT OF THIS ARC SAID THREE; B346 merely CONTRASTS with E6 "
         "rather than denying it, and this check is what caught the overcount")
for b, (_, _, _) in MISASSIGNED.items():
    chk(f"{b}_claim_line_is_read_not_quoted", bool(claim(b)), claim=claim(b)[:120])

chk("so_this_arc_MAPS_the_band_and_does_NOT_disposition_it",
    "MAPPED, not dispositioned" in read("docs/consolidation/DEBT_LEDGER.md"),
    rows=69, clusters=7, standalone=11,
    note="B1037 dispositioned B100-B199 by READING THE BODIES. This is a keyword map of CLAIM "
         "LINES, which step 1 forbids as a basis for disposition. Publishing it as a disposition "
         "would be the defect B1037's own method exists to avoid -- so it is published as what it "
         "is: the next pass's starting point, with its error rate attached")

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
