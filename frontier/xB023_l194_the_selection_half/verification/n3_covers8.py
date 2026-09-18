import warnings, sys
warnings.filterwarnings("ignore")
import snappy
for nm, sl in [("m004", (1, 1)), ("o10_143849", (1, 0)), ("o10_143849", (0, 1))]:
    M = snappy.Manifold(nm); M.dehn_fill(sl)
    for d in (8, 9, 10):
        try:
            cs = M.covers(d)
        except Exception as e:
            print(f"{nm} {sl} deg {d}: err {type(e).__name__}", flush=True); continue
        print(f"{nm} {sl} deg {d}: {len(cs)} covers"
              + (f"  first H1 {cs[0].homology()}" if cs else ""), flush=True)
        if cs:
            break
