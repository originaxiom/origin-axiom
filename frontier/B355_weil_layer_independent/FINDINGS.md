# B355 — the Weil layer, independently: conventions earned, the cross-session tables verified, and the phase null fired

**Status: banked (frontier). Campaign W1.1 (the value-boundary queue, `docs/OPEN_LEADS.md`). Resolves the L56
blocker by independent reconstruction. Firewalled; nothing to `CLAIMS.md`; no physics claim. Numerical tier for
field recognitions (PSLQ, re-verified at higher precision); the construction gates are exact-to-precision.**

## What was built

The Weil representation `W_N` of `SL(2,ℤ/N)` for odd `N ∈ {3,5,15}` on `ℂ[ℤ/N]`, **from scratch, with the
conventions earned rather than assumed**: a systematic search over `T_c = mult e_N(c·x²)`, Fourier kernel
`e_N(d·xy)`, normalization `μ ∈ {i^k√N}` returned exactly the family **`d ≡ −2c (mod N)`, `μ = g_c(N)`** (the
Gauss sum) as the unique relation-satisfying convention; the canonical member is `T = e_N(x²)`,
`S = F_{−2}/g(N)`. `L = S T⁻¹ S⁻¹` (matrix identity verified); the metallic word `A_m = RᵐLᵐ`.

**Gates (all pass; MB12 discipline — the conventions were selected by the relations, then locked):**
`S⁴=I`, `(ST)³=S²`, `S²=±parity`, `T^N=I` at all three levels; **the composite-level Gauss gate**
`tr ρ₁₅(T) = g(15) = i√15` computed directly at level 15 (the CRT-twist catch — a naive `W₃⊗W₅` tensor passes
per-prime checks and fails this); **twisted-factor multiplicativity** `tr ρ₁₅(A_m) = tr ρ₃^{(2)}(A_m)·tr ρ₅^{(3)}(A_m)`
(the cofactor-twisted CRT factors, verified for m=1..4); **word well-definedness** (200 random S,T-words,
equal `SL(2,ℤ/15)`-image ⇒ equal operators); **`⟨R,L⟩ = SL(2,ℤ/15)`** (BFS order 2880).

## The cross-session layer: VERIFIED (L56 unblocked without the missing script)

- **Trace layer:** `tr ρ_N(A_m) = 1` for all `(N,m)` tested **except bronze** (`m=3`) at `N=3,15` where it is
  **3** — exactly the cross-session table.
- **The Weil-divisibility law at operator level:** `ρ_N(A_m) = 1 ⟺ A_m ≡ I (mod N)` — with B354's exact
  `RᵐLᵐ = [[1+m²,m],[m,1]]` this gives `ρ` trivial iff `N | m` componentwise; verified for
  `m ∈ {1,2,3,5,15}` at all levels, **including the "seed 15 trivializes at the seam level" prediction**.
- **The fingerprint tables (gauge-invariant form):** computed from eigen**projectors** — `M_ij = tr(P_iQ_j)` —
  never eigenvectors (raw overlap entries are gauge). Results: **(1,2): 11 distinct values** (the cross-session
  count), all real, containing the quartic **`2025T⁴−3375T³+1935T²−435T+31` — which appears in no other pair**
  (the (1,3) table carries two *different* quartic classes, shared with (1,2); the (2,3) table has **zero
  quartics** — rational + `ℚ(√5)` only). **Every recognized quadratic has squarefree discriminant 5** — the
  golden tower only. The **flattening no-go is thereby verified**: no `√3`, no `√15`, no Eisenstein-side field
  extension anywhere in the real observable class at level 15. *(Recognition tier: PSLQ at dps 30–60,
  re-verified at higher precision; numerical, honestly labeled.)*

## The new result: the phase aperture at level 15 is EMPTY (pre-registered null — FIRED)

The declared evasion of the flattening was *phases* — complex observables. The gauge-invariant phase observable
is the **triple product** `B_{ijk} = tr(P_iQ_jR_k)` over the three seeds' projector families (Bargmann-type;
raw overlap phases are gauge and were not used). Pre-registered null: all triples single-end.

**Result: all `11×11×5 = 605` triple products are exactly REAL** (numpy sweep: 0 nonreal at `1e-8`; mpmath
spot-checks at dps 40: `|Im| ≤ 1.6e-40`, the precision floor). Not merely single-end — **no phase content
exists at all.** The flattening extends from the real pair observables to the triple phases.

**Mechanism (ingredient verified, proof = follow-up):** complex conjugation implements the outer conjugation
`γ ↦ DγD⁻¹`, `D = diag(1,−1)`, on the whole image — **`conj(T) = T⁻¹` and `conj(S) = S⁻¹` exactly**. A full
reality proof for the triple class from this antiunitary (plus the symmetry of the `A_m`) is the named residual.

**Campaign consequence:** the level-15 quantum channel is now closed for *both* observable classes (real
overlaps *and* phases) by verified computation. The one remaining aperture in this lane is **level 45** (W1.4)
— where `ℚ(ζ₉)⁺` is a real cubic and the flattening argument *permits* end-mixing inside real entries.

## Honest tiers

- **Exact-to-precision:** the construction gates; the trace layer; the divisibility law; triple reality
  (605/605 real; spot floor 1e-40); the conjugation ingredient.
- **Numerical (PSLQ):** every field recognition (quartic identification, disc classification). No claim of
  proof for minimal polynomials; they match the cross-session claims and my independent B354-era spot-checks.
- **Not claimed:** any physics; any seam statement beyond "not reachable in these observable classes at these
  levels"; GOVERNANCE §6.1-C — the channel status is `open/no-breach-by-this-class`, not impossibility.

**Provenance.** Campaign: the value-boundary queue (OPEN_LEADS, 2026-07-02), W1.1. Cross-session source
(now verified): the L56 quantum layer. Mechanism precedents: B354 (the divisibility law), B314 (Galois
symmetrization). Prior art context: Weil/metaplectic representations are classical (Weil 1964; Gauss-sum
normalizations per Milgram); the *application* — pair/triple projector fingerprints of metallic monodromies —
follows the repo's B131→B354 lane. Reproducer: `weil_layer.py` (module main prints gates + tables);
test: `tests/test_b355_weil_layer_independent.py`.
