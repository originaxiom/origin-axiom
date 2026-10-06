"""R2 (the register as complex conjugation, prime by prime) and R3 (the paper's Scope 7.2 on A5). PREREG_2 34082da5."""
import itertools, sympy as sp, snappy

# ---------- Riley's representation, checked exactly over Z[omega] ----------
om = sp.Symbol('om')
def red(e): return sp.expand(sp.rem(sp.expand(e), om**2 + om + 1, om))
X = sp.Matrix([[1, 1], [0, 1]]); Y = sp.Matrix([[1, 0], [-om, 1]])
Xi, Yi = X.inv(), Y.adjugate()                      # det Y = 1
W = Xi * Y * X * Yi
lhs = (W * X).applyfunc(red); rhs = (Y * W).applyfunc(red)
print(f"Riley relation w x = y w exact over Z[omega]: {lhs == rhs}")
print(f"tr(xy) = {red((X*Y).trace())}  (not in Z: the control that c can act)")

WORDS = ['x', 'y', 'xy', 'xY', 'xxy', 'xyy', 'xyxY', 'xxyY', 'xyXy']
def mat_word(wd, Xm, Ym, mul, inv, I):
    r = I
    for c in wd: r = mul(r, {'x': Xm, 'X': inv(Xm), 'y': Ym, 'Y': inv(Ym)}[c])
    return r

# ---------- arithmetic in Z[omega]/(p) as pairs (a,b) = a + b*omega, omega^2 = -1 - omega ----------
def make_ring(p):
    def add(u, v): return ((u[0]+v[0]) % p, (u[1]+v[1]) % p)
    def mulr(u, v):
        a, b = u; c, d = v                           # (a+b w)(c+d w) = ac + (ad+bc) w + bd w^2
        return ((a*c - b*d) % p, (a*d + b*c - b*d) % p)
    def neg(u): return ((-u[0]) % p, (-u[1]) % p)
    return add, mulr, neg
def mats(p):
    add, mulr, neg = make_ring(p)
    one, zero = (1, 0), (0, 0)
    def mm(A, B): return tuple(tuple(add(mulr(A[i][0], B[0][j]), mulr(A[i][1], B[1][j])) for j in range(2)) for i in range(2))
    def mi(A):  # det 1
        return ((A[1][1], neg(A[0][1])), (neg(A[1][0]), A[0][0]))
    I = ((one, zero), (zero, one))
    return mm, mi, I, add, mulr, neg
def conj_entry(u):   # c: omega -> omegabar = -1 - omega ;  a + b w  ->  (a - b) - b w
    return (u[0] - u[1], -u[1])

# ---------- R2: prime by prime ----------
print(f"\n{'p':>3} {'type':>9} {'relation mod p':>15} {'rho vs rhobar on the test words':>34}")
verdict = True
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    typ = 'ramified' if p == 3 else ('inert' if p % 3 == 2 else 'split')
    mm, mi, I, add, mulr, neg = mats(p)
    Xp = (((1, 0), (1, 0)), ((0, 0), (1, 0)))
    Yp = (((1, 0), (0, 0)), (((0, p-1)), (1, 0)))                    # -omega = (0, -1)
    c = lambda A: tuple(tuple(tuple(v % p for v in conj_entry(A[i][j])) for j in range(2)) for i in range(2))
    Xc, Yc = c(Xp), c(Yp)
    Wp = mm(mm(mm(mi(Xp), Yp), Xp), mi(Yp))
    rel = mm(Wp, Xp) == mm(Yp, Wp)
    def tr(A): return add(A[0][0], A[1][1])
    if typ == 'split':
        # reduce mod pi: omega -> r, a root of t^2+t+1 in F_p; rhobar mod pi = rho with omega -> the other root
        roots = [r for r in range(p) if (r*r + r + 1) % p == 0]
        ev = lambda u, r: (u[0] + u[1]*r) % p
        diff = []
        for wd in WORDS:
            t = tr(mat_word(wd, Xp, Yp, mm, mi, I))
            diff.append(ev(t, roots[0]) != ev(t, roots[1]))
        res = f"non-conjugate (traces differ on {sum(diff)}/{len(WORDS)} words)" if any(diff) else "SAME traces"
        verdict &= any(diff)
    else:
        diff = []
        for wd in WORDS:
            a = tr(mat_word(wd, Xp, Yp, mm, mi, I)); b = tr(mat_word(wd, Xc, Yc, mm, mi, I))
            if typ == 'ramified':          # in F3 omega = 1: evaluate a + b
                a = (a[0] + a[1]) % 3; b = (b[0] + b[1]) % 3
            diff.append(a != b)
        if typ == 'ramified':
            res = "SAME representation (c invisible)" if not any(diff) else f"differ on {sum(diff)} words"
            verdict &= not any(diff)
        else:
            res = f"non-conjugate, Frobenius-related (differ on {sum(diff)}/{len(WORDS)})" if any(diff) else "SAME traces"
            verdict &= any(diff)
    verdict &= rel
    print(f"{p:>3} {typ:>9} {str(rel):>15} {res:>34}")
print(f"R2: {'PASS' if verdict else 'KILL'}")

# ---------- R3: the paper's Scope 7.2 ----------
A5 = [g for g in itertools.permutations(range(5)) if sum(1 for i in range(5) for j in range(i+1, 5) if g[i] > g[j]) % 2 == 0]
def pm(g, h): return tuple(g[h[i]] for i in range(5))
def pinv(g):
    r = [0]*5
    for i, gi in enumerate(g): r[gi] = i
    return tuple(r)
e = tuple(range(5))
def gsize(gs):
    S = {e}; fr = [e]
    while fr:
        x = fr.pop()
        for g in gs:
            y = pm(x, g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)
G4 = snappy.Manifold('m004').fundamental_group(); gs = list(G4.generators()); rs = list(G4.relators())
def evp(wd, val):
    r = e
    for ch in wd: r = pm(r, val[ch.lower()] if ch.islower() else pinv(val[ch.lower()]))
    return r
n = sum(1 for vals in itertools.product(A5, repeat=len(gs))
        if all(evp(r, dict(zip(gs, vals))) == e for r in rs) and gsize(vals) == 60)
print(f"\nR3(i)  surjections pi1(m004) ->> A5 (SnapPy presentation, by enumeration): {n}")
mm, mi, I, add, mulr, neg = mats(2)
Xp = (((1, 0), (1, 0)), ((0, 0), (1, 0))); Yp = (((1, 0), (0, 0)), ((0, 1), (1, 0)))
S = {I}; fr = [I]
while fr:
    a = fr.pop()
    for g in (Xp, Yp):
        b = mm(a, g)
        if b not in S: S.add(b); fr.append(b)
print(f"R3(ii) order of Riley's image mod 2 in SL(2,F4) = A5 (order 60): {len(S)}")
