#!/usr/bin/env python3
"""xB008 cells G1-G5, exactly as sealed in PREREGISTRATION.md (sha256 30bb937b...,
commit 91c9b94, pushed BEFORE the gate was written).  Each cell asserts its mathematics."""
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]


def _mod(p):
    spec = importlib.util.spec_from_file_location("_m", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


LK = _mod(ROOT / "scripts" / "checks" / "linkage_kills.py")


def G1():
    """THE EFFICACY CELL, and the reason this arc was pre-registered at all."""
    k = LK.adjudicate(LK.Q3_ORIGINAL)[1]
    print("G1       xB005's Q3, AS IT ORIGINALLY STOOD before Addendum 1, presented to the gate")
    print(f"         class = {k}   (C means the gate REDS on it)")
    assert k == "C", ("the gate does not catch the single error it was designed from. "
                      "It is theatre. Report that and do NOT ship it.")
    print("G1 PASS  THE GATE CATCHES THE ERROR IT WAS DESIGNED FROM.")


def G2():
    k = LK.adjudicate(LK.Q3_CORRECTED)[1]
    print(f"\nG2       the CORRECTED Q3 (Addendum 1's text, which names the dissociation)")
    print(f"         class = {k}   (anything but C means the gate PASSES it)")
    assert k != "C", "the gate cannot tell a defect from its repair; it must not ship"
    print("G2 PASS  the repair is recognised -- the gate is not merely keyword-allergic.")


def G3():
    out = subprocess.run([sys.executable, str(ROOT/"scripts"/"gates"/"gates.py")],
                         capture_output=True, text=True, timeout=1800).stdout
    lines = out.splitlines()
    n_pass = sum(1 for l in lines if l.startswith("  PASS"))
    n_fail = sum(1 for l in lines if l.startswith("  FAIL"))
    print(f"\nG3       the present tree: {n_pass} PASS, {n_fail} FAIL")
    assert any(l.startswith("  PASS  linkage-kills") for l in lines), "the new gate is not green"
    assert n_fail == 0, f"the tree reds: {[l for l in out.splitlines() if 'FAIL' in l][:3]}"
    assert n_pass == 34, f"expected 34 gates (33 + this one), got {n_pass}"
    print("G3 PASS  33/33 became 34/34; nothing retroactively red.")


def G4():
    print("\nG4       the two-way self-test")
    fails = LK.selftest_quiet()
    for nm, blob, want in (("planted E82 kill", LK.PLANT_BAD, "C"),
                           ("sound: named theorem", LK.PLANT_OK_THM, "A"),
                           ("sound: computed base rate", LK.PLANT_OK_RATE, "R")):
        print(f"         {nm:<28} -> {LK.adjudicate(blob)[1]} (want {want})")
    f = ROOT/"frontier"/"B727_base_rate_the_structure"/"FINDINGS.md"
    hits, k, _ = LK.adjudicate(f.read_text(encoding="utf-8", errors="replace"))
    print(f"         {'B727, the record''s sound form':<28} -> trips {bool(hits)}, class {k} (want not C)")
    assert not fails, fails
    assert hits and k != "C"
    print("G4 PASS  catches a planted E82 kill AND clears B727 -- calibrated both ways.")


def G5():
    novel, hits, frozen = LK.check()
    print(f"\nG5       the ratchet: {len(hits)} hits, {len(frozen)} frozen, {len(novel)} new")
    assert not novel
    real = LK.baseline
    try:
        LK.baseline = lambda: set(list(frozen)[1:])
        novel2, _, _ = LK.check()
        print(f"         unfreeze one entry -> {len(novel2)} new (the gate must RED)")
        assert novel2
    finally:
        LK.baseline = real
    assert not LK.check()[0]
    print("G5 PASS  a new unexhibited linkage kill reds; restoring returns to green.")
    d = json.loads((ROOT/"docs"/"LINKAGE_BASELINE.json").read_text(encoding="utf-8"))
    n_e82 = sum(1 for v in d["adjudication"].values() if v["xB006_class"] == "E82")
    print(f"\n         and the baseline is HONEST about itself: of {len(d['frozen'])} frozen "
          f"entries, xB006 read every one and found {n_e82} genuine E82 candidates.")
    print("         Reporting the raw count as 'wrong kills' would be the same over-reach")
    print("         the instrument audits, so the adjudication ships WITH the baseline.")


if __name__ == "__main__":
    G1(); G2(); G3(); G4(); G5()
    print("\nVERIFIED")
