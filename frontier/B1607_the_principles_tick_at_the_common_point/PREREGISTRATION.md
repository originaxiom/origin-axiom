# B1607 — PREREGISTRATION: THE PRINCIPLE'S TICK AT THE COMMON POINT — the rule a → ab, b → a as one automorphism of the records: its lift at the quaternion point, its action on the three parities, and what each of the two hands (the records' orientation; the parities' cyclic order) does under the rule, under the moves, and under the double tick

cc (main), 2026-10-08, after S86. A weave arc: exact computations (sympy; SnapPy for one identification) on the
principle's own rule σ: a → ab, b → a, at the point every move fixes. **Sealed before `principle_tick.py` runs.** No
physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /Gieseking|a -> ab|a→ab|mirror rule|orientation.revers|non-orientable|3-cycle|parity 3|rotation sense|ω/ω²|omega.*omega|GM5c|the swap|double cover of m000|orientation double cover/: 76 of 1379 arcs on main match (NEGATIVE 5, OPEN 6, PROVED 65)`
— **the record already holds C1's substance, and C1 is sealed as a control, not a claim:** B14 (±LP are the only square
roots of LR in GL(2,ℤ)), B16/B19 (P is the unique primitive-pair exchange involution, forced by (LX)² = LR), B466 (the
whole σ-story is the Gieseking deck action), B469 (every metallic bundle double-covers a non-orientable one), B749 (the
det −1 sibling is the Gieseking), GENESIS §3 (m000 is the bundle of LP) and GM5c (if the swap is legal the golden matrix
LP = [[1,1],[1,0]] is generated; on the words route the swap is native). The rule's matrix is that golden matrix.
**The seat's W25–W29** (read before this seal, rows at S87): W25 (the weave's forced bundles are self-conjugate; the
weave's S₄ exchanges ω and ω²); W26 (the mirror of every thread is a thread, S φ⁻¹ S⁻¹ = reverse(φ) with L ↔ R; each
move is a transposition of the parities mod 2, so F-MC's order-3 orientation flips at every tick, 98 odd-trace words to
length 10); W28 (the common point as the qubit: Q₈ the Pauli group, the parities the three axes, the lifts of L, R, P,
−I as the Clifford group 2O). **Main's own B1601** (the linear parts at the common point are the cube's rotations on the
three lines; odd-trace words have even length). **Derived before the seal, in the design (disclosed):** a 3-cycle of S₃
is inverted by conjugation with any transposition, and L, R, P are transpositions on the parities, so the sense of a
thread's parity 3-cycle should flip under rotation of the word by an odd prefix; the two 3-cycles of GL(2,𝔽₂) are
symmetric matrices and mat(mirror w) = mat(w)ᵀ, so the mirror should keep the sense while reversal (conjugation by P)
inverts it; the mirror rule a → ba, b → a is ι σ ι with ι: a → a⁻¹, b → b⁻¹, and ι lifts to k ∈ Q₈, so the mirror
rule's lift should be 2T-conjugate to the rule's. These are the predictions below; they are informed, and the arc is
sealed so that the computation, not the argument, is what the record carries.

## Disclosed

Not blind: the seat's W26 states the flipping and main's design derives it. C1 reproduces facts already banked. The
SnapPy bundle names for σ's mapping torus are a convention (`b-+…`/`b--…`); C1b is settled by isometry to m000 and by
the double cover, not by the name. C2's "class" is 2T-conjugacy computed by brute force over 2T (24 elements); the
order-6 lift is the one with real part +½ (the other, −½, has order 3). C3's words are the 16 unsigned odd-trace
primitive words to length 8 of B1601, up to rotation; "sense" is which of the two 3-cycles on the parities (p₁, p₂,
p₃) = ((1,0), (0,1), (1,1)) the word's matrix induces mod 2.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **C1a** (control) | σ's matrix is [[1,1],[1,0]], det −1; σ = P∘R exactly as automorphisms; σ² = LR exactly as matrices and up to an inner automorphism as automorphisms; the mirror rule is ι σ ι | 99% |
| **C1b** (control) | σ's mapping torus is non-orientable and isometric to m000 (the Gieseking manifold), with volume half of m004's; m000's orientable double cover is m004 | 90% |
| **C2a** | the lifts of σ to the quaternion point (τ i τ⁻¹ = k, τ j τ⁻¹ = i) are exactly ±(1 − i − j − k)/2, orders 6 and 3, both in 2T; the mirror rule's lifts are the k-conjugates of these, in the same 2T-class | 85% |
| **C2b** | the inverse rule's order-6 lift lies in the other 2T-class of order-6 elements (there are two, of size 4), and the lifts of L and R, which lie outside 2T, conjugate the rule's lift into that other class | 75% |
| **C3a** | on the three parities L, R and P act by transpositions, σ and σ⁻¹ by the two 3-cycles, σ² = LR by σ⁻¹'s; every odd-trace word to length 8 acts by a 3-cycle and has even length | 98% |
| **C3b** | the sense is constant under even rotations and inverted under every odd rotation, for all 16 words — the sense is a property of the marked word, not of the thread | 90% |
| **C3c** | the mirror keeps the sense and reversal inverts it, for all 16 words — the sense is not the mirror bit | 85% |
| **C3d** | lifting the three 2-torsion points to the plane in the 64 ways gives triangles of both orientations: the oriented fibre orients no parity triangle | 95% |

**The reading, written before the run (the cells can only lower it).** Two ℤ/2's are in play and they are not the
same: (i) the records' orientation (det), which the swap P and the rule σ reverse and every move L, R keeps — on the
weave's surface this is T against T̄ (W21, verified at S85: the form is reversed by the swap); (ii) the parities'
cyclic order (ω against ω², 27 against 27̄, the McKay orientation), which each move L, R inverts, P inverts, and σ
keeps. The double tick σ² = LR keeps both. So: the principle's own tick carries the McKay orientation and reverses the
records'; the weave's moves carry the records' orientation and erase the McKay one; the double tick's even subweave
(the index-2 subgroup of SL(2,ℤ), even-length words) keeps both. Consequences to write if the cells hold: (1) GM5c as
a fork with computed branches — if the rule is a move of the weave, the weave contains the mirror (σ = P∘R) and its
three is achiral (T ↔ T̄), its object the non-orientable quotient (the Gieseking at the root); the chiral three of
W21/W22/B1606 lives on the double tick's weave ⟨L, R⟩, whose object is the orientation double cover (m004 over m000),
and the hand of (i) is the choice of its sheet, which the rule — the deck involution (B466) — does not make. (2) The
McKay orientation (ii) is invariant under the rule's own iteration and under the even subweave, and is not a thread
invariant and not the mirror bit (the seat's W26 on main's code; main's contemplation candidate "the sense of the
root's 3-cycle" dead as a thread invariant). (3) Neither hand is derived on the weave; each is derived on a subweave
the weave does not select — a selection, located. 0 of 19 stands.

## Instruments

`verification/principle_tick.py`; hashes in `ARTIFACT_HASHES.txt`.
