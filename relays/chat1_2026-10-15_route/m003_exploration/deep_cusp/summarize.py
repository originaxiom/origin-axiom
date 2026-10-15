import json, math, sys
R = json.load(open(sys.argv[1]))
print("per thread: ln(s2/s1)/(2 pi rho), ln(s3/s1)/(2 pi rho) [W84 law: -1, -1.5], ln max|Y|, closure, convergence")
for key, v in R.items():
    rho = v["rho"]
    print(f"\n{key}  rho = {rho:.3f}  Npts {v['Npts']}")
    for sec in ("zero", "up", "down", "lepton"):
        if sec not in v: continue
        z = v[sec]
        row = []
        for cell, d in z["cells"].items():
            if d is None: row.append(f"{cell}: --"); continue
            row.append(f"{cell}: {d['ln s2/s1']/(2*math.pi*rho):+.3f} {d['ln s3/s1']/(2*math.pi*rho):+.3f} lnY {d['ln max|Y|']:.1f} cv {d['conv (ln, Npts vs 0.8 Npts)']:.0e}")
        print(f"  {sec:6s} clos {z['closure (Y1 integrand, one period on)']:.0e} rad {z['max ball radius']:.0e}")
        for r_ in row: print("      " + r_)

print("\nslopes along each tower (per unit 2 pi rho): d ln(s2/s1), d ln(s3/s1)  [W84: -1, -1.5]; d ln Kdiag/(2 pi drho) [W84: 1.75, 0.25, 1.25 in K32]")
towers = {}
for key, v in R.items():
    towers.setdefault(key.split("N=")[1], []).append((v["rho"], key))
for N, lst in towers.items():
    lst.sort()
    for (r1, k1), (r2, k2) in zip(lst, lst[1:]):
        d = 2 * math.pi * (r2 - r1)
        print(f"\nN={N}: rho {r1:.2f} -> {r2:.2f}")
        for sec in ("zero", "up", "down", "lepton"):
            out = []
            for cell in R[k1][sec]["cells"]:
                a, b = R[k1][sec]["cells"][cell], R[k2][sec]["cells"][cell]
                if a is None or b is None: continue
                out.append(f"{cell} {(b['ln s2/s1']-a['ln s2/s1'])/d:+.3f} {(b['ln s3/s1']-a['ln s3/s1'])/d:+.3f}")
            kd = [(y - x) / d for x, y in zip(R[k1][sec]["cells"]["C1"]["ln K diag"], R[k2][sec]["cells"]["C1"]["ln K diag"])]
            dy = (R[k2][sec]["cells"]["C1"]["ln max|Y|"] - R[k1][sec]["cells"]["C1"]["ln max|Y|"]) / d
            print(f"  {sec:6s} K32 diag {[round(x,3) for x in kd]}  C1 ln max|Y| per 2 pi drho {dy:+.3f}")
            print("      " + " | ".join(out))
