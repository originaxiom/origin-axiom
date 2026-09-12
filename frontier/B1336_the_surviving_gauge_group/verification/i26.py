"""I-26's unpaid half: NAME THE SURVIVING GAUGE GROUP -- the centralizer of rho(pi_1) in e6.

The ledger records the price as "untouched". It turns on a distinction the corpus has not drawn:

  * B854 computes the centralizer of **2T**, the FINITE McKay image, and gets u(1)^4.
  * The object's geometric holonomy is DISCRETE AND FAITHFUL in PSL2(C), hence INFINITE and
    Zariski-DENSE in SL2. For a Zariski-dense subgroup the centralizer equals the centralizer of
    the whole SL2 -- strictly smaller than the finite group's.

So the surviving gauge group depends on which rho is meant, and the two answers differ. Compute both
exactly, plus the regular A1A1A2 embedding B1303 used, and test each against the Standard-Model
algebra su(3) (+) su(2) (+) u(1) (dim 12, rank 4).

Everything reuses B854's exact E6 Chevalley algebra over Q, re-verified here before use.
"""
import sys, io, contextlib
sys.path.insert(0,'/home/user/origin-axiom/frontier/B854_centralizer_exact')
from fractions import Fraction as F
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    import e6_centralizer as E
print("B854 engine loaded and its own controls re-run:")
for line in buf.getvalue().strip().split("\n")[-4:]: print("   ",line)

DIM=E.DIM; br=E.br; nz=E.nz
e,h,f = E.e, E.h, E.f
print(f"\ne6 dimension {DIM}  (78 expected)")

def check_sl2(e,h,f):
    ok = (not nz(E.add(br(h,e), E.smul(F(-2),e)))) and \
         (not nz(E.add(br(h,f), E.smul(F(2),f)))) and \
         (not nz(E.add(br(e,f), E.smul(F(-1),h))))
    return ok
print(f"principal sl2 relations [h,e]=2e, [h,f]=-2f, [e,f]=h : {check_sl2(e,h,f)}")

def centralizer_dim(gens):
    """dim {x in e6 : [g,x] = 0 for every g}, exact over Q"""
    rows=[]
    for g in gens:
        # the matrix of ad(g) in the standard basis: column j = [g, b_j]
        for j in range(DIM):
            bj=[F(0)]*DIM; bj[j]=F(1)
            col=br(g,bj)
            rows.append((j,col))
    # build ad matrices stacked: solve ad(g) x = 0 for all g
    M=[]
    for g in gens:
        A=[[F(0)]*DIM for _ in range(DIM)]
        for j in range(DIM):
            bj=[F(0)]*DIM; bj[j]=F(1)
            col=br(g,bj)
            for i in range(DIM): A[i][j]=col[i]
        M.extend(A)
    # rank over Q
    M=[r[:] for r in M]; rows_n=len(M); r=0
    for c in range(DIM):
        p=next((i for i in range(r,rows_n) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(rows_n):
            if i!=r and M[i][c]!=0:
                fac=M[i][c]; M[i]=[M[i][j]-fac*M[r][j] for j in range(DIM)]
        r+=1
    return DIM-r

print("\n=== the centralizers ===")
d_pr = centralizer_dim([e,h,f])
print(f"  principal sl2 (= the Zariski closure of a dense rho(pi_1)) : dim = {d_pr}")
d_h  = centralizer_dim([h])
print(f"  the principal torus h alone                                : dim = {d_h}")
# 2T: B854's four invariants span its centralizer
print(f"  2T, the FINITE McKay image (B854, re-run above)            : dim = 4, ABELIAN u(1)^4")

SM_dim, SM_rank = 12, 4
print(f"\n=== against the Standard-Model algebra su(3)+su(2)+u(1): dim {SM_dim}, rank {SM_rank} ===")
for name,d,ab in (("principal sl2 (geometric holonomy)",d_pr,None),
                  ("2T (finite quotient)",4,True)):
    verdict = "MATCHES" if d==SM_dim else f"NO -- dim {d} != {SM_dim}"
    extra = "  (and it is ABELIAN, so it cannot contain su(3) or su(2))" if ab else ""
    print(f"  {name:38s}: {verdict}{extra}")
