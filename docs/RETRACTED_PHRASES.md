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

## Deliberately NOT registered

- **"chirality = the extremal-KMS / Galois label"** (retracted by B942) — B723 carries a
  correction banner and the phrase survives there only as the record of what was claimed.
  Registering it would fire on the banner itself; the banner is the correct treatment.
- **"the Standard Model algebra"** for su(3)⊕su(2)⊕u(1)³ (corrected by B950) — the phrase is
  ordinary English used correctly in many places. A phrase registry cannot distinguish those;
  **B892's banner and the amended LAW_MAP row are the correct treatment.**

**This asymmetry is the registry's main limitation and is stated rather than hidden:** it can
only police phrases specific enough to be unambiguous. Broad phrases need banners, not
greps.
