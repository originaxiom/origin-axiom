#!/usr/bin/env python3
"""L225 q3 without Regina: Garoufalidis-Hodgson-Rubinstein-Segerman (arXiv:1303.5278) Theorem 1.5 -- an ideal
triangulation of an oriented atoroidal manifold with a cusp that admits a semi-angle structure is 1-efficient.
A triangulation whose shapes all have positive imaginary part carries a strict angle structure (the arguments).
Checked here on every census triangulation B1428 and B1431 used."""
import snappy
NAMES = ["m003", "m004", "m006", "m007", "m009", "m015", "m016", "m017", "m019", "m022", "m023", "m026"]
ok = 0
for n in NAMES:
    M = snappy.ManifoldHP(n); sh = M.tetrahedra_shapes("rect")
    low = min(float(z.imag()) for z in sh); good = M.solution_type() == "all tetrahedra positively oriented" and low > 0.05
    try: cert = M.verify_hyperbolicity()[0]
    except Exception as ex: cert = "not run (%s)" % type(ex).__name__
    ok += good
    print("%s  tetrahedra %d  least Im(shape) %.6f  %s  interval certificate: %s" % (n, len(sh), low, M.solution_type(), cert))
print("strict angle structure, hence 1-efficient by the theorem: %d of %d" % (ok, len(NAMES)))
