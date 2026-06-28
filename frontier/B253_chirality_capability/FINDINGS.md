# B253 — adjudication of the Chat-2 handoff: "the chirality REDUCTION"

**Status: banked adjudication (frontier). Part A is firewall-clean rep theory; Part B is firewalled. Nothing to
`CLAIMS.md`.** Verifies the Chat-2 handoff (2026-06-28, the follow-up to the B252 obstruction).
`chirality_capability.py` (pyenv) + `chirality_capability_sage.py` (Sage). Owner's standing instruction: be brave
but **break it**; verify every link including chat-2's self-corrections; verify-don't-trust on my own deflations too.

## Verdict (one line)
**Part A is real and bankable; chat-2's correction of its own prior claim is valid and adopted; Part B's "decidable
reduction" is overstated — it is a firewalled speculation, not decidable from the object.**

## Part A — bankable, firewall-clean (Sage-verified)
A gauge group supports chiral matter **iff** it has a **complex** (non-self-dual) representation. Verified:

| end (B248) | group | `|Out|` | min rep | reality | complex-rep-capable |
|---|---|---|---|---|---|
| hyperbolic `ℚ(√−3)` | **E₆** | 2 | 27 | **complex** | **yes** |
| spherical `ℚ(√5)` | **E₈** | 1 | 248 (adjoint) | real | no |
| (Niven-excluded, B249) | E₇ | 1 | 56 | pseudoreal | no |

**The object-specific observation (via B248):** the figure-eight's geometric transition runs from the
complex-rep-capable end (E₆, hyperbolic) to the no-complex-rep end (E₈, spherical) — *the "chirality axis" (in the
4d-GUT reading) coincides with the B248 transition axis*, and E₇ (also no complex rep) is independently Niven-excluded
(B249), consistent. This is firewall-clean: a statement about the abstract McKay-label groups, asserting **no**
physics. (The word "chirality" is the firewalled gloss; the banked content is *complex-representation capability*.)

## The correction chat-2 owes (valid — adopted, refines B252)
B252 wrote that the object "**cannot source** a matter–antimatter asymmetry." **Too strong.** Amphicheirality gives
the `27↔27̄` swap as an *explicit* (representation-theory) symmetry; a theory with an explicit symmetry can still
produce asymmetry by **spontaneously breaking** it. Precise, defensible statement (B252 core, retained): the object
has **no explicit CP-odd datum**; any asymmetry would arise by spontaneous breaking of the amphicheiral involution
`τ`, which needs **dynamics** (a potential, vacua) — *external* to the object (firewall `K018`). This fits the
**S040** thesis exactly: *the object supplies the symmetric seed; the world supplies the breaking.* B252's FINDINGS
is updated accordingly.

## Part B — the "reduction" (firewalled, not object-decidable)
The dichotomy is logically clean — `τ` gauged ⟹ `27/27̄` identified ⟹ vector-like ⟹ non-chiral; `τ` global + SSB ⟹
two mirror vacua, each chiral (a Left–Right structure, "amphicheirality as the *origin* of chirality"). But it is
**not decidable from the object**, for three independent reasons:

1. **3d, not 4d.** The 3d-3d correspondence (`K006`) gives `T[4₁]` a **3d** N=2 theory (6d on a 3-manifold). 4d
   chirality (Weyl fermions, a 4d E₆ GUT's 27, Left–Right models) is a 4d notion; class-S (4d) needs a *2*-manifold,
   not the 3-manifold `4₁`. **4d chirality is not an observable of the object's licensed theory.**
2. **E₆ is a McKay label, not a 4d gauge group** (`B247`). There is no dynamical 27 to be chiral or vector-like.
3. **gauging `τ` is a model-building choice; SSB needs dynamics** the firewall (`K018`) says the object does not
   supply. So gauged-vs-global-and-broken is not object-determined.

**The proposed cheap discriminator (Chern–Simons) is inconclusive here.** `τ` reverses orientation ⟹ acts by
`CS → −CS`; the figure-eight has `CS=0` (B250), so `τ` is **anomaly-free / gaugeable** — but *gaugeable ≠ gauged*,
and `CS=0` leaves **both** branches open. It would be decisive only if `CS≠0` (obstructing the gauging ⟹ forcing
`τ` global). So branch (b) ("amphicheirality as the origin of chirality") is a **legitimate firewalled reading**
(consistent with S040: symmetric seed + external breaking) — recorded in `S042` — **not** a bankable or
object-decidable reduction.

## Honesty notes
- I **tried to break Part A** (looked for a complex rep of E₈ / a self-dual obstruction to E₆'s 27) — it holds; it
  is standard and Sage-confirmed.
- I **checked chat-2's self-correction** rather than inheriting it: the correction (explicit symmetry ≠ no
  asymmetry) is logically sound and genuinely refines B252; I adopted it. (Last turn I nearly *over*-deflated B252's
  Step 3; this turn the risk was the opposite — rubber-stamping a brave reopening. Both are caught by the same rule:
  compute the claim.)
- The net firewall position is unchanged and *better located*: the object is explicitly CP-symmetric (no explicit
  chiral datum), gives a 3d theory, and supplies no dynamics — so any chirality is external, exactly like the scale.

Anchors: B247 (dead bridge), B248/B249/B250 (the transition; CS=0), B252 (the obstruction — refined here), H36/B210
(amphicheirality = E₆ outer automorphism; dual McKay), K006 (3d-3d ⟹ 3d, not 4d), K018 (firewall: no dynamics/scale),
S040 (symmetric seed + external breaking), S042 (the firewalled capstone — branch b recorded). Sage: `WeylCharacterRing`.
