# W-F4: the non-orientable closing carries no matter in the module classes computed on the tick's own family, and the odd tick sees all of its double cover's matter (B1926's addendum recomputed and completed)

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note closes card W-F4
(`relays/cards/CHAT1_W-F4_the_non_orientable_closing.md`, d6b9023a1).

**How it was checked.** Computed once, on this seat's own code; expectations committed first. The two planted errors
reach N1 and N3 only, and both were caught. The referee of this note recomputed N3 and N4 independently at golden
n = 3, on its own code and two other primes; § 4 has the details.
- **The sealed run.** The script (sha256 `2edb676d…41c37d6`, pushed at 885b81fa2) was run once; its output was
  committed (97bb46000) before it was read. All six expectations were met as coded.
- **The method.** Exact ranks over two prime fields (10561849 and 10563433); the two give the same census. The helpers
  are W-C8 part 2a's, taken by text.
- **The levels.** Golden σ at n = 1, 3, 5, with double covers at levels 2, 6 and 10; bronze τ₃ at n = 1, with double
  cover at level 2. Characters take t-values among the 2e-th roots of unity.

## 1. The results

| line | result |
|---|---|
| N1 | **Transfer.** h^i(G_2n; π*χ) = h^i(G_n; χ) + h^i(G_n; χ ⊗ w) for i = 0, 1, 2, and the same for the interior classes n, on every character: 2, 16 and 242 golden, 18 bronze |
| N2 | **B1926's addendum, recomputed independently.** Every fibre-non-trivial χ with χ(μ_n) = −1 pulls back to a level-2n character trivial on μ_2n that carries a class with c(λ) ≠ 0: golden 0, 3 and 10, bronze 2. Every fibre-non-trivial χ with χ(μ_n) = +1 has h¹ = 0 |
| N3 | **The whole accounting.** The record's data at level 2n number golden 0, 15 and 120, bronze 8. The deck-invariant ones are exactly N2's pull-backs (0, 3, 10; 2). **The rest come in deck pairs** (0, 6, 55; 3), and each is seen at level n through the induced module Ind ψ, with h⁰, h¹, h² and n equal to ψ's on the double cover. This was checked on every fibre-non-trivial ψ that is not deck-invariant, at every t-value computed: 96, 2,420 and 36 characters ψ, which give 48, 1,210 and 18 modules up to isomorphism. The pairing is inferred from the count. Closure under the deck holds by hand, since the deck fixes ψ(μ_2n) and preserves c(λ) ≠ 0; the referee checked it at golden n = 3 |
| N4 | **The closed objects at odd levels** (the fibre's puncture filled, k = 1, or a cone point, k = 2 to 6): h¹(G_n,k; ℓ) is 1 for ℓ trivial and 0 for every other character. So the only non-split abelian doublets are α ⊗ U, U the unipotent extension by the tick's class |
| N5 | On those closed objects, **every character, every non-split abelian doublet and every induced module has untwisted gap h¹(V) − h¹(V*) = 0**. Its twisted gap equals h⁰(V) − h⁰(V* ⊗ w). Per k: golden 2, 16, 242 characters with as many doublets and 0, 48, 1,210 induced modules; bronze 18, 18 and 18. On the induced modules h¹(G_n,k; Ind ψ) = h¹(G_2n,k; ψ) |
| N6 | **Control, recomputing agy-exp's X-SM example independently.** On N₃ × S¹, (h⁰, h¹) is (0, 3) for V, (0, 2) for V* and (1, 4) for V* ⊗ ω, exactly as agy-exp found, in this seat's extension convention. V ⊗ ω gives (0, 2). So the instrument registers an untwisted gap where one exists |
| P1, P2 | The plants fired. With w left out, transfer fails (8 and 22 characters at golden n = 3 and 5). Ind built with τ^(n+1) fails the relations on every ψ tried (96 and 2,420) |

## 2. By hand, for every level

- **N1 and N3 are Shapiro's lemma.** For p odd, π_*1 = 1 ⊕ w and Ind is exact. The cusp of G_n is one Klein bottle,
  whose preimage is one torus (g_2n = τⁿ(g_n) g_n, asserted in the run, which gives μ_2n = μ_n² in G_n), so the
  interior classes correspond too. This covers the cohomology identities, not N3's counts. Those also need N2's second
  part (h¹ = 0 when χ(μ) = +1), whose proof by hand is card W-F6's.
- **N4.** On a closed fibre (λᵏ = 1, with p prime to k), every θ-cocycle has k·c(λ) = 0, so c(λ) = 0. For θ ≠ 1, the
  line H¹(F; θ) is detected by c(λ) = (1 − θ(b))c(a) + (θ(a) − 1)c(b) (B1506 T1), so H¹(F_k; θ) = 0. With H⁰(F_k; θ) = 0
  too, the Wang sequence gives H¹(G; ℓ) = 0 for every fibre-non-trivial ℓ. For fibre-trivial ℓ, H¹ is the
  ℓ(t)-eigenspace of the monodromy on H¹(F_k), plus the tick's class when ℓ = 1. In characteristic 0 the monodromy's
  eigenvalues are not roots of unity, so for every finite-order ℓ only the tick's class survives. Over F_p this holds
  for p outside a finite set at each level.
- **N5 follows.** α ⊗ U has the dual α⁻¹ ⊗ U. For α ≠ 1 both have h¹ = 0, by N4 and 0 → α → α ⊗ U → α → 0; for α = 1
  they coincide. The twisted-gap identity is twisted Poincaré duality with Euler characteristic 0, which holds on
  G_n,k over a field of characteristic prime to k. An induced module's h¹ is its double cover character's, which is 0
  by N4 at level 2n (N4's argument does not use the parity of the level).
- **The double cover's count (N6's identity).** On a closed non-orientable Q with double cover Q̃:
  - h¹(Q̃; π*V) − h¹(Q̃; π*V*) = [h¹(V) − h¹(V* ⊗ w)] + [h¹(V ⊗ w) − h¹(V*)], which twisted duality, applied twice,
    reduces to invariant terms.
  - So an untwisted gap on Q is a split between the two deck halves of a count that, on the orientable double cover,
    is the invariant-vector term only.
  - On the control: 3 − 2 on Q, against 5 − 6 = h⁰ difference −1 on Q̃.

## 3. What it means for the system

- **The puncture is strengthened again (line 4 of W-C8 part 4's page).**
  - On the tick's own family, the non-orientable closing is no rival: every closing computed carries no record matter
    and no untwisted gap in any module class computed.
  - That covers W-F3's orientable cone points and, here, the non-orientable closings, filled or coned.
  - The agy lane's relay of 2026-11-14 reads a non-orientable closing as a second road to chirality (its § 3). On this
    family, for closings that keep the fibre and for characters, abelian doublets and induced modules, that road is
    closed.
  - It stays open on objects outside the family, such as N₃ × S¹. There (§ 2) its chirality is a split between the
    deck halves, which the orientable double cover does not see.
- **Main's B1926 addendum.**
  - Recomputed independently: N2.
  - Completed: N3. The twisted characters are only the deck-invariant part of the double cover's record data; the
    larger part arrives at the odd tick as two-dimensional induced modules.
  - By Shapiro, the odd tick and its double cover carry the same classes, sorted differently: by characters at the
    even tick, by twisted characters and induced doublets at the odd tick.
  - So "the frame has no matter of its own at an odd tick" follows from Shapiro's lemma for every module (by hand,
    p odd; not independently checked). What stays a choice is P-846's condition, that counting respects covers.
- **A reading** (not a result): with the classes the same, the even-tick condition becomes a condition on labels. At an
  even tick all of the record's data are characters. At an odd tick most of them are not (55 of 65 deck-classes at
  golden n = 5). If what is observed is labelled by characters of the level, only the even tick shows the whole
  record.

## 4. Typed

| statement | how checked |
|---|---|
| N1, N3 on the levels named | computed once; expectations committed first; tested against planted errors (2, both caught) |
| N2, N4, N5 on the levels named | computed once; expectations committed first |
| N3 and N4 at golden n = 3 (N4 for k = 1 to 6, and for all 1,056 characters with t-values in the 264th roots of unity) | recomputed independently, by the referee, on its own code and two other primes |
| N1, and N3's identity h^i(G_n; Ind ψ) = h^i(G_2n; ψ) with n, for every level and module, p odd | not independently checked (by hand, Shapiro) |
| N4, N5 for every odd level, every k ≥ 1 and every finite-order character, in characteristic 0 (over F_p: p prime to k and to \|coker(A_n − I)\|, and no eigenvalue of A_n equal to ℓ(t)^±1) | not independently checked (by hand) |
| N2 (main's statement) | recomputed independently |
| N6 (agy-exp's numbers) | recomputed independently |
| the non-orientable closing is dead on the tick's family | computed once on the levels named, and by hand for every odd level (not independently checked), for characters, abelian doublets and induced modules; modules of other kinds and closings that change the fibre are not computed |
| a non-orientable closing's chirality is a split of the double cover's count | not independently checked (by hand); computed once on the control |
| the even-tick condition as a condition on labels | a reading |

## 5. Not computed

- Modules of dimension above two, other than induced ones, and irreducible two-dimensional modules not induced from
  the double cover.
- Closings that change the fibre.
- Golden levels above 5 (double covers above 10).

## 6. Files

`relays/chat1_2026-11-14_wf4/`: `wf4_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf4_checks_out.txt`,
`wf4_checks_err.txt` (empty).

This note was read by one session before it was pushed. Its corrections are applied but one: the record's lane names
and the closing count stay.

0 of 19.
