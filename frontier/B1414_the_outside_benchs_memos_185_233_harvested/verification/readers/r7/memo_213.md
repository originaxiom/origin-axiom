# Reader r7 — Memo 213 (`memos/THE_CUSP_CANNOT_TELL.md`)

## 1. HEADLINE

"L71: THE PERIPHERAL SLOPE IS THE SAME IN EVERY BLOCK, AND THAT IS A THEOREM ABOUT THE CUSP,
NOT AN ANSWER." No per-memo date line in body; INDEX.md row 311 records "banked 2026-09-12."
CELL 1 = A, CELL 2 = B, CELL 3 = A; controls C1–C4 passing.

## 2. CLAIMS

1. **CELL 1 = A**: `slope_m := [ξ(λ)]/[ξ(a)] = −2√−3` **exactly** (over ℚ(ζ6), no floating
   point) for every m=1..12 — both θ-odd exponents (4,8), all six E6 exponents, all six
   non-exponents; `−2√−3` is the figure-eight's own cusp shape. Controls: relator=identity in
   every block, `ρ(λ)` commutes with `ρ(a)`, matches P2W5-L72's exact table at the six E6
   exponents, SnapPy agrees in magnitude to 2.220e-15 (sign difference fenced in advance as
   SnapPy's own orientation convention). Grade: OUTCOME A, exact, "read alone that is a
   headline."
2. **CELL 2 = B**: the cusp's own cocycle condition `(ρ(a)−I)ξ(λ)=(ρ(λ)−I)ξ(a)` **already
   forces** the ratio, for every m=1..12, with no solution in the (4,6,...,26)-dimensional
   solution space differing from `−2√−3`. Mechanism (post-hoc, computed not preregistered):
   `ρ(a)=exp(N)`, `ρ(λ)=exp(τN)`, same nilpotent N; `f∘N=0` and `f(ker N)=0` checked exactly for
   m=1..6 ⇒ `f(ξ(λ))=τ·f(ξ(a))` **identically, for any cocycle, on any manifold with this
   cusp.** Grade: OUTCOME B — "the invariant is blind by construction."
3. Conclusion: "L71 is not answered, and this route cannot answer it" — the CELL-1 constancy is
   a theorem about ℤ² with a unipotent action, true for every knot and every block, not a fact
   about the figure-eight, E6, or θ-grading. Grade: NEGATIVE, explicit.
4. **CELL 3 = A**: confirms from the other side — the conjugate rep gives `+2√−3` at m=1,4,8 (the
   statistic DOES move with the representation), but it moves "exactly as the cusp shape
   moves" — passing MB12 shows the instrument is not constant, not that it is informative
   (explicitly citing "memo 164 again"). Grade: OUTCOME A / negative-confirming.
5. Rule added: "when a statistic comes out identical across every case, the next cell asks
   whether the statistic COULD have differed — before the constancy is written down as a
   finding." Grade: methodological rule, self-critical (the memo states it would have banked a
   wrong object-specific claim had CELL 2 not been in the seal).
6. §5 names three untried candidates for L71 that do NOT factor through the cusp (none claimed
   to work): the full 2-dim peripheral class (not just its 1-dim coker shadow); the
   cup-product/symplectic pairing on Sym^{2m} (B270 did only m=1); the per-block Zariski closure
   of the representation (B576 did the *algebra* version, "a different question"). Grade: named
   follow-ups, not executed.
7. Fence: the disclosure that m=1,2 were computed in a scratch prototype **before** the seal was
   written, and the CELL 1 prior was declared knowing them — but CELL 2 (the decisive outcome)
   "had no prior declared and went against the direction the author expected." Grade:
   self-disclosed prior-knowledge fence.

## 3. CERTIFICATE

- `certificates/l71_cusp_slope.py` — EXISTS. `outputs/l71_cusp_slope.txt` — EXISTS; tail matches
  the memo's mechanism section closely, showing `f∘N=0: True`, `dim ker N=1`, `f(ker N)=0: True`
  for m=1..6, and ends "So the statistic reads the CUSP SHAPE and nothing else... DONE."
- `seals/L71_CUSP_SLOPE_PREREG.md` — EXISTS; **sha256 recomputed and matches exactly**:
  `788faf6fd92a0674109f38307cdf1725bb9f28c298e533956e181d47fc19ad31`, committed before the
  certificate, "with the m=1,2 prototype disclosed inside it," as claimed.
- No addendum changed this seal within the memo file itself.

## 4. ON MAIN ALREADY?

- **(c) NOT on main, for the memo's specific content.** Grep across `frontier/`, `docs/`,
  `papers/` (excluding `outside_bench/`) for "peripheral coker", "l71_cusp_slope", "slope_m"
  returns **zero hits**. No `frontier/B*` arc exists for this computation, and it is not cited
  in `docs/OPEN_LEADS.md`.
- **Confirmed directly: `docs/OPEN_LEADS.md`'s L71 row (line 522) is unchanged and still reads
  plain `OPEN`** — unlike L72 and L78 (both of which carry the "[SUPERSEDED IN PLACE
  2026-09-12 — outside-bench memos 206/208/210/211/213/214/215...]" bracket), L71's row has
  **no such bracket at all**, even though memo 213 (and its successor memo 214, not assigned to
  me) is listed as one of the contributing memos in *other* rows' brackets. This is not a
  contradiction (memo 213's own conclusion is that L71 remains genuinely unanswered — the memo
  never claims L71 itself should be marked resolved), but it does mean the "computable content
  is finished" recommendation from the owner register (see below) has **not** been applied to
  the row text.
- I checked `outside_bench/THE_OWNER_REGISTER.md` R122 ("go for it": the peripheral route is
  exhausted, provably — the direct successor session to this memo, running memo 213's own named
  follow-up on the full peripheral class). R122 explicitly states: **"This bench does not edit
  `docs/OPEN_LEADS.md`"** and R122-2 recommends (not executes) "re-pose L71 as a
  literature/specialist item or close it, citing its four computable components [B575, B576,
  B270, memos 213–214]." So the absence of a write-back on L71's row is **by the outside bench's
  own stated policy**, not an oversight or a contradiction — the batched brackets on L72/L78's
  rows appear to have been added by a *different*, later banking pass that did not extend to
  L71 (possibly because L71's row, unlike L72/L78, is not itself claimed "resolved" or
  "superseded" — only a *sub-route* within it is closed).
- The three cited "computable components" (B575, B576, B270) are real, pre-existing main arcs
  (I did not re-verify their content, out of scope — they are cited as prior facts, not new
  claims of this memo).

## 5. NEEDS COMPUTATION HERE

- Claim 1 (exact slope `−2√−3` for all m=1..12): NEEDS COMPUTATION — cheap, exact linear algebra
  over ℚ(ζ6). A verifier should rebuild `ρ(a)`, `ρ(λ)` on `Sym^{2m}(ℂ²)` from the figure-eight's
  holonomy and recompute the peripheral cocycle ratio for at least the six E6 exponents.
  Expected: exactly `−2√−3` (or `+2√−3` for the conjugate rep, per CELL 3).
- Claim 2 (the cocycle condition forces the ratio — the decisive negative): NEEDS COMPUTATION —
  this is the single discriminating fact of the whole memo. A verifier should independently
  solve `(ρ(a)−I)ξ(λ)=(ρ(λ)−I)ξ(a)` for m=1..6 and confirm the solution space's ratio is pinned
  to `−2√−3` with no freedom, and separately verify `f∘N=0` and `f(ker N)=0` exactly (both are
  finite exact linear-algebra checks, not estimates).
- Claim 4 (CELL 3, conjugate rep gives `+2√−3`): NEEDS COMPUTATION — cheap, same recomputation
  with the complex-conjugate representation.
- Claim 6 (three named untried routes): DOCUMENTARY (nothing to compute — these are proposals,
  explicitly "not claimed to work").

## 6. SUPERSESSION

- Memo 213's own route (the peripheral coker slope) is superseded/exhausted by its **own direct
  successor**, register R122 / "memo 213 named successor" work (memo 214, not assigned to me),
  which shows (per R122-1, R122-2, quoted in §4 above) that the canonical peripheral data
  reaches only a 1-dimensional subspace of the 2-dimensional `H¹(T²;V)` — i.e., memo 213's
  "second coordinate" follow-up (claim 6, first bullet) was itself run and found to also be
  forced/empty. This is a continuation-and-closure of memo 213's own named successor, not a
  contradiction of memo 213 itself; memo 213's headline stands as accurate.
- `docs/OPEN_LEADS.md` L71 row is NOT updated (see §4) — by the bench's own stated non-editing
  policy, not because of any dispute.
- No later INDEX.md row marks memo 213 itself as withdrawn.

## 7. GRADE PROPOSAL

**REGISTER.** This is a well-controlled, honestly-reported NEGATIVE result (an entire
computational route to L71 closed as structurally uninformative, with the mechanism proved
exactly) — it is documentary/methodological in the sense that its value is in ruling out a
route and adding a reusable rule (claim 5), not in producing a positive value or an object-
specific fact. It deserves a row (the negative is real, controlled, and cheap to reproduce) but
is not itself a "REPRODUCE-AND-BANK" computation in the sense of adding new object-specific
knowledge — its main artifact is knowing NOT to trust the peripheral-coker invariant, which is
best captured as a registered negative plus the follow-up pointer to L71's remaining (named,
un-computable-here) geometric-naming question.
