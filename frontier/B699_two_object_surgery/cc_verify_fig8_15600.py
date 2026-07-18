import snappy
from sage.all import GF, matrix
M = snappy.Manifold('m004')
G = M.fundamental_group()
def tr(w):
    X=G.SL2C(w); return complex(X[0][0]+X[1][1])
a,b=G.generators()
def rec(z, tol=1e-6):
    x=z.real; y=z.imag/(3**0.5)
    for P in range(-8,9):
        for Qn in range(-8,9):
            if abs(x-P/2)<tol and abs(y-Qn/2)<tol: return (P,Qn)
    return None
tA=rec(tr(a)); tB=rec(tr(b)); tAB=rec(tr(a+b))
print("fig-8 tr A,B,AB = (P+Q sqrt-3)/2:", tA,tB,tAB)
F25=GF(25,'g')                     # Conway (works with libgap)
# find r in F25 with r^2 = 2 (=-3 mod 5), i.e. r = sqrt(-3)
r=[x for x in F25 if x*x==F25(2)][0]
half=F25(3)                        # 1/2 in F_5
def red(PQ):
    P,Qn=PQ; return half*(F25(P)+F25(Qn)*r)
ta,tb,tab=red(tA),red(tB),red(tAB)
A=matrix(F25,[[ta,-1],[1,0]])
done=False
for p in F25:
    s=tb-p
    for q in F25:
        rr=ta*p+q-tab
        if p*s-q*rr==1:
            B=matrix(F25,[[p,q],[rr,s]])
            # BFS closure (avoid GAP): generate the group
            from itertools import product
            def imm(m):
                m2=matrix(F25,m); m2.set_immutable(); return m2
            I=imm([[1,0],[0,1]])
            gensm=[imm(A),imm(B),imm(A.inverse()),imm(B.inverse())]
            grp={I}; frontier=[I]
            while frontier:
                x=frontier.pop()
                for g in gensm:
                    y=imm(x*g)
                    if y not in grp:
                        grp.add(y); frontier.append(y)
                if len(grp)>16000: break
            print(f"  |<A,B>| (BFS) = {len(grp)}   (|SL(2,25)|=15600, |2I|=120)")
            print("  => fig-8 RAW holonomy FILLS SL(2,F_25), NOT 2I" if len(grp)==15600 else f"  order {len(grp)}")
            done=True; break
    if done: break
