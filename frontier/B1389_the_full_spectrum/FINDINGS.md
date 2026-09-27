# B1389 — THE FULL SPECTRUM (kill test 2, sealed): MIXED. On a member with a cuspidal Higgs class, the 27's spin-0 sector alone gives whole, anomaly-free Standard-Model generations. The Higgs direction must lie in the cone −1 < a/b < 2/3 round γ; there the 5 of the 15 has the opposite γ-charge to the 10 and enters as the 5̄. On cube~3.24 that is two generations in the frame. But the gauge multiplet's own broken roots, which 7d E₆ super-Yang–Mills always carries, make the local spectrum anomalous for every direction and in every frame that includes them. On the pure γ direction the 78's own 5̄ cancels the generation's 5̄ exactly and leaves a lone 10.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's "how do we continue bravely"; test 2 of
the kill tests, decidable before sL-8 because the pattern multiplies the count N · **Seal:** `PREREGISTRATION.md`, committed and
pushed at 8d9498d2 before any direction was read; sha256 in `docs/SEAL_LEDGER.md` · **Status:** MIXED, as sealed. Both halves are
exact (rational arithmetic, every cone visited). · **Fence:** the seat's frame; generations in the frame are not generations in
nature · **Price:** unchanged, 0 of 19 · **Numbering:** B1389.

## 0. Seen from above

**The question.** B1386/B1387 found a non-zero chiral count, N(v₊) = ±2 on cube~3.24, for "the spin-0 half of a generation". The
frame's rule gives every sector an index on a cuspidal member:
- a spin-0 sector μ (an SL(2)_β singlet: a weight of the 27 or a root of the 78) gets sign(⟨H, μ⟩)·N;
- every doublet gets 0 (B1372's Lemma A);
- here H = aY + bγ is the Higgs direction.

So the whole chiral spectrum follows from the charges. Is it complete generations, and is it anomaly-free?

**The sealed outcome.**

| frame (the bulk matter) | verdict | what the cones give |
|---|---|---|
| F27 (the 27) | **PASS** | exactly one complete generation (Q, u^c, e^c, d^c, L) per unit N, SM-anomaly-free, on the open cone −1 < a/b < 2/3 (both signs of b); everywhere else the 10 splits and the spectrum is anomalous |
| F78 (7d E₆ super-Yang–Mills) | FAIL | a chiral X,Y-type exotic (3,2)_{−5/6} whenever a ≠ 0; a lone 5̄ at a = 0 |
| F27+78 | FAIL | anomalous in all 12 cones; on the pure γ ray, a lone 10 |
| F133 (E₇'s adjoint, broken to E₆ × U(1)) | FAIL | anomalous in all 40 regions (24 distinct contents) |

Overall **MIXED**, as the declared prior (about 55%) expected.

**Why the 27 works.** In the record's own vectors (B1368), the spin-0 15 of the 27 carries two γ-charges:

| | Q | u^c | e^c | D | H_u |
|---|---|---|---|---|---|
| Y | 1/6 | −2/3 | 1 | −1/3 | 1/2 |
| γ | −2/3 | −2/3 | −2/3 | 4/3 | 4/3 |

The 10 carries γ = −2/3 and the 5 carries γ = +4/3. Along γ the 5 therefore has the opposite chirality to the 10. A 5 at negative
chirality is a 5̄ with exactly (d^c, L)'s quantum numbers. So the 15 alone is 10 + 5̄. The cone's edges are the hypercharge
component at which u^c (a/b = −1) or e^c (a/b = 2/3) would flip; the 5's own flips (a/b = 4, −8/3) lie outside.

**Why the fuller frames fail.** The 78's spin-0 non-Standard-Model roots are the 35's:
- the X,Y bosons' partners, with γ = 0 and Y = ∓5/6, which are chiral whenever the Higgs field has a Y-component;
- a 5 at γ = −2 and a 5̄ at γ = +2.

On the pure γ direction the 78 contributes one 5̄ per unit N. That cancels, exactly, the 5̄ the 27's 5 supplies, and leaves a lone 10
(anomalous: SU(3)³ ≠ 0). Off it, the X,Y partners turn chiral too. No direction and no admixture of E₇'s U(1) cures it.

**What this does and does not say.**
- *It corrects an inherited reading.* B1368 proved "one half of every generation is never chiral" on m004, where spin-0 sectors
  cannot be chiral at all. B1369–B1387 carried it on as "the spin-0 half is the 10". On a cuspidal member the spin-0 sector is the
  whole 15, and it carries whole generations: in the 27-frame the missing 5̄ was inside the spin-0 sector all along.
- *It finds the frame inconsistent as a gauge theory.* The bulk that 7d E₆ super-Yang–Mills actually carries (the 78's broken
  roots) is anomalous in every direction. Non-abelian anomalies have no Green–Schwarz cure. So the local spectrum is consistent only
  if the completion cancels the gauge sector's anomaly (anomaly inflow at the cusps), or the 78's charged roots are removed or
  paired. This is the completion's third job in sL-8.
- *U(1)_γ, in the passing cone, has universal anomalies.* The mixed anomalies are equal once normalised: [SU(3)]²γ = [SU(2)]²γ =
  (3/5)·Y²γ = ±5/3 (Y in SU(5) normalisation). A single Green–Schwarz axion can make it massive, as B864 requires of every abelian
  direction other than hypercharge over a chiral generation.
- *No physics is crossed.* The generations are the frame's, conditional on sL-8 (which count, which completion) and now on the
  anomaly's cancellation. 0 of 19.

## 1. The seal

- **Sealed:** `PREREGISTRATION.md` at 8d9498d2, before any direction was read.
- **Declared prior:** F27 PASS about 85%; F78 FAIL about 85%; F27+78 FAIL about 75%; F133 FAIL about 70%; overall MIXED about 55%.
- **The criterion.**
  - A frame passes if some open cone gives an SM-anomaly-free net content equal to n ≠ 0 complete generations, with no chiral
    SM-charged exotic.
  - The anomalies checked are [SU(3)]³, [SU(3)]²Y, [SU(2)]²Y, Y³, grav·Y and Witten's.
  - Overall: POSITIVE if F27+78 or F133 passes; MIXED if only F27 or F78; NEGATIVE if none.
- **The consequences, fixed in advance:**
  - *F27 passes.* B1368's frame theorem is scoped to members without a cuspidal class. The 27's spin-0 sector carries |N|
    generations; for cube~3.24, two in the frame, conditional on sL-8.
  - *All fuller frames fail.* The frame is consistent only if something outside it cancels the anomaly. That is registered as a
    lead, and the 27-frame's generations are physical only with the 78's charged roots removed or paired.

## 2. Computed (`verification/full_spectrum.py`, record `full_spectrum_run.txt`; exact rationals)

- **The banked identity, reproduced first.**
  - B1368's census:
    - the 27 by SL(2)_β spin: 15 + 12;
    - the 78's roots by spin: 30 + 40 + 2;
    - the 27's spin-0 content: Q-type 6, u^c-type 3, e^c-type 1, D-type 3, H-type 2;
    - 22 non-SM spin-0 roots with six (Y·α, γ·α) pairs.
  - B1366's two SM singlets have equal non-zero γ.
  - The controls:
    - every weight of the 27 at +1 is anomaly-free;
    - one generation is anomaly-free and is recognised as one;
    - a lone 10 has [SU(3)]³ ≠ 0.
- **The rule.**
  - A spin-0 sector μ carries index sign(⟨H, μ⟩)·N, and 0 where ⟨H, μ⟩ = 0.
  - Doublets carry 0 (B1372's Lemma A).
  - The content is |N_μ| left-handed multiplets in sign(N_μ)·μ.
  - Anomalies come from the weights, with a generic SU(3) Cartan direction t = (1, 2, −3) and the SU(2) direction s.
- **Every cone.**
  - F27 and F78 have critical lines at a/b ∈ {4, −1, 2/3, −8/3} and {4, 0, −6}, respectively. Every open sector and every ray is
    visited, both signs.
  - F27+78 has 12 open sectors.
  - F133 has 40 regions of the plane arrangement in (a, b, c), with 24 distinct contents, found by exact-sign sampling round every
    intersection line.
- **F27's passing cone** is −1 < a/b < 2/3.
  - Per unit N it holds one generation: for b > 0 an anti-generation, for b < 0 a generation. The overall sign is the choice of the
    class's generator.
  - U(1)_γ's anomalies there: γ³ = ±400/27, γ²Y = 0, γY² = ±25/9, grav·γ = ±40/3, [SU(3)]²γ = ±140/3 with Tr₃ t² = 14 (so ±5/3 at
    T(fund) = ½), and [SU(2)]²γ = ±5/3.
- **F78, F27+78, F133.** No open cone is anomaly-free. The record lists every cone's content and non-zero anomalies.

## 3. The statements

**Theorem (the 27's spin-0 sector carries whole generations).** In the seat's frame, on a member with a cuspidal Higgs class of count
N, with the Higgs direction H = aY + bγ in the open cone −1 < a/b < 2/3, the 27's spin-0 sector has net chiral content |N| complete
Standard-Model generations. That is |N|·(Q + u^c + e^c + d^c + L), SM-anomaly-free, with d^c and L supplied by the 5 of the 15 at
negative chirality. Outside the cone the 10 splits and the content is anomalous.

**Theorem (the gauge sector spoils it).** In the same frame, for every H ≠ 0, the net chiral content of the 78's spin-0 broken roots
is anomalous. So is the 27's content together with them, with or without E₇'s U(1)_Z component (F133). On the pure γ direction the
total is a lone 10 per unit N.

**Corollary (cube~3.24).** N = ±2, so the 27-frame gives two generations in the cone. The fuller frames give anomalous spectra.

## 4. What it means

- **Test 2 splits the frame.**
  - As a matter frame the 27 works. The record's long-standing reading, "the spin-0 half of a generation", undersold it: the spin-0
    sector of the 27 is a whole generation factory once the class is cuspidal.
  - As a gauge theory the frame is anomalous. A 7d E₆ theory carries its 78, and the 78's broken roots are chiral too. The anomaly
    has to go somewhere.
- **Where it can go is the completion.** In a non-compact local model, anomalies of the local spectrum are cancelled by inflow from
  the ends. Here the ends are the cusps, and their completion is sL-8. The completion now has three jobs:
  1. fix which count is physical;
  2. fix whether the cut respects the symmetry;
  3. carry the gauge sector's anomaly.
  The first two could still come out either way. The third is forced: a consistent completion must supply chiral matter at the cusps
  that cancels the local anomaly, and that matter is itself part of the spectrum.
- **The three generations question is unchanged.** Two, not three, on cube~3.24 (sL-5's cover-resolution question is where a three
  would come from). Counts are also conditional on B1388's anatomy (which count) and on the anomaly (which completion).

## 5. Fences

- **The frame.** Pantev–Wijnholt on the cusped 3-manifold, B1351 (ii) per sector with the charge sign, and B1372's Lemma A for the
  doublets. The four frames are the record's readings, and none is derived here as the physical one.
- **The count.** Any non-zero N. The pattern multiplies it, so B1388's two counts and sL-8's definition question do not change the
  pattern, only the number.
- **The Higgs direction** ranges over c(SM)'s Cartan plane (and E₇'s U(1) for F133). Non-abelian Higgs data beyond SL(2)_β's
  geometric part is not considered.
- **Anomalies.**
  - The criterion is the Standard Model's gauge anomalies, local and global.
  - The extra U(1)s are reported: universal in the passing cone.
  - Mixed gravitational anomalies of the SM factors vanish identically.
- **Generations in the frame are not generations in nature.** No physics is crossed. 0 of 19.

## 6. Files

- `PREREGISTRATION.md` — the seal.
- `verification/full_spectrum.py`, `verification/full_spectrum_run.txt`:
  - the record's vectors, verbatim from B1368;
  - the banked identity and controls;
  - every cone of the four frames, with its content and anomalies.
- `tests/test_b1389_the_full_spectrum.py` — the lock:
  - the identity;
  - F27's cone and its universal U(1)_γ anomalies;
  - every cone of F78 and F27+78 failing;
  - the 78's lone 5̄ on the γ ray.
