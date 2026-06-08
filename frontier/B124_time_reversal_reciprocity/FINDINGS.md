# B124 — reciprocal `(λ,1/λ)` pairs + the time-reversal involution `λ↔1/λ` (V113)

**Two tiers, strictly separate** (the entire discipline of this probe). §1 is a **generic symplectic** fact; §2 is
the one **metallic-specific** residue. The interpretation ("two-headed time") is firewalled elsewhere
(`philosophy/P006`, the dynamics fork `speculations/S002`) and never shares a sentence with the math.

## §1 — GENERIC (symplectic): reciprocal pairs + time-reversal swaps stable/unstable

The trace map is a reversible area-preserving (symplectic) map; at a hyperbolic fixed point its Jacobian spectrum is
**reciprocal-closed** `(λ, 1/λ)`, and **time-reversal** (iterating the inverse map) acts as the involution
`λ ↔ 1/λ`, swapping the stable and unstable manifolds. Computed anchor — the SL(2) **void** fixed point `(2,2,2)`:

- Jacobian eigenvalues `{φ², −1, φ⁻²}`. The pair `φ²·φ⁻² = 1` is a reciprocal `(λ,1/λ)` pair (the symplectic
  2-plane); `−1` is self-reciprocal (the parity/sign direction); `det = φ²·(−1)·φ⁻² = −1` (orientation-reversing,
  consistent with B118/B121).
- `(DT)⁻¹` has the **same** spectrum `{φ⁻²,−1,φ²}` with stable/unstable **roles swapped**: the forward-unstable
  direction (`φ²`) is the backward-stable one. The map has **no preferred direction**.

**Scope (load-bearing).** This reciprocal/mirror structure is **generic to all area-preserving maps** — it is
symplectic geometry, *not* a feature of the metallic seed. The **only metallic-specific datum is the rate**
(`log φ²`, the expansion exponent). Same lesson as unitarity / tautological roots / the volume conjecture
(`speculations/TOMBSTONES.md`): the deep-looking structure is the ambient framework doing the work; the metallic part
supplies a number. **Banked as the generic symplectic time-reversal structure, exhibited on the void spectrum** — not
as a metallic discovery.

## §2 — METALLIC-SPECIFIC (the supplement): a det=−1 sign/chirality asymmetry — but **no arrow**

At SL(2) the two directions are symmetric (generic, §1). At SL(n≥3), `det=−1`, the tower `ρ_n = ⊕_d Sym^d(M)^{μ_d}`
carries **negative reciprocal-pair modes** (the `char(−M^h)` sign sectors); at `det=+1` it carries **none** (computed,
n=2..10: the det=+1 spectrum has zero `−1` modes at every n). So there is a genuine `det=−1`-specific
positive-vs-negative **sign/chirality imbalance**, `O(n/2)` — **more than generic symplectic** (Chat-1's catch
stands), tied to the **inversion identity `char(M⁻¹)=char(−M)`** (B118) and cross-referenced to **B118/B121
amphichirality** (this asymmetry *is* the amphichirality / orientation-reversal surfacing in the mode counts).

**Correction A — it is a parity/chirality (P-like) asymmetry, NOT a time-direction (T-like) arrow.** Decisive
recompute: **expanding count == contracting count, EXACTLY, every n, both det signs** (reciprocal pairing forces it;
survives to SL(n)). The two time directions have **identically many** modes — there is **no arrow**. `−w₀` =
contragredient = character-level time-reversal, and its `±1` eigenspaces are time-reversal **even** vs **odd**; an
excess of one is **symmetric between the two directions**, not a forward-vs-backward preference. **The metallic
structure breaks chirality (P-like, = amphichirality B118/B121) and preserves time-direction symmetry (T-like) in the
mode count.**

**Correction B — the exact constant is OPEN; do NOT bank `⌊n/2⌋`.** Verified the imbalance is real but the *exact*
constant is **bookkeeping-dependent**: distinct natural decompositions give distinct sequences —
- the raw `±1`-eigenvalue excess `N(+1)−N(−1)` **oscillates period-4** `[−1,0,1,0,−1,0,1,0,−1]` (n=2..10) — **not**
  monotone `⌊n/2⌋ = [1,1,2,2,3,3,4,4,5]`;
- the pos-minus-neg **sector** excess (here) is `[0,1,3,4,4,5,7,8,8]`;
- the handoff's sector-multiplicity count `[1,1,2,4,5,5,6,8,9]` matches `⌊n/2⌋` **only through n=4**.

None is a clean monotone `⌊n/2⌋` past n=4 (the n≥5 regime is inflated by the B117 two-sequence middle-band doubling).
So: **bank the qualitative det=−1 sign/chirality imbalance (`O(n/2)`, B112-backed); the exact constant is open.**

## What this is and is not

- **Is:** a generic symplectic time-reversal structure (§1) + one real metallic-specific residue — a det=−1 *handedness*
  (P) asymmetry (§2), exact constant open.
- **Is not:** an arrow of time (the spectrum is exactly forward/backward symmetric at every rank); a metallic feature
  of the reciprocal structure itself (that is symplectic geometry); anything physical (the map's "time" is
  iteration-count of a monodromy on moduli space — firewalled).

Nothing here lowers the wall: the functorial `Sym(W)→trace-ring` construction is untouched.

**Anchors:** the void Jacobian `{φ²,−1,φ⁻²}` (B122 `sym_tower_is_void_specific`); `ρ_n = ⊕Sym^d(M)^{μ_d}` (B103);
the inversion identity `char(M⁻¹)=char(−M)` and the det=−1 parity (B118/B121); the two-sequence middle-band doubling
(B117). Interpretation: `philosophy/P006`, `speculations/S002`. Ledger **V113**.
