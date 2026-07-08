#!/usr/bin/env python3
"""B485 v2 - metallic A-poly, fraction-free elimination. Validate m=1 vs known fig-8."""
import sympy as sp
x,b1,b2,b3,b4,p,q,r,s,Mv,Lv = sp.symbols('x b1 b2 b3 b4 p q r s Mv Lv')
a=sp.Matrix([[x,-1],[1,0]]); b=sp.Matrix([[b1,b2],[b3,b4]])
Lam=sp.Matrix([[p,q],[r,s]])
def apply_R(w):
    o=[]
    for ch in w: o+= {'a':['a'],'A':['A'],'b':['a','b'],'B':['B','A']}[ch]
    return o
def apply_L(w):
    o=[]
    for ch in w: o+= {'a':['a','b'],'A':['B','A'],'b':['b'],'B':['B']}[ch]
    return o
def phi_word(m):
    fa,fb=['a'],['b']
    for _ in range(m): fa,fb=apply_L(fa),apply_L(fb)
    for _ in range(m): fa,fb=apply_R(fa),apply_R(fb)
    return fa,fb
gen={'a':a,'A':a.adjugate(),'b':b,'B':b.adjugate()}  # adjugate = inverse for det1
def wmat(w):
    M=sp.eye(2)
    for ch in w: M=M*gen[ch]
    return M
def run(m, timeout_note=""):
    fa,fb=phi_word(m); Ma,Mb=wmat(fa),wmat(fb)
    eqs=[]
    for (G,PhiG) in [(a,Ma),(b,Mb)]:
        E=Lam*G-PhiG*Lam
        eqs += [sp.expand(E[i,j]) for i in range(2) for j in range(2)]
    eqs.append(b1+b4-sp.symbols('y'))  # keep y? no - eliminate; instead fix det b
    eqs=[e for e in eqs if e!=b1+b4-sp.symbols('y')]
    eqs.append(b1*b4-b2*b3-1)          # det b = 1
    eqs.append(p*s-q*r-1)              # det Lam = 1
    comm=sp.expand(sp.trace(a*b*a.adjugate()*b.adjugate()))
    eqs.append(sp.expand(Mv*Mv - comm*Mv + 1))   # M+1/M = kappa
    eqs.append(sp.expand(Lv*Lv - (p+s)*Lv + 1))  # L+1/L = tr Lam
    G=sp.groebner(eqs, x,b1,b2,b3,b4,p,q,r,s,Mv,Lv, order='lex')
    ap=[g for g in G.exprs if g.free_symbols<={Mv,Lv} and g.free_symbols]
    print(f"m={m}: phi(a)={''.join(fa)[:30]} phi(b)={''.join(fb)[:30]}", flush=True)
    print(f"  A-poly (Mv,Lv) factors:", flush=True)
    for g in ap[:2]:
        print("   ", sp.factor(g), flush=True)
    if not ap: print("   (elimination gave no pure Mv,Lv relation in budget)", flush=True)
run(1)
print("M1 DONE", flush=True)
