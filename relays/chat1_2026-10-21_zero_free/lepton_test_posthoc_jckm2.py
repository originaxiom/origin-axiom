#!/usr/bin/env python3
"""chat1, 2026-10-21 -- POST HOC (labelled), second instrument: J_CKM at the stage-Q quark solutions themselves.

Why.  The first post-hoc instrument (lepton_test_posthoc_jckm.py, output 44b51519a) refitted the quarks at each fixed
tau* with a small search and did not reproduce stage Q's chi2_q at most sites (e.g. 166 against 2.7e-18), so its J
verdicts are not trusted.  This instrument does not refit: it replays stage Q exactly (the sealed script's seeds,
search sizes and creation order, lepton_test.py at c848d32b0) for the assignments named on the command line, keeps
every endpoint's parameters, and reads J at each kept endpoint (chi2_q <= 3.84).  Written and committed before its
one run.

Read-outs, per kept endpoint: tau in F, chi2_q, J, and the observables.  The check of the replay: the distinct tau*
it finds equal stage Q's (lepton_test_stageQ.json) to 1e-6.
No prediction is made; the measured J is 3.08e-5 (PDG 2024).
"""
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC = (HERE / "lepton_test.py").read_text()
HEAD = SRC.split("# ------------------------------------------------------------------------------------------- the launch fix")[0]
NS = {"__file__": str(HERE / "lepton_test.py"), "__name__": "lepton_test_head"}
exec(compile(HEAD, "lepton_test_head", "exec"), NS)
SA, TF, QUARK, A_ALLOW = NS["SA"], NS["TF"], NS["QUARK"], NS["A_ALLOW"]
T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


secs = {}
rngQ = np.random.default_rng(2110)
for num, (ut, uk, dt, dk) in QUARK.items():          # the sealed creation order
    for typ, k in ((ut, uk), (dt, dk)):
        if (typ, k) not in secs:
            secs[(typ, k)] = TF.SectorParam(typ, k, rngQ)

nums = [int(x) for x in sys.argv[1:]] or [11, 13, 14]
out = {"label": "POST HOC, after 1caa0e263 and 44b51519a were read", "assignments": {}}
stageQ = json.loads((HERE / "lepton_test_stageQ.json").read_text())
for num in nums:
    ut, uk, dt, dk = QUARK[num]
    model = TF.Model(secs[(ut, uk)], secs[(dt, dk)])
    rng = np.random.default_rng(2110 + num)
    P1 = TF.random_starts(model, rng, 40000)
    v1 = TF.stage1(model, P1, SA.LOGD, A_ALLOW)
    order = np.argsort(v1)
    f = lambda p: model.chi2(p, SA.LOGD, A_ALLOW)  # noqa: E731
    kept = []
    for i in order[:200]:
        p, v = TF.nm(f, P1[i], 6000)
        p, v = TF.nm(f, p, 6000)
        if v <= 3.84:
            r = model.evaluate(p, ycap=1e9)
            tf, obs, J = r[0], r[3][0][0], r[3][1][0]
            kept.append({"tau": [tf.real, tf.imag], "chi2_q": v, "J": float(J), "obs": obs.tolist()})
    distinct = sorted({(round(abs(k["tau"][0]), 3), round(k["tau"][1], 3)) for k in kept})
    sq = sorted({(round(abs(q["tau"][0]), 3), round(q["tau"][1], 3)) for q in stageQ["QOUT"][str(num)]["distinct tau*"]})
    out["assignments"][str(num)] = {"kept": kept, "replay matches stage Q": distinct == sq}
    for k in sorted(kept, key=lambda k: k["chi2_q"]):
        log(num, [round(x, 4) for x in k["tau"]], f"chi2_q {k['chi2_q']:.2e}", f"J {k['J']:.3e}")
    log(num, "replay matches stage Q:", distinct == sq)
    (HERE / f"lepton_test_posthoc_jckm2_{'_'.join(map(str, nums))}.json").write_text(json.dumps(out, indent=1))
log("written")
