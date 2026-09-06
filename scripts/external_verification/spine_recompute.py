"""Independent recomputation of the Origin Axiom spine claims (own code, no repo imports).
Each check prints PASS/FAIL with the computed numbers."""
import itertools, math
import sympy as sp
import mpmath as mp
import numpy as np

results = {}
def check(name, ok, detail=""):
    results[name] = bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

# ---------- 1. A = LR: trace 3, eigenvalues phi^{+-2}, A = F^2 ----------
L = sp.Matrix([[1,1],[0,1]]); R = sp.Matrix([[1,0],[1,1]]); A = L*R
phi = (1+sp.sqrt(5))/2
ev = sorted(A.eigenvals().keys(), key=lambda e: float(e))
check("A=LR=[[2,1],[1,1]], tr 3, det 1", A == sp.Matrix([[2,1],[1,1]]) and A.trace()==3 and A.det()==1)
check("eigenvalues phi^-2, phi^2", sp.simplify(ev[0]-phi**-2)==0 and sp.simplify(ev[1]-phi**2)==0, str(ev))
F = sp.Matrix([[1,1],[1,0]]); check("Fibonacci F^2 = A", F*F == A)
# Mobius fixed points of A: tau^2 - tau - 1 = 0
tau = sp.symbols('tau'); fp = sp.solve(sp.together((2*tau+1)/(tau+1)-tau), tau)
check("Mobius fixed pts of A are phi, -1/phi", set(sp.simplify(x) for x in fp) == {sp.simplify(phi), sp.simplify(-1/phi)}, str(fp))

# ---------- 2. figure-eight group, Riley rep, trace field ----------
# 2-bridge presentation of 4_1 (= 5/3): <a,b | a w = w b>, w = b a^-1 b^-1 a   (a, b meridians)
u = sp.symbols('u')
a = sp.Matrix([[1,1],[0,1]]); b = sp.Matrix([[1,0],[u,1]])
ai, bi = a.inv(), b.inv()
w = b*ai*bi*a
rel = sp.simplify(a*w - w*b)
polys = set()
for e in rel:
    e = sp.factor(sp.expand(e))
    if e != 0: polys.add(e)
print("   relation entries (must all vanish on the Riley locus):", polys)
riley = sp.factor(sp.expand((a*w - w*b)[0,1]))  # the Riley polynomial
print("   Riley polynomial candidate:", riley)
om = sp.Rational(1,2) + sp.sqrt(3)*sp.I/2        # u = 1+omega = e^{i pi/3}, the Riley root
sol = sp.solve(u**2-u+1, u)
# check that u = omega (or its conjugate) kills the whole relation
ok=True
for uu in sol:
    M = (a*w - w*b).subs(u, uu)
    ok = ok and sp.simplify(M) == sp.zeros(2,2)
check("Riley locus of 4_1 is u^2-u+1=0, u = 1+omega = e^{i pi/3}: trace field Q(sqrt-3)  [B266: t=1+omega]", ok and all(sp.minimal_polynomial(s, u)==u**2-u+1 for s in sol), str(sol))
# longitude: search words in a,b whose Riley image is +-[[1,z],[0,1]] with z not an integer (the cusp shape of 4_1 is 2 sqrt(-3))
import itertools as _it
a_n = a.subs(u, om); b_n = b.subs(u, om); w_n = w.subs(u, om)
gens_n = {'a':a_n,'A':a_n.inv(),'b':b_n,'B':b_n.inv()}
found=None
# numeric search first (floats), then exact verification of the single word found
gens_f={k:np.array(v.tolist(),dtype=complex) for k,v in gens_n.items()}
for length in range(2,9):
    for word in _it.product('aAbB', repeat=length):
        wd=''.join(word)
        if any(x+y in wd for x,y in [('a','A'),('A','a'),('b','B'),('B','b')]): continue
        Mf=np.eye(2,dtype=complex)
        for ch in wd: Mf=Mf@gens_f[ch]
        if abs(Mf[1,0])<1e-9 and abs(abs(Mf[0,0])-1)<1e-9 and abs(Mf[0,0]-Mf[1,1])<1e-9 and abs(Mf[0,1].imag)>1e-6:
            M=sp.eye(2)
            for ch in wd: M=M*gens_n[ch]
            M=sp.simplify(M)
            if M[1,0]==0 and abs(M[0,0])==1 and M[0,0]==M[1,1] and sp.im(M[0,1])!=0:
                found=(wd,M); break
    if found: break
lam_word, lam_n = found
check("longitude found: a word commuting with meridian a, translation 2*sqrt(3)*i (cusp shape 2sqrt(-3))",
      sp.simplify(lam_n*a_n-a_n*lam_n)==sp.zeros(2,2) and sp.simplify(sp.im(lam_n[0,1])**2-12)==0,
      f"lambda={lam_word} -> {list(lam_n)}, tr={sp.simplify(lam_n.trace())}")
# ---------- 3. reduction mod (sqrt-3): image is SL(2,F3) = 2T of order 24 ----------
def mat_mod3(M):  # omega -> 1 mod the prime (1-omega) since Z[w]/(1-w) = F3
    return tuple(tuple(int(sp.nsimplify(M[i,j].subs(sp.sqrt(3)*sp.I, 2*sp.Symbol('w')+1)).subs(sp.Symbol('w'),1)) % 3 for j in range(2)) for i in range(2))
def mmul3(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2))%3 for j in range(2)) for i in range(2))
gens = [mat_mod3(a_n), mat_mod3(b_n)]
grp = {((1,0),(0,1))}; frontier=[((1,0),(0,1))]
while frontier:
    new=[]
    for g in frontier:
        for h in gens:
            x = mmul3(g,h)
            if x not in grp: grp.add(x); new.append(x)
    frontier=new
check("mod-(sqrt-3) image of pi_1(4_1) is SL(2,F3) (order 24 = 2T)", len(grp)==24, f"order {len(grp)}, gens {gens}")
# 2T = SL(2,3): center {+-I}, quotient A4 of order 12
check("all elements have det 1 mod 3", all((g[0][0]*g[1][1]-g[0][1]*g[1][0])%3==1 for g in grp))

# ---------- 4. McKay graph of 2T = affine E6 ----------
# realise 2T as the 24 unit Hurwitz quaternions in SU(2) (complex 2x2)
def q2m(a_,b_,c_,d_):  # quaternion a+bi+cj+dk -> SU(2) matrix
    return np.array([[a_+1j*b_, c_+1j*d_],[-c_+1j*d_, a_-1j*b_]])
units=[]
for s in itertools.product([1,-1], repeat=1):
    pass
units += [q2m(*v) for v in [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]]
units += [q2m(*[s/2 for s in signs]) for signs in itertools.product([1,-1], repeat=4)]
assert len(units)==24
# irreps of 2T: 1, w, w^2 (via 2T -> A4 -> Z/3), natural 2, 2 x w, 2 x w^2, 3 (= Sym^2 natural)
# compute characters: need the Z/3 quotient map. 2T/Q8 = Z/3; Q8 = the 8 units of +-1,+-i,+-j,+-k.
def key(M): return tuple(np.round(M.flatten(),6))
Q8 = {key(m) for m in units[:8]}
# label cosets: pick g0 = (1+i+j+k)/2 as generator of Z/3
g0 = q2m(.5,.5,.5,.5)
def z3_label(M):
    for k in range(3):
        # M in Q8 * g0^k ?
        cand = M @ np.linalg.matrix_power(np.linalg.inv(g0), k)
        if key(cand) in Q8: return k
    raise ValueError
wz = np.exp(2j*np.pi/3)
chars = {}
chars['1']  = [1 for M in units]
chars['w']  = [wz**z3_label(M) for M in units]
chars['w2'] = [wz**(2*z3_label(M)) for M in units]
chars['2']  = [np.trace(M) for M in units]
chars["2'"] = [np.trace(M)*wz**z3_label(M) for M in units]
chars["2''"]= [np.trace(M)*wz**(2*z3_label(M)) for M in units]
chars['3']  = [np.trace(M)**2-1 for M in units]     # Sym^2 char = chi^2 - chi(g^2); for SU(2): t^2 - 1 (chi(g^2)=t^2-2, so Sym2 = (t^2 + (t^2-2))/2 = t^2-1)
names = list(chars)
# orthonormality check
G = np.array([[np.mean(np.array(chars[x])*np.conj(chars[y])) for y in names] for x in names])
check("2T character table orthonormal (7 irreps, dims 1,1,1,2,2,2,3)", np.allclose(G, np.eye(7), atol=1e-9))
# McKay matrix: multiplicity of irrep j in irrep i (x) natural 2
Mk = np.zeros((7,7),dtype=int)
for i,x in enumerate(names):
    for j,y in enumerate(names):
        Mk[i,j] = int(round(np.real(np.mean(np.array(chars[x])*np.array(chars['2'])*np.conj(chars[y])))))
print("   McKay matrix rows:", {names[i]: [names[j] for j in range(7) if Mk[i,j]] for i in range(7)})
degs = [1,1,1,2,2,2,3]
check("McKay graph symmetric, Perron eigenvalue 2, marks = irrep dims (affine E6: 3 legs of length 2 on a trivalent node)",
      (Mk==Mk.T).all() and abs(max(np.linalg.eigvals(Mk).real)-2)<1e-9 and np.allclose(Mk@np.array(degs), 2*np.array(degs))
      and sorted(Mk.sum(axis=1))==[1,1,1,2,2,2,3])

# ---------- 5. Vol(m004) = (3 sqrt3 / 2) L(chi_-3, 2) = 9 sqrt3 zeta_K(2)/pi^2 ----------
mp.mp.dps = 40
Lchi = (mp.polygamma(1, mp.mpf(1)/3) - mp.polygamma(1, mp.mpf(2)/3))/9   # L(chi_-3,2) = sum_{n=1 mod 3} 1/n^2 - sum_{n=2 mod 3} 1/n^2
vol_formula = 3*mp.sqrt(3)/2*Lchi
# independent volume: 2 * regular ideal tetrahedron = 6 Lobachevsky(pi/3) = 3 * Clausen(pi/3)... use Cl2(theta)= -int_0^theta log|2 sin(t/2)| dt
Cl2 = lambda th: -mp.quad(lambda t: mp.log(2*mp.sin(t/2)), [0, th])
vol_tet = 3*Cl2(2*mp.pi/3)/2   # regular ideal tetrahedron = 3*Lob(pi/3), Lob(th) = Cl2(2th)/2
vol_m004 = 2*vol_tet
print(f"   Vol via Clausen = {vol_m004}\n   (3sqrt3/2) L(chi_-3,2) = {vol_formula}\n   SnapPy value 2.0298832128193072")
check("Vol(m004) = (3sqrt3/2)L(chi_-3,2) to 30 digits", abs(vol_m004-vol_formula) < mp.mpf(10)**-30)
check("Vol(m004) matches 2.0298832128193072", abs(vol_m004-mp.mpf('2.0298832128193072')) < 1e-15)

# ---------- 6. sin^2 theta_W = 3/8 is the SU(5)-normalisation for ANY complete SU(5)-compatible rep ----------
from fractions import Fraction as Fr
# one SM generation as (dim_color, dim_weak, Y) with multiplicities
gen = [(3,2,Fr(1,6)),(3,1,Fr(-2,3)),(3,1,Fr(1,3)),(1,2,Fr(-1,2)),(1,1,Fr(1)),(1,1,Fr(0))]   # Q,u^c,d^c,L,e^c,nu^c
def traces(fields):
    T3sq = sum(c*(Fr(1,4)*2) for c,wk,Y in fields if wk==2)   # each doublet: Tr T3^2 = 1/2 per colour copy
    Ysq  = sum(c*wk*Y*Y for c,wk,Y in fields)
    return T3sq, Ysq
def s2w(fields):
    T3sq,Ysq = traces(fields); r = T3sq/Ysq; return r/(1+r)   # sin^2 = Tr T3^2 /(Tr T3^2 + Tr Y^2) with g1 normalised as SU(5)
five_bar = [(3,1,Fr(1,3)),(1,2,Fr(-1,2))]; ten = [(3,2,Fr(1,6)),(3,1,Fr(-2,3)),(1,1,Fr(1))]
five = [(3,1,Fr(-1,3)),(1,2,Fr(1,2))]
sixteen = ten+five_bar+[(1,1,Fr(0))]
ten_so10 = five+five_bar
twenty7 = sixteen+ten_so10+[(1,1,Fr(0))]
vals = {"5bar":s2w(five_bar),"10":s2w(ten),"16":s2w(sixteen),"5bar+10 (15 Weyl)":s2w(ten+five_bar),"27":s2w(twenty7)}
print("   sin^2 theta_W at the symmetry point:", vals)
check("sin^2 theta_W = 3/8 for 5bar, 10, 16, 27 alike (non-discriminating)", all(v==Fr(3,8) for v in vals.values()))

# ---------- 7. global form kernel Z6 ----------
# centre elements (w^a I3, (-1)^b I2, e^{i th}) acting trivially on all SM fields with Y in (1/6)Z, colour triality t, weak duality d:
# element acts on a field with (triality t, duality d, hypercharge Y) by w^{a t} (-1)^{b d} e^{i th 6Y}... use th = 2 pi k/6
kernel=[]
for aa in range(3):
    for bb in range(2):
        for k in range(6):
            ok=True
            for c,wk,Y in gen:
                t = 1 if c==3 else 0; d = 1 if wk==2 else 0
                phase = Fr(aa*t,3) + Fr(bb*d,2) + Fr(k,6)*Y*6   # in units of 2 pi... careful Y*6 integer
                # field with colour 3bar has triality 2: encode by sign of Y? use antitriplets: u^c,d^c are 3bar
                if (c,wk,Y) in [(3,1,Fr(-2,3)),(3,1,Fr(1,3))]: phase = Fr(aa*2,3) + Fr(bb*d,2) + Fr(k,6)*Y*6
                if phase.denominator!=1 and (phase - int(phase))!=0: ok=False
            if ok: kernel.append((aa,bb,k))
check("kernel of SU(3)xSU(2)xU(1) -> action on one SM generation is Z6 (order 6)", len(kernel)==6, str(kernel))

# ---------- 8. anomaly uniqueness of Y: depends on whether nu^c is included ----------
# charges on a 16 = 10_{-1} + 5bar_{3} + 1_{-5} under SU(5)xU(1)_chi; psi = +1 on all of the 16
fields16 = [("Q",3,2,Fr(1,6),-1,1),("uc",3,1,Fr(-2,3),-1,1),("ec",1,1,Fr(1),-1,1),("dc",3,1,Fr(1,3),3,1),("L",1,2,Fr(-1,2),3,1),("nuc",1,1,Fr(0),-5,1)]
def anomalies(fields, coeffs):
    a_,b_,c_ = coeffs
    Q = lambda f: a_*f[3]+b_*f[4]+c_*f[5]
    grav = sum(f[1]*f[2]*Q(f) for f in fields)
    su3  = sum(f[2]*Q(f) for f in fields if f[1]==3)          # U(1)-SU(3)^2 (T(3) common factor dropped)
    su2  = sum(f[1]*Q(f) for f in fields if f[2]==2)          # U(1)-SU(2)^2
    cubic= sum(f[1]*f[2]*Q(f)**3 for f in fields)
    return grav, su3, su2, cubic
import sympy
aY,bX,cP = sympy.symbols('a b c')
for label, fl in [("15 Weyl (no nu^c)", [f for f in fields16 if f[0]!="nuc"]), ("16 Weyl (with nu^c)", fields16)]:
    an = anomalies(fl, (aY,bX,cP))
    lin = [sympy.expand(x) for x in an[:3]]
    sol = sympy.solve(lin, [bX,cP], dict=True)
    print(f"   {label}: linear anomalies (grav, SU3^2, SU2^2) = {lin}; solutions for (b,c): {sol}")
check("with 15 Weyl fermions, anomaly freedom forces b=c=0 (Y unique up to scale)  [B864 reproduced]",
      sympy.solve([sympy.expand(x) for x in anomalies([f for f in fields16 if f[0]!='nuc'], (aY,bX,cP))[:3]], [bX,cP]) == {bX:0, cP:0})
an16 = anomalies(fields16,(aY,bX,cP))
check("with the 16 (nu^c included) chi is ALSO anomaly-free, so Y is NOT unique: a 2-dim gaugeable space",
      all(sympy.expand(x).coeff(bX)==0 for x in an16[:3]) and sympy.expand(an16[3]).coeff(bX**3)==0)

# ---------- 9. every Sym^n of SL(2) is self-dual (E65) ----------
def symn(g, n):
    # matrix of g acting on homogeneous polys of degree n in x,y: x-> g00 x + g10 y, y -> g01 x + g11 y  (check homomorphism below)
    x,y = sp.symbols('x y')
    X = g[0,0]*x + g[1,0]*y; Y = g[0,1]*x + g[1,1]*y
    basis = [x**(n-i)*y**i for i in range(n+1)]
    M = sp.zeros(n+1,n+1)
    for j,bj in enumerate(basis):
        img = sp.Poly(sp.expand(bj.subs({x:X,y:Y}, simultaneous=True)), x, y)
        for i,bi in enumerate(basis):
            M[i,j] = img.coeff_monomial(bi)
    return M
g1 = sp.Matrix([[2,1],[1,1]]); g2 = sp.Matrix([[1,3],[1,4]])
hom_ok = all(sp.simplify(symn(g1*g2,n) - symn(g1,n)*symn(g2,n)) == sp.zeros(n+1,n+1) for n in [2,3])
anti_ok = all(sp.simplify(symn(g1*g2,n) - symn(g2,n)*symn(g1,n)) == sp.zeros(n+1,n+1) for n in [2,3])
print("   Sym^n construction is a homomorphism:", hom_ok, " anti-homomorphism:", anti_ok)
# self-duality: exists invariant bilinear form J with S^T J S = J for all S = symn(g) -> solve for J on generators of SL(2,Z)
ok_all=True
for n in range(1,9):
    # dimension of the space of invariant bilinear forms J (S^T J S = J for both generators) via the kernel of a Kronecker system
    S1, S2 = symn(sp.Matrix([[1,1],[0,1]]),n), symn(sp.Matrix([[1,0],[1,1]]),n)
    S1n, S2n = np.array(S1.tolist(),dtype=float), np.array(S2.tolist(),dtype=float)
    d=(n+1)**2
    Ksys = np.vstack([np.kron(S1n.T, S1n.T) - np.eye(d), np.kron(S2n.T, S2n.T) - np.eye(d)])   # vec(S^T J S) = (S^T (x) S^T) vec(J) in row-major convention
    sv = np.linalg.svd(Ksys, compute_uv=False)
    kernel_dim = d - int((sv > 1e-9*sv[0]).sum())
    ok_all = ok_all and kernel_dim==1   # exactly one invariant form: sl2 irreps are self-dual
check("Sym^n (n=1..8) admits an invariant bilinear form (1-dim space) => self-dual, so 27|_{SL2} = 27bar|_{SL2}", ok_all)

# ---------- 10. E8 ⊃ E6 x SU(3): 248 = (78,1)+(1,8)+(27,3)+(27bar,3bar) dimension check only ----------
check("dimension bookkeeping 248 = 78 + 8 + 27*3 + 27*3", 78+8+81+81 == 248)

print("\nSUMMARY:", sum(results.values()), "/", len(results), "checks passed")
