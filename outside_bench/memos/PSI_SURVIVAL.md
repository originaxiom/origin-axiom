# NOTHING ABELIAN SURVIVES BUT THE SM — the unique chain's torus is the SM torus EXACTLY; the family u(1) dies with gcd-1 charges (trivial remnant, continuous AND discrete), and the dark block exits the chain unprotected
## (outside bench, 2026-08-26; seventy-seventh memo; the memo 72 × memos 56–58 cross-link — what the unique chain does to the dark ledger)

### THE FACTS (`certificates/psi_survival.py`; asserts GREEN)
- **FACT 1 (torus equality, both directions).** The annihilator of the two
  vev directions in the Cartan has dim 4 (memo 72), the four SM generators
  (color pair, T3, Y) each annihilate both vevs, and they are linearly
  independent — so the surviving torus **IS** the SM torus, not merely
  contains it. **No extra u(1) of any kind survives the unique chain**: not
  u(1)_ψ, not u(1)_χ, not any gauged family direction. (Rank arithmetic:
  6 → 4 with both broken directions seen by the vevs.)
- **FACT 2 (how the family charge dies).** The ψ-charges of the vev pair
  are (1, −2) — both nonzero, so the family u(1) is broken twice over —
  and gcd(1, 2) = 1: **the unbroken remnant of u(1)_ψ is ℤ/1 = trivial**.
  Not even a discrete cyclic shadow survives from the continuous side.
  Cross-check from the lattice side (memo 72/76 machinery recomputed
  in-run): the ψ-parity PATTERN is absent from the surviving gradings —
  the two computations agree from opposite ends.
- **FACT 3 (the dark ledger after the chain).** Memo 58's anomaly-payment
  theorem (T_dark = −T₁₆) is conditional on a GAUGED family u(1). After
  the unique chain that u(1) is broken with trivial remnant (FACT 2), and
  memo 76 measured BRANCH N — no surviving ℤ/2 is odd on the whole
  15-plet, none is constant-odd on the ψ-10 dark class. **Kinematic
  conclusion: below the chain, nothing the root lattice or the surviving
  gauge group supplies protects the E6 dark candidates of this frame.**
  Their stability, if any, must come from Gates-2/3 territory (potential
  accidents, global symmetries) — or is absent. Above the breaking, the
  payment theorem stands unchanged as a consistency condition on the UV
  spectrum.

> **The dark arc (memos 56–58) and the chain arc (memos 70/72) now meet,
> and the meeting is a pincer: the object forces a dark block into the
> spectrum as the anomaly payment for the visible generation (conditional,
> memo 58), and the object's only SM-breaking chain then strips that block
> of every kinematic protection it had. If this frame is the right reading,
> dark-sector stability is not a symmetry fact — it is a dynamics fact or
> it is false. That is a falsifiable-shaped statement, reached entirely by
> exact computation, and it contradicts no observation: nothing observed
> says dark matter is protected by a gauged parity. Necessary conditions
> only; no potential, no vacuum, no values; Gate 5 untouched.**

### Certificates
`certificates/psi_survival.py`; output `outputs/psi_survival_out.txt`
(in-lane rerun byte-identical).
