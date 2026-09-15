#!/usr/bin/env python3
"""MASTER VERIFIER --- every surviving claim of the session, re-derived from scratch.
No cached JSON is read. Each claim carries its own control. Exit 0 only if every claim
PASSES and every control behaves as declared."""
import sympy as sp, snappy, itertools, math, json, sys, time
R_=[]; t0=time.time()
def rec(tag, claim, ok, detail=""):
    R_.append((tag, claim, ok, detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag:14s} {claim:52s} {detail}", flush=True)

print("="*104); print("STAGE A --- algebra (F5, G1, G2, Galois)"); print("="*104)
# ---- F5: the tick contains the swap
R=sp.Matrix([[1,1],[0,1]]); L=sp.Matrix([[1,0],[1,1]]); S=sp.Matrix([[0,1],[1,0]]); M=sp.Matrix([[1,1],[1,0]])
rec("F5.1","M = R*S  (tick = twist x swap)", (R*S)==M, f"det M = {M.det()}")
rec("F5.2","S*R*S = L (swap exchanges R and L)", (S*R*S)==L and (S*L*S)==R)
rec("F5.3","M^2 = RL", (M*M)==R*L, f"tr = {(M*M).trace()}")
def swapw(w): return w.replace('R','x').replace('L','R').replace('x','L')
def cyc(w): return {w[i:]+w[:i] for i in range(len(w))}
def word(w):
    A=sp.eye(2)
    for c in w: A=A*(R if c=='R' else L)
    return A
ok=all(word(X+swapw(X))==(word(X)*S)**2 for X in ['R','RR','RL','RRL','RLL','RRLL'])
rec("F5.4","(X*S)^2 has word X.swap(X)", ok, "checked 6 X's, matrix identity")
# ---- G1: kappa identity + Casimir
x,y,z=sp.symbols('x y z'); KAP=x**2+y**2+z**2-x*y*z-2
a1,a2,a3,b1,b2,b3=sp.symbols('a1 a2 a3 b1 b2 b3')
A=sp.Matrix([[a1,a2],[a3,(1+a2*a3)/a1]]); B=sp.Matrix([[b1,b2],[b3,(1+b2*b3)/b1]])
Ai=sp.Matrix([[A[1,1],-a2],[-a3,a1]]); Bi=sp.Matrix([[B[1,1],-b2],[-b3,b1]])
X_,Y_,Z_=sp.trace(A),sp.trace(B),sp.trace(A*B)
rec("G1.1","tr[a,b] = x^2+y^2+z^2-xyz-2",
    sp.simplify(sp.together(sp.trace(A*B*Ai*Bi)-(X_**2+Y_**2+Z_**2-X_*Y_*Z_-2)))==0)
def gold(f,g):
    bxy,byz,bzx=2*z-x*y,2*x-y*z,2*y-x*z
    fx,fy,fz=[sp.diff(f,v) for v in (x,y,z)]; gx,gy,gz=[sp.diff(g,v) for v in (x,y,z)]
    return sp.expand((fx*gy-fy*gx)*bxy+(fy*gz-fz*gy)*byz+(fz*gx-fx*gz)*bzx)
rec("G1.2","kappa is the Goldman Casimir", all(sp.simplify(gold(KAP,v))==0 for v in (x,y,z)))
dec=x**2*y+z**3-3*x*z
rec("G1.3","C-NULL: decoy cubic NOT central", not all(sp.simplify(gold(dec,v))==0 for v in (x,y,z)))
rec("G1.4","structure fns = grad(kappa) (Nambu)",
    all(sp.simplify(a-b)==0 for a,b in [(2*z-x*y,sp.diff(KAP,z)),(2*x-y*z,sp.diff(KAP,x)),(2*y-x*z,sp.diff(KAP,y))]))
# ---- G2: multiplier == det on Aut(F2) generators
def sub(T,e): return sp.expand(e.subs({x:T[0],y:T[1],z:T[2]},simultaneous=True))
def mult(T):
    out=[]
    for (u,v),st in [((T[0],T[1]),2*z-x*y),((T[1],T[2]),2*x-y*z),((T[2],T[0]),2*y-x*z)]:
        lhs,rhs=gold(u,v),sub(T,st)
        if sp.simplify(rhs)==0: return None
        q=sp.simplify(sp.cancel(lhs/rhs))
        if not q.is_number: return None
        out.append(q)
    return out[0] if len(set(out))==1 else None
gens={'P':((y,x,z),-1),'I':((x,y,x*y-z),-1),'U':((z,y,y*z-x),1)}
rec("G2.1","Goldman multiplier = det on Aut(F2) gens", all(mult(T)==d for T,d in gens.values()),
    " ".join(f"{k}:{mult(T)}" for k,(T,d) in gens.items()))
rec("G2.2","C-ALIVE: identity multiplier = +1", mult((x,y,z))==1)
S3_=(z,z,z**2-2)
rec("G2.3","stratum 4 image lies in {kappa=2}", sp.simplify(sub(S3_,KAP)-2)==0)
# ---- Galois separation (Lemma A)
n=12; zt=sp.exp(2*sp.pi*sp.I/n)
units=[k for k in range(1,n) if sp.gcd(k,n)==1]
both=[k for k in units
      if sp.simplify(zt**((4*k)%n)-zt**8)==0 and sp.simplify((zt**((4*k)%n)-zt**((8*k)%n))-(zt**4-zt**8))==0]
rec("LemA.1","no sigma inverts chi AND fixes Q(sqrt-3)", len(both)==0, f"candidates={units}")
rec("LemA.2","C-ALIVE: some sigma inverts chi",
    any(sp.simplify(zt**((4*k)%n)-zt**8)==0 for k in units))

print("\n"+"="*104); print("STAGE B --- SnapPy structural (F4, F5 scale, the non-bundle negative)"); print("="*104)
G=snappy.Manifold('m000')
rec("F4.1","Gieseking cusp is a Klein bottle", G.cusp_info()[0]['topology']=='Klein bottle cusp')
D=G.orientation_cover()
rec("F4.2","its orientation cover has a torus cusp", D.cusp_info()[0]['topology']=='torus cusp')
rec("F4.3","cover is isometric to m004", D.is_isometric_to(snappy.Manifold('m004')))
def det2(g):
    m=g.cusp_maps()[0]; return int(m[0,0]*m[1,1]-m[0,1]*m[1,0])
isos=snappy.Manifold('m004').symmetry_group().isometries()
mats={(int(g.cusp_maps()[0][0,0]),int(g.cusp_maps()[0][0,1]),
       int(g.cusp_maps()[0][1,0]),int(g.cusp_maps()[0][1,1])) for g in isos}
rec("F4.4","m004 realises diag(1,-1) (B286 slope flip)", (1,0,0,-1) in mats, f"{len(mats)} distinct cusp actions")
# F5 at scale
dbl=[]; 
for k in range(1,5):
    for t in itertools.product('RL',repeat=k):
        X=''.join(t); W=X+swapw(X)
        if 'R' in W and 'L' in W:
            dbl.append((W, snappy.Manifold('b++'+W).symmetry_group().is_amphicheiral()))
rec("F5.5","every double tick is amphichiral", all(a for _,a in dbl), f"{len(dbl)} tested, {sum(1 for _,a in dbl if a)} amph")
dbw={w for w,_ in dbl}; oth=[]
for k in range(2,7):
    for t in itertools.product('RL',repeat=k):
        W=''.join(t)
        if 'R' not in W or 'L' not in W: continue
        if any(v in dbw for v in cyc(W)): continue
        try: oth.append((W, snappy.Manifold('b++'+W).symmetry_group().is_amphicheiral()))
        except Exception: pass
ch=sum(1 for _,a in oth if not a)
rec("F5.6","C-NULL: chirality EXISTS off the double-tick locus", ch>0, f"{ch}/{len(oth)} chiral")
rec("F5.7","tr(W)-2 a perfect square <=> double tick",
    all((lambda tr,d: (math.isqrt(tr-2)**2==tr-2)==d)(int(word(w).trace()), any(v in dbw for v in cyc(w)))
        for w in ['RL','RRL','RRLL','RLRL','RRRL','RRRLL','RRRLLL','RRLLLR','RRLRL','RLLR']))
# the negative: B1330's objects are NOT punctured-torus bundles
neg=True
for nm,W in [('s958','RLRLRL'),('v2873','RLRLRL'),('t12833','RLRLRLRL'),('t12835','RLRLRLRL')]:
    Mt=snappy.Manifold(nm)
    for s in ['b++','b+-','b--','b-+']:
        if Mt.is_isometric_to(snappy.Manifold(s+W)): neg=False
rec("NEG.1","B1330's four are NOT those bundles", neg, "16 isometry tests, none isometric")
rec("NEG.2","TRAP: s958 and s961 share volume, differ",
    abs(float(snappy.Manifold('s958').volume())-float(snappy.Manifold('s961').volume()))<1e-9
    and not snappy.Manifold('s958').is_isometric_to(snappy.Manifold('s961')))
json.dump([(t,c,o,d) for t,c,o,d in R_], open('../out/stageAB.json','w'))
print(f"\n  stage A+B elapsed {time.time()-t0:.0f}s")
fails=[r for r in R_ if not r[2]]
print(f"\n  A+B: {len(R_)-len(fails)}/{len(R_)} PASS")
sys.exit(1 if fails else 0)
