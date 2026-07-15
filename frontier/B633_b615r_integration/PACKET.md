# B615-R PACKET — the uncertainty-aware re-analysis (cc2 → cc)

**Verdict: OUTCOME A — the AMBIGUOUS dissolves under every correction, separately and
combined. Branch 3's SM-silent closure is HARDENED: it now rests on scheme-stated,
scale-stated, uncertainty-correct inputs.** Sealed design `DESIGN.md` + runner hashed
pre-run (`SEAL.txt`); outputs banked verbatim (`outputs/RUN_OUTPUT.txt`).

## The decomposition (Šidák-corrected best-grid p; B615 recorded: 0.0775)

| variant | correction applied | p (tier 1e-2) | p (tier 1e-3) |
|---|---|---|---|
| a | old centrals + 2σ windows | 0.6249 | 0.4313 |
| b | NuFIT-6.1/PDG-2026 centrals, point windows | 0.3458 | 0.1929 |
| **c (headline)** | **both** | **0.1450** | **0.1904** |
| c2 | c with the other-octant θ₂₃ (0.550) | 0.3152 | 0.3931 |
| c3 | c with scheme-consistent G3 (correction iii) | 0.1450 | 0.1904 |

Mechanisms, visible in the pair tables:
- **The width correction alone dissolves the original signal** (variant a) — B615's own
  disclosure predicted this direction; now it is a computation.
- **NuFIT 6.1's octant flip** (sin²θ₂₃: 0.546 → 0.470 NO best fit) kills the
  (4/7)sin²(4π/7) match outright; it reappears only in the c2 sensitivity, where the
  overall p is weaker still (0.32).
- **The golden coincidence, priced honestly:** 1/(2φ) = 0.30902 sits 2.2×10⁻⁴ from the new
  sin²θ₁₂ central (0.3088 ± 0.0067) — 0.03σ. But the experiment's ±1σ window also contains
  4/13, 8/25, 3/10, and 225/692 from the same inventory; the matched null prices exactly
  that crowding (G2 observed 7, expected 3.2). A point-match 30× tighter than the
  measurement's resolution carries no additional evidence — this is the statistical content
  of the whole re-analysis in one line.
- **G3 (mass ratios): zero matches in every scheme column** (recorded / pole-pole /
  MS-bar-common-μ), and the scheme spread itself (m_t/m_b: 36–61) is banked as the
  demonstration that the recorded G3 targets were not well-defined (correction iii).

## Proposed register updates (for cc; nothing applied by this seat)

1. **The Branch-3 residual (corrected p = 0.078) → DISSOLVED-BY-REANALYSIS** (this packet):
   the stopping rule's one suggestive item is chance-compatible under uncertainty-correct
   treatment at every variant. The SM-values closure stands with no residual asterisk.
2. **New register row (forward-looking, zero-cost): the golden-θ₁₂ question becomes
   experimentally decidable.** JUNO-class precision (σ(sin²θ₁₂) → ~0.5%, an order tighter)
   will separate 1/(2φ) = 0.30902 from 4/13 = 0.30769 from today's central 0.3088. No
   action for any seat — nature will adjudicate the one surviving coincidence. (Context:
   golden-ratio PMNS ansätze are a populated external literature; the A₅ bridge readings
   were already refuted in-repo, B619.)
3. **The Input-Completeness Ledger** (`INPUT_LEDGER.md`, this packet) adopted as a
   mandatory checklist for any future SM-facing cell; the B615 inputs audited against it
   in-file (three items failed: scheme statement, scale statement, uncertainties —
   documented, not blamed; the verdicts survive the audit).

## Method note

Same 217-pair inventory and machinery as the recorded B615 (object side copied verbatim;
Poisson-binomial exact tails; Šidák over the four grids; G4's convention row carried but
flagged). No new object quantities — this is the disclosure's own flagged re-analysis, so
the sealed B614 "new tests need held-out quantities" clause is untouched. Inputs sourced:
NuFIT 6.1 (Nov-2025 data), PDG RPP-2026 (2026-06-01); PDG CL=90% quark-mass errors
converted (/1.645); asymmetric σ taken conservatively (max).
