"""R61 -- exact over Z[omega] (omega^2 = -1 - omega), pure integers. theta = sigma: x->x^-1, y->y^-1."""
import itertools
from fractions import Fraction as Fr
def frac_div(num, den):
    r, s = den; conj = (r - s, -s); n = zm(num, conj); dd = zm(den, conj); assert dd[1] == 0
    return (Fr(n[0], dd[0]), Fr(n[1], dd[0]))
def zm(a, b): (p,q),(r,s) = a,b; return (p*r - q*s, p*s + q*r - q*s)
def za(a, b): return (a[0]+b[0], a[1]+b[1])
def zneg(a): return (-a[0], -a[1])
ONE, ZERO, W = (1,0), (0,0), (0,1)
def mm(A, B): return [[za(zm(A[i][0],B[0][j]), zm(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def det(A): return za(zm(A[0][0],A[1][1]), zneg(zm(A[0][1],A[1][0])))
def inv(A):
    assert det(A) == ONE, det(A)
    return [[A[1][1], zneg(A[0][1])], [zneg(A[1][0]), A[0][0]]]
x = [[ONE, ONE],[ZERO, ONE]]; y = [[ONE, ZERO],[zneg(W), ONE]]
D = {'x': x, 'y': y, 'X': inv(x), 'Y': inv(y)}
I2 = [[ONE, ZERO],[ZERO, ONE]]
def ev(word, DD=D):
    M = I2
    for ch in word: M = mm(M, DD[ch])
    return M
def invw(s): return ''.join(c.swapcase() for c in reversed(s))
def reduced(wd): return all(wd[i] != wd[i+1].swapcase() for i in range(len(wd)-1))
def words(alph, maxlen, minlen=1):
    for L in range(minlen, maxlen+1):
        for p in itertools.product(alph, repeat=L):
            wd = ''.join(p)
            if reduced(wd): yield wd
REL = 'xyXYxYXyxY'; assert ev(REL) == I2
A, B, T = ev('xY'), ev('yxYXyX'), x
assert mm(mm(T, A), inv(T)) == mm(mm(A, B), A) and mm(mm(T, B), inv(T)) == mm(A, B)
sig = {'x': 'X', 'y': 'Y'}
def sw(word): return ''.join(sig[c] if c.islower() else invw(sig[c.lower()]) for c in word)
Fd = {'a': A, 'b': B, 'A': inv(A), 'B': inv(B)}
def h1(wd): return (sum(1 if c=='a' else -1 if c=='A' else 0 for c in wd), sum(1 if c=='b' else -1 if c=='B' else 0 for c in wd))
found = {}
for name, tgt in (('sigma(a)', ev(sw('xY'))), ('sigma(b)', ev(sw('yxYXyX')))):
    for k in range(-3, 4):
        Tk = ev('x'*k) if k >= 0 else ev('X'*(-k))
        Mk = mm(mm(Tk, tgt), inv(Tk))
        hit = next((wd for wd in words('abAB', 9) if ev(wd, Fd) == Mk), None)
        if hit: found[name] = (k, hit); break
print("[a] sigma restricted to the fiber (up to the base shift t^k):", found)
if len(found) == 2:
    va, vb = h1(found['sigma(a)'][1]), h1(found['sigma(b)'][1])
    Ms = [[va[0], vb[0]], [va[1], vb[1]]]
    d = Ms[0][0]*Ms[1][1] - Ms[0][1]*Ms[1][0]
    def m2(P, Q): return [[sum(P[i][k]*Q[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    M2 = [[2,1],[1,1]]; Msinv = [[Ms[1][1]*d, -Ms[0][1]*d], [-Ms[1][0]*d, Ms[0][0]*d]]
    conj = m2(m2(Ms, M2), Msinv)
    print(f"    sigma on H1(F) = {Ms}, det = {d};  sigma M^2 sigma^-1 = {conj}; M^-2 = [[1,-1],[-1,2]] -> {conj == [[1,-1],[-1,2]]}")
# longitude = fiber boundary [a,b], conjugated into the stabilizer of infinity
lam_word = 'xY' + 'yxYXyX' + 'yX' + 'xYxyXY'          # a b a^-1 b^-1
lam = ev(lam_word)
def upper_unip(M): return M[1][0] == ZERO and M[0][0] == ONE and M[1][1] == ONE
tr = za(lam[0][0], lam[1][1]); print("[b] trace of rho([a,b]) =", tr, "(parabolic iff +-2)")
assert tr in ((2,0), (-2,0))
a_, b_, c_, d_ = lam[0][0], lam[0][1], lam[1][0], lam[1][1]
# fixed point p = (a - d)/(2c)   (disc = 0)
p_fix = frac_div(za(a_, zneg(d_)), zm((2,0), c_)) if c_ != ZERO else 'oo'
print("    fixed point of the longitude:", p_fix)
def frac_div(num, den):
    r, s = den; conj = (r - s, -s); n = zm(num, conj); dd = zm(den, conj); assert dd[1] == 0
    return (Fr(n[0], dd[0]), Fr(n[1], dd[0]))
p_fix = frac_div(za(a_, zneg(d_)), zm((2,0), c_)) if c_ != ZERO else 'oo'
gamma_word = None
if p_fix != 'oo':
    for wd in words('xyXY', 10, 0):
        M = ev(wd); r, s_ = M[1][0], M[1][1]
        val = (Fr(r[0])*p_fix[0] - Fr(r[1])*p_fix[1] + Fr(s_[0]), Fr(r[0])*p_fix[1] + Fr(r[1])*p_fix[0] - Fr(r[1])*p_fix[1] + Fr(s_[1]))
        if val == (0, 0): gamma_word = wd; break
    assert gamma_word is not None, "no gamma with gamma(p) = oo up to length 10"
    g = ev(gamma_word); lamC = mm(mm(g, lam), inv(g))
else:
    gamma_word, lamC = '', lam
assert lamC[1][0] == ZERO
if lamC[0][0] != ONE: lamC = [[zneg(v) for v in row] for row in lamC]   # -I ambiguity in PSL
tau = lamC[0][1]
assert mm(x, lamC) == mm(lamC, x)
print(f"    conjugated by rho('{gamma_word or '1'}'): translation by tau = {tau[0]} + {tau[1]} w  = {tau[0] - tau[1]/2} + {tau[1]*3**0.5/2:.6f} i"
      f"  (SnapPy cusp shape 2 sqrt3 i = {2*3**0.5:.6f} i)")
def coords(z):
    p, q = z; v = Fr(q, 1) / tau[1]; u = Fr(p, 1) - v*tau[0]; return (u % 1, v % 1)
Gs = [[zneg(ONE), ZERO],[ZERO, ONE]]
def frac_div(num, den):
    r, s = den; conj = (r - s, -s); n = zm(num, conj); dd = zm(den, conj); assert dd[1] == 0
    return (Fr(n[0], dd[0]), Fr(n[1], dd[0]))
def mob_inf(M):
    a, c = M[0][0], M[1][0]; return None if c == ZERO else frac_div(a, c)
def mob(M, z):   # z in Q(omega) as Fractions, or 'oo'
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if z == 'oo': return 'oo' if c == ZERO else frac_div(a, c)
    def fr_mul(u, v): return (u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0] - u[1]*v[1])
    def fr_add(u, v): return (u[0]+v[0], u[1]+v[1])
    zf = z; num = fr_add(fr_mul((Fr(a[0]),Fr(a[1])), zf), (Fr(b[0]),Fr(b[1]))); den = fr_add(fr_mul((Fr(c[0]),Fr(c[1])), zf), (Fr(d[0]),Fr(d[1])))
    if den == (0, 0): return 'oo'
    r, s_ = den; conj = (r - s_, -s_); n = fr_mul(num, conj); dd = fr_mul(den, conj); assert dd[1] == 0
    return (n[0]/dd[0], n[1]/dd[0])
def to_inf_point(e, other):
    for wd in words('xyXY', 10, 0):
        M = ev(wd)
        if mob(M, e) == 'oo':
            g = mob(M, other); return coords(g)
    return None
pairs = {}
for wd in words('xyXY', 6, 0):
    H = mm(ev(wd), Gs)
    if za(H[0][0], H[1][1]) != ZERO: continue
    a, b, c, d = H[0][0], H[0][1], H[1][0], H[1][1]
    if c == ZERO: eps = ['oo', frac_div(b, za(d, zneg(a)))]
    else: eps = [frac_div(za(za(a, zneg(d)), (2,0)), zm((2,0), c)), frac_div(za(za(a, zneg(d)), (-2,0)), zm((2,0), c))]
    pts = [coords(eps[1-i]) if e == 'oo' else to_inf_point(e, eps[1-i]) for i, e in enumerate(eps)]
    if any(p is None for p in pts): continue
    key = tuple(sorted(pts))
    if key not in pairs: pairs[key] = wd
    if len(pairs) >= 6: break
print("[c] arcs of Fix(sigma): endpoint pairs on the cusp torus C/Lambda, coordinates (u, v) meaning u + v*tau:")
for k, wd in pairs.items(): print(f"    {k}   (from the involution rho('{wd or '1'}') . sigma)")
print("    2-torsion points: (0,0), (1/2,0), (0,1/2), (1/2,1/2).")
