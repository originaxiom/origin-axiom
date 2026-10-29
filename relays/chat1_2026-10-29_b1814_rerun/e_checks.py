"""B1814 BLIND RERUN: the agreement cells E1-E4 of BLIND_RERUN_RULE.md (sealed c0259df7d), read against main's census and
comparison only after this seat's census (b0c206418) and comparison (d61495146) were committed unread.

  E1  D1, D1h, D2 reach the same verdict on both censuses
  E2  resolved shares per arm (unforced and by hand) within 2 percentage points of main's
  E3  the arms' Im tau marginals agree (two-sample KS p > 0.01 for each arm)
  E4  the five p's quoted in S256 within a factor 2 of main's, or both <= 0.01:
      p_F A1 (unforced, six), p_F A0 (unforced, six), p_nn A1 unforced (six), p_nn A1 by hand (six), the nine by hand
      (A1, p_nn)

Usage: python3 e_checks.py <main's B1814 verification folder>   (writes e_checks_out.txt and e_checks.json here)
"""
import json
import pathlib
import sys

from scipy.stats import ks_2samp

HERE = pathlib.Path(__file__).resolve().parent


def load(folder):
    folder = pathlib.Path(folder)
    comp = json.loads((folder / "comparison.json").read_text(encoding="utf-8"))
    im = {"A0": [], "A1": []}
    with open(folder / "census.jsonl", encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            im[r["arm"]].append(r["Im_tau"])
    return comp, im


def main():
    main_dir = sys.argv[1]
    mc, mim = load(main_dir)
    oc, oim = load(HERE)
    lines, out = [], {}

    def say(s=""):
        lines.append(s)

    say("B1814 BLIND RERUN: the agreement cells (rule c0259df7d); this seat's census b0c206418, comparison d61495146")
    say()
    cells = ["D1_the_unforced_world_typical_under_the_geometric_clock", "D1h_by_hand_typical_under_the_geometric_clock",
             "D2_the_clock_depths_typical_under_A1_not_A0"]
    e1 = {c: [mc["cells"][c], oc["cells"][c]] for c in cells}
    E1 = all(a == b for a, b in e1.values())
    out["E1"] = {"main_vs_rerun": e1, "holds": E1}
    say("E1 " + "; ".join("%s main %s, rerun %s" % (c.split("_")[0], a, b) for c, (a, b) in e1.items()) + "  -> %s" % E1)

    e2 = {}
    for key in ("A0|unforced", "A0|hand", "A1|unforced", "A1|hand"):
        arm = key.split("|")[0]
        sm = mc["results"][key]["resolved draws"] / len(mim[arm])
        so = oc["results"][key]["resolved draws"] / len(oim[arm])
        e2[key] = {"main": sm, "rerun": so, "diff_pp": 100 * (so - sm)}
    E2 = all(abs(v["diff_pp"]) <= 2 for v in e2.values())
    out["E2"] = {"shares": e2, "holds": E2}
    say("E2 " + "; ".join("%s main %.4f rerun %.4f (%+.2f pp)" % (k, v["main"], v["rerun"], v["diff_pp"]) for k, v in e2.items())
        + "  -> %s" % E2)

    e3 = {}
    for arm in ("A0", "A1"):
        ks = ks_2samp(mim[arm], oim[arm])
        e3[arm] = {"n_main": len(mim[arm]), "n_rerun": len(oim[arm]), "D": float(ks.statistic), "p": float(ks.pvalue)}
    E3 = all(v["p"] > 0.01 for v in e3.values())
    out["E3"] = {"ks": e3, "holds": E3}
    say("E3 " + "; ".join("%s KS D %.4f p %.4f (n %d, %d)" % (a, v["D"], v["p"], v["n_main"], v["n_rerun"]) for a, v in e3.items())
        + "  -> %s" % E3)

    picks = [("p_F A1 unforced", "A1|unforced", "six", "p_F"), ("p_F A0 unforced", "A0|unforced", "six", "p_F"),
             ("p_nn A1 unforced", "A1|unforced", "six", "p_nn"), ("p_nn A1 by hand", "A1|hand", "six", "p_nn"),
             ("the nine by hand (A1, p_nn)", "A1|hand", "nine", "p_nn")]
    e4 = {}
    for nm, key, which, stat in picks:
        a = mc["results"][key][which][stat]
        b = oc["results"][key][which][stat]
        ok = (a <= 0.01 and b <= 0.01) or (max(a, b) / min(a, b) <= 2)
        e4[nm] = {"main": a, "rerun": b, "ratio": max(a, b) / min(a, b), "within": ok}
    E4 = all(v["within"] for v in e4.values())
    out["E4"] = {"p": e4, "holds": E4}
    say("E4 " + "; ".join("%s main %.4f rerun %.4f (x%.2f)" % (k, v["main"], v["rerun"], v["ratio"]) for k, v in e4.items())
        + "  -> %s" % E4)
    say()
    out["cells"] = {"E1": E1, "E2": E2, "E3": E3, "E4": E4}
    say("CELLS: " + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in out["cells"].items()))
    (HERE / "e_checks_out.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (HERE / "e_checks.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
