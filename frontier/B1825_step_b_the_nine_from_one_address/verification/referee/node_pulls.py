# post-scan: ten pulls at the least-chi2_ten and least-chi2_nine node rows; appended to node_scan.json
import sys, json, gzip, math
import numpy as np
P = "frontier/B1825_step_b_the_nine_from_one_address/verification/referee/node_scan.json"
J = json.load(open(P)); tt = np.array(J["t10"]); tt[4] -= math.log(3); tt[5] += math.log(3); sig = np.array(J["sigma"])
names = ["c/t","u/t","s/b","d/b","mu/tau","e/tau","|V_us|","|V_cb|","|V_ub|","|J|"]
out = {}
for k in ("ten", "nine"):
    b = J["best"][k]; fn, tau, line, d, r, lab = b[1], b[2], b[3], b[4], b[5], b[6]
    for ln in gzip.open("audit/drafts/rigid_census/refined/" + fn, "rt"):
        rec = json.loads(ln)
        if rec.get("tau") == tau and rec.get("line") == line and "rows" in rec:
            for x in rec["rows"]:
                if x[0] == d and x[1] == r and x[2] == lab:
                    f = np.log(np.array([x[3][1], x[3][0], x[4][1], x[4][0], x[5][1], x[5][0], x[6][0], x[6][1], x[6][2], abs(x[7])]))
                    out[k] = dict(zip(names, ((f - tt) / sig).tolist())); out[k]["chi2"] = float((((f-tt)/sig)**2).sum())
J["pulls"] = out; json.dump(J, open(P, "w"), indent=1); print(json.dumps(out, indent=1))
