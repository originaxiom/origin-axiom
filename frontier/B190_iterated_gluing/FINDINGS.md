# B190 — abstract iterated gluing: iterating does not converge to a forced-unique value

**Date:** 2026-06-22. **Status:** Masterplan III, **Track F** (first of two). Pushes the abstract trace-ring
gluing (B174's `(p,q,r)` mapping-class maps) past B185's pair-cap, **in both directions** — open gluing (a fork)
and closed/loop gluing (over-determination = fixed points) — to test quantitatively whether iterating drives the
constraint side toward a *unique* selection or proliferates. **Computed** (sympy; no 3-manifold built). **Result:
it does not converge to a forced-unique value** — confirming B185 in the trace ring. **Firewall-side:** emergent
low-dim-topology / character-variety math (`K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16
frozen. Ledger V183. Reproducer `iterated_gluing.py` (`ALL CHECKS PASS`).

## The two directions

Maps (B174): `S` (swap `μ↔λ`): `(p,q,r)→(q,p,r)`; `T` (Dehn twist): `(p,q,r)→(p,r,pr−q)`.

- **C1 — OPEN gluing proliferates.** The fork size (Bézout degree of the single-map glued variety) **grows** with
  the gluing word: `T^k → 8+k` (linear in twists: 9,10,11,12,13), and swaps `~double` (`S=16, ST=32, STSTS=64`).
  Always `>1`, never `0` — iterating the gluing gives *more* discrete structure, never convergence to a unique
  point. (Sharpens B174's "fork grows with complexity" into the explicit `8+k` / doubling laws.)
- **C2 — CLOSED/LOOP over-determination → finite discrete, growing.** A closed-loop gluing imposes the composed
  word's **fixed-point** condition on the boundary variety. For pseudo-Anosov words the fixed-point set is
  **finite and grows with length**: `ST→1, TST→2, STST→3`. So over-determination *does* collapse the continuum to
  a discrete set (selection-to-discrete confirmed). (Reducible Dehn-twist words like `T` keep a 1-parameter fixed
  *curve* — parabolic, not finite.)
- **C3 — but NOT forced-unique, and the lone unique is vacuous.** The only count-1 loop (`ST`) fixes the **trivial**
  point `(2,2,2)` (all traces `2` = reducible; MB12-vacuous). Genuine non-trivial fixed points first appear at
  `STST` — **two golden-field points** `((√5−1)/2, −(√5+1)/2, …)` — as a *multiplet*, and the count grows with the
  loop word. So the "selection" is **per-gluing-choice with the count proliferating**, never a single forced value.
  This is the trace-ring realization of B185's "selects-to-discrete, not forced-unique."
- **C4 — FIREWALL + scope.** The abstract trace-ring iteration is computed in both directions; the *literal*
  closed-loop 3-manifold realization is multi-cusp = **NEEDS-SPECIALIST** (B185's 1-cusp cap).

## What this means for the search (S036)

The **SELECTION** ingredient's "does iterating the constraint force a unique value?" is now answered in the trace
ring: **no.** Open gluing proliferates (the fork grows: `8+k` / doubling); closed/over-determined gluing collapses
to a finite discrete set that *also* grows with the loop word (the lone unique case is the trivial point; genuine
fixed points are golden-field multiplets). The genuine selections that *do* appear are tied to the **golden field**
(`√5`) — consistent with the metallic/golden privilege (B176) — but they come in growing multiplets, per loop-word,
so no single forced-universal value emerges. This confirms B185 (selection-to-unique not delivered) in both the open
and the over-determined directions, and isolates the genuine route (closed-loop / multi-cusp) as the specialist one.

## Scope / honesty
- Pure abstract trace-ring computation (sympy resultants + fixed-point solving) for the figure-eight seed; the
  literal closed-loop **multi-cusp 3-manifold** realization remains NEEDS-SPECIALIST (B185).
- The golden-field fixed points are read off the `STST` solution; deeper words give larger multiplets (the count
  grows) — not exhaustively enumerated.
- Emergent low-dim-topology / character-variety mathematics (`K010` boundary); nothing to `../../CLAIMS.md`.

## Anchors
`B185_constraint_selection` (the pair-cap + "selects-to-discrete, not unique" this confirms/sharpens),
`B174_gluing_map_landscape` (the `(p,q,r)` maps + single-map fork sizes), `B131`/`K014` (the κ-fork), `B176`
(golden privilege — the golden-field fixed points), `B67` (the figure-eight A-poly curve), `docs/OPEN_LEADS.md` H5.
External: mapping-class-group action on the relative `SL(2,ℂ)` character variety; Dehn twists vs pseudo-Anosov
(reducible fixed curve vs finite fixed points); Bézout / Kitano–Nozaki (fork finiteness).

## Reproduction
`python frontier/B190_iterated_gluing/iterated_gluing.py` — C1 open-fork growth laws; C2 closed-loop fixed-point
counts (finite, growing); C3 the trivial-unique + golden-field multiplets; C4 firewall/scope. Prints
`ALL CHECKS PASS`. Fast locks in `tests/test_b190_iterated_gluing.py` (2 tests, ~0.8s).
