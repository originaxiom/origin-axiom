# B1145 — SP-2: the beat closes on the fermion-capable stratum's 27 over the selected lift (exact) — the last spin-lift bit is assigned; the physical-generation reading is thesis-level, not a theorem

**Status: banked (frontier). Verdict PROVED (every identity EXACT over ℚ(√−3), verified THREE
independent ways). The single live frontier cell after the phase-III digest, sealed as a prereg
(sha256 `c384dd3e069e6963`) BEFORE the answer was known and BEFORE the cloud's memo-29 result was
seen — so this bench's derivation is genuinely blind. Harvest arc — cloud memo 29 (THE SEAT
CLOSES), re-derived on THIS bench. Gate 5 n/a (topology/representation theory, no SM value). Lock
`tests/test_b1145_sp2_fermion_seat.py`.**

## The question (the sealed prereg, one bit)

B1141 proved the object's beat SELECTS one of m004's two spin structures (χ_beat, the untwisted
lift; the twisted is forbidden by norm-form positivity). B1112 proved the fermion-capable landing
is the **odd A1/su(6) stratum** (27-weights {−1:6, 0:15, +1:6}, ODD — it needs a lift), while the
trinification A2 landing is even/projective. **SP-2 asked: does the lift the odd fermion-capable
stratum requires equal the one the beat selects?** MATCH → the generation's kinematic seat closes
on-object; MISMATCH → chirality is exiled to the E₈/2I door. Either banks.

## The answer: MATCH — SP-2 GREEN

**The mechanism (why it must close).** The A1 stratum is the minimal nilpotent; the 27 is
**minuscule**, so it restricts to that root-sl₂ as exactly **6·(fundamental 2) ⊕ 15·(singlet)** —
the twelve odd-weight (±1) states are 6 copies of the fundamental doublet (the fermions), the
fifteen weight-0 states are singlets. The beat **W = exp(q·e)** lives at the SL(2,ℂ) level,
*upstream* of the embedding, so **Ω = exp(ρ₂₇(q·e)) ∘ gal** closes on the 27 **functorially** — the
fermion doublets, being copies of the fundamental 2 on which B1141 already selected χ_beat, inherit
it. (The oddness has content: C = ρ₂₇(−I) = diag((−1)^wt) ≠ I, so the two lifts are genuinely
different matter reps; the χ=−1 side needs no rep-level check — its GROUP extension already fails,
memo 28.)

**The exact identities (own code, exact ℚ(√−3), no floats):**
- 27-weights {−1:6, 0:15, +1:6} (ODD); relator `abABaBAbaB` = +I (a genuine SL-rep over the lift);
- C ≠ I, C² = I, C commutes with A27 and B27 (oddness certified);
- **Ω² = A27** (the χ=+1 lifted meridian), **Ω·A27·Ω⁻¹ = A27**, **Ω·B27·Ω⁻¹ = ρ₂₇(B⁻¹ABA⁻¹B)** —
  all three EXACT.

## Verified three independent ways

1. **This bench, blind** — the analytical mechanism (minuscule ⇒ fundamental-2 inheritance), derived
   from the sealed prereg before any memo-29 contact.
2. **The cloud's own certificate** (`sp2_seat.py`, golden_gate) — re-run from primary source on a
   clean checkout here: reproduces every identity exactly.
3. **Independent own-code, adversarial** (`verification/sp2_independent.py`) — reuses ONLY banked
   B1102/B883 machinery (never twisted_double.py or any golden_gate path), re-certifies ρ₂₇ on all
   3003 Chevalley brackets, and passes non-vacuity checks: wrong relator words ≠ I; C-centrality is
   a real constraint (32/72 root vectors commute, 40 do not); E27² = F27² = 0 (the minuscule
   structure). VERDICT: SP-2 GREEN.

## What it establishes, and what it explicitly does NOT (codex-sharpened)

**Established (exact, three-way verified):** the object's beat closes on the odd (fermion-capable)
A1 stratum's 27 over the beat-selected spin lift — Ω²=A27, Ω·A27·Ω⁻¹=A27, Ω·B27·Ω⁻¹=ρ(w(B)), all
exact. The last discrete spin-lift bit (B1122's freedom ledger) is thereby **assigned consistently
with the fermion-capable stratum's internal structure**, not left free. That algebraic closure is
the theorem.

**Does NOT establish (the honest fence — sharpened by the codex seat's close-out audit, which
re-ran all 46 cloud certificates, confirmed this exact algebra reproduces, and banked it as
`OA-C1056` while rejecting the physical over-reading):**
- the A1 here is an su(2) **internal to E₆** (its centralizer is su(6)) — **not** the 4d Lorentz
  group; its ±1 parity is an internal quantum number, **not a 4d Weyl spinor**;
- **no Pin structure** is constructed; **no Dirac operator or index**; **no 4d chirality**;
- **three physical generations are NOT proved**;
- the "ten-word inner-modification" exhaustiveness was taken on the memo's say-so, not re-proved.

So **"the generation's seat closes on-object" is the program's THESIS reading** (the
object's-geometry → physics identification the whole programme is trying to earn) — **not a
theorem.** What *is* a theorem is the exact algebraic closure above: the last discrete bit is
assigned, on-object, by the beat. Whether that internal assignment is the *spacetime* fermion seat
is precisely the unpaid bridge (the E₆(−26) spacetime branch, B1140). Codex seat credited.

**Also fenced (as before):** fermionic *kinematics* not *dynamics* (a Dirac operator/action stays
the unpaid verb); a rep-level closure, not a field theory; no SM value enters (Gate 5 n/a).

## B1141 NEEDS-CERT — dischargeable

B1141 fenced the beat's cohomological packaging / "Galois∘Fibonacci" naming as taken on the memo's
say-so (the substance was verified). The beat trilogy (`gieseking_beat.py`, `beat_descent.py`,
`sigma27.py`) is now reachable in the golden_gate primary source, and the hardened intertwiner cert
(all four sign-twisted targets, not just the target signs) is available — so the fence is
dischargeable from primary source when promoted. The SP-2 closure above does not depend on it.

Cloud seat credited (memo 29 + the hardened cert). The value verdict is unchanged: this is
structure, not a value — the SM numbers remain closed-disjoint from every computable route.
