#!/usr/bin/env python3
"""W146, POST HOC (after the one run's read-out, which found L1 recorded as failed and the other eight cells held).
Nothing here was in the rule.

  P1  the diagnosis of L1: the script added to the rule's cell a second condition, Lemma A's identity
      sum_k m_k^2 |<conj g, l_k>|^2 = |g.g|^2 |u|^2 to 1e-20 relative, which held only to 8.5e-14 at 30 digits. The
      same 20 000 draws (the generator seeded 146, as in the run) are replayed: at 30 digits they reproduce the run's
      two numbers, and at 60 digits the identity's relative error falls with the precision. The worst draw's |g.g|,
      |u| and right side are read out
  P2  the rule's own L1 prediction, as run: sympy's identity and the light-state bound (never exceeded by 1e-12)

    python3 -B the_higgs_invariant_dichotomy_posthoc.py      # writes the_higgs_invariant_dichotomy_posthoc.json
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W  # noqa: E402  (W146's committed script, unchanged)

OUT = HERE / "the_higgs_invariant_dichotomy_posthoc.json"


def replay(dps, n=20000):
    """L1's loop exactly as committed, with the working precision as a parameter"""
    rng = np.random.default_rng(146)
    worst, worst_id, at = -mp.inf, mp.mpf(0), None
    h0 = np.array([0, 1, 1j]) / np.sqrt(2)
    with mp.workdps(dps):
        for i in range(n):
            w = complex(rng.normal(), rng.normal())
            u = W.crandn(rng, 3) * 10 ** rng.uniform(-3, 1)
            g = h0 + 10 ** rng.uniform(-6, 0) * W.crandn(rng, 3) if i % 2 else W.crandn(rng, 3)
            g = g / np.linalg.norm(g)
            gm = [mp.mpc(x) for x in g]
            gm = [x / mp.sqrt(W.nrm2(gm)) for x in gm]
            um = [mp.mpc(x) for x in u]
            Y = mp.matrix(W.Y_of(mp.mpc(w), um, gm, mp))
            E, Q = mp.eighe(Y * Y.H)
            m = [mp.sqrt(max(e, 0)) for e in E]
            gbar = [mp.conj(x) for x in gm]
            ov = [abs(sum(mp.conj(Q[r, k]) * gbar[r] for r in range(3))) for k in range(3)]
            sin_t = mp.sqrt(ov[1] ** 2 + ov[2] ** 2)
            gg = abs(W.dot(gm, gm))
            worst = max(worst, sin_t - gg * mp.sqrt(W.nrm2(um)) / m[1])
            rhs = gg ** 2 * W.nrm2(um)
            err = abs(sum(m[k] ** 2 * ov[k] ** 2 for k in range(3)) - rhs) / rhs
            if err > worst_id:
                worst_id, at = err, {"draw": i, "|g.g|": mp.nstr(gg, 3), "|u|": mp.nstr(mp.sqrt(W.nrm2(um)), 3),
                                     "right side": mp.nstr(rhs, 3), "m3": mp.nstr(m[2], 4)}
    return {"max (sin theta - bound)": mp.nstr(worst, 4), "max relative identity error": mp.nstr(worst_id, 3),
            "worst draw": at}


def main():
    run = json.loads((HERE / "the_higgs_invariant_dichotomy.json").read_text(encoding="utf-8"))["L1"]
    r30, r60 = replay(30), replay(60)
    same = (r30["max (sin theta - bound)"] == run["max (sin theta - |g.g| |u| / m2)"]
            and r30["max relative identity error"] == run["max relative |sum m_k^2 |<conj g, l_k>|^2 - |g.g|^2 |u|^2|"])
    out = {"arc": "W146", "status": "POST HOC, after the read-out",
           "P1 the replay at 30 digits": r30, "P1 it reproduces the run's two numbers": bool(same),
           "P1 the replay at 60 digits": r60,
           "P1 the identity's error falls by at least 10^25 at 60 digits": bool(
               mp.mpf(r60["max relative identity error"]) < mp.mpf(r30["max relative identity error"]) * 1e-25),
           "P2 the rule's prediction as run": {"sympy identity": run["Y h = Y^T h = (h.h) u (sympy)"],
                                                "bound never exceeded by 1e-12": bool(
                                                    mp.mpf(run["max (sin theta - |g.g| |u| / m2)"]) <= 1e-12)}}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
