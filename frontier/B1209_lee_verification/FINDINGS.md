# B1209 — THE LEE VERIFICATION (R52-3): three questions answered from the source, and the hoped-for bridge to the observer's bit is CLOSED

**Verdict**: `NEGATIVE` (a named route closes; the positive half stands) · **2026-08-29** ·
**Gate 5 clean** (topology and Newton polygons; no measured value) · discharges **R52-3** and the
**E37 CITED/UNVERIFIED** grade B1198 carried

## What was owed

B1198 put the SEAM-A bar's literature half "in hand rather than absent" and named its verification
step: **read §7.4 + Appendix A of Lee, arXiv:2502.11950** and answer three questions. The paper was
**obtained and read on this bench** — not cited from an abstract — so the three answers below are
from the source text, and the load-bearing one is **independently re-derived from main's own
banked A-polynomial**.

> Dong Uk Lee, *"Chern–Simons invariants of hyperbolic three-manifolds, mixed Tate motives, and
> motivic path torsor of augmented character varieties"* (arXiv:2502.11950). Theorem 2 constructs,
> for any complete finite-volume hyperbolic 3-manifold, a **mixed Tate motive over the invariant
> trace field** whose Beilinson regulator is the complex volume.

## Q1 — Is the admissible tangent-vector set a torsor, and under what group?

**YES, and the group is ℤ/|a₁| — which for our object is TRIVIAL.**

Lee states the count directly (§7.4, before Conjecture 7.4.2):

> *"When a₁ = 1, such choice of the parameter z amounts to a choice of a tangent vector ∂/∂z; in
> general, there are several (i.e. as many as |a₁|) choices for a tangent vector ∂/∂z giving
> a₂ ∈ (2πi)ℤ."*

So the admissible set has exactly **|a₁|** elements, and rescaling the uniformizer by an |a₁|-th
root of unity acts simply transitively on them: a **torsor under ℤ/|a₁|**. His Appendix A computes
**a₁ = +1, −1, +1, −1** at the four ideal points of 4₁, and reports that **all four satisfy the
conjecture**.

**This bench does not take that on trust.** a₁ and b₁ are the orders of vanishing of the meridian
and longitude eigenvalues at the ideal point, so **(a₁, b₁) is a primitive edge vector of the
Newton polygon of the A-polynomial** — which main banked at **B67**. Computing that polygon here:

| edge | primitive vector | (a₁, b₁) | boundary slope b₁/a₁ |
|---|---|---|---|
| (0,1) → (4,0) | (4, −1) | (−1, 4) | −4 |
| (4,0) → (8,1) | (4, 1) | (1, 4) | 4 |
| (8,1) → (4,2) | (−4, 1) | (1, −4) | −4 |
| (4,2) → (0,1) | (−4, −1) | (−1, −4) | 4 |

**Every edge has |ΔL| = 1, so |a₁| = 1 at every ideal point** — and the four (a₁, b₁) pairs
reproduce Lee's four cases exactly, with boundary slopes ±4 matching the figure-eight's known
values. The structural reason is now ours: *the A-polynomial's Newton polygon is thin in L.*

> **CONSEQUENCE — the bridge is closed.** The torsor group is **ℤ/|a₁| = trivial** for m004. It is
> **not ℤ/2 and not V₄**, so there is **no contact** between Lee's choice-of-tangential-base-point
> and the programme's orientation bit (B1174 / B1182 / B1183). The hoped-for identification —
> *"the outside instance of the missing archimedean marking"* — **fails, and now with a stated
> mechanism rather than as an absence.**

**This confirms B1201 from the source.** B1198's original claim (*"the tangential base point is
chosen, not derived"*) was withdrawn at B1201 on this bench's own computation that |a₁| = 1 at all
four ideal points. Lee's own appendix says the same, and the Newton polygon explains why. **The
withdrawal was correct and is now double-sourced.**

## Q2 — Does the 4₁ confirmation use the CS = 0 degeneracy?

**NO.** Appendix A confirms Conjecture 7.4.2 *"by direct computation based on an explicit
description of the Neumann–Zagier potential on the deformation curve as provided in [Hik07]"* —
Hikami's equation, itself obtained by the saddle point method. The four cases are evaluated with
dilogarithm identities, and the limits (the (1,3)-entries) come out as **±4ζ(2) = ±2π²/3**,
rational multiples of (2πi)² exactly as the conjecture requires.

**The CS = 0 degeneracy that B1195/GC-21 made exact plays no role**, so that hoped-for contact point
is closed too. The one genuine adjacency is that Hikami's curve comes from **the saddle point
method** — the same instrument family as GC-21 — but the appendix's verification does not use the
degeneracy.

## Q3 — Does the trace-field statement specialize to ℚ(√−3) as the seam needs?

**YES, exactly, and with no special-casing.** Lee's Theorem 2 places the motive in
`Ext¹_{MT(k(M))}(ℚ(0), ℚ(2))` over the **invariant trace field k(M)**. For m004 the invariant trace
field **is ℚ(√−3)** (banked: trace field x² − x + 1). So the construction lands over the programme's
own field **by its general statement**, which is the strongest form this question could have been
answered in.

## What this leaves

**The positive half stands and is the valuable half**: an outside, published construction of a
**mixed Tate motive over ℚ(√−3) whose Beilinson regulator is our complex volume**, with 4₁ as a
verified appendix case. That is a genuine meeting point for the arithmetic side.

**The negative half is this arc's own finding**: Lee does **not** supply the free archimedean
marking SEAM-A is missing — for our manifold there is nothing free there at all. **The W₀ bar
stands unchanged**, and one route to it is now closed with its reason named, which is a narrower and
more useful state than "the reading list is in hand."

**Fences.** The three answers are from the source text, quoted; Lee's own computations are cited,
not re-derived — except the |a₁| = 1 fact, which is independently derived here from main's banked
A-polynomial and therefore does not rest on his appendix. Conjecture 7.4.2 remains a **conjecture**
in general (verified by Lee for 4₁ and, for at least one ideal point, 5₁); nothing here asserts it
beyond those cases.
