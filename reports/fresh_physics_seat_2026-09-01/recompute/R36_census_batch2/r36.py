#!/usr/bin/env python3
"""R36 — second batch of cheap recomputes (SnapPy/PARI/sympy, no Sage) for reader-flagged rows:
B331 (chi_27 at the order-3 element of the principal SL2 = 0), B333 (h(-15)=2; 14 of 123 fundamental discriminants
down to -400 have h=2), B335 (3-fold cover: vol ratio 3, isometry group order 24 with abelianization (Z/2)^2, not
SL(2,3)), B406 (a_p(15a1) == a_p(40a1) mod 4 at every good prime < 200), B486 (cusp modulus 2sqrt3 i: rectangular,
disc -48), B488/B489 (n-fold cyclic covers of 4_1, n=1..8: H1 = (Z/?)..., torsion = |2 - L(2n)|, vol = n vol(4_1)),
B509/B510 (Y^2 = X^3 - 2X + 1: conductor 40, j = 55296/5, torsion Z/4, 2-isogenous to 40a1; Jacobian of
d^2 = (c^2-1)(c^2-5) is the same curve), B520 (arccosh(5/2))."""
import json, os, math
import snappy
from snappy import pari
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
out, lines = {}, []
def say(s): print(s, flush=True); lines.append(s)
pari.set_real_precision(30)

say('== B331: chi_27(g) for g of order 3 in the principal SL(2) ==')
# 27|principal SL2 = V16 + V8 + V0 (dims 17+9+1); chi_{V_n}(diag(w,w^-1)) = sum_{k=0..n} w^(n-2k), w = e^{2 pi i/3}
w = complex(math.cos(2*math.pi/3), math.sin(2*math.pi/3))
chi = {n: sum(w ** (n - 2*k) for k in range(n + 1)) for n in (16, 8, 0)}
tot = sum(chi.values())
say('  principal decomposition 27 = V16+V8+V0 (E6 exponents 1,4,5,7,8,11 -> the 27 sees 16,8,0): chi = %s, total %.12f%+.12fi (bank 0)' % ({n: round(c.real) for n, c in chi.items()}, tot.real, tot.imag))
out['B331'] = dict(chi=tot.real)

say('== B333: class numbers ==')
h15 = int(pari.qfbclassno(-15)); fund = [D for D in range(-3, -401, -1) if pari.isfundamental(D)]
h2 = [D for D in fund if int(pari.qfbclassno(D)) == 2]
say('  h(-15) = %d (bank 2); fundamental discriminants in [-400,-3]: %d (bank 123); with h = 2: %d (bank 14): %s' % (h15, len(fund), len(h2), h2))
out['B333'] = dict(h15=h15, n_fund=len(fund), n_h2=len(h2), h2=h2)

say('== B335 / B488 / B489: cyclic covers of the figure-eight ==')
M = snappy.Manifold('m004'); v = M.volume()
L = lambda n: round(((1+5**.5)/2)**n + ((1-5**.5)/2)**n)
rows = []
for n in range(1, 9):
    C = M.covers(n, cover_type='cyclic')[0] if n > 1 else M
    H = C.homology(); tors = 1
    for c in H.coefficients if hasattr(H, 'coefficients') else []: 
        if c: tors *= c
    st = str(H)
    rows.append((n, st, float(C.volume() / v), abs(2 - L(2*n))))
    say('  n=%d  H1 %-22s vol/vol(4_1) = %.10f  |2-L(2n)| = %d' % (n, st, C.volume() / v, abs(2 - L(2*n))))
out['B489'] = rows
C3 = M.covers(3, cover_type='cyclic')[0]
S = C3.symmetry_group()
say('  3-fold cover: isometry group order %d, abelianization %s (bank: order 24, NOT SL(2,3): abelianization (Z/2)^2 vs Z/3)' % (S.order(), S.abelianization()))
try:
    ls = C3.length_spectrum(1.5)
    say('  shortest geodesics: %s' % [(str(g.length)[:12], g.multiplicity) for g in ls[:3]])
except Exception as e: say('  length spectrum: %r' % e)
say('  cusp shape of cover %s' % C3.cusp_info('shape'))
out['B335'] = dict(order=int(S.order()), abelianization=str(S.abelianization()))

say('== B406: a_p(15a1) == a_p(40a1) mod 4 at good primes < 200 ==')
E15 = pari.ellinit([1, 1, 1, -10, -10]); E40 = pari.ellinit([0, 0, 0, -7, -6])
viol = [int(p) for p in pari.primes(200) if int(p) not in (2, 3, 5) and (int(pari.ellap(E15, p)) - int(pari.ellap(E40, p))) % 4]
say('  violations: %s (bank: zero); torsion 15a1 %s, 40a1 %s' % (viol, pari.elltors(E15)[1], pari.elltors(E40)[1]))
out['B406'] = dict(violations=viol)

say('== B486: cusp modulus ==')
z = complex(M.cusp_info('shape')[0]); a, b = 1.0, z
say('  shape %s: rectangular (Re = %.1e), lattice Z + 2sqrt3 i Z, disc of the order Z[2sqrt3 i] = -48 (2sqrt3 i)^2 = -12 -> disc -48; translations (1, %.6f) orthogonal' % (z, z.real, abs(z)))
out['B486'] = dict(shape=str(z))

say('== B509 / B510: the square-time curve ==')
E = pari.ellinit([0, 0, 0, -2, 1])
gr = pari.ellglobalred(E)
say('  Y^2 = X^3 - 2X + 1: disc %s, conductor %s, j = %s, torsion %s' % (E.disc(), gr[0], E.j(), pari.elltors(E)[1]))
cls = [(str(pari.ellinit(ent[0]).j()), [int(x) for x in ent[0]]) for ent in pari.ellisomat(E40)[0]]
say('  40a class j-invariants: %s ; j(E) in class: %s ; isomorphic to 40a1: %s' % ([c[0] for c in cls], str(E.j()) in [c[0] for c in cls], E.j() == E40.j()))
iso = pari.ellisomat(E40)
Ej = pari.ellfromeqn(pari('d^2 - (c^2-1)*(c^2-5)')); Ej = pari.ellinit(Ej)
say('  Jacobian of d^2 = (c^2-1)(c^2-5): conductor %s, j = %s  (= j of Y^2=X^3-2X+1: %s)' % (pari.ellglobalred(Ej)[0], Ej.j(), Ej.j() == E.j()))
say('  y^2 = x(x-1)(x-5): j = %s (bank 40a1, 148176/25)' % pari.ellinit([0, -6, 0, 5, 0]).j())
out['B509_B510'] = dict(j=str(E.j()), conductor=int(gr[0]), jac_j=str(Ej.j()), x_x1_x5_j=str(pari.ellinit([0, -6, 0, 5, 0]).j()))

say('== B520: arccosh(5/2) ==')
say('  arccosh(5/2) = %.10f (bank ~1.5668); = log((5+sqrt21)/2) = %.10f' % (math.acosh(2.5), math.log((5 + 21 ** .5) / 2)))
json.dump(out, open(HERE + '/r36_out.json', 'w'), indent=1, default=str)
open(HERE + '/r36_out.txt', 'w').write('\n'.join(lines) + '\n')
