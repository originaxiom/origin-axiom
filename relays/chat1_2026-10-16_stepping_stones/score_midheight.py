"""S-mass and the direction of the misses on the per-field thread frame's masses (a scoreboard: the data were seen; no claim).

Scores a record file written by midheight_scan.py (3 < h <= 6, words of length <= 16) or by the S-shape replication's
sealed run (s_shape_seal.py; words of length 13 and 14 at h <= 3; only its "class" records), with the acceptance rules
and S-mass exactly as the low-thread seal defined them (W66's predicate as W88 used it: a = 0.10, six ratios,
Sigma z^2 <= 12.592; a class-cell is accepted for an assignment only if every sector has three nonzero, strictly
ordered masses, closure <= 1e-20 on its line and r_calc <= 1e-6). On the replication's file it must reproduce
smass_on_replication_run.txt; that is its check.

Read-outs:
- coverage (errors, point counts, the largest accepted r_calc and closure);
- S-mass: passes for the Standard Model and the nulls, their best chi^2, the SM's rank;
- the coherent rule's threads (main's S_THE_PUSH_BACK §8.3b, D alone: Psi = #R - #L = 0 mod 4): how many classes, and
  S-mass restricted to them;
- which way the masses miss, over accepted class-cells: the median of ln(predicted / observed) for each of the six
  ratios (negative: the predicted hierarchy is stronger than the observed one), the fraction of cells where it is
  positive, and the median of ln(predicted ratio) / ln(observed ratio) (above 1: too strong); for the SM, and for
  every assignment pooled; overall and by height band.
Usage: python3 -B score_midheight.py <records.json> > <run.txt>
"""
import json, math, os, statistics as st, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units")
A_ALLOW, CHI6, CLOSURE_MAX, RCALC_MAX = 0.10, 12.592, 1e-20, 1e-6
SEC_DATA = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}
hz = json.load(open(os.path.join(TU, "received_HZ2021_running_masses_MZ.json")))
MV, MS = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
target = {}
for sec, (f1, f2, f3) in SEC_DATA.items():
    target[sec] = [(MV[f1] / MV[f3], math.hypot(MS[f1] / MV[f1], MS[f3] / MV[f3])),
                   (MV[f2] / MV[f3], math.hypot(MS[f2] / MV[f2], MS[f3] / MV[f3]))]

o = json.load(open(sys.argv[1]))
allrecs = [r for r in o["records"] if r.get("kind", "class") == "class"]
errs = [r for r in allrecs if r.get("error")]
recs = [r for r in allrecs if not r.get("error")]
names = sorted({k.split("|")[0] for r in recs for k in r["cells"]})
nulls = [n for n in names if n != "SM"]
hs = sorted(r["height"] for r in recs)
print(f"records: {len(allrecs)} classes, {len(errs)} with an error; heights {hs[0]:.3f} .. {hs[-1]:.3f}; "
      f"N: {sorted({r['N'] for r in recs})}; assignments: {len(names)} (the SM and {len(nulls)} nulls)")
if "npp" in recs[0]:
    npps = {}
    for r in recs:
        npps[r["npp"]] = npps.get(r["npp"], 0) + 1
    print(f"points per unit length (classes): {dict(sorted(npps.items()))}")


def band(h):
    return "h<=3" if h <= 3 else ("3<h<=4" if h <= 4 else ("4<h<=5" if h <= 5 else "5<h<=6"))


def accepted(r, n, cell):
    out = []
    for sec in SEC_DATA:
        c = r["cells"].get(f"{n}|{sec}|{cell}")
        key = tuple(r["plan"][f"{n}|{sec}"][0])
        cval = r["closure"].get(f"pf|{key}")
        if c is None:
            return None, "no masses"
        if min(c["s"]) <= 1e-30 * max(c["s"]):
            return None, "rank deficient"
        if not (c["s"][0] < c["s"][1] < c["s"][2]):
            return None, "degenerate singular values"
        if cval is None or cval > CLOSURE_MAX:
            return None, "closure"
        if c["r_calc"] is None or c["r_calc"] > RCALC_MAX:
            return None, "convergence"
        out.append(c)
    return out, None


best = {n: (float("inf"), None) for n in names}
passes = {n: 0 for n in names}
why_sm, cells_total, acc_sm, acc_all = {}, 0, 0, 0
lr = {}          # (who, band, sec, i) -> list of ln(pred/obs)
lq = {}          # (who, band, sec, i) -> list of ln(pred)/ln(obs)
worst_rc, worst_cl = 0.0, 0.0
best_by_band = {}
coh = {"classes": 0, "SM passes": 0, "null passes": 0, "SM best": float("inf"), "nulls best": float("inf")}
for r in recs:
    b = band(r["height"])
    psi0 = (r["word"].count("R") - r["word"].count("L")) % 4 == 0
    coh["classes"] += int(psi0)
    for cell in sorted({k.split("|")[2] for k in r["cells"]}):
        cells_total += 1
        for n in names:
            cs, why = accepted(r, n, cell)
            if cs is None:
                if n == "SM":
                    why_sm[why] = why_sm.get(why, 0) + 1
                continue
            acc_all += 1
            acc_sm += int(n == "SM")
            chi = 0.0
            for sec, c in zip(SEC_DATA, cs):
                s1, s2, s3 = c["s"]
                worst_rc = max(worst_rc, c["r_calc"])
                key = tuple(r["plan"][f"{n}|{sec}"][0])
                worst_cl = max(worst_cl, r["closure"][f"pf|{key}"])
                for i, ((x, rx), val) in enumerate(zip(target[sec], (s1 / s3, s2 / s3)), start=1):
                    z = (math.log(val) - math.log(x)) / math.sqrt(c["r_calc"] ** 2 + rx ** 2 + A_ALLOW ** 2)
                    chi += z * z
                    for who in (("SM", "all") if n == "SM" else ("all",)):
                        for bb in ("all heights", b):
                            lr.setdefault((who, bb, sec, i), []).append(math.log(val) - math.log(x))
                            lq.setdefault((who, bb, sec, i), []).append(math.log(val) / math.log(x))
            passes[n] += int(chi <= CHI6)
            if psi0:
                who_ = "SM" if n == "SM" else "null"
                coh[f"{who_} passes"] += int(chi <= CHI6)
                kb = "SM best" if n == "SM" else "nulls best"
                coh[kb] = min(coh[kb], chi)
            if chi < best[n][0]:
                best[n] = (chi, f"N={r['N']} {r['word']} {tuple(r['line'])} h={r['height']:.3f} {cell}")
            k = ("SM" if n == "SM" else "nulls", b)
            if (chi, n) < best_by_band.get(k, (float("inf"), "")):
                best_by_band[k] = (chi, n)

nb = sorted((v[0], n) for n, v in best.items() if n != "SM")
print(f"class-cells per assignment: {cells_total}; accepted: SM {acc_sm}, all assignments {acc_all}; "
      f"the SM's rejections by reason: {dict(sorted(why_sm.items()))}")
print(f"largest accepted r_calc {worst_rc:.1e}; largest accepted closure {worst_cl:.1e}")
print(f"S-mass passes: SM {passes['SM']}; nulls total {sum(passes[n] for n in nulls)}")
print(f"the SM's best chi^2: {best['SM'][0]:.1f} at {best['SM'][1]}")
print(f"the nulls' best chi^2: {nb[0][0]:.1f} ({nb[0][1]} at {best[nb[0][1]][1]}); median of the nulls' best: "
      f"{nb[len(nb) // 2][0]:.1f}; the SM's rank by its best: {1 + sum(1 for v, n in nb if v < best['SM'][0])} of {len(names)}")
for k in sorted(best_by_band):
    print(f"  best chi^2 in {k[1]:8s} ({k[0]}): {best_by_band[k][0]:.1f}" + (f" ({best_by_band[k][1]})" if k[0] == "nulls" else ""))
print(f"the coherent rule's threads (Psi = 0 mod 4): {coh['classes']} of {len(recs)} classes; S-mass passes there: SM "
      f"{coh['SM passes']}, nulls {coh['null passes']}; best chi^2 there: SM {coh['SM best']:.1f}, nulls {coh['nulls best']:.1f}")
print("which way the masses miss: median ln(pred/obs) [fraction of cells weaker than observed] "
      "{median ln-ratio pred/obs}")
bands = ["all heights"] + sorted({band(r["height"]) for r in recs})
for who in ("SM", "all"):
    for bb in bands:
        if (who, bb, "up", 1) not in lr:
            continue
        n_ = len(lr[(who, bb, "up", 1)])
        row = []
        for sec in SEC_DATA:
            parts = []
            for i in (1, 2):
                v, q = lr[(who, bb, sec, i)], lq[(who, bb, sec, i)]
                parts.append(f"m{i}/m3 {st.median(v):+6.2f} [{sum(x > 0 for x in v) / len(v):.2f}] {{{st.median(q):.2f}}}")
            row.append(f"{sec}: " + ", ".join(parts))
        print(f"  {'the SM' if who == 'SM' else 'every assignment'}, {bb} ({n_} accepted class-cells): " + "; ".join(row))
