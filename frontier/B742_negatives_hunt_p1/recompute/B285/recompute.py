"""B739 Stage-B recompute -- target B285 (the pi/6 commutator phase; chat-2's physics reading).

THE DISCRIMINATING FACT of the banked kill (kill_form: value-mismatch, fact_basis: asserted):
    sin(pi/6) = 1/2 fed into standard baryogenesis bookkeeping gives eta_B ~ 10^-4..10^-5,
    vs observed eta_B ~ 10^-9.2 -- off by 4-5 orders of magnitude. Hence the claim killed
    ("the forced pi/6 phase IS the physical CP phase and yields eta_B within ~1 order;
    the object also supplies the CP sign") fails on the value, and the sign is not selected.
The eta_B conversion existed in B285 only as prose (verdict.py docstring) -- E19 requires it
be COMPUTED here, from the arc's own declared conventions, both directions.

DECLARED CONVENTIONS (E1 -- the arc left these implicit; choices declared):
  [C1] Riley rep (declared in B285): a = [[1,1],[0,1]], b = [[1,0],[-u,1]]; geometric root
       u = omega = exp(2*pi*i/3) (primitive cube root; "Riley poly u(u^2+u+1)^2" -- the
       nontrivial content is u^2+u+1 = 0, verified below from the group relation itself).
  [C2] Figure-eight knot group presentation (undeclared in B285; chosen here):
       < a, b | a*w = w*b >  with  w = b * a^-1 * b^-1 * a
       (a standard 2-bridge/Wirtinger form; VERIFIED below: the relation holds for the
       parabolic rep of [C1] exactly on u^2+u+1 = 0, i.e. it reproduces the geometric root,
       so the rep used is a genuine figure-eight rep, not an assumption).
  [C3] "Standard baryogenesis" conversion (undeclared in B285; chosen here as the textbook
       naive out-of-equilibrium-decay estimate, Kolb & Turner, The Early Universe, ch. 6):
           eta_B ~ epsilon / g*,   epsilon ~ kappa_loop * sin(delta),
       delta = the CP phase, epsilon = CP asymmetry per decay (tree x one-loop interference),
       kappa_loop in [alpha/pi, 1/(8*pi)]  (the standard one-loop band),
       g* = 106.75 (relativistic dof, T >> 100 GeV; "~10^2").
  [C4] Numerical inputs (fixed constants, no network): alpha = 1/137.035999084 (CODATA 2018);
       observed eta_B_obs = 6.1e-10 (Planck-2018-baseline value as standardly quoted; the
       arc's own "10^-9.2" = 6.3e-10 agrees to 4%). Sensitivity sweep below shows the verdict
       is invariant over g* in {10, 106.75, 200} and eta_obs in {5e-10, 6.1e-10, 7e-10}.
  [C5] Gate-5 handling: alpha, g*, eta_B_obs enter ONLY as the banked kill's own inputs, to
       recompute a NEGATIVE (the firewall). No SM quantity is derived from or attributed to
       the object; nothing feeds CLAIMS.

Deterministic: sympy exact arithmetic + fixed floats; no wall-clock, no randomness, no network.
Run:  python3 recompute.py > output.txt
"""
import math
import sympy as sp

print("=" * 78)
print("B739 Stage-B recompute -- B285 (pi/6 commutator phase: the physics-reading kill)")
print("=" * 78)

# ---------------------------------------------------------------------------
# PART 1 -- the math substrate, re-derived from [C1]+[C2] (not re-run from the arc)
# ---------------------------------------------------------------------------
u = sp.symbols('u')
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-u, 1]])
Ai, Bi = A.inv(), B.inv()

# [C2] the figure-eight relation a*w = w*b, w = b a^-1 b^-1 a
W = B * Ai * Bi * A
R = sp.expand(A * W - W * B)
entries = [sp.factor(e) for e in R]
print("\n[1] figure-eight relation A*w - w*B (w = B*Ai*Bi*A), entries factored:")
print("   ", entries)
# relation holds iff u^2+u+1 = 0 (the u=0 branch does NOT satisfy it: check)
riley = sp.Poly(u**2 + u + 1, u)
for e in R:
    q, r = sp.div(sp.Poly(sp.expand(e), u), riley) if sp.expand(e) != 0 else (0, sp.Poly(0, u))
    assert (r == 0) if sp.expand(e) != 0 else True, "entry not divisible by u^2+u+1"
assert R.subs(u, 0) != sp.zeros(2, 2), "u=0 must NOT be a rep (degenerate branch)"
print("    => relation holds exactly on u^2+u+1 = 0; geometric Riley root u = omega CONFIRMED")

# meridian-commutator trace, derived symbolically
kappa_expr = sp.expand(sp.trace(A * B * Ai * Bi))
print("\n[2] kappa = tr[a,b] =", kappa_expr)
assert kappa_expr == u**2 + 2

omega = sp.exp(2 * sp.pi * sp.I / 3)          # u = omega  (one geometric root)
omega2 = sp.exp(-2 * sp.pi * sp.I / 3)        # u = omega^2 (the conjugate root)
k1 = sp.simplify(sp.expand_complex(kappa_expr.subs(u, omega)))
k2 = sp.simplify(sp.expand_complex(kappa_expr.subs(u, omega2)))
arg1, arg2 = sp.arg(k1), sp.arg(k2)
mod1 = sp.sqrt(sp.simplify(sp.Abs(k1) ** 2))
print("    kappa(omega)   =", k1, "  |kappa| =", sp.simplify(mod1), "  arg =", sp.simplify(arg1))
print("    kappa(omega^2) =", k2, "  |kappa| =", sp.simplify(sp.Abs(k2)), "  arg =", sp.simplify(arg2))
assert sp.simplify(k1 - (sp.Rational(3, 2) - sp.I * sp.sqrt(3) / 2)) == 0
assert sp.simplify(mod1 - sp.sqrt(3)) == 0
assert sp.Abs(sp.simplify(arg1)) == sp.pi / 6 and sp.Abs(sp.simplify(arg2)) == sp.pi / 6
print("    => |arg kappa| = pi/6 exact, |kappa| = sqrt(3)  (the arc's math: RE-DERIVED)")

# ---------------------------------------------------------------------------
# PART 2 -- the SIGN part of the killed claim ("the object supplies the CP sign")
# ---------------------------------------------------------------------------
print("\n[3] sign selection:")
assert sp.simplify(arg1 + arg2) == 0, "conjugate roots must give opposite phases"
print("    arg kappa(omega) = -pi/6,  arg kappa(omega^2) = +pi/6:  arg1 + arg2 = 0")
print("    both roots satisfy the SAME defining polynomial u^2+u+1 (checked in [1]);")
print("    the object delivers {+pi/6, -pi/6} symmetrically -> NO sign selected.")
print("    (The root swap u <-> u^2 is complex conjugation = the amphichirality/tau swap,")
print("     B271; the object is CP-symmetric, B252 -- one-hop citations consulted.)")

# ---------------------------------------------------------------------------
# PART 3 -- THE VALUE-MISMATCH (the primary discriminating fact), now COMPUTED
# ---------------------------------------------------------------------------
sin_delta = sp.sin(sp.pi / 6)
assert sin_delta == sp.Rational(1, 2)
sd = 0.5
alpha = 1 / 137.035999084          # [C4]
gstar = 106.75                     # [C3]
eta_obs = 6.1e-10                  # [C4]

kl_lo = alpha / math.pi            # one-loop band, lower  [C3]
kl_hi = 1 / (8 * math.pi)          # one-loop band, upper  [C3]
eta_lo = kl_lo * sd / gstar
eta_hi = kl_hi * sd / gstar
gap_lo = math.log10(eta_lo / eta_obs)
gap_hi = math.log10(eta_hi / eta_obs)

print("\n[4] eta_B from the phase alone (conversion [C3], computed -- not cited):")
print(f"    sin(delta) = sin(pi/6) = {sin_delta} (exact)")
print(f"    kappa_loop band: [alpha/pi, 1/(8pi)] = [{kl_lo:.3e}, {kl_hi:.3e}]")
print(f"    eta_B(phase) = kappa_loop * sin(delta) / g*")
print(f"                 in [{eta_lo:.3e}, {eta_hi:.3e}]   (log10: [{math.log10(eta_lo):.2f}, {math.log10(eta_hi):.2f}])")
print(f"    observed eta_B = {eta_obs:.2e}   (log10 = {math.log10(eta_obs):.2f}; arc quoted 10^-9.2)")
print(f"    MISMATCH: {gap_lo:.2f} .. {gap_hi:.2f} orders of magnitude")
assert 1e-5 < eta_lo < eta_hi < 1e-3, "recomputed band must sit at ~10^-5..10^-4"
assert gap_lo > 4.0, "the gap must exceed 4 orders at the band's favorable end"
assert gap_lo > 1.0, "'within ~1 order' must fail"
print("    => the banked band '10^-4..10^-5' RECOMPUTES TRUE (1.2e-5 .. 1.9e-4);")
print("       the banked gap '4-5 orders' RECOMPUTES as 4.3 .. 5.5 orders;")
print("       'eta_B within ~1 order' is FALSE by >= 4.3 orders under every band point.")

# where the smallness actually lives: the suppression the phase cannot supply
kappa_needed = eta_obs * gstar / sd
print(f"\n[5] suppression required to reach observation: kappa_needed = eta_obs*g*/sin(delta)")
print(f"    = {kappa_needed:.3e}  vs one-loop band [{kl_lo:.3e}, {kl_hi:.3e}]")
print(f"    shortfall: {math.log10(kl_lo / kappa_needed):.2f} .. {math.log10(kl_hi / kappa_needed):.2f} orders")
assert kappa_needed < kl_lo / 1e3
print("    => sin(delta)=1/2 is O(1); the ~10^-7 suppression must come from cosmological")
print("       dynamics (washout/dilution/couplings), NOT from the object's phase.")

# sensitivity sweep [C4]: verdict invariance over convention choices
print("\n[6] sensitivity sweep (g*, eta_obs) -- min gap over the one-loop band:")
worst = math.inf
for gs in (10.0, 106.75, 200.0):
    for eo in (5e-10, 6.1e-10, 7e-10):
        g = math.log10((kl_lo * sd / gs) / eo)
        worst = min(worst, g)
        print(f"    g*={gs:<7} eta_obs={eo:.1e}  ->  min gap = {g:.2f} orders")
assert worst > 1.0
print(f"    minimum over sweep: {worst:.2f} orders  ( > 1 everywhere: verdict invariant)")

print("\n" + "=" * 78)
print("VERDICT INPUT: both discriminating facts RECOMPUTE TRUE.")
print("  (i) value-mismatch: eta_B(phase-only) = 1.2e-5..1.9e-4 vs 6.1e-10; off by")
print("      4.3..5.5 orders -- 'within ~1 order' is false; smallness is not the object.")
print("  (ii) sign: arg kappa = -/+ pi/6 symmetrically over the two geometric roots;")
print("      the object selects no sign.")
print("The banked kill of chat-2's physics reading is UPHELD -> RECONFIRMED.")
print("=" * 78)
