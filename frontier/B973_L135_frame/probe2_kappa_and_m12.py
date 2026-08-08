"""B973 scout probe 2: rebuild kappa and M12 from the bench's own material.

Recipe taken from the REPO's own definitional document (B911 CMT_DRAFT.md §2,
ingredient list) -- not guessed. Inputs: B854's build only.
"""
import sys, json, time
sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp
import frame
from fractions import Fraction as Fr

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

G = frame._G
DIM, N = frame.DIM, frame.N
ROOTS, BB, C = frame.ROOTS, frame.BB, frame.C
INV = G["INV"]
CH = {n: INV[n] for n in (8, 14, 16, 22)}
R = {}

AD = {n: frame.ad(CH[n]) for n in (8, 14, 16, 22)}
log("ad matrices built")

# ---------- core, floor, and the 18-dim quotient core/floor ----------
core = AD[8].nullspace(); Bc = sp.Matrix.hstack(*core)
P = (Bc.T * Bc).inv() * Bc.T
C14 = P * AD[14] * Bc; C22 = P * AD[22] * Bc
fl = C14.nullspace(); Fc = sp.Matrix.hstack(*fl)
fdim = Fc.shape[1]; cdim = Bc.shape[1]
log(f"core {cdim}, floor {fdim}")

piv = list(sp.Matrix(Fc.T).rref()[1])
comp = [i for i in range(cdim) if i not in piv][: cdim - fdim]
T = sp.Matrix.hstack(Fc, sp.eye(cdim)[:, comp])
Ti = T.inv()
M14 = Ti * C14 * T; M22 = Ti * C22 * T
assert M14[:, :fdim].is_zero_matrix and M22[:, :fdim].is_zero_matrix
Q14 = M14[fdim:, fdim:]; Q22 = M22[fdim:, fdim:]
log(f"quotient dim = {Q14.shape[0]} (18); deg bound deg nu <= 18 PROVEN (18x18, entries affine in s)")

# ---------- nu(s) = det(Q14 + s Q22) by interpolation, 19 nodes + 6 checks ----
s = sp.symbols('s')
def detat(s0):
    return (Q14 + sp.Rational(s0) * Q22).det()
nodes = list(range(19))
vals = [detat(x) for x in nodes]
nu = sp.interpolate(list(zip(nodes, vals)), s)
nu = sp.expand(nu)
checks = all(sp.simplify(nu.subs(s, x) - detat(x)) == 0 for x in range(-6, 0))
log(f"nu degree {sp.degree(nu, s)} (18); 6 extra-node checks: {checks}")
fac = sp.factor_list(sp.Poly(nu, s))
kap = None
for f_, m_ in fac[1]:
    if m_ == 6 and sp.degree(f_, s) == 3:
        kap = sp.Poly(f_, s)
log(f"nu = c * (cubic)^6 : {kap is not None}")
kap_prim = sp.Poly(sp.primitive(kap.as_expr())[1], s)
log(f"kappa = {kap_prim.as_expr()}")
R["kappa"] = str(kap_prim.as_expr())
R["kappa_irreducible"] = bool(kap_prim.is_irreducible)
R["kappa_constant_is_minus_19cubed"] = bool(kap_prim.as_expr().subs(s, 0) == -19**3)
disc = sp.discriminant(kap_prim.as_expr(), s)
R["kappa_disc_squarefree_kernel"] = sorted(int(q) for q in sp.factorint(disc)
                                           if sp.factorint(disc)[q] % 2 == 1)
R["nu_degree"] = int(sp.degree(nu, s)); R["nu_extra_node_checks"] = bool(checks)
log(f"irreducible {R['kappa_irreducible']}; const -19^3 {R['kappa_constant_is_minus_19cubed']}; "
    f"disc squarefree kernel {R['kappa_disc_squarefree_kernel']}")

# ---------- mod-p: the three compact walls, their span, and M12 ----------
kc = [int(kap_prim.as_expr().coeff(s, k)) for k in range(4)]
def rootsp(co, p): return [x for x in range(p) if sum(c*pow(x,k,p) for k,c in enumerate(co)) % p == 0]
denoms = {c.denominator for n in (8,14,16,22) for c in CH[n] if c}
q = 40829
while True:
    q = int(sp.nextprime(q))
    if any(d % q == 0 for d in denoms) or kc[3] % q == 0: continue
    if len(set(rootsp(kc, q))) == 3: break
p = q
log(f"fresh split prime p = {p} (not 40829/40039 etc.)")
R["prime"] = p

def redp(x): x = sp.Rational(x); return x.p % p * pow(x.q % p, p-2, p) % p
def matp(M): return [[redp(M[i,j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
def rankp(rows):
    rows = [r[:] for r in rows]; n = len(rows[0]) if rows else 0; r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p-2, p)
        rows[r] = [v*inv % p for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]; rows[i] = [(a - f*b) % p for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows): break
    return r
def nullp(rows):
    n = len(rows[0]) if rows else DIM
    rows = [r[:] for r in rows]; where = {}; r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p-2, p); rows[r] = [v*inv % p for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]; rows[i] = [(a-f*b) % p for a, b in zip(rows[i], rows[r])]
        where[c] = r; r += 1
    free = [c for c in range(n) if c not in where]
    out = []
    for fc in free:
        v = [0]*n; v[fc] = 1
        for c, rr in where.items(): v[c] = (-rows[rr][fc]) % p
        out.append(v)
    return out

AD14p, AD22p = matp(AD[14]), matp(AD[22])
AD8p, AD16p = matp(AD[8]), matp(AD[16])
def pencil(A, B, t): return [[(A[i][j] + t*B[i][j]) % p for j in range(DIM)] for i in range(DIM)]
sr = sorted(rootsp(kc, p))
W = []
for r0 in sr:
    ker = nullp(pencil(AD14p, AD22p, r0))
    W.append(ker)
    log(f"  compact wall s={r0}: dim z = {len(ker)} (30)")
R["compact_wall_dims"] = [len(w) for w in W]
span = rankp([list(x) for x in zip(*(W[0]+W[1]+W[2]))])
log(f"  triple span = {span} (66)")
R["triple_span"] = span

# exact Killing Gram on the Chevalley basis (sparse), then mod p
K = [[0]*DIM for _ in range(DIM)]
for i in range(N):
    for j in range(N):
        K[i][j] = sum((sum(r[k]*C[i][k] for k in range(N)))*(sum(r[k]*C[j][k] for k in range(N)))
                      for r in ROOTS)
for ri, r in enumerate(ROOTS):
    mi = ROOTS.index(tuple(-x for x in r)); tr = Fr(0)
    for k in range(DIM):
        w = BB[N+mi][k]; acc = Fr(0)
        for pdx, wp in enumerate(w):
            if wp: acc += wp * BB[N+ri][pdx][k]
        tr += acc
    K[N+ri][N+mi] = int(tr)
Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
R["killing_rank_mod_p"] = rankp(Kp)
log(f"  Killing rank mod p = {R['killing_rank_mod_p']} (78)")

rows = [[sum(v[i]*Kp[i][j] for i in range(DIM) if v[i]) % p for j in range(DIM)]
        for v in W[0]+W[1]+W[2]]
M12 = nullp(rows)
R["M12_dim"] = len(M12)
log(f"  M12 = Killing-perp of the 66-span: dim {len(M12)} (12)")
core_cols = [[redp(Bc[i,j]) for i in range(DIM)] for j in range(cdim)]
R["M12_cap_core"] = len(M12) + len(core_cols) - rankp([list(x) for x in zip(*(M12+core_cols))])
log(f"  M12 cap core = {R['M12_cap_core']} (0)")
inv_ok, ranks = [], []
for nm, A in (("g8",AD8p),("g14",AD14p),("g16",AD16p),("g22",AD22p)):
    img = [[sum(A[i][k]*v[k] for k in range(DIM) if v[k]) % p for i in range(DIM)] for v in M12]
    inv_ok.append(rankp([list(x) for x in zip(*(M12+img))]) == len(M12))
    ranks.append(rankp(img))
R["M12_torus_invariant"] = all(inv_ok); R["M12_charge_ranks"] = ranks
log(f"  torus-invariant: {all(inv_ok)}; charge ranks on M12: {ranks} (12,12,12,12)")

json.dump(R, open("/Users/dri/origin-axiom/frontier/B973_L135_frame/scout_probe2_results.json","w"),
          indent=1, sort_keys=True)
log("DONE")
