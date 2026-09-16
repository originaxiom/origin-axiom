#!/usr/bin/env python3
"""NON-SEMISIMPLE pi_1-MODULES OVER Q(sqrt-3), CHARACTERISTIC ZERO.
No finite group; Maschke does NOT apply (that was my retracted error).
Identical traces, different h^1 -- explicit witnesses for FRESH_EYES Q16 on the
programme's own objects, over the programme's own field.
  m202: traces (2,2)   h^1 = 2 (non-ss)  vs  4 (semisimplification)
  s959: traces (2,2,2) h^1 = 2 (non-ss)  vs  4
And the gap SCALES with dimension (single Jordan blocks, m202):
  dim 2: 2 vs 4   dim 3: 2 vs 6   dim 4: 2 vs 8
SCOPE: these are Jordan-block proxies, NOT the E_6 27, and h^1 is NOT t_0 - r_1.
Shows character-blindness is real and grows; shows NO nonzero index."""
import snappy, sympy as sp, itertools
def h1(M, R, n):
    G=M.fundamental_group(); gens=G.generators(); rel=G.relators(); ng=len(gens)
    def fox(w,var):
        D=sp.zeros(n,n); P=sp.eye(n)
        for ch in w:
            low=ch.lower(); g=R(low)
            if ch.islower():
                if low==var: D=D+P
                P=P*g
            else:
                gi=g.inv()
                if low==var: D=D-P*gi
                P=P*gi
        return sp.expand(D)
    d0=sp.Matrix.vstack(*[R(g)-sp.eye(n) for g in gens])
    d1=sp.Matrix.vstack(*[sp.Matrix.hstack(*[fox(r,v) for v in gens]) for r in rel])
    return (ng*n-d1.rank())-d0.rank()
def run(nm, dims=(2,3,4)):
    w=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
    M=snappy.Manifold(nm); G=M.fundamental_group()
    gens=G.generators(); rel=G.relators(); ng=len(gens)
    V=None
    for vals in itertools.product([sp.Integer(0),sp.Integer(1),w],repeat=ng):
        if all(v==0 for v in vals): continue
        def phi(word,vals=vals):
            s=sp.Integer(0)
            for ch in word: s+=vals[gens.index(ch.lower())]*(1 if ch.islower() else -1)
            return sp.expand(s)
        if all(sp.simplify(phi(r))==0 for r in rel): V=list(vals); break
    if V is None: return
    print(f"{nm}: hom phi -> {[sp.nsimplify(v) for v in V]}")
    for d in dims:
        def U(word,d=d,V=V):
            t=sp.Integer(0)
            for ch in word: t+=V[gens.index(ch.lower())]*(1 if ch.islower() else -1)
            Mx=sp.zeros(d,d)
            for i in range(d):
                for j in range(i,d): Mx[i,j]=t**(j-i)/sp.factorial(j-i)
            return Mx
        def T(word,d=d): return sp.eye(d)
        print(f"   dim {d}: non-semisimple h^1 = {h1(M,U,d)}   semisimplified h^1 = {h1(M,T,d)}")
if __name__=="__main__":
    run('m202'); run('s959',dims=(2,))
