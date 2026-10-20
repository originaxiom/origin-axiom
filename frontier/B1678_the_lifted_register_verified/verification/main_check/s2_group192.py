from lib import *
import itertools,sys
# J in H? find u with J = I_u o Delta^2
Delta=L@Ri@L; D2=Delta@Delta
Jinv=Aut((-1,),(-2,))
found=None
import itertools
letters=[1,2,-1,-2]
cands=[()]
for n in range(1,5):
    cands+= [w for w in itertools.product(letters,repeat=n) if red(w)==w]
for u in cands:
    Iu=Aut(red(u+(1,)+inv(u)),red(u+(2,)+inv(u)))
    if (Iu@D2).key()==Jinv.key(): found=u;break
print("J = I_u o Delta^2 with u =",found)
# closure
def key(M): return tuple(np.round(M.flatten(),5).view(float).round(4)+0.0)
def closure(mats,limit=5000):
    n=mats[0].shape[0]
    I=np.eye(n,dtype=complex)
    seen={key(I):I};frontier=[I]
    while frontier:
        new=[]
        for M in frontier:
            for G in mats:
                N=M@G;k=key(N)
                if k not in seen:
                    seen[k]=N;new.append(N)
                    if len(seen)>limit: return len(seen)
        frontier=new
    return len(seen)
def blk(*Ms):
    n=sum(m.shape[0] for m in Ms);B=np.zeros((n,n),dtype=complex);i=0
    for m in Ms:
        B[i:i+m.shape[0],i:i+m.shape[0]]=m;i+=m.shape[0]
    return B
allg=['L','Lb','R','Rb']
def Uleft(e): # left action on V: U_e = D_{e^-1}
    return np.linalg.inv(Vrep(e))   # D is a rep of opposite group => D_{e^-1}=D_e^{-1}
for label,gl in [("L,R only",['L','R']),("four wordings",allg)]:
    es=[GENS[n] for n in gl]
    Vs=[Uleft(e) for e in es]; Ws=[Wrep(e) for e in es]
    print(label,": |V image|=",closure(Vs)," |W image|=",closure(Ws)," |joint V+W|=",closure([blk(v,w) for v,w in zip(Vs,Ws)]))
# joint including inverses explicitly not needed in finite group
# Also image with central eps added (E includes eps): is -I in image?
es=[GENS[n] for n in allg]
Vs=[Uleft(e) for e in es]; Ws=[Wrep(e) for e in es]
J=[blk(v,w) for v,w in zip(Vs,Ws)]
print("joint image contains eps (= -I on V, -I? on W)?")
