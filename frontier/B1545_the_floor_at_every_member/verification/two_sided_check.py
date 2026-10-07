#!/usr/bin/env python3
"""B1545, update of 2026-10-07: the ceiling beside the floor, read on this arc's own banked record.

Lemma F' bounds I(W1) from below. The same identity bounds it from above:
    I(W1) = -b0 + h0(dN; W1*) - r1(W1)        (step (1))
    h0(dN; W1*) = 2 m_A + m_B                  (step (2))
so, as r1(W1) >= 0,
    k - m_A - b0 <= I(W1) <= 2 m_A + m_B - b0,
with the ceiling attained exactly when no class of W1 restricts non-trivially to the boundary.

This script reads members_check.json (288 readings, route R) and records, at every reading:
  - the floor and the ceiling;
  - the form |I(W1)| <= m_A + b0, which does not follow from the floor (the floor in the other order bounds I(W2),
    not I(W1)), and the readings where it fails;
  - the identity of step (1), recomputed from the recorded terms.
It writes two_sided_check.json beside itself. Nothing is recomputed in cohomology: the record is the banked one."""
import collections
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def evaluate(rows):
    out = dict(n=len(rows), floor_fails=0, ceiling_fails=0, ceiling_attained=0, identity_fails=0,
               abs_form_fails=0, abs_form_fail_cases=[], all_cusps_C=dict(readings=0, I_values=[]),
               gap_histogram={})
    cases = collections.Counter()
    gaps = collections.Counter()
    for r in rows:
        mA, mB, b0, k, I = len(r["A"]), len(r["B"]), r["b0"], r["k"], r["I(W)"]
        floor, ceiling = k - mA - b0, 2 * mA + mB - b0
        out["floor_fails"] += I < floor
        out["ceiling_fails"] += I > ceiling
        out["ceiling_attained"] += I == ceiling
        out["identity_fails"] += I != -b0 + r["h0(dN;W*)"] - r["r1(W)"] or r["h0(dN;W*)"] != 2 * mA + mB
        gaps[ceiling - I] += 1
        if abs(I) > mA + b0:
            out["abs_form_fails"] += 1
            cases[(r["cover"], mA, mB, b0, k, I)] += 1
        if mA == 0 and mB == 0:
            out["all_cusps_C"]["readings"] += 1
            out["all_cusps_C"]["I_values"] = sorted(set(out["all_cusps_C"]["I_values"]) | {I})
    out["abs_form_fail_cases"] = [dict(cover=c, m_A=a, m_B=b, b0=z, k=kk, I_W1=i, readings=n,
                                       ceiling=2 * a + b - z, abs_form_bound=a + z)
                                  for (c, a, b, z, kk, i), n in sorted(cases.items())]
    out["gap_histogram"] = {str(g): gaps[g] for g in sorted(gaps)}
    return out


def main():
    rec = json.loads((HERE / "members_check.json").read_text())
    out = evaluate(rec["rows"])
    out["source"] = "members_check.json (this arc's banked record, route R)"
    out["statement"] = ("k - m_A - b0 <= I(W1) <= 2 m_A + m_B - b0 at every finite-order member and class; "
                        "|I(W1)| <= m_A + b0 is not a consequence of the floor")
    (HERE / "two_sided_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in ("n", "floor_fails", "ceiling_fails", "ceiling_attained", "identity_fails",
                                          "abs_form_fails")}))


if __name__ == "__main__":
    main()
