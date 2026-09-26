# B1380 — THE PUNCTURE IS THE WORD'S: the chain's puncture (P019's A5b, B749's fork F6, one of B1003's two FRAGILE axioms) is implied by the carrier axiom as P019 itself states it — no closed surface has a free fundamental group, and of the four surfaces whose fundamental group is F₂ only the once-punctured torus realizes the golden substitution — so F6's sibling does not drop the puncture, it abelianizes the carrier's group, replacing the word by its letter counts (the Fibonacci word's n+1 factors of each length fall to 2 images); orientation is untouched and is now the one independent fragile axiom on the words route, while the matrix route still pays the puncture

**Date:** 2026-09-26 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's directive — *"we have weak spots on
our chain, genesis and m004"* — after B1379 found that the external web seat's genesis work leaves both fragile forks where
B1003 put them · **Status:** PROVED (the carrier theorem; every computation below, own code) · RE-PRICED (the puncture: from an
independent axiom to a consequence of A5) · orientation UNCHANGED · **Fence:** mathematics about declared axioms; nothing here
reaches physics · **Price: unchanged, 0 of 19** · **Numbering:** B1380.

## 0. Seen from above

B1003 priced the chain's entrance at "five cheap axioms, TWO load-bearing ones: orientation and the puncture", each with a
named sibling — the Gieseking manifold for orientation (F5), the closed torus bundle of the same matrix, Sol, for the puncture
(F6). B1379 checked whether the owner's uploaded genesis architecture removes either and found it does not. This arc goes back to
the record's own statement of the axioms. P019 writes the carrier axiom as **A5: "The description is realized as an action on a
carrier: the rank-2 free group F₂ with σ's abelianization acting as a mapping class — i.e. the once-punctured torus"**, and then
adds the puncture separately, **A5b: "here at the origin it is an insertion, and this chain says so."** The question is whether
A5b is independent of A5. It is not.

## 1. Computed

`verification/puncture.py` (S1–S7; record `verification/puncture_run.txt`; about a second).

| | item | result |
|---|---|---|
| S1 | σ: a ↦ ab, b ↦ a on F₂ = F(a, b) | an automorphism (inverse a ↦ b, b ↦ b⁻¹a, checked both ways); abelianization [[1,1],[1,0]] (det −1); σ² = (a ↦ aba, b ↦ ab), abelianization [[2,1],[1,1]], m004's monodromy |
| S2 | the peripheral word [a, b] | **σ([a,b]) is conjugate to [a,b]⁻¹; σ²([a,b]) to [a,b]** — the fiber-level form of the orientation fork. Instrument control: 300 seeded products of elementary Nielsen moves (154 of det +1, 146 of det −1) all send [a,b] to a conjugate of [a,b]^det (Nielsen's commutator theorem) |
| S3 | closed surfaces | none has π₁ ≅ F₂: orientable genus g gives trivial, ℤ² (abelian) or H₁ of rank 2g ≥ 4; non-orientable N_k gives H₁ = ℤ^(k−1) ⊕ ℤ/2 (Smith form, k ≤ 6), and free groups have torsion-free H₁ |
| S4 | the surfaces with π₁ ≅ F₂ | χ = −1 with boundary: exactly **S(1,1)** (once-punctured torus), **S(0,3)** (thrice-punctured sphere), **N(1,2)** (twice-punctured projective plane), **N(2,1)** (once-punctured Klein bottle); peripheral classes in H₁ = ℤ²: (0,0); (1,0), (0,1), (−1,−1); (0,1), (−2,−1); (−2,−2) |
| S5 | which of the four realize σ | det(Mʲ ∓ I) ≠ 0 for j ≤ 48 (M = σ's abelianization; true for all j, as φ is not a root of unity): **σ and σ² are not realizable on S(0,3), N(1,2), N(2,1)** (a nonzero peripheral class would make some Mʲ fix it up to sign); realizable on S(1,1) only. Controls: the same test does NOT fire on the swaps that are realized on S(0,3) and N(2,1) |
| S6 | the word against its letter counts | the Fibonacci word (σ's fixed point) has **n + 1 factors of length n, and exactly 2 letter-count images, for every n ≤ 60**; the 8 190 positive words of length ≤ 12 are distinct in F₂ and fall to 90 points of ℤ² (ab and ba coincide); the frequency of a is 0.618034 = 1/φ |
| S7 | SnapPy | b++LR = m004 (σ² on the once-punctured torus); **b-+L = m000, the Gieseking manifold** (σ itself; non-orientable; its orientation cover is m004; volumes 1.0149416064 and 2.0298832128); **m004(0,1)**: flat tetrahedra (Sol), H₁ = ℤ, volume 0; (0,1) is the only filling with b₁ = 1 among small slopes (the fiber's boundary, B749 F6) |

## 2. The carrier theorem

**Theorem.** Let S be a surface with π₁(S) ≅ F₂ on which the golden substitution σ (or σ²) is induced by a homeomorphism, up
to the choice of identification and inner automorphisms. Then S is the once-punctured torus.

*Proof.* (i) S is not closed (S3): the closed surface groups are trivial, ℤ², of first Betti number at least 4, or have
2-torsion in H₁; F₂ is none of these. (ii) So π₁(S) is free of rank 1 − χ(S), χ(S) = −1, and S is one of the four surfaces of
S4. (iii) A homeomorphism h permutes the n punctures, so h^(n!) fixes each, and its action on H₁(S) = ℤ² sends every peripheral
class to plus or minus itself. That action is GL(2, ℤ)-conjugate to M = σ's abelianization (inner automorphisms act trivially on
H₁), and no power of M has an eigenvalue ±1 (its eigenvalues are φ and −1/φ). So every peripheral class must vanish in H₁. On
S(0,3), N(1,2) and N(2,1) some peripheral class does not (S4/S5). (iv) On S(1,1) the peripheral class is the commutator; σ
sends it to a conjugate of its inverse and σ² to a conjugate of itself (S2), so both preserve the peripheral structure, and by the
Dehn–Nielsen–Baer theorem for the once-punctured torus (Nielsen) both are induced by homeomorphisms — σ reversing orientation,
σ² preserving it. ∎

**Corollary (A5 ⟹ A5b).** A5 as P019 states it — the description realized as a mapping class of a carrier whose fundamental group
is the rank-2 free group — already forces the puncture: there is no closed carrier with that group, and among the ones with a
puncture only the once-punctured torus carries σ. The fiber's orientability comes free as well (the two non-orientable
F₂-surfaces are excluded by (iii)). P019's parenthetical "the carrier is chosen as the minimal geometric object whose fundamental
group is free of rank 2" does not by itself select a surface — all four have χ = −1 — but σ does.

## 3. What F6 varies, re-read

F6's sibling is the closed torus bundle of the same matrix (m004(0,1), Sol). Its fiber is the torus, π₁ = ℤ² — **not F₂ with a
point removed, but F₂ abelianized.** Dropping the puncture while keeping A5's group is impossible (§2 (i)); F6 therefore varies
A5 itself, replacing the substitution on words by the substitution on letter counts. S6 says what that costs. Morse–Hedlund's
minimum, the content of C1 — n + 1 factors of each length — collapses to 2 images of each length; distinct descriptions that the
word itself contains (ab and ba both occur) are identified; what survives is the frequency, the slope 1/φ: **the hearing,
ℚ(√5).** That is exactly B749's own computed verdict on F6 — *"closure strips exactly the being half ... while hearing is
monodromy-borne and survives whole"* — now with its reason. B749's F8 found that the word's non-geometric carriers see only the
hearing; F6's sibling is the geometric carrier of the word's letter counts, and it too sees only the hearing. **Being (ℚ(√−3))
needs both: geometry (F8) and the word's order (F₂, this arc).**

Why F₂ and not a quotient of it: F₂ is the group of the description with nothing imposed — the group completion of the free
monoid of words, into which the positive words inject (S6). Any smaller group identifies descriptions the word distinguishes;
the abelianization identifies all descriptions with equal letter counts. The chain's own invariant-selection rule (B1379 §2.6,
"no unforced collapse": a selector natural under the data's automorphisms cannot collapse a free orbit) forbids that. A reader
who lets the carrier realize only σ's abelianization is not dropping the puncture; they are replacing the description by its
counts, which C3 (being is inexhaustible description) does not allow.

## 4. The price, restated

| route | independent choices before the object | fragile |
|---|---|---|
| **words** (THE CHAIN, C1–C5; P019) | C3 (the one metaphysical commitment), C4 = A5 (the geometric carrier; priced GEOMETRY-NECESSARY by F8, and now carrying the puncture), C5 = A6 (orientation) | **one: orientation** (sibling the Gieseking manifold, m000) |
| **matrix** (docs/UNIQUENESS_THEOREM.md, A1–A6) | the ℤ² substrate (A1) is exactly the abelianized description; its A5 computes torsion on "the mapping torus M_B of B acting on the 2-torus" — the closed bundle — and cannot see the puncture (B1379 S6: equal H₁), so the puncture must be declared | two: orientation and the puncture |

F6's computation is unchanged and remains a true statement about the abelianized carrier; what changes is its reading. The two
routes to the object now differ in price, and the words route is the cheaper: one fragile axiom against two.

## 5. Orientation — not touched, and why

σ and σ² are both realized on the once-punctured torus (S2, §2 (iv)); their mapping tori are the Gieseking manifold and m004
(S7). The carrier theorem cannot choose between them, and nothing in C1–C4 does: the Fibonacci word is fixed by σ and σ² alike.
Orientation remains C5 — "choosing the child of the parent" (B1003) — and is now the chain's one independent fragile axiom on
the words route. Its price is unchanged: the discarded sibling is m004's own orientation quotient, with every face of the object
present.

## 6. For main (relayed, not applied)

The paper's §axioms and chain table price the entrance at two fragile axioms, orientation and the puncture. On the words route —
the route the chain table follows — the puncture is implied by the carrier axiom (this arc's theorem, a one-paragraph proof from
the classification of surfaces, Nielsen's commutator theorem and H₁); the fragile price is one axiom, orientation. On the
uniqueness theorem's route it stays two. Suggested: keep both statements, each with its route.

## 7. Caveats

The Dehn–Nielsen–Baer realization on the once-punctured torus is cited (classical), its necessary condition computed (S2); the
four-surface list is the classification of compact surfaces at χ = −1, enumerated; the eigenvalue check is computed to j ≤ 48 and
holds for every j because φ is not a root of unity. The preference for F₂ over its quotients is argued from the chain's own
"no unforced collapse" (B1379) and from C3; a reader who rejects both is rejecting A5 as P019 wrote it, not A5b. Nothing here
touches C3, C4's geometry price (F8) or orientation. P019 is hash-pinned by B749 and is not edited; the re-pricing lives in
docs/THEOREM_LEDGER.md (C4, C5), dated notes on B1003 and B1379, docs/LAW_MAP.md and docs/COSMOLOGY_LEDGER.md.

## Verification

`verification/puncture.py`. Lock: `tests/test_b1380_the_puncture_is_the_words.py` (the automorphisms and the peripheral dichotomy
with the Nielsen control; the closed surfaces; the four surfaces and realizability with controls; the word against its counts;
SnapPy's three siblings).

**Sources.** philosophy/P019_the_genesis_axiom_chain.md (A5, A5b, A6); B749 (forks F5, F6, F8); B1003 (the prices); B1379 (the
source audit, "no unforced collapse", S6); docs/THEOREM_LEDGER.md Part I; docs/UNIQUENESS_THEOREM.md. Nielsen (1917: every automorphism of F₂
sends [a, b] to a conjugate of [a, b]^(±1)); Dehn–Nielsen–Baer (realization by homeomorphisms); Morse–Hedlund (1940); the
classification of compact surfaces.
