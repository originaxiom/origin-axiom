"""B1210 — the paper-spine sweep. These locks keep the spine SWEPT rather than remembered."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1210_paper_spine_sweep"
SPEC = ROOT / "papers" / "P3_THE_PAPER" / "SPEC.md"
POOL = ROOT / "papers" / "P3_THE_PAPER" / "CLAIM_CANDIDATES.md"


def _law_arcs():
    out = []
    for p in ROOT.glob("frontier/*/arc_verdict.json"):
        try: v = json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if v.get("creates_law") and v.get("verdict") in ("PROVED", "NEGATIVE"):
            out.append(v["id"])
    return sorted(out)


def test_every_law_creating_arc_is_in_the_claim_pool():
    """The pool is the paper's defence against being written from memory. If a new law-creating arc
    banks and the pool is not regenerated, this fails -- which is the point."""
    pool_text = POOL.read_text(encoding="utf-8")
    missing = [a for a in _law_arcs() if not re.search(rf"`{a}`", pool_text)]
    assert not missing, (f"{len(missing)} law-creating arcs absent from CLAIM_CANDIDATES.md: "
                         f"{missing[:8]} -- regenerate with the arc's verification/ scripts")


def test_the_landing_is_in_the_recognition_table_not_the_forced_list():
    """B1210's load-bearing correction: arriving at su(3)+su(2)+u(1)^3 is the A2+A1 Levi, classical
    (Borel-de Siebenthal / Dynkin). If it ever migrates back to the forced list, the paper's most
    exposed claim is over-claimed again."""
    s = SPEC.read_text(encoding="utf-8")
    i_rec = s.index("## 5. The recognition table")
    i_next = s.index("## 6.", i_rec)
    recognition = s[i_rec:i_next]
    assert "Levi" in recognition and "Borel" in recognition, (
        "the Levi deflation must live in the recognition table")
    forced = s[s.index("**I — FORCED.**"):s.index("**II —")]
    # Scope matters here too -- the same lesson the sweep itself learned. The phrase DOES appear in
    # this section, inside the blockquoted correction that quotes the earlier draft. What must not
    # happen is the landing being asserted as forced in the running prose.
    prose = "\n".join(l for l in forced.splitlines() if not l.lstrip().startswith(">"))
    assert "landing on" not in prose, "the landing must not be listed among the forced results"
    assert "landing on" in forced, "the correction note must keep quoting what it corrected"


def test_the_z6_row_cites_the_stronger_footing():
    s = SPEC.read_text(encoding="utf-8")
    z6 = s[s.index("global ℤ₆ form"):s.index("global ℤ₆ form") + 400]
    assert "B1080" in z6, "B862 alone is the conditional footing; B1080 extends it"


def test_the_reportable_supersession_number_is_the_clause_scoped_one():
    """The instrument's own correction, locked: a claim-scoped matcher reads every verb as applying
    to every reference and produced a number that was mostly noise. Both are recorded; the second
    is the one that may be reported."""
    r = json.loads((ARC / "b1210_results.json").read_text(encoding="utf-8"))
    first = r["instrument"]["first_pass_claim_scope"]
    second = r["instrument"]["second_pass_clause_scope"]
    assert first["status"] == "MOSTLY NOISE" and second["status"] == "REPORTABLE"
    assert second["spec_citations_flagged"] < first["spec_citations_flagged"]
    assert len(first["falsifying_spot_checks"]) >= 2, "a discarded number needs its falsifiers kept"


def test_the_coverage_gap_that_motivated_the_arc_is_recorded_honestly():
    r = json.loads((ARC / "b1210_results.json").read_text(encoding="utf-8"))
    c = r["coverage"]
    assert c["cited_by_spec_of_those"] < c["law_creating_arcs_in_corpus"] / 10
    assert r["answer"].startswith("NO")


def test_the_disposition_column_is_left_to_an_editor():
    """The sweep produces candidates, not decisions. A machine-filled disposition would be the
    same failure as a memory-written spine, one level up."""
    t = POOL.read_text(encoding="utf-8")
    # B1213 re-rendered this page on the union criterion, so the wording moved. The INVARIANT is
    # what this lock is for and it is unchanged: the column ships empty and the page says the call
    # belongs to an editor.
    assert "editorial call" in t
    assert "| | " in t or "|  |" in t, "the disposition column must ship empty"
