"""Only a knot complement (H_1 = Z) has a Kashaev invariant. Same volume, different status."""
import snappy
for m in ['m004','m003']:
    M=snappy.Manifold(m); print(m, M.homology(), f"{float(M.volume()):.12f}", "knot" if str(M.homology()).replace(' ','')=='Z' else "not a knot")
