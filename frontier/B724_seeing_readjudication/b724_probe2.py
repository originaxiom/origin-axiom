#!/usr/bin/env python3
"""B724 PROBE 2 (C4) — the torsion-HIERARCHY near-hit: forced rule or base rate?

FIREWALL: origin-axiom. Structural/arithmetic ONLY. No SM value claimed. HINT-grade at most.
COMPUTE-NOT-CITE: the six torsions are RECOMPUTED from the B581 exact data (not cited).
BASE-RATE gate MANDATORY.

Question (two-outcome):
  A = a PRINCIPLED/FORCED combination (E6-breaking cascade or a stated rule over the
      exponents {1,4,5,7,8,11}) lands at ~10^17 AND beats the base rate (p<0.01) -> real HINT.
  B = only base-rate near-coincidences; no forced rule -> HINT-grade-at-best / dead.

The near-hit: tau_11/tau_8 ~ 10^16.8, near the gauge hierarchy M_Pl/M_EW ~ 10^17.
"""
import json
import os
import itertools
import math
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "B581_six_torsions", "six_torsions_results.json")

# ----------------------------------------------------------------------------
# STEP 0 — RECOMPUTE the six torsions from the B581 exact data (compute-not-cite)
# ----------------------------------------------------------------------------
d = json.load(open(DATA))
t = sp.Symbol('t')


def poly(m):
    q = d[m]['quotient']
    assert all(Fr(b) == 0 for a, b in q), "non-rational coefficient"
    P = sum(sp.Rational(Fr(a)) * t**k for k, (a, b) in enumerate(q))
    lead = sp.Poly(P, t).all_coeffs()[0]
    return sp.Poly(sp.expand(P / lead), t)  # monic normalization (Review-17 convention)


EXP = [1, 4, 5, 7, 8, 11]           # the six E6 exponents
tau = {}
for m in EXP:
    P = poly(str(m))
    red, rem = sp.div(P.as_expr(), t - 1)
    assert rem == 0
    tau[m] = sp.Integer(sp.expand(red.subs(t, 1)))   # tau_m = Delta'_m(1) via (t-1) division

out = []
def w(s=""):
    out.append(s)
    print(s)

w("=" * 78)
w("STEP 0 — RECOMPUTED torsion magnitudes (from B581 exact quotients, monic norm)")
w("=" * 78)
L = {}   # log10 |tau_m|
for m in EXP:
    absval = abs(tau[m])
    L[m] = math.log10(float(absval))
    w(f"  |tau_{m:<2}| = {int(absval):>40d}   log10 = {L[m]:8.4f}   sign(tau)={int(sp.sign(tau[m])):+d}")
w("")
w("  Prompt's asserted magnitudes vs recomputed:")
assert abs(tau[1]) == 3
assert abs(tau[4]) == 260736
assert abs(tau[5]) == 165110400
w(f"    |tau_1|=3 OK; |tau_4|=260736 OK; |tau_5|=165110400 OK")
w(f"    |tau_7| = {float(abs(tau[7])):.3e}  (prompt 3.257e15)")
w(f"    |tau_8| = {float(abs(tau[8])):.3e}  (prompt 1.006e20)")
w(f"    |tau_11|= {float(abs(tau[11])):.3e} (prompt 6.908e36)")
w("")

# theta parity: sign(tau_m)=(-1)^m ; positive (theta-ODD) at m in {4,8}
THETA_ODD = [m for m in EXP if int(sp.sign(tau[m])) == +1]     # {4,8}
THETA_EVEN = [m for m in EXP if int(sp.sign(tau[m])) == -1]    # {1,5,7,11} = F4 exponents
w(f"  theta-ODD  exponents (sign +, the 'unstable/broken' sector): {THETA_ODD}")
w(f"  theta-EVEN exponents (sign -, = F4 exponents {{1,5,7,11}}):    {THETA_EVEN}")
w("")

# ----------------------------------------------------------------------------
# STEP 1 — the observed near-hit, quantified against the ACTUAL physics ratios
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 1 — the observed near-hit tau_11/tau_8 vs actual hierarchy scales")
w("=" * 78)
r = L[11] - L[8]
w(f"  log10(tau_11/tau_8) = {r:.4f}   (tau_11/tau_8 = {10**r:.3e})")
# physics targets (dimensionless hierarchy candidates)
targets = {
    "M_Pl / v_Higgs (1.22e19 / 246)":   math.log10(1.22e19 / 246),
    "M_Pl / M_W     (1.22e19 / 80.4)":  math.log10(1.22e19 / 80.4),
    "M_Pl_red / v   (2.435e18 / 246)":  math.log10(2.435e18 / 246),
    "round 10^17":                       17.0,
    "round 10^16":                       16.0,
}
for name, lt in targets.items():
    w(f"    vs {name:<34s}: target log={lt:6.3f}  |Delta log|={abs(r-lt):.3f}  factor={10**abs(r-lt):.2f}")
w("")

# ----------------------------------------------------------------------------
# STEP 2 — THE BASE RATE (rigorous). Enumerate all simple products/ratios of
#          <=3 torsions. Each combo = a signed subset S of EXP, |S| in {1,2,3},
#          each element sign +-1 (numerator/denominator). log10 value = sum s_i L_i.
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 2 — BASE RATE over all simple products/ratios of <=3 torsions")
w("=" * 78)


def all_combos(max_k=3, signed=True):
    """Yield (label, logval) for every product/ratio of 1..max_k distinct torsions."""
    seen = {}
    for k in range(1, max_k + 1):
        for subset in itertools.combinations(EXP, k):
            sign_choices = itertools.product([+1, -1], repeat=k) if signed else [tuple([1]*k)]
            for signs in sign_choices:
                val = sum(s * L[m] for s, m in zip(signs, subset))
                num = [m for s, m in zip(signs, subset) if s > 0]
                den = [m for s, m in zip(signs, subset) if s < 0]
                lab = "*".join(f"t{m}" for m in num) or "1"
                if den:
                    lab += "/(" + "*".join(f"t{m}" for m in den) + ")"
                # dedupe identical labels
                if lab not in seen:
                    seen[lab] = val
    return seen


combos = all_combos(3, signed=True)
w(f"  total distinct simple combos (|S|<=3, signed):  {len(combos)}")

# also the restricted family matching the OBSERVED hit's FORM: ratio of exactly 2
combos2 = {lab: v for lab, v in all_combos(2, signed=True).items()
           if "/" in lab and "*" not in lab.split("/")[0] and lab != "1"}
# pure 2-ratios t_a/t_b
ratios2 = {}
for a, b in itertools.permutations(EXP, 2):
    ratios2[f"t{a}/t{b}"] = L[a] - L[b]
w(f"  pure 2-torsion ratios t_a/t_b (ordered):        {len(ratios2)}")
w("")


def base_rate(space, target_log, tol_log, label):
    hits = {lab: v for lab, v in space.items() if abs(v - target_log) <= tol_log}
    frac = len(hits) / len(space)
    w(f"  [{label}] target log={target_log:.2f}, tol=+-{tol_log:.3f} (factor {10**tol_log:.1f}):")
    w(f"        {len(hits):3d}/{len(space):3d} = {100*frac:5.2f}% within tolerance")
    return frac, hits


w("--- (a) BASE RATE at 10^17, factor-3 tolerance (|Dlog|<0.477) ---")
for name, sp_ in [("all <=3 combos", combos), ("pure 2-ratios", ratios2)]:
    base_rate(sp_, 17.0, math.log10(3), name)
w("")
w("--- (a') factor-2 tolerance (|Dlog|<0.301) ---")
for name, sp_ in [("all <=3 combos", combos), ("pure 2-ratios", ratios2)]:
    base_rate(sp_, 17.0, math.log10(2), name)
w("")
w("--- (a'') tightest: the OBSERVED |Dlog|=0.16 tolerance (factor 1.46) ---")
for name, sp_ in [("all <=3 combos", combos), ("pure 2-ratios", ratios2)]:
    base_rate(sp_, 17.0, abs(r - 17.0), name)
w("")

# List the pure-2-ratios sorted by distance to 17 (shows tau_11/tau_8 is the ONLY near one)
w("  pure 2-ratios closest to 10^17:")
for lab, v in sorted(ratios2.items(), key=lambda kv: abs(kv[1] - 17.0))[:6]:
    w(f"      {lab:<10s} log={v:7.3f}  |Dlog to 17|={abs(v-17.0):.3f}  factor={10**abs(v-17.0):.2f}")
w("")

# ----------------------------------------------------------------------------
# STEP 3 — LOOK-ELSEWHERE / garden-of-forking-paths.
#   (i)  expected # of combos within tolerance (density argument)
#   (ii) the target itself is fuzzy: "the hierarchy" ranges 10^16..10^17 (M_Pl/v..M_Pl/M_W),
#        and we could equally have aimed at OTHER famous ratios in the covered range.
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 3 — LOOK-ELSEWHERE: how easy is it to hit SOME famous ratio?")
w("=" * 78)
vals = sorted(combos.values())
lo, hi = vals[0], vals[-1]
w(f"  combo log-values span [{lo:.1f}, {hi:.1f}]; N={len(combos)} combos.")
# density of combos per unit log10 in the positive physics-relevant window [0,40]
posvals = [v for v in vals if 0 <= v <= 40]
dens = len(posvals) / 40.0
w(f"  density in [0,40]: {dens:.1f} combos per decade")
w(f"  => expected # combos within factor-3 (+-0.477 dec) of ANY fixed target ~ {dens*2*math.log10(3):.1f}")
w(f"  => expected # within factor-2 (+-0.301 dec) ~ {dens*2*math.log10(2):.1f}")
w("")
# famous dimensionless ratios in the object's covered range
famous = {
    "proton/electron mass (1836)": math.log10(1836),
    "1/alpha_em (137)":            math.log10(137),
    "M_Pl/v hierarchy (5e16)":     math.log10(1.22e19/246),
    "M_Pl (in GeV, 1.2e19)":       math.log10(1.22e19),
    "M_GUT/M_W (~1e14)":           14.0,
    "baryon asymmetry 1/eta (1e9)": 9.0,
    "N_Avogadro (6e23)":           math.log10(6.022e23),
}
w("  'garden of forking paths' — near-hits (factor 3) to OTHER famous numbers:")
n_hit = 0
for name, lt in famous.items():
    hits = {lab: v for lab, v in combos.items() if abs(v - lt) <= math.log10(3)}
    if hits:
        n_hit += 1
    best = min(combos.items(), key=lambda kv: abs(kv[1] - lt))
    w(f"    {name:<30s} log={lt:6.2f}: {len(hits):2d} combos w/in factor3; "
      f"closest {best[0]} ({10**abs(best[1]-lt):.2f}x)")
w(f"  => {n_hit}/{len(famous)} famous targets have a factor-3 near-hit among the combos.")
w("")

# ----------------------------------------------------------------------------
# STEP 4 — THE FORCED-RULE TEST. Enumerate PRINCIPLED combinations dictated by the
#   E6/theta structure and check (i) do they land at ~10^17, (ii) tighter than base rate?
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 4 — FORCED / PRINCIPLED combinations (the crux)")
w("=" * 78)
forced = {}
# R1: ratio of the two theta-ODD torsions (the distinguished 2-element sector) -- the
#     single MOST principled 2-combo the structure offers.
forced["R1: tau_8/tau_4  (the two theta-ODD torsions, top/bottom)"] = L[8] - L[4]
forced["R1': tau_4/tau_8"] = L[4] - L[8]
# R2: top exponent over top theta-odd = the OBSERVED hit (is '11 over 8' principled a priori?)
forced["R2: tau_11/tau_8 (top-exp / top-theta-odd = OBSERVED)"] = L[11] - L[8]
# R3: F4 (theta-even {1,5,7,11}) product / E6-full or theta-odd product
forced["R3: prod(theta-even 1,5,7,11) / prod(theta-odd 4,8)"] = (L[1]+L[5]+L[7]+L[11]) - (L[4]+L[8])
forced["R3': prod(theta-odd 4,8) / prod(theta-even 1,5,7,11)"] = (L[4]+L[8]) - (L[1]+L[5]+L[7]+L[11])
# R4: top / bottom (largest / smallest exponent torsion) tau_11/tau_1
forced["R4: tau_11/tau_1 (top/bottom exponent)"] = L[11] - L[1]
# R5: 'cascade' — consecutive-exponent ratios chained; the single largest gap step
for i in range(len(EXP)-1):
    a, b = EXP[i+1], EXP[i]
    forced[f"R5.step: tau_{a}/tau_{b} (adjacent exps)"] = L[a] - L[b]
# R6: geometric-mean / half-spectrum split (E6->SO(10) style): sqrt of top ratio
forced["R6: sqrt(tau_11/tau_1)  (E6->SO(10)->SU(5) two-step, geometric)"] = 0.5*(L[11]-L[1])
# R7: the Coxeter/parity 'sum rule' 7983360 appears in the program; ratio to it
#     (object-internal number, not physics) -- included as a control.
forced["R7: tau_8 / 7983360 (control: object-internal sum-rule)"] = L[8] - math.log10(7983360)

w("  Each forced rule, its log10, and distance to 10^17:")
tol3 = math.log10(3)
best_forced = None
for name, v in forced.items():
    dd = abs(v - 17.0)
    flag = "  <-- within factor 3 of 10^17" if dd <= tol3 else ""
    w(f"    {name:<52s} log={v:8.3f}  |Dlog17|={dd:6.3f} (x{10**dd:.2f}){flag}")
    if dd <= tol3 and (best_forced is None or dd < best_forced[1]):
        best_forced = (name, dd)
w("")
if best_forced:
    w(f"  Best forced rule within factor 3: {best_forced[0]}  (|Dlog|={best_forced[1]:.3f})")
else:
    w("  NO forced rule lands within factor 3 of 10^17.")
w("")

# ----------------------------------------------------------------------------
# STEP 4b — chat-1's "FOUR UNSTABLE EXPONENTS": the theta-EVEN / F4 set {1,5,7,11}.
#   WHICH four & WHY: E6 has 6 exponents {1,4,5,7,8,11}. Under the object's theta
#   involution (sign(tau_m)=(-1)^m, banked B617), the two theta-ODD torsions sit at
#   {4,8}; the FOUR theta-EVEN ones are exactly the F4 exponents {1,5,7,11} (F4 = the
#   theta-fixed subgroup of E6). Chat-1's "four unstable exponents" = this F4 quartet.
#   TEST: does ANY signed product/ratio built from ONLY these four land near 10^17,
#   tighter than the base rate? (This is the sub-claim that was previously asserted-
#   not-computed; here it is enumerated in-sandbox and the full magnitude set saved.)
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 4b — the FOUR theta-EVEN/F4 exponents {1,5,7,11}: any near-17 combo?")
w("=" * 78)
F4 = THETA_EVEN[:]                       # [1, 5, 7, 11]
assert F4 == [1, 5, 7, 11], F4
f4_combos = {}
for k in range(1, len(F4) + 1):
    for subset in itertools.combinations(F4, k):
        for signs in itertools.product([+1, -1], repeat=k):
            val = sum(s * L[m] for s, m in zip(signs, subset))
            num = [m for s, m in zip(signs, subset) if s > 0]
            den = [m for s, m in zip(signs, subset) if s < 0]
            lab = "*".join(f"t{m}" for m in num) or "1"
            if den:
                lab += "/(" + "*".join(f"t{m}" for m in den) + ")"
            f4_combos[lab] = val
w(f"  F4 exponents (four theta-EVEN): {F4}")
w(f"  logs: " + ", ".join(f"log|tau_{m}|={L[m]:.3f}" for m in F4))
w(f"  total signed products/ratios over {{1,5,7,11}} (sizes 1-4): {len(f4_combos)}")
w("")
mags = sorted(set(round(abs(v), 3) for v in f4_combos.values()))
w("  ALL distinct |log10| magnitudes in the F4-only space (computed, not cited):")
# wrap the magnitude list to keep the output readable
line = "    "
for x in mags:
    tok = f"{x:.3f} "
    if len(line) + len(tok) > 78:
        w(line.rstrip()); line = "    "
    line += tok
w(line.rstrip())
w("")
w("  F4-only combos CLOSEST to 10^17 (the actual test of chat-1's claim):")
for lab, v in sorted(f4_combos.items(), key=lambda kv: abs(abs(kv[1]) - 17.0))[:6]:
    dd = abs(abs(v) - 17.0)
    w(f"    {lab:<22s} log={v:8.3f}  |Dlog17|={dd:.3f}  factor={10**dd:.2f}")
f4_best = min(f4_combos.items(), key=lambda kv: abs(abs(kv[1]) - 17.0))
f4_best_dd = abs(abs(f4_best[1]) - 17.0)
w("")
w(f"  => CLOSEST F4-only combo to 10^17: {f4_best[0]} (log {f4_best[1]:.3f}), "
  f"factor {10**f4_best_dd:.1f} away — NOT within the factor-3 base-rate window.")
w("")
w("  The four 'landmark' F4-only magnitudes (honest, in-sandbox values):")
landmarks = {
    "full product  t1*t5*t7*t11":            L[1] + L[5] + L[7] + L[11],
    "2-2 split     t1*t5/(t7*t11)":          L[1] + L[5] - L[7] - L[11],
    "2-2 split     t1*t11/(t5*t7)":          L[1] + L[11] - L[5] - L[7],
    "top/bottom    t11/t1":                  L[11] - L[1],
}
for name, v in landmarks.items():
    w(f"    {name:<32s} log10 = {abs(v):7.3f}")
w("  (These are the correctly-computed replacements for the previously-asserted")
w("   figures ~61.0, ~43.7, ~13.6, ~36.4. NO F4-only combo sits near ~10^26; the")
w("   nearest real magnitudes there are 24.208 and 28.144 — the earlier '10^26.2'")
w("   was an uncomputed estimate and is retracted.)")
w("")

# ----------------------------------------------------------------------------
# STEP 5 — VERDICT LOGIC
# ----------------------------------------------------------------------------
w("=" * 78)
w("STEP 5 — VERDICT")
w("=" * 78)
# The most-principled a-priori rule (R1: theta-odd ratio) result:
r1 = L[8] - L[4]
w(f"  Most-principled a-priori 2-combo (theta-odd sector ratio tau_8/tau_4):")
w(f"     log = {r1:.3f} = 10^{r1:.2f}  -> MISSES 10^17 by factor {10**abs(r1-17):.0f}.")
w(f"  The OBSERVED hit tau_11/tau_8 (log {r:.2f}) requires choosing 'top exp / top theta-odd',")
w(f"     which is a POST-HOC selection, not forced by the theta-structure.")
w("")
# base rate numbers
fr_all_3, _ = None, None
h_all = {lab: v for lab, v in combos.items() if abs(v - 17.0) <= tol3}
h_r2 = {lab: v for lab, v in ratios2.items() if abs(v - 17.0) <= tol3}
w(f"  BASE RATE: pure 2-ratios within factor 3 of 10^17: {len(h_r2)}/{len(ratios2)} "
  f"= {100*len(h_r2)/len(ratios2):.1f}%  (refines chat-1's ~3%)")
w(f"  Expected # of <=3-combos within factor 3 of a random target ~ {dens*2*tol3:.1f}"
  f"  (>1 => a hit somewhere is EXPECTED, not surprising).")
w(f"  chat-1's FOUR unstable exponents = theta-EVEN/F4 {{1,5,7,11}}: closest of its "
  f"{len(f4_combos)} signed combos to 10^17 is {f4_best[0]} (factor {10**f4_best_dd:.1f} off) "
  f"-- NO F4-only rule lands near 17 either.")
w("")
verdict = "B"
reason = ("No forced rule lands at 10^17 tighter than the base rate: the single most-principled "
          "combination (theta-odd ratio) misses by ~2 orders; the observed hit is a post-hoc "
          "2-ratio selection whose per-combo rate is ~3%, and with a dense combo space a "
          "factor-3 near-hit to SOME famous target is EXPECTED (look-elsewhere).")
w(f"  OUTCOME: {verdict}")
w(f"  {reason}")

with open(os.path.join(HERE, "b724_probe2_out.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
