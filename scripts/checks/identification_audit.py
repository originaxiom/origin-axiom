#!/usr/bin/env python3
"""IDENTIFICATION AUDIT -- the pre-flight check against the programme's dominant error mode.

MANDATORY before claiming any cross-structure connection ("X here IS Y there").

THE FAILURE CLASS. This programme succeeds when it TYPES and fails when it IDENTIFIES. Every
identification failure in the record has one shape: two structures with matching labels, in
DIFFERENT PLACES, joined without a map.
  * B813  -- CS(m004) = theta_QCD. A functional VALUE cannot fill a COEFFICIENT slot. Dead on type.
  * B1223 -- V4 x| S3 = D4 triality. THE TEMPLATE: the map existed, the ACTION was trivial
             (Q(sqrt77) disjoint from the faces => direct, not semidirect). "Direct is not semidirect."
  * B1228 -- pi_1(m004) ->> 2T identified with the transverse ALE Gamma. Two different 2T's.
  * B1230 -- the object's Z/3 identified with the boundary CFT's module group. Same species, one
             cell later, inside the computation presented as the stronger recovery.

WHY IT IS NOT MERELY HYGIENE. By B1225 the object provably CANNOT identify -- naming requires an
outside. So an unearned identification is not a reasoning slip: it is an OBSERVER INPUT the ledger
never counted, and the parameter count is a LOWER BOUND until every one is earned or priced.

THE DISCRIMINATOR (B1223, promoted to standing in WORKING_RULES.md):
    exhibit the MAP, then show it ACTS FAITHFULLY.
    Matching orders, names, dimensions or numbers are NOT a connection.

THIS INSTRUMENT REPORTS CANDIDATES, NEVER VERDICTS. An instrument built to catch hasty gluing must
not glue. Judgment stays with a seat; the tool only surfaces the claims that need it.

    python3 scripts/checks/identification_audit.py              # the register's state
    python3 scripts/checks/identification_audit.py --extract    # candidates across the corpus
    python3 scripts/checks/identification_audit.py --triage     # + auto-sort the obvious
    python3 scripts/checks/identification_audit.py --selftest   # planted controls, both directions
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "docs" / "IDENTIFICATION_LEDGER.md"
BASELINE = ROOT / "docs" / "IDENTIFICATION_BASELINE.json"

# --- identification-shaped language -------------------------------------------------------------
# Deliberately NARROW. A wide net would flag every sentence in the corpus and the instrument would
# be ignored -- the fate of any checker that cries wolf (the B806 lexicon-blindness lesson).
IDENT = re.compile(
    r"\b(?:is|are)\s+(?:literally\s+|exactly\s+|precisely\s+)?the\s+same\b"
    r"|\bidentif(?:y|ied|ication|ying)\s+(?:of\s+|with\s+|the\s+)"   # the ACT, not the noun
    r"|\bidentified\s+with\b"
    r"|\bdictionary\b"
    r"|\bequate[ds]?\s+(?:with|to)\b"
    r"|\bone\s+and\s+the\s+same\b"
    r"|\bcoincide[ds]?\s+with\b"
    r"|\bcorrespond(?:s|ence)\s+(?:to|between)\b"
    r"|≡",                                                      # an explicit "is identically"
    re.I,
)
# NOTE on precision (measured 2026-09-01, and the reason the net is narrow): a first draft included
# the bare emphatic "IS the", which this repo's caps-heavy prose triggers constantly -- 272 BARE
# candidates, overwhelmingly false. A checker that cries wolf is ignored (the B806 lexicon-blindness
# lesson), so the net requires an explicit correspondence construct, not emphasis. It will MISS
# identifications phrased without one; that is the deliberate trade, and judgment still stays with
# a seat. Recall is measured by the selftest's planted glue, not assumed.
# typing language -- the SUCCESS mode. Presence of these near an identification usually means the
# claim is being CLASSIFIED rather than glued, which lowers (never eliminates) suspicion.
TYPING = re.compile(
    r"\btyp(?:e|ed|ing)\b|\bclassif\w+|\bparity\b|\bvalue group\b|\bover the field\b"
    r"|\bcategor\w+|\bgrade[ds]?\b|\bsort(?:ed|s)?\b",
    re.I,
)
# an exhibited map -- what would make an identification EARNED
MAP = re.compile(
    r"\bmap\b|\bmorphism\b|\bisomorphism\b|\bfunctor\b|\bacts?\s+(?:faithfully|transitively|trivially)\b"
    r"|\bequivariant\b|\bsemidirect\b|\bexhibit\w*\b",
    re.I,
)


def _arcs():
    for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        yield p.parent.name, d.get("id") or p.parent.name, d.get("verdict", "?"), \
            d.get("claim_one_line", ""), d.get("identifications", None)


def _ledger_rows():
    if not LEDGER.exists():
        return []
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|(.*)", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        status = next((c.replace("*", "") for c in cells
                       if c.replace("*", "") in ("EARNED", "REFUTED", "UNEARNED")), "?")
        rows.append({"id": m.group(1), "claim": cells[0] if cells else "",
                     "status": status})
    return rows


def cmd_state():
    rows = _ledger_rows()
    by = {}
    for r in rows:
        by.setdefault(r["status"], []).append(r["id"])
    print(f"identification ledger: {len(rows)} rows -- {LEDGER.relative_to(ROOT)}")
    for st in ("EARNED", "REFUTED", "UNEARNED", "?"):
        if st in by:
            print(f"  {st:9s} {len(by[st]):3d}   {' '.join(by[st])}")
    un = len(by.get("UNEARNED", []))
    print(f"\n  UNEARNED = {un}   <- these are UNPRICED OBSERVER INPUTS (B1225: the object cannot identify)")
    print("  the input ledger's parameter count is a LOWER BOUND while any row is UNEARNED.")
    if BASELINE.exists():
        base = json.loads(BASELINE.read_text(encoding="utf-8")).get("unearned", None)
        print(f"  ratchet baseline: {base}   current: {un}   "
              f"{'OK' if base is not None and un <= base else 'INCREASED -- the gate reds'}")
    return rows


def cmd_extract(quiet=False):
    """Mechanical pass. CANDIDATES ONLY -- never a verdict."""
    hits = []
    for d, aid, verdict, claim, decl in _arcs():
        if not claim:
            continue
        for sent in re.split(r"(?<=[.;])\s+", claim):
            if IDENT.search(sent):
                hits.append({"arc": aid, "verdict": verdict, "sentence": sent.strip()[:220],
                             "typing_nearby": bool(TYPING.search(sent)),
                             "map_nearby": bool(MAP.search(sent)),
                             "declared": decl is not None})
                break
    if not quiet:
        print(f"CANDIDATES (not verdicts): {len(hits)} arcs carry identification-shaped language\n")
        for h in hits[:25]:
            flag = "map?" if h["map_nearby"] else ("typed" if h["typing_nearby"] else "BARE")
            print(f"  [{flag:5s}] {h['arc']:7s} {h['verdict']:9s} {h['sentence'][:120]}")
        if len(hits) > 25:
            print(f"  ... and {len(hits)-25} more")
    return hits


def cmd_triage():
    hits = cmd_extract(quiet=True)
    bare = [h for h in hits if not h["map_nearby"] and not h["typing_nearby"]]
    typed = [h for h in hits if h["typing_nearby"] and not h["map_nearby"]]
    mapped = [h for h in hits if h["map_nearby"]]
    print(f"TRIAGE of {len(hits)} candidates:\n")
    print(f"  MAP-LANGUAGE PRESENT  {len(mapped):4d}  -- likely EARNED or at least argued; low priority")
    print(f"  TYPING-LANGUAGE ONLY  {len(typed):4d}  -- probably a classification, not a glue; low priority")
    print(f"  BARE                  {len(bare):4d}  <- NEEDS JUDGMENT: an identification with neither")
    print(f"                                 a map named nor a typing frame. This is the pile.")
    print("\n  sample of the BARE pile (a seat must judge each; the tool does NOT):")
    for h in bare[:15]:
        print(f"    {h['arc']:7s} {h['verdict']:9s} {h['sentence'][:118]}")
    return {"mapped": len(mapped), "typed": len(typed), "bare": len(bare), "total": len(hits)}


def cmd_selftest():
    """MB12: planted controls in BOTH directions -- AND an honest blind-spot control.

    THE MEASURED LIMIT (2026-09-01, and it must not be papered over): the detector MISSES the
    bare-assertion form -- "X IS Y" with no correspondence construct -- which is EXACTLY how this
    bench phrased the C-5b error the instrument was built for. Widening to catch it produced 272
    candidates, overwhelmingly false (the caps-heavy prose triggers "IS the" constantly).

    So detection is a LOSSY SAFETY NET, not the mechanism. The mechanism is the RULE plus the
    arc_verdict `identifications` DECLARATION, which the gate enforces. This control exists so no
    future seat mistakes the net for coverage.
    """
    explicit = "The Z/3 is identified with the boundary algebra's module group."
    bare = "The object's Z/3 IS the boundary algebra's module group."     # the real C-5b phrasing
    typed = "The parameters are classified by parity and dimension over the field Q(zeta_12)."
    mapped = "The isomorphism is exhibited and acts faithfully, so the product is semidirect."
    ok = [
        ("catches an EXPLICIT identification", bool(IDENT.search(explicit))),
        ("spares a typing claim", not IDENT.search(typed)),
        ("sees map language when present", bool(MAP.search(mapped))),
        ("ledger parses", len(_ledger_rows()) > 0),
        # the blind spot, asserted as a FACT so it cannot be forgotten:
        ("KNOWN BLIND SPOT: bare 'X IS Y' is NOT caught (declaration, not detection, is the mechanism)",
         not IDENT.search(bare)),
    ]
    for name, res in ok:
        print(f"  [{'PASS' if res else 'FAIL'}] {name}")
    good = all(r for _, r in ok)
    print("CONTROLS PASS" if good else "CONTROLS FAIL")
    if good:
        print("\n  RECALL IS PARTIAL BY DESIGN. The detector finds explicit correspondence claims;")
        print("  it does NOT find bare assertions. Do not treat --extract as coverage.")
    return 0 if good else 1


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--selftest":
        sys.exit(cmd_selftest())
    elif arg == "--extract":
        cmd_extract()
    elif arg == "--triage":
        cmd_triage()
    else:
        cmd_state()
