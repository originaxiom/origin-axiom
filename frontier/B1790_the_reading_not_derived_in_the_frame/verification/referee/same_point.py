import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import common as C, json, numpy as np
from fractions import Fraction as Fr
d = json.load(open(__import__("pathlib").Path(__file__).resolve().parent.parent / "mirror.json"))
for r in d:
    re, im, a, b = r["point"]; sp = C.spectra(complex(re, im), Fr(a), Fr(b), "L_max")
    dev = max(abs(C.dln(sp[(s, "S")], sp[(s, "St")]) - r["%s|L_max|S" % s][1]) for s in C.SECT)
    print(r["point"], "| note's flip column minus same-point S-vs-St difference (L_max, max over sectors): %.1e" % dev)
