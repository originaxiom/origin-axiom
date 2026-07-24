#!/usr/bin/env python3
"""W4-192 -- H118: the Baez-Schwahn F4 nested-Jordan door (arXiv:2606.15235).

QUESTION (Gate-5-Q sensitive, STRUCTURAL only):
  h2(C) subset h3(C) subset h3(O) is a nested chain in the exceptional Jordan
  algebra J = h3(O) (27-dim), Aut(J)=F4 (52-dim).  The subgroup of F4 that
  preserves the nested pair has Lie algebra of dim 12 = dim(su3 (+) su2 (+) u1)
  -- the "fifth F4 door".  Does ANY object structure CANONICALLY select this
  qubit-qutrit nested pair, or is the pair a CHOICE from a positive-dimensional
  moduli (same disease as the four closed F4 routes: faces on different
  subalgebras)?

  This cell frames every observable as a property of the Jordan algebra / its
  derivation Lie algebra / F4-orbits.  NO SM-value claim, NO physics reading,
  nothing to CLAIMS.  E20 is applied to any specialness: canonical selection
  would require a ZERO-dimensional (rigid, F4-unique) nested pair; a positive
  orbit dimension is decisive evidence AGAINST canonicity.

WHAT IS COMPUTED IN-CELL (no cited numbers; every fact derived here):
  1. der(O) = g2:  dim of derivation algebra of the octonions      (expect 14)
  2. der(J) = f4:  dim of derivation algebra of h3(O)               (expect 52)
     -- both from an explicit octonion multiplication table + nullspace solve.
  3. Stab_{f4}(nested C-pair):  D in f4 with D(h3C)<=h3C, D(h2C)<=h2C
     -- the DOOR: dim = 12 (= dim su3+su2+u1) if the door is real.
  4. COMPARATOR CONTROL (E20): the SAME recipe with the composition
     subalgebra R and H in place of C:
        Stab_{f4}(nested R-pair),  Stab_{f4}(nested H-pair).
     If these differ from 12, the recipe does NOT privilege C; the C
     (qubit-qutrit) choice is INPUT BY HAND, not selected by the recipe.
  5. NON-CANONICITY (moduli / F4-transitivity):
     (a) complex-structure orbit: dim{ D(e1) : D in der(O) } = tangent to the
         G2-orbit of a complex structure inside O   (expect 6 = S^6).
     (b) idempotent orbit:        dim{ D(E33) : D in f4 } = tangent to the
         F4-orbit of a primitive idempotent (OP^2)   (expect 16).
     Positive orbit dims  =>  the "which C, which h2 block" data lives on a
     continuous F4/G2-orbit  =>  NO canonical point.

VERDICT LOGIC (in code, can emit A / B / UNRESOLVED, non-vacuous):
  construction must first check out (f4_dim==52, g2_dim==14) else UNRESOLVED.
  door_exists := stab_C_dim == 12.
  canonical   := (cstruct_orbit_dim == 0) and (idemp_orbit_dim == 0)
                 and (comparators single out C uniquely as forced, not chosen).
  RESOLVED-A  if door_exists and canonical selection shown.
  RESOLVED-B  if door_exists but the nested pair sits on positive-dim moduli
              (no canonical selection) -- the expected close-by-computation.
  UNRESOLVED  if the construction is inconsistent.

Re-runnable: pyenv python3, needs numpy only.
"""
import json, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
def log(*a): print(f"[{time.time()-T0:7.2f}s]", *a, flush=True)

# ----------------------------------------------------------------- octonions
# Basis e0=1, e1..e7.  Oriented Fano triples (i, i+1, i+3 mod 7, 1-indexed):
# on a line (a,b,c):  e_a e_b = e_c,  e_b e_c = e_a,  e_c e_a = e_b  (cyclic +),
# reversed pairs give the negative.  e_i^2 = -1.  This is a consistent
# (alternative, non-associative) octonion algebra.
TRIPLES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
# prod[(i,j)] = (sign, k) meaning e_i e_j = sign * e_k   (i,j in 1..7, i!=j)
_prod = {}
for (a,b,c) in TRIPLES:
    for (i,j,k) in [(a,b,c),(b,c,a),(c,a,b)]:
        _prod[(i,j)] = (+1,k)
        _prod[(j,i)] = (-1,k)

def omul(u, v):
    """octonion product of two length-8 real vectors."""
    w = np.zeros(8)
    for i in range(8):
        if u[i] == 0: continue
        for j in range(8):
            if v[j] == 0: continue
            ui, vj = u[i], v[j]
            if i == 0:          # 1 * e_j = e_j
                w[j] += ui*vj
            elif j == 0:        # e_i * 1 = e_i
                w[i] += ui*vj
            elif i == j:        # e_i^2 = -1
                w[0] -= ui*vj
            else:
                s,k = _prod[(i,j)]
                w[k] += s*ui*vj
    return w

def oconj(u):
    c = -u.copy(); c[0] = u[0]; return c

# sanity: alternative algebra, norm multiplicative on basis
for i in range(8):
    ei = np.zeros(8); ei[i]=1
    n = omul(ei, oconj(ei))
    assert abs(n[0]-1) < 1e-12 and np.allclose(n[1:],0), ("norm", i, n)

# ----------------------------------------------- exceptional Jordan algebra J
# vec27 layout: [a,b,c, x(8), y(8), z(8)]  <->  3x3 Hermitian octonion matrix
#   M = [[a, z, conj(y)],
#        [conj(z), b, x],
#        [y, conj(x), c]]
IA,IB,IC = 0,1,2
IX = slice(3,11); IY = slice(11,19); IZ = slice(19,27)

def vec_to_mat(v):
    M = np.zeros((3,3,8))
    M[0,0,0]=v[IA]; M[1,1,0]=v[IB]; M[2,2,0]=v[IC]
    z=v[IZ]; x=v[IX]; y=v[IY]
    M[0,1]=z;        M[1,0]=oconj(z)
    M[1,2]=x;        M[2,1]=oconj(x)
    M[2,0]=y;        M[0,2]=oconj(y)
    return M

def mat_to_vec(M):
    v = np.zeros(27)
    v[IA]=M[0,0,0]; v[IB]=M[1,1,0]; v[IC]=M[2,2,0]
    v[IZ]=M[0,1]; v[IX]=M[1,2]; v[IY]=M[2,0]
    return v

def matmul_oct(A,B):
    C = np.zeros((3,3,8))
    for i in range(3):
        for k in range(3):
            acc = np.zeros(8)
            for j in range(3):
                acc += omul(A[i,j], B[j,k])
            C[i,k]=acc
    return C

def jordan(u, v):
    """Jordan product u o v = (UV+VU)/2 on vec27; result is Hermitian."""
    U = vec_to_mat(u); V = vec_to_mat(v)
    P = matmul_oct(U,V); Q = matmul_oct(V,U)
    M = 0.5*(P+Q)
    # M must be Hermitian: diag imaginary ~0, M[j,i]=conj(M[i,j])
    for d in range(3):
        assert abs(M[d,d,1:]).max() < 1e-9, "diag not real"
    return mat_to_vec(M)

# structure constants J[i,j,:]  (27x27x27), symmetric in i,j
N = 27
BASIS = np.eye(N)
Jc = np.zeros((N,N,N))
for i in range(N):
    for j in range(i, N):
        p = jordan(BASIS[i], BASIS[j])
        Jc[i,j] = p; Jc[j,i] = p
# commutativity assert
assert np.allclose(Jc, Jc.transpose(1,0,2)), "Jordan product not commutative"
# identity element e = diag(1,1,1) = a+b+c basis sum ; e o X = X
e_id = np.zeros(N); e_id[IA]=e_id[IB]=e_id[IC]=1
for i in range(N):
    assert np.allclose(jordan(e_id, BASIS[i]), BASIS[i]), ("identity", i)
log("Jordan algebra J=h3(O) built: dim", N, " identity + commutativity OK")

# ---------------------------------------------- rank / nullspace via SVD gap
def nullspace(A, name=""):
    """return (dim, basis columns Nx k, gap) for null(A) with a reported
    singular-value gap justifying the rank cut; rank stable at 2 tolerances."""
    if A.shape[0] == 0:
        return A.shape[1], np.eye(A.shape[1]), np.inf
    U,S,Vt = np.linalg.svd(A, full_matrices=True)
    smax = S[0] if S.size else 1.0
    tol1 = smax*1e-8*max(A.shape)
    tol2 = smax*1e-6*max(A.shape)
    r1 = int((S > tol1).sum()); r2 = int((S > tol2).sum())
    n = A.shape[1]
    # gap ratio between smallest "nonzero" and largest "zero" singular value
    nz = S[S > tol1]
    zr = S[S <= tol1]
    gap = (nz.min()/zr.max()) if (nz.size and zr.size and zr.max()>0) else np.inf
    assert r1 == r2, (name, "rank unstable across tol", r1, r2, S[max(0,r1-2):r1+2])
    dim = n - r1
    Nb = Vt[r1:].T.copy()  # columns span null space
    return dim, Nb, gap

# ---------------------------------------------- der(O) = g2  (dim expect 14)
# D in R^{8x8}, D(1)=0, D(uv)=D(u)v + u D(v).  Build linear constraints.
def oct_struct():
    S = np.zeros((8,8,8))
    for i in range(8):
        for j in range(8):
            S[i,j] = omul(BASIS8[i], BASIS8[j])
    return S
BASIS8 = np.eye(8)
Sc = oct_struct()   # Sc[i,j,k]: e_i e_j = sum_k Sc[i,j,k] e_k

# unknowns D[m,p] (64). Constraint for each (i,j,k):
#  sum_p S[i,j,p] D[k,p] - sum_m D[m,i] S[m,j,k] - sum_n D[n,j] S[i,n,k] = 0
rows = []
for i in range(8):
    for j in range(8):
        for k in range(8):
            row = np.zeros((8,8))
            for p in range(8): row[k,p] += Sc[i,j,p]
            for m in range(8): row[m,i] -= Sc[m,j,k]
            for nn in range(8): row[nn,j] -= Sc[i,nn,k]
            rows.append(row.reshape(-1))
# also D(1)=0 (D e0 = 0): D[:,0]=0
for m in range(8):
    r = np.zeros((8,8)); r[m,0]=1; rows.append(r.reshape(-1))
A_g2 = np.array(rows)
g2_dim, g2_null, g2_gap = nullspace(A_g2, "g2")
log(f"der(O)=g2 dim = {g2_dim}  (expect 14), svd-gap ~ {g2_gap:.1e}")

# ---------------------------------------------- der(J) = f4  (dim expect 52)
# unknowns D[k,p] (729). constraint per (i<=j, k):
#  sum_p J[i,j,p] D[k,p] - sum_m D[m,i] J[m,j,k] - sum_n D[n,j] J[i,n,k] = 0
rows = []
for i in range(N):
    for j in range(i, N):
        Jij = Jc[i,j]
        for k in range(N):
            row = np.zeros((N,N))
            row[k,:] += Jij                 # + sum_p J[i,j,p] D[k,p]
            row[:,i] -= Jc[:,j,k]           # - sum_m D[m,i] J[m,j,k]
            row[:,j] -= Jc[i,:,k]           # - sum_n D[n,j] J[i,n,k]
            rows.append(row.reshape(-1))
A_f4 = np.array(rows)
log(f"f4 constraint matrix {A_f4.shape}")
f4_dim, f4_null, f4_gap = nullspace(A_f4, "f4")   # f4_null: 729 x f4_dim
log(f"der(J)=f4 dim = {f4_dim}  (expect 52), svd-gap ~ {f4_gap:.1e}")

# derivation basis as k x (N,N) matrices
Dbasis = [f4_null[:,a].reshape(N,N) for a in range(f4_dim)]

# ---------------------------------------- subalgebra index sets (vec27 coords)
def oct_idx(base, comps):  # base=3(x)/11(y)/19(z), comps subset of 0..7
    return [base+c for c in comps]

def chain(Kcomps):
    """indices for h3(K) and h2(K) with octonion sub-basis Kcomps (0 in it)."""
    h3 = [IA,IB,IC] + oct_idx(3,Kcomps) + oct_idx(11,Kcomps) + oct_idx(19,Kcomps)
    h2 = [IA,IB] + oct_idx(19,Kcomps)          # a,b diag + z off-diag(1,2)
    return sorted(h3), sorted(h2)

C_comps = [0,1]            # C = <e0,e1>
R_comps = [0]              # R = <e0>
H_comps = [0,1,2,4]        # H = <e0,e1,e2,e4> (e1e2=e4 line (1,2,4)) quaternions

def is_subalgebra(idx):
    idx = set(idx)
    for i in idx:
        for j in idx:
            p = Jc[i,j]
            leak = [k for k in range(N) if k not in idx and abs(p[k])>1e-9]
            if leak: return False
    return True

def stab_dim(idx_sets, name):
    """dim of { D in f4 : D(S)<=S for every S in idx_sets }."""
    for s in idx_sets:
        assert is_subalgebra(s), (name, "not a Jordan subalgebra", s)
    rows = []
    for S in idx_sets:
        Sset = set(S); out = [k for k in range(N) if k not in Sset]
        for a in range(f4_dim):
            pass
        # leakage: for each s in S, each out-coord o: (D s)_o = sum_a c_a Dbasis[a][o,s]
        for s in S:
            for o in out:
                row = np.array([Dbasis[a][o,s] for a in range(f4_dim)])
                rows.append(row)
    A = np.array(rows) if rows else np.zeros((0,f4_dim))
    d,_,gap = nullspace(A, name)
    return d, gap

h3C,h2C = chain(C_comps)
h3R,h2R = chain(R_comps)
h3H,h2H = chain(H_comps)
assert len(h3C)==9 and len(h2C)==4, (len(h3C),len(h2C))
assert len(h3R)==6 and len(h2R)==3
assert len(h3H)==15 and len(h2H)==6

stabC_dim, gC = stab_dim([h3C,h2C], "stab_nested_C")
stabR_dim, gR = stab_dim([h3R,h2R], "stab_nested_R")
stabH_dim, gH = stab_dim([h3H,h2H], "stab_nested_H")
# also the un-nested stabilizers (just h3K) for context
stabC3_dim,_ = stab_dim([h3C], "stab_h3C")
log(f"Stab_f4(nested C) dim = {stabC_dim}   (h3C alone = {stabC3_dim})")
log(f"Stab_f4(nested R) dim = {stabR_dim}")
log(f"Stab_f4(nested H) dim = {stabH_dim}")

# ---------------------------------------- NON-CANONICITY: orbit tangent dims
# (a) complex-structure orbit: tangent = { D(e1) : D in der(O) }, dim of image
e1 = BASIS8[1]
img = np.array([ (g2_null[:,a].reshape(8,8) @ e1) for a in range(g2_dim) ])  # k x 8
# rank of img.T (8 x k): dimension of the orbit tangent space
_, S_img, _ = np.linalg.svd(img.T, full_matrices=False)
tol = (S_img[0] if S_img.size else 1.0)*1e-8*8
cstruct_orbit_dim = int((S_img > tol).sum())
log(f"complex-structure orbit tangent dim = {cstruct_orbit_dim}  (expect 6 = S^6)")

# (b) idempotent orbit: tangent = { D(E33) : D in f4 }, E33 = diag(0,0,1)
E33 = np.zeros(N); E33[IC]=1
imgJ = np.array([ (Dbasis[a] @ E33) for a in range(f4_dim) ])  # k x 27
_, S_imgJ, _ = np.linalg.svd(imgJ.T, full_matrices=False)
tolJ = (S_imgJ[0] if S_imgJ.size else 1.0)*1e-8*27
idemp_orbit_dim = int((S_imgJ > tolJ).sum())
log(f"primitive-idempotent orbit tangent dim = {idemp_orbit_dim}  (expect 16 = OP^2)")

# ------------------------------------------------------------- verdict (in code)
f4_ok = (f4_dim == 52) and (g2_dim == 14)
door_exists = (stabC_dim == 12)          # 12 = dim(su3 (+) su2 (+) u1)
# E20: canonical selection would require BOTH the complex structure and the
# nested idempotent (h2 block) to be RIGID (zero-dim F4/G2-orbit) so that the
# object has no freedom in the pick.  Comparator: the recipe privileges C only
# if C alone yields the 12-dim stabilizer AND R,H are somehow excluded by the
# recipe itself (they are not -- they are just different composition-algebra
# inputs, each a legitimate nested chain giving its own stabilizer).
comparators_show_C_is_a_choice = (stabR_dim != stabC_dim) and (stabH_dim != stabC_dim)
noncanonical = (cstruct_orbit_dim > 0) or (idemp_orbit_dim > 0)

if not f4_ok:
    verdict = "UNRESOLVED"
    headline = f"construction inconsistent (f4={f4_dim}!=52 or g2={g2_dim}!=14)"
elif door_exists and (cstruct_orbit_dim == 0 and idemp_orbit_dim == 0
                       and not comparators_show_C_is_a_choice):
    # a rigid, recipe-forced, F4-unique nested pair -> canonical selection
    verdict = "RESOLVED-A"
    headline = ("nested C-pair is F4-rigid and recipe-forced: the object "
                "canonically selects the qubit-qutrit pair (dim-12 stabilizer)")
elif door_exists and noncanonical:
    verdict = "RESOLVED-B"
    headline = (f"door real (Stab_f4(nested C)=12=dim su3+su2+u1) but the nested "
                f"pair sits on positive-dim moduli (complex-struct orbit "
                f"{cstruct_orbit_dim}, idempotent orbit {idemp_orbit_dim}; "
                f"comparators R={stabR_dim},H={stabH_dim} != 12): NO canonical "
                f"selection -- the qubit-qutrit pair is a choice, not forced")
else:
    verdict = "UNRESOLVED"
    headline = (f"ambiguous: door_exists={door_exists}, stabC={stabC_dim}, "
                f"orbits=({cstruct_orbit_dim},{idemp_orbit_dim})")

discriminating_fact = (
    f"Stab_f4(nested h2(C)<h3(C)<h3(O)) has dim {stabC_dim} "
    f"(= dim su3+su2+u1 = 12 iff door real); but the complex structure inside O "
    f"lies on a {cstruct_orbit_dim}-dim G2-orbit and the h2-selecting idempotent "
    f"on a {idemp_orbit_dim}-dim F4-orbit, and the SAME nested-stabilizer recipe "
    f"gives dim {stabR_dim} for R and {stabH_dim} for H -- so C, and the pair, "
    f"are chosen not canonically forced.")

log("VERDICT:", verdict)
log("HEADLINE:", headline)

results = {
    "cell": "W4-192",
    "hint": "H118",
    "gate": "5-Q (structural only; no SM-value/physics claim; E20 on specialness)",
    "verdict": verdict,
    "headline": headline,
    "discriminating_fact": discriminating_fact,
    "g2_dim": g2_dim,
    "f4_dim": f4_dim,
    "stab_nested_C_dim": stabC_dim,
    "stab_h3C_only_dim": stabC3_dim,
    "stab_nested_R_dim": stabR_dim,
    "stab_nested_H_dim": stabH_dim,
    "complex_structure_orbit_dim": cstruct_orbit_dim,
    "primitive_idempotent_orbit_dim": idemp_orbit_dim,
    "door_exists": bool(door_exists),
    "comparators_show_C_is_a_choice": bool(comparators_show_C_is_a_choice),
    "noncanonical_positive_moduli": bool(noncanonical),
    "svd_gaps": {"g2": float(g2_gap), "f4": float(f4_gap),
                 "stab_C": float(gC), "stab_R": float(gR), "stab_H": float(gH)},
    "notes": ("dim-12 stabilizer is reported as dim(su3 (+) su2 (+) u1), a "
              "Lie-algebra structure fact only; no Standard-Model value or "
              "physics reading is asserted (Gate 5-Q).  The verdict turns on "
              "whether the nested pair is canonically selected (rigid) or "
              "chosen from a moduli space; positive orbit dims => chosen."),
}
with open(os.path.join(HERE,"results.json"),"w") as f:
    json.dump(results, f, indent=2)
log("wrote results.json")
