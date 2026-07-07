# B448 — the heartbeat adjudication: two handoffs, one exact orbit-field tower

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`. The multi-seat (B398-discipline)
adjudication of the two 2026-07-07 handoffs (Chat-2 "informed SM verdict"; Chat-1 "complete session
handoff"), plus the decisive new computation both pointed at: the trace-map periodic-orbit field
tower on the cusp locus, with the silver control.**

**Namespace note (binding):** the cross-chat corpus labeled "B296–B322" collides with banked repo
probes (B298–B300 = the V238 arc; B316; B322). Those labels are NOT used here; everything verified
from that corpus banks under THIS probe number.

## Part A — Chat-2's handoff: reproduced exactly (ALL CHECKS PASS)

`chat2_reproduction.py`, exact rationals throughout. The construction decoded from the handoff's
own numbers: word = the **period-doubling substitution 1→12, 2→11** (not Fibonacci); cocycle =
ordered product of `A(m) = [[m²+1, m], [m, 1]]`.

- Level-2 anchor `M = [[75,46],[44,27]]`, D=2, sum=192, |D|/sum = 1/96 — bit-for-bit. det ≡ 1
  at every level; eigenvalue field of M is ℚ(√26) (disc 102²−4 = 400·26 ✓).
- **The cocycle heartbeat**: D/sum → the exact period-2 limit cycle, even → **+0.010417735…**,
  odd → **−0.074495779…**, stable through level 12 (word length 4096).
- **The three structural NOs verified**: no self-selection (a 2-cycle attractor, never a fixed
  value); no definite chirality (sign(D) alternates −+−+ every level; the "definite" observables
  are artifacts — det≡1 trivially, a−d>0 is Perron–Frobenius, exactly as Chat-2 self-caught); no
  native scale (converges with the independently banked B413/B181/B447 scale-free results).
- **Genericity confirmed**: the variant matrix `[[m²+1,m],[1,1]]` converges to a *different*
  2-cycle (+0.0227/−0.0411); the symmetric golden matrix gives D ≡ 0 identically; an
  abelianization-variant cocycle gives a different D-sequence entirely. Mechanism generic,
  values are labels. Agreed dispositions: **"actualization theorem" renamed conditional
  rule-selection construction** (three chosen premises; the cocycle choice and the filter stack
  are load-bearing); the uniqueness-vs-mirror_reopen claim (1 of 16) remains single-seat
  (the closure formula was not in either handoff) — recorded, not banked.
- One correction to Chat-2's "last open door": band topology at the single-particle level is
  **theorem-dead** (gap-labeling + the solved Dry Ten Martini + KZ Chern=label — the campaign
  review), not open; the surviving door is the **interacting** case (D3), where no gap-labeling
  theorem exists.

## Part B — Chat-1's handoff: verified items and corrected items

**Verified** (this session): `Jones(4₁; e^{2πi/5}) = 1−√5` (exact, by hand and numerically);
`M_pd − M_fib = [[0,1],[0,0]]` nilpotent (one line); the ℚ(√26) eigenvalue field; and — the real
find — **the period-2 heartbeat: confirmed exactly** (Part C). The Child-Program, arrangement-
hypothesis, walk, dark-locus-Legendre, and B444 items match the banked record.

**Corrected** (items Chat-1 still carries that are already adjudicated):
1. *"V₁/V₂ amplify through trinification → 26+ E₆ components"* — *killed at B445*: those are
   reducible Levi-valued reps (they factor through SL(3)); the count is knot-independent.
2. *"The CS Hessian at the principal E₆ point = the mass matrix; eigenvalues = mass ratios;
   θ-odd lighter ⇒ matter lighter than gauge"* — **the object it names is already banked as
   ZERO**: the cup product H¹×H¹→H² vanishes in all six directions (B352, dps 100; to third
   order, B370). Their "mass matrix" is the zero matrix; the reading is the killed 3-generations
   trap. Any Computation-C run would reproduce a banked zero.
3. *Kashaev "phase = finite-T CS"* — vacuous: `⟨4₁⟩_N = Σ|(q)_k|²` is a sum of non-negative
   reals, `arg ≡ 0` identically (verified). The growth is banked (B419).
4. *"Seam values as L-function periods"* — the ratio-matching is the B322-killed value hunt;
   the L-values themselves are banked (B420).
5. *Level-45 dark locus flow* — legitimate and already registered (W1.5 / the campaign's F2/W-line).

## Part C — the orbit-field tower (the decisive new computation; exact)

**Setup.** Repo convention (B416): `T₁(x,y,z) = (z, x, xz−y)`, the figure-eight monodromy `= T₁²`,
κ conserved. **Reduction** (verified against T₁ numerically): T₁-orbits ARE the solutions of the
cyclic quadratic recursion `a_{n+2} = a_n·a_{n+1} − a_{n−1}`, state = `(a_n, a_{n−1}, a_{n+1})`;
the cusp locus κ=−2 is `a_n² + a_{n−1}² + a_{n+1}² − a_n a_{n−1} a_{n+1} = 0`. Period-k orbits on
κ=−2 = an exact ideal (k quadrics + 1 cubic), solved by Groebner over ℚ (`orbit_fields.py`).

**The classical anchor:** κ=−2 **is the Markov surface** (`x²+y²+z² = xyz`; scaling x=3a gives the
Markov equation `a²+b²+c²=3abc`; (3,3,3) ↔ the fundamental triple (1,1,1); the integer T₁-orbit of
(3,3,3) walks the Markov tree). Classical territory — a credibility anchor, no novelty claimed.

**The tower (T₁-periods on κ=−2, exact eliminant factors):**

| T₁-period | monodromy meaning | field | note |
|---|---|---|---|
| 1 | — | ℚ (a=0: the (0,0,0) point) | the frozen point; a=2 is the void (κ=+2, excluded) |
| 2 | **monodromy-FIXED** | **ℚ(√−3)**: `x²−3x+3`, disc −3 | **the discrete-faithful pair — the trace field, re-derived dynamically. Chat-1's "first heartbeat": CONFIRMED EXACTLY** |
| 3 | — | *nothing new* | no genuine period-3 orbits on κ=−2 |
| 4 | monodromy-period-2 (double cover) | **ℚ(√−7)**: `x²−x+2`, disc −7 | **the CHIRALITY field (B147/B316/B444) — its THIRD independent appearance.** The orbit in closed form: `(−1, (1+√−7)/2, −1, (1−√−7)/2)` |
| 5 | mirror-twisted 5-fold | irreducible quintic `x⁵+x⁴+x²+3x+1`, disc 7²·17² (a square) | **NOT ℚ(√5) — Chat-1's field-tower hypothesis (period 5 → golden) REFUTED** |
| 6 | monodromy-period-3 | ℚ(√−3) again: `x²+3x+3` | the Eisenstein partner |
| 7 | — | irreducible deg-14, disc 3²·13⁷·23³·367³·6029² | generic large orbit field |

(T₁ itself is the half-monodromy: `T₁² = L∘R` verified; the half corresponds to the det-−1
Fibonacci matrix `C=[[1,1],[1,0]]`, `C² = A` — even T₁-periods = characters extending to cyclic
covers of the bundle; odd periods are mirror-twisted. [MATH] for the even-period covering reading;
[HOOK] for any RRL-bundle connection of the period-4 orbit — a named follow-up, not asserted.)

**The silver control** (`silver_control.py`; twist maps verified against 2×2 matrices first):
silver monodromy S = L²R². Gate: Fix(S) on κ=−2 gives `z⁴+16` → ℚ(ζ₈) ⊃ ℚ(i) = silver's banked
invariant trace field (B316) ✓. **Silver's double-beat** (Fix(S²)∖Fix(S)): `z²+3` (ℚ(√−3)),
`z²+4` (ℚ(i)), `z⁴−z²+4` (resolvent disc −15). **No ℚ(√−7).**

## Verdict (campaign bins)

- **Chat-1's field-tower hypothesis: TESTED-NEGATIVE.** √5 appears at NO period ≤ 7 — the golden
  field is dynamically absent from the hyperbolic-end orbit tower, consistent with the banked
  two-ended structure (√5 lives at the E₈/spherical end, not on κ=−2).
- **The heartbeat field tower LAUNDERS into the whitelist — and beautifully.** The first beat is
  the trace field (ℚ(√−3), the geometric pair); the double beat is the chirality field (ℚ(√−7)),
  its third independent mechanism (B147 chiral cousins; B444 SL(3); now the monodromy's own
  double-cover orbit arithmetic). The silver control confirms the labels are object-specific and
  the mechanism generic (silver's beats carry ITS fields — i, √−3, a −15-resolvent — small
  discriminants recur promiscuously across the class at low periods, the known small-number
  caution). No new low-period fields; no H1. **The warm/dynamical layer reads back the frozen
  arithmetic — the campaign's H0a, confirmed at a new channel.**
- **Banked positives:** the exact recursion reduction; the tower table (k ≤ 7); the closed-form
  period-4 orbit; the Markov-surface identification of the cusp locus; the silver control pair;
  the two-handoffs adjudication above. The two heartbeats (Chat-2's cocycle 2-cycle on the
  period-doubling word; Chat-1's trace-map orbits) are **distinct objects with distinct
  mechanisms** — kept apart here and in the Concept Atlas card.

## Reproduce

```
python3 chat2_reproduction.py   # exact; prints ALL CHECKS PASS
python3 orbit_fields.py         # the tower, k=1..7 (Groebner, ~1 min)
python3 silver_control.py       # the control (gate + beat fields)
pytest ../../tests/test_b448.py
```
