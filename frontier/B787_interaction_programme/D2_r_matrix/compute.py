"""
B787 Door D2 -- R-matrix braiding interaction (Fibonacci MTC).

Prereg (PREREGISTRATION.md, D2 R-matrix):
  OUTCOME A: a Born probability from R on the pointer-object tau x tau pair equals
             JUNO (0.30902) EXACTLY or clears base-rate, OR yields a new exact invariant.
  OUTCOME B: all Born numbers are {0.276, known MTC values, base-rate} -- physics-silent.

Setup (exact):
  Fibonacci MTC R-matrix on the tau x tau fusion channel (dim 2, basis {|1>,|tau>}):
      R = diag(e^{-4 pi i / 5},  e^{+3 pi i / 5}).
  Pointer and object are two Fibonacci anyons; their pair state lives in tau x tau.
  The measurement torsor V4 = {1, c, theta, c.theta} (tests/test_b766_torsor.py):
      1      = identity
      c      = complex conjugation K (antiunitary; orientation/chirality flip)
      theta  = the 27<->27bar channel swap  = sigma_x = [[0,1],[1,0]] (reversal)
      c.theta= K . sigma_x
  Each orientation g gives a state |psi_g> = U_g |psi>; the interaction Born number is
  the self-overlap  |<psi_g| R |psi_g>|^2.

Targets:  JUNO = 0.30902 (the one pin);  |S_tautau|^2 = 1/(phi*sqrt5) = 0.27639 (THEOREM,
NOT JUNO -- do not force 0.276 -> 0.307).

EVERYTHING is exact sympy. The V4-invariance is PROVED symbolically (general amplitudes);
the numbers are given in closed radical form. An adversarial alternative reading (the
transition amplitude |<psi|R|psi_g>|^2) is also computed, to test whether ANY reading
reaches JUNO at a principled state -- and to expose the amplitude-tuning base-rate trap.
"""
import sympy as sp

# ---------------------------------------------------------------- exact constants
phi   = (1 + sp.sqrt(5)) / 2
JUNO  = sp.Rational(30902, 100000)              # the pin, as given (0.30902)
S2    = 1/(phi*sp.sqrt(5))                       # |S_tautau|^2 THEOREM = 1/(phi*sqrt5)

lam1  = sp.exp(sp.Rational(-4, 5)*sp.pi*sp.I)    # R eigenvalue on channel |1>
lam2  = sp.exp(sp.Rational( 3, 5)*sp.pi*sp.I)    # R eigenvalue on channel |tau>
R     = sp.diag(lam1, lam2)

# rectangular (exact) forms
lam1r = sp.expand_complex(lam1)
lam2r = sp.expand_complex(lam2)

# the eigen-phase overlap that governs every Born number here
overlap = sp.simplify(sp.re(lam1*sp.conjugate(lam2)))   # cos(arg lam1 - arg lam2)

lines = []
def P(*a): lines.append(" ".join(str(x) for x in a))

P("="*74)
P("B787 D2 -- Fibonacci R-matrix braiding, Born probs at the 4 V4 orientations")
P("="*74)
P(f"R = diag(e^(-4 pi i/5), e^(3 pi i/5))")
P(f"  lam1 = e^(-4pi i/5) = {lam1r}   (num {complex(lam1):.6f})")
P(f"  lam2 = e^(+3pi i/5) = {lam2r}   (num {complex(lam2):.6f})")
P(f"  |lam1|=|lam2|=1 exact: {sp.simplify(abs(lam1)-1)==0 and sp.simplify(abs(lam2)-1)==0}")
P("")
P("Targets:")
P(f"  JUNO  = {JUNO} = {float(JUNO):.6f}   (the pin)")
P(f"  |S_tautau|^2 = 1/(phi sqrt5) = {sp.nsimplify(S2)} = {float(S2):.6f}   (THEOREM, != JUNO)")
P(f"  |S_tautau|^2 closed form (5-sqrt5)/10 check: "
  f"{sp.simplify(S2 - (5-sp.sqrt(5))/10)==0}")
P("")
P("Eigen-phase overlap  cos(arg lam1 - arg lam2) = Re(lam1 conj(lam2)):")
P(f"  = {overlap} = {float(overlap):.7f}   [ = cos(3pi/5) = -(sqrt5-1)/4 ]")
P(f"  identity cos(3pi/5) = -(sqrt5-1)/4 : "
  f"{sp.simplify(overlap - (-(sp.sqrt(5)-1)/4))==0}")
P("")

# ================================================================ V4 action
def U(g, psi):
    """apply V4 orientation g in {'1','c','theta','ctheta'} to a 2-vector psi."""
    a, b = psi[0], psi[1]
    if g == '1':      return sp.Matrix([a, b])
    if g == 'c':      return sp.Matrix([sp.conjugate(a), sp.conjugate(b)])         # antiunitary
    if g == 'theta':  return sp.Matrix([b, a])                                      # channel swap
    if g == 'ctheta': return sp.Matrix([sp.conjugate(b), sp.conjugate(a)])
    raise ValueError(g)

def _abs2(amp):
    """|amp|^2 as an exact REAL sympy expression (robust to unevaluated Abs)."""
    return sp.simplify(sp.re(sp.expand(amp*sp.conjugate(amp))))

def zero(expr):
    """True iff expr is exactly 0 -- forces denesting of sqrt(30+10 sqrt5)=5+sqrt5 etc."""
    return sp.simplify(sp.sqrtdenest(sp.expand(expr))) == 0

def born_self(g, psi):
    """|<psi_g| R |psi_g>|^2 with psi_g = U_g psi (the door's observable)."""
    v = U(g, psi)
    amp = (v.conjugate().T * R * v)[0, 0]     # <v|R|v> = |v1|^2 lam1 + |v2|^2 lam2
    return _abs2(amp)

# ----------------------------------------------------------------
# STEP 1 -- SYMBOLIC PROOF: the self-overlap Born number is V4-INVARIANT.
# general complex amplitudes a,b (the modulus^2 P,Q are what survive).
# ----------------------------------------------------------------
a, b = sp.symbols('a b')
Pmod, Qmod = sp.symbols('P Q', nonnegative=True)   # P=|a|^2, Q=|b|^2, P+Q=1
psi_sym = sp.Matrix([a, b])

born_g = {}
for g in ('1', 'c', 'theta', 'ctheta'):
    v = U(g, psi_sym)
    amp = (v.conjugate().T * R * v)[0, 0]
    # <v|R|v> = |v1|^2 lam1 + |v2|^2 lam2 ; substitute |a|^2->P, |b|^2->Q
    amp = amp.rewrite(sp.Abs)
    amp = amp.subs({sp.Abs(a)**2: Pmod, sp.Abs(b)**2: Qmod,
                    sp.conjugate(a)*a: Pmod, sp.conjugate(b)*b: Qmod,
                    a*sp.conjugate(a): Pmod, b*sp.conjugate(b): Qmod})
    born = sp.simplify(sp.expand(amp*sp.conjugate(amp)))
    born = sp.simplify(born.subs({sp.Abs(a)**2: Pmod, sp.Abs(b)**2: Qmod}))
    born_g[g] = sp.simplify(sp.re(born))     # it is real

# closed form of the generic self-overlap Born, in P (with Q=1-P)
born_general = sp.simplify(born_g['1'].subs(Qmod, 1-Pmod))
P("-"*74)
P("STEP 1  self-overlap reading  |<psi_g|R|psi_g>|^2  -- V4 invariance (symbolic)")
P("-"*74)
for g in ('1','c','theta','ctheta'):
    P(f"  born[{g:7s}](P,Q) = {sp.simplify(born_g[g])}")
inv_1c   = zero(born_g['1'] - born_g['c'])
inv_1th  = zero(born_g['1'] - born_g['theta'])
inv_1cth = zero(born_g['1'] - born_g['ctheta'])
P(f"  born[1]-born[c]      = 0 ? {inv_1c}")
P(f"  born[1]-born[theta]  = 0 ? {inv_1th}    (needs sqrt(30+10sqrt5)=5+sqrt5 denest)")
P(f"  born[1]-born[ctheta] = 0 ? {inv_1cth}")
P(f"  ==> ALL FOUR V4 ORIENTATIONS EQUAL (exact): {inv_1c and inv_1th and inv_1cth}")
born_closed = 1 - 2*Pmod*(1-Pmod)*(3+sp.sqrt(5))/4
P(f"  generic closed form (Q=1-P):  Born(P) = 1 - 2 P(1-P)(3+sqrt5)/4")
P(f"     matches computed born[1]|Q=1-P : {zero(born_general - born_closed)}")
P("")

# ----------------------------------------------------------------
# STEP 2 -- the EXACT range of the self-overlap Born over all states P in [0,1].
# ----------------------------------------------------------------
Bmin = sp.simplify(born_general.subs(Pmod, sp.Rational(1,2)))   # min at P=1/2
Bmax = sp.simplify(born_general.subs(Pmod, 0))                  # max at P=0 or 1
P("-"*74)
P("STEP 2  exact range of the self-overlap Born over ALL pointer-object states")
P("-"*74)
P(f"  min at P=1/2 : Born = {Bmin} = {float(Bmin):.6f}   [ = sin^2(36deg) = (5-sqrt5)/8 ]")
P(f"     identity (5-sqrt5)/8 = sin^2(pi/5): "
  f"{sp.simplify(Bmin-(5-sp.sqrt(5))/8)==0 and sp.simplify(Bmin-sp.sin(sp.pi/5)**2)==0}")
P(f"  max at P=0/1 : Born = {Bmax} = {float(Bmax):.6f}")
P(f"  ==> self-overlap Born in [ (5-sqrt5)/8 , 1 ] = [{float(Bmin):.5f}, 1]")
P(f"  JUNO={float(JUNO):.5f}  <  {float(Bmin):.5f} = min ?  "
  f"{JUNO < Bmin}   -> JUNO STRUCTURALLY UNREACHABLE")
P(f"  |S_tautau|^2={float(S2):.5f}  <  {float(Bmin):.5f} = min ?  "
  f"{S2 < Bmin}   -> also unreachable")
P("")

# ----------------------------------------------------------------
# STEP 3 -- the two PRINCIPLED pointer-object states, exact self-overlap Born.
# equal (unbiased pointer)  P=Q=1/2 ;  quantum-dimension  P:Q = d_1^2:d_tau^2 = 1:phi^2.
# ----------------------------------------------------------------
P_eq   = sp.Rational(1,2)
P_qd   = 1/(1+phi**2)                          # = 1/(2+phi) = 1/(phi sqrt5)
Q_qd   = 1 - P_qd
P("-"*74)
P("STEP 3  self-overlap Born at the two PRINCIPLED states")
P("-"*74)
P(f"  quantum-dim weight P_qd = 1/(1+phi^2) = 1/(phi sqrt5) = {sp.nsimplify(P_qd)} "
  f"= {float(P_qd):.6f}  (equals |S_tautau|^2)")
be_eq = sp.simplify(born_general.subs(Pmod, P_eq))
be_qd = sp.simplify(born_general.subs(Pmod, P_qd))
P(f"  equal        P=1/2   : Born = {be_eq} = {float(be_eq):.6f}   [(5-sqrt5)/8]")
P(f"  quantum-dim  P=P_qd  : Born = {sp.nsimplify(be_qd)} = {float(be_qd):.6f}   [(7-sqrt5)/10]")
P(f"     (7-sqrt5)/10 check: {sp.simplify(be_qd-(7-sp.sqrt(5))/10)==0}")
P(f"  self-overlap Born =? JUNO at either principled state: "
  f"{sp.simplify(be_eq-JUNO)==0 or sp.simplify(be_qd-JUNO)==0}")
P(f"  self-overlap Born =? |S_tautau|^2 at either principled state: "
  f"{sp.simplify(be_eq-S2)==0 or sp.simplify(be_qd-S2)==0}")

# numeric cross-check of the symbolic self-overlap via explicit vectors
P("")
P("  numeric cross-check (explicit complex vectors, all four g):")
for label, Pv in (("equal", P_eq), ("quantum-dim", P_qd)):
    psi = sp.Matrix([sp.sqrt(Pv), sp.sqrt(1-Pv)])
    vals = {g: float(born_self(g, psi)) for g in ('1','c','theta','ctheta')}
    P(f"    {label:11s}: " + "  ".join(f"{g}={vals[g]:.6f}" for g in ('1','c','theta','ctheta')))

# ----------------------------------------------------------------
# STEP 4 -- adversarial alternative reading: transition amplitude |<psi|R|psi_g>|^2.
# does ANY orientation/state reach JUNO at a principled state?  (and expose the trap)
# ----------------------------------------------------------------
def born_trans(g, psi):
    v = U(g, psi)
    amp = (psi.conjugate().T * R * v)[0, 0]
    return _abs2(amp)

P("")
P("-"*74)
P("STEP 4  adversarial reading  |<psi|R|psi_g>|^2  (transition, not the door's obs.)")
P("-"*74)
# symbolic for real psi = (sqrt P, sqrt Q):  g=1,c -> self value ; g=theta,ctheta -> P Q |lam1+lam2|^2
sumsq = _abs2(lam1+lam2)
P(f"  |lam1+lam2|^2 = {sp.nsimplify(sumsq)} = {float(sumsq):.6f}   [ = (5-sqrt5)/2 ]")
P(f"     (5-sqrt5)/2 check: {sp.simplify(sumsq-(5-sp.sqrt(5))/2)==0}")
for label, Pv in (("equal", P_eq), ("quantum-dim", P_qd)):
    psi = sp.Matrix([sp.sqrt(Pv), sp.sqrt(1-Pv)])
    vals = {g: born_trans(g, psi) for g in ('1','c','theta','ctheta')}
    P(f"  {label:11s}: " + "  ".join(f"{g}={float(vals[g]):.6f}" for g in ('1','c','theta','ctheta')))
    P(f"               exact theta-branch = {sp.nsimplify(vals['theta'])}")
# quantum-dim theta transition == |S_tautau|^2 exactly?
psi_qd = sp.Matrix([sp.sqrt(P_qd), sp.sqrt(1-P_qd)])
th_qd  = born_trans('theta', psi_qd)
P(f"  quantum-dim theta-transition =? |S_tautau|^2 (the THEOREM, NOT JUNO): "
  f"{sp.simplify(th_qd - S2)==0}")
# JUNO reachable in transition-theta only by TUNING P: P(1-P)*(5-sqrt5)/2 = JUNO
Pt = sp.symbols('Pt', positive=True)
tune = sp.solve(sp.Eq(Pt*(1-Pt)*(5-sp.sqrt(5))/2, JUNO), Pt)
tune_f = sorted(set(float(s) for s in tune if s.is_real and 0 <= s <= 1))
P(f"  JUNO in transition-theta requires TUNED P(1-P) = 2 JUNO/(5-sqrt5) = "
  f"{float(2*JUNO/(5-sp.sqrt(5))):.6f}")
P(f"     -> non-canonical P in {[round(x,5) for x in tune_f]} (neither 1/2 nor 1/(phi sqrt5))")
P(f"     transition-theta range over P: [0, (5-sqrt5)/8] = [0, {float((5-sp.sqrt(5))/8):.5f}] "
  f"CONTAINS JUNO -> a 1-param family sweeps it = BASE-RATE TRAP, not a hit.")

# ----------------------------------------------------------------
# STEP 5 -- base-rate assessment + verdict
# ----------------------------------------------------------------
P("")
P("-"*74)
P("STEP 5  base-rate assessment + verdict")
P("-"*74)
# the near-coincidence: cos72 = (sqrt5-1)/4 vs JUNO
cos72 = (sp.sqrt(5)-1)/4
P(f"  cos(72deg) = (sqrt5-1)/4 = {float(cos72):.7f}  vs JUNO {float(JUNO):.7f}  "
  f"Delta = {abs(float(cos72-JUNO)):.2e}")
P(f"    -- but (sqrt5-1)/4 is (a) the eigen-phase OVERLAP, NOT a Born number, and")
P(f"       (b) a pentagon/phi anchor already in the look-elsewhere candidate set.")
P("")
P("  candidate anchors in [0,1] (prereg set): JUNO 0.30902, 1/phi 0.61803, "
  "1/(phi sqrt5) 0.27639,")
P("     2/3, 1/2, 1/3, cos^2/sin^2 of cardinal angles, small rationals  (~12 candidates)")
P("  programme look-elsewhere budget ~ 3.6 expected chance hits (error-48 density).")
P("")
P("  Born numbers produced at PRINCIPLED states (exact radicals):")
P(f"     self-overlap  equal      : (5-sqrt5)/8  = {float(be_eq):.6f}")
P(f"     self-overlap  quantum-dim: (7-sqrt5)/10 = {float(be_qd):.6f}")
P(f"     transition    quantum-dim: (5-sqrt5)/10 = {float(th_qd):.6f}  (= |S_tautau|^2 THEOREM)")
P("  JUNO matches at a principled state: NONE.")
P("  self-overlap Born is V4-INVARIANT (exact) and bounded below by (5-sqrt5)/8=0.34549,")
P("     so JUNO=0.30902 and |S_tautau|^2=0.27639 are BOTH structurally unreachable.")
P("  JUNO appears only by tuning a free amplitude in the transition reading (the trap).")
P("")
P("  VERDICT: OUTCOME B -- physics-silent MISS.")
P("     Exact structural residue (NOT a JUNO hit, recorded to HINT_LEDGER only):")
P("       (i)  the pointer-object braiding self-overlap Born is exactly V4-invariant")
P("            (the measurement torsor is INVISIBLE to a diagonal R -- c only conjugates,")
P("            theta only relabels channels; |sum p_i lam_i|^2 is invariant under both);")
P("       (ii) it is bounded below by sin^2(36deg)=(5-sqrt5)/8, placing JUNO and")
P("            |S_tautau|^2 strictly outside the achievable window;")
P("       (iii)the quantum-dim transition-theta Born reproduces |S_tautau|^2=(5-sqrt5)/10")
P("            EXACTLY (self-consistency with the MTC theorem, not JUNO).")

out = "\n".join(lines)
print(out)
with open(__file__.rsplit('/',1)[0] + "/output.txt", "w") as f:
    f.write(out + "\n")
