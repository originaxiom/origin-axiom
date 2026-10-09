import itertools, numpy as np, sympy as sp
np.set_printoptions(precision=5, suppress=True, linewidth=150)
rng = np.random.default_rng(12345)

# ---------- build G ----------
def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(3):
        for j in range(i+1, 3):
            if p[i] > p[j]: s = -s
    return s

zs_all = [np.exp(2j*np.pi*k/8) for k in range(8)]
G = []   # (matrix, label)
for p in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        S = np.zeros((3, 3))
        for i in range(3):
            S[p[i], i] = signs[i]       # column i -> row p[i]
        if round(np.linalg.det(S)) != 1: continue
        sg = perm_sign(p)
        for k, z in enumerate(zs_all):
            if abs(z**4 - sg) < 1e-9:
                G.append((z*S, dict(perm=p, signs=signs, k=k, S=S, z=z)))
print("|G| =", len(G), " (S count:", len(G)//4, ")")
# distinctness
mats = [g for g, _ in G]
dist = all(np.abs(mats[i]-mats[j]).max() > 1e-9 for i in range(len(mats)) for j in range(i))
print("all distinct:", dist)
# closure
def inG(m): return any(np.abs(m-g).max() < 1e-9 for g in mats)
print("closed under product:", all(inG(a@b) for a in mats for b in mats))
print("closed under inverse:", all(inG(np.linalg.inv(a)) for a in mats))
print("unitary:", all(np.abs(a.conj().T@a-np.eye(3)).max() < 1e-12 for a in mats))
ia = np.diag([-1., 1, -1]).astype(complex); ib = np.diag([1., -1, -1]).astype(complex)
print("inner_a in G:", inG(ia), " inner_b in G:", inG(ib))
print("scalars in G:", [c for c in [1, -1, 1j, -1j] if inG(c*np.eye(3))], " other scalars:",
      [z for z in zs_all if inG(z*np.eye(3)) and min(abs(z-c) for c in [1,-1,1j,-1j]) > 1e-9])
print("characters (a,b) of e_i:", [(int(ia[i, i].real), int(ib[i, i].real)) for i in range(3)])

# ---------- S_mod candidates ----------
def turns(m):
    ev = np.linalg.eigvals(m)
    return sorted(round((np.angle(e)/(2*np.pi) % 1)*8) % 8 for e in ev), \
           max(abs(abs(e)-1) for e in ev)
def target_turns(m):
    ev = np.linalg.eigvals(m)
    t = sorted(((np.angle(e)/(2*np.pi)) % 1)*8 for e in ev)
    return t
cands_all = []
for g, info in G:
    t = target_turns(g)
    if np.allclose(sorted(t), sorted([3, 3, 7]), atol=1e-7) or np.allclose(sorted([x % 8 for x in t]), sorted([3,3,7]), atol=1e-7):
        cands_all.append((g, info))
print("\nelements of G with eigenvalue turns {3/8,3/8,7/8}:", len(cands_all))
cands = []
for g, info in cands_all:
    P = np.abs(g)  # support pattern
    swap = abs(g[0,1]) > .5 and abs(g[1,0]) > .5 and abs(g[2,2]) > .5 and abs(g[0,0]) < 1e-9 and abs(g[1,1]) < 1e-9
    print(" perm", info['perm'], "signs", info['signs'], "z=e^{2 pi i k/8}, k=", info['k'], "swap12&fix3:", swap)
    if swap: cands.append((g, info))
print("S_mod candidates (swap e1<->e2, fix e3):", len(cands))
for g, info in cands:
    print(" g^2 =", np.round(g@g, 6).tolist() , " g^8 = I:", np.allclose(np.linalg.matrix_power(g, 8), np.eye(3)), " g^4 =", np.round(np.linalg.matrix_power(g,4)[0,0],6))
# relation of candidates
if len(cands) == 2:
    d = np.linalg.inv(cands[0][0]) @ cands[1][0]
    print(" g0^-1 g1 =", np.round(d, 6).tolist(), "  inner_a*inner_b =", (ia@ib).real.diagonal())

# ---------- tensor actions ----------
def basis_full():
    B = []
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3), complex); E[i, j] = 1; B.append(E)
    return B
def basis_sym():
    B = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3), complex); E[i, j] = 1; E[j, i] = 1; B.append(E)
    return B
def rep_matrix(act, basis):
    # coordinates in the (non-orthonormal) basis via lstsq on flattened
    Bm = np.array([b.flatten() for b in basis]).T  # 9 x d
    cols = []
    for b in basis:
        img = act(b).flatten()
        coef, res, rk, sv = np.linalg.lstsq(Bm, img, rcond=None)
        assert np.abs(Bm@coef - img).max() < 1e-10
        cols.append(coef)
    return np.array(cols).T
tensors = {
    'Dirac  Tbar(x)T': (lambda g: (lambda M: g.conj().T @ M @ g), basis_full()),
    'T(x)T          ': (lambda g: (lambda M: g.T @ M @ g), basis_full()),
    'Sym2 T         ': (lambda g: (lambda M: g.T @ M @ g), basis_sym()),
}
def nullspace(A, tol=1e-9):
    u, s, vh = np.linalg.svd(A)
    r = (s > tol).sum()
    return vh[r:].conj().T
def sing(M): return np.linalg.svd(M, compute_uv=False)

def classify(sv, tol=1e-8):
    sv = sorted(sv)
    d01 = abs(sv[0]-sv[1]) < tol; d12 = abs(sv[1]-sv[2]) < tol
    if d01 and d12: return 'all-equal'
    if d01: return 'pair(low)+single'
    if d12: return 'pair(high)+single'
    return 'THREE-DISTINCT'

def run(Smod_info, c_iota, verbose=True, full_control=False):
    g_S, info = Smod_info
    out = {}
    for name, (actf, basis) in tensors.items():
        d = len(basis)
        R = lambda g: rep_matrix(actf(g), basis)
        Bm = np.array([b.flatten() for b in basis]).T
        # iota
        iota = c_iota*np.eye(3)
        Riota = R(iota)
        iev = np.unique(np.round(np.linalg.eigvals(Riota), 9))
        # inner-fixed subspace (coordinates in 'basis')
        A = np.vstack([R(ia)-np.eye(d), R(ib)-np.eye(d)])
        N = nullspace(A)
        mats_fixed = [(Bm@N[:, k]).reshape(3, 3) for k in range(N.shape[1])]
        offdiag = max(np.abs(m - np.diag(np.diag(m))).max() for m in mats_fixed)
        # S acts on fixed subspace
        RS = R(g_S)
        img = RS@N
        Ares = np.linalg.lstsq(N, img, rcond=None)[0]
        closure_err = np.abs(N@Ares - img).max()
        evs = np.linalg.eigvals(Ares)
        res = dict(dim=N.shape[1], offdiag=offdiag, closure=closure_err, iota=iev, evs=evs, eig={})
        # scan 48th roots
        for k in range(48):
            lam = np.exp(2j*np.pi*k/48)
            Ns = nullspace(Ares - lam*np.eye(Ares.shape[0]), tol=1e-8)
            if Ns.shape[1] == 0: continue
            # random combos
            classes = {}
            single_ok = True; worst_single = 0
            cnt = 0
            for t in range(400):
                coef = rng.normal(size=Ns.shape[1]) + 1j*rng.normal(size=Ns.shape[1])
                if t == 0 and Ns.shape[1] == 1: coef = np.array([1.0+0j])
                vec = N@(Ns@coef)
                M = (Bm@vec).reshape(3, 3)
                U, s, Vh = np.linalg.svd(M)
                cl = classify(s)
                classes[cl] = classes.get(cl, 0) + 1
                if cl.startswith('pair'):
                    # find odd singular value: the one not equal to the other two
                    idx = np.argsort(s)
                    if cl == 'pair(low)+single': odd = idx[2]
                    else: odd = idx[0]
                    # eigenvector of M M^dagger at odd singular value -> left sing vec U[:,odd]
                    vcol = U[:, odd]
                    ov = abs(vcol[2])
                    worst_single = max(worst_single, 1-ov)
                    # also M^dag M
                    ov2 = abs(Vh[odd, :][2]); worst_single = max(worst_single, 1-ov2)
            res['eig'][k] = dict(lam=lam, dim=Ns.shape[1], classes=classes, worst_single=worst_single,
                                 basis=[ (Bm@(N@Ns[:, j])).reshape(3, 3) for j in range(Ns.shape[1])])
        out[name] = res
    return out

for ci, (g_S, info) in enumerate(cands):
    for c_iota in [1, -1, 1j, -1j]:
        out = run((g_S, info), c_iota)
        print(f"\n===== S_mod candidate #{ci} (signs {info['signs']}, z=ω^{info['k']}), iota scalar c={c_iota} =====")
        for name, r in out.items():
            print(f"[{name}] inner-fixed dim={r['dim']}  max|offdiag|={r['offdiag']:.1e}  S-closure err={r['closure']:.1e}  iota eig={np.round(r['iota'],6)}")
            for k, e in r['eig'].items():
                print(f"    S-eigenvalue e^(2πi*{k}/48) = {np.round(e['lam'],5)}  dim={e['dim']}  sv-classes over 400 random combos: {e['classes']}  worst(1-|<e3|odd sv vec>|)={e['worst_single']:.1e}")
        if ci == 0 and c_iota == 1: pass
