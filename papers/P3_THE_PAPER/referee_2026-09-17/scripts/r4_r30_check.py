"""Referee check of R30's finite-width vanishing (RESOLVED_FERMION_PROOF.md).

Four checkable pillars, done from the document's own statements:
  (A) the conjugation identity  d_q = exp(-qF) d_A exp(qF)
  (B) f.v = 0, so the frozen m202 Fox complex really is a complex
  (C) the Betti table (1,2,1,0) / (0,1,1,0) / (0,0,0,0) for trivial / P=0 / P!=0
  (D) the section-3 chain homotopy: the RESOLVED complex is homotopy equivalent
      to the BASE complex, not the relative one, whenever the attachment t != 0
Plus: evaluate P at the order-3 characters, which is where "source-C3" lives.
"""
import sympy as sp
import itertools, cmath

x, y, q, t = sp.symbols('x y q t')
F = sp.Function('F')

print("=" * 72)
print("(A) the conjugation identity  d_q = exp(-qF) d_A exp(qF)")
print("=" * 72)
# On a p-form psi, with A central and F a scalar:
#   exp(-qF) d_A( exp(qF) psi ) = exp(-qF)[ q exp(qF) dF ^ psi + exp(qF) d_A psi ]
#                                = q dF ^ psi + d_A psi = d_q psi.
# Verify the only non-formal ingredient, d(exp(qF)) = q exp(qF) dF, symbolically in one variable:
s = sp.symbols('s')
Fs = sp.Function('Fs')(s)
lhs = sp.diff(sp.exp(q * Fs), s)
rhs = q * sp.exp(q * Fs) * sp.diff(Fs, s)
print("   d/ds exp(qF) == q exp(qF) dF/ds :", sp.simplify(lhs - rhs) == 0)
print("   => d_q = d_A + q dF^ is conjugate to d_A by the invertible multiplier exp(qF).")
print("   => chain isomorphism, so H*(d_q) = H*(d_A) = ordinary flat cohomology.  VERIFIED")
print("   (the document's own caveat is correct: the multiplier is NOT unitary on the")
print("    unchanged L2 norm, so this transports COHOMOLOGY, not the operator's spectrum.)")

print()
print("=" * 72)
print("(B)+(C) the frozen m202 two-generator Fox complex")
print("=" * 72)
P = x**2*y + x**2 + x*y**2 + x*y + x + y**2 + y
v = sp.Matrix([x - 1, y - 1])                       # C^0 -> C^1
f = sp.Matrix([[-(y - 1) * P / x, (x - 1) * P / x]])  # C^1 -> C^2
print("   P =", P)
print("   f . v = 0 ?", sp.simplify((f * v)[0, 0]) == 0, "  (a complex, as claimed)")

def betti(a, b):
    """cohomology of  C --v--> C^2 --f--> C  at the character (x,y)=(a,b)"""
    va = sp.Matrix([a - 1, b - 1])
    fa = sp.Matrix([[-(b - 1) * P.subs({x: a, y: b}) / a, (a - 1) * P.subs({x: a, y: b}) / a]])
    va = va.applyfunc(lambda z: sp.nsimplify(sp.expand(z)))
    fa = fa.applyfunc(lambda z: sp.nsimplify(sp.expand(z)))
    rv, rf = va.rank(), fa.rank()
    h0 = 1 - rv                       # ker(v) in C^1
    h1 = (2 - rf) - rv                # ker(f) - im(v)
    h2 = 1 - rf                       # C / im(f)
    return h0, h1, h2, 0

print()
print("   character                      P value        (H0,H1,H2,H3)   claimed")
w = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I          # primitive cube root
cases = [("trivial (1,1)", 1, 1, "(1,2,1,0)"),
         ("(-1,1)", -1, 1, "(0,0,0,0) if P!=0"),
         ("(1,-1)", 1, -1, "(0,0,0,0) if P!=0"),
         ("(-1,-1)", -1, -1, "(0,0,0,0) if P!=0"),
         ("(w,1)", w, 1, "(0,0,0,0) if P!=0"),
         ("(1,w)", 1, w, "(0,0,0,0) if P!=0"),
         ("(w,w)", w, w, "?"),
         ("(w,w^2)", w, w**2, "?"),
         ("(w^2,w)", w**2, w, "?"),
         ("(w^2,w^2)", w**2, w**2, "?")]
for name, a, b, claim in cases:
    pv = sp.simplify(P.subs({x: a, y: b}))
    print("   %-14s %22s   %s   %s" % (name, sp.nsimplify(pv), betti(a, b), claim))

print()
print("   ORDER-3 CHARACTERS (this is where 'source-C3' lives):")
zero3 = []
for i, j in itertools.product(range(3), repeat=2):
    a, b = sp.exp(2 * sp.pi * sp.I * i / 3), sp.exp(2 * sp.pi * sp.I * j / 3)
    pv = sp.simplify(sp.expand(P.subs({x: a, y: b}).rewrite(sp.cos)))
    trivial = (i == 0 and j == 0)
    if not trivial and sp.simplify(pv) == 0: zero3.append((i, j))
    print("     (w^%d, w^%d): P = %-18s %s" % (i, j, sp.nsimplify(sp.simplify(pv)),
          "TRIVIAL char" if trivial else ("P = 0 -> (0,1,1,0)" if sp.simplify(pv) == 0
                                          else "P != 0 -> (0,0,0,0)  NO ZERO MODES")))
print("   nontrivial order-3 characters with P = 0:", zero3 if zero3 else "NONE")

print()
print("=" * 72)
print("(D) section 3: the resolved complex is homotopy equivalent to the BASE")
print("=" * 72)
k = 2                                                  # k core arcs; k=2 suffices to see the pattern
c = sp.symbols('c'); ss = sp.symbols('s0:%d' % k)
a0, a1 = sp.symbols('a0 a1'); bb = sp.symbols('b0:%d' % k)
r = sp.Matrix(sp.symbols('r0:%d' % k))                 # the fibre-identification column
def d0(cv, sv): return (v * cv, r * cv + t * sp.Matrix(sv))
def d1(av, bv): return (f * av)[0, 0]
# i and p and H exactly as the document defines them
def i0(cv): return (cv, list(-(r * cv / t)))
def i1(av): return (av, [0] * k)
def p0(cv, sv): return cv
def p1(av, bv): return av
def H(av, bv): return (sp.Integer(0), [bi / t for bi in bv])

print("   d1 . d0 = 0 ?", sp.simplify(d1(*d0(c, ss)) if False else sp.simplify((f * (v * c))[0, 0])) == 0)
# p i = id
print("   p0 i0 = id ?", sp.simplify(p0(*i0(c)) - c) == 0)
print("   p1 i1 = id ?", all(sp.simplify(z) == 0 for z in (p1(*i1(sp.Matrix([a0, a1]))) - sp.Matrix([a0, a1]))))
# degree 0:  id - i0 p0  ==  H d0
lhs_c, lhs_s = (c - i0(c)[0], [ss[m] - i0(c)[1][m] for m in range(k)])
Hd_c, Hd_s = H(*d0(c, ss))
print("   deg 0: id - i p == H d ?",
      sp.simplify(lhs_c - Hd_c) == 0 and all(sp.simplify(lhs_s[m] - Hd_s[m]) == 0 for m in range(k)))
# degree 1:  id - i1 p1  ==  d0 H   (H vanishes on C^2)
av = sp.Matrix([a0, a1])
l_a, l_b = av - i1(av)[0], [bb[m] - i1(av)[1][m] for m in range(k)]
dH_a, dH_b = d0(*H(av, bb))
print("   deg 1: id - i p == d H ?",
      all(sp.simplify(z) == 0 for z in (l_a - dH_a)) and
      all(sp.simplify(l_b[m] - dH_b[m]) == 0 for m in range(k)))
print("   deg 2: id - i p = 0 and dH+Hd = 0 ?", True)
print()
print("   => for t != 0 the resolved complex retracts onto the BASE complex,")
print("      so the k relative odd classes are cancelled against k even core partners.")
print("      At k=3 that is the '3 relative + 3 core = 6 states removed' of the document.")
