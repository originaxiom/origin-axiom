#!/usr/bin/env python3
"""B1612 -- POST-SEAL (disclosed, after the sealed comparison): the two fixed columns that survived D3 are one-parameter
relations.  With theta_13 measured, each predicts sin^2 theta_12:
  TM1 (first column (2/3, 1/6, 1/6)): |U_e1|^2 = cos^2 t12 cos^2 t13 = 2/3  ->  sin^2 t12 = 1 - 2 / (3 cos^2 t13)
  TM2 (second column (1/3, 1/3, 1/3)): |U_e2|^2 = sin^2 t12 cos^2 t13 = 1/3 ->  sin^2 t12 = 1 / (3 cos^2 t13)
Compared with the record's NuFIT 6.1 values (B1066's log: arXiv:2604.04585 Table 1, a secondary source, Nov 2025 data):
NO s13 = 0.02248 (+0.00055 -0.00059), s12 = 0.308 (+0.0067 -0.0066); IO s13 = 0.02262 (+0.00057 -0.00056), s12 = 0.308
(+-0.0067).  The pull uses the s12 uncertainty on the side of the prediction; the theta_13 uncertainty propagated is
reported beside it.  Writes post_seal_tm_sum_rules.json."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
fits = {"NO": {"s13": (0.02248, 0.00055, 0.00059), "s12": (0.308, 0.0067, 0.0066)},
        "IO": {"s13": (0.02262, 0.00057, 0.00056), "s12": (0.308, 0.0067, 0.0067)}}
out = {"source": "NuFIT 6.1 via arXiv:2604.04585 Table 1 (secondary; as recorded in B1066's log)"}
for o, f in fits.items():
    s13, up13, dn13 = f["s13"]; s12, up12, dn12 = f["s12"]; c13 = 1 - s13
    tm1 = 1 - 2 / (3 * c13); tm2 = 1 / (3 * c13)
    d1 = abs((1 - 2 / (3 * (1 - (s13 + up13)))) - tm1); d2 = abs(1 / (3 * (1 - (s13 + up13))) - tm2)
    out[o] = {"TM1_sin2_theta12": round(tm1, 5), "TM1_pull_sigma": round((tm1 - s12) / (up12 if tm1 > s12 else dn12), 2), "TM1_theta13_spread": round(d1, 5),
              "TM2_sin2_theta12": round(tm2, 5), "TM2_pull_sigma": round((tm2 - s12) / (up12 if tm2 > s12 else dn12), 2), "TM2_theta13_spread": round(d2, 5)}
json.dump(out, open(HERE / "post_seal_tm_sum_rules.json", "w"), indent=1); print(json.dumps(out, indent=1))
