#!/usr/bin/env python3
"""R02 blind recomputation, part 2: the B1011 instrument.

Written BLIND: no repo verification scripts read. SU(3) level-2 modular data built
from the Kac-Peterson formula directly.

Claim under test (B1011): with R = T and L = S^-1 T^-1 S on the six SU(3)_2
primaries, the group G = <R,L> has order 2880 = |2T x 2I|, 63 = 7 x 9 conjugacy
classes, global scalars +-1, and rho_6 = (chi x V2(2I)) (+) (V2(2T) x V2(2I))
as a 2T x 2I representation, verified by a 63/63 class-by-class (size, chi_odd,
chi_even) match against the model characters chi(A)trV2(B) and trV2(A)trV2(B).

Method:
  * S-matrix numerator Sigma_{lm} = sum_{w in W(A2)} det(w) e^{-2pi i (w(l+rho), m+rho)/5}
    -- all entries in Z[zeta_15]. Exact check Sigma Sigma^dag = 75 I in Z[x]/(x^15-1)
    reduced mod Phi_15.
  * T = diag(e^{2pi i (h - c/24)}), h = Casimir/5, c = 16/5 -> zeta_15 powers
    (-2, 2, 2, 7, 8, 8) on primaries ordered [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)].
    (Alt convention without c/24 also run, to type any convention mismatch.)
  * Enumerate <R, L> over F_p at TWO primes p = 331, 421 (both = 1 mod 15,
    different from the bank's 61/241 except none shared), zeta_15 -> fixed
    element of order 15. Faithfulness of reduction: the standard Minkowski/Serre
    fact that reduction mod p (p not dividing the group order-relevant primes,
    p > 2, entries p-integral) is injective on finite matrix groups.
  * Conjugacy classes by orbit closure under conjugation by the generators.
  * chi_odd/chi_even via the central charge-conjugation C = Sigma^2/75:
    P_odd = (I-C)/2. Class match against the exact quaternion-model characters
    of 2T x 2I (chi = the Z3 character with kernel Q8), embedded in F_p via the
    same zeta_15 (omega = zeta_15^5, sqrt5 = 1 + 2(zeta_15^3 + zeta_15^12)).
  * CONTROL: a deliberately wrong model (chi -> trivial in the odd factor) must
    FAIL the 63/63 match.
  * Float cross-check of the group order.
"""
import itertools, json
from fractions import Fraction as Fr

HERE = __file__.rsplit('/',1)[0]

# ---------------- exact Z[zeta15] as vectors mod (x^15 - 1), equality mod Phi15 ----------------
PHI15 = [1,-1,0,1,-1,1,0,-1,1]  # x^8 - x^7 + x^5 - x^4 + x^3 - x + 1 (coeffs ascending)
def cyc(k=None):
    v = [0]*15
    if k is not None: v[k % 15] = 1
    return tuple(v)
def cadd(a,b): return tuple(x+y for x,y in zip(a,b))
def csub(a,b): return tuple(x-y for x,y in zip(a,b))
def cneg(a): return tuple(-x for x in a)
def cmul(a,b):
    v = [0]*15
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: v[(i+j)%15] += x*y
    return tuple(v)
def cconj(a):
    v = [0]*15
    for i,x in enumerate(a): v[(15-i)%15] = x
    return tuple(v)
def is_zero_mod_phi15(a):
    # reduce poly (deg<15) mod Phi15 over Q; zero iff remainder zero
    r = [Fr(x) for x in a]
    deg = 14
    P = [Fr(c) for c in PHI15]
    for d in range(14, 7, -1):
        if r[d] != 0:
            f = r[d] / P[8]
            for i in range(9):
                r[d-8+i] -= f*P[i]
    return all(x == 0 for x in r[:8]) and all(x == 0 for x in r[8:])

# ---------------- SU(3)_2 modular data ----------------
PRIM = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]
RHO = (1,1)
def s1(v): a,b = v; return (-a, a+b)
def s2(v): a,b = v; return (a+b, -b)
def weyl():
    seen = {}
    frontier = [((0,1),(1,0),1)]  # (image of e1?, ...) -- instead act on generic: store as function comp
    # represent w by its action on a pair basis via composition of s1,s2 applied to input
    # simpler: enumerate words up to length 3
    els = {}
    def apply(word, v):
        for c in reversed(word):
            v = s1(v) if c == 1 else s2(v)
        return v
    for L in range(0,4):
        for word in itertools.product([1,2],repeat=L):
            key = (apply(word,(1,0)), apply(word,(0,1)))
            if key not in els:
                els[key] = (word, (-1)**L)
    assert len(els) == 6, len(els)
    return [(w,s) for (w,s) in els.values()], apply
WEYL, wapply = weyl()

def ip3(u,v):
    # (u,v) = (2 u1 v1 + u1 v2 + u2 v1 + 2 u2 v2)/3 ; return 3*(u,v) as int
    return 2*u[0]*v[0] + u[0]*v[1] + u[1]*v[0] + 2*u[1]*v[1]

def sigma_matrix():
    M = [[None]*6 for _ in range(6)]
    for i,l in enumerate(PRIM):
        lp = (l[0]+1, l[1]+1)
        for j,m in enumerate(PRIM):
            mp = (m[0]+1, m[1]+1)
            acc = cyc(None)
            for (word, sgn) in WEYL:
                wl = wapply(word, lp)
                n = ip3(wl, mp)      # 3*(w(l+rho), m+rho); exponent -2pi n/15
                term = cyc(-n)
                acc = cadd(acc, term if sgn == 1 else cneg(term))
            M[i][j] = acc
    return M

SIGMA = sigma_matrix()

# exact unitarity: Sigma Sigma^dag = 75 I
def mat_mul_cyc(A,B):
    n = len(A)
    return [[
        __import__('functools').reduce(cadd, (cmul(A[i][k], B[k][j]) for k in range(n)))
        for j in range(n)] for i in range(n)]
SIGD = [[cconj(SIGMA[j][i]) for j in range(6)] for i in range(6)]
PROD = mat_mul_cyc(SIGMA, SIGD)
unit_ok = True
for i in range(6):
    for j in range(6):
        target = cyc(0) if i==j else cyc(None)
        t = tuple(75*x for x in target)
        if not is_zero_mod_phi15(csub(PROD[i][j], t)):
            unit_ok = False
print('Sigma Sigma^dag = 75 I exactly:', unit_ok)

# T exponents (in units of zeta_15): h = (l, l+2rho)/2 / 5 ; c/24 = 2/15
def t_exponents(with_c24=True):
    exps = []
    for l in PRIM:
        n = ip3(l, (l[0]+2, l[1]+2))   # 3*(l, l+2rho)
        # h = n/(3*2*5) = n/30 ; 15*h = n/2
        assert n % 2 == 0
        m = n // 2                      # 15*h
        if with_c24: m -= 2             # 15*(h - 2/15)
        exps.append(m % 15)
    return exps
TEXP = t_exponents(True)
TEXP_NOC = t_exponents(False)
print('T exponents (zeta15 powers, with c/24):', TEXP)
print('T exponents (no c/24):', TEXP_NOC)

# ---------------- quaternion models (rebuild here; identical conventions to part 1) ----------------
class Qd:
    __slots__=('a','b')
    def __init__(s,a,b): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): return Qd(s.a+o.a, s.b+o.b)
    def __sub__(s,o): return Qd(s.a-o.a, s.b-o.b)
    def __neg__(s): return Qd(-s.a,-s.b)
    def __mul__(s,o): return Qd(s.a*o.a+5*s.b*o.b, s.a*o.b+s.b*o.a)
    def __eq__(s,o): return s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def fl(s):
        import math; return float(s.a)+float(s.b)*math.sqrt(5)
class Quat:
    __slots__=('w','x','y','z')
    def __init__(s,w,x,y,z): s.w=w;s.x=x;s.y=y;s.z=z
    def __mul__(p,q):
        return Quat(p.w*q.w-p.x*q.x-p.y*q.y-p.z*q.z,
                    p.w*q.x+p.x*q.w+p.y*q.z-p.z*q.y,
                    p.w*q.y-p.x*q.z+p.y*q.w+p.z*q.x,
                    p.w*q.z+p.x*q.y-p.y*q.x+p.z*q.w)
    def conj(p): return Quat(p.w,-p.x,-p.y,-p.z)
    def key(p): return (p.w.a,p.w.b,p.x.a,p.x.b,p.y.a,p.y.b,p.z.a,p.z.b)
    def __eq__(p,q): return p.key()==q.key()
    def __hash__(p): return hash(p.key())
def quat(w,x,y,z):
    c=lambda v: v if isinstance(v,Qd) else Qd(v,0)
    return Quat(c(w),c(x),c(y),c(z))

def build_2T():
    E=[]
    for i in range(4):
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; E.append(quat(*v))
    for s in itertools.product([Fr(1,2),Fr(-1,2)],repeat=4):
        E.append(quat(*s))
    assert len(set(E))==24
    return E
def build_2I():
    T=build_2T()
    phi=Qd(Fr(1,2),Fr(1,2)); iphi=Qd(Fr(-1,2),Fr(1,2))
    vals=[Qd(0,0),Qd(1,0),iphi,phi]
    evens=[p for p in itertools.permutations(range(4))
           if sum(1 for a in range(4) for b in range(a+1,4) if p[a]>p[b])%2==0]
    extra=set()
    for p in evens:
        base=[vals[p[i]] for i in range(4)]
        for signs in itertools.product([1,-1],repeat=4):
            extra.add(Quat(*[Qd(c.a*Fr(1,2)*s, c.b*Fr(1,2)*s) for c,s in zip(base,signs)]))
    E=list(set(T)|extra)
    assert len(E)==120
    return E

def q_classes(E):
    S=set(E); seen=set(); out=[]
    for g in E:
        if g in seen: continue
        orb={g}; st=[g]
        while st:
            x=st.pop()
            for h in E:
                y=h*x*h.conj()
                if y not in orb: orb.add(y); st.append(y)
        seen|=orb; out.append(list(orb))
    return out

T24 = build_2T(); I120 = build_2I()
clsT = q_classes(T24); clsI = q_classes(I120)
print('2T classes:', sorted(len(c) for c in clsT))
print('2I classes:', sorted(len(c) for c in clsI))

# chi: Z3 character of 2T with kernel Q8. Q8 = the 8 unit quaternions.
Q8 = set()
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; Q8.add(quat(*v))
# 2T/Q8 = Z3 generated by omega_el = (1+i+j+k)/2 coset; chi(g) = omega^k where g in Q8*omega_el^k
om_el = quat(Fr(1,2),Fr(1,2),Fr(1,2),Fr(1,2))
coset = {}
for g in Q8: coset[g] = 0
for g in list(coset.keys()):
    pass
c1 = {om_el*g for g in Q8}; c2 = {om_el*om_el*g for g in Q8}
for g in c1: coset[g] = 1
for g in c2: coset[g] = 2
assert len(coset) == 24
def chi_exp(g): return coset[g]   # chi(g) = omega^chi_exp(g)

# ---------------- mod-p machinery ----------------
def run_prime(p, texp):
    # find zeta of order 15 in F_p
    assert (p-1) % 15 == 0
    z = None
    for g in range(2, p):
        cand = pow(g, (p-1)//15, p)
        if pow(cand, 15, p) == 1 and all(pow(cand, k, p) != 1 for k in [1,3,5]):
            z = cand; break
    Z = [pow(z, k, p) for k in range(15)]
    def cyc_to_fp(v): return sum(c*Z[i] for i,c in enumerate(v)) % p
    Sg = tuple(tuple(cyc_to_fp(SIGMA[i][j]) for j in range(6)) for i in range(6))
    Tm = tuple(tuple((Z[texp[i]] if i==j else 0) for j in range(6)) for i in range(6))
    def mmul(A,B):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(6)) % p for j in range(6)) for i in range(6))
    def minv(A):
        # Gauss-Jordan mod p
        n=6; M=[list(r)+[1 if i==j else 0 for j in range(n)] for i,r in enumerate(A)]
        for col in range(n):
            piv=None
            for r in range(col,n):
                if M[r][col]%p: piv=r; break
            M[col],M[piv]=M[piv],M[col]
            inv=pow(M[col][col],p-2,p)
            M[col]=[x*inv%p for x in M[col]]
            for r in range(n):
                if r!=col and M[r][col]%p:
                    f=M[r][col]
                    M[r]=[(x-f*y)%p for x,y in zip(M[r],M[col])]
        return tuple(tuple(M[i][n+j] for j in range(n)) for i in range(n))
    Tinv = tuple(tuple((pow(Z[texp[i]],p-2,p) if i==j else 0) for j in range(6)) for i in range(6))
    Sinv = minv(Sg)
    R = Tm
    L = mmul(mmul(Sinv, Tinv), Sg)
    I6 = tuple(tuple(1 if i==j else 0 for j in range(6)) for i in range(6))
    # BFS closure with word tracking
    from collections import deque
    words = {I6: ''}
    dq = deque([I6])
    gens = [('R',R), ('L',L)]
    while dq:
        g = dq.popleft()
        for nm, h in gens:
            x = mmul(g,h)
            if x not in words:
                words[x] = words[g] + nm
                dq.append(x)
        if len(words) > 20000: raise RuntimeError('group too big?')
    order = len(words)
    # scalars
    scalars = [words[g] for g in words if all(g[i][j]==0 for i in range(6) for j in range(6) if i!=j)
               and len({g[i][i] for i in range(6)})==1]
    # conjugacy classes: orbits under conjugation by generators
    elems = list(words.keys())
    Rinv = minv(R); Linv = minv(L)
    conj_gens = [(R,Rinv),(L,Linv)]
    unseen = set(elems); classes = []
    while unseen:
        g = next(iter(unseen))
        orb = {g}; st=[g]
        while st:
            x = st.pop()
            for h,hi in conj_gens:
                y = mmul(mmul(h,x),hi)
                if y not in orb: orb.add(y); st.append(y)
        unseen -= orb
        classes.append(orb)
    # charge conjugation: with honest S = Sigma/(5 i sqrt3), S^2 = C; unnormalized
    # Sigma^2 = -75 C (since (5 i sqrt3)^2 = -75).  So C = -Sigma^2/75.
    S2 = mmul(Sg,Sg)
    inv75 = pow(75, p-2, p)
    C = tuple(tuple((-S2[i][j]*inv75) % p for j in range(6)) for i in range(6))
    central = (mmul(C,R)==mmul(R,C)) and (mmul(C,L)==mmul(L,C))
    Cperm = [[C[i][j] for j in range(6)] for i in range(6)]
    # class data: (size, tr_odd, tr_even) with tr_odd = (tr g - tr Cg)/2
    inv2 = pow(2,p-2,p)
    def tr(g): return sum(g[i][i] for i in range(6)) % p
    gclass = []
    class_words = []
    for orb in classes:
        g = min(orb, key=lambda e: len(words[e]))
        t = tr(g); tc = tr(mmul(C,g))
        t_odd = (t - tc) * inv2 % p
        t_even = (t + tc) * inv2 % p
        gclass.append((len(orb), t_odd, t_even))
        class_words.append(words[g] if words[g] else '(identity)')
    # model side: 2T x 2I with chi(A) tr V2(B), tr V2(A) tr V2(B)
    om = Z[5]  # zeta_15^5 = primitive cube root
    sqrt5 = (1 + 2*(Z[3] + Z[12])) % p
    def qd_to_fp(q): # a + b sqrt5 with Fractions
        num_a, den_a = q.a.numerator, q.a.denominator
        num_b, den_b = q.b.numerator, q.b.denominator
        return (num_a*pow(den_a,p-2,p) + num_b*pow(den_b,p-2,p)*sqrt5) % p
    def trV2(q): return (2*qd_to_fp(q.w)) % p
    model = []
    for CA in clsT:
        a = CA[0]
        chiA = pow(om, chi_exp(a), p)
        trA = trV2(a)
        for CB in clsI:
            b = CB[0]
            model.append((len(CA)*len(CB), (chiA*trV2(b))%p, (trA*trV2(b))%p))
    # control model: chi -> trivial
    model_ctrl = []
    for CA in clsT:
        a = CA[0]; trA = trV2(a)
        for CB in clsI:
            b = CB[0]
            model_ctrl.append((len(CA)*len(CB), trV2(b)%p, (trA*trV2(b))%p))
    match = sorted(gclass) == sorted(model)
    # also try conjugate chi
    model_bar = []
    for CA in clsT:
        a = CA[0]
        chiA = pow(om, (3-chi_exp(a))%3, p)
        trA = trV2(a)
        for CB in clsI:
            b = CB[0]
            model_bar.append((len(CA)*len(CB), (chiA*trV2(b))%p, (trA*trV2(b))%p))
    match_bar = sorted(gclass) == sorted(model_bar)
    match_ctrl = sorted(gclass) == sorted(model_ctrl)
    return dict(p=p, order=order, n_classes=len(classes),
                class_sizes=sorted(len(c) for c in classes),
                scalars=scalars, C_central=central,
                match_63=match, match_63_chibar=match_bar, control_wrongmodel_matches=match_ctrl,
                class_words=class_words, gclass=gclass)

results = {}
for p in (331, 421):
    r = run_prime(p, TEXP)
    results[f'p{p}'] = {k:v for k,v in r.items() if k not in ('gclass',)}
    print(f"p={p}: order={r['order']} classes={r['n_classes']} scalars={r['scalars']} "
          f"C central={r['C_central']} 63/63 match={r['match_63']} (chibar: {r['match_63_chibar']}) "
          f"control-wrong-model matches={r['control_wrongmodel_matches']}")

# convention probe: T without c/24
r_noc = run_prime(331, TEXP_NOC)
results['no_c24_probe'] = dict(order=r_noc['order'], n_classes=r_noc['n_classes'], scalars=r_noc['scalars'])
print('no-c/24 convention: order', r_noc['order'], 'classes', r_noc['n_classes'], 'n_scalars', len(r_noc['scalars']))

# float cross-check of the order
import numpy as np, cmath
z = cmath.exp(2j*cmath.pi/15)
Sf = np.array([[sum(v[k]*z**k for k in range(15)) for v in row] for row in SIGMA])
Tf = np.diag([z**e for e in TEXP])
Rf = Tf; Lf = np.linalg.inv(Sf) @ np.linalg.inv(Tf) @ Sf
def keyf(M):
    v = M.reshape(-1)
    return tuple(np.round(v.real*1e6).astype(np.int64)) + tuple(np.round(v.imag*1e6).astype(np.int64))
seen = {keyf(np.eye(6,dtype=complex)): np.eye(6,dtype=complex)}
frontier=[np.eye(6,dtype=complex)]
while frontier:
    nf=[]
    for g in frontier:
        for h in (Rf,Lf):
            x=g@h; k=keyf(x)
            if k not in seen:
                seen[k]=x; nf.append(x)
    frontier=nf
    if len(seen)>20000: break
results['float_order'] = len(seen)
print('float order:', len(seen))

json.dump(results, open(HERE+'/blind_instrument_out.json','w'), indent=1, default=str)
