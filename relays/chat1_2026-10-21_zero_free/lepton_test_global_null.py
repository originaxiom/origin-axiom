#!/usr/bin/env python3
"""chat1, 2026-10-21 -- POST HOC (labelled), after the lepton test's output was read (1caa0e263): the family-wide null.

Why.  The sealed rule's L5 control is per passing (tau*, pair): it asks how often random targets are fitted as well
by that one pair at that one tau*.  The family has 324 tests with a degree of freedom, so a per-test f near 0.005
is roughly what chance gives somewhere.  This asks the family-wide question, as W115's T3 does for its own family.

Fixed now (written and committed before its one run):
- The family: every (tau*, pair) of the sealed test with dof >= 1 (36 tau* x 9 pairs = 324 tests), the same pairs,
  parametrisations, chi2 (a = 0.10, the IO penalty 6.1) and pass marks.
- The statistic: the family's best p-value, max over tests of 1 - CDF_chi2(dof)(chi2_min).  The data's value is
  read from lepton_test.json's stage L (the sealed search).
- The null: N = 40 random targets (seed 9100 + n), drawn as L5 draws them (each log-observable shifted uniformly
  within a decade centred on the data, sin^2 targets redrawn above 0.99, both orderings), each fitted over the whole
  family with a reduced search (600 random vectors, Nelder-Mead from the best 3 at most 2000 evaluations, then the
  best once more), for runtime.  The same reduced search is run on the data, so both sides are searched alike; the
  data's sealed family-best p is reported beside it.
- The read-out: p_global = the fraction of targets whose family-best p is at or above the data's (reduced search on
  both sides), and the number of passes per target (median, quartiles) against the data's 8.
- Prediction (prior): p_global >= 0.05, so the family's best fit to the data is not special.  70%.
- Checkpointed per target (lepton_test_global_null.jsonl) and resumable past the job limit.
"""
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
from scipy.stats import chi2 as CHI2

HERE = Path(__file__).resolve().parent
T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


# the sealed test's module provides the pairs, data and fit; import it without running its stages
SRC = (HERE / "lepton_test.py").read_text()
HEAD = SRC.split("# ------------------------------------------------------------------------------------------- the launch fix")[0]
NS = {"__file__": str(HERE / "lepton_test.py"), "__name__": "lepton_test_head"}
exec(compile(HEAD, "lepton_test_head", "exec"), NS)
SA, TF, DATA, Pair, ChargedParam, SymParam = NS["SA"], NS["TF"], NS["DATA"], NS["Pair"], NS["ChargedParam"], NS["SymParam"]
fit_pair = NS["fit_pair"]
TT, BB, MQT, MQB = NS["TT"], NS["BB"], NS["MQT"], NS["MQB"]
import multiprocessing as MPR  # noqa: E402

TAUS = [complex(*T["tau"]) for T in json.loads((HERE / "lepton_test_stageQ.json").read_text())["TAUS"]]
rngL = np.random.default_rng(2111)                     # the sealed creation order, so the same random directions
CH = {+1: [(TT, 5), (MQT, 4)], -1: [(BB, 3), (BB, 7), (MQB, 4)]}
WB = {+1: [(TT, 1), (TT, 5)], -1: [(BB, 3), (BB, 7)]}
PAIRS = []
for sL in (+1, -1):
    for ct, ck in CH[sL]:
        for wt, wk in WB[sL]:
            ch = ChargedParam(ct, ck, rngL)
            ch.base.k = ck
            wb = SymParam(wt, wk, rngL)
            wb.base.k = wk
            PAIRS.append(Pair(ch, wb))
TESTS = [(ti, pi) for ti in range(len(TAUS)) for pi in range(len(PAIRS)) if PAIRS[pi].dof >= 1]
UE = {ti: SA.u_eta_np(np.array([t])) for ti, t in enumerate(TAUS)}
CK = HERE / "lepton_test_global_null.jsonl"


def family(data, seed):
    best_p, npass = 0.0, 0
    for k, (ti, pi) in enumerate(TESTS):
        U, E = UE[ti]
        pair = PAIRS[pi]
        _, v = fit_pair(pair, U, E, np.random.default_rng(seed * 1000 + k), data=data, n1=600, n2=3, n3=1, maxfev=2000)
        p = 1 - CHI2.cdf(v, pair.dof) if np.isfinite(v) and v < 1e29 else 0.0
        best_p = max(best_p, float(p))
        npass += int(v <= CHI2.ppf(0.95, pair.dof))
    return best_p, npass


def target(n):
    rt = np.random.default_rng(9100 + n)
    while True:
        tg = {o: DATA[o][0] + rt.uniform(-math.log(10) / 2, math.log(10) / 2, size=6) for o in ("NO", "IO")}
        if not any(np.any(np.exp(tg[o][2:5]) > 0.99) for o in tg):
            break
    td = {o: (tg[o], DATA[o][1], DATA[o][2]) for o in tg}
    bp, npass = family(td, 9100 + n)
    log("target", n, "family-best p", round(bp, 4), "passes", npass)
    return f"T {n}", {"family_best_p": bp, "passes": npass}


if __name__ == "__main__":
    done = {}
    if CK.exists():
        for line in CK.read_text().splitlines():
            if line.strip():
                d = json.loads(line)
                done[d["job"]] = d["rec"]
    jobs = ["D"] + [n for n in range(40) if f"T {n}" not in done]
    if "D" in done:
        jobs.remove("D")

    def run(j):
        if j == "D":
            bp, npass = family(DATA, 9099)
            log("data (reduced search)", "family-best p", round(bp, 4), "passes", npass)
            return "D", {"family_best_p": bp, "passes": npass}
        return target(j)

    with MPR.get_context("fork").Pool(2) as pool:
        for key, rec in pool.imap_unordered(run, jobs):
            with CK.open("a") as fh:
                fh.write(json.dumps({"job": key, "rec": rec}) + "\n")
            done[key] = rec
    sealed = json.loads((HERE / "lepton_test.json").read_text())["stage L"]
    sealed_best = max(1 - CHI2.cdf(r["chi2_min (a = 0.10)"], r["dof"]) for r in sealed if r["dof"] >= 1)
    D = done["D"]
    T = [done[f"T {n}"] for n in range(40)]
    p_global = sum(1 for t in T if t["family_best_p"] >= D["family_best_p"]) / len(T)
    out = {"label": "POST HOC, after 1caa0e263 was read", "tests": len(TESTS), "targets": len(T),
           "data family-best p (sealed search)": float(sealed_best), "data (reduced search)": D,
           "p_global": p_global, "null passes: median": float(np.median([t["passes"] for t in T])),
           "null passes: quartiles": [float(np.percentile([t["passes"] for t in T], q)) for q in (25, 75)],
           "prediction p_global >= 0.05 holds": bool(p_global >= 0.05), "seconds (this launch)": time.time() - T0}
    (HERE / "lepton_test_global_null.json").write_text(json.dumps(out, indent=1))
    log(out)
