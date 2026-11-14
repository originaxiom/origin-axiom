#!/usr/bin/env python3
"""SM-C10, post hoc, labelled: written after this seat's run and the web seat's W-C8 part 2a were both committed, to
reconcile the two censuses at five ticks (m407).  The web seat's doublets include alpha = beta (l trivial, the unipotent
doublets from H^1(G; C)); this seat's sealed population took alpha != beta.  Here: the alpha = beta doublets at n = 5
on this seat's code (characters of order dividing 11 or 22), and their twisted h1 gap h1(V* (x) w) - h1(V).
    python3 posthoc_c10_unipotent.py [out.json]"""
import sys, json, itertools, pathlib
from fractions import Fraction as Fr
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_c10 as C


def main():
    G = C.Group(5); w = {1: 1.0, 2: 1.0, 3: -1.0}; chars = set()
    for N in (11, 22):
        for th in itertools.product(range(N), repeat=3):
            if all(sum(int(G.E[i, k]) * th[k] for k in range(3)) % N == 0 for i in range(len(G.rels))):
                chars.add(tuple(Fr(a, N) for a in th))
    cnt = Counter(); n = 0
    for a in sorted(chars):
        V = C.module(G, a, a)
        if V is None: continue
        n += 1; cnt[C.coh(G, C.twist(C.dual(V), w))["h1"] - C.coh(G, V)["h1"]] += 1
    out = {"n": 5, "characters": len(chars), "unipotent_doublets": n, "g_w_census": {str(k): v for k, v in sorted(cnt.items())}}
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else HERE / "c10_posthoc_unipotent.json", "w"), indent=1)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
