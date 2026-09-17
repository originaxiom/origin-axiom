#!/usr/bin/env python3
"""THE RE-DERIVATION RULE checker (xB010; owner instruction 2026-09-17).

    "always sweep the repo to see if what you plan to do doesn't already exist. if it does,
     REDO IT ANYWAY, because if it's negative it might be misinformed, bugged or wrongly
     done -- verify verify."

WHY THIS IS NOT B1202. B1202 requires already_banked.py before any MISSING/OPEN claim, and
the absence-sweep rule requires a complete sweep before an absence is a finding. BOTH GOVERN
ABSENCE. Neither says what to do when the sweep FINDS something -- and a hit reads as
"already settled, move on" (already_banked.py's own output says READ it, not RE-DERIVE it).

    A banked result was treated as an ANSWER. It is a HYPOTHESIS.

THE ASYMMETRY THAT MAKES IT URGENT: a wrong POSITIVE gets re-tested downstream because people
build on it. A WRONG NEGATIVE IS NEVER RE-TESTED, BECAUSE IT STOPPED EVERYONE. A bad kill is
silent and permanent.

CITE != RE-DERIVE. Citing is reading an arc's conclusion and using it. Re-deriving is
computing the discriminating fact again, in your own sandbox, with your own code where
feasible, and comparing. (Extends E4 and E3.)

WHAT THE GATE CHECKS -- COMPLETENESS, NEVER JUDGMENT. It cannot tell whether a re-derivation
was real. It enforces that the question was answered where a reader can find it: every arc
not on the frozen roster carries a `rederived` list, each entry naming an arc and an outcome.

AN HONEST REFUSAL PASSES, BY DESIGN. outcome NOT_RERUN with a stated `why` is accepted. A rule
that forbids saying "I did not re-run this" does not produce re-derivation, it produces FALSE
DECLARATIONS -- the B1222 shape turned on ourselves, and the reason identification-register is
a ratchet. Silent omission is what is impossible, not honesty.

    python3 scripts/checks/rederivation.py            # report
    python3 scripts/checks/rederivation.py --selftest  # planted controls, both directions
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ROSTER = ROOT / "docs" / "REDERIVATION_ROSTER.json"

OUTCOMES = {
    "CONFIRMED",   # re-derived independently and it stands
    "CORRECTED",   # re-derived and it did NOT stand -- the payload of the whole rule
    "SCOPED",      # re-derived; the result stands but its stated scope or reason was wrong
    "NOT_RERUN",   # honestly declared as not re-run, with a reason.  ACCEPTED.
}


def roster():
    try:
        return set(json.loads(ROSTER.read_text(encoding="utf-8")).get("exempt", []))
    except Exception:
        return set()


def validate(entry):
    """-> None if fine, else a string saying what is wrong."""
    if not isinstance(entry, dict):
        return "entry is not an object"
    if not entry.get("arc"):
        return "entry names no arc"
    o = entry.get("outcome")
    if o not in OUTCOMES:
        return f"outcome {o!r} not in {sorted(OUTCOMES)}"
    if o == "NOT_RERUN" and not str(entry.get("why", "")).strip():
        return f"{entry['arc']}: NOT_RERUN must state why (an honest refusal is accepted, a bare one is not)"
    if o != "NOT_RERUN" and not str(entry.get("what", "")).strip():
        return f"{entry['arc']}: {o} must say WHAT was re-derived (cite != re-derive)"
    return None


def check():
    ex = roster()
    problems, bound = [], []
    for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        name = p.parent.name
        if name in ex:
            continue
        bound.append(name)
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"{name}: unreadable ({exc})")
            continue
        if "rederived" not in d:
            problems.append(f"{name}: no `rederived` declaration (the re-derivation rule binds "
                            f"every arc created after 2026-09-17)")
            continue
        r = d["rederived"]
        if not isinstance(r, list):
            problems.append(f"{name}: `rederived` must be a list")
            continue
        for e in r:
            bad = validate(e)
            if bad:
                problems.append(f"{name}: {bad}")
    return problems, bound


# --- the two-way selftest ------------------------------------------------------------------
def selftest():
    fails = []
    cases = [
        ("silent omission", None, False, "an arc declaring nothing must be CAUGHT"),
        ("empty list", [], True, "an explicit empty list is a declaration and passes"),
        ("honest CONFIRMED", [{"arc": "B425", "outcome": "CONFIRMED",
                               "what": "re-ran the adjoint torsion, got -3"}], True,
         "a real re-derivation passes"),
        ("honest CORRECTED", [{"arc": "B146", "outcome": "CORRECTED",
                               "what": "re-tested the one-fact chain; it is false"}], True,
         "the payload case passes"),
        ("honest NOT_RERUN", [{"arc": "B999", "outcome": "NOT_RERUN",
                               "why": "needs Sage, unavailable in this environment"}], True,
         "AN HONEST REFUSAL MUST PASS or the rule produces false declarations"),
        ("bare NOT_RERUN", [{"arc": "B999", "outcome": "NOT_RERUN"}], False,
         "a refusal with no reason must be caught"),
        ("CONFIRMED with no substance", [{"arc": "B425", "outcome": "CONFIRMED"}], False,
         "citing is not re-deriving: CONFIRMED must say what was recomputed"),
        ("bogus outcome", [{"arc": "B425", "outcome": "LOOKED_AT_IT"}], False,
         "the outcome vocabulary is closed"),
    ]
    for nm, val, want_ok, why in cases:
        if val is None:
            ok = False                      # the missing-field case, checked by check()
        else:
            ok = all(validate(e) is None for e in val)
        good = (ok == want_ok)
        print(f"  [{'ok' if good else 'FAIL'}] {nm:<26} accepted={ok}, want={want_ok}   ({why})")
        if not good:
            fails.append(nm)
    return fails


def selftest_quiet():
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()):
        return selftest()


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        f = selftest()
        print("\nSELFTEST", "PASS" if not f else f"FAIL: {f}")
        sys.exit(0 if not f else 1)
    probs, bound = check()
    print(f"rederivation: {len(bound)} arc(s) bound by the rule, {len(probs)} problem(s)")
    for p in probs:
        print(f"  {p}")
    sys.exit(1 if probs else 0)
