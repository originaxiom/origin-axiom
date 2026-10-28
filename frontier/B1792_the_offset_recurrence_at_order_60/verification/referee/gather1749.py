import pathlib
import json, math, pickle, importlib.util, sys
from fractions import Fraction as Fr
R = str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/")
sp = importlib.util.spec_from_file_location("b1726_census", R + "B1726_the_two_ingredients_replicated/verification/census.py")
K = importlib.util.module_from_spec(sp); sys.modules["b1726_census"] = K; sp.loader.exec_module(K)
L = K.lines()
want = {i: (a, b) for i, (a, b) in enumerate(L) if Fr(a) == Fr(2, 5)}
print("slope-2/5 lines in B1726's 266:", len(want), sorted((str(b), math.lcm(Fr(a).denominator, Fr(b).denominator)) for a, b in want.values()))
P = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "rb"))
n = 0
with open(R + "B1749_the_six_at_fresh_apexes/verification/census.jsonl") as fh:
    for l in fh:
        r = json.loads(l)
        if r["line"] not in want: continue
        a, b = want[r["line"]]; n += 1
        key = (str(Fr(b)), round(r["Re_tau"], 9), round(r["Im_tau"], 9))
        rec = {"order": math.lcm(Fr(a).denominator, Fr(b).denominator), "src": "B1749"}
        for h in ("L_max", "L_2"):
            rec[h] = {sec + rd: [math.log(max(x, 1e-300)) for x in r[f"{sec}|{h}|{rd}"]] for sec in ("up", "down", "lep") for rd in ("S", "St")}
        P["rows"][key] = rec
print("B1749 slope-2/5 rows", n)
pickle.dump(P, open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "wb"))
