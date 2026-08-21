# B1119 — THE ANOMALY, RESOLVED: a fake invariant form, caught by the classification theorem as checksum

**Status: banked (frontier). Verdict PROVED (a resolved error + a banked detection
method). Harvest arc (ANOMALY_RESOLVED.md, the EIGHTH memo; cloud seat credited).
Banked as a PAIR with B1118 (the error-class and the checksum method travel with the
result, per the outside bench's request). Gate 5 untouched. Lock
`tests/test_b1119_anomaly.py`.**

## The anomaly and its root cause

B1118's first real-form run produced an "impossible" invariant value — **character
−10**, which no real form of E₆ can carry. Root cause: **a FAKE INVARIANT FORM.** The
inner product used (⟨e_r, e_{−r}⟩ = +1) is invariant under the STANDARD convention, but
the paper's convention has [e_r, e_{−r}] = −h_r uniformly, so the ad-invariant form
needs **⟨e_r, e_{−r}⟩ = −1**. The +1 form was τ-invariant (invariant under the symmetry
being studied) but NOT ad-invariant — a form that passed five checks because none
tested ad-invariance.

## THE DETECTION METHOD (the banked contribution): the classification theorem as checksum

**An "impossible" invariant value means an instrument is lying.** The finite
classification of E₆ real forms admits only characters in a known set; −10 is not in
it; therefore the form (not the algebra) was wrong. This is a general, reusable
checksum: **when a computed invariant lands outside the classification theorem's
allowed values, the computation — not the object — is at fault.** Filed as the method,
E-class in the error ledger.

## The corrected results (exact, controls green)

- control τ = id → split **E₆(6)**, character **+6** ✓
- variant A (mirror swap, identity on color) → **E₆(2)** quaternionic (color sl(3,ℝ)),
  the signature honestly established (it was insensitive to the defect)
- variant B (mirror swap, duality on color) → **E₆(6) split**, character +6 (the former
  "−10" in full), color su(2,1)
- compact-involution control → −78 exact

**Neither lift gives compact color** — the open question (the finite 𝔽₂-kernel sweep,
C-AR1). **B1114's Lorentz algebra is UNAFFECTED** (it uses only brackets and
dimensions, which the invariant form does not enter) — the so(3,1)⊕su(3) result stands.

## Fences

The corrected verdicts are exact with controls green (the cloud seat's certificate;
carried). The compact-color question is open. The value of this arc is the METHOD
(classification-as-checksum) as much as the corrected numbers. No SM value; Gate 5
untouched.
