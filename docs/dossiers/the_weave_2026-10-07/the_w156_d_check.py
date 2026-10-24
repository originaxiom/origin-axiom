# Post hoc (2026-10-24, after W156's read): which census row carries B1749 FINDINGS' D = 10.94? D from the stored
# values (reading (S~, S, S), c = 3, L_max) at the 12 rows below the six's bar, on this seat's arithmetic. Not sealed.
import json, math, subprocess
REV = "f3038f81b53e69b11d4c1f429d53b657ae837f65"
raw = subprocess.run(["git", "show", f"{REV}:frontier/B1749_the_six_at_fresh_apexes/verification/census.jsonl"],
                     capture_output=True, text=True, check=True).stdout
rows = [json.loads(l) for l in raw.splitlines() if l.strip()]
strip = json.load(open("docs/dossiers/the_weave_2026-10-07/third_opinion_b1749.json"))["C1"]["rows"]
for s in strip:
    for r in rows:
        if abs(r["Re_tau"] - s["Re_tau"]) < 1e-9 and abs(r["Im_tau"] - s["Im_tau"]) < 1e-9 and r["line"] in (149, 151):
            up, dn, lep = r["up|L_max|St"], r["down|L_max|S"], r["lep|L_max|S"]
            lmt, let = math.log(lep[0]) + math.log(3), math.log(lep[1]) - math.log(3)
            D = math.exp(lmt + math.log(dn[1]) - math.log(dn[0]) - let)
            if (s["line"] == ["2/5", "1/10"]) == (r["line"] == 149):
                print(round(s["chi2_six"], 3), s["line"], r["Re_tau"], round(r["Im_tau"], 4), "D", round(D, 3))
