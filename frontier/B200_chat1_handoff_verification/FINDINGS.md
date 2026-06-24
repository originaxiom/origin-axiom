# B200 — verification of the chat1 (2026-06-24) independent-computation handoff

**Date:** 2026-06-24. **Status:** a cross-session (chat1) handoff of three "MATH" results + one
speculative framing, **re-derived before banking** (verify-don't-trust; cf. B197 for the chat2 analog). Verdicts:
**R2 VERIFIED + banked** (one new, correct increment); **R1 REFUTED** (a tautology / out-of-regime claim — caught,
recorded so it is not re-proposed); **R3 standard ETH** (not banked; its specific numbers did not even reproduce in a
quick check); the **"not nothing" ladder** stays **firewalled** (POSTULATED, known results, selection-bias deflation).
Standalone condensed-matter / symbolic-dynamics math; **no physics claim; nothing to `CLAIMS.md`; P1–P16 untouched.**
Ledger V193.

## R2 — on-site is the unique finite-range interaction preserving the Sturmian alphabet **[VERIFIED, banked]**

For the Fibonacci chain (potential `V∈{0,1}` on the word `a→ab, b→a`), an interaction at range `d` makes a bound
composite see the **paired** potential `V_n + V_{n+d}`. Re-derived (own enumerator, F-word to length 987):

| `d` | paired values | subword complexity `p(1..5)` | Sturmian? |
|---|---|---|---|
| **0 (on-site)** | 2 (unchanged) | `2,3,4,5,6` (= `L+1`) | **YES** |
| 1 (NN) | 2 (`bb` never occurs) | `2,3,4,`**`6`**`,7` | **NO** (breaks at `L=4`) |
| 2 (NNN) | 3 | — | NO (3 letters) |

The NN paired sequence has only 2 values yet `p(4)=6>5`, so it is **not Sturmian**; its letter ratio ≈ **3.27**
(neither `φ` nor `φ²`). **Structural reason** (general, not just d≤2): on-site acts on *single* sites, so the composite
sees the same site sequence; any `d≥1` makes it see *pairs*, whose sequence carries correlations the substitution does
not control → higher complexity. So **on-site is the unique finite-range interaction preserving the two-letter
Sturmian structure.** A new, correct angle (the repo uses Sturmian 36× but never tested interaction-selection by
complexity); refines `K019` (collective metallic spectrum) and the B171–B176 interaction frontier. **Tier `[num /
combinatorial]`.** *Honest scope:* this preserves the *alphabet / complexity* (a proxy for "metallic-preserving"); the
full spectral consequence (same Cantor structure for the composite) is a further step, not claimed here.

## R1 — "κ₁=κ₂=3 at U=t" (the doublon is a single-particle replica) **[REFUTED]**

The claim used the doublon hopping `t_eff = 2t²/U` (2nd-order perturbation theory) → `λ_eff = VU/t² = λ_single` at
`U=t`. **Two fatal problems, both re-derived:**

1. **Out of regime.** `t_eff = 2t²/U` is a **strong-coupling (U≫t)** result. At `U=t` it gives `t_eff = 2t` — a "bound
   pair" *more mobile than a single particle*. A genuine 2-body Hubbard ED on the Fibonacci chain (1↑1↓, N=13) shows
   the prediction fails precisely at `U=t` and works only at `U≫t`:

   | U | `t_eff` | doublon band-gap below | RMS(true 2-body band vs the `t_eff` prediction) |
   |---|---|---|---|
   | **U=t=1** | **2.0** | **0.05** (no band) | **3.77** ✗ |
   | U=5 | 0.40 | 0.69 | 0.70 |
   | U=20 | 0.10 | 15.4 | 0.19 ✓ |

2. **Circular "verification."** The handoff's "RMS=0" compared the *effective model* (a Fibonacci chain built with
   `λ_eff`) to the single particle — but at `U=t`, `λ_eff = λ_single` **by construction**, so it is the *same chain*
   rescaled → RMS=0 **tautologically**. It never tested the true doublon (which, as above, does **not** match).

So the "exact one-step structural fixed point at `U=t`" is **vacuous**: the bare identity `λ_eff=VU/t²=V/t at U=t` is
just where an out-of-regime formula's ratio crosses 1. The "interaction-level analogue of the golden ratio" framing is
**unsupported**. Recorded REFUTED so it is not re-proposed. *(This is a verify-don't-trust catch: a claimed numerical
verification that was circular.)*

## R3 — many-body filling thermalizes (Poisson→GOE) **[STANDARD ETH; not banked]**

The handoff concedes this is textbook eigenstate-thermalization, finite-size (13 sites). A quick independent
level-spacing check (spinless fermions, N=13) did **not** reproduce the specific signature — `⟨r⟩` at M=1 came out
**0.64** (not Poisson ≈0.386) and 0.56 at M=2 — i.e. the numbers are setup/finite-size-sensitive. So R3 is recorded as
a known textbook phenomenon, **not banked** as a result; its only content is the (already-held) framing that the
single unit's form is robust only at one body (cf. B183 for the open-system route).

## Speculation — the "not nothing" ladder **[FIREWALLED, POSTULATED]**

A framing collecting *known* physics results (anomaly factorization `(y+4x)(y−2x)=0`; `N_g=3` from CP violation; `m_t`
from vacuum stability, Degrassi 2012; the Weinberg `Λ` bound) as instances of "minimal nontrivial solution at a
consistency boundary." The handoff is honest that **none are our discoveries**, the unifying interpretation is a thesis,
and there may be **selection bias** (we only observe viable, near-boundary values). "not nothing" already appears in 7
repo files; the `det(Sym^{n−1}[A,B])=1` "form ceiling" is textbook (implicit in `K012`). **Kept behind the firewall**
(motivational only); **nothing to `CLAIMS.md`**, no physics content promoted.

## Net

Of the three incoming "MATH" results, **only R2 survives** as a new, verified, bankable increment; **R1 is refuted**
(circular + out-of-regime), **R3 is standard** (and didn't reproduce cleanly), the speculation stays firewalled. The
chat1 handoff was valuable mainly for R2 and as another verify-don't-trust exercise.

## Reproduction
`python sturmian_interaction.py` (pyenv) → `ALL CHECKS PASS` (R2 complexity; R1 the 2-body ED refutation table; R3
report-only). Fast lock: `tests/test_b200_chat1_handoff_verification.py` (R2 + the R1 refutation, 2 passed).
