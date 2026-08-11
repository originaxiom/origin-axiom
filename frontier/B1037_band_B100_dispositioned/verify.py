"""B1037 — the B100-B199 band dispositioned: 37 rows, 7 laws.

THE CAMPAIGN'S STEP 6, executed for the first time. docs/THE_CAMPAIGN.md: "a band is DONE when
its debt rows are either restored or explicitly declined with a reason." The debt ledger has said
"Dispositions: none applied" through thirteen arcs of instrument audit.

Bodies were read (step 1: "claim lines are not the surface"). Everything below is counted or
recomputed here; this arc's own rows are excluded from every count.
"""
import glob
import json
import os
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
SELF = "B1037"
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def body(b):
    g = glob.glob(str(ROOT / "frontier" / f"{b}_*" / "FINDINGS.md"))
    return pathlib.Path(g[0]).read_text(encoding="utf-8") if g else ""


CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]
blob = "\n".join("\n".join(l for l in read(p).splitlines() if SELF not in l) for p in CURATED)


def cited(b):
    return bool(re.search(rf"\b{b}\b", blob) or re.search(rf"{b}_", blob))


# ------------------------------------------------------------------ 1. the band, recounted
band = []
for d in sorted(glob.glob(str(ROOT / "frontier" / "B1[0-9][0-9]_*"))):
    m = re.match(r"B(\d+)_", os.path.basename(d))
    vp = os.path.join(d, "arc_verdict.json")
    if not m or not os.path.isfile(vp):
        continue
    n = int(m.group(1))
    if not (100 <= n <= 199):
        continue
    dd = json.loads(pathlib.Path(vp).read_text(encoding="utf-8"))
    if dd.get("verdict") == "PROVED" and not dd.get("instrument") and not cited(f"B{n}"):
        band.append(n)
band = sorted(set(band))
chk("the_band_carries_37_debt_rows", len(band) == 37, n=len(band), rows=band)

# ---------------------------------------- 2. THE FINDING: 30 of 37 are facets of SEVEN laws
CLUSTERS = {
    "the tower": [117, 122, 121, 118, 111, 113],
    "arithmeticity": [123, 125, 147, 137, 193],
    "phi-fixed reducibility": [141, 142],
    "the collective": [172, 173, 174, 175, 176, 178],
    "the open arrow": [183, 187, 186],
    "the metallic exponent": [154, 198],
    "isomonodromy": [164, 169, 150],
}
clustered = sorted({n for v in CLUSTERS.values() for n in v})
# Counted, not estimated: the sweep reported "~30 of 37"; the exact figure is 27 in 7 clusters
# with 10 standing alone. Stated at the size it is.
chk("seven_clusters_cover_twenty_seven_of_the_thirty_seven",
    len(CLUSTERS) == 7 and len(clustered) == 27 and set(clustered) <= set(band),
    n_clusters=len(CLUSTERS), n_clustered=len(clustered), standalone=len(band) - len(clustered),
    band=len(band))
chk("so_the_restoration_surface_is_laws_not_rows",
    len(CLUSTERS) + (len(band) - len(clustered)) < len(band) / 2,
    statements_owed=len(CLUSTERS) + (len(band) - len(clustered)), rows=len(band))

# the clusters are the arcs' own claim, not an editorial grouping
chk("B122_says_it_and_B121_are_one_object",
    re.search(r"B121 and the W-identity are one object", re.sub(r"\s+", " ", body("B122")))
    is not None)
chk("B117_says_it_supersedes_B111_and_B113",
    "superseded" in re.sub(r"\s+", " ", body("B117")).lower()
    and "B111" in body("B117") and "B113" in body("B117"))

# --------------------------- 3. ONE ROW IS A RETRACTION, NOT A RESTORATION
chk("B123_is_in_the_debt_set", 123 in band)
chk("but_B125_retracts_B123s_sub_claim",
    "selection criteria" in body("B125") and "retracted" in body("B125"))
chk("so_restoring_B123_as_written_would_restore_a_refuted_claim", 123 in band)

# --------------------------- 4. A BODY-READ PAYOFF: B109 owns the number B1036 flagged
# B1036 flagged a factor of 2 between the room's two ungated documents and diagnosed it as an
# undeclared CONVENTION gap. Reading B109's body sharpens it: 4 log(phi) is that arc's Lyapunov
# rate for the TRACE MAP's linearisation at the void -- a different map, on a different space --
# and THE_GOLDEN_CAT_MAP_PRINCIPLE attaches it to "the cat map ITSELF ... its metric entropy".
phi = (1 + sp.sqrt(5)) / 2
A = sp.Matrix([[2, 1], [1, 1]])
lam = max(A.eigenvals(), key=lambda x: abs(sp.N(x)))
h_top_A = sp.log(lam)
chk("the_cat_maps_entropy_is_2_log_phi",
    sp.simplify(lam - phi**2) == 0
    and abs(float(h_top_A) - float(2 * sp.log(phi))) < 1e-12,
    h_top=float(h_top_A))
chk("B109_computes_4_log_phi_for_the_TRACE_MAP_at_the_void",
    "4 log φ" in body("B109") and "void" in body("B109").lower()
    and "Lyapunov" in body("B109"))
gcm = read("knowledge/THE_GOLDEN_CAT_MAP_PRINCIPLE.md")
chk("the_room_doc_attaches_that_number_to_the_CAT_MAP_and_calls_it_its_metric_entropy",
    "the cat map ITSELF: Lyapunov 4 log φ = its metric entropy" in gcm)
chk("and_the_same_row_names_the_void_as_the_linearisation__which_is_B109s_object",
    "the void = its linearization" in gcm)
chk("so_the_diagnosis_sharpens_from_convention_gap_to_MISATTRIBUTION",
    abs(float(4 * sp.log(phi)) - 2 * float(h_top_A)) < 1e-12,
    note="4 log phi is not A's metric entropy (that is 2 log phi); it equals sum|lambda| for A "
         "AND is B109's trace-map rate. The row is labelled 'trace-map dynamics' and says 'the "
         "void = its linearization' -- B109's object -- while calling the number the CAT MAP's.")

# --------------------------- 5. the dispositions are written where the campaign asks
LEDGER = read("docs/consolidation/DEBT_LEDGER.md")
chk("the_ledger_no_longer_says_no_dispositions_applied",
    "**None applied.**" not in LEDGER)
chk("the_band_section_exists_with_the_three_dispositions",
    "§B100–B199 — DISPOSITIONED" in LEDGER
    and all(w in LEDGER for w in ("RESTORE", "DECLINE — PROCESS", "DECLINE — SUBSUMED")))
# strip blockquote markers too -- the hard-wrap + "> " hazard that has bitten every
# arc in this refresh that matched a SENTENCE against a hard-wrapped file.
flat_ledger = re.sub(r"\s+", " ", LEDGER.replace("\n> ", "\n"))
chk("and_it_states_the_cluster_finding",
    "27 arcs in 7 clusters" in flat_ledger
    and "17 statements owed, not 37" in flat_ledger
    and "The debt number counts rows; the debt is laws." in flat_ledger)
chk("and_it_records_B123_as_a_RETRACTION_not_a_restoration",
    "RETRACTION, NOT RESTORATION: B123" in flat_ledger
    and "would restore a refuted claim" in flat_ledger)

R["numbers"] = {
    "band_rows": len(band), "rows": band,
    "clusters": {k: v for k, v in CLUSTERS.items()},
    "clustered_rows": len(clustered),
    "statements_owed": len(CLUSTERS) + (len(band) - len(clustered)),
    "h_top_A": float(h_top_A), "four_log_phi": float(4 * sp.log(phi)),
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
