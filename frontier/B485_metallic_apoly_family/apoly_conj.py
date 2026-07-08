#!/usr/bin/env python3
"""B485 - metallic A-polynomial via the conjugation method (exact sympy).
Once-punctured torus bundle, monodromy phi = R^m L^m acting on F2=<a,b>:
  R: a->a, b->ab ;  L: a->ab, b->b.
Rep rho: a=[[x,-1],[1,0]] (tr x), b=[[0,t],[-1/t,y]] (tr y), z=tr(ab).
Extend to bundle: exists Lam (=rho(monodromy longitude)) with Lam rho(g) Lam^-1 = rho(phi(g)).
Meridian M: tr rho([a,b]) = kappa = M+1/M. Longitude L: tr Lam = L+1/L.
Eliminate internal params -> A(M,L). Report A-poly + genus per m."""
import sympy as sp

x,y,t = sp.symbols('x y t')
a = sp.Matrix([[x,-1],[1,0]])
b = sp.Matrix([[0,t],[-1/t,y]])
Ai = a.inv(); Bi = b.inv()
gen = {'a':a,'A':Ai,'b':b,'B':Bi}

def phi_word(m):
    # phi = R^m L^m; R: a->a,b->ab ; L: a->ab,b->b. Compose on the two generators.
    # represent images as words (strings) in a,b
    def apply_R(w):
        out=''
        for ch in w:
            if ch=='a': out+='a'
            elif ch=='A': out+='A'
            elif ch=='b': out+='ab'
            elif ch=='B': out+='BA'
        return out
    def apply_L(w):
        out=''
        for ch in w:
            if ch=='a': out+='ab'
            elif ch=='A': out+='BA'
            elif ch=='b': out+='b'
            elif ch=='B': out+='B'
        return out
    fa,fb='a','b'
    for _ in range(m): fa,fb=apply_L(fa),apply_L(fb)
    for _ in range(m): fa,fb=apply_R(fa),apply_R(fb)
    return fa,fb

def wmat(w):
    M=sp.eye(2)
    for ch in w: M=M*gen[ch]
    return M

def apoly(m):
    fa,fb=phi_word(m)
    Ma,Mb=wmat(fa),wmat(fb)
    # Lam unknown SL2: [[p,q],[r,s]], ps-qr=1
    p,q,r,s,Mv,Lv=sp.symbols('p q r s Mv Lv')
    Lam=sp.Matrix([[p,q],[r,s]])
    eqs=[]
    for (G,PhiG) in [(a,Ma),(b,Mb)]:
        E=sp.expand( Lam*G - PhiG*Lam )   # Lam G = phi(G) Lam
        for i in range(2):
            for j in range(2):
                eqs.append(sp.together(E[i,j]))
    eqs=[sp.numer(e) for e in eqs]
    eqs.append(p*s-q*r-1)
    # meridian kappa = tr[a,b]
    comm=a*b*Ai*Bi
    kappa=sp.expand(sp.trace(comm))
    eqs.append(sp.numer(sp.together(kappa-(Mv+1/Mv))))
    eqs.append(p+s-(Lv+1/Lv))   # tr Lam = L+1/L
    G=sp.groebner(eqs,[x,y,t,p,q,r,s], Mv,Lv, order='lex')
    apolys=[g for g in G.exprs if g.free_symbols<= {Mv,Lv}]
    print(f"m={m}: phi(a)={fa[:40]}, phi(b)={fb[:40]}", flush=True)
    print(f"  A-poly factors (in Mv,Lv): {[sp.factor(ap) for ap in apolys][:3]}", flush=True)
    return apolys

for m in (1,2):
    apoly(m)
print("CONJ APOLY DONE", flush=True)
