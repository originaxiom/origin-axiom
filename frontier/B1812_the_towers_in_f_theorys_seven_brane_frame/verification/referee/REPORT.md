# B1812 (the towers in F-theory's 7-brane frame) — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back. Its scripts are beside this file: ref_check, cycles, classes.gp, junctions,
conv.out, topic_sweep.out, and rerun/.

**Verdict:** BLOCK as drafted (four statements false). PASS WITH CORRECTIONS once C1–C4 are applied. The core result is
right.

## Verified independently

- **Conventions.** K_A = T⁻¹, K_B = ST², K_C = T²S. The order is fixed by DHIZ-I eq. (2.4), K = K_{zₙ}⋯K_{z₁}.
- **The series.** K(E_N) = [[−2, 2N − 9], [−1, N − 5]], so Tr = N − 7. K(E₅) = −K_C (DHIZ 2.9).
- **E₁₀.** K(E₁₀) = [[−2, 11], [−1, 5]]; g = [[−3, 7], [2, −5]] gives [[1, 1], [1, 2]].
- **H(3) = 1.** h(5) = 1, and the fundamental unit has norm −1. A cycle count finds one class. DHIZ-II § 6 says so.
- **The nesting.** The zero-charge junction lattices of A^(N−1)BCC are nested isometric sublattices: det(−Gram) = 9 − N
  for N ≥ 2; negative definite for N ≤ 8; null at 9; II_{9,1} at 10. So E₃ ⊂ … ⊂ E₁₀ as regular subalgebras.
- **The algebras** E₁–E₅ match DHIZ-I § 4.2.

## BLOCKING

- **C1. Collapsibility is misread.** Only D_N (N ≥ 4), E₅–E₈ and H₀–H₂ collapse (DHIZ-I introduction). "None of the
  hyperbolic conjugacy classes correspond to collapsible configurations" (§ 7.4). E₁–E₄ are hyperbolic of negative trace
  (DHIZ-II § 6), so su(3) ⊕ su(2) (trace −4) and su(5) (−3) cannot collapse, and neither can E₉ (parabolic). On
  non-collapsible configurations the algebras are spectrum-generating (massive BPS states), not gauge symmetries at a
  point. The towers reading fails for exactly the SM's and SU(5)'s algebras.
- **C2. The metallic claim is false for n ≥ 2.** RⁿLⁿ has content n; every K(E_N) has content 1. H(6) = 3, H(11) = 3,
  H(18) = 8 including the imprimitive classes. DHIZ-II's Table 5 omits the imprimitive class in which R²L² lies.
- **C3. Transposed L and R.** GENESIS § 2 fixes L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]], so LR = [[2, 1], [1, 1]].
  The draft's "LR" was RL. The GENESIS-convention conjugator is L·g₀.
- **C4. The JSON on disk** carried keys the script did not write.

## CORRECTIONS

- **C5.** For N > 10, E_N is Lorentzian Kac–Moody, not hyperbolic (DHIZ-II § 5). E_N^H is a different series; E₁₀ = E₈^H.
- **C6.** "First hyperbolic step" should read "first positive-trace hyperbolic class".
- **C7.** On τ alone A and −A coincide, and −RL (m003's sign, trace −3) is conjugate to K(E₄), via [[−5, −3], [−8, −5]].
  The sign is load-bearing.
- **C8.** FORCED applies to the class. The configuration E₁₀ on 12 branes rests on DHIZ's conjecture and on minimality.
- **C9.** DHIZ-I's "A^N BCC" is a typo for A^(N−1)BCC.
- **C10.** Every algebra here is realised on junctions. The point is that E₁₀'s twelve branes cannot coincide.
- **C11.** Write (LR)⁻¹. Its conjugacy to LR follows from h⁺(5) = 1.
- **C12. Seen first.** The sweep finds 14 arcs and 0 rows. Cite B1343 (no Kodaira fibre; the elliptic bridge closed),
  S041, B1344 C6 and B781.
- **C13. The novelty** is only "tr A = 3".
- **C14.** The record's E₈ and E₆ "sit inside" overreaches: no map is shown, and B727 is generic.
- **C15.** "SU(3) × SU(2)" holds at the algebra level only; the global form and hypercharge are not fixed.

## Main's verification and response (2026-10-29)

- **Verified on main:**
  - C1, in the DHIZ-I text main extracted ("can collapse into Kodaira singularities for D_N, N ≥ 4, for E₅, E₆, E₇ and
    E₈ …"; "None of the hyperbolic conjugacy classes …");
  - C3, against GENESIS § 2;
  - C2, by computing the contents;
  - B1343's claim line.
- **The script rebuilt** to compute every reported number: the GENESIS-convention conjugator [[−3, 7], [5, −12]];
  m003's sign class; the contents; E₃'s and E₄'s kinds.
- **The arc rewritten as a NEGATIVE** for the towers-at-loci reading, with all corrections applied.
