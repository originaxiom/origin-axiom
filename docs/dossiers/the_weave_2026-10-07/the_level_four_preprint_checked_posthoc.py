"""W58, POST HOC (written after W58's one run and its read-out; labelled; W58's JSON is unchanged). Two cells failed as
worded: K4 on two printed entries, and K7(a) on the lepton anchor (pull -2.7 on the record's data). These checks trace
both.

  PH1  K4's two misses: m_c recomputed from Table I's measured m_t, and |V_td| from the printed (rounded) |V_ub| and
       theta13/theta23.
  PH2  the anchor m_tau/m_mu = eps^(-7/2) / (2 theta3)^4 with eps from the data (Eq. 23) instead of 14/75, on the
       preprint's Table I and on the record's data (Huang and Zhou at M_Z): the pull at the data ratio's own error (as
       K7 read it) and at the error propagated through eps from all three lepton masses (taken independent). The test
       statistic is T = ln(m_tau/m_mu) + (7/2) ln eps + 4 ln(2 theta3(tau(eps))), eps = (m_e m_tau / m_mu^2)^(2/3):
       data minus prediction in logs, so a pull is T / sigma.
  PH3  the anchor's coverage (K6's definition) at that propagated precision, on the declared family, the form-value
       family and the anchor's box.

Run: python3 the_level_four_preprint_checked_posthoc.py  ->  the_level_four_preprint_checked_posthoc.json beside it.
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_level_four_preprint_checked as LF  # noqa: E402  (W58: the claims, the thetas, the coverage)

OUT = HERE / "the_level_four_preprint_checked_posthoc.json"


def ph1():
    m, _ = LF.table_one()
    (t2, t3, t4), _ = LF.thetas_two_routes(LF.TAU_B)
    e = LF.EPS
    mc = 2 ** 1.5 * e ** 4 * t3 * m["t"]
    vtd = (0.003721 / 0.08865) ** 1.5
    return {"m_c from the measured m_t (GeV), printed 0.6239": mc,
            "|V_td| = (0.003721 / 0.08865)^(3/2), printed 0.008599": vtd,
            "both reproduce to the printed digits": bool(abs(mc - 0.6239) <= 1e-4 and abs(vtd - 0.008599) <= 1e-6)}


def T_stat(me, mmu, mtau, eps=None):
    e = (me * mtau / mmu ** 2) ** (2 / 3) if eps is None else eps
    tau = 2j / math.pi * math.log(1 / e)
    (_, t3, _), _ = LF.thetas_two_routes(tau)
    return math.log(mtau / mmu) + 3.5 * math.log(e) + 4 * math.log(2 * t3), e


def ph2_one(v, s):
    T0, e = T_stat(v["e"], v["mu"], v["tau"])
    grads, var = {}, 0.0
    for k in ("e", "mu", "tau"):
        h = 1e-6 * v[k]
        up, dn = dict(v), dict(v)
        up[k] += h
        dn[k] -= h
        g = (T_stat(up["e"], up["mu"], up["tau"])[0] - T_stat(dn["e"], dn["mu"], dn["tau"])[0]) / (2 * h / v[k])
        grads[k] = g
        var += (g * s[k] / v[k]) ** 2
    ratio_sig = math.hypot(s["tau"] / v["tau"], s["mu"] / v["mu"])
    T_fixed, _ = T_stat(v["e"], v["mu"], v["tau"], eps=LF.EPS)
    return {"eps from the data": e, "T (eps from the data)": T0, "T (eps = 14/75)": T_fixed,
            "d T / d ln m (e, mu, tau)": grads,
            "the data ratio's relative error (K7's sigma)": ratio_sig,
            "the propagated relative error of T": math.sqrt(var),
            "pull at K7's sigma (eps from the data)": T0 / ratio_sig,
            "pull at the propagated sigma (eps from the data)": T0 / math.sqrt(var),
            "pull at K7's sigma (eps = 14/75)": T_fixed / ratio_sig}


def ph2():
    m, _ = LF.table_one()
    s = LF.CLAIMS["Table I (MS-bar at M_Z, the preprint's Ref. [4]; masses in GeV)"]["sigma"]
    v, sh = LF.hz("HZ2021_running_masses_MZ.json")
    return {"the preprint's Table I": ph2_one(m, s), "the record's data (Huang and Zhou at M_Z)": ph2_one(v, sh)}


def ph3(sig):
    (_, t3, t4), _ = LF.thetas_two_routes(LF.TAU_B)
    y = LF.TAU_B.imag
    fam = {"declared": [k / 2 * math.log(2) for k in range(-2, 3)],
           "form-value": LF.prefactors(3, 3, t3, t4, y), "the anchor's box": LF.prefactors(8, 4, t3, t4, y)}
    m, _ = LF.table_one()
    t = LF.EPS ** -3.5 * m["mu"] / m["tau"]
    return {name: dict(zip(("coverage", "hits"), LF.coverage(t, sig, prefs))) for name, prefs in fam.items()}


def main():
    p2 = ph2()
    sig = p2["the preprint's Table I"]["the propagated relative error of T"]
    out = {"status": "W58 post hoc: K4's two misses and the anchor's precision traced (labelled; W58's JSON unchanged)",
           "PH1": ph1(), "PH2": p2,
           "PH3: the anchor's coverage at its propagated precision (Table I)": {"sigma": sig, **ph3(sig)}}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
