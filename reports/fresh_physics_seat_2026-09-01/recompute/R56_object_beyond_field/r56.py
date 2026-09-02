#!/usr/bin/env python3
"""R56 -- THE OBJECT BEYOND ITS FIELD: everything measurable that varies across the 14 manifolds sharing
Q(sqrt-3), with m004 vs its sister m003 as the sharpest pair, and the triangulation data that define the
object-level 3d theory (the fork the program set aside).  Every number computed here (SnapPy 3.3.2, sympy)."""
import json, os, sys, itertools
import snappy, sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = {}
def say(*a): print(*a); sys.stdout.flush()
FAM = ["m003","m004","m202","m203","m206","m207","m208","m410","m412","s118","s119","s594","s595","s596"]

say("=" * 96); say("A. THE 14 FIELD-MATES: object-level invariants (all share Q(sqrt-3), E6, the Bianchi group)"); say("=" * 96)
rows = {}
for n in FAM:
    M = snappy.Manifold(n)
    G = M.symmetry_group()
    sh = M.cusp_info('shape')[0]
    ls = M.length_spectrum(1.6)
    cov = [len(M.covers(d)) for d in (2, 3, 4, 5, 6)]
    r = dict(H1=str(M.homology()), vol=round(float(M.volume()), 9), cusp_shape=(round(float(sh.real), 9), round(float(sh.imag), 9)),
             cusp_area=round(float(M.cusp_areas()[0]), 9), sym=G.order(), amph=bool(G.is_amphicheiral()),
             systole=(round(float(ls[0].length.real), 9) if ls else None), n_short=len(ls),
             short_lengths=sorted({round(float(x.length.real), 6) for x in ls}), covers_2_6=cov, CS=round(float(M.chern_simons()), 9))
    rows[n] = r
    say(f"  {n:5s} H1={r['H1']:10s} vol={r['vol']:.6f} tau={r['cusp_shape']} area={r['cusp_area']:.4f} |Sym|={r['sym']} amph={r['amph']} "
        f"systole={r['systole']} #len<1.6={r['n_short']} covers(2..6)={r['covers_2_6']} CS={r['CS']}")
OUT['A_family'] = rows
def distinct(key): return len({str(rows[n][key]) for n in FAM})
say("\n  number of distinct values across the 14:")
for k in ('H1', 'vol', 'cusp_shape', 'cusp_area', 'sym', 'amph', 'systole', 'covers_2_6', 'CS', 'short_lengths'):
    say(f"    {k:14s}: {distinct(k)}")
uniq = [k for k in ('H1', 'cusp_shape', 'cusp_area', 'covers_2_6', 'short_lengths', 'systole') if sum(1 for n in FAM if str(rows[n][k]) == str(rows['m004'][k])) == 1]
say(f"  invariants that single out m004 within the family: {uniq}")
OUT['A_m004_separators'] = uniq

say(); say("=" * 96); say("B. m004 vs m003: fillings (the closings differ object by object)"); say("=" * 96)
fills = {}
for n in ('m004', 'm003'):
    fills[n] = {}
    for q in range(1, 7):
        for p in (1,):
            M = snappy.Manifold(n); M.chern_simons(); M.dehn_fill((p, q))
            st = M.solution_type()
            try:
                v = float(M.volume()); h = str(M.homology())
                cs = float(M.chern_simons()) if 'positively' in st else None
                if 'positively' not in st: h = h + ' [' + st + ']'
            except Exception as e:
                v, cs, h = None, None, type(e).__name__ + ':' + str(e)[:40]
            fills[n][f"({p},{q})"] = (v, cs, h)
    say(f"  {n}: " + "; ".join((f"{s}: vol={v:.5f} CS={cs:+.5f} H1={h}" if cs is not None else f"{s}: vol={v} H1={h}") for s, (v, cs, h) in fills[n].items()))
OUT['B_fillings'] = fills

say(); say("=" * 96); say("C. THE TRIANGULATION DATA (Neumann-Zagier / DGG input) for m004 and m003"); say("=" * 96)
z1, z2, m, l = sp.symbols('z1 z2 m l')
apolys = {}
for n in ('m004', 'm003'):
    M = snappy.Manifold(n)
    say(f"  {n}: tetrahedra {M.num_tetrahedra()}, shapes {[complex(z) for z in M.tetrahedra_shapes('rect')]}")
    say("   gluing matrix (rows: edges then meridian, longitude; columns z1 z1' z1'' z2 z2' z2'' ):"); say("   " + str(M.gluing_equations()).replace("\n", "\n   "))
    rect = M.gluing_equations('rect')
    say(f"   rect form (a, b, c): prod z^a (1-z)^b = c : {rect}")
    # A-polynomial by elimination: edge equation(s) with RHS c; meridian row = m, longitude row = l (SnapPy convention:
    # the cusp rows evaluate to the holonomy eigenvalues; we take them as m and l and check against 4_1's known curve).
    ne = M.num_tetrahedra()
    edges = rect[:-2]; mer, lon = rect[-2], rect[-1]
    zs = [z1, z2]
    def expr(a, b, c): return sp.Mul(*[zs[i] ** a[i] * (1 - zs[i]) ** b[i] for i in range(ne)]) - c
    def cusp(a, b, c, var): return sp.Mul(*[zs[i] ** a[i] * (1 - zs[i]) ** b[i] for i in range(ne)]) - c * var
    # clear denominators: numerators of the rational functions
    E = [sp.numer(sp.together(expr(*e))) for e in edges]
    Mq = sp.numer(sp.together(cusp(*mer, m))); Lq = sp.numer(sp.together(cusp(*lon, l)))
    # Groebner elimination (lex, z1 > z2 > m > l): the generators free of z1, z2 cut out the (m,l) curve
    G = sp.groebner(E + [Mq, Lq], z1, z2, m, l, order='lex')
    free = [g for g in G.exprs if not (g.has(z1) or g.has(z2))]
    A = sp.factor(sp.gcd_list(free)) if free else None
    apolys[n] = str(A)
    say(f"   eliminant in (m, l) from the Groebner basis: {A}")
    # numerical convention check on a hyperbolic filling: compare the cusp-row products with SnapPy's holonomies
    N = snappy.Manifold(n); N.dehn_fill((1, 5))
    zz = [complex(z) for z in N.tetrahedra_shapes('rect')]
    val = lambda a, b: complex(sp.Mul(*[zs[i] ** a[i] * (1 - zs[i]) ** b[i] for i in range(ne)]).subs({z1: zz[0], z2: zz[1]}))
    hol = N.cusp_info()[0]['holonomies']
    import cmath
    em, el = cmath.exp(complex(hol[0])), cmath.exp(complex(hol[1]))
    pm, pl = val(mer[0], mer[1]), val(lon[0], lon[1])
    say(f"   convention check at filling (1,5): meridian product {pm:.6f} vs exp(H_m) {em:.6f} vs exp(2H_m) {em**2:.6f}")
    say(f"                                     longitude product {pl:.6f} vs exp(H_l) {el:.6f} vs exp(2H_l) {el**2:.6f}")
    if A is not None:
        say(f"   A(m=product_m, l=product_l) at the filling = {complex(A.subs({m: pm, l: pl})):.3e}  (should be ~0)")
OUT['C_apolys'] = apolys

say(); say("=" * 96); say("D. THE DGG THEORY AT THE FORK"); say("=" * 96)
say("""  DGG (Dimofte-Gaiotto-Gukov 2011): an ideal triangulation with N tetrahedra and one cusp defines a 3d N=2 theory
  T[M]: N chiral multiplets (one per tetrahedron, 'T_Delta' = a free chiral with U(1)_{-1/2} level), glued by the
  symplectic (Neumann-Zagier) data above: U(1)^{N-1} gauge symmetry, Chern-Simons levels and a superpotential from the
  internal edges, one flavour U(1) from the cusp.  For m004 and m003, N = 2: gauge U(1), two chirals, ONE internal edge.
  The theories are defined by the two gluing matrices printed in C, which differ; their moduli spaces on S^1 x R^2 are
  the two A-polynomial curves printed in C, which differ.  THIS is the first invariant after the shape field that is
  the object's and not the field's.  It is a 3d supersymmetric theory, not the Standard Model.""")
json.dump(OUT, open(os.path.join(HERE, 'r56_results.json'), 'w'), indent=1, default=str)
say("r56_results.json written")
