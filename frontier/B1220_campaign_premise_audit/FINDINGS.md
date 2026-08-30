# B1220 — THE CAMPAIGN'S PREMISE AUDIT: all three math cells were already answered, and every answer is stronger than the cell assumed

**Status: banked (frontier). Verdict PROVED** (three premises audited against the banked record;
three corrections; one internal contradiction found in a banked verdict line; λ's acceptance gate
assembled from banked pieces). Cells 1–3 of the publication campaign, **not run as designed —
because none of them needed to be.** Gate 5 clean.

## What happened

`docs/PUBLICATION_CAMPAIGN.md` opened with six cells and a stop rule: **Cell 0 gates Cells 1–3.**
Cell 0 (B1219) ran and reported the gate open — *no banked work found that changes their design.*

**That verdict was correct and insufficient, and the distinction matters.** Cell 0 sweeps
**arcs → surfaces**: it finds banked results that reached *no* surface. The arcs that actually
decide Cells 1–3 are all **on** surfaces — they are recent, cited, and perfectly visible. Cell 0 was
never going to see them. What found them was running `already_banked.py` **on each cell's own
premise** before running the cell.

**Result: all three math cells were already substantially answered.** Not one needed its designed
computation.

---

## Cell 1 — λ's acceptance gate: IT ALREADY EXISTS, in banked pieces

The cell was to *write* a failable criterion. The criterion is already proved; nobody had assembled
it into a gate.

**GC-15's theorem** (B1191, extracted verbatim): data is a pair **(T, G)** with
**G := Stab_Aut(D)|_T read off D itself, never chosen.** A measure μ is *expressible from D* iff
μ = Φ(D) with Φ natural under Aut — and that **forces g∗μ = μ for every g ∈ G**. *This half is
unconditional: it holds in every regime with no extra hypothesis.* Three proved regimes settle
existence/uniqueness/cost:

| regime | invariant object | selector cost |
|---|---|---|
| (i) T finite, G transitive | unique invariant probability = counting 1/\|T\| | **exactly log₂\|T\| bits** |
| (ii) T = S¹, G = ⟨irrational rotation⟩ | unique = Lebesgue (Weyl) | — |
| (iii) non-compact, Haar non-normalizable | none | prior-vs-point **ill-typed** |

plus B1196/GC-27's new boundary characterization: **prior-vs-point is ill-typed exactly at Haar
non-normalizability.**

**So λ's gate, stated:** *λ is derivable from the object iff a pair (T, G) can be **read off D** for
it — never chosen — and T falls in a regime admitting a normalizable G-invariant measure.*

**It is failable in both directions, which is the whole requirement**: regime (i) shows it can
**accept** (with the cost priced exactly); and it currently **rejects** — GC-27 records that **λ
fails even the theorem's first hypothesis: no (T, G) pair has been read off D for it.** MB12
satisfied by demonstration, not assertion.

### A contradiction inside a banked verdict line, found here

**B1196's `claim_one_line` says:** *"the sigma and lambda continuous legs sit on **the
non-normalizable side** of the sharp boundary, which is WHY they are anchors."*

**B1196's own cell record (GC-27) says:** the dichotomy *"cleanly explains why σ and λ sit on
**opposite sides** of a sharp boundary"* — and, decisively, that **λ fails even the theorem's first
hypothesis**, with the seal typed **PARTIAL** and two remaining lemmas named.

These are not the same statement. The verdict line asserts the theorem *explains* λ; the cell says
the theorem *does not reach* λ. **The summary overstates its own cell**, in the direction that makes
the record look more finished. Corrected by dated addendum, not edit. *This is E53's mechanism at
its smallest scale: one arc, two texts, and the shorter one is the one everybody reads.*

---

## Cell 2 — the ℙ³: the exhaustion was already run, and the row is CLOSED-PERMANENT

The cell was to decide by exhaustion whether a second independent condition exists, with a
pre-registered expectation of **none**.

**Already done, and the expectation was right.** B1208 LEG 9: *"B1206's ledger **STANDS at dim 1** —
**all three of its named candidates are now negative**, and **the space they were drawn from is
closed**."* And **B1196: "5 CLOSED-PERMANENT (the ℙ³ floor)"**, PROVED — **hardened twice** by B1208.

Candidate (iii) — the λ-term's rank, B1206's own "cheapest" discriminator — was convicted
**MB12-vacuous**: rank 1 is *impossible* for a doublet–doublet–singlet coupling, so the fork's two
branches were *"impossible"* and *"always."* B1208 also **corrected the derivation** of that
impossibility: t₃-conservation is only the Cartan and permits the rank-1 witness `[[0,−3],[0,0]]`;
the exclusion needs **full SU(2) invariance**, which gives the one-dimensional invariant space
`[[0,−c],[c,0]]` with det = c².

**The one datum that could overturn it, and it is externally blocked.** B1208 preregistered a
three-outcome fork on whether the **lepton** leg admits a character triple satisfying the down row's
selection rule (down legs: A₇ × B₆ × B₂). Outcome **(b)** — different characters selecting different
classes → a second independent 3×3×4 tensor → **the ledger closes at dim 0 and the ℙ³ flips
PERMANENT → FORCED** — is *"the largest single lever currently identified on the value arm."*

B1215 carried it one step: the rule is **not a constant** — the invariant is the raw total, so
ρ+σ = 3 − χ(A) mod 12, reproducing the spec's own 8 for A₇ and giving **4 for A₁₁**; on the
spec-pinned alphabet A₁₁ yields (0,4) and (2,2), with (2,2) vanishing by the same skewness that
killed (4,4). **Fenced honestly:** that the lepton leg *is* A₁₁ is a reading of codex's frames,
which their own certificate leaves **undetermined at generation level** — evidence against branch
(a), toward (b) or (c), deciding neither.

**Status: the datum is in flight at another seat.** codex R028 pinned the frame layer but claims no
Yukawa entry; R029 states no status for **R030's in-flight characteristic-zero Yukawa computation**.
**Cell 2 is blocked on R030, not on us** — and that is a scheduling fact, not a mathematical gap.

---

## Cell 3 — B632's symmetric texture: answered NEGATIVE, by the cell's own method

The campaign called this *"the one cell whose outcome this bench genuinely cannot predict."* It was
predicted, in 2026-08-12, by **B1036 (PROVED)** — using **Mayer–Vietoris from banked pieces**, which
is precisely the method B632's cell 3 registers.

**B1036's headline: "THE DOUBLE GAINS CLASSES, NOT THE SYMMETRIC PAIRING."** h¹(dbl;27) = **5** =
2+2+1 against the solo 3, by **two independent routes agreeing blockwise** (the MV assembly with
identity gluing, and direct Fox calculus on the double's 3-generator 3-relator presentation).

**V3, which is Cell 3's question:** *"THE SYMMETRIC TEXTURE'S OBSTRUCTION EXTENDS … the record route
computes the seam-sector pairing (direct T² restrictions, holonomy-invariant form, gauge control
PASS) and finds the **symmetric support EMPTY in every cell of every block including the seam-born
classes**: the one scalar sector the closed double newly opens carries **no mass-shaped pairing**;
**the solo antisymmetry wall extends through the seam.**"*

Two of its routes **halted at their own sealed controls**, and the second halt was itself a finding
(the per-side scalar route's vacuity *is* B632's O2 restated). Two of five pre-registered silent
failure modes **fired loudly at sealed controls — which is the system working.**

**The genuinely unrun residual is narrower than the cell as written**, and B1036 names it: **the full
V-valued double assembly.** That, not "the symmetric texture on the double," is the live item.

---

## What this says about the campaign, and about the method

**Three for three.** Every math cell's premise was stale, and in **every** case the banked record was
**stronger** than the campaign assumed: a gate that exists rather than one to be invented; a row
CLOSED-PERMANENT rather than one condition short; a texture proved empty rather than an open
computation.

**Cell 0's design gap, named.** Cell 0 asks *"which banked results reached no surface?"* The far more
expensive failure is *"which of my premises is stale?"* — and those arcs are usually **on** surfaces,
so no off-surface sweep can find them. **A campaign must audit each cell's premise against
`already_banked.py` before running it, not only sweep for orphans.** That is now the campaign's
stop rule 1b, and it is the single cheapest instrument in this programme: three cells, three hits,
zero computation.

**What actually remains** (unchanged in difficulty, sharply reduced in scope):
1. **λ** — a (T, G) pair read off D. The gate is written; nothing satisfies it yet.
2. **the ℙ³** — codex R030's in-flight lepton Yukawa, deciding branch (b) vs (c).
3. **the double** — the full V-valued assembly.

None of the three is what the campaign set out to compute, and all three are better posed.
