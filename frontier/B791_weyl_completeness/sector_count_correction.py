"""B791 CORRECTION — the per-sector count is dim(V_i)*W(T), NOT W(T).

Chat-1's criterion (and cc's verification of it) carried a factor error: it divided out
dim(V_i) once too often. The arithmetic in the original table was right; the DERIVATION
behind it was not, and cc verified the former without checking the latter.

CONSEQUENCE: Chat-1's headline "live defect" (Gate 9 cannot discharge Gate 5) EVAPORATES.
Gate 9's sealed interval is sufficient. The real bug is the hand-set screen cap -- which was
cc's separate catch, and is now the whole story rather than a footnote.
"""
import json

import mpmath as mp

mp.mp.dps = 25
line = "=" * 74
OUT = {}

L2chi = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
VOL_P = mp.mpf(3) ** mp.mpf(1.5) * mp.zeta(2) * L2chi / (4 * mp.pi ** 2)
W = VOL_P / (6 * mp.pi ** 2)
DIMS = {"V1": 1, "V5": 5, "V6": 6}

print(f"{line}\nTHE CORRECTION\n{line}")
print("""  L^2(Gamma_41\\H^3) = L^2(Gamma_p\\H^3, E_rho),  E_rho = E1 + E5 + E6 of RANKS 1, 5, 6.
  Weyl on a rank-m flat bundle counts m*W(T) eigenvalues. Those are generically SIMPLE:
  E_i has IRREDUCIBLE holonomy, so nothing forces a dim(V_i)-fold degeneracy. (A
  dim(V_i)-fold degeneracy would need a finite group acting on m004 itself -- but the
  degree-12 cover is NON-REGULAR, image order 1920 with point stabiliser 160, so there is
  no such deck action.)

      => sector i contributes  dim(V_i) * W(T)  DISTINCT eigenvalues to m004.

  Chat-1 wrote N_i(T) ~ W(T) "the same in every sector", obtained by dividing the
  with-multiplicity count dim(V_i)*W(T) by an assumed multiplicity dim(V_i). That
  multiplicity is not there.""")

print(f"\n  total = sum_i dim(V_i) W = {1+5+6} W = "
      f"{mp.nstr(12 * W, 10)}  = Vol(m004)/(6 pi^2)? "
      f"{abs(12*W - mp.mpf('2.029883212819307250042405108549')/(6*mp.pi**2)) < mp.mpf('1e-25')}")

print(f"\n{line}\nCONSISTENCY ANCHOR (why the error hid)\n{line}")
print("  V1 has dim 1, so BOTH readings give W(T) there -- and V1 is exactly the inherited")
print("  parent spectrum, the one sector we can check against a known count. The readings")
print("  only diverge at V5 and V6, which is where no independent count was available...")

print(f"\n{line}\nTHE DISCRIMINATOR: the bank's OWN screen retention\n{line}")
print("  GATE9 outputs: screen retained V5 = 25, V6 = 24, against a hand-set cap of 24.\n")
print(f"  {'sector':>8} {'dim*W(12) [corrected]':>24} {'W(12) [Chat-1]':>18} {'observed':>10}")
for s, d in DIMS.items():
    if s == "V1":
        continue
    print(f"  {s:>8} {float(d * W * 12 ** 3):>24.1f} {float(W * 12 ** 3):>18.1f}"
          f" {(25 if s == 'V5' else 24):>10}")
print("\n  V5: corrected predicts 24.7, observed 25 -- essentially exact.")
print("  V6: corrected predicts 29.6, observed 24 == THE CAP. It was TRUNCATED, not complete.")
print("  Chat-1's reading predicts 4.9 for both, i.e. a 5x over-retention. The data says the")
print("  screen was ON budget, and that the cap is what broke the run.")
OUT["screen_V5_pred_corrected"] = float(5 * W * 12 ** 3)
OUT["screen_V6_pred_corrected"] = float(6 * W * 12 ** 3)

print(f"\n{line}\nCHAT-1'S 'LIVE DEFECT' EVAPORATES\n{line}")
print("  GATE5 requires 10 distinct per sector. Solve dim(V_i) W T^3 = 10:")
for s, d in (("V5", 5), ("V6", 6)):
    Tn = (mp.mpf(10) / (d * W)) ** (mp.mpf(1) / 3)
    print(f"    {s}: T = {mp.nstr(Tn, 5)}")
    OUT[f"gate5_required_r_{s}"] = float(Tn)
print("  GATE9's sealed interval reaches 12 > both. => GATE 9 CAN DISCHARGE GATE 5.")
print("  No widening to 15.5, no 2.03x cost, no re-preregistration needed.")
print("\n  THE REAL BUG is the hand-set cap: V6 needs ~30 and the cap is 24, so V6 is")
print("  truncated before confirmation ever runs; V5 trips the guard at 25 > 24.")
print("  Replace the constant with a budget-derived cap (a stated multiple of dim(V_i)*W).")

print(f"\n{line}\nRESTATED COMPLETENESS CRITERION\n{line}")
print("  For sector s and confirmed interval [a,b]:")
print("      mu_s = dim(V_s) * W * (b^3 - a^3),   z = (n_s - mu_s)/sqrt(mu_s)")
print("  PASS |z| <= 2; FAIL-LOW => skipping; FAIL-HIGH => spurious survivors.")
print("  Evaluated on CONFIRMED counts only, declared before confirmation runs.")
print(f"\n  {'r <=':>6} {'V1':>8} {'V5':>8} {'V6':>8} {'m004 total':>12}")
tab = []
for T in (6.0, 7.5, 10.0, 12.0):
    row = {"T": T, **{s: float(d * W * T ** 3) for s, d in DIMS.items()},
           "total": float(12 * W * T ** 3)}
    tab.append(row)
    print(f"  {T:>6} {row['V1']:>8.2f} {row['V5']:>8.2f} {row['V6']:>8.2f} {row['total']:>12.2f}")
OUT["table"] = tab

print(f"\n{line}\nAPPLIED TO cc3's B792 SCAN\n{line}")
r_found = [3.938916868176512, 4.900085371107029, 5.670720032723125, 5.912917880350969]
T = mp.mpf("5.9129")
mu = 12 * W * T ** 3
z = (len(r_found) - mu) / mp.sqrt(mu)
print(f"  cc3 confirmed {len(r_found)} two-height-stable dips below r = {float(T)}")
print(f"  corrected expectation (all sectors) = {mp.nstr(mu, 4)}   z = {mp.nstr(z, 3)}")
print(f"  |z| <= 2 => PASS, but on the SKIPPING side. Under Chat-1's counting the")
print(f"  expectation would be {mp.nstr(3*W*T**3, 3)} and z = {mp.nstr((4-3*W*T**3)/mp.sqrt(3*W*T**3), 3)}")
print("  -- the opposite side. So the factor decides which way cc3's scan is off.")
OUT["cc3_n"] = len(r_found)
OUT["cc3_expected"] = float(mu)
OUT["cc3_z"] = float(z)

json.dump(OUT, open(__file__.rsplit("/", 1)[0] + "/results_correction.json", "w"), indent=2)
print(f"\n{line}\nresults_correction.json written\n{line}")
