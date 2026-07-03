# B371 — the minimal two-state sector: exact, two-path verified, seam-coupled at the rigid value

**Status: banked (frontier) + promoted at banking (P56, P57 — the steady-state §5.1 rule: exact,
test-locked, two independent computation paths). FIREWALLED: the originating question was "can we
compute a photon?" and the answer is NO — no gauge field, spacetime, mass, or coupling exists in
this mathematics (K020). What is banked is a *photon-shaped slot* only in the strict sense below.**

## The sector (all exact; this repo's engine + an independently relayed exact computation agree)

The level-15 quantization contains a distinguished 2-dimensional subspace — the sum of the
`a = 6` and `a = 14` eigenspaces of `W₁` — with, exactly:

1. **Invariance** under the full Weil image (both generators; zero residual).
2. **Irreducibility** by mechanism: the dihedral relation `Ŝ W₁ Ŝ⁻¹ = W₁⁻¹` holds **globally**
   (`Ŝ = D⁻¹·WR·D⁻¹`, the palindrome lift of `S = R⁻¹LR⁻¹`), and it swaps the two eigenlines.
3. **Helicity pairing**: `tr ρ_slot(Ŝ) = 0` with `(PŜP)² = ζ₆₀¹⁸·P` — eigenvalues exactly
   `±ζ₆₀⁹`: opposite unit quarter-turn weights modulo a common center phase, exchanged by `Ŝ`.
4. **The metallic shadows**: `tr ρ_slot(A₁) = tr ρ_slot(A₄) = (1−√5)/2 = 1−φ` exactly — the
   golden monodromy turns the sector by the regular pentagon's angle (order 10); seeds 2, 3 give
   trace exactly 1 (order 6). Seeds 1 and 4 are indistinguishable here — the finer-than-spectrum
   theme again.
5. **The true parity** (the relayed probe's honest correction of its own P1): naive parities do
   not commute with this half-characteristic model; the true parity is `J = Ŝ²` — monomial with
   support `j → 1−j`, commuting exactly with both generators.
6. **The Weyl identity**: `J · Par = ζ₆⁻¹ · X · Z` exactly (X = one-step translation, Z = clock).
   Corollary: the banked Par-inserted pair observable inserts, up to the parity sign and a fixed
   sixth root, the **elementary Weyl operator XZ** — the seam is a parity-signed one-step hopping
   amplitude between spectral projectors.
7. **The seam connection** (against the banked exact (1,2) table): the sector's cells are exactly
   `{6,14} × {2,10}`, all at `±1/48` — **the seam couples the sector to itself at the rigid
   value**; and the rigid rows `{0,4,6,14}` + silent row `{16}` are exactly the trivial-at-3
   parity tower, the six rich rows exactly the odd-at-3 tower (the value stratification IS the
   prime-3 parity split, at support level).

## Provenance and the two paths

Pre-registered cross-session before computation (P1–P5 with kill conditions); computed exactly
there; **independently re-verified here from scratch in the banked engine** (`slot_verification.py`
— every check an exact Fraction identity). The relayed errors ledger is part of the record: the
naive-parity failure, and two wrong Burnside certificates before the structural irreducibility
proof — caught by their own standing rules.

## Open (registered): the row-16 silence

Row 16 (the third trivial-at-3 line) is exactly silent in the (1,2) table, and no forcing law
survives: three candidate involutions are each killed by the exact data. The localized statement —
the block-diagonal part of XZ on the 3-dim block annihilates the cluster-16 line while coupling
0 and 4 — and whether ±1/48 is derivable as the unique symmetry-allowed sector↔sector XZ matrix
element (a selection-rule theorem) are registered in `OPEN_LEADS` (fresh pre-registration required
before any attempt).

**Provenance.** B358/B367 (engine, tables), B366 (the lift this sector lives in), the relayed
exploration set (verified item-by-item). Reproducer: `slot_verification.py` (~2 min); locks:
`tests/test_b371_two_state_sector.py`.
