# LIT-GATE — the level-ladder campaign (run 2026-07-15, seat cc2)

Four AI literature sweeps (three sonnet + one haiku searchers; synthesis by this seat).
Per house style: an AI sweep DE-RISKS novelty language, it does not close it —
anything marked APPEARS-UNRECORDED is NEEDS-SPECIALIST before any novelty claim.

## Verdict table

| Finding | Lit verdict | What the literature says |
|---|---|---|
| The clock is Pisano-anchored (PRED-4) | **KNOWN-MECHANISM (deflates + upgrades)** | The congruence-subgroup chain — Coste–Gannon (math/9909080, conditional), **Bantay** (CMP 233 (2003) 423, N = ord(T), conductor F = ℚ(ζ_N)), **Ng–Schauenburg** (CMP 300 (2010) 1, Thm 6.7/6.8/7.1: projective kernel ⊇ Γ(N), N = FSexp = ord(θ); linear lifts N \| ord ρ(T) \| 12N), **Dong–Lin–Ng** (ANT 9 (2015) 2121, Thm 3.10(ii): kernel ⊇ Γ(n), n = ord of the actual T) — proves ρ_k factors through SL(2, ℤ/ord(T_k)). Hence ord(ρ_k(A₁)) **divides** ord(A₁ mod ord(T_k)) automatically. |
| — the equality per level | **NEW DATA on a known frame** | Verified against our exact T-exponents: ord(T_k) = 12, 84, 180, 48 at k = 1..4; divisibility holds at every rung (1\|12, 4\|24, 60\|60, 12\|12); **equality at k = 3, 4; proper quotient at k = 1, 2.** The residual question is now injectivity of ρ_k on ⟨A₁ mod ord(T_k)⟩ — the literature does not address orders of specific hyperbolic mapping classes (agent: NOT-FOUND; no Pisano connection anywhere). PRED-5's replacement mechanism is this congruence statement. |
| The subfield ladder / splitting law (L74) | **FRAMED-KNOWN, COMPUTATION UNRECORDED** | The framework is fully established: Coste–Gannon (PLB 323 (1994) 316) — ℚ[S] abelian, Galois acts by signed permutations; **Bantay** (math/0102149 Prop. 4) — **ℚ[S] = ℚ(ζ_N) exactly, N = ord(T)** (so our level-4 arithmetic lives in ℚ(ζ₄₈), sharpening the ζ₁₉₂ envelope; FSS94 confirm M = 3 for E₆, N = 3κ). But **no structural theorem predicts WHICH subfield appears per level** for any rank ≥ 2 algebra (Gannon math/0103044 explicitly defers to case-by-case Weyl-lattice computation); the 2021-22 Galois-orbit papers (Buican–Radhakrishnan, Plavnik et al.) have no affine-E₆ content beyond level 1. **The E₆ subfield ladder computation is NOT FOUND.** Rank-1 folklore parallel: Ising = SU(2)₂ (κ=4) generates √2; Fibonacci (κ=5) generates √5 — our E₆ ladder (√5 at κ=15, √2 at κ=16) mirrors the A₁ pattern. Disambiguation guard: the "E₆ modular invariant" literature (CIZ SU(2)₁₀) is the unrelated ADE label — the repo already knows this (Face IV). |
| — external corroboration at k = 4 | **NEW HINT (NOTICED-grade)** | FSS94 (hep-th/9410010, p.29) list **E₆ level 4** as a "Pure Galois Invariant" (scaling ℓ=7, 7² ≡ 1 mod 48, type Extension/HSE); Gannon's classification flags E₆ exceptional invariants at **k = 4**, 6, 12. The level where our theater goes silent (Z₄ = 0) is exactly E₆'s first exceptional-modular-invariant level. Whether the extension invariant's existence is the *mechanism* of the zero (the trace reorganizing across the extended chiral algebra) is a sharp, checkable hint — proposed for the ledger, not claimed. |
| Z₄ = 0 exactly (H133's kill) | **APPEARS-UNRECORDED (needs-specialist)** | **Jeffrey, CMP 147 (1992) 563, Prop. 4.5** gives the exact torus-bundle formula for **general simply-laced G** (E₆ qualifies) and monodromy TᵖS — A₁ ~ T³S (unique trace-3 hyperbolic class, disc 5, h=1) — as a Weyl-sum of coroot-lattice Gauss sums with B_w = 3 − w − w⁻¹. **No published evaluation for any exceptional G exists.** The only documented exact-vanishing mechanism (Jeffrey Thm 3.7: lens spaces, Z = 0 iff p ≡ 2 mod 4, gcd(r,p)=1) is structurally inapplicable (our \|H₁\| = \|det(A₁−I)\| = 1). A multi-term Weyl–Gauss sum collapsing to exactly 0 at one r (=16) while giving exactly ±1 at neighbors matches no recorded criterion. |
| The Z-ladder {+1,+1,+1,0} / flatness | **FLATNESS KNOWN, CONSTANCY UNRECORDED** | "Growth rate 0" for Anosov torus bundles is documented (Andersen–Jørgensen arXiv:1206.2552 §5.1, via Jeffrey; Andersen–Petersen arXiv:1803.09510 Thm 1.3; Charles TAMS 2012), proven for SU(2)/SU(n) only. Exact level-independent constancy Tr ρ_k = +1 is NOT-FOUND anywhere. Funar (G&T 17 (2013) 2289): Sol bundles indistinguishable by ALL TQFT invariants (congruence-property-based) — context for why isolated-level arithmetic is structurally admissible. Cautionary precedent: Karowski–Schrader–Vogt (Exp. Math. 6 (1997)) reported anomalous numerics in the 4₁-surgery family (different phenomenon; methodological footnote). |
| L76 tower 1 (cover torsion = Alexander resultants) | **KNOWN (classical)** | Fox's formula, per Gordon's survey (LNM 685 (1978) 1–60): \|H₁\| = \|Res(Δ, tⁿ−1)\|. The figure-eight Lucas/Fibonacci closed form and the Pisano-divisibility phrasing were NOT FOUND in knot-theoretic sources (the underlying identities L_{2n}−2 = 5F_n² etc. are standard number theory) — the cell claims no novelty regardless. |
| ord(T) closed form for affine E₆ | **NOT IN THE LITERATURE** | Kac–Peterson give the eigenvalue formula, Vafa finiteness; Coste–Gannon give a sufficient N only for A_r (n = 24(r+1)). No table or closed form for E₆ found — our exact per-level ord(T) values are computed, not citable. |

## Corrections this gate forces on FINDINGS.md

1. **PRED-4's row is rescored** from "HOLDS in form (map underdetermined)" to: divisibility is
   the Ng–Schauenburg/Bantay/DLN congruence property (KNOWN); the campaign's contribution is
   the exact equality pattern {quotient, quotient, equal, equal} at k = 1..4 and the exact
   ord(T_k) values — data on a known frame. The Pisano candidate-set framing (N ∈ {6, 9, 12,
   16, …}) is RETIRED as numerology-adjacent; the canonical modulus is ord(T_k).
2. **New residual question registered:** is ρ_k injective on ⟨A₁ mod ord(T_k)⟩ for all
   k ≥ 3? (True at 3, 4; false at 1, 2.) A proof would make the clock law exact at all
   higher rungs.
3. The level-5 follow-on gains a sharp pre-computable prediction: ord(T₅) from the
   T-exponents at κ = 17, and the clock must divide ord(A₁ mod ord(T₅)); under the
   injectivity conjecture, equality.
4. **A second-pipeline verification cell is REGISTERED (not run):** evaluate Jeffrey's
   Prop. 4.5 (CMP 147 (1992) 563, general simply-laced G, monodromy T³S ~ A₁) for E₆ at
   r = 13, 14, 15, 16 — a Weyl-sum of coroot-lattice Gauss sums, fully computable — and
   compare (up to the framing phase) with our Z-ladder {+1, +1, +1, 0}. Agreement would be
   a disjoint-pipeline confirmation in the B577 style; the r = 16 term would exhibit the
   Z₄ = 0 as a Gauss-sum collapse, likely exposing the 2-adic mechanism (16 = 2⁴ is the
   only prime-power conductor in range with det B_w interactions at the even prime).

5. **Bantay's conductor theorem sharpens the envelope and the priced-out values:** ℚ[S] =
   ℚ(ζ_{ord T}) means the level-4 magnitudes live in ℚ(ζ₄₈)∩ℝ (degree ≤ 8) and level-3's in
   ℚ(ζ₁₈₀)∩ℝ (degree ≤ 24). The one unidentified level-4 even value therefore has a
   degree-{1,2,4,8} minimal polynomial with coefficients > 1e14 (our sweep bound) — exactly
   recoverable from the counts via sympy if ever needed; the six level-3 unknowns may be
   degree 24 (beyond the sweep), consistent with being genuinely priced out.
6. **NOTICED rows proposed from the gate:** (i) the k = 4 exceptional-invariant coincidence
   (row above); (ii) the rank-1 parallel — inert-import forms recur across algebras at
   prime-power conductors (A₁: √2 at κ=2², √5 at κ=5; E₆: √5 at κ=3·5, √2 at κ=2⁴).

**Gate methodology:** three sonnet + one haiku search agents (per the seat's cost rule),
primary sources downloaded and text-extracted where available; synthesis and the exact
ord(T) verification computed by this seat. Agent mis-attributions caught and corrected in
the record (de Boer–Goeree ≠ the quasi-Galois paper — that is Fuchs–Schellekens–Schweigert
hep-th/9412009; Gepner hep-th/0606081 ≠ Gannon). AI sweeps de-risk; APPEARS-UNRECORDED
rows remain NEEDS-SPECIALIST before any novelty claim (H2 discipline).
