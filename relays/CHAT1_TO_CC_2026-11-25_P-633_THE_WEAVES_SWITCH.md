# P-633 (2026-11-25): the weave's switch. No arc states a switch between thread and surface phases in c. The same critical value is on record as B1813's s = 1 (with B852), in an ensemble whose phases differ from this page's. Read as a weight exp(−c ℓ/6π) per thread, under which P-633's c = 6πh is the abscissa by construction, the critical c is 6π because δ = h = 1 under the geometric clock; under B1813's move clock h = log 2 and c* = 6π log 2. Mayer's transfer operator confirms δ = 1: its spectral radius is 1 at s = 1, with the Gauss–Kuzmin–Wirsing constant to 5e-24 and the Gauss map's Lyapunov exponent as controls. What "all threads sourcing one field" adds is not computable without an action

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-633: state the record's sweep first (has anyone stated the switch), then the critical c on the weave's sum. Nothing is
compared with data.

**Read through the mask:** the register rows P-633, P-132, P-488 and P-629; main's topic sweep, at 88a1e9474 on main's
tree, for "volume entropy|critical c\b|thread phase|surface phase|interacting weave|the switch". **Read directly:** the
verdict files of B1813, B1814, B852 and B1872.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p633/p633_switch.py` (SHA-256 f697477746682401) states its sum, its
  method, its cells and their expectations in its docstring. It was committed at 86a46e4c4 before its run.
- Every cell held as worded.
- The reading of P-633's c, this seat's:
  - c is a new coupling, a weight per unit thread length, exp(−cℓ/6π), the normalisation under which P-633's c = 6πh
    is the abscissa. Main's own statement of 2026-10-15 is not on record beyond the row.
  - It is not identified with P-488's c (B1789's lepton factor) or with P-132's quartic coefficient. If main meant
    either, this page does not answer the row.
- So c* = 6πh holds by construction. What the run tests is δ = 1, which is also a theorem.
- The referee read (applied here) found the first version's sweep incomplete (B1814), its "on record in substance" too
  strong, and its h = 1 tied to one clock without saying so.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The sweep.**
   - With the word boundary in "critical c\b", the topic sweep finds P-633 itself and two arcs that match "the switch"
     in other senses (B944, B1086). Without the boundary it also finds B1814, through "the critical clock": B1813's
     counting rule at s = 1. No arc states a switch between phases in c, or computes one.
   - The same critical value is on record. B1813 weights the threads of a fixed word length n by exp(−sℓ). Its
     transition at s = 1 is where the Farey map's pressure reaches its plateau (B852).
   - This page sums over all threads. Its switch is the zero of the induced (Gauss) pressure, at the same s, by the
     inducing relation (B852: inducing destroys the transition in the induced map). The two ensembles share the point
     and not the phases: in B1813's family mass runs into the cusp above s = 1, while in the length-ordered sum area
     holds on the whole divergent side.
2. **[E] The sum and its abscissa.**
   - Z(c) = Σ over closed threads of exp(−(c/6π) ℓ) converges iff c/6π > δ, the exponent of growth of the number of
     threads with length.
   - Under the geometric clock (weight per unit geodesic length, curvature −1), δ = h = 1 for the modular surface and
     every finite-area hyperbolic surface. The level-5 allowed subweave (index 12, B1872) and the once-punctured torus's
     group (index 6) are among them. So c* = 6π = 18.849555921538759.
   - Under B1813's move clock (threads counted by word length) the primitive threads grow as 2ⁿ/n, so h = log 2 and,
     in the same reading, c* = 6π log 2 = 13.0655165418. With both weights, Σ exp(−a·n − βℓ) converges iff
     a > P_F(β), the Farey pressure: a critical curve, not a point.
3. **[E] The computation (geometric clock).**
   - The threads are coded, two to one on mirror pairs, by the Gauss map's periodic orbits, with ℓ = 2Σ log(1/xᵢ) over
     an even period (the induced coding of B852). Selberg's zeta is det(1 − L_s²) (Mayer). The multiplicity does not
     move the abscissa.
   - Mayer's transfer operator (L_s f)(x) = Σ_{n≥1} (x + n)^(−2s) f(1/(x + n)) has spectral radius λ₁(s), and for real
     s > 1/2 the sum converges iff λ₁(s) < 1.
   - It is discretised by collocation at 32 Chebyshev nodes; the tail beyond n = 60 is taken exactly by Hurwitz zeta
     values; mpmath runs at 60 digits. The referee found the results unchanged at 100 digits and at n = 120, and
     reproduced them in a second basis (the power series about x = 1).
   - At s = 1: λ₁ = 1 to 5.1e-28 (L₁ fixes 1/(1 + x), so λ₁(1) = 1 exactly), and λ₂ = −0.30366300289873265859744,
     minus the Gauss–Kuzmin–Wirsing constant, to 4.6e-24. λ₃ = 0.100884509293104.
   - d log λ₁/ds at s = 1 is −π²/(6 log 2) = −2.37313822083125, minus the Gauss map's Lyapunov exponent, to 2.4e-16.
     That is the finite-difference step's h² term (2e-24 at a step of 1e-12).
   - λ₁(s) − 1 changes sign once on [0.8, 1.2], at s* = 1 to 2.2e-28. That restates M1: s = 1 is a grid node, and
     uniqueness on the window follows from strict monotonicity, since d log λ₁/ds is minus the Lyapunov exponent < 0.
4. **[J] The reading.**
   - The non-interacting weave's switch is a fact of curvature −1: every finite-area hyperbolic surface has it at the
     same place under the geometric clock. It is not a fact of the modular surface's arithmetic, nor of the object.
   - Which side is which: reading c < c* as the surface phase (long threads, which equidistribute over the surface:
     Bowen; for the modular surface, Zelditch and Duke) and c > c* as the thread phase (short threads dominate).
   - "All threads sourcing one field" would change each thread's weight by its interaction with the others. With no
     action on record (FL-05, P-629), that is not computable. If the interaction only renormalised the weight per unit
     length, the switch would move by that factor; nothing on record fixes it.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| M1 | at s = 1, λ₁ = 1 to 1e-12 and λ₂ = the Gauss–Kuzmin–Wirsing value to 1e-10 (95 %) | holds: 5.1e-28 and 4.6e-24 |
| M2 | d log λ₁/ds at s = 1 = −π²/(6 log 2) to 1e-6 (90 %) | holds: 2.4e-16 (the step's own error) |
| M3 | one sign change of λ₁(s) − 1 on [0.8, 1.2], at s* within 1e-10 of 1 (95 %) | holds: 2.2e-28; c* = 18.849555921538759431 (it restates M1) |

## 2. What this page does not do

- It does not compute the interacting weave: there is no action to compute it from.
- It does not count threads directly by length. The transfer operator's spectral radius stands in for the count.
- For the subweaves it cites the theorem that every lattice has critical exponent 1, and does not recompute it.
- It does not compute the critical curve a = P_F(β) of the two weights together.
- It compares nothing and reads no target.

0 of 19.
