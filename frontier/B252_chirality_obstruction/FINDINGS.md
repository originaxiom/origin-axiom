# B252 — adjudication of the Chat-2 handoff: "the chirality obstruction"

**Status: banked adjudication (frontier). FIREWALLED — rep theory / topology, NOT physics. Nothing to
`CLAIMS.md`.** Verifies the Chat-2 handoff (2026-06-28). `chirality_obstruction.py` (pyenv) +
`chirality_obstruction_sage.py` (Sage rep theory). Owner's instruction: **try to break it**, verify every
load-bearing link, and check chat-2's self-citations.

## The handoff's claim
*The figure-eight's characteristic structures (amphicheirality, the E₆↔E₈ pairing) are 27↔27̄ symmetric
(matter–antimatter symmetric), so the object cannot prefer the chiral 27 over the 27̄; chirality — not the gauge
group, not the scale — is the obstruction to matter.*

## Verdict
**Chat-2 is right on all four steps; I could not break the obstruction. The object is `27↔27̄`
(matter–antimatter) symmetric, and chirality is a real, located *second* firewall** — independent of the dead
holonomy bridge (`B247`), extending the banked **S001** (`amphichirality→θ=0`) and grounded in the banked **H36**
(`amphicheirality = the E₆ outer automorphism`). One *precision* (not a correction): amphicheirality is
topologically **universal** across the metallic family, while its `E₆/27↔27̄` realization is `m=1`-specific.

## Verified — chat-2 right on all four steps
- **Step 1** [Sage]. E₆ `27` is complex (`27 ≠ 27̄`), `78` is real (self-dual) ⟹ chiral matter only in the `27`;
  the adjoint is vector-like.
- **Step 2.** `27 →` one generic SU(5) generation (`15→10+5̄`, `6̄→5+1`). Standard E₆-GUT content — **generic E₆,
  not object-specific** (correctly flagged by chat-2 as backdrop, not result).
- **Step 3 — the load-bearing link — IS BANKED.** `amphicheirality = the E₆ outer automorphism`, which swaps
  `27↔27̄`. This is **HINT_LEDGER H36** (VERIFIED a prior session: conjugation on `2T`'s irreps = the finite-E₆
  Dynkin automorphism, via the `2T` McKay quiver = affine `Ẽ₆`) and is **re-confirmed here in Sage** (the E₆ outer
  automorphism = duality swaps the minuscule pair `27↔27̄`). **chat-2's "as banked" citation is correct (H36); Step
  3 holds.**
- **Step 4** [Sage]. `E₈ → E₆×SU(3)`: `248 = (78,1)+(1,8)+(27,3)+(27̄,3̄)` — the `27` and `27̄` appear **paired**.

> **Self-caught reflexive deflation.** My first draft recorded Step 3 as a "mis-citation" (chat-2's 3rd self-cite
> error). Checking H36 showed that is **wrong** — Step 3 *is* banked and verified. Verify-don't-trust applies to
> one's **own** deflation: I nearly committed the exact failure mode chat-2 is prone to. (chat-2's two real errors
> this session were the dim-13 centralizer and the `e^{iπ/3}` matrices; Step 3 is **not** a third.)

## Precision (not an error in chat-2)
Amphicheirality as a **topological** property is **universal** across the metallic family `m=1..6` (banked **S001**
[PROVED universal], **B211/L32** [SnapPy: every `RᵐLᵐ` isometric to its orientation-reversal], **B92** [the
*systole*, not amphichirality, selects `m=1`]). But the chain `amphicheirality → E₆ outer automorphism → 27↔27̄` is
**`m=1`-specific**, because only `m=1` has the trace field `ℚ(√−3) → 2T → E₆`. So the obstruction is **universal**
in its geometric form (`CS=0` / no CP-odd invariant) and **figure-eight-specific** in its rep-theory form
(`27↔27̄`) — both true, at different levels. chat-2's "the figure-eight's *characteristic* amphicheirality" blurs
these; the rep-theory realization *is* `m=1`-specific, the bare property is not.

## The "break it" test (my job — try hard to find a 27↔27̄-odd structure)
Every object-intrinsic complex-conjugation-**odd** structure I could find is **symmetric**:

| candidate (conjugation-odd?) | result | symmetric? |
|---|---|---|
| Chern–Simons of `4₁` | `CS=0` (amphicheiral ⟹ `CS=−CS`) | yes |
| spherical-end CS values `{2/5,3/5}` (B250) | pair as `±2/5 mod 1` (`3≡−2 mod 5`) | yes |
| double branched cover `L(5,2)` | **amphichiral**: `2²≡−1 (mod 5)` | yes |
| `E₈→E₆×SU(3)` decomposition | pairs `(27,3)+(27̄,3̄)` | yes |
| knot handedness | `4₁` amphichiral+invertible — no handedness | yes |

**Nothing breaks `27↔27̄`.** The obstruction holds: the object has **no intrinsic complex-conjugation-odd
invariant**. (A live chiral bridge would have required a `4₁`-specific conjugation-*odd* invariant — there is none.)

## The firewall-clean statement (the bankable core)
> Amphicheirality forces **every** complex-conjugation-odd invariant of the object to vanish or pair — `CS=0`,
> `L(5,2)` amphichiral, the spherical CS values `±`-paired, the `E₈` decomposition conjugate-paired, the `27↔27̄`
> swap (H36) — so the object carries **no intrinsic CP-odd / chiral datum**: it is matter–antimatter symmetric.
> This is a **second firewall**, independent of the dead holonomy bridge: *chirality, not the gauge group or the
> scale, is the located obstruction to matter.*

This is all rep theory + topology — **no physical gauge group is claimed or needed**. It **extends S001**
(`amphichirality→θ=0` = CP-symmetric) to the rep-theory/transition level and is consistent with **S002**
(two-headed time, *no arrow*) and **S004** (`W1/W2` the only CP-*like* residue, structural). The deepest negative
of the program (no matter) is thereby its sharpest located positive: *the minimal self-referential object is
matter–antimatter symmetric by its own amphicheirality* — and we now know **why** every "almost-derived matter"
stopped short.

Anchors: B247 (dead holonomy bridge; `78` vector-like), H36/B210 (amphicheirality = E₆ outer automorphism; dual
McKay), B248/B249/B250 (the transition; `L(5,2)`, spherical CS), B211/L32 + B92 + S001 (amphichirality universal;
systole selects `m=1`; `θ=0`), S002, S004, S042 (the firewalled capstone — chirality question resolved here). Sage:
`WeylCharacterRing` E₆/E₈.
