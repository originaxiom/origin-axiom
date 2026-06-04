# Physics computation plan — every path as a falsifiable probe

**For:** repository implementation · **From:** Dritëro (planning pass) · **Date:** 2026-06-04
**Method:** each path is a probe with **controls baked in** so a *negative* result CLOSES the path
honestly (the project's own discipline: failures are results). A probe that can only say "yes" is
numerology; every probe below can say "no." Three are **precomputed** in `physics_probes/*.py`
(verify + extend them); the rest are specced with their controls. Proven core P1–P16 untouched;
all probe output is exploratory/uncommitted until reviewed.

**Honest triage up front (so effort goes where it can pay):**
- **TIER 1 — real physics, computable now, PRECOMPUTED:** Path 1 (quasicrystal), 1b (gap labeling),
  7 (emergent precondition). Genuine crossings, but they land in 1D condensed matter — they do
  **not** reach the thesis. Value: real results + the one genuinely-novel extension (SL(n) model).
- **TIER 2 — computable, involved, implementer builds:** Path 4 (Reidemeister torsion), Path 3 (3d-3d
  *input* data). Topological; cross-validate the framework; prepare the object an expert would need.
- **TIER 3 — thesis-relevant but blocked; probe with HEAVY controls, expect negative:** Path 5
  (gauge), Path 6 (cosmological constant — already a repo kill; do NOT refit).
- **TIER 4 — not a computation:** Path 8 (catalogue the impossibility) — a writeup, deferred.

---

## TIER 1 — PRECOMPUTED (verify exactly, then extend)

### Path 1 — the trace map IS 1D quasicrystal physics (`path1_quasicrystal.py`)
**Precomputed & confirmed:** the SL(2) trace map is reproduced *exactly* from the physical
transfer matrices `M_j=[[E−V_j,−1],[1,0]]` (3e-15 violation); the Fricke–Vogt invariant
`I=(δ/2)²` exactly (so the repo's `I=1/4` surface = physical coupling `δ=V_A−V_B=1` — a real
dictionary entry); the spectrum is a Cantor set (vanishing bandwidth).
**Task — verify** the three checks reproduce. **Then the genuinely novel extension (the only
TIER-1 piece that could be new physics):**
- **Path 1-SL(n): does an n-channel / n-band tight-binding chain realize the SL(n) trace map, and
  do the tower's `a_d` multiplicities control its spectrum / gap structure?** Build an n-component
  transfer-matrix chain (transfer matrices in a larger group) whose trace recursion reduces to the
  project's SL(n) trace map under `φ_m`. **CONTROL:** if you cannot construct such a model whose
  traces follow the SL(n) trace map, report that as a NEGATIVE (the SL(n) tower has no physical
  realization — important and honest). If you can, compute its spectrum and test whether `a_d`
  appears in the gap-label / band structure.
**Reachability:** real physics; the SL(n) extension is the one genuinely-open, genuinely-novel
computable question in TIER 1. Still 1D condensed matter — not the thesis.

### Path 1b — gap labeling: a genuine topology→physics bridge (`path1b_gaplabeling.py`)
**Precomputed & confirmed:** 12/12 spectral gaps' IDOS values fall on the `Z+Zω` lattice
(`ω=1/φ`), errors ≤0.001 — a topological (K-theory) invariant fixing a measurable filling fraction.
**Task — verify**, then **extend to the SL(n)/multichannel model** (Path 1-SL(n)): do its gap
labels carry the tower's `a_d` data? **CONTROL:** compare against a periodic chain (trivial labels)
and a random chain (no quantized labels). **Reachability:** the strongest *real* topology↔physics
crossing available — but 1D, not the thesis.

### Path 7 — does the system have the STRUCTURE for emergent geometry? (`path7_emergent.py`)
**Precomputed — weakly NEGATIVE (controlled):** (A) the quasicrystal ground state is *critical*
(entanglement entropy `S~A·logL`, slope between periodic-critical and random-area-law) — clears the
*necessary* precondition for an emergent-geometry reading; but (B) the intrinsic counting is
*linear* (factor complexity `p(k)=k+1` exactly, Sturmian/zero-entropy; tower entropy `n·log μ`
linear) — the **wrong kind** for the sub-extensive/area scaling holographic emergence needs.
**Task — verify** both, push the entanglement fit to larger `L` (the slope should approach a
clean constant; confirm log not power), and **state the verdict**: critical-yes / area-law-no.
**CONTROL** is already in the script (periodic + random baselines). **Reachability:** this is the
most thesis-*aligned* path, and it came back weakly disqualifying — the natural entropy is the wrong
type. Record as a partial closure unless larger `L` overturns it.

---

## TIER 2 — computable, implementer builds (topological; cross-validate / prepare the object)

### Path 4 — adjoint Reidemeister torsion = 1-loop Chern–Simons partition function
At the **geometric (hyperbolic)** representation, the adjoint torsion is the semiclassical CS
partition function — a concrete number, computable from the rep data. B67 already has the
figure-eight geometric rep; the Ishibashi–Mizuno / Tran–Yamaguchi torsion formulae give a check.
**Task:** compute the adjoint torsion for (i) the figure-eight complement (= metallic `m`,
monodromy `M²`, from B67's rep) and (ii) the metallic mapping tori `φ_m`, and compare to the
published torsion = product-of-PGL₂-torsions formula. **CONTROL:** the torsion must match the
literature value where it exists (figure-eight); a mismatch means a bug, not a discovery.
**Reachability:** genuine invariant, cross-validates the framework — but **topological** (it is the
1-loop term of a TQFT; no propagating dynamics). Does NOT cross to the thesis. Value = a real
check + connects the tower to the torsion literature.

### Path 3 — 3d-3d correspondence: prepare the input data (the one expert-worthy crossing)
The 3d-3d correspondence maps the mapping torus to a 3D **N=2** gauge theory *with genuine local
dynamics* — the one place these objects touch dynamical (not topological) physics. Full extraction
needs a specialist, BUT the **input** is computable now: the Neumann–Zagier gluing data / the
A-polynomial of the metallic mapping tori (B67 has the figure-eight A-polynomial already).
**Task:** compute the A-polynomial / NZ datum for `φ_m`, `m=1,2,3` mapping tori (extend B67's
method). This is the concrete object a Dimofte/Gukov-circle specialist would evaluate. **CONTROL:**
the `m` giving the figure-eight must reproduce B67's known A-polynomial exactly.
**Reachability:** crosses into real dynamical physics — but lands in **3D supersymmetric** gauge
theory (wrong dimension, wrong symmetry for our world) and says nothing about origin/necessity.
Highest information value *if* an expert is ever consulted; until then, this prepares the object.
**Do NOT claim physics extraction from this — only prepare the data.**

---

## TIER 3 — thesis-relevant but blocked (HEAVY controls; expect negative)

### Path 5 — gauge symmetry from the SL(n) structure
The hope: the tower's SL(n) becomes nature's gauge group. **The honest probe is narrow:** does the
tower predict a *specific, novel, checkable* gauge-structural fact — NOT "resembles a gauge theory"?
**CONTROLS (mandatory, this is the numerology-risk path):** (i) any claimed feature must distinguish
the *actual* gauge data of nature (SU(3)×SU(2)×U(1), chiral reps, 3 generations) from generic SL(n)
structure; (ii) test the SAME claim against alternate substitutions `φ_m` (m≠1) and alternate `n` —
if the "match" appears for arbitrary choices, it's coincidence; (iii) the repo's `FAILURE_ATLAS`
"gauge dictionary missing" entry is the prior — beat it or confirm it. **Expected outcome:** "only
resembles" → confirm the gauge-dictionary kill from the structural side. **Do NOT** record a
resemblance as a match. **Reachability:** low; one honest structural check, probably negative.

### Path 6 — cosmological constant as near-cancellation residue
**This is already a repo KILL** (the "exact vacuum cancellation as category error" line; the CC
formula killed by null-hypothesis testing). **Do NOT refit another CC formula** — reopening a kill
without new input is the avoidance pattern. **The only permitted action:** state *precisely* what
NEW structural input would be required to reopen it (e.g. a derivation of a dimensionful scale from
within the framework, which Path 1's `δ↔I` dictionary does NOT supply), and leave it closed.
**Reachability:** the thesis's most direct test and a 50-year wall already bounced off here. Closed
pending a fundamentally new idea — not a computation.

---

## What this plan honestly is

Two paths (1, 1b) are **real physics, confirmed, modest** (1D). One (7) is the **most
thesis-aligned and came back weakly negative** (wrong entropy type). Two (4, 3) are **topological
cross-checks / object-prep**, not thesis crossings. Two (5, 6) are **thesis-relevant and blocked**
(numerology-risk / prior kill). **No probe here crosses from the framework into thesis-supporting
dynamical physics** — that is itself the result, and it is consistent with the `FAILURE_ATLAS`.
The genuinely-novel computable target is **Path 1-SL(n)** (does the tower describe a real
multichannel spectrum?); the genuinely-useful prep is **Path 3** (the object for an eventual
expert). Everything is a controlled probe: run them, record yes/no, and the map of which doors are
shut is the honest deliverable.

**Sequence:** verify the three precomputes exactly → build Path 1-SL(n) (the novel target,
with its negative-result control) → Path 4 torsion (cross-check) → Path 3 A-polynomial prep →
Path 5 gauge probe (heavy controls). Path 6 stays closed. Each result uncommitted, labeled by what
it shows, no overclaiming. Stop after each tier for review.
