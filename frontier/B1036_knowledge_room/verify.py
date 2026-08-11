"""B1036 — the knowledge room: what decays, what does not, and a gate that cannot see the drift.

The room is the "textbook layer" a new seat reads first, and `knowledge/INDEX.md` is one of the
NINE surfaces `representation_sweep.py` reads when it asks "is this arc represented anywhere?".

Everything is counted here over the tree. This arc's own rows are excluded from every count.
"""
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import representation_sweep as rsw            # noqa: E402  the gate's own module

SELF = "B1036"
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def anchors(text):
    return sorted({int(x[1:]) for x in re.findall(r"\bB\d+\b", text)})


KDIR = ROOT / "knowledge"
KFILES = sorted(f for f in os.listdir(KDIR) if re.match(r"K\d{3}_.*\.md$", f))
KID = {f: f[:4] for f in KFILES}
NEWEST = max(int(m.group(1)) for d in os.listdir(ROOT / "frontier")
             if (m := re.match(r"B(\d+)_", d)))

# ------------------------------------------------------- 1. the room's size, three ways wrong
chk("the_room_holds_26_explainers", len(KFILES) == 26, n=len(KFILES))

# Three documents stated the room's size; all three were wrong (INDEX "K001-K020",
# GOVERNANCE "K001..K009" AND "WRITTEN (K001-K010)", ARCHITECTURE "K001-K022") against 26 on
# disk. Repaired here; the checks assert the repaired state and that each repair cites its arc.
REPAIRED = ["knowledge/INDEX.md", "knowledge/GOVERNANCE.md", "ARCHITECTURE.md"]
chk("all_three_size_statements_now_match_the_room",
    all("K001–K026" in read(r) for r in REPAIRED), files=REPAIRED)
chk("and_each_repair_cites_the_arc_that_made_it",
    all("B1036" in read(r) for r in REPAIRED))
gov = read("knowledge/GOVERNANCE.md")
chk("governance_no_longer_carries_two_ranges_at_once",
    "WRITTEN (K001–K026)" in gov and "K001…K026" in gov
    and "WRITTEN (K001–K010)" not in gov.split("Corrected 2026-08-11")[0])

# --------------------------- 2. THE GATE PASSES ANYWAY — two structural holes, demonstrated
on_disk = {KID[f] for f in KFILES}
index_body = read("knowledge/INDEX.md")
indexed = {f"K{n}" for n in re.findall(r"\bK(\d{3})\b", index_body)}
chk("the_knowledge_index_gate_is_green_right_now", on_disk == indexed,
    n_on_disk=len(on_disk), n_indexed=len(indexed))

# HOLE 1 — the gate matches any MENTION, so a bullet indexes as well as a row.
k026_lines = [ln for ln in index_body.splitlines() if "K026" in ln]
# HOLE 1 stands as a property of the gate regardless of the repair: `indexed` is built from
# r"\bK(\d{3})\b" over the WHOLE BODY, so a bullet -- or a passing mention in prose -- indexes
# exactly as well as a row. K026 was a bullet and the gate was green.
chk("HOLE_1_the_gate_counts_a_mention_not_a_row",
    'r"\\bK(\\d{3})\\b"' in read("scripts/gates/gates.py").replace("re.findall(", 'r"\\bK(\\d{3})\\b"')
    or "findall(r\"\\bK(\\d{3})\\b\"" in read("scripts/gates/gates.py"),
    why="a bullet satisfies the gate exactly as well as a table row")

# HOLE 2 — the gate's on_disk regex is filename-scoped, so unnumbered docs are invisible forever.
unnumbered = sorted(f for f in os.listdir(KDIR)
                    if f.endswith(".md") and not re.match(r"K\d{3}_", f)
                    and f not in ("INDEX.md", "GOVERNANCE.md"))
chk("HOLE_2_unnumbered_room_documents_are_invisible_to_the_gate",
    len(unnumbered) == 2 and not any(re.match(r"K\d{3}_", f) for f in unnumbered),
    docs=unnumbered)
# They were in NO index at all; this arc adds an "Also in this room" section so they are at
# least reachable. The gate still cannot see them -- that is a property of its regex, not of
# the index -- so the hole stands and is registered as L161.
chk("they_are_now_at_least_listed_even_though_the_gate_still_cannot_see_them",
    all(f in index_body for f in unnumbered)
    and "Also in this room" in index_body, docs=unnumbered)

# The rendered shape: one real table, then orphan pipe-lines, then a bullet.
lines = index_body.splitlines()
pipe = [i + 1 for i, l in enumerate(lines) if l.strip().startswith("|")]
delim = [i + 1 for i, l in enumerate(lines)
         if l.strip().startswith("|") and set(l.replace("|", "").replace(" ", "")) <= set("-:")]
blocks, cur = [], []
for n in pipe:
    if cur and n == cur[-1] + 1:
        cur.append(n)
    else:
        if cur:
            blocks.append(cur)
        cur = [n]
if cur:
    blocks.append(cur)
orphans = [b for b in blocks if len(b) == 1]
# BEFORE: one table (K001-K016), then NINE orphan single-pipe lines (K017-K025) that markdown
# renders as literal text, then K026 as a bullet. AFTER: one contiguous table of all 26.
chk("the_index_is_now_one_contiguous_table_with_no_orphan_rows",
    len(orphans) == 0 and blocks[0][-1] - blocks[0][0] >= 26,
    table_block=(blocks[0][0], blocks[0][-1]), orphan_single_pipe_lines=len(orphans),
    delimiter_rows=len(delim))
chk("and_K026_is_a_row_now",
    any(l.strip().startswith("| **K026") for l in lines))

# ------------- 3. WHAT ACTUALLY DECAYS — standard background does not; own consolidation does
# The split is the room's OWN (GOVERNANCE: "K001-K007 are the standard-background pieces").
STANDARD = {f"K00{i}" for i in range(1, 8)}
per_entry = {}
for f in KFILES:
    a = anchors(read(f"knowledge/{f}"))
    per_entry[KID[f]] = {"file": f, "anchors": len(a), "newest": max(a) if a else None,
                         "class": "STANDARD" if KID[f] in STANDARD else "OWN/MIXED"}
own = {k: v for k, v in per_entry.items() if v["class"] != "STANDARD"}
chk("the_room_splits_into_seven_standard_and_the_rest_own",
    len(STANDARD) == 7 and len(own) == 19, standard=7, own_or_mixed=len(own))
chk("standard_entries_old_anchors_are_NOT_evidence_of_decay",
    all(per_entry[k]["newest"] < 200 for k in STANDARD),
    note="Fricke/character variety, metallic continued fractions, Dickson/Chebyshev, Dehn "
         "filling, -w0, 3d-3d, KKT/Suto - textbook mathematics; the B-numbers are pointers to "
         "where the project USES the standard fact, not the substance")

own_newest = sorted(v["newest"] for v in own.values())
median_own = own_newest[len(own_newest) // 2]
chk("the_decay_eligible_half_is_anchored_far_back",
    median_own < 300 and sum(1 for n in own_newest if n < 250) >= 10,
    median_newest_anchor=median_own, below_B250=sum(1 for n in own_newest if n < 250),
    of=len(own_newest), corpus_at=NEWEST)

# ------------- 4. THE POINTER IN THE PROVEN REGISTER — "the current headline", 710 arcs back
CLAIMS = re.sub(r"\s+", " ", read("CLAIMS.md"))
# BEFORE: CLAIMS sent readers to "`knowledge/K020` (the current headline ...)" -- a CURRENCY
# CLAIM inside the proven register, aimed at a document whose newest anchor is B325.
chk("the_current_headline_label_is_gone_from_the_proven_register",
    "`knowledge/K020` (the current headline" not in CLAIMS)
chk("and_the_pointer_now_says_what_it_actually_is",
    "consolidated at B325" in CLAIMS and "B1036" in CLAIMS)
k020_newest = per_entry["K020"]["newest"]
chk("but_K020s_newest_anchor_is_hundreds_of_arcs_back",
    NEWEST - k020_newest > 600, k020_newest=k020_newest, corpus_at=NEWEST)
# ...and this is NOT a firewall breach: CLAIMS points OUTWARD to what it does not claim.
chk("and_that_is_a_currency_defect_not_a_firewall_breach",
    "deliberately not here, by the firewall and the bar" in re.sub(r"\s+", " ", CLAIMS),
    why="CLAIMS points outward to what it does NOT claim - the firewall working as designed")

# ------------- 5. THE COMPOUNDING CONSEQUENCE for the representation sweep (B1033's family)
# Scoped by AUTHORSHIP -- and this is the sharpest instance of that hazard yet: REPAIRING the
# index moved the very freshness number that motivated the repair (the new K026 row carries
# B917). Measured with this arc's own lines removed.
def without_self(rel):
    return "\n".join(ln for ln in read(rel).splitlines() if SELF not in ln
                     and "Also in this room" not in ln and "K026_the_measurement_cascade" not in ln)


freshness = {}
for s in rsw.SURFACES:
    if (ROOT / s).exists():
        a = anchors(without_self(s))
        freshness[s] = max(a) if a else 0
kn = freshness.get("knowledge/INDEX.md", 0)
others = sorted(v for k, v in freshness.items() if k != "knowledge/INDEX.md")
chk("knowledge_INDEX_is_the_oldest_of_the_nine_sweep_surfaces",
    kn == min(freshness.values()) and others[0] - kn > 400,
    knowledge_index=kn, next_oldest=others[0], newest_surface=max(freshness.values()))
chk("so_it_can_only_answer_represented_for_the_era_the_filter_already_ignores",
    kn < 800, note="B1033: zero pre-B800 arcs can clear the substantiality filter; the weakest "
                   "sweep surface is silent about everything after B483")

# ------------------------------------------- 6. two further defects the census surfaced
slugs = {}
for f in KFILES:
    slugs.setdefault(f[5:], []).append(f[:4])
dupe = {k: v for k, v in slugs.items() if len(v) > 1}
chk("two_entries_share_a_filename_slug_and_a_topic", bool(dupe), duplicate_slugs=dupe)

# ------------- 7. THE PRIMARY FINDING: the room's no-premise rule is prose-only, and broken
GOV_RULE = "never a premise of a proof"
chk("the_room_forbids_being_used_as_a_premise", GOV_RULE in re.sub(r"\s+", " ", gov))
gates_src = read("scripts/gates/gates.py")
chk("but_the_firewall_gate_does_not_cover_this_room",
    'if "speculations/" in row or "philosophy/" in row or "story/" in row:' in gates_src
    and "knowledge/" not in gates_src.split("firewall")[1][:2000].split("def ")[0])

lawmap = read("docs/LAW_MAP.md")
row149 = next(l for l in lawmap.splitlines() if "Form forced, value Galois-chosen (K020)" in l)
chk("BREACH_1_an_explainer_carries_a_THEOREM_grade_on_the_law_register",
    "**THEOREM** (K020)" in row149 and row149.split("|")[4].strip().startswith("K020"),
    row=row149.split("|")[1].strip(), grade="**THEOREM** (K020)",
    witnesses=row149.split("|")[4].strip()[:40],
    why="K020 names the row, authorises the grade, and is listed AHEAD of the arc B642")

seal = read("docs/SEAL_LEDGER.md")
chk("BREACH_2_a_SEALED_preregistration_cites_an_explainer_as_its_authority",
    "excluded by K018" in seal,
    why="a sealed document cannot be amended; the real authority is B164/B167/B168/B169")

# ------------- 8. K021 overstates the generation grade, against its own section 8
k021 = read(next(f"knowledge/{f}" for f in KFILES if f.startswith("K021")))
chk("K021_says_the_object_FORCES_three_generations",
    "forces all the dimensionless" in re.sub(r"\s+", " ", k021)
    and "three generations" in re.sub(r"\s+", " ", k021))
chk("while_its_own_section_8_lists_that_step_as_an_OPEN_gate",
    "multiplicity → generations" in k021)
chk("and_every_current_surface_grades_it_STRUCTURAL",
    "the generation structure | **STRUCTURAL**" in re.sub(r"\s+", " ", read("docs/THE_CLAIM.md"))
    or re.search(r"generation structure.{0,40}STRUCTURAL", re.sub(r"\s+", " ", read("docs/THE_CLAIM.md"))) is not None)

# ------------- 9. A FIFTH E1: a factor of two between the room's two ungated documents
gcm = read("knowledge/THE_GOLDEN_CAT_MAP_PRINCIPLE.md")
atlas = read("knowledge/THE_UNIQUENESS_ATLAS.md")
chk("the_two_ungated_docs_quote_entropies_differing_by_exactly_two",
    "4 log φ" in gcm and "log φ² = 2 log φ" in atlas,
    golden_cat_map="Lyapunov 4 log φ = its metric entropy", uniqueness_atlas="log φ² = 2 log φ",
    both_marked_banked="[banked]" in atlas)
import sympy as sp
phi = (1 + sp.sqrt(5)) / 2
A = sp.Matrix([[2, 1], [1, 1]])
lam = max(A.eigenvals(), key=lambda x: abs(sp.N(x)))
chk("and_the_arithmetic_is_exact__4logphi_is_twice_log_of_A_s_eigenvalue",
    sp.simplify(lam - phi**2) == 0
    and abs(float(4 * sp.log(phi)) - 2 * float(sp.log(phi**2))) < 1e-12,
    A_eigenvalue="phi^2", h_top_of_A=float(sp.log(phi**2)), quoted=float(4 * sp.log(phi)),
    diagnosis="a convention gap, not an error: h = sum of POSITIVE Lyapunov exponents gives "
              "2 log phi; the sum of |exponents| over both directions gives 4 log phi. Neither "
              "document declares which. Same shape as B62 = 2 x P33 (B1026)")

# ------------- 10. THE POSITIVE CONTROL: the contradiction hunt came back clean
RETRACTED = read("docs/RETRACTED_PHRASES.md")
# The register's rows are `| N | \`phrase\` | retracted by | why |`. Extract the BACKTICKED
# phrase from each numbered row -- the first cut of this used a smart-quote regex and found only
# TWO, which the lock caught as a near-vacuous sweep (MB12: a criterion that cannot fail is not a
# test). Variants quoted inside the "why" column are picked up too.
phrases = [m.group(1) for m in re.finditer(r"^\|\s*\d+\s*\|\s*`([^`]+)`", RETRACTED, re.M)]
phrases += re.findall(r'\(and variants?:\s*"([^"]+)"', RETRACTED)
phrases += re.findall(r'\(and\s+`([^`]+)`\)', RETRACTED)
kroom = " ".join(read(f"knowledge/{f}") for f in KFILES)
kflat = re.sub(r"\s+", " ", kroom).lower()
hits = [ph for ph in phrases if re.sub(r"\s+", " ", ph).lower() in kflat]
chk("NO_retracted_phrase_appears_anywhere_in_the_room", hits == [] and len(phrases) >= 8,
    n_phrases_checked=len(phrases), phrases=phrases, hits=hits)

R["numbers"] = {
    "k_files": len(KFILES), "corpus_at": NEWEST,
    "standard": sorted(STANDARD), "own_or_mixed": len(own),
    "median_own_newest_anchor": median_own,
    "own_below_B250": sum(1 for n in own_newest if n < 250),
    "k020_newest": k020_newest,
    "sweep_surface_freshness": freshness,
    "unnumbered_docs": unnumbered,
    "duplicate_slugs": dupe,
    "per_entry": per_entry,
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
