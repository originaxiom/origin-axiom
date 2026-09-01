# G1 — the su(3)⊕g₂ descent COMPUTED: registerable at step 1 (B873 confirmed), and every chain terminates at su(3) — a NON-SM ENDPOINT

**Cell:** G1_su3_g2_descent · **Date:** 2026-09-01 · **Seat:** fresh physics campaign (owner-elected batch-3 cell, closes the T8b quantifier gap of `campaign/T8_terminality_draft/VERIFICATION.md` Finding 1). Mathematics scope; Gate 5 untouched — every number below is a dimension, Dynkin index, central charge, conformal weight, anomaly coefficient, or multiset count.

## VERDICT: **NON-SM-ENDPOINT**

**Every registerable-respecting chain through su(3)⊕g₂ terminates at su(3) (⊕ abelian dials) with generation content {3: 7, 6̄: 1} — chain-independent.** The endpoint is named, computed, and it is not the Standard Model algebra.

Three headline consequences:

1. **The T8b gap closes AGAINST the wide quantifier.** Rule-independence does **not** extend to the specials-inclusive menu: min-dim on that menu picks su(3)⊕g₂ at step 1 (dim 22 < 24 = SU(3)³) and lands at su(3), never the SM. The draft's SCOPE CORRECTION (part (ii) restricted to B994's regular menus) is thereby **necessary, not merely prudent** — the unrestricted §2(ii) statement is now *refuted by computation*, not just unproven. The corrected (restricted) theorem stands untouched.
2. **The SM algebra appears on this branch and is NOT terminal there.** The chain passes through su(3)⊕su(2)⊕u(1) with content {(3,2): 2, (3,1): 3, (6̄,1): 1} — and su(2)→u(1) **stays registerable** ({3: 7, 6̄: 1} is complex), so every selection function must continue past it. Sharpening for the draft: **terminality is a property of the (algebra, content) pair, not of the algebra** — B863's part (i) is a statement about the SM algebra *with the banked generation content*, and remains correct as such (this cell's engine reproduces B863's terminality on that content as a control).
3. **NOT-REGISTERABLE-AT-STEP-1 is FALSE** — the task's flagged shortcut ("g₂ has only real reps, so the restriction may be forced self-conjugate") does not close the gap. g₂'s reps are indeed all real, but chirality lives in the **su(3) factor**: in 27 = (3,7) ⊕ (6̄,1) the 3 (×7 states) and the 6̄ are unpaired. Step 1 is registerable, confirming B873 layer 5 with an independent implementation.

---

## 1. The embedding and the branching of the 27 — derived, then diffed

su(3)⊕g₂ is the maximal S-subalgebra of e₆ with embedding indices x = (2,1) (Dynkin's table for existence; everything else computed). Conformality: c(su(3)₂) + c(g₂₁) = 16/5 + 14/5 = **6** = c(E₆ at level 1) — exact, the one registerable special completion B873 found.

**Independent derivation of the branching** (no Slansky import): exhaustive enumeration of all multisets of (A₂ irrep ⊗ G₂ irrep) pairs under four computed constraints —

| constraint | survivors |
|---|---|
| Σ dim = 27, Σ T_su(3) = 2·T_E6(27) = 6, Σ T_g2 = 1·T_E6(27) = 3 | 4: (3,7)+(6,1) · (3,7)+(6̄,1) · (3̄,7)+(6,1) · (3̄,7)+(6̄,1) |
| + exact conformal weight h_A2 + h_G2 = 2/3 = h(27 of (E₆)₁) | 4 (all pass) |
| + su(3) cubic anomaly Σ = 0 (forced: **E₆ has no cubic Casimir**, so every restriction of the 27 is anomaly-free on any su(3) factor; A(3)·7 + A(6) = 7+7 = 14 kills the crossed pairings) | **2 — the conjugate pair** |

**27 = (3,7) ⊕ (6̄,1), unique up to overall conjugation** (verdicts below are conjugation-invariant). **Diff vs B873:** agrees with its cited Slansky branching and reproduces its x = (2,1) T-arithmetic; the conformal-weight and anomaly filters are this cell's additions — the branching is now *derived*, closing the last citation on this row.

## 2. Conventions stated (E23 class) and the criterion's bite (MB12)

**C1.** Generation content = the branching of the **full 27** (B861's uniform object). **C2.** Registerable(g→h) = the multiset of **non-abelian** irreducible content of the descended generation is complex; **all** u(1) charges stripped ("dial-stripped", B860/B861). This convention is *pinned by the banked corpus*: B863's row (a) [su(2)→u(1): {3:2, 3̄:2, 1:3} ⇒ NO] is derivable **only** under it — with charges retained that multiset would be complex and the SM would not be terminal. **C3/C4.** Menu below a product node = structural maximal reductive subalgebras: factor-wise maximals (su(3): regular su(2)⊕u(1), principal so(3); g₂: regular su(3)′, regular su(2)⊕su(2), principal su(2)₂₈; su(2): u(1)) **plus (twisted) diagonals of isomorphic factor pairs** — complete per Dynkin's classification of maximal subalgebras of semisimple algebras; the per-factor lists are classical for rank ≤ 2. This is B863's step class (its rows (a),(b) are likewise non-conformal structural descents), and every *genuine conformal* case at these levels — g₂₁ ⊃ su(2)₁⊕su(2)₃ (c = 1+9/5 = 14/5 ✓), g₂₁ ⊃ su(2)₂₈ (c = 84/30 = 14/5 ✓), su(3) ⊃ principal so(3) — is already a member of the structural list.

**Mandatory controls, all passing (7/7 + engine control):**

| control | want | got |
|---|---|---|
| E₆ → SO(10)×U(1), {16,10,1} (banked registerable, B861) | chiral | **chiral ✓** |
| E₆ → Sp(8), 27 self-dual (banked kill, B861) | not | **not ✓** |
| SU(5) → SU(4)×U(1) (banked kill, B861/B994) | not | **not ✓** |
| SU(5) → SM (banked positive) | chiral | **chiral ✓** |
| B863 (a) su(2)→u(1), {3:2, 3̄:2, 1:3} | not | **not ✓** |
| B863 (b′) su(3)₁→su(2)₄ principal (conformal case) | not | **not ✓** |
| B863 SM generation itself (positive control) | chiral | **chiral ✓** |
| **engine control**: the SM node with banked content run through the same descent engine | terminal | **terminal ✓** (B863 reproduced) |

The criterion fails and passes on the banked rows exactly as banked — failable both ways, bite demonstrated.

## 3. The descent tree (complete; 6 chains; one endpoint)

Step 1: E₆ → su(3)⊕g₂, content {(3,7), (6̄,1)} — **registerable** (complex: no (3̄,7)/(6,1) partners).

Step 2 menu (5 options): both su(3)-breakings **die** (su(2)⊕u(1): {(2,7),(1,7),(3,1),(2,1),(1,1)} all self-conjugate; principal so(3): {(3,7),(5,1),(1,1)} all real) — every su(2)/g₂ irrep is self-conjugate, so once su(3) breaks, nothing complex remains. All three g₂-breakings **survive**:

| chain (registerable steps only) | terminal |
|---|---|
| su(3)⊕g₂ → su(3)⊕su(3)′ (7→3+3̄+1) → su(3)⊕su(2)′⊕u(1) [= SM algebra, content {(3,2):2,(3,1):3,(6̄,1)}] → **su(3)** | {3:7, 6̄:1} |
| su(3)⊕g₂ → su(3)⊕su(3)′ → su(3)⊕so(3)′ (principal) → **su(3)** | {3:7, 6̄:1} |
| su(3)⊕g₂ → su(3)⊕su(2)⊕su(2) (7→(2,2)+(1,3)) → su(3)⊕su(2) (either factor → u(1); 2 chains) → **su(3)** | {3:7, 6̄:1} ×2 |
| su(3)⊕g₂ → su(3)⊕su(2)⊕su(2) → su(3)⊕su(2)_diag (7→3+3+1) → **su(3)** | {3:7, 6̄:1} |
| su(3)⊕g₂ → su(3)⊕su(2)₂₈ (principal, 7→7) → **su(3)** | {3:7, 6̄:1} |

At su(3)⊕su(3)′ the (twisted and untwisted) **diagonal su(3)** options die — 3⊗3′+3⊗3̄′+3+6̄ = {6,3̄,8,1,3,6̄} pairs up exactly (checked, not assumed: the pairing is an accident of this content, not a general fact). At the terminal node, su(3) with {3:7, 6̄:1}: both su(3)-descents die (any su(3) irrep restricted to su(2) or so(3) is self-conjugate/real), abelianization dies. **Terminal.**

**Six maximal chains; every one ends at su(3) (⊕ abelian dials), content {3: 7, 6̄: 1}** — chain-independent, because stripping the (always-real) g₂-side remnants of the 7 sends 3⊗7 ⊕ 6̄⊗1 → {3:7, 6̄:1} regardless of route. The structural reason the endpoint is forced: everything descending from the real 7 stays self-conjugate under every further restriction (conjugation commutes with restriction — B873's inheritance lemma), so chirality is confined to the unbroken su(3) factor; no descent *of* su(3) preserves a complex non-abelian multiset; hence the halt is exactly at su(3).

**Consistency check, not input:** the endpoint content is anomaly-free — 7·A(3) + A(6̄) = 7 − 7 = 0 — as it must be (E₆ has no cubic Casimir). The chiral su(3) theory with seven 3's and one 6̄ is a perfectly consistent non-SM terminus.

## 4. What this does to T8b, precisely

- **Part (ii), wide quantifier: REFUTED.** On the draft's §1 (specials-inclusive) menu there are registerable-respecting selection functions whose chains do not end at the SM — min-dim is one (E₆ → su(3)⊕g₂ [22] → su(3)⊕su(2) [11] → su(3) [8]). "Exactly six chains, all ending at the SM" is true **only** on the regular menus, exactly as the SCOPE CORRECTION restricts it. The correction is upgraded from "honest scope pending an open computation" to "the exact boundary of the true statement, with a computed counterexample beyond it."
- **Part (ii), restricted quantifier (post-correction): UNTOUCHED and now sharp.** B994's six regular chains are unaffected.
- **Part (i): UNTOUCHED, with a wording sharpening owed.** The SM algebra is terminal *for the banked generation content*; this branch exhibits the same algebra with different content ({(3,2):2, (3,1):3, (6̄,1)}) that is **not** terminal. The draft's part (i) should bind the content explicitly (it de facto does — its table is content-specific — but the phrase "the SM algebra … is TERMINAL" invites an algebra-level reading this cell now falsifies).
- **B873's "cannot win": CONFIRMED and completed.** su(3)⊕g₂ still cannot win under dimension-maximal ranking (22 < 46), and now its full descent is on the record: the menu's last uncomputed special row is closed.
- **For the terminality *story*, the finding cuts both ways and should be reported as such:** the endpoint su(3) is a genuine non-SM registerable terminus of the extended poset (a major fact *against* any hope of extending rule-independence), while simultaneously *strengthening* the restricted theorem by exhibiting exactly why the restriction is where it is. Under max-dim — the banked cascade's actual rule — nothing changes anywhere.

## 5. Honest boundaries

- **Menu class at product nodes** is the structural class (C3/C4), matching B863's step class. Under a strictly conformal-only submenu the registerable step-2 options reduce to {su(3)⊕su(2)⊕su(2), su(3)⊕su(2)₂₈} (both conformal at the induced levels; the regular su(3)′ ⊂ g₂ row is a non-conformal structural descent, same class as B863's row (b)) — **both still funnel to su(3)**, and if instead one demanded conformality so strictly that no option survived at some node, the chain would halt even earlier at a *larger* non-SM algebra. The NON-SM-ENDPOINT verdict is robust to the menu-class choice; only the name of the terminus (su(3) vs an earlier halt) could shift under a class this cell has no banked license to impose.
- The branching 27 = (3,7)⊕(6̄,1) is derived up to overall conjugation only; all registerability verdicts are conjugation-invariant, so this is no loss.
- Per-factor maximal-subalgebra lists (su(3), su(2), g₂) are classical rank ≤ 2 facts used as such; diagonals per Dynkin's product classification. No P5-style completeness import beyond these.
- Nothing here touches values, generations, real forms, or the object-side route to E₆; the two external inputs of F2 (E₆ itself, chirality) stand exactly as banked.

## Files

- `su3_g2_descent.py` — the full computation (branching derivation, criterion + controls, descent engine, tree). Run: `python3 su3_g2_descent.py`; all assertions are live (controls hard-fail the run).
- `results.json` — machine-readable: rule verifications (44/44), branching filter chain (4→4→2), controls (8/8), the tree, terminals, chains, verdict.
- `branching_data.json` — every branching rule used, with its verification method.
