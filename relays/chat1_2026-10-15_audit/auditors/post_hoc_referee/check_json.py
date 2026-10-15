"""Referee 2 (read-only): recompute the read-out's numbers from post_hoc_completions.json and weights_cells.json."""
import json, math, sys, statistics
from scipy.stats import spearmanr

D = "<repo>/relays/chat1_2026-10-14_step3/"
p = json.load(open(D + "post_hoc_completions.json"))["per thread"]
s = json.load(open(D + "weights_cells.json"))["per thread"]
words = list(p)
print("threads", len(words))

# ---------------- (a) admission sets
for comp in ("H-ORTH", "H-E4", "H-PART", "H-THETA2"):
    for cell in ("C2", "C3"):
        adm = sorted(w for w in words if p[w][f"{comp} {cell}"]["admitted"])
        print(comp, cell, "admitted", len(adm))
sealed_adm = {c: sorted(w for w in words if s[w][c]["admitted"]) for c in ("C1", "C2", "C3")}
ph_adm = {f"{comp} {cell}": sorted(w for w in words if p[w][f"{comp} {cell}"]["admitted"])
          for comp in ("H-ORTH", "H-E4") for cell in ("C2", "C3")}
base = sealed_adm["C2"]
print("same admitted set everywhere (sealed C1..C3, post hoc H-ORTH/H-E4):",
      all(v == base for v in list(sealed_adm.values()) + list(ph_adm.values())))
unadm = [w for w in words if w not in base]
print("unadmitted:", [(w, round(p[w]["y_max"], 3)) for w in unadm])
# would the unadmitted ones fail N-agreement too?
for w in unadm:
    print("  ", w, {k: f'{p[w][k]["N256 vs N384"]:.1e}' for k in ("H-ORTH C2", "H-ORTH C3", "H-E4 C2", "H-E4 C3")},
          "sealed C2/C3 agree", f'{s[w]["C2"]["N256 vs N384"]:.1e}', f'{s[w]["C3"]["N256 vs N384"]:.1e}')
# worst N agreement among admitted
for k in ("H-ORTH C2", "H-ORTH C3", "H-E4 C2", "H-E4 C3"):
    print("worst admitted N256/384", k, max(p[w][k]["N256 vs N384"] for w in base))

# ---------------- (a) the control: H-ORTH from the E4 basis vs weights_cells.json
rows = []
for w in words:
    d = []
    for cell in ("C2", "C3"):
        for k in (("m2/m3", "m1/m3") if cell == "C2" else ("m2/m3",)):
            a, b = p[w][f"H-ORTH {cell}"][k], s[w][cell][k]
            d.append((abs(a - b) / abs(b), cell, k))
    rows.append((max(d), w))
adm_d = sorted((r[0][0], r[1], r[0][1], r[0][2]) for r in rows if r[1] in base)
all_d = sorted((r[0][0], r[1], r[0][1], r[0][2]) for r in rows)
print("control worst over admitted:", adm_d[-1])
print("control median over admitted:", statistics.median(x[0] for x in adm_d))
print("control worst over all:", all_d[-1])
print("control top 12 overall:")
for x in all_d[-12:]:
    print("   ", f"{x[0]:.2e}", x[1], x[2], x[3], "admitted" if x[1] in base else "UNADMITTED", "y", round(p[x[1]]["y_max"], 2))
# also m1/m3 for C3 and per-quantity breakdown on the admitted
for cell, k in (("C2", "m2/m3"), ("C2", "m1/m3"), ("C3", "m2/m3")):
    v = [abs(p[w][f"H-ORTH {cell}"][k] - s[w][cell][k]) / abs(s[w][cell][k]) for w in base]
    print("  admitted", cell, k, "max", f"{max(v):.2e}", "median", f"{statistics.median(v):.2e}")

# ---------------- (b) rank 2 under H-E4
for cell in ("C2", "C3"):
    k = f"H-E4 {cell}"
    m13 = [(p[w][k]["m1/m3"], w) for w in base]
    print(k, "rank2 flag on all admitted:", all(p[w][k]["rank 2"] for w in base), "max m1/m3 admitted", max(m13))
    print("   max m1/m3 over all threads", max((p[w][k]["m1/m3"], w) for w in words))
    print("   max m1/m2 over admitted", max((p[w][k]["m1/m2"], w) for w in base))

# ---------------- (c) the table
for comp in ("H-ORTH", "H-E4"):
    for cell in ("C2", "C3"):
        k = f"{comp} {cell}"
        r = p["LR"][k]
        order = sorted(base, key=lambda w: -p[w][k]["m2/m3"])
        band = [w for w in base if 0.002 <= p[w][k]["m2/m3"] <= 0.07]
        rk2 = sum(p[w][k]["rank 2"] for w in base)
        rho = spearmanr([p[w]["y_max"] for w in base], [math.log(p[w][k]["m2/m3"]) for w in base]).correlation
        print(k, "root 1 :", round(r["m2/m3"], 4), ":", f'{r["m1/m3"]:.4g}', "place", order.index("LR") + 1, "of", len(base),
              "band", len(band), "rank2 on", rk2, "Spearman", round(rho, 4))
        if comp == "H-E4" and cell == "C3":
            print("    band threads:", sorted((round(p[w][k]["m2/m3"], 5), w, round(p[w]["y_max"], 2)) for w in band))
        if comp == "H-ORTH" and cell == "C2":
            r3band = [w for w in band if not p[w][k]["rank 2"]]
            print("    least m1/m2 in band", min((p[w][k]["m1/m2"], w) for w in r3band))
            print("    m1/m2 range over admitted", min(p[w][k]["m1/m2"] for w in base), max(p[w][k]["m1/m2"] for w in base))

k = "H-E4 C3"
low = sorted((p[w]["y_max"], w, p[w][k]["m2/m3"]) for w in base if p[w]["y_max"] < 1.75)
print("H-E4 C3, admitted below y = 1.75:", len(low))
for y, w, v in low:
    print("   ", w, round(y, 3), round(v, 4))
others = [v for y, w, v in low if w != "LR"]
print("   others' range", min(others), max(others))
srt = sorted((p[w][k]["m2/m3"], w, round(p[w]["y_max"], 3)) for w in base)
print("H-E4 C3 lowest admitted:", srt[:6])
srt_all = sorted((p[w][k]["m2/m3"], w, round(p[w]["y_max"], 3), w in base) for w in words)
print("H-E4 C3 lowest over ALL threads:", srt_all[:8])
# distinct values below y=1.75 (mirror pairs)
print("H-ORTH C3 others below y=1.75:", sorted(round(p[w]["H-ORTH C3"]["m2/m3"], 4) for y, w, v in low if w != "LR"))
