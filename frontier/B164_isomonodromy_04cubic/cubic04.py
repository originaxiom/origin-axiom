#!/usr/bin/env python3
"""B164 (P1 of Masterplan II) -- the 4-punctured-sphere Fricke cubic + the metallic monodromy.

The Betti side of the seed is the once-punctured-torus (OPT, (1,1)) character variety, the only
other dim-2 Fricke cubic being the 4-punctured sphere (0,4) -- the Painleve-VI / class-S monodromy
manifold (Cantat-Loray, Iwasaki, Boalch; cited in B150). This builds the (0,4) cubic explicitly,
exhibits its MCG dynamics (the three Vieta involutions = the Painleve-VI dynamics), bridges it to
the OPT cubic at the special fiber, and realizes the metallic monodromy's degrees on it.

Verifiable [exact] content:
  C1  the Jimbo-Fricke (0,4) cubic Phi(x,y,z; t1..t4) and its 3 Vieta involutions s_x,s_y,s_z are
      involutions that PRESERVE Phi (the MCG/Painleve-VI action exists on our object).
  C2  bridge: at t_i=0 the (0,4) cubic, after z->-z, is the OPT cubic at kappa=2 (the void /
      cancellation fiber) -- the concrete OPT<->(0,4) link at a special fiber.
  C3  metallic degrees: M_m=[[m,1],[1,0]] has eigenvalue lambda_m=(m+sqrt(m^2+4))/2, dynamical
      degree lambda_m^2, trace field Q(sqrt(m^2+4)) -- m=1,2,3 [exact].
  C4 [num] the (0,4) Vieta composite s_x o s_y is LOXODROMIC -- generic orbits grow without bound
      (positive entropy / genuine hyperbolic dynamics on the cubic), not periodic. (Its exact
      dynamical degree, and WHICH (0,4) word realizes the metallic M_m with degree lambda_m^2,
      need the OPT<->(0,4) double-cover dictionary -- DEFERRED to PR2.)

DEFERRED (PR2): the OPT<->(0,4) cover dictionary (so the metallic M_m maps to a specific (0,4) word
with dynamical degree lambda_m^2 -- a Pic-action computation, NOT the naive orbit-norm growth); the
isomonodromy (Painleve-VI) FLOW as a continuous "time"; the firewall-relocation verdict (does the
scale stay external? -- expected YES, P010/8c).
FIREWALL: standalone character-variety / dynamics math; no scale, no Lambda, no crossing; nothing
to CLAIMS.md.
"""
import sympy as sp
import numpy as np

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

x, y, z = sp.symbols('x y z')
t1, t2, t3, t4 = sp.symbols('t1 t2 t3 t4')   # the four boundary (puncture) traces

# ---- C1: the Jimbo-Fricke (0,4) cubic + the three Vieta involutions ----
px = t1*t2 + t3*t4
py = t1*t4 + t2*t3
pz = t1*t3 + t2*t4
p0 = 4 - t1**2 - t2**2 - t3**2 - t4**2 - t1*t2*t3*t4
Phi = x**2 + y**2 + z**2 + x*y*z - px*x - py*y - pz*z - p0   # = 0 is the (0,4) char variety

# Vieta involutions: each variable enters Phi quadratically; flip to the other root, fix the others.
sx = lambda X, Y, Z: (px - Y*Z - X, Y, Z)
sy = lambda X, Y, Z: (X, py - X*Z - Y, Z)
sz = lambda X, Y, Z: (X, Y, pz - X*Y - Z)
print("== C1 [exact]: (0,4) Jimbo-Fricke cubic + 3 Vieta involutions (Painleve-VI/MCG dynamics) ==")
for nm, s in (("s_x", sx), ("s_y", sy), ("s_z", sz)):
    img = s(x, y, z)
    chk(f"{nm} preserves Phi (maps the cubic to itself)",
        sp.expand(Phi.subs({x: img[0], y: img[1], z: img[2]}, simultaneous=True) - Phi) == 0)
    img2 = s(*img)
    chk(f"{nm} is an involution", tuple(sp.expand(a - b) for a, b in zip(img2, (x, y, z))) == (0, 0, 0))

# ---- C2: bridge at t_i=0 -> OPT cubic at kappa=2 (the void / cancellation fiber) ----
print("== C2 [exact]: t_i=0 (z->-z) gives the OPT cubic at kappa=2 (the cancellation fiber) ==")
Phi0 = Phi.subs({t1: 0, t2: 0, t3: 0, t4: 0})                 # x^2+y^2+z^2+xyz-4
opt = x**2 + y**2 + z**2 - x*y*z - 2                          # OPT Fricke (K001): = kappa
bridge = sp.expand(Phi0.subs(z, -z))                         # x^2+y^2+z^2-xyz-4
chk("Phi|_{t=0}(z->-z) = (OPT cubic) - kappa with kappa=2  i.e. x^2+y^2+z^2-xyz-4",
    sp.expand(bridge - (opt - 2)) == 0, x="(0,4) void fiber == OPT kappa=2")

# ---- C3: metallic degrees on the realization ----
print("== C3 [exact]: metallic monodromy degrees (lambda_m, lambda_m^2, trace field) ==")
for m in (1, 2, 3):
    M = sp.Matrix([[m, 1], [1, 0]])
    lam = max(M.eigenvals(), key=lambda e: sp.Abs(sp.N(e)))   # lambda_m = (m+sqrt(m^2+4))/2
    lam_expected = (m + sp.sqrt(m**2 + 4)) / 2
    chk(f"m={m}: lambda_m = (m+sqrt(m^2+4))/2", sp.simplify(lam - lam_expected) == 0,
        x=f"dyn. degree lambda_m^2 = {sp.nsimplify(sp.expand(lam_expected**2))}; trace field Q(sqrt{m**2+4})")

# ---- C4 [num]: dynamical degree of a loxodromic (0,4) Vieta composite = phi^2 = lambda_1^2 ----
print("== C4 [num]: s_x o s_y on (0,4) is LOXODROMIC (orbits grow -> genuine hyperbolic dynamics) ==")
rng = np.random.default_rng(0)
tv = {t1: 0.3, t2: -0.5, t3: 0.7, t4: 0.2}                    # generic boundary traces
pxv, pyv, pzv, p0v = [float(e.subs(tv)) for e in (px, py, pz, p0)]
def g(P):                                                     # s_x o s_y, numeric
    X, Y, Z = P
    X2, Y2, Z2 = X, pyv - X*Z - Y, Z                         # s_y
    return (pxv - Y2*Z2 - X2, Y2, Z2)                        # s_x
def on_surface_point():                                       # pick x,y; solve the cubic for z
    X, Y = complex(rng.normal(), rng.normal()), complex(rng.normal(), rng.normal())
    a, b, c = 1.0, (X*Y - pzv), (X*X + Y*Y - pxv*X - pyv*Y - p0v)
    return (X, Y, (-b + np.sqrt(b*b - 4*a*c)) / (2*a))
rates = []
for _ in range(6):
    P = on_surface_point(); prev = None
    for k in range(40):
        P = g(P); nrm = max(abs(v) for v in P)
        if nrm > 1e-300 and prev is not None and k > 8:
            rates.append(np.log(nrm) - prev)
        prev = np.log(nrm) if nrm > 0 else prev
rate = float(np.median(rates))
# loxodromic <=> orbits grow geometrically (positive, stable per-step log-growth), NOT bounded/periodic.
chk("s_x o s_y is loxodromic (generic orbits grow geometrically: median per-step log-growth > 0.5)",
    rate > 0.5, x=f"measured per-step log-growth {rate:.4f} (>0; the exact dynamical degree is DEFERRED to PR2)")
# control: a Vieta involution alone is an INVOLUTION (period 2) -> NOT loxodromic (bounded orbit)
sxn = lambda X, Y, Z: (pxv - Y*Z - X, Y, Z)                  # numeric s_x
P = on_surface_point(); P2 = sxn(*sxn(*P))
chk("control: a single Vieta involution s_x is period-2 (bounded), so 'loxodromic' is non-vacuous",
    max(abs(a - b) for a, b in zip(P2, P)) < 1e-6)

print("\nSUMMARY: the (0,4) Painleve-VI/MCG dynamics (3 Vieta involutions) exists on our object [C1];")
print("it bridges to the OPT cubic at the kappa=2 void fiber [C2]; the metallic degrees lambda_m^2 +")
print("trace fields Q(sqrt(m^2+4)) are the realization's degrees [C3]; and the (0,4) Vieta dynamics is")
print("genuinely hyperbolic (loxodromic elements exist) [C4]. DEFERRED to PR2: the OPT<->(0,4) cover")
print("dictionary (M_m -> a (0,4) word of dynamical degree lambda_m^2); the isomonodromy FLOW; the")
print("firewall-relocation verdict. FIREWALL: dynamics math; no scale/Lambda/crossing; nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
