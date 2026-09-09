#!/usr/bin/env python3
"""coverage_candidates.py -- what the length proxy could not see (B1247, Review 54 R54-1/R54-2).

THE DEFECT THIS REPLACES.  `representation_sweep` screens arcs by `claim_one_line` LENGTH
(floor 500).  Measured: 282 arcs watched, 674 unwatched -- 98.6% effective on what it sees and
blind to 70% of the corpus.  The proxy fails hardest on the DENSE: the seam family B286-B295 runs
166-197 characters, and B286's 182 characters relocate the programme's central wall.

TWO THINGS A CHARACTER COUNT CANNOT MEASURE, both reported here instead:

  --unrepresented   substantive arcs on NO synthesis surface, RANKED BY IN-DEGREE (how many other
                    arcs declare them in `depends_on`).  An arc others build on that no surface
                    mentions is the real debt; an arc nothing cites and no surface names is
                    peripheral.  Measured 2026-09-03: 158 unrepresented, of which only 9 have
                    in-degree > 0.  The backlog was never 154 items -- it is 9.

  --chain-gap       arcs represented on synthesis surfaces but ABSENT FROM THE CHAIN, ranked by
                    surface-degree.  This is the direction nothing had ever checked: THE CHAIN IS
                    NOT IN `representation_sweep`'s SURFACES LIST AT ALL.  Validated against the
                    chain as it stood at B1243, BEFORE C46: it flags B286 (3 surfaces), B294 (2),
                    B287 (1), B295 (1) and correctly does NOT flag B288, which C8 already cited.

WHY NEITHER IS A BUILD GATE.  At threshold 1 the chain-gap list is ~688 arcs: the chain is a
curated 46-link spine, not a catalogue, so "absent from the chain" is not a defect -- it is the
normal case.  WHICH absences matter is a judgement, and the decadal review is where judgement
belongs.  These are REPORTERS that feed the review; the build gate stays where a hard criterion
exists (`docs/CHAIN_COVERAGE.json`, which fails when a PINNED result is dropped).  An in-degree
screen was tried first and REJECTED on its own evidence: the seam family has in-degree 1-2, so it
would have missed exactly the case that motivated the change.
"""
import argparse, collections, glob, json, os, re, sys

ROOT = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SURFACES = ["docs/LAW_MAP.md", "docs/THE_SM_VERDICT.md", "docs/SM_SPECIFICATION_LEDGER.md",
            "docs/GUT_REQUIREMENTS_LEDGER.md", "docs/CAMPAIGN_STATUS.md", "docs/OPEN_LEADS.md",
            "docs/OPEN_PROBLEMS.md", "docs/HINT_LEDGER.md", "knowledge/INDEX.md"]
CHAIN = ["docs/THEOREM_LEDGER.md", "docs/THE_END_TO_END_CHAIN.md"]


def corpus():
    arcs, indeg = {}, collections.Counter()
    for p in glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d.get("id"), str):
            continue
        arcs[d["id"]] = d
        for dep in (d.get("depends_on") or []):
            if isinstance(dep, str):
                indeg[dep] += 1
    sub = {k: v for k, v in arcs.items()
           if v.get("verdict") in ("PROVED", "NEGATIVE") and not v.get("instrument")}
    return sub, indeg


def _read(paths):
    out = {}
    for f in paths:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            out[f] = open(p, encoding="utf-8", errors="ignore").read()
    return out


def unrepresented(sub, indeg, surf=None):
    txt = " ".join((surf or _read(SURFACES)).values())
    out = [(a, indeg[a]) for a in sub if not re.search(rf"\b{a}\b", txt)]
    return sorted(out, key=lambda x: -x[1])


def chain_gap(sub, surf=None, chain_text=None):
    st = surf or _read(SURFACES)
    ct = chain_text if chain_text is not None else " ".join(_read(CHAIN).values())
    out = []
    for a in sub:
        deg = sum(1 for t in st.values() if re.search(rf"\b{a}\b", t))
        if deg and not re.search(rf"\b{a}\b", ct):
            out.append((a, deg))
    return sorted(out, key=lambda x: -x[1])


def selftest():
    sub = {"B900": {"verdict": "PROVED", "depends_on": []},
           "B901": {"verdict": "PROVED", "depends_on": ["B900"]},
           "B902": {"verdict": "NEGATIVE", "depends_on": ["B900"]}}
    indeg = collections.Counter({"B900": 2})
    # unrepresented: B902 on no surface; B900/B901 present
    surf = {"s": "B900 and B901 are discussed here."}
    u = unrepresented(sub, indeg, surf)
    assert [a for a, _ in u] == ["B902"], u
    # ranking: an arc others depend on outranks one nothing cites
    surf2 = {"s": "nothing here"}
    u2 = unrepresented(sub, indeg, surf2)
    assert u2[0] == ("B900", 2), u2
    # chain-gap: on a surface, absent from the chain -> flagged; in the chain -> not
    g = chain_gap(sub, {"s": "B900 B901"}, "B901 only")
    assert [a for a, _ in g] == ["B900"], g
    assert not chain_gap(sub, {"s": "B900"}, "B900 is cited"), "in-chain must not be flagged"
    # the rejected alternative, recorded as a control: in-degree alone would MISS a low-in-degree arc
    assert indeg["B901"] == 0, "the seam-family shape: load-bearing yet barely depended on"
    print("selftest: 5/5 controls pass (unrepresented +/-, in-degree ranking, chain-gap +/-)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unrepresented", action="store_true")
    ap.add_argument("--chain-gap", action="store_true")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return 0
    sub, indeg = corpus()
    only = a.unrepresented or a.chain_gap
    if a.unrepresented or not only:
        u = unrepresented(sub, indeg)
        q = [x for x in u if x[1] > 0]
        print(f"UNREPRESENTED (no synthesis surface): {len(u)} substantive arcs")
        print(f"  of these, DEPENDED ON by another arc -- the real queue: {len(q)}")
        print(f"  in-degree 0 (cited by nothing, on no surface): {len(u) - len(q)} -- peripheral")
        for arc, d in u[:a.top]:
            n = len(sub[arc].get("claim_one_line") or "")
            print(f"    {arc:7} in-deg {d:2}  claim {n:5} chars  "
                  f"{'(length screen was BLIND)' if n < 500 else '(length screen saw it)'}")
    if a.chain_gap or not only:
        g = chain_gap(sub)
        print(f"\nCHAIN-GAP (on a synthesis surface, absent from the chain): {len(g)}")
        print("  NOT a defect list -- the chain is a curated spine. A review adjudicates; "
              "promotions get PINNED in docs/CHAIN_COVERAGE.json, which is the gate.")
        for arc, d in g[:a.top]:
            print(f"    {arc:7} on {d} surface(s)  {sub[arc]['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
