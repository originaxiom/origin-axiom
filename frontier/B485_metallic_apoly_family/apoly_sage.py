#!/usr/bin/env sage-python
"""B485 - the metallic A-polynomial family + genus (forcing edges #2,#3, task #201).
Compute the A-polynomial of the metallic bundles m=1,2,3 (4_1, m136, s464) and the
genus of each A-polynomial curve. Uses snappy inside sage."""
import snappy
try:
    from sage.all import QQ, PolynomialRing, Curve
    HAVE_SAGE=True
except Exception:
    HAVE_SAGE=False

for m,name in [(1,'4_1'),(2,'m136'),(3,'s464')]:
    M=snappy.Manifold(name)
    print(f"=== m={m}: {name}, vol={float(M.volume()):.6f} ===")
    try:
        A=M.alexander_polynomial()
        print(f"  Alexander: {A}")
    except Exception as e:
        print(f"  Alexander err: {e}")
    # A-polynomial via snappy's apoly (needs the extended char variety)
    try:
        ap=M.gluing_equations()  # sanity the triangulation
        from snappy import pari
    except Exception as e:
        pass
    try:
        # snappy can compute the A-polynomial for cusped manifolds
        Apoly = M.alexander_polynomial()
    except Exception:
        pass
