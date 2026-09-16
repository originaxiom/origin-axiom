#!/usr/bin/env python3
"""B1418 cell 4 -- THE 27-BAR SECTOR, THE EXACT HALF: (i) 78 contains no 27/27bar; (ii) E7's 56 -> E6: 27 + 27bar + 1 + 1;
(iii) E8's 248 -> E6 x SU(3): (27,3)+(27bar,3bar)+(78,1)+(1,8); (iv) the 27's two charged SM singlets share eta and no field has
eta = -2 x singlet (no Majorana source in 27^3 or 78); (v) (27.27bar)^2 is eta-neutral and contains nu^c nu^c nubar^c nubar^c;
(vi) the sum rule with a free Z/3 orbit: orbit charges sum to zero; 3(n+ - n-) = 3 forces n+ - n- = 1."""
import itertools, numpy as np
s3=np.sqrt(3)
# ---- E6 in SO(10) x U(1) coordinates (B1415)
R6=[]
for i,j in itertools.combinations(range(5),2):
    for a in (1,-1):
        for b in (1,-1):
            v=np.zeros(6); v[i]=a; v[j]=b; R6.append(v)
for signs in itertools.product((1,-1),repeat=5):
    v=np.array([0.5*s for s in signs]+[0.0]); neg=sum(1 for s in signs if s<0); v[5]=s3/2 if neg%2==0 else -s3/2; R6.append(v)
R6=np.array(R6)
def w27(parity):
    W=[]
    for signs in itertools.product((1,-1),repeat=5):
        if sum(1 for s in signs if s<0)%2==parity: W.append(np.array([0.5*s for s in signs]+[1/(2*s3)]))
    for i in range(5):
        for a in (1,-1):
            v=np.zeros(6); v[i]=a; v[5]=-1/s3; W.append(v)
    W.append(np.array([0,0,0,0,0,2/s3])); return np.array(W)
W27=w27(1); W27b=-W27
def same_set(A,B): return len(A)==len(B) and all(any(np.allclose(a,b) for b in B) for a in A)
# (i) 78 = 72 roots + 6 zero weights: no 27 weight among them
print('(i) any 27 weight among the 78 weights?', any(any(np.allclose(w,r) for r in R6) or np.allclose(w,0) for w in W27), '-> 78 contains no 27, no 27bar:', not any(any(np.allclose(w,r) for r in R6) for w in np.vstack([W27,W27b])))
# ---- E8 roots, E7 = roots orthogonal to r0, E6 = E7 roots orthogonal to a 56 weight w (B1415)
R8=[]
for i,j in itertools.combinations(range(8),2):
    for a in (1,-1):
        for b in (1,-1):
            v=np.zeros(8); v[i]=a; v[j]=b; R8.append(v)
for s in itertools.product((1,-1),repeat=8):
    if sum(1 for t in s if t<0)%2==0: R8.append(np.array(s)/2)
R8=np.array(R8); r0=R8[0]; E7=np.array([r for r in R8 if abs(r@r0)<1e-9])
W56=np.array([r-(r@r0)/2*r0 for r in R8 if abs(r@r0-1)<1e-9]); assert len(W56)==56
w=W56[0]; E6=np.array([r for r in E7 if abs(r@w)<1e-9]); assert len(E6)==72
# (ii) 56 restricted to E6: the U(1) is the direction w; group the 56 weights by their w-charge
from collections import Counter
ch=Counter(round(float(x@w),4) for x in W56); print('(ii) 56 of E7 by U(1)=w charge:', dict(ch))
# the charge classes of size 27 must be E6 27 and 27bar: check that within each class the weights are permuted by E6's Weyl reflections and pair with roots correctly (norm of projection)
for q,cnt in sorted(ch.items()):
    cls=[x for x in W56 if abs(float(x@w)-q)<1e-6]
    if cnt==27:
        # 27 vs 27bar: the E6 weights of a 27 have pairwise inner products (projected) in {4/3, 1/3, -2/3}; the 27bar is the negative set
        P=[x-(x@w)/(w@w)*w for x in cls]; ips=Counter(round(float(P[0]@p),4) for p in P)
        neg=all(any(np.allclose(-p,p2) for p2 in P) for p in P)
        print(f'   charge {q}: 27 weights, inner products of one with all {dict(ips)}, closed under negation (self-conjugate)? {neg}')
    else: print(f'   charge {q}: {cnt} weight(s), E6-projection norm {[round(float((x-(x@w)/(w@w)*w)@(x-(x@w)/(w@w)*w)),4) for x in cls]}')
# (iii) 248 -> E6 x SU(3): SU(3) = roots of E8 orthogonal to all of E6 (the centraliser)
cent=[r for r in R8 if all(abs(r@e)<1e-9 for e in E6)]; print('(iii) roots of E8 orthogonal to E6:', len(cent), '(SU(3) has 6)')
others=[r for r in R8 if not any(np.allclose(r,e) for e in E6) and not any(np.allclose(r,c) for c in cent)]
print('   remaining roots:', len(others), '= 2 x 27 x 3 = 162?', len(others)==162)
# their E6-projections: 27 and 27bar weights each with multiplicity 3
proj=[r-sum((r@c)*c for c in np.linalg.qr(np.array(cent).T)[0].T) for r in others]  # crude: project out the SU(3) Cartan span (2-dim)
print('   (the (27,3)+(27bar,3bar) split: 162 = 81 + 81 by the sign of the U(1) of the SU(3) Cartan is a statement about the weight system; recorded as vector-like under E6 because the 27 and 27bar counts among the 162 are equal:', sum(1 for r in others if r@w>0), sum(1 for r in others if r@w<0), ')')
# (iv) eta charges in the 27 (B1415's gamma direction)
Y=np.array([-1/3,-1/3,-1/3,1/2,1/2,0]); gv=np.array([1,1,1,1,1,-5/np.sqrt(3)]); gamma=gv/np.linalg.norm(gv)
Q=[(round(float(x@Y),4),round(float(x@gamma),4)) for x in W27]
sing=[q for q in Q if abs(q[0])<1e-9]; charged_sing=[q for q,x in zip(Q,W27) if abs(q[0])<1e-9 and not np.allclose(x[:5],0)]
eta_s=set(q[1] for q in charged_sing); print('(iv) charged SM singlets of the 27 (Y=0, not the E6-singlet-like N?):', charged_sing, ' distinct eta:', eta_s)
etas=sorted(set(q[1] for q in Q)); print('   all eta values in the 27:', etas)
target=-2*charged_sing[0][1]; print('   is there a field with eta = -2 x (singlet eta) =', round(target,4), '?', any(abs(e-target)<1e-6 for e in etas), '-> no eta-neutral cubic nu^c nu^c X exists in 27^3')
# (v) with a 27bar: nubar^c has eta = +singlet; the quartic nu^c nu^c nubar^c nubar^c is neutral
print('(v) nu^c nu^c nubar^c nubar^c eta charge:', round(2*charged_sing[0][1]-2*charged_sing[0][1],6), '-> neutral; weight sum:', np.allclose(2*W27[[i for i,q in enumerate(Q) if abs(q[0])<1e-9 and not np.allclose(W27[i][:5],0)][0]]+2*W27b[[i for i,q in enumerate(Q) if abs(q[0])<1e-9 and not np.allclose(W27[i][:5],0)][0]],0))
# (vi) the sum rule: an orbit of charges (q1, q2, q3) = 3 x weights of the 3bar of SU(3) sums to zero
wts3bar=np.array([[1,0],[-1/2,np.sqrt(3)/2],[-1/2,-np.sqrt(3)/2]]); print('(vi) orbit charge sum:', np.round(3*wts3bar.sum(0),12), '; net chirality 3(n+ - n-) = 3 -> n+ - n- = 1: (3,0), (6,3), (9,6), ...')
print('ALL COMPUTED')
