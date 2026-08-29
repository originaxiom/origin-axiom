# B1215 — THE CODEX TRANSCRIPT HARVEST: a registered theorem protected, four dishonest wrappers fixed, and a stalled lead carried one step

**Verdict**: `OPEN` · **2026-08-29** · **Gate 5 clean** · harvested from codex's working transcript
(owner-relayed), not from their commits alone

## LEG 1 — R022 does **not** refute B1182, and the boundary is worth pinning

Codex's transcript summarises R022 as *"abstract V₄ torsors agree, but the original three-way
field-labelled identification is **false**."* Read alone, that reads as a refutation of
**T-V4-TORSOR-IDENT** — a theorem this bench registered **hours earlier** (B1214). It is not one, and
the distinction is exact:

- **R022's negative is about branch vs being × hearing**: *"with field labels, branch vs
  being-×-hearing NOT label-preserving (√3 vs √5; ram {2,3} vs {3,5}); three-way claim ILL-TYPED
  until branch labels + measurement carrier frozen."*
- **B1182's theorem is about the √−3-internal pair**: the **frame** V₄ = ⟨c, r⟩ and the **branch**
  V₄ = Gal(ℚ(ζ₁₂)/ℚ). No being × hearing, no √5, no ramification at 5.

**Our own banked record settles it**, in B1175's charter-close text: *"C4 REFUTED-AS-STATED by the
author → **C4′** (the √−3-internal pair, R022's frozen-data spec; **being × hearing DROPPED**)."*
**B1182 is C4′ — the pair that survived after R022's negative removed the third leg.** The three-way
claim (OA-C1133) remains ill-typed and open; the two-way one is proved.

> Recorded because a reader of codex's summary — including a future one of ours — would otherwise
> conclude that a registered theorem had been refuted the same day it was registered.

## LEG 2 — their wrapper flag is real, and three of the four were mine from today

Codex reports *"several main reproduction wrappers silently fail under a dependency-poor system
Python."* Measured here: of **52** `reproduce.sh` wrappers, **4 printed REPRODUCES with no gate on
the computation's own output** — they assert success on the *process exiting 0*, not on the
computation asserting anything. **Three were written by this seat today** (B1210, B1211, B1213), in
the same session that banked B1207's lesson about instruments that cannot fail.

**The fourth is worse and is the real find.** `B1175/verification/reproduce.sh` **re-runs nothing at
all** — it echoes the harvest's conclusions and prints REPRODUCES. The certificates it describes live
on codex's branch and are not vendored, so the script *cannot* re-execute them, and it must not claim
to. It now prints **RECORD**, with the correction at the top of the file:

> *a reproducer that reproduces nothing is worse than no reproducer, because it answers the question
> it was never asked.*

The three gated wrappers now grep their own output for the computation's marker. **Ungated: 0.**

## LEG 3 — the stalled lead, carried one step

Codex's last finding before their quota ran out, uncertified by them:

> *"the tail-selection equation used for the quark leg cannot be copied unchanged to the lepton leg.
> For A₁₁ the required raw B-pair sum is 4 mod 12, not 8; the only pure-tail pair inside the physical
> B₂ sector is (2,2), and it vanishes by skewness."*

**Checkable from the height-308 spec's own numbers, without their frames — and it checks out.**

- The spec states the rule for the down leg as *ρ + σ ≡ 8 (mod 12)* with A₇. The invariant behind it
  is the **raw total**: the three raw characters (7, 6, 2) sum to **3 mod 12**, so
  **ρ + σ ≡ 3 − χ(A) (mod 12)**. That gives **8** for A₇ — reproducing the spec's own stated rule —
  and **4** for A₁₁. **The rule is not a constant, and cannot be copied between legs with different
  A-characters. Codex's correction to their own R024 is arithmetically right.**
- **The instrument is calibrated by the spec, not chosen**: a first pass allowed character 10 and
  produced a fourth A₇ pair (10,10) the spec does not list, so the tail alphabet runs 0…8 and the
  spec's three-pair list **(0,8), (2,6), (4,4)** is what pins it. On that alphabet the A₁₁ case gives
  **(0,4) and (2,2)** — and **(2,2) is repeated, so it vanishes by the same skewness that killed
  (4,4) in the down case.**

**Fenced, and the fence matters**: that the lepton leg *is* A₁₁ is a reading of codex's frames, which
are not on this bench and which **their own certificate leaves UNDETERMINED at the generation
level**. This cell verifies the **consequence** of that reading, not the reading.

> **Conditional consequence for B1208's fork**: *if* the lepton leg is A₁₁, its tail structure
> **differs** from the down leg's — evidence **against branch (a)** (same tensor) and toward (b) or
> (c). It does not decide between them: the connecting (non-tail) contributions are untouched.

## LEG 4 — their honest chain, adopted as an external reading

Codex states the SM chain in nine steps, and it is close enough to ours to be worth carrying as an
independent statement rather than paraphrasing: bare *"not nothing"* does not uniquely select a seed
independently of description language · Fibonacci is **conditional** on a restricted rule category ·
Fibonacci → oriented punctured-torus carrier **conditional** · **given m004, m004 → SL(2,𝔽₃) = 2T →
E₆ is proved** · E₆ supplies an exact SM-shaped skeleton, anomaly ratios and cubic support · **a
unique compact 4d QFT functor is not derived and unrestricted uniqueness is refuted** · the heterotic
construction is a conditional witness, **not an object-forced realization** · **three chiral
generations are not derived** · vacuum, spectrum, Yukawas, dynamics and normalized values remain
unclosed. Their summary: *"genuine structural mathematics, but not yet a parameter-free Standard
Model or TOE."*

**That is our position too**, and having it written by a hostile-audit seat is worth more to the paper
than writing it ourselves. Their canonical ledger now types **185 questions**: 70 PROVED, 55 REFUTED,
15 CONDITIONAL, 22 EXTERNAL_BLOCKER, 2 EMPIRICAL, **21 OPEN**.

## Carried, not actioned

Two further debts they name, neither verified here: the paper branch's *"112-member" verifier still
running its withdrawn 14-member census*, and outside scripts depending on floating git refs or
self-scanning growing files. **The first is cc3's to fix and is relayed; the second is cloud's.**
Their roadmap's top item — the characteristic-zero height-308 evaluator in five steps — matches the
ask this bench relayed, and is theirs to run.
