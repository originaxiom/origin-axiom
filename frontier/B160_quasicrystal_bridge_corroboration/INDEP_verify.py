#!/usr/bin/env python3
"""INDEPENDENT re-derivation of the quasicrystal-bridge headline (verify-don't-trust).

Written from scratch; does NOT import the handoff scripts. Confirms:
 1. Generic Fricke identity  tr[A,B] = x^2+y^2+z^2 - x y z - 2   (x=trA,y=trB,z=trAB),
    so "kappa = tr[A,B]" really IS the Fricke commutator-trace invariant of the
    once-punctured-torus character variety.        [numeric on random SL(2,C), exact-ish]
 2. For the metallic transfer matrices A=[[E-lam,-1],[1,0]], B=[[E,-1],[1,0]]:
       z = tr(AB) = x y - 2   and   tr[A,B] = lambda^2 + 2,  independent of E.   [SYMBOLIC]
 3. Fibonacci trace map x' = 2 x_k x_{k-1} - x_{k-2} conserves the Fricke-Vogt
    invariant I = a^2+b^2+c^2 - 2abc - 1.                                         [SYMBOLIC]
 4. Silver trace map (a,b,c) -> (b, bc-a, (b^2-1)c-ab) conserves Fricke
    kappa = a^2+b^2+c^2 - abc - 2, and matches the matrix recursion M_{k+1}=M_{k-1}M_k^2. [SYMBOLIC+NUM]
 5. kappa = -2  <=>  lambda = 2i (imaginary coupling): the commutator becomes
    PARABOLIC (trace -2, NOT scalar -I) -> the cusp / complete hyperbolic figure-eight point. [SYMBOLIC]
"""
import sympy as sp
ok=True
def chk(n,c,extra=""):
    global ok; ok=ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}"+(f"  {extra}" if extra else ""))

E,lam=sp.symbols('E lambda')
I2=sp.eye(2)

print("== 1) generic Fricke identity tr[A,B] = x^2+y^2+z^2-xyz-2 (random SL(2,C)) ==")
import random
random.seed(1)
allok=True
for _ in range(6):
    def randSL():
        a,b,c=[sp.Rational(random.randint(-4,4),random.randint(1,3)) for _ in range(3)]
        # d so that ad-bc=1: pick a,b,c then d=(1+bc)/a (a!=0)
        while a==0: a=sp.Rational(random.randint(1,4),random.randint(1,3))
        d=(1+b*c)/a
        return sp.Matrix([[a,b],[c,d]])
    A=randSL(); B=randSL()
    x=sp.trace(A); y=sp.trace(B); z=sp.trace(A*B)
    lhs=sp.trace(A*B*A.inv()*B.inv())
    rhs=x**2+y**2+z**2-x*y*z-2
    if sp.simplify(lhs-rhs)!=0: allok=False
chk("tr[A,B] = x^2+y^2+z^2-xyz-2 on 6 random SL(2) pairs", allok)

print("== 2) metallic transfer matrices: z=xy-2, tr[A,B]=lambda^2+2 (E-independent) ==")
A=sp.Matrix([[E-lam,-1],[1,0]]); B=sp.Matrix([[E,-1],[1,0]])
chk("det A=det B=1", sp.simplify(A.det())==1 and sp.simplify(B.det())==1)
x=sp.trace(A); y=sp.trace(B); z=sp.expand(sp.trace(A*B))
chk("z = tr(AB) = x*y - 2", sp.simplify(z-(x*y-2))==0)
kap=sp.simplify(sp.trace(A*B*A.inv()*B.inv()))
chk("tr[A,B] = 2 + lambda^2", sp.simplify(kap-(2+lam**2))==0, extra=f"tr[A,B]={kap}")
chk("tr[A,B] independent of E", E not in kap.free_symbols)
chk("Fricke cubic with z=xy-2 collapses to (x-y)^2+2 = lambda^2+2",
    sp.simplify((x**2+y**2+z**2-x*y*z-2)-(lam**2+2))==0)

print("== 3) Fibonacci trace map conserves Fricke-Vogt I = a^2+b^2+c^2-2abc-1 ==")
a,b,c=sp.symbols('a b c')
# half-trace Fibonacci trace map: (a,b,c) -> (b, c, 2*b*c - a)   [x_{k+1}=2 x_k x_{k-1}-x_{k-2}]
ap,bp,cp = b, c, 2*b*c-a
Ivog=lambda X,Y,Z: X**2+Y**2+Z**2-2*X*Y*Z-1
chk("I(b,c,2bc-a) - I(a,b,c) = 0", sp.simplify(Ivog(ap,bp,cp)-Ivog(a,b,c))==0)

print("== 4) silver trace map conserves Fricke kappa = a^2+b^2+c^2-abc-2 + matches matrices ==")
ap2,bp2,cp2 = b, b*c-a, (b**2-1)*c-a*b
Kfr=lambda X,Y,Z: X**2+Y**2+Z**2-X*Y*Z-2
chk("kappa(silver-map) - kappa = 0 (symbolic)", sp.simplify(Kfr(ap2,bp2,cp2)-Kfr(a,b,c))==0)
# numeric match to matrix recursion M_{k+1}=M_{k-1} M_k^2 with the silver word
import numpy as np
def sig(w): return ''.join('aab' if ch=='a' else 'a' for ch in w)
s={-1:'b',0:'a'}
for k in range(1,8): s[k]=sig(s[k-1])
def Mw(word,Ev,lm):
    M=np.eye(2)
    for ch in word:
        V=lm*(1.0 if ch=='a' else 0.0)
        M=np.array([[Ev-V,-1.0],[1.0,0.0]])@M
    return M
Ev,lm=0.6,1.0
Mn={k:Mw(s[k],Ev,lm) for k in range(-1,7)}
matrec=all(np.allclose(Mn[k+1],Mn[k-1]@Mn[k]@Mn[k]) for k in range(0,5))
chk("silver matrix recursion M_(k+1)=M_(k-1) M_k^2", matrec)
def triple(k): return (np.trace(Mn[k-1]),np.trace(Mn[k]),np.trace(Mn[k-1]@Mn[k]))
mapok=True
for k in range(1,5):
    A_,B_,C_=triple(k); apx,bpx,cpx=triple(k+1)
    if not np.allclose([apx,bpx,cpx],(B_,B_*C_-A_,(B_**2-1)*C_-A_*B_)): mapok=False
chk("silver trace map matches the actual matrices (numeric)", mapok)

print("== 5) kappa=-2 <=> lambda=2i : commutator becomes PARABOLIC (cusp / figure-eight) ==")
# tr[A,B] = 2 + lambda^2 = -2  =>  lambda^2 = -4  =>  lambda = 2i
chk("2 + (2i)^2 = -2", sp.simplify(2+(2*sp.I)**2-(-2))==0)
Ai=A.subs(lam,2*sp.I).subs(E,sp.Rational(1,2)); Bi=B.subs(E,sp.Rational(1,2))
Ci=sp.simplify(Ai*Bi*Ai.inv()*Bi.inv())
chk("commutator trace = -2 at lambda=2i", sp.simplify(sp.trace(Ci)+2)==0)
chk("commutator is NOT scalar -I (genuine parabolic, not central)", sp.simplify(Ci-(-I2))!=sp.zeros(2))
# parabolic <=> trace -2 and (C+I)^2 = 0 (single Jordan block, eigenvalue -1)
chk("(C - (-1)I)^2 = 0  (single Jordan block => parabolic)", sp.simplify((Ci+I2)**2)==sp.zeros(2))

print("\n"+("ALL INDEP CHECKS PASS" if ok else "SOME FAILED"))
import sys; sys.exit(0 if ok else 1)
