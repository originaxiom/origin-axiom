# THE FOUR DISTINGUISHED PARITIES — C-P1 closed: the 20-row stratum dictionary complete from scratch, the projective count is exactly 9, and the one lift-sensitive distinguished stratum sits under the beat
## (outside bench, 2026-08-25; thirtieth memo — the first banked in the corpus repo's `outside_bench/` lane; every claim exact)

### The cell (opened by memo 2, 2026-08-21)
`PROJECTIVE_HATCH` classified the 16 Levi-regular strata of e₆ by the parity of their
27-spectrum — projective (all weights even) = the composed holonomy φ∘ρ is independent
of the SL(2,ℂ) lift; odd = the stratum reads the spin bit — and found 6 projective. The
**4 distinguished-non-regular strata were left unclassified**, the projective count
bounded 6–10. C-P1: classify them. After memos 28–29 the cell gained stakes: odd strata
are the fermion-capable ones, and the beat selects the lift they must live over.

### THE THEOREM (`certificates/cp1_strata.py`, all exact over ℚ; no literature input)
1. **The complete characteristic census, from first principles.** For every dominant
   labeling c ∈ {0,1,2}⁶, H_c is the weighted-Dynkin element of a nilpotent stratum iff
   a generic e ∈ g(2) admits f ∈ g(−2) with [e,f] = H_c — then (e, H_c, f) is an exact
   sl₂-triple (the gradings supply the other two relations) and dominance makes H_c the
   stratum's label. Sweeping all 729 candidates with exact linear algebra:
   **exactly 20 nonzero characteristics** — E₆'s full nonzero-orbit count, REPRODUCED,
   not assumed. Every claimed triple is verified by exact brackets before acceptance.
2. **The 16 Levi-regular rows re-derived independently** (2ρ∨ of each of the 63
   simple-root subsets, reflected to dominance, deduped): 16 distinct, all among the 20 —
   memo 2's census confirmed by a different construction.
3. **The four distinguished-non-regular strata** are the leftovers, with exact orbit
   dimensions 58, 64, 66, 70 (labels in the bench's simple-root order):
   | label c | dim O | 27-spectrum | parity |
   |---|---|---|---|
   | (0,0,0,2,0,0) | 58 | {±4:3, ±2:6, 0:9} | **even — projective** |
   | (1,2,1,0,1,1) | 64 | {±7:1, ±6:1, ±5:2, ±4:1, ±3:2, ±2:2, ±1:3, 0:3} | **ODD — lift-sensitive, fermion-capable** |
   | (2,0,0,2,0,2) | 66 | {±8:1, ±6:2, ±4:4, ±2:4, 0:5} | **even — projective** |
   | (2,2,2,0,2,2) | 70 | {±12:1, ±10:1, ±8:2, ±6:2, ±4:3, ±2:3, 0:3} | **even — projective** |
   (Naming, CITED for orientation only — the computation nowhere uses it: the dims
   58/64/66/70 are the standard D₄(a₁)/D₅(a₁)/E₆(a₃)/E₆(a₁) of Collingwood–McGovern.
   Consistently, the one non-even label — the D₅(a₁) row, with 1's in c — is the one odd
   spectrum.)
4. **The full dictionary, every parity recomputed from scratch:** projective strata =
   6 of 16 Levi-regular (memo 2's six, re-verified in this same run) + 3 of 4
   distinguished = **9 of 20, exact**. Memo 2's bound 6–10 lands on 9.
5. **The beat covers the new odd stratum.** For the lift-sensitive distinguished
   stratum, with its exact JM triple (e, H, f): the composed matter rep satisfies the
   relator = +I, and Ω = exp(ρ₂₇(qe)) ∘ gal obeys **Ω² = A₂₇** with both intertwinings
   exact — memo 29's functorial mechanism (W = exp(q·e) upstream; e's coefficients
   rational, hence Galois-fixed, hence Ω² = exp((q+q̄)ρ(e)) = A₂₇) checked on the nose.

> **Therefore C-P1 is CLOSED: the 20-row stratum/parity dictionary is complete and
> exact. Nine strata are projective — reachable by the object's bare PSL(2,ℂ) geometry
> with no spin bit. Eleven are lift-sensitive — and every one of them lives over the
> single lift the object's own beat selects (memo 28), closing under the beat exactly
> where checked (memo 29's A1 seat; the distinguished row here). The parity ledger of
> the landing has no unclassified rows left.**

### What this changes, and what it does not
The repricing of memo 2 sharpens: the projective menu is exactly 9 (log₂9 ≈ 3.2 bits of
lift-free class choice, still 0 bits SM-facing — the trinification landing remains the
unique projective SM-compatible row, untouched here). The fermion-capable side gains one
distinguished member (dim 64): fermionicity is not a Levi-regular privilege. NOT
claimed: any physical role for the distinguished strata beyond their parity type;
dynamics; values. Gate 5 untouched.

### Fences
The census control is two-sided: false positives are impossible (every accepted H comes
with an exactly verified sl₂-triple), and false negatives (a genericity miss in the
random e-draws) are excluded by the count itself landing on 20 — one miss would leave
19. Deterministic seed; re-runs reproduce byte-identically. The orbit names are CITED
decoration; every load-bearing number (the census, the dims, the spectra, the parities,
the beat closure) is computed in the certificate.

### Certificates
`certificates/cp1_strata.py`; output `outputs/cp1_strata_out.txt`. Machinery:
the vendored `certificates/twisted_double.py` stack (ρ₂₇ verified on all 3003 brackets
in-run).

### CODEX ADDENDUM (adopted 2026-08-25, from codex/seat-r001 R003 Wave 1 — the fourth bench's hostile verification of this memo; corrections filed at point of occurrence)
1. **Reproduction:** `cp1_strata.py` re-run isolated (SHA-256-locked source,
   Python 3.12.1 / SymPy 1.14.0), exit 0, byte-identical output; all four
   distinguished rows confirmed exact.
2. **Their extension, adopted with credit:** the selected-beat identities verified on
   **ALL ELEVEN odd rows** (`verify_cp1_all_odd.py`, keyed to this certificate's
   hash) — this memo checked the odd distinguished row and memo 29 the Levi A1; the
   campaign's spine coverage over strata is now complete by the codex computation.
3. **Sharpened fence, ADOPTED — census completeness:** every accepted row carries an
   exact bracket-verified sl₂ witness (the positives are sound), but absence for
   rejected labels is NOT algebraically proven — four seeded generic trials failing
   is not a nonexistence proof, and the `len == 20` control leans on the CITED
   Bala–Carter count. Reclassification: the census is EXACT-POSITIVE +
   CITED-COMPLETE, not independently complete. (An independent completeness proof —
   exact genericity certificates for the solvability rank condition, or an
   exhaustive structured e-search — is the named follow-up.)
4. **Scope sharpening, ADOPTED in the codex's crisper form:** since the 9 projective
   rows need no lift and all 11 odd rows accept the selected-beat construction,
   **beat-compatibility selects 0 of the 20 rows** — the beat is a functorial
   compatibility mechanism AFTER a stratum is chosen, not a selector of the A1
   landing, a fermion construction, or a generation theorem. What the beat selects
   is the LIFT (χ = +1, memo 28); what selects among strata is projectivity/geometry
   (memo 2) — two different mechanisms, now cleanly separated. B1145's internal-A1
   fence propagates unchanged.

### One sentence for the ledger
The four rows memo 2 could not reach are reached: one is fermion-capable and three are
projective, the dictionary stands complete at 9 projective of 20 with nothing
unclassified, and every stratum that can carry matter now provably sits on the one side
of the spin fork the object itself selected — the parity story of the landing is over.
