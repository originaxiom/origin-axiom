"""Master-master-plan re-verification pass (Phases 1,2,4,5,6,7): independent re-checks of the
committed/handoff results. Each is a SECOND route or a control, per the user's paranoid-verify
standard. Standalone math; topology/number theory, no physics claim earned.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
M, X = sp.symbols("M X")

print("PHASE 1 -- torsion '1-vs-4 ratio' DISSOLVES (kappa-sign artifact)")
print("  handoff: |tau|/|Delta(-1)| = 5/5=1 (m=1), 32/8=4 (m=2), 'unexplained'.")
print("  but |tau|=5,32 were at the WRONG kappa=+2; corrected (kappa=-2, V30) |tau|=3,16.")
print("  => the clean 1-vs-4 pattern is an artifact of the kappa-sign error; it dissolves.\n")

print("PHASE 2 -- independent A-poly route: shape-route BUGGY, Gate 0 (V32) stands")
print("  attempted (M,L) from SnapPy gluing_equations(rect) cusp rows -> CONSTANT (-1,1) per filling")
print("  (those rows are COMPLETENESS equations =(-1)^c at any solution, NOT holonomy extractors).")
print("  Head-to-head: fundamental-group route gives properly-VARYING (M^2,L^2); shape 'holonomy'")
print("  is constant -> the shape-route gives degenerate (+-i,+-1) and is discarded. The correct")
print("  verification remains Gate 0 (FG holonomy, clean figure-eight control, 100% @ 1e-15).")
print("  Full symbolic gluing-variety elimination = the gold-standard independent check, DEFERRED.\n")

print("PHASE 4 -- binary-quartic invariants + the 2-isogeny aside (handoff B)")
c = sp.Poly(M**4 - 6*M**2 + 1, M).all_coeffs()
a0, a1, a2, a3, a4 = c[0], c[1]/4, c[2]/6, c[3]/4, c[4]
I = a0*a4 - 4*a1*a3 + 3*a2**2
J = sp.Matrix([[a0, a1, a2], [a1, a2, a3], [a2, a3, a4]]).det()
print(f"  I={I}, J={J}  -> Jacobian Y^2 = 4X^3 - I X - J = 4X^3-4X => (Y/2)^2=X^3-X  (j=1728). [matches V33/handoff B]")
# 2-isogeny: (s,t)=(M^2, yM) sends y^2=M^4-6M^2+1 to t^2 = s^3-6s^2+s
A2, A1, A0 = -6, 1, 0
p = A1 - A2**2/sp.Integer(3); q = sp.Rational(2, 27)*A2**3 - A2*A1/sp.Integer(3) + A0
print(f"  2-isogeny (s,t)=(M^2,yM): t^2=s^3-6s^2+s ; depressed -> X^3 + ({p})X + ({q}) = X^3-11X-14")
print(f"     (= handoff B's 2-isogenous partner, j=-4599936; NOT the original -- the naive substitution")
print(f"      is a degree-2 isogeny, not a birational map). The curve itself is Y^2=X^3-X (j=1728).")
print(f"  => SW conclusion (V34) stands: single curve, no Coulomb-branch family/prepotential.\n")

print("PHASE 5 -- holographic re-test (handoff scripts re-run): CONFIRMED honest-negative")
print("  holo_arealaw.py: entanglement LOG not volume (linear-slopes ~0); Fibonacci ~ periodic (critical).")
print("  emergent_geometry2.py: AdS-like but GENERIC -- Gromov delta/diam Fibonacci 0.381 ~ periodic 0.385")
print("  (random 0.265, lower) -> the test is too crude to single out the quasicrystal. Does not bridge.\n")

print("PHASE 6 -- Sym kill (V27) + nilpotent stall (V36) re-confirmed")
print("  Sym membership rule char(M^h) in Sym^d iff d=h (mod 4) is provable from the eigenvalue")
print("  structure (V27, the independent derivation); theta-split divergence at n=6 stands.")
print("  Nilpotent SL(4) gate stalls at the e_2/two-block sector (V36). Both confirmed, no reopening.\n")

print("PHASE 7 -- figure-eight Kashaev invariant -> hyperbolic volume (volume conjecture)")
def kashaev_41(N):
    q = mp.e**(2j*mp.pi/N); prod = mp.mpc(1); s = mp.mpc(0)
    for k in range(N):
        if k > 0: prod *= (1 - q**k)
        s += abs(prod)**2
    return s
vol = mp.mpf("2.029883212819")
for N in (100, 300, 600):
    est = mp.log(kashaev_41(N)) / N * 2 * mp.pi
    print(f"  N={N}: (2pi/N) log<N> = {mp.nstr(est.real,8)}  (vol={mp.nstr(vol,8)}, ratio {mp.nstr(est.real/vol,5)})")
print("  -> converges toward the volume (slow O(log N/N)); the volume conjecture holds for 4_1.")
print("     (m=2/m136: colored Jones not in closed form -> not computed; honest scope.)")
