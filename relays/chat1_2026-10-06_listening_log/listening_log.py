"""The listening log (PREREG 5b5e70c6): run three acts tick by tick and record only native invariants."""
import itertools, json, snappy, sympy as sp

PRIMES = [2, 3, 5, 7, 11, 13]
ACTS = {'golden': (1, 'b-+L'), 'silver': (2, 'b-+LL'), 'bronze': (3, 'b-+LLL')}

def clock(X, p):
    Xp = X.applyfunc(lambda v: v % p); P = Xp; k = 1
    while P != sp.eye(2): P = (P * Xp).applyfunc(lambda v: v % p); k += 1
    return k
def kerdim(Y, p):
    Yp = Y.applyfunc(lambda v: v % p)
    return 2 - sp.Matrix(Yp).rank(iszerofunc=lambda v: v % p == 0) if False else 2 - rank_mod(Yp, p)
def rank_mod(A, p):
    M = [[int(A[i, j]) % p for j in range(2)] for i in range(2)]; r = 0
    for c in range(2):
        k = next((i for i in range(r, 2) if M[i][c] % p), None)
        if k is None: continue
        M[r], M[k] = M[k], M[r]; iv = pow(M[r][c], -1, p); M[r] = [(v * iv) % p for v in M[r]]
        for i in range(2):
            if i != r and M[i][c] % p: f = M[i][c]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r
def prank(h, p): return sum(1 for q in str(h).replace(' ', '').split('+') if q.startswith('Z/') and int(q[2:]) % p == 0)

# ---------- the 2T door ----------
q = 3
SL = [g for g in itertools.product(range(q), repeat=4) if (g[0]*g[3]-g[1]*g[2]) % q == 1]
def mul(g, h): a, b, c, d = g; e, f, x, y = h; return ((a*e+b*x) % q, (a*f+b*y) % q, (c*e+d*x) % q, (c*f+d*y) % q)
def inv(g): a, b, c, d = g; return (d, (-b) % q, (-c) % q, a)
I = (1, 0, 0, 1)
def ev(w, val):
    r = I
    for ch in w: r = mul(r, val[ch.lower()] if ch.islower() else inv(val[ch.lower()]))
    return r
def gsize(gs):
    S = {I}; fr = [I]
    while fr:
        x = fr.pop()
        for g in gs:
            y = mul(x, g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)
def door(N):
    G = N.fundamental_group(); gens = list(G.generators()); rels = list(G.relators())
    if len(gens) > 3: return None
    return sum(1 for vals in itertools.product(SL, repeat=len(gens))
               if all(ev(r, dict(zip(gens, vals))) == I for r in rels) and gsize(vals) == 24)

rows = []
for act, (m, name) in ACTS.items():
    X = sp.Matrix([[m, 1], [1, 0]]); P = snappy.Manifold(name); v0 = float(P.volume())
    Lw, Rw = 'L' * m, 'R' * m
    def tick(k):  # the bundle of X_m^k (validated against golden's unique cyclic covers, k = 1..10)
        return snappy.Manifold('b++' + (Lw + Rw) * (k // 2)) if k % 2 == 0 else snappy.Manifold('b-+' + Lw + (Rw + Lw) * ((k - 1) // 2))
    clocks = {p: clock(X, p) for p in PRIMES}
    for k in range(1, 11):
        C = tick(k)
        Xk = X**k; h = C.homology(); ori = C.is_orientable()
        try: sym = C.symmetry_group(); so = sym.order(); am = sym.is_amphicheiral() if ori else None
        except Exception: so, am = None, None
        try: cs = round(float(C.chern_simons()) % 0.5, 10) if ori else None
        except Exception: cs = None
        try: nm = ([str(x) for x in C.identify()] or ['?'])[0]
        except Exception: nm = '?'
        row = dict(act=act, k=k, det=int(Xk.det()), orientable=ori, name=nm, vol_ratio=round(float(C.volume()) / (k * v0), 10),
                   cusps=C.num_cusps(), H1=str(h), sym=so, amphichiral=am, CS=cs, door=door(C))
        for p in PRIMES:
            row[f'r{p}'] = prank(h, p); row[f'ker{p}'] = 2 - rank_mod(Xk - sp.eye(2), p); row[f'home{p}'] = (k % clocks[p] == 0)
        rows.append(row)
    print(f"{act}: clocks {clocks}")
json.dump(rows, open(__file__.replace('listening_log.py', 'log.json'), 'w'), indent=1)

# ---------- A1: the table ----------
print(f"\n{'act':6} {'k':>2} {'det':>3} {'or':>2} {'name':>14} {'H1':>20} {'r2 r3 r5 r7 r11 r13':>20} {'sym':>4} {'amph':>5} {'CS':>8} {'door':>5}")
for r in rows:
    pr = ' '.join(f"{r[f'r{p}']}" for p in PRIMES)
    print(f"{r['act']:6} {r['k']:>2} {r['det']:>3} {('Y' if r['orientable'] else 'N'):>2} {r['name'][:14]:>14} {r['H1'][:20]:>20} "
          f"{pr:>20} {str(r['sym']):>4} {str(r['amphichiral']):>5} {str(r['CS']):>8} {str(r['door']):>5}")
# ---------- A2: the fixed analysis ----------
print("\nA2")
E1 = all(r['orientable'] == (r['k'] % 2 == 0) for r in rows); E4 = all(abs(r['vol_ratio'] - 1) < 1e-8 for r in rows)
E2 = all(r[f'r{p}'] == r[f'ker{p}'] for r in rows for p in PRIMES)
E3 = all(r['amphichiral'] for r in rows if r['k'] % 4 == 2)
print(f"  E1 orientability alternates: {E1}   E4 volume ratio 1: {E4}   E2 p-rank = ker dim: {E2}   E3 k=2 mod 4 amphichiral: {E3}")
for act in ACTS:
    R = [r for r in rows if r['act'] == act]
    full = {p: [r['k'] for r in R if r[f'r{p}'] == 2] for p in PRIMES}
    one = {p: [r['k'] for r in R if r[f'r{p}'] == 1] for p in PRIMES}
    print(f"  {act}: full p-layers (p-rank 2) at ticks {full}")
    print(f"  {' ' * len(act)}  half p-layers (p-rank 1) at ticks {one}")
    print(f"  {' ' * len(act)}  k=0 mod 4 amphichiral: {[(r['k'], r['amphichiral']) for r in R if r['k'] % 4 == 0]}")
    print(f"  {' ' * len(act)}  CS on orientable ticks: {[(r['k'], r['CS']) for r in R if r['orientable']]}")
    print(f"  {' ' * len(act)}  2T door by tick: {[(r['k'], r['door']) for r in R]}")
    print(f"  {' ' * len(act)}  |Sym| by tick: {[(r['k'], r['sym']) for r in R]}")
