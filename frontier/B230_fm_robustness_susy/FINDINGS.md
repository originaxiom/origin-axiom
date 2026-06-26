# B230 — golden's SUSY-uniqueness is robust to AFM/FM; the FM "silver SUSY" is a central-charge coincidence (not real)

**Date:** 2026-06-27. **Status:** stress-test of B224/B228 under the ferromagnetic coupling (chat1's check), with a
verify-don't-trust catch. **Golden's SUSY-uniqueness is robust to the AFM/FM choice**, and the FM family's apparent
SUSY member (silver) is a central-charge coincidence, not genuine supersymmetry — which **reinforces B228's coset
criterion over bare central-charge matching**. Firewall: dimensionless CFT/coset rep-theory; **nothing to
`CLAIMS.md`; P1–P16 untouched.** Ledger **V233**.

## The check

The su(2)_k anyon chain has two couplings (Feiguin–Trebst–Ludwig):
```
   AFM:  M(k+1, k+2)          golden (k=3) -> M(4,5) = TCI, c=7/10
   FM:   Z_k parafermion,     c = 2(k-1)/(k+2);   golden (k=3) -> Z_3 = c=4/5 = 3-state Potts
```

Does the **FM** metallic family (level `k=m²+2`) have a SUSY member? A naive central-charge test flags **m=2
(silver)**:
```
   silver FM = Z_6 parafermion,  c = 2·5/8 = 5/4  =  c(SM(6))   (the N=1 super minimal model with p=6).
```

## The catch (verify-don't-trust)

This is a **central-charge coincidence, not supersymmetry.** The Z₆ parafermion is the coset `SU(2)₆/U(1)`; the
super minimal model `SM(6)` is the coset `(SU(2)₄ × SU(2)₂)/SU(2)₆`. **Different cosets → different CFTs** with the
same `c=5/4`. The parafermion CFTs are not N=1 super minimal models. So the silver FM chain is **not** SUSY.

This is a clean illustration of why **B228's coset coincidence is the rigorous criterion** and why B224's original
central-charge matching, taken alone, could admit false positives. The rigorous (coset) test gives: the **only**
metallic chain in **any** coupling that is genuinely an N=1 super minimal model is **golden + AFM** (= the TCI, via
the unique ordinary/super coset coincidence at SU(2)₃, B228).

## Net

Golden's SUSY-uniqueness is **robust to the AFM/FM choice**: golden+AFM is the unique genuine SUSY metallic chain;
golden+FM is the 3-state Potts (not SUSY); and the only FM central-charge near-miss (silver, c=5/4) is a coset
mismatch, not real SUSY. The episode reinforces the methodological point — use the coset identity (B228), not
central-charge matching, as the test for "is this CFT supersymmetric." `[cited]` FM→Z_k parafermion / AFM→M(k+1,k+2)
(Feiguin–Trebst–Ludwig); `[exact]` the central charges, the coincidence, and the coset distinction (3 pytest locks).
Novelty UNCHECKED. (`B224 → B228 → B230`.)
