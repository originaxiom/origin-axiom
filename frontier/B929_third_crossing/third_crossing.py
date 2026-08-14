"""B929 THE THIRD CROSSING — computed per the sealed prereg; data contacted after seal.

Object side (banked, blind): B928's m_S primary (m_A secondary), ascending-rho order.
Measured side (post-seal contact): PDG CKM moduli |V_us| = 0.2243 +- 0.0008,
|V_cb| = 0.0408 +- 0.0014, |V_ub| = 0.00382 +- 0.00020 (world averages).
Tiers per seal: T1 shape (same-side cascade + a = ln r2/ln r1 in (1,3));
T2 quant (factor-2 per ratio, both orientations, doubling priced).
"""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
B928 = json.load(open(os.path.join(HERE, "..", "B928_d2_decode", "results.json")))

# the sheet: m_S branch values in K, ascending-rho (banked exact rationals-in-K
# evaluated: use the stored 50d certificates)
certs = B928["Q3_certificates_50d_by_ascending_rho"]
def get3(name):
    v = certs[name]
    return [float(x) for x in v] if isinstance(v, list) else None
mS = get3("m_S") or get3("mS")
mA = get3("m_A") or get3("mA")
res = {"sheet_mS": mS, "sheet_mA": mA}
s = [abs(x) for x in mS]
r1, r2 = s[1]/s[0], s[2]/s[1]
res["object_triple_s"] = s
res["r"] = [r1, r2]

# measured (post-seal)
Vus, Vcb, Vub = 0.2243, 0.0408, 0.00382
q1, q2 = Vcb/Vus, Vub/Vcb
res["measured_q"] = [q1, q2]

# T1
same_side = (r1 > 1 and r2 > 1) or (r1 < 1 and r2 < 1)
a = math.log(r2)/math.log(r1) if r1 != 1 else float("inf")
T1 = bool(same_side and 1 < a < 3)
res["T1"] = {"same_side": same_side, "a": a, "pass": T1}

# T2 (both orientations; factor 2)
def within2(x, y): return 0.5 <= x/y <= 2.0
o1 = within2(r1, q1) and within2(r2, q2)
o2 = within2(1/r1, q1) and within2(1/r2, q2)
T2 = bool(o1 or o2)
res["T2"] = {"orient_fwd": o1, "orient_rev": o2, "pass": T2,
             "ratios_fwd": [r1/q1, r2/q2], "ratios_rev": [(1/r1)/q1, (1/r2)/q2]}

verdict = "HIT-FULL" if (T1 and T2) else ("HIT-SHAPE" if T1 else "MISS")
res["sealed_verdict"] = verdict
res["priced_bits"] = 2

# secondary (non-verdict): m_A ratios; v-weight ratios vs mass cascade
sa = [abs(x) for x in mA]
res["secondary_mA_r"] = [sa[1]/sa[0], sa[2]/sa[1]]
# v-weights from HIER roots (banked 90d values)
v2 = [5.69496465426270228, 8.32706418238040182, 19.4508737756638681]
import math as m2
v = [m2.sqrt(x) for x in v2]
res["secondary_v_ratios"] = [v[1]/v[0], v[2]/v[1]]
# quark mass cascade (PDG MSbar, rough): up-type m_u:m_c:m_t and down-type
res["secondary_note"] = "recorded only; no verdict weight per seal"

json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print("object triple s:", ["%.6g" % x for x in s])
print("r1, r2 =", "%.6g" % r1, "%.6g" % r2, " a =", "%.4g" % a)
print("measured q1, q2 =", "%.6g" % q1, "%.6g" % q2)
print("T1:", T1, " T2:", T2)
print("SEALED VERDICT:", verdict)
