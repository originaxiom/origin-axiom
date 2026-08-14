"""B791 — the per-sector Weyl completeness budget for the B788 Maass bank.

ORIGIN: the criterion is Chat-1's (verification receipt, 2026-07-28). This file is cc's
INDEPENDENT re-derivation — the Humbert volume is recomputed from the L-value, not taken
from the receipt, and every table row is regenerated.

THE CRITERION. Gamma_41 < Gamma_p = PSL(2,O_3) of index 12, and
L^2(Gamma_41\\H^3) = L^2(Gamma_p\\H^3, E) with E = Ind 1 of rank 12, decomposing as
E_1 + E_5 + E_6 of ranks 1, 5, 6. Weyl for a flat bundle counts WITH multiplicity as
rank(E_i) * W(T). A V_i-isotypic eigenspace has dimension a multiple of dim V_i, so under
generic multiplicity (one copy of V_i per eigenvalue) the count of DISTINCT parameters is

        N_i(T)  ~  W(T)      -- THE SAME IN EVERY SECTOR, including the parent.

The arithmetic identity 1 + 5 + 6 = 12 is what makes it uniform. Sum check:
sum_i dim(V_i) * W(T) = 12 W(T) = Vol(Gamma_41)/(6 pi^2) T^3.  Verified below.
"""
import json

import mpmath as mp

mp.mp.dps = 30
line = "=" * 74
OUT = {}

# ---- Humbert volume of the parent, from the L-value (independent of the receipt) --------
L2chi = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9      # L(2, chi_-3)
zK2 = mp.zeta(2) * L2chi
VOL_P = mp.mpf(3) ** mp.mpf(1.5) * zK2 / (4 * mp.pi ** 2)
VOL_41 = mp.mpf("2.029883212819307250042405108549")
W = VOL_P / (6 * mp.pi ** 2)

print(f"{line}\nTHE BUDGET\n{line}")
print(f"  Vol(PSL(2,O_3)\\H^3) = {mp.nstr(VOL_P, 15)}")
print(f"  W = Vol_p/(6 pi^2)  = {mp.nstr(W, 12)}       (receipt: 0.0028565)")
OUT["W"] = float(W)

print(f"\n  CONSISTENCY (the step that makes per-sector uniformity work):")
lhs, rhs = 12 * W, VOL_41 / (6 * mp.pi ** 2)
print(f"    12 * W                 = {mp.nstr(lhs, 12)}")
print(f"    Vol(m004)/(6 pi^2)     = {mp.nstr(rhs, 12)}")
print(f"    equal?  {abs(lhs - rhs) < mp.mpf('1e-25')}   <- 1+5+6 = 12 checks out")
OUT["consistency_12W_equals_m004_weyl"] = bool(abs(lhs - rhs) < mp.mpf("1e-25"))

print(f"\n{line}\nEXPECTED DISTINCT EIGENVALUES PER SECTOR\n{line}")
print(f"  {'r <=':>8} {'N_i(T) = W T^3':>18}")
rows = []
for T in (5.0, 8.0, 10.0, 12.0, 15.2, 18.0, 20.0, 24.5):
    v = W * mp.mpf(T) ** 3
    rows.append({"T": T, "N": float(v)})
    print(f"  {T:>8} {float(v):>18.4f}")
OUT["table"] = rows

print(f"\n{line}\nTHE GATE-9 / GATE-5 SPECIFICATION MISMATCH (verified vs the sealed JSON)\n{line}")
g9 = (mp.mpf("0.50"), mp.mpf("12.00"))          # GATE9_PROTOCOL.json search_interval
mu = W * (g9[1] ** 3 - g9[0] ** 3)
need = mp.mpf(10)
T_need = (need / W) ** (mp.mpf(1) / 3)
print(f"  GATE9_PROTOCOL search_interval      = [{g9[0]}, {g9[1]}]")
print(f"  GATE5_PROTOCOL distinct/sector = 10, trial_count = 80")
print(f"  budget on Gate 9's interval   mu    = {mp.nstr(mu, 6)} per sector")
print(f"  r required for 10 per sector        = {mp.nstr(T_need, 6)}")
print(f"  spectral-volume cost of 12 -> 15.2  = {mp.nstr((T_need / g9[1]) ** 3, 5)}x")
print(f"  => Gate 9 as sealed buys ~{float(mu/need)*100:.0f}% of what Gate 5 requires. REAL DEFECT.")
OUT["gate9_mu"] = float(mu)
OUT["gate5_required_r"] = float(T_need)
OUT["cost_ratio"] = float((T_need / g9[1]) ** 3)

print(f"\n{line}\nTHE ARBITRARY CONSTANT THIS REPLACES (cc's addition)\n{line}")
print("  GATE9_PROTOCOL.json  screen.maximum_minima_per_sector = 24  (hand-set, not derived)")
print("  Gate 9's observed screen retention: V5 = 25, V6 = 24")
print("  => the run failed the guard `screen_minimum_cap_respected` because V5 hit 25 against")
print("     an ARBITRARY cap of 24. W(T) supplies the principled replacement: a cap derived")
print("     from the spectral budget (mu ~ 4.94/sector on [0.5,12], so a coarse screen should")
print("     retain a stated multiple of mu, and the confirmation stage should return to ~mu).")
print("     This is why 'calibrate then extend' fixes the ACTUAL failure cause.")

print(f"\n{line}\nTHE SECOND CALIBRATION POINT (Chat-1, verified here)\n{line}")
lam_p = mp.mpf("51.014")                        # Grunewald-Huntebrinker 1996, parent ground state
r_p = mp.sqrt(lam_p - 1)
T1 = (1 / W) ** (mp.mpf(1) / 3)                 # Weyl: W(T) = 1
print(f"  parent lambda_1 = {lam_p}  =>  r = {mp.nstr(r_p, 10)}")
print(f"  Weyl first-eigenvalue prediction  W(T)=1 at r = {mp.nstr(T1, 10)}")
print(f"  agreement = {mp.nstr(abs(r_p - T1) / T1 * 100, 4)} %")
print(f"  W(r=7.0721) = {mp.nstr(W * r_p ** 3, 6)}  <- it IS the ground state, so")
print(f"                lambda_1(m004) <= 51.014 is likely TIGHT on V1, not just a bound.")
print(f"  W(r=24.5033) = {mp.nstr(W * mp.mpf('24.5033') ** 3, 6)}  <- the existing DCHY control")
print(f"  Bessel mode-budget ratio 24.5033/7.0721 = {mp.nstr(mp.mpf('24.5033') / r_p, 4)}x")
print("  => independent SOURCE (G-H 1996 vs DCHY 2025) at the OPPOSITE spectral end, and")
print("     truncation is r-dependent -- which is exactly how Gate 8 died. Two heights at one")
print("     r cannot pin truncation; they share the target.")
OUT["second_control_r"] = float(r_p)
OUT["second_control_weyl_r"] = float(T1)
OUT["second_control_agreement_pct"] = float(abs(r_p - T1) / T1 * 100)

json.dump(OUT, open(__file__.rsplit("/", 1)[0] + "/results.json", "w"), indent=2)
print(f"\n{line}\nresults.json written\n{line}")
