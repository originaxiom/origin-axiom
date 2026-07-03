# B399 (Wall Campaign W-A) — PRE-REGISTRATION: the scale wall via the (1+c)/12 tower

**Committed before the 1215 computation. The owner-approved wall campaign, W-C sequence
(scale first). Firewalled: level-model statements only; "scale" names the wall being
priced, not a claim.**

## A1 — the walk law (the 1215 rung decides between two registered candidates)

Data: singles values (1+c)/12 with c = 2 (levels 15, 45, 135; 4 cells each) and c ∈ ζ₉⁺
orbit (level 405 = 3⁴·5; 12 cells = 4 × orbit-3). The c-field depth lags the level's
3-depth by 2. Sum rule Σ = 1 at all four rungs. For 1215 = 3⁵·5 (ord(W₁) = 1620), the
candidates:

- **CAND-FIX (normalizer fixed):** values (1+c)/12, c over the ζ₂₇⁺ orbit (degree 9);
  the sum rule then forces cell count 12 — one orbit copy plus multiplicity pattern
  (4/3 × 9 = 12): support 12 cells, each orbit value appearing 4/3... NOT integral —
  so CAND-FIX survives only with a non-uniform multiplicity (registered as: 12 cells,
  values from the ζ₂₇⁺ orbit with multiplicities (2,1,1)-patterned, Σ = 1).
- **CAND-DEG (degree-scaled normalizer):** values (1+c)/(4·deg) = (1+c)/36 with c over
  ζ₂₇⁺ (deg 9), support 4 × 9 = 36 cells, Σ = 4·(9 + Tr c)/36 = 1 exactly (Tr = 0). This
  candidate UNIFIES the prior rungs: at deg 1 (c = 2 "orbit"), (1+2)/4·1... = 3/4 ✗ —
  CAND-DEG fails retroactively at deg 1 unless the degenerate normalizer is 12; so
  CAND-DEG is registered as the DEPTH-3 LAW: (1+c)/(4·deg) for deg ≥ 3 with the deg = 1
  levels normalized at 12 (the transition at 405 being deg 3: (1+c)/12 = (1+c)/(4·3) ✓✓
  — NOTE: 405's own values ALREADY satisfy (1+c)/(4·3): the two candidates AGREE at 405
  and diverge at 1215).

KILL: neither — bank the actual support/values (the law then needs a third form).
Machinery: numpy F_p singles at 1215 (2 primes ≡ 1 mod 4860; int64 chunked matmul;
detached, PID-watcher; ~2–4 h). Locks from the JSON.

## A3 — the normalizer's origin (is the singles' 1/12 the seam's 1/12?)

Derive the level-15 single constant 1/4 in closed form from the trace formula (P64) the
way B386 derived the pair constants: t₁(a) = (1/20)Σ_j ζ₂₀^{−ja}·tr(Par·W₁ʲ) with
tr(Par·W₁ʲ) = ζ₆⁻¹·χ₁(j)·ζ₁₅^{Q_j(1,1)} on the domain. REGISTERED QUESTION: does the
assembled closed form exhibit the SAME 1/16 + 1/48-type det-class split (the seam's 1/12
mechanism), or a different decomposition? SAME split ⇒ the two 1/12s are one object
(bank the unification); different ⇒ two independent 1/12s (bank the distinction — equally
structural). Two-outcome.

## A2 — the hierarchy probe (prices Wall 1)

With the walk law banked: the value-distribution statistics across levels (min, max,
spread, products of extreme values across consecutive rungs). REGISTERED QUESTION: does
any cross-level dimensionless combination grow/shrink EXPONENTIALLY in the depth (a
hierarchy mechanism), or is everything bounded by the c-range (1+c)/12 ∈ (−1/12, 1/4]?
Registered expectation: BOUNDED (the honest prior); an exponential separation would be
the surprise outcome demanding its own gauntlet.
