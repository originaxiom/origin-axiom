# Independent check of the web seat's TAU2 word map on Gamma6 = ker(pi1(m004) -> Z/6, a,b -> 1),
# in the SOURCE's own Reidemeister-Schreier convention, against the faithful (holonomy) representation.
import mpmath as mp
mp.mp.dps = 50
W=[2,-1,-2,1]; REL=[1]+W+[-2]+[-x for x in reversed(W)]
def rewrite(word,n,k=0):  # copied verbatim in logic from m6_exact_qz8_engine.py
    o=[]
    for L in word:
        if L==1:
            if k==n-1: o.append(1)
            k=(k+1)%n
        elif L==-1:
            if k==0: o.append(-1)
            k=(k-1)%n
        elif L==2: o.append(2+k); k=(k+1)%n
        else: k=(k-1)%n; o.append(-(2+k))
    return o,k
def mat(a,b,c,d): return mp.matrix([[a,b],[c,d]])
def inv2(M): return mat(M[1,1],-M[0,1],-M[1,0],M[0,0])
def ev(word, gens):
    X=mp.eye(2)
    for L in word: X = X*(gens[L] if L>0 else inv2(gens[-L]))
    return X
def dist(A,B): return max(abs(A[i,j]-B[i,j]) for i in range(2) for j in range(2))
# holonomy: a=[[1,1],[0,1]], b=[[1,0],[z,1]], solve relator a W b^-1 W^-1 = I for z
def relres(z):
    g={1:mat(1,1,0,1),2:mat(1,0,z,1)}
    R=ev(REL,g); return R[0,0]-1
sols=set()
for z0 in [mp.mpc(-0.5,0.8),mp.mpc(-0.5,-0.8),mp.mpc(0.5,0.8),mp.mpc(0.5,-0.8),mp.mpc(1,1),mp.mpc(-1,1)]:
    try:
        z=mp.findroot(relres,z0)
        g={1:mat(1,1,0,1),2:mat(1,0,z,1)}
        if dist(ev(REL,g),mp.eye(2))<1e-30 and abs(mp.im(z))>1e-10: sols.add((mp.nstr(z,20)))
    except Exception as e: pass
print("holonomy parameters z with non-real value solving the relator:", sols)
z=mp.findroot(relres, mp.mpc(0.5,0.866))
a=mat(1,1,0,1); b=mat(1,0,z,1); g={1:a,2:b}
print("z =",mp.nstr(z,20),"| relator residual",mp.nstr(dist(ev(REL,g),mp.eye(2)),5))
n=6
def base(gg):  # word in a,b of cover generator gg (source convention)
    if gg==1: return [1]*6
    k=gg-2; return [1]*k+[2]+([] if k==5 else [-1]*(k+1))
G={gg: ev(base(gg),g) for gg in range(1,8)}
# sanity 1: rewriting base words returns the generator itself
for gg in range(1,8): assert rewrite(base(gg),6,0)==([gg],0), gg
# sanity 2: the six RS relators hold in the restricted holonomy
RELS=[rewrite(REL,n,k)[0] for k in range(n)]
print("RS relators residual under restricted holonomy:", mp.nstr(max(dist(ev(r,G),mp.eye(2)) for r in RELS),5))
TAU2={1:[1],2:[4],3:[5],4:[6],5:[7,-1],6:[1,2,-1],7:[1,3]}
A2=a*a; A2i=inv2(A2)
print("max |rho(TAU2[g]) - a^2 rho(g) a^-2| over g=1..7:", mp.nstr(max(dist(ev(TAU2[gg],G), A2*G[gg]*A2i) for gg in range(1,8)),5))
# relators pushed through TAU2 (substitute each generator by its TAU2 word)
def push(word): 
    out=[]
    for L in word: out += TAU2[L] if L>0 else [-x for x in reversed(TAU2[-L])]
    return out
print("relators after TAU2 substitution, max residual:", mp.nstr(max(dist(ev(push(r),G),mp.eye(2)) for r in RELS),5))
# order 3 modulo inner: TAU2^3 = conjugation by a^6 = x1 (an element of Gamma6)
def comp(w,times):
    for _ in range(times): w=push(w)
    return w
X1=G[1]; X1i=inv2(X1)
print("TAU2^3(g) vs x1 g x1^-1, max residual:", mp.nstr(max(dist(ev(comp([gg],3),G), X1*G[gg]*X1i) for gg in range(1,8)),5))
# symbolic identity (group level, independent of any representation): rewrite(a^2 base(g) a^-2) == TAU2[g]
print("symbolic RS identity a^2 g a^-2 == TAU2[g] for all g:", all(rewrite([1,1]+base(gg)+[-1,-1],6,0)==(TAU2[gg],0) for gg in range(1,8)))
# --- the SM lane's B1378 "corrected" candidate, same test
T2_B1378={1:[1],2:[4],3:[5],4:[6],5:[7],6:[1,2,-1],7:[1,3,-1]}
def push2(word,T):
    out=[]
    for L in word: out += T[L] if L>0 else [-x for x in reversed(T[-L])]
    return out
print("B1378 candidate: max |rho(T[g]) - a^2 rho(g) a^-2|:", mp.nstr(max(dist(ev(T2_B1378[gg],G), A2*G[gg]*A2i) for gg in range(1,8)),5))
print("B1378 candidate: relators after substitution, max residual:", mp.nstr(max(dist(ev(push2(r,T2_B1378),G),mp.eye(2)) for r in RELS),5))
# is a^k b a^-k (B1378 docstring's generator) even in Gamma6? exponent sum mod 6
print("exponent sum of a^k b a^-k mod 6 =", (1)%6, "(nonzero => NOT in the kernel)")
