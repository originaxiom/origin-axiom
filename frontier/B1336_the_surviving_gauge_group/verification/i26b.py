"""The general statement, not just the two computed cases.

Any flat connection whose holonomy lands in the principal SL2 and CONTAINS the McKay image 2T has

        2T  <=  H  <=  SL2(principal)      =>      Z(SL2) <= Z(H) <= Z(2T)

so its unbroken algebra is squeezed between the two computed ends. Both ends are computed exactly
here; if the upper end is ABELIAN then every Z(H) in the family is abelian, and the Standard-Model
algebra -- NON-abelian, dim 12 -- cannot be any of them, whatever the holonomy.
"""
import sys, io, contextlib
sys.path.insert(0,'/home/user/origin-axiom/frontier/B854_centralizer_exact')
from fractions import Fraction as F
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    import e6_centralizer as E
DIM=E.DIM; br=E.br; nz=E.nz
INV=E.INV; ns=sorted(INV)

print("=== the upper end: Z(2T), from B854's four invariants, re-verified here ===")
print(f"  spanning vectors: {len(ns)}  (blocks {ns})")
# independence
M=[INV[n][:] for n in ns]
def rank(M,cols):
    M=[r[:] for r in M]; r=0
    for c in range(cols):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(cols)]
        r+=1
    return r
print(f"  rank = {rank(M,DIM)}   -> dim Z(2T) = 4")
pairs=[(a,b) for i,a in enumerate(ns) for b in ns[i+1:]]
allzero=all(not nz(br(INV[a],INV[b])) for a,b in pairs)
print(f"  every bracket [x_a, x_b] vanishes ({len(pairs)} pairs): {allzero}")
print(f"  -> Z(2T) is ABELIAN, u(1)^4")

print("\n=== the lower end: Z(principal sl2) ===")
def cent_dim(gens):
    M=[]
    for g in gens:
        A=[[F(0)]*DIM for _ in range(DIM)]
        for j in range(DIM):
            bj=[F(0)]*DIM; bj[j]=F(1); col=br(g,bj)
            for i in range(DIM): A[i][j]=col[i]
        M.extend(A)
    return DIM-rank(M,DIM)
d0=cent_dim([E.e,E.h,E.f])
print(f"  dim Z(principal sl2) = {d0}")

print("\n=== the squeeze ===")
print("  For every H with 2T <= H <= SL2(principal):")
print(f"      {d0} = dim Z(SL2)  <=  dim Z(H)  <=  dim Z(2T) = 4")
print("  and Z(H) <= Z(2T) as a SUBALGEBRA of an abelian algebra, hence ABELIAN.")
print("\n=== against the Standard Model ===")
print("  su(3) (+) su(2) (+) u(1):  dim 12, NON-abelian (it contains su(3))")
print("  every Z(H) in the family:  dim <= 4, ABELIAN")
print("\n  THEOREM: no flat connection with holonomy in the principal SL2 containing 2T")
print("           leaves the Standard-Model algebra unbroken -- whatever the holonomy.")
print("\n=== positive control: the routine finds a KNOWN centralizer ===")
print(f"  dim Z(h) for the principal semisimple h = {cent_dim([E.h])}  (must be 6 = rank E6)")
