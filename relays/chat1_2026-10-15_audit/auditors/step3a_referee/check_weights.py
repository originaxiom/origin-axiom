"""Referee's read-only recomputation from weights_cells.json (no physics recomputed; reads committed JSON only)."""
import json, math, sys
from itertools import combinations

P = "/home/claude/origin-axiom/relays/chat1_2026-10-14_step3/weights_cells.json"
LL = "/home/claude/origin-axiom/relays/chat1_2026-10-14_selection/lagrange_law.json"
d = json.load(open(P))
per = d["per thread"]
words = list(per.keys())
print("n words", len(words))

def rots(w):
    return {w[k:] + w[:k] for k in range(len(w))}
def rev(w): return w[::-1]
def mir(w): return w.translate(str.maketrans("LR", "RL"))
def lyn(w): return min(rots(w))
def refl_sym(w):
    R = rots(w)
    return rev(w) in R or mir(w) in R

sym = [w for w in words if refl_sym(w)]
nonsym = [w for w in words if not refl_sym(w)]
print("reflection-symmetric:", len(sym), " non-symmetric:", len(nonsym))
print("non-symmetric words:", nonsym)

cells = ("C1", "C2", "C3")
adm = {c: [w for w in words if per[w][c]["admitted"]] for c in cells}
for c in cells:
    print(c, "admitted", len(adm[c]))
print("same admitted set in all cells:", set(adm["C1"]) == set(adm["C2"]) == set(adm["C3"]))
excl = [w for w in words if w not in adm["C1"]]
print("excluded:", [(w, round(per[w]["y_max"], 4)) for w in excl])
print("min y_max among excluded:", min(per[w]["y_max"] for w in excl), " max y_max among admitted:", max(per[w]["y_max"] for w in adm["C1"]))
print("excluded all symmetric:", all(refl_sym(w) for w in excl))
# why excluded: y_max>3 vs N-agreement vs K pd
for w in excl:
    print("  ", w, {c: (per[w][c]["K positive definite"], per[w][c]["N256 vs N384"]) for c in cells})
ll = json.load(open(LL))
llper = ll["readouts"]["per thread"]
ll_adm = [w for w in llper if llper[w].get("admitted")]
ll_excl = [w for w in llper if not llper[w].get("admitted")]
print("Lagrange law admitted:", len(ll_adm), " excluded:", sorted(ll_excl))
print("same ten as Lagrange law:", sorted(ll_excl) == sorted(excl))

print("\n== N256 vs N384, worst admitted per cell ==")
for c in cells:
    w_ = max(adm[c], key=lambda w: per[w][c]["N256 vs N384"])
    print(c, per[w_][c]["N256 vs N384"], w_)
    # note: C3 uses only m2/m3; what about m1/m2 agreement etc is not in JSON

print("\n== root ==")
for c in cells:
    r = per["LR"][c]
    m = r["m"]
    print(c, "masses/m3:", [x / m[2] for x in m], "m2/m3", r["m2/m3"], "m1/m3", r["m1/m3"], "m1/m2", r["m1/m2"])

print("\n== S1: C3 m1/m3 on admitted ==")
v = max((per[w]["C3"]["m1/m3"], w) for w in adm["C3"])
print("max C3 m1/m3 admitted:", v)
print("count < 1e-10:", sum(per[w]["C3"]["m1/m3"] < 1e-10 for w in adm["C3"]))

band = lambda c: [w for w in adm[c] if 0.002 <= per[w][c]["m2/m3"] <= 0.07]
print("\n== bands ==")
for c in cells:
    print(c, "in band:", len(band(c)))
print("C2 band m1/m2 range:", min((per[w]["C2"]["m1/m2"], w) for w in band("C2")), max((per[w]["C2"]["m1/m2"], w) for w in band("C2")))
print("C2 all admitted m1/m2 range:", min((per[w]["C2"]["m1/m2"], w) for w in adm["C2"]), max((per[w]["C2"]["m1/m2"], w) for w in adm["C2"]))
mins = sorted((per[w]["C2"]["m1/m2"], w) for w in band("C2"))[:4]
print("C2 smallest in band:", mins)
print("S2 hits:", [w for w in band("C2") if per[w]["C2"]["m1/m2"] <= 0.005])
print("C2 band list:", sorted(band("C2")))
print("C3 band list (", len(band("C3")), "):", sorted(band("C3")))
print("S4 JSON list equals:", sorted(band("C3")) == sorted(d["S4"]["C3 admitted in the band"]))
print("root in C3 band:", "LR" in band("C3"), per["LR"]["C3"]["m2/m3"])
c2s = sorted(((per[w]["C2"]["m2/m3"], w) for w in adm["C2"]), reverse=True)[:5]
print("C2 top m2/m3:", c2s)
print("C1 band least m1/m2:", sorted((per[w]["C1"]["m1/m2"], w) for w in band("C1"))[:4])
print("C1 band (", len(band("C1")), ") ", sorted(band("C1")))
print("JSON readout C1 least:", d["readouts"]["C1 under the invariant formula: least m1/m2 in the band"])
print("C1 all admitted m1/m2 min:", sorted((per[w]["C1"]["m1/m2"], w, per[w]["C1"]["m2/m3"]) for w in adm["C1"])[:6])

print("\n== factor-10 claim: least m1/m2 in band over C1 and C2 vs 0.002 and 0.0047 ==")
for c in ("C1", "C2"):
    m = min(per[w][c]["m1/m2"] for w in band(c))
    print(c, m, "ratio to 0.0047:", m / 0.0047, "ratio to 0.002:", m / 0.002)

print("\n== phi checks ==")
phi = (1 + 5 ** 0.5) / 2
a, b = per["LR"]["C2"]["m2/m3"], per["LR"]["C2"]["m1/m3"]
print("m2/m3", a, "phi/2", phi / 2, "abs diff", phi / 2 - a, "rel", (phi / 2 - a) / (phi / 2))
print("m1/m3", b, "1/phi", 1 / phi, "abs diff", 1 / phi - b, "rel", (1 / phi - b) / (1 / phi))
print("root C2 N256 vs N384:", per["LR"]["C2"]["N256 vs N384"])

print("\n== Spearman (recomputed, no scipy: rank correlation by hand) ==")
def rank(xs):
    idx = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[idx[j + 1]] == xs[idx[i]]:
            j += 1
        for k in range(i, j + 1):
            r[idx[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
def spearman(x, y):
    rx, ry = rank(x), rank(y)
    n = len(x); mx = sum(rx) / n; my = sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    return cov / math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
for c in cells:
    ws = adm[c]
    print(c, spearman([per[w]["y_max"] for w in ws], [math.log(per[w][c]["m2/m3"]) for w in ws]),
          "JSON:", d["readouts"][f"{c}: Spearman(y_max, ln m2/m3)"])

print("\n== C3 root vs threads below y = 1.75 ==")
low = sorted((per[w]["y_max"], w, per[w]["C3"]["m2/m3"]) for w in adm["C3"] if per[w]["y_max"] < 1.75)
for t in low:
    print("  y=%.4f %-10s C3 m2/m3=%.6f  mirror-lyndon=%s" % (t[0], t[1], t[2], lyn(mir(t[1]))))
distinct = {}
for y, w, v in low:
    key = frozenset({w, lyn(mir(w))})
    distinct.setdefault(key, []).append((w, v))
print("distinct up to mirror:", len(distinct), "(including root)")
others = [v for y, w, v in low if w != "LR"]
print("range over others:", min(others), max(others))
# what about thresholds near 1.75
print("y values near 1.75:", sorted(set(round(per[w]["y_max"], 4) for w in adm["C3"]))[:15])

print("\n== nearest per sector ==")
print(d["readouts"]["nearest admitted (thread, cell) per sector, in (ln m2/m3, ln m1/m3) distance (read-out only)"])

print("\n== reality ==")
def im(w, c, key):
    return per[w][c]["matrices (N = 384)"][key]
adm_sym = [w for w in adm["C1"] if refl_sym(w)]
adm_non = [w for w in adm["C1"] if not refl_sym(w)]
print("admitted symmetric:", len(adm_sym), " admitted non-symmetric:", len(adm_non))
for c in cells:
    kl = max((im(w, c, "max|Im K_L|/|K_L|"), w) for w in adm_sym)
    kr = max((im(w, c, "max|Im K_R|/|K_R|"), w) for w in adm_sym)
    y = max((im(w, c, "max|Im Y|/|Y|"), w) for w in adm_sym)
    print(c, "SYM  max ImKL", kl, " max ImKR", kr, " max ImY", y)
for c in cells:
    kl = (min(im(w, c, "max|Im K_L|/|K_L|") for w in adm_non), max(im(w, c, "max|Im K_L|/|K_L|") for w in adm_non))
    kr = (min(im(w, c, "max|Im K_R|/|K_R|") for w in adm_non), max(im(w, c, "max|Im K_R|/|K_R|") for w in adm_non))
    y = (min(im(w, c, "max|Im Y|/|Y|") for w in adm_non), max((im(w, c, "max|Im Y|/|Y|"), w) for w in adm_non))
    print(c, "NON  ImKL range", kl, " ImKR range", kr, " ImY range", y)
# all 51 symmetric, including excluded
for c in cells:
    y = max((im(w, c, "max|Im Y|/|Y|"), w) for w in sym)
    k = max((max(im(w, c, "max|Im K_L|/|K_L|"), im(w, c, "max|Im K_R|/|K_R|")), w) for w in sym)
    print(c, "ALL 51 SYM max ImY", y, " max ImK", k)

print("\n== H-ORTH ==")
print("max H-orth residual admitted:", max((per[w]["H-orth residual"], w) for w in adm["C1"]))
print("max H-orth residual all:", max((per[w]["H-orth residual"], w) for w in words))
cb_adm = [(x, w) for w in adm["C1"] for x in per[w]["|c_b|"]]
cb_all = [(x, w) for w in words for x in per[w]["|c_b|"]]
print("|c_b| admitted range:", min(cb_adm), max(cb_adm))
print("|c_b| all range:", min(cb_all), max(cb_all))
print("root |c_b|:", per["LR"]["|c_b|"])
