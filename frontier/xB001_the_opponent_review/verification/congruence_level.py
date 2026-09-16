# O_3 = Z[w], w^2 = -1-w.  Figure-eight group Gamma = <A,B> in SL(2,O_3)  (Riley's parabolic rep)
#   A = [[1,1],[0,1]],  B = [[1,0],[-w,1]]
# Test congruence: index of image of Gamma in PSL(2,O_3/(n)) == 12 (the geometric index)  <=>  Gamma contains Gamma(n).
import sys
def mk(n):
    def mul(x,y):
        a,b=x; c,d=y
        return ((a*c-b*d)%n, (a*d+b*c-b*d)%n)
    def add(x,y): return ((x[0]+y[0])%n,(x[1]+y[1])%n)
    def neg(x): return ((-x[0])%n,(-x[1])%n)
    return mul,add,neg
def matmul(M,N,mul,add):
    return tuple(add(mul(M[i*2],N[j]), mul(M[i*2+1],N[2+j])) for i in range(2) for j in range(2))
def group_order(gens,n,one,zero,mul,add):
    I=(one,zero,zero,one); S={I}; fr=[I]
    while fr:
        x=fr.pop()
        for g in gens:
            y=matmul(x,g,mul,add)
            if y not in S: S.add(y); fr.append(y)
    return S
def sl2_order(n):
    # |SL(2,R)|, R=Z[w]/n, by counting rows: brute force for small n via |GL|/|R*| is safer -> count directly
    mul,add,neg=mk(n)
    R=[(a,b) for a in range(n) for b in range(n)]
    units=[]
    for u in R:
        for v in R:
            if mul(u,v)==(1%n,0): units.append(u); break
    return len(R),len(units)
for n in [2,4,8]:
    mul,add,neg=mk(n)
    one=(1%n,0); zero=(0,0); w=(0,1%n)
    A=(one,one,zero,one)
    B=(one,zero,neg(w),one)
    H=group_order([A,B],n,one,zero,mul,add)
    # center of SL(2,R): scalars lam*I with lam^2=1
    scal=[(a,b) for a in range(n) for b in range(n) if mul((a,b),(a,b))==one]
    Z=set()
    for s in scal: Z.add((s,zero,zero,s))
    # |H*Z|
    HZ=set()
    for h in H:
        for z in Z: HZ.add(matmul(h,z,mul,add))
    # |SL(2,R)| by generating from elementary matrices over the whole ring (R euclidean -> onto)
    gens=[]
    for r in [(a,b) for a in range(n) for b in range(n)]:
        gens.append((one,r,zero,one)); gens.append((one,zero,r,one))
    G=group_order(gens,n,one,zero,mul,add)
    print(f"n={n}: |SL(2,O/n)|={len(G)}  |center|={len(Z)}  |PSL|={len(G)//len(Z)}  |im Gamma|={len(H)}  |Gamma*Z|={len(HZ)}  PSL-index={len(G)//len(HZ)}")
