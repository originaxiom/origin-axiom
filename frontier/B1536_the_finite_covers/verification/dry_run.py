#!/usr/bin/env python3
"""B1536 dry run of run.py's read_cover on banked data only: the levels M2 and M3 read as bases, on the finite abelian covers of
sm:B1532's population, at the lambda = 1 characters only (kappa = 0, the banked members), by both routes.  Checks: Part P's
census equals sm:B1532's banked histogram (as control K1); Part S and Part O agree between the routes.

    python3 dry_run.py   ->  dry_run.json"""
import json
import sys
import time
import warnings
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib as CL  # noqa: E402
import control_k1 as K1  # noqa: E402
import population as POP  # noqa: E402
import run as RUN  # noqa: E402

_orig = POP.characters


def lam1_only(st, perms):
    cus, L, Nroot, chars = _orig(st, perms)
    return cus, L, Nroot, [(u, k) for (u, k) in chars if k == 0]


def main():
    POP.characters = lam1_only
    t0 = time.time()
    out = {"levels": {}}
    banked, _, _ = K1.banked_hist([2, 3], Path("/tmp") / "b1536_k1")
    for n in (2, 3):
        name = "+" + "LR" * n
        st = CL.state(name)
        chars = [tuple(Fr(x) for x in u) for u in st["fibre characters"]]
        subs = K1.all_subgroups(chars)
        hist = {"N": Counter(), "R": Counter()}
        agreeS, agreeO, nO, bad = 0, 0, 0, []
        for i, B in enumerate(subs):
            perms = K1.abelian_cover(B)
            rows = {rt: RUN.read_cover((rt, name, f"B{i}", perms)) for rt in ("N", "R")}
            for a, b in zip(rows["N"][:-1], rows["R"][:-1]):
                assert (a["u"], a["kappa"]) == (b["u"], b["kappa"])
                agreeS += a["S"] == b["S"]
                for rt, r in (("N", a), ("R", b)):
                    if "P" in r:
                        hist[rt][(n, "c1", r["P"]["count"][0], r["P"]["count"][1])] += 1
                        if not r["P"]["all"]:
                            bad.append((rt, i, r["u"]))
                if "O" in a or "O" in b:
                    nO += 1
                    sa = [(x["S"], [y["count"] + [y["k"]] for y in x["readings"]]) for x in a.get("O", [])]
                    sb = [(x["S"], [y["count"] + [y["k"]] for y in x["readings"]]) for x in b.get("O", [])]
                    agreeO += sa == sb
        bk = Counter({k: v for k, v in banked.items() if k[0] == n})
        out["levels"][str(n)] = {"Part P (N) = banked": hist["N"] == bk, "Part P (R) = banked": hist["R"] == bk,
                                 "Part S rows agreeing": agreeS, "Part O rows": nO, "Part O rows agreeing": agreeO,
                                 "failed readings": bad}
        print(n, out["levels"][str(n)], f"{time.time() - t0:.0f}s", flush=True)
    out["holds"] = all(v["Part P (N) = banked"] and v["Part P (R) = banked"] and v["Part O rows"] == v["Part O rows agreeing"]
                       and not v["failed readings"] for v in out["levels"].values())
    out["seconds"] = round(time.time() - t0)
    print(json.dumps({"holds": out["holds"], "seconds": out["seconds"]}))
    if "--record" in sys.argv:
        (HERE / "dry_run.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
