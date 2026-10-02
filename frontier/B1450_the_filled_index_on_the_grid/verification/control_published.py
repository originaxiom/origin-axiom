#!/usr/bin/env python3
"""Control: the instrument against every figure-eight entry published in Celoria-Hodgson-Rubinstein,
arXiv:2509.09886, Tables 9 and 10 and the limit series below Table 9 (to q^10)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from filled_index import filled, s_str
X = 20
def ser(*c, half=None):
    d = {2 * i: v for i, v in enumerate(c) if v}
    if half: d.update({k: v for k, v in half.items() if v})
    return d
ONE = {0: 1}
PUB = {
    (1, 0): {}, (0, 1): ONE, (1, 1): ONE, (2, 1): ONE, (3, 1): ONE, (4, 1): None,
    (5, 1): ser(1, -1, -2, -1, -1, 1, 2, 7, 8, 12, 14),
    # the printed row has "1 - t - q^(3/2) ..."; t is read here as q^(1/2)
    (6, 1): {0: 1, 1: -1, 3: -1, 4: -1, 5: -1, 9: 1, 10: 3, 11: 4, 12: 4, 13: 6, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 6, 20: 4},
    (7, 1): ser(1, 0, -1, 0, 1, 3, 3, 6, 4, 2, -4),
    (8, 1): ser(1, 0, -1, 0, 2, 5, 6, 8, 4, -2, -14),
    (9, 1): ser(1, 0, -1, 0, 0, 2, 2, 4, 1, -1, -6),
    (10, 1): {0: 1, 4: -1, 5: 1, 7: 1, 9: 1, 10: 2, 11: 2, 12: 2, 13: 1, 14: 4, 15: -1, 16: 2, 17: -5, 19: -9, 20: -4},
    (1, 2): ser(1, -2, -3, 0, 3, 10, 14, 22, 20, 14, -2),
    (1, 3): ser(1, -2, -3, 1, 6, 13, 16, 17, 4, -20, -55),
    (1, 4): ser(1, -2, -3, 1, 6, 13, 16, 17, 4, -20, -54),
}
LIMIT = ser(1, 0, -1, 0, 0, 2, 2, 4, 2, 0, -4)      # lim_{n -> oo} I_{m004(n,1)}, to q^10
ok = 0
for sl, pub in PUB.items():
    got, info = filled(sl[0], sl[1], X)
    good = (got is None) if pub is None else (got == pub)
    ok += good
    print(sl, "AGREES" if good else "DIFFERS", "| undefined" if got is None else "| " + (s_str(got, X) or "0"), flush=True)
got, info = filled(40, 1, X); good = got == LIMIT; ok += good
print((40, 1), "equals the published limit series to q^10" if good else "DIFFERS from the limit series", "|", s_str(got, X), flush=True)
print("published entries reproduced: %d of %d" % (ok, len(PUB) + 1))
