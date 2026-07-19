#!/usr/bin/env python3
# =====================================================================
# B715 PROBE 2 — Is the object's native gauge structure inherently
# COMPLEX (complex Chern-Simons of E6(C)), NOT compact Yang-Mills?
#
# (a) REVERIFY B565-H1 independently (no re-run: rebuild + rederive):
#     the geometric holonomy rho(pi_1(4_1)) lands in E6(C)/F4(C) in
#     NO real form, and in NO compact form.
#       (a-i)   exact fig-8 holonomy over Q(sqrt-3); relator + parabolic
#               meridian confirm it is THE geometric (discrete-faithful) rep
#       (a-ii)  E6 exponents derived FROM the Cartan matrix (not cited);
#               adjoint trace tr Ad_e6(rho(a)) = 37437270 + 38799960 sqrt(3) i
#               NON-REAL -> kills ALL real forms
#       (a-iii) regular-unipotent meridian: Jordan {3,9,11,15,17,23} in E6
#               = regular unipotent (6 blocks = rank) -> kills ALL compact forms
# (b) CHARACTERIZE: inherently complex -> complex Chern-Simons of E6(C)
#     at the trace field Q(sqrt-3); Witten 1988 (3d gravity = complex CS of
#     the H^3 isometry group); the arithmetic-CS meeting (B708). NOT compact YM.
#
# Two-outcome: A = hidden compact real form / SM-like compact gauge group;
#              B = inherently complex (complex CS), no compact slice.
# Firewalled: structural/arithmetic only. No SM value, no physics assertion
# beyond the structural characterization.
# =====================================================================
import sympy as sp

s3 = sp.sqrt(3)            # real sqrt 3
I  = sp.I                  # sqrt -1
w  = sp.sqrt(-3)           # = s3 * I ; Q(sqrt-3) generator
LOG = []
def out(*a):
    s = ' '.join(str(x) for x in a); print(s); LOG.append(s)

out("="*70)
out("B715 PROBE 2 — native gauge structure: complex CS vs compact YM")
out("="*70)

# ---------------------------------------------------------------------
# PART 0 — E6 exponents derived INDEPENDENTLY from the Cartan matrix
#   (Kostant): adjoint of E6 restricted to the principal sl2 =
#   direct sum of Sym^{2 m_i}, m_i = exponents. Eigenvalues of the
#   Cartan matrix of a simply-laced g are  2 - 2 cos(pi m_i / h),
#   h = Coxeter number. For E6 h = 12. Solve for the m_i.
# ---------------------------------------------------------------------
out("\n[PART 0] E6 exponents from the Cartan matrix (not cited)")
# E6 Dynkin (Bourbaki): chain 1-3-4-5-6, node 2 hangs off node 4.
edges = [(1,3),(3,4),(4,5),(5,6),(2,4)]
Cm = sp.zeros(6,6)
for i in range(6): Cm[i,i] = 2
for (u,v) in edges:
    Cm[u-1,v-1] = -1; Cm[v-1,u-1] = -1
out("  E6 Cartan matrix built; symmetric:", Cm == Cm.T, " det =", Cm.det())
h = 12  # Coxeter number of E6 (independently: largest exponent 11 => h = 11+1)
evs = sorted([sp.nsimplify(e, [sp.sqrt(2),sp.sqrt(3),sp.sqrt(5)]) for e in Cm.eigenvals()])
exps = []
for m in range(1, h):
    lam = sp.simplify(2 - 2*sp.cos(sp.pi*sp.Integer(m)/h))
    for e in Cm.eigenvals():
        if sp.simplify(e - lam) == 0:
            exps.append(m); break
exps = sorted(set(exps))
out("  eigenvalue-matched exponents m_i =", exps)
dims = [2*m+1 for m in exps]
out("  principal-sl2 isotypic dims (2m+1) =", dims, " sum =", sum(dims))
assert exps == [1,4,5,7,8,11], exps
assert sum(dims) == 78, "dim E6 must be 78"
out("  => dim E6 = 78 (partitioned); matches B575 gl(27) build (23,17,15,11,9,3). PASS")
# F4 subalgebra exponents (regular-unipotent cross-check target)
F4_exps = [1,5,7,11]; out("  F4 exponents =", F4_exps, " dims", [2*m+1 for m in F4_exps],
                          " sum =", sum(2*m+1 for m in F4_exps), "(= dim F4 52)")

# ---------------------------------------------------------------------
# PART 1 (a-i) — EXACT geometric holonomy of the figure-eight over Q(sqrt-3)
#   Independently recognised (PSLQ, 60 digits) then VERIFIED by the
#   group relation, NOT trusted from SnapPy floats. The relator holding
#   + parabolic meridian = the discrete-faithful (geometric) rep.
#   SnapPy presentation:  < a,b | a b b b a B A A B >  (B=b^-1, A=a^-1)
# ---------------------------------------------------------------------
out("\n[PART 1] exact figure-eight holonomy over Q(sqrt-3) (a-i)")
# recognised exact entries (all in Q(sqrt3, i); traces land in Q(sqrt-3)):
a = sp.Matrix([[2 + s3*I,        -s3/2 - sp.Rational(3,2)*I],
               [s3 - I,          -1                        ]])
b = sp.Matrix([[0,                          -s3/2 - sp.Rational(1,2)*I],
               [ s3/2 - sp.Rational(1,2)*I, -sp.Rational(3,2) - s3/2*I ]])
def inv(M): return sp.Matrix([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]])  # SL2 inverse (det=1)
da, db = sp.simplify(a.det()), sp.simplify(b.det())
out("  det a =", da, "  det b =", db)
assert da == 1 and db == 1
A, B = inv(a), inv(b)
R = sp.simplify(a*b*b*b*a*B*A*A*B)
inPSL = (R == sp.eye(2)) or (R == -sp.eye(2))
out("  relator  a b b b a B A A B  =", R.tolist(), "= +-I in SL2:", inPSL)
assert inPSL, "recognised matrices must satisfy the fig-8 relator (in PSL2)"
out("  => a genuine PSL(2,C) = Isom+(H^3) representation of pi_1(4_1)")
out("     (relator = -I: the geometric holonomy is a PSL2, i.e. H^3-isometry, rep)")
# meridian word in this presentation is A B B; geometric => parabolic (tr +-2)
mer = A*B*B
trm = sp.simplify(mer.trace())
out("  meridian (A B B) trace =", trm, " -> parabolic:", trm in (2,-2))
assert trm in (2,-2), "geometric rep: meridian must be parabolic"
tr_a = sp.simplify(a.trace())
out("  tr a =", tr_a, " = 1 + sqrt(-3):", sp.simplify(tr_a-(1+w))==0)
# trace field check: tr(a), tr(b), tr(ab) all in Q(sqrt-3)?
trab = sp.simplify((a*b).trace())
def in_Qsqrtm3(t):
    # t = p + q*sqrt(-3) with p,q rational?  q = Im(t)/sqrt3, p = Re(t)
    p = sp.nsimplify(sp.re(t)); q = sp.nsimplify(sp.im(t)/s3)
    return (sp.simplify(t - (p + q*w)) == 0) and p.is_rational and q.is_rational
out("  tr a =", tr_a, "  tr b =", sp.simplify(b.trace()), "  tr ab =", trab)
for nm,t in [('tr a',tr_a),('tr b',sp.simplify(b.trace())),('tr ab',trab)]:
    ok = in_Qsqrtm3(t)
    out(f"    {nm} in Q(sqrt-3):", ok); assert ok
out("  trace field = Q(sqrt-3) (invariant trace field of 4_1) -- non-real. PASS")
# irreducibility (so this is THE geometric rep, not a reducible parabolic one):
irr = sp.simplify((a*b*A*B).trace() - 2)
out("  tr[a,b]-2 =", irr, " -> IRREDUCIBLE:", irr != 0); assert irr != 0
# the meridian image is a NONTRIVIAL unipotent (needed for PART 3):
mernontriv = (mer != sp.eye(2)) and (mer != -sp.eye(2))
out("  meridian != +-I (nontrivial parabolic/unipotent):", mernontriv); assert mernontriv

# The double-precision SnapPy branch B565 used has tr a = -1 - sqrt(-3) = -(1+sqrt-3).
# Since Sym^{even}(-g) = Sym^{even}(g), BOTH branches give the SAME adjoint trace.
out("  note: B565 branch has tr a = -(1+sqrt-3); Sym^{even}(-g)=Sym^{even}(g)")
out("        => identical E6 adjoint trace for both Galois branches (checked below).")

# ---------------------------------------------------------------------
# PART 2 (a-ii) — E6 ADJOINT TRACE via the principal sl2, EXACT.
#   Ad_e6 | principal-sl2  = (+)_{m in exps} Sym^{2m}.
#   tr Ad_e6(rho(g)) = sum_m chi_{2m}(tr rho(g)),
#   chi_d = SL2 character of Sym^d (Chebyshev-U in t = tr):
#   chi_0=1, chi_1=t, chi_d = t chi_{d-1} - chi_{d-2}.
#   NON-REAL adjoint trace kills ALL real forms (a real form's adjoint
#   is a REAL representation -> real traces on the whole real group).
# ---------------------------------------------------------------------
out("\n[PART 2] E6 adjoint trace via principal sl2 (a-ii)")
def chi(d, t):
    c0, c1 = sp.Integer(1), t
    if d == 0: return c0
    for _ in range(2, d+1):
        c0, c1 = c1, sp.expand(t*c1 - c0)
    return c1
def adj_trace(t):
    return sp.expand(sum(chi(2*m, t) for m in exps))
for label, t in [("tr a = 1+sqrt-3 (HP branch)", 1+w),
                 ("tr a = -1-sqrt-3 (B565 branch)", -1-w)]:
    val = adj_trace(t)
    val = sp.nsimplify(sp.expand(val))
    out(f"  {label}:  tr Ad_e6 =", val)
target = 37437270 + 38799960*s3*I
got = sp.nsimplify(sp.expand(adj_trace(-1-w)))
out("  B565 target = 37437270 + 38799960*sqrt(3)*i")
match = sp.simplify(got - target) == 0
out("  MATCH B565-H1 (exact, in Q(sqrt-3)):", match)
assert match
# non-real?
imag = sp.im(sp.expand(got))
out("  Im(tr Ad_e6) =", sp.simplify(imag), " -> NON-REAL:", sp.simplify(imag) != 0)
assert sp.simplify(imag) != 0
out("  DISCRIMINATING FACT #1: adjoint trace is NON-REAL")
out("    => rho(pi_1) lies in NO real form of E6 (real form => real adjoint traces).")
# adjoint traces on a compact/real form are algebraic integers in a TOTALLY REAL field;
# here the value has a nonzero imaginary part in Q(sqrt-3): impossible for any real form.

# independent cross-check via F4 (folding subgroup): F4 adjoint trace also non-real
def adj_trace_F4(t): return sp.expand(sum(chi(2*m, t) for m in F4_exps))
f4val = sp.nsimplify(sp.expand(adj_trace_F4(-1-w)))
out("  cross-check F4 adjoint trace =", f4val, " NON-REAL:", sp.simplify(sp.im(f4val))!=0)

# ---------------------------------------------------------------------
# PART 3 (a-iii) — REGULAR-UNIPOTENT MERIDIAN kills COMPACT forms.
#   The parabolic meridian rho(mer) is (up to sign) a regular unipotent
#   J2 in SL2. Under the principal embedding, Sym^{2m}(J2) is a SINGLE
#   Jordan block of size 2m+1 (unipotent). So Ad_e6(rho(mer)) is unipotent
#   with Jordan type {3,9,11,15,17,23}: SIX blocks = rank(E6) = REGULAR
#   unipotent. A compact Lie group has NO nontrivial unipotent element
#   (every element is semisimple / lies in a torus). => no compact form.
# ---------------------------------------------------------------------
out("\n[PART 3] regular-unipotent meridian kills compact forms (a-iii)")
xs, ys = sp.symbols('x y')
J = sp.Matrix([[1,1],[0,1]])         # regular unipotent in SL2
def sym_mat(Asp, d):
    xi = Asp[0,0]*xs + Asp[1,0]*ys
    yi = Asp[0,1]*xs + Asp[1,1]*ys
    basis = [xs**(d-i)*ys**i for i in range(d+1)]
    S = sp.zeros(d+1, d+1)
    for j,bj in enumerate(basis):
        img = sp.expand(bj.subs({xs: xi, ys: yi}, simultaneous=True))
        P = sp.Poly(img, xs, ys)
        for i in range(d+1):
            S[i,j] = P.coeff_monomial(xs**(d-i)*ys**i)
    return S
assert sym_mat(J,1) == J   # gate the convention: Sym^1 = identity map
e6_blocks = []
for m in exps:
    S = sym_mat(J, 2*m); N = S - sp.eye(2*m+1)
    k = 0; Pn = sp.eye(2*m+1)
    while True:
        Pn = Pn*N; k += 1
        if Pn == sp.zeros(2*m+1, 2*m+1): break
    e6_blocks.append(k)
    assert k == 2*m+1, (m,k)   # single Jordan block of full size
out("  Sym^{2m}(J2) nilpotency degrees (= block sizes) =", e6_blocks)
out("  Ad_e6(unipotent meridian) Jordan type =", sorted(e6_blocks, reverse=True),
    " -> #blocks =", len(e6_blocks), "= rank(E6) = REGULAR unipotent")
assert sorted(e6_blocks) == [3,9,11,15,17,23]
assert len(e6_blocks) == 6
out("  DISCRIMINATING FACT #2: the meridian image is a nontrivial (regular) UNIPOTENT")
out("    => rho(pi_1) lies in NO COMPACT real form (compact => every element")
out("       semisimple; no nontrivial unipotents). The 'compact slice' is absent.")

# ---------------------------------------------------------------------
# PART 4 (b) — CHARACTERIZE THE KIND + TWO-OUTCOME VERDICT
# ---------------------------------------------------------------------
out("\n[PART 4] characterization + verdict")
out("  Both discriminating facts are structural theorems on the SAME holonomy:")
out("   (1) non-real adjoint trace 37437270 + 38799960 sqrt(3) i  -> NO real form")
out("   (2) regular-unipotent meridian {3,9,11,15,17,23}          -> NO compact form")
out("  The image sits in E6(C) but in no real (a fortiori no compact) form.")
out("  A COMPACT Yang-Mills gauge group is exactly a compact real form; the")
out("  hyperbolic geometry provides no such slice (compactness = unitarity =")
out("  a MEASUREMENT-face feature, per B565 addendum).")
out("")
out("  KIND: inherently COMPLEX. The native gauge object = complex Chern-Simons")
out("  of E6(C) at the trace field Q(sqrt-3). Consistent with:")
out("   - Witten 1988: 3d (Euclidean) gravity = complex CS with gauge group the")
out("     isometry group of H^3 (here promoted along principal sl2 into E6(C));")
out("   - the arithmetic-CS meeting (B708): CS on Q(sqrt-3)'s arithmetic.")
out("  It is NOT a compact Yang-Mills theory: the compact slice is precisely")
out("  what the hyperbolic geometry does not supply.")
out("")
out("  TWO-OUTCOME:")
out("   A (hidden compact / SM-like compact gauge group): REFUTED")
out("       -- no real form at all; a fortiori no compact real form.")
out("   B (inherently complex, complex CS, no compact slice): CONFIRMED")
out("  ==> OUTCOME B.")

with open(__file__.replace('.py','_out.txt'),'w') as f:
    f.write('\n'.join(LOG)+'\n')
out("\n[written b715_probe2_out.txt]")
