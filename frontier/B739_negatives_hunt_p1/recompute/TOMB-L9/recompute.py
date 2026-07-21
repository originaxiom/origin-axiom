#!/usr/bin/env python3
"""
B739 Stage-B recompute — TOMB-L9 (S014: Lambda = Lambda_Planck * phi^(-2N), and the k~137 variant).

Banked kill (TOMBSTONES.md:L9, citing CLAIMS.md D1-D3, FAILURE_ATLAS A2):
  "DEAD by null hypothesis — ~60% of random constants match as well — and by
   circularity (N is defined by the answer it is meant to predict)."

THE discriminating fact (the fact that, if true, kills the claim):
  The phi^(-2N) match to Lambda carries no predictive content, because
  (a) CIRCULARITY: N is an integer FITTED from the answer — the family
      {phi^(-2N) : N in Z} is a uniform grid in log10-space of spacing
      2*log10(phi) ~ 0.418 dex, so ANY target value whatsoever is matched to
      within half a step (<= 0.209 dex) by construction; and
  (b) BASE-RATE: a random base b, fitted the same way, matches comparably
      (the banked epitaph's specific quantification was "~60% match as well").
Both legs are recomputed below from scratch (E19: compute, not cite).

DECLARED CONVENTIONS (E1 — none of these were declared by the original arc;
the legacy source, legacy/handoff/handoff.md:61, gives only
"Lambda = phi^{-2N} without derived N"):
  C1. Target: T = 122 dex, i.e. Lambda_obs / Lambda_Planck = 10^(-122), the
      canonical order-of-magnitude the legacy claim addressed ("the 10^-122
      cosmological-constant problem" in Planck units, Lambda * l_Pl^2).
      This is a cosmological/GR number, not a Standard-Model quantity (Gate 5
      respected). Sensitivity is run at T = 121.539 (Lambda*l_Pl^2 = 2.888e-122)
      and T = 122.959 (rho_Lambda/rho_Planck = 1.1e-123) to show no conclusion
      depends on the convention choice.
  C2. Fit rule (both for phi and for random bases): N* = round(T / (2*log10 b)),
      integer, N* >= 1; residual r(b, T) = | T - 2*N* * log10(b) | in dex.
  C3. "Random constant" model for the null: base b drawn UNIFORM on (1, 10]
      (a random O(1-10) constant substituted for phi in the same formula family
      b^(-2N)). M = 100_000 draws, seed = 739 (fixed, declared; the only
      randomness in this script). Robustness: a second model, b log-uniform on
      [1.05, 100].
  C4. "Matches as well" = fitted residual <= phi's own fitted residual at the
      same T (the strict reading of "match as well [as phi]"). The full residual
      CDF is also printed, including the threshold that WOULD be needed to make
      the "~60%" figure true.
  C5. k~137 variant: read as the value formula Lambda = Lambda_Planck *
      phi^(-2k) with k = 137 (the arithmetic content that is recomputable here;
      D1's separate Chern-Simons-normalization argument is not needed for the
      value-level adjudication).

Deterministic: no wall-clock, no network; single fixed seed (739) declared above.
"""

import math
import random

PHI = (1 + math.sqrt(5)) / 2
STEP = 2 * math.log10(PHI)          # log10-spacing of the phi^(-2N) grid
T_MAIN = 122.0                      # C1
T_SENS = [121.539, 122.959]         # C1 sensitivity
SEED = 739
M_DRAWS = 100_000

line = "-" * 72


def fit_residual(b: float, T: float):
    """C2: best integer N and residual (dex) for Lambda-ratio 10^-T vs b^(-2N)."""
    s = 2 * math.log10(b)
    if s <= 0:
        return None, float("inf")
    N = max(1, round(T / s))
    return N, abs(T - N * s)


print("=" * 72)
print("TOMB-L9 recompute: S014  Lambda = Lambda_Planck * phi^(-2N)")
print("=" * 72)
print(f"phi                 = {PHI:.12f}")
print(f"grid step 2*log10(phi) = {STEP:.6f} dex")
print()

# ----------------------------------------------------------------------
# FACT 1 — CIRCULARITY, computed (the sound leg of the kill).
# N is obtained by inverting the formula on the observed answer; and the
# fitted family matches ANY target, so the match is guaranteed a priori.
# ----------------------------------------------------------------------
print(line)
print("FACT 1 — circularity / guaranteed-match (the vacuity of the fit)")
print(line)
N_phi, r_phi = fit_residual(PHI, T_MAIN)
print(f"T = {T_MAIN} dex: best-fit N* = {N_phi}  (= round({T_MAIN}/{STEP:.6f}) "
      f"= round({T_MAIN/STEP:.3f})) -> residual {r_phi:.4f} dex")
print("  i.e. N is DEFINED by the answer: no derivation of N exists in the")
print("  claim (legacy: 'Lambda = phi^{-2N} without derived N').")

# Sweep arbitrary hypothetical targets: the fit succeeds for ALL of them.
worst = 0.0
total = 0.0
count = 0
Tq = 50.0
while Tq <= 200.0:
    _, r = fit_residual(PHI, Tq)
    worst = max(worst, r)
    total += r
    count += 1
    Tq = round(Tq + 0.001, 3)
print(f"sweep T in [50, 200] dex, step 0.001 ({count} targets):")
print(f"  max fitted residual  = {worst:.6f} dex  (theory bound: step/2 = {STEP/2:.6f})")
print(f"  mean fitted residual = {total/count:.6f} dex  (theory: step/4 = {STEP/4:.6f})")
print("  => the phi^(-2N) family with fitted integer N matches ANY value of the")
print("     constant to <= 0.209 dex (a factor < 1.62). A 'match' is guaranteed")
print("     before Lambda is even looked at: ZERO discriminating power without an")
print("     independent derivation of N. This is the circularity leg, computed.")
print()

# ----------------------------------------------------------------------
# FACT 2 — the BASE-RATE (null) leg: does "~60% of random constants match
# as well" reproduce?  (No script ever existed in-repo for this clause.)
# ----------------------------------------------------------------------
print(line)
print("FACT 2 — the null test (random bases, fitted the same way)")
print(line)
rng = random.Random(SEED)
res_uniform = []
for _ in range(M_DRAWS):
    b = 1.0 + 9.0 * rng.random()          # C3: uniform (1, 10]
    _, r = fit_residual(b, T_MAIN)
    res_uniform.append(r)
res_uniform.sort()

frac_aswell = sum(1 for r in res_uniform if r <= r_phi) / M_DRAWS
median_r = res_uniform[M_DRAWS // 2]
# threshold that would be needed for the "~60%" clause to be true:
thr60 = res_uniform[int(0.60 * M_DRAWS)]
print(f"model C3: b ~ Uniform(1,10], M = {M_DRAWS}, seed = {SEED}, T = {T_MAIN}")
print(f"  phi's fitted residual                       = {r_phi:.4f} dex")
print(f"  fraction of random b with residual <= phi's = {frac_aswell*100:.1f}%")
print(f"  median random-base residual                 = {median_r:.3f} dex")
print(f"  CDF: <=0.1 dex: {sum(1 for r in res_uniform if r <= 0.1)/M_DRAWS*100:.1f}%"
      f"   <=0.2: {sum(1 for r in res_uniform if r <= 0.2)/M_DRAWS*100:.1f}%"
      f"   <=0.3: {sum(1 for r in res_uniform if r <= 0.3)/M_DRAWS*100:.1f}%"
      f"   <=0.42: {sum(1 for r in res_uniform if r <= 0.42)/M_DRAWS*100:.1f}%")
print(f"  threshold at which '60% match' WOULD hold   = {thr60:.3f} dex")
print(f"     (i.e. '60%' requires calling a factor-{10**thr60:.1f} miss a 'match'")
print(f"      — a convention the epitaph never declared)")

# robustness: log-uniform bases
res_lu = []
for _ in range(M_DRAWS):
    b = 10 ** (rng.random() * (2 - math.log10(1.05)) + math.log10(1.05))
    _, r = fit_residual(b, T_MAIN)
    res_lu.append(r)
res_lu.sort()
frac_lu = sum(1 for r in res_lu if r <= r_phi) / M_DRAWS
print(f"robustness, b ~ LogUniform[1.05, 100]: fraction matching as well "
      f"= {frac_lu*100:.1f}%, median residual = {res_lu[M_DRAWS//2]:.3f} dex")
print()
print("  => the '~60% of random constants match as well' clause is FALSE under")
print("     the strict reading (it is ~10%, and phi sits in the good tail,")
print("     BETTER than the random-base median) — reproducing, independently,")
print("     the B565 exhumation finding (which struck the clause from the")
print("     epitaph while keeping S014 dead on circularity).")
print()

# sensitivity of both facts to the Lambda convention (C1)
print(line)
print("Sensitivity to the Lambda-ratio convention (C1)")
print(line)
for T in [T_MAIN] + T_SENS:
    Np, rp = fit_residual(PHI, T)
    rng2 = random.Random(SEED)
    cnt = 0
    med_lo = 0
    res2 = []
    for _ in range(M_DRAWS):
        b = 1.0 + 9.0 * rng2.random()
        _, r = fit_residual(b, T)
        res2.append(r)
        if r <= rp:
            cnt += 1
    res2.sort()
    print(f"  T = {T:8.3f}: N* = {Np}, phi residual = {rp:.4f} dex, "
          f"random-b as-well fraction = {cnt/M_DRAWS*100:.1f}%, "
          f"median = {res2[M_DRAWS//2]:.3f} dex")
print("  => never remotely 60% under the strict reading; the kill's substance")
print("     (no predictive content) holds under every convention.")
print()

# ----------------------------------------------------------------------
# FACT 3 — the k~137 variant (C5), arithmetic check.
# ----------------------------------------------------------------------
print(line)
print("FACT 3 — the k~137 variant, as a value formula")
print(line)
v137 = 2 * 137 * math.log10(PHI)
print(f"  phi^(-2*137) = 10^-{v137:.2f}; target 10^-{T_MAIN}")
print(f"  miss = {T_MAIN - v137:.2f} dex (a factor 10^{T_MAIN - v137:.1f})")
print("  => k=137 does NOT even value-match; only the fitted N* = 292 does,")
print("     and FACT 1 shows that fit is guaranteed for any target.")
print()

# ----------------------------------------------------------------------
# Verdict summary
# ----------------------------------------------------------------------
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"1. CIRCULARITY leg: COMPUTED AND UPHELD. N* = {N_phi} is defined by the")
print(f"   answer; the fitted family matches ANY target to <= {STEP/2:.4f} dex")
print("   (max over a 150-dex sweep = %.4f dex). The claim has zero" % worst)
print("   discriminating power. This kills S014.")
print(f"2. '~60%' clause: DOES NOT REPRODUCE. Strict as-well-as-phi fraction:")
print(f"   {frac_aswell*100:.1f}% (uniform bases; {frac_lu*100:.1f}% log-uniform); phi's fit")
print(f"   ({r_phi:.3f} dex) beats the random-base median ({median_r:.3f} dex).")
print("   Matches the banked B565 correction (TOMBSTONES.md lines 345-349):")
print("   the quantitative clause is struck; the kill rests on leg 1.")
print(f"3. k~137 variant: misses by {T_MAIN - v137:.1f} dex. Dead at the value level.")
print()
print("VERDICT: RECONFIRMED — S014 stays dead on the computed circularity/")
print("guaranteed-match fact; the 60% figure stays struck (as already banked).")
