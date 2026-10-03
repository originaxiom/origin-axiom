#!/usr/bin/env python3
"""B1529 post-run read (written after the run; disclosed in FINDINGS; it does not change the sealed reading): the content of
P4-P6 and G on every crossing located, the sealed brackets' and the coverage check's together.

Sources: the sealed records crossings_<name>.json (the pole brackets of +-LLLRLRR tagged by post_run_poles' test) and
post_run_coverage.json's entries.  Each located crossing is checked by check_read, which is read_out.crossings' loop body for one
crossing.  The two are compared on the sealed records: per state, check_read's failure lists must equal read_out's.
It also matches the located crossings to the twenty first-order crossings of each ring (post_run_coverage.predicted).  Each
must be within 0.01 degrees of exactly one, and each first-order crossing is found at most once per source.
Writes post_run_read.json and prints a summary."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import read_out as RO  # noqa: E402

MATCH_TOL = 0.01


def check_read(kind, rd):
    """read_out.crossings' checks on one located crossing: (structure fails, index fails, mechanism fails, rows T, rows Fox/W)"""
    sf, ixf, mf = [], [], []
    rows_t = rows_fw = 0
    for mod, rec in rd.items():
        if mod not in ("4", "L2"):
            continue
        want_e = 1 if mod == "4" else 2
        ks = rec["kappa*"]
        if rec["e"] != want_e or len(ks) != want_e:
            sf.append([kind, mod, "e", rec["e"], "twists", len(ks)])
        if mod == "L2" and len(ks) == 2 and float(rec["|kappa1 kappa2 - 1|"]) > 1e-30:
            sf.append([kind, mod, "|kappa1 kappa2 - 1|", rec["|kappa1 kappa2 - 1|"]])
        for tw in rec["twists"]:
            rt = tw["route T"]
            rows_t += rt["rows"]
            if set(rt["rows by (t0, s0)"]) != {"(1, 1)"}:
                sf.append([kind, mod, "(t0, s0)", rt["rows by (t0, s0)"]])
            if rt["I != 0"] or rt["hypothesis fails"]:
                ixf.append([kind, mod, "route T", rt["I values"], rt["hypothesis fails"]])
            if mod == "L2" and (rt["smallest |chi_K(kappa*)| rel"] is None
                                or float(rt["smallest |chi_K(kappa*)| rel"]) <= 1e-20):
                mf.append([kind, tw["kappa*"], rt["smallest |chi_K(kappa*)| rel"]])
            for row in tw["Fox and W"]:
                rows_fw += 1
                F, W, T = row["Fox"], row["W"], row["T"]
                agree = ((F["h1"], F["h1*"], F["t0"], F["s0"], F["I"])
                         == (W["h1(V)"], W["h1(V*)"], W["t0"], W["s0"], W["I"])
                         == (T["h1"], T["h1*"], T["t0"], T["s0"], T["I"]))
                if F["I"] != 0 or not all(F["checks"].values()) or not agree:
                    ixf.append([kind, mod, row["u"], "Fox", F["I"], "W", W["I"], "T", T["I"], "agree", agree])
    return sf, ixf, mf, rows_t, rows_fw


def circ(x, y):
    d = (y - x) % 360
    return d - 360 if d > 180 else d


def main():
    import post_run_coverage as PC
    import post_run_poles as PP
    import crossings as C
    sealed_ro = RO.crossings()
    out = {"states": {}, "agrees with read_out on the sealed records": True}
    cov = {}
    f = HERE / "post_run_coverage.json"
    if f.exists():
        for e in json.loads(f.read_text())["entries"]:
            cov.setdefault(e["sign"] + e["word"], []).append(e)
    tot = {"first-order crossings": 0, "located": 0, "rows T": 0, "rows Fox/W": 0, "structure fails": 0,
           "index fails": 0, "mechanism fails": 0, "unmatched": 0, "found twice": 0}
    for sign, word in RO.TEN:
        name = RO.name_of(sign, word)
        st = sign + word
        x1 = json.loads((C.B1527 / ("x1_" + name + ".json")).read_text())
        pred = PC.predicted(x1["type-one frames"][0])
        tagged = PP.brackets_with_poles(name)
        rec = json.loads((HERE / ("crossings_" + name + ".json")).read_text())
        assert len(rec["crossings"]) == len(tagged)
        s = {"first-order crossings": len(pred), "sealed brackets": len(tagged),
             "sealed brackets through a pole": sum(b["pole"] for b in tagged),
             "sealed located": 0, "sealed located on a pole bracket": 0, "coverage targets": len(cov.get(st, [])),
             "coverage located": 0, "structure fails": [], "index fails": [], "mechanism fails": [], "rows T": 0,
             "rows Fox/W": 0, "unmatched": [], "found": {}}
        sealed_sf, sealed_ixf, sealed_mf = [], [], []
        located = []
        for b, e in zip(tagged, rec["crossings"]):
            if "read" not in e:
                continue
            s["sealed located"] += 1
            s["sealed located on a pole bracket"] += b["pole"]
            sf, ixf, mf, rt, rfw = check_read(e["kind"], e["read"])
            sealed_sf += sf
            sealed_ixf += ixf
            sealed_mf += mf
            located.append(("sealed", e["kind"], e["alpha (deg)"], sf, ixf, mf, rt, rfw))
        ro = sealed_ro["states"].get(st)
        if ro is None or (ro["structure fails"], ro["index fails"], ro["mechanism fails"]) != (sealed_sf, sealed_ixf, sealed_mf):
            out["agrees with read_out on the sealed records"] = False
        for e in cov.get(st, []):
            if "read" not in e:
                continue
            s["coverage located"] += 1
            sf, ixf, mf, rt, rfw = check_read(e["kind"], e["read"])
            located.append(("coverage", e["kind"], e["alpha (deg)"], sf, ixf, mf, rt, rfw))
        for src, kind, al, sf, ixf, mf, rt, rfw in located:
            s["structure fails"] += sf
            s["index fails"] += ixf
            s["mechanism fails"] += mf
            s["rows T"] += rt
            s["rows Fox/W"] += rfw
            hits = [p for p in pred if p[0] == kind and abs(circ(p[1], al)) <= MATCH_TOL]
            if len(hits) != 1:
                s["unmatched"].append([src, kind, al])
                continue
            key = f"{kind} {hits[0][1]:.4f}"
            s["found"].setdefault(key, []).append(src)
        s["first-order crossings located"] = len(s["found"])
        s["found twice"] = {k: v for k, v in s["found"].items() if len(v) > 1}
        out["states"][st] = s
        tot["first-order crossings"] += len(pred)
        tot["located"] += len(s["found"])
        tot["rows T"] += s["rows T"]
        tot["rows Fox/W"] += s["rows Fox/W"]
        tot["structure fails"] += len(s["structure fails"])
        tot["index fails"] += len(s["index fails"])
        tot["mechanism fails"] += len(s["mechanism fails"])
        tot["unmatched"] += len(s["unmatched"])
        tot["found twice"] += len(s["found twice"])
    out["totals"] = tot
    out["after the run"] = {
        "P4 content (structure at every located crossing)": tot["structure fails"] == 0,
        "P5 content (I = 0, routes agree)": tot["index fails"] == 0,
        "P6 content (mechanism)": tot["mechanism fails"] == 0,
        "G content (P5 on the golden rings)": all(not out["states"][g]["index fails"] for g in RO.GOLDEN_TEN),
        "located / first-order": f"{tot['located']} / {tot['first-order crossings']}"}
    (HERE / "post_run_read.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({k: v for k, v in out.items() if k != "states"}, indent=1, default=str))
    for st, s in out["states"].items():
        print(f"{st}: sealed {s['sealed located']}/{s['sealed brackets']} (pole {s['sealed brackets through a pole']}, located "
              f"on a pole bracket {s['sealed located on a pole bracket']}); coverage {s['coverage located']}/"
              f"{s['coverage targets']}; first-order located {s['first-order crossings located']}/20; unmatched "
              f"{len(s['unmatched'])}; twice {len(s['found twice'])}; fails {len(s['structure fails'])}/"
              f"{len(s['index fails'])}/{len(s['mechanism fails'])}")


if __name__ == "__main__":
    main()
