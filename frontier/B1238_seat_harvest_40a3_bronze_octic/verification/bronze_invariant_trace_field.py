"""Bronze (m=3): the INVARIANT trace field, computed -- the question B1237 left open after E55.
Metallic monodromy phi_m = [[m,1],[1,0]] (det -1); the orientable bundle is phi_m^2 = R^m L^m
(m=1: RL = m004, m=2: RRLL = m136, m=3: RRRLLL = census s464). Cusped => arithmetic iff the invariant
trace field is imaginary quadratic with integral invariant traces (Maclachlan-Reid, non-cocompact case).
Two independent routes, both at 1000 bits (~300 digits):
  (i)  invariant traces tr(g^2) from SnapPy's polished holonomy (lift-sign independent);
  (ii) the tetrahedra shape field (= invariant trace field for cusped M, Neumann-Reid 1992 Thm 2.4).
Minimal polynomials by PARI algdep (LLL); a relation is ACCEPTED only if irreducible, max|coeff| < 1e12
and |p(t)| < 1e-200 -- the earlier run showed that residual alone is no test (50-digit-coefficient
degree-5 'relations' at 170 digits are LLL noise). Field degree = max minpoly degree over generic
integer combinations of the generators (a primitive element of the compositum)."""
import snappy
from snappy.pari import pari
pari.set_real_precision(300)
CB, RES = pari(10)**12, pari(10)**(-200)
def minpoly(t, dmax=16):
    for d in range(2, dmax+1):
        p = t.algdep(d)
        if p.polisirreducible() and max(abs(c) for c in p.Vec()) < CB and abs(p.subst('x', t)) < RES:
            return p
    return None
def field_of(vals, label):
    combos = [(1,2,3,0,0,0),(1,-2,3,5,-7,0),(2,3,-5,7,11,-13),(3,1,4,1,5,9),(1,1,1,1,1,1)]
    best = (0, None)
    for coef in combos:
        t = sum(c*v for c, v in zip(coef, vals[:6])); p = minpoly(t); d = p.poldegree() if p is not None else None
        print(f"   {label} combo {coef}: minpoly degree {d}")
        if p is not None and d > best[0]: best = (d, p)
    d, p = best
    if p is None:
        print(f"   -> {label}: no accepted relation up to degree 16: degree > 16"); return None
    red = pari(f"polredabs({p})"); sig = pari(f"nfinit({red})").nf_get_sign(); disc = pari(f"nfdisc({red})")
    print(f"   -> {label} FIELD: degree {d}, polredabs {red}, signature (r1,r2)={sig}, disc {disc}")
    return red
def cx(z): return pari(str(z.real()).replace(' ','') + "+(" + str(z.imag()).replace(' ','') + ")*I")
def run(name):
    M = snappy.Manifold(name)
    print(f"\n== {name}: vol = {M.volume(bits_prec=200)}  H1 = {M.homology()}  identify = {[m.name() for m in M.identify()]}")
    G = M.fundamental_group(); rho = M.polished_holonomy(bits_prec=1000, lift_to_SL2=False)
    mats = {g: rho(g) for g in G.generators()}; mats.update({g.upper(): rho(g.upper()) for g in G.generators()})
    def tr2(w):
        A = mats[w[0]]
        for c in w[1:]: A = A*mats[c]
        A2 = A*A; return cx(A2[0,0] + A2[1,1])
    gens = list(G.generators())
    words = [gens[0], gens[1], gens[0]+gens[1], gens[0]+gens[1].upper(), gens[0]*2+gens[1], gens[0]+gens[1]*2]
    vals = [tr2(w) for w in words]
    for w, v in zip(words, vals):
        p = minpoly(v); print(f"   tr({w}^2) = {v.precision(20)}  minpoly {p}  monic={p.pollead()==1 if p is not None else None}")
    K1 = field_of(vals, "invariant-trace")
    shapes = [cx(s) for s in M.tetrahedra_shapes('rect', bits_prec=1000)]
    while len(shapes) < 6: shapes = shapes + shapes
    for i, s in enumerate(shapes[:M.num_tetrahedra()]): print(f"   shape z_{i} = {s.precision(20)}  minpoly {minpoly(s)}")
    K2 = field_of(shapes, "shape")
    same = (K1 is not None and K2 is not None and pari(f"nfisisom({K1},{K2})") != 0)
    print(f"   routes agree (nfisisom): {same}")
    K = K1 if K1 is not None else K2
    if K is not None:
        d = K.poldegree(); sig = pari(f"nfinit({K})").nf_get_sign()
        print(f"   ==> {name}: invariant trace field degree {d}, {'IMAGINARY QUADRATIC -> ARITHMETIC-side' if d==2 and sig[0]==0 else 'NOT imaginary quadratic -> NON-ARITHMETIC (cusped)'}")
for name in ("b++RL", "b++RRLL", "b++RRRLLL"): run(name)
print("DONE")
