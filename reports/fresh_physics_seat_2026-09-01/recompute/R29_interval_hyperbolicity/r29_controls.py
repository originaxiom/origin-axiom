#!/usr/bin/env python3
"""R29 negative controls: the certificate must REFUSE non-hyperbolic manifolds and perturbed shapes.
Torus-knot complements (3_1, 5_1, 7_1) have a flat solution of the gluing equations (a genuine zero of the
log form) — the Krawczyk step passes, the Im z > 0 gate must fail.  A 1e-30 perturbation of m004's shapes
must fail the numeric-residual gate before any interval work."""
import snappy, mpmath as mp
import r29_krawczyk as r

for name in ['3_1', '5_1', '7_1', 'L6a1', 'K12n242', '9_42', 'm004']:
    M = snappy.Manifold(name)
    res = r.verify(name)
    print('%-8s %-36s -> verified=%-5s K=%s Im>0=%s' % (name, M.solution_type(), res.get('verified'),
          res.get('krawczyk_contractive'), res.get('im_positive')))

M = snappy.Manifold('m004')
z = [mp.mpc(str(s.real()), str(s.imag())) for s in M.high_precision().tetrahedra_shapes('rect')]
z[0] += mp.mpf('1e-30')
rows = r.logform_rows(M)
print('perturbed m004 shapes: row-0 residual = %s (gate is 1e-50)' % mp.nstr(abs(r.F_num(rows[0], z, 0)), 5))
