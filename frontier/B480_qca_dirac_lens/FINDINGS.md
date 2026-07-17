# B480 — the QCA/Dirac lens: NULL, and the reason is a structural type-mismatch (not a gap)

**Owner directive (2026-07-08): the object has scale, chirality, dynamics — dig into them
structurally, run the one probe never run. Done. First cell (Q1) below; verdict binned per
the prereg.**

## Reproduce-gate — PASSED
A generic rotation coin C(θ) in the split-step walk yields emergent mass = θ exactly
(D'Ariano–Perinotti universality: the Dirac equation emerges from ANY 2-state walk, mass =
coin coupling). The harness is faithful. **This already says the Dirac emergence is generic
— not something the object specially produces.**

## The object's contribution, measured
- **The object supplies a distinguished, maximally-chiral coin.** The natural doublet (the
  2-dim Weil block of W_m at level 3, the 2-dim irrep of the mod-3 image Q₈) has eigenvalues
  **±i — order 4**, a π/2 Weyl rotation, for every member m (verified m = 1,2,3). This is a
  real chirality fact: the object's canonical internal doublet is maximally chiral.
- **But the mass is NOT object-forced.** A coin with eigenvalues ±i gives mass = the
  ALIGNMENT angle α between the coin axis and the shift axis (verified: α=0 → massless
  Weyl; α=π/4 → mass π/2; α=π/2 → massless again). The object fixes the coin's spectrum,
  not the alignment — and the mass lives entirely in the alignment. So the emergent mass is
  a free embedding parameter, **not** a distinguished object invariant. → NULL/TUNABLE for
  the mass.

## The decisive dynamics test — the object's dynamics is the WRONG TYPE for a Dirac field
A free relativistic field has a smooth dispersion E(k) (picket-fence spectrum, level-ratio
⟨r⟩ → 1). The object's own dynamics does not:
- **Classically** the metallic cat map is Anosov — positive Lyapunov exponent log λ_m,
  genuinely chaotic (banked: certified hyperbolicity, escape rates B186/B451).
- **Quantum-mechanically** the level-N spectrum is arithmetically DEGENERATE, not a
  dispersion: the level-N spectrum is arithmetically DEGENERATE — an exact
  degenerate picket fence: ord(A mod 181) = 45 slots × multiplicities {4×44, 5×1};
  ord(A mod 301) = 88 × {2×3, 3×45, 4×40} (pinned by the exact trace identity
  |tr Uᵗ|² = #Fix(Aᵗ)). [CORRECTION 2026-07-17, B666 cell 6: the originally quoted
  ⟨r⟩ = 0.16 was an eigensolver-noise artifact of these exact degeneracies (exact
  conventions give ⟨r⟩ = 0 with degeneracies, 1 on distinct slots); reproducer
  frontier/B666_leads_campaign/cell6/b480_rederive.py].
Neither is a smooth free-field dispersion. **A chaotic/arithmetic map is categorically not
a free relativistic field** — this is a type-mismatch confirmed by digging, not a gap to be
filled by more computation.

## Verdict (per prereg): NULL, with one STRUCTURAL-BUT-KNOWN linkage
- **Mass:** NULL/TUNABLE — the Dirac emergence is generic (D'Ariano), the mass is an
  alignment artifact, not object-forced. No mass value voiced (HELD from birth held).
- **Chirality:** STRUCTURAL-BUT-KNOWN — the object's doublet is a maximally-chiral order-4
  coin (from Q₈). Real and distinguished, but a maximally-chiral coin aligned gives the
  generic massless Weyl mode (θ=0); it is not a new relation. Connects to the banked residue
  (B466/B289) as a chirality fact, not a fire.
- **Dynamics:** the object HAS dynamics, but it is chaotic/arithmetic, structurally the
  WRONG TYPE for the D'Ariano free-Dirac route. If forced, the "masses" are gap labels =
  class data (B447), not dynamical field content.

**No B398 escalation: the probe does not fire.** The honest upshot for the owner's
challenge: the object genuinely has scale, chirality, and dynamics — but the deepest
structural probe of whether they are the SM's confirms the type-mismatch rather than a
hidden bridge. The dynamics is chaos, not a free field; the chirality is a coin spectrum,
not a forced mass; the scale is a distinguished number, not a physical one. Digging deeper
sharpened the negative into a *reason*, which is the useful outcome.

Blocking lit-gate (for any future write-up): D'Ariano–Perinotti PRA 90 (2014); Bisio–
D'Ariano–Tosini; Kurlberg–Rudnick (arithmetic spectral degeneracy); the Fibonacci-walk
literature. Reproducer: `qca_dispersion.py` (this session's cells). Firewall: no physics
claim; nothing physics-shaped banked.
