#!/usr/bin/env python3
"""A5: THE PARITY LEMMA — is the projectivity criterion's second clause redundant?

Memo 2/30's criterion: a stratum is projective (27-parity all even) iff its
weighted-Dynkin labels are all even AND <omega_1, H> is even.  Memo 30's data:
all 9 even-labeled rows are projective, all 11 rows with a 1 are odd — the AND
never bit.  LEMMA CANDIDATE: for E6, every even-labeled element of the COROOT
lattice automatically has <omega_1, H> even, so the criterion collapses to the
single adjoint-only condition 'even orbit'.

Proof by exhaustive lattice check (E6-specific, exact):
  - the candidate set for even characteristics is {0,2}^6 dominant labels c
    with H = sum c_j omega_j^vee in the COROOT lattice (h of an sl2-triple is
    always a coroot-lattice element — standard);
  - H in coroot lattice  <=>  m = A^{-1} c integral;
  - <omega_1, H> = m_1  (expand H = sum m_i alpha_i^vee; <omega_1,alpha_i^vee>
    = delta_{1i});
  - check: is m_1 even for EVERY such c (all 64 candidates, not just the 9
    realized characteristics)?
Also the converse side from memo 30's banked data: every row with an odd label
has odd 27-content (re-checked there); this cert closes the even side as a
LATTICE theorem, stronger than the 20-row empirics.
"""
from fractions import Fraction as F
import itertools

# E6 Cartan matrix in the bench's simple-root order — recovered from exact
# brackets and printed by cp1_strata.py (banked, memo 30); asserted symmetric.
A=[[2,0,-1,0,0,0],
   [0,2,0,-1,0,0],
   [-1,0,2,-1,0,0],
   [0,-1,-1,2,-1,0],
   [0,0,0,-1,2,-1],
   [0,0,0,0,-1,2]]
N=6
assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))

def inv(M):
    n=len(M); aug=[[F(M[i][j]) for j in range(n)]+[F(1) if k==i else F(0) for k in range(n)] for i in range(n)]
    for col in range(n):
        p=next(i for i in range(col,n) if aug[i][col]!=0)
        aug[col],aug[p]=aug[p],aug[col]
        pv=aug[col][col]; aug[col]=[x/pv for x in aug[col]]
        for i in range(n):
            if i!=col and aug[i][col]!=0:
                fq=aug[i][col]; aug[i]=[x-fq*y for x,y in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]
Ainv=inv(A)

total=0; integral=0; all_even=True; witness=[]
for c in itertools.product((0,2),repeat=N):
    if all(x==0 for x in c): continue
    total+=1
    m=[sum(Ainv[i][j]*F(c[j]) for j in range(N)) for i in range(N)]
    if not all(x.denominator==1 for x in m): continue
    integral+=1
    m1=m[0]
    witness.append((c, int(m1), int(m1)%2==0))
    if int(m1)%2!=0: all_even=False

print(f"even-labeled candidates c in {{0,2}}^6 \\ {{0}}: {total}")
print(f"of these, H = sum c_j omega_j^vee lies in the COROOT lattice: {integral}")
for c,m1,ok in witness:
    print(f"  c={c}: <omega_1,H> = m_1 = {m1}  even: {ok}")
print(f"\n<omega_1,H> even for EVERY even-labeled coroot-lattice element: {all_even}")
assert all_even

# cross-check against memo 30's nine banked even-labeled characteristics
banked9=[(0,0,0,2,0,0),(0,2,0,0,0,0),(0,2,0,2,0,0),(2,0,0,0,0,2),(2,0,0,2,0,2),
         (2,2,0,0,0,2),(2,2,0,2,0,2),(2,2,2,0,2,2),(2,2,2,2,2,2)]
in_cand={c for c,_,_ in witness}
print("all 9 banked even characteristics appear among the integral candidates:",
      all(c in in_cand for c in banked9))
assert all(c in in_cand for c in banked9)

print("""
A5 LEMMA (E6): for every even-labeled element of the coroot lattice,
<omega_1, H> is automatically even — so on the 27 the parity of a stratum is
decided by the ADJOINT data alone:  PROJECTIVE  <=>  EVEN ORBIT.
The criterion's second clause is provably redundant; memo 30's dictionary
(9 projective = the 9 even-labeled rows) is the realized instance.""")
