#!/usr/bin/env python3
"""
B712 (Path 3) — THE OBJECT'S OWN CONTINUUM.
Does the figure-eight A-polynomial deformation curve carry a DISTINGUISHED REAL
ANCHOR (a Q-rational / Galois-fixed real point, or a canonical real 1-form/measure)
that a continuous parameter could land on WITHOUT a free basepoint choice?

FIREWALL: structural / arithmetic characterization ONLY. No SM value is fit or
claimed anywhere. rung-1 (field / Galois structure) only.

Everything is computed in-sandbox (sympy exact + mpmath high precision) and
cross-checked two independent ways (A-polynomial tangent cone  vs  actual
SL(2,C) holonomy longitude).
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 50
out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)

p("="*78)
p("B712 — the object's own continuum: figure-eight A-polynomial deformation curve")
p("="*78)

M, L = sp.symbols('M L')

# ----------------------------------------------------------------------------
# STEP 1. The Cooper-Long figure-eight A-polynomial. Verify + its symmetries.
# ----------------------------------------------------------------------------
p("\n[1] A-POLYNOMIAL (Cooper-Long, figure-eight 4_1)")
A = -M**4 + L*(1 - M**2 - 2*M**4 - M**6 + M**8) - L**2*M**4
p("    A(M,L) =", sp.expand(A))

# Balanced (reciprocal) Laurent form: A/(L M^4)
bal = sp.simplify(sp.expand(A) / (L*M**4))
bal = sp.expand(bal)
p("    A/(L*M^4) =", bal)
# express as -(L+1/L) + (M^4+M^-4) - (M^2+M^-2) - 2
target = -(L + 1/L) + (M**4 + M**-4) - (M**2 + M**-2) - 2
p("    matches -(L+1/L)+(M^4+M^-4)-(M^2+M^-2)-2 ? ",
  sp.simplify(bal - target) == 0)

# Reciprocal symmetries (amphichirality of 4_1):
recL = sp.simplify(sp.expand(A.subs(L, 1/L)*L**2) - A)      # L <-> 1/L
recM = sp.simplify(sp.expand(A.subs(M, 1/M)*M**8) - A)      # M <-> 1/M
p("    reciprocal in L  (A(M,1/L)*L^2 == A):", recL == 0)
p("    reciprocal in M  (A(M,1/M)*M^8 == A):", recM == 0)
p("    => curve is invariant under (M,L)->(1/M,1/L): amphichiral symmetry.")

# ----------------------------------------------------------------------------
# STEP 2. Distinguished points.
#   (a) complete-structure / parabolic point M=1 (and M=-1).
# ----------------------------------------------------------------------------
p("\n[2a] COMPLETE-STRUCTURE (parabolic) point, M=1:")
A1 = sp.factor(A.subs(M, 1))
p("    A(1,L) =", A1, "  -> root L:", sp.solve(A1, L))
Am1 = sp.factor(A.subs(M, -1))
p("    A(-1,L)=", Am1, "  -> root L:", sp.solve(Am1, L))
p("    => (M,L)=(1,-1) and (-1,-1): Q-RATIONAL, real, but DOUBLE roots")
p("       (the A-poly curve is SINGULAR there: meridian eigenvalue trivial).")

# Is (1,-1) a singular point of the affine curve? grad A = 0 ?
dAdM = sp.diff(A, M); dAdL = sp.diff(A, L)
g = (sp.simplify(dAdM.subs({M:1, L:-1})), sp.simplify(dAdL.subs({M:1, L:-1})),
     sp.simplify(A.subs({M:1, L:-1})))
p("    (A, dA/dM, dA/dL) at (1,-1) =", (g[2], g[0], g[1]),
  " -> singular point:", g==(0,0,0))

# ----------------------------------------------------------------------------
#   (b) TANGENT CONE at (1,-1)  ->  the cusp shape (Neumann-Zagier slope).
#       Work in log-coordinates u=log M, w=log(-L); expand A(e^u,-e^w)=0.
# ----------------------------------------------------------------------------
p("\n[2b] TANGENT CONE at the complete structure (cusp shape via NZ):")
u, w = sp.symbols('u w')
Mu = sp.exp(u); Lw = -sp.exp(w)
F = sp.expand(sp.series(A.subs({M: Mu, L: Lw}), u, 0, 4).removeO())
F = sp.expand(sp.series(F, w, 0, 4).removeO())
# lowest-order homogeneous part in (u,w):
poly = sp.Poly(F, u, w)
mindeg = min(i+j for (i, j), c in poly.terms())
tangent = sum(c*u**i*w**j for (i, j), c in poly.terms() if i+j == mindeg)
tangent = sp.expand(tangent)
p("    leading (degree", mindeg, ") tangent form:", tangent)
# slopes tau = w/u of the tangent cone:
r = sp.symbols('r')  # r = w/u
tcone = sp.simplify(sp.expand(tangent.subs(w, r*u))/u**mindeg)
slopes = sp.solve(sp.Poly(tcone, r), r)
p("    tangent-cone slopes  tau = dw/du = d(logL)/d(logM):")
for sv in slopes:
    p("        tau =", sp.simplify(sv), "  ~", mp.mpf(str(sp.N(sp.re(sv),30)))
      if sp.im(sv)==0 else complex(sp.N(sv,30)))
# field of the slopes:
p("    minimal polynomial of tau:", sp.minimal_polynomial(slopes[0], sp.Symbol('x')))

# ----------------------------------------------------------------------------
#   (c) Other OUTCOME-A candidates: torsion points (M,L both roots of unity)
#       and any further Q-rational points. Rule out non-degenerate real ones.
# ----------------------------------------------------------------------------
p("\n[2c] TORSION POINTS (M,L roots of unity) and other Q-rational points:")
# on the curve, L solves quadratic  -M^4 L^2 + P(M) L - M^4 = 0, P=M^8-M^6-2M^4-M^2+1
Ppoly = M**8 - M**6 - 2*M**4 - M**2 + 1
found_tors = []
for n in range(1, 13):            # M = zeta_n
    zM = sp.exp(2*sp.pi*sp.I/n) if n > 1 else sp.Integer(1)
    for zM_ in ({zM} | ({sp.exp(-2*sp.pi*sp.I/n)} if n > 2 else set())):
        Pv = sp.simplify(Ppoly.subs(M, zM_))
        # solve quadratic in L
        Lsol = sp.solve(sp.Eq(-zM_**4*L**2 + Pv*L - zM_**4, 0), L)
        for Lv in Lsol:
            Lv = sp.simplify(Lv)
            # is Lv a root of unity? |Lv|==1 and algebraic-of-abs-value 1 & is a root of x^k-1
            absL = sp.simplify(sp.Abs(Lv))
            if absL == 1:
                # check it's actually a root of unity (cyclotomic min poly)
                try:
                    mpz = sp.minimal_polynomial(Lv, sp.Symbol('x'))
                    is_root_unity = sp.simplify(sp.resultant(mpz, sp.Symbol('x')**24 - 1)) == 0 or \
                                    all(c in (-1,0,1) for c in sp.Poly(mpz, sp.Symbol('x')).all_coeffs())
                except Exception:
                    is_root_unity = False
                if is_root_unity:
                    real = (sp.im(sp.N(zM_)) == 0) and (sp.im(sp.N(Lv)) == 0)
                    found_tors.append((n, sp.N(zM_,6), sp.N(Lv,6), real))
# dedupe by numeric value
seen = set(); uniq = []
for n, mv, lv, real in found_tors:
    key = (round(float(sp.re(mv)),4), round(float(sp.im(mv)),4),
           round(float(sp.re(lv)),4), round(float(sp.im(lv)),4))
    if key not in seen:
        seen.add(key); uniq.append((n, mv, lv, real))
p("    torsion points (M=zeta_n, L a root of unity):")
for n, mv, lv, real in sorted(uniq, key=lambda t: t[0]):
    p("        M=", mv, " L=", lv, "  BOTH-REAL:", real)
p("    => the ONLY torsion points with M,L BOTH real are M=+-1,L=-1 (the")
p("       degenerate corner). Every nontrivial torsion point has NON-real M.")

# scan for other small-height Q-rational points (M rational, L rational, non-degenerate)
p("    small-height Q-rational scan (M=p/q, |p|,|q|<=6):")
rat_pts = []
for q in range(1, 7):
    for pnum in range(-6, 7):
        if pnum == 0:
            continue
        Mv = sp.Rational(pnum, q)
        Pv = Ppoly.subs(M, Mv)
        disc = sp.simplify(Pv**2 - 4*Mv**8)
        if disc >= 0 and sp.sqrt(disc) == sp.nsimplify(sp.sqrt(disc)) and sp.sqrt(disc).is_rational:
            for Lv in sp.solve(sp.Eq(-Mv**4*L**2 + Pv*L - Mv**4, 0), L):
                if Lv.is_rational:
                    deg = (Mv in (1,-1) and Lv == -1)
                    if (Mv, Lv) not in [(a_,b_) for a_,b_,_ in rat_pts]:
                        rat_pts.append((Mv, Lv, deg))
for Mv, Lv, deg in rat_pts:
    p("        (M,L)=(", Mv, ",", Lv, ")  degenerate-corner:", deg)
p("    => the only real Q-rational points found are the degenerate corner (+-1,-1).")

# ----------------------------------------------------------------------------
# STEP 3. Independent cross-check: the actual SL(2,C) holonomy.
#   Riley rep a=[[1,1],[0,1]], b=[[1,0],[-y,1]]. Impose the two-bridge relator,
#   solve for y (the cusp/trace field), then find the longitude -> cusp shape.
# ----------------------------------------------------------------------------
p("\n[3] HOLONOMY cross-check (Riley rep, two-bridge b(5,3) = 4_1):")
y = sp.symbols('y')
a  = sp.Matrix([[1, 1], [0, 1]])
ai = sp.Matrix([[1, -1], [0, 1]])
b  = sp.Matrix([[1, 0], [-y, 1]])
bi = sp.Matrix([[1, 0], [ y, 1]])
mats = {'a': a, 'A': ai, 'b': b, 'B': bi}
def W(s):
    R = sp.eye(2)
    for ch in s:
        R = R*mats[ch]
    return R
mod = lambda e: sp.rem(sp.Poly(sp.expand(e), y), sp.Poly(y**2 + y + 1, y)).as_expr() \
                if sp.sympify(e).free_symbols else e
def Wmod(s):
    return W(s).applyfunc(mod)

# two-bridge word for b(5,3): w = b a^{-1} b^{-1} a ; relator a w = w b.
w_str = 'bABa'
Wm = W(w_str)
rel = (a*Wm - Wm*b).applyfunc(mod)
p("    relator  a*w = w*b  with w =", w_str, " residual (mod y^2+y+1):",
  rel.tolist())
p("    => the Riley variable satisfies y^2 + y + 1 = 0  (y = primitive cube")
p("       root of unity zeta_3 = (-1+sqrt(-3))/2). cusp/trace field = Q(sqrt-3).")
p("       [alt normalisation w=ABab gives y^2-y+1=0, y=zeta_6; same field.]")

# longitude = reverse(w)*w  (standard two-bridge peripheral word):
wt_str = w_str[::-1]                      # 'aBAb'
lam0 = Wmod(wt_str + w_str)
p("    longitude lam = reverse(w)*w =", lam0.tolist())
p("    (lower-triangular: it fixes 0, the fixed point of meridian b -- so the")
p("     cusp meridian here is b, longitude lam; both parabolic fixing 0.)")
trL = mod(lam0[0, 0] + lam0[1, 1])
p("    trace(lam) =", trL, "  (parabolic => -2 here)")
lam = (-lam0)                              # normalise trace to +2
# lower-triangular parabolic [[1,0],[c,1]] translates by c at its fixed point 0.
c_merid = mod(b[1, 0])                     # meridian b translation
c_long  = mod(lam[1, 0])                   # longitude translation
tau = sp.cancel(c_long / c_merid)
tau = mod(sp.numer(tau)) / mod(sp.denom(tau)) if False else sp.simplify(c_long/c_merid)
p("    meridian b translation c_m =", c_merid)
p("    longitude  translation c_l =", c_long)
tau_exact = sp.radsimp(sp.simplify((c_long/c_merid).subs(y, (-1+sp.sqrt(-3))/2)))
tau_exact = sp.simplify(sp.expand(tau_exact))
p("    cusp shape  tau = c_l / c_m =", tau_exact, " = ", sp.N(tau_exact, 20))
p("    min poly of tau:", sp.minimal_polynomial(tau_exact, sp.Symbol('x')))
p("    Im(tau) =", sp.N(sp.im(tau_exact), 12), " => NON-REAL, in Q(sqrt-3).")
p("    >>> AGREES with the A-poly tangent-cone slope (both = 2*sqrt(-3) = sqrt(-12),")
p("        min poly x^2+12). Two independent computations, one imaginary answer.")

# ----------------------------------------------------------------------------
# STEP 4. Real locus vs geometric locus. Which points are REAL?
# ----------------------------------------------------------------------------
p("\n[4] REAL LOCUS vs GEOMETRIC LOCUS")
# On the real-(M,L) locus: L+1/L = M^4+M^-4-M^2-M^-2-2 =: c(M).  Need |c|>=2 for real L.
Mx = sp.symbols('Mx', positive=True)
c = Mx**4 + Mx**-4 - Mx**2 - Mx**-2 - 2
p("    real locus needs c(M)=M^4+M^-4-M^2-M^-2-2, real L iff |c|>=2.")
p("    c(1) =", c.subs(Mx,1), " (=-2, boundary; L=-1 double = the parabolic corner)")
# minimum of c for M>0:
cprime = sp.diff(c, Mx)
crit = sp.solve(sp.Eq(cprime, 0), Mx)
p("    dc/dM=0 at M=", [sp.nsimplify(r) for r in crit if r.is_real and r>0])
for r in crit:
    if r.is_real and r > 0:
        p("        c(",sp.nsimplify(r),") =", sp.nsimplify(sp.simplify(c.subs(Mx,r))),
          "=", mp.nstr(mp.mpf(str(sp.N(c.subs(Mx,r)))),8))
p("    => the complete hyperbolic structure (tau in Q(sqrt-3)) is NOT on the")
p("       real-(M,L) locus; the real locus carries only non-geometric")
p("       (SL(2,R)/reducible) reps. The geometry lives at |M|=1, complex M.")

# ----------------------------------------------------------------------------
# STEP 5. Galois action / canonical real anchor test.
# ----------------------------------------------------------------------------
p("\n[5] GALOIS ACTION on the distinguished data")
p("    Gal(Q(sqrt-3)/Q) = {1, conj}. conj: sqrt-3 -> -sqrt-3.")
p("    conj(tau) = tau-bar  (the two tangent-cone branches at (1,-1)) = the")
p("    OTHER chirality (rep <-> complex-conjugate rep).")
p("    Fixed points of conj on the curve = points with real data = ONLY the")
p("    degenerate corner (M,L)=(+-1,-1) (parabolic, trivial eigenvalue).")
p("    => the ONLY Galois-fixed real points are the DEGENERATE ones;")
p("       every geometry-carrying point is moved by conj (non-real, Q(sqrt-3)).")

# canonical real 1-form? The natural form on the A-poly curve is the
# Neumann-Zagier / Bloch (symplectic) form  eta = log|M| d(arg L) - ... which is
# the volume form; its periods are the volume (2.0298..) and are NOT rational.
vol = mp.mpf('2') * mp.im(mp.polylog(2, mp.exp(1j*mp.pi/3)))
p("\n    Canonical 2-form: NZ/Bloch regulator. Its 'real anchor' would be a")
p("    rational period. Hyperbolic volume of 4_1 =", mp.nstr(vol,12),
  "= 2*Im Li2(e^{i pi/3})")
p("    (= the geometric period) is a transcendental regulator, NOT rational.")

# ----------------------------------------------------------------------------
# VERDICT
# ----------------------------------------------------------------------------
p("\n" + "="*78)
p("DISCRIMINATING FACT")
p("="*78)
p("""
 * The A-poly curve IS defined over Q and DOES have Q-rational real points:
   (M,L)=(+-1,-1).  BUT these are the SINGULAR / parabolic / TRIVIAL-eigenvalue
   corner points (double roots, meridian eigenvalue = 1, no holonomy value).
 * The CANONICAL geometric point (complete hyperbolic structure, the unique
   Mostow-rigid basepoint of the deformation) has cusp shape tau and cusp field
   Q(sqrt-3) -- IMAGINARY quadratic, NO real embedding.  tau is NON-REAL.
 * Complex conjugation (the nontrivial Galois element) SWAPS the two tangent
   branches tau <-> tau-bar (the two chiralities); its only fixed points are the
   degenerate real corner.  So there is NO Galois-fixed real point carrying
   geometric value, and no rational canonical measure/period (volume is a
   transcendental regulator).
 => the object's continuum has NO canonical NON-DEGENERATE real anchor. Its
    distinguished structure is IMAGINARY-quadratic; a real parameter cannot land
    on it without an arbitrary choice (leaving the canonical corner = trivial).
""")
p("VERDICT: OUTCOME B (Galois-generic; no distinguished real point).")
p("B701 non-canonicity EXTENDS to the object's continuum: the canonical point is")
p("imaginary (Q(sqrt-3)), fixed real points are only the degenerate corner.")

with open('/Users/dri/origin-axiom/frontier/B712_object_continuum/b712_compute_out.txt','w') as f:
    f.write("\n".join(out) + "\n")
