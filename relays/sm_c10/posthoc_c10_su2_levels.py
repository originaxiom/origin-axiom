#!/usr/bin/env python3
"""SM-C10, a second post hoc check (2026-11-14), after agy-exp's correction relayed by main (M33): h^1 of the SU(2)
family (post hoc 2: x -> i, y -> j, g in SU(2) carrying the act) level by level, under the page's assignment t -> c g^n
and under t -> (c g)^n, for c a root of unity of order up to 12.  Uses this page's own code (run_c10, posthoc_c10).
    python3 posthoc_c10_su2_levels.py"""
import json
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_c10 as C
import posthoc_c10 as P

base, g = P.common_point_g()
out = {}
for assign in ("t -> c g^n", "t -> (c g)^n"):
    out[assign] = {}
    for n in range(1, 7):
        G = C.Group(n)
        gn = np.linalg.matrix_power(g, n)
        hits, mods = [], 0
        for N in range(1, 13):
            for e in range(N):
                if math.gcd(e, N) != 1 and not (N == 1 and e == 0):
                    continue
                c = np.exp(2j * math.pi * e / N)
                tv = c * gn if assign == "t -> c g^n" else np.linalg.matrix_power(c * g, n)
                V = {1: base[1], 2: base[2], 3: tv}
                if not all(np.allclose(C.mat_of(V, r), np.eye(2), atol=1e-9) for r in G.rels):
                    continue
                mods += 1
                h = C.coh(G, V)["h1"]
                if h:
                    hits.append([f"c = exp(2 pi i {e}/{N})", h])
        out[assign][n] = {"modules": mods, "h1 non-zero": hits}
        print(assign, n, mods, hits)
(HERE / "c10_posthoc_su2_levels.json").write_text(json.dumps(out, indent=1))
