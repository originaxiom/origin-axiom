#!/usr/bin/env python3
"""B1607 -- POST-SEAL CHECK (disclosed): the sealed C1a predicted sigma = P o R exactly and the run returned False for both
P o R and R o P.  Which exact composition the rule is: sigma = L o P (the swap, then L), and P o R is the MIRROR rule
a -> ba, b -> a.  Both have the H_1 matrix [[1, 1], [1, 0]] (GENESIS's golden LP).  Pure word arithmetic; writes
post_seal_lp.json."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def inv(w): return "".join(c.swapcase() for c in reversed(w))
def red(w):
    o = []
    for c in w:
        if o and o[-1] == c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def apply(auto, w): return red("".join(auto[c] if c.islower() else inv(auto[c.lower()]) for c in w))
def compose(f, g): return {x: apply(f, g[x]) for x in "ab"}
sigma = {"a": "ab", "b": "a"}; mirror = {"a": "ba", "b": "a"}
L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; P = {"a": "b", "b": "a"}
table = {f"{f}∘{g}": compose(eval(f), eval(g)) for f in "LRP" for g in "LRP" if f != g}
out = {"sigma_equals_L_after_P": compose(L, P) == sigma, "mirror_equals_P_after_R": compose(P, R) == mirror,
       "sigma_equals_P_after_R": compose(P, R) == sigma, "which_compositions_equal_sigma": [k for k, v in table.items() if v == sigma],
       "which_compositions_equal_mirror": [k for k, v in table.items() if v == mirror], "table": table}
json.dump(out, open(HERE / "post_seal_lp.json", "w"), indent=1, ensure_ascii=False); print(json.dumps(out, indent=1, ensure_ascii=False))
