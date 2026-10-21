#!/usr/bin/env python3
"""chat1, 2026-10-21 -- POST HOC (labelled), after the lepton test's output was read (1caa0e263): is the CKM phase
reachable at each quark-fixed tau*?

Why.  The quark stage (W114's chi-squared, inherited by LEPTON_TEST_RULE.md) fits m_u/m_c, m_c/m_t, m_d/m_s, m_s/m_b,
|V_us|, |V_cb|, |V_ub| and |V_td| -- not J.  The best lepton passes sit at tau* with Re tau near 0 (a CP locus), where
the quark fit is only compatible (chi2_q about 2.5), and a flat unitarity triangle there would be excluded by the
measured J.  This checks it, at all 36 tau*, written and committed before its one run.

Fixed now.  At each tau* (fixed), for its assignment, W114's quark model with tau held fixed:
  (A) the |V|-only fit (W114's chi2, a = 0.10): 3000 random coefficient vectors (seed 4000 + index), Nelder-Mead from
      the best 10 (6000 evaluations each), then from the best 2 again; read-outs chi2_A and J at the best point;
  (B) the same with log|J| added as a ninth observable: J = 3.08e-5, relative error 0.045 (PDG 2024's
      3.08 +0.15 -0.13 x 1e-5, symmetrised), combined with a = 0.10 as W66 does; chi2_B at the best point.
The predictions (priors), fixed now:
  P1 at the two Re tau ~ 0 sites (0.003 + 1.4875i, 0.00004 + 1.4061i), chi2_B - chi2_A > 9 (J excluded)   75%
  P2 at the exact quark sites (chi2_q < 1e-6; 16 of the 36), chi2_B < 3.84 (J reachable) at least at half   60%
Read-outs: chi2_A, chi2_B and J at every tau*.  Nothing here changes a sealed cell; it says which passes survive J.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
COMMIT = "c9f001d9ded23c059fae7d4475c98231404fec45"
SRC = "docs/dossiers/the_weave_2026-10-07/"
PINS = {"the_strong_angle.py": "a9c4b15b82739289b4698a388da117d4c517380826fcacfc16c6065221028622",
        "the_tuned_fit.py": "21f979beccd96c5470109d91579eff17af289c6951ed7485822a84e2149c713b",
        "received/HZ2021_running_masses_MZ.json": None, "received/B1612_data.json": None}
T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


TMP = Path(tempfile.mkdtemp(prefix="pj_sm_"))
for name, pin in PINS.items():
    blob = subprocess.check_output(["git", "-C", str(REPO), "show", f"{COMMIT}:{SRC}{name}"])
    if pin is not None and hashlib.sha256(blob).hexdigest() != pin:
        raise SystemExit(f"hash mismatch for {name}")
    (TMP / name).parent.mkdir(parents=True, exist_ok=True)
    (TMP / name).write_bytes(blob)
sys.path.insert(0, str(TMP))
import the_strong_angle as SA  # noqa: E402
import the_tuned_fit as TF  # noqa: E402
import multiprocessing as MPR  # noqa: E402

A = 0.10
J_D, J_REL = 3.08e-5, 0.045
P_, M_ = 1, -1
TT, BB, MQT, MQB = (P_, P_), (M_, M_), (P_, M_), (M_, P_)
QUARK = {11: (MQB, 4, BB, 7), 13: (BB, 7, MQB, 4), 14: (BB, 3, BB, 7)}
secs = {}
rngQ = np.random.default_rng(2110)
for num, (ut, uk, dt, dk) in QUARK.items():
    for typ, k in ((ut, uk), (dt, dk)):
        if (typ, k) not in secs:
            secs[(typ, k)] = TF.SectorParam(typ, k, rngQ)
TAUS = json.loads((HERE / "lepton_test_stageQ.json").read_text())["TAUS"]


def job(idx):
    T = TAUS[idx]
    num = T["assignment"]
    ut, uk, dt, dk = QUARK[num]
    model = TF.Model(secs[(ut, uk)], secs[(dt, dk)])
    tau = T["tau"]

    def full(v):
        return np.concatenate([[tau[0], tau[1]], v])

    def chiA(v):
        return model.chi2(full(v), SA.LOGD, A)

    def chiB(v):
        r = model.evaluate(full(v))
        if r is None:
            return 1e30
        obs, J = r[3][0][0], r[3][1][0]
        c = SA.chi2_many(obs, SA.LOGD, A)
        if not np.isfinite(c) or abs(J) < 1e-30:
            return 1e30
        z = (np.log(abs(J)) - np.log(J_D)) / np.hypot(J_REL, A)
        return float(c + z * z)

    def J_at(v):
        r = model.evaluate(full(v))
        return float(r[3][1][0]) if r is not None else float("nan")

    out = {"assignment": num, "tau*": tau, "chi2_q (stage Q)": T["chi2_q"]}
    nv = model.up.nfree + model.dn.nfree
    for lab, f in (("A", chiA), ("B", chiB)):
        rng = np.random.default_rng(4000 + idx + (0 if lab == "A" else 500))
        V = rng.normal(size=(3000, nv))
        vals = np.array([f(v) for v in V])
        order = np.argsort(vals)
        s2 = sorted((TF.nm(f, V[i], 6000) for i in order[:10]), key=lambda t: t[1])
        s3 = sorted((TF.nm(f, p, 6000) for p, _ in s2[:2]), key=lambda t: t[1])
        p, v = s3[0]
        out[f"chi2_{lab}"] = v
        out[f"J at the {lab} fit"] = J_at(p)
    log(idx, num, [round(x, 4) for x in tau], "chi2_A", round(out["chi2_A"], 3), "J_A", f"{out['J at the A fit']:.2e}",
        "chi2_B", round(out["chi2_B"], 3), "J_B", f"{out['J at the B fit']:.2e}")
    return idx, out


if __name__ == "__main__":
    with MPR.get_context("fork").Pool(2) as pool:
        res = dict(pool.map(job, range(len(TAUS))))
    rows = [res[i] for i in range(len(TAUS))]
    near0 = [r for r in rows if abs(r["tau*"][0]) < 0.01 and r["chi2_q (stage Q)"] > 1e-6]
    exact = [r for r in rows if r["chi2_q (stage Q)"] < 1e-6]
    P1 = all(r["chi2_B"] - r["chi2_A"] > 9 for r in near0)
    P2 = 2 * sum(1 for r in exact if r["chi2_B"] < 3.84) >= len(exact)
    out = {"label": "POST HOC, after 1caa0e263 was read", "rows": rows,
           "P1 (Re tau ~ 0 sites: J excluded)": {"sites": len(near0), "holds": bool(P1)},
           "P2 (exact sites: J reachable at least at half)": {"sites": len(exact),
                                                            "reachable": sum(1 for r in exact if r["chi2_B"] < 3.84),
                                                            "holds": bool(P2)},
           "seconds": time.time() - T0}
    (HERE / "lepton_test_posthoc_jckm.json").write_text(json.dumps(out, indent=1, default=str))
    log("P1", out["P1 (Re tau ~ 0 sites: J excluded)"], "P2", out["P2 (exact sites: J reachable at least at half)"])
    log("written lepton_test_posthoc_jckm.json")
