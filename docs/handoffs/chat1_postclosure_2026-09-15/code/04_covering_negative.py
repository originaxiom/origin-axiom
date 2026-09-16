#!/usr/bin/env python3
"""THE CENTRAL NEGATIVE: no covering path from m004 or m003 to any det=3 manifold.
Their degree-2 and degree-3 covers are UNIQUE and 1-CUSPED, so they stay in a lattice
class that can never carry an order-3. m202/s959 have the right volumes and 2 cusps."""
import snappy
if __name__=="__main__":
    for base in ['m004','m003']:
        B=snappy.Manifold(base)
        for d in (2,3):
            cs=B.covers(d)
            print(f"{base} degree-{d}: {len(cs)} cover(s) -> "
                  f"{[(c.num_cusps(), round(float(c.volume()),6)) for c in cs]}")
        for tgt in ['m202','s959']:
            T=snappy.Manifold(tgt); d=round(float(T.volume())/float(B.volume()))
            iso=any(c.is_isometric_to(T) for c in B.covers(d))
            print(f"   {base} -> {tgt} (degree {d}): is a cover? {iso}")
