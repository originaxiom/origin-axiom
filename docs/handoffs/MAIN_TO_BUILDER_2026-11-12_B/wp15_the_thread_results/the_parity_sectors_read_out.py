#!/usr/bin/env python3
"""WP-1.5; harvest row 916: the read-out of the_parity_sectors_on_main.py against the SM seat's table (its W7).

The seat's table, as data: for each state, on how many of the three non-zero parities a member stands at the resolving
tick, and the members' structure where it gives one.  Compared class by class of states; the labels of the parities and
the sign of kappa are conventions and are not compared (the script's docstring says why)."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
SEAT = {"LR": (3, 0, None), "LLLR": (3, 0, None), "LLLLLR": (3, 0, None), "LLLRLR": (3, 0, None), "LLLRRR": (3, 0, None), "LLRLRR": (3, 0, None),
        "LLR": (2, 2, (2, 1, 1)), "LLLLR": (2, 2, (2, 1, 1)), "LLLRR": (2, 0, None), "LLRLR": (2, 0, None), "LLRR": (1, 2, None), "LLLLRR": (1, 0, None)}
rows = [json.loads(l) for l in (HERE / "the_parity_sectors_on_main.jsonl").read_text().split("\n") if l.strip()]
by = collections.defaultdict(list)
for r in rows: by[r["state"]].append(r)
CHECKS, table = [], {}
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""))
ok_all, zero_members, per_state = True, 0, {}
for st, rs in sorted(by.items()):
    assert len(rs) == 48 and collections.Counter(r["class"] for r in rs) == {"zero": 12, "parity 1": 12, "parity 2": 12, "parity 3": 12}, (st, len(rs))
    mem = collections.defaultdict(list)
    for r in rs:
        if r["n"] > 0: mem[r["class"]].append((r["k"], (r["a1"], r["r1"], r["n"])))
    zero_members += len(mem.get("zero", []))
    parities = sorted(c for c in mem if c != "zero"); structures = sorted({s for c in parities for _, s in mem[c]})
    kappas = sorted({k for c in parities for k, _ in mem[c]}); each_once = all(len(mem[c]) == 1 for c in parities)
    tick, npar, struct = SEAT[st[3:]]
    good = rs[0]["tick"] == tick and len(parities) == npar and (struct is None or structures == [struct]) and each_once
    ok_all &= good
    table[st] = {"tick": rs[0]["tick"], "parities with a member": len(parities), "one member on each of them": each_once, "at k (kappa = zeta_12^k)": kappas, "structures": [list(s) for s in structures], "as the seat's table": good}
    print("%-12s tick %d: members on %d of the three parities%s" % (st, rs[0]["tick"], len(parities), "" if not parities else ", one each, at k = %s, structure %s" % (kappas, structures)))
check("all 24 states read, 48 characters each, twelve in each of the four classes", len(by) == 24, len(by))
check("state by state the seat's table: the tick, the number of parities that carry a member, and the structure where the table gives one", ok_all, [s for s, t in table.items() if not t["as the seat's table"]])
check("no member at the zero parity on any state", zero_members == 0, zero_members)
check("members stand on two parities or on none, never on one and never on all three", all(t["parities with a member"] in (0, 2) for t in table.values()), sorted({t["parities with a member"] for t in table.values()}))
check("no odd-trace state carries a member at its third tick", all(t["parities with a member"] == 0 for s, t in table.items() if t["tick"] == 3))
json.dump({"table": table, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "the_parity_sectors_read_out.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
