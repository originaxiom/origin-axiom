# B1475 — THE SPIN SWAP, PHASE 1b: on every one of the seven swap members NO spin structure is mirror-invariant — amphichiral manifolds none of whose spin structures is amphichiral — and the orientation-odd, spin-dependent quantity Im R₁^{(s)}(t) is a continuous invariant there, nonzero on all seven and in √3·ℚ at t = 2; zero on the knot

**Verdict: PROVED** (scope: the seven swap members and three fix controls of the 112-family; reach *class*; the
theorem-shaped statement for m003 by hand, for the others by computation on every spin structure and every reversing
isometry found). cc (main), 2026-10-04. Pre-registration sealed at `37bde38e` (sha256 `1d03d430…`) before any cell
ran. L246 Phase 1b: **advanced and paid.** **The prize first:** the family contains amphichiral manifolds on which
*no* spin structure survives the mirror — the fermionic bit has no mirror-symmetric value there — and the knot A5
chose is not one of them (both of its spin structures are mirror-invariant, B279 and here). No physics is banked.
**0 of 19.**

## 0. Seen first

As sealed: `topic_sweep.py "spin structure|orientation-odd|2-torsion|Im R|mirror-invariant|amphichiral spin"` —
VERDICT 45 of 1347 arcs (NEGATIVE 2, OPEN 1, PROVED 42); B849, B1224/B1239, B279, B1474, B1471 read. **Literature:**
the torsor picture only; whether "amphichiral manifold with no amphichiral spin structure" has a name in the
literature was not searched — no novelty is claimed for the phenomenon, only for its occurrence in this family.

## 1. What was computed, and one post-seal correction

`verification/spin_quantity.py` → `spin_quantity.json`, `spin_quantity_run.txt`: for each member, every spin structure
s = ρ⊗χ (χ ∈ Hom(π₁, ±1): 2 on m003, m207, t12838, o10_150695, m004, t12839; 4 on s955, s957; 8 on s960, s961), the odd
Wada functions R₁^{(s)}, R₃^{(s)} at t ∈ {2, 3, 0.6}; for every reversing τ of B1474 the mirror partner τ·χ and the
checks conj R^{(χ)} = R^{(τ·χ)} and D_{τ·χ} = −D_χ; the mirror-invariant spin structures {χ : τ·χ = χ}; D_{s₀}(2).
`verification/spin_index.py` → `spin_index.json`: the class index on twisted lifts where the fibred route reaches.

**Post-seal correction, disclosed.** The sealed partner formula τ·χ = η·(χ∘τ⁻¹) failed the symmetry check on
s960 (24 of 96) and s961 (16 of 96) — the two members where τ* acts nontrivially on the characters — and nowhere else.
The derivation gives τ·χ = (η·χ)∘τ⁻¹ (from C·conj ρ(g)·C⁻¹ = η(g)ρ(τg): conj((ρ⊗χ)(g)) ~ (ρ ⊗ (ηχ)∘τ⁻¹)(τg)); the two
agree exactly when τ* is trivial. Corrected and re-run: 0 failures on all 432 checks; the sealed run is kept
(`spin_quantity_sealed_formula.json`). The mirror-invariant sets changed only on s961 (6 → 4 of 8); no swap member's
"NONE" changed.

## 2. The sealed predictions, scored

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | conj R^{(τ·s)} = R^{(s)} on all of Spin(M) | 85% | **HOLDS, 432 of 432** (after the formula correction) |
| P2 | D_{s₀}(t) ≠ 0 on all seven swap members; 0 on the fix controls | 90% | **HOLDS**: m003 √3, m207 −4√3, s955 √3/8, s957 8√3, s960 −√3, t12838 56√3, o10_150695 −836√3 at t = 2 (every value in √3·ℚ — the trace field's √−3); controls ≤ 3·10⁻⁴⁷ |
| P3 | m003 has no mirror-invariant spin structure; at least one other swap member has none | 90% / 60% | **HOLDS, STRONGER: none of the seven has one** — on every reversing isometry found, every spin structure is moved (m003 by hand: H¹ = ℤ/2 forces τ* = id, so (1+τ*)χ = 0 ≠ η₀) |
| P4 | on s957 and s960 some spin structure off the geometric K-orbit is mirror-invariant | 55% | **FAILS**: none on either |
| P5 | I(ρ⊗χ) = 0 for every sign character on m003, m004, t12839 | 80% | **PARTLY REACHED**: on t12839 (+LR level 4): 40 parabolic ends, 80 rows, **I = 0 on the 22 rows where the sign twist is a module** and "not a module" on 58 (the twist breaks the bundle relation there); at level 1 the engine's curve ends are elliptic (−LR) or absent (+LR), so the geometric lift of m003 and m004 is not reached by this route — the m003 index on its geometric lift **stays owed** (instrument limit, not a result) |

Fix controls' mirror-invariant spin structures: m004 2 of 2 (B279), t12839 2 of 2, s961 4 of 8.

## 3. What it means

- **B849 read on (M, s).** B849's argument — X(M) = X(M̄) by the isometry, X(M̄) = −X(M) by oddness, so 2X = 0 —
  binds an orientation-odd invariant of *M*. For an invariant of the pair (M, s) the isometry gives X(M, s) = −X(M, τ·s),
  which constrains X(M, s) only when τ·s = s. On the seven swap members no s satisfies that for any τ, and
  D_s(t) = Im R₁^{(s)}(t) is a continuous, t-dependent, nonzero orientation-odd invariant of (M, s) on an *amphichiral*
  manifold — the thing B849 proves cannot exist on m004, where both spin structures are mirror-fixed and D ≡ 0.
- **The statement for Phase 1c.** For the family's amphichiral rank-one members: *either every spin structure is
  mirror-invariant for some reversing isometry (m004, t12839), or a subset is (s961, m206, o10_150696, o10_150707 —
  the last three by the trivial K of B1474), or none is (the seven)*; the knot is in the first class by B279's
  theorem, and A5 is the choice of the knot. The three classes are the three values of the fermionic bit's fate under P.
- **The √3.** Every D_{s₀}(2) lies in √3·ℚ: the odd part of the twisted polynomial takes values in √−3·ℚ(t) on the
  family (the invariant trace field is ℚ(√−3)); a computed fact, not interpreted here.
- **Not claimed:** any physics; any selection; that D is the "chirality carrier" of L246's thesis — that is Phase 2's
  question (B279's unbanked η link). **The imported expectation, stated separately:** none. **0 of 19.**

## 4. Errors in this arc

The partner formula (§1), corrected and disclosed, the sealed run kept; the index route's reach at level 1
misjudged in the seal (C4 was sealed on three members and reaches one); P4 wrong (both swap members with larger
H¹(M;ℤ/2) have no mirror-invariant spin structure either).

**Provenance.** `verification/spin_quantity.py` → `spin_quantity.json`, `spin_quantity_run.txt`,
`spin_quantity_sealed_formula.json`, `spin_quantity_run_sealed_formula.txt`; `verification/spin_index.py` →
`spin_index.json`, `spin_index_run.txt`. Lock `tests/test_b1475_spin_swap_1b.py`. Cross-refs L246, B1474, B1471,
B849, B279, B1141, B1382 (the parent's Pin type — the same bit, for Phase 1c).
