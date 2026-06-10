# B150 — class-S coincidence (L14): characterize the object, tag FORCED / PERMITTED / RHYME

**Question.** Does the SL(2,ℤ) trace-map / mapping-class action on the once-punctured-torus character variety (B148's
object) coincide with the S-duality / mapping-class action on the Coulomb branch of the class-S theory of the once-
punctured torus? A **scoping/characterization** pass (focused literature read) — **not** a verdict-of-match, no sandbox
"match" fabricated.

**The binding distinction (two spaces).** SL(2,ℤ) on the **UV coupling τ** = well-known modularity = HOMONYM → **RHYME**.
FORCED requires the action **on the character variety** to reproduce the B148 anchors (hyperbolic classes, λ_m²,
ℚ(√(m²+4)) fixed slopes, the κ cubic, κ=−2 Markov).

**Answer — MIXED.**
- **FORCED at the character-variety / MCG level.** The SL(2,ℤ) trace-map action on the Fricke character variety **is** the
  N=2\* S-duality mapping-class action — same cubic, same MCG, same Dehn-twist generators, same action; λ_m² = the
  Cantat–Loray dynamical degree; κ=−2 = the Markov fiber. Literature-confirmed: **Allegretti–Shan (2411.17378)** —
  S-duality acts "on the character variety itself through MCG, not merely on τ", Coulomb branches MCG-permuted;
  **Cantat–Loray (AIF 2009 / 0711.1579)** — dynamical degree = homology spectral radius; **GMN (0907.3987)** — Coulomb =
  Hitchin moduli.
- **RHYME at the τ-modularity level** (homonym) **and at the physical-magnitude / gauge level** (gauge group free input,
  no scale fixed, N=2\* non-chiral — the firewall, L15's separate question).
- **Even the FORCED part is mathematics** (symmetry = a known duality action); it does **not** cross to physical
  magnitude. L15 untouched.

**Files.** `probe.py` (re-asserts the B148 anchor data + the tagged comparison + verdict), `FINDINGS.md`,
`../../tests/test_b150_class_s_coincidence.py` (5 passed: anchor data + comparison-table honesty structure).

**Run.** `python -m pytest tests/test_b150_class_s_coincidence.py -q` (pyenv).

Ledger **V139**. Anchors: B148, B149, K006, LADDER_LITERATURE (N=2\*), S024. External: 2411.17378, 0711.1579/0711.1727
(AIF 2009), 0907.3987, 0904.2715, 1103.5748.
