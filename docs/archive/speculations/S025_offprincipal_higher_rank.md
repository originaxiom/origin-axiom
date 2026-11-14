# S025 — independent spectral content off the principal locus, at higher rank (the S011 continuation)

**Status: `DORMANT`.** Firewalled; not a claim. Phase 3 of the physics-bridge sweep (a HEAVY/deferred fork,
mapped + obstruction stated). The successor to `S011` (the off-locus sector). Nothing promotes to `../CLAIMS.md`;
the physics chapter stays CLOSED.

**[MATH] (the situation, cited).** B107 isolated the one open physics fork as the **off-principal multichannel /
irreducible** sector: the tower, torsion, and degree=rank all live on or near the principal component
(`tr A = tr A⁻¹ = 1` → principal `Sym^{n−1}` → SL(2)-determined → the single golden scale). Genuinely irreducible
SL(n) reps **off** that locus would be the only place independent spectral content could live. **B110** then proved
this sector **EMPTY for 4₁ at SL(3)** (all three irreducible components of the HMP character variety sit on the
forced locus `tr A = tr A⁻¹`); **B115** found the known **SL(4)** Dehn-filling reps are forced-locus too. So the
fork is narrowed to: **higher rank (SL(4)/SL(5)) off-locus components, or a different manifold.**

**[LEAP] (kept separate).** If an irreducible off-locus SL(n) rep exists, its trace-map linearization need not be
SL(2)-determined — it could carry a second scale (not `±φᵏ`), the first genuinely-new spectral content. This is the
only surviving route to "the tower touches a multichannel system."

**[HOOK] (the concrete computation + its obstruction).** Decide whether off-locus irreducible SL(4)/SL(5) reps of
the figure-eight group exist, and if so compute their trace-map Jacobian (reuse `B106.sl4_dehn_jacobian`) to test
for a non-`φ` neutral eigenvalue. **Obstruction (why it is DORMANT):** there is **no SL(4) figure-eight
character-variety classification** (the SL(3) one is Heusener–Muñoz–Porti 1505.04451; no SL(4) analogue, B115), so
the off-locus components are genuinely uncomputed — finding them is a research-level char-variety problem, not a
bounded probe. And even if found, the **multichannel realization is non-Hermitian** (`SL(n)=Sp` only at n=2,
`sln_multichannel_probe`), so any spectral reading needs a non-self-adjoint / PT-symmetric framework.

**Negative beside the leap.** EMPTY at the only place it has been checked exhaustively (4₁/SL(3), B110). The fork is
**not dead** (untested at higher rank / other manifolds) but it is **strongly narrowed** and gated on machinery the
repo does not have. Honest status: a real open boundary, not a queued calculation.

Related: `S011` (the parent), `S007` (the gap-labeling it would feed), B107 (the open-fork statement), B110/B115
(the EMPTY/forced-locus results), `sln_multichannel_probe` (the Hermitian obstruction), `PHYSICS_BRIDGE_MAP.md`.
