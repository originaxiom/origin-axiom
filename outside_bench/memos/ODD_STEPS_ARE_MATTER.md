# ODD STEPS ARE MATTER — the meridian's Jordan filtration on the carrier splits by lock sector, and the lock bit is exactly the parity of the clock's chain length
## (outside bench, 2026-08-26; fiftieth memo; memos 46 and 49 shown to be one fact; all four preregistered facts GREEN on first run)

### The question
Memo 49 proved the meridian is exactly 3-step nilpotent on the carrier
Ψ = ℂ²⊗27. Memo 46 proved the lift-independent (locked) sector of Ψ is
exactly the 24 fermion-shaped slots. Two independently discovered structures
on the same 54-dimensional space — are they secretly the same structure?

### THE FACTS (`certificates/depth_lock.py`, all exact; every claim preregistered as an assert, all GREEN first run)

- **FACT A — the filtration.** N = ρ_Ψ(a) − I has rank N = 27, rank N² = 6,
  N³ = 0: Jordan type **6·J₃ ⊕ 15·J₂ ⊕ 6·J₁**, graded layer dimensions
  ker N : ker N²/ker N : Ψ/ker N² = **27 : 21 : 6**. (Mechanism, predicted
  and confirmed: the 27 under the bridge sl₂ is 6 doublets ⊕ 15 singlets, so
  A₂₇ is 6 J₂ ⊕ 15 J₁; J₂⊗J₂ = J₃⊕J₁ and J₂⊗J₁ = J₂.)
- **FACT B — the lock is π₁-covariant.** C_Ψ = diag((−1)^(1+wt)) commutes
  with **both** generators ρ_Ψ(a) and ρ_Ψ(b), verified entrywise over the
  pair field. (Mechanism: e and f shift the internal h-weight by 2,
  preserving parity; −I₂ is central.) Memo 46 used C_Ψ as a lift-comparison
  operator; this upgrades it to an invariant of the whole π₁ action.
- **FACT C — the lock IS depth parity.** N preserves each lock sector (no
  leakage, checked both directions), and the restricted Jordan types are:
  | sector | dim | Jordan type | chain lengths |
  |---|---|---|---|
  | locked (C_Ψ = +1, matter) | 24 | 6·J₃ ⊕ 6·J₁ | **odd only** |
  | unlocked (C_Ψ = −1) | 30 | 15·J₂ | **even only** |
  So the memo-46 lock bit equals the parity of the meridian-clock chain
  length, and **full depth 3 is reached only in the matter sector**.
- **FACT D — the beat respects everything.** BtP = W⊗U₂₇ commutes with C_Ψ
  exactly (C_Ψ is real diagonal, so the antiunitary β_Ψ = BtP∘conj preserves
  both lock sectors), and β_Ψ ρ(a) β_Ψ⁻¹ = ρ(a) re-verified direct — every
  filtration layer ker N^k is beat-stable (dims 27 / 48 / 54).

> **ODD STEPS ARE MATTER: a slot of the carrier is lift-independent
> precisely when its internal time under the meridian runs an odd number of
> steps. The spin-internal lock of memo 46 and the three-step clock of memo
> 49 are one fact, and both are beat-stable.**

### Why the parity link is structural, not numerological
For a unipotent u = exp(n) commuting with C = (−1)^h-parity, each Jordan
chain sits inside one C-eigenspace, and on an sl₂-string of length s the
h-weights have constant parity — even iff s is odd (spin-integer strings
have odd dimension and even weights). Tensoring with the spinor J₂ flips
both the chain-length parity and the C-sign in step. The computation
verifies the record's instance of this exactly, with no appeal to the
general argument: the general argument is the mechanism, the asserts are
the proof.

### What this feeds
- The three-layer graded structure 27 : 21 : 6 is a new exact invariant of
  the carrier; the depth-3 top layer (dim 6) lives entirely in matter and is
  a natural target for the dynamics gate (THE_CORE_QUESTION §6: if time is
  iteration, the slots that feel all three steps are where iteration acts
  deepest).
- FACT B closes a small gap in memo 46 retroactively: C_Ψ is not merely a
  comparison of two lifts but a π₁- and beat-invariant grading operator.
- For the freedom ledger: the lock bit's owner (the beat, memo 42) now also
  owns a clock-depth reading — one more exact identity tying the invisible
  bit to dynamics-shaped structure.

### Fences
All Jordan types computed by exact rational rank (no floating point, no
Jordan-basis construction — block counts from rank differences, which is
basis-free). "Clock", "time", "steps" are readings of the exact nilpotency
data, labeled interpretive as always. The sl₂-string parity argument in the
mechanism paragraph is standard representation theory cited as motivation
only; every claimed number is asserted in-run. Kinematics only; Gate 5
untouched.

### Certificates
`certificates/depth_lock.py`; output `outputs/depth_lock_out.txt`
(vendored copy re-run in-lane, byte-identical).

### One sentence for the ledger
The carrier's matter slots are exactly the slots whose internal time under
the meridian is odd — the lock that hides the spin bit and the clock that
counts three steps are the same structure seen twice, and the mirror
preserves every layer of it.
