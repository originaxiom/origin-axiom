"""Auditor: are chat1's Reading-A negatives invariant if M is the lane's literal (block-conjugated) quaternion su(2)?
S = diag(b, a, ab) flips the Cartan's sign on blocks b and ab: h_Q' = (-1, 1, 1, -1, -1, 1) on ws_0..ws_5."""
import json, itertools
from collections import Counter
from fractions import Fraction as F
src = open("indep_e8.py").read().split("# --- independent admissible-Y search")[0]
g = {}; exec(compile(src, "indep_core", "exec"), g)
WS, ROOTS, ODD, HQ, dot, add, neg = g["WS"], g["ROOTS"], g["ODD"], g["HQ"], g["dot"], g["add"], g["neg"]
sg = (-1, 1, 1, -1, -1, 1)
HQp = tuple(sum(s * w[k] for s, w in zip(sg, WS)) for k in range(8))
roots_Mp = [add(WS[2*r], WS[2*r+1], -1) if sg[2*r] > 0 else add(WS[2*r+1], WS[2*r], -1) for r in range(3)]
roots_Mp += [neg(b) for b in roots_Mp]
ALPHA = tuple(F(x) for x in (0, 0, 0, 1, 0, 1, 0, 0))
out = {"roots_of_Mprime_are_E8_roots": all(b in ROOTS for b in roots_Mp),
       "Mprime_roots_p_even": all(dot(b, HQ) % 2 == 0 for b in roots_Mp),
       "same_puncture_parity": all((dot(r, HQp) - dot(r, HQ)) % 2 == 0 for r in ROOTS),
       "A1b'_p_odd_roots_in_Mprime_roots": sum(1 for r in ODD if r in roots_Mp),
       "A1c'_alpha.hQ'_distribution": dict(Counter(str(dot(r, HQp)) for r in ODD)),
       "lane_alpha_hQ_W70": str(dot(ALPHA, HQ)), "lane_alpha_hQ_literal": str(dot(ALPHA, HQp)),
       "pair_sums_(+-beta_r)_are_roots_of_Mprime": all(s in roots_Mp for s in [add(g["WS"][2*r], g["WS"][2*r+1], -1) for r in range(3)] + [neg(add(g["WS"][2*r], g["WS"][2*r+1], -1)) for r in range(3)])}
print(json.dumps(out, indent=1))
