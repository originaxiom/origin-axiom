#!/usr/bin/env python3
"""Upgrade the 63/63 class-by-class character match to EXACT cyclotomic arithmetic.

Still blind (no repo verification scripts read). Uses the class-representative
words found by the mod-p enumeration (p=331), evaluates them exactly in
Z[zeta_15, 1/75], and compares (chi_odd, chi_even) class-by-class against the
exact quaternion-model characters in Q(zeta_15), equality tested mod Phi_15.
Also: the nontrivial scalar element must be exactly -Identity, and the class
size multiset must equal {sA*sB}.
"""
import itertools, json
from math import gcd
from fractions import Fraction as Fr
src = open(__file__.replace('exact_traces.py','blind_instrument.py')).read()
src = src.split("results = {}")[0].replace("HERE = __file__.rsplit('/',1)[0]", "HERE='.'")
exec(src)

p = 331
r = run_prime(p, TEXP)
words = r['class_words']
sizes = [s for s,_,_ in r['gclass']]
print('max word length:', max(len(w) for w in words if w != '(identity)'))
# class size multiset check
prod_sizes = sorted(len(a)*len(b) for a in clsT for b in clsI)
print('class sizes == 2T x 2I products:', sorted(sizes) == prod_sizes)
assert sum(sizes) == 2880

# ---- exact matrices over Z[zeta15] with power-of-75 denominators ----
def matmul_int(A, B):
    return [[__import__('functools').reduce(cadd, (cmul(A[i][k], B[k][j]) for k in range(6)))
             for j in range(6)] for i in range(6)]

def reduce_mat(M, den):
    g = den
    for row in M:
        for v in row:
            for c in v:
                g = gcd(g, abs(c))
                if g == 1: return M, den
    if g > 1:
        M = [[tuple(c//g for c in v) for v in row] for row in M]
        den //= g
    return M, den

I6c = [[cyc(0) if i==j else cyc(None) for j in range(6)] for i in range(6)]
Tc  = [[ (cyc(TEXP[i]) if i==j else cyc(None)) for j in range(6)] for i in range(6)]
Tbar= [[ (cyc(-TEXP[i]) if i==j else cyc(None)) for j in range(6)] for i in range(6)]
Sc  = [[SIGMA[i][j] for j in range(6)] for i in range(6)]
Sdag= [[cconj(SIGMA[j][i]) for j in range(6)] for i in range(6)]
# L = Sigma^{-1} T^{-1} Sigma = (Sigma^dag/75) T^bar Sigma  (T unitary diag)
Lnum = matmul_int(matmul_int(Sdag, Tbar), Sc)   # denominator 75
GENS = {'R': (Tc, 1), 'L': (Lnum, 75)}

def evalword(w):
    M, den = I6c, 1
    if w == '(identity)': return M, den
    for ch in w:
        Gm, Gd = GENS[ch]
        M = matmul_int(M, Gm); den *= Gd
        M, den = reduce_mat(M, den)
    return M, den

def trace_cyc(M):
    return __import__('functools').reduce(cadd, (M[i][i] for i in range(6)))

# theta = -Sigma^2/75, exact: numerator -Sigma^2, den 75 (equality only mod Phi15)
S2 = matmul_int(Sc, Sc)
ThN = [[cneg(S2[i][j]) for j in range(6)] for i in range(6)]
ThN, thden = reduce_mat(ThN, 75)
# verify theta equals the conjugation permutation P (0->0, 1<->2, 3->3, 4<->5) mod Phi15
P = {0:0, 1:2, 2:1, 3:3, 4:5, 5:4}
perm_ok = True
for i in range(6):
    for j in range(6):
        target = cyc(0) if P[i]==j else cyc(None)
        if not is_zero_mod_phi15(csub(ThN[i][j], tuple(thden*c for c in target))):
            perm_ok = False
print('theta = -Sigma^2/75 IS the conjugation permutation exactly (mod Phi15):', perm_ok)

# exact scalar check: evaluate the nontrivial scalar word
sw = [w for w in r['scalars'] if w][0]
Msc, dsc = evalword(sw)
minus_ok = all(
    is_zero_mod_phi15(csub(Msc[i][j], (tuple(-dsc if k==0 else 0 for k in range(15)) if i==j else cyc(None))))
    for i in range(6) for j in range(6))
print(f'nontrivial scalar ({sw}) is exactly -1:', minus_ok)

# exact class characters
gclass_exact = []
for w, s in zip(words, sizes):
    M, den = evalword(w)
    ThM = matmul_int(ThN, M)                     # denominator den*thden
    t   = tuple(thden*c for c in trace_cyc(M))   # bring to common den den*thden
    tth = trace_cyc(ThM)
    # chi_odd = (t - tth)/(2 den thden), chi_even = (t + tth)/(2 den thden)
    gclass_exact.append((s, csub(t,tth), cadd(t,tth), 2*den*thden))

# model exact: omega = zeta^5, sqrt5 = 1 + 2(zeta^3 + zeta^12); values as cyc with denominator
def qd_to_cyc(q):  # a + b sqrt5, Fractions -> (cyc numerator, int denominator)
    da, db = q.a.denominator, q.b.denominator
    D = da*db // gcd(da,db)
    na = q.a.numerator * (D//da); nb = q.b.numerator * (D//db)
    sqrt5 = cadd(cyc(0), cadd(cadd(cyc(3),cyc(3)), cadd(cyc(12),cyc(12))))  # 1+2z3+2z12
    v = cadd(tuple(na*c for c in cyc(0)), tuple(nb*c for c in sqrt5))
    return v, D
model_exact = []
for CA in clsT:
    a = CA[0]; ka = chi_exp(a)   # chi(a) = omega^ka = zeta^(5 ka)
    trA, dA = qd_to_cyc(Qd(2*a.w.a, 2*a.w.b))
    for CB in clsI:
        b = CB[0]
        trB, dB = qd_to_cyc(Qd(2*b.w.a, 2*b.w.b))
        odd = cmul(cyc(5*ka), trB)          # chi(A) trV2(B), denominator dB
        even = cmul(trA, trB)               # denominator dA*dB
        model_exact.append((len(CA)*len(CB), odd, dB, even, dA*dB))

# exact bipartite perfect matching (greedy: values are distinct enough; do full matching)
def eq_frac_cyc(n1, d1, n2, d2):
    # n1/d1 == n2/d2 in Q(zeta15)?
    a = tuple(x*d2 for x in n1); b = tuple(x*d1 for x in n2)
    return is_zero_mod_phi15(csub(a,b))

unused = list(range(63))
assign = []
ok = True
for (s, odd2, even2, twod) in gclass_exact:
    hit = None
    for idx in unused:
        (ms, modd, mod_d, meven, meved) = model_exact[idx]
        if ms != s: continue
        if not eq_frac_cyc(odd2, twod, modd, mod_d): continue
        if not eq_frac_cyc(even2, twod, meven, meved): continue
        hit = idx; break
    if hit is None:
        ok = False
        print('NO exact model match for class with size', s)
        break
    unused.remove(hit); assign.append(hit)
print('EXACT 63/63 class-by-class character match:', ok and not unused)

json.dump({'exact_63_match': ok and not unused,
           'scalar_is_minus_identity': minus_ok,
           'theta_is_permutation': perm_ok,
           'class_sizes_are_products': sorted(sizes) == prod_sizes,
           'max_word_len': max(len(w) for w in words if w != '(identity)')},
          open(__file__.replace('exact_traces.py','exact_traces_out.json'),'w'), indent=1)
