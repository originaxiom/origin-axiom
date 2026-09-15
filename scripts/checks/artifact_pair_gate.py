"""A cell's two committed artifacts must not contradict each other.

WHY THIS EXISTS (2026-09-12). A cell writes two things: a human `output.txt` and a
machine-readable `results.json`. Nothing ties them together, and on 2026-09-12 three of the
75 cells carrying a verdict in both places carried DIFFERENT ones:

  * `P2W5-L72`  -- output.txt RESOLVED-A, results.json UNRESOLVED. Re-running the cell's own
    unmodified `compute.py` reproduced output.txt byte-for-byte; the JSON differed in 51
    fields and recorded `h1 = 0` for all six E6 exponents, a failed relator check from an
    older code version, preserved as though it were a result.
  * `W4-017r`   -- results.json `PENDING_PART_B` with only the `part_A` key: a snapshot
    taken between part A and part B and never rewritten.
  * `W2-270`    -- THE OTHER DIRECTION. output.txt said UNRESOLVED because "depth 9-11
    recomputation did not complete", while its results.json already CONTAINED the depth
    7-11 sequence. Both files were committed in the same commit, already inconsistent.

So there is no privileged artifact: "always trust the JSON" would have been wrong one time
in three. This gate is the cheap half of the defence -- a string comparison, sub-second, no
re-running. The expensive half already exists and is complementary:
`scripts/checks/instrument_freshness.py` RE-RUNS `verify.py` cells and compares
`results.json`; it never reads `output.txt`, and it scans a different population.

THE RULE: a pair is a MISMATCH when BOTH artifacts carry a verdict and the text's verdict
appears among NONE of the JSON's. A cell carrying a verdict on only one side is a
formatting gap, reported and not failed.

VERDICT EXTRACTION, stated because it is the only judgement in the file:
  * from `output.txt`: the LAST match of `(FINAL )?VERDICT:\\s*(\\S+)` (cells print a final
    verdict line, sometimes prefixed by a log timestamp, sometimes after a `=== VERDICT ===`
    banner);
  * from `results.json`: EVERY string-valued key named `verdict`, at any depth (some cells
    nest theirs, and some carry a second deliberate reading such as
    `verdict_under_universal_reading`, which is not a `verdict` key and is ignored).

    python3 scripts/checks/artifact_pair_gate.py             # the gate
    python3 scripts/checks/artifact_pair_gate.py --selftest  # bite control (MB12)
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FRONTIER = ROOT / "frontier"
VERDICT_RE = re.compile(r"(?:FINAL\s+)?VERDICT:\s*(\S+)")


def text_verdict(body: str) -> str | None:
    """The cell's decisive printed verdict: the LAST one it prints."""
    hits = VERDICT_RE.findall(body)
    return hits[-1].rstrip(".,;") if hits else None


def json_verdicts(obj, out=None) -> list[str]:
    """Every string-valued 'verdict' key, at any depth."""
    if out is None:
        out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "verdict" and isinstance(v, str):
                out.append(v)
            else:
                json_verdicts(v, out)
    elif isinstance(obj, list):
        for v in obj:
            json_verdicts(v, out)
    return out


def is_mismatch(txt: str | None, js: list[str]) -> bool:
    """The gate's whole decision, isolated so --selftest can bite it directly."""
    return bool(txt) and bool(js) and txt not in js


def scan():
    both, one_side, unreadable, bad = 0, 0, [], []
    for j in sorted(FRONTIER.glob("**/results.json")):
        o = j.parent / "output.txt"
        if not o.exists():
            continue
        try:
            d = json.loads(j.read_text())
        except Exception as e:
            unreadable.append((j, str(e)[:60]))
            continue
        txt = text_verdict(o.read_text(errors="replace"))
        js = json_verdicts(d)
        if txt and js:
            both += 1
            if is_mismatch(txt, js):
                bad.append((j.parent, txt, js))
        elif txt or js:
            one_side += 1
    return both, one_side, unreadable, bad


def selftest() -> int:
    """MB12: the detector must be able to FIRE and able to STAY SILENT."""
    fire = [
        ("RESOLVED-A", ["UNRESOLVED"]),
        ("UNRESOLVED", ["RESOLVED-B"]),
        ("RESOLVED-A", ["PENDING_PART_B"]),
    ]
    quiet = [
        ("RESOLVED-A", ["RESOLVED-A"]),
        ("HARDENS", ["HARDENS", "something-else"]),
        ("RESOLVED-A", []),           # one side only -- a gap, not a contradiction
        (None, ["RESOLVED-A"]),
        (None, []),
    ]
    ok = True
    print("  artifact-pair-gate --selftest")
    for t, j in fire:
        got = is_mismatch(t, j)
        print(f"    must FIRE : text={t!r:16s} json={j}  -> {got}")
        ok &= got
    for t, j in quiet:
        got = is_mismatch(t, j)
        print(f"    must be QUIET: text={t!r:16s} json={j}  -> {got}")
        ok &= not got
    # the extractor itself, on the three real shapes seen in the corpus
    shapes = {
        "=== VERDICT ===\nVERDICT: RESOLVED-A\n": "RESOLVED-A",
        "[   860.0s]   FINAL VERDICT: RESOLVED-B\n": "RESOLVED-B",
        "VERDICT: UNRESOLVED (=> EXTERNAL).\n": "UNRESOLVED",
        "no verdict anywhere\n": None,
    }
    for body, want in shapes.items():
        got = text_verdict(body)
        print(f"    extractor : {body.strip()[:40]!r:44s} -> {got!r} (want {want!r})")
        ok &= got == want
    nested = json_verdicts({"a": {"verdict": "X"}, "verdict_under_universal_reading": "Y"})
    print(f"    json keys : nested verdict found={nested} (a non-'verdict' key is ignored)")
    ok &= nested == ["X"]
    print(f"  selftest: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    both, one_side, unreadable, bad = scan()
    for j, e in unreadable:
        print(f"  artifact-pair-gate: UNREADABLE json {j.relative_to(ROOT)} ({e})")
    if bad:
        print(f"  artifact-pair-gate: {len(bad)} of {both} cells CONTRADICT THEMSELVES --")
        for d, txt, js in bad:
            print(f"    {d.relative_to(ROOT)}")
            print(f"      output.txt   VERDICT: {txt}")
            print(f"      results.json verdict(s): {js}")
        print("  Neither artifact is privileged: on the three found in 2026-09, the JSON was")
        print("  stale twice and the TEXT was stale once. Re-run the cell's own compute.py and")
        print("  commit BOTH artifacts from that one run.")
        return 1
    print(f"  artifact-pair-gate: ok ({both} cells carry a verdict on both sides and agree; "
          f"{one_side} carry one on a single side -- a formatting gap, not a contradiction)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
