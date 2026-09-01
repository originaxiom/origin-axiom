"""R33 shared: invariant trace field of a cusped hyperbolic manifold = its tetrahedral shape field
(Neumann-Reid 1992, Thm 2.4, for cusped manifolds), computed WITHOUT Sage: polished shapes at
`bits` bits (snappy.snap), a primitive element w = sum c_i z_i with small distinct integer c_i,
PARI algdep -> factor -> the irreducible factor vanishing at w to 1e-(digits/2); degree cross-checked
with a second coefficient vector. Field named by polredabs (x^2-x+1 = Q(sqrt-3), x^2+1 = Q(i), x^2-x+2 = Q(sqrt-7))."""
import snappy
from snappy import pari
from snappy.snap import polished_tetrahedra_shapes

C1 = (1, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127)
C2 = (2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230, 252, 275, 299, 324, 350, 377, 405, 434, 464, 495)

def minpoly_of(w, maxdeg, tol, digits):
    """incremental algdep: the FIRST degree d at which a relation holds to tol; then the irreducible factor
    vanishing at w (algdep can return a reducible multiple, e.g. x^3+1 for a primitive 6th root of unity)."""
    for d in range(1, maxdeg + 1):
        try: p = pari.algdep(w, d)
        except Exception: continue      # PARI refuses degree 1 for non-real input
        if abs(pari.subst(p, 'x', w)) > tol: continue
        # spurious-relation guard: a genuine relation is cheap; algdep can always fit a degree-d relation with
        # coefficients of ~digits/(d+1) digits, so demand (d+1)*log10(H) < digits/2
        H = max(abs(int(c)) for c in pari.Vec(p))
        if (d + 1) * len(str(H)) > digits * 0.5: continue
        best = None
        for f, _ in zip(*pari.factor(p)):
            if pari.poldegree(f) < 1: continue
            if abs(pari.subst(f, 'x', w)) < tol and (best is None or pari.poldegree(f) < pari.poldegree(best)): best = f
        if best is not None: return best
    return None

def shape_field(M, bits=1000, maxdeg=16):
    digits = int(bits * 0.3)
    pari.set_real_precision(digits)
    zs = [z.gen for z in polished_tetrahedra_shapes(M, bits_prec=bits)]
    tol = pari(10) ** (-int(digits * 0.5))
    res = []
    for C in (C1, C2):
        w = sum(c * z for c, z in zip(C, zs))
        res.append(minpoly_of(w, maxdeg, tol, digits))
    if res[0] is None or res[1] is None: return None
    d0, d1 = int(pari.poldegree(res[0])), int(pari.poldegree(res[1]))
    f = res[0] if d0 >= d1 else res[1]
    deg = int(pari.poldegree(f))
    fr = pari.polredbest(f) if deg <= 12 else f
    sig = None; disc = 'skipped'
    if deg <= 8:
        disc = str(pari.nfdisc(fr)); sig = [int(x) for x in pari.nfinit(fr)[1]]
    return dict(degree=deg, poly=str(fr), disc=disc, signature=sig, degrees_two_choices=[d0, d1])

def field_name(poly):
    return {'x^2 - x + 1': 'Q(sqrt-3)', 'x^2 + 1': 'Q(i)', 'x^2 - x + 2': 'Q(sqrt-7)', 'x^2 + 2': 'Q(sqrt-2)', 'x^2 - x + 3': 'Q(sqrt-11)'}.get(poly, poly)
