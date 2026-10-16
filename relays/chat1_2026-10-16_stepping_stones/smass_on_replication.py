"""S-mass, post hoc, on the S-shape replication's fresh configurations (a scoreboard: the data were seen; no claim).

The replication (seal ec8ba7e87, output 2a4bd10fe) computed the per-field masses of the Standard Model and 112
distinct nulls on 136 classes of closing configurations (Lyndon words of length 13 and 14 at height <= 3, N = 9, 11,
12), but its seal scored only S-shape. This scores S-mass on the same masses, exactly as the low-thread seal defined it
(W66's predicate as W88 used it, a = 0.10, six ratios, Sigma z^2 <= 12.592, its acceptance rules), so that the
low-thread result (no assignment passes anywhere on T-low) can be extended to these configurations or not.
Usage: python3 -B smass_on_replication.py <decompressed s_shape_seal_output.json> > smass_on_replication_run.txt
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units")
A_ALLOW, CHI6 = 0.10, 12.592
SEC_DATA = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
hz = json.load(open(os.path.join(TU, "received_HZ2021_running_masses_MZ.json")))
MV, MS = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
target = {}
for sec, (f1, f2, f3) in SEC_DATA.items():
    target[sec] = [(MV[f1] / MV[f3], math.hypot(MS[f1] / MV[f1], MS[f3] / MV[f3])),
                   (MV[f2] / MV[f3], math.hypot(MS[f2] / MV[f2], MS[f3] / MV[f3]))]
o = json.load(open(sys.argv[1]))
recs = [r for r in o["records"] if r["kind"] == "class" and not r.get("error")]
names = sorted({k.split("|")[0] for k in recs[0]["cells"]})
best = {n: (float("inf"), None) for n in names}
passes = {n: 0 for n in names}
cells_total = 0
for r in recs:
    for cell in sorted({k.split("|")[2] for k in r["cells"]}):
        cells_total += 1
        for n in names:
            chi, ok = 0.0, True
            for sec in SEC_DATA:
                c = r["cells"].get(f"{n}|{sec}|{cell}")
                key = tuple(r["plan"][f"{n}|{sec}"][0])
                if c is None or min(c["s"]) <= 1e-30 * max(c["s"]) or not (c["s"][0] < c["s"][1] < c["s"][2]) \
                        or r["closure"].get(f"pf|{key}", 1) > 1e-20 or c["r_calc"] is None or c["r_calc"] > 1e-6:
                    ok = False; break
                s1, s2, s3 = c["s"]
                for (x, rx), val in zip(target[sec], (s1 / s3, s2 / s3)):
                    z = (math.log(val) - math.log(x)) / math.sqrt(c["r_calc"] ** 2 + rx ** 2 + A_ALLOW ** 2)
                    chi += z * z
            if not ok:
                continue
            passes[n] += int(chi <= CHI6)
            if chi < best[n][0]:
                best[n] = (chi, f"N={r['N']} {r['word']} {tuple(r['line'])} {cell}")
nb = sorted((v[0], n) for n, v in best.items() if n != "SM")
print(f"class-cells per assignment: {cells_total // 1}; assignments: {len(names)} (the SM and {len(names) - 1} nulls)")
print(f"S-mass passes: SM {passes['SM']}; nulls total {sum(v for n, v in passes.items() if n != 'SM')}")
print(f"the SM's best chi^2: {best['SM'][0]:.1f} at {best['SM'][1]}")
print(f"the nulls' best chi^2: {nb[0][0]:.1f} ({nb[0][1]}); median of the nulls' best: {nb[len(nb) // 2][0]:.1f}; "
      f"the SM's rank by its best: {1 + sum(1 for v, n in nb if v < best['SM'][0])} of {len(names)}")
