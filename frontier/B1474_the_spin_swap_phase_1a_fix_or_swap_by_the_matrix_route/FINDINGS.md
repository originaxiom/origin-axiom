# B1474 — THE SPIN SWAP, PHASE 1a: the mirror's action on the spin structure decided at matrix level — GENUINE SWAP on seven amphichiral non-knots, FIX on six including the knot and its tower cover; the swap is well defined only modulo the orientation-preserving isometries' sign characters K, and both routes agree on every member decided

**Verdict: PROVED** (scope: the 112-family's 54 rank-one members; reach *class*; the swap/fix table a computed fact, the
thesis of L246 untouched and firewalled). cc (main), 2026-10-04. Pre-registration sealed at `cb09deb0` (sha256
`1f6cdb42…`) before any member but the two controls ran. L246 Phase 1a: **advanced**. **The prize first:** the family
contains amphichiral members on which no orientation-reversing isometry preserves the geometric spin structure — the
case B279 proved impossible for the knot — and the knot A5 chose is not one of them. **0 of 19.**

## 0. Seen first

As sealed: `topic_sweep.py "spin structure|…|SL(2,C) lift|1-loop"` — VERDICT 18 of 1343 arcs (B279, B804, B1118, B1141,
B940/B933, B1471 read). **Literature:** the torsor fact — spin structures ↔ SL(2,ℂ) lifts of the holonomy, an affine
space over H¹(M;ℤ/2) (Culler 1986, "Lifting representations to covering groups") — searched for and used, not re-read
here; nothing else searched. Nothing on main had the fix/swap table beyond m004.

## 1. The route and the two post-seal repairs, disclosed

For each rank-one member, every automorphism τ of π₁ with ρ∘τ ≅ conj ρ in PSL(2,ℂ) is found by word search (images of
the generators as reduced words of length ≤ L, L = 5 → 7 until a solution; a single C ∈ SL(2,ℂ) with
C·conj ρ(g)·C⁻¹ = η(g)·ρ(τg) for all generators; the relators preserved). **η is the sign character: trivial = that
isometry FIXES the spin structure of the geometric lift, nontrivial = SWAPS it with ρ⊗η.** `verification/spin_swap.py`
→ `spin_swap.json`, `spin_swap_run.txt`; controls `controls.json` (pre-seal) and `repair_check.json`.
- **Repair 1 (efficiency; the route unchanged):** the sealed implementation solved C by an SVD per full tuple of
  candidate words and stalled on the first three-generator member (four members in thirty minutes); replaced by
  solving C from the first two generators' candidate pair and *testing* the rest by matrix distance. The two controls
  reproduce exactly (`repair_check.json`: m004 FIX, 40 solutions; m003 SWAP, 40; m206 FIX, 40).
- **Repair 2 (a cap, disclosed):** members with no orientation-reversing isometry by SnapPy are searched to L = 5 only
  — exhausting L = 7 on a three-generator chiral member costs hours and can only confirm an absence SnapPy states.
  Their row reads NONE-at-L5.

## 2. The sealed predictions, scored

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | every amphichiral member yields a τ at L ≤ 7; no chiral member yields any | 85% | **13 of 13 yield** — twelve on SnapPy's default presentation, o10_150696 only on its shortest presentation (none to L = 8 on the default; 8 solutions at L = 6 after retriangulation); **41 of 41 chiral yield none** (at L = 5) |
| P2 | FIX on m004, m206, s961, t12839, o10_150696, o10_150707; SWAP on m003, m207, s955, s957, s960, t12838, o10_150695 | 80% | **13 of 13 as predicted** once K is read (§3): 12 directly, s961 as FIX-able after its MIXED row |
| P3 | one η per member (all reversing isometries agree) | 70% | **FAILS, informatively:** s957 (two η's), s960 (three), s961 (three, one trivial). The η-set is a **coset η₀K** of the group K of sign characters of the orientation-*preserving* isometries (§3) |
| P4 | on SWAP members η = (−1)^φ on m003, m207, s960, t12838, o10_150695; a torsion character on s955, s957 | 75% | **HOLDS** on all seven, read modulo K where K is nontrivial |
| P5 | every knot complement among the 54 is FIX | 95% | **HOLDS** (m004 is the only H₁ = ℤ member) |

## 3. The finding P3's failure forced: the swap is defined modulo K, and it is genuine on seven

`verification/preserving_characters.py` → `preserving_characters.json`: the same search with target ρ instead of conj ρ
finds the orientation-preserving automorphisms σ (ρ∘σ ≅ ρ) and their sign characters χ_σ; **K = ⟨χ_σ⟩** (closed under
products in the post-processing; the search returns generators). Then for every member: the reversing η's found lie in
one coset η₀K (checked), and

> **the mirror genuinely swaps the geometric spin structure iff 1 ∉ η₀K — iff no orientation-reversing isometry fixes it.**

| member | H₁ | K | reversing η's | verdict | torsion route (B1471, odd n real?) | agree |
|---|---|---|---|---|---|---|
| m004 | ℤ | 1 | 1 | **FIX** | real | ✓ |
| m206 | ℤ/5⊕ℤ | 1 | 1 | **FIX** | real | ✓ |
| s961 | (ℤ/4)²⊕ℤ | {1, (−1,1,1), (1,−1,−1)}+ | = K | **FIX-able** | real | ✓ |
| t12839 | ℤ/3⊕ℤ/15⊕ℤ | 1 | 1 | **FIX** | real | ✓ |
| o10_150707 | (ℤ/2)²⊕ℤ | 1 | 1 | **FIX** | real | ✓ |
| m003 | ℤ/5⊕ℤ | 1 | (−1)^φ | **GENUINE SWAP** | complex | ✓ |
| m207 | (ℤ/3)²⊕ℤ | 1 | (−1)^φ | **GENUINE SWAP** | complex | ✓ |
| s955 | ℤ/20⊕ℤ | 1 | torsion char. | **GENUINE SWAP** | complex | ✓ |
| s957 | ℤ/4⊕ℤ | {1, (1,1,−1)} | (1,−1,±1) | **GENUINE SWAP** | complex | ✓ |
| s960 | ℤ/2⊕ℤ/10⊕ℤ | order 4 | a coset without 1 | **GENUINE SWAP** | complex | ✓ |
| t12838 | (ℤ/7)²⊕ℤ | 1 | (1,−1,1) | **GENUINE SWAP** | complex | ✓ |
| o10_150695 | ℤ/5⊕ℤ/25⊕ℤ | 1 | (−1)^φ | **GENUINE SWAP** | complex | ✓ |
| o10_150696 | (ℤ/11)²⊕ℤ | 1 | 1 (shortest presentation, L = 6) | **FIX** | real | ✓ |

**The torsion route is blind to K** (R is invariant under ρ ↦ ρ⊗χ for χ ∈ K), which is exactly why it reports
"real at odd n" iff 1 ∈ η₀K: the two routes agree on all thirteen members, and the matrix route is the finer one.
**Seven genuine swaps, all non-knots; six fixes, the knot among them; A5's knot is on the fixed side.**

## 4. What it means, and what it does not

- L246 Phase 1a is paid: the swap is a fact of the family, decided by a route that does not use the torsion, with the
  mechanism that made the sealed P3 fail named (K). The thesis — the construction excluded, at A5, the members where
  the object's own ℤ/2 acts nontrivially on its fermionic bit — is **supported in its first step and not yet tested in
  its physical one**: Phase 1b asks whether the swap carries a continuous orientation-odd quantity; Phase 2 is B279's
  unbanked η link. No physics is banked here. **The imported expectation, stated separately:** none. **0 of 19.**
- The question Phase 1c must answer is now sharp: on the SWAP members *no* spin structure in the geometric lift's
  K-orbit is mirror-invariant — what, then, is the set of mirror-invariant spin structures on those members (it may
  be empty, or lie in another K-orbit), and does the index of B1297 see the difference?

## 4b. Coverage and the kind of certificate (the two codex seats' audit of the design, read 2026-10-04)

Both codex lanes read B1474's seal within hours and asked three things, all taken: **(i) coverage** — the search stops
at the first word length with a solution and after 40 witnesses, so a verdict is for the *found reversing witnesses
together with the orientation-preserving generating set K* (§3), not for an enumerated Isom(M); on every member the
found η's lie in one coset η₀K, which is what the verdict needs; **(ii) the guard** — a sign pattern that is not a
character of π₁ now raises instead of being appended (none was ever observed); **(iii) the certificate is numerical** —
50 digits, SVD tolerance 10⁻²⁵, with the conjugacy residual, C's invertibility and the relator check retained; it is
not an exact or interval certificate. The app lane's note that a "conjugate subtraction" R_s − conj R_{τ·s} vanishes
identically is right and is why Phase 1b's quantity is Im R_s, not that difference.

## 5. Errors in this arc

The sealed implementation's cost (Repair 1) and the cap (Repair 2), both disclosed; the K search returns generators,
not the closed group (closed in post-processing; verdicts unchanged); o10_150696 beyond the route's reach at L = 8 on the default presentation and
decided only on its shortest one (relators of length 23; 8 solutions at L = 6) — the presentation dependence of the search's reach is a limit of the instrument, stated.

**Provenance.** `verification/spin_swap.py` → `spin_swap.json`, `spin_swap_run.txt`, `controls.json`, `repair_check.json`;
`preserving_characters.py` → `preserving_characters.json`; `o10_150696_L8.json`, `o10_150696_retri.txt`. Lock
`tests/test_b1474_spin_swap_1a.py`. Cross-refs L246, B1471, B279, B1141, B1118, B197, B1234.
