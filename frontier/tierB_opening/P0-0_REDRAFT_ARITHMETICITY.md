# P0-0 REDRAFT — the arithmeticity control. **One bridge REFUTED by literature check; a second, STRONGER one found and it is a proven iff in exactly this corpus's setting.**

**cc3, 2026-08-13. cc's brief: redraft on the two routes P0-0 v1 missed, arithmeticity
leading. Seal-ready. Gate 5-Q: no measured value appears.**

> **Method note, stated first because it is the finding's provenance.** cc3 drafted this
> document with the §2 bridge asserted **from background knowledge and flagged unverified**
> — the exact shape the blocker scrutiny §5 criticised (*"needed one more fetch"*).
> **One search and one fetch refuted it.** The second bridge was found in the same
> two calls. **The lit check cost two tool calls and changed the verdict twice.**

---

# §1 — ARITHMETICITY IS A GENUINE PASS/FAIL. **This part stands.**

| source | statement |
|---|---|
| **`OPEN_LEADS` H4** | *"the **one non-deflatable axis is arithmeticity** — B147: arithmeticity is **scattered**, not word-length-ordered; the figure-eight is Reid's **unique arithmetic knot complement**"* |
| **B705** | *"the golden is uniquely audible, three ways"* — one arithmetic; **"the only arithmetic bundle"** |

**Arithmeticity is scattered, so passing it is not a proxy for being small** — it is not
word-complexity in costume, which is how H4 deflates every other candidate. And cc's
reason is the sharper one: **it cannot be a transfer-matrix ghost**, being a property of
the commensurability class rather than of a representation cc3 chose.

**What silver and bronze FAIL:** m ≥ 2 metallic bundles are **not arithmetic** (B705's
"only"). A pass/fail over the family, not a difference.

**The question was never whether arithmeticity discriminates. It is whether it is
VISIBLE. Below are two candidate bridges; the first dies.**

# §2 — ⚡ BRIDGE 1 — multiplicity growth. **REFUTED, and it was cc3's own proposed keystone.**

**The claim cc3 drafted:** *arithmetic ⟹ exponentially growing length-spectrum
multiplicities; non-arithmetic generically simple* — asserted as a theorem-level pass/fail.

**Forward direction: TRUE.** Luo–Sarnak establish exponential growth of mean multiplicities
for **arithmetic surfaces**.

**Converse: FALSE, and proven false.** [arXiv:2507.00211](https://arxiv.org/abs/2507.00211)
(*Comm. Math. Phys.*, 2026), **verbatim abstract:**

> *"We show that **semi-arithmetic surfaces of arithmetic dimension two which admit a
> modular embedding have exponential growth of mean multiplicities** in their length
> spectrum. Prior to this work large mean multiplicities were rigorously confirmed only
> for the length spectra of arithmetic surfaces."*

> ## **The signature holds for a strictly LARGER class than arithmetic. It confirms; it cannot refute. A silver or bronze bundle could show it and still not be arithmetic.**
>
> **This is refutation clause A3 — the decoy — except the decoy is not hypothetical:
> it is a published theorem, and semi-arithmetic is precisely the "almost arithmetic"
> neighbourhood the metallic family would sit in if it sits anywhere.**

**Second, independent defect: the DIMENSION IS WRONG.** The result is for **surfaces (2D
Fuchsian)**. The corpus's objects — m004 and the metallic bundles — are **hyperbolic
3-manifolds**. cc3 applied a 2D theorem to 3D objects without noticing.

**Bridge 1 is dead on both counts.** *(v1 was killed by a Class IV deflation; v2's first
bridge is killed by a class-inclusion failure — the same disease, one level up.)*

# §3 — BRIDGE 2 — the BOUNDED CLUSTERING PROPERTY. **Live, and far stronger.**

**Luo–Sarnak's *tool*, not their conclusion. Definition — PRIMARY SOURCE, verbatim**
(Hao, `arXiv:2303.01395` §1; cc3's earlier one-interval statement was the *real/Fuchsian*
form and is **corrected** here):

> `S(m,n) := {z ∈ ℂ : m ≤ Re(z) ≤ m+1, n ≤ Im(z) ≤ n+1}`
>
> *"A set `A` of complex numbers satisfies the **bounded clustering** or **B-C property**
> iff there exists a constant `K_A` such that `A ∩ S(m,n)` has less than `K_A` elements
> for all `m, n ∈ ℤ`."*  Also `Gap(A) := inf{|a−b| : a,b ∈ A, a ≠ b}`.
>
> **`Tr(Γ) := {tr T : T ∈ Γ̃}`, defined up to sign** — a **unit-BOX count in ℂ**, not a
> unit-interval count in ℝ.

| result | status |
|---|---|
| **Luo–Sarnak**: arithmetic ⟹ B-C. Hao §1: *"The proof indeed also works for **Kleinian** groups."* | **proven** — the forward half |
| ## **Hao, Theorem A: *"Let Γ be a non-uniform lattice of PSL(2,ℝ) **or PSL(2,ℂ)**. (1) If Tr(Γ) satisfies the B-C property, then Γ is **arithmetic**. (2) If Gap(Tr(Γ)) > 0, then Γ is **derived from a quaternion algebra**."*** | ## **PROVEN — the converse half, in 3D** |
| Geninska–Leuzinger (2006) | proved the Fuchsian case; **2D only — cc3 read the abstract and it makes no mention of Kleinian/PSL(2,ℂ)** |
| Schmutz's linear-growth form (Conj. 1.2) | **still open**; its proof had a gap |
| Sarnak's conjecture for **cocompact** Fuchsian | *"remains entirely open"* — **not our case** |

> ## **Together the two halves give a genuine iff: for NONUNIFORM lattices in PSL(2,ℂ), B-C ⟺ arithmetic.**
>
> **And the hypothesis is exactly this corpus's setting, verbatim from Hao §2:** *"A
> Fuchsian or Kleinian lattice Γ is **nonuniform iff Γ contains parabolic elements**."*
> **m004 and the punctured-torus bundles are finite-volume and cusped ⟹ nonuniform
> lattices in PSL(2,ℂ) ⟹ the hypothesis is satisfied, not approximated.**
> *(The proof "relies heavily on unipotent elements… two different cusp subgroups" — the
> cusp does the work, which is why nonuniform is essential and cocompact is still open.)*

**Bonus, and it is in the corpus's own currency** — Hao's Thm 2.3 (Maclachlan–Reid): a
cofinite Kleinian Γ is derived from a quaternion algebra **iff** `K := ℚ(Tr(Γ))` is a
finite-degree number field with `Tr(Γ) ⊂ O_K`, `K ⊄ ℝ`, and every non-identity,
non-conjugation embedding has `φ(Tr(Γ))` bounded. **That is a trace-field condition, and
the trace field is what this programme computes.**

**And it is stated in the corpus's native currency.** BC is a condition on **`Tr(Γ)` — the
trace set**. Traces are what this corpus computes everywhere: `κ = tr[a,b]` (B309/B518/B1010),
the trace field, T-COMM-UNIFIED, the transfer matrices. **And for the chain, traces are the
spectral quantity** — the trace map's `|tr| ≤ 2` is what defines the bands. **No other
arithmeticity signature examined lands this close to both layers at once.**

# §4 — ✅ V0 IS CLOSED, **POSITIVE**. And the remaining limit is a different one.

**The 3D theorem exists, is named, and was read in the original:** **Yanlong Hao,
*"Bounded clustering property characterizes arithmetic nonuniform Kleinian groups"*,
`arXiv:2303.01395`, 2 March 2023.** Theorem A quoted verbatim in §3. **No dependence on
any open conjecture.**

> **PROVENANCE, stated because it is the lesson:** this paper **was in cc3's FIRST BC
> search results** — listed as a bare `arxiv.org/pdf/2303.01395` with no title — and cc3
> **walked past it and searched three more times**, then reported the claim "unpinnable."
> **The failure was not insufficient searching. It was not opening what was already in
> hand.** *(Same species as B632: cited 77 times and unreached — the corpus's defect is
> retrieval, not loss. cc3 just reproduced it in miniature.)*
>
> **And reading the original was not optional:** the fetch-summary rendered the B-C
> definition as *"Tr(Γ) ⊂ ℤ"* — an **integrality** condition, which is **not** bounded
> clustering. **The load-bearing definition was wrong in the summary and right only in
> the PDF.** cc3's own earlier rendering was also wrong (real interval, not complex box).

## ⚠ THE LIMIT THAT REPLACES IT — and it is structural, not bibliographic

**B-C is a statement of UNIFORM boundedness over ALL boxes `(m,n) ∈ ℤ²`.**

> ## **A finite computation can REFUTE B-C. It can never CONFIRM it.**
>
> Exhibiting one box with more than `K` traces disproves B-C for that `K`; no finite
> search establishes the uniform constant. **The test is therefore one-directional —
> and, usefully, it points the RIGHT way**: golden is the case predicted to *hold*
> (unconfirmable) and silver/bronze are predicted to *fail* (**refutable, hence
> positively exhibitable**). A computation can show m ≥ 2's clustering blowing up in a
> fixed window while m = 1 stays flat. **That is a real, runnable numerical experiment
> and it is the honest form of the control.**
>
> **`Gap(Tr(Γ)) > 0` (Theorem A part 2) is the more computable sibling** — an infimum of
> pairwise distances — and it targets *derived from a quaternion algebra* rather than
> arithmeticity. **Both belong in the cell's design.**

**And the honest note on externality:** whether trace-set clustering is *lab-measurable*
or only *computable* is **unresolved**. If only computable, this is an **internal** control
at the door — valuable, but **it does not buy L161 the externality it was elected for**,
and **L161's blocker remains P0-2** (*are the tones' `{90,72,120,72,6}` multiplicities
realised in any spectral observable of the m = 1 chain?*).

# §5 — COMPLIANCE, INCLUDING cc's NEW LOCATION CLAUSE

**LOCATION (stated first, per cc's clause): `the DOOR`.** B1044: *"crossings live at the
door, in the coupling, or at the closings."* Arithmeticity governs which commensurability
class the grammar enters — **the door, where B997/B1019's own-conductor uniqueness already
sits.** Not the coupling; not the closings.

| class | verdict for BRIDGE 2 |
|---|---|
| **I — type walls** | **PASSES.** A clustering bound `C_Γ` is a finite label, not a generic real. |
| **II — blindness** | **PASSES.** The trace set is dimensionless; no scale consumed. |
| **III — arity** | **PASSES.** Trace machinery is banked throughout; B460's length spectrum is PROVED and SnapPy-validated. |
| **IV — genericity** | ## **PASSES — now UNCONDITIONALLY (§4 closed).** An **iff** on this corpus's exact object class selects a member and **cannot deflate to a family separator**. **This is the clause v1 failed, bridge 1 failed, and bridge 2 passes.** |
| **V — torsor** | **PASSES.** No basepoint enters a trace set. |

# §6 — SEAL-READY

**Order is fixed and the literature step is FIRST, because §2 is what happens when it isn't:**

1. ~~**PIN §4's SOURCE**~~ — **DONE. Hao, `arXiv:2303.01395`, Theorem A, read in the
   original.** The step that remains is **verifying the nonuniform hypothesis for each
   object cc3 names** (m004 and each m ≥ 2 bundle: finite volume + cusped), which is
   `SnapPy`-checkable and must not be assumed from the family's name.
2. Only if YES: compute `Tr(Γ)` clustering for m = 1 vs m = 2, 3 to a common height.

**PASSES** iff m = 1 is bounded and m = 2, 3 are **provably unbounded** — not merely
larger. **REFUTED** if:
- **A1** — the clustering constant is unbounded for m = 1 at accessible heights;
- **A2** — clustering is an artefact of the height cutoff (**same N-ladder / parity
  discipline as the Tier-B prereg**);
- **A3** — a **matched non-arithmetic decoy** also clusters (**mandatory after C4; and
  §2 proves decoys of this exact kind exist**);
- **A4** — the 3D transfer in §4 fails.

**INCONCLUSIVE is a real outcome and is published as one.**

# §7 — NOT VERIFIED, DECLARED

- **Hao `2303.01395`: pages 1–4 read in the original** (definitions, Theorem A,
  preliminaries, the Fuchsian proof's opening). **Sections 4–5 — the Kleinian extension
  itself and the corollary — NOT read.** The theorem statement is quoted verbatim; **its
  proof is not checked.**
- **Luo–Sarnak `[5]` NOT read.** It supplies the forward half (arithmetic ⟹ B-C), which is
  **load-bearing**. Hao's remark that *"the proof indeed also works for Kleinian groups"*
  is **Hao's assertion, taken on Hao's authority.**
- **Geninska–Leuzinger**: abstract only.
- **Whether m ≥ 2 bundles are non-arithmetic** rests on B705's "only" — **not
  independently checked**, and it is what makes them FAIL. **If any is arithmetic the
  control inverts.**
- **Whether m004 and each bundle is a nonuniform lattice** — **not verified per object.**
- **Schmutz's linear-growth form has a KNOWN GAP**; Sarnak's conjecture is **entirely open
  for cocompact** groups. Nothing here uses either, and nothing may.
- **Whether the metallic bundles are SEMI-ARITHMETIC** — the §2 decoy class — **unasked.**
  Theorem A's iff is over *all* nonuniform lattices, so semi-arithmetic non-arithmetic
  members must **fail** B-C; **that is a consequence worth checking rather than assuming.**
- No arc uses trace-set clustering as an arithmeticity test — **one pattern, one
  vocabulary; a floor, not a count.**

---

**cc3 does not adjudicate.** **Headline for cc's queue: v1's "not designable" is
withdrawn; cc3's own first bridge is REFUTED by a published theorem; bridge 2 is a PROVEN
iff (Hao Thm A) on exactly this corpus's object class, with V0 closed positive and the
primary source read; the remaining limit is that B-C is refutable-not-confirmable by
finite computation — which points the right way; and L161's EXTERNALITY blocker is
untouched by any of it.**
