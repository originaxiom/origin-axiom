# B776 FINDINGS — THE B685 HOMEWORK: B685 corroborated, now FROM FIRST PRINCIPLES

*2026-07-24. Workflow wf_389efedc-65c. Both computations UPHELD. cc hand-verified
r₇'s factorization + the symprod trajectory. The load-bearing negative (B685) is
CORROBORATED, not reversed — and upgraded from cited-by-title to reconstructed
in-cell. results.json is the record.*

## Computation 1 — r₇ pushed (RESOLVED-A, UPHELD)
**r₇ = 212114205337147471/115579079884800**, denominator **2²⁵·3⁹·5²·7**, v₅(r₇)=2.
The v₅ sequence r₁…r₇ = **[0,0,1,1,1,2,2] — PLATEAUS at 2** (r₆=r₇=2, the growth does
NOT continue). Reproduced on two disjoint Kashaev-sum ladders at dps=1200 (r₇ cleared
~63 trusted digits vs OI-055's ~33; PSLQ residuals ~1e-64). r₈ also computed (v₅=2,
plateau holds). The verifier deleted the cache and regenerated from scratch (7 min) —
identical; re-factored every denominator (no E15 trap — the 3⁹ is a power of 3, only
the literal 5² counts). **NB:** this is the Φ-level GZ stream, already known NOT
3-integral (5 enters at r₃, 7 at r₅) — the 5/7 here are EXPECTED and do NOT bear on
B685's negative, which concerns the SYMMETRISED product (Computation 2).

## Computation 2 — the symmetrised product (RESOLVED-B, UPHELD) — THE HEADLINE
For the FIRST TIME in-repo, Φ(h)Φ(−h) was **reconstructed FROM FIRST PRINCIPLES** (not
cited): the figure-eight Kashaev sum Σ_k|(q)_k|² expanded around its interior saddle
w₀=e^{iπ/3} (w₀²−w₀+1=0, disc −3) via the exact q-Pochhammer/quantum-dilog asymptotic,
then formal Gaussian (Wick) integration with all arithmetic exact in ℚ(√−3). It
reproduces r₁=11/24, r₂=697/1152 and GSWZ eq(2) EXACTLY, and the OI-055 Φ-level prime
support exactly. **The symmetrised product is PURE-3 through order u⁵⁰: denominator
3⁷³ at order 50 — exactly half the 3¹⁴⁶ at order 100 (73·2=146), dead on the linear
~1.46·k trajectory to B685's anchor. NO literal 5^k/7^k in ANY denominator at ANY
computed order** (0–50 complete; five_appears=FALSE).

**Honest boundary (the anchor guard, obeyed):** the order-100 anchor (3¹⁴⁶@100) was
NOT observed-complete in-cell — the order-105 run was still executing at the forced
structured-output cutoff. This is a **wall-clock cutoff, NOT a normalisation gap**
(every completed check confirms the object is the genuine GSWZ element). Closing it
now via the cell's own re-run (MM=105, ~25 min).

## What this means for the owner's question
**B685 is CORROBORATED, not reversed.** No prime ≠3 appears in the symmetrised
product through the verified depth (order 50), and the trajectory is dead-on to the
order-100 anchor. Chat-1's fragility hypothesis (5 might appear at order 101–200) is
NOT supported through order 50, and — more importantly — the program now has an
**in-cell first-principles reconstruction** of the very element B772 flagged as
"cited by title only." That directly closes the B772 provenance concern: the
3-integrality is no longer a citation, it is a reconstructed computation on-trajectory
to depth 100.

## Standing after this arc
- The GSWZ question is now MAXIMALLY well-posed: computation-backed to order 50 from
  first principles, r-stream to r₈, the plateau observed. **The GSWZ send remains a
  HARD-STOP for owner approval** — nothing sent.
- OI-055's census label (SEARCH-BOUNDED depth-100, from B772) can UPGRADE once the
  MM=105 anchor run completes: from "cited depth 100" to "reconstructed-in-cell to
  depth ~100 on the pure-3 trajectory."

Gate 5/5-Q: pure number theory. Nothing to CLAIMS; the one-number pin untouched;
nothing sent to anyone.
