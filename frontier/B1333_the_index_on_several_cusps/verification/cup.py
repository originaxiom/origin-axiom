"""The cup product on H^1(T;W) and the isotropy of L_V, exactly over Q(zeta_12).

pi_1(T) = Z^2 = <mu, lam>, A = rho(mu), B = rho(lam), commuting.
Z^1 = {(u,v) : (A-1)v = (B-1)u},  B^1 = {((A-1)w, (B-1)w)}.
Cup product on the fundamental class [mu|lam] - [lam|mu]:
    <z, z'> = F(z(mu), A z'(lam)) - F(z(lam), B z'(mu))
with F the invariant form on W, obtained by SOLVING rho(g)^T F rho(g) = F.
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as F
from q12 import *
from q12 import _dot
from fi_lib import get_rho, wev, sym, blockdiag, fox, invariants, order3_chars, analyse

def transpose(M): return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def invariant_forms(mats, d):
    """all F with g^T F g = F for every g -- solve the linear system exactly"""
    rows=[]
    for g in mats:
        gt=transpose(g)
        # (g^T F g - F)_{ab} = sum_{i,j} g[i][a] F[i][j] g[j][b] - F[a][b] = 0
        for a in range(d):
            for b in range(d):
                row=[Z]*(d*d)
                for i in range(d):
                    for j in range(d):
                        row[i*d+j]=add(row[i*d+j], mul(g[i][a],g[j][b]))
                row[a*d+b]=sub(row[a*d+b],ONE)
                rows.append(row)
    ns=nullspace(rows,d*d)
    return [[[v[i*d+j] for j in range(d)] for i in range(d)] for v in ns]

def cocycles(A,B,d):
    """Z^1(T;W) as vectors (u,v) of length 2d, and B^1"""
    rows=[]
    Am=msub(A,eye(d)); Bm=msub(B,eye(d))
    for x in range(d):
        row=[Z]*(2*d)
        for y in range(d):
            row[y]      = neg(Bm[x][y])   # -(B-1)u
            row[d+y]    = Am[x][y]        #  (A-1)v
        rows.append(row)
    Zs=nullspace(rows,2*d)
    Bs=[]
    for i in range(d):
        w=[ONE if k==i else Z for k in range(d)]
        Bs.append([_dot(Am[x],w) for x in range(d)]+[_dot(Bm[x],w) for x in range(d)])
    return Zs,Bs

def cup(z,zp,A,B,Fm,d):
    u,v   = z[:d],  z[d:]
    up,vp = zp[:d], zp[d:]
    Avp=[_dot(A[x],vp) for x in range(d)]
    Bup=[_dot(B[x],up) for x in range(d)]
    def pair(p,q):
        s=Z
        for i in range(d):
            for j in range(d): s=add(s,mul(mul(Fm[i][j],p[i]),q[j]))
        return s
    return sub(pair(u,Avp), pair(v,Bup))

def gram(basis,A,B,Fm,d):
    return [[cup(p,q,A,B,Fm,d) for q in basis] for p in basis]

def reduce_mod(basis, Bs, ncols):
    """a basis of span(basis) modulo span(Bs)"""
    out=[]; cur=[list(b) for b in Bs]
    for v in basis:
        if rank(cur+[v])>rank(cur):
            cur.append(list(v)); out.append(list(v))
    return out
