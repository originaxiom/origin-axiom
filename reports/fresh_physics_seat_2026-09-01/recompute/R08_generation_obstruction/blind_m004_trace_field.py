#!/usr/bin/env python3
"""R08 BLIND computation, part (i): the (invariant) trace field of m004 (figure-eight knot
complement), independently of the arc's verification scripts.

Three independent routes:
  A. Shape field: high-precision tetrahedron shapes -> algdep -> exact min poly, disc.
     (Neumann-Reid: for a cusped hyperbolic manifold the shape field EQUALS the invariant
      trace field, so this is a computation of the invariant trace field.)
  B. Trace field directly: numerical SL(2,C) holonomy from snappy's fundamental_group,
     min polys of tr(a), tr(b), tr(ab) and of the invariant generators tr^2.
  C. Sanity: disc, signature, Galois group of the found polynomial (exact, via PARI).

No arc verification/ script or tests/ file has been opened before running this.
"""
import snappy
from snappy import pari
import json, sys

pari.set_real_precision(120)
DIG = 100

def to_pari_c(z):
    return pari(str(z.real())) + pari(str(z.imag()))*pari('I')

def algdep_checked(w, maxdeg, tol_exp=-60):
    """Find min poly of complex w by pari.algdep, verified by residual + irreducibility."""
    if abs(pari.imag(w)) < pari(10)**tol_exp:
        w = pari.real(w)  # treat numerically-real values as real so degree 1 can be found
    for d in range(1, maxdeg+1):
        try:
            p = pari.algdep(w, d)
        except Exception:
            continue  # e.g. complex number cannot satisfy a degree-1 rational poly
        if p.poldegree() < 1:
            continue
        res = abs(pari.subst(p, pari('x'), w))
        scale = max(abs(int(c)) for c in pari.Vec(p))
        if res / scale < pari(10)**tol_exp and p.polisirreducible():
            return p
    return None

out = {}

# ---- Route A: shape field ----
M = snappy.Manifold('m004')
shapes = M.tetrahedra_shapes('rect', bits_prec=400)
out['num_tetrahedra'] = len(shapes)
pshapes = [to_pari_c(z) for z in shapes]
shape_polys = [str(algdep_checked(z, 8)) for z in pshapes]
out['shape_min_polys'] = shape_polys
# primitive element for the whole shape field (two coefficient sets for robustness)
for tag, coeffs in [('c1', [1, 3]), ('c2', [5, -2])]:
    w = sum(c*z for c, z in zip(coeffs, pshapes))
    p = algdep_checked(w, 12)
    out[f'shape_field_minpoly_{tag}'] = str(p)
    out[f'shape_field_degree_{tag}'] = int(p.poldegree())

# canonical field data from the single-shape poly (both shapes identical for m004)
p0 = pari(shape_polys[0])
out['shape_poly_disc'] = str(pari.poldisc(p0))
out['nfdisc'] = str(pari.nfdisc(p0))
out['signature'] = [int(x) for x in pari.nfinit(p0)[1]]  # nf[2] = [r1,r2]

# ---- Route B: traces of the holonomy ----
Mh = snappy.ManifoldHP('m004')
G = Mh.fundamental_group()
out['group_gens'] = G.num_generators()
words = ['a', 'b', 'ab', 'aB', 'abAB']
traces = {}
for wd in words:
    m = G.SL2C(wd)
    tr = m[0, 0] + m[1, 1]
    traces[wd] = str(tr)
    ptr = to_pari_c(tr)
    p = algdep_checked(ptr, 8, tol_exp=-30)   # HP = ~64 digits
    out[f'minpoly_tr({wd})'] = str(p)
    p2 = algdep_checked(ptr*ptr, 8, tol_exp=-30)  # invariant trace field generators tr^2
    out[f'minpoly_tr^2({wd})'] = str(p2)
out['traces_numeric'] = traces

# ---- Route C: exact classification of the found field ----
target = pari('x^2 - x + 1')
out['banked_poly_matches_shape_poly'] = bool(
    pari.nfisisom(p0, target) != pari(0) if p0.poldegree() == target.poldegree() else False)
out['target_poly_disc'] = str(pari.poldisc(target))
out['target_nfdisc'] = str(pari.nfdisc(target))
out['galois_note'] = 'degree 2 => Galois group Z/2 automatically'

print(json.dumps(out, indent=2))
with open(sys.path[0] + '/blind_m004_output.json', 'w') as f:
    json.dump(out, f, indent=2)
