# B570 Lane C, cell C3 — RESULT: the θ-odd sector is dynamically ALIVE at level 2

**Run 2026-07-14, FIRST, by owner directive** ("C3 is the decisive cell... run it first,
verify it hard, bank whatever it gives"). Reproducer: `c3_e6_level2_monodromy.py`.
Locks: `tests/test_b570_c3_level2.py`. Independent adversarial re-derivation: see
the verification note at the end.

## The computation

E₆ level-2 modular data built from scratch: all 51,840 elements of W(E₆) enumerated
exactly; Kac–Peterson S at k+h∨ = 14; T from h(λ) = (λ, λ+2ρ)/28 (h(27) = 13/21,
h(78) = 6/7, h(650) = 9/7, h(351) = 25/21, h(351′) = 4/3), c = 78/7.

**Consistency gates passed before evaluation** (the B569 lesson):
S unitary + symmetric (3e-14); S² = exactly the conjugation permutation = the θ
diagram flip; (ST)³ = S², S⁴ = I (genuine SL(2,ℤ) rep, 1e-13); **all 729 Verlinde
fusion numbers are non-negative integers** (dev 3e-14); the S-column quantum
dimensions match the independent q-Weyl-dimension product formula on all 9
primaries (two independent methods). ρ(A₁) computed via two SL(2,ℤ) words
(T²ST and T·ST⁻¹S⁻¹) — agree to 1e-13.

## The answer

> **ρ(A₁) restricted to the θ-odd 3-space is NON-SCALAR: an SU(3) element of
> order 4 with eigenvalues {+1, +i, −i} (det = 1).**
> At level 1 the θ-odd sector was inert (the scalar +1, B569). At level 2 the
> monodromy genuinely rotates the chiral-difference directions: the 27−27̄
> direction is transported into the (351−351̄) and (351′−351̄′) directions.
> The preregistered falsifier ("trivial again → the θ-odd sector is
> monodromy-blind at low level") did **NOT** fire.

Supporting exact facts: Z = Tr ρ(A₁) = **+1 again at level 2** (Tr odd block = 1,
Tr even block = 0); the θ-even 6×6 block has eigenvalues {1, 1, −1, −1, +i, −i};
the θ-split is exactly preserved (off-block norm 2e-14, forced: C = S² is central).

## What this does and does not say (firewall)

- **Does say:** chirality above the fold is DYNAMICAL — the object's monodromy
  dynamics does not factor through the θ-even (F₄-side) quotient; the chiral
  directions carry non-trivial monodromy. This is the first positive
  chirality-sector signal in seventeen campaigns, in the precise operational
  sense preregistered in Lane C.
- **Does not say:** that the monodromy "selects 27 over 27̄." It cannot — C = S²
  is CENTRAL in every modular rep, so every monodromy commutes with conjugation;
  the θ-eigenspaces are always preserved. The dynamical content lives *within*
  the odd sector, as its non-scalar order-4 rotation.
- No SM claim. The θ-odd dynamics is a property of the stage's level-2
  measurement face; whether any play can couple to it is exactly the rest of
  Lane C (C1, C2, Q-A/Q-B/Q-C) and AP4.

## The sharpest form (the S_odd handback)

The cross-seat sharpening asked: could S restricted to the θ-odd space conspire to
cancel the three distinct T-phases (13/21, 4/3, 25/21 — all confirmed exact; note
the third pair is 351−351̄ = ω₃/ω₅, not 2925 — ω₄ enters at level 3)? Computed
directly: **S_odd is NOT diagonal** — the conspiracy is ruled out by inspection:

```
S_odd = −i · [[ 0.591009,  0.736976,  0.327985],
              [ 0.736976, −0.327985, −0.591009],
              [ 0.327985, −0.591009,  0.736976]]      (unitary; entries pure imaginary)
```

The moduli are exactly (2/√7)·sin(kπ/7), k = 1, 2, 3 (verified to 6 digits) — a
7th-root sine pattern of M(2,7)-minimal-model type. **Flagged as an observation
(HINT), not banked as an identification** — the sign/phase pattern has not been
matched against the exact M(2,7) data. If real, the θ-odd sector of E₆ level 2
carries its own tiny modular world with k+h∨ = 14 → 7 arithmetic.

## Verification

Independent re-derivation by an adversarial verifier (separate implementation,
own Weyl enumeration, own conventions, sensitivity checks vs S ↔ S* and primary
ordering): see the appended note.
