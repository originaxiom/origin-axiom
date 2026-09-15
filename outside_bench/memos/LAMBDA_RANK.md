# THE λ-TERM'S RANK — B1206's own named CHEAPEST closer, computed and CLOSED NEGATIVELY: the rank is 2, but the 2 is the SU(2) ε tensor, and rank 1 is impossible
## (outside bench memo 128, 2026-08-29; certificate `certificates/lambda_rank.py`, GREEN; the owner's GO on the bench's ranking)

**The setting.** B1206 (banked, verdict OPEN) moved the ℙ³ row from
*"no linear conditions exist"* to **"exactly one exists; the forcing is
one condition short"**:

| step | source | dim |
|---|---|---|
| the Higgs line ℙ(B₀) | — | 3 |
| − 1 canonical linear condition | the λ-term C(N₁, H_u, ·) | 2 |
| − 1 nonlinear condition | det Y_d(h) = 0 (B1205) | **1** |
| points require | | 0 |

It named three candidates for the missing condition and called
**(iii) the λ-term's own rank** *"the cheapest"*: banked as *"2 nonzero
entries in one functional, but if the underlying map has rank 2 rather
than 1 the ledger closes immediately."* The row it cites is **memo
80's**, byte-verified at B1171 — and memo 80's certificate is on this
bench, so the cheapest closer was computable here with **no new
mathematics**: memo 80's Jordan-cubic construction is imported
verbatim (the exhaust-before-building rule), not re-derived.

- **L2 — the λ matrix, exact.** On memo 80's roster (Hu = [14, 22],
  Hd = [16, 18], neutrals [1, 17]): **N₁ → 2 nonzero, N₂ → 0** — the
  banked row reproduced entry-for-entry. The block is
  **[[0, 1], [−1, 0]]**, and its **rank over ℚ is 2**.
- **L3 — the full docket form.** C(N₁, ·, ·) on B₀ = Hu ∪ Hd is
  symmetric of **rank 4** (nondegenerate); C(N₂, ·, ·) is identically
  zero.
- **L4 — B1206's candidate (i), free in the same cell.** The
  exotic-mass row D·Dᶜ·N₁: **3 nonzero, rank 3** (a permutation
  matrix); N₂ → 0.

## ⚠ IN-RUN CORRECTION — THE PREREGISTERED FORK IS ILL-POSED, AND THAT IS THE FINDING

The fork written before the run said **rank 2 ⟹ two independent
conditions ⟹ the ledger closes**. The run returned rank 2. **It does
not close**, and the reason is structural rather than a patch:

- memo 80's Hu is **two states with t₃ = −1 and +1** — the two SU(2)
  components of **one doublet** (its own docstring: *"Higgs docket
  4 = 2 doublets"*); likewise Hd.
- **L5, the t₃-conservation gate:** all **45** nonzero C triples have
  t₃ summing to zero (proved here, exactly parallel to memo 80's
  Y-conservation gate). **Therefore the Hu × Hd block is forced
  antidiagonal, its rank lies in {0, 2}, and RANK 1 IS IMPOSSIBLE** for
  any doublet–doublet–singlet coupling.
- The observed block **is** the **SU(2) ε tensor**. Rank 2 measures the
  **nondegeneracy of ε — the gauge group** — not a second condition.

**A fork whose branches are "impossible" and "always" decides nothing.**
The correct instrument is the number of **gauge-invariant functionals**,
and that is **ONE**: N₁ · ε^{ab} Hu_a Hd_b.

**The same trap on candidate (i):** the **colour-conservation gate**
(also PASS on all 45 triples) forces the D × Dᶜ block to be a
permutation matrix, so its rank lies in {0, 3} and the 3 is the **SU(3)
δ contraction**. **One** invariant functional there too.

## THE VERDICT

**B1206's candidate (iii) — its own named cheapest closer — is CLOSED
NEGATIVELY, for a structural reason rather than a count coming out
small. Candidate (i) is closed negatively by the same argument in the
same cell. B1206's ledger STANDS at dim 1: the ℙ³ is still exactly one
condition short.**

**All three named candidates are now negative.** (ii),
doublet–triplet splitting, is typed **EXTERNAL and colour-choice
dependent** by B298/B299 — banked, re-read for this cell — so by
B1206's own statement it cannot supply an object-side condition.

**What that does and does not mean.** It does **not** prove no
condition can exist. It proves **the record's named routes are
exhausted**, which is materially stronger than "not yet found". The
consequence is that **B1196's CLOSED-PERMANENT verdict on the ℙ³ is
HARDENED, not overturned**, and any future closer must come from a
source none of the three candidates names.

## CROSS-SOURCE FINDING, filed for the primary record

memo 80's roster counts **STATES** (Hu 2, Hd 2, docket 4 = 2 doublets);
B1206's ledger leans on **B1161's sector table Q/dc/Hd/Hu = 3/3/4/1**,
which counts **GENERATION MULTIPLICITIES**. These are different spaces,
and **B1206's cited datum comes from the first while its ledger is
built on the second.** Under the second reading Hu is pinned and the
λ-term is one functional by construction — **the same answer this cell
reaches on the first**, which is why the verdict is robust across the
mismatch. The mismatch itself does not change the count either way, but
it should be reconciled in the primary before the ledger is quoted
again.

**Fences.** Zero/nonzero patterns, ranks and counts only; nothing here
asserts that any coupling takes any value or that the λ-term must
vanish. Gate 5 untouched.

### ⚠ ADDENDUM 1 (2026-08-29) — BENCH ERROR #13, caught by CODEX and UPHELD: the exclusion of rank 1 needs FULL SU(2), not Cartan conservation
codex's audit of B1205–B1208 states: *"**full SU(2), rather than merely
Cartan conservation, forces the lambda block to rank zero or two**."*
**They are right and this memo was wrong.**

This memo argued: t₃-conservation ⟹ the Hu × Hd block is antidiagonal ⟹
**rank ∈ {0,2}, rank 1 impossible.** **The last step is a non-sequitur.**
An antidiagonal block [[0,b],[c,0]] with **exactly one** nonzero entry has
**rank 1** — and it conserves t₃ perfectly. Verified: (b,c) = (1,0) and
(0,1) both give rank 1. **Cartan conservation does not exclude rank 1.**

**What does:** full **SU(2)** invariance. The invariant pairing of two
doublets to a singlet is **unique up to scale** (ε^{ab}), so the block must
be λ·[[0,1],[−1,0]] — rank 0 or 2, never 1.

**The verdict is unchanged:** the observed block *is* ε, and the count of
gauge-invariant functionals is still **one**. **The stated reason was too
weak**, and is repaired in the certificate. The same repair applies to the
colour block: it is full **SU(3)** invariance (the unique δ^i_j
contraction), not Cartan colour-weight conservation, that forces rank
∈ {0,3}.

**Credit: codex.** This is the second time an outside seat has corrected
this bench on a *reason* while leaving the *result* standing — the pattern
worth keeping. This addendum is the only mutation.
