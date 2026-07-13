# B570 — THE ALLOWED-PLAYS CAMPAIGN: results ledger

**Run 2026-07-14** (21 agents: 12 compute cells + verifiers + AP6 synthesis; 0 errors).
C3 and Q-A ran first inline by owner directive (C3_RESULT.md, QA_RESULT.md — C3
independently re-derived and confirmed; Q-A corroborated by the campaign's own QA
cell). The theorem: `THE_SELECTION_RULES.md`. Every cell adversarially verified;
verifier repairs applied at banking (noted per cell). Locks: 105 new tests green
(`test_b570_{ap1,ap2,ap3,ap4,ap5,c1,c2,c4,qa,c3_level2,qa_trichotomy,theta_odd_spine}.py`).

## The clause cells

**AP1 — the cast monoid 𝒞 (CONFIRMED, verifier full-holds).** The anomaly-free
casts (Σmᵢχᵢ ≡ Σmᵢχᵢ³ ≡ 0 mod 11, χ = (1,3,6,7)) form a finitely generated monoid
with a **35-element Hilbert basis** (generator totals in {7,10,…,19}; completeness
by independent DP-reachability vs brute force to total 80, zero mismatches;
verifier extended to 500). Achievable totals = {0,7} ∪ [10,∞): exactly 8 forbidden
totals. The three B568-SQ minimal casts = the bottom nonzero stratum. The base
cast (1,1,1,1) fails at (lin,cub) = (6,4) — the banked T2 arithmetic.

**AP2 — the allowed-theater table (CONFIRMED; one repair).** All 243 consistent
abelian (ℤ/N, q) theaters, N ≤ 24, gates-first, plus Fib/DFib/Ising/SU(2)₁..₄:
**Tr ρ(A₁) = +1 exactly for every abelian theater** — a closed-form Gauss–Milgram
theorem, q-independent. Z always real; full value set {−1/φ, 0, 1/φ², 1} (the
golden values enter with the Fibonacci theories). 249/250 theaters SIGHTED (only
N=1 blind). Repair (verifier catch): the DFib Gauss–Milgram gate was hardcoded in
the cell's code; the verifier computed it independently (G = 2+φ = D_tot exactly,
c = 0) — true, but the gate must be computed, not asserted; noted in the open list.

**AP3 — the clock theorem (CONFIRMED, verifier full-holds).**
**ord(A₁ mod N) = π(N)/gcd(π(N), 2)** (π = Pisano period): proved, two methods,
zero exceptions for all N ≤ 1000. The stage ticks at Fibonacci–Pisano frequencies.
The prereg's "c mod 24 phase" clause is FALSIFIED cleanly: ρ(A₁) = [T,S] is a
commutator, algebraically independent of any overall phase on T.

**AP4 — the chiral-selector table + THE FIFTH WALL (CONFIRMED; two repairs).**
Table (exact weight arithmetic, two routes/row): 27|_H **complex** for
Spin(10)×U(1), SU(3)³, SU(6)×SU(2), G₂×SU(3); **self-dual** for F₄, Sp(8).
Reachability: the object's E₆(ℂ) holonomy (B565 construction) factors through the
**principal SL(2,ℂ)**, which is θ-stable (the F₄-principal nilpotent is regular in
E₆ — Jordan (17,9,1) on the 27 from both gradings), and every SL(2,ℂ) rep is
self-dual: **the 27 restricted to the holonomy closure is vector-like for ANY
E₆-embedding of the rank-1 holonomy. The preregistered falsifier fired: the
chirality wall holds even complexified — the FIFTH WALL.** Chiral rows exist;
none is reachable by the principal transfer. Repairs: the "self-dual iff H ⊆ F₄
or Sp(8)" biconditional DOWNGRADED to conjecture (6 subgroups checked; converse
unproven); the Zariski-density step should cite Borel density for the lattice
(conclusion true and standard).

**AP5 — the order obstruction (CONFIRMED, verifier full-holds).** One-line
criterion; program-levels table ord = {3:4, 5:10, 11:5, 15:20, 30:60, 165:20,
1155:40} (two methods). Retro-kills B567's spectrum claims computedly (6 ∤ 20,
6 ∤ 40); passes C3's banked order-4 block.

## Lane C (the seventeenth question)

**C3 (banked separately, run first): the θ-odd 3-space at level 2 is dynamically
alive** — non-scalar SU(3) monodromy, order 4, eigenvalues {1, ±i};
independently re-derived, convention-robust. See C3_RESULT.md.

**Q-A (banked separately + campaign corroboration): the trichotomy resolves to
the third branch.** θ fixes the geometric component (principal sl₂ ⊂ F₄ = E₆^θ),
c moves it (Galois pair (5±√−3)/2, min poly t²−5t+7, disc −3); c is the
amphichiral Galois/mirror involution, orthogonal to θ at the group level, equal
to the fold at the tangent after mirror-correction (d(σ∘φ⁻¹) = θ). See
QA_RESULT.md (Level-3 corrected during banking — registry catch below).

**C2 — the gap-chirality duality (CONFIRMED, verifier full-holds).** PROVED
biconditional at SL(2,ℂ), verified on the object: all-traces-real ⟺ ρ̄ ≅ ρ ⟺
conjugates into a real form. All three fail on tr(ab) = (5−√−3)/2 ∉ ℝ. **The
compactness gap and the c-chirality are formally equivalent, both directions** —
you cannot close the gap without losing the object's chirality. It is c-chirality
(not the SM's θ-slot) that the gap is dual to.

**C1 — cusp-sign propagation: NULL (verifier: null well-founded).** The cusp-sign
map acts antilinearly on each of the six 1-dim exponent lines with J² = +1
forced (any antilinear map on a ℂ-line squares to |λ|² ≥ 0) — sign-free by
construction; no discrimination between θ-even and θ-odd exponents. Banked as the
honest null. **Verifier catch (banked as a correction): the registry's T-θTANGENT
wording conflicted with B353** — the amphichiral involution is ANTILINEAR
(conj∘θ); the ℂ-linear θ is realized by the hyperelliptic involution (B353).
Registry entry corrected; QA_RESULT Level-3 rewritten accordingly.

**C4 — the cover-chirality census (CONFIRMED; one phrasing repair).** Every
cyclic cover of 4₁, n = 2..12 — unbranched (symmetry group 8n, full, amphichiral)
AND branched Σ_n(4₁) (orders 5, 16, 45, 121, 320, 841, 2205, 5776, 15125, 39601,
103680 matching the Alexander product exactly) — is **amphichiral. Zero chirality
anywhere in the cover family**; the five-sources handoff's "chiral covers ↔ θ-odd
exponents {4,8}" row is refuted outright. (B470's chiral limbs are the LETTER
tower — the dossier stands.) Repair: methods-count per row stated honestly
(two SnapPy methods on the unbranched family; one SnapPy method + the lens-space
criterion (n=2, q²≡−1 mod 5) + the lifting theorem (n=3,4) on the branched family).

**C5+Q-C — QUARANTINED (verifier kill of the conclusion, upheld).** The cell's
headline discriminating fact ("mirror = entrywise conjugate on the θ-odd block")
is an algebraic tautology, true for any unitary data; and it was computed on the
WZW modular data, not the geometric holonomy Q-C asks about (category mismatch).
The "residue lands in the c-column" conclusion is NOT banked from this cell — the
c-column verdict stands on QA + C2 instead. **Q-C (the residue's transport
through the geometric holonomy) remains OPEN.** The cell's numbers were exact;
its test is not adopted.

## The theorem and the SM audit

`THE_SELECTION_RULES.md` (AP6): a play passes iff M ∈ 𝒞 ∧ T sighted ∧ S reachable
∧ D passes the clock ∧ Λ relational. The SM, run once: **fails S (the fifth
wall), fails Λ (no absolute scale), fails D at every tested level, is unevaluable
at M pending a dictionary (which must now land in the 35-generator monoid), and
has exactly ONE live positive channel — clause T, where C3's order-4 θ-odd
rotation shows the measurement face is chirality-sighted even though the algebra
face is chirality-blind.** Two controls (an AF toy failing only S; the Ising
world failing S by incapacity and M by dictionary) show the clauses discriminate.
The B568-SQ minimal play is recovered as the monoid's ground state.

## The open list

See THE_SELECTION_RULES.md §5 (10 items), headed by: the AP4 biconditional
converse; Q-C's honest transport computation; whether any play can couple to the
C3 channel; and whether the object's c-chirality (the one it has, gap-dual by C2)
can be spent by any selector at all.

Firewalled. Nothing to CLAIMS.md.
