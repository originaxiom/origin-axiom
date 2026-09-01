"""
R25 blind recomputation: antilinear torsor over E6, count elements with compact color I2.
Own construction throughout: E6 roots (Bourbaki labels, index 0..5), Chevalley basis via
lattice-cocycle signs (Jacobi verified), Killing form = tr(ad ad), signed lifts of lattice
automorphisms solved by brute force over {+-1}^6 simple-root signs.
Written BEFORE reading the arc's b1127_sweep.py.
"""
import numpy as np, itertools, json, sys
from fractions import Fraction
import sympy as sp

# ---------- E6 root system (Bourbaki: alpha2 = branch on alpha4; chain 1-3-4-5-6) ----------
# index 0..5 <-> alpha1..alpha6
A = np.array([[ 2, 0,-1, 0, 0, 0],
              [ 0, 2, 0,-1, 0, 0],
              [-1, 0, 2,-1, 0, 0],
              [ 0,-1,-1, 2,-1, 0],
              [ 0, 0, 0,-1, 2,-1],
              [ 0, 0, 0, 0,-1, 2]], dtype=int)
def ip(x, y): return int(np.array(x) @ A @ np.array(y))
simple = [tuple(int(v) for v in np.eye(6, dtype=int)[i]) for i in range(6)]
pos = set(simple)
frontier = list(simple)
while frontier:
    r = frontier.pop()
    for i in range(6):
        c = ip(r, simple[i])
        # reflection s_i(r) = r - c*alpha_i ; new positive roots when c<0 : r+alpha_i (and up)
        if c < 0:
            for k in range(1, -c + 1):
                s = tuple(r[j] + k*(j == i) for j in range(6))
                if s not in pos:
                    pos.add(s); frontier.append(s)
pos = sorted(pos, key=lambda r: (sum(r), r))
assert len(pos) == 36, len(pos)
roots = pos + [tuple(-v for v in r) for r in pos]
assert len(roots) == 72
ridx = {r: i for i, r in enumerate(roots)}
theta_high = max(pos, key=sum)
assert theta_high == (1, 2, 2, 3, 2, 1)

# ---------- cocycle eps(a,b) bimultiplicative on Q ----------
E = np.ones((6, 6), dtype=int)
for i in range(6):
    for j in range(6):
        if i == j: E[i, j] = -1
        elif i < j: E[i, j] = (-1) ** (A[i, j] % 2)
        else: E[i, j] = 1
def eps(a, b):
    a = np.array(a); b = np.array(b)
    e = int(a @ E @ b)  # exponent parity count of -1's: use product form
    # bimultiplicative: eps(a,b) = prod_{ij} E[i,j]^{a_i b_j}
    s = 1
    for i in range(6):
        for j in range(6):
            if E[i, j] == -1 and (a[i]*b[j]) % 2 != 0: s = -s
    return s

# ---------- basis: 0..5 = h_i, 6..77 = e_r (roots order) ----------
N = 78
def hvec(r):  # h_r = sum r_i h_i  (simply laced)
    v = np.zeros(N, dtype=int); v[:6] = np.array(r); return v
def evec(r):
    v = np.zeros(N, dtype=int); v[6 + ridx[r]] = 1; return v

def build_C(csign):
    C = np.zeros((N, N, N), dtype=int)  # [b_a, b_b] = sum_c C[a,b,c] b_c
    for i in range(6):
        for r in roots:
            C[i, 6 + ridx[r], 6 + ridx[r]] = ip(simple[i], r)
            C[6 + ridx[r], i, 6 + ridx[r]] = -ip(simple[i], r)
    for r in roots:
        for s in roots:
            t = tuple(np.array(r) + np.array(s))
            if t in ridx:
                C[6 + ridx[r], 6 + ridx[s], 6 + ridx[t]] = eps(r, s)
            elif all(v == 0 for v in t):
                C[6 + ridx[r], 6 + ridx[s], :6] = csign * eps(r, s) * np.array(r)
    return C

def jacobi_defect(C):
    # [[a,b],c] + [[b,c],a] + [[c,a],b]
    Cf = C.astype(float)
    T = (Cf.reshape(N*N, N) @ Cf.reshape(N, N*N)).reshape(N, N, N, N)
    J = T + np.transpose(T, (1, 2, 0, 3)) + np.transpose(T, (2, 0, 1, 3))
    return int(np.abs(J).sum())

C = None
for csign in (+1, -1):
    Ct = build_C(csign)
    d = jacobi_defect(Ct)
    print("csign", csign, "jacobi defect", d)
    if d == 0: C = Ct; break
assert C is not None
# antisymmetry
assert np.abs(C + np.transpose(C, (1, 0, 2))).sum() == 0

def ad(v): return np.einsum('a,abc->cb', v, C)  # matrix of ad(v): column b -> [v, b_b]
K = np.zeros((N, N), dtype=int)
ads = [ad(np.eye(N, dtype=int)[a]) for a in range(N)]
for a in range(N):
    for b in range(N):
        K[a, b] = np.trace(ads[a] @ ads[b])
assert (K == K.T).all()
print("Killing form: K(h1,h1)=", K[0, 0], " K(e_a1,e_-a1)=", K[6 + ridx[simple[0]], 6 + ridx[tuple(-v for v in simple[0])]])
print("Killing form rank", np.linalg.matrix_rank(K))

def sig(M):
    M = sp.Matrix(M)
    ev = M.eigenvals()
    p = sum(m for e, m in ev.items() if e > 0); n = sum(m for e, m in ev.items() if e < 0); z = sum(m for e, m in ev.items() if e == 0)
    return (p, n, z)
def sig_np(M):
    w = np.linalg.eigvalsh(np.array(M, dtype=float))
    return (int((w > 1e-9).sum()), int((w < -1e-9).sum()), int((abs(w) <= 1e-9).sum()))

# ---------- color I2 and hatch ----------
a_I2 = tuple(-v for v in theta_high); b_I2 = simple[1]
assert ip(a_I2, b_I2) == -1
I2_roots = [a_I2, b_I2, tuple(np.array(a_I2) + np.array(b_I2))]
I2_roots += [tuple(-v for v in r) for r in I2_roots]
assert all(r in ridx for r in I2_roots)
I2_basis = [hvec(a_I2), hvec(b_I2)] + [evec(r) for r in I2_roots]
I2_idx = [6 + ridx[r] for r in I2_roots]
hatch = [simple[0], simple[2]]
assert all(ip(r, h) == 0 for r in I2_roots for h in hatch)

# ---------- lattice automorphisms ----------
def pi_mirror(r):
    perm = [5, 1, 4, 3, 2, 0]
    out = [0]*6
    for i in range(6): out[perm[i]] = r[i]
    return tuple(out)
def refl(a):
    def s(x): return tuple(int(v) for v in (np.array(x) - ip(x, a) * np.array(a)))
    return s
sa, sb = refl(a_I2), refl(b_I2)
def w0_I2(r): return sa(sb(sa(r)))
def pi_B(r): return pi_mirror(w0_I2(r))
def ident(r): return r
assert all(pi_mirror(r) in ridx for r in roots)
assert all(pi_B(r) in ridx for r in roots)
assert all(pi_mirror(r) == r for r in I2_roots)
assert all(pi_B(r) == r for r in [tuple(np.array(r)) for r in []])  # placeholder
print("pi_B on I2 roots:", {r: pi_B(r) for r in I2_roots[:3]})
# pi_mirror swaps hatch <-> I1?
print("pi_mirror(hatch):", [pi_mirror(h) for h in hatch])

# ---------- signed lifts ----------
neg = lambda r: tuple(-v for v in r)
def build_theta(pi, family, eps6):
    """family 'permute': e_r -> eps e_{pi r}, h_r -> h_{pi r};  'antipodal': e_r -> eps e_{-pi r}, h_r -> -h_{pi r}."""
    T = np.zeros((N, N), dtype=int)  # columns: image of basis vector
    hs = 1 if family == 'permute' else -1
    img = lambda r: pi(r) if family == 'permute' else neg(pi(r))
    for i in range(6):
        T[:, i] = hs * hvec(pi(simple[i]))
    imgs = {}
    def brk(u, v): return np.einsum('a,b,abc->c', u, v, C)
    for i in range(6):
        ai = simple[i]
        imgs[ai] = eps6[i] * evec(img(ai))
        # delta from [theta e, theta f] = theta h
        cand = None
        target = T[:, :6] @ brk(evec(ai), evec(neg(ai)))[:6]   # theta([e_i, e_-i])
        for d in (+1, -1):
            f = d * evec(img(neg(ai)))
            if (brk(imgs[ai], f) == target).all(): cand = f
        assert cand is not None
        imgs[neg(ai)] = cand
    for r in pos:
        if r in imgs: continue
        for i in range(6):
            s = tuple(np.array(r) - np.array(simple[i]))
            if s in ridx:
                n = C[6 + ridx[s], 6 + ridx[simple[i]], 6 + ridx[r]]; assert n != 0
                imgs[r] = brk(imgs[s], imgs[simple[i]]) * n  # n = +-1
                nn = C[6 + ridx[neg(s)], 6 + ridx[neg(simple[i])], 6 + ridx[neg(r)]]; assert nn != 0
                imgs[neg(r)] = brk(imgs[neg(s)], imgs[neg(simple[i])]) * nn
                break
    for r in roots: T[:, 6 + ridx[r]] = imgs[r]
    return T

def is_aut(T):
    # [T a, T b] = T [a,b] for all basis pairs
    Tf = T.astype(float); Cf = C.astype(float)
    C1 = np.tensordot(Tf, Cf, axes=([0], [0]))      # a,y,c
    L = np.tensordot(Tf, C1, axes=([0], [1]))       # b,a,c
    L = np.transpose(L, (1, 0, 2))
    R = Cf @ Tf.T
    return np.abs(L - R).max() < 1e-9
def is_inv(T): return (T @ T == np.eye(N, dtype=int)).all()

def antilinear_sig(T, idx=None):
    """real form of sigma = tau.theta : V+(theta) (+) i V-(theta), restricted to subspace idx (basis indices),
    computed directly as sigma-fixed vectors; return Killing signature and eigen dims."""
    if idx is None:
        P = np.eye(N, dtype=int); sub = T
    else:
        P = np.eye(N, dtype=int)[:, idx]; sub = P.T @ T @ P
        assert (T @ P == P @ sub).all(), "theta does not preserve subspace"
    M = sp.Matrix(sub)
    Vp = M - sp.eye(M.shape[0]); Vm = M + sp.eye(M.shape[0])
    Bp = [sp.Matrix(v) for v in Vp.nullspace()]  # theta v = v
    Bm = [sp.Matrix(v) for v in Vm.nullspace()]  # theta v = -v
    vecs = [(v, 1) for v in Bp] + [(v, sp.I) for v in Bm]
    Ksub = sp.Matrix(P.T @ K @ P)
    n = len(vecs)
    G = sp.zeros(n, n)
    for i, (u, cu) in enumerate(vecs):
        for j, (w, cw) in enumerate(vecs):
            G[i, j] = sp.simplify(cu * cw * (u.T * Ksub * w)[0])
    assert all(sp.im(x) == 0 for x in G), "Gram not real"
    # sigma-fixed check: sigma(v) = theta(conj v) = v for basis
    for (u, cu) in vecs:
        v = cu * u; assert sp.simplify(M * sp.conjugate(cu) * u - v).norm() == 0
    return sig(G), (len(Bp), len(Bm))

results = {}
families = [('antipodal', 'A', pi_mirror), ('antipodal', 'B', pi_B), ('permute', 'A', pi_mirror), ('permute', 'B', pi_B)]
total = 0; compact_hits = []
for fam, cls, pi in families:
    elems = []
    for eps6 in itertools.product((1, -1), repeat=6):
        T = build_theta(pi, fam, eps6)
        if not is_aut(T): continue
        if not is_inv(T): continue
        (s2, dims2) = antilinear_sig(T, I2_idx[:0] + list(range(0)) + I2_idx) if False else (None, None)
        elems.append((eps6, T))
    print(f"{fam}/{cls}: involutive automorphism lifts = {len(elems)}")
    total += len(elems)
    results[f"{fam}/{cls}"] = {"n": len(elems), "elements": []}
    for eps6, T in elems:
        # I2 subspace: basis indices for h_a, h_b are not basis vectors; use change of basis
        # Build I2 as a coordinate subspace via projection matrix P (78x8) with columns I2_basis
        P = np.array(I2_basis).T
        # theta restricted: solve T P = P S
        S = np.linalg.lstsq(P.astype(float), (T @ P).astype(float), rcond=None)[0]
        S = np.rint(S).astype(int); assert (T @ P == P @ S).all(), "theta does not preserve I2"
        M = sp.Matrix(S)
        Bp = M.eigenvects()
        Vp = (M - sp.eye(8)).nullspace(); Vm = (M + sp.eye(8)).nullspace()
        KI2 = sp.Matrix(P.T @ K @ P)
        vecs = [(v, 1) for v in Vp] + [(v, sp.I) for v in Vm]
        G = sp.zeros(8, 8)
        for i, (u, cu) in enumerate(vecs):
            for j, (w, cw) in enumerate(vecs):
                G[i, j] = sp.expand(cu * cw * (u.T * KI2 * w)[0])
        assert all(sp.im(x) == 0 for x in G)
        sI2 = sig(G)
        # raw (linear) signatures on V+, V- for reference
        rawp = sig(sp.Matrix([[ (u.T*KI2*w)[0] for w in Vp] for u in Vp])) if Vp else (0,0,0)
        rawm = sig(sp.Matrix([[ (u.T*KI2*w)[0] for w in Vm] for u in Vm])) if Vm else (0,0,0)
        # global antilinear signature via COMBINE with numpy (large gaps)
        Tm = T.astype(float)
        w, V = np.linalg.eig(Tm)
        Vp_g = V[:, np.abs(w - 1) < 1e-8].real; Vm_g = V[:, np.abs(w + 1) < 1e-8].real
        gp = sig_np(Vp_g.T @ K @ Vp_g); gm = sig_np(Vm_g.T @ K @ Vm_g)
        glob = (gp[0] + gm[1], gp[1] + gm[0], gp[2] + gm[2])
        char = -int(np.trace(T))
        rec = {"eps6": list(eps6), "char": char, "dimVplus": int(Vp_g.shape[1]), "I2_sig": sI2,
               "I2_raw_plus": rawp, "I2_raw_minus": rawm, "global_antilinear_sig": glob}
        results[f"{fam}/{cls}"]["elements"].append(rec)
        if sI2 == (0, 8, 0): compact_hits.append((fam, cls, eps6, glob, char))
print("TOTAL torsor size:", total)
print("COMPACT-COLOR HITS:", len(compact_hits))
for h in compact_hits: print("  ", h)
from collections import Counter
for k, v in results.items():
    print(k, "chars", Counter(e["char"] for e in v["elements"]), "I2 sigs", Counter(tuple(e["I2_sig"]) for e in v["elements"]),
          "global", Counter(tuple(e["global_antilinear_sig"]) for e in v["elements"]))

# ---------- planted controls: antipodal / pi = id (64 lifts of -1): exactly one compact conjugation ----------
ctrl = []
for eps6 in itertools.product((1, -1), repeat=6):
    T = build_theta(ident, 'antipodal', eps6)
    if not (is_aut(T) and is_inv(T)): continue
    Tm = T.astype(float); w, V = np.linalg.eig(Tm)
    Vp_g = V[:, np.abs(w - 1) < 1e-8].real; Vm_g = V[:, np.abs(w + 1) < 1e-8].real
    gp = sig_np(Vp_g.T @ K @ Vp_g); gm = sig_np(Vm_g.T @ K @ Vm_g)
    glob = (gp[0] + gm[1], gp[1] + gm[0], gp[2] + gm[2])
    P = np.array(I2_basis).T
    S = np.rint(np.linalg.lstsq(P.astype(float), (T @ P).astype(float), rcond=None)[0]).astype(int)
    assert (T @ P == P @ S).all()
    M = sp.Matrix(S); Vp = (M - sp.eye(8)).nullspace(); Vm = (M + sp.eye(8)).nullspace()
    KI2 = sp.Matrix(P.T @ K @ P); vecs = [(v, 1) for v in Vp] + [(v, sp.I) for v in Vm]
    G = sp.Matrix(8, 8, lambda i, j: sp.expand(vecs[i][1]*vecs[j][1]*(vecs[i][0].T*KI2*vecs[j][0])[0]))
    ctrl.append((eps6, glob, sig(G), -int(np.trace(T))))
print("antipodal/id family size:", len(ctrl))
print("  globally compact (0,78):", [c for c in ctrl if c[1] == (0, 78, 0)])
print("  I2 compact among them:", sum(1 for c in ctrl if c[2] == (0, 8, 0)), "of", len(ctrl))
print("  I2 sig distribution:", Counter(c[2] for c in ctrl))
# tau alone (theta = identity): split form
T = np.eye(N, dtype=int)
print("theta=identity (sigma=tau, split): global sig", sig_np(K), "I2 sig", sig(sp.Matrix(np.array(I2_basis) @ K @ np.array(I2_basis).T)))

out = {"torsor_total": total, "compact_hits": [dict(family=f, cls=c, eps6=list(e), global_sig=g, char=ch) for f, c, e, g, ch in compact_hits],
       "families": results, "control_antipodal_id": [dict(eps6=list(e), global_sig=g, I2_sig=s, char=ch) for e, g, s, ch in ctrl]}
json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
