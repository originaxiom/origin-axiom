#!/usr/bin/env python3
"""B460 cell 1 — the child's geodesic length spectrum (table cell; verdict pre-forced).
Controls: 4_1(7,1), the Weeks manifold, one generic closed census manifold."""
import snappy

def spec(name, cutoff=1.5):
    M = snappy.ManifoldHP(name)
    try:
        L = M.length_spectrum(cutoff, full_rigor=True)
    except Exception:
        L = M.length_spectrum(cutoff)
    print(f"== {name}: vol={float(M.volume()):.9f}  H1={M.homology()}")
    for g in L:
        cl = complex(g.length)
        print(f"   len={cl.real:.10f}  torsion={cl.imag:+.10f}  mult={g.multiplicity}  topology={g.topology}")
    return L

for nm in ["4_1(5,1)", "4_1(7,1)", "m003(-3,1)", "m007(3,1)"]:
    try:
        spec(nm)
    except Exception as e:
        print(f"== {nm}: FAILED {type(e).__name__}: {e}")
    print()
