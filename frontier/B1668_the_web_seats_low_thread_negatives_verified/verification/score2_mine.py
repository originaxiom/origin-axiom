"""Independent S-mass scorer for per-field scoreboards (midheight_scan / s_shape replication), written from the
twisted-units preregistration (S-mass: z=(ln Xcalc - ln Xdata)/sqrt(rcalc^2+rdata^2+a^2), a=0.10, six ratios,
sum z^2 <= 12.592; acceptance: closure<=1e-20, rcalc<=1e-6, s1>1e-30 s3, strictly ordered)."""
import json, sys, math, collections
o = json.load(open(sys.argv[1])); dd = sys.argv[2]
hz = json.load(open(f"{dd}/received_HZ2021_running_masses_MZ.json"))["masses_GeV"]; mv, ms = hz["value"], hz["sigma"]
a = 0.10
T = {}
for sec, (p, q, w) in {"up": "uct", "down": "dsb", "lepton": ("e", "mu", "tau")}.items():
    T[sec] = [(math.log(mv[p]/mv[w]), math.hypot(ms[p]/mv[p], ms[w]/mv[w])), (math.log(mv[q]/mv[w]), math.hypot(ms[q]/mv[q], ms[w]/mv[w]))]
recs = [r for r in o["records"] if r.get("kind", "class") == "class" and not r.get("error")]
print("class records", len(recs), "errors", sum(1 for r in o["records"] if r.get("error")))
names = sorted({k.split("|")[0] for k in recs[0]["cells"]}); print("assignments", len(names))
best = {n: (1e300, None) for n in names}; passes = collections.Counter(); acc = 0; ncell = 0
bandbest = {}
def band(h): return "h<=3" if h <= 3 else "3<h<=4" if h <= 4 else "4<h<=5" if h <= 5 else "5<h<=6"
for r in recs:
    cells = sorted({k.split("|")[2] for k in r["cells"] if k.startswith("SM|up|")})
    for c in cells:
        ncell += 1
        for n in names:
            chi = 0.0; ok = True
            for s in ("up", "down", "lepton"):
                e = r["cells"].get(f"{n}|{s}|{c}")
                cl = r["closure"].get("pf|" + str(tuple(r["plan"][f"{n}|{s}"][0])))
                if e is None or cl is None or e["r_calc"] is None: ok = False; break
                sv = e["s"]
                if not (sv[0] > 1e-30*sv[2] and sv[0] < sv[1] < sv[2] and cl <= 1e-20 and e["r_calc"] <= 1e-6): ok = False; break
                for (lt, rt), lv in zip(T[s], (math.log(sv[0]/sv[2]), math.log(sv[1]/sv[2]))):
                    chi += ((lv - lt)**2) / (e["r_calc"]**2 + rt**2 + a*a)
            if not ok: continue
            acc += 1; passes[n] += chi <= 12.592
            if chi < best[n][0]: best[n] = (chi, (r["N"], r["word"], tuple(r["line"]), c))
            k = ("SM" if n == "SM" else "null", band(r["height"]))
            if chi < bandbest.get(k, (1e300,))[0]: bandbest[k] = (chi, n)
nulls = sorted((v[0], n) for n, v in best.items() if n != "SM")
print("class-cells/assignment", ncell, "accepted (all assignments)", acc)
print("passes SM", passes["SM"], "nulls total", sum(passes[n] for n in names if n != "SM"))
print("SM best", best["SM"]); print("best null", nulls[0], best[nulls[0][1]][1]); print("median null best", nulls[len(nulls)//2][0])
print("SM rank", 1 + sum(v < best["SM"][0] for v, _ in nulls), "of", len(names))
for k in sorted(bandbest): print("band best", k, bandbest[k])
