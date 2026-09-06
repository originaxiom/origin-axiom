"""R62 -- the full symmetry group on the cusp torus, exactly. iota's translation vector; the mirror's action; slopes fixed."""
import itertools
from fractions import Fraction as Fr
exec(open('r61_fast.py').read().split("# ---- (a) sigma on the fiber")[0] if "# ---- (a)" in open('r61_fast.py').read() else open('r61_fast.py').read().split("A, B, T = ev('xY')")[0])
# --- cusp lattice (from R61): tau = 2 + 4w, Lambda = Z + Z tau, cusp at infinity, meridian x = translation by 1
tau = (2, 4)
def coords(z):
    p, q = z; v = Fr(q, 1) / tau[1]; u = Fr(p, 1) - v*tau[0]; return (u % 1, v % 1)
def conjZ(a): p, q = a; return (p - q, -q)        # omega -> omega^2 = -1 - omega
def mob(M, z):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if z == 'oo': return 'oo' if c == ZERO else frac_div(a, c)
    def fm(u, v): return (u[0]*v[0] - u[1]*v[1], u[0]*v[1] + u[1]*v[0] - u[1]*v[1])
    def fa(u, v): return (u[0]+v[0], u[1]+v[1])
    num = fa(fm((Fr(a[0]),Fr(a[1])), z), (Fr(b[0]),Fr(b[1]))); den = fa(fm((Fr(c[0]),Fr(c[1])), z), (Fr(d[0]),Fr(d[1])))
    if den == (0, 0): return 'oo'
    r, s_ = den; cj = (r - s_, -s_); n = fm(num, cj); dd = fm(den, cj); assert dd[1] == 0
    return (n[0]/dd[0], n[1]/dd[0])
def gamma_to_inf(pt, maxlen=10):
    for wd in words('xyXY', maxlen, 0):
        M = ev(wd)
        if mob(M, pt) == 'oo': return wd, M
    return None
# ---------- iota: conjugator from R60 (exact): G_iota = [[-1, -w], [-1, 1]] (det = -1 - w^2 ... recomputed below)
Gi = [[zneg(ONE), zneg(W)], [zneg(ONE), ONE]]
# check it realizes iota: rho(iota(u)) = Gi^-1 rho(u) Gi  for the fiber involution x->xyX, y->xYxyX
io = {'x': 'xyX', 'y': 'xYxyX'}
def iw(word): return ''.join(io[c] if c.islower() else invw(io[c.lower()]) for c in word)
for u in 'xy':
    assert mm(Gi, ev(iw(u))) == mm(D[u], Gi), u
print("[iota] conjugator G_iota realizes x->xyX, y->xYxyX:", True, " det =", det(Gi))
p = mob(Gi, 'oo'); print("       G_iota(oo) =", p)
wd, g = gamma_to_inf(p); h = mm(g, Gi)          # h fixes infinity
print(f"       gamma = rho('{wd}') sends it to oo; h = gamma.G_iota = {h}  (c entry must be 0: {h[1][0] == ZERO})")
# h acts on C as z -> (a z + b)/d ; alpha = a/d, beta = b/d
alpha = frac_div(h[0][0], h[1][1]); beta = frac_div(h[0][1], h[1][1])
print(f"       on the cusp torus: z -> alpha z + beta with alpha = {alpha}, beta = {beta} -> coordinates (u,v) of beta: {coords(beta)}")
print("       => iota acts on the cusp torus as the TRANSLATION by", coords(beta), " (a 2-torsion point: u,v in {0,1/2})")
v_iota = coords(beta)
# the other strong inversion sigma' = sigma o iota: z -> -(z + beta) = -z - beta: fixed points 2z = -beta mod Lambda
print("       fixed points of sigma' = sigma o iota on the cusp torus: the four points z with 2z = -beta, i.e. -beta/2 + E[2] =",
      sorted({((-v_iota[0]/2 + Fr(i,2)) % 1, (-v_iota[1]/2 + Fr(j,2)) % 1) for i in range(2) for j in range(2)}))
# ---------- the mirror: an automorphism m with rho(m(u)) = Dm . conj(rho(u)) . Dm^-1  (antiholomorphic)
def conjM(M): return [[conjZ(M[i][j]) for j in range(2)] for i in range(2)]
found = None
for L1 in range(1, 6):
    for w1 in words('xyXY', L1, L1):
        M1 = ev(w1)
        if za(M1[0][0], M1[1][1]) != za(conjM(x)[0][0], conjM(x)[1][1]): continue   # trace must match (trace 2 for x-image)
        for L2 in range(1, 7):
            for w2 in words('xyXY', L2, L2):
                if w2 == w1: continue
                M2_ = ev(w2)
                if za(M2_[0][0], M2_[1][1]) != (2, 0): continue
                # solve E conj(rho(u)) = rho(m u) E  for E (4 unknowns over Q(omega)) -> use the same nullspace approach mod a prime-free exact method:
                # brute: E ranges over small integer matrices? Instead check the relator first
                mp = {'x': w1, 'y': w2}
                def mw(word): return ''.join(mp[c] if c.islower() else invw(mp[c.lower()]) for c in word)
                if ev(mw(REL)) != I2 and ev(mw(REL)) != [[zneg(ONE), ZERO],[ZERO, zneg(ONE)]]: continue
                # check that the pair is conjugate to the conjugated pair: compare traces of x, y, xy, xY under both
                tr = lambda M: za(M[0][0], M[1][1])
                ok = all(tr(ev(mw(t))) == tr(conjM(ev(t))) for t in ('x', 'y', 'xy', 'xY', 'xxy', 'xyy'))
                if ok:
                    found = (w1, w2); break
            if found: break
        if found: break
    if found: break
print("[mirror] an automorphism x->", found[0] if found else None, " y->", found[1] if found else None,
      " whose image pair has the traces of the Galois-conjugate representation (candidate amphichiral map)")
if found:
    mp = {'x': found[0], 'y': found[1]}
    def mw(word): return ''.join(mp[c] if c.islower() else invw(mp[c.lower()]) for c in word)
    # action on H1(M) = Z (meridian class = x): exponent sum of the image of x
    es = lambda wd: sum(1 if c in 'xy' else -1 for c in wd)
    print(f"        meridian class: x -> {found[0]} has exponent sum {es(found[0])}  (mirror reverses the meridian iff -1)")
    # longitude image: the fiber boundary [a,b]; its image under m as a word; compare with lambda^{+-1} up to conjugacy via trace of lambda*x-powers is insufficient;
    # instead compute the induced map on the cusp: find E with E conj(rho(u)) E^-1 = rho(m u), then E conj acts on the horosphere at oo if it fixes oo
    # solve linear system for E over Q(omega) by brute force on the 4x... use fractions: unknown E = [[e0,e1],[e2,e3]]; equations E*conj(rho u) - rho(mu)*E = 0
    import sympy as sp
    w_ = sp.Rational(-1,2) + sp.sqrt(3)*sp.I/2
    def tosp(M): return sp.Matrix([[M[i][j][0] + M[i][j][1]*w_ for j in range(2)] for i in range(2)])
    e = sp.symbols('e0:4'); E = sp.Matrix([[e[0], e[1]], [e[2], e[3]]])
    eqs = []
    for u in 'xy': eqs += list(sp.expand(E*tosp(conjM(D[u])) - tosp(ev(mw(u)))*E))
    sol = sp.solve(eqs, e, dict=True); Es = sp.simplify(E.subs(sol[0])); fr = [s_ for s_ in e if s_ not in sol[0]]
    Es = sp.simplify(Es.subs({fr[0]: 1}))
    print("        conjugator E =", Es.tolist(), " det =", sp.simplify(Es.det()))
    # the antiholomorphic map z -> E(conj z): does it fix oo?  E = [[a,b],[c,d]]: maps oo to a/c
    a_, b_, c_, d_ = Es
    if c_ == 0:
        print(f"        it fixes oo: z -> ({a_}/{d_}) conj(z) + ({b_}/{d_});  on the cusp torus H1: meridian 1 -> {sp.simplify(a_/d_)}, tau -> {sp.simplify(a_/d_ * sp.conjugate(2*sp.sqrt(3)*sp.I))} = {sp.simplify(-(a_/d_))} tau")
    else:
        print("        E does not fix oo; compose with gamma:", gamma_to_inf(frac_div((int(sp.re(a_)),0),(1,0)) if False else None))
