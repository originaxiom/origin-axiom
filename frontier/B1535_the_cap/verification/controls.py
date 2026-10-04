#!/usr/bin/env python3
"""B1535 controls (pre-seal; banked comparisons only).  Re-run unchanged after the seal, they must reproduce controls.json in every
field but the timings (the banked identity, PREREGISTRATION section 8).  No mixed class and no census row outside the dry run is
read here.

  K1s  Theorem C's identities at m135's non-simple member u1 = (0, 1/2): every class sm:B1534 read (c_int, c_g1, c_g2, the special
       class) at every contributing twist, against the banked terms (a deterministic subset of k1.json's 144, re-read here).
  K2   Part M's routes on pure classes, against sm:B1534's banked sums (Lemma S; Lemma R at chi0 != 1):
         m135 u1 on <(1/2, 1/2)>: pure-1 at c_int, c_g1, c_g2; pure-(1/2, 1/2) at u2's c_int and c_g1;
         m135 (0, 0) on the Klein group <(0, 1/2), (1/2, 0)>: pure-1 at the class;
         m136 (0, 1/2; 1/2) on <(0, 0; 1/2)>: pure-1 at the class;
       in route RS at both primes, and in route Ind on the order-2 covers.
  K3   Part W's dry run on +LR (m004) and -LLRR (m135), both routes.
  K4   The cover's own presentation: Schreier ranks, cusp counts and the relators' identity for the covers of K2."""
import json
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cap_lib as CL  # noqa: E402
import part_m as PM  # noqa: E402
import part_w as PW  # noqa: E402
import rs_lib as RS  # noqa: E402

ML, SL, E = PM.ML, PM.SL, PM.E
F = Fraction


def k1s(banked):
    st = SL.setup("-LLRR")
    m = next(x for x in SL.members(st) if x["u"] == (F(0), F(1, 2)))
    bm = next(x for x in banked["states"]["-LLRR"]["members"] if x["u"] == ["0", "1/2"] and x["kappa"] == "0")
    Pb, Pi, _, _ = SL.pencil(st, m, SL.char(st, (0, 0), 0), "(L2E)*")
    s = SL.special_points(Pb, Pi)["rational"][0]
    sname = next(k for k in bm["classes"] if k.startswith("special"))
    classes = {"c_int": m["c_int"], "c_g1": SL.lin(m["c_b"], m["c_int"], E.ONE, E.K.of(F(3, 7))),
               "c_g2": SL.lin(m["c_b"], m["c_int"], E.ONE, E.K.of(F(-11, 5))), sname: SL.lin(m["c_b"], m["c_int"], E.ONE, s)}
    rows = []
    for cname, c in classes.items():
        W1 = E.extension(m["V"], c, m["L"])
        for wk in SL.contributing(st, m):
            R = CL.reading(st["G"], W1, SL.char(st, *wk))
            T = [R["I(W)"], R["I(L2W)"]]
            rows.append({"class": cname[:20], "chi": SL.key(wk), "T": T, "banked": bm["terms"][cname][SL.key(wk)],
                         "all": R["all"], "k": R["k"], "rk d1": R["rk d1"]})
    return {"rows": rows, "holds": all(r["T"] == r["banked"] and r["all"] for r in rows)}


def k2(banked):
    out = []
    cases = [("-LLRR", (F(0), F(1, 2)), F(0), [ML.lab(F(1, 2), F(1, 2), 0)]),
             ("-LLRR", (F(0), F(0)), F(0), [ML.lab(0, F(1, 2), 0), ML.lab(F(1, 2), 0, 0)]),
             ("+LLRR", (F(0), F(1, 2)), F(1, 2), [ML.lab(0, 0, F(1, 2))])]
    for state, u, kap, gens in cases:
        st = SL.setup(state)
        mems = SL.members(st)
        m = next(x for x in mems if x["u"] == u and x["kappa"] == kap)
        nu = PM.lab_of(u, kap)
        B = tuple(ML.closure(gens))
        cov = PM.cover_of(st, B)
        cls = PM.classes_at(st, mems, m, B)
        for name, comps in cls.items():
            if not name.startswith("pure-"):
                continue
            x = next(iter(comps))
            tgt = PM.lemma_r_target(name, x, nu)
            bsum = PM.banked_sum(banked, state, tgt[0], tgt[1], B)
            r1, r2 = PM.read_rs(st, nu, B, comps, RS.P1, cov), PM.read_rs(st, nu, B, comps, RS.P2, cov)
            row = {"state": state, "nu": PM.lstr(nu), "|B|": len(B), "class": name, "banked": bsum,
                   "RS p1": [r1["I(W)"], r1["I(L2W)"]], "RS p2": [r2["I(W)"], r2["I(L2W)"]],
                   "RS all": r1["all"] and r2["all"], "RS k": [r1["k"], r2["k"]], "cusps": r1["cusps"]}
            if len(B) == 2:
                ri = PM.read_ind(st, nu, B, comps)
                row["Ind"] = [ri["I(W)"], ri["I(L2W)"]]
                row["Ind all"] = ri["all"]
            row["agree"] = row["RS p1"] == row["RS p2"] == bsum and row.get("Ind", bsum) == bsum and row["RS all"] and \
                row.get("Ind all", True)
            out.append(row)
    return {"rows": out, "holds": all(r["agree"] for r in out)}


def k3():
    R = [r for r in PW.rows() if r["state"] in ("+LR", "-LLRR")]
    recs = [PW.one(r) for r in R]
    return {"rows": [{"state": r["state"], "X chars": r["X"]["chars"], "X n != 0": len(r["X"]["n != 0"]),
                      "mu != tau": len(r["X"]["mu != tau"]), "S order | 12": r["S"]["order | 12"],
                      "S n != 0": len(r["S"]["n != 0"]), "agree": r["agree on order | 12"], "X h1": r["X"]["h1 pattern"],
                      "S h1": r["S"]["h1 pattern"]} for r in recs],
            "holds": all(not r["X"]["n != 0"] and not r["S"]["n != 0"] and not r["X"]["mu != tau"] and
                         r["agree on order | 12"] for r in recs)}


def k4():
    rows = []
    for state, gens in (("-LLRR", [ML.lab(F(1, 2), F(1, 2), 0)]), ("-LLRR", [ML.lab(0, F(1, 2), 0), ML.lab(F(1, 2), 0, 0)]),
                        ("-LLRR", [ML.lab(F(1, 4), F(1, 4), 0), ML.lab(0, F(1, 2), 0)]), ("+LLRR", [ML.lab(0, 0, F(1, 2))])):
        st = SL.setup(state)
        B = tuple(ML.closure(gens))
        cov = PM.cover_of(st, B)
        rows.append({"state": state, "|B|": len(B), "order": cov.order, "generators": len(cov.sgens), "relators": len(cov.rels),
                     "cusps": len(cov.cusps), "cusp t' power": cov.cusp_m})
    return {"rows": rows}


def main():
    t0 = time.time()
    banked = json.loads((PM.B1534V / "terms.json").read_text())
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    for name, fn in (("K1s", lambda: k1s(banked)), ("K2", lambda: k2(banked)), ("K3", k3), ("K4", k4)):
        t1 = time.time()
        out[name] = fn()
        print(name, {k: v for k, v in out[name].items() if k != "rows"}, f"({time.time() - t1:.0f} s)", flush=True)
    out["all hold"] = all(out[k].get("holds", True) for k in ("K1s", "K2", "K3"))
    out["seconds"] = round(time.time() - t0)
    name = "controls_rerun.json" if "--rerun" in sys.argv else "controls.json"
    (HERE / name).write_text(json.dumps(out, indent=1, default=str) + "\n")
    print("ALL HOLD" if out["all hold"] else "A CONTROL FAILS", f"({out['seconds']} s)")


if __name__ == "__main__":
    main()
