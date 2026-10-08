# B1607 — THE PRINCIPLE'S TICK AT THE COMMON POINT: the rule a → ab, b → a is L∘P — the swap, then a move — with the golden matrix LP, det −1, and σ² = LR; at the quaternion point it lifts into 2T and the moves' lifts exchange its class with its inverse's; on the three parities the moves are transpositions and the rule a 3-cycle, and the sense of a thread's parity 3-cycle is neither a thread invariant nor the mirror bit — so the two hands are complementary (the rule reverses the records' orientation and keeps the McKay orientation; every move does the opposite; the double tick keeps both) and neither is derived on the weave

**Verdict: PROVED** (every cell holds; one sub-claim of the control C1a — the letter — corrected post-seal). cc (main),
2026-10-08. Sealed `805e2d488` (PREREGISTRATION sha256 671d6328) before `principle_tick.py` ran; the run took six
seconds. No physical quantity. **0 of 19.**

**Credit.** The SM seat's W26 (each move a transposition of the parities, so the order-3 orientation flips at every
tick) stated the parity half of this before main computed it; its W28 (the common point as the qubit, the lifts as the
Clifford group) is the same quaternion point read from the other side. The record's early arcs B14, B16, B19, B466,
B469 and B1323 (the Fibonacci tick is LP) hold C1's substance; C1 re-verifies them as a control.

## 0. Seen first

As sealed: `VERDICT topic-sweep /Gieseking|a -> ab|a→ab|mirror rule|orientation.revers|non-orientable|3-cycle|parity 3|rotation sense|ω/ω²|omega.*omega|GM5c|the swap|double cover of m000|orientation double cover/: 76 of 1379 arcs on main match (NEGATIVE 5, OPEN 6, PROVED 65)`
— B14, B16/B19, B466, B469, B749, GENESIS §3 and GM5c (the golden matrix LP; the Fibonacci tick is LP, B1323; m000 is
the bundle of LP); the seat's W25–W29 read before the seal; main's B1601. The S₃ argument for C3 was derived in the
design and disclosed in the seal. **Literature:** only standard facts, read and not searched further — the Gieseking
manifold as the non-orientable once-punctured-torus bundle double-covered by the figure-eight complement (Gieseking
1912; Thurston's notes); GL(2, 𝔽₂) ≅ S₃ with its two 3-cycles conjugate by any transposition; the binary tetrahedral
group's two conjugacy classes of order-6 elements, exchanged by the binary octahedral group; the unique index-2
subgroup of SL(2, ℤ) (abelianisation ℤ/12); Skuratovskii's square-root identity as already cited at GM5c.

## 1. The computation (`principle_tick.py`, exact; `principle_tick.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C1a** (control) | σ's matrix [[1,1],[1,0]], det −1; σ = P∘R exactly; σ² = LR exactly as matrices and up to inner; the mirror rule is ι σ ι | 99% | **HOLDS except the letter:** σ = **L∘P** exactly (the swap, then L); P∘R is the *mirror* rule a → ba, b → a — the two have the same H₁ matrix LP and differ by ι. σ² = LR as matrices and up to the inner automorphism by b⁻¹a⁻¹ (conjugator `BA`); the mirror rule is ι σ ι. Post-seal: `post_seal_lp.py` (the only composition of two of L, R, P equal to σ is L∘P; the only one equal to the mirror rule is P∘R) |
| **C1b** (control) | σ's mapping torus non-orientable, isometric to m000, volume half of m004's; m000's orientable double cover is m004 | 90% | **HOLDS** — SnapPy's `b-+L`, `b--L`, `b-+R`, `b--R` are all m000 (H₁ = ℤ, volume 1.014941606 = half of m004's 2.029883213); m000's only double cover is orientable and isometric to m004. (`b-±LR`, the word LR with the reversal flag, is a different non-orientable manifold, volume 1.8319, H₁ = ℤ/2 ⊕ ℤ.) |
| **C2a** | the lifts of σ are ±(1 − i − j − k)/2, orders 6 and 3, in 2T; the mirror rule's lifts are their k-conjugates, in the same 2T-class | 85% | **HOLDS** — τ = (1 − i − j − k)/2 (order 6) and −τ (order 3), both in 2T, acting i → k, j → i, k → j; the mirror rule's lifts ±(1 + i + j − k)/2 = k τ k⁻¹ (i → −k, j → i, k → −j), the same 2T-class |
| **C2b** | the inverse rule's order-6 lift is in the other 2T-class of order-6 elements (two classes of four); the lifts of L and R, outside 2T, conjugate σ's lift into that class | 75% | **HOLDS** — 2T has 8 elements of order 6 in two classes of 4; σ's and the mirror rule's lifts are in one, σ⁻¹'s lift (1 + i + j + k)/2 (i → j → k) in the other; the lifts of L ((1 + i)/√2) and R ((1 − j)/√2), order 8, outside 2T, each carry σ's lift to the other class; P's lift (i + j)/√2 (order 4) is outside 2T, ι's lift k inside |
| **C3a** | L, R, P transpositions on the parities; σ, σ⁻¹ the two 3-cycles; σ² = LR with σ⁻¹'s; every odd-trace word to length 8 a 3-cycle of even length | 98% | **HOLDS** — L swaps (0,1),(1,1); R swaps (1,0),(1,1); P swaps (1,0),(0,1); σ is (1,0) → (1,1) → (0,1); σ² = LR the inverse; ι the identity; all 30 odd-trace words (up to rotation; 16 up to the swap — the seal's "16" was that count) are 3-cycles of even length |
| **C3b** | the sense is constant under even rotations and inverted under odd ones, all words | 90% | **HOLDS** on all 30 — **not a thread invariant** |
| **C3c** | the mirror keeps the sense, reversal inverts it, all words | 85% | **HOLDS** on all 30 — **not the mirror bit** |
| **C3d** | the 64 lifts of the three 2-torsion points give triangles of both orientations | 95% | **HOLDS** — orientations {−1, +1}: the oriented fibre orients no parity triangle |

## 2. What it says

**The rule contains the swap.** The principle's one tick is σ = L∘P: swap the records, then apply L. Its matrix is
GENESIS's golden LP (B1323), det −1 — one tick reverses the records' orientation; the double tick σ² = LR is the
genesis theorem's root, orientation-preserving; σ's mapping torus is the Gieseking manifold m000 and the root thread
m004 is its orientation double cover, the deck involution being σ itself (B466). So GM5c — is the swap a legal move —
is the question whether the principle's own tick is a move of the weave.

**Two ℤ/2's, and they are complementary.**
- (i) **The records' orientation** (det on H₁; on the weave's surface T against T̄, since W21's form is reversed by
  the swap, S85): reversed by the rule and by P; kept by every move L, R; kept by the double tick.
- (ii) **The McKay orientation** (the cyclic order of the three parities; ω against ω²; 27 against 27̄; at the
  quaternion point the 2T-class of the order-6 lift): kept by the rule (a 3-cycle, even); inverted by every single move
  L, R and by P (transpositions) and so by every odd rotation of a word; kept by the mirror; kept by the double tick
  σ² and by the index-2 subweave of even-length words.

So the rule carries (ii) and erases (i); the moves carry (i) and erase (ii); the double tick keeps both; the full
weave keeps neither — (ii) is not even a thread invariant, since rotating a word by an odd prefix is conjugation by a
transposition, and the oriented fibre does not orient the triangle of parities (C3d).

**GM5c with its branches computed.** If the rule is a move of the weave, P is in, the weave contains its own mirror
(it is mirror-closed either way, W26), and its three is achiral: T ↔ T̄, its object the non-orientable quotient (the
Gieseking at the root). The chiral three of W21/W22/B1606 lives on the double tick's weave ⟨L, R⟩ = SL(2, ℤ), whose
object is the orientation double cover — m004 over m000 at the root — and the hand of (i) is the choice of its sheet,
which the rule, being the deck involution, does not make. The fork stays open on GENESIS (v1.29 records both branches);
what it decides is now computed.

**Negatives, by name.** Main's contemplation candidate — "the sense of the root's 3-cycle relative to the oriented
fibre as the chirality bit" — is dead as a thread invariant (C3b, C3d); it survives only as a property of a marked
word, i.e. of the rule's own tick. The seat's W26 is verified on main by this route. The rule and its mirror are not
told apart at the common point (C2a: k-conjugate lifts; C3a: the same 3-cycle) — the mirror bit is not at the
quaternion point either; what the common point sees is σ against σ⁻¹, the direction of the tick.

**The grade.** Neither hand is derived on the weave; each is derived on a subweave the weave does not select — (i) on
the double tick's SL(2, ℤ), (ii) on its index-2 subgroup of even-length words. A selection, located. 0 of 19 stands.
What this makes computable next: the chiral three on the even subweave carries both hands at once — the index-2
subgroup of SL(2, ℤ) (the preimage of A₃, containing Γ(2)) is the group of M₁,₂'s double cover on which the McKay
orientation is a global choice; whether that cover's holomorphic triplet is still three, and whether the parity grading
of W22 becomes the ℤ/3 of (ii) there, is one computation (the B1608 design).

## 3. Disclosed

- The letter in C1a: the design wrote σ = P∘R; the computation says σ = L∘P and P∘R is the mirror rule (same matrix).
  Recorded as a failed sub-claim of a control; nothing downstream used the letter.
- The seal said "16 words"; the instrument enumerates 30 (up to rotation); 16 is the count up to the swap. Every
  statement holds on all 30.
- The S₃ argument behind C3b/C3c was derived in the design (disclosed in the seal); the computation is what the record
  carries. Not blind to the seat's W26.
- `post_seal_lp.py` is post-seal (pure word arithmetic, six lines of logic).

## 4. Files

`verification/principle_tick.py` (sealed), `principle_tick.json`, `principle_tick_run.txt`; `post_seal_lp.py` →
`post_seal_lp.json`; `adoption/amend.py` (GENESIS v1.29), `received/GENESIS_v1_28_main.md`. Test:
`tests/test_b1607_the_principles_tick_at_the_common_point.py`.
