"""Attack 5: B1788's tropical.predict per reading; (a) the note's 2/5 table; (b) slopes (denominator <= 60) where a sector's reading
leaves its m1/m3 exponent unchanged; (c) any slope a' where the flipped assignment (S, S~, S~) has the exponents of (S~, S, S) at 2/5;
(d) local exponents from the frame at Im tau 4.0-5.0 on (2/5, 1/10) and (2/5, 3/10), every sector and reading (own driver)."""
import sys; sys.path.insert(0, str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/B1788_the_closed_form_of_the_exponents/verification")); sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import tropical as T, math, json
from fractions import Fraction as Fr
P = {rd: T.polys(rd) for rd in ("S", "St")}
def ex(a, sec, rd):
    l, r = T.SECTORS[sec]; return T.predict(P[rd], T.E(T.SIXY[l] * a, T.SIXY[r] * a))
print("(a) alpha = 2/5:", {"%s %s" % (s, rd): tuple(map(str, ex(Fr(2, 5), s, rd))) for s in T.SECTORS for rd in ("S", "St")})
print("    alpha = 1/10:", {"%s %s" % (s, rd): tuple(map(str, ex(Fr(1, 10), s, rd))) for s in T.SECTORS for rd in ("S", "St")})
blind = {s: [] for s in T.SECTORS}; m2diff = []; allslopes = sorted({Fr(j, N) for N in range(1, 61) for j in range(N)})
target = {"up": ex(Fr(2, 5), "up", "St"), "down": ex(Fr(2, 5), "down", "S"), "lep": ex(Fr(2, 5), "lep", "S")}
partners = []
for a in allslopes:
    for s in T.SECTORS:
        eS, eT = ex(a, s, "S"), ex(a, s, "St")
        if eS[1] == eT[1]: blind[s].append(str(a))
        if eS[0] != eT[0]: m2diff.append((str(a), s))
    if ex(a, "up", "S") == target["up"] and ex(a, "down", "St") == target["down"] and ex(a, "lep", "St") == target["lep"]: partners.append(str(a))
print("(b) %d slopes; m1/m3 exponent reading-blind: up %d, down %d, lep %d; examples up:" % (len(allslopes), len(blind["up"]), len(blind["down"]), len(blind["lep"])), blind["up"][:12])
print("    second-generation exponent differs between readings on:", m2diff[:10], "(count %d)" % len(m2diff))
print("(c) slopes whose flipped assignment reproduces (S~,S,S)'s exponents at 2/5:", partners)
import common as C, numpy as np
res = {}
for b in (Fr(1, 10), Fr(3, 10)):
    ys = (4.0, 4.5, 5.0); sp = {y: C.spectra(complex(0.3, y), Fr(2, 5), b, "L_max") for y in ys}
    for s in C.SECT:
        for rd in ("S", "St"):
            loc = [float(-math.log(sp[y2][(s, rd)][1] / sp[y1][(s, rd)][1]) / (2 * math.pi * (y2 - y1))) for y1, y2 in ((4.0, 4.5), (4.5, 5.0))]
            loc2 = [float(-math.log(sp[y2][(s, rd)][0] / sp[y1][(s, rd)][0]) / (2 * math.pi * (y2 - y1))) for y1, y2 in ((4.0, 4.5), (4.5, 5.0))]
            res["(2/5,%s) %s %s" % (b, s, rd)] = {"m2/m3 local": [round(x, 3) for x in loc2], "m1/m3 local": [round(x, 3) for x in loc], "closed": [str(e) for e in ex(Fr(2, 5), s, rd)]}
for k, v in res.items(): print("(d)", k, v)
json.dump(res, open(__import__("pathlib").Path(__file__).resolve().parent / "exponents.json", "w"), indent=1)
