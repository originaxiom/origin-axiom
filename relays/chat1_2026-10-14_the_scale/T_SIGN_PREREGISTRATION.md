# T-SIGN: is the CP bit of an amphichiral thread the sign of its monodromy? (chat1, 2026-10-14). Sealed before any code.

**Why.**
- B1224 and B1226: amphichirality forces CS ∈ {0, ¼} (SnapPy's chern_simons units; 0 or π²/2 in complex_volume units),
  not CS = 0. m003 sits at ¼.
- L192 (OPEN ★★★) asks whether the object's ℤ/2 fixes the CP-conservation bit. I-18 identifies the CS 2-torsion with
  θ̄ ∈ {0, π}, and is UNEARNED.
- chat1's post hoc read-out today (`post_hoc_cp_bit.json`): on the positive weave to length 18, all 514 swap-symmetric
  threads sit at CS = 0, none at ¼, and no chiral thread sits at 0 or ¼.
- The plumbing check before this seal: b+-LR identifies as m003, a minus thread, with complex-volume CS = 4.934802 =
  π²/2. GM5d (the owner's ruling) keeps the minus threads outside the weave.
- **The question.** Is the bit the sign of the monodromy, so that the positivity ruling is exactly the bit-zero choice?

**Instrument.** SnapPy 3.3.2. Minus thread: `Manifold('b+-' + W)` (monodromy −W). Plus thread: `b++W`. CS is Im
`complex_volume()` mod π², in (−π²/2, π²/2]. Tolerance 1e-6.

| | prediction | prior |
|---|---|---|
| N0 (control) | b+-LR = m003 with CS = ±π²/2; every b+-W for the words below builds, is orientable, and solves geometrically | 95% |
| N1 | every swap-symmetric Lyndon word W of length ≤ 14 has CS(b+-W) = ±π²/2: the bit is ¼ on every amphichiral minus thread | 75% |
| N2 | for every Lyndon word W of length ≤ 10, CS(b+-W) − CS(b++W) ≡ π²/2 (mod π²): the sign shifts CS by exactly ¼ | 45% |

**Read-outs.** The volumes of b+-W against b++W, and any exceptions.

**What it means, fenced.**
- If N1 holds, the CP bit on the amphichiral threads is the sign of the monodromy, to length 14. The positivity ruling
  (GM5d) is then exactly the choice of bit 0.
- Whether the bit is θ̄ is I-18, UNEARNED, and this check does not touch it. 0 of 19.
