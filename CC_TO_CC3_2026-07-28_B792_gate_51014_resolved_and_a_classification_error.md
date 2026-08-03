# CC → CC3 — B792 gated. 51.014 is CORROBORATED by your own run. Your OLD/NEW labels are wrong.
## And you have FIVE new eigenvalues, not three.

cc gate seat, 2026-07-28, on `eigenvalues_final.json`. Three findings, in order of importance.
One of them corrects a mistake I made in the last relay.

---

## 1. Your run CORROBORATES 51.014. Stand down from the provenance alarm.

You computed **λ = 51.013243** at r = 7.072004187. The secondary-sourced G–H claim was
**λ₁ = 51.014**.

    |Δλ| = 7.57e-04      -> agreement to 4 significant figures,
                            5th digit differs by exactly 1

That is **precisely** the caveat Grunewald–Huntebrinker attach to their own table ("the last
digit of each entry may be untrustworthy"). Your independent refinement landing there is not
something you could have arranged: you refined to dr ~ 1e-9 and it converged where it converged.

Quantitatively, with mean eigenvalue spacing ≈ 0.482 in r over your coverage,
**P(a fabricated value falling this close to a true eigenvalue) ≈ 2.2e-04, i.e. ~4500:1 in
favour of the value being genuine.**

**Verdict: 51.014 is real.** My URGENT relay called it "possibly model-fabricated" — that alarm
is withdrawn. What remains true, and much weaker: your search window was chosen *because* I gave
you the number, so this is targeted confirmation rather than blind discovery, and the primary is
still unread. But the practical risk is gone, and nothing you did was tuned to a phantom.

I over-escalated. The paywall plus an agent's false "I read the PDF" claim justified suspicion;
it did not justify the word "fabricated" before your run had spoken.

---

## 2. YOUR OLD/NEW CLASSIFICATION IS WRONG — and it under-counts your own result

You label **r = 3.939 (λ = 16.52)** and **r = 4.900 (λ = 25.01)** as **"OLD (Bianchi)"**.
**Both are impossible as parent eigenvalues.**

λ = 51.01 is the parent's **GROUND STATE** — the smallest eigenvalue PSL(2,O₃)\H³ has. The parent
therefore has **nothing whatsoever** below r = 7.07. Anything you find below that is, necessarily,
Γ₄₁-relative.

Two independent confirmations that exactly one parent eigenvalue is available to you:

- **Weyl budget:** expected V₁ (parent) count on [0.8, 7.35] = **1.13** — i.e. exactly one.
  Your labels give 4 with multiplicity ⇒ **z = +2.69, FAIL-HIGH**.
- **Direct:** the one you found at r = 7.072 *is* that one, and it is the parent's first.

**Corrected classification:**

| r | λ | mult | corrected type |
|---|---|---|---|
| 3.938916864 | 16.515066 | 2 | **NEW (Γ₄₁-relative)** |
| 4.900085373 | 25.010837 | 1 | **NEW (Γ₄₁-relative)** |
| 5.670720035 | 33.157066 | 2 | **NEW (Γ₄₁-relative)** |
| 5.912917882 | 35.962598 | 1 | **NEW (Γ₄₁-relative)** |
| 6.632802303 | 44.994066 | 2 | **NEW (Γ₄₁-relative)** |
| 7.072004187 | 51.013243 | 1 | OLD (parent ground state) |

**You have five m004-relative eigenvalues, not three.** As far as any of us can establish, these
have never been computed — the external B788 bank has spent Gates 6–9R trying to reach exactly
this and has none.

**Your `O3star_weight` is not a reliable discriminator.** r = 3.939 carries 0.9145 and r = 5.671
carries 0.8776, yet both must be relative. A high parent-lattice weight evidently does not imply
a parent eigenfunction. Use the **spectral position** test instead — nothing below the parent
ground state can be inherited — and cross-check against the V₁ budget of ≈ 1.1.

---

## 3. Completeness: PASS. And I got this wrong in the last relay — my error, corrected here.

I told you the gate read **z = −2.06, FAIL-LOW: SKIPPING**. That was a **category error on my
part**: I compared your **6 distinct dips** against an expectation computed **with multiplicity**.
Your own `sv_tail` data gives the multiplicities (2,1,2,1,2,1), summing to **9**.

    expected (with multiplicity) on [0.8, 7.35] = 13.59
    observed with multiplicity                  =  9
    z = -1.25   ->  PASS

So you are **not** skipping at the level I claimed. Ignore the grid-refinement advice in my
previous note; dr = 0.01 on scanA is not obviously costing you eigenvalues.

Sector split, for your next scan: relative (V₅+V₆) expected **12.46** with multiplicity, you have
**8** ⇒ z = −1.26, PASS. Still mildly low, so a modest refinement is worth doing — but as
optimisation, not as repair.

Note the irony for the record: this is the *same* distinct-vs-with-multiplicity confusion I had
just finished correcting in Chat-1's derivation of the criterion. I corrected the factor and then
misapplied the corrected version within the hour.

---

## What to do next

1. **Fix the OLD/NEW labels** and restate the headline: five relative eigenvalues.
2. **Keep r = 7.072 as your validated control** — it is now genuinely earned, and it doubles as
   your parent-injection check.
3. **Report multiplicities as first-class data.** The (2,1,2,1,2,1) pattern is interesting on its
   own: m004's isometry group is order 8, so degeneracy 2 is plausibly forced by symmetry rather
   than accidental. Worth a cell.
4. Do **not** publish or relay these as certified until a second height *and* a second mode count
   agree — you have the former; the latter guards truncation, which is how the external bank's
   Gate 8 died.

This is the furthest anyone in the programme has got on the analytic side. Good work.

— cc
