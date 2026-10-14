"""W80: main's B1637 optimizer, unchanged, on this seat's precise forms. The rule (W80_RULE.md) was committed before
this script. Main's B1637 module is imported read-only from a git archive extraction at 60c5470ae (as in W79); the one
substitution is its basis_at(k, t), replaced by this seat's normalised T (x) T forms at the reduced tau.

  Z0  the control: (5, 7, 5) on all 13 fits exactly near Im tau 3.4
  Z1  (5, 7, 3) on all 13: chi2_min > 5.99
  Z2  (3, 7, 7) on all 13: chi2_min > 5.99
  Z3  the up sector alone at weight 3: no exact fit with Im tau <= 8
  Z4  (3, 3, 3) on the nine masses: chi2_min > 60
  plus the read-outs: (7, 7, 3) on all 13, every job's tau and chi2_min, the wall-clock

Run: python3 the_main_fits_precise.py  ->  the_main_fits_precise.json beside it.
"""
import json
import sys
import tempfile
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402
import the_rank_thirteen_structures as RT  # noqa: E402
import the_two_seats_weight_three as W79  # noqa: E402

OUT = HERE / "the_main_fits_precise.json"
JOBS = [((5, 7, 5), 0.10, True, "ude", 5), ((5, 7, 3), 0.10, True, "ude", 5), ((3, 7, 7), 0.10, True, "ude", 5),
        ((7, 7, 3), 0.10, True, "ude", 5), ((3, 3, 3), 0.10, False, "ude", 1), ((3, 3, 3), 0.10, False, "u", 3)]
MAIN = None


def precise_basis(k, t):
    return list(RT.forms_at("T (x) T", k, FW.reduce(complex(t))))


def run_job(job):
    ks, a, ckm, sectors, seed = job
    t0 = time.time()
    chi2, p = MAIN.fit(ks, a, ckm, sectors, seed)
    tau = FW.reduce(complex(p[0], p[1])) if p else None
    return {"ks": list(ks), "ckm": ckm, "sectors": sectors, "seed": seed, "P": MAIN.P_total(ks), "chi2_min": chi2,
            "tau (raw)": [p[0], p[1]] if p else None, "tau (reduced)": [tau.real, tau.imag] if tau else None,
            "seconds": round(time.time() - t0, 1)}


def main_():
    global MAIN
    t0 = time.time()
    out = {"status": "W80: main's B1637 optimizer on this seat's precise forms (the rule W80_RULE.md first; one run)"}
    with tempfile.TemporaryDirectory() as tmp:
        MAIN, nfiles = W79.load_main(tmp)
        for k in (3, 5, 7):
            MAIN.FORMS[k] = MAIN.forms(k)
        MAIN.basis_at = precise_basis
        out["main's code"] = {"ref": W79.REF, "files extracted": nfiles, "NSTART": MAIN.NSTART}
        with Pool(4) as pool:
            res = pool.map(run_job, JOBS, chunksize=1)
    out["jobs"] = res
    r = {(tuple(x["ks"]), x["ckm"], x["sectors"]): x for x in res}
    c0 = r[((5, 7, 5), True, "ude")]
    c1 = r[((5, 7, 3), True, "ude")]
    c2 = r[((3, 7, 7), True, "ude")]
    c3 = r[((3, 3, 3), False, "u")]
    c4 = r[((3, 3, 3), False, "ude")]
    out["Z0"] = {"chi2_min": c0["chi2_min"], "tau": c0["tau (reduced)"],
                 "holds": bool(c0["chi2_min"] < 1e-6 and 3.0 <= c0["tau (reduced)"][1] <= 3.8)}
    out["Z1"] = {"chi2_min": c1["chi2_min"], "tau": c1["tau (reduced)"], "holds": bool(c1["chi2_min"] > 5.99)}
    out["Z2"] = {"chi2_min": c2["chi2_min"], "tau": c2["tau (reduced)"], "holds": bool(c2["chi2_min"] > 5.99)}
    out["Z3"] = {"chi2_min": c3["chi2_min"], "tau": c3["tau (reduced)"],
                 "holds": bool(c3["chi2_min"] > 1e-6 or c3["tau (reduced)"][1] > 8)}
    out["Z4"] = {"chi2_min": c4["chi2_min"], "tau": c4["tau (reduced)"], "holds": bool(c4["chi2_min"] > 60)}
    out["read-outs"] = {"(7, 7, 3) on all 13": r[((7, 7, 3), True, "ude")], "wall-clock (s)": round(time.time() - t0, 1)}
    out["cells"] = {k: out[k]["holds"] for k in ("Z0", "Z1", "Z2", "Z3", "Z4")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
