#!/usr/bin/env python3
"""B1520 -- the read-out (PREREGISTRATION section 5): the two routes compared, the action of the sixteen maps on the vacua, and
the registered outcome. Reads symmetries.json, route_intertwiner.json, route_traceform.json, lift_e8.json and followup_index.json.

For each map Phi = (sigma, d):
- its action on the family: 'fixes q' if Phi(rho_q) = rho_q, 'q -> 1/q' if Phi(rho_q) = rho_{1/q}, 'leaves the family' if neither
  (outcome C), from the two routes, which must agree;
- its action on the central twist: Phi(mu (x) rho_q) = mu^e (x) Phi(rho_q), e = (sigma's sign on H1 = Z) * (-1)^d;
- whether it flips main's index (count-odd: d = 1, by L1 and L2) and whether it reverses orientation.
The vacuum mu (x) rho_q (q > 0, mu in C*) is fixed by Phi iff Phi fixes q and mu^e = mu. Outcome A (registered kill, NEGATIVE): every
vacuum is fixed by some count-odd Phi. Outcome B: some vacuum is fixed by none. Outcome C: some Phi leaves the family. If the two
routes disagree on any of the 32 decisions, or route 2's Gram determinant has a positive root, or any control or banked identity
of the symmetries, the two routes or the lift failed, no outcome is read ('undecided'). P6 needs the follow-up's banked identity.
The registered predictions P1-P6 are scored here mechanically, as written in PREREGISTRATION section 4.
Usage: python3 decide.py   (writes decide.json)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def main():
    sym, r1, r2 = load("symmetries.json"), load("route_intertwiner.json"), load("route_traceform.json")
    lift, fol = load("lift_e8.json"), load("followup_index.json")
    out = {"controls": {"symmetries": sym["passed"], "route 1": r1["controls"]["controls passed"],
                        "route 2": r2["controls"]["controls passed"], "lift": lift["passed"]}}
    rows, agree = {}, True
    for key in r1["table"]:
        a, b = r1["table"][key], r2["table"][key]
        fix1, inv1 = a["to rho_q"]["isomorphic for every q > 0"] is True, a["to rho_{1/q}"]["isomorphic for every q > 0"] is True
        fix2, inv2 = b["to rho_q"]["all Theorem-T traces equal"], b["to rho_{1/q}"]["all Theorem-T traces equal"]
        if (fix1, inv1) != (fix2, inv2):
            agree = False
        name = key[2:] if key.startswith("D.") else key
        d = key.startswith("D.")
        h1 = sym["representatives"][name]["on H1"]
        e = h1 * (-1 if d else 1)
        action = "fixes q" if fix1 and not inv1 else ("q -> 1/q" if inv1 and not fix1 else ("both" if fix1 and inv1 else "leaves the family"))
        rows[key] = {"orientation": sym["representatives"][name]["orientation"], "count-odd (dualised)": d,
                     "on the family (R1)": action, "R2 agrees": (fix1, inv1) == (fix2, inv2),
                     "on the twist: mu -> mu^e, e": e}
    out["the two routes agree on all 32 decisions"] = agree
    gram_ok = r2["positive roots of det Gram"] == []
    out["route 2's Gram determinant has no positive root"] = gram_ok
    out["the sixteen maps"] = rows
    leaves = [k for k, v in rows.items() if v["on the family (R1)"] == "leaves the family"]
    fix_all = [k for k, v in rows.items() if v["on the family (R1)"] == "fixes q"]
    pair_all = [k for k, v in rows.items() if v["on the family (R1)"] == "q -> 1/q"]
    odd_fix = [k for k in fix_all if rows[k]["count-odd (dualised)"]]
    odd_fix_all_mu = [k for k in odd_fix if rows[k]["on the twist: mu -> mu^e, e"] == 1]
    odd_fix_all_mu_kept = [k for k in odd_fix_all_mu if rows[k]["orientation"] == "kept"]
    bare = [k for k in rows if not rows[k]["count-odd (dualised)"]]
    rev_fix = [k for k in fix_all if k in bare and rows[k]["orientation"] == "reversed"]
    rev_pair = [k for k in pair_all if k in bare and rows[k]["orientation"] == "reversed"]
    out["stabiliser of a vacuum q != 1 (maps fixing every q)"] = fix_all
    out["maps pairing q with 1/q"] = pair_all
    out["count-odd maps fixing every vacuum, every twist mu"] = odd_fix_all_mu
    out["of these, orientation kept (Lemma G's charge conjugation needs one)"] = odd_fix_all_mu_kept
    out["bare maps fixing every q"] = [k for k in fix_all if k in bare]
    out["bare orientation-reversing maps fixing every q"] = rev_fix
    out["bare orientation-reversing maps pairing q with 1/q"] = rev_pair
    out["maps leaving the family"] = leaves
    controls_ok = all(out["controls"].values())
    out["every control and banked identity passed"] = controls_ok
    if not (agree and gram_ok and controls_ok):
        outcome = "undecided"
    elif leaves:
        outcome = "C"
    elif odd_fix_all_mu:
        outcome = "A"
    else:
        outcome = "B"
    out["registered outcome"] = outcome
    fol_ok = (fol["BANKED IDENTITY: I(W1) = -1 at all six prime-root pairs (B1509)"]
              and fol["every bare image -1 and every dualised image +1"] and len(fol["maps"]) == 16)
    out["follow-up: I(W1) = -1 and every count-odd image +1, every bare image -1"] = fol_ok
    # route 2's exact conjugacy loci: every pair should be conjugate at every q > 0 or exactly at q = 1
    loci = {f"{k} {t}": r2["table"][k][t]["conjugate exactly at q > 0"] for k in r2["table"] for t in ("to rho_q", "to rho_{1/q}")}
    out["route 2: the conjugacy loci of the 32 pairs"] = loci
    out["every locus is 'every q > 0' or exactly q = 1"] = all(v == "every q > 0" or v == ["1"] for v in loci.values())
    # P2's second half: rho_q* and rho_q are conjugate exactly at q = 1
    p2_roots = r2["table"]["D.id"]["to rho_q"]["conjugate exactly at q > 0"]
    out["P2: rho_q* vs rho_q conjugate exactly at q > 0"] = p2_roots
    bare_fix = [k for k in fix_all if k in bare]
    out["predictions"] = {
        "P1 the routes agree on all 32 decisions": agree,
        "P2 rho_q* = rho_{1/q}, not rho_q for q != 1": rows["D.id"]["on the family (R1)"] == "q -> 1/q" and p2_roots == ["1"],
        "P3 no map leaves the family": not leaves,
        "P4 eight fix every q; bare 4 fix + 4 pair; bare reversing 2 fix + 2 pair": len(fix_all) == 8 and len(bare_fix) == 4
        and len([k for k in pair_all if k in bare]) == 4 and len(rev_fix) == 2 and len(rev_pair) == 2,
        "P5 outcome A with witness D.theta": outcome == "A" and "D.theta" in odd_fix_all_mu,
        "P6 the follow-up": fol_ok,
    }
    out["predictions true"] = sum(1 for v in out["predictions"].values() if v)
    (HERE / "decide.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
