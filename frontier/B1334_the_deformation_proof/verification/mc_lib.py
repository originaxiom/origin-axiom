"""The index on SEVERAL boundary tori, derived from the same pair sequence as B1297.

B1297 (one cusp):  I(V) = n(V) - n(V*) = (a_0 - a*_0) + t*_0 - r_1,  and in domain D,  I = t_0 - r_1.

Re-derivation with  dM = T_1 u ... u T_c,  t_k := sum_i h^k(T_i;V):

  (1) a_3 = 0                       M is homotopy equivalent to a 2-complex     -- no cusp count
  (2) a_0 - a_1 + a_2 = 0           chi(M;V) = d*chi(M) = 0                     -- no cusp count
  (3) a_2 = b*_1                    Poincare-Lefschetz H^k(M;V) = H^{3-k}(M,dM;V*)^*  -- no cusp count
  (4) b*_1 = (t*_0 - a*_0) + n(V*)  exactness of the pair sequence, using that
                                    H^0(M;V*) -> H^0(dM;V*) is INJECTIVE
                                    (v |-> (v,...,v) on c components; M connected) -- SURVIVES c > 1
  (5) r_1 + r*_1 = t_1              L_V and L_{V*} are mutual annihilators; the pairing on
                                    H^1(dM) is the DIRECT SUM of the per-torus pairings, and a
                                    direct sum of perfect pairings is perfect              -- SURVIVES c > 1

so  n(V) = a_1 - r_1  and the same algebra gives, verbatim,

        I(V) = (a_0 - a*_0) + t*_0 - r_1,     and in D (a_0 = a*_0, t_0 = t*_0):   I = t_0 - r_1
                                                                                       = sum_i t_0^(i) - r_1

The formula is UNCHANGED. What changes is the geometry underneath it:
  * B^1(dM;V) = (+)_i B^1(T_i;V) -- each torus carries its OWN coboundaries, so the space L_V sits
    in is a direct sum and dim B^1(dM) = sum_i (d - t_0^(i)), not d - t_0.
  * isotropy of L_V is now a condition on a SUM of per-torus pairings, which can vanish by
    CANCELLATION between cusps -- impossible with one cusp, and exactly where B1332's mechanism
    (V|_T = V*|_T from cusp-triviality) can fail, since a character may be trivial on one cusp
    and not another.

Everything here is CHECKED, not asserted: the driver verifies (2), (5), the two expressions for I,
and t_1 = t_0 + t*_0, on every sector.
"""
import sys
from index_lib import (matmul, matadd, matsub, eye, zeros, scal, matinv, rank,
                       nullspace, fox, word_eval, cocycle_value, invariants)

def cusp_data(peripherals, rho, p, d):
    """per-cusp (A_i, B_i, t_0^(i), t_1^(i))"""
    out=[]
    for (mu,lam) in peripherals:
        A=word_eval(mu,rho,p,d); B=word_eval(lam,rho,p,d)
        t0=invariants([A,B],p,d)
        Am=matsub(A,eye(d),p); Bm=matsub(B,eye(d),p)
        # B^1(T_i): image of w |-> ((A-1)w, (B-1)w); dim = d - t0
        rB=d-t0
        # Z^1(T_i) = {(u,v): (A-1)v = (B-1)u}
        rows=[[ (-Bm[x][y])%p for y in range(d)]+[Am[x][y] for y in range(d)] for x in range(d)]
        t1=len(nullspace(rows,p,2*d))-rB
        out.append(dict(mu=mu,lam=lam,A=A,B=B,t0=t0,t1=t1,rB=rB))
    return out

def h_star(gens,rels,rho,p,d):
    """a_0, a_1, a_2 and Z^1(M;V) from the presentation 2-complex"""
    g=len(gens)
    a0=invariants([rho[x] for x in gens],p,d)
    J=[]
    for r in rels:
        bl=[fox(r,x,rho,p,d) for x in gens]
        for a in range(d):
            J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullspace(J,p,g*d)
    a1=len(Zs)-(d-a0)                 # dim Z^1 - dim B^1,  dim B^1 = d - a_0
    a2=len(rels)*d-rank(J,p)          # coker of d^1
    return a0,a1,a2,Zs

def analyse_mc(gens,rels,peripherals,rho,p,d):
    """everything the index needs, on c cusps"""
    g=len(gens)
    a0,a1,a2,Zs=h_star(gens,rels,rho,p,d)
    cusps=cusp_data(peripherals,rho,p,d)
    c=len(cusps)
    t0=sum(x['t0'] for x in cusps); t1=sum(x['t1'] for x in cusps)
    # restriction of H^1(M;V) to (+)_i H^1(T_i;V), as vectors of length 2*c*d
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]
        row=[]
        for x in cusps:
            row += cocycle_value(x['mu'],gens,rho,p,d,z)+cocycle_value(x['lam'],gens,rho,p,d,z)
        R.append(row)
    # B^1(dM) = (+)_i B^1(T_i): each cusp gets its OWN w, so the blocks are independent
    Bt=[]
    for i,x in enumerate(cusps):
        Am=matsub(x['A'],eye(d),p); Bm=matsub(x['B'],eye(d),p)
        for k in range(d):
            row=[0]*(2*c*d)
            for r_ in range(d):
                row[2*i*d+r_]     = Am[r_][k]
                row[2*i*d+d+r_]   = Bm[r_][k]
            Bt.append(row)
    rB=rank(Bt,p)
    r1=rank(R+Bt,p)-rB
    return dict(c=c,a0=a0,a1=a1,a2=a2,t0=t0,t1=t1,r1=r1,rB=rB,
                t0s=[x['t0'] for x in cusps], t1s=[x['t1'] for x in cusps],
                live=sum(1 for x in cusps if x['t0']>0),
                n=a1-r1, I=t0-r1)

def dual_rho(rho,gens,p,d):
    """V* : g |-> (rho(g)^{-1})^T"""
    out={}
    for x in gens:
        Ai=matinv(rho[x],p)
        out[x]=[[Ai[j][i] for j in range(d)] for i in range(d)]
    return out

def check(gens,rels,peripherals,rho,p,d):
    """compute V and V*, verify every identity, return the row.

    I_exact := n(V) - n(V*) is the DEFINITION; the derivation's content is that it equals
    (a_0 - a*_0) + t*_0 - r_1, and that inside domain D that collapses to t_0 - r_1.
    Both are checked; being in D is reported, never assumed."""
    A=analyse_mc(gens,rels,peripherals,rho,p,d)
    B=analyse_mc(gens,rels,peripherals,dual_rho(rho,gens,p,d),p,d)
    I_exact = A['n']-B['n']
    inD = (A['a0']==B['a0']) and (A['t0']==B['t0'])
    ids={
      # note: a_0-a_1+a_2 = d*(1-g+|rels|) identically, so this checks the PRESENTATION has
      # deficiency 1, not the manifold -- recorded as what it is
      "deficiency-1 (a0-a1+a2=0)": A['a0']-A['a1']+A['a2']==0,
      "r1+r1*=t1"                : A['r1']+B['r1']==A['t1'],
      "t1=t0+t0*"                : A['t1']==A['t0']+B['t0'],
      "I_exact=(a0-a0*)+t0*-r1"  : I_exact==(A['a0']-B['a0'])+B['t0']-A['r1'],
      "I(V*)=-I(V)"              : (B['n']-A['n'])==-I_exact,
    }
    if inD:
        ids["in D: I_exact=t0-r1"]= I_exact==A['t0']-A['r1']
    A['I_exact']=I_exact; B['I_exact']=-I_exact; A['inD']=inD
    return A,B,ids
