# THE LONGITUDE IS THE LOCK — the boundary curve's semisimple part on the carrier is exactly the matter grading, and the cusp's entire fixed space lives inside matter
## (outside bench, 2026-08-26; fifty-first memo; the lock traced to its home in the group; all preregistered facts GREEN on first run)

### The question
Memo 50 upgraded C_Ψ = diag((−1)^(1+wt)) from a lift-comparison to a π₁- and
beat-invariant grading operator (matter = +1). An invariant grading operator
that commutes with everything invites one question: **where in the group does
it live?** The answer is the boundary.

### THE FACTS (`certificates/longitude_lock.py`, all exact over the pair field ℚ(q); preregistered as asserts, GREEN first run)

- **FACT 0 (anchor).** tr ρ₂(λ) = −2 exactly for the longitude λ = bABaaBAb
  — the banked lift, re-verified in-run. So ρ₂(λ) = (−I₂)·(2-step unipotent).
- **FACT 1.** C₂₇ = (−1)^wt commutes with the entire internal image (A₂₇,
  B₂₇ and inverses, entrywise weight-parity) — the 27-level analogue of memo
  50's FACT B.
- **FACT 2.** C₂₇·ρ₂₇(λ) is unipotent with nilpotency degree exactly 2:
  **ρ₂₇(λ) = C₂₇ · (2-step unipotent).** The internal A1 bridge sends the
  −unipotent class to the internal lock times a unipotent drift. (Mechanism:
  under the bridge's SL₂, −I acts on the 27 — weights {±1, 0} — as (−1)^wt,
  which *is* C₂₇.)
- **FACT 3.** On the carrier, C_Ψ commutes with ρ_Ψ(λ), and C_Ψ·ρ_Ψ(λ) is
  unipotent with nilpotency degree exactly 3 (two nontrivial 2-step tensor
  factors, depth 2+2−1 — the same composition law as memo 49).
- **FACT 4.** Therefore, by uniqueness of the multiplicative Jordan
  decomposition (C_Ψ semisimple of order 2 commuting with the unipotent
  part, both asserted directly):
  **ρ_Ψ(λ) = C_Ψ · U_λ — the semisimple part of the longitude on the
  carrier IS the lock operator.** The matter/non-matter distinction is not
  an operator imposed from outside: it is the eigenvalue grading of the
  boundary curve itself. The cusp's two generators divide the labor — the
  meridian supplies the clock (memos 49/50), the longitude supplies the sign.
- **FACT 5 (measured).** The joint cusp-fixed space
  {v : ρ_Ψ(μ)v = v and ρ_Ψ(λ)v = v} has dimension **12**, and imposing
  "vanishes on the unlocked sector" leaves the dimension unchanged: **the
  carrier's entire cusp-fixed space lies inside matter.** (On the unlocked
  sector the longitude's semisimple eigenvalue is −1, so no fixed vector can
  have support there — the containment is forced by FACT 4 and confirmed by
  exact rank.)

> **THE LONGITUDE IS THE LOCK: ρ_Ψ(λ) = C_Ψ · (3-step unipotent). The
> grading whose +1 sector is the 24 fermion-shaped slots (memo 46), which
> equals clock-depth parity (memo 50), is the semisimple part of the
> boundary curve. What the cusp holds completely still — a 12-dimensional
> space — is matter and only matter.**

### The convergence, stated once
Four independently-run computations now name the same 24-dimensional sector:
memo 46 (lift-independence), memo 47 (the Yukawa's selection rule), memo 50
(odd clock chains), memo 51 (the longitude's +1 eigenspace). Each was
preregistered separately; each is exact. The record's matter sector is
massively over-determined — which is what "structural" is supposed to mean.

### A derived observation (exact, from banked numbers)
Memo 50: dim(ker N ∩ locked) = 24 − 12 = 12 — the meridian's fixed space
inside matter. FACT 5's joint fixed space is also 12. So **the longitude
fixes everything the meridian fixes in matter**: within the locked sector,
λ-invariance imposes nothing beyond μ-invariance. The peripheral ℤ² acts on
matter through its meridian factor alone at the fixed-vector level.

### What this feeds
- Memo 37 (the blanket blind spot: the cusp character is blind to the
  interior bit) now has a dual: what the cusp *does* see of the carrier —
  its fixed space — is purely matter. Boundary-blindness and
  boundary-fixing both single out the same structures.
- The dynamics gate (THE_CORE_QUESTION §6): the boundary curve carrying the
  matter sign as its semisimple part is one more exact identity in the
  "reflection–time" cluster (β² = μ, memo 46; now λ_ss = C_Ψ).
- For the seat: memos 49–51 form a natural arc (TRACE THREE → ODD STEPS →
  LONGITUDE) and should be harvested together.

### Fences
"Multiplicative Jordan decomposition" uniqueness is the standard theorem,
invoked with both hypotheses (semisimplicity and commutation) verified
in-run; every number is asserted. The bridge-factorization reading in FACT
2's mechanism sentence is motivation; the computation is on the word itself,
no factorization assumed. Interpretive glosses ("what the cusp holds still")
labeled by position, as always. Kinematics only; Gate 5 untouched.

### Certificates
`certificates/longitude_lock.py`; output `outputs/longitude_lock_out.txt`
(vendored copy re-run in-lane, byte-identical).

### One sentence for the ledger
The boundary curve of the object acts on the carrier as the lock times a
three-step drift — matter is the +1 eigenspace of the longitude, time is the
odd chains of the meridian, and the twelve dimensions the whole boundary
holds fixed are all of them matter.
