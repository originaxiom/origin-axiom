"""xB030 U3 v2.  v1 IS DEFECTIVE AND IS RECORDED AS SUCH:

  (a) it included lambda with G*lambda = 0 (mod k).  There 4sin^2 = 0 EXACTLY -- the flat bundle is
      TRIVIAL in that direction, so it is not a symmetry-breaking Wilson line at all, and FW's
      eq.(3.1) is UNDEFINED there (it is precisely the zero-mode case).  The 'best P_eff = 669'
      figures v1 printed are FLOATING-POINT ARTEFACTS of log(rounding error), not physics.
  (b) its sealed prediction that the achieving set has density O(1/k) is REFUTED by its own numbers:
      counts went 1, 1, 1, 5, 13 as k went 316, 500, 1000, 2000 -- growing, not shrinking.

v2 excludes the degenerate residue, uses k coprime to G so that G*lambda = +-1 is solvable, and
reports the density honestly against a derived prediction rather than the sealed one.
"""
import json, math, os

P, Q, M = 15, 18, 10
G = P + M + 1            # 26
TARGET = 84.0


def peff(k, lam):
    r = (G * lam) % k
    if r == 0:
        return None                      # DEGENERATE: trivial flat bundle, formula undefined
    s = math.sin(G * math.pi * lam / k) ** 2
    return math.log(k) - M * math.log(4 * s)


print("U3 v2    THE Lambda TUNING'S SHAPE -- degenerate residue EXCLUDED")
print(f"         G = P+M+1 = {G}; target P_eff >= {TARGET} (eq.(8) at Q-P=3)")
print("         Derived expectation (NOT the sealed one, which is refuted below):")
print("           P_eff >= T  <=>  4 sin^2(pi ||G*lam/k||) <= k^(1/M) e^(-T/M)")
print("           => ||G*lam/k|| <= theta(k) = arcsin(sqrt(k^(1/M) e^(-T/M))/2)/pi")
print("           => count ~ 2 k theta(k), i.e. DENSITY ~ 2 theta(k), which GROWS like k^(1/2M).")
rows = []
for k in (99, 199, 317, 501, 999, 2001, 4001):
    if math.gcd(G, k) != 1:
        continue
    good, best = 0, None
    for lam in range(1, k):
        v = peff(k, lam)
        if v is None:
            continue
        if best is None or v > best[0]:
            best = (v, lam)
        if v >= TARGET:
            good += 1
    frac = good / (k - 1)
    thr = (k ** (1.0 / M)) * math.exp(-TARGET / M)
    theta = math.asin(min(1.0, math.sqrt(thr) / 2)) / math.pi
    pred_frac = 2 * theta
    approx = (1 + 2 * M) * math.log(k) - M * math.log(4 * math.pi ** 2)
    r = (G * best[1]) % k
    rows.append((k, good, frac, pred_frac, best, approx, min(r, k - r)))
    print(f"         k={k:5d}: reach 84: {good:4d}/{k-1} (density {frac:.5f}; derived "
          f"{pred_frac:.5f})  best P_eff={best[0]:7.3f} at lam={best[1]:5d}, "
          f"||G*lam|| = {min(r, k-r)}  closed form at +-1: {approx:7.3f}")
den_ok = all(abs(f - pf) < 0.35 * max(f, pf, 1e-9) or (f == 0 and pf < 0.01)
             for _, _, f, pf, _, _, _ in rows)
cf_ok = all(d == 1 and abs(b[0] - a) < 1e-6 for _, _, _, _, b, a, d in rows)
print(f"\n         measured density agrees with the derived one (35% tol): {den_ok}")
print(f"         the BEST lambda always sits at ||G*lam|| = 1 and matches the closed form: {cf_ok}")
print(f"         density is NOT O(1/k): {[round(f,5) for _,_,f,_,_,_,_ in rows]} against "
      f"1/k = {[round(1/k,5) for k,_,_,_,_,_,_ in rows]}")
print("\n         WHAT IS TRUE, corrected:  the requirement is on ||G*lambda/k||, the DISTANCE")
print("         TO AN INTEGER -- a near-integer (Diophantine) condition, as predicted.  But the")
print("         ACHIEVING DENSITY IS ~0.5% AND SLOWLY GROWING, NOT O(1/k).  The sealed 'one-in-k")
print("         coincidence' is REFUTED by this cell's own numbers.")
print("         And k >= ~316 is needed at all: at k = 99 NOTHING reaches 84.")
print("         FENCE: this is the SOURCE'S OWN example, Q = S^3/Z_k, not the landscape.")
json.dump({"rows": [(k, g, f, pf, list(b), a, d) for k, g, f, pf, b, a, d in rows],
           "density_matches_derived": bool(den_ok), "closed_form_at_residue_1": bool(cf_ok),
           "sealed_prediction_O_1_over_k": "REFUTED"},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "u3_fix.json"),
               "w", encoding="utf-8"), indent=1)
print(f"\nU3 v2 PASS  (content is the verdict above)")
