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
| **mirror set (θ-even)** | **UNCONSUMED — the last licensed row. B1349 (2026-09-13) RECOMMENDS NOT SPENDING IT:** the sector is now posed — projective image `A₄ × A₅` (720), `ℂ⁴_even` irreducible, maximal `|Stab| = 15 = 3×5` on a **rank-1 product state**, so the **residual freedom is 48**. R11's arithmetic fails on either branch — one output against a 48-fold selection (`log₂48 ≈ 5.58` bits), or against a 48-element target set — so the cell is **vacuous by MB12 before the seal**. **UPDATED same day (B1349 addendum): THE GALOIS CUT IS DONE — `48 → 8`.** Rational (hence Galois-fixed) directions number **8** of the 96 maximal-stabiliser ones, so the anchor cost falls from `log₂48 ≈ 5.58` bits to **`log₂8 = 3` bits** and `outputs − anchors` improves from −4.6 to **−2**. Still short, so the row still should not be spent — but the remaining question is now exactly one thing: **count how many independent numbers the θ-even mirror set carries. Four suffices to close R11.** **UPDATED again same day (B1349 addendum 2): THE OUTPUTS ARE COUNTED, AND THE ROW SPLITS IN TWO ALONG `gcd(m,15)`.** On the θ-even sector `Re h` is **ear-independent exactly when `gcd(m,15) > 1`** and ear-dependent exactly on the 8 **units** of ℤ/15 (`φ(15) = 8`) — verified exhaustively and exactly over the complete period (`ord(R) = ord(L) = 15`, zero violations). **Branch A (`gcd(m,15) > 1`, 7 words): no direction is selected, so the 3-bit anchor is NOT consumed, and the readout is one of 4 forced values `{−1/(2φ), 0, 1/2, 1}` — `outputs − anchors` is `+4`, or `+1` on the most conservative count, and R11 CLOSES on three of its four readings.** **Branch B (`gcd(m,15) = 1`, 8 words): only 2 ear-discriminating directions (`dim_ℝ span{Q_m} = 3` with `G` in the span) against 3 bits = `−1` — DOES NOT CLOSE.** So: **if this row is ever spent, spend it on a word with `gcd(m,15) > 1`** — the arc's first positive instruction. **BUT THE ROW IS STILL NOT RECOMMENDED FOR SPENDING, AND THE REASON HAS MOVED:** R11 is an *input-accounting* gate, not a physics gate, and branch A's cheapest output is `−1/(2φ)`, whose modulus is precisely the `1/(2φ)` that **B856 already took to a bench and could not discriminate** (its `|h|²` reading REFUTED ON KIND; the surviving `Re h` in a 1σ window holding ≥17 natural candidates). **What now gates this row is kind-correctness, not arithmetic** — and on B856's own precedent that is the harder gate. Structural note: every ear-**dependent** eigenvalue is `(1/(2√2)) ×` a unit of `ℤ[φ]` and **`√2 ∉ ℚ(ζ₆₀)`** (proved: `Φ₆₀` irreducible over `ℚ(√2)`; conductor 8 ∤ 60), while all four ear-**independent** values lie in `ℚ(√5) ⊂ ℚ(ζ₆₀)` — **selecting an ear costs a field extension the modular data does not contain.** **UPDATED again (B1349 addendum 3): THE 4/4 SPLIT IS ESTABLISHED AND BRANCH B TIES AT ZERO.** Addendum 1 left the split of the 8 rational directions between the two orbits of 48 *indicated, not established*; computed exactly in `ℚ(ζ₆₀)` (projective canonicalisation by exact field inversion; `|orbit|` divides 720 asserted for all eight) it is **[4, 4]** — orbit 1 holds `e₁, e₂, (1,0,0,1), (0,1,1,0)`, orbit 2 holds `e₃, e₄, (1,0,0,−1/2), (0,1,−1/2,0)`, both of size 48 with `|Stab| = 15`. **Confined to one orbit — as it is whenever the orbit is generated rather than chosen — the anchor is `log₂4 = 2 bits`, not 3, so branch B reads `2 − 2 = 0` and FAILS BY A TIE** (R11 requires strictly `> 0`). Sharper than addendum 2's `−1`: one more ear-discriminating direction would close it, **and there is provably no third** — `dim_ℝ span{Q_m : m` a unit`} = 2` exactly. Branch B does not fail for want of effort; it fails by one dimension the sector does not contain. Branch A now closes on **four of six** readings. **UPDATED again (B1349 addendum 4): THE KIND GATE'S FIRST STEP, AND BRANCH B IS EXCLUDED ON KIND TOO.** The first kind question needs no data: does the reading land in **this row's own banked value set**? B1011 C6 banks 15 θ-even values `{0, ±1/4, ±1/(4φ), ±1/2, ±1/(2φ), ±φ/4, ±φ/2, ±1}`. **Branch A's four forced values `−1/(2φ), 0, 1/2, 1` are ALL FOUR ELEMENTS of it. NONE of branch B's four ear-dependent extremes is** — `φ²/(2√2)` ≈ 0.9256, `1/(φ·2√2)` ≈ 0.2185, `√5/(2√2)` ≈ 0.7906, `1/(2√2)` ≈ 0.3536, the nearest banked values off by 0.018–0.074. **And it is the field, not an accident:** every branch-B reading carries `1/√2` and generates `ℚ(√2,√5)`, while this row's declared field is `ℚ(√5)` and `√2 ∉ ℚ(ζ₆₀)` — so a branch-B reading *cannot* be a member, as field arithmetic rather than as an approximation. **TWO INDEPENDENT GATES NOW REJECT BRANCH B** (the `2 − 2 = 0` tie, and kind), neither depending on the other. **Branch A earns KIND-ELIGIBLE — right field, right bounds, an actual element of the banked set — which is NOT kind-correct:** whether the mirror row is the right observable is the question B856 lost on its own sector, and nothing here touches it. Note also that this is a **third independent signature of the `gcd(m,15)` split**, and the only one checkable against a law banked *before* the question was asked: the corpus's own C6 agrees exactly on branch A and disagrees exactly on branch B. **CORRECTED SAME DAY (B1349 addendum 5) — THE “FOUR OF SIX” COUNT IS WITHDRAWN, AND THE OBJECT'S OWN WORD IS ON THE DEAD BRANCH.** The metallic words carry `SL(2,ℤ)` trace `m²+2`, so **`m = 1` is the GOLDEN** — and **B997** proves the golden is the *unique* metallic grammar whose own-conductor shadow is a McKay group. But `gcd(1,15) = 1`, so the golden word is a **unit**: ear-dependent, and therefore on **branch B, dead on both gates**. Silver (`m = 2`) too; the first live word is bronze. **So this row's arithmetic closes only on words the object does not single out** — and the one branch-A value outside ℚ, `−1/(2φ)`, occurs only at `m ∈ {6,9}`. Addenda 2–4 priced the **ear** and silently treated the **word** as given, which it cannot be; naming a non-unit costs `log₂7 ≈ 2.81` bits, and with that term restored **branch A closes on ONE reading of four, not four of six** (`4 − 2.81 = +1.19` only; every other reading negative). The mathematics stands — the `gcd` law, the exact spectra, the field statement, the C6 containment, the 4/4 split; the **accounting** was short an anchor (`ERROR_LEDGER` **E76**). **CLOSED (B1405 + B1407, 2026-09-14) — THE ROW IS DEAD, AND ON POWER RATHER THAN ACCOUNTING.** B1405: the word anchor is not mis-SIZED but mis-TYPED — `ord(R) = ord(L) = 15` makes the readout a function of `m mod 15` while the manifold is not (`weld(1) = weld(16)` exactly, against `vol = 2.0299` and `7.1769`), so naming a residue and naming a manifold are different acts; **five** independent principles (minimal volume, minimal systole, Jørgensen extremality, B997's McKay uniqueness, the existence of a conductor) all output `m = 1`, a **unit**, hence branch B. B1407: **this row's own spec settles the remaining fork** — *"this row's one shot, with **zero anchors consumed**"* (above) and `CAMPAIGN_STATUS` twice — so **branch A, whose anchor is non-zero by construction, is UNLICENSED**, and branch B is dead on the two gates already recorded. **And the observable that DOES meet the spec exists:** B1406's normalised graded trace `tr(C·RᵐLᵐ)/tr(C)` has **zero anchors** (a trace has no ear; `m = 1` is free), range `[−1,1]`, field `ℚ(√5)`, and **all six of its values are members of C6's banked 15** — yet at the object's own word it reads **`1/(2φ)`, exactly the value recorded above as the one B856 already took to a bench and could not discriminate**. **So the anchor problem was always solvable and was never the binding constraint: this row could not have worked at any anchor price.** L209 CLOSED. **The recommendation is unchanged and better founded: DO NOT SPEND THIS ROW** — not because the arithmetic is short by a hair, but because the only branch on which it is not short asks the programme to read its coupling off a grammar that is not the object's. | never drawn on by any sealed comparison (B1011 C6 delivered the set; no arc took it to data) | *(stamp 2026-08-19: still CURRENT as of B1082 — the stale-absence sweep verified this absence/openness against the full corpus.)*

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

**Reading note (2026-08-19, the owner's catch):** the consumption ledger above books
CONTACT PAIRINGS under seals, not rows-forever — B1066's own language ("any re-pose is a
new arc under a new seal") governs. The tones row's sin²θ pairing is spent; its
kind-correct moduli pairing (K2's own admissible row) had never been contacted and seals
as B1075 with the second-shot status priced. An unearned negative is as bad as
numerology — the dual protocol's words, applied to this table's own reading.
