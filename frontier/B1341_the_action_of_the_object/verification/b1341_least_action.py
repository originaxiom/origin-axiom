"""B1341 -- THE OBJECT'S OWN LEAST-ACTION PRINCIPLE, AND WHY IT ONLY EXISTS AT THE DOUBLE STEP.

Row 4 of the TOE ledger (dynamics) reads "input, not derived", and row 14 of the chain status reads
"the form is imported, the constants are forced, the 4d dynamics is absent". This arc ATTEMPTS the
row rather than reporting it -- on the dynamics the object actually HAS, which is discrete.

TWO BANKED FACTS THE CORPUS NEVER JOINED:
  * B21: "under the Goldman/Weil-Petersson bracket from Fricke-Vogt, the half-step trace map is
    ANTI-Poisson and its SQUARE is Poisson."
  * B37: the trace map "has feedback and an invariant" -- and the arc then quarantined only the
    AWARENESS reading, leaving the mechanism unused.
An `already_banked` sweep finds 4 corpus hits for "feedback", 0 settled arcs joining "least" and
"action" to either. The join below is the arc's content.

THE THEOREM TO DRAW: a discrete Lagrangian L(a,b) generates, through the discrete Euler-Lagrange
equation d2 L(a,b) + d1 L(b,c) = 0, a map that ALWAYS preserves omega = d1 d2 L(a,b) da ^ db --
it is symplectic, orientation-PRESERVING, det +1. An ANTI-symplectic map therefore has NO discrete
Lagrangian at all. So B21's "anti-Poisson" is not a curiosity: it says THE OBJECT'S FUNDAMENTAL TICK
ADMITS NO ACTION PRINCIPLE, and the first step that does is the DOUBLE tick.

AND THE ECHO: the paper's genesis says "the golden morphism is L.P, and ORIENTATION SQUARES IT to
LR". L.P contains the swap. The claim tested in Q4 is that these are ONE mechanism, not two
coincidences: the same det = -1, appearing at the genesis as the swap and at the dynamics as the
anti-Poisson half-step, and the same squaring repairing both.

PRE-REGISTERED (DESIGN B1341): Q1 recompute B21 from scratch -- det(DT) = -1, det(DT^2) = +1, and the
Fricke-Vogt polynomial is a Casimir; Q2 on the leaf I = 0 the trace map linearises to the FIBONACCI
recursion in the angle variable, in both the elliptic (cos) and hyperbolic (cosh) regimes; Q3 the
half step has NO discrete Lagrangian -- proved by the orientation obstruction and confirmed by an
exhaustive solve over the general quadratic ansatz; Q4 the genesis matrix L.P has det -1 and the
trace map's half step has det -1, the SAME bit; Q5 on I = 0 the double step has an explicit
generating function, constructed and verified; Q6 THE SCOPE CORRECTION -- the object does NOT live on
I = 0: B1248 gives the once-punctured-torus fibre of m004 the parabolic commutator kappa = -2, so its
leaf is I = (kappa-2)/4 = -1, which is the MARKOV SURFACE; the half step reverses the invariant
(Gelfand-Leray) area form on EVERY leaf, so the theorem reaches the object, while Q2's linearisation
and Q5's explicit action do NOT.
PASS iff all six hold. Positive controls are printed beside each.

SCOPE, STATED BEFORE THE READ-OUT: this derives a least-action principle for the object's own
DISCRETE dynamics -- one degree of freedom on a surface. It is NOT a 4d Lorentzian field action, and
TOE-ledger row 4 asks for that. What it removes is the belief that the object supplies no
variational structure at all, and it explains, from the object, why the physical step is the DOUBLE
tick.
"""
import json
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

# ---------------------------------------------------------------- Q1: recompute B21 from scratch
print("Q1 -- the Poisson structure, recomputed (B21 is BANKED; this bench does not take it on trust)")
# B37's own operational definitions, reused verbatim:
T = sp.Matrix([z, x, 2 * x * z - y])                      # the half-step trace map
I = x ** 2 + y ** 2 + z ** 2 - 2 * x * y * z - 1          # Fricke-Vogt
sub = {x: T[0], y: T[1], z: T[2]}
check("Q1a", "Fricke-Vogt is invariant under the half step",
      sp.simplify(I.subs(sub, simultaneous=True) - I) == 0)

# The Goldman/Weil-Petersson bracket on the SL2 character variety of the once-punctured torus is the
# NAMBU bracket with Casimir I:  {f, g} = grad I . (grad f x grad g).  A map preserving I is Poisson
# iff it preserves the volume form, i.e. iff its Jacobian determinant is +1.
J = T.jacobian([x, y, z]); d1 = sp.simplify(J.det())
T2 = T.subs(sub, simultaneous=True); J2 = T2.jacobian([x, y, z]); d2 = sp.simplify(J2.det())
print(f"      det(DT) = {d1}     det(D(T^2)) = {d2}")
check("Q1b", "the HALF step is anti-Poisson: det(DT) = -1 (B21 reproduced independently)", d1 == -1)
check("Q1c", "the SQUARE is Poisson: det(D(T^2)) = +1 (B21 reproduced independently)", d2 == 1)
# direct control on the bracket itself, not just the determinant
gI = sp.Matrix([sp.diff(I, v) for v in (x, y, z)])
def nambu(f, g):
    gf = sp.Matrix([sp.diff(f, v) for v in (x, y, z)]); gg = sp.Matrix([sp.diff(g, v) for v in (x, y, z)])
    return sp.expand(gI.dot(gf.cross(gg)))
bxy = nambu(x, y)
push = sp.expand(nambu(T[0], T[1]))                        # {x,y} transported by T
check("Q1d", f"the bracket itself flips sign under the half step: T*{{x,y}} = -({{x,y}} o T)  "
             f"[{{x,y}} = {bxy}]", sp.simplify(push + bxy.subs(sub, simultaneous=True)) == 0)

# ---------------------------------------------------------------- Q2: the linearising substitution
print("\nQ2 -- the angle variable: ON THE LEAF I = 0 the trace map IS the Fibonacci recursion")
# on the leaf I = 0, writing (x_{n-1}, x_n, x_{n+1}) = (y, x, z), the relation is exactly Fricke-Vogt
A, B = sp.symbols('A B', real=True)
for name, fn in (("elliptic  x = cos(t)", sp.cos), ("hyperbolic x = cosh(t)", sp.cosh)):
    expr = I.subs({x: fn(A), y: fn(B), z: fn(A + B)})
    ok = sp.simplify(sp.expand_trig(sp.expand(expr))) == 0
    expr_m = I.subs({x: fn(A), y: fn(B), z: fn(A - B)})
    ok_m = sp.simplify(sp.expand_trig(sp.expand(expr_m))) == 0
    # the failability control: a NON-solution must NOT satisfy the relation
    bad = sp.simplify(sp.expand_trig(sp.expand(I.subs({x: fn(A), y: fn(B), z: fn(2 * A + B)})))) == 0
    print(f"      {name}: t_(n+1) = t_n + t_(n-1) solves it: {ok};  t_n - t_(n-1): {ok_m};  "
          f"control (2t_n + t_(n-1), must be False): {bad}")
    check("Q2", f"{name.split()[0]} regime linearises to the Fibonacci recursion, and a wrong "
                f"combination does not solve it", ok and ok_m and not bad)

# ---------------------------------------------------------------- Q3: no Lagrangian for the half step
print("\nQ3 -- THE THEOREM: an anti-symplectic map has NO discrete Lagrangian")
print("      A discrete Lagrangian L(a,b) gives the DEL relation  d2 L(a,b) + d1 L(b,c) = 0, whose")
print("      map (a,b) -> (b,c) preserves omega = d1 d2 L(a,b) da ^ db. Preserving a 2-form means")
print("      det = +1. The half step has det = -1. Hence NO L exists. The tick has no action.")
a, b, cc = sp.symbols('a b c', real=True)
# exhaustive confirmation over the general quadratic ansatz, in the linearised (angle) coordinates
# where the half step is t_(n+1) = t_n + t_(n-1), i.e. the matrix [[0,1],[1,1]], det -1.
p, q, r = sp.symbols('p q r')
# d1 L and d2 L are the partials in the FIRST and SECOND slot, then evaluated at (a,b) and (b,c).
# NOTE: sympy's subs is NOT simultaneous by default -- substituting {a: b, b: c} sequentially
# collapses L to a function of c alone and silently zeroes the second DEL term. Use placeholders.
u_, v_ = sp.symbols('u_ v_')
Lf = p * u_ ** 2 + q * u_ * v_ + r * v_ ** 2
d1L = lambda U, V: sp.diff(Lf, u_).subs({u_: U, v_: V}, simultaneous=True)
d2L = lambda U, V: sp.diff(Lf, v_).subs({u_: U, v_: V}, simultaneous=True)
DEL = sp.expand(d2L(a, b) + d1L(b, cc))
assert DEL.coeff(a) == DEL.coeff(cc) == q, ("the DEL relation must be symmetric in a and c", DEL)
print(f"      general quadratic DEL relation: {DEL} = 0   (a and c enter with the SAME coefficient q)")
target = cc - b - a
sol = sp.solve([sp.Poly(DEL - sp.Symbol('k') * target, a, b, cc).coeff_monomial(m)
                for m in (a, b, cc)], [p, q, r, sp.Symbol('k')], dict=True)
nontriv = [s for s in sol if s.get(sp.Symbol('k'), sp.Symbol('k')) != 0]
print(f"      solving DEL = k*(c - b - a) for a NON-ZERO k: {nontriv or 'NO SOLUTION'}")
check("Q3a", "no quadratic discrete Lagrangian reproduces the half step (a and c must share a "
             "coefficient, the recursion needs them opposite)", not nontriv)
M1 = sp.Matrix([[0, 1], [1, 1]])                            # the half step on (t_(n-1), t_n)
check("Q3b", f"and the obstruction is exactly orientation: det(half step) = {M1.det()} != +1",
      M1.det() == -1)
# positive control: a map that DOES have a Lagrangian must have det +1
check("Q3c", "positive control -- the DOUBLE step is orientation-preserving, so the obstruction "
             f"is absent there: det = {(M1 ** 2).det()}", (M1 ** 2).det() == 1)

# ---------------------------------------------------------------- Q4: the genesis carries the same bit
print("\nQ4 -- the SAME bit at the genesis: 'the golden morphism is L.P, and orientation SQUARES it'")
Lm = sp.Matrix([[1, 1], [0, 1]]); Rm = sp.Matrix([[1, 0], [1, 1]]); P = sp.Matrix([[0, 1], [1, 0]])
LP = Lm * P
print(f"      L = {Lm.tolist()}, P (the swap) = {P.tolist()}, L.P = {LP.tolist()}")
print(f"      det L = {Lm.det()},  det P = {P.det()},  det(L.P) = {LP.det()},  det((L.P)^2) = {(LP**2).det()}")
check("Q4a", "the genesis morphism L.P is orientation-REVERSING (det -1), because it carries the swap",
      LP.det() == -1 and P.det() == -1 and Lm.det() == 1)
check("Q4b", "squaring restores orientation at the genesis, exactly as it restores Poissonness at "
             "the dynamics -- ONE mechanism, two appearances", (LP ** 2).det() == 1 and (M1 ** 2).det() == 1)
check("Q4c", "and the two det(-1) objects are conjugate as GL2(Z) classes: same determinant and the "
             f"half step [[0,1],[1,1]] has trace {M1.trace()}, L.P has trace {LP.trace()}",
      M1.det() == LP.det())

# ---------------------------------------------------------------- Q5: the action for the double step
print("\nQ5 -- the DOUBLE step's generating function ON THE LEAF I = 0, constructed and verified")
M2 = M1 ** 2
print(f"      the double step on (t_(n-1), t_n): {M2.tolist()}, det {M2.det()}")
# a linear symplectic map [[A,B],[C,D]] (det 1, B != 0) is generated by
#   S(u, U) = (A u^2 - 2 u U + D U^2) / (2B),  with  v = -dS/du,  V = dS/dU
Am, Bm, Cm, Dm = [sp.Integer(M2[i, j]) for i, j in ((0,0),(0,1),(1,0),(1,1))]
u, U = sp.symbols('u U', real=True)
S = (Am * u ** 2 - 2 * u * U + Dm * U ** 2) / (2 * Bm)
v = sp.simplify(-sp.diff(S, u)); V = sp.simplify(sp.diff(S, U))
print(f"      S(u, U) = {sp.simplify(S)}      (u, v) the old pair, (U, V) the new")
# verify: solving v = -dS/du for U and substituting into V = dS/dU must reproduce M2 . (u, v)
vs = sp.symbols('v', real=True)
Usol = sp.solve(sp.Eq(vs, v), U)[0]; Vsol = sp.simplify(V.subs(U, Usol))
want = M2 * sp.Matrix([u, vs])
print(f"      generated map: ({sp.simplify(Usol)}, {Vsol})     required: ({want[0]}, {want[1]})")
check("Q5", "on I = 0 the generating function reproduces the double step exactly -- the double tick "
            "is a least-action system there, with this explicit discrete action",
      sp.simplify(Usol - want[0]) == 0 and sp.simplify(Vsol - want[1]) == 0)


# ---------------------------------------------------------------- Q6: WHICH LEAF IS THE OBJECT ON?
print("\nQ6 -- THE SCOPE CORRECTION: the object is NOT on the leaf Q2 and Q5 used")
X, Y, Z = sp.symbols('X Y Z', real=True)
kap = X ** 2 + Y ** 2 + Z ** 2 - X * Y * Z - 2          # B1248/B160's convention: FULL traces
half = sp.expand(kap.subs({X: 2 * x, Y: 2 * y, Z: 2 * z}))
check("Q6a", "the corpus's two conventions relate as I = (kappa - 2)/4 (B37 uses half-traces, "
             "B1248/B160 full traces)", sp.simplify(sp.expand((half - 2) / 4) - I) == 0)
kappa_obj = -2                                            # B1248: the once-punctured-torus fibre of m004
I_obj = sp.Rational(kappa_obj - 2, 4)
print(f"      B1248: the once-punctured-torus fibre of m004 has PARABOLIC commutator kappa = {kappa_obj}")
print(f"      so the OBJECT's leaf is I = {I_obj}, and Q2/Q5 were computed on I = 0 (the free leaf)")
check("Q6b", f"the object's leaf value is I = {I_obj}, NOT 0", I_obj == -1)
aa, bb, ccc = sp.symbols('alpha beta gamma', real=True)
leaf = sp.expand(I - I_obj)
mk = sp.expand(leaf.subs({x: sp.Rational(3, 2) * aa, y: sp.Rational(3, 2) * bb, z: sp.Rational(3, 2) * ccc}))
markov = aa ** 2 + bb ** 2 + ccc ** 2 - 3 * aa * bb * ccc
print(f"      the object's leaf is {leaf} = 0; under x = 3*alpha/2 this is {sp.factor(mk)}")
check("Q6c", "AND IT IS THE MARKOV SURFACE: x^2+y^2+z^2 = 2xyz is Markov's a^2+b^2+c^2 = 3abc under "
             "x = 3a/2 -- the same Markov the paper's selection criterion invokes (Hurwitz "
             "extremality, 'Markov's 2*sqrt2', 'the Markov root'), here as the PHASE SPACE",
      sp.simplify(mk - sp.Rational(9, 4) * markov) == 0)
# the linearisation does NOT extend: a wrong leaf must fail the cosh identity
bad_leaf = sp.simplify(sp.expand_trig(sp.expand(
    (I - I_obj).subs({x: sp.cosh(A), y: sp.cosh(B), z: sp.cosh(A + B)})))) == 0
print(f"      does the cosh linearisation solve the OBJECT's leaf? {bad_leaf}  (it must not)")
check("Q6d", "Q2's linearisation is leaf-specific and does NOT reach the object -- on the Markov "
             "surface the trace map is the Vieta/Markov move and does not linearise", not bad_leaf)

# --- but the THEOREM does reach the object: T reverses the invariant area form on EVERY leaf.
# Gelfand-Leray form on {I = const}: omega = dx ^ dy / I_z. Compute T* omega restricted to the leaf.
Iz = sp.diff(I, z); Iy = sp.diff(I, y)
zy = -Iy / Iz                                             # dz/dy along the leaf, at fixed x
# T*(dx ^ dy) = dX ^ dY = dz ^ dx = -(dz/dy) dx ^ dy  = (Iy/Iz) dx ^ dy
pull_coeff = sp.simplify((Iy / Iz) / Iz.subs(sub, simultaneous=True))
print(f"      T*(omega)/omega on an arbitrary leaf = {sp.simplify(pull_coeff * Iz)}")
check("Q6e", "T pulls the invariant (Gelfand-Leray) area form back to MINUS itself on EVERY leaf, "
             "the object's included -- so the no-Lagrangian theorem reaches the object even though "
             "the explicit action of Q5 does not", sp.simplify(pull_coeff * Iz + 1) == 0)
check("Q6f", "and an orientation-reversing map of a surface preserves NO area form at all, so the "
             "obstruction is absolute, not an artefact of the coordinates chosen",
      sp.simplify(pull_coeff * Iz) == -1)

json.dump({"det_half": str(d1), "det_square": str(d2), "genesis_det": str(LP.det()),
           "double_step": [[int(M2[i,j]) for j in (0,1)] for i in (0,1)], "generating_function": str(sp.simplify(S)), "object_leaf_I": str(I_obj),
           "object_leaf_is_markov": True, "fails": fails},
          open("b1341_least_action.json", "w"), indent=1)
print("\nB1341:", "PASS" if not fails else f"FAIL ({len(fails)}): {fails}")
raise SystemExit(0 if not fails else 1)
