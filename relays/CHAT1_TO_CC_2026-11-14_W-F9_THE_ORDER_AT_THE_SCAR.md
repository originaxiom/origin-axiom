# W-F9: the order at the scar is irreducible. It is the degree in which the frame reads matter (interior H¹ rather than interior H² of the same module); duality exchanges the two and negates the index, and every symmetry of the manifold, the mirror included, preserves it

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free), by hand with a computed check.
This note closes card W-F9 (`relays/cards/CHAT1_W-F9_the_order_at_the_scar.md`, 7ac9ce67f).

**How it was checked.** Argued by hand; not independently checked. Computed once, on this seat's own code, with
expectations committed first and tested against planted errors (1, caught).
- **The sealed run.** The script (sha256 `cdedb389…56cca7ac`, pushed at 7ac9ce67f) was run once; its output was
  committed (a6f28290e) before it was read. Both expectations were met.
- **The method.** Exact ranks over one prime field (12000421). The helpers are W-C8 part 2a's, taken by text.

## 1. The results

On the record's modules V(ℓ, α) = [[α, cβ], [0, β]], with β = α/ℓ and c(λ) = 1 (B1438):

| level | modules | (h⁰, h¹, n) of V* = that of V(ℓ, ℓα⁻¹) | I = +1 / I = −1 | I odd under α ↦ ℓα⁻¹ | wrong partner V(ℓ, α⁻¹) |
|---|---|---|---|---|---|
| golden 4 | 12 | all | 4 / 4 | yes | fails on 8 |
| golden 6 | 210 | all | 36 / 36 | yes | fails on 108 |
| golden 8 | 1,892 | all | 244 / 244 | yes | fails on 696 |
| bronze 2 | 56 | all | 8 / 8 | yes | fails on 24 |

The I = ±1 counts reproduce part 2a's sealed run (golden) and part 5 (bronze). O1 compares the invariants
(h⁰, h¹, n), not isomorphism classes. The oddness of I and the balance of the census follow from O1's n-column, so they
are not separate evidence; O2's own content is the four counts. The wrong partner could be tested on 8, 198, 1,848
and 48 modules, and failed on 8, 108, 696 and 24.

**A second computation.** The referee of this note recomputed § 1 independently, on its own code, at all four levels
(golden 4 in two prime fields):
- it found an explicit intertwiner V* → V(ℓ, ℓα⁻¹) on all 2,170 modules, and none for the wrong partner;
- it computed n²(V) directly, as the kernel of H²(G; V) → H²(P; V) through an explicit chain map, without duality.
  n²(V) equals n(V*) on all 2,170;
- at golden 4, I = +1 on α = ℓ⁻¹, −1 on α = ℓ², and 0 on the fixed points α² = ℓ;
- the mirror (a ↦ ab, b ↦ a, t ↦ t) preserves n¹, n² and I on all 12 modules of golden level 4.

## 2. By hand

1. **Duality is an involution on the record's modules.** V has sub α and quotient β. So V* has sub β⁻¹ = ℓα⁻¹ and
   quotient α⁻¹, with extension class in H¹(G; ℓ), the same ℓ. At an orientable level that line is 1-dimensional and
   the class is non-zero (it is −c; rescaling one basis vector restores c(λ) = 1). Hence V* ≅ V(ℓ, ℓα⁻¹): α ↦ ℓα⁻¹ at fixed ℓ, with fixed points α² = ℓ.
2. **The index of one module is a difference of degrees.**
   - n(W) = rank(H¹_c(W) → H¹(W)), the interior classes.
   - Poincaré–Lefschetz duality on the orientable cusped manifold pairs H¹_c(V*) with H²(V), and H¹(V*) with H²_c(V).
     The map that forgets support in degree 1 for V* is dual to the one in degree 2 for V.
   - So n(V*) = n²(V) := rank(H²_c(V) → H²(V)), and **I(V) = n¹(V) − n²(V)**.
   - At the non-orientable levels the same holds with V* ⊗ w in place of V* (twisted duality, W-C8 part 2a).
3. **Every symmetry preserves the index.**
   - n is defined from G, the peripheral subgroup P and V alone. So any automorphism of G that sends P to a conjugate
     of P has n(φ*V) = n(V), and I(φ*V) = I(V).
   - This covers every homeomorphism of the manifold, orientation-reversing ones included, since n uses no
     orientation. Every orientable level here is amphicheiral: the tick has determinant −1 and commutes with its
     powers, so it induces an orientation-reversing self-homeomorphism, the mirror.
   - So no symmetry of the manifold carries a module to its dual when I ≠ 0. **The mirror does not exchange the
     order.**

## 3. What it means for the system (W-C8 part 4's page, § 2)

- **The order is irreducible.**
  - The frame reads matter as interior classes in degree 1, through line 6's slope (from u_χ ∈ H¹) and line 7's n.
  - The opposite reading, interior classes in degree 2, is the same frame transported by duality. It gives the
    opposite order: the census of § 1 with every sign reversed.
  - **The transport, line by line (by hand):**
    - Lines 1 to 5, 8 and 9 are statements about the group, the face, the act and the selections. They never mention
      the read-out's degree, so they hold unchanged.
    - Line 6's slope s(χ) = u_χ(μ) is a degree-1 class of a character. Both frames use it as data, so it is the same
      object in both.
    - Line 7 transports with I ↦ −I. B1438's firing law n¹(V(ℓ, α)) = [s(α) = s(ℓ)] becomes
      n²(V(ℓ, α)) = n¹(V(ℓ, ℓα⁻¹)) = [s(ℓα⁻¹) = s(ℓ)].
    - Twisted duality at the non-orientable levels transports the same way, with V* ⊗ w.
  - No symmetry of the construction picks between them: automorphisms preserve I, duality negates it. And no clause
    invariant under duality can pick.
  - The order is equivalent to the frame's choice of degree. Since every line of the page transports under duality
    (above), the degree-2 frame is a counterexample to any derivation of the order from the page, and the order is
    irreducible.
- **For the page:** the free datum "the order at the scar, V against V*" moves from "open" to "irreducible:
  equivalent to the read-out's degree (interior H¹ rather than interior H²); exchanged by duality, preserved by every
  symmetry, the mirror included".
  - This agrees with the SM seat's reading (the one free bit) and with SM-C8 (the relation carries the order and does
    not choose it). It sharpens both, by naming what the bit is.
  - It separates the order from the hand: the mirror preserves the index, so at orientable levels the order is not the
    hand.
  - At odd ticks, SM-C10 reads the bit the boundary controls as the order combined with the tick parity. Here that is
    V* ⊗ w in place of V*.

## 4. Typed

| statement | how checked |
|---|---|
| § 1's table | computed once; expectations committed first; tested against planted errors (1, caught); the I counts reproduced (part 2a, part 5); recomputed independently by the referee (four levels) |
| V* ≅ V(ℓ, ℓα⁻¹) for every record module at orientable levels | not independently checked (by hand); its invariants computed once on the levels named; the isomorphism recomputed independently by the referee (explicit intertwiners, 2,170 modules) |
| I(V) = n¹(V) − n²(V) | by hand (Poincaré–Lefschetz duality); recomputed independently by the referee, n² computed directly without duality on 2,170 modules |
| every automorphism keeping the cusp preserves I | not independently checked (by hand) |
| the order is equivalent to the read-out's degree (I(V) = n¹(V) − n²(V)) | not independently checked (by hand) |
| the order is irreducible: every line of the page transports under duality | not independently checked (by hand; the transport written out in § 3) |

## 5. Files

`relays/chat1_2026-11-14_wf9/`: `wf9_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf9_checks_out.txt`,
`wf9_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied. The line-by-line transport in
§ 3 was written after the read, at its request (the read found irreducibility asserted, not argued).

0 of 19.
