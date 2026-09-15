# Memo 220 — L72's UNIQUENESS RESIDUAL IS DISCHARGED, AND THE OBVIOUS ROUTE WOULD HAVE BEEN WRONG

**Certificate:** `outside_bench/certificates/l72_residual_discharged.py` ·
**Output:** `outside_bench/outputs/l72_residual_discharged.txt`
**No seal** — this verifies a computed object against statements **read verbatim** from a
source, supplied by the owner, that memo 219 recorded as unreachable from this box.

**Source, now read:** Rowell, Stong, Wang, *"On classification of modular tensor
categories"*, **arXiv:0712.1377v4, 9 Nov 2009** (and the published copy, both supplied as
PDFs by the owner, 2026-09-13). Memo 219 recorded `arxiv.org`, `people.tamu.edu` and
`escholarship.org` all returning `EGRESS_BLOCKED`; **the owner's upload is how this bench
came to read it.**

---

## 1. The residual, and what it needed

`P2W5-L72` fenced one thing as EXTERNAL: *"uniqueness-up-to-gauge of the level-2 F-symbols
(constructed + verified, **not classified**)."* Memo 211 closed its Galois half; memo 218
showed it reaches no reported number; memo 219 said the rest was literature this box could
not reach. **It is now reached, and it closes.**

## 2. Four checks, all passing

**CHECK 1 — the fusion rules.** RSW §5.3.6, quoted: *"Fusion rules: α² = 1 + β,
αβ = α + β, β² = 1 + α + β."* Computed on this bench from the Verlinde formula on the
rebuilt E₆ level-2 stage: **α² = 1 + β · αβ = α + β · β² = 1 + α + β.** Identical.

**CHECK 2 — the quantum dimensions.** RSW **Theorem 3.2(3)** gives the only rank-3 modular
S̃ of this shape: *"d₁ is a real root of x³ − 2x² − x + 1 … the largest d₁ =
2.246979604…, and d₂ = 2cos(π/7) = 1.801937736…"*; §5.3.6 gives dims `{1, d, d²−1}` with
`d = 2cos(π/7)`. This bench's centraliser: **1, 1.801937736, 2.246979604** — every printed
digit.

**CHECK 3 — which member of the orbit.** RSW's listed representative has twists
`θ₁ = 1, θ_α = e^{2πi/7}, θ_β = e^{10πi/7}`, i.e. `h = 0, 1/7, 5/7`. Ours are
`h = 0, 2/7, 6/7`. **Complex conjugation maps ours exactly onto theirs.**

> So this bench's centraliser is the **complex conjugate** of RSW's chosen representative —
> **exactly consistent with memo 211's CELL 3**, which matched `k′ = 1` at 1.1e−15 and
> *rejected* `k′ = 6`, the conjugate, on S at 8.4e−2 and T at 8.7e−1.

**CHECK 4 — the sentence that discharges it.** RSW §5.4, verbatim:

> *"For the (A₁, 5)_½ fusion rule, all unitary MTCs are the one listed in last subsection
> and those from the two symmetries S → −S and complex conjugate."*

## 3. The discharge

The fusion rule is ours (CHECK 1). Its unitary MTCs are **completely listed**: the
`(A₁,5)_½` category and its images under **two named symmetries**. Our S and T pin which
member we are (CHECK 3, and memo 211 already rejected the other). A category so determined
has its F-symbols determined **up to gauge**.

> **The residual is discharged.** *"Constructed + verified, not classified"* is now
> **classified** — against a complete list, not against a uniqueness heuristic.

## 4. And the obvious route would have been wrong

The tempting citation was *"modular data determines the category."* **RSW state that as a
conjecture, in their own words, at §2:**

> *"Very likely the modular symbol of an MTC determines the MTC, and we do not know when a
> modular symbol becomes a modular data."*

**And it is false in general** — Mignard–Schauenburg exhibit arbitrarily many inequivalent
modular categories with the same modular data, the smallest known family at **rank 49**
(memo 219, search-derived).

> **INTERPRETIVE.** Had this bench leaned on the natural-sounding principle, the discharge
> would have rested on a statement its own authors called *"very likely"* and that was later
> disproved. What actually closes it is the **explicit realization classification** at rank
> ≤ 4 — a stronger, unconditional statement about this one fusion rule. **The difference
> between the two is the whole value of having read the paper instead of a summary of it.**

## 5. A free confirmation of the stage

RSW **Table 3** (*"Unitary Quantum Group Categories of rank ≤ 12"*) lists
**`(E₆, k), k = 1, 2` at ranks 3 and 9** — exactly the two stages this bench rebuilt from
the E₆ Cartan matrix in memos 206 and 211, and exactly the ranks those memos computed. A
number the bench derived and the paper tabulates, agreeing without either being consulted
for the other.

## 6. Scope, stated

- RSW classify **unitary** MTCs. Our centraliser's quantum dimensions are all positive
  (computed: 1, 1.8019, 2.2470) and it sits inside the E₆ level-2 WZW category; **unitarity
  of that ambient category is standard and is cited here, not proved on this bench.**
- The discharge is about **uniqueness of the category**, hence of the F-symbols up to gauge.
  It says nothing new about the *values* the cell computed — memo 218 already showed no
  reported number depends on them.
- **Memo 219 §5 is superseded on this point**: it said the residual *"is still not
  discharged"* because full texts were unreachable. The owner supplied the text; it is
  discharged. Memo 219's measurement of the egress block stands unchanged and is why the
  upload mattered.
