#!/usr/bin/env python3
"""m202 and m003: is there ANY parabolic generating pair? The meridian ones fail the
abelianisation test for m202 (both) and for m003's (mer,b). Other parabolics exist:
the second cusp's meridian, the longitudes, and products -- check them."""
import numpy as np, snappy
from math import gcd

def m2(S): return np.array([[complex(S[0,0]),complex(S[0,1])],[complex(S[1,0]),complex(S[1,1])]],dtype=complex)
def tr(M): return M[0,0]+M[1,1]
def inv2(M):
    d=M[0,0]*M[1,1]-M[0,1]*M[1,0]
    return np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]],dtype=complex)/d
def kap(G,wa,wb):
    A,B=m2(G.SL2C(wa)),m2(G.SL2C(wb)); return complex(tr(A@B@inv2(A)@inv2(B)))
def exps(w):
    e=[0,0]
    for ch in w:
        i=0 if ch.lower()=='a' else 1
        e[i]+= 1 if ch.islower() else -1
    return e
def idx(rows):
    g=0
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            g=gcd(g,abs(int(rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0])))
    return g

for n,km2 in (("m003",4.0),("m202",7.0)):
    M=snappy.Manifold(n); G=M.fundamental_group(); nc=M.num_cusps()
    rels=[exps(r) for r in G.relators()]
    full=idx([[1,0],[0,1]]+rels)
    print("="*84); print(f"{n}   cusps={nc}   H_1={M.homology()}   |K-2| target={km2}"); print("="*84)
    cands={}
    for c in range(nc):
        cands[f"meridian({c})"]=G.meridian(c)
        cands[f"longitude({c})"]=G.longitude(c)
    for lab,w in list(cands.items()):
        if not w: continue
        try: t=complex(tr(m2(G.SL2C(w))))
        except Exception: continue
        par=abs(abs(t)-2)<1e-6
        e=exps(w)
        line=f"  {lab:>13} = {w!r:<14} |tr|={abs(t):.6f} {'PARABOLIC' if par else 'not parabolic':<14}"
        ok=[]
        for other,eo in (("a",[1,0]),("b",[0,1])):
            i2=idx([e,eo]+rels)
            gen_ok = (i2==full)
            if gen_ok and par:
                k=abs(kap(G,w,other)-2)
                ok.append(f"({lab[:3]},{other}) ab-OK kappa={k:.6f}{' MATCH' if abs(k-km2)<1e-6 else ' DIFFERS'}")
            elif par:
                ok.append(f"({lab[:3]},{other}) abelianisation FORBIDS")
        print(line)
        for o in ok: print(f"                 {o}")
