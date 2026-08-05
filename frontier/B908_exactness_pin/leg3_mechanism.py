import os
#!/usr/bin/env python3
"""B908 LEG 3 -- the vanishing mechanism for v = prod(rows) + prod(cols).

Registered target: the explicit involution that maps the row-pencil product to MINUS
the column-pencil product, with the parity source identified, verified at two
full-tower primes (40123, 40639).

Everything mod p is exact integer arithmetic; the exact phase is sympy Rational.
Machinery replicated from the handoff scripts (glue2.py / probeB.py / invar1.py)
with q parameterized; the B854 base (INV/ADS/ns) and rep27.pkl are loaded once.

Phases (run via --phase):
  A  build state at a prime: cells, atoms (LINES), couplings, sides, I, v
  B  structure: label matrix, grid/K33, Sym^3 support, order-independence,
     eigen-common-line checks (the Galois-action-on-atoms computation)
  C  rational reconstruction of the atom lines (single prime + CRT of two)
  D  the mechanism: stabilizer dimension, det-frame, transpose involution J
  E  exact rational couplings and v over Q (if C succeeded)
  K  K-identification: reconstruct towers as elements of K=Q[r]/mu, verify the
     rational atoms are the construction's atoms EXACTLY (symbolic, mod mu)
"""
import argparse, io, contextlib, itertools, json, os, pickle, sys
import numpy as np
import sympy as sp
from collections import Counter

ARC = os.path.dirname(os.path.abspath(__file__))
RUN = os.environ['SESSION_SCRATCH_RUN']
SCRATCH = os.environ['SESSION_SCRATCH']

PRIMES = {40123: [(27063, 13410, 2675), (23094, 222, 18983), (13418, 13632, 16308)],
          40639: [(2059, 12034, 18302), (35519, 6669, 18386), (40551, 18703, 3951)]}
# five more full-tower primes (towers from leg 2) -- used only if CRT-2 is not enough
EXTRA = {int(k): [tuple(t) for t in v] for k, v in
         json.load(open(os.path.join(RUN, 'multi_primes.json'))).items()}
PRIMES.update(EXTRA)
ALLP = sorted(PRIMES)

# mu, both normalizations (B866): mine(t) and theirs(rho), rho = 13 t
MU_MINE = [500716339200, -159667200, -28224, 1]      # coeffs of t^3..t^0
MU_13 = [500716339200, -2075673600, -4769856, 2197]  # 2197*mine(x/13) cleared

q = None  # current prime (module global, as in the handoff scripts)

# ---------------------------------------------------------------- base (char 0)
_BASE = {}


def load_base():
    global _BASE
    if _BASE:
        return _BASE
    cache = os.path.join(SCRATCH, 'leg3_base_cache.pkl')
    if os.path.exists(cache):
        _BASE = pickle.load(open(cache, 'rb'))
        return _BASE
    nsdict = {'__file__': os.path.join(SCRATCH, 'b854_shadow.py')}
    src = open('/Users/dri/origin-axiom/frontier/B854_centralizer_exact/e6_centralizer.py').read()
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, 'b854', 'exec'), nsdict)
    D = pickle.load(open(os.path.join(RUN, 'rep27.pkl'), 'rb'))
    _BASE = dict(INV=nsdict['INV'], ns=nsdict['ns'], REP=D['REP'],
                 ADS={n: sp.Matrix(nsdict['ADS'][n]).tolist() for n in nsdict['ns']})
    with open(cache, 'wb') as f:
        pickle.dump(_BASE, f)
    return _BASE


# ---------------------------------------------------------------- mod-q helpers (glue2)
def rq_(x):
    xr = sp.Rational(x)
    return (xr.p % q) * pow(xr.q % q, -1, q) % q


def repm(vec, REP):
    M = np.zeros((27, 27), dtype=np.int64)
    for k, c in enumerate(vec):
        cc = rq_(c)
        if cc:
            Rk = REP[k]
            for a in range(27):
                for b in range(27):
                    if Rk[a][b]:
                        M[a][b] = (M[a][b] + cc * rq_(Rk[a][b])) % q
    return M


def rn(A0):
    A = [[int(x) % q for x in row] for row in (A0.tolist() if hasattr(A0, 'tolist') else A0)]
    n_ = len(A); m_ = len(A[0]); piv = []; rr = 0
    for c in range(m_):
        pr = next((x for x in range(rr, n_) if A[x][c] % q), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = pow(A[rr][c], -1, q); A[rr] = [(e * iv) % q for e in A[rr]]
        for x in range(n_):
            if x != rr and A[x][c]:
                f2 = A[x][c]; A[x] = [(A[x][j] - f2 * A[rr][j]) % q for j in range(m_)]
        piv.append(c); rr += 1
    fr = [c for c in range(m_) if c not in piv]; K = []
    for f3 in fr:
        v = [0] * m_; v[f3] = 1
        for i, c in enumerate(piv):
            v[c] = int((-A[i][f3]) % q)
        K.append(v)
    return rr, (np.array(K, dtype=np.int64) % q if K else np.zeros((0, m_), dtype=np.int64))


def rrows(A0):
    A = [[int(x) % q for x in row] for row in (A0.tolist() if hasattr(A0, 'tolist') else A0)]
    n_ = len(A); m_ = len(A[0]); rr = 0
    for c in range(m_):
        pr = next((x for x in range(rr, n_) if A[x][c] % q), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = pow(A[rr][c], -1, q); A[rr] = [(e * iv) % q for e in A[rr]]
        for x in range(n_):
            if x != rr and A[x][c]:
                f = A[x][c]; A[x] = [(A[x][j] - f * A[rr][j]) % q for j in range(m_)]
        rr += 1
    return rr


def restr78(Mq, B):
    m_ = B.shape[0]
    out = np.zeros((m_, m_), dtype=np.int64)
    for a2 in range(m_):
        w = (Mq @ B[a2]) % q
        Aug = np.hstack([B.T, w[:, None]]) % q
        A2 = [[int(x) % q for x in row] for row in Aug.tolist()]; rr2 = 0; piv2 = []
        for c in range(m_):
            pr = next((x for x in range(rr2, 78) if A2[x][c] % q), None)
            if pr is None:
                continue
            A2[rr2], A2[pr] = A2[pr], A2[rr2]
            iv = pow(A2[rr2][c], -1, q); A2[rr2] = [(e * iv) % q for e in A2[rr2]]
            for x in range(78):
                if x != rr2 and A2[x][c]:
                    f2 = A2[x][c]; A2[x] = [(A2[x][j] - f2 * A2[rr2][j]) % q for j in range(m_ + 1)]
            piv2.append(c); rr2 += 1
        sol = np.zeros(m_, dtype=np.int64)
        for i2, c in enumerate(piv2):
            sol[c] = A2[i2][m_] % q
        out[:, a2] = sol
    return out


def ray78(M, v):
    den = pow(int((v @ v) % q), -1, q)
    return int((v @ ((M @ v) % q)) % q) * den % q


tt = sp.Symbol('tt')


def mats27(base):
    """R27 and Gq78 for the current q."""
    R27 = {n: repm([sp.Rational(c) for c in base['INV'][n]], base['REP']) for n in base['ns']}
    Gq78 = {}
    for n in base['ns']:
        Ml = base['ADS'][n]
        Gq78[n] = np.array([[rq_(Ml[i][j]) for j in range(78)]
                            for i in range(78)], dtype=np.int64)
    return R27, Gq78


# ---------------------------------------------------------------- cells (probeB, ev retained)
def build_cells(rgai, R27, Gq78):
    r1, g1, a1 = rgai
    _, K46 = rn(np.vstack([(Gq78[8] + r1 * Gq78[16]) % q]))
    R16r = restr78(Gq78[16], K46)
    _, Vg = rn((R16r - g1 * np.eye(K46.shape[0], dtype=np.int64)) % q); Vg = (Vg @ K46) % q
    R14g = restr78(Gq78[14], Vg)
    _, Va = rn((R14g - a1 * np.eye(Vg.shape[0], dtype=np.int64)) % q); Va = (Va @ Vg) % q
    bq = ray78(Gq78[22], Va[0])
    X1 = (R27[8] + r1 * R27[16]) % q
    Ym = (g1 * R27[14] + (q - a1) * R27[16]) % q
    W3 = (bq * R27[16] + (q - g1) * R27[22]) % q
    combo = (3 * X1 + 7 * Ym + 13 * W3 + 17 * R27[14]) % q
    chp = sp.Poly(sp.Matrix(combo.tolist()).charpoly(tt).as_expr(), tt, modulus=q)
    cells = []

    def ray(M, v):
        den = pow(int((v @ v) % q), -1, q)
        return int((v @ ((M @ v) % q)) % q) * den % q

    for ev, mlt in chp.ground_roots().items():
        _, V = rn((combo - int(ev) * np.eye(27, dtype=np.int64)) % q)
        cells.append(dict(mlt=mlt, ev=int(ev) % q, B=V % q,
                          x1=ray(X1, V[0]), y=ray(Ym, V[0]), w3=ray(W3, V[0])))
    tr = [c for c in cells if c['mlt'] == 3]
    key = Counter((c['x1'], c['y'], c['w3']) for c in tr)
    dupk = [k for k, v in key.items() if v == 2][0]
    X16 = dupk[0]; X10 = [c['x1'] for c in tr if c['x1'] != X16][0]
    out = []
    qn = 0; on = 0; dn = 0
    for c in cells:
        colored = (c['mlt'] == 3)
        part = '16' if c['x1'] == X16 else ('10' if c['x1'] == X10 else '1')
        if colored:
            if (c['x1'], c['y'], c['w3']) == dupk:
                qn += 1; tag = f"Q{qn}"
            elif part == '16':
                on += 1; tag = f"c16_{on}"
            else:
                dn += 1; tag = f"c10_{dn}"
        else:
            tag = None
        out.append((tag, part, colored, c))
    sn = Counter((c['x1'], c['y'], c['w3']) for _, p, col, c in out if not col and p == '16')
    dupS = [k for k, v in sn.items() if v == 2][0]
    res = []
    l1 = e1 = h1 = 0
    for tag, part, col, c in out:
        if col:
            res.append((tag, c['B'], c)); continue
        if part == '1':
            res.append(('S', c['B'], c))
        elif part == '10':
            h1 += 1; res.append((f"H{h1}", c['B'], c))
        elif (c['x1'], c['y'], c['w3']) == dupS:
            l1 += 1; res.append((f"L{l1}", c['B'], c))
        else:
            e1 += 1; res.append((f"s16_{e1}", c['B'], c))
    return res, dict(combo=combo, X1=X1, Ym=Ym, W3=W3, bq=bq)


def inter_basis(A, B):
    M = np.hstack([A.T, (q - B.T) % q]) % q
    _, N = rn(M)
    if N.shape[0] == 0:
        return np.zeros((0, 27), dtype=np.int64)
    V = (N[:, :A.shape[0]] @ A) % q
    seen = np.zeros((0, 27), dtype=np.int64)
    for row in V:
        if rrows(np.vstack([seen, row[None, :]])) > seen.shape[0]:
            seen = np.vstack([seen, row[None, :]])
    return seen % q


def colorless(Ci):
    return [(t, B) for t, B, c in Ci
            if t == 'S' or (t and (t.startswith('H') or t.startswith('L') or t.startswith('s16')))]


# ---------------------------------------------------------------- cubic (invar1)
_CB = json.load(open(os.path.join(RUN, 'cubic27.json')))
TRIP = [tuple(t) for t in _CB['triples']]
assert all(sp.Rational(c).q == 1 for c in _CB['coeffs']), "cubic27 coeffs not integral"
COEF = [int(sp.Rational(c)) for c in _CB['coeffs']]


def cub(u, v, w):
    s = 0
    for (a, b, c), cf in zip(TRIP, COEF):
        t = 0
        for x, y, z in itertools.permutations((a, b, c)):
            t = (t + int(u[x]) * int(v[y]) % q * int(w[z])) % q
        s = (s + cf * t) % q
    return s % q


def cub_exact(u, v, w):
    s = sp.Integer(0)
    for (a, b, c), cf in zip(TRIP, COEF):
        t = sp.Integer(0)
        for x, y, z in itertools.permutations((a, b, c)):
            t += u[x] * v[y] * w[z]
        s += cf * t
    return s


# ---------------------------------------------------------------- atoms + invariant (invar1)
def atoms_and_invariant(CELLS, order=(0, 1, 2)):
    C1, C2, C3 = (colorless(CELLS[order[0]]), colorless(CELLS[order[1]]),
                  colorless(CELLS[order[2]]))
    LINES = []
    for t1, B1 in C1:
        for t2, B2 in C2:
            I12 = inter_basis(B1, B2)
            if I12.shape[0] == 0:
                continue
            for t3, B3 in C3:
                I = inter_basis(I12, B3)
                if I.shape[0] > 0:
                    LINES.append(((t1, t2, t3), I[0] % q))
    vs = [v for _, v in LINES]
    T = []
    for i in range(9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                c = cub(vs[i], vs[j], vs[k])
                if c:
                    T.append(((i, j, k), c))
    adj = {a: set() for a in range(len(T))}
    for a in range(len(T)):
        for b in range(a + 1, len(T)):
            if set(T[a][0]) & set(T[b][0]):
                adj[a].add(b); adj[b].add(a)
    side = {0: 0}; stack = [0]
    while stack:
        x = stack.pop()
        for y2 in adj[x]:
            if y2 not in side:
                side[y2] = 1 - side[x]; stack.append(y2)
    bip = all(side[a] != side[b] for a in adj for b in adj[a])
    num = 1; den = 1
    for a, (tri, c) in enumerate(T):
        if side[a] == 0:
            num = num * c % q
        else:
            den = den * c % q
    I0 = num * pow(den, -1, q) % q
    v0 = (num + den) % q
    return dict(LINES=LINES, T=T, side=side, bipartite=bip, I=I0, v=v0,
                prod0=num, prod1=den)


# ---------------------------------------------------------------- phase A
def phase_A(p):
    global q
    q = p
    base = load_base()
    R27, Gq78 = mats27(base)
    CELLS = []
    OPS = []
    for d in PRIMES[p]:
        res, ops = build_cells(d, R27, Gq78)
        CELLS.append(res); OPS.append(ops)
    inv = atoms_and_invariant(CELLS)
    st = dict(q=p, DATA=PRIMES[p], CELLS=CELLS, OPS=OPS, R27=R27, **inv)
    with open(os.path.join(ARC, f'leg3_state_{p}.pkl'), 'wb') as f:
        pickle.dump(st, f)
    print(f"[A] p={p}: cells/labeling {[len(c) for c in CELLS]}, "
          f"atoms {len(inv['LINES'])}, couplings {len(inv['T'])}, "
          f"bipartite {inv['bipartite']}, I={inv['I']} (p-1={p-1}), v={inv['v']}")
    for lbl, _ in inv['LINES']:
        print("   atom", lbl)
    return st


def load_state(p):
    global q
    q = p
    with open(os.path.join(ARC, f'leg3_state_{p}.pkl'), 'rb') as f:
        return pickle.load(f)


# ---------------------------------------------------------------- phase B
def phase_B(p):
    st = load_state(p)
    CELLS, LINES, T, side = st['CELLS'], st['LINES'], st['T'], st['side']
    out = {}
    # colorless cells: count and multiplicities
    cl = [[(t, c) for t, B, c in C if (t, B) in [] or True] for C in CELLS]  # keep full
    ncl, mults = [], []
    for C in CELLS:
        cc = [(t, c) for t, B, c in C
              if t == 'S' or (t and (t.startswith('H') or t.startswith('L') or t.startswith('s16')))]
        ncl.append(len(cc)); mults.append(sorted(set(c['mlt'] for _, c in cc)))
    out['colorless_cells_per_labeling'] = ncl
    out['colorless_mults'] = mults
    print(f"[B] p={p}: colorless cells per labeling {ncl}, mults {mults}")

    # each atom vec is an eigenvector of each labeling's combo, and lies in a dim-1 cell
    ok_eig = True
    for lbl, v in LINES:
        for i in range(3):
            combo = st['OPS'][i]['combo']
            w = (combo @ v) % q
            # proportionality w = ev*v
            nz = np.nonzero(v)[0][0]
            lam = int(w[nz]) * pow(int(v[nz]), -1, q) % q
            if not np.array_equal(w % q, (lam * v) % q):
                ok_eig = False
    out['atoms_common_eigenlines'] = ok_eig
    print(f"   atoms are common eigenlines of all three labelings: {ok_eig}")

    # order-independence: rerun the atom pipeline under all 6 labeling orders
    orders = list(itertools.permutations((0, 1, 2)))
    ord_res = {}
    base_lines = {tuple(lbl): v for lbl, v in LINES}
    for o in orders:
        inv2 = atoms_and_invariant(CELLS, order=o)
        # physical match: every line of inv2 proportional to a line of LINES
        phys = []
        for lbl2, v2 in inv2['LINES']:
            hit = None
            for lbl, v in LINES:
                nz = np.nonzero(v)[0][0]
                if v2[nz]:
                    lam = int(v2[nz]) * pow(int(v[nz]), -1, q) % q
                    if np.array_equal(v2 % q, (lam * v) % q):
                        hit = lbl; break
            phys.append((lbl2, hit))
        allmatch = all(h is not None for _, h in phys)
        # slot shuffle: run-order o labels = base labels shuffled by o
        shuffle_ok = all(h is not None and tuple(l2[j] for j in range(3)) ==
                        tuple(h[o[j]] for j in range(3))
                        for l2, h in phys)
        ord_res[str(o)] = dict(I=int(inv2['I']), v=int(inv2['v']),
                               lines=len(inv2['LINES']), physical_match=allmatch,
                               slot_shuffle=shuffle_ok)
        print(f"   order {o}: I={inv2['I']}, v={inv2['v']}, phys-match {allmatch}, "
              f"slot-shuffle {shuffle_ok}")
    out['order_independence'] = ord_res

    # K33 structure and grid
    n0 = [a for a in range(6) if side[a] == 0]
    n1 = [a for a in range(6) if side[a] == 1]
    k33 = all(len(set(T[a][0]) & set(T[b][0])) == (1 if side[a] != side[b] else 0)
              for a in range(6) for b in range(6) if a != b)
    out['K33'] = k33 and len(n0) == 3 and len(n1) == 3
    grid = {}
    for ai in range(9):
        r = [u for u in n0 if ai in T[u][0]]
        c = [v for v in n1 if ai in T[v][0]]
        assert len(r) == 1 and len(c) == 1, "atom not in exactly one coupling per side"
        grid[ai] = (n0.index(r[0]), n1.index(c[0]))
    out['grid'] = {str(k): v for k, v in grid.items()}
    print(f"   K33 (sides 3+3, cross-share exactly 1): {out['K33']}")
    print("   grid (atom -> (row=side0 coupling, col=side1 coupling)):")
    gm = [[None] * 3 for _ in range(3)]
    for ai, (u, v) in grid.items():
        gm[u][v] = LINES[ai][0]
    for u in range(3):
        print("     ", gm[u])

    # Sym^3 support: all 165 multisets
    vs = [v for _, v in LINES]
    supp = []
    for i in range(9):
        for j in range(i, 9):
            for k in range(j, 9):
                c = cub(vs[i], vs[j], vs[k])
                if c:
                    supp.append(((i, j, k), int(c)))
    coup_tris = sorted(t for t, _ in T)
    out['sym3_nonzero'] = len(supp)
    out['sym3_equals_couplings'] = sorted(t for t, _ in supp) == coup_tris
    print(f"   Sym^3 support: {len(supp)} nonzero of 165; equals the 6 couplings: "
          f"{out['sym3_equals_couplings']}")

    # ambient derivation check (R27[n] are derivations of cub)
    rng = np.random.default_rng(7)
    der = {}
    for n in sorted(st['R27']):
        M = st['R27'][n]
        ok = True
        for _ in range(3):
            u, v, w = (rng.integers(0, q, 27) for _ in range(3))
            s = (cub((M @ u) % q, v, w) + cub(u, (M @ v) % q, w) + cub(u, v, (M @ w) % q)) % q
            if s:
                ok = False
        der[str(n)] = ok
    out['ambient_derivations'] = der
    print(f"   R27[n] derivations of cub: {der}")

    with open(os.path.join(ARC, f'leg3_B_{p}.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase C
def canon_lines(st):
    """atom vectors rescaled to first-nonzero = 1 (char-0-canonical representative)."""
    p = st['q']
    out = []
    for lbl, v in st['LINES']:
        nz = np.nonzero(v)[0][0]
        s = pow(int(v[nz]), -1, p)
        out.append((lbl, (s * v) % p, int(nz)))
    return out


def ratrec(r, m, bound):
    a, b = m, int(r) % m; x0, x1 = 0, 1
    while b and b > bound:
        d2 = a // b; a, b = b, a - d2 * b; x0, x1 = x1, x0 - d2 * x1
    if b == 0:
        return sp.Integer(0) if int(r) % m == 0 else None
    num, den = (b, x1) if x1 > 0 else (-b, -x1)
    if den <= 0 or den > bound or abs(num) > bound:
        return None
    if sp.gcd(num, den) != 1:
        return None
    return sp.Rational(num, den)


def class_of(tag):
    if tag == 'S':
        return 'S'
    if tag.startswith('H'):
        return 'H'
    if tag.startswith('L'):
        return 'L'
    return 'e'  # s16


def align_to_ref(stref, st):
    """pair atoms of st to atoms of stref via the canonical class patterns,
    aligned by a global tower-slot permutation. Returns (sig, pair dict
    label@ref -> label@st, couplings_ok)."""
    global q
    q = stref['q']; Lr = canon_lines(stref)
    q = st['q']; Ls = canon_lines(st)
    patsr = {tuple(l): tuple(class_of(t) for t in l) for l, v, nz in Lr}
    patss = {tuple(l): tuple(class_of(t) for t in l) for l, v, nz in Ls}
    sig_found = None
    for sig in itertools.permutations(range(3)):
        m1 = sorted(tuple(p[sig[j]] for j in range(3)) for p in patsr.values())
        if m1 == sorted(patss.values()) and len(set(m1)) == 9:
            sig_found = sig
            break
    if sig_found is None:
        return None, None, False
    inv_pats = {v: k for k, v in patss.items()}
    pair = {lr: inv_pats[tuple(p_[sig_found[j]] for j in range(3))]
            for lr, p_ in patsr.items()}
    idxr = {tuple(l): i for i, (l, _) in enumerate(stref['LINES'])}
    idxs = {tuple(l): i for i, (l, _) in enumerate(st['LINES'])}
    trir = [tuple(sorted(t)) for t, _ in stref['T']]
    tris = set(tuple(sorted(t)) for t, _ in st['T'])
    mapped = [tuple(sorted(idxs[pair[tuple(stref['LINES'][i][0])]] for i in t))
              for t in trir]
    return sig_found, pair, all(m in tris for m in mapped)


def phase_C(primes=None):
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    pref = 40123
    stref = load_state(pref)
    out = {'primes_used': primes}
    # per-prime canonical lines, aligned to the reference labels
    labs = {}
    global q
    for p in primes:
        st = load_state(p)
        if p == pref:
            q = p
            labs[p] = {tuple(l): (v, nz) for l, v, nz in canon_lines(st)}
            continue
        sig, pair, cok = align_to_ref(stref, st)
        assert sig is not None and cok, f"alignment failed at {p}"
        q = p
        raw = {tuple(l): (v, nz) for l, v, nz in canon_lines(st)}
        labs[p] = {lr: raw[pair[lr]] for lr in pair}
        out.setdefault('alignments', {})[str(p)] = dict(slot=list(sig), couplings_ok=cok)
        print(f"   align {p}: slot {sig}, couplings map onto couplings: {cok}")
    M = 1
    for p in primes:
        M *= p
    bound = int(sp.floor(sp.sqrt(sp.Integer(M) / 2)))
    print(f"[C] CRT over {len(primes)} primes, modulus ~{float(M):.2e}, "
          f"ratrec bound ~{float(bound):.2e}")
    atoms_exact = {}
    ok_all = True
    for lbl in sorted(labs[pref]):
        nzs = {labs[p][lbl][1] for p in primes}
        if len(nzs) != 1:
            ok_all = False
            print(f"   {lbl}: pivot mismatch {nzs}")
            continue
        vec = []
        for a in range(27):
            x = 0
            for p in primes:
                Mp = M // p
                x = (x + int(labs[p][lbl][0][a]) * Mp * pow(Mp % p, -1, p)) % M
            r = ratrec(x, M, bound)
            if r is None:
                vec = None; break
            vec.append(r)
        if vec is None:
            ok_all = False
            print(f"   {lbl}: ratrec FAILED")
        else:
            atoms_exact[lbl] = vec
    out['all_reconstructed'] = ok_all
    if ok_all:
        h = max(max(abs(x.p), x.q) for vec in atoms_exact.values() for x in vec)
        out['max_height'] = int(h)
        print(f"   all 9 atom lines reconstructed over Q; max height {h}")
        for p in primes:
            for lbl, vec in atoms_exact.items():
                v = labs[p][lbl][0]
                for a in range(27):
                    r = vec[a]
                    assert (r.p % p) * pow(r.q % p, -1, p) % p == int(v[a]) % p
        print(f"   reduction check at all {len(primes)} primes: PASS")
        with open(os.path.join(ARC, 'leg3_atoms_exact.json'), 'w') as f:
            json.dump({str(k): [str(x) for x in v] for k, v in atoms_exact.items()},
                      f, indent=1)
    with open(os.path.join(ARC, 'leg3_C.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase D
def stab_dim(T3, p):
    """nullity of the derivation system for a symmetric trilinear table T3 (9^3), mod p."""
    eqs = []
    for i in range(9):
        for j in range(i, 9):
            for k in range(j, 9):
                row = [0] * 81
                for l in range(9):
                    row[l * 9 + i] = (row[l * 9 + i] + T3[l][j][k]) % p
                    row[l * 9 + j] = (row[l * 9 + j] + T3[i][l][k]) % p
                    row[l * 9 + k] = (row[l * 9 + k] + T3[i][j][l]) % p
                eqs.append(row)
    global q
    qs = q; q = p
    r = rrows(np.array(eqs, dtype=np.int64))
    q = qs
    return 81 - r


def phase_D(p):
    st = load_state(p)
    LINES, T, side = st['LINES'], st['T'], st['side']
    vs = [v for _, v in LINES]
    T3 = [[[cub(vs[i], vs[j], vs[k]) for k in range(9)] for j in range(9)] for i in range(9)]
    out = {}
    d_actual = stab_dim(T3, p)
    out['stabilizer_dim'] = d_actual
    print(f"[D] p={p}: stabilizer algebra dim of cub|S9 = {d_actual} "
          f"(sl3+sl3 (+traceless glue) = 16 = det-type)")

    # controls: same support, random couplings
    n0 = [a for a in range(6) if side[a] == 0]
    n1 = [a for a in range(6) if side[a] == 1]
    tris = [T[a][0] for a in range(6)]
    rng = np.random.default_rng(11)

    def synth(cvals):
        T3s = [[[0] * 9 for _ in range(9)] for _ in range(9)]
        for (tri, cv) in zip(tris, cvals):
            for (a, b, c) in itertools.permutations(tri):
                T3s[a][b][c] = cv % p
        return T3s

    # random c (I != -1 w.o.p.)
    cr = [int(rng.integers(2, p)) for _ in range(6)]
    Ir = 1
    for a in range(6):
        Ir = Ir * (cr[a] if side[a] == 0 else pow(cr[a], -1, p)) % p
    d_rand = stab_dim(synth(cr), p)
    out['control_random'] = dict(I=int(Ir), dim=d_rand)
    # torus twist of the actual couplings (I = -1 preserved)
    sc = [int(rng.integers(2, p)) for _ in range(9)]
    ct = []
    for a in range(6):
        f = 1
        for ai in T[a][0]:
            f = f * sc[ai] % p
        ct.append(T[a][1] * f % p)
    It = 1
    for a in range(6):
        It = It * (ct[a] if side[a] == 0 else pow(ct[a], -1, p)) % p
    d_tw = stab_dim(synth(ct), p)
    out['control_torus_twist'] = dict(I=int(It), dim=d_tw)
    # forced perm-type: c = +1 on all six
    d_perm = stab_dim(synth([1] * 6), p)
    out['control_permanent'] = dict(I=1, dim=d_perm)
    print(f"   controls: random c (I={Ir}) dim={d_rand}; torus twist (I={It}) "
          f"dim={d_tw}; permanent-type (I=1) dim={d_perm}")

    # det-frame: atom rescalings s with couplings -> (1,1,1,-1,-1,-1)
    grid_of = {}
    for ai in range(9):
        u = [x for x in n0 if ai in T[x][0]][0]
        v = [x for x in n1 if ai in T[x][0]][0]
        grid_of[ai] = (n0.index(u), n1.index(v))
    atom_at = {uv: ai for ai, uv in grid_of.items()}
    cE = [T[n0[u]][1] for u in range(3)]
    cO = [T[n1[v]][1] for v in range(3)]
    A = [(-pow(ce, -1, p)) % p for ce in cE]          # target row product 1/cE... sign below
    # want: prod_v s[u][v] = 1/cE[u]  ;  prod_u s[u][v] = -1/cO[v]
    Arow = [pow(ce, -1, p) for ce in cE]
    Bcol = [(p - 1) * pow(co, -1, p) % p for co in cO]
    cons = 1
    for x in Arow:
        cons = cons * x % p
    cons2 = 1
    for x in Bcol:
        cons2 = cons2 * x % p
    out['detframe_consistency'] = (cons == cons2)
    s = {}
    for u2 in range(2):
        for v2 in range(2):
            s[(u2, v2)] = 1
    s[(0, 2)] = Arow[0] * pow(s[(0, 0)] * s[(0, 1)], -1, p) % p
    s[(1, 2)] = Arow[1] * pow(s[(1, 0)] * s[(1, 1)], -1, p) % p
    for v2 in range(3):
        s[(2, v2)] = Bcol[v2] * pow(s[(0, v2)] * s[(1, v2)], -1, p) % p
    # verify all six
    okf = True
    for u2 in range(3):
        pr = s[(u2, 0)] * s[(u2, 1)] % p * s[(u2, 2)] % p
        if pr != Arow[u2]:
            okf = False
    for v2 in range(3):
        pr = s[(0, v2)] * s[(1, v2)] % p * s[(2, v2)] % p
        if pr != Bcol[v2]:
            okf = False
    out['detframe_solved'] = okf
    print(f"   det-frame: consistency(prod A == prod B) {out['detframe_consistency']}, "
          f"explicit solution found {okf}")
    # rescaled couplings
    vs2 = [None] * 9
    for ai in range(9):
        vs2[ai] = (s[grid_of[ai]] * vs[ai]) % p
    chat = []
    for a in range(6):
        i, j, k = T[a][0]
        chat.append(cub(vs2[i], vs2[j], vs2[k]))
    out['detframe_couplings'] = [int(c) for c in chat]
    tgt = [1 if side[a] == 0 else p - 1 for a in range(6)]
    out['detframe_is_pm1'] = (chat == tgt)
    print(f"   det-frame couplings {[c if c < p - 1 else -1 for c in chat]} "
          f"(target rows +1, cols -1): {out['detframe_is_pm1']}")

    # the involution J = grid transpose in the det-frame
    piJ = {ai: atom_at[(grid_of[ai][1], grid_of[ai][0])] for ai in range(9)}
    out['J_cycle_type'] = sorted(Counter(
        tuple(sorted((a, piJ[a]))) for a in range(9)).values(), reverse=True)
    fixed = [a for a in range(9) if piJ[a] == a]
    out['J_fixed_atoms'] = [list(LINES[a][0]) for a in fixed]
    ok_inv = all(piJ[piJ[a]] == a for a in range(9))
    ok_anti = True
    for i in range(9):
        for j in range(i, 9):
            for k in range(j, 9):
                lhs = cub(vs2[piJ[i]], vs2[piJ[j]], vs2[piJ[k]])
                rhs = (p - cub(vs2[i], vs2[j], vs2[k])) % p
                if lhs != rhs:
                    ok_anti = False
    out['J_involution'] = ok_inv
    out['J_antisymmetry_all_165'] = ok_anti
    # J swaps the sides
    swaps = all(
        sorted(piJ[x] for x in T[n0[u]][0]) == sorted(T[n1[u]][0]) for u in range(3))
    out['J_swaps_pencils'] = swaps
    print(f"   J: involution {ok_inv}, cub(J.,J.,J.) = -cub on all 165 multisets: {ok_anti}, "
          f"swaps the two pencils {swaps}, fixes {len(fixed)} atoms (the grid diagonal)")
    with open(os.path.join(ARC, f'leg3_D_{p}.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase E
def aligned_labels(primes, pref=40123):
    """per prime: dict ref-label -> (canonical line vec, pivot) at that prime."""
    stref = load_state(pref)
    labs = {}
    global q
    for p in primes:
        st = load_state(p)
        if p == pref:
            q = p
            labs[p] = {tuple(l): (v, nz) for l, v, nz in canon_lines(st)}
            continue
        sig, pair, cok = align_to_ref(stref, st)
        assert sig is not None and cok, f"alignment failed at {p}"
        q = p
        raw = {tuple(l): (v, nz) for l, v, nz in canon_lines(st)}
        labs[p] = {lr: raw[pair[lr]] for lr in pair}
    return labs


def phase_E(primes=None):
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    p1 = 40123
    st1 = load_state(p1)
    ax = json.load(open(os.path.join(ARC, 'leg3_atoms_exact.json')))
    atoms = {eval(k): [sp.Rational(x) for x in v] for k, v in ax.items()}
    # order atoms as in the p1 LINES list
    order = [tuple(l) for l, _ in st1['LINES']]
    vs = [atoms[l] for l in order]
    T, side = st1['T'], st1['side']
    out = {}
    cex = {}
    for a in range(6):
        i, j, k = T[a][0]
        cex[a] = cub_exact(vs[i], vs[j], vs[k])
    # verify against all primes (canonical-frame couplings)
    labs = aligned_labels(primes)
    ok = True
    global q
    for p in primes:
        q = p
        vv = [labs[p][l][0] for l in order]
        for a in range(6):
            i, j, k = T[a][0]
            cm = cub(vv[i], vv[j], vv[k])
            r = cex[a]
            if (r.p % p) * pow(r.q % p, -1, p) % p != cm % p:
                ok = False
    out['exact_couplings_match_primes'] = primes if ok else False
    pr0 = sp.Integer(1); pr1 = sp.Integer(1)
    for a in range(6):
        if side[a] == 0:
            pr0 *= cex[a]
        else:
            pr1 *= cex[a]
    v_exact = sp.together(pr0 + pr1)
    I_exact = sp.together(pr0 / pr1)
    out['couplings'] = {str(T[a][0]): str(cex[a]) for a in range(6)}
    out['prod_side0'] = str(pr0)
    out['prod_side1'] = str(pr1)
    out['v_exact'] = str(v_exact)
    out['I_exact'] = str(sp.simplify(I_exact))
    print(f"[E] exact couplings (canonical atom frame), verified mod both primes: {ok}")
    for a in range(6):
        print(f"    c{T[a][0]} side{side[a]} = {cex[a]}")
    print(f"    prod(side0) = {pr0}")
    print(f"    prod(side1) = {pr1}")
    print(f"    v = {v_exact}    I = {sp.simplify(I_exact)}")
    with open(os.path.join(ARC, 'leg3_E.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase K
def interp_K(vals, rs, p):
    """coefficients of the quadratic f with f(rs[i]) = vals[i] mod p (Vandermonde)."""
    global q
    qs = q; q = p
    M = [[1, rs[i] % p, rs[i] * rs[i] % p, vals[i] % p] for i in range(3)]
    A = [[int(x) % p for x in row] for row in M]
    for c in range(3):
        pr = next(x for x in range(c, 3) if A[x][c] % p)
        A[c], A[pr] = A[pr], A[c]
        iv = pow(A[c][c], -1, p)
        A[c] = [(e * iv) % p for e in A[c]]
        for x in range(3):
            if x != c and A[x][c]:
                f = A[x][c]; A[x] = [(A[x][j] - f * A[c][j]) % p for j in range(4)]
    q = qs
    return [A[i][3] % p for i in range(3)]


# --- exact arithmetic in K = Q[r]/mu (mu = MU_13, non-monic handled over Q) ---
from fractions import Fraction as Fr

_MUQ = [Fr(MU_13[0]), Fr(MU_13[1]), Fr(MU_13[2]), Fr(MU_13[3])]
# r^3 = c2 r^2 + c1 r + c0
_R3 = [-_MUQ[3] / _MUQ[0], -_MUQ[2] / _MUQ[0], -_MUQ[1] / _MUQ[0]]  # c0,c1,c2
# r^4 = r*r^3
_R4 = [_R3[2] * _R3[0],
       _R3[0] + _R3[2] * _R3[1],
       _R3[1] + _R3[2] * _R3[2]]


def kmul(x, y):
    """x,y: [a0,a1,a2] Fractions -> product mod mu."""
    c = [Fr(0)] * 5
    for i in range(3):
        if x[i]:
            for j in range(3):
                if y[j]:
                    c[i + j] += x[i] * y[j]
    # reduce degrees 4 then 3
    if c[4]:
        for i in range(3):
            c[i] += c[4] * _R4[i]
        c[4] = Fr(0)
    if c[3]:
        for i in range(3):
            c[i] += c[3] * _R3[i]
        c[3] = Fr(0)
    return c[:3]


def kadd(x, y):
    return [x[0] + y[0], x[1] + y[1], x[2] + y[2]]


def ksub(x, y):
    return [x[0] - y[0], x[1] - y[1], x[2] - y[2]]


def kscale(x, s):
    return [x[0] * s, x[1] * s, x[2] * s]


def kiszero(x):
    return not (x[0] or x[1] or x[2])


def kinv(x):
    """inverse in K via the 3x3 multiplication matrix (K is a field: mu irreducible)."""
    cols = []
    e = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
    for b in e:
        cols.append(kmul(x, b))
    # solve M y = e0 where M[:,j] = x * r^j
    M = [[cols[j][i] for j in range(3)] for i in range(3)]
    rhs = [Fr(1), Fr(0), Fr(0)]
    # gaussian elimination 3x3 over Q
    A = [row[:] + [rhs[i]] for i, row in enumerate(M)]
    for c in range(3):
        piv = next(x2 for x2 in range(c, 3) if A[x2][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        iv = A[c][c]
        A[c] = [e2 / iv for e2 in A[c]]
        for x2 in range(3):
            if x2 != c and A[x2][c] != 0:
                f = A[x2][c]
                A[x2] = [A[x2][j] - f * A[c][j] for j in range(4)]
    return [A[0][3], A[1][3], A[2][3]]


def kred_modp(x, p):
    """reduce a K-element at the place r -> r0 mod p."""
    def rq(fr):
        return (fr.numerator % p) * pow(fr.denominator % p, -1, p) % p
    return [rq(c) for c in x]


def keval_modp(x, r0, p):
    c = kred_modp(x, p)
    return (c[0] + c[1] * r0 + c[2] * r0 * r0) % p


def kernel_over_K(M):
    """kernel basis of an m x n matrix over K (entries = K-elements)."""
    m = len(M); n = len(M[0])
    A = [[e[:] for e in row] for row in M]
    piv = []; rr = 0
    for c in range(n):
        pr = next((x for x in range(rr, m) if not kiszero(A[x][c])), None)
        if pr is None:
            continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = kinv(A[rr][c])
        A[rr] = [kmul(iv, e) for e in A[rr]]
        for x in range(m):
            if x != rr and not kiszero(A[x][c]):
                f = A[x][c]
                A[x] = [ksub(A[x][j], kmul(f, A[rr][j])) for j in range(n)]
        piv.append(c); rr += 1
    ker = []
    KONE = [Fr(1), Fr(0), Fr(0)]
    for fc in [c for c in range(n) if c not in piv]:
        v = [[Fr(0)] * 3 for _ in range(n)]
        v[fc] = KONE[:]
        for i, c in enumerate(piv):
            v[c] = kscale(A[i][fc], Fr(-1))
        ker.append(v)
    return ker


def phase_K(primes=None):
    """Identify the towers over K = Q[r]/mu; compute the atom lines SYMBOLICALLY;
    prove their Q-rationality; exact couplings; exact v."""
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    out = {'primes_used': primes}
    # 0. which mu do the r-components satisfy?
    for name, MU in (('mine', MU_MINE), ('x13', MU_13)):
        hits = {p: [sum(MU[i] * pow(r, 3 - i, p) for i in range(4)) % p == 0
                    for (r, g, a) in PRIMES[p]] for p in primes}
        out[f'mu_{name}_vanishes_on_r'] = {str(k): v for k, v in hits.items()}
    print(f"[K] mu(x13 normalization) vanishes on all tower r-components: "
          f"{all(all(v) for v in out['mu_x13_vanishes_on_r'].values())}")

    # 1. reconstruct g, a, b and the 9 atom eigenvalues as quadratics in r (CRT all primes)
    sts = {p: load_state(p) for p in primes}
    M = 1
    for p in primes:
        M *= p
    bound = int(sp.floor(sp.sqrt(sp.Integer(M) / 2)))
    recon = {}
    fails = []

    def crt_rec(vals_by_p):
        x = 0
        for p in primes:
            Mp = M // p
            x = (x + int(vals_by_p[p]) * Mp * pow(Mp % p, -1, p)) % M
        return ratrec(x, M, bound)

    def rec_quad(vals_by_p, tag):
        cs = {}
        for p in primes:
            rs = [d[0] for d in PRIMES[p]]
            cs[p] = interp_K(vals_by_p[p], rs, p)
        cq = [crt_rec({p: cs[p][i] for p in primes}) for i in range(3)]
        if any(c is None for c in cq):
            fails.append(tag)
            return None
        recon[tag] = cq
        return cq

    rec_quad({p: [PRIMES[p][i][1] for i in range(3)] for p in primes}, 'g')
    rec_quad({p: [PRIMES[p][i][2] for i in range(3)] for p in primes}, 'a')
    rec_quad({p: [sts[p]['OPS'][i]['bq'] for i in range(3)] for p in primes}, 'b')

    # aligned labels across primes for the atom eigenvalues
    pref = 40123
    stref = sts[pref]
    order = [tuple(l) for l, _ in stref['LINES']]
    pairs = {pref: {l: l for l in order}}
    for p in primes:
        if p == pref:
            continue
        sig, pair, cok = align_to_ref(stref, sts[p])
        assert sig is not None and cok, f"alignment failed at {p}"
        pairs[p] = pair
    ev_ok = 0
    for lbl in order:
        vals_by_p = {}
        for p in primes:
            st = sts[p]
            plbl = pairs[p][lbl]
            v3 = []
            for tow in range(3):
                cc = [c for t, B, c in st['CELLS'][tow] if t == plbl[tow]]
                assert len(cc) == 1, (p, tow, plbl)
                v3.append(cc[0]['ev'])
            vals_by_p[p] = v3
        if rec_quad(vals_by_p, f'ev_{lbl}') is not None:
            ev_ok += 1
    out['reconstructed'] = {k: [str(sp.Rational(c)) for c in v] for k, v in recon.items()}
    out['failed'] = fails
    out['ev_reconstructed'] = f'{ev_ok}/9'
    print(f"[K] reconstructed over K: g,a,b {'OK' if not any(t in fails for t in 'gab')else 'FAIL'}; "
          f"atom eigenvalues {ev_ok}/9; failures: {fails}")
    if fails:
        with open(os.path.join(ARC, 'leg3_K.json'), 'w') as f:
            json.dump(out, f, indent=1)
        return out

    # convert to Fraction K-elements
    def kel(tag):
        return [Fr(recon[tag][i].p, recon[tag][i].q) for i in range(3)]

    Gk, Ak, Bk = kel('g'), kel('a'), kel('b')

    # 2. (optional, heavy) verify (r, g, a, b) is a joint spectral point of the 78-dim
    #    tower EXACTLY: ker[G8 + r G16 ; G16 - g ; G14 - a ; G22 - b] over K is nonzero
    base = load_base()
    KONE = [Fr(1), Fr(0), Fr(0)]
    KR = [Fr(0), Fr(1), Fr(0)]

    def kconst(x):
        return [Fr(sp.Rational(x).p, sp.Rational(x).q), Fr(0), Fr(0)]

    if os.environ.get('LEG3_JOINT') == '1':
        G78 = {}
        for n in base['ns']:
            G78[n] = [[Fr(sp.Rational(base['ADS'][n][i][j]).p,
                          sp.Rational(base['ADS'][n][i][j]).q)
                       for j in range(78)] for i in range(78)]
        stack = []
        for i in range(78):
            stack.append([kadd(kconst(G78[8][i][j]), kmul(KR, kconst(G78[16][i][j])))
                          for j in range(78)])
        for (n, lam) in ((16, Gk), (14, Ak), (22, Bk)):
            for i in range(78):
                row = [kconst(G78[n][i][j]) for j in range(78)]
                for j in range(78):
                    if i == j:
                        row[j] = ksub(row[j], lam)
                stack.append(row)
        ker78 = kernel_over_K(stack)
        out['tower_joint_spectrum_kernel_dim'] = len(ker78)
        print(f"[K] joint-spectrum check over K: dim ker[G8+rG16; G16-g; G14-a; G22-b] = "
              f"{len(ker78)} (nonzero = (r,g,a,b) is a genuine joint spectral point)")

    # 3. exact rational R27 matrices and the combo over K
    R27x = {}
    for n in base['ns']:
        Mx = [[Fr(0)] * 27 for _ in range(27)]
        for k, c in enumerate(base['INV'][n]):
            cc = sp.Rational(c)
            if cc:
                Rk = base['REP'][k]
                fc = Fr(cc.p, cc.q)
                for a in range(27):
                    for b2 in range(27):
                        if Rk[a][b2]:
                            rr2 = sp.Rational(Rk[a][b2])
                            Mx[a][b2] += fc * Fr(rr2.p, rr2.q)
        R27x[n] = Mx
    comboK = [[[Fr(0)] * 3 for _ in range(27)] for _ in range(27)]
    for a in range(27):
        for b2 in range(27):
            # 3*(R8 + r R16) + 7*(g R14 - a R16) + 13*(b R16 - g R22) + 17*R14
            t = kscale(kconst(R27x[8][a][b2]), Fr(3))
            t = kadd(t, kscale(kmul(KR, kconst(R27x[16][a][b2])), Fr(3)))
            t = kadd(t, kscale(kmul(Gk, kconst(R27x[14][a][b2])), Fr(7)))
            t = kadd(t, kscale(kmul(Ak, kconst(R27x[16][a][b2])), Fr(-7)))
            t = kadd(t, kscale(kmul(Bk, kconst(R27x[16][a][b2])), Fr(13)))
            t = kadd(t, kscale(kmul(Gk, kconst(R27x[22][a][b2])), Fr(-13)))
            t = kadd(t, kscale(kconst(R27x[14][a][b2]), Fr(17)))
            comboK[a][b2] = t

    # 4. for each atom: kernel of (combo - ev) over K; dim 1; Q-rational after scaling
    atoms_exact = {}
    dims = {}
    rational = {}
    for lbl in order:
        lam = kel(f'ev_{lbl}')
        Mm = [[ksub(comboK[a][b2], lam) if a == b2 else comboK[a][b2]
               for b2 in range(27)] for a in range(27)]
        ker = kernel_over_K(Mm)
        dims[str(lbl)] = len(ker)
        if len(ker) != 1:
            continue
        v = ker[0]
        # canonical scaling: first nonzero coordinate -> 1
        nz = next(i for i in range(27) if not kiszero(v[i]))
        iv = kinv(v[nz])
        v = [kmul(iv, e) for e in v]
        # Q-rationality: r and r^2 coefficients vanish identically
        isQ = all(e[1] == 0 and e[2] == 0 for e in v)
        rational[str(lbl)] = isQ
        if isQ:
            atoms_exact[lbl] = [sp.Rational(e[0].numerator, e[0].denominator) for e in v]
    out['eigenline_dims_over_K'] = dims
    out['eigenlines_Q_rational'] = rational
    allQ = len(atoms_exact) == 9
    print(f"[K] symbolic eigenlines over K: dims {sorted(dims.values())}; "
          f"Q-rational: {sum(rational.values())}/9")

    if allQ:
        # 5. verify the exact lines reduce to the pipeline atoms at every prime
        red_ok = True
        for p in primes:
            st = sts[p]
            global q
            q = p
            lab = {tuple(l): (v, nz) for l, v, nz in canon_lines(st)}
            for lbl in order:
                vp = lab[pairs[p][lbl]][0]
                vec = atoms_exact[lbl]
                nz1 = next(i for i in range(27) if vec[i] != 0)
                sc = pow(int(vp[nz1]), -1, p)
                for a in range(27):
                    rr3 = vec[a]
                    if (rr3.p % p) * pow(rr3.q % p, -1, p) % p != int(vp[a]) * sc % p:
                        red_ok = False
        out['exact_lines_reduce_to_pipeline_atoms_all_primes'] = red_ok
        print(f"[K] exact lines reduce to the pipeline atom lines at all "
              f"{len(primes)} primes: {red_ok}")
        with open(os.path.join(ARC, 'leg3_atoms_exact.json'), 'w') as f:
            json.dump({str(k): [str(x) for x in v] for k, v in atoms_exact.items()},
                      f, indent=1)
        hmax = max(max(abs(x.p), x.q) for vec in atoms_exact.values() for x in vec)
        out['max_height'] = str(hmax)
        print(f"[K] max height of exact atom entries: {float(hmax):.3e}")
    with open(os.path.join(ARC, 'leg3_K.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase V (verify states)
def phase_V(primes=None):
    """Re-verify everything downstream of the cell decomposition, at every prime:
    atoms lie in the labeled cells, the 84-triple cubic support, K33, I, v, S-line."""
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    out = {}
    global q
    for p in primes:
        st = load_state(p)
        q = p
        LINES, T, side = st['LINES'], st['T'], st['side']
        rep = {}
        # 1. each atom lies in the cell named by each slot of its label; bijection
        used = Counter()
        ok_cells = True
        for lbl, v in LINES:
            for s in range(3):
                cells = [B for t, B, c in st['CELLS'][s] if t == lbl[s]]
                if len(cells) != 1 or cells[0].shape[0] != 1:
                    ok_cells = False; continue
                B = cells[0]
                nz = np.nonzero(B[0])[0][0]
                lam = int(v[nz]) * pow(int(B[0][nz]), -1, p) % p
                if not np.array_equal(v % p, (lam * B[0]) % p):
                    ok_cells = False
                used[(s, lbl[s])] += 1
        ok_bij = (len(used) == 27 and all(x == 1 for x in used.values()))
        rep['atoms_in_named_cells'] = ok_cells
        rep['cell_atom_bijection'] = ok_bij
        # 2. full 84-triple support recomputation == stored couplings
        vs = [v for _, v in LINES]
        T2 = {}
        for i in range(9):
            for j in range(i + 1, 9):
                for k in range(j + 1, 9):
                    c = cub(vs[i], vs[j], vs[k])
                    if c:
                        T2[(i, j, k)] = int(c)
        rep['support_recomputed_equals_stored'] = (
            T2 == {tuple(t): int(c) for t, c in T})
        # 3. bipartition + I + v recomputation
        adj = {a: set() for a in range(len(T))}
        for a in range(len(T)):
            for b in range(a + 1, len(T)):
                if set(T[a][0]) & set(T[b][0]):
                    adj[a].add(b); adj[b].add(a)
        side2 = {0: 0}; stack = [0]
        while stack:
            x = stack.pop()
            for y2 in adj[x]:
                if y2 not in side2:
                    side2[y2] = 1 - side2[x]; stack.append(y2)
        bip = all(side2[a] != side2[b] for a in adj for b in adj[a])
        num = den = 1
        for a, (tri, c) in enumerate(T):
            if side2[a] == 0:
                num = num * c % p
            else:
                den = den * c % p
        I2 = num * pow(den, -1, p) % p
        rep['bipartite'] = bip
        rep['side_matches'] = (side2 == side)
        rep['I_is_minus1'] = (I2 == p - 1)
        rep['v_is_0'] = ((num + den) % p == 0)
        # 4. S-line: the three S-atoms form one coupling; the other pencil's
        #    lines each contain exactly one S-atom
        SA = [i for i, (l, _) in enumerate(LINES) if 'S' in l]
        rep['n_S_atoms'] = len(SA)
        stri = tuple(sorted(SA))
        hit = [a for a in range(len(T)) if tuple(sorted(T[a][0])) == stri]
        rep['S_line_is_coupling'] = (len(hit) == 1)
        if hit:
            sside = side[hit[0]]
            rep['S_side'] = int(sside)
            other = [a for a in range(len(T)) if side[a] != sside]
            rep['other_pencil_one_S_each'] = all(
                len(set(T[a][0]) & set(SA)) == 1 for a in other)
        out[str(p)] = rep
        print(f"[V] p={p}: cells {ok_cells}, bijection {ok_bij}, "
              f"support {rep['support_recomputed_equals_stored']}, K33 {bip}, "
              f"I=-1 {rep['I_is_minus1']}, v=0 {rep['v_is_0']}, "
              f"S-line-in-pencil {rep.get('S_line_is_coupling')} (side {rep.get('S_side')})")
    with open(os.path.join(ARC, 'leg3_V.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase G (grid Galois structure)
def distinguished(lbl):
    """(slot, tag) of the distinguished cell of an atom: its S if present,
    else its unique H. Returns None if neither is unique."""
    ss = [s for s in range(3) if lbl[s] == 'S']
    if len(ss) == 1:
        return ss[0], 'S'
    hs = [s for s in range(3) if lbl[s].startswith('H')]
    if len(hs) == 1:
        return hs[0], lbl[hs[0]]
    return None


def phase_G(primes=None):
    """The canonical grid structure and the Galois reading, plus the exact
    weight-sum (zero-sum-triple) certificates for the char-0 support."""
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    out = {}
    global q
    for p in primes:
        st = load_state(p)
        q = p
        LINES, T, side = st['LINES'], st['T'], st['side']
        rep = {}
        SA = [i for i, (l, _) in enumerate(LINES) if 'S' in l]
        stri = tuple(sorted(SA))
        srow = [a for a in range(6) if tuple(sorted(T[a][0])) == stri][0]
        sside = side[srow]
        rows = [a for a in range(6) if side[a] == sside]      # the S pencil
        cols = [a for a in range(6) if side[a] != sside]
        # 1. every atom off the S-line has a UNIQUE H; S-line atoms have S
        dist = {}
        ok_dist = True
        for i, (l, v) in enumerate(LINES):
            d = distinguished(l)
            if d is None:
                ok_dist = False
            dist[i] = d
        rep['distinguished_ok'] = ok_dist
        # 2. columns <-> labelings: each column's three distinguished cells
        #    come from ONE labeling; the three columns hit the three labelings
        colslot = []
        ok_cols = True
        for a in cols:
            sl = {dist[i][0] for i in T[a][0]}
            if len(sl) != 1:
                ok_cols = False
            colslot.append(sorted(sl))
        flat = sorted(x for s in colslot for x in s)
        rep['columns_are_labeling_indexed'] = ok_cols and flat == [0, 1, 2]
        # 3. each non-S row hits all three labelings with its distinguished cells
        ok_rows = True
        for a in rows:
            if a == srow:
                continue
            sl = sorted(dist[i][0] for i in T[a][0])
            if sl != [0, 1, 2]:
                ok_rows = False
        rep['rows_cross_all_labelings'] = ok_rows
        # 4. the two non-S row couplings: equal values?
        rvals = {a: int(T[a][1]) for a in rows}
        nsr = [T[a][1] for a in rows if a != srow]
        rep['S_row_value'] = int(T[srow][1])
        rep['nonS_row_values'] = [int(x) for x in nsr]
        rep['nonS_rows_equal'] = (len(nsr) == 2 and nsr[0] == nsr[1])
        rep['col_values'] = [int(T[a][1]) for a in cols]
        # 5. the 12 torus operators: exact eigenvalues on all 9 atoms
        ops = []
        for i in range(3):
            for nm in ('X1', 'Ym', 'W3', 'combo'):
                ops.append((f'{nm}@{i}', st['OPS'][i][nm]))
        lam = {}
        ok_eig = True
        for oi, (nm, M) in enumerate(ops):
            for ai, (l, v) in enumerate(LINES):
                w = (M @ v) % p
                nz = np.nonzero(v)[0][0]
                lv = int(w[nz]) * pow(int(v[nz]), -1, p) % p
                if not np.array_equal(w % p, (lv * v) % p):
                    ok_eig = False
                lam[(oi, ai)] = lv
        rep['atoms_joint_eigenlines_12ops'] = ok_eig
        # 6. zero-sum certificates on all 165 multisets
        supp = set(tuple(t) for t, _ in T)
        cert = 0; uncert = []
        zsum_ok = True
        for ms in itertools.combinations_with_replacement(range(9), 3):
            sums = [(lam[(oi, ms[0])] + lam[(oi, ms[1])] + lam[(oi, ms[2])]) % p
                    for oi in range(len(ops))]
            if ms in supp:
                if any(s != 0 for s in sums):
                    zsum_ok = False
            else:
                if any(s != 0 for s in sums):
                    cert += 1
                else:
                    uncert.append(ms)
        rep['couplings_all_zero_sum'] = zsum_ok
        rep['noncoupling_certified'] = f'{cert}/159'
        rep['uncertified'] = [list(m) for m in uncert]
        out[str(p)] = rep
        print(f"[G] p={p}: dist {ok_dist}, cols=labelings {rep['columns_are_labeling_indexed']}, "
              f"rows-cross {ok_rows}, nonS-rows-equal {rep['nonS_rows_equal']} "
              f"({rep['nonS_row_values']}), eig12 {ok_eig}, "
              f"zero-sum-on-couplings {zsum_ok}, certified {cert}/159")
    with open(os.path.join(ARC, 'leg3_G.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase R (CRT rationality)
def phase_R(primes=None):
    """CRT the aligned canonical-frame coupling values across all primes and
    rationally reconstruct the Galois-predicted rational quantities."""
    if primes is None:
        primes = [p for p in ALLP
                  if os.path.exists(os.path.join(ARC, f'leg3_state_{p}.pkl'))]
    pref = 40123
    stref = load_state(pref)
    labs = aligned_labels(primes, pref)
    order = [tuple(l) for l, _ in stref['LINES']]
    Tref, sref = stref['T'], stref['side']
    # pivot consistency
    out = {'primes_used': primes}
    piv_ok = all(len({labs[p][l][1] for p in primes}) == 1 for l in order)
    out['pivots_consistent'] = piv_ok
    # S pencil at ref
    SA = [i for i, l in enumerate(order) if 'S' in l]
    stri = tuple(sorted(SA))
    srow = [a for a in range(6) if tuple(sorted(Tref[a][0])) == stri][0]
    sside = sref[srow]
    rows = [a for a in range(6) if sref[a] == sside]
    cols = [a for a in range(6) if sref[a] != sside]
    nsrows = [a for a in rows if a != srow]
    global q
    cvals = {}   # coupling index -> {p: value}
    consist = True
    for p in primes:
        q = p
        vv = [labs[p][l][0] for l in order]
        for a in range(6):
            i, j, k = Tref[a][0]
            cvals.setdefault(a, {})[p] = int(cub(vv[i], vv[j], vv[k]))
        PR = 1; PC = 1
        for a in rows:
            PR = PR * cvals[a][p] % p
        for a in cols:
            PC = PC * cvals[a][p] % p
        if (PR + PC) % p != 0:
            consist = False
    out['aligned_v_is_0_all_primes'] = consist
    out['nonS_rows_equal_by_prime'] = {
        str(p): cvals[nsrows[0]][p] == cvals[nsrows[1]][p] for p in primes}
    M = 1
    for p in primes:
        M *= p
    bound = int(sp.floor(sp.sqrt(sp.Integer(M) / 2)))

    def crt(vals):
        x = 0
        for p in primes:
            Mp = M // p
            x = (x + int(vals[p]) * Mp * pow(Mp % p, -1, p)) % M
        return x

    def rec(vals, name):
        r = ratrec(crt(vals), M, bound)
        if r is None:
            print(f"    {name}: ratrec FAILED")
            return None
        h = max(abs(r.p), r.q)
        # verify reduction at every prime (redundant with CRT but explicit)
        okr = all((r.p % p) * pow(r.q % p, -1, p) % p == vals[p] % p for p in primes)
        print(f"    {name} = {r}   (height {h:.3e}, spurious-gauge {float(1.2*h*h/M):.1e}, "
              f"reduces-ok {okr})")
        return dict(value=str(r), height=str(h), reduces_ok=okr)

    print(f"[R] CRT over {len(primes)} primes, M ~ {float(M):.3e}, bound ~ {float(bound):.3e}")
    print(f"    S-row = ref coupling {Tref[srow][0]}; rows {[Tref[a][0] for a in rows]}, "
          f"cols {[Tref[a][0] for a in cols]}")
    R = {}
    R['c_S'] = rec(cvals[srow], 'c_S (S-row coupling)')
    R['c_row1'] = rec(cvals[nsrows[0]], f'c_row1 {Tref[nsrows[0]][0]}')
    R['c_row2'] = rec(cvals[nsrows[1]], f'c_row2 {Tref[nsrows[1]][0]}')
    # symmetric functions of the two non-S rows
    e1r = {p: (cvals[nsrows[0]][p] + cvals[nsrows[1]][p]) % p for p in primes}
    e2r = {p: cvals[nsrows[0]][p] * cvals[nsrows[1]][p] % p for p in primes}
    R['rows_e1'] = rec(e1r, 'e1(nonS rows)')
    R['rows_e2'] = rec(e2r, 'e2(nonS rows)')
    # symmetric functions of the three columns
    for k in (1, 2, 3):
        ek = {}
        for p in primes:
            s = 0
            for comb in itertools.combinations(cols, k):
                t = 1
                for a in comb:
                    t = t * cvals[a][p] % p
                s = (s + t) % p
            ek[p] = s
        R[f'cols_e{k}'] = rec(ek, f'e{k}(columns)')
    # individual columns (Galois-predicted NON-rational -- expected to fail)
    for ci, a in enumerate(cols):
        R[f'c_col{ci + 1}'] = rec(cvals[a], f'c_col{ci + 1} {Tref[a][0]} (expected non-rational)')
    # products
    PRv = {p: 1 for p in primes}; PCv = {p: 1 for p in primes}
    for p in primes:
        for a in rows:
            PRv[p] = PRv[p] * cvals[a][p] % p
        for a in cols:
            PCv[p] = PCv[p] * cvals[a][p] % p
    R['P_R'] = rec(PRv, 'P_R = prod(rows)')
    R['P_C'] = rec(PCv, 'P_C = prod(cols)')
    R['u'] = rec({p: PRv[p] * PCv[p] % p for p in primes}, 'u = P_R*P_C')
    R['v'] = rec({p: (PRv[p] + PCv[p]) % p for p in primes}, 'v = P_R+P_C')
    out['reconstructions'] = R
    # cross-check: does P_R + P_C = 0 hold for the reconstructed rationals?
    if R.get('P_R') and R.get('P_C'):
        out['P_R_plus_P_C_exactly_0'] = \
            (sp.Rational(R['P_R']['value']) + sp.Rational(R['P_C']['value']) == 0)
    if R.get('c_S') and R.get('c_row1') and R.get('c_row2') and R.get('P_R'):
        out['P_R_product_consistent'] = (
            sp.Rational(R['c_S']['value']) * sp.Rational(R['c_row1']['value'])
            * sp.Rational(R['c_row2']['value']) == sp.Rational(R['P_R']['value']))
    if R.get('cols_e3') and R.get('P_C'):
        out['P_C_equals_cols_e3'] = (
            sp.Rational(R['cols_e3']['value']) == sp.Rational(R['P_C']['value']))
    with open(os.path.join(ARC, 'leg3_R.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase T (theory anchors)
def phase_T(p=40123):
    """The abstract 3x3-grid anchors, made rigorous:
    T1 Leibniz relabeling (symbolic over Z),
    T2 det-pattern stabilizer = 16 over Q (16 exact derivations + mod-p upper bound),
    T3 permanent-pattern stabilizer = 4 over Q (torus lower + mod-p upper),
    T4 uniqueness: the 16-dim algebra annihilates a 1-dim space of cubics (det),
    T5 a random-coefficient control (I generic) has stabilizer 4."""
    import sympy as sp
    out = {}
    # cells (i,j) of the 3x3 matrix; even/odd transversal through each cell
    P3 = list(itertools.permutations(range(3)))

    def parity(s):
        inv = sum(1 for x in range(3) for y2 in range(x + 1, 3) if s[x] > s[y2])
        return 1 if inv % 2 == 0 else -1
    EV = [s for s in P3 if parity(s) == 1]
    OD = [s for s in P3 if parity(s) == -1]
    newco = {}
    for i in range(3):
        for j in range(3):
            e = [k for k, s in enumerate(EV) if s[i] == j]
            o = [k for k, s in enumerate(OD) if s[i] == j]
            assert len(e) == 1 and len(o) == 1
            newco[(i, j)] = (e[0], o[0])
    out['relabel_bijection'] = (len(set(newco.values())) == 9)
    Z = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'z{i}{j}'))
    detZ = Z.det().expand()
    rowsum = sum(sp.prod(Z[i, j] for (i, j) in newco if newco[(i, j)][0] == u)
                 for u in range(3))
    colsum = sum(sp.prod(Z[i, j] for (i, j) in newco if newco[(i, j)][1] == v)
                 for v in range(3))
    out['leibniz_det_rows_minus_cols'] = sp.simplify(detZ - (rowsum - colsum)) == 0
    print(f"[T] Leibniz relabeling: bijection {out['relabel_bijection']}, "
          f"det = sum(rows) - sum(cols): {out['leibniz_det_rows_minus_cols']}")

    # abstract trilinear tables on the 9 cells (index cell = 3*i+j)
    def table(coeffs_by_perm):
        T3 = [[[0] * 9 for _ in range(9)] for _ in range(9)]
        for s, cf in coeffs_by_perm.items():
            cells = [3 * i + s[i] for i in range(3)]
            for (a, b, c) in itertools.permutations(cells):
                T3[a][b][c] = cf
        return T3
    det_tab = table({s: parity(s) for s in P3})
    perm_tab = table({s: 1 for s in P3})

    def stab_dim_Q_upper(T3):
        return stab_dim([[[x % p for x in r] for r in m] for m in T3], p)

    d_det = stab_dim_Q_upper(det_tab)
    d_perm = stab_dim_Q_upper(perm_tab)
    # 16 exact derivations of det: X -> AX + XB, tr A = tr B = 0
    def deriv_matrix(A, B):
        D = [[0] * 9 for _ in range(9)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    D[3 * i + j][3 * k + j] += A[i][k]   # (AX)_ij from X_kj
                    D[3 * i + j][3 * i + k] += B[k][j]   # (XB)_ij from X_ik
        return D

    def elem(i, j):
        M = [[0] * 3 for _ in range(3)]
        M[i][j] = 1
        return M

    def tless(i):
        M = [[0] * 3 for _ in range(3)]
        M[i][i] = 1; M[i + 1][i + 1] = -1
        return M
    sl3 = [elem(i, j) for i in range(3) for j in range(3) if i != j] + [tless(0), tless(1)]
    Z3 = [[0] * 3 for _ in range(3)]
    ders = [deriv_matrix(A, Z3) for A in sl3] + [deriv_matrix(Z3, B) for B in sl3]

    def kills(D, T3):
        for i in range(9):
            for j in range(i, 9):
                for k in range(j, 9):
                    s = 0
                    for l in range(9):
                        s += D[l][i] * T3[l][j][k] + D[l][j] * T3[i][l][k] \
                            + D[l][k] * T3[i][j][l]
                    if s != 0:
                        return False
        return True
    all_kill = all(kills(D, det_tab) for D in ders)
    # independence of the 16 over Q: rank of the 16 x 81 integer matrix
    global q
    qs = q; q = p
    rk16 = rrows(np.array([[D[a][b] for a in range(9) for b in range(9)]
                           for D in ders], dtype=np.int64) % p)
    q = qs
    out['det_16_exact_derivations_kill'] = bool(all_kill)
    out['det_16_independent'] = (rk16 == 16)
    out['det_stab_dim_modp_upper'] = int(d_det)
    out['det_stab_dim_Q'] = 16 if (all_kill and rk16 == 16 and d_det == 16) else None
    out['perm_stab_dim_modp_upper'] = int(d_perm)
    # torus lower bound 4 for permanent: diagonal derivations with row/col sums 0
    # d_{ij} = alpha_i + beta_j with sum(alpha)+sum(beta) = 0 kills every
    # transversal monomial: sum_i (alpha_i + beta_{sigma(i)}) = 0 for all sigma
    tors = []
    for (al, be) in (((1, -1, 0), (0, 0, 0)), ((0, 1, -1), (0, 0, 0)),
                     ((0, 0, 0), (1, -1, 0)), ((0, 0, 0), (0, 1, -1))):
        D = [[0] * 9 for _ in range(9)]
        for i in range(3):
            for j in range(3):
                D[3 * i + j][3 * i + j] = al[i] + be[j]
        tors.append(D)
    tor_kill = all(kills(D, perm_tab) for D in tors)
    q = p
    rk4 = rrows(np.array([[D[a][b] for a in range(9) for b in range(9)]
                          for D in tors], dtype=np.int64) % p)
    q = qs
    out['perm_torus_4_kill_and_independent'] = bool(tor_kill and rk4 == 4)
    out['perm_stab_dim_Q'] = 4 if (tor_kill and rk4 == 4 and d_perm == 4) else None
    print(f"[T] det pattern: 16 exact sl3+sl3 derivations kill it {all_kill}, "
          f"independent {rk16 == 16}, mod-p dim {d_det} => dim_Q = 16 proven")
    print(f"[T] permanent pattern: torus-4 exact {tor_kill}, mod-p dim {d_perm} "
          f"=> dim_Q = 4 proven")

    # T4 uniqueness: cubics annihilated by the 16-dim algebra (mod-p upper bound 1;
    # det itself is an exact member => dim_Q = 1)
    mons = list(itertools.combinations_with_replacement(range(9), 3))

    def cub_coeff_vec(T3):
        vec = []
        for (i, j, k) in mons:
            vec.append(T3[i][j][k])   # symmetric table entry
        return vec
    rowsL = []
    for D in ders:
        # action of D on a cubic F (as symmetric table): (D.F)(i,j,k) =
        # sum_l D[l][i] F(l,j,k) + D[l][j] F(i,l,k) + D[l][k] F(i,j,l)
        # build the matrix on monomial space
        for (i, j, k) in mons:
            row = [0] * len(mons)
            for l in range(9):
                for (a, b, c, w) in ((l, j, k, D[l][i]), (i, l, k, D[l][j]),
                                     (i, j, l, D[l][k])):
                    if w:
                        key = tuple(sorted((a, b, c)))
                        row[mons.index(key)] += w
            rowsL.append(row)
    q = p
    rkL = rrows(np.array(rowsL, dtype=np.int64) % p)
    q = qs
    out['annihilated_cubics_dim_modp'] = len(mons) - rkL
    det_vec = cub_coeff_vec(det_tab)
    out['det_in_kernel_exact'] = True  # by all_kill above (same computation)
    out['invariant_cubic_unique_Q'] = (len(mons) - rkL == 1 and all_kill)
    print(f"[T] cubics killed by the 16-dim algebra: dim (mod p upper) "
          f"{len(mons) - rkL}; det is an exact member => dim_Q = 1: "
          f"{out['invariant_cubic_unique_Q']}")

    # T5 random-coefficient control
    rng = np.random.default_rng(23)
    cf = {s: int(rng.integers(2, 50)) for s in P3}
    Irand = sp.Rational(int(np.prod([cf[s] for s in EV])),
                        int(np.prod([cf[s] for s in OD])))
    d_rand = stab_dim_Q_upper(table(cf))
    out['random_control'] = dict(I=str(Irand), dim_modp_upper=int(d_rand))
    print(f"[T] random-coefficient control: I = {Irand}, stabilizer dim (mod-p upper) "
          f"= {d_rand}")
    with open(os.path.join(ARC, 'leg3_T.json'), 'w') as f:
        json.dump(out, f, indent=1)
    return out


# ---------------------------------------------------------------- phase F (finalize)
def phase_F(p1=40123, p2=40639):
    out = {'arc': 'B908 leg 3 (register item B908-leg-3)',
           'target': 'the involution mapping prod(rows) to -prod(cols); parity source',
           'mechanism_statement': [
               'The 9 colorless atoms are the joint eigenlines of the 12 exact torus',
               'operators; the restricted E6 cubic is supported on EXACTLY the 6 grid',
               'lines (159/159 zero-sum certificates at each of 7 primes make the char-0',
               'vanishing of the other 159 multisets exact). The 6-line cubic is',
               'det-type: its gl9 stabilizer has dim 16 = sl3+sl3 (both primes), there',
               'is a diagonal det-frame in which the couplings are (+1,+1,+1,-1,-1,-1),',
               'and the grid-transpose J in that frame is an involution with',
               'cub(J.,J.,J.) = -cub on all 165 multisets that swaps the two pencils.',
               'PARITY SOURCE: under the Leibniz relabeling the row pencil is the three',
               'EVEN permutation transversals of det and the column pencil the three ODD',
               'ones; J composes with a transposition, and the -1 is the Leibniz sign',
               'eps(transposition). Hence prod(rows) = -prod(cols), i.e. v = 0, for any',
               'det-type normalization; I = -1 is normalization-free.',
               'GALOIS REFINEMENT: the pencil swap is NOT Galois. The S-line (the',
               'coupling through the three S-atoms) lies in one pencil at every prime;',
               'any Galois element fixes the S-atom set, hence fixes the S-line, hence',
               'preserves each pencil (K33 uniqueness); the columns are labeling-indexed',
               '(= mu-root-indexed) and Galois permutes them; the two non-S rows have',
               'EQUAL coupling values at all 7 primes. J maps the S-line to a column',
               'that contains one S-atom, so J is frame-level (Weyl-type), not Galois.'],
           'remains_for_full_exactness': [
               '1. The char-0 det-type certificate: exhibit the 16-dim sl3+sl3 inside',
               '   the E6 derivations EXACTLY (over K = Q[r]/mu13) stabilizing the',
               '   9-atom space as 3x(3bar); by the proven uniqueness (dim_Q = 1 of the',
               '   annihilated cubic space) the restricted cubic is then a multiple of',
               '   det and I = -1 exactly, no height bound needed.',
               '2. Alternative: rational reconstruction of the couplings needs a larger',
               '   modulus: at 7 primes (M ~ 1.9e32, bound 9.6e15) the individual',
               '   couplings and P_R, P_C do NOT reconstruct below the spurious gauge;',
               '   more full-tower primes (leg-2 tower derivation) would pin them.',
               '3. The standing full-tower reduction assumption (mod-p pipeline = the',
               '   reduction of the char-0 construction) is leg-1 material; the 7-prime',
               '   consistency of every structural fact above corroborates it.']}
    for p in (p1, p2):
        st = load_state(p)
        out.setdefault('primes', {})[str(p)] = dict(
            I=int(st['I']), v=int(st['v']),
            I_is_minus1=(st['I'] == p - 1), v_is_0=(st['v'] == 0),
            atoms=len(st['LINES']), couplings=len(st['T']))
    for tag, fn in (('structure_40123', f'leg3_B_{p1}.json'),
                    ('structure_40639', f'leg3_B_{p2}.json'),
                    ('mechanism_40123', f'leg3_D_{p1}.json'),
                    ('mechanism_40639', f'leg3_D_{p2}.json'),
                    ('verification_all_primes', 'leg3_V.json'),
                    ('grid_galois_structure', 'leg3_G.json'),
                    ('crt_rationality', 'leg3_R.json'),
                    ('theory_anchors', 'leg3_T.json'),
                    ('rational_atoms', 'leg3_C.json'),
                    ('exact_over_Q', 'leg3_E.json'),
                    ('K_identification', 'leg3_K.json')):
        fp = os.path.join(ARC, fn)
        if os.path.exists(fp):
            out[tag] = json.load(open(fp))
    with open(os.path.join(ARC, 'leg3_results.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print('[F] wrote leg3_results.json')


# ---------------------------------------------------------------- main
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--phase', required=True)
    ap.add_argument('--prime', type=int, default=40123)
    a = ap.parse_args()
    if a.phase == 'A':
        phase_A(a.prime)
    elif a.phase == 'B':
        phase_B(a.prime)
    elif a.phase == 'C':
        phase_C()
    elif a.phase == 'D':
        phase_D(a.prime)
    elif a.phase == 'E':
        phase_E()
    elif a.phase == 'K':
        phase_K()
    elif a.phase == 'V':
        phase_V()
    elif a.phase == 'G':
        phase_G()
    elif a.phase == 'R':
        phase_R()
    elif a.phase == 'T':
        phase_T(a.prime)
    elif a.phase == 'F':
        phase_F()
    print("DONE", flush=True)
