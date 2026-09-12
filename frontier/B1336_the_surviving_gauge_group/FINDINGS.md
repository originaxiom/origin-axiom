# B1336 — the surviving gauge group: I-26's "untouched" half, and it is abelian or nothing

**Verdict: NEGATIVE**, with a theorem. This pays part of a named price and the answer is a
constraint, not a licence.

## What was owed

`docs/IDENTIFICATION_LEDGER.md`, I-26 — the row every generation count in the corpus is conditional
on (B1253, B1255, B1256, B1257, and the `h^1` readings of B1036/B1086):

> *"**Naming the surviving gauge group — the centralizer of `rho(pi_1)` — remains part of the price
> and is untouched.**"*

Its other half was paid at B1295 (`chi(d+M) = 0` by computation). This is the untouched half.

## The distinction the corpus has not drawn

B854 computes the centralizer of **2T**, the *finite* McKay image, and gets `u(1)^4`. But the
object's geometric holonomy is **discrete and faithful**, hence a lattice in `PSL2(C)`, hence
**Zariski-dense** (Borel density). For a Zariski-dense subgroup the centralizer is that of the whole
`SL2` — strictly smaller than the finite group's. **The two questions have different answers, and
the corpus has been using the finite one where the row asks about the holonomy.**

Computed exactly over `Q` on B854's E6 Chevalley algebra, its own controls re-run first:

| holonomy image | centralizer in `e6` |
|---|---|
| **2T**, the finite McKay quotient | `dim 4`, **abelian** `u(1)^4` (B854, re-verified: rank 4, all six brackets vanish) |
| **the geometric holonomy** (Zariski-dense in the principal `SL2`) | **`dim 0`** |
| *positive control:* the principal semisimple `h` alone | `dim 6` = rank `E6` ✓ |

## The theorem, which covers everything between

For any `H` with `2T <= H <= SL2` (principal), `Z(SL2) <= Z(H) <= Z(2T)`, so `Z(H)` is a
**subalgebra of an abelian algebra**:

> ### Every such `Z(H)` is abelian of dimension at most 4.
> ### The Standard-Model algebra is non-abelian of dimension 12.
> ### So no flat connection with holonomy in the principal `SL2` containing `2T` leaves the
> ### Standard-Model algebra unbroken — whatever the holonomy.

It needs no case analysis: the upper end being abelian does all the work.

## What this means for I-26

The identification reads `dim H^1(M; 27_rho)` as a count of **massless multiplets of a gauge
group**. This half of the price asks which group. The answer, on the corpus's own embedding:
**none of any size** for the geometric holonomy, and an **abelian `u(1)^4`** at best if the
connection is the finite `2T` one. There is no non-abelian gauge group for the classes to be
multiplets *of*.

**I-26 is not earned by this and the ratchet does not move** — it is made harder, and the row should
record that the surviving group has now been named and is abelian or trivial.

## Scope — what is NOT claimed

- **This constrains the flat-connection route only.** The paper's Standard-Model gauge algebra comes
  from the ninth closing `Y_9`, a closed manifold, not from the centralizer of this flat connection.
  Nothing here refutes that; it says the flat `E6` connection cannot supply the group, so the
  closing must, and the `h^1` readings on the cusped object cannot be multiplet counts.
- **The embedding is I-25, and I-25 is UNEARNED.** All of this is for the *principal* `sl2`. Other
  embeddings give other centralizers — B1303 computed `dim 2` for the regular `A1 A1 A2`. Those are
  also far from 12, but they are not covered by the theorem above.
- **Prior art, and it is not ours.** The SM-derivation seat's **sm:B1269** — *"I-26's surviving gauge
  group named for every holonomy the corpus supplies, the Standard-Model algebra is not a centralizer
  in e6"* — reached this first. It is recorded **SCHEDULED** in `docs/HARVEST_LEDGER.md` row 125
  since 2026-09-09, with *"no main text names it"*, and its arc is not in this repository. This bench
  re-derived the part above independently rather than on the seat's word; **B1269's fuller claim —
  every holonomy the corpus supplies — is NOT verified here.** The credit for the headline is theirs.

## The invisible-work note

This is the fourth instance of the pattern the record keeps catching: a seat computes something that
settles a named price, it is logged as SCHEDULED, and no main text names it. Two days of index work
were spent before this row was even read. **The harvest ledger's SCHEDULED rows should be swept
before the next campaign picks a target**, not after.

Reproduce: `verification/i26.py` (the centralizers, with the rank-6 control),
`verification/i26b.py` (the squeeze theorem). Both reuse `frontier/B854_centralizer_exact/e6_centralizer.py`,
whose own controls re-run on import. Logs in `verification/logs/`.
