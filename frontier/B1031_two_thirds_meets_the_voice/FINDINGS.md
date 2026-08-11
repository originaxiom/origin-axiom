# B1031 — FINDINGS: the two-thirds theorem meets the voice

**Seat:** cc · **Date:** 2026-08-11 · Verification/scrutiny arc (incoming-results protocol;
no outcome-prior to protect — the content is the scrutiny plus a desk-proved corollary).
Compute: `b1031_verify.py`. Owner-directed ("agreed. lets do them").

## §1 — the external input, with provenance (post-cutoff literature)

**The paper:** *"More than two thirds of the zeros of the Riemann zeta function lie on the
critical line"* — author: a large language model (Anthropic); dated **2026-08-10**; the
mathematics communicated and contextualised by L. Alpöge and R. Furman; examined by
B. Conrey and D. Goldston. Main results: **liminf N₀\*(T,2T)/N(T,2T) ≥ 2/3
unconditionally** (simple, on-line; optimised 0.6725), distinct ≥ 5/6 (Theorems A–D), and
**the same for every primitive Dirichlet L-function** (Theorem E). Method: Weil's explicit-
formula Hermitian form restricted to a finite Gabor family; off-line pairs enter as
signature-(1,1) blocks; Sylvester's inertia + a rank–trace inequality (von Neumann) replace
the termwise positivity that fails off the line; the prime side is Montgomery's two moments,
unconditional after Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (arXiv:2306.04799,
2501.14545); the negative-index observation is Bombieri's (2000).

**Fetched 2026-08-11** from `www.anthropic.com/research/riemann-zeta`; artifacts archived
off-tree with SHA-256 prefixes: paper `6792988e` · informal note `45e0330a`\* · discovery
appendix `271aba2d`\* · transcripts `a615cac7`\* · arXiv 2306.04799 `133071c4`\* ·
arXiv 2501.14545 `ebb34c5e`\* (\*assignment of the four starred prefixes to files recorded
in the archive listing; the paper's own hash is as stated). Lean repository
`github.com/anthropics/zeta-23-lean` at commit `3635e748…a00510`.

## §2 — the scrutiny: the verification verified

Performed at bank time on the archived clone, this seat, locally:

- `AUDIT.md` records `lake build` clean (8890 jobs), **zero** `axiom` declarations in the
  sources, `sorry` **only** in the deliberate comparator statement files (15 + 12; none
  under `Zeta23/` or any `Solution` file) — **re-checked by direct grep on the clone**;
- `#print axioms` on all 27 comparator statements returns exactly
  `[propext, Classical.choice, Quot.sound]` — including
  `dirichlet_two_thirds_on_critical_line`, the statement our corollary consumes;
- statements are expressed directly against Mathlib's `riemannZeta` (no statement gap);
  the toolchain and Mathlib commit are pinned; constants separately verified symbolically
  (31 checks, recorded in the paper's Appendix B.2).

**Scrutiny verdict: nothing for us to add at the proof level.** The paper also states its
own limits with house-grade honesty (§7.5): it is a **degree-one method** (an individual
GL(2) L-function gets c = 6/13 < ½ — nothing, whatever the window), λ ≤ 1 is forced exactly
at the Hardy–Littlewood prime-pair wall, and **"RH itself is out of reach of the
mechanism"** — the all-moments ceiling is proportion 1, which still permits o(N)
exceptions. Our GL(2)-flavoured McKay/tensor objects sit outside its reach *by its own
stated wall* — recorded so nobody retries it here naively.

## §3 — the corollary (desk-proved; every self-contained step verified in-sandbox)

For K = ℚ(√−3): ζ_K(s) = ζ(s)·L(s,χ₋₃), by r = 1∗χ — **verified exactly** as the integer
identity r(n) = (1/6)#{x²+xy+y² = n} = Σ_{d|n} χ₋₃(d) for n ≤ 3000 (lattice count against
character convolution, V1), with a truncation-tail-tight floating check of the factored
series at s = 2. The zeros of ζ_K (with multiplicity) are those of ζ together with those of
L(χ₋₃); Theorem A gives the first factor ≥ 2/3 on-line, Theorem E (q = 3 fixed) the second;
the union arithmetic is exact (V2). Therefore:

> **≥ 2/3 (dyadic liminf, counted WITH multiplicity) of the nontrivial zeros of
> ζ_K(ℚ(√−3)) lie on the critical line, unconditionally.** Via B737 (the object's voice =
> Λ_K(s)/Λ_K(s+1), banked): **two thirds of the numerator zeros of the object's own cusp
> voice are certified critical.**

**The fence (V3), stated before anyone asks:** simplicity and distinct-point counts do
NOT transfer — a common zero of the two factors (existence OPEN; its absence is part of
the grand-simplicity picture) would be multiple in ζ_K while simple in each factor. This
arc claims location-with-multiplicity only. And the B737 crux stands untouched: **the ζ is
the field's, not the object's** — this corollary certifies where the voice's numerator
zeros sit; it does not make them the object's.

## §4 — one numerics lesson, recorded

The first draft of V1's floating check computed L(2,χ₋₃) by `nsum` acceleration on the
mod-3-periodic sign pattern and **failed**; the exact Hurwitz form
3⁻ˢ[ζ(s,⅓) − ζ(s,⅔)] fixed it. The lesson (series acceleration on periodic-sign patterns
is unreliable; use closed/Hurwitz forms) is kept visibly in the source — the exact integer
identity, not the float, was always the load-bearing check.

## Verdict: PROVED (scrutiny affirmative; corollary desk-proved with its fence)

Companion: `knowledge/K027_the_convergent_protocol.md` (the methodological convergence —
the paper's discovery appendix runs this repo's protocol, independently evolved). Relay
sent to the audit seat with an adversarial invitation on the fence and the Theorem-E
uniformity reading. Gate 5 untouched; no SM value anywhere; nothing about RH is claimed
beyond what the external theorem states.
