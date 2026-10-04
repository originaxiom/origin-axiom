#!/usr/bin/env python3
"""B1538 -- THE SCOPED READ-OUT (PREREGISTRATION_ADDENDUM.md section 3): P7' and P8' on the in-scope candidates, by the sealed
evaluate.  Run once, after the sealed read_out.py --record has run once.

    python3 read_out_scoped.py [--record]    ->  read_out_scoped.json, read_out_scoped_log.txt

Inputs: the sealed read-out's (identity.json; controls.json's K10 and K11; run_L.jsonl; run_F.jsonl, which is the sealed
partial record followed by Part F''s rows), and the scope, recomputed by run_f_scoped.py's candidates() (its aggregates must
equal the addendum's).  ONE call of the sealed read_out.evaluate, loaded by path and unchanged, on:
  - Part L's rows with every out-of-scope candidate's hit removed and nothing else changed, so that the call's candidates are
    exactly the in-scope ones;
  - run_F.jsonl's rows at in-scope candidates.
Only that call's P7 and P8 (as P7', P8') and its Part F block are kept.  Its other values are discarded: they are computed on
edited Part L rows and mean nothing; the sealed read-out's own predictions stand.  The verdict (the addendum's section 4) is
decided here from the sealed read_out.json and P8', and written with them."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(alias, name):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


def verdict(sealed, p8s):
    """the addendum's section 4, from the sealed read-out's predictions and P8'.  P8' False with P8 not False cannot happen
    (the sealed read-out reads every in-scope row too); it is recorded as OPEN, for the cause to be found."""
    p = sealed["predictions"]
    if not all(p[k] is True for k in ("P1", "P2", "P3", "P9")):
        return "OPEN"                                   # until the cause is resolved and recorded (sealed section 9)
    if p["P8"] is False:
        return "PROVED"                                 # room for two at some member read, in or out of scope
    if p["P8"] is None and p8s is True:
        return "NEGATIVE"                               # scoped: the in-scope candidates; the others are OPEN
    if p["P8"] is True and p8s is True:
        return "NEGATIVE"                               # the whole population (not expected: Part F is incomplete)
    return "OPEN"


def main():
    log = []

    def say(s):
        log.append(s)
        print(s)
    RO = load("b1538_read_out_sealed", "read_out.py")
    DR = load("b1538_run_f_scoped", "run_f_scoped.py")
    sealed = json.loads((HERE / "read_out.json").read_text())       # the sealed read-out, run once before this
    cands = DR.candidates(DR.sealed_run())
    agg = DR.aggregates(cands)
    assert agg == DR.SEALED, "the scope's aggregates differ from the addendum's"
    out_keys = {(c["key"][0], tuple(c["key"][1]), c["key"][2], tuple(c["key"][3])) for c in cands if not c["in scope"]}
    in_keys = {(c["key"][0], tuple(c["key"][1]), c["key"][2], tuple(c["key"][3])) for c in cands if c["in scope"]}
    L = RO.load_rows("run_L.jsonl")
    removed = 0
    for r in L:
        if r["read"]:
            keep = [h for h in r["hits"] if (r["cover"], tuple(h["zeta"]), h["m"], tuple(h["s"])) not in out_keys]
            removed += len(r["hits"]) - len(keep)
            r["hits"] = keep
    Fr = [f for f in RO.load_rows("run_F.jsonl")
          if (f["cover"], tuple(f["chi"]["zeta"]), f["chi"]["m"], tuple(f["chi"]["s"])) in in_keys]
    ident = json.loads((HERE / "identity.json").read_text())
    ctl = json.loads((HERE / "controls.json").read_text())
    discarded = []
    res = RO.evaluate(ident, L, Fr, discarded.append, ctl["K10"]["covers"], ctl["K11"]["manifest"])
    p7s, p8s = res["predictions"]["P7"], res["predictions"]["P8"]
    out = {"scope": agg, "out-of-scope hits removed from Part L's rows (that call only)": removed,
           "in-scope Part F rows": len(Fr), "Part F (in scope)": res["Part F"],
           "Part L read in full (the call's coverage)": res["every cover read"],
           "routes agree (in scope)": res["Part F"]["routes agree"] if isinstance(res["Part F"], dict) else None,
           "P7'": p7s, "P8'": p8s,
           "the sealed read-out": {"P7": sealed["predictions"]["P7"], "P8": sealed["predictions"]["P8"],
                                   "P1": sealed["predictions"]["P1"], "P2": sealed["predictions"]["P2"],
                                   "P3": sealed["predictions"]["P3"], "P9": sealed["predictions"]["P9"]},
           "verdict": verdict(sealed, p8s)}
    say(f"P7': {p7s}")
    say(f"P8': {p8s}")
    say(f"verdict: {out['verdict']}")
    say(json.dumps({k: v for k, v in out.items() if k not in ("P7'", "P8'", "verdict")}))
    out["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out_scoped.json").write_text(json.dumps(out, indent=1) + "\n")
        (HERE / "read_out_scoped_log.txt").write_text("\n".join(log) + "\n")
    return out


if __name__ == "__main__":
    main()
