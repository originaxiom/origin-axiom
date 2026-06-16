# B156 — the Ω strict-full cone: positive-shear histories, the R/G family, and its invariants

**Date:** 2026-06-16. **Status:** six Ω theorems INDEPENDENTLY RE-DERIVED + adversarially verified — core R/G
algebra [proved], TC-2 reciprocity [proved], Fibonacci block-count [exact], history-entropy=log 2 [proved],
**TC-1** Ω₄ unique minimal seed [exact], **TC-4** orientation no-go [proved]; strict-full survivor counts
L4–L9 re-confirmed by two independent enumerators ([exact]), L10 re-run in progress (see `## Counts`). Scope
sharpened by the source-chat cross-check: **Ω is the abelianized shadow of the trace-map tower, not its
mechanism** (the strict-full shears commute — see `## Scope`). Standalone linear algebra / combinatorics /
symbolic dynamics; **no Origin-core claim, no physics**; proven core P1–P16 untouched. Nothing promotes to
`../../CLAIMS.md`. Ledger: V149 (+ V150 completion).

**Provenance.** This banks the **Ω-specific** content of a cross-session "Ω" history-enumeration program
(handoff `origin_axiom_handoff_2026-06-15`, gitignored working room `audit/handoff_2026-06-15/`) onto our
current main. Per verify-don't-trust, **every claim was independently re-derived here with fresh code** (not
the handoff's own scripts) before banking; a 4-claim verification workflow with adversarial skeptics
confirmed all four with high confidence and no refutation. The Ω program is the **SL(4) lift of our P6**
(SL(2) shears preserving a signature-(1,1) form); this is the same construction, dimension-lifted.

**B-number bridge.** The Ω branch uses its own internal numbering (B206…B907), preserved here as provenance;
it does **not** collide with our B1–B155 (different objects). The Ω "B206" golden×phase object is already
banked in our sequence as [`frontier/B155_golden_phase_bridge/`](../B155_golden_phase_bridge/) (V148); this
B156 banks the surrounding strict-full cone / R-G / entropy results.

## The object

Positive **elementary row-shears** `S_ij = I + E_ij` (row_i += row_j, i≠j) act on 4×4 integer matrices; a
**history** is a word in the 12 shears. A matrix is **strict-full** iff it admits a **nondegenerate**
symmetric `G` with `MᵀGM=G`. The explicit 2-parameter family is `R_{a,m} ∈ SL(4,ℤ)` with invariant form
`G_{a,m}`, wall coordinate `δ = 2a−1−m`; the shears `A=S₀₃: δ→δ+2` and `C=S₂₃: δ→δ−1` move between members.

## Results (each independently re-derived here; reproducers in this folder)

| # | result | tier | reproducer |
|---|---|---|---|
| 1 | **Core R/G algebra** | **[proved]** (symbolic, exact) | `omega_independent_verify.py` |
| 2 | **TC-2: strict-full ⟹ reciprocal char poly** | **[proved]** | `tc2_reciprocity_verify.py` |
| 3 | **Fibonacci block-count** | **[exact]** | `verify_fib_blocks.py` |
| 4 | **Wall-avoiding history entropy = log 2** | **[proved]** | `opus_wall_entropy_verify.py` |
| 5 | **Strict-full survivor counts L4–L10** | **[exact] L4–L9 (two methods); L10 re-run in progress** | `independent_recount.py` |
| 6 | **TC-1: Ω₄ is the unique minimal strict-full seed** | **[exact]** | `tc1_tc4_verify.py` |
| 7 | **TC-4: orientation no-go (zero net Pfaffian residual)** | **[proved]** | `tc1_tc4_verify.py` |

**1. Core R/G algebra.** For `R_{a,m}` and `G_{a,m}` (symbolic a,m, fresh sympy): `det R = 1`;
`charpoly(R) = x⁴ − a x³ + (2a−2m−4) x² − a x + 1` (palindromic, via Newton's identities `e=[a,2a−2m−4,a,1]`);
`RᵀGR = G`; `det G = −δ/(m+1)`; `S₀₃R = R_{a+1,m}` (δ→δ+2), `S₂₃R = R_{a,m+1}` (δ→δ−1); signature **(1,3)**
on the live cone `m≥0, δ≥1`, degenerating to `(1,2,1)` at the wall `δ=0` (null vector `((a−4)/2, −a/2, a, 1)`,
boundary char poly `(x+1)²(x²−(a+2)x+1)`), flipping to `(2,2)` for `δ<0`. Constant-(1,3) is **rigorous** (not
sampled): `det G < 0` on the convex live cone + a Sylvester pivot certificate `[−1, 2/(m+1), 1, −δ/(m+1)]`
whose only vanishing locus is the wall. 16/16 checks PASS.

**2. TC-2 (strict-full ⟹ reciprocal).** Clean linear algebra: `MᵀGM=G` with `G` invertible gives
`Mᵀ = G M⁻¹ G⁻¹`, so `M ~ M⁻¹`; similar matrices share a char poly, and the spectrum is closed under
`λ↦1/λ` — for `det M = 1` and even `n` the char poly is exactly palindromic. Re-derived symbolically
(generic `M,G` at n=4) + 8/8 strict-full SL(4,ℤ) shear-products palindromic + two non-reciprocal controls
that admit **no** nondegenerate invariant form (the contrapositive). The skeptic could not break it
(symplectic/skew, degenerate-G, and field-change attacks all failed).

> **verify-don't-trust correction (banked).** The handoff's exposition wrote the reversal identity as
> `xⁿ p_M(1/x) = (−1)ⁿ det(M) p_M(x)` and called it general — that is **circular** (it already assumes the
> theorem). The correct general identity is `xⁿ p_M(1/x) = (−1)ⁿ det(M) p_{M⁻¹}(x)`; it collapses to the
> handoff's form only after `M ~ M⁻¹`. Also: with `det M = 1`, odd `n` gives **anti**-palindromic, even `n`
> palindromic — the Ω sector is n=4 (even), so the Ω application is unaffected. The result stands; the
> intermediate step is now stated correctly.

**3. Fibonacci block-count.** The admissible block-words (the parse of strict-full histories into blocks) are
in bijection with compositions of `n` into parts `{1,2}`, so the count at length `n` is `F_{n+1}`: independent
enumeration (DP, brute, explicit, transfer-matrix) gives `1,1,2,3,5,8,13,21,34,55,89,144,233` for n=0..12,
matching the documented sequence; the transfer matrix has eigenvalues `(1±√5)/2`, spectral radius `φ`. The
block-word→shear-string map is injective with unique parse, so these count **distinct** histories. 21/21 PASS.

**4. Wall-avoiding history entropy = log 2.** The shears act on `δ` by `A:+2`, `C:−1`; "wall-avoiding"
histories keep `δ≥1`. The number `W_n(δ)` of length-n wall-avoiding `{A,C}` words has exponential rate
**exactly log 2**, by an exact mechanism (not just numerics): `log W_n − n·log 2` converges to a **bounded**
constant `= log(survival probability)`, and the survival probability solving the first-passage recurrence
(`p_d = ½p_{d+2} + ½p_{d−1}`, `p_0=1`; characteristic `r³−2r+1=0`, roots `{1, 1/φ, −φ}`) is exactly
`1 − φ^{−δ} > 0`. So `W_n(δ) ~ (1 − φ^{−δ})·2ⁿ ⟹ rate = log 2`. DP==brute through n=14, matches the handoff
wall-automaton tables through n=20; `W_{n+1}/W_n → 2` to 10 digits even for the closest-to-wall start.
(The history-entropy value `log 2` is the **final** one — it supersedes earlier lower bounds `log φ` from the
Fibonacci blocks and `(1/3)log 7` from length-3 blocks, both `< log 2`.)

**6. TC-1 — Ω₄ is the unique minimal strict-full seed.** The minimal level at which *any* strongly-connected
positive-shear history exists is `L=4` (a strongly connected digraph on 4 nodes needs ≥4 edges), and among
**all** strongly-connected `L=4` histories the strict-full ones have characteristic polynomial **exactly**
`x⁴−4x³+5x²−4x+1 = (4,5,4) = golden×phase` and nothing else (144 SC histories at L4; the strict-full subset is
the 96 with charpoly (4,5,4)). So the Ω₄ seed (= the `frontier/B155` golden×phase object) is the unique
minimal strict-full seed, and the whole survivor tower is rooted there. **[exact]**

**7. TC-4 — orientation no-go.** Define the orientation `Ω(w)` of a history as the Pfaffian of the
antisymmetrized dependency-count matrix `A_{ij}=C_{ij}−C_{ji}` (`Pf = A₀₁A₂₃ − A₀₂A₁₃ + A₀₃A₁₂`). Under a
relabeling `π` of the 4 nodes, `A ↦ PπAPπᵀ`, so `Ω(πw) = sign(π)·Ω(w)` (Pfaffian transforms by `det Pπ`),
while `M(πw) = PπM(w)Pπᵀ` preserves strong-connectivity and strict-fullness. Hence any relabel-closed
ensemble pairs each `w` (via an **odd** `π`) with a partner of opposite `Ω`, so the **net orientation residual
is 0** (verified: the sign law symbolically, ensemble closure on the L4 strict-full set, and net sum = 0 over
all SC histories at L4 and L5). Consequence: orientation residuals are **boundary-induced, not internally
derived** — this is the rigorous core of the "non-cancellation" motivation, stated as a *proved no-go*, not as
a physics claim. **[proved]**

## Scope: Ω is the abelianized shadow of the trace-map tower, NOT its mechanism

The Ω₄ seed is the same canonical golden×phase object reached from the character-variety side
([`frontier/B155`](../B155_golden_phase_bridge/)); the two programs **converge on a shared canonical object**.
But the stronger reading — "Ω *is* the figure-eight/metallic trace-map tower" — is **false as a mechanism**:
the two strict-full shears `A = S₀₃` and `C = S₂₃` **commute** (`E₀₃E₂₃ = E₂₃E₀₃ = 0 ⟹ AC = CA`), so the map
`R↦A, L↦C` *cannot* faithfully represent the **noncommutative** trace-map monodromy. (This is exactly why the
R-cone endpoint entropy is **0** — the endpoint depends only on the count of `C` moves, order-independent.) So
Ω is, at most, the **abelianized / non-collapse skeleton** of the tower. The open test — the **Ω↔tower bridge
audit** (never run): do the exact `R,L` trace-map relations get realized by any Ω generators? does the
Fricke–Vogt `κ` pull back to `δ` or `det G`? does `χ_Ω` specialize to the Dickson/Lucas factors of the tower?
— if those fail, Ω is **declared standalone**. (Recorded in `docs/OPEN_LEADS.md`.)

## Counts (strict-full survivors)

A **strict-full survivor** at level `L` = a length-L history that starts from an **Ω₄ seed** (strongly
connected, char poly `x⁴−4x³+5x²−4x+1` = golden×phase, strict-full at L4) and stays strict-full at **every**
level 4..L. The recursion is `survivors_L = strict-full subset of (survivors_{L−1} × 12 shears)`.

| L | strict-full survivors | endpoint matrices | re-run status |
|---|---|---|---|
| 4 | 96 | 36 | **[exact]** two methods (exact-`det`, no-shortcut + reciprocity-shortcut) |
| 5 | 672 | 240 | **[exact]** two methods |
| 6 | 3840 | 960 | **[exact]** two methods |
| 7 | 20928 | 3240 | **[exact]** two methods |
| 8 | 105312 | 9396 | **[exact]** re-run confirmed (independent state-propagation) |
| 9 | 521904 | 25536 | **[exact]** re-run confirmed (independent state-propagation) |
| 10 | 2488080 | 65472 | [artifact; independent re-run in progress] |

> **verify-don't-trust note.** The handoff's *own* brute-force script (`omega_reproduce_l4_l6.py`) attributes
> strict-full status **per char-poly class representative**, which **over-counts** (it reports L5=3120, L6=57792
> — wrong). The correct count is **per-matrix** (a class can mix full and non-full matrices). Our independent
> `independent_recount.py` uses an **exact** test ("∃ nondegenerate invariant form" ⟺ `det` of a generic
> member of `{G : MᵀGM=G}` is not the zero polynomial), with **no** reciprocity shortcut in the validation
> run, and reproduces the handoff's true counts 96/672/3840/20928 — re-confirming TC-2 as a side effect (every
> survivor is reciprocal). The L8–L10 re-run (heavy background job, reciprocity-shortcut, state-propagation
> over endpoint matrices) is in progress; counts above are the handoff artifact values (with SHA256 in the
> bundle) pending the independent re-run confirmation.

## Firewall — claim-boundary table (verbatim from the Ω handoff `B898–B907`)

| Claim | Status | Safe wording |
|---|---:|---|
| `R_{a,m} ∈ SL(4,Z)` | PROVED | Direct determinant identity. |
| `R^T G R = G` | PROVED | Explicit rational invariant symmetric form. |
| `det(G)=-δ/(m+1)` | PROVED | Exact collapse wall at `δ=0`. |
| Signature `(1,3)` on live cone | PROVED | Algebraic signature only. |
| Infinite positive strict-full branch | PROVED | `A^n R_{8,0}` suffices. |
| Wall-avoiding history entropy `log 2` | PROVED | Counts histories, not endpoints. |
| Endpoint entropy in restricted R-cone | PROVED ZERO | Endpoint depends only on number of `C` moves. |
| Full Ω endpoint entropy | OPEN | Finite growth observed, no all-depth proof. |
| Full Ω class entropy | OPEN | Finite growth observed, no all-depth proof. |
| U/V free semigroup | REFUTED | Relation appears at depth 7. |
| U/V positive endpoint entropy | OPEN | Growth data inconclusive. |
| Physical spacetime metric | FORBIDDEN | Not derived. |
| Physical entropy | FORBIDDEN | Not derived. |
| Gravity/QM/cosmology | FORBIDDEN | Not derived. |

**Firewall (restated):** signature (1,3) = **algebraic inertia** of a bilinear form, NOT spacetime/metric/time;
history entropy is **combinatorial** (a word-growth rate), NOT thermodynamic; the "non-cancellation"
motivation (the collapse wall `δ=0` ⟺ form degenerates) is firewalled motivation, not a derivation. Nothing
here touches `CLAIMS.md`. Novelty of the R/G/(1,3)/entropy package is **NEEDS-SPECIALIST** (the expert packet
`papers/omega_strict_full_note/` is the owner-send artifact; the AI literature scan de-risks, it does not
certify).

## Reproduction

`python` (pyenv, not sage) on each reproducer in this folder prints PASS:
`omega_independent_verify.py` (16 checks), `tc2_reciprocity_verify.py` (PART A–D), `verify_fib_blocks.py`
(21 checks), `opus_wall_entropy_verify.py` (entropy = log 2 + the survival mechanism), `tc1_tc4_verify.py`
(TC-1 minimal-seed uniqueness + TC-4 orientation no-go). The survivor counts:
`independent_recount.py --max-level 7` (L4–L7, exact, no shortcut) and
`independent_recount.py --recip-shortcut --max-level 10` (the L8–L10 re-run; L8/L9 confirmed = 105312/521904,
L10 in progress).

## Provenance note (the source reasoning)

The cross-session ChatGPT/Ω chat that produced this work (which itself ingested the ~1085pp Claude trace —
the two chats cross-examined each other) was digested as a cross-check (gitignored
`audit/handoff_2026-06-15/chatgpt_omega_transcripts/`). It confirmed every banked claim, fixed the entropy
value to its final `log 2` (older drafts used `(1/3)log 7`), surfaced TC-1/TC-4 (now banked), and produced the
collaboration's concluding verdict — the commuting-shears scope above (Ω is the abelianized shadow, not the
tower mechanism). Verify-don't-trust: all of TC-1/TC-4 were re-derived here, not transcribed.
