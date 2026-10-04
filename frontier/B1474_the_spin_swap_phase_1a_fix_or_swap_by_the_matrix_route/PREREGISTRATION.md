# B1474 — PREREGISTRATION: THE SPIN SWAP, PHASE 1a — does the mirror fix or swap the spin structure, member by member, by a route independent of the torsion?

**Sealed before any member but the two controls is run.** cc (main), 2026-10-04. Lead L246 (the execution plan the
owner approved 2026-10-04), Phase 1a. The question: on which amphichiral members of the 112-family does an
orientation-reversing isometry fix the spin structure of the geometric lift, and on which does it swap it with the
other — decided at matrix level, not through the twisted polynomial.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "spin structure|spin structures|H^1(M; Z/2)|lift to SL(2|SL(2,C) lift|1-loop|one-loop"`:
  VERDICT 18 of 1343 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 15). Read: **B279** (the amphicheiral involution
  τ of 4₁ FIXES both spin structures, by the S³-bounding spin structure and the ℤ/2-torsor argument; "for every
  ambient symmetry of every knot complement"; chat-2's "SWAP → chiral matter possible" shut on m004; its firewall
  names the η / parity step as unbanked), **B804** (m004's cusp spin structure bounding for every spin structure),
  **B1118/B1141** (the discrete freedom ledger {C, P, spin lift}; "fermionicity and chirality both hang on" the spin
  lift; the object's beat selects it on m004), **B940/B933** (the sealed Dirac run on (m004, ρ₁)), **B1471** (the odd-n
  cells: conj R_n = R_n^{ρ⊗ε} on seven amphichiral members with ε nontrivial — the torsion route to the same
  question, which this arc must not reuse as evidence), **B197** (the m003/m004 tie broken by torsion), **B1234** and
  the lane's xB012 (what A5 buys and costs). **Literature:** spin structures on an oriented 3-manifold form a torsor
  over H¹(M; ℤ/2) and correspond to lifts of the holonomy from PSL(2,ℂ) to SL(2,ℂ) (Culler 1986, "Lifting
  representations to covering groups"); an isometry acts on the torsor affinely, so on m003 (H¹(M;ℤ/2) = ℤ/2, no
  nontrivial automorphism) a swap lives in the translation part and cannot be read from the action on cohomology
  alone — which is why the route below is at matrix level. Culler not re-read here; the torsor fact is standard.

## 1. The route, fixed now

For each member M with H₁ of rank one (the 54 of B1471) and lifted holonomy ρ (SnapPy HP, lift repaired): find every
automorphism τ of π₁(M) with ρ∘τ ≅ conj ρ in PSL(2,ℂ) by word search — images w_g of the generators (reduced words of
length ≤ L, L raised from 5 to 7 until a solution appears) with tr ρ(w_g) = ± conj tr ρ(g), a single C ∈ SL(2,ℂ) with
**C · conj ρ(g) · C⁻¹ = η(g) · ρ(w_g)** for all generators at once, and the relators preserved (ρ(τ r) = ±1). Such τ
are exactly the orientation-reversing isometries' actions (an orientation-preserving one has ρ∘g ≅ ρ, and ρ ≇ conj ρ
for a finite-volume hyperbolic manifold). **η: π₁ → {±1} is the sign character; η trivial = the isometry FIXES the
spin structure of ρ; η nontrivial = it SWAPS it with ρ⊗η.** Up to 40 solutions per member are collected (they repeat
modulo inner automorphisms) and the **set** of η's is reported. Instrument `verification/spin_swap.py`
(sha256 86e60de705008642 at the seal; `verification/controls.json`), run before the seal on the two controls only and disclosed below.

## 2. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | every amphichiral member (13 by isometry) yields at least one τ at L ≤ 7; no chiral member yields any (the control that the route cannot find a swap where there is no mirror) | 85% |
| P2 | FIX on m004, m206, s961, t12839, o10_150696, o10_150707; SWAP on m003, m207, s955, s957, s960, t12838, o10_150695 — the torsion route's split, now by an independent route | 80% |
| P3 | on each member the set of η's is a single character: all reversing isometries agree (equivalently, orientation-preserving isometries carry a trivial sign character) | 70% |
| P4 | on the SWAP members η is the character B1471 found: (−1)^φ on m003, m207, s960, t12838, o10_150695; a torsion character on s955 and s957 | 75% |
| P5 | every knot complement among the 54 (H₁ = ℤ: m004 and any other) is FIX — B279's theorem as a control | 95% |

**What a failure would mean.** P2 false anywhere: the two routes disagree — an instrument error on one side, to be
found before any verdict (the arc's kill, per L246). P3 false: fix/swap is a property of the isometry, not the
manifold, and L246's thesis must be restated per isometry. P5 false: B279's theorem or this instrument is wrong,
and the arc stops to find which.

## 3. Disclosed

Run before the seal: m004 (L = 6, 40 solutions, every η trivial → FIX) and m003 (L = 5, 40 solutions, every η =
(−1)^φ → SWAP), as the instrument's controls — one from B279's theorem, one from the torsion route. Known before
the seal: B1471's split of the thirteen (P2 is at 80% because of it, not 50%). Not run: any other member.

## 4. Scope

Frame F-CI; object the 112-family at level one, the 54 rank-one members; reach *class*; hypotheses: SnapPy's HP
holonomy, word length ≤ 7 (a member with no τ found at L = 7 is reported UNDETERMINED, not FIX). Nothing here is
a count on a vacuum or a physics claim; the thesis of L246 is firewalled and this arc decides only the fix/swap table.
