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

| 9 | `the one scale lever stands` | **B408's own correction**, registered **B1048** | The 1.2170 ratio was an artifact of **max over embeddings**, which is biased by embedding count; the normalised ratio is **0.7649 < 1** and **the object has NO scale lever in any tested channel**. `B408`'s `arc_verdict` was always `NEGATIVE`; only the headline said otherwise, and **it said so for 122 arcs**. Registering it required giving B408's headline a **correction banner** — the B723 treatment — which B1048 added, pointing at B408's own correction 27 lines below. **A scale-lever claim is what `WHAT_WOULD_COUNT` grades Tier 2 on**, so a live use of this phrase is the most consequential single sentence in the corpus. |
| 10 | `every Galois-invariant functional of the orbit is < 1` | **B1048** | Over-broad. The elementary symmetric **`e₁ = 3/2 > 1`** and the sixth power mean **`M₆ = 1.0134 > 1`**. The true statement is about **averages**: the power-mean family contracts for every `p` below **`p* = 5.5932…`** and exceeds 1 only as it degenerates toward `max` — the very bias B408's correction named. **B426's theorem is not weakened; it is given its boundary**, and B426 now carries the banner. |

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
