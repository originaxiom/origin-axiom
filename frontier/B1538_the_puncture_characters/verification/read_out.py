#!/usr/bin/env python3
"""B1538 -- THE READ-OUT: the sealed predictions read from the run's records, once (PREREGISTRATION section 7).

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

Inputs: identity.json (the banked identity, re-run before the run), run_L.jsonl (Part L) and, if present, run_F.jsonl (Part F).
Every prediction is decided here from the records; nothing is judged by hand.

  P1  the identity held: controls K0-K8 all hold, and every sealed file hashes as sealed.
  P2  route P agrees with route W at every root read (two primes) and at every mu_12 check.
  P3  route T agrees with the sum of n over the powers at every hit it reads, and reads at least one hit if any exists.
  P4  some puncture character of population A has n >= 1.
  P5  no puncture character of population A has n >= 2.
  P6  no puncture character on m004's covers has n >= 1.
  P7  Part F: at every candidate (a puncture chi = nu^4 with n(chi) >= 2), no member nu has capL2 >= 2.  Vacuous if Part L has
      no candidate.
  P8  the verdict: no finite-order member nu on a cover of population A, with nu^4 among the characters read, has
      min(capW, capL2) >= 2 (Theorem C: no count of two or more generations there)."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_rows(name):
    p = HERE / name
    if not p.exists():
        return None
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def evaluate(ident, L, Fr, say=print):
    """the predictions from the records (pure: read_out_selftest.py calls it on synthetic rows)"""
    assert L is not None, "Part L has no records"
    chunks = {}
    for r in L:
        chunks.setdefault(r["cover"], {"want": r["chunks"], "have": set(), "read": True})
        chunks[r["cover"]]["have"].add(r["chunk"])
        chunks[r["cover"]]["read"] &= r["read"]
    complete = {c for c, v in chunks.items() if v["read"] and v["have"] == set(range(v["want"]))}
    out = {"covers": len(chunks), "covers read in full": len(complete),
           "covers incomplete": sorted(set(chunks) - complete)}
    hits = [dict(h, cover=r["cover"], state=r["state"]) for r in L if r["read"] for h in r["hits"]]
    out["puncture orbits read"] = sum(r.get("puncture orbits", 0) for r in L)
    out["puncture characters read"] = sum(r.get("puncture characters", 0) for r in L)
    out["hits (n >= 1), Galois orbits"] = len(hits)
    out["n distribution"] = {}
    for h in hits:
        out["n distribution"][str(h["n"])] = out["n distribution"].get(str(h["n"]), 0) + 1
    p_dis = sum(len(r["route P"]["disagree"]) for r in L if r["read"])
    p_reads = sum(r["route P"]["reads"] for r in L if r["read"])
    t_dis = sum(len(r["route T"]["disagree"]) for r in L if r["read"])
    t_reads = sum(r["route T"]["reads"] for r in L if r["read"])
    out["route P"] = {"reads": p_reads, "disagree": p_dis}
    out["route T"] = {"reads": t_reads, "disagree": t_dis,
                      "skipped": sum(r["route T"]["skipped"] for r in L if r["read"])}
    pred = {}
    pred["P1"] = bool(ident.get("identity holds"))
    pred["P2"] = p_dis == 0 and p_reads > 0
    pred["P3"] = t_dis == 0 and (t_reads > 0 or not hits)
    pred["P4"] = len(hits) > 0
    maxn = max([h["n"] for h in hits], default=0)
    out["max n"] = maxn
    pred["P5"] = maxn <= 1
    pred["P6"] = not any(h["state"] == "m004" for h in hits)
    out["every cover read"] = len(complete) == len(chunks)
    cands = [h for h in hits if h["n"] >= 2]
    out["candidates (n >= 2)"] = len(cands)
    if not cands:
        pred["P7"] = True
        out["P7"] = "vacuous: no candidate"
        pred["P8"] = True
    elif Fr is None:
        pred["P7"] = None
        pred["P8"] = None
        out["P7"] = "Part F not yet run"
    else:
        members = [f for f in Fr if f.get("member")]
        two = [f for f in members if f["R"]["capL2"] >= 2 or f["P4"]["capL2"] >= 2]
        agree = all(f["h1 R"] == f["h1 P4"] for f in Fr) and all(f["R"] == f["P4"] for f in members)
        out["Part F"] = {"readings": len(Fr), "members": len(members), "members with capL2 >= 2": len(two),
                         "routes agree": agree}
        pred["P7"] = not two
        pred["P8"] = not [f for f in members for k in ("R", "P4")
                          if min(f[k]["capW"], f[k]["capL2"]) >= 2]
    out["predictions"] = pred
    for k in sorted(pred):
        say(f"{k}: {pred[k]}")
    say(json.dumps({k: v for k, v in out.items() if k != "predictions"}))
    return out


def main():
    log = []

    def say(s):
        log.append(s)
        print(s)

    ident = json.loads((HERE / "identity.json").read_text())
    out = evaluate(ident, load_rows("run_L.jsonl"), load_rows("run_F.jsonl"), say)
    out["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(out, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return out


if __name__ == "__main__":
    main()
