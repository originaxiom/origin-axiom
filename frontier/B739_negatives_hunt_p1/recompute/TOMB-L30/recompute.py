#!/usr/bin/env python3
"""
B739 Stage-B recompute — TOMB-L30 (tombstone S019, TOMBSTONES.md:L30)

Banked kill (S019): "Fisher metric on CS level k. A heuristic information-geometry
reading on the Chern-Simons level. DEAD - heuristic, not rigorous; no bounded test
survived. Kill: the dead-sweep V-rows (see archive/PHYSICS_RESONANCES.md)."

Citation topology (verified by inspection during this recompute):
  - archive/PHYSICS_RESONANCES.md (the tombstone's one-hop citation) contains ZERO
    occurrences of "Fisher" - no Fisher-specific computation lives there.
  - The one rigorous Fisher computation in the kill's neighborhood is
    paths/E21_self_evidencing_closure/FINDINGS.md item (d), ledgered as V6:
        F(m) = 16/(m^2(m^2+4)) = 16/disc(char(M^2)) = 16*g_WP(m^2+2) = (4/Delta_eig)^2
  - docs/atlas/FAILURE_ATLAS.md ("Hessian-Signature And Fisher-On-k Heuristics Are
    Not Spacetime", consolidated row C4) states S019's actual content: the Fisher
    metric "on the parameter k/m" is the same positive Weil-Petersson coefficient -
    a 1-D positive metric on a parameter line, not a spacetime metric, and carries
    no rigorous k-object.

THE DISCRIMINATING FACT (the fact that, if true, kills S019):
  The only Fisher/information metric constructible from the arc's own declared
  conventions collapses EXACTLY to 16 * g_WP(tr M^2) - an elementary chain-rule
  identity on the classical parameter line - and it is
    (i)   IDENTICALLY k-FREE (the CS level k never enters the object),
    (ii)  POSITIVE-definite 1-D (no indefinite direction for any "emergence" reading),
    (iii) CONTENT-FREE beyond WP (its length element is d(LE) itself: sqrt(F) dI = dLE).
  Hence the "information-geometry reading on the CS level k" has no rigorous object:
  the reading collapsed to Weil-Petersson before k could enter -> the kill
  ("heuristic, not rigorous; no bounded test survived") is upheld iff (i)-(iii)
  recompute true.

DECLARED CONVENTIONS (E1):
  C1 (repo convention, B92/B107 family): metallic matrix M = [[m,1],[1,0]],
     det M = -1, tr M = m; the manifold-carrying square M^2 has
     char(M^2) = t^2 - (m^2+2) t + 1.
  C2 (E21 declared): coordinate I = c^2 - 1; matching point I* = m^2/4;
     self-model discrepancy D(I) = (4I - m^2)^2; length/Lyapunov function
     LE(I) = arccosh(2I + 1).
  C3 (E21 declared): g_WP(alpha) = 1/(alpha^2 - 4) (Goldman/Weil-Petersson
     coefficient), evaluated at alpha = tr(M^2) = m^2 + 2;
     Delta_eig = Lambda - 1/Lambda (eigenvalue gap of M^2).
  C4 (E1 CHOICE - undeclared in E21, declared here): "the Fisher information of
     D(I)" is read as the Fisher information of the 1-parameter unit-variance
     Gaussian location family with mean LE(I), i.e. F(I) = (dLE/dI)^2, evaluated
     at I* = m^2/4. This is the unique elementary reading that (a) reproduces
     E21(d)'s stated closed form and (b) matches E21's own derivation note
     ("follows from the chain rule on LE(I)=arccosh(2I+1)").
  C5 (repo quantum-side convention, TOMBSTONES.md itself): at CS level k the
     quantum rep is defined over q = exp(2*pi*i/(k+2)); k ranges over positive
     integers (a discrete family).

Deterministic: sympy-only symbolic computation; no wall-clock, no randomness,
no network.
"""

import sympy as sp

m, I, c, t, k, alpha = sp.symbols('m I c t k alpha', positive=True)

lines = []


def log(s=""):
    lines.append(s)
    print(s)


log("=" * 76)
log("TOMB-L30 (S019) Stage-B recompute - Fisher metric on CS level k")
log("=" * 76)

# ---------------------------------------------------------------- Step 0
log()
log("STEP 0 - conventions instantiated (C1, C2)")
M = sp.Matrix([[m, 1], [1, 0]])
M2 = M * M
char_M2 = sp.expand((t ** 2 - sp.trace(M2) * t + M2.det()))
log(f"  M = [[m,1],[1,0]]      det M   = {M.det()}   tr M = {sp.trace(M)}")
log(f"  char(M^2)              = {char_M2}")
assert char_M2 == sp.expand(t ** 2 - (m ** 2 + 2) * t + 1)

# The E21(a/b) algebraic bridge: on I = c^2 - 1 the restricted char poly is
# t^2 - (4c^2-2) t + 1; equality with char(M^2) at I = m^2/4 is one linear identity.
bridge = sp.expand((4 * c ** 2 - 2).subs(c ** 2, m ** 2 / 4 + 1))  # I=c^2-1=m^2/4
log(f"  4c^2 - 2 at I=m^2/4    = {bridge}   (= tr M^2 = m^2+2: "
    f"{sp.simplify(bridge - (m**2 + 2)) == 0})")
assert sp.simplify(bridge - (m ** 2 + 2)) == 0
# D(I) is the squared residual of that identity:
resid = sp.expand((4 * c ** 2 - 2) - (m ** 2 + 2)).subs(c ** 2, I + 1)
D = sp.expand(resid ** 2)
log(f"  residual (4c^2-2)-(m^2+2) on I=c^2-1 = {resid}   => D(I) = {D}")
assert D == sp.expand((4 * I - m ** 2) ** 2)

# ---------------------------------------------------------------- Step 1
log()
log("STEP 1 - the Fisher object from the declared conventions (C2+C4)")
LE = sp.acosh(2 * I + 1)
dLE_dI = sp.simplify(sp.diff(LE, I))
log(f"  LE(I)     = arccosh(2I+1)")
log(f"  dLE/dI    = {dLE_dI}")
F_of_I = sp.simplify(dLE_dI ** 2)
log(f"  F(I)      = (dLE/dI)^2 = {F_of_I}")
Istar = m ** 2 / 4
F_m = sp.simplify(F_of_I.subs(I, Istar))
log(f"  F(m) = F(I*)|I*=m^2/4  = {F_m}")
F_target = 16 / (m ** 2 * (m ** 2 + 4))
ok1 = sp.simplify(F_m - F_target) == 0
log(f"  F(m) == 16/(m^2(m^2+4)) (the banked E21(d)/V6 value):  {ok1}")
assert ok1

# sanity: LE at the matching point is log(Lambda), Lambda = top eigenvalue of M^2
Lam = sp.simplify((m ** 2 + 2 + m * sp.sqrt(m ** 2 + 4)) / 2)
ok_le = sp.simplify(sp.expand_trig(LE.subs(I, Istar)) - sp.log(Lam)) == 0
ok_le_num = all(
    abs(float(LE.subs([(I, mm ** 2 / sp.Integer(4))]).evalf(30))
        - float(sp.log(Lam.subs(m, mm)).evalf(30))) < 1e-25
    for mm in range(1, 7))
log(f"  LE(I*) == log(Lambda(M^2)) [symbolic/numeric m=1..6]: "
    f"{bool(ok_le or ok_le_num)}")
assert ok_le or ok_le_num

# ---------------------------------------------------------------- Step 2
log()
log("STEP 2 - the banked identity chain, re-derived symbolically (all m)")
disc = sp.expand(sp.discriminant(char_M2, t))
log(f"  disc(char(M^2))        = {disc}   (= m^2(m^2+4): "
    f"{sp.simplify(disc - m**2*(m**2+4)) == 0})")
assert sp.simplify(disc - m ** 2 * (m ** 2 + 4)) == 0
ok2 = sp.simplify(F_m * disc - 16) == 0
log(f"  F(m) * disc(char(M^2)) == 16 exactly:                  {ok2}")
assert ok2

g_WP = 1 / (alpha ** 2 - 4)
g_WP_at = sp.simplify(g_WP.subs(alpha, m ** 2 + 2))
ok3 = sp.simplify(F_m - 16 * g_WP_at) == 0
log(f"  g_WP(m^2+2)            = {g_WP_at}")
log(f"  F(m) == 16 * g_WP(m^2+2) exactly (all m):              {ok3}")
assert ok3

Delta_eig = sp.simplify(Lam - 1 / Lam)
ok4 = sp.simplify(Delta_eig - m * sp.sqrt(m ** 2 + 4)) == 0
ok5 = sp.simplify(F_m - (4 / Delta_eig) ** 2) == 0
log(f"  Delta_eig = Lambda-1/Lambda = {sp.sqrt(sp.factor(Delta_eig**2))}"
    f"   (= m*sqrt(m^2+4): {ok4})")
log(f"  F(m) == (4/Delta_eig)^2:                               {ok5}")
assert ok4 and ok5

log()
log("  numeric spot table (exact rationals):")
log("    m | F(m)=16/(m^2(m^2+4)) | g_WP(m^2+2) | F/g_WP")
for mm in range(1, 7):
    Fv = sp.Rational(16, mm ** 2 * (mm ** 2 + 4))
    gv = sp.Rational(1, (mm ** 2 + 2) ** 2 - 4)
    log(f"    {mm} | {str(Fv):>20} | {str(gv):>11} | {Fv/gv}")
    assert Fv / gv == 16

# ---------------------------------------------------------------- Step 3
log()
log("STEP 3 - THE DISCRIMINATING FACT, part (i): the object is k-FREE")
log(f"  free symbols of F(m):  {F_m.free_symbols}")
dF_dk = sp.diff(F_m, k)
log(f"  dF/dk                  = {dF_dk}   (identically zero: {dF_dk == 0})")
assert dF_dk == 0 and F_m.free_symbols == {m}
# The arc's only k-object (C5): q = exp(2*pi*I/(k+2)) - shares no variable with F.
q_of_k = sp.exp(2 * sp.pi * sp.I * 1 / (k + 2))
shared = F_m.free_symbols & q_of_k.free_symbols
log(f"  quantum-side family q(k) = exp(2*pi*i/(k+2));"
    f" shared variables with F: {shared or 'NONE'}")
assert shared == set()
log("  => the CS level k never enters the one rigorous Fisher object;")
log("     a 'Fisher metric reading ON k' has no computed object to read.")
log("     (k is moreover a DISCRETE level - the arc declares no interpolating")
log("      family p(x|k), so no Fisher form on k was ever constructible from")
log("      declared conventions; the only continuous parameter is I, i.e. m.)")

# ---------------------------------------------------------------- Step 4
log()
log("STEP 4 - part (ii): POSITIVITY (no indefinite/'Lorentzian' direction)")
pos = sp.simplify(sp.Gt(F_m, 0))  # m > 0 declared positive
log(f"  F(m) > 0 for all m > 0:  {pos}")
assert pos == sp.true
log("  => a 1-D positive-definite WP coefficient; nothing indefinite exists")
log("     for the 'emergence' reading (atlas C4) to stand on.")

# ---------------------------------------------------------------- Step 5
log()
log("STEP 5 - part (iii): ZERO content beyond WP (the length element is dLE)")
ratio = sp.simplify(sp.sqrt(F_of_I) / dLE_dI)
log(f"  sqrt(F(I)) / (dLE/dI)  = {ratio}")
assert ratio == 1
log("  => sqrt(F) dI = dLE exactly: the 'information geometry' is the")
log("     translation-length (WP) element restated - one identity, no new")
log("     structure, exactly E21's 'one equation, several costumes'.")

# ---------------------------------------------------------------- Verdict
log()
log("=" * 76)
log("VERDICT INPUT")
log("=" * 76)
log("""
Recomputed, from the arc's own declared conventions:
  F(m) = 16/(m^2(m^2+4)) = 16/disc(char(M^2)) = 16*g_WP(m^2+2) = (4/Delta_eig)^2
holds EXACTLY for all m (symbolic; spot-checked m=1..6), with
  (i)   dF/dk = 0 identically, free_symbols(F) = {m}: the CS level k never
        enters - the 'reading on k' has no object,
  (ii)  F > 0 (positive 1-D WP coefficient - no indefinite direction),
  (iii) sqrt(F) dI = dLE (the metric is the WP/length element itself -
        an elementary chain-rule identity, zero independent content).
The one-hop citation target (archive/PHYSICS_RESONANCES.md) contains no
Fisher computation ('Fisher' occurs 0 times); the only rigorous Fisher fact
in the kill's neighborhood is the collapse identity above (E21(d)/V6).

This upholds the banked kill: the S019 'information-geometry metric reading
on the Chern-Simons level k' was heuristic with no bounded test - the only
bounded test that ever existed collapses to Weil-Petersson on the classical
m-line before k enters.  RECONFIRMED.
""")
log("ALL ASSERTIONS PASSED")

import pathlib
out = pathlib.Path(__file__).with_name("output.txt")
out.write_text("\n".join(lines) + "\n")
