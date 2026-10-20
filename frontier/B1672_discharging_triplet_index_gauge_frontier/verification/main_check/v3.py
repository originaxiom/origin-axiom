import numpy as np, itertools
exec(open("v1.py").read().split("# ---- 1.")[0])
red=om.red; winv=om.inv
def app(f,w): return om.apply(f,w)
def comp(f,g): return om.compose(f,g)
Lab={"a":"a","b":"ab"};Lba={"a":"a","b":"ba"};Rab={"a":"ab","b":"b"};Rba={"a":"ba","b":"b"}
def inverse_of(f):
    # shears' inverses explicitly
    return {"Lab":{"a":"a","b":"Ab"},"Lba":{"a":"a","b":"Ba"}}  # not used
gens={"Lab":Lab,"Lba":Lba,"Rab":Rab,"Rba":Rba,
      "lab":{"a":"a","b":"Ab"},"lba":{"a":"a","b":"bA"},"rab":{"a":"aB","b":"b"},"rba":{"a":"Ba","b":"b"}}
# fix: inverse of (a,b)->(a,ba) is b -> a^-1 b? (a,ba): b' = ba -> b = b' a^-1 -> "bA"? compute by check
def ident(f): return f=={"a":"a","b":"b"}
ginv={}
for n,f in gens.items():
    for m,g in gens.items():
        if ident(comp(f,g)) and ident(comp(g,f)): ginv[n]=m
print("inverse pairs",ginv)
M={}
for n,f in gens.items():
    Mx=om.M_of(f); M[n]=Mx
    print(n,"lift found",Mx is not None)
TB=cp.TB
# SL2Z images and generation of Inn
def h1(f): return om.h1(f)
print("det H1 of each:",[round(np.linalg.det(h1(f))) for f in gens.values()])
# well-definedness test
zeta=np.exp(1j*np.pi/4)
twist={"Lab":zeta,"Lba":zeta,"Rab":1/zeta,"Rba":1/zeta,"lab":1/zeta,"lba":1/zeta,"rab":zeta,"rba":zeta}
def key(f): return (f["a"],f["b"])
def run(N,restrict=None):
    seen={}  # key -> (matrix_untw, matrix_tw, word)
    bad_un=0; bad_tw=0; total=0
    frontier=[({"a":"a","b":"b"},np.eye(6,dtype=complex),1.0+0j,())]
    seen[key(frontier[0][0])]=[(frontier[0][1],frontier[0][2])]
    badex=None
    for L in range(N):
        nxt=[]
        for f,Mx,t,wd in frontier:
            for n,g in gens.items():
                if wd and ginv[wd[-1]]==n: continue
                f2=comp(f,g); M2=Mx@M[n]; t2=t*twist[n]
                k=key(f2)
                if len(f2["a"])>40 or len(f2["b"])>40: continue
                total+=1
                if k in seen:
                    for (Mo,to) in seen[k][:1]:
                        # compare as matrices on V (6x6), untwisted and twisted
                        if not np.allclose(Mo,M2,atol=1e-7): bad_un+=1
                        if not np.allclose(to*Mo,t2*M2,atol=1e-7) and not np.allclose(to*Mo[:,:],t2*M2,atol=1e-7):
                            bad_tw+=1
                            if badex is None: badex=(wd+(n,),k)
                else:
                    seen[k]=[(M2,t2)]
                    nxt.append((f2,M2,t2,wd+(n,)))
        frontier=nxt
    return total,len(seen),bad_un,bad_tw,badex
for N in (7,):
    print("N",N,run(N),flush=True)
