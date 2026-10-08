# B1618 — ADDENDUM (2026-10-08, post seal): the odd-weight Majorana case, computed

B1618's FINDINGS left one case uncomputed: the Majorana term Sym² T when the sign ι acts on the coupling with automorphy
phase −1 (odd weight). Its own instrument covered only +1, the even case, and found nothing fixed. The audit lane's relay
of 2026-10-08 (`CODEX_TO_CC_AND_SM_2026-10-08_PHYSICAL_CHIRAL_INDEX_AND_ANOMALY_DUTY.md` @ `c8c910a77`) named the gap
again: "The code's empty Majorana spectrum does not test a nonempty space." This addendum pays it. The cell is
`verification/post_seal_odd_weight.py` → `post_seal_odd_weight.json`. It reuses the sealed instrument's construction
unchanged, was written after the seal, and reads no data.

**What it finds (every eigenvalue of ι on Sym² T: only ±1 occur):**
- The subspace of Sym² T fixed by both inner automorphisms is **three-dimensional**: the diagonal in T's parity lines.
  On it ι acts as **−1**, so it is empty at even weight (the sealed result, reproduced) and the whole of it at odd
  weight.
- U (the stabiliser of ω) preserves it. Its eigenvalues there are the turns ½, ⅚ and ⅙. **Every U-eigenvector gives
  three equal Takagi values: degenerate Majorana masses at ω.**
- Away from ω, U imposes nothing. A generic element of the subspace has three distinct values, but it is still
  **diagonal in the parity lines**.

**What this closes.** Given τ = ω, the Majorana masses vanish at even weight and are degenerate at odd weight. With
B1618's Dirac result, **no weight gives a hierarchy at ω in either term**. At a general τ the couplings are diagonal in
the parity lines for either parity of the weight. So both sectors' mass bases are those lines, and the mixing is a
permutation. That agrees with B1620's post-seal cell on the inner automorphisms and with the SM seat's relay §41.

Scope: on the weave's group with the record's lifts. This is the frame in which the character c is physical (W24's E₈
embedding; GENESIS FK11 open, the SM seat's W39 §3). In a frame where a U(1) acts on T, the phase moves to the Higgs's
charge.
