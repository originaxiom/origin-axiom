"""B1033 — the two debt registers reconciled, and the sweeper's substantiality bar measured.

Occasion: `docs/consolidation/DEBT_LEDGER.md` (this refresh's own deliverable) was built without
checking whether the repository already had a debt register. It does — `docs/REPRESENTATION_TRIAGE.md`
(L143/B976), with a sweeper and a FAILING gate behind it. The ledger cites it zero times.

Reconciling the two turned up something bigger than the omission: the sweeper's substantiality
filter is **era-dependent**, and by construction cannot flag any arc banked before ~B800.

Everything below reads banked artifacts. No mathematics is asserted.
"""
import glob
import json
import os
import pathlib
import re
import statistics as st
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import representation_sweep as rsw  # noqa: E402  the gate's own module, not a reimplementation

R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


# The five hand-written consolidations the DEBT_LEDGER measures.
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]


def _blob(rels, exclude_own=True):
    """Scoped by AUTHORSHIP — the SIXTH instance of one hazard in five arcs, and this time it
    moved a published number: this arc's own LAW_MAP row cites B976, which would have removed
    B976 from the very set being measured. Every citation search here drops the rows this arc
    wrote. THE_LADDER's X31 named the shape: 'registering a gap creates hits for the gap.'"""
    out = []
    for p in rels:
        if not (ROOT / p).exists():
            continue
        txt = read(p)
        if exclude_own:
            txt = "\n".join(ln for ln in txt.splitlines() if "B1033" not in ln)
        out.append(txt)
    return "\n".join(out)


def cited(b, blob):
    return bool(re.search(rf"\b{b}\b", blob) or re.search(rf"{b}_", blob))


# ------------------------------------------------------------------ the corpus, read once
ARCS = {}
for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
    m = re.match(r"B(\d+)_", os.path.basename(d))
    vp = os.path.join(d, "arc_verdict.json")
    if not m or not os.path.isfile(vp):
        continue
    n = int(m.group(1))
    if n in ARCS:
        continue          # B58 has three directories; count the B-number once
    dd = json.loads(pathlib.Path(vp).read_text(encoding="utf-8"))
    fp = os.path.join(d, "FINDINGS.md")
    ARCS[n] = {"verdict": dd.get("verdict"), "instrument": bool(dd.get("instrument")),
               "clen": len(dd.get("claim_one_line") or ""),
               "fsize": os.path.getsize(fp) if os.path.isfile(fp) else 0}


def band(n):
    return (n // 100) * 100


BANDS = sorted({band(n) for n in ARCS})
MEDIAN = {lo: st.median([ARCS[n]["clen"] for n in ARCS if band(n) == lo]) for lo in BANDS}

# ------------------------------------------------------- 1. the two rules, side by side
cur_blob = _blob(CURATED)
sweep_blob = _blob(rsw.SURFACES)

# ...and the arc itself is excluded from the set it measures. Scoping only the ROWS still left
# B1033 counting itself as an uncited debt row; the published figure is "the corpus at B1032".
SELF = 1033
ledger_set = {n for n, a in ARCS.items()
              if n != SELF and a["verdict"] == "PROVED" and not a["instrument"]
              and not cited(f"B{n}", cur_blob)}
triage_set = {n for n, a in ARCS.items()
              if a["verdict"] in ("PROVED", "NEGATIVE") and not a["instrument"]
              and a["clen"] >= 500 and not cited(f"B{n}", sweep_blob)}
triage_rows = {int(x[1:]) for x in
               re.findall(r"^\| `(B\d+)`", read("docs/REPRESENTATION_TRIAGE.md"), re.M)}

chk("the_two_rules_give_different_sets",
    len(ledger_set) > 200 and len(triage_set) < 30,
    ledger=len(ledger_set), triage_live=len(triage_set), triage_rows=len(triage_rows),
    overlap=len(ledger_set & triage_rows))
chk("the_overlap_is_small", len(ledger_set & triage_rows) < 10,
    overlap=sorted(f"B{n}" for n in ledger_set & triage_rows))
chk("the_sweeper_module_is_the_gates_own_not_a_reimplementation",
    hasattr(rsw, "SURFACES") and hasattr(rsw, "sweep") and len(rsw.SURFACES) == 9)

# B976 — the arc whose lead CREATED the triage — sits in the ledger's set. It is NOT a triage row,
# and correctly so: it IS cited on two sweep surfaces. Both registers behave as designed; what was
# missing is that the ledger never said so.
chk("b976_is_in_the_ledger_set_and_correctly_not_a_triage_row",
    976 in ledger_set and 976 not in triage_rows)
chk("b976_is_cited_on_sweep_surfaces", cited("B976", sweep_blob))

# --------------------------------- 2. THE FINDING: the substantiality bar is a step in time
step = {lo: (int(MEDIAN[lo]), sum(1 for n in ARCS if band(n) == lo and ARCS[n]["clen"] >= 500),
             sum(1 for n in ARCS if band(n) == lo)) for lo in BANDS}
pre800 = [n for n in ARCS if n < 800]
pre800_over = [n for n in pre800 if ARCS[n]["clen"] >= 500]
chk("NO_arc_before_B800_can_ever_clear_the_500_char_bar",
    pre800_over == [], n_pre800=len(pre800), over=pre800_over)
chk("the_median_claim_length_steps_by_an_order_of_magnitude_at_B800",
    MEDIAN[700] < 200 and MEDIAN[900] > 2000,
    median_by_band={f"B{lo}": int(MEDIAN[lo]) for lo in BANDS})
chk("so_the_bar_measures_the_banking_convention_not_substance",
    all(MEDIAN[lo] < 200 for lo in BANDS if lo < 800)
    and all(MEDIAN[lo] > 600 for lo in BANDS if lo >= 800))

# The register's own calibration set: the ELEVEN its preamble names as cited zero times.
# B862 is deliberately excluded there ("Only B862 appears — and only because the solo seat caught
# it an hour earlier"), so 11, not 12, is the right denominator.
CALIB = [860, 861, 863, 864, 865, 868, 869, 870, 871, 872, 873]
TRI = read("docs/REPRESENTATION_TRIAGE.md")
B976F = read("frontier/B976_cascade_recovery/FINDINGS.md")
# The register states the COUNT ("Eleven banked cascade arcs (B860-B873)"); B976's FINDINGS names
# the members and excludes B862 explicitly ("Only B862 appears - and only because the solo seat
# caught it an hour earlier").
chk("the_calibration_set_is_the_eleven_named_by_B976_and_counted_by_the_register",
    len(CALIB) == 11 and all(n in ARCS for n in CALIB)
    and "Eleven banked cascade arcs" in re.sub(r"\s+", " ", TRI)   # hard-wrapped
    and all(f"B{n}" in B976F for n in CALIB)
    and "Only B862 appears" in B976F and 862 not in CALIB)
chk("all_eleven_clear_the_bar_as_the_register_claims",
    all(ARCS[n]["clen"] >= 500 for n in CALIB),
    lengths={f"B{n}": ARCS[n]["clen"] for n in CALIB})
chk("the_calibration_set_is_entirely_post_convention",
    all(ARCS[n]["clen"] >= 500 for n in CALIB) and min(CALIB) >= 800)

# AND THE MARGIN IS TWO CHARACTERS. B862 — the twelfth arc of the same block, the one that
# DERIVES THE GLOBAL Z6 FORM — carries a claim line of 498. It was excluded from the calibration
# only because a different seat had already cited it. Had it not been, the "11 of 11" would have
# been 11 of 12, and the miss would have been the block's most consequential member.
chk("the_bars_margin_on_its_own_calibration_block_is_two_characters",
    ARCS[862]["clen"] == 498, b862_claim_len=ARCS[862]["clen"], bar=500)

# Scoped by AUTHORSHIP — the fifth instance of one hazard in four arcs. This arc's own scope-limit
# block is what puts era language into the register, so an unscoped search would report the gap as
# already stated the moment it was stated.
TRI_BEFORE = TRI.split("⚠ MEASURED SCOPE LIMIT")[0] + TRI.split("**Why claim length, not file size.**")[-1]
chk("the_register_stated_its_calibration_but_never_scoped_it_in_time",
    "catches **11 of 11**" in TRI and "every **substantial** banked arc" in TRI
    and not re.search(r"\bera\b|\bbefore B\d|\bpre-B\d", TRI_BEFORE, re.I))
chk("and_this_arc_is_what_adds_the_scope_limit",
    "MEASURED SCOPE LIMIT" in TRI and "structurally blind to two-thirds" in re.sub(r"\s+", " ", TRI))

# ------------------- 3. a candidate repair, TESTED AND REJECTED before being proposed (MB12)
def band_relative(n):
    return ARCS[n]["clen"] >= 2 * MEDIAN[band(n)]


recovered = sum(1 for n in CALIB if band_relative(n))
chk("the_obvious_band_relative_fix_FAILS_its_own_calibration",
    recovered <= 3, recovered=recovered, of=len(CALIB),
    note="2x-band-median recovers 1 of 12 — proposing it would have replaced a known blind "
         "spot with an unknown one")

# And the measure the register REJECTED is the era-stable one — which is why the rejection
# was right for its purpose and wrong as a general principle.
fmed = {lo: int(st.median([ARCS[n]["fsize"] for n in ARCS if band(n) == lo])) for lo in BANDS}
chk("FINDINGS_size_is_era_STABLE_unlike_claim_length",
    max(fmed.values()) / max(1, min(fmed.values())) < 4
    and max(MEDIAN.values()) / max(1, min(MEDIAN.values())) > 15,
    findings_median_by_band=fmed)

# ------------------------------------ 4. consequence for the ledger's own stratification
above = sorted(n for n in ledger_set if ARCS[n]["clen"] >= 500)
chk("every_ledger_row_clearing_the_bar_is_late_corpus",
    above and min(above) >= 800, lowest=f"B{min(above)}" if above else None, count=len(above))
# Bounded as a SHARE, not a raw count -- amended 2026-08-11 (B1040). The original form asserted
# `> 200` rows dropped, which the RESTORATIONS THIS CAMPAIGN EXISTS TO MAKE then eroded: B1038,
# B1039 and B1040 retired thirteen rows and the count crossed the threshold at 198/216, breaking a
# passing lock without touching the finding. This arc's own prose already said the intended form
# ("the lock bounds the share rather than pinning the integer, precisely so ordinary consolidation
# work does not break it") -- the check simply did not implement it. The structural result is
# untouched: the lowest above-bar row is still B870, and the share is 92 %.
_below = len(ledger_set) - len(above)
chk("so_stratifying_the_ledger_by_that_bar_would_discard_the_entire_early_corpus",
    _below / max(1, len(ledger_set)) > 0.85,
    would_be_dropped=_below, of=len(ledger_set),
    share="%.3f" % (_below / max(1, len(ledger_set))))

# ------------------------------------------------- 5. the repairs this arc actually makes
LEDGER = read("docs/consolidation/DEBT_LEDGER.md")
chk("the_ledger_now_cites_the_triage_register",
    "REPRESENTATION_TRIAGE" in LEDGER and "representation_sweep" in LEDGER
    and "representation-sweep" in LEDGER)
chk("the_ledger_carries_both_counts_and_refuses_the_stratification",
    "234" in LEDGER and "10 live" in LEDGER
    and all(s in re.sub(r"\s+", " ", LEDGER)
            for s in ("That is refused.", "discard the entire pre-B800 corpus")))

# the E1 misattribution, repointed
for loc in ("frontier/B1024_l153_bits/FINDINGS.md",
            "frontier/B1026_the_one_involution/FINDINGS.md",
            "tests/test_b1026_one_involution.py"):
    t = read(loc)
    chk(f"e1_source_repointed_in_{os.path.basename(loc)}",
        "ERROR_LEDGER" not in t.split("most recurrent")[0][-260:]
        if "most recurrent" in t else True)
chk("the_error_ledger_really_does_not_say_it",
    "most recurrent" not in read("docs/ERROR_LEDGER.md"))
chk("but_governance_and_working_rules_do",
    "most recurrent error class is undeclared choice" in re.sub(r"\s+", " ", read("GOVERNANCE.md"))
    and "most recurrent error" in re.sub(r"\s+", " ", read("WORKING_RULES.md")))

R["numbers"] = {
    "ledger_rule": len(ledger_set), "triage_rule_live": len(triage_set),
    "triage_rows": len(triage_rows), "overlap": len(ledger_set & triage_rows),
    "ledger_rows_clearing_the_bar": len(above), "lowest_such": f"B{min(above)}" if above else None,
    "pre_B800_arcs": len(pre800), "pre_B800_clearing_the_bar": len(pre800_over),
    "median_claim_len_by_band": {f"B{lo}": int(MEDIAN[lo]) for lo in BANDS},
    "median_findings_bytes_by_band": fmed,
    "band_relative_recovery_of_calibration_block": f"{recovered}/{len(CALIB)}",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
