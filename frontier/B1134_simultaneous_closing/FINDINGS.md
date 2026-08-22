# B1134 — THE SIMULTANEOUS CLOSING: one conjugation buys so(3,1) AND compact su(3), forced into the object's own M(𝕆,ℂ)

**Status: banked (frontier). Verdict PROVED (the MATH: a single involution realizes
Lorentz signature and compact color together, and every such realization lands in
E₆(−26)=EIV=M(𝕆,ℂ)). Harvest arc — the cloud seat's tenth memo THE SIMULTANEOUS CLOSING
(golden_gate commit `3e65114`, Fable-5 session), verified TWO-BENCH: the cloud seat's
canonical sweep + THIS bench's fully independent re-derivation (own slot-swapper search,
own GF(2) sign-lift solver, own signature/character machinery; only the banked-and-locked
Chevalley e₆ of B1102 is shared, imported not rebuilt). Cloud seat credited. The MATH is
confirmed exact; ONE novelty over-claim is corrected and fenced below. Gate 5 untouched.
Lock `tests/test_b1134_simultaneous_closing.py`.**

## The question (the open question B1114 itself flagged)

Two banked halves of the observer's real-structure closing sat side by side, apparently
mutually exclusive:

- **B1114 (Lorentz):** so(3,1) ≅ sl(2,ℂ)_ℝ exists only when the antilinear real structure
  **SWAPS** the two same-class sl₂ triples (hatch ↔ I₁). B1114's own real-form fence:
  the Lorentz pair's realized host is E₆(2) or E₆(6) split — *"neither gives COMPACT
  (physical) color… Realizing the Lorentz pair with compact color is the open
  𝔽₂-kernel-sweep question (B1119's C-AR1)."*
- **B1127 (compact color):** compact su(3) color (0,8) was reached only in the
  antipodal/identity-on-color class, landing in E₆(−26) — a **different real form** from
  B1114's Lorentz host, with the simultaneous Lorentz status never established.

Read jointly: signature and color-compactness looked like they could not be bought by the
same conjugation. Either the observer needs two separate real structures, or a family had
been missed. **B1114 left this explicitly open.** This arc closes it.

## THE THEOREM (verified exact, two-bench)

> **There is a single involution θ (dressed with the observer's antilinear conjugation τ
> at ∞) on e₆ that realizes Lorentz so(3,1) AND compact su(3) color simultaneously — and
> EVERY such realization has global character −26, i.e. lands in E₆(−26) = EIV = M(𝕆,ℂ),
> the object's own magic-square algebra (B882/B904).**

Sweeping the **48** involutive slot-swappers of Aut(Φ(E₆)) = W(E₆) ∪ δW(E₆) [24 in W,
24 in δW] — those that swap the two triple-carrying A₂'s (hatch, I₁) while preserving the
color A₂ (I₂) setwise — against all involutive signed Chevalley lifts (𝔽₂-exhaustive):

- **480 (swapper, lift) pairs**; color-signature histogram **(4,4):216, (5,3):240,
  (0,8):24**; every pair passes θ²=I and a 40-trial automorphism spot-check.
- **All 24 (0,8) hits:** global character **−26**, double **(3,3)** = so(3,1), θ²=I;
  a representative passes the FULL 3003-pair Chevalley-bracket automorphism check with
  **0 failures**.
- **A clean bijection (bonus, not in the memo):** (4,4) ⟺ χ=+6, (5,3) ⟺ χ=+2,
  **(0,8) ⟺ χ=−26**, always. Color compactness and the M(𝕆,ℂ) host are the same fact.

So the observer's *entire* real-structure bill — signature **and** color compactness — is
**one conjugation**, and that conjugation is **forced into the object's own algebra**. Only
τ (the conjugation at ∞) is the observer's; the linear part θ is an integral Chevalley-
lattice automorphism (B1127's framing fence stands: the object's own arithmetic mirror is
trivial on the ℚ-rational color layer, so the compactifier τ is the observer's generic
conjugation — into the object's own M(𝕆,ℂ) form).

## THE INDEPENDENT VERIFICATION (this bench, own code)

Own script `verify_simul_closing.py` (imports only B1102's vendored e₆; everything else
freshly authored), full run in `b1134_run.log`, results pinned in `b1134_results.json`:

- **Tasks 1–5 CONFIRMED exact:** 48 slot-swappers (own BFS closure of |W(E₆)|=51840 + own
  brute-force diagram-automorphism search, δ=(5,1,4,3,2,0) independently matching B1125's
  stated "0↔5, 2↔4, fix 1,3"); the histogram; χ=−26 / (3,3) / θ²=I on all 24 hits; the
  full 3003-bracket automorphism on a representative; all three controls (antipodal →
  χ=−78, color (0,8), so(3,1)-double 0, BOTH 0; permute → χ=+6, (4,4); mixed → χ=+2, (5,3)).
- **Solver validated on the control:** 64 = 2⁶ involutive sign solutions recovered on the
  antipodal control (NOT collapsed to 1/64), by a genuine reduced-row-echelon GF(2) solve
  with no separate back-substitution pass — structurally avoiding the exact ordering-bug
  class the cloud seat caught (its error #15); cross-checked by a second independent
  GF(2)-rank computation (nullity 6, agrees).
- **Checksum clean:** every character across all 560 θ-evaluations fell inside the five-
  real-form set {+6, +2, −14, −26, −78}, and all five were witnessed — zero instrument
  breaks (B1119's classification-theorem-as-checksum discipline).
- **Own bugs caught en route (reported faithfully):** (1) a first ad-invariance check
  iterated `combinations(78,3)` and silently always placed a Cartan element in the
  distinguished slot, so both sign conventions spuriously passed — fixed by ranging x over
  all 78 basis vectors (234,234 triples; the −1 convention passes all, +1 fails 252);
  (2) a false premise that A₂'s longest element is independent of the simple pair used to
  build it (false for S₃) — dropped, replaced by a direct property check.

## THE NOVELTY FENCE (the one correction — integrate the math, correct the framing)

The memo's phrase *"precisely the family neither swept torsor contained"* **overstates by
4 of 24.** Element-by-element (exact permutation-tuple membership, not aggregate):

- The winning hits come from **6 distinct swapper elements.** **One of them, NEG∘π_mirror,
  is already in B1127's swept torsor** — its 4 (0,8) hits **exactly match B1127's stored
  `genuine_torsor_compact_hits`** (same character −26, same color (0,8), same 4-solution
  bit-structure). B1127 implicitly already contained the simultaneous closing on these 4;
  it simply never checked the Lorentz swap on those elements.
- The **remaining 20 of 24 hits, from 5 distinct swapper elements**, are **genuinely
  outside** both B1125's and B1127's swept torsors (confirmed by exact non-membership).

So the truth is *stronger* than the memo's framing, not weaker: the simultaneous closing is
reachable from **multiple independent directions**, all landing in E₆(−26). Also minor: the
memo's "nontrivial reflection" is loose shorthand — all 6 hit-generating swappers act
**fixed-point-freely** on the color A₂ (0/6 roots fixed), none is a literal 2-root
reflection.

## What it settles — and what it does NOT

**SETTLED (structure):** the observer's real-structure closing is a *single* rigid act, and
it is forced into the object's own M(𝕆,ℂ). B1114's open question (Lorentz + compact color
together) is closed; B1114's "signature is the observer's" and B1127's "compact color is
the observer's" are hereby exhibited as **the same closing**.

**NOT settled, and NOT claimed (values):** this is a structural theorem — it produces **no
Standard-Model number**, and the banked period-disjointness (V-3/B1126, the value-probe
wave B1128–B1133) is untouched. What it does *for* values is sharpen the one open door
(values-as-regulators, not periods): the physical real form is now *forced* to
E₆(−26)=J₃(𝕆), collapsing the observer's real-structure freedom to one act; and the 24
hits leave **64 fixed dimensions** where hypercharge and 27-reality would organize — the
natural, finite, untested value target. That is a **firewalled hypothesis**, computed
nowhere yet, and it is the natural next cell (relayed).

## Credit + relay

The result is the **cloud seat's** (tenth memo, golden_gate `3e65114`). Integrated here
under B1134 per integrate-don't-merge, re-derived independently before banking. Relayed
back to the cloud seat (via this FINDINGS + the commit message, which the seat monitors):
the novelty is **20/24 genuinely new + 4/24 already in B1127** (the "precisely neither
torsor" phrase overstates by 4); "reflection" should read "fixed-point-free on the color
A₂". The underlying theorem stands in full.

Gate 5 untouched (no SM quantity enters any object-side computation here).
