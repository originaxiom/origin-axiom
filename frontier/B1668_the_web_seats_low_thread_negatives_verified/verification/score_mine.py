"""Independent scorer for the twisted-units T-low output, written from PREREGISTRATION_TWISTED_UNITS.md sections 3-6
(not importing twisted_units_seal.score). Usage: score_mine.py output.json data_dir"""
import json, sys, math, numpy as np, collections
out_path, ddir = sys.argv[1], sys.argv[2]
d = json.load(open(out_path)); recs = d["records"]
hz = json.load(open(f"{ddir}/received_HZ2021_running_masses_MZ.json"))["masses_GeV"]
ck = json.load(open(f"{ddir}/received_B1612_data.json"))["ckm_abs"]
mv, ms = hz["value"], hz["sigma"]; a = 0.10
SECS = {"up": "uct", "down": "dsb", "lepton": ("e", "mu", "tau")}
names3 = {"up": ("u","c","t"), "down": ("d","s","b"), "lepton": ("e","mu","tau")}
tgt = {}
for s, (x, y, w) in names3.items():
    r1 = mv[x]/mv[w]; r2 = mv[y]/mv[w]
    e1 = math.hypot(ms[x]/mv[x], ms[w]/mv[w]); e2 = math.hypot(ms[y]/mv[y], ms[w]/mv[w])
    l1, l2 = math.log(r1), math.log(r2)
    tgt[s] = dict(l1=l1, l2=l2, e1=e1, e2=e2, lrho=math.log(l1/l2), erho=math.hypot(e1/abs(l1), e2/abs(l2)))
VV, VS = ck["value"], ck["sigma"]
ctg = {k: (math.log(VV[i][j]), VS[i][j]/VV[i][j]) for k, (i, j) in {"us": (0,1), "cb": (1,2), "ub": (0,2)}.items()}
def zf(lx, rx, ly, ry): return (lx-ly)/math.sqrt(rx*rx+ry*ry+a*a)
CHI = {"mass": 12.592, "shape": 7.815, "ckm": 7.815}
asg = sorted({k.split("|")[0] for r in recs for k in r["plan"]})
assert len(asg) == 200 and "SM" in asg
rows = []   # one per (rec, assignment, reading, cell)
fail = collections.Counter(); worst_clos = 0.0; maxrc = 0.0
for r in recs:
    clos = r["closure"]; C = r["cells"]
    for name in asg:
        for reading, tag, pi in (("per-field", "pf", 0), ("minimal", "mn", 1)):
            cells = sorted({k.split("|")[3] for k in C if k.startswith(f"{name}|{reading}|up|")})
            for cell in cells:
                ok = True; E = {}
                for s in SECS:
                    e = C.get(f"{name}|{reading}|{s}|{cell}")
                    key = tuple(r["plan"][f"{name}|{s}"][pi]); cl = clos.get(f"{tag}|{key}")
                    if e is None or cl is None: ok = False; fail["missing"] += 1; continue
                    sv = e["s"]; worst_clos = max(worst_clos, cl); maxrc = max(maxrc, e["r_calc"])
                    if not (sv[0] > 1e-30*sv[2]): ok = False; fail["zero sv"] += 1
                    if not (sv[0] < sv[1] < sv[2]): ok = False; fail["degenerate"] += 1
                    if cl > 1e-20: ok = False; fail["closure"] += 1
                    if e["r_calc"] > 1e-6: ok = False; fail["rcalc"] += 1
                    E[s] = e
                row = dict(i=r["index"], N=r["N"], name=name, reading=reading, cell=cell, ok=ok, word=r["word"])
                if ok:
                    cm = cs = 0.0; 
                    for s, e in E.items():
                        sv = e["s"]; l1 = math.log(sv[0]/sv[2]); l2 = math.log(sv[1]/sv[2]); rc = e["r_calc"]
                        t = tgt[s]
                        z1 = zf(l1, rc, t["l1"], t["e1"]); z2 = zf(l2, rc, t["l2"], t["e2"])
                        lrho = math.log(l1/l2)
                        er = math.hypot(rc/abs(l1), rc/abs(l2))
                        zr = zf(lrho, er, t["lrho"], t["erho"])
                        cm += z1*z1 + z2*z2; cs += zr*zr
                        row[s] = (l1, l2)
                    Uu = np.array([[complex(*z) for z in rr] for rr in E["up"]["U"]])
                    Ud = np.array([[complex(*z) for z in rr] for rr in E["down"]["U"]])
                    V = np.abs(Uu.conj().T @ Ud); rcc = max(E["up"]["r_calc"], E["down"]["r_calc"])
                    cc = 0.0
                    for k, (i, j) in {"us": (0,1), "cb": (1,2), "ub": (0,2)}.items():
                        cc += zf(math.log(V[i, j]), rcc, *ctg[k])**2
                    row.update(chi_mass=cm, chi_shape=cs, chi_ckm=cc,
                               w94=(E["lepton"]["s"][1]/E["lepton"]["s"][2])/(E["down"]["s"][1]/E["down"]["s"][2]))
                rows.append(row)
print("rows", len(rows), "failures", dict(fail), "worst closure", worst_clos, "max r_calc", maxrc)
import pickle; pickle.dump(rows, open(out_path.rsplit("/",1)[0] + "/mine_rows.pkl", "wb"))
res = {}
def counts(stat, reading, scope):
    c = collections.Counter()
    for w in rows:
        if w["reading"] != reading or (scope != "all" and w["N"] != scope): continue
        if w["ok"] and w["chi_"+stat] <= CHI[stat]: c[w["name"]] += 1
    sm = c["SM"]; nulls = [c[n] for n in asg if n != "SM"]
    return sm, (1 + sum(x >= sm for x in nulls))/(len(nulls)+1), sum(nulls)/len(nulls)
for st, rd, sc in [("mass","per-field","all"),("mass","minimal","all"),("shape","per-field","all"),("shape","minimal","all"),
                   ("ckm","per-field","all"),("ckm","minimal","all"),("mass","per-field",9),("mass","per-field",11),("mass","per-field",12),
                   ("shape","per-field",9),("shape","per-field",11),("shape","per-field",12)]:
    print("claim", st, rd, sc, counts(st, rd, sc))
# best chi2
for rd in ("per-field", "minimal"):
    best = collections.defaultdict(lambda: (1e300, None))
    for w in rows:
        if w["reading"] == rd and w["ok"] and w["chi_mass"] < best[w["name"]][0]: best[w["name"]] = (w["chi_mass"], (w["N"], w["word"], w["cell"]))
    sm = best["SM"]; nul = sorted(v[0] for n, v in best.items() if n != "SM")
    allb = sorted(v[0] for v in best.values())
    print(rd, "SM best chi2", sm, "best null", nul[0], "SM rank among 200 by best cell", allb.index(sm[0]) + 1)
    n_pass = sum(1 for w in rows if w["reading"] == rd and w["ok"] and w["chi_mass"] <= 12.592)
    print(rd, "total mass passes (any assignment)", n_pass)
print("accepted assignment-cells", sum(w["ok"] for w in rows), "of", len(rows))
print("SM cells", sum(1 for w in rows if w["name"] == "SM"))
w94 = [w["w94"] for w in rows if w["name"] == "SM" and w["ok"]]
print("W94 SM range", min(w94), max(w94))
