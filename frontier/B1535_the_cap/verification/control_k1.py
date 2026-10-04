#!/usr/bin/env python3
"""B1535 control K1 (pre-seal, banked data only): Theorem C's identities at every one of sm:B1534's 144 banked terms.

For each member of m135 and m136 (sm:B1534's population, rebuilt by its own silver_lib), each class sm:B1534 read (the one class;
or c_int, c_g1 (s = 3/7), c_g2 (s = -11/5) and the special class, its s recomputed by silver_lib's pencil and checked against
the banked value) and each contributing character, cap_lib.reading asserts the identities and the cap, and the two indices are
compared with the banked term.  Writes k1.json and k1_log.txt.  No quantity of the sealed question is read here: the mixed
classes and the census are not touched."""
import json
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1534V = ROOT / "frontier" / "B1534_the_silver_covers" / "verification"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(B1534V))
import cap_lib as CL  # noqa: E402
import silver_lib as SL  # noqa: E402

E = CL.E
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def main():
    t0 = time.time()
    banked = json.loads((B1534V / "terms.json").read_text())
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "terms": [], "failures": []}
    say(f"B1535 control K1, {out['started']}")
    for state in ("-LLRR", "+LLRR"):
        st = SL.setup(state)
        brec = banked["states"][state]
        for m in SL.members(st):
            u, kap = [str(x) for x in m["u"]], str(m["kappa"])
            bm = next(x for x in brec["members"] if x["u"] == u and x["kappa"] == kap)
            C = SL.contributing(st, m)
            if m["h1"] == 1:
                classes = {"the class": m["classes"]["the class"]}
            else:
                Pb, Pi, _, _ = SL.pencil(st, m, SL.char(st, (0, 0), 0), "(L2E)*")
                sp = SL.special_points(Pb, Pi)
                assert len(sp["rational"]) == 1 and not sp["quadratic"], sp
                s = sp["rational"][0]
                bname = next(k for k in bm["classes"] if k.startswith("special"))
                bval = complex(bm["classes"][bname][1].strip("()").replace(" ", ""))
                assert abs(complex(s.num(mp)) - bval) < 1e-40, ("the special s", s.num(mp), bval)
                classes = {"c_int": m["c_int"],
                           "c_g1": SL.lin(m["c_b"], m["c_int"], E.ONE, E.K.of(Fraction(3, 7))),
                           "c_g2": SL.lin(m["c_b"], m["c_int"], E.ONE, E.K.of(Fraction(-11, 5))),
                           bname: SL.lin(m["c_b"], m["c_int"], E.ONE, s)}
            for cname, c in classes.items():
                W1 = E.extension(m["V"], c, m["L"])
                assert W1.check(st["G"].rels)
                for wk in C:
                    ck = SL.key(wk)
                    R = CL.reading(st["G"], W1, SL.char(st, *wk))
                    T = [R["I(W)"], R["I(L2W)"]]
                    bT = bm["terms"][cname][ck]
                    row = {"state": state, "u": u, "kappa": kap, "class": cname, "chi": ck, "T": T, "banked": bT,
                           "agree": T == bT, "k": R["k"], "b0": R["b0"], "n((VL)*)": R["n((VL)*)"], "n(V)": R["n(V)"],
                           "n(L)": R["n(L)"], "rk d1": R["rk d1"], "checks": R["checks"], "all": R["all"]}
                    out["terms"].append(row)
                    if not (row["agree"] and row["all"]):
                        out["failures"].append(row)
                    say(f"{state} u {u} kappa {kap} {cname[:12]:12s} chi {ck}: T {tuple(T)} banked {tuple(bT)} "
                        f"k {R['k']} b0 {R['b0']} n(VL*) {R['n((VL)*)']} rk d1 {R['rk d1']} "
                        f"{'ok' if row['agree'] and row['all'] else 'FAIL'} ({time.time() - t0:.0f} s)")
    out["n terms"] = len(out["terms"])
    out["holds"] = not out["failures"] and out["n terms"] == 144
    out["seconds"] = round(time.time() - t0)
    (HERE / "k1.json").write_text(json.dumps(out, indent=1, default=str))
    say(f"K1: {out['n terms']} terms, {len(out['failures'])} failures: {'HOLDS' if out['holds'] else 'FAILS'} "
        f"({out['seconds']} s)")
    (HERE / "k1_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
