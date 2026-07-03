# B380 (D3 substrate) — the Galois covariance laws of the pair tables: symmetries ARE Galois

**Status: banked (frontier) + P61 promoted at banking (exact; two independent computation paths —
the relayed pre-registered census and this repo's full re-verification on the banked tables).
The relayed pre-registration + handoff are the provenance; every claim below re-verified here
cell-exactly. Firewalled.**

## R1 — a new proven symmetry of every banked table: σ₃₁

    t(31a mod o₁, 31b mod o₂) = t(a,b)   (all four components)
verified on ALL cells of ALL SIX tables. Proof (sound, four lines): 31 ≡ 1 (mod 15) fixes every
generator entrywise (entries ∈ ℚ(ζ₁₅)) and fixes Par; σ₃₁ therefore permutes eigenprojectors by
the label map; and 31 ∈ Gal(ℚ(ζ₆₀)/H) so the H-projection commutes and stored values are fixed.
Corollary on (1,2): rows 1↔11 and 9↔19 carry identical full vectors under (a,b) ↦ (11a, 7b) —
half the odd-row content is redundant under a proven symmetry.

## R2 — the mirror is conjugation (upgrade of the banked Coxeter antisymmetry)

    t(a, −b mod 12) = τ₃(t(a,b)),   τ₃: (x,y,z,s) ↦ (x,y,−z,−s)
holds on EVERY (1,2) cell (verified). Mirror-column reality (b = 0) is now DERIVED. Mechanism
gap recorded: no single Galois element induces (a, b) ↦ (a, −b); the candidate mechanism is the
dihedral relation moving the Weyl point (the seam as one member of an SL₂-orbit of Weyl-point
pairings) — flagged as a structural direction, not claimed.

## R3 — the census (16 Galois elements × 6 tables; re-verified here)

c ∈ {1, 31}: pass everywhere. c ∈ {11, 41} (√−3-flip, ζ₅-fixing): EXACT on the trivial-at-3
tower of (1,2) (all 36 odd-row cells fail — the measured domain line), and FULLY exact on
(1,3), (1,4), (2,3), (3,4) — including the new law on the bright (3,4). The eight √5-flipping
elements fail on every table (verified: zero full passes) — **the √5-conjugacy of the sector
constants (P60) lives at trace level only**. And (2,3) is stabilized by the ENTIRE √5-fixing
half-group {1,11,19,29,31,41,49,59} (verified: exactly those 8) — an enhanced symmetry,
mechanism open.

## The F₄ reciprocal duality (the earlier returned claim: now VERIFIED — right object found)

The K2-columns 1 and 5 of (1,2) (the two F₄ carriers): elementwise ratios
{−3/2, −4, −1/4, −2/3, −1/4, −4} — reciprocal pairs {−4, −1/4} and {−3/2, −2/3} exactly; and
the 2-column Gram is EQUAL-NORM: ⟨v₁,v₁⟩ = ⟨v₅,v₅⟩ = 49/115200 with ⟨v₁,v₅⟩ = −13/57600
(perfect-square discriminant — rational eigenvalues, consistent with the banked canonical
full-matrix spectrum {1/576, 1/576, 1/768, 23/19200} up to the normalization of the sector
vectors). My earlier non-reproduction used rows — a wrong-object error on the verifying side,
corrected by the relayed specification.

## Intake of record (hints, not claims)

1/48 = Haar(2T×ℤ/2) and 1/48 = B₂/8 (two readings of the normalization — D3(b) substrate);
the McKay node assignment (2T graph = affine E₆; the 3-local Weil part ↔ the central node);
the dilog-bridge NEGATIVE (no direct 1/48 ↔ vol(4₁) identity; common Eisenstein root only).

## Residues, ranked

(i) row-16 reality (t(16,·) ∈ ℚ(√5)) — cornered by the laws, not yet forced; (ii) the mirror's
non-Galois mechanism (the Ŝ/Weyl-orbit direction); (iii) why 1/12; (iv) (2,3)'s half-group
stabilizer mechanism; (v) the trace-level-only √5-conjugacy (defect tracelessness).

**Provenance.** The relayed PREREG + handoff (committed there before computation); the banked
step0 tables; P56/P57/P60. Locks: `tests/test_b380_galois_covariance.py`.
