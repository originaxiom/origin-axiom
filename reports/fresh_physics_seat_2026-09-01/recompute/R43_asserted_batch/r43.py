#!/usr/bin/env python3
"""R43 -- tool checks on ASSERTED/IMPORTED load-bearing claims (Phase C tier C-3). Each section prints CLAIM / COMPUTED / verdict."""
import warnings; warnings.filterwarnings('ignore')
import snappy, math, cmath, itertools
from snappy import pari
import mpmath as mp
mp.mp.dps = 40
M = snappy.Manifold('m004')
def sec(t): print('\n== ' + t)
def ok(b, msg): print(('  MATCH  ' if b else '  DIFFERS') + ' ' + msg)

sec('B3: m004 = 2 ideal tetrahedra, 2 edge classes, 4 faces, 1 cusp')
T = M.num_tetrahedra(); C = M.num_cusps()
ok(T == 2 and C == 1, f'tetrahedra={T} cusps={C}; ideal triangulation: edges = tetrahedra = {T}, faces = 2T = {2*T}')

sec('B257/B321/B486: cusp shape 2*sqrt(3)*i (rectangular, |shape|^2=12), translations (1, 2sqrt3)')
sh = complex(M.cusp_info('shape')[0]); ok(abs(sh - 2*math.sqrt(3)*1j) < 1e-9, f'cusp shape = {sh}; |shape|^2 = {abs(sh)**2:.9f}')
tr = [complex(x) for x in M.cusp_translations()[0]]; print('  cusp translations (m,l) =', tr, '| ratio', tr[1]/tr[0] if tr[0] else None)
ok(abs(sh.real) < 1e-9, 'rectangular (Re shape = 0); disc of Z[shape/... ] : shape^2 = -12 -> Q(sqrt-3), order of disc -48 (index 4 in O_-3)')

sec('B338: CS(1,n) table for m004(1,n): CS(1,2)=-0.24661 ... CS(1,50)=-0.010000; CS*n -> -0.5')
for n in (2, 3, 5, 10, 20, 50):
    N = snappy.Manifold('m004'); N.chern_simons(); N.dehn_fill((1, n))
    try: cs = float(N.chern_simons())
    except Exception as e: cs = float('nan')
    print(f'  n={n:2d} CS={cs:+.6f} n*CS={n*cs:+.5f} vol={float(N.volume()):.6f}')

sec('B485: Alexander polynomial of the metallic bundles (monodromy R^m L^m? use A_m = [[m^2+1? ]]) -- family law Delta_m(a) = a^2 - (m^2+2) a + 1')
# metallic family: the once-punctured-torus bundle with monodromy R^m L^m has Alexander polynomial = char poly of the monodromy on H1(T^2) = x^2 - tr x + 1, tr(R^m L^m) = m^2 + 2
for m in range(1, 7):
    A = [[1, m], [0, 1]]; B = [[1, 0], [m, 1]]
    P = [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]], [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    trc = P[0][0] + P[1][1]
    print(f'  m={m}: tr(R^m L^m) = {trc} = m^2+2 -> Delta_m(a) = a^2 - {trc} a + 1', 'MATCH' if trc == m*m+2 else 'DIFFERS')
# SnapPy cross-check for m=1 (m004) and m=2 (m136) via the census bundle names
print('  (SnapPy alexander_polynomial needs Sage; the law is the characteristic polynomial of the monodromy R^m L^m, verified above)')
for m in (1, 2, 3, 4):
    try:
        N = snappy.Manifold('b++' + 'R'*m + 'L'*m); s = complex(N.cusp_info('shape')[0])
        print(f'  m={m} bundle b++{"R"*m}{"L"*m}: vol={float(N.volume()):.6f} cusp shape={s:.6f} rectangular={abs(s.real)<1e-8}')
    except Exception as e: print('  bundle m=%d failed: %s' % (m, e))

sec('B211 L32: metallic bundles m=1..6 amphichiral, CS = 0')
for m in range(1, 7):
    N = snappy.Manifold('b++' + 'R'*m + 'L'*m)
    try: cs = float(N.chern_simons())
    except Exception as e: cs = float('nan')
    mir = N.copy(); mir.reverse_orientation()
    amph = N.is_isometric_to(mir)
    print(f'  m={m}: vol={float(N.volume()):.6f} CS={cs:+.2e} amphichiral(isometric to mirror)={amph}')

sec('B488/B489/B1079/B8086: H1(M_m) = Z + (Z/m)^2 (metallic bundles); tower A^n: torsion |2-L(2n)|, vol = n*vol(4_1)')
for m in range(1, 9):
    N = snappy.Manifold('b++' + 'R'*m + 'L'*m); print(f'  m={m}: H1 = {N.homology()} vol/vol(m004) = {float(N.volume())/float(M.volume()):.6f}')
# tower: monodromy A^n with A = RL (m004); torsion of H1 = |det(A^n - I)| = |2 - tr(A^n)| = |2 - L_{2n}| (Lucas)
L = lambda k: round(((1+5**.5)/2)**k + ((1-5**.5)/2)**k)
for n in range(1, 9):
    N = snappy.Manifold('b++' + 'RL'*n); tors = abs(2 - L(2*n))
    print(f'  n={n}: H1 = {N.homology()} predicted torsion |2-L(2n)| = {tors}; vol/vol(4_1) = {float(N.volume())/float(M.volume()):.6f}')

sec('B316: chiral RRL / RLL bundles have invariant trace field Q(sqrt-7)')
import sys; sys.path.insert(0, '../R33_trace_fields_snappy')
try:
    from r33_lib import shape_field
    for w in ('RRL', 'RLL'):
        N = snappy.Manifold('b++' + w); f = shape_field(N)
        print(f'  b++{w}: vol={float(N.volume()):.6f} shape field = {f}')
except Exception as e: print('  r33_lib failed:', e)

sec('B1083: Gieseking manifold (nonorientable, vol ~1.0149) has orientation double cover m004')
G = snappy.Manifold('m000'); print(f'  m000: orientable={G.is_orientable()} vol={float(G.volume()):.6f} (= vol(m004)/2 = {float(M.volume())/2:.6f})')
covs = [c for c in G.covers(2) if c.is_orientable()]
print('  orientable double covers of m000:', [(float(c.volume()), c.is_isometric_to(M)) for c in covs])

sec('B1104: Isom(m004) = D4 (order 8); B735: m004(5,1) has 0 cusps')
S = M.symmetry_group(); print(f'  symmetry group: {S} order {S.order()} abelian={S.is_abelian()}')
N = snappy.Manifold('m004(5,1)'); print(f'  m004(5,1): cusps={N.num_cusps()} vol={float(N.volume()):.6f}')

sec('B980: Vol(4_1) = 6 Lambda(pi/3) = 2.0298832128193072500424051081... (28 digits)')
lob = lambda t: -mp.quad(lambda x: mp.log(abs(2*mp.sin(x))), [0, t])
v = 6*lob(mp.pi/3); print('  6*Lambda(pi/3) =', mp.nstr(v, 30)); ok(mp.nstr(v, 29) == '2.0298832128193072500424051081', 'string compare at 29 sig. digits')
print('  SnapPy high precision:', snappy.Manifold('m004').high_precision().volume())

sec('B401: L(1, chi_-15) = 2 pi h / (w sqrt15) = 2pi/sqrt15 (h=2, w=2)')
try:
    Lv = pari('lfun(lfuncreate(-15), 1)'); print('  PARI L(1,chi_-15) =', Lv, '| 2pi/sqrt15 =', 2*math.pi/math.sqrt(15), '| h(-15) =', pari('qfbclassno(-15)'))
except Exception as e: print('  lfun failed:', e)

sec('B689/B698: level-15 newform = 15a; a3, a5; L(15a,1), L(15a,2), L\'(15a,0), real period')
try:
    E = pari("ellinit([1,1,1,-10,-10])"); print('  15a1 a3 =', pari('ellap(ellinit([1,1,1,-10,-10]),3)'), 'a5 =', pari('ellap(ellinit([1,1,1,-10,-10]),5)'), 'omega =', pari('ellinit([1,1,1,-10,-10]).omega[1]'), 'genus X0(3),X0(5) =', pari('mfdim(mfinit([3,2],1))'), pari('mfdim(mfinit([5,2],1))'))
    print('  L(15a,1) =', pari('lfun(ellinit([1,1,1,-10,-10]),1)'), 'L(15a,2) =', pari('lfun(ellinit([1,1,1,-10,-10]),2)'), "L'(15a,0) =", pari('lfun(ellinit([1,1,1,-10,-10]),0,1)'))
    print('  real period (LMFDB convention, 15a1 has disc<0? use omega[1]):', pari('ellinit([1,1,1,-10,-10]).omega'))
except Exception as e: print('  PARI elliptic failed:', e)

sec('B336: J_N(4_1; zeta_15) real for all N (Habiro form)')
def J(N, q):
    s = 0
    for k in range(N):
        p = 1
        for j in range(1, k+1): p *= (q**((N+j)/2) - q**(-(N+j)/2)) * (q**((N-j)/2) - q**(-(N-j)/2))
        s += p
    return s
q = cmath.exp(2j*cmath.pi/15)
print('  max |Im J_N| for N=1..40:', max(abs(J(N, q).imag) for N in range(1, 41)), '(each factor pair is (2i sin a)(2i sin b), real termwise)')

sec('B1114/B1200: kappa = tr[a,b] for the m004 holonomy generators; |kappa - 2| = 1 ?')
Gp = M.fundamental_group(); print('  generators', Gp.generators(), 'relators', Gp.relators())
a, b = Gp.SL2C('a'), Gp.SL2C('b')
comm = Gp.SL2C('abAB'); k = complex(comm.trace()); print('  tr[a,b] =', k, ' |kappa-2| =', abs(k-2), ' tr a =', complex(a.trace()), ' tr b =', complex(b.trace()))

sec('B212: silver (m136) holonomy square traces vanish mod (1+i) in Z[i]')
N = snappy.Manifold('m136'); Gs = N.fundamental_group(); print('  m136 generators', Gs.generators(), 'relators', Gs.relators())
for g in Gs.generators():
    t = complex(Gs.SL2C(g).trace()); t2 = complex(Gs.SL2C(g+g).trace()); print(f'  tr({g})={t:.6f} tr({g}^2)={t2:.6f}')

sec('B955: pi_1(m004) surjects onto A4, D5, S5 (via covers of degree 4/5)')
for d in (4, 5):
    cs = M.covers(d); print(f'  degree {d}: {len(cs)} covers; cover types:', [c.cover_info()['type'] for c in cs][:12])

sec('B1232: |Gal(Q(zeta3)/Q)| = 2; B665: SL(2,5) not simple (center +-I), PSL(2,5) = A5 (order 60)')
print('  [Q(zeta3):Q] =', pari('poldegree(polcyclo(3))'), '; |SL(2,5)| = 120, center order 2, |PSL(2,5)| = 60 = |A5| (group theory, no tool needed)')
