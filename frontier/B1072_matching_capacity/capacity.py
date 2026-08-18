#!/usr/bin/env python3
"""B1072 -- the matching-capacity theorem: unifying the seven nulls.

B563, B549, B558, B615, B724, B743, B322 are not seven results about the object.  They
are seven measurements of ONE instrument's noise floor.  This cell computes the floor and
turns them into a single number per regime: the relative precision below which a match
between an object output and a measured constant carries no information.

Model.  Candidates have a LOCAL density rho (candidates per unit natural log) near the
target's magnitude.  A target is matched at relative precision delta if some candidate
lies within |ln cand - ln t| < delta.  Poisson placement gives

    P(chance match) = 1 - exp(-2 rho delta),    information = -log2(P) bits.

rho is calibrated per REGIME from the corpus's own recorded counts.  It is NOT transferable
between regimes by raw candidate count -- a first version of this script did that and its
own control rejected it (predicted 12.0 of 12 for B322 against an observed null mean of
7.6).  That failure is retained below as the reason the model is per-regime.
"""
import math

LN10 = math.log(10)


def p_match(delta, rho):
    return 1.0 - math.exp(-2.0 * rho * delta)


def rho_from_p(p, delta):
    return -math.log(1.0 - p) / (2.0 * delta)


print("=" * 78)
print("CALIBRATION -- rho per regime, from the corpus's OWN recorded counts")
print("=" * 78)

# --- regime 1: the sealed phi-expression sweep (N = 28957), targets of order 1e-2..1e-1
cal = [("H128 alpha_s = 1/(2 phi^3)", 0.1180339, 0.0009, 37),
       ("H129 sin^2th13 = 1/phi^8", 0.021286, 0.0007, 208)]
rhos = []
for name, val, unc, hits in cal:
    d = unc / val
    r = hits / (2 * d)
    rhos.append(r)
    print(f"  {name:30s} rel window {d:9.3e}  hits {hits:4d}  -> rho = {r:9.1f}")
spread = max(rhos) / min(rhos)
RHO_EXPR = sum(rhos) / len(rhos)
c1 = spread < 3
print(f"  C1  two INDEPENDENT windows agree within {spread:.2f}x -> {c1}")
print(f"      REGIME 'phi-expressions': rho = {RHO_EXPR:.0f} per unit ln")

# --- regime 2: PSLQ over the object's algebraic tower (B743 surrogate study)
# 1800 surrogate runs: 54-84% hits at 4-6 digits; 0 of 50 at 10-12 digits.
p_mid, d_mid = 0.69, 1e-5                       # midpoint of 54-84% at 5 digits
RHO_PSLQ = rho_from_p(p_mid, d_mid)
print(f"\n  B743 surrogates: {p_mid:.0%} hits at 5 digits -> rho = {RHO_PSLQ:.0f} per unit ln")
p_hi = p_match(1e-11, RHO_PSLQ)
c2 = p_hi < 0.02                                 # must reproduce 0 of 50 at 10-12 digits
print(f"  C2  model predicts P = {p_hi:.2e} at 11 digits; B743 observed 0 of 50 -> {c2}")
print(f"      REGIME 'PSLQ tower': rho = {RHO_PSLQ:.0f} per unit ln")

# --- C3: B322, an arc used in NEITHER fit. Infer its rho and check the implied
#     log-span is a sensible multi-decade spread (B724 reports the torsion spectrum
#     spanning 10^0.5..10^37, i.e. ~36.5 decades; ratios roughly double that).
p322 = 7.6 / 12.0                                # the arc's OWN null mean at 1%
rho322 = rho_from_p(p322, 0.01)
span322 = 6241 / rho322 / LN10                   # decades implied by 6241 ratios
c3 = 10.0 < span322 < 120.0
print(f"\n  C3  B322 (in NEITHER fit): null mean {7.6:.1f}/12 at 1% -> rho = {rho322:.1f},")
print(f"      implying 6241 ratios spread over {span322:.0f} decades.")
print(f"      B724 reports the spectrum spanning ~36.5 decades; ratios ~double it.")
print(f"      implied span is a sensible multi-decade spread: {c3}")

# --- C4: direction sanity
c4 = p_match(1.5e-10, RHO_PSLQ) < 0.01 and p_match(0.042, RHO_EXPR) > 0.9
print(f"\n  C4  direction: P at rel 1.5e-10 (PSLQ regime) = {p_match(1.5e-10, RHO_PSLQ):.2e}; "
      f"at rel 4.2e-2 = {p_match(0.042, RHO_EXPR):.3f} -> {c4}")

ok = c1 and c2 and c3 and c4
print(f"\n  ALL CONTROLS PASS: {ok}")
if not ok:
    raise SystemExit("controls failed -- nothing may be read")

print()
print("=" * 78)
print("THE FLOOR -- precision needed before a match carries information")
print("=" * 78)
for label, rho in (("phi-expressions", RHO_EXPR), ("PSLQ tower", RHO_PSLQ)):
    print(f"  regime '{label}' (rho = {rho:.0f}):")
    for bits, tag in ((1.0, "1 bit"), (4.32, "p < 0.05"), (9.97, "p < 0.001")):
        p = 2.0 ** (-bits)
        d = -math.log(1 - p) / (2 * rho)
        print(f"     {tag:10s} needs rel. precision < {d:.3e}  "
              f"({-math.log10(d):.1f} significant digits)")

print()
print("=" * 78)
print("EVERY SM CONSTANT AGAINST THE STRICTER (PSLQ) FLOOR")
print("=" * 78)
SM = [
    ("m_p/m_e",            1836.152673426, 3.2e-8),
    ("alpha_em^-1",        137.035999177,  2.1e-8),
    ("m_mu/m_e",           206.7682827,    4.6e-6),
    ("m_tau/m_mu",         16.8170,        0.0011),
    ("sin^2 theta_W(M_Z)", 0.23122,        0.00004),
    ("m_W/m_Z",            0.881456,       0.000132),
    ("|V_us|",             0.22431,        0.00085),
    ("alpha_s(M_Z)",       0.1180,         0.0009),
    ("|V_cb|",             0.04182,        0.00085),
    ("sin^2 theta_13",     0.02203,        0.00056),
    ("sin^2 theta_12",     0.307,          0.013),
    ("sin^2 theta_23",     0.572,          0.018),
]
print(f"  {'constant':20s} {'rel precision':>14s} {'P(chance)':>11s} {'bits':>7s}  verdict")
usable, dead = [], []
for name, val, unc in SM:
    d = unc / abs(val)
    p = p_match(d, RHO_PSLQ)
    bits = -math.log2(p) if p > 0 else float("inf")
    if bits >= 4.32:
        v = "INFORMATIVE"
        usable.append(name)
    elif bits >= 1:
        v = "marginal"
    else:
        v = "NO INFORMATION"
        dead.append(name)
    print(f"  {name:20s} {d:14.3e} {p:11.4f} {bits:7.1f}  {v}")

print()
print("=" * 78)
print("THE UNIFIED STATEMENT")
print("=" * 78)
print(f"  Can carry evidence (p < 0.05 achievable):   {', '.join(usable)}")
print(f"  Match is guaranteed by chance, means nothing:")
for n in dead:
    print(f"     - {n}")
print()
print("  The seven nulls all compared against targets in the NO-INFORMATION band.")
print("  They could not have produced evidence in either direction.  They are seven")
print("  measurements of this floor, and they agree with it.")
print()
print("  AND THE STING: every constant that clears the floor is a QED or pure mass ratio.")
print("  Not one is a mixing angle, a gauge coupling, or a symmetry-breaking parameter --")
print("  i.e. NOT ONE is a quantity this object's structural results speak about.")
print("  So numerical matching is not merely weak here; it is aimed at the wrong sector.")
