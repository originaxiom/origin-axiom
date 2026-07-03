"""B401 P1+P2 -- the class-group action on banked constants + prime spectroscopy."""
import json, os
from fractions import Fraction as Fr

# ---- P1: sigma_cl on the banked constants ----
def scl(t): return (t[0], -t[1], -t[2], t[3])
CONSTS = {
    "slot":        (Fr(0), Fr(0), Fr(-1,12), Fr(-1,12)),
    "3block":      (Fr(0), Fr(0), Fr(-1,12), Fr(1,12)),
    "face_B382":   (Fr(0), Fr(0), Fr(1,24),  Fr(-1,24)),
    "face_B397":   (Fr(0), Fr(0), Fr(-1,24), Fr(-1,24)),
    "class1_part": (Fr(0), Fr(0), Fr(-1,16), Fr(-1,16)),
    "class5_part": (Fr(0), Fr(0), Fr(-1,48), Fr(-1,48)),
}
orbit = {}
for n, v in CONSTS.items():
    im = scl(v)
    partner = next((m for m, w in CONSTS.items() if w == im), None)
    neg_partner = next((m for m, w in CONSTS.items() if tuple(-x for x in w) == im), None)
    orbit[n] = dict(image=[str(x) for x in im], equals=partner, equals_minus=neg_partner)
    print(f"P1 {n:13s} -> {[str(x) for x in im]}  = {partner or ''} {('= -'+neg_partner) if neg_partner else ''}")

# ---- P2: prime spectroscopy ----
def ideal_class(p):
    """ramified / inert / principal / nonprincipal in Q(sqrt-15), disc -15."""
    if p in (3, 5): return "ramified"
    if p == 2:
        return "nonprincipal"          # -15 = 1 mod 8 -> split; norm-2 form is 2x^2+xy+2y^2
    ls = pow(-15 % p, (p-1)//2, p)
    if ls == p-1: return "inert"
    # split: principal iff represented by x^2+xy+4y^2
    import itertools
    for x in range(-p, p+1):
        for y in range(-p, p+1):
            if x*x + x*y + 4*y*y == p: return "principal"
    return "nonprincipal"

PRIMES_SEEN = {
    2:  "denominators everywhere (2-powers up to 2^6)",
    3:  "denominators; the 3-side",
    5:  "denominators; the 5-side / golden boundary",
    7:  "the (3,4) Gram ratio 7/5; |tr J| = 7",
    23: "the Gram eigenvalue 23/19200; the 23/75 ratio",
    11: "handoff numerology only (6/11) -- control",
    13: "F4 Gram inner -13/57600",
}
spec = {}
for p, where in PRIMES_SEEN.items():
    c = ideal_class(p)
    spec[str(p)] = dict(cls=c, where=where)
    print(f"P2 prime {p:3d}: {c:13s} | {where}")
json.dump(dict(orbit=orbit, spectroscopy=spec),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p1_p2.json"), "w"), indent=1)
print("DONE")
