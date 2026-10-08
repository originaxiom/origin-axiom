# B1623 — THE OWED LITERATURE CHECKS (Review 62's R62-2): Lemma F's step (2) verified on main for the seat's four; Lemma F and three of main's four NEEDS-LIT theorems not found in the literature as stated; T-PERIODIC-CURVE (A) implied by Tillmann–Yao; the N₄₅ from-scratch reading declined, with its reason

**Verdict: PROVED** (a literature and verification arc; it clears R62-2 at its second carry). cc (main), 2026-10-09. The
literature search was done by a research agent (a subagent of this session) with web search; its references were
spot-checked on main. Every "not found" below is a negative from a bounded search, not a proof of novelty, and the
registry keeps NEEDS-LIT where that is the honest status. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /literature check|NEEDS-LIT|Lemma F|half lives|Menal-Ferrer|Tillmann/: 8 of 1394 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 6)`
— the four theorems' arcs (B1438, B1440, B1444, B1445); the SM seat's sm:B1544 (Lemma F) and sm:B1545 (F′); B1494 (N₄₅
rebuilt on main); B1604 (T-NO-INDEX-IN-THREE). **Literature:** as listed in §1.

## 1. What was found

| statement | verdict | the nearest literature | references checked on main |
|---|---|---|---|
| **T-RANK-BOUND** (B1440) | **not found in this form** | The inputs are standard: half lives, half dies (the restriction image is Lagrangian for self-dual coefficients — Heusener–Porti, *Infinitesimal projective rigidity under Dehn filling*, Geom. Topol. 15 (2011), arXiv:0908.2863, Lemma 5.3) and the Wang/LHS sequence of the fibration. The half I ≤ n − r is immediate from h⁰(∂N; V*) ≤ n − r; the half \|I\| ≤ r uses the fibre. Daly (arXiv:2411.04431, 2024) uses the same LHS route for projective rigidity without the bound | Daly's paper exists as cited (fetched) |
| **T-SLOPE-LAW** (B1438) | **related, not the same** | Dedekind–Rademacher and Meyer functions evaluate the signature and η of torus-bundle monodromies over the same continued-fraction word (Atiyah, *The logarithm of the Dedekind η-function*, Math. Ann. 278 (1987); Kirby–Melvin, Math. Ann. 299 (1994)). That is not the slope of an H¹(M; χ) class. The nearest framework is Dubois–Yamaguchi, AGT 12 (2012), arXiv:1107.3283 | Atiyah, Kirby–Melvin known to main |
| **T-PERIODIC-CURVE** (B1444) | **(A) implied; (B) not found** | (A): Tillmann–Yao, *On the topology of character varieties of once-punctured torus bundles*, Algebr. Geom. Topol. 25 (2025) 5389–5437, arXiv:2206.14954, Proposition 17. A diagonal character lies on exactly one curve of irreducible characters, transversely, at a simple root of a twisted Alexander polynomial. With Heusener–Porti, AGT 5 (2005), arXiv:math/0411365. Their hypotheses must be matched to the record's (the stable letter's eigenvalue) before citing. (B), the first-order torsion formula: nearest is Yamaguchi's limit of non-acyclic torsion at a simple root (order zero, knots; arXiv:math/0512277) | Tillmann–Yao fetched, journal reference confirmed |
| **T-MASS-TERM** (B1445) | **not found** | nothing on the second-order torsion of a product of deforming representations at a reducible point; nearest is the torsion-as-a-function survey (Porti, arXiv:1511.00400) | — |
| **Lemma F** (sm:B1544) | **related, not the same** | Menal-Ferrer–Porti, *Twisted cohomology for hyperbolic three manifolds*, Osaka J. Math. 49 (2012), arXiv:1001.2242, Theorem 0.1: for ρ_n (n ≥ 2) the restriction to the cusps is injective with image of half dimension. No source treats the extension W or a bound k − m − 1 | known to main |

## 2. Lemma F's step (2), verified on main

The agent raised a caution: step (2), h⁰(T; W*) = 2 at every cusp, seemed to fail. Its hand computation took ρ to be the
two-dimensional holonomy lift, because main's brief described it so. **That was main's error in the brief.** In sm:B1544
ρ is the seat's *four*, which is real (ρ̄ = ρ, its §2): the Lorentz action X ↦ gXg* on Hermitian 2 × 2 matrices. Checked
by hand on main:
- for a parabolic g = [[1, z], [0, 1]], (gXg*)₂₂ = X₂₂, (gXg*)₁₂ = X₁₂ + zX₂₂ and (gXg*)₂₁ = X₂₁ + z̄X₂₂;
- the cocycle identity for the commuting pair then gives, on the (1, 2) and (2, 1) entries, z₁x⁽²⁾₂₂ = z₂x⁽¹⁾₂₂ and
  z̄₁x⁽²⁾₂₂ = z̄₂x⁽¹⁾₂₂, so both (2, 2) entries vanish when z₂/z₁ ∉ ℝ;
- the invariant functional X ↦ X₂₂ therefore kills c and lifts to W*, so h⁰(T; W*) = 1 + 1 = 2;
- the lift's sign cancels in ρ ⊗ ρ̄, so no cusp is non-positive for the four.

**Step (2) stands**, and Lemma F's proof is unchanged. Steps (1) and (3) were followed on the page at the harvest (row 897).

## 3. The N₄₅ reading from scratch: declined, with its reason

R62-2 asked main to recompute one of the seat's readings, N₄₅'s ζ⁰ eigenspace (interior part, generic class, (−1, −10)),
with main's own code. **Declined.** No claim on main rests on it:
- GENESIS records only N₄₅'s rebuild and its rooms (B1494, v1.20);
- B1604's T-NO-INDEX-IN-THREE shows that a class-index reading on a cover of a thread is not an index, so the reading
  carries no generation count;
- the weave's grade (B1606) derives the flavour three without it.

Main's reproduction by re-run (all 380 of sm:B1541's readings identical, row 894) stands as its verification.

## 4. Disclosed

- The search was a subagent's: about 25 queries, bounded, with two closest classical PDFs unreadable to it. "Not found"
  is that search's result.
- References were spot-checked on main by fetching Tillmann–Yao's and Daly's arXiv pages; the others are standard and
  known to main. The agent's theorem numbers come from its reading of the papers. Lemma 5.3 and Proposition 17 should be
  re-read before any citation in a paper.
- Main's brief misdescribed the seat's ρ (§2). The agent's caution followed from the brief, not from the seat's text.

## 5. Files

This page; the registry's lit-status column for the four theorems (`docs/THEOREM_REGISTRY.md`); harvest row 897's status.
Lock: `verification/test_b1623_the_owed_literature_checks.py`.
