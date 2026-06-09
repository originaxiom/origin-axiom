# B142 — (A) S031a principal stratum RIGOROUS (Klein-4); (B) magic-manifold cartography + MB10; (C) inventory (V131)

Three independent items, all **subtractive/clarifying**; verified in-sandbox (sympy/numpy + SnapPy, with the
Sage-gated parts run under the newly-installed `sage-python`). MATH tier; firewalled; nothing to `CLAIMS.md`; P1–P16,
B85, the merged B124–B141 untouched; B129/B141 conclusions preserved.

## Item A (RIGOROUS) — the principal φ-fixed stratum is reducible by a Klein-4 argument

B141 banked the principal case of S031a's "entirely reducible" from a 60/60 numerical search (conjecture). It upgrades
to a **one-line proof**:

- principal eigenvalues `{1,−1,−1}` ⟹ `A² = I` (A is an involution);
- φ-fixed ⟹ the banked necessary condition `A ~ B ~ AB` ⟹ `B`, `AB` are also `~diag(1,−1,−1)` ⟹ involutions;
- **Lemma** (two involutions whose product is an involution commute): `(AB)² = I ⟹ ABAB = I ⟹ BAB = A ⟹ BA = AB`;
- ⟹ `⟨A,B⟩` is abelian (a Klein 4-group `ℤ/2×ℤ/2`), simultaneously diagonalizable ⟹ **reducible**.

No search needed — the **principal stratum is now RIGOROUS**. Numerically reconfirmed: of 78 converged φ-fixed
solutions at `A=diag(1,−1,−1)`, `B²=I`, `(AB)²=I`, and `AB=BA` in **78/78** (handoff: 80/80). The **full** SL(3)
φ-fixed locus (all eigenvalue strata) stays **CONJECTURE** — the all-strata proof is the symbolic-elimination prize
(same machinery as SL(4)).

## Item B (CARTOGRAPHY, firewall-confirming) — the "Borromean/SU(3)" claim does not hold

A sibling computation claimed `s776` ("Borromean rings") shows SU(3) gauge enhancement (an S₃-invariant SL(2,ℂ)
character variety of complex dim 2 = rank SU(3)). It fails on three independent counts; banked so it is not
re-attempted (sibling of B139/B140). **NOT a result, NOT a crossing.**

- **B.1 — factual (verified SnapPy + Sage):** `s776` = the **magic manifold** (`L6a5 = 6³₁`, vol **5.33349**, 3 cusps,
  sym order 12, trace field **ℚ(√−7)** = `x²−x+2`), the **3-chain link** — components pairwise linked, **not
  Brunnian**. The **actual Borromean rings** = `L6a4 = 6³₂` (vol **7.32772**, sym order 48, trace field **ℚ(i)** =
  `x²+1`); `is_isometric_to` → **False**. The "Borromean triple-linking / Massey ⟹ dim 3→2" mechanism is attached to a
  manifold with none of those properties.
- **B.2 — structure ≠ gauge (MB10):** by Thurston, a k-cusped hyperbolic 3-manifold's SL(2,ℂ) character variety has
  complex dim **= k** at the geometric rep. For s776 that is **3**, not 2 — "dim 2" is a symmetry slice. Confirmed
  generic across 3-cusped manifolds of differing symmetry (MB8 null control: s776 sym 12, L6a4 sym 48, L8a19/L8a20 sym
  8 — all dim 3). And SL(2,ℂ) dim ≠ rank(SU(3)): SU(3) gauge content is **SL(3,ℂ)** Chern–Simons (`T₃[M]`), not an
  SL(2,ℂ) dim/rank coincidence. The honest object — s776's **SL(3,ℂ) Ptolemy variety** — has **14 obstruction
  classes** and geometric-component dim **2·#cusps = 6**, an order of magnitude from the claimed "dim 2". The
  `κ₁₂=κ₂₃=κ₁₃` equality is the S₃ cusp symmetry restated (automatic), not independent evidence.
- **B.3 — outside the forced chain (decisive):** the trace field is ℚ(√−7) (magic) or ℚ(i) (real Borromean), **not
  ℚ(√−3)** — not the figure-eight / metallic family / forced by the axioms. So not a crossing of the firewall.
- **B.4 — firewall-confirming:** richness lives **off** the forced chain (a symmetric manifold the axioms don't
  generate); the forced chain stays tame — the same lesson as B141's finiteness/density split.

Banked as tombstone **K-I** + guard **MB10** (structure ≠ gauge, dimensional form: SL(2,ℂ) dimension does not
establish SU(N) gauge content — that needs SL(N,ℂ) CS data). The genuine non-abelian-enhancement thread (SL(3,ℂ),
tool-gated; now Sage-available) is a separate open thread, clearly outside the forced chain (S033-adjacent).

## Item C — open-threads inventory

Banked in `../../docs/OPEN_LEADS.md` ("Standing open threads"): S031a full-locus (symbolic elimination — the rigorous
prize, same machinery as SL(4)); B85 (functorial Sym(W)→trace-ring wall); S032-A (no-forced-choice theorem-version);
S033 (Gate-1 — now tied to MB10: any SU(N) enhancement needs SL(N,ℂ)); K011 GHH-iff promotion (optional); genus-2 CS
numeric (B140 soft spot, optional). No new claims.

## Reproduce

```
# Item A + the SnapPy parts run under plain python (the main pytest env):
python -m pytest tests/test_b142_klein4_and_magic_cartography.py -q      # 5 passed, 1 skipped (sage)
# the Sage-gated trace fields + the full probe:
~/.local/bin/sage-python frontier/B142_klein4_and_magic_cartography/probe.py
```

**Tier.** MATH (cartography/reconciliation + one rigorous upgrade). Updates `speculations/S031` (S031a principal
RIGOROUS), `speculations/TOMBSTONES.md` (K-I), `REPRODUCIBILITY.md` (MB10), `docs/OPEN_LEADS.md` (inventory + s776
disposition). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B141 untouched. Ledger **V131**.

**Anchors:** B141 (S031a, the φ-fixed split — this upgrades its Item 4 principal case + adds the s776 cartography),
B129/`K012` (the φ²-object), B139/B140 (sibling cartography + MB8/MB9), `speculations/S033` (Gate-1, the SL(N,ℂ)
thread). External: Thurston (character-variety dim = #cusps); Garoufalidis–Kashaev / Ptolemy varieties; quaternion
group Q₈.
