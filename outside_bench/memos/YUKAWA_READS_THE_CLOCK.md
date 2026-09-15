# THE YUKAWA READS THE CLOCK — the unique coupling is supported on exactly the seven sl₂-allowed depth blocks of the meridian's grading, with odd total chain length at every vertex
## (outside bench, 2026-08-26; fifty-second memo; the depth filtration of memo 50 and the unique coupling of memo 48 shown compatible to the entry level; all preregistered facts GREEN on first run)

### The question
Memo 50 graded the carrier by the meridian's Jordan chains (lengths 3/2/1,
multiplicities 6/15/6, odd = matter). Memo 48 proved Y = ε⊗C is the unique
coupling. Does the coupling see the clock — and if so, with what selection
rule?

### THE FACTS (`certificates/yukawa_clock.py`, all exact; preregistered asserts, GREEN first run)

- **FACT A — invariance verified, not cited.** The meridian's log sits in a
  diagonal sl₂-triple (E, H, F) = (tautological triple ⊗ bridge triple);
  [E₂₇,F₂₇] = H_int verified, and Y's derivation identity under all three
  computed directly on its 540-entry sparse support: zero for E, F, H.
  (C itself rebuilt in-run as the unique e₆ invariant — 270 ordered triples,
  memo 48's nullspace.)
- **FACT B — chain-adapted bases, explicit and checked.** String bases
  constructed exactly: on the 27, 6 doublet chains (bottoms solved by exact
  6×6 elimination) + 15 singlets; on Ψ, 6 chains of length 3, 15 of length
  2, 6 of length 1 — every E-step verified to land on the recorded next
  vector, every top verified killed. (= memo 50's 6 J₃ ⊕ 15 J₂ ⊕ 6 J₁.)
- **FACT C — no leakage.** Over all weight-compatible string triples,
  every one of the 11 sl₂-forbidden depth blocks (s₁,s₂,s₃) is identically
  zero — computed exhaustively, entry by entry, not cited from Clebsch.
- **FACT D — no extra vanishing (expected branch landed).** Every one of
  the 7 allowed blocks is hit, with exact witnesses:
  | block (s₁,s₂,s₃) | nonzero entries | reading |
  |---|---|---|
  | (3,3,1) | 90 | deep matter ↔ deep matter via internal **singlet** |
  | (3,2,2) / (2,3,2) | 120 + 120 | deep matter ↔ unlocked via internal **doublet** |
  | (2,2,1) | 180 | unlocked ↔ unlocked via internal **singlet** |
  | (2,1,2) / (1,2,2) | 60 + 60 | frozen matter ↔ unlocked via internal **doublet** |
  | (1,1,1) | 30 | frozen matter ↔ frozen matter via internal **singlet** |
- **FACT E — the parity law.** Every nonzero block has s₁+s₂+s₃ **odd** —
  the depth-level refinement of memo 47's {2-odd: 30, 0-odd: 15} lock rule
  (odd chains = locked slots, memo 50, so odd total depth ⟺ an even number
  of unlocked legs at each vertex).

> **THE YUKAWA READS THE CLOCK: the coupling's support over the meridian's
> depth grading is exactly the representation-theoretic maximum — all seven
> allowed blocks, none of the eleven forbidden ones — and total chain
> length is conserved mod 2 at every vertex. Depth-3 matter couples to
> itself only through internal singlets and to the unlocked sector only
> through internal doublets; the six frozen matter lines (length 1) are not
> decoupled — they talk through singlets to each other and through doublets
> to the unlocked sector.**

### Why this is a result and not a tautology
Invariance forces the forbidden blocks to vanish (and the certificate
proves that vanishing directly rather than citing it). It does **not** force
the allowed blocks to be nonzero: each allowed block's coefficient lives in
a multiplicity space that the object's specific C could have annihilated. A
zero allowed block would have been a stronger-than-symmetry selection rule;
the preregistered two-outcome cell landed on "representation-theoretic
maximum" — the coupling is exactly as connected as the symmetry permits.

### What this feeds
- Memos 49–52 now form a closed quartet: the meridian's two clocks (49),
  the clock-parity lock (50), the longitude as the lock's home (51), and
  the coupling's depth selection rule (52).
- The (3,3,1) block — deep matter self-coupling through internal singlets —
  is the natural seed for the three-family question (named follow-up): the
  family triplet should be probed against this block first.
- For the freedom ledger: "which depth blocks couple" is object-paid
  structure (computed, forced to the rep-theoretic maximum); the numerical
  values inside each block remain behind Gate 5.

### Fences
The identification chains = strings uses ρ_Ψ(a) = exp(E_diag), exact here.
Zariski/interpretation steps play no role — every claim in this cell is a
finite exact computation. The physical glosses ("talk", "frozen", "deep")
are labeled readings of the exact block table. Kinematics only; values
untouched; Gate 5 untouched.

### Certificates
`certificates/yukawa_clock.py`; output `outputs/yukawa_clock_out.txt`
(vendored copy re-run in-lane, byte-identical).

### One sentence for the ledger
The unique coupling wires the carrier's depth layers together in exactly the
pattern the symmetry allows and no other — deep matter to deep matter
through singlets, matter to the unlocked sector through doublets, odd total
depth at every vertex — so the clock that times the slots also routes their
interactions.
