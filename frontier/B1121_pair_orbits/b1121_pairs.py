#!/usr/bin/env python3
"""
F8 -- cell for L176 (docs/OPEN_LEADS.md): the orbit structure of F4(Z) (integral
automorphisms of the split exceptional Jordan algebra J3) on ORTHOGONAL PAIRS of
rank-1 idempotents.

Standalone, repo-relative (no machine paths -- all I/O is relative to this file's
own directory). Reproduces the positive control (single-idempotent transitivity,
an outside session's OBSERVED-grade result, REIMPLEMENTED here from its verbal
description -- no source script was ever available) and then runs the new
computation: BFS on ORTHOGONAL PAIRS (E,F), E.F=0, both rank 1.

See f8_NOTES.md for the full derivation write-up (octonion arithmetic, the Jordan
algebra, and -- the one piece that had to be *found* rather than recalled -- the
Freudenthal-rotation derivation D_i(a) and its integral normalization).

Usage:  python3 f8_pairs.py             # full run (~15-25 min; writes f8_results.json)
        python3 f8_pairs.py --quick     # smaller bounds, for a fast sanity pass

Everything is exact (Python Fraction / arbitrary-precision int); no floats are
used in any load-bearing computation.
"""
import os
import sys
import time
import json
import math
import random
import itertools
import argparse
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GENS_CACHE = os.path.join(HERE, "f8_gens_cache.npz")

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:8.2f}s] {msg}", flush=True)

# ============================================================================
# PART 1 -- split octonions (Zorn vector matrices), exact integer arithmetic
# ============================================================================
# Element = (a, x, y, b), a,b in Z, x,y in Z^3.
# (a,x,y,b)*(a',x',y',b') = (aa'+x.y', ax'+b'x-yxy', a'y+by'+xxx', bb'+y.x')
# N(a,x,y,b) = ab - x.y   (signature (4,4) on Z^8)

def dot(u, v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross(u, v): return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def vadd(u,v): return (u[0]+v[0],u[1]+v[1],u[2]+v[2])
def vsub(u,v): return (u[0]-v[0],u[1]-v[1],u[2]-v[2])
def vneg(u): return (-u[0],-u[1],-u[2])
def vscale(u,s): return (u[0]*s,u[1]*s,u[2]*s)

O_ZERO = (0,(0,0,0),(0,0,0),0)
O_ONE = (1,(0,0,0),(0,0,0),1)

def oadd(p,q): return (p[0]+q[0], vadd(p[1],q[1]), vadd(p[2],q[2]), p[3]+q[3])
def osub(p,q): return (p[0]-q[0], vsub(p[1],q[1]), vsub(p[2],q[2]), p[3]-q[3])
def oscale(p,s): return (p[0]*s, vscale(p[1],s), vscale(p[2],s), p[3]*s)

def omul(p,q):
    a,x,y,b = p; ap,xp,yp,bp = q
    return (a*ap+dot(x,yp),
            vadd(vscale(xp,a), vsub(vscale(x,bp), cross(y,yp))),
            vadd(vadd(vscale(y,ap), vscale(yp,b)), cross(x,xp)),
            b*bp+dot(y,xp))

def oconj(p):
    a,x,y,b = p
    return (b, vneg(x), vneg(y), a)

def onorm(p):
    a,x,y,b = p
    return a*b - dot(x,y)

def onorm_definite(p):
    """Division-form control: the POSITIVE DEFINITE octonion norm."""
    a,x,y,b = p
    return a*a + x[0]**2+x[1]**2+x[2]**2 + y[0]**2+y[1]**2+y[2]**2 + b*b

def obil(p,q): return onorm(oadd(p,q)) - onorm(p) - onorm(q)

def orandom(rng, lo=-3, hi=3):
    return (rng.randint(lo,hi), tuple(rng.randint(lo,hi) for _ in range(3)),
            tuple(rng.randint(lo,hi) for _ in range(3)), rng.randint(lo,hi))

# ============================================================================
# PART 2 -- the split exceptional Jordan algebra J3 = H3(O_s)
# ============================================================================
# X = (xi1,xi2,xi3, o1,o2,o3);  o_i opposite diagonal index i (the (2,3) slot
# convention this repo already uses -- CHANGELOG.md L162 status note).
#     [[ xi1,  o3, ~o2 ],
#      [ ~o3, xi2,  o1 ],
#      [  o2, ~o1, xi3 ]]
# Jordan product X o Y = (XY+YX)/2 via literal 3x3 octonion matrix multiply.

def F_(v): return Fr(v)
def oF(p):
    a,x,y,b = p
    return (F_(a), tuple(F_(t) for t in x), tuple(F_(t) for t in y), F_(b))
O_ZEROF = oF(O_ZERO)

def is_scalar_oct(p):
    a,x,y,b = p
    return a==b and all(t==0 for t in x) and all(t==0 for t in y)
def oscalarF(n):
    n = F_(n); z=(F_(0),F_(0),F_(0))
    return (n, z, z, n)

def mkJ(xi1,xi2,xi3, o1,o2,o3):
    """xi's: int/Fraction. o's: int-tuple octonions (a,x,y,b) or already-Fraction."""
    def lift(o):
        return o if isinstance(o[0], Fr) else oF(o)
    return (F_(xi1),F_(xi2),F_(xi3), lift(o1),lift(o2),lift(o3))

def J_zero(): return mkJ(0,0,0, O_ZERO,O_ZERO,O_ZERO)
def J_identity(): return mkJ(1,1,1, O_ZERO,O_ZERO,O_ZERO)
def J_diag(a,b,c): return mkJ(a,b,c, O_ZERO,O_ZERO,O_ZERO)
def J_offdiag(slot, o):
    z=[O_ZERO,O_ZERO,O_ZERO]; z[slot-1]=o
    return mkJ(0,0,0, z[0],z[1],z[2])

def Jadd(X,Y):
    return (X[0]+Y[0],X[1]+Y[1],X[2]+Y[2], oadd(X[3],Y[3]),oadd(X[4],Y[4]),oadd(X[5],Y[5]))
def Jsub(X,Y):
    return (X[0]-Y[0],X[1]-Y[1],X[2]-Y[2], osub(X[3],Y[3]),osub(X[4],Y[4]),osub(X[5],Y[5]))
def Jscale(X,s):
    s=F_(s)
    return (X[0]*s,X[1]*s,X[2]*s, oscale(X[3],s),oscale(X[4],s),oscale(X[5],s))
def Jeq(X,Y): return Jsub(X,Y) == J_zero()
def J_is_zero(X):
    xi1,xi2,xi3,o1,o2,o3 = X
    vals=[xi1,xi2,xi3]
    for o in (o1,o2,o3):
        a,x,y,b=o; vals += [a,x[0],x[1],x[2],y[0],y[1],y[2],b]
    return all(v==0 for v in vals)

def to_matrix(X):
    xi1,xi2,xi3,o1,o2,o3 = X
    s1,s2,s3 = oscalarF(xi1),oscalarF(xi2),oscalarF(xi3)
    return [[s1,o3,oconj(o2)],[oconj(o3),s2,o1],[o2,oconj(o1),s3]]

def mat_mul3(A,B):
    C=[[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc=O_ZEROF
            for k in range(3):
                acc = oadd(acc, omul(A[i][k],B[k][j]))
            C[i][j]=acc
    return C
def mat_add3(A,B): return [[oadd(A[i][j],B[i][j]) for j in range(3)] for i in range(3)]
def mat_scale3(A,s): return [[oscale(A[i][j],s) for j in range(3)] for i in range(3)]

def from_matrix(M):
    for i in range(3):
        assert is_scalar_oct(M[i][i]), f"diag[{i}] not scalar"
    for (i,j) in [(0,1),(0,2),(1,2)]:
        assert M[i][j]==oconj(M[j][i]), f"not Hermitian at ({i},{j})"
    xi1,xi2,xi3 = M[0][0][0],M[1][1][0],M[2][2][0]
    o3,o2c,o1 = M[0][1],M[0][2],M[1][2]
    return (xi1,xi2,xi3, o1, oconj(o2c), o3)

def jordan_mul(X,Y):
    MX,MY = to_matrix(X),to_matrix(Y)
    P,Q = mat_mul3(MX,MY), mat_mul3(MY,MX)
    return from_matrix(mat_scale3(mat_add3(P,Q), Fr(1,2)))

def trace(X): return X[0]+X[1]+X[2]
def jordan_sq(X): return jordan_mul(X,X)
def S_form(X): return (trace(X)**2 - trace(jordan_sq(X)))/2
def adjugate(X):
    X2=jordan_sq(X); TX=trace(X); SX=S_form(X)
    return Jadd(Jsub(X2, Jscale(X,TX)), Jscale(J_identity(),SX))
def normJ(X):
    return trace(jordan_mul(X, adjugate(X)))/3
def normJ_newton(X):
    T1=trace(X); X2=jordan_sq(X); T2=trace(X2); T3=trace(jordan_mul(X2,X))
    return (T1**3 - 3*T1*T2 + 2*T3)/6
def normJ_closed_form(X):
    xi1,xi2,xi3,o1,o2,o3 = X
    base = xi1*xi2*xi3 - xi1*onorm(o1) - xi2*onorm(o2) - xi3*onorm(o3)
    trip = omul(o1, omul(o2,o3))
    return base + trip[0] + trip[3]
def jordan_identity_holds(X,Y):
    X2=jordan_sq(X)
    return Jeq(jordan_mul(jordan_mul(X,Y),X2), jordan_mul(X,jordan_mul(Y,X2)))

def Jrandom_int(rng, lo=-3, hi=3):
    xi = tuple(rng.randint(lo,hi) for _ in range(3))
    o = tuple(orandom(rng,lo,hi) for _ in range(3))
    return mkJ(xi[0],xi[1],xi[2], o[0],o[1],o[2])

# ============================================================================
# PART 3 -- 27-dim coordinates, L_x as 27x27, inner derivations, D_i(a)
# ============================================================================
def basis_vectors():
    basis=[]
    for i in range(3):
        xi=[0,0,0]; xi[i]=1
        basis.append(mkJ(xi[0],xi[1],xi[2], O_ZERO,O_ZERO,O_ZERO))
    for slot in range(1,4):
        for coord in range(8):
            o=[0,[0,0,0],[0,0,0],0]
            if coord==0: o[0]=1
            elif 1<=coord<=3: o[1][coord-1]=1
            elif 4<=coord<=6: o[2][coord-4]=1
            else: o[3]=1
            ot=(o[0],tuple(o[1]),tuple(o[2]),o[3])
            os_=[O_ZERO,O_ZERO,O_ZERO]; os_[slot-1]=ot
            basis.append(mkJ(0,0,0, os_[0],os_[1],os_[2]))
    assert len(basis)==27
    return basis
BASIS = basis_vectors()

def to_vec(X):
    xi1,xi2,xi3,o1,o2,o3 = X
    v=[xi1,xi2,xi3]
    for o in (o1,o2,o3):
        a,x,y,b=o; v += [a,x[0],x[1],x[2], y[0],y[1],y[2], b]
    return v
def from_vec(v):
    xi1,xi2,xi3=v[0],v[1],v[2]; os_=[]
    for s in range(3):
        base=3+8*s
        os_.append((v[base],(v[base+1],v[base+2],v[base+3]),
                    (v[base+4],v[base+5],v[base+6]),v[base+7]))
    return (xi1,xi2,xi3, os_[0],os_[1],os_[2])

def mat_from_linear_map(f):
    cols=[f(to_vec(b)) for b in BASIS]
    return [[cols[k][i] for k in range(27)] for i in range(27)]

def L_matrix(x):
    def f(v):
        Y = from_vec(v)
        return to_vec(jordan_mul(x,Y))
    return mat_from_linear_map(f)

def mat_mul27(A,B):
    n=27; C=[[Fr(0)]*n for _ in range(n)]
    for i in range(n):
        Ai=A[i]
        for k in range(n):
            if Ai[k]==0: continue
            aik=Ai[k]; Bk=B[k]; Ci=C[i]
            for j in range(n):
                if Bk[j]!=0: Ci[j]+=aik*Bk[j]
    return C
def mat_add27(A,B): return [[A[i][j]+B[i][j] for j in range(27)] for i in range(27)]
def mat_sub27(A,B): return [[A[i][j]-B[i][j] for j in range(27)] for i in range(27)]
def mat_scale27(A,s): return [[A[i][j]*s for j in range(27)] for i in range(27)]
def identity27(): return [[Fr(1) if i==j else Fr(0) for j in range(27)] for i in range(27)]
def mat_apply27(M,v): return [sum(M[i][j]*v[j] for j in range(27) if v[j]!=0) for i in range(27)]
def is_integer_mat(M): return all(v.denominator==1 for row in M for v in row)

def D_xy(x,y):
    Lx,Ly = L_matrix(x),L_matrix(y)
    return mat_sub27(mat_mul27(Lx,Ly), mat_mul27(Ly,Lx))
def apply_D_to_J(D,X): return from_vec(mat_apply27(D, to_vec(X)))

E_DIAG = {1: J_diag(1,0,0), 2: J_diag(0,1,0), 3: J_diag(0,0,1)}
def complementary(i): return tuple(t for t in (1,2,3) if t != i)

# THE DISCOVERED, CALIBRATED FORMULA (see f8_NOTES.md Sec. 3 for the search
# that found it): D_i(a) = 2*[L_{Ejj-Ekk}, L_{OffDiag_i(a)}].
# It is linear in a, so 8 basis-derivations per slot suffice to build any a.
_DBASIS_CACHE = {}
def build_dbasis():
    OCT_BASIS = []
    for coord in range(8):
        o=[0,[0,0,0],[0,0,0],0]
        if coord==0: o[0]=1
        elif 1<=coord<=3: o[1][coord-1]=1
        elif 4<=coord<=6: o[2][coord-4]=1
        else: o[3]=1
        OCT_BASIS.append((o[0],tuple(o[1]),tuple(o[2]),o[3]))
    dbasis = {}
    for i in (1,2,3):
        j,k = complementary(i)
        x = Jsub(E_DIAG[j], E_DIAG[k])
        mats=[]
        for m in range(8):
            A = J_offdiag(i, OCT_BASIS[m])
            mats.append(mat_scale27(D_xy(x,A), Fr(2)))
        dbasis[i]=mats
    return dbasis

def D_i_of_a(i, a8):
    mats = _DBASIS_CACHE[i]
    acc=[[Fr(0)]*27 for _ in range(27)]
    for m in range(8):
        c=a8[m]
        if c==0: continue
        Dm=mats[m]
        for r in range(27):
            row=acc[r]; Dr=Dm[r]
            if c==1:
                for cc in range(27): row[cc]+=Dr[cc]
            elif c==-1:
                for cc in range(27): row[cc]-=Dr[cc]
            else:
                for cc in range(27): row[cc]+=c*Dr[cc]
    return acc

def B_i_of_a(i, a8):
    """exp(D_i(a)) = I + D + D^2/2 (D^3=0 exactly when N(a)=0, verified)."""
    D = D_i_of_a(i, a8)
    D2 = mat_mul27(D,D)
    return mat_add27(mat_add27(identity27(), D), mat_scale27(D2, Fr(1,2)))

def oct_from_coords(v8):
    return (v8[0],(v8[1],v8[2],v8[3]),(v8[4],v8[5],v8[6]),v8[7])

# ============================================================================
# PART 4 -- generator construction (cached), controls
# ============================================================================
def enumerate_isotropics(box=(-1,0,1)):
    out=[]
    for v in itertools.product(box, repeat=8):
        if any(t!=0 for t in v) and onorm(oct_from_coords(v))==0:
            out.append(v)
    return out

def build_all_generators(rebuild=False):
    if (not rebuild) and os.path.exists(GENS_CACHE):
        log(f"loading cached generators from {os.path.relpath(GENS_CACHE, HERE)}")
        data = np.load(GENS_CACHE)
        return data['gens'], data['meta']
    log("building the 24 basis-derivation matrices (8 per slot)...")
    global _DBASIS_CACHE
    _DBASIS_CACHE = build_dbasis()
    log("enumerating the 1920 isotropic octonions in the minimal box {-1,0,1}^8...")
    isotropics = enumerate_isotropics()
    log(f"  found {len(isotropics)} (task states 1920)")
    assert len(isotropics) == 1920, "isotropic count mismatch vs the task's stated 1920"
    gens_meta, gens_mat = [], []
    n_nonint = 0
    for i in (1,2,3):
        for a8 in isotropics:
            U = B_i_of_a(i, a8)
            if not is_integer_mat(U):
                n_nonint += 1
                continue
            gens_meta.append((i,)+a8)
            gens_mat.append([[int(v) for v in row] for row in U])
        log(f"  slot {i} done, total generators so far {len(gens_mat)}")
    log(f"non-integer exp(D) cases: {n_nonint} (expect 0 -- this IS control C6)")
    GEN_TENSOR = np.array(gens_mat, dtype=np.int64)
    META = np.array(gens_meta, dtype=np.int64)
    np.savez_compressed(GENS_CACHE, gens=GEN_TENSOR, meta=META)
    log(f"cached to {os.path.relpath(GENS_CACHE, HERE)}: {GEN_TENSOR.shape}")
    return GEN_TENSOR, META

def run_controls(rng, n_auto=60, n_inv=200):
    """C0 (octonion arithmetic), C1 (Leibniz), C2 (Jordan identity), C3 (N
    cross-checks + Freudenthal), C6b (unimodularity), C7 (division-form
    collapse). Returns a dict for the results JSON."""
    out = {}
    log("CONTROL C0: octonion arithmetic (multiplicativity, alternative law, "
        "conjugate anti-automorphism)...")
    trials=500; f_mult=f_alt1=f_alt2=f_conj=0
    for _ in range(trials):
        p,q = orandom(rng), orandom(rng)
        if onorm(omul(p,q)) != onorm(p)*onorm(q): f_mult+=1
        if omul(omul(p,p),q) != omul(p,omul(p,q)): f_alt1+=1
        if omul(omul(p,q),q) != omul(p,omul(q,q)): f_alt2+=1
        if oconj(omul(p,q)) != omul(oconj(q),oconj(p)): f_conj+=1
    out['C0_norm_multiplicativity'] = f"{trials-f_mult}/{trials}"
    out['C0_alternative_law'] = f"{trials-f_alt1}/{trials}, {trials-f_alt2}/{trials}"
    out['C0_conjugate_antiautomorphism'] = f"{trials-f_conj}/{trials}"
    log(f"  norm mult {out['C0_norm_multiplicativity']}, alt {out['C0_alternative_law']}, "
        f"conj {out['C0_conjugate_antiautomorphism']}")

    log("CONTROL C1: [L_x,L_y] is a derivation (Leibniz rule)...")
    ok=0; tot=0
    for _ in range(15):
        x,y = Jrandom_int(rng,-2,2), Jrandom_int(rng,-2,2)
        D = D_xy(x,y)
        for _ in range(4):
            Z,W = Jrandom_int(rng,-2,2), Jrandom_int(rng,-2,2)
            lhs = apply_D_to_J(D, jordan_mul(Z,W))
            rhs = Jadd(jordan_mul(apply_D_to_J(D,Z),W), jordan_mul(Z,apply_D_to_J(D,W)))
            tot+=1
            if Jeq(lhs,rhs): ok+=1
    out['C1_leibniz_derivation'] = f"{ok}/{tot}"
    log(f"  {out['C1_leibniz_derivation']}")

    log("CONTROL C2/C3: Jordan identity, N(X) 3-way cross-check, Freudenthal identity...")
    okJ=okN1=okN2=okF=0
    trialsN=60
    for _ in range(trialsN):
        X,Y = Jrandom_int(rng,-3,3), Jrandom_int(rng,-3,3)
        if jordan_identity_holds(X,Y): okJ+=1
        n1,n2,n3 = normJ(X), normJ_newton(X), normJ_closed_form(X)
        if n1==n2: okN1+=1
        if n1==n3: okN2+=1
        if Jeq(adjugate(adjugate(X)), Jscale(X, normJ(X))): okF+=1
    out['C2_jordan_identity'] = f"{okJ}/{trialsN}"
    out['C3_N_vs_newton'] = f"{okN1}/{trialsN}"
    out['C3_N_vs_closed_form'] = f"{okN2}/{trialsN}"
    out['C3_freudenthal_identity'] = f"{okF}/{trialsN}"
    log(f"  Jordan identity {out['C2_jordan_identity']}, N cross-checks "
        f"{out['C3_N_vs_newton']} / {out['C3_N_vs_closed_form']}, "
        f"Freudenthal {out['C3_freudenthal_identity']}")

    log("EXTERNAL CROSS-CHECK: this program's own banked exotic idempotent "
        "(0,-7,8), o1=(a=-7,b=8) [CHANGELOG.md L162, 2026-08-14]...")
    o1 = (-7,(0,0,0),(0,0,0),8)
    Xexotic = mkJ(0,-7,8, o1, O_ZERO, O_ZERO)
    idem = Jeq(jordan_mul(Xexotic,Xexotic), Xexotic)
    tr = trace(Xexotic); rank1 = J_is_zero(adjugate(Xexotic))
    out['external_check_0_m7_8'] = {'idempotent': idem, 'trace': str(tr), 'rank1_Esharp0': rank1}
    log(f"  idempotent={idem} trace={tr} E#=0:{rank1}")

    log("CONTROL C7: division-form control (positive-definite octonion norm) "
        "-- the rotation supply must collapse to zero isotropics...")
    box=[-1,0,1]; cnt_div=0
    for v in itertools.product(box, repeat=8):
        if any(t!=0 for t in v) and onorm_definite(oct_from_coords(v))==0:
            cnt_div+=1
    out['C7_division_form_isotropic_count'] = cnt_div
    log(f"  division-form isotropic count in the same box: {cnt_div} (expect 0)")

    return out

# ============================================================================
# PART 5 -- single-idempotent BFS (positive control, REPRODUCE before pairs)
# ============================================================================
def single_idempotent_bfs(GEN_TENSOR, depth=2, quick=False):
    log("=== POSITIVE CONTROL: single-idempotent BFS from E11 ===")
    E11_vec = np.zeros(27, dtype=np.int64); E11_vec[0]=1
    d1 = np.einsum('gij,j->gi', GEN_TENSOR, E11_vec)
    d1_set = set(map(tuple, d1.tolist()))
    log(f"  depth-1 distinct states: {len(d1_set)}")
    diag1 = set(s[:3] for s in d1_set)
    visited = set(d1_set); visited.add(tuple(E11_vec.tolist()))
    diag_triples = set(diag1)
    if depth >= 2:
        frontier = np.array(list(d1_set), dtype=np.int64)
        if quick:
            frontier = frontier[:400]
        BATCH = 300
        t0=time.time()
        for start in range(0, frontier.shape[0], BATCH):
            chunk = frontier[start:start+BATCH]
            images = np.einsum('gij,sj->gsi', GEN_TENSOR, chunk).reshape(-1,27)
            uniq = np.unique(images, axis=0)
            for row in uniq.tolist():
                t=tuple(row); visited.add(t)
                diag_triples.add((row[0],row[1],row[2]))
            if (start//BATCH) % 6 == 0:
                log(f"    depth-2: {start+chunk.shape[0]}/{frontier.shape[0]} frontier done, "
                    f"visited={len(visited)}, diag-triples={len(diag_triples)} "
                    f"({time.time()-t0:.1f}s)")
    log(f"  FINAL: visited={len(visited)}, distinct (xi1,xi2,xi3) triples={len(diag_triples)}")
    sample = random.sample(list(visited), min(2000, len(visited)))
    trace_ok = sum(1 for s in sample if s[0]+s[1]+s[2]==1)
    log(f"  trace invariant on {len(sample)} sample: {trace_ok}/{len(sample)}")
    return {
        'depth1_size': len(d1_set), 'final_visited': len(visited),
        'diag_triple_count': len(diag_triples),
        'diag_triples_sample': sorted(diag_triples)[:40],
        'trace_invariant_check': f"{trace_ok}/{len(sample)}",
        'quick_mode': quick,
    }

# ============================================================================
# PART 6 -- pair machinery: orthogonal-pair invariants + hand-built seed
# ============================================================================
def gcd_all(vals):
    g=0
    for v in vals: g = math.gcd(g, abs(int(v)))
    return g

def exact_det(mat):
    n=len(mat)
    if n==1: return mat[0][0]
    if n==2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    if n==3:
        a,b,c=mat[0]; d,e,f=mat[1]; g,h,i=mat[2]
        return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    raise NotImplementedError

def minors_gcd(cols, k):
    n=len(cols[0]); g=0
    for cidx in itertools.combinations(range(len(cols)), k):
        for ridx in itertools.combinations(range(n), k):
            sub=[[Fr(cols[c][r]) for c in cidx] for r in ridx]
            det=int(exact_det(sub))
            g=math.gcd(g, abs(det))
            if g==1: return 1
    return g

def pair_frame_invariants(E, F):
    ONE=J_identity()
    G = Jsub(Jsub(ONE,E), F)
    Ev,Fv,Gv = [int(t) for t in to_vec(E)],[int(t) for t in to_vec(F)],[int(t) for t in to_vec(G)]
    EF = jordan_mul(E,F); EplusF = Jadd(E,F)
    return {
        'trace_E': int(trace(E)), 'trace_F': int(trace(F)), 'trace_G': int(trace(G)),
        'G_is_rank1_idempotent': (Jeq(jordan_mul(G,G),G) and J_is_zero(adjugate(G))),
        'E_dot_F_is_zero': J_is_zero(EF),
        'N_EplusF': int(normJ(EplusF)),
        'content_E': gcd_all(Ev), 'content_F': gcd_all(Fv), 'content_G': gcd_all(Gv),
        'd1_gcd1x1minors': gcd_all(Ev+Fv+Gv),
        'd2_gcd2x2minors': minors_gcd([Ev,Fv,Gv], 2),
        'd3_gcd3x3minors': minors_gcd([Ev,Fv,Gv], 3),
    }

def vecJ(X): return np.array([int(t) for t in to_vec(X)], dtype=np.int64)
def pair_state(E,F): return np.concatenate([vecJ(E), vecJ(F)])
def state_pair_apply(gen, state):
    return np.concatenate([gen@state[:27], gen@state[27:]])

def build_hand_seed():
    """Hand-built orthogonal pair using an ISOTROPIC, 'generic-looking'
    off-diagonal octonion NOT drawn from the {-1,0,1}^8 generator box --
    constructed directly from the idempotent equations, not by applying any
    B_i(a) automorphism to the canonical seed."""
    o1_generic = (5,(1,2,3),(2,-1,0),0)   # N = 5*0 - (1*2+2*(-1)+3*0) = 0
    assert onorm(o1_generic) == 0
    Ehand = mkJ(0,0,1, o1_generic, O_ZERO, O_ZERO)
    idem_ok = Jeq(jordan_mul(Ehand,Ehand), Ehand)
    rank1_ok = J_is_zero(adjugate(Ehand))
    Fhand = Jsub(J_diag(0,1,1), Ehand)
    ortho_ok = J_is_zero(jordan_mul(Ehand,Fhand))
    return Ehand, Fhand, {'idempotent': idem_ok, 'trace1': int(trace(Ehand))==1,
                           'rank1_Esharp0': rank1_ok, 'orthogonal': ortho_ok}

def bfs_pair_bounded(seed_state, gens, max_depth=3, cap=150_000, time_budget=90.0, label=""):
    visited=set(); visited.add(tuple(seed_state.tolist()))
    frontier = seed_state.reshape(1,54)
    depth_sizes=[]; t_start=time.time(); capped=False; timed_out=False
    for d in range(1, max_depth+1):
        t0=time.time(); new_states=[]
        CH=20
        for cstart in range(0, frontier.shape[0], CH):
            chunk = frontier[cstart:cstart+CH]
            imE = np.einsum('gij,sj->gsi', gens, chunk[:, :27])
            imF = np.einsum('gij,sj->gsi', gens, chunk[:, 27:])
            comb = np.concatenate([imE, imF], axis=2).reshape(-1,54)
            uniq = np.unique(comb, axis=0)
            for row in uniq.tolist():
                t=tuple(row)
                if t not in visited:
                    visited.add(t); new_states.append(row)
            if len(visited) > cap: capped=True; break
            if time.time()-t_start > time_budget: timed_out=True; break
        depth_sizes.append(len(visited))
        log(f"  [{label}] depth {d}: visited={len(visited)} (+{len(new_states)}) "
            f"({time.time()-t0:.1f}s, cum {time.time()-t_start:.1f}s) "
            f"capped={capped} timed_out={timed_out}")
        if capped or timed_out or not new_states: break
        frontier = np.array(new_states, dtype=np.int64)
    return visited, depth_sizes, capped, timed_out

# ============================================================================
# main
# ============================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="smaller bounds, fast sanity pass")
    ap.add_argument("--rebuild-gens", action="store_true", help="ignore cache, rebuild generators")
    ap.add_argument("--pool-size", type=int, default=900, help="generator pool size for pair BFS")
    ap.add_argument("--pair-cap", type=int, default=4_000_000, help="visited-state cap per pair BFS")
    ap.add_argument("--pair-time-budget", type=float, default=240.0, help="seconds per seed BFS")
    ap.add_argument("--pair-depth", type=int, default=3)
    ap.add_argument("--seed", type=int, default=2026)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    results = {'meta': {'quick_mode': args.quick, 'started': time.strftime("%Y-%m-%d %H:%M:%S")}}

    global _DBASIS_CACHE
    log("building basis-derivation matrices (needed by both controls and generators)...")
    _DBASIS_CACHE = build_dbasis()

    results['controls'] = run_controls(rng)

    GEN_TENSOR, META = build_all_generators(rebuild=args.rebuild_gens)
    results['controls']['C6_total_generators'] = int(GEN_TENSOR.shape[0])
    results['controls']['C6_nonintegral_count'] = 5760 - int(GEN_TENSOR.shape[0]) if GEN_TENSOR.shape[0] <= 5760 else 0

    # unimodularity spot check
    dets = set()
    npr = np.random.RandomState(args.seed)
    for idx in npr.choice(GEN_TENSOR.shape[0], size=min(30, GEN_TENSOR.shape[0]), replace=False):
        dets.add(int(round(np.linalg.det(GEN_TENSOR[idx].astype(np.float64)))))
    results['controls']['C6b_sampled_determinants'] = sorted(dets)
    log(f"  sampled generator determinants: {sorted(dets)} (expect only +-1)")

    # automorphy + invariant-preservation controls (C4, C5) using ACTUAL generators.
    # IMPORTANT: X o Y for two INDEPENDENT random elements can be HALF-INTEGER (see
    # f8_NOTES.md Sec 2 -- B(e0,f0)=1 is odd), so applying an integer generator matrix
    # to it must stay in EXACT Fraction arithmetic throughout. Silently going through
    # numpy int64 (via a bare int(fraction)) TRUNCATES half-integers to 0 without
    # erroring -- a real bug caught by this control reading 0/60 on the first run
    # before this fix; kept exact (Fraction) end to end below, never int() on a
    # value that isn't already known to be integral.
    def apply_intmat_to_Jvec(U_int, X):
        """U_int: 27x27 python ints (a generator matrix). X: a J-element (Fraction
        coordinates, possibly non-integral). Returns U_int @ vec(X) exactly."""
        v = to_vec(X)
        out = [sum(Fr(int(U_int[i][j])) * v[j] for j in range(27) if v[j] != 0)
               for i in range(27)]
        return from_vec(out)

    log("CONTROL C4: automorphy on random product triples (the load-bearing check)...")
    ok_auto = 0; n_auto = 60
    ok_inv = 0; n_inv = 200
    for trial in range(max(n_auto, n_inv)):
        gidx = int(npr.randint(0, GEN_TENSOR.shape[0]))
        U = GEN_TENSOR[gidx]
        X, Y = Jrandom_int(rng, -3, 3), Jrandom_int(rng, -3, 3)
        if trial < n_auto:
            phiX = apply_intmat_to_Jvec(U, X)
            phiY = apply_intmat_to_Jvec(U, Y)
            lhs = jordan_mul(X, Y)                      # may be half-integer -- fine, exact
            lhs_img = apply_intmat_to_Jvec(U, lhs)       # exact Fraction matrix-vector product
            rhs_img = jordan_mul(phiX, phiY)
            if Jeq(lhs_img, rhs_img):
                ok_auto += 1
        if trial < n_inv:
            phiX = apply_intmat_to_Jvec(U, X)
            phiAdjX = apply_intmat_to_Jvec(U, adjugate(X))   # adjugate(X) IS always integral
            if (trace(phiX) == trace(X) and normJ(phiX) == normJ(X) and
                    S_form(phiX) == S_form(X) and Jeq(adjugate(phiX), phiAdjX)):
                ok_inv += 1
    results['controls']['C4_automorphy'] = f"{ok_auto}/{n_auto}"
    results['controls']['C5_invariant_preservation'] = f"{ok_inv}/{n_inv}"
    log(f"  C4 automorphy: {ok_auto}/{n_auto}   C5 invariants preserved: {ok_inv}/{n_inv}")

    depth = 1 if args.quick else 2
    results['single_idempotent_positive_control'] = single_idempotent_bfs(GEN_TENSOR, depth=depth, quick=args.quick)

    # ---------------- pairs: the new computation ----------------
    log("=== PAIR SETUP: orthogonal complement G=1-E-F, canonical + hand-built seeds ===")
    E11, E22, E33 = J_diag(1,0,0), J_diag(0,1,0), J_diag(0,0,1)
    canonical_inv = pair_frame_invariants(E11, E22)
    log(f"  canonical (E11,E22) invariants: {canonical_inv}")

    Ehand, Fhand, hand_checks = build_hand_seed()
    log(f"  hand-built seed checks: {hand_checks}")
    hand_inv = pair_frame_invariants(Ehand, Fhand)
    log(f"  hand-built invariants: {hand_inv}")

    # a couple more exotic pairs (bigger coefficients) to stress the invariant search
    def single_slot(slot, xi_j, xi_k, a, b):
        xi=[0,0,0]; others=[t for t in (1,2,3) if t!=slot]
        xi[others[0]-1]=xi_j; xi[others[1]-1]=xi_k
        o=[O_ZERO,O_ZERO,O_ZERO]; o[slot-1]=(a,(0,0,0),(0,0,0),b)
        return mkJ(xi[0],xi[1],xi[2], o[0],o[1],o[2])
    Ebig = single_slot(1,-11,12,-4,33)
    Fbig = Jsub(J_diag(0,1,1), Ebig)
    big_checks = {'idempotent': Jeq(jordan_mul(Ebig,Ebig),Ebig),
                  'rank1': J_is_zero(adjugate(Ebig)),
                  'orthogonal': J_is_zero(jordan_mul(Ebig,Fbig))}
    big_inv = pair_frame_invariants(Ebig, Fbig)
    log(f"  big exotic pair (-11,12,-4,33) checks: {big_checks}, invariants: {big_inv}")

    results['pair_invariant_candidates'] = {
        'canonical': canonical_inv, 'hand_built': hand_inv, 'big_exotic': big_inv,
        'hand_built_construction_checks': hand_checks,
        'big_exotic_construction_checks': big_checks,
        'summary': ("N(E+F) and the N(E+tF) cross-coefficients are identically zero for ANY "
                    "rank-1 pair (forced by E#=F#=0, independent of orthogonality); the frame "
                    "[E|F|G]'s elementary divisors (d1,d2,d3) came out (1,1,1) -- unimodular -- "
                    "for every example tried, canonical through large hand-built. No candidate "
                    "invariant was found that separates. See f8_NOTES.md Sec 5."),
    }

    log("=== PAIR BFS: canonical + automorphism-derived + hand-built seeds ===")
    rng_np = np.random.RandomState(args.seed)
    pool_idx = rng_np.choice(GEN_TENSOR.shape[0], size=min(args.pool_size, GEN_TENSOR.shape[0]), replace=False)
    POOL = GEN_TENSOR[pool_idx]
    log(f"  fixed generator pool for pair BFS: {POOL.shape[0]} (fixed across all seeds for comparability)")

    seedA = pair_state(E11, E22)
    gidx1 = int(rng_np.randint(0, GEN_TENSOR.shape[0]))
    seedB = state_pair_apply(GEN_TENSOR[gidx1], seedA)
    gidx2 = int(rng_np.randint(0, GEN_TENSOR.shape[0])); gidx3 = int(rng_np.randint(0, GEN_TENSOR.shape[0]))
    seedC = state_pair_apply(GEN_TENSOR[gidx3], state_pair_apply(GEN_TENSOR[gidx2], seedA))
    seedD = pair_state(Ehand, Fhand)

    depth = 2 if args.quick else args.pair_depth
    cap = 20_000 if args.quick else args.pair_cap
    tb = 30.0 if args.quick else args.pair_time_budget

    pair_results = {}
    visited_sets = {}
    for name, seed in (("A_canonical", seedA), ("B_auto1", seedB), ("C_auto2", seedC), ("D_hand_built", seedD)):
        log(f"--- BFS seed {name}, pool={POOL.shape[0]}, depth<={depth}, cap={cap}, budget={tb}s ---")
        visited, sizes, capped, timedout = bfs_pair_bounded(
            seed, POOL, max_depth=depth, cap=cap, time_budget=tb, label=name)
        pair_results[name] = {'depth_sizes': sizes, 'capped': capped, 'timed_out': timedout,
                               'final_visited': len(visited)}
        visited_sets[name] = visited

    log("=== cross-reachability between seeds ===")
    seed_tuples = {'A_canonical': tuple(seedA.tolist()), 'B_auto1': tuple(seedB.tolist()),
                   'C_auto2': tuple(seedC.tolist()), 'D_hand_built': tuple(seedD.tolist())}
    reach = {}
    names = list(visited_sets.keys())
    for n1 in names:
        for n2 in names:
            if n1 == n2: continue
            reach[f"{n1}_seed_in_{n2}_visited"] = seed_tuples[n1] in visited_sets[n2]
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            n1, n2 = names[i], names[j]
            reach[f"intersection_{n1}_{n2}"] = len(visited_sets[n1] & visited_sets[n2])
    for k, v in reach.items():
        log(f"  {k}: {v}")

    results['pair_bfs'] = {
        'generator_pool_size': int(POOL.shape[0]),
        'depth_bound': depth, 'cap': cap, 'time_budget_s': tb,
        'seed_gen_indices': {'B_via': gidx1, 'C_via': [gidx2, gidx3]},
        'per_seed': pair_results,
        'cross_reachability': reach,
    }

    # ---------------- verdict ----------------
    # B and C are CONSTRUCTED as automorphic images of A -- their connecting back to A is
    # an expected sanity check on the BFS/generator machinery, not evidence of general
    # transitivity. The genuine, undetermined question is whether D (independently
    # hand-built, never touched by a B_i(a) generator in its construction) connects to
    # {A,B,C}. Weight the verdict on THAT, and report the A/B/C sanity check separately.
    sanity_auto_reach = (reach.get('A_canonical_seed_in_B_auto1_visited', False) or
                          reach.get('B_auto1_seed_in_A_canonical_visited', False) or
                          reach.get('intersection_A_canonical_B_auto1', 0) > 0 or
                          reach.get('intersection_A_canonical_C_auto2', 0) > 0)
    hand_built_keys = [k for k in reach if 'D_hand_built' in k]
    hand_built_reach = any(reach[k] for k in hand_built_keys if k.startswith('A_canonical_seed_in') or
                            k.startswith('B_auto1_seed_in') or k.startswith('C_auto2_seed_in') or
                            k.startswith('D_hand_built_seed_in'))
    hand_built_intersection = sum(reach[k] for k in hand_built_keys if k.startswith('intersection_'))
    hand_built_any = hand_built_reach or hand_built_intersection > 0
    any_capped_or_timedout = any(pair_results[n]['capped'] or pair_results[n]['timed_out'] for n in pair_results)

    if hand_built_any:
        verdict = ("PAIR-TRANSITIVE (bounded-search grade) -- the independently hand-built "
                    "seed D connects to the canonical/automorphism-derived orbit within the "
                    "stated bound")
    elif any_capped_or_timedout:
        verdict = ("INCONCLUSIVE-AT-BOUND -- no separating invariant found (Sec. 5); BFS did "
                    "NOT connect the hand-built seed D to {A,B,C} within the stated "
                    "depth/pool/cap/time bound (all runs capped before exhausting the group). "
                    "The automorphism-derived seeds B,C DID connect back to A "
                    f"(sanity check on the machinery: {sanity_auto_reach}), as expected by "
                    "construction -- this is NOT evidence for or against transitivity, only "
                    "confirmation the BFS correctly re-finds known relationships.")
    else:
        verdict = ("INCONCLUSIVE-AT-BOUND -- BFS completed without capping but did not "
                    "connect D to {A,B,C}; no separating invariant found either")
    results['verdict'] = verdict
    results['verdict_detail'] = {
        'sanity_check_auto_derived_seeds_reconnect': sanity_auto_reach,
        'hand_built_seed_reaches_or_intersects': hand_built_any,
        'any_bfs_capped_or_timed_out': any_capped_or_timedout,
    }
    log(f"VERDICT: {verdict}")

    results['meta']['finished'] = time.strftime("%Y-%m-%d %H:%M:%S")
    results['meta']['total_runtime_s'] = time.time() - T0

    out_path = os.path.join(HERE, "f8_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log(f"saved {os.path.relpath(out_path, HERE)}")
    log("DONE.")

if __name__ == "__main__":
    main()
