#!/usr/bin/env python3
"""THE LAST TARGET -- t12835, the one manifold B1330 actually left uncomputed.

Seal: outside_bench/seals/THE_LAST_TARGET_PREREG.md
      sha256 fe869b6b238eaf03173afd0a98452c62b62166047f35187bf890c58744ed5cf4

BENCH ERROR #34's fix, applied: read the sibling branch BEFORE calling anything
unrun.  It paid -- B1330's "NOT DONE: s958, t12833 and t12835 ... are named,
not computed" is itself STALE.  Two addenda dated 2026-09-11 computed s958 and
t12833.  Only t12835 was left "(pending at write time)".

THE COMPUTATION IS B1330's OWN CODE, VENDORED BYTE-IDENTICAL to
  origin/claude/paper-verification-ufp0zn:frontier/B1330_the_best_case_object/verification/
in outside_bench/certificates/lib/b1330/ (see PROVENANCE.md).  No line modified.
This file does not recompute anything; it RUNS that code and CHECKS it.

V1  s958 and t12833 must reproduce B1330's banked numbers, or the cell stops.
V2  relator images printed before any twisted computation (B1330's own lesson:
    "A -I lift silently invalidates every odd-weight germ").
V3  T5 asserted on every sector: t0 = 0 => I = 0.  A t0 = 0 with I != 0 is
    IMPOSSIBLE and fails the cell -- that is how B1330 caught its own false
    NON-ZERO INDEX: 10.
V4  in-domain population printed before any conclusion; >= 1 required.
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW = os.path.join(ROOT, "outside_bench", "outputs", "the_last_target_raw.txt")
DUP = os.path.join(ROOT, "outside_bench", "outputs", "the_last_target_t12835.txt")

# B1330 ADDENDUM 2 (2026-09-11), banked -- V1's targets
BANKED = {
    "s958":   {"lift": "I",  "nonzero": 0},
    "t12833": {"lift": "-I", "nonzero": 0, "t0_max": 4, "t0_ge2": 12, "sectors": 16},
}


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def parse(raw):
    """Parse the vendored script's output into per-manifold blocks."""
    out = {}
    cur = None
    for line in raw.splitlines():
        m = re.match(r"=== (\S+) === chiral=(\S+)", line.strip())
        if m:
            cur = {"name": m.group(1), "chiral": m.group(2) == "True",
                   "relators": [], "validated": None, "chars": None,
                   "sectors": None, "dist": None, "t0_ge2": None, "nonzero": None,
                   "nonzero_rows": []}
            out[m.group(1)] = cur
            continue
        if cur is None:
            continue
        m = re.match(r"relator '(.+)' -> (.+)$", line.strip())
        if m:
            cur["relators"].append((m.group(1), m.group(2).strip()))
        elif line.strip().startswith("RELATORS VALIDATED:"):
            cur["validated"] = line.strip().split(":")[1].strip() == "True"
        elif "order-3 cusp-trivial characters:" in line:
            cur["chars"] = int(line.strip().split(":")[1])
        elif "EXACT in-domain sectors:" in line:
            cur["sectors"] = int(line.strip().split(":")[1])
        elif line.strip().startswith("(t0,I):"):
            cur["dist"] = line.strip().split(":", 1)[1].strip()
        elif line.strip().startswith("t0>=2:"):
            cur["t0_ge2"] = int(line.strip().split(":")[1])
        elif "NON-ZERO INDEX:" in line:
            cur["nonzero"] = int(line.strip().split(":")[1])
        elif line.strip().startswith("Sym"):
            cur["nonzero_rows"].append(line.strip())
    return out


def main() -> int:
    print("=" * 78)
    print(" THE LAST TARGET -- t12835")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/THE_LAST_TARGET_PREREG.md
    sha256 fe869b6b238eaf03173afd0a98452c62b62166047f35187bf890c58744ed5cf4""")
    failures = []

    if not os.path.exists(RAW):
        print(f"FATAL: {RAW} missing -- run the vendored final_index.py first")
        return 2
    with open(RAW, encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    res = parse(raw)
    # t12835 was run TWICE, in two independent processes from the same vendored
    # script: once inside the three-manifold run and once alone.  The alone run
    # is read here; agreement between them is control V5.
    dup = {}
    if os.path.exists(DUP):
        with open(DUP, encoding="utf-8", errors="replace") as fh:
            dup = parse(fh.read())
    # KEEP THE TWO PARSES SEPARATE.  A first version merged dup into res and
    # then "compared" them -- an object against itself, a control that could
    # not fail (MB12).  res_own is the three-manifold run's own block; dup is
    # the standalone run's.  They are only ever compared, never merged.
    res_own = {k: v for k, v in res.items()}
    if res.get("t12835", {}).get("nonzero") is None and \
       dup.get("t12835", {}).get("nonzero") is not None:
        res["t12835"] = dup["t12835"]   # for reporting the RESULT only

    rule("WHAT WAS ALREADY DONE, and why this cell is one manifold and not three")
    print("""    B1330's closing line -- "NOT DONE: s958, t12833 and t12835 ... are named,
    not computed" -- is STALE.  Its own addenda of 2026-09-11 report:
      s958    20 exact in-domain sectors (Q(omega) and Q(zeta_12)), 8 at
              t0 >= 2, every index ZERO
      t12833  16 exact sectors, t0 to 4, 12 at t0 >= 2, ZERO
      t12835  "(pending at write time; its odd-power non-zeros are the same
              artifact)"
    So ONE target remained.  Reading the sibling branch before running is
    BENCH ERROR #34's fix, and it saved recomputing two settled manifolds.""")

    # ------------------------------------------------------------------ V2
    rule("CONTROL V2 -- relator images, printed before any twisted computation")
    print("""    B1330's own lesson, verbatim: "Always print the relator images before
    trusting a twisted computation.  A -I lift silently invalidates every
    odd-weight germ."  The vendored GERMS list is EVEN-ONLY for that reason.
""")
    ok_v2 = True
    for nm in ("s958", "t12833", "t12835"):
        r = res.get(nm)
        if not r:
            print(f"    {nm:8s} ABSENT from the run")
            ok_v2 = False
            continue
        lifts = {im for _, im in r["relators"]}
        lift = "I" if lifts == {"I"} else ("-I" if "-I" in lifts else "MIXED/BAD")
        print(f"    {nm:8s} chiral={r['chiral']}  lift={lift:5s} validated={r['validated']}"
              f"  order-3 chars={r['chars']}")
        for w, im in r["relators"]:
            print(f"             {w!r} -> {im}")
        if not r["validated"]:
            ok_v2 = False
    print(f"    -> {'PASS' if ok_v2 else 'FAIL'} (every relator must be exactly +-I)")
    if not ok_v2:
        failures.append("V2")

    # ------------------------------------------------------------------ V1
    rule("CONTROL V1 -- s958 and t12833 must reproduce B1330's banked numbers")
    ok_v1 = True
    for nm, want in BANKED.items():
        r = res.get(nm)
        if not r:
            print(f"    {nm}: ABSENT")
            ok_v1 = False
            continue
        checks = [("non-zero index", r["nonzero"], want["nonzero"])]
        if "sectors" in want:
            checks.append(("in-domain sectors", r["sectors"], want["sectors"]))
        if "t0_ge2" in want:
            checks.append(("t0 >= 2", r["t0_ge2"], want["t0_ge2"]))
        for label, got, exp in checks:
            good = (got == exp)
            print(f"    {nm:8s} {label:18s} got {got}  banked {exp}  {'ok' if good else 'MISMATCH'}")
            ok_v1 = ok_v1 and good
    print(f"    -> {'PASS' if ok_v1 else 'FAIL'}")
    if not ok_v1:
        failures.append("V1")
        print("""    A V1 failure STOPS THE CELL: the method drifted in transit, and a fresh
    null on t12835 would mean nothing.""")

    # ------------------------------------------------------------------ V3/V4
    rule("CONTROL V3 -- T5 asserted on every sector: t0 = 0 => I = 0")
    print("""    This is exactly how B1330 caught its own false NON-ZERO INDEX: 10.
    T5: t1 = t0 + t0* = 0 bounds r1 = 0, so t0 = 0 forces I = 0.  A sector
    reporting t0 = 0 with I != 0 is IMPOSSIBLE -- the computation is wrong,
    not the theorem.
""")
    ok_v3 = True
    for nm, r in res.items():
        d = r.get("dist")
        if not d:
            continue
        bad = re.findall(r"\(0,\s*(-?\d+)\)", d)
        viol = [b for b in bad if int(b) != 0]
        print(f"    {nm:8s} (t0,I) distribution: {d}")
        print(f"             t0=0 sectors with I != 0: {len(viol)}")
        if viol:
            ok_v3 = False
    print(f"    -> {'PASS' if ok_v3 else 'FAIL'}")
    if not ok_v3:
        failures.append("V3")

    rule("CONTROL V4 -- in-domain population, printed before any conclusion")
    ok_v4 = True
    for nm in ("s958", "t12833", "t12835"):
        r = res.get(nm)
        n = r.get("sectors") if r else None
        print(f"    {nm:8s} exact in-domain sectors: {n}   t0>=2: {r.get('t0_ge2') if r else None}")
        if not n:
            ok_v4 = False
    print(f"    -> {'PASS' if ok_v4 else 'FAIL'} (every manifold needs >= 1 in-domain sector)")
    if not ok_v4:
        failures.append("V4")

    # ------------------------------------------------------------------ outcome
    rule("CONTROL V5 -- t12835 was run TWICE, independently; the runs must agree")
    a = res_own.get("t12835", {})     # the three-manifold run's OWN block
    b = dup.get("t12835", {})         # the standalone run's block
    fields = ("sectors", "t0_ge2", "nonzero", "dist")
    print("    run-1 = the three-manifold run's own t12835 block")
    print("    run-2 = the standalone t12835 run  (two separate processes)")
    if a.get("nonzero") is None or b.get("nonzero") is None:
        which = "run-1" if a.get("nonzero") is None else "run-2"
        print(f"    {which} has NOT finished its t12835 block.")
        print("    -> PENDING, not agreement.  A self-comparison is not a control;")
        print("       an earlier version of this cell merged the two and compared")
        print("       an object to itself, which passed vacuously.  Reported as")
        print("       pending until two independent blocks exist.")
    else:
        same = all(a.get(f) == b.get(f) for f in fields)
        for f in fields:
            print(f"    {f:9s} run-1 {str(a.get(f)):28s} run-2 {str(b.get(f))}")
        print(f"    -> {'PASS' if same else 'FAIL'} (independent runs must agree)")
        if not same:
            failures.append("V5")

    rule("THE PREREGISTERED OUTCOME -- t12835")
    t = res.get("t12835")
    if not t:
        print("    t12835 ABSENT from the run.")
        failures.append("t12835-absent")
        outcome = "-"
    else:
        print(f"    lift                    : {'-I (projective)' if any(im == '-I' for _, im in t['relators']) else 'I (genuine)'}")
        print(f"    order-3 cusp-trivial chars: {t['chars']}")
        print(f"    exact in-domain sectors : {t['sectors']}")
        print(f"    (t0, I) distribution    : {t['dist']}")
        print(f"    sectors at t0 >= 2      : {t['t0_ge2']}")
        print(f"    NON-ZERO INDEX          : {t['nonzero']}")
        for row in t["nonzero_rows"]:
            print(f"      {row}")
        outcome = "A" if t["nonzero"] == 0 else "B"
        print(f"\n    -> OUTCOME {outcome}")
        if outcome == "A":
            print("""    Every in-domain sector vanishes.  B1330's "NOT DONE" line is discharged
    and all four best-case objects now agree.""")
        else:
            print("""    A NON-ZERO INDEX with relators validated as +-I, even germs only, and
    T5 intact.  Reported with its germ, character and identity checks.""")

    rule("WHAT THIS IS WORTH -- stated in the seal BEFORE the run")
    print("""    A sixth zero is BOOKKEEPING, NOT NEWS, and the seal says so in advance.
    Since B1330 was written:
      B1334 (PROVED)  the first proof of I = 0 in the record, on a stated
                      domain: for every chi in S^0, I(W (x) chi) = 0 whenever W
                      restricts to dM self-dually -- and Sym^m of an SL2
                      holonomy qualifies.
      B1331 (OPEN)    the reduction: I = 0 follows from ISOTROPY ALONE, and
                      L_V and L_{V*} are THE SAME SUBSPACE.
      B1332 (OPEN)    isotropy broadened and NOT broken -- six further
                      one-cusped manifolds, geometric holonomy, char 0 at 40
                      digits, 128 genuine scalar equations, ALL ISOTROPIC.
    The live question is no longer "scan another manifold".  It is ISOTROPY.""")

    rule("VERDICT")
    print(f"    t12835 = OUTCOME {outcome}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: nothing about generations -- I-26 is UNEARNED, and until it
    is earned every generation-count statement in the corpus is conditional on
    it.  No net chiral spectrum.  No value.  Gate 5 untouched.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
