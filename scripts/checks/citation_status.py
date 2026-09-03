#!/usr/bin/env python3
"""citation_status.py -- THE POINT-OF-USE GATE (B1243).

THE FAILURE CLASS.  A claim is USED without checking its status WHERE IT IS USED.  The ledgers
already record every retraction, refutation and scope correction; until now nothing read them at
the moment a document leans on the claim.  On 2026-09-03 seven errors in one exchange had exactly
this shape -- including one by the seat doing the correcting, who graded another seat's theorem
from a summary of it rather than from its own text, and had the wrong grade accepted downstream
because it arrived with authority (E58).

WHAT IT DOES **NOT** DO, AND WHY.  The first design of this gate forbade a THEOREM link to cite an
arc whose verdict is NEGATIVE or RETRACTED.  Run against the live corpus it produced SEVEN
violations, ALL FALSE:

  * B731 is RETRACTED *because* it established that m004 IS congruence -- exactly what C9 asserts.
  * B282's NEGATIVE kills a genericity claim while its surviving arithmetic atom is what C6 cites.

An arc can prove one thing while killing another (tests/test_b833_negative_routing.py says so of
kill records; the converse holds too).  A verdict-based prohibition would have red the build on
seven honest citations and made the fastest path to green DELETING PROVENANCE -- the B1222 shape,
aimed at ourselves.  So the verdict layer here REPORTS and never fails.

WHAT IT DOES.  It fails on the one shape that is always an error: a document leaning on an arc
whose FINDINGS carries a **correction banner** -- a blockquote in its first 30 lines saying the arc
was corrected, re-scoped, superseded or partially retracted -- while the citing text gives no sign
the author saw it.  That is not a judgement about the mathematics; it is a judgement about whether
the reader was warned.  Four arcs in the corpus carry such a banner.

  --chain      docs/THEOREM_LEDGER.md against the live arcs (default)
  --doc PATH   the same for any document (a paper, a distilled repo's statements file)
  --export P   chain + per-link status + identification rows as JSON, for downstream repos to pin
  --selftest   planted controls in BOTH directions (MB12)
"""
import argparse, glob, json, os, re, sys

ROOT = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEDGER = os.path.join(ROOT, "docs", "THEOREM_LEDGER.md")
IDENT = os.path.join(ROOT, "docs", "IDENTIFICATION_LEDGER.md")
COVERAGE = os.path.join(ROOT, "docs", "CHAIN_COVERAGE.json")

LINK = re.compile(r"^\*\*(C\d+[a-z]?)\s*\[([A-Z-]+)", re.M)
ARC = re.compile(r"\bB(\d{2,4})\b")
BANNER_KEY = re.compile(r"(PARTIALLY RETRACTED|CORRECTED BY|SENTENCE CORRECTED|SCOPE.CORRECTED"
                        r"|SUPERSEDED BY|RETRACTED BY|RE-SCOPED|WITHDRAWN BY)", re.I)
# stemmed, so "correcting"/"corrected"/"correction" all count as the author having seen it
ACK = re.compile(r"(correct|retract|withdraw|scope|supersed|re-scoped|amend|overstat|\bNB\b|caveat|fenc)", re.I)
DEAD = {"NEGATIVE", "RETRACTED"}


def verdicts():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(d.get("id"), str):
            out[d["id"]] = d.get("verdict")
    return out


def banner_of(findings_path):
    """a REAL banner: a blockquote line in the first 30 lines carrying a correction keyword.
    Body prose that merely discusses supersession (B1237's audit table) must NOT match."""
    try:
        head = open(findings_path, encoding="utf-8", errors="ignore").readlines()[:30]
    except OSError:
        return None
    for ln in head:
        s = ln.strip()
        if s.startswith(">") and BANNER_KEY.search(s):
            return re.sub(r"^[>#\s]+", "", s)[:160]
    return None


def banners():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "frontier", "*", "FINDINGS.md")):
        b = banner_of(p)
        if b:
            out[os.path.basename(os.path.dirname(p)).split("_")[0]] = b
    return out


def ident_rows():
    rows = {}
    if not os.path.exists(IDENT):
        return rows
    for line in open(IDENT, encoding="utf-8"):
        m = re.match(r"\|\s*(I-\d+)\s*\|", line)
        if m:
            st = re.search(r"\*\*(EARNED|UNEARNED|REFUTED)\*\*", line)
            rows[m.group(1)] = st.group(1) if st else "?"
    return rows


def links(text):
    ms = list(LINK.finditer(text))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.append((m.group(1), m.group(2), text[m.start():end]))
    return out


def audit(text, ban, vd=None):
    """violations = links citing a BANNERED arc with no acknowledgement in the citing text."""
    vd = vd or {}
    bad, seen = [], []
    for cid, lab, body in links(text):
        cited = sorted({"B" + n for n in ARC.findall(body)})
        hit = [a for a in cited if a in ban]
        ack = bool(ACK.search(body))
        seen.append({"link": cid, "label": lab, "cites": cited,
                     "bannered": hit, "acknowledges": ack,
                     "dead_cited": sorted(a for a in cited if vd.get(a) in DEAD)})
        if hit and not ack:
            bad.append((cid, lab, hit))
    return bad, seen


def coverage(text=None, rows=None):
    """THE SECOND DIRECTION.  The first asks whether a cited claim is stale.  This asks whether a
    load-bearing claim is cited AT ALL.  docs/UNIQUENESS_THEOREM.md -- the machine-checked genesis
    theorem, banked on day 9 -- sat uncited by the chain for three months while appearing on every
    other synthesis surface, so B977's third gate could not fire on it.  Nothing checked the chain's
    own COVERAGE.  Returns the rows whose token is missing from the chain."""
    if rows is None:
        if not os.path.exists(COVERAGE):
            return [], []
        rows = json.load(open(COVERAGE, encoding="utf-8")).get("must_appear_in_chain", [])
    text = text if text is not None else open(LEDGER, encoding="utf-8").read()
    missing = [r for r in rows if r["token"] not in text]
    return rows, missing


def selftest():
    ban = {"B901": "> ## CORRECTED BY B950 -- the sentence overstates"}
    miss = "**C90 [THEOREM - a claim].** rests on B901 and B900.\n"
    okay = "**C91 [THEOREM - a claim].** rests on B901, corrected by B950.\n"
    nogo = "**C92 [NO-GO - a wall].** the kill is B901 (scope named).\n"
    clean = "**C93 [THEOREM - a claim].** rests on B900 only.\n"
    b, _ = audit(miss, ban);  assert [x[0] for x in b] == ["C90"], "positive control failed"
    b, _ = audit(okay, ban);  assert not b, "acknowledgement control failed"
    b, _ = audit(nogo, ban);  assert not b, "acknowledgement-in-no-go control failed"
    b, _ = audit(clean, ban); assert not b, "clean control failed"
    b, _ = audit(miss + okay + nogo + clean, ban)
    assert [x[0] for x in b] == ["C90"], f"mixed control failed: {b}"
    # the banner detector itself, both ways
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        real = os.path.join(d, "a.md"); prose = os.path.join(d, "b.md")
        open(real, "w").write("# T\n\n> ## SENTENCE CORRECTED BY B950 -- overstates\n\nbody\n")
        open(prose, "w").write("# T\n\n| 2 | B258 | superseded by something | note |\n\nbody\n")
        assert banner_of(real), "banner positive control failed"
        assert banner_of(prose) is None, "banner negative control failed (body prose must not match)"
    # coverage detector, both ways -- synthetic rows, so these controls never go vacuous
    synth = [{"token": "UNIQUENESS_THEOREM", "why": "w", "since": "s", "arc": "a"},
             {"token": "B1138", "why": "w", "since": "s", "arc": "a"}]
    assert len(coverage("nothing here", synth)[1]) == 2, "coverage positive control failed"
    assert not coverage("UNIQUENESS_THEOREM and B1138 both cited", synth)[1], "coverage negative control failed"
    assert len(coverage("only UNIQUENESS_THEOREM", synth)[1]) == 1, "coverage partial control failed"
    print("selftest: 10/10 controls pass (missing-ack caught; ack, no-go, clean, mixed; banner +/-; coverage 0/1/2-missing)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chain", action="store_true")
    ap.add_argument("--doc")
    ap.add_argument("--export")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return 0
    vd, ban = verdicts(), banners()
    path = a.doc or LEDGER
    text = open(path, encoding="utf-8").read()
    bad, seen = audit(text, ban, vd)
    ncite = sum(len(s["cites"]) for s in seen)
    print(f"citation status: {os.path.relpath(path, ROOT)} -- {len(seen)} links, {ncite} arc "
          f"citations, {len(vd)} arcs resolved, {len(ban)} bannered arcs in the corpus")
    dead = [s for s in seen if s["dead_cited"]]
    print(f"  REPORT (never fails): {len(dead)} link(s) cite a NEGATIVE/RETRACTED arc -- legitimate "
          f"when the arc's surviving content is what is used (e.g. a retraction that established the fact)")
    if a.export:
        json.dump({"links": seen, "identifications": ident_rows(),
                   "bannered_arcs": ban, "arcs": dict(sorted(vd.items()))},
                  open(a.export, "w"), indent=1)
        print(f"  exported -> {os.path.relpath(a.export, ROOT) if a.export.startswith(ROOT) else a.export}")
    rows, missing = coverage(text if (a.doc is None) else None)
    if rows:
        print(f"  COVERAGE: {len(rows) - len(missing)}/{len(rows)} pinned results present in the chain")
    if bad or missing:
        for r in missing:
            print(f"\nCOVERAGE VIOLATION: the chain no longer carries {r['token']!r}\n"
                  f"  why it is pinned: {r['why']}  (since {r['since']}, {r['arc']})")
    if bad:
        print(f"\nVIOLATIONS: {len(bad)} link(s) cite a corrected arc without acknowledging it")
        for cid, lab, hit in bad:
            for h in hit:
                print(f"  {cid} [{lab}] cites {h}, whose FINDINGS says:\n      {ban[h]}")
    if bad or missing:
        return 1
    print("  no link cites a corrected arc without acknowledging it: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
