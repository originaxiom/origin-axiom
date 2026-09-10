import snappy, warnings, itertools, sys; warnings.filterwarnings("ignore")
from index_lib import *

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def order3_chars(gens,rels,mu,lam):
    """psi in (Z/3)^g killing all relators and mu,lambda; psi != 0"""
    g=len(gens); rows=[expsum(r,gens) for r in rels]+[expsum(mu,gens),expsum(lam,gens)]
    rows=[[x%3 for x in r] for r in rows]
    ns=nullspace(rows,3,g)
    out=set()
    for coeffs in itertools.product(range(3),repeat=len(ns)):
        v=[0]*g
        for c,b in zip(coeffs,ns):
            for i in range(g): v[i]=(v[i]+c*b[i])%3
        if any(v): out.add(tuple(v))
    return sorted(out)

def sl2p_reps(gens,rels,mu,p,limit=None):
    """all rho: pi_1 -> SL(2,p) with rho(mu) parabolic non-trivial"""
    els=[(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
    out=[]
    for combo in itertools.product(els,repeat=len(gens)):
        rho={g:[[m[0],m[1]],[m[2],m[3]]] for g,m in zip(gens,combo)}
        if not all(word_eval(r,rho,p,2)==eye(2) for r in rels): continue
        Mu=word_eval(mu,rho,p,2)
        if Mu==eye(2): continue
        if (Mu[0][0]+Mu[1][1])%p != 2%p: continue      # parabolic: trace 2
        out.append(rho)
        if limit and len(out)>=limit: break
    return out

def sym_power(A,m,p):
    """Sym^m of a 2x2 matrix, on basis x^m, x^(m-1)y, ..., y^m"""
    d=m+1; из=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    from math import comb
    for j in range(d):        # image of basis vector x^(m-j) y^j
        # (a x + c y)^(m-j) (b x + dd y)^j   -> collect
        coeffs=[0]*d
        for s in range(m-j+1):
            for t in range(j+1):
                cf = comb(m-j,s)*pow(a,m-j-s,p)*pow(c,s,p) * comb(j,t)*pow(b,j-t,p)*pow(dd,t,p)
                coeffs[s+t]=(coeffs[s+t]+cf)%p
        for i in range(d): из[i][j]=coeffs[i]
    return из

def run(name,p=7,m=1,verbose=True):
    M=snappy.Manifold(name); G=M.fundamental_group()
    gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
    reps=sl2p_reps(gens,rels,mu,p,limit=40)
    chars=order3_chars(gens,rels,mu,lam)
    if verbose: print(f"{name}: gens={len(gens)} reps(parabolic)={len(reps)} order-3 cusp-trivial chars={len(chars)}")
    om=[x for x in range(2,p) if pow(x,3,p)==1][0]     # element of order 3 in F_p^*
    results=[]
    for rho in reps:
        base={g:sym_power(rho[g],m,p) for g in gens}
        d=m+1
        for psi in chars:
            V ={g:scal(pow(om,psi[i],p),base[g],p) for i,g in enumerate(gens)}
            Vd={g:scal(pow(om,(-psi[i])%3,p),base[g],p) for i,g in enumerate(gens)}
            A=analyse(gens,rels,mu,lam,V ,p,d)
            B=analyse(gens,rels,mu,lam,Vd,p,d)
            results.append((A,B))
    return results
