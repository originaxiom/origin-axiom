"""S053 (firewalled speculation) — the SELECTION-RULE LENS, first probe.

THE LENS: every closed door of the program measured a class function / Galois invariant /
commensurability invariant -- and all launder (the object IS a symmetry). The SM is not a
spectrum but a set of SELECTION RULES (charge conservation, anomaly cancellation, forbidden
transitions) = the KERNEL / the ZEROS. We read the image (values, launder) and filed every ZERO
(seam-dark, phase-null, CS=0, baryon sum=0) as a NO. Invert: read the ZEROS as selection rules.

FIRST PROBE: the seam operator S = W1 . Par . W2 on the level-15 theta rep (Z/15). Its ZERO
entries = the forbidden transitions = the selection rule. Result (exact, cyclotomic):
  * S has 45 allowed / 180 forbidden of 225.
  * the allowed set is EXACTLY {(i,j) : j - 2i == 3 (mod 5)} -- a linear conservation law.
  * it lives ENTIRELY in the mod-5 (golden/level-5) factor; mod-3 (Eisenstein) is FREE
    (all 9 (i mod3, j mod3) cells equally populated).
  * "2" is the primitive root mod 5 (Frobenius) -> level-5 Weil/Gauss-sum arithmetic.
  * DIRECTED: W1.W2 gives 45 (selective) but W2.W1 gives 225 (no rule). The asymmetry is
    beyond Galois (Galois preserves zero-count); it is a genuine order-specific structure in the
    natural (charge) basis. This EXTENDS B427 (exchange = sigma_17 at the TRACE level) to a
    structural zero-pattern asymmetry.

CONTROL (discriminates): W1.Par.W1 = 75, W2.Par.W2 = 75, W2.Par.W1 = 225, I.Par.I = 15. The
45-rule is specific to the W1.W2 order, not "any product is sparse."

HONEST VERDICT -- Bin B (the rule is golden-forced), lens VALIDATED:
  [MATH] the lens extracts a REAL, exact selection rule (a directed mod-5 conservation law) where
         the value-lens saw only "the seam is dark." The reframing works: the zeros carry structure.
  [MATH] the rule is purely mod-5, primitive-root-2 => the level-5 Weil arithmetic = the golden
         (sqrt5) numerator structure the whole program showed is FORCED. So it is NOT a specific
         SM selection rule; it is the forced arithmetic, now wearing a conservation-law costume.
  [HOOK] the DIRECTIONALITY (W1.W2 selects, W2.W1 does not; beyond Galois) is the live residue --
         a directed/oriented conservation law is CP/arrow/chirality-shaped, and it appears at the
         golden seam. The clearest next probe.
  [LEAP] "physics = the object's selection rules (kernel), existence = the cancellation remainder
         (Origin Axiom)": the lens is the right category; this first rule is forced, not physical.

NEGATIVES: the rule is forced by level-5 (needs the level-5-alone control to fully seal Bin B);
"selection rule" is loose -- no SPECIFIC SM rule is matched, only the CATEGORY. No physics claim;
nothing to CLAIMS. This is a firewalled method-validation + a live residue, not a result.
"""
import sys
sys.path.insert(0, "frontier/B367_value_map"); sys.path.insert(0, "frontier/B358_seam_certification")
from step0_exact_matrices import build_theta_W
import cyclo_engine as CE
N = 15


def _iszero(e):
    return all(c == 0 for c in e) if isinstance(e, list) else e == 0


def parmat():
    return [[(CE.ONE if j == (-i) % N else CE.ZERO) for j in range(N)] for i in range(N)]


def allowed(A, B):
    S = CE.mmul(CE.mmul(A, parmat()), B)
    return set((i, j) for i in range(N) for j in range(N) if not _iszero(S[i][j]))


def seam_rule():
    W1, W2 = build_theta_W(1), build_theta_W(2)
    al = allowed(W1, W2)
    rev = allowed(W2, W1)
    rule_holds = all((j - 2 * i) % 5 == 3 for i, j in al) and len(al) == 45
    from collections import Counter
    mod3_free = len(set(Counter((i % 3, j % 3) for i, j in al).values())) == 1
    return dict(allowed=len(al), reverse=len(rev), rule="j-2i==3 (mod5)",
                rule_holds=rule_holds, directed=(len(al) != len(rev)), mod3_free=mod3_free)


if __name__ == "__main__":
    r = seam_rule()
    print("seam selection rule:", r)
    assert r["rule_holds"] and r["directed"] and r["mod3_free"]
    print("LENS VALIDATED (real selection rule extracted); verdict Bin B (golden-forced);"
          " live residue = the directionality.")
