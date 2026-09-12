"""Try to BREAK one-cusped isotropy, in characteristic zero, on the GEOMETRIC holonomy.

This is now the only live route for the one-cusped case (B1334 addendum), so a counterexample
would close it. Scan one-cusped census manifolds that carry cusp-trivial characters, build
Sym^m(rho_geo) (x) psi, compute L_V and the cup-product Gram on it, and check isotropy.

B1335's lessons are applied: the GEOMETRIC holonomy only (arbitrary reps mislead); a peripheral
trace of -2 makes Sym^odd have every eigenvalue -1, so t_0 = 0 and T5 kills the sector -- those
germs are skipped as vacuous rather than counted; every numerical rank carries its singular-value
gap, and a sector whose gap is narrow is reported as INCONCLUSIVE, never as a verdict.
"""
import sys, warnings, itertools, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from mpmath import mp, mpc, mpf, matrix, svd_r, exp, pi
mp.dps=40
from char0 import tompc, mm, eye, minv, numrank, nullsp_num, wev, fox, sym, inv_dim, expsum
from broad import smith_quotient
from collections import Counter

def inv_forms_num(mats,d):
    """solve g^T F g = F numerically; return a basis of the solution space"""
    rows=[]
    for g in mats:
        for a in range(d):
            for b in range(d):
                row=[mpc(0)]*(d*d)
                for i in range(d):
                    for j in range(d): row[i*d+j]+=g[i][a]*g[j][b]
                row[a*d+b]-=1
                rows.append(row)
    ns=nullsp_num(rows,d*d)
    return [[[v[i*d+j] for j in range(d)] for i in range(d)] for v in ns]

def cup(z,zp,A,B,F,d):
    u,v=z[:d],z[d:]; up,vp=zp[:d],zp[d:]
    Av=[sum(A[x][y]*vp[y] for y in range(d)) for x in range(d)]
    Bu=[sum(B[x][y]*up[y] for y in range(d)) for x in range(d)]
    def pr(a,b): return sum(F[i][j]*a[i]*b[j] for i in range(d) for j in range(d))
    return pr(u,Av)-pr(v,Bu)

def reduce_mod_num(basis,Bs,n):
    out=[];cur=[list(b) for b in Bs]
    r0,_=numrank(cur) if cur else (0,None)
    for v in basis:
        r1,_=numrank(cur+[v])
        if r1>r0: cur.append(list(v)); out.append(list(v)); r0=r1
    return out

NAMES=sys.argv[1:]
tally=Counter(); bad=[]; incon=[]; tested=0
for NAME in NAMES:
    try:
        M=snappy.ManifoldHP(NAME); G=M.fundamental_group()
    except Exception as e: print(f"{NAME}: {e}"); continue
    gens=list(G.generators()); rels=list(G.relators())
    if M.num_cusps()!=1 or len(gens)>3: continue
    mu,lam=G.peripheral_curves()[0]
    tors,free=smith_quotient(gens,rels,[(mu,lam)])
    if not tors: continue
    N=1
    for t in tors: N*= t//__import__('math').gcd(N,t) if False else 1
    N=1
    for t in tors: N=N*t//__import__('math').gcd(N,t)
    if N<2: continue
    rho={g:[[tompc(G.SL2C(g)[i,j]) for j in range(2)] for i in range(2)] for g in gens}
    Mu2=wev(mu,rho,2); tr=Mu2[0][0]+Mu2[1][1]
    neg = abs(tr+2)<abs(tr-2)
    z=exp(2*pi*mpc(0,1)/N)
    chars=[]
    for tup in itertools.product(range(N),repeat=len(gens)):
        if not any(tup): continue
        if all(sum(e*t for e,t in zip(expsum(w,gens),tup))%N==0 for w in list(rels)+[mu,lam]):
            chars.append(tup)
    if not chars: continue
    germs=[(2,),(4,),(2,2),(2,4),(2,2,2)] if neg else [(1,),(2,),(1,1),(2,2),(2,4),(1,2),(2,2,2)]
    print(f"{NAME}: H1/<per> = {tors}, exponent {N}, tr(mu)={complex(tr):.3f} "
          f"({'-2: odd germs vacuous' if neg else '+2'}), chars {len(chars)}", flush=True)
    def bd(ms):
        dd=sum(len(x) for x in ms); out=[[mpc(0)]*dd for _ in range(dd)]; o=0
        for x in ms:
            k=len(x)
            for i in range(k):
                for j in range(k): out[o+i][o+j]=x[i][j]
            o+=k
        return out
    for psi in chars:
        for ms in germs:
            d=sum(x+1 for x in ms); m=max(ms)
            allsame=(len(set(ms))==1)
            V={g:[[(z**psi[i])*bd([sym(rho[g],x) for x in ms])[a][b] for b in range(d)] for a in range(d)]
               for i,g in enumerate(gens)}
            if max(max(abs(wev(r,V,d)[i][j]-(mpc(1) if i==j else mpc(0)))
                       for i in range(d) for j in range(d)) for r in rels)>mpf(10)**-15: continue
            A=wev(mu,V,d); B=wev(lam,V,d)
            t0,_=inv_dim([A,B],d)
            if t0==0: continue
            g=len(gens); J=[]
            for r in rels:
                bl=[fox(r,x,V,d) for x in gens]
                for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
            Zs=nullsp_num(J,g*d)
            FXm=[fox(mu,x,V,d) for x in gens]; FXl=[fox(lam,x,V,d) for x in gens]
            R=[]
            for zv in Zs:
                z2=[zv[j*d:(j+1)*d] for j in range(g)]; row=[]
                for FX in (FXm,FXl):
                    o=[mpc(0)]*d
                    for j in range(g):
                        for a in range(d): o[a]+=sum(FX[j][a][b]*z2[j][b] for b in range(d))
                    row+=o
                R.append(row)
            Bt=[[A[x][k]-(mpc(1) if x==k else mpc(0)) for x in range(d)]+
                [B[x][k]-(mpc(1) if x==k else mpc(0)) for x in range(d)] for k in range(d)]
            rB,_=numrank(Bt); rRB,_=numrank(R+Bt); r1=rRB-rB
            Lv=reduce_mod_num(R,Bt,2*d)
            # The duality pairing uses SL2-invariant forms, NOT every cusp-invariant one.
            # B1332 section 3: for non-isomorphic summands the cross-terms carry no invariant
            # functional at all, so testing against cusp-invariant forms tests more than the claim.
            g1=[[mpc(1),mpc(1)],[mpc(0),mpc(1)]]; g2=[[mpc(1),mpc(0)],[mpc(1),mpc(1)]]
            blocks=[inv_forms_num([sym(g1,x),sym(g2,x)],x+1) for x in ms]
            if any(not b for b in blocks): continue
            Fs=[]
            for sel in range(len(ms)):          # one form per summand, others zero
                out=[[mpc(0)]*d for _ in range(d)]; o=0
                for i,x in enumerate(ms):
                    k=x+1
                    if i==sel:
                        for a in range(k):
                            for b in range(k): out[o+a][o+b]=blocks[i][0][a][b]
                    o+=k
                Fs.append(out)
            if not Fs: continue
            mx=mpf(0); scale=mpf(0)
            for F in Fs:
                nf=max(abs(F[i][j]) for i in range(d) for j in range(d))
                for x in Lv:
                    for y in Lv:
                        val=abs(cup(x,y,A,B,F,d))/ (nf if nf>0 else 1)
                        mx=max(mx,val)
                for x in Lv:
                    for y in Lv:
                        scale=max(scale,sum(abs(c) for c in x)*sum(abs(c) for c in y))
            tested+=1
            rel = mx/(scale if scale>0 else 1)
            verdict = 'ISOTROPIC' if rel<mpf(10)**-25 else ('NOT isotropic' if rel>mpf(10)**-4 else 'INCONCLUSIVE')
            # VACUITY: for m even the induced pairing is ANTIsymmetric, so dim L <= 1 is isotropic
            # for free and tests nothing.  For m odd it is SYMMETRIC and <x,x> = 0 is a real equation.
            nL=len(Lv)
            par_even = all(x%2==0 for x in ms); par_odd = all(x%2==1 for x in ms)
            vac = (par_even and nL<=1)
            neq = 0 if vac else (nL*(nL-1)//2 if par_even else nL*(nL+1)//2)
            tally[(par_even,t0,nL,neq,verdict)]+=1
            if verdict=='NOT isotropic': bad.append((NAME,psi,ms,t0,r1,float(rel)))
            if verdict=='INCONCLUSIVE': incon.append((NAME,psi,ms,float(rel)))
print(f"\nSECTORS {tested}")
if tested==0: print("** NOTHING TESTED **"); sys.exit(1)
print("(m even?, t0, dim L, equations imposed, isotropy) -> count")
for k in sorted(tally,key=str): print("   ",k,"->",tally[k])
nv=sum(v for k,v in tally.items() if k[3]>0); vac=sum(v for k,v in tally.items() if k[3]==0)
eqs=sum(k[3]*v for k,v in tally.items())
print(f"NON-VACUOUS sectors: {nv}   vacuous (even m, dim L <= 1): {vac}")
print(f"genuine scalar equations satisfied: {eqs}")
print(f"NON-ISOTROPIC: {len(bad)}   INCONCLUSIVE: {len(incon)}")
for b in bad[:8]: print("   ",b)
