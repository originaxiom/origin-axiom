# B369 (W2.9) — the concatenation-kill test: gluing the blocks kills the seam

**Status: banked (frontier). The pre-registered prediction HIT (6/6 words seam-null), plus one design-error
gate diagnosed into an exact structural identity (rotation acts on the Par-readout by the √5-Galois
involution). Campaign W2.9. Firewalled; nothing to `CLAIMS.md`.**

## The question and the registered prediction

The seam is a PAIR observable: `tr(Par·P_a(W_{m₁})·Q_b(W_{m₂}))` carries `√−15` (B358–B367). The two-block
word `R^{m₁}L^{m₁}R^{m₂}L^{m₂}` is a SINGLE once-punctured-torus bundle built from the same blocks — its
theta lift is the product of the seed lifts, `W_word = W_{m₁}·W_{m₂}`. Registered before computing
(OPEN_LEADS W2.9): **the word's single-seed readout is seam-null** — the single-object wall holds inside
the seam observable, and gluing kills what pairing carries.

## The verdict: the prediction hit, 6/6

For words (1,2), (2,1), (1,3), (2,3), (3,4), (1,4): every nonzero eigenprojector readout
`tr(Par·P_a(W_word))`, H-averaged and solved exactly, has **zero √−3 and zero √−15 coefficients**
(`concat_kill.py`, `concat_kill.json`; all exact). In particular the **(3,4) word is clean while the (3,4)
pair is bright at Σs² = 1/192** — the sharpest form of the statement:

> **The seam lives in the unglued pair relation. Concatenating the same blocks into one monodromy kills
> it.** The single-object wall extends beyond the metallic seeds to these first non-seed single objects
> (word orders at level 15: 4, 4, 20, 20, 4, 10 — far from the seeds' 20/12/6).

Context data (no claim): the (1,2)-word's monodromy trace is 15 ≡ 0 (mod 15); its lift has order 4.

## The failed gate, diagnosed — and the Galois identity it uncovered

The first design included a naive consistency gate: cyclically rotated words ((1,2) vs (2,1)) are conjugate
— the same bundle — so their *readout multisets* were required to agree. **That gate failed.** Diagnosis:
the gate tested a non-invariant — `tr(Par·P_a)` is data of the (lift, Par) pair, not of the manifold, and
Par-conjugation in the theta lift is the nontrivial Heisenberg twist (`X¹Z²`, B358). The failure is a
design error, recorded, not weakened away; manifold-level data (order, cleanliness verdict) agree, and the
exact fine structure is:

> **Rotation acts on the Par-readout by the √5-Galois involution, exponent-wise:**
> `r₍₂,₁₎(a) = σ(r₍₁,₂₎(a))` for every exponent `a`, where σ: √5 ↦ −√5
> (e.g. a=0: (5−√5)/16 ↦ (5+√5)/16; a=2: (3+√5)/16 ↦ (3−√5)/16; rational entries fixed).

Same manifold, lift section moved by the Heisenberg twist, arithmetic moved by Galois — one more exact
instance of "the arithmetic lives in the lift sector", now on single objects. Locked as
`rotation_galois_identity` in the reproducer.

## What this changes

The June two-block word-trace lead resolves as registered: complementary to the seam channel, and now
computed — the wall's verdict-level statement generalizes off the seed family, while the sector-level
readout carries new arithmetic (the rotation-Galois action). The seam's boundary sharpens: multiplicity is
essential not just for values but against any single-monodromy gluing of the same content.

**Provenance.** B358 (engine, the X¹Z² lemma), B367 (seed lifts, matrix machinery), B361/B367 (the pair
data this contrasts with), OPEN_LEADS W2.9 (the registration). Reproducer: `concat_kill.py` (~4 min);
locks: `tests/test_b369_concat_kill.py`.
