#!/usr/bin/env python3
"""B1538 -- THE READ-OUT: the sealed predictions read from the run's records, once (PREREGISTRATION section 7).

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

Inputs: identity.json (the banked identity, re-run before the run), run_L.jsonl (Part L), if present run_F.jsonl (Part F), and
controls.json's K10 (Proposition H's character zeta_H on each cover with D = Z^2 / 2Z^2, located by structure alone) and K11
(the population manifest: every cover, its chunks and its puncture orbits).
Every prediction is decided here from the records; nothing is judged by hand.  A population-wide prediction is True only on
complete records (every manifest chunk exactly once, the orbit counts matching; Part F with every planned reading), False on
any refuting row, and None otherwise: missing, duplicate or incomplete records never certify a negative (R87).

  P1  the identity held: controls K0-K10 all hold, and every sealed file hashes as sealed.
  P2  route P agrees with route W at every root read (two primes) and at every mu_12 check.
  P3  route T agrees with the sum of n over the powers at every hit it reads, and reads at least one hit if any exists.
  P4  some puncture character of population A has n >= 1.
  P5  no puncture character of population A has n >= 2.
  P6  no puncture character on m004's covers has n >= 1.
  P7  Part F: at every candidate (a puncture chi = nu^4 with n(chi) >= 2), no member nu has capL2 >= 2.  Vacuous if Part L has
      no candidate.
  P8  the verdict: no finite-order member nu on a cover of population A, with nu^4 among the characters read, has
      min(capW, capL2) >= 2 (Theorem C: no count of two or more generations there).
  P9  Proposition H: on every cover of K10, the sum over the roots of unity s of n(zeta_H, s) is 4.
  P10 Proposition H: on every cover of K10 where tau acts on Q_8 non-trivially, n(zeta_H, s) <= 2 at every s.
  P11 Proposition H: on every cover of K10 where tau acts on Q_8 as the identity, n(zeta_H, s) is even at every s.
  Each of P9-P11 is None unless every cover it reads was read in full."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_rows(name):
    p = HERE / name
    if not p.exists():
        return None
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def evaluate(ident, L, Fr, say=print, hcov=None, manifest=None):
    """the predictions from the records (pure: control K9 calls it on synthetic rows).
    hcov: K10's covers, {cover id: {"ez", "m", "acts on Q8 as the identity", ...}}, or None.
    manifest: K11's population, {cover id: {"chunks", "puncture orbits", ...}}, or None.
    Coverage (the audit lane's R87): the records are complete only if every manifest cover's every chunk appears exactly once,
    read, with no other cover, and each cover's puncture orbits sum to the manifest's.  A prediction that a found row can
    refute is False on that row, whatever the coverage; a population-wide one is True only on complete records, else None.
    Part F is complete only if every candidate has its header row, its fourth roots counted twice alike (enumerated and by the
    Smith form), and exactly its planned readings, with no other."""
    assert L is not None, "Part L has no records"
    seen, dup = {}, []
    for r in L:
        key = (r["cover"], r["chunk"])
        if key in seen:
            dup.append(list(key))
        seen[key] = r
    by_cover = {}
    for (c, _), r in seen.items():
        by_cover.setdefault(c, []).append(r)
    duplicated = {c for c, _ in dup}
    problems = {"duplicate rows": dup, "unexpected covers": [], "chunk mismatch": {}, "not read": [],
                "orbit count mismatch": {}}
    covered = set()
    if manifest is None:
        for c, rows in by_cover.items():
            want = rows[0]["chunks"]
            if (c not in duplicated and all(r["read"] for r in rows) and all(r["chunks"] == want for r in rows)
                    and {r["chunk"] for r in rows} == set(range(want))):
                covered.add(c)
    else:
        problems["unexpected covers"] = sorted(set(by_cover) - set(manifest))
        for c, exp in sorted(manifest.items()):
            rows = by_cover.get(c, [])
            have = {r["chunk"] for r in rows}
            if have != set(range(exp["chunks"])) or any(r["chunks"] != exp["chunks"] for r in rows):
                problems["chunk mismatch"][c] = {"want": exp["chunks"], "have": sorted(have)}
            elif not all(r["read"] for r in rows):
                problems["not read"].append(c)
            elif sum(r.get("puncture orbits", 0) for r in rows) != exp["puncture orbits"]:
                problems["orbit count mismatch"][c] = [sum(r.get("puncture orbits", 0) for r in rows),
                                                       exp["puncture orbits"]]
            elif c not in duplicated:
                covered.add(c)
    complete = (manifest is not None and not dup and not problems["unexpected covers"]
                and covered == set(manifest))
    out = {"covers in the records": len(by_cover), "covers read in full": len(covered),
           "covers expected": None if manifest is None else len(manifest),
           "coverage problems": {k: v for k, v in problems.items() if v}, "every cover read": complete}
    hits = [dict(h, cover=r["cover"], state=r["state"]) for r in seen.values() if r["read"] for h in r["hits"]]
    out["puncture orbits read"] = sum(r.get("puncture orbits", 0) for r in seen.values())
    out["puncture characters read"] = sum(r.get("puncture characters", 0) for r in seen.values())
    out["hits (n >= 1), Galois orbits"] = len(hits)
    out["n distribution"] = {}
    for h in hits:
        out["n distribution"][str(h["n"])] = out["n distribution"].get(str(h["n"]), 0) + 1
    rd = [r for r in seen.values() if r["read"]]
    p_dis = sum(len(r["route P"]["disagree"]) for r in rd)
    p_reads = sum(r["route P"]["reads"] for r in rd)
    t_dis = sum(len(r["route T"]["disagree"]) for r in rd)
    t_reads = sum(r["route T"]["reads"] for r in rd)
    out["route P"] = {"reads": p_reads, "disagree": p_dis}
    out["route T"] = {"reads": t_reads, "disagree": t_dis, "skipped": sum(r["route T"]["skipped"] for r in rd)}

    def whole(found_false, fallback=True):
        """False on a refuting row; else the fallback on complete records; else None"""
        return False if found_false else (fallback if complete else None)
    pred = {}
    pred["P1"] = bool(ident.get("identity holds"))
    pred["P2"] = whole(p_dis > 0, p_reads > 0)
    pred["P3"] = whole(t_dis > 0, t_reads > 0 or not hits)
    pred["P4"] = True if hits else (False if complete else None)
    maxn = max([h["n"] for h in hits], default=0)
    out["max n"] = maxn
    pred["P5"] = whole(maxn >= 2)
    pred["P6"] = whole(any(h["state"] == "m004" for h in hits))
    cands = [h for h in hits if h["n"] >= 2]
    out["candidates (n >= 2)"] = len(cands)
    ckeys = {(h["cover"], tuple(h["zeta"]), h["m"], tuple(h["s"])) for h in cands}
    if not cands:
        pred["P7"] = whole(False)
        pred["P8"] = whole(False)
        out["Part F"] = "no candidate"
    elif Fr is None:
        pred["P7"] = None
        pred["P8"] = None
        out["Part F"] = "not yet run"
    else:
        heads, reads, fdup, fcount = {}, {}, [], []
        for f in Fr:
            ck = (f["cover"], tuple(f["chi"]["zeta"]), f["chi"]["m"], tuple(f["chi"]["s"]))
            if f.get("kind") == "candidate":
                if ck in heads:
                    fdup.append(["candidate", list(map(str, ck))])
                heads[ck] = f["planned"]
                if f.get("fourth roots") != f.get("fourth roots by the Smith form") or f["planned"] != 4 * f.get("fourth roots", -1):
                    fcount.append(list(map(str, ck)))
            else:
                nk = (tuple(f["nu"]["zeta"]), f["nu"]["m"], tuple(f["nu"]["s"]))
                if nk in reads.setdefault(ck, {}):
                    fdup.append(["reading", list(map(str, ck))])
                reads[ck][nk] = f
        f_missing = sorted(str(k) for k in ckeys if k not in heads)
        f_short = sorted(str(k) for k in ckeys if k in heads and len(reads.get(k, {})) != heads[k])
        f_extra = sorted(str(k) for k in set(heads) | set(reads) if k not in ckeys)
        f_complete = not (f_missing or f_short or f_extra or fdup or fcount)
        readings = [f for k in ckeys for f in reads.get(k, {}).values()]
        members = [f for f in readings if f.get("member")]
        two = [f for f in members if f["R"]["capL2"] >= 2 or f["P4"]["capL2"] >= 2]
        both = [f for f in members for k in ("R", "P4") if min(f[k]["capW"], f[k]["capL2"]) >= 2]
        agree = all(f["h1 R"] == f["h1 P4"] for f in readings) and all(f["R"] == f["P4"] for f in members)
        out["Part F"] = {"candidates": len(ckeys), "planned readings": sum(heads.get(k, 0) for k in ckeys),
                         "readings": len(readings), "members": len(members), "members with capL2 >= 2": len(two),
                         "routes agree": agree, "complete": f_complete,
                         "problems": {"missing candidates": f_missing, "short candidates": f_short,
                                      "unexpected candidates": f_extra, "duplicates": fdup,
                                      "fourth-root counts that differ from the Smith form's": fcount}}
        pred["P7"] = False if two else (True if complete and f_complete else None)
        pred["P8"] = False if both else (True if complete and f_complete else None)
    # Proposition H: the sum of n(zeta_H, s) over every root of unity s, its largest term and its odd terms, on K10's covers
    if hcov is None:
        pred["P9"] = None
        pred["P10"] = None
        pred["P11"] = None
        out["Proposition H"] = "K10's covers not given"
    else:
        sums, tops, odds, unread = {}, {}, {}, []
        for cid, hc in sorted(hcov.items()):
            if cid not in covered:
                unread.append(cid)
                continue
            at = [h for h in hits if h["cover"] == cid and list(h["zeta"]) == list(hc["ez"]) and h["m"] == hc["m"]]
            sums[cid] = sum(h["n"] for h in at)
            tops[cid] = max([h["n"] for h in at], default=0)
            odds[cid] = [h["n"] for h in at if h["n"] % 2]
        out["Proposition H"] = {"covers": len(hcov), "sum of n": sums, "largest n": tops, "odd n": odds,
                                "not read in full": unread}
        moved = [c for c, hc in hcov.items() if not hc["acts on Q8 as the identity"]]
        fixed = [c for c, hc in hcov.items() if hc["acts on Q8 as the identity"]]
        pred["P9"] = None if unread or not hcov else all(v == 4 for v in sums.values())
        pred["P10"] = None if not moved or any(c in unread for c in moved) else all(tops[c] <= 2 for c in moved)
        pred["P11"] = None if not fixed or any(c in unread for c in fixed) else all(not odds[c] for c in fixed)
    out["predictions"] = pred
    for k in sorted(pred, key=lambda x: int(x[1:])):
        say(f"{k}: {pred[k]}")
    say(json.dumps({k: v for k, v in out.items() if k != "predictions"}))
    return out


def main():
    log = []

    def say(s):
        log.append(s)
        print(s)

    ident = json.loads((HERE / "identity.json").read_text())
    ctl = json.loads((HERE / "controls.json").read_text())
    out = evaluate(ident, load_rows("run_L.jsonl"), load_rows("run_F.jsonl"), say, ctl["K10"]["covers"],
                   ctl["K11"]["manifest"])
    out["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(out, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return out


if __name__ == "__main__":
    main()
