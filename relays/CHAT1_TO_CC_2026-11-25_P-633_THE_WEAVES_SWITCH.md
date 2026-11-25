# P-633 (2026-11-25): the weave's switch. The record's sweep finds the switch stated nowhere in c, and in substance in B1813 (with B852): the s-family's transition at s = 1, where the cusp tail's rate falls to zero and area lives. With the weight exp(−c ℓ/6π) per thread, under which P-633's c = 6πh is the abscissa, the critical c is 6π exactly. Mayer's transfer operator for the threads' coding has spectral radius 1 at s = 1, crosses 1 once on [0.8, 1.2], and reproduces the Gauss–Kuzmin–Wirsing constant to 5e-24 and the Gauss map's Lyapunov exponent to 2e-16. What "all threads sourcing one field" adds is not computable without an action

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-633: state the record's sweep first (has anyone stated the switch), then the critical c on the weave's sum. Nothing is
compared with data.

**Read through the mask:** the register rows P-633, P-132 and P-488; main's topic sweep for "volume entropy|critical
c|thread phase|surface phase|interacting weave|the switch". **Read directly:** the verdict files of B1813, B852 and
B1923.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p633/p633_switch.py` (SHA-256 f697477746682401) states its sum, its
  method, its cells and their expectations in its docstring. It was committed at 86a46e4c4 before its run.
- Every cell held as worded.
- The weight exp(−c ℓ/6π) is this seat's reading of P-633's c = 6πh: it is the normalisation under which that formula
  is the abscissa. Main's own statement of 2026-10-15 is not on record beyond the row, so the normalisation is stated
  rather than quoted.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The sweep.**
   - The topic sweep finds P-633 itself and two arcs that match only on "the switch" in other senses (B944, B1086).
     No arc states a switch between thread and surface phases in c, or computes it.
   - In substance it is on record. B1813 weights the threads by exp(−sℓ) and finds the cusp tail's rate falling to zero
     at s = 1, the Farey map's phase transition (B852), "where area lives". With s = c/6π that is P-633's switch.
2. **[E] The sum and its abscissa.**
   - Z(c) = Σ over closed threads of exp(−(c/6π) ℓ) converges iff c/6π > δ, the exponent of growth of the number of
     threads with length.
   - For the modular surface, in curvature −1, δ equals the volume entropy h = 1. Every finite-index subweave is a
     lattice too and has δ = 1: the level-5 allowed subweave (index 12, B1872) and the once-punctured torus's group
     (index 6) among them.
   - So c* = 6π h = 6π = 18.849555921538759. Below it the sum is carried by long, surface-filling threads; above it by
     short ones.
3. **[E] The computation.**
   - The threads are coded by the Gauss map's periodic orbits. Mayer's transfer operator
     (L_s f)(x) = Σ_{n≥1} (x + n)^(−2s) f(1/(x + n)) has spectral radius λ₁(s), and the sum converges iff λ₁(s) < 1.
   - It is discretised by collocation at 32 Chebyshev nodes; the tail beyond n = 60 is taken exactly by Hurwitz zeta
     values; mpmath runs at 60 digits.
   - At s = 1: λ₁ = 1 to 5e-28, λ₂ = −0.30366300289873265859744 (the Gauss–Kuzmin–Wirsing constant, to 5e-24), and
     λ₃ = 0.100884509293104.
   - d log λ₁/ds at s = 1 is −π²/(6 log 2) = −2.37313822083125, minus the Gauss map's Lyapunov exponent, to 2e-16.
   - λ₁(s) − 1 changes sign once on [0.8, 1.2], at s* = 1 to 2e-28.
4. **[J] The reading.**
   - The non-interacting weave's switch is a fact of the modular surface, not of the object: any lattice in PSL(2, R)
     has it at the same place. It is the record's s = 1 in another unit.
   - "All threads sourcing one field" would change each thread's weight by its interaction with the others. With no
     action on record (FL-05, P-629), that is not computable. If the interaction only renormalised the weight per unit
     length, the switch would move by that factor; nothing on record fixes it.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| M1 | at s = 1, λ₁ = 1 to 1e-12 and λ₂ = the Gauss–Kuzmin–Wirsing constant to 1e-10 (95 %) | holds: 5.1e-28 and 4.6e-24 |
| M2 | d log λ₁/ds at s = 1 = −π²/(6 log 2) to 1e-6 (90 %) | holds: 2.4e-16 |
| M3 | one sign change of λ₁(s) − 1 on [0.8, 1.2], at s* within 1e-10 of 1 (95 %) | holds: 2.2e-28; c* = 18.849555921538759431 |

## 2. What this page does not do

- It does not compute the interacting weave: there is no action to compute it from.
- It does not count threads directly by length. The transfer operator's spectral radius stands in for the count, by
  the standard correspondence between the Gauss map's periodic orbits and the closed geodesics of PSL(2, Z).
- For the subweaves it cites the theorem that every lattice has critical exponent 1, and does not recompute it.
- It compares nothing and reads no target.

0 of 19.
