# THE B496 REDISCOVERY — the hunt caught this bench: memos 117/118 (and parts of 119/120) re-derived a PROVED banked arc without citing it
## (outside bench memo 121, 2026-08-28; certificate `certificates/b496_rediscovery.py`, GREEN; the owner's "hunt the repo for it"; **BENCH ERROR #11 — rediscovery without citation**)

**What B496 banks** (`frontier/B496_tm_endomorphism`, verdict
**PROVED**, independently re-derived by the banking seat via
`verify_tm.py`):

> **T1 — the TM trace map:** T(x,y,z) = **(z, z, xyz − x² − y² + 2)**
> *arc_verdict:* "The Thue–Morse trace map (z, z, xyz − x² − y² + 2)
> and its exact kappa-factorization κ′ − 2 = (κ−2)(x²+y²−xyz)
> verified, **with degree growth 2**."
> *Q1:* "**T_golden = (z, x, xz−y)** … verified to **PRESERVE κ**
> exactly"; and on κ = −2, "one T_TM sends **κ → 2 + 4z² ≥ 2 (over ℝ)**
> … a **one-way door OFF the Markov surface** (exact)."

**Verified overlap, exactly:**
- **V1:** memo 117's layering map L : (A,B) ↦ (AB,BA) **IS** B496's T1
  — identical as polynomial maps. (Of course: Thue–Morse *is*
  a↦ab, b↦ba.)
- **V2:** memo 118's closed form (z′ = z²−κ, κ′ = z²(2−κ)+κ²−2) is
  **algebraically B496's κ-factorization** in other coordinates — both
  reduce to k² − kz² + 2z² − 2.
- Memo 120's "growth exponent 2" is B496's banked **"degree growth 2."**
- Memo 119's "T_golden preserves κ, L does not" is B496's Q1, which
  also studies the mixed semigroup ⟨T_golden, T_TM⟩ — memo 119's
  [T,L] question.

**GENUINELY NEW (not found in B496 by this hunt):**
1. **THE COMPLEX EVASION.** B496's ejection bound is stated **over ℝ**:
   κ → 2 + 4z² ≥ 2. The record's own tower is **Eisenstein**: at level
   1 z₁ = 2−4ω with **z₁² = −12 < 0**, so **κ₂ = −46, below the real
   floor.** The tower does not contradict B496 — it runs in a
   direction the real case cannot see.
2. **The tower passes exactly through κ = −2 at level 1** — the
   object's own layering lands on B496's Markov surface after one
   step, then leaves it. B496's Q1(b) treats the figure-eight point
   under *one* TM event; the **iterated tower from the record's own
   (a,b)** was not run there.
3. Memo 119's involution layer (s, e, R), the full commutation table,
   and **(RT)² = id** strengthening memo 97.

**THE LESSON, recorded as standing practice:** the owner's "hunt the
repo for it" caught a rediscovery **three memos deep**. The standing
rule — exhaust the repo before claiming — has been applied before
saying *"we don't have X"*; it must equally be applied **before
building**. Gate 5 untouched.
