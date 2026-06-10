# B149 — is B89's family the COMPLETE solution variety? (H1, refocused)

**Question.** B89 proved M⁴=L exact over ℚ(ω) on a *posited* 4-parameter family of SL(4) figure-eight bundle reps
(A-spectrum {1,1,ω,ω²}). Is that family the **complete** solution variety of the defining ideal, or are there other
components where M⁴=L is unchecked?

**Answer — OUTCOME (a).** B89's family is the **complete component of irreducible** bundle reps, and **M⁴=L holds on
all of them (unconditional on the irreducible locus)**. The full ideal has more components, but they are exactly the
**reducible** (rank `Q≤1`, `Q=0`) and **vacuous** (`det t=0`) loci — not genuine bundle reps (MB7).

**How.** The defining ideal `I` (10 quadratics, `S=tAt` off-pattern, 16 vars over ℚ(ω)) is decomposed by gauge-rank of
the coupling block `Q=t[0:2,2:4]` (`rank 2 / 1 / 0` exhaust all reps up to gauge):
- **rank Q=2** (B89's): exactly **2** components — B89's family (`det≠0`) + a vacuous (`det≡0`) branch; **M⁴=L on both**
  by exact ideal membership. (symbolic, `decomposition.json`)
- **rank Q=0**: **reducible — exhibited** (`Q=0` ⇒ `span(e₂,e₃)` invariant). (symbolic)
- **rank Q=1**: vacuous or reducible.
- **Irreducibility** decided by **Burnside (algebra-dim=16)** exactly over **F_p** (two primes): the only stratum with
  irreducible reps is rank Q=2 = B89's family; decisive cell (irreducible ∧ M⁴=L fails) = **0**. (`irreducibility_fp.json`)

**Why the careful test.** The Schur **commutant test is invalid** for irreducibility (a reducible *non-semisimple* rep
can have commutant = scalars) — it spuriously flagged the provably-reducible `Q=0` stratum as irreducible. The correct
**Burnside** test, validated against the `Q=0` symbolic exhibit, gives the clean result. (See FINDINGS "Methodology
note".)

**Files.** `probe.py` (pyenv: ideal, B89-family-in-V(I) gate, M⁴=L identity, `Q=0`-reducible exhibit, `algebra_rank`),
`decompose.py` (sage: stratified `minimal_associated_primes` + per-component M⁴=L membership → `decomposition.json`),
`classify_fp.py` (sage: exact F_p Burnside classification → `irreducibility_fp.json`), `FINDINGS.md`,
`../../tests/test_b149_sl4_ideal_completeness.py` (6 passed).

**Run.** `python -m pytest tests/test_b149_sl4_ideal_completeness.py -q` (pyenv).

Ledger **V138**. Anchors: B89, B73, B71, B95, `../B89_sl4_symbolic_M4L/`.
