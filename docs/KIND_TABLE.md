# THE KIND TABLE + THE RG TAXONOMY — the two admissibility ledgers every crossing consults (B1020)

**Banked 2026-08-10 (B1020). Living document (`doc-currency`).** Both ledgers answer the same
question — *what may a crossing compare?* — BEFORE any value is looked at. R5 (kinds) and R2
(running) consult these tables; a prereg proposing a pair absent from the admissible list does
not seal. Every object-side row cites its banked arc; every SM-side/RG row is a classical input,
cited not derived.

---

## PART 1 — THE KIND TABLE

**The rule it operationalizes (R5):** a crossing's (object quantity, SM target) pair must be
kind-admissible BEFORE sealing. The worked kill: B856/JUNO — the proposed reading was refuted on
kind, and even the kind-corrected pairing (|h|² vs sin²θ₁₂, both probability-kind) was then
excluded numerically at −2.3σ. Kind admissibility is necessary, never sufficient.

### The object side — the two channels' value kinds (all banked)

| object quantity | kind | bounds | field | channel |
|---|---|---|---|---|
| tones Re(ζ⁻¹ūMu) ∈ {0,±1/(2φ),±1/2,±φ/2,±1} | **amplitude-part** (real part of a unitary matrix element) | [−1, 1] | ℚ(√5) | coupling |
| \|h\|² ∈ {1/(φ√5), φ/√5, 1} | **probability** | [0, 1] | ℚ(√5) | coupling |
| mirror set (incl. ±¼, ±φ/4, ±1/(4φ)) | **amplitude-part** | [−1, 1] | ℚ(√5) | coupling |
| arg(h) (the χ phases: 0, ±2π/3) | **phase** | (−π, π] | ℚ(ω) | coupling |
| det-ratios {±17/384, ±1} | **determinant ratio** (frame-relative!) | ℚ | ℚ | pair |
| K-norm −(953/2304)² | **norm ratio** (frame-relative) | ℚ | ℚ | pair |
| hierarchy carriers (D₂ data, v_g² = roots(HIER)) | **eigenvalue ratio** | ℝ₊ | cubic K | pair |
| CS = 0, θ-structure | **topological phase** (no running) | quantized | — | object-level |

### The SM side — dimensionless target classes by kind

| SM target class | kind | notes |
|---|---|---|
| sin²θ_ij (mixing) | **probability** | admissible partner: \|h\|²-type ONLY |
| CKM/PMNS moduli \|V_ij\| | **amplitude modulus** [0,1] | admissible: \|tone\|-type |
| CP phases δ | **phase** | admissible: arg(h)-type |
| mass RATIOS m_i/m_j | **eigenvalue ratio** ℝ₊ | admissible: hierarchy-carrier-type (PAIR channel — frame question then bites: B936!) |
| gauge-coupling ratios | **coupling ratio** | runs hard (see Part 2) |
| θ_QCD | **topological phase** | admissible: CS-type — BUT the functor gate (B1009) fronts it |
| generation count, ℤ₆ | **integer/structure** | already Tier-1 territory, not crossing targets |

### The admissible-pairs corollary (the table's output)
- **coupling channel → mixing/moduli/phases** (kind-admissible; anchor-free; the ONLY fully open
  admissible lane after B856's one exclusion)
- **pair channel → mass ratios** (kind-admissible BUT frame-relative — B936; a crossing here must
  first exhibit a frame-invariant residue, which B1016 says is NOT the coupling's Re h — none is
  currently banked ⟹ this lane is CLOSED until one is)
- **object-level θ → θ_QCD** (kind-admissible; FUNCTOR-GATED — B1009; stays a HOOK)
- everything else: kind-inadmissible; a prereg proposing it does not seal.

## PART 2 — THE RG TAXONOMY (R2)

Ranked by running-sensitivity of the SM target (classical inputs, cited not derived):

| target | running | crossing viability under R2 |
|---|---|---|
| θ_QCD | none (topological) | best-in-class on R2; functor-gated on R5 |
| CKM/PMNS angles & phases | negligible below GUT scale (Yukawa-suppressed) | **best open lane** — matches the coupling channel's admissible kinds |
| mass ratios (same type) | slow (log; QCD ratios stable) | viable on R2; blocked on frame (Part 1) |
| mass ratios (cross-type, e.g. m_t/m_b) | tan β / Yukawa-sensitive | weak |
| sin²θ_W | STRONG (the B915 killer) | requires the derived ladder — high bar |
| gauge ratios α_i/α_j | STRONG | same |

## THE CONVERGENCE (the deliverable's one sentence)

**Both ledgers point at the same lane: the coupling channel's amplitude/probability/phase values
against mixing-sector targets — kind-admissible, anchor-free, RG-quiet.** That is the fourth
crossing's candidate class, now derived twice over (R5 × R2), with B856's single exclusion
(θ₁₂-vs-|h|² at −2.3σ) already on its look-elsewhere ledger.

## Cells for the sealed arc
- K1: the object-side kind assignments verified against the banked sources (each row cites its arc).
- K2: the SM-side classes with their kinds (classical, cited).
- K3: the admissible-pairs corollary derived, the closed lanes stated with their closers.
- K4: the RG ranking (classical inputs cited; no new RG computation).
- K5: register the corollary in CROSSING_REQUIREMENTS (R5/R2 now have their tables) + the
  mixing-lane look-elsewhere ledger opened with B856's exclusion as row 1.

## THE CONSUMPTION LEDGER (added 2026-08-18 at L166's registration — the A4 adjudication; `doc-currency`)

The one-shot rule consumes CONTACT ROWS, not vocabulary: a row is spent when a sealed
comparison DRAWS on it. Booking, coupling channel (arc-cited):

| coupling row | status | consumed by |
|---|---|---|
| tones (the five-tone set) | **CONSUMED** | B1066 R-B (the φ-geometric triple; MISS, decisive) |
| probability (\|h\|²) | **CONSUMED** | B1066 R-A (the listener pair; MISS, decisive) |
| phases (arg h ∈ {0, ±2π/3}) | **CONSUMED** | B1027 + B1063 (the pre-committed refresh; MISS both sectors) |
| **mirror set (θ-even)** | **UNCONSUMED — the last licensed row** | never drawn on by any sealed comparison (B1011 C6 delivered the set; no arc took it to data) |

Reading note: B1066's "the kind table's current rows were both consumed here" counts the
TWO rows its own relations drew from (tones, probability) — the plain reading, since the
channel has four rows and the phases row was consumed by earlier arcs. The pair-channel
rows carry their own frame-relative fences (R10) and are not booked here.

**The binding consequence for the crossing (L166 / `docs/LISTENER_MAP_SPEC.md`):** any
future contact through the mirror row is a NEW ARC under a NEW SEAL against then-current
data (the one-shot rule, B1063's precedent), and — per the main-goal architecture — only
AFTER a constructed Λ pins u from field data (AC2's redaction test; never a fit). The
mirror row is where AC4′'s discriminating territory sits (the Track-A A3 landscape): the
crossing's designed shape is Λ → u → the mirror-sector prediction → this row's one shot,
with zero anchors consumed (R11's open lane).
