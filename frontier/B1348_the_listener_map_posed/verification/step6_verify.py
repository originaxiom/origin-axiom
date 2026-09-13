"""B1348 step 6 -- verify the load-bearing claims for the verdict."""
import numpy as np
S=np.load("/tmp/b1348_S.npy"); T=np.load("/tmp/b1348_T.npy")
W=[(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
R=T; L=np.linalg.inv(S)@np.linalg.inv(T)@S
i01,i10,i02,i20=W.index((0,1)),W.index((1,0)),W.index((0,2)),W.index((2,0))
F=np.zeros((6,2),dtype=complex); F[i01,0],F[i10,0]=1,-1; F[i02,1],F[i20,1]=1,-1
rest=lambda M: np.linalg.lstsq(F,M@F,rcond=None)[0]
Ro,Lo=rest(R),rest(L)
def psl_key(M,q=7):
    a=(M/np.sqrt(np.linalg.det(M))).flatten()
    f=lambda z:tuple((round(float(x.real),q),round(float(x.imag),q)) for x in z)
    return min(f(a),f(-a))
seen,frontier,mats={psl_key(np.eye(2))},[np.eye(2,dtype=complex)],[np.eye(2,dtype=complex)]
gens=[Ro,Lo,np.linalg.inv(Ro),np.linalg.inv(Lo)]
while frontier:
    nxt=[]
    for M in frontier:
        for g in gens:
            P=M@g;k=psl_key(P)
            if k not in seen: seen.add(k);nxt.append(P);mats.append(P)
    frontier=nxt
f1=np.array([1,0],dtype=complex); f2=np.array([0,1],dtype=complex)
par=lambda a,b,tol=1e-7: abs(abs(np.vdot(a/np.linalg.norm(a), b/np.linalg.norm(b)))-1)<tol

fails=[]
def ck(tag,lab,ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {lab}")
    if not ok: fails.append(tag)

stab=lambda v: sum(1 for M in mats if par(M@v, v))
print("Q1 -- the canonical weight directions are VERTICES")
ck("Q1a", f"|Stab(f1)| = {stab(f1)} = 5, so f1 lies in the 12-orbit", stab(f1)==5)
ck("Q1b", f"|Stab(f2)| = {stab(f2)} = 5, so f2 lies in the 12-orbit too", stab(f2)==5)
ck("Q1c", f"CONTROL: |Stab(f1+f2)| = {stab(np.array([1,1],dtype=complex))} = 1, generic -- so the "
          f"criterion DISCRIMINATES and is not vacuous", stab(np.array([1,1],dtype=complex))==1)

print("\nQ2 -- the stabiliser is cyclic of order 5")
St=[M for M in mats if par(M@f1,f1)]
gen=None
for M in St:
    pw={psl_key(np.linalg.matrix_power(M,k)) for k in range(1,6)}
    if len(pw)==5: gen=M
ck("Q2", "Stab(f1) is CYCLIC of order 5 (a generator exhibited)", gen is not None)

print("\nQ3 -- the orbit of f1 has size 12, and f2 IS IN IT")
def ckey(v,q=6):
    v=v/np.linalg.norm(v); v=v/np.exp(1j*np.angle(v[np.argmax(np.abs(v))]))
    return tuple((round(float(x.real),q),round(float(x.imag),q)) for x in v)
orb={ckey(M@f1) for M in mats}
ck("Q3a", f"|orbit(f1)| = {len(orb)} = 60/5 = 12", len(orb)==12)
hit=[M for M in mats if par(M@f1,f2)]
ck("Q3b", f"there EXISTS g in the group with g.f1 parallel to f2 ({len(hit)} of them) -- so f1 and "
          f"f2 are in the SAME orbit and NO group-stated rule can separate them", len(hit)>0)

print("\nQ4 (AC4') -- the discriminating quantity, with its two-direction witness")
print(f"      quantity: |Stab| on CP^1_odd.   f1 -> 5,   f1+f2 -> 1.   It VARIES.")
ck("Q4", "AC4' satisfied: a computed quantity that provably varies over the codomain, exhibited by "
         "two directions with different values, and Lambda's value (5) is pinned by the "
         "construction rather than chosen", stab(f1)==5 and stab(np.array([1,1],dtype=complex))==1)
print("\nB1348:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
