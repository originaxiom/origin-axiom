# B1477 — ADDENDUM (2026-10-07): the unexplained residue read at a longer cutoff — an unsealed check, archived so that it is not lost

**What FINDINGS §4 left.** Theorem B's criterion (an odd number of rotation-π geodesics at some length forbids every
mirror-invariant spin structure) was read at the sealed cutoff 3.0. Eight manifolds certified to have no
mirror-invariant spin structure showed no odd count there and are not explained by Theorem A either (they are at
Chern–Simons class 0, rectangular or closed): v3103, t10425, o10_085947, o10_149515 and the closed m078(5,1),
v1222(−5,1), v1695(−5,1), v3283(−3,1). "Certified none, mechanism not identified."

**The check.** `verification/residue_cutoff.py 3.8` recomputes that residue from `pi_geodesics.json` (it is not typed
in) and reads the same criterion at cutoff 3.8 → `residue_cutoff_3p8.json`, `residue_cutoff_3p8_run.txt`.

| manifold | kind | geodesics to 3.8 | rotation-π | an odd count at length |
|---|---|---|---|---|
| v3103 | cusped | 123 | 7 | 3.416401 |
| o10_149515 | cusped | 145 | 1 | 3.271677 |
| m078(5,1) | closed | 157 | 1 | 3.138144 |
| v3283(−3,1) | closed | 171 | 1 | 3.497925 |
| v1695(−5,1) | closed | 167 | 1 | 3.788180 |
| t10425 | cusped | 144 | 0 | — |
| o10_085947 | cusped | 164 | 0 | — |
| v1222(−5,1) | closed | 143 | 0 | — |

**Reading.** On five of the eight the residue was the cutoff's: Theorem B explains them once the spectrum is read
further. **Three stay unexplained — t10425, o10_085947, v1222(−5,1) — with no rotation-π geodesic at all to length 3.8.**
On those the obstruction is not a rotation-π geodesic of that length and not a cusp's fixed class.

**Status.** Unsealed and exploratory: it was first run in a session on 2026-10-06 without a seal, and re-run from this
script at the landing that archives it. It changes no verdict of B1477 and creates no law. It is the first input to the
statement main proposes to seal next (lead L246, "the complete obstruction"): for a mirror f and a lift s the class
ω_f, the restriction of η_f(s) to the f-invariant classes of H₁(M; ℤ/2), does not depend on s, and f fixes some spin
structure exactly when ω_f ≡ 1 — Theorem A being ω_f on a cusp's fixed class and Theorem B on an invariant rotation-π
geodesic. The three manifolds above are where that statement would first say something the two theorems do not.
