# B1495 — PREREGISTRATION: THE ORBIT IN ONE MODULE — L8a15's three members, one deck orbit, read as a single rank-15 module: its 10′ count is three by additivity; is its 5̄′ count three too, or do the cross terms between generations break the shape?

cc (main), 2026-10-07. The SM seat's three-orbit (verified on main at S74): +LLLR is the only generated state whose
companion has three ends, and on that companion L8a15 the three one-generation members ν, τν, τ²ν are one orbit of
the deck ℤ/3 — the three fixed points of L³R acting by translation. By Shapiro the three is the count of the state at
four ⊗ Ind ν ⊗ ℂ[T]: it lives in the relation between the state and its companion (the owner's rule of the day). The
orbit as a reading of "three generations" is a selection until FK14 is ruled; this arc does not adopt it. It reads
one number nothing has read: **the three members put into one module.** Sealed before the cross terms are read on
L8a15. No physical quantity is predicted. 0 of 19.

## 1. The question

W_i = W₁(ν_i) = [[V_i, z_i], [0, 1]] (rank 5; the line is trivial at sign characters) for the three members. The orbit
module W = W₁ ⊕ W₂ ⊕ W₃ (rank 15) has I(W) = Σ I(W_i) = −3 by additivity of the class index over direct sums: the
10′ count is three, trivially. Its exterior square is not a direct sum of the pieces' squares:
Λ²W = ⊕_i Λ²W_i ⊕ ⊕_{i<j} W_i ⊗ W_j, so I(Λ²W) = Σ_i I(Λ²W_i) + Σ_{i<j} I(W_i ⊗ W_j) = −3 + (the cross terms). In the
seat's dictionary the 5̄′ count is the exterior square's; three generations in one module need I(Λ²W) = I(W) = −3,
i.e. **every cross term zero.** Each cross term is a rank-25 module on a three-cusped manifold, read by B1492's stacked
instrument.

## 2. Seen first

`VERDICT topic-sweep /cross term|tensor product of|W_1 \(x\) W_1|orbit module|one module|deck orbit|three-orbit|Lambda\^2 W|Λ²W/: 10 of 1366 arcs on main match (PROVED 10)`
— on point: B1443 (the coupling tensor over a deck orbit of generation-shaped backgrounds on the root's three-fold cover, in the earlier SM frame), B1438 (a deck orbit does not mix or split), B1485 (the members read singly); the rest the earlier frame's census arcs.
On the seats: the SM seat's three-orbit dossier (Propositions A and B), sm:B1509 (the join: I(W₁) = −1 iff e ∪ c = 0;
Λ²W₁ filtered by Λ²A and A ⊗ 1), sm:B1535 (Theorem C: I(Λ²W₁) ∈ [−n(ν³ ⊗ ρ), 0]). On main: B1485/B1492 (the members
read (−1, −1) each), B1486 (two orders fuse into an irreducible module counting zero — a different sum of two members).
**Literature:** none for the cross terms.

**Seen before the seal — the control (`cross_m136.json`):** on m136, whose two members are the two sign characters
with an interior class (not a deck orbit), the instrument reads W₁(ν₁), W₁(ν₂) at (−1, −1) each (B1485's numbers), and
the one cross term W₁(ν₁) ⊗ W₁(ν₂) at **I = −1** (the relator check passes at rank 25): the two-member module reads
I(W) = −2 and I(Λ²W) = −3 — the cross term is not zero there, so the criterion can fail. **Nothing has been read on
L8a15 beyond B1492's single members.**

## 3. Disclosed

Numerical (40 digits, 10⁻²⁴); the members' classes are B1492's (`survey_L8a15.json`); the extension classes are
representatives (a different representative of the same class gives an isomorphic W_i). The cross terms' pieces —
V_i ⊗ V_j (rank 16), V_i, V_j (rank 4 each), the trivial line — are not read separately unless a cross term is
non-zero, in which case the piece responsible is named. Not blind to the m136 control.

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **O1** | each of L8a15's three members reads (−1, −1) in this instrument (B1492's numbers reproduced) and the relator check passes on every W_i and W_i ⊗ W_j | 95% |
| **O2** | the three cross terms are equal (the deck ℤ/3 permutes the pairs) | 85% |
| **O3** | every cross term is zero — I(Λ²W) = −3: the three members form one generation-shaped module of rank 15 | 30% |
| **O4** | if O3 fails: the cross term is −1 as on m136, and I(Λ²W) = −6 — the 5̄′ count six for a 10′ count three | 45% |

**Reading rules.** O3 true is the headline: the first generation-shaped three in one module on a state-born object —
relayed to the SM seat with the decomposition before anything is built on it, graded as a **selection** (the orbit sum
is supplied by ℂ[T], the ends; a rule the genesis has not supplied) under THE_BAR, and a FK14 entry. O3 false: the
value and the piece responsible, and the statement that the orbit's three is a 10′ three with a different 5̄′ count —
the deck symmetry relates the generations but does not make their exterior square one generation's. Either way
nothing is promoted.

## 5. Instruments

`verification/cross.py` (B1492's `multicusp.py` imported from its arc; the Kronecker product; the index of each cross
term), the control `cross_m136.json`; hashes in `ARTIFACT_HASHES.txt`.
