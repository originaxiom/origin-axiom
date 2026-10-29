"""Referee R6: the horocycle-by-hand read-out (A1, (S~, S, S), c = 3, L_max: data p_nn 0.123 where only 1.5% of random
hierarchies are typical at that fixed configuration) graded by a class-choosing null as free as the choices behind it:
8 readings x c in {1, 3} x horocycle in {drawn, L_max, L_2} (48 configurations), best p_nn per random hierarchy (seeds
1741-1745, the first 1 000 each).  Also the 32-configuration menu without "drawn"."""
import json, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import r3_independent as R
t6, s6, _, _ = R.target(); arms = R.load_census(); cf = R.cfg_seq()
menu = {}
for a in (0, 1):
    for b in (0, 1):
        for l in (0, 1):
            for c in (1, 3):
                for h in (None, 0, 1):
                    menu[(a, b, l, c, h)] = R.Typ(R.model(arms["A1"], cf, fixed=(a, b, l), c=c, horo=h), s6)
out = {"data p_nn at (S~,S,S), c=3, L_max": float(menu[(1, 0, 0, 3, 0)].pnn(t6)[0][0]),
       "data best over the 48": float(max(ty.pnn(t6)[0][0] for ty in menu.values()))}
r48, r32, r16 = [], [], []
for s in range(1741, 1746):
    Rh = R.rand_hier(s)[:1000]; P = {k: ty.pnn(Rh)[0] for k, ty in menu.items()}
    r48.append(float(np.mean(np.max(list(P.values()), axis=0) > out["data p_nn at (S~,S,S), c=3, L_max"])))
    r32.append(float(np.mean(np.max([v for k, v in P.items() if k[4] is not None], axis=0) > out["data p_nn at (S~,S,S), c=3, L_max"])))
    r16.append(float(np.mean(np.max([v for k, v in P.items() if k[4] is None], axis=0) > 0.05)))
out["share of random hierarchies whose best p_nn over the 48 exceeds the data's L_max value"] = float(np.mean(r48))
out["the same over the 32 fixed-horocycle configurations"] = float(np.mean(r32))
out["check: the sealed free null (16, drawn) at 0.05"] = float(np.mean(r16))
(HERE / "r6_out.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
