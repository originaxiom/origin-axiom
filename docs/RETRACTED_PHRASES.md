# THE RETRACTED-PHRASE REGISTRY

*Purpose (L139, from B965): **retracting a claim does not retract its instances.** B964
retracted the bare use of "VEV" and wrote a rule; one hour later the LAW_MAP audit found that
exact error still live in a row written the same day. A retraction needs a **sweep**.*

**How this works.** Each row is a phrase that must not appear as a **live claim** anywhere in
the tracked corpus. It **may** appear inside a retraction record, a correction banner, a
quotation of what was formerly claimed, or a test that enforces its absence — those are
*mentions*, not *uses*. The sweeper (`scripts/checks/retraction_sweep.py`, gated as
`retraction-sweep`) enforces exactly that distinction.

**Adding a row is part of retracting.** A retraction is not complete until its phrase is
registered here and the sweep is clean.

| # | retracted phrase (case-insensitive) | retracted by | why it is wrong |
|---|---|---|---|
| 1 | `the object does not supply a VEV` | **B964** | False. An adjoint VEV's unbroken group **is** the centralizer of that element, so the measurement cascade **is** an adjoint Higgs mechanism. The object supplies the rank-preserving half; it lacks the rank-reducing **27** half. |
| 2 | `stops one step short` *(as a general claim)* | **B964** | Scope error. True only for **27-only** breaking; the **78** contains a **24**, so the standard chain completes. |
| 3 | `the first 25-digit Maass eigenvalue` | **B943** | Priority claim on a sweep of unrecorded depth; prior art found, precedent number refuted (13 places, not ~10). |
| 4 | `the golden power` *(for 5¹²)* | **B941 amendment** | B937 refuted the golden-field reading four independent ways: 5 is a **residue characteristic**. The open question is the **exponent**, not the field. |
| 5 | `no intermediate regime` *(as a general claim)* | **B963** | Scope error. B576's threshold holds only for deformations containing the **principal sl₂**, not for arbitrary or finite-image representations. |
| 6 | `the object is hyperbolic` *(as a claim about the object as a whole)* | **B981** | Half-face reading. **B248 proves a cone-angle transition through all three curvature signs**: hyperbolic ℚ(√−3)/E₆ at α=0, **Euclidean** at α=2π/3, **spherical** ℚ(√5)/E₈ at α=π. B250 computes **both** ends (CS=0 **vs π²/5**). Any argument resting on the object being negatively curved *only* is unsound. |
| 7 | `measurement = the β=1 SSB` *(and `measurement=the β=1 SSB`)* | **B942**, registered **B1004** | Retracted by B942 (computed two ways, four escape hatches closed) and **refuted** by B957 (every B700 torsor has structure group **ℤ/2**; a group of order two is not the idèle class group of ℚ(√−3); the fields are mutually blind). **B967 deliberately left this unregistered** so the sweep would not fire on B723's own correction banner — **and the cost was three LAW_MAP rows still asserting it, one INHERITING IT AS AN AXIOM.** Registered now; the banner text is a *mention*, which the sweep's cue-matching already handles. |
| 8 | `chirality and rank compete for one resource` *(and variants: "one contested bit", "two holes sharing one resource")* | **B1017** | Category slip. τ is the only rank-reducing **involution** (true), but the cascade's rank drop is by **VEVs** (⟨1⟩, ⟨ν^c⟩) — not involutions. Five resources; the rank closing unsourced by the torsor. |
| 9 | `E₆ × E₈` *(the **product** form — the doorway factorizing; and `the doorway factorizes`)* | **cc3, `1a0b5a90`** (banked `27d9ceb9`, withdrawn the same day) | **Wrong three ways.** (1) The fiber-field-side group at congruence level 15 is **`2I × ℤ/3`, order 360**, not order 2880. (2) `LAW_MAP` banks the congruence-level-15 form as **IRREDUCIBLE** — **59 of 60 primes falsify** the `L`-factorization (B695) — so the claim asserts the *opposite* of the banked law. (3) Part III claims no such chain. **The real mechanism is the two curvature ends** (B248/B981), carried by §5.3 of the structure paper. **The correct banked form is the dual pair `E₆ + E₈`, which is TRUE and must stay usable** — hence this row polices the **product**, not the sum. |
| 10 | `the whole exceptional series` *(for `N ∈ {3,4,5}` giving `2T`, `2O`, `2I`)* | **cc3, `61ddb1f5`**, confirming **B207** (2026-06-25) | `E₇ = 2O` **never occurs.** At prime level `\|SL(2,𝔽_p)\| = p(p²−1)` is never `48` (B207; L105 refines `2O` to a *quotient*, not a subgroup; CLAIMS E11's GAP census finds `2O` absent from golden/silver/bronze). And although `\|SL(2,ℤ/4)\| = 48 = \|2O\|`, that group has **seven** involutions where every finite subgroup of `SU(2)` has exactly **one** — an order coincidence. `E₆` and `E₈` are realized as groups; the `E₇` slot is not. |

> **Row 9 was registered too broadly on the first attempt, and the sweep caught it.** The
> phrase first registered was `2T × 2I`, which fired on
> `frontier/B654_listening_synthesis/FINDINGS.md:92` — **a true statement.**
> `SL(2,ℤ/15) ≅ 2T × 2I` is a genuine theorem: `15 = 3·5` is coprime, so `ℤ/15 ≅ ℤ/3 × ℤ/5`
> as rings by CRT, hence `SL(2,ℤ/15) ≅ SL(2,ℤ/3) × SL(2,ℤ/5) ≅ 2T × 2I`, order
> `24 · 120 = 2880` (verified). **What was retracted was never the group theory** — it was the
> claim that *the object's* level-15 structure factorizes that way and yields a product of
> exceptional algebras. Narrowed to the **product form `E₆ × E₈`**, which is the false claim's
> signature and which the true dual pair `E₆ + E₈` does not match. **This is the registry's
> stated limitation working as designed: a phrase must be specific enough to be unambiguous,
> and the sweep is what proves it is not.**
>
> **Note on row 9 — the registry's own rule, applied to its author.** The header states:
> *"Adding a row is part of retracting. A retraction is not complete until its phrase is
> registered here and the sweep is clean."* The doorway claim was withdrawn on 2026-08-14 and
> the prose row corrected, **but the phrase was never registered — so the sweep stayed blind,
> and the retracted chain survived in the paper's FIGURE 0 spec until 2026-08-15**, where it
> would have been redrawn into the compiled PDF. **This is exactly the B965 pattern the
> registry exists to prevent, committed by the seat that wrote the correction.** Registered
> late, with the delay recorded rather than tidied away.

## Deliberately NOT registered

- **~~"chirality = the extremal-KMS / Galois label"~~ — MOVED TO ROW 7 (B1004).** The non-registration was correct in intent and wrong in effect: leaving it out kept the sweep quiet **and left three LAW_MAP rows asserting the retracted clause.** The mention-cue machinery handles correction banners; the phrase belongs in the registry.
- *(original note:)* **"chirality = the extremal-KMS / Galois label"** (retracted by B942) — B723 carries a
  correction banner and the phrase survives there only as the record of what was claimed.
  Registering it would fire on the banner itself; the banner is the correct treatment.
- **"the Standard Model algebra"** for su(3)⊕su(2)⊕u(1)³ (corrected by B950) — the phrase is
  ordinary English used correctly in many places. A phrase registry cannot distinguish those;
  **B892's banner and the amended LAW_MAP row are the correct treatment.**

**This asymmetry is the registry's main limitation and is stated rather than hidden:** it can
only police phrases specific enough to be unambiguous. Broad phrases need banners, not
greps.

## Currency read 2026-08-13 (window B1018–B1064; head B1064)

Three phrases retracted in this window, registered with their treatment:

- **~~"cubic-cyclic K"~~ (retracted 2026-08-13, the sweep's ONE-K block)** — the banking
  seat's mischaracterization of the charge field, proven wrong on-bench: a cyclic cubic has
  SQUARE discriminant; disc μ's squarefree part is 77. The correct phrase: **an S₃ cubic
  with quadratic resolvent ℚ(√77)** (B866's own statement; B894's banked resolvent, now
  understood as forced). Specific enough to police: any new "cubic-cyclic" near K fires.
- **~~"A5 certified (cc3)" / "all 18 roots loxodromic" as an x-only claim~~ (retracted
  2026-08-13, bdbc4267 + the M5 addendum)** — x-eliminant typing reported as full-triple
  certification, withdrawn by its author under the full-triple rule they wrote. Treatment:
  the ASYMMETRY PRINCIPLE now standing (one elliptic coordinate excludes; certification
  requires all three), and A5 was subsequently certified properly (18/18 deterministic,
  60-digit, this bench). The phrase "all loxodromic" without a full-triple citation fires.
- **~~"the bridge is one step wide" as a statement about THE CHAIN~~ (corrected
  2026-08-13, the segment-correction, both seats)** — B1044's true statement about
  Layers 2/3 mis-scoped to the whole chain, whose Part I DERIVES m004 from C1–C6.
  Treatment: banner-style (the phrase is true at its own scope); the sweep ledger's
  re-frame section carries the scoping.

## Currency addition 2026-08-14 (the B426 boundary repair; ported from the consolidation branch's rows 9–10)

- **~~"THE SEAM DOES NOT CONTRACT — the one scale lever stands … Ratio ≈ 1.2170 > 1"~~**
  — the 1.2170 is ONE Galois conjugate, not an invariant of the orbit; retracted on
  the branch (their row 9), ported with the boundary repair.
- **~~"Every Galois-invariant functional of the orbit is < 1"~~** (B426's slogan) —
  false: e₁ = 3/2 and M₆ = 1.0134 exceed 1 (verified from the banked minpoly). The
  defensible form: **every genuine AVERAGE contracts (p < p\* = 5.5932)** — the
  boundary computed in B426's 2026-08-14 addendum.
