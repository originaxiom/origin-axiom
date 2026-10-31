"""Step B's control: the census's evaluator (B1821's cm_zero_line.rows_at, which the refined census ran) reproduces B1726's
sealed DR census (data-free: both are frame outputs).  B1726 writes w = a tau + b and stores (m2/m3, m1/m3); B1821 writes
w = a tau - b and stores (m1/m3, m2/m3): B1726's line (a, b) is B1821's (a, -b).  Both use the same b1656_funcs (byte-
identical copies) and B1691's sections.  40 random B1726 points; every sector, both radii, both readings, and the CKM for each
(up, down) reading pair.  Prints the largest |ln| difference only."""
import json, math, pathlib, random, sys
from fractions import Fraction as Fr
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
spec = __import__("importlib.util").util.spec_from_file_location("b1726", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
B26 = __import__("importlib.util").util.module_from_spec(spec); spec.loader.exec_module(B26)
recs = [json.loads(l) for l in (ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.jsonl").read_text().splitlines()]
random.seed(20261030); pick = random.sample(recs, 40); L = B26.lines()
worst = {"sectors": 0.0, "ckm_moduli": 0.0, "ckm_J": 0.0}; n = 0
for r in pick:
    a, b = L[r["line"]]
    rows = Z.rows_at(complex(r["Re_tau"], r["Im_tau"]), (a, (-b) % 1))
    dr = [x for x in rows if x["direction"] == "DR"]
    def row(rad, ru, rd):
        lab = ("S~" if ru == "St" else "S") + ("S~" if rd == "St" else "S") + "S"
        return next(x for x in dr if x["radius"] == rad and x["reading"] == lab)
    for sec, key in (("up", "up"), ("down", "down"), ("lep", "lepton")):
        for rad in ("L_max", "L_2"):
            for rn in ("S", "St"):
                x = row(rad, rn if sec == "up" else "S", rn if sec == "down" else "S") if sec != "lep" else \
                    next(y for y in dr if y["radius"] == rad and y["reading"].endswith("S~" if rn == "St" else "S") and y["reading"].startswith("SS"))
                m21, m11 = r["%s|%s|%s" % (sec, rad, rn)]
                mine = x[key]                                              # (m1/m3, m2/m3)
                for p_, q_ in ((m11, mine[0]), (m21, mine[1])):
                    if p_ > 1e-12 and q_ > 1e-12: worst["sectors"] = max(worst["sectors"], abs(math.log(p_ / q_)))
    for rad in ("L_max", "L_2"):
        for ru in ("S", "St"):
            for rd in ("S", "St"):
                x = row(rad, ru, rd); v = r["ckm|%s|%s|%s" % (rad, ru, rd)]
                for p_, q_ in zip(v[:3], x["V"]):
                    if p_ > 1e-12 and q_ > 1e-12: worst["ckm_moduli"] = max(worst["ckm_moduli"], abs(math.log(p_ / q_)))
                if abs(v[3]) > 1e-15 and abs(x["J"]) > 1e-15: worst["ckm_J"] = max(worst["ckm_J"], abs(math.log(abs(v[3]) / abs(x["J"]))))
    n += 1
print(json.dumps({"points": n, "largest_abs_ln_difference": worst}))
