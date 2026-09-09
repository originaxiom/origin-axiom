# B840 — the three loose ends closed, and one of them was hiding a vacuous verdict

cc banking seat, 2026-08-01, at the owner's direction to close them all. Gate 5 untouched.

## B590 — the one that mattered

Paused 2026-07-14 with *"bank pending"*. Both cells were run.

**R2/V3 delivered its blind result**: nine Φ-orbits of size 3 on the 27, charge split 1/10/16 gate
PASS, `|16ᵢ∩16ⱼ|` = 16/10, **triple intersection `16∩16∩16` = 6**, three distinct singlets, and the
singlet's own orbit profile `(1,16,16)`. Read blind, no interpretation attached.

**R1 was printing `SEALED` at m=3 on both seeds — and the verdict was empty.**

> `polish_mp` built **9 complex trace equations (18 real) for 22 real unknowns**, and `mdnewton`
> needs a square system. It raised `cannot solve underdetermined system` on **every input at every
> m**. The loop counts that exception and `continue`s **before** the membership test — so
> `escapes == 0` held because **nothing was ever tested.**

**The m=1 pipeline validation shared the defect** (12 irreducible / 12 polish failures), so the guard
built to catch exactly this could not fire. **MB12 vacuity, in both the verdict and its own control.**

**Three bugs, fixed:** the underdetermined polish (exact torus gauge `B[0,1]=B[0,2]=1`, since the
residual SL(3) diagonal torus is exactly 2 complex dof and traces are conjugation-invariant); a
**50-vs-70-digit truncation** in `in_field` that let `lindep` fit a spurious height-10¹⁸ relation
past the residual gate; and control values built in **double precision** against a 1e-30 gate.
**The last two are independent — fixing either alone left the control failing.**

**With the pipeline working, m=1 does not seal**: 13/13 escapes, traces not in ℚ(√−3) (lindep heights
~10⁵⁰ against a 10⁶ gate). **R1 is now blocked on a real, diagnosed failure instead of passing
vacuously** — a strictly better state, and the m=3 question returns to the open queue.

**My own first fix was wrong** and the m=1 validation caught it: I pinned the gauge entries to their
*unpolished* least-squares values, capping the polish at ~1e-9. Replaced with the exact gauge.

**Unresolved and recorded:** the script computes the bronze trace field as **degree 8**; the prereg
quotes B578-D6 for **degree 6**. [B1238, 2026-09-02: the invariant trace field is degree **8** — the octic x⁸+6x⁶−x⁵+12x⁴−3x³+8x²−x+2 (disc 391728981, two routes at 1000 bits); the 6 was a residual-only integer-relation artefact (E56); resolved: 8]

## B557 — a filename artifact, like B519 before it

**Its results were reported all along**, in `CARRIERS_FINDINGS.md` and `E2_FINDINGS.md`. B837 counted
it as unreported because neither is called `FINDINGS.md`. Consolidated, no new result.

**E2 is the load-bearing cell and it is a partial deflation, not a confirmation:** by B517's
intertwining requirement `C = p(M)`, so the escalator rule `(C,D) = (M, M²)` is **FORCED at rung 1
and a CHOICE above it.** "Canonical" survives only at the first rung. **E0, the lit-gate that the
prereg made gate all novelty language, never ran — so no novelty claim is available and none is
made.**

## B499 — preregistered, never run

The directory holds a prereg and **nothing else**. Verdict `OPEN`, because **a campaign that never
ran settled nothing — which is not the same as one that ran and found nothing.** Its commitments
remain unspent and executable as written: the committed W2 null, the **283 airlock**, and a
statistics gate fixing **match = field isomorphism, not discriminant**, with LMFDB base rates.

## The pattern across all three

| arc | looked like | actually was |
|---|---|---|
| B590 | paused, bank pending | a **vacuous SEALED** hiding under a pause |
| B557 | unreported | reported under two other filenames |
| B499 | unreported | genuinely never run |

**Three arcs flagged by one audit, three different underlying states.** B837 said its number was 3
and that reading each was required; reading each is what separated them.

`tests/test_b840_loose_ends.py`
