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
