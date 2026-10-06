# B1483 — ADDENDUM (2026-10-07, post-seal): why exactly the golden and silver words were the exceptions — the cusp lattice is hexagonal or square there, and nowhere else

**What R2 left.** On 32 of the 34 amphichiral − word states the two classes of spin structures put non-isomorphic
(complex-conjugate) elliptic curves at the cusp; on −LR (m003) and −LLRR (m135) the end curves have real j. FINDINGS
said these are "the golden and silver words, the two arithmetic ones", and gave no reason.

**The reason — a lemma.** On a − state the mirror is rhombic at the cusp with fixed class L, and every spin structure
has σ(L) = −1. The two classes of spin structures are the two characters σ₊, σ₋ of the cusp lattice Λ (mod 2) that are
−1 on L; the mirror exchanges them. So the end data (E, σ₊) and (E, σ₋), E = ℂ/Λ, are complex conjugate.

> **They are isomorphic if and only if Λ has an automorphism of order greater than 2 — that is, if and only if the
> cusp's own curve is the hexagonal one (j = 0) or the square one (j = 1728).**

*Proof.* An isomorphism (E, σ₊) → (E, σ₋) is a rotation u of Λ carrying σ₊ to σ₋. The rotations ±1 act trivially on
Hom(Λ, ℤ/2), so u has order 3, 4 or 6, and Λ is hexagonal or square. Conversely: the rotation of order 3 of the
hexagonal lattice permutes its three non-zero characters mod 2 cyclically, so some power carries σ₊ to σ₋; and on the
square lattice ℤ[i] a rhombic mirror fixes the class of 1 + i, the two characters that are −1 on it are (+, −) and
(−, +) on (1, i), and multiplication by i exchanges them. □

**The check** (`verification/exceptions_explained.py` → `exceptions_explained.json`): the modulus of the cusp's own
curve on all 68 amphichiral word states, from the shapes stored by the sealed run. It is real on all 68 (an
amphichiral cusp). It is 0 or 1728 on exactly two — **−LR, hexagonal, and −LLRR, square** — and those are exactly the
two − states whose end curves are real. On the 34 + states every end curve is real, as R1 found, for a different
reason: there the mirror fixes the spin structure.

**What it adds, and what it does not.**
- R2's "32 of 34" is now a statement with its exceptions derived: **at the boundary, the hand of a − state is visible
  in the end datum unless the cusp lattice has a symmetry of order 3 or 4.** The lemma is about the pair (E, σ); that
  the curve E_s alone already has non-real j on the other 32 is the census fact of R2 and is not proved here.
- On the two exceptional states the two classes of spin structures cannot be told apart by anything read from the cusp
  lattice with its sign character. They are still told apart by the phase of B1481 (m003: ±π/3 at t = 1).
- The two exceptions are the − states of the two arithmetic words, the same two on which B1481's phase showed a number
  field; and m135 is one of the two states where the SM seat's frame reads its one generation (sm:B1530). That
  co-occurrence is recorded, not explained, and nothing is built on it.

**Status.** Post-seal: written after the sealed cells returned, on their stored output; the lemma is proved on this
page; the check ran once. It changes no sealed prediction's outcome and creates no law beyond T-END-CURVE's.
