# THE THREE-FAMILY YUKAWA IS INTER-FAMILY — inside E8 the coupling on the family triplet of 27's is exactly ε_family ⊗ the Jordan cubic, so same-family Yukawa couplings vanish identically in that channel
## (outside bench, 2026-08-26; fifty-third memo; the named three-family follow-up of G-3 and memo 52 executed; one machine-caught error filed below; POSSIBILITY-SPACE CELL — E8 is not object-paid)

### The question and its standing
Golden_gate G-3 proved the 27 enters E8 exactly three times, indexed by the
triplet of the fourth orthogonal A2: 248 = (8,1) + (1,78) + (3,27) + (3̄,27̄).
If those three copies are "the three families", what Yukawa does the ambient
algebra itself induce on them? **Fence up front:** E8 is possibility space,
not object-paid; this cell maps the space the family triplet lives in. The
object connection is that the internal factor comes out forced to be the
object's own unique coupling (memos 32/47/48).

### THE FACTS (`certificates/family_yukawa.py`, with the vendored generic
Chevalley builder `certificates/e7_ladder.py`; every number exact, every
property verified in-run, not cited)

- **FACT 1 (G-3 re-anchored).** All four orthogonal A2 slots rebuilt: each
  with 72-root e₆ complement and 162 crossing roots in 6 projection classes
  × 27. Family block = the 81 roots over the three triplet weights; 27
  distinct e₆-weights per family block.
- **FACT 2 (support).** The zero-sum triples inside the family block number
  exactly **270 = 45 internal weight-zero triples × 6 family assignments**,
  and **every one has three distinct family weights — a same-family
  zero-sum triple does not exist at all.** The selection rule is decided at
  the root-lattice level before any structure constant is consulted.
- **FACT 3 (the form).** κ(r) = tr(ad e_r ∘ ad e_{−r}) = −60 for all 81
  family roots — the Killing normalization computed by exact 248-dim
  ad-trace, no convention trusted. T(x,y,z) := K(x,[y,z]) built from κ and
  the Frenkel–Kac cocycle.
- **FACT 4 (invariance verified).** The derivation identity for T equals
  zero for **all 78 generators** — the 72 complement-e₆ root vectors and
  the 6 family-A2 root vectors — computed by sparse scattering over the
  1620-entry support.
- **FACT 5.** T is totally antisymmetric on all 270 × 6 ordered entries.
- **FACT 6 (exact factorization, gauge-corrected).** All values are ±κ, and
  with σ a per-root sign gauge solved constructively over GF(2) (270
  equations, 126 unknowns, rank 97, consistent) the identity
  T((μᵢ,a),(μⱼ,b),(μₖ,c)) = κ·sgn(ijk)·σᵢₐσⱼᵦσₖ꜀·S({a,b,c})
  holds on **all 1620 entries**, with S a symmetric ±1 function on the 45
  internal triples. In the σ-rescaled basis **T = ε_family ⊗ C_sym
  exactly**; C_sym is e₆-invariant (FACT 4), symmetric, nonzero, supported
  on the 45 — by the banked dimension-1 count (memo 48 rung 3) it **is the
  Jordan cubic up to scale**.
- **FACT 7 (the family factor is forced too).** dim Inv_{sl₃}(3⊗3⊗3) = 1
  computed in-run, and the survivor is totally antisymmetric: ε is the only
  thing the family index could carry.

> **THE RESULT: in the E8 channel the three-family Yukawa is
> ε_family ⊗ C_Jordan — its support always takes one leg from each family.
> Same-family (diagonal) Yukawa couplings are identically zero: not
> suppressed, absent, and absent already at the root-lattice level.**

### Error filed (machine-caught; preregistration did its job — lane error #4)
The first draft preregistered that the raw extraction
C'(a,b,c) = T((μ₁,a),(μ₂,b),(μ₃,c)) would be totally symmetric. The assert
failed. Root cause: the Chevalley root vector e_{(μᵢ,w_a)} differs from the
factorized basis fᵢ⊗v_a by a per-root sign c_{i,a}, so the raw C' carries
c₁ₐc₂ᵦc₃꜀ and need not be symmetric — the correct claim is the existence of
the sign gauge, which the corrected cell proves constructively (GF(2) solve
+ forward verification on every entry) rather than assuming. The refuted
raw-symmetry check is retained in the certificate as a report line.

### Reading (interpretive, labeled)
- If a three-family world takes its family index from the G-3 triplet, the
  cubic E8 channel gives purely off-diagonal Yukawa texture; diagonal
  masses would have to come from outside this channel (e.g. symmetry
  breaking that mixes the channel with others). The record asserts nothing
  about which — values and dynamics stay behind Gate 5.
- Sign of the combined exchange: ε_spin (memo 47, antisymmetric) ×
  ε_family (antisymmetric) × C (symmetric) is symmetric under simultaneous
  exchange of two full one-particle slots. Memo 47's antisymmetry was the
  single-family statement; with a family index the kinematic exchange sign
  flips. Statistics live at the field level, not here — flagged, not
  claimed.

### Fences
Possibility-space cell: nothing here says the object pays E8 (G-3's fence
stands). Killing invariance of K(x,[y,z]) is a theorem but is not leaned
on — invariance is verified generator by generator (FACT 4). The
identification of C_sym with the Jordan cubic cites the banked dim-1 count
(memo 48), which is in-lane and twice re-run. Kinematics only; Gate 5
untouched.

### Certificates
`certificates/family_yukawa.py` (+ vendored `certificates/e7_ladder.py`);
output `outputs/family_yukawa_out.txt` (vendored copy re-run in-lane,
byte-identical).

### One sentence for the ledger
The ambient algebra that holds three copies of the 27 wires them with the
only coupling it could — the family epsilon times the object's own Jordan
cubic — and that coupling never lets a family talk to itself: the diagonal
is empty by root arithmetic alone.
