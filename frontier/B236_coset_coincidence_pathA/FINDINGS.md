# B236 — Path A CLOSED: the ordinary/super coset coincidence at SU(2)₃ (the H21 gate)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Run: `python coset_coincidence.py` (pyenv). Verifies chat1's Path A references by central charge.

## Result
The coset-coincidence **mechanism** behind B228 is now referenced and verified:
- ordinary `M(m,m+1)=(SU(2)_{m-2}×SU(2)_1)/SU(2)_{m-1}` (GKO 1986); super `SM_k=(SU(2)_k×SU(2)_2)/SU(2)_{k+2}`
  (**Lashkevich, hep-th/9301093, eq.3**) — both verified to give the right minimal-model central charges.
- **The coincidence:** `M(4,5)` and `SM_1` are **literally the same coset** `(SU(2)_1×SU(2)_2)/SU(2)_3`, c=7/10.
- **Uniqueness:** a sweep finds `(m=4, k=1)` is the **only** (ordinary, super) pair sharing the same coset data —
  the mechanism is unique to the TCI. The uniqueness *fact* is Qiu 1986 (via Johnson–Clifford hep-th/0311129).
- **The mechanism as a proposition** ("the coincidence *is* the two cosets being equal at `SU(2)₃`") is, to chat1's
  search, **not stated** — so it stands as a modest original organizing observation (not a deep theorem).
- **Bonus:** `TCI = (E₇)₁⊕(E₇)₁/(E₇)₂` (c=7/10, verified) — **E₇ appears in the TCI itself as a coset algebra**,
  a different role from the excluded McKay/congruence `2O` (B210/B234); no contradiction, a paper nuance.

**Closes the H21 gate** on the PC19 paper's originality claim. Firewall: dimensionless CFT coset data.

## Anchors
B228 (the coincidence, now mechanism-referenced), B210/B234 (the McKay E₇ exclusion the E₇-coset nuance sits beside).
Refs: GKO 1986; Lashkevich hep-th/9301093; Qiu 1986 / Johnson–Clifford hep-th/0311129; the (E₇) coset hep-th/0301229.
