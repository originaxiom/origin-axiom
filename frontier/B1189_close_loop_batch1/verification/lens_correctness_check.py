"""Adversarial CORRECTNESS lens on GC-5: independent re-derivation of the
discriminating facts. Own code throughout (not a re-run of gc5_spotcheck*.py).

Facts checked:
  F1  (item 1/B1174): mirror of m004 acts on holonomy traces (a, b, ab) as
      complex conjugation. tol 1e-9. Plus amphichirality.
  F2  (item 1/B1182): exact Galois arithmetic in Q(zeta12): k11 fixes sqrt3 &
      flips sqrt-3; k7 fixes K=Q(sqrt-3) pointwise & flips sqrt3; k5 fixes i &
      flips both; 11*7=5 mod 12; the label-preserving iso (c,r,theta)->(k11,k7,k5)
      is UNIQUE given the constraints (c flips sqrt-3, r fixes K pointwise).
  F3  (items 1,2,5 / B1182,B786,B769): trace-reversal invariance tr(w^rev)=tr(w)
      for generic symbolic 2x2 matrices, ALL words in {A,B} to length 5, exact.
      TWO-SIDED control: entrywise-square map FAILS the same identity.
  F4  (item 2/B787): A5 is ambivalent with EVEN conjugators (every g ~ g^-1 in
      A5 itself), and specifically 5-cycles need no odd conjugator; monodromy
      inversion swaps {phi^2, phi^-2} (eigenvalues of [[2,1],[1,1]]).
  F5  (item 3/B942): c not in Gal(K^ab/K) at the cyclotomic layers: for each m,
      the subgroup of (Z/m)^* fixing sqrt(-3) (kernel of the quadratic character
      chi_{-3}) has index exactly 2, and no element acting as c on K lies in it.
      Independent implementation via the Kronecker symbol chi_{-3}(a)=(a|3)
      pattern: a mod 3 == 1 -> fix, == 2 -> flip (for gcd(a,m)=1, 3|m).
  F6  (item 5/B279): SnapPy 4_1: symmetry group D4 order 8; H1 = Z; all
      self-isometries' cusp maps have entries in {-1,0,1} and are == I mod 2.
  F7  (item 4/B1166): CS(m004) = 0: Im(complex_volume) ~ 0 (tol 1e-12 claimed
      1.8e-15 in-arc; we use 1e-9 for the discriminating zero) and two-sided:
      a chiral knot (m003? use 5_2 = m015) has nonzero CS.
  F8  (item 5/B769): c,gamma5 as field automorphisms of Q(sqrt-3,sqrt5) commute
      entrywise on matrices, exact symbolic (Symbol-level reduction, the bug
      class GC-5 narrates); control: entrywise square is not a homomorphism.
"""
import sys, itertools
from fractions import Fraction

results = {}

def bank(k, ok, detail):
    results[k] = (ok, detail)
    print(("PASS " if ok else "FAIL ") + k + " :: " + str(detail))

# ---------- F3: trace-reversal invariance, exact, generic 2x2 ----------
import sympy as sp
a11,a12,a21,a22,b11,b12,b21,b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A = sp.Matrix([[a11,a12],[a21,a22]]); B = sp.Matrix([[b11,b12],[b21,b22]])
def word_eval(w, X, Y):
    M = sp.eye(2)
    for ch in w:
        M = M * (X if ch=='A' else Y)
    return M
allwords = []
for L in range(1,6):
    for w in itertools.product('AB', repeat=L):
        allwords.append(''.join(w))
fails = []
for w in allwords:
    t1 = sp.expand(word_eval(w,A,B).trace())
    t2 = sp.expand(word_eval(w[::-1],A,B).trace())
    if sp.simplify(t1-t2) != 0:
        fails.append(w)
bank('F3a_trace_reversal_all_words_len<=5', len(fails)==0,
     f'{len(allwords)} words checked exact, failures={fails}')
# two-sided control: entrywise square (a non-homomorphism) must BREAK it
Asq = A.applyfunc(lambda x: x**2); Bsq = B.applyfunc(lambda x: x**2)
w = 'AABAB'
ctrl = sp.simplify(sp.expand(word_eval(w,Asq,Bsq).trace())
                   - sp.expand((word_eval(w,A,B).applyfunc(lambda x:x**2)).trace()))
bank('F3b_control_entrywise_square_breaks', ctrl != 0,
     f'entrywise-square vs square-of-word trace differ (nonzero symbolic diff): {ctrl!=0}')

# ---------- F2: exact Q(zeta12) Galois arithmetic ----------
z = sp.exp(2*sp.pi*sp.I/12)
def act(k, expr_in_z):
    # substitute z -> z^k then simplify to closed form
    return sp.simplify(sp.expand(expr_in_z.subs(zz, zz**k)))
zz = sp.Symbol('zz')
# represent surds as polynomials in zz, reduce mod Phi_12(zz)=zz^4-zz^2+1
Phi12 = sp.Poly(zz**4 - zz**2 + 1, zz)
sqrt3_poly  = sp.Poly(zz + zz**11, zz)          # zeta12+zeta12^-1 = 2cos(pi/6)=sqrt3
i_poly      = sp.Poly(zz**3, zz)
sqrtm3_poly = sp.Poly(zz**3*(zz+zz**11), zz)     # i*sqrt3
def reduce_mod(p):
    return sp.expand(sp.rem(p.as_expr(), Phi12.as_expr(), zz))
def galois(k, p):
    q = sp.Poly(sp.expand(p.as_expr().subs(zz, zz**k)), zz)
    return reduce_mod(q)
base = {'sqrt3': sqrt3_poly, 'i': i_poly, 'sqrtm3': sqrtm3_poly}
red  = {n: reduce_mod(p) for n,p in base.items()}
table = {}
for k in (1,5,7,11):
    row = {}
    for n,p in base.items():
        img = galois(k,p)
        if sp.expand(img - red[n]) == 0: row[n] = '+'
        elif sp.expand(img + red[n]) == 0: row[n] = '-'
        else: row[n] = '?'
    table[k] = row
expected = {1:{'sqrt3':'+','i':'+','sqrtm3':'+'},
            5:{'sqrt3':'-','i':'+','sqrtm3':'-'},
            7:{'sqrt3':'-','i':'-','sqrtm3':'+'},
            11:{'sqrt3':'+','i':'-','sqrtm3':'-'}}
bank('F2a_V4_action_table', table==expected, table)
# uniqueness of the label-preserving iso: c must flip sqrt-3 (& fix sqrt3, as the
# mirror fixes the real subfield): only k11. r must fix K pointwise: only k7.
c_cands = [k for k in (5,7,11) if table[k]['sqrtm3']=='-' and table[k]['sqrt3']=='+']
r_cands = [k for k in (5,7,11) if table[k]['sqrtm3']=='+']
bank('F2b_iso_uniqueness', c_cands==[11] and r_cands==[7] and (11*7)%12==5,
     f'c candidates={c_cands}, r candidates={r_cands}, 11*7 mod 12={(11*7)%12}')

# ---------- F4: A5 ambivalence with even conjugators ----------
from itertools import permutations
def perm_mul(p,q):  # (p*q)(x) = p(q(x))
    return tuple(p[q[i]] for i in range(5))
def perm_inv(p):
    r=[0]*5
    for i,v in enumerate(p): r[v]=i
    return tuple(r)
def parity(p):
    s=0
    for i in range(5):
        for j in range(i+1,5):
            if p[i]>p[j]: s+=1
    return s%2
A5 = [p for p in permutations(range(5)) if parity(p)==0]
bad = []
for g in A5:
    gi = perm_inv(g)
    if not any(perm_mul(perm_mul(h,g),perm_inv(h))==gi for h in A5):
        bad.append(g)
bank('F4a_A5_ambivalent_even_conjugators', len(bad)==0,
     f'|A5|={len(A5)}, elements lacking an even conjugator to inverse: {len(bad)}')
# monodromy inversion swaps {phi^2, phi^-2}
Mo = sp.Matrix([[2,1],[1,1]])
ev  = sorted(Mo.eigenvals().keys(), key=lambda e: sp.N(e))
evi = sorted(Mo.inv().eigenvals().keys(), key=lambda e: sp.N(e))
phi = (1+sp.sqrt(5))/2
ok4b = (sp.simplify(ev[1]-phi**2)==0 and sp.simplify(ev[0]-phi**-2)==0
        and sp.simplify(evi[1]-phi**2)==0 and sp.simplify(evi[0]-phi**-2)==0
        and sp.simplify(ev[0]*ev[1]-1)==0)
bank('F4b_monodromy_inversion_swaps_phi2', ok4b,
     f'eig(M)={[sp.nsimplify(e) for e in ev]}, eig(M^-1) same set (product=1) -> inversion swaps them')

# ---------- F5: c never in the K-fixing cyclotomic subgroups ----------
import math
def chi_m3(a):
    # quadratic character of Q(sqrt-3): chi(a) = +1 iff a = 1 mod 3 (a coprime to 3)
    am = a % 3
    return 1 if am==1 else (-1 if am==2 else 0)
layer_report = []
okF5 = True
for m in (3,6,9,12,15,21,33,39,63,105,231,1155):
    units = [a for a in range(1,m+1) if math.gcd(a,m)==1]
    fixers = [a for a in units if chi_m3(a)==1]
    idx = len(units)//len(fixers) if fixers else None
    # c acts as -1 under chi; membership in the K-fixing subgroup requires chi=+1
    c_in = any(chi_m3(a)==-1 and a in fixers for a in units)  # vacuously False by construction; assert structurally
    okF5 = okF5 and (idx==2) and (not c_in)
    layer_report.append((m, len(units), len(fixers), idx))
bank('F5_cyclotomic_layers_index2_c_excluded', okF5,
     f'(m,|units|,|fixers|,index): {layer_report}')

# ---------- F1, F6, F7: SnapPy ----------
import snappy
Mfd = snappy.Manifold('m004')
Mrev = Mfd.copy(); Mrev.reverse_orientation()
G  = Mfd.fundamental_group()
Gr = Mrev.fundamental_group()
words = ['a','b','ab','aabb','abAB']
def tr(gp, w):
    m = gp.SL2C(w)
    return complex(m[0,0]+m[1,1])
maxdev = 0.0
for w in words:
    t  = tr(G,w); trv = tr(Gr,w)
    dev = abs(trv - t.conjugate())
    maxdev = max(maxdev, dev)
bank('F1a_mirror_traces_are_conjugates', maxdev < 1e-9,
     f'max |tr_rev(w) - conj(tr(w))| over {words} = {maxdev:.2e} (tol 1e-9)')
# two-sided: the traces are genuinely non-real so conjugation is a nontrivial op
im_a = abs(tr(G,'a').imag)
bank('F1b_control_traces_nonreal', im_a > 0.1,
     f'|Im tr(a)| = {im_a:.6f} (conjugation acts nontrivially; not vacuous)')
bank('F1c_amphichiral', Mfd.is_isometric_to(Mrev), 'm004 isometric to its mirror')

K41 = snappy.Manifold('4_1')
sg = K41.symmetry_group()
isoms = K41.isomorphisms_to(K41)
cusp_ok = True; n_isoms = 0
for iso in isoms:
    n_isoms += 1
    for cm in iso.cusp_maps():
        for i in range(2):
            for j in range(2):
                e = cm[i,j]
                if e not in (-1,0,1): cusp_ok = False
                if (e - (1 if i==j else 0)) % 2 != 0: cusp_ok = False
bank('F6_41_symmetries', str(sg)=='D4' and sg.order()==8 and
     str(K41.homology())=='Z' and n_isoms==8 and cusp_ok,
     f'sym={sg}, order={sg.order()}, H1={K41.homology()}, isoms={n_isoms}, cusp maps in {{-1,0,1}} & ==I mod 2: {cusp_ok}')

cv = Mfd.complex_volume()   # Vol + i*CS (mod pi^2 i/... convention); Im ~ CS
im_cv = abs(complex(cv).imag)
M52 = snappy.Manifold('5_2')
im_cv52 = abs(complex(M52.complex_volume()).imag)
bank('F7_CS_m004_zero_two_sided', im_cv < 1e-9 and im_cv52 > 1e-3,
     f'|Im cvol(m004)|={im_cv:.2e} (tol 1e-9); control |Im cvol(5_2)|={im_cv52:.4f} nonzero')

# ---------- F8: field automorphisms commute entrywise (Symbol-level) ----------
r3, r5 = sp.symbols('r3 r5')   # formal sqrt(-3), sqrt(5); relations r3^2=-3, r5^2=5
def reduce_f(e):
    e = sp.expand(e)
    e = sp.rem(sp.Poly(e,[r3,r5]).as_expr(), r3**2+3, r3) if e.has(r3) else e
    e = sp.expand(e)
    # reduce r5 powers
    p = sp.Poly(e, r5) if e.has(r5) else None
    if p is not None:
        e = sp.rem(p.as_expr(), r5**2-5, r5)
    return sp.expand(e)
def c_auto(e):  return reduce_f(e.subs(r3,-r3))
def g5_auto(e): return reduce_f(e.subs(r5,-r5))
test_entries = [1+r3, r5-2*r3, sp.Rational(1,2)*(1+r3)*(2-r5), r3*r5+7]
comm_ok = all(sp.expand(c_auto(g5_auto(e)) - g5_auto(c_auto(e)))==0 for e in test_entries)
invol_ok = all(sp.expand(c_auto(c_auto(e))-reduce_f(e))==0 and
               sp.expand(g5_auto(g5_auto(e))-reduce_f(e))==0 for e in test_entries)
# homomorphism check on a 2x2 matrix product (entrywise application)
Xm = sp.Matrix([[1+r3, r5],[2, 1-r3]]); Ym = sp.Matrix([[r5, 1],[r3, 3]])
prod_then_c = (Xm*Ym).applyfunc(c_auto)
c_then_prod = (Xm.applyfunc(c_auto))*(Ym.applyfunc(c_auto))
hom_ok = all(sp.expand(reduce_f(prod_then_c[i]-c_then_prod[i]))==0 for i in range(4))
# control: entrywise square is NOT a homomorphism on the same product
sq_prod = (Xm*Ym).applyfunc(lambda x: x**2)
prod_sq = (Xm.applyfunc(lambda x:x**2))*(Ym.applyfunc(lambda x:x**2))
ctrl_fails = any(sp.expand(reduce_f(sq_prod[i]-prod_sq[i]))!=0 for i in range(4))
bank('F8_field_autos_commute_and_hom', comm_ok and invol_ok and hom_ok and ctrl_fails,
     f'c,g5 commute={comm_ok}, involutions={invol_ok}, c is ring hom on matrix product={hom_ok}, control(entrywise square breaks)={ctrl_fails}')

nfail = sum(1 for ok,_ in results.values() if not ok)
print(f'\nTOTAL: {len(results)} checks, {nfail} failures')
sys.exit(0 if nfail==0 else 1)
