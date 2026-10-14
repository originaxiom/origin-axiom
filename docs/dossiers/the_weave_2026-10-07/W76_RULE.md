# W76 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner's order is "we look what fixes τ then we count free numbers".** The SM specification ledger (B1226)
  types the numbers by kind. Box D is the β-odd numbers (θ_QCD, δ_CKM, δ_PMNS). B1224 proved that amphichirality makes
  CS 2-torsion, so on m004 a β-odd number is a bit, not a value. The ledger registers that reading as L192: "box D was
  never actually tested".
- **W75 carried B1224's bit to the weave.** The weave's threads come in mirror pairs, so a weave sum taken over W and
  swap(W) alike is real, with phase 0 or π. W74 found the surface frame CP-invariant: with one coupling,
  arg det(M_u M_d) = 0, so θ̄ = θ.
- **Which bit, then?** A 2-torsion CS is 0 or π²/2 (mod π², in the record's normalisation). A read-out of W75 (no
  prior) found that all 55 mirror-symmetric threads to length 12 have CS = 0, and none has π²/2. B1224's census found
  π²/2 on half of the amphichiral manifolds it read (3 of 6), so the weave's threads may be special.
- **This arc asks whether the bit is 0 on every mirror-symmetric thread, further out.** If it is, then wherever the
  weave carries a β-odd bit, the bit is 0. With W74's arg det M = 0, the surface frame's θ̄ would be 0 if θ is read as
  the bit. That reading is L192's dictionary, which is not earned.

## Weave or thread?

- **A census of every thread under a stated rule:** every Lyndon word in L, R of length 2 to 16, with the bundle
  `b++` + word (the record's GM5d convention in GENESIS), none hand-picked. That is 8 798 threads.
- **The quantity is each thread's own CS,** not one defined by the joint action. So this is a census of thread
  quantities over every thread, and its claim (the bit on every mirror-symmetric thread) is about all threads at once.
  It is labelled a **weave census**, not a joint-action result.
- **The tags.** No dictionary: the reading of θ as the bit is L192's, registered and not banked.

## Seen before the rule (disclosed)

- **Read before this rule:** chat1's census to length 12 (K1b: every swap-symmetric thread has 2CS ≡ 0) and W75's
  read-outs to length 12 (55 mirror-symmetric threads, none with CS = π²/2, all at 0), and B1224's table.
- **Worked by hand.**
  - **The mirror.** M_{swap W} ≅ −M_W, since P L P = R with P = [[0, 1], [1, 0]], det P = −1.
  - **Reversal.** Reversal keeps the oriented bundle: φ_{rev W}ᵀ = φ_{swap W}, and φᵀ is conjugate to φ⁻¹ in SL(2, ℤ).
    M_{φ⁻¹} ≅ −M_φ, so M_{rev W} ≅ M_W.
  - **So a thread is mirror-symmetric** when swap(W) is a rotation of W, or of W reversed. Then M_W ≅ −M_W and
    2CS ≡ 0.
  - **The count of threads.** Lyndon words of length n = 13, 14, 15 and 16 number 630, 1 161, 2 182 and 4 080. With
    745 to length 12, the total is 8 798.
  - **No proof was found that CS = 0 rather than π²/2.** The layered triangulation pairs mirrored tetrahedra, but the
    flattenings may leave the 2-torsion class.
- **Nothing beyond length 12 has been computed.**

## The method (fixed here)

- **The threads.** SnapPy 3.3.2, `Manifold('b++' + W)` for every Lyndon word W (L < R) of length 2 to 16.
  CS = Im `complex_volume()`, reduced mod π² to (−π²/2, π²/2].
  - The solution type is recorded, and so is any exception.
- **Mirror-symmetric:** the least rotation of swap(W) equals W, or equals the least rotation of W reversed.
  - Each is recorded by kind: swap equals a rotation, or swap equals the reversal, or both.
- **The bit** of a mirror-symmetric thread is 0 if |CS| < 10⁻⁸, ½ if ||CS| − π²/2| < 10⁻⁸, and "neither" otherwise.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **B0, the instrument** | 8 798 threads, every one with the solution "all tetrahedra positively oriented" and no exception; b++LR has \|CS\| < 10⁻⁹. | 95% |
| **B1, the 2-torsion (control)** | Every mirror-symmetric thread has 2CS ≡ 0 mod π² to 10⁻⁸: no thread's bit is "neither". | 97% |
| **B2, the bit** | Every mirror-symmetric thread to length 16 has CS = 0: none has CS = π²/2. | 75% |
| **B3, no stray torsion** | No thread that is not mirror-symmetric has 2CS ≡ 0 mod π² (to 10⁻⁶). | 85% |

**The read-outs (no prior).**
- The number of mirror-symmetric threads at each length, and by kind.
- The largest |CS| among the mirror-symmetric threads.
- Any thread with |CS| < 10⁻⁶ that is not mirror-symmetric.
- The wall-clock time.

## The reading, written before the run (predicted)

- **If B2 holds: wherever the weave carries a β-odd bit, the bit is 0.** The weave's own mirror-symmetric threads
  never carry π²/2, unlike half of B1224's amphichiral census.
- **For θ̄ (I-18), not earned.** In the surface frame with one coupling, arg det M = 0 (W74). If θ is read as the
  weave's bit (L192's dictionary), then θ̄ = 0, which the data allow (|θ̄| < 10⁻¹⁰). Two things are still owed: that
  dictionary, and a sector split (main's P-128) that keeps arg det M = 0 while giving J ≠ 0.
- **For δ_CKM, the bit reading fails the data.** δ_CKM is about 1.14 rad (65°), neither 0 nor π. So the CKM phase cannot be
  a bit of the weave. It must come from what splits the sectors, as W74 said.
- **If B2 fails,** the bit is not fixed on the weave, and box D's reading is a bit with no selected value.
- **The count stays 0 of 19** either way.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
