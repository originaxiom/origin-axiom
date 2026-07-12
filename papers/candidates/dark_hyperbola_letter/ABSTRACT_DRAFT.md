# CC header (2026-07-12) — status, corrections, and the one gate

**Provenance:** seat draft (target: Letters in Mathematical Physics), banked
as candidate PC22. The seat text is preserved verbatim below; this header
records what changed and what blocks submission.

**Status against the repo (B534, this session):**
- Dark hyperbola: **PROVED all odd primes** (complete Gauss-sum derivation +
  exact integer-count verification at 12 primes; `frontier/B534_dark_hyperbola`,
  `tests/test_b534.py`).
- Power-set magnitudes: **PROVED for square-free N via CRT** (exact at N=15
  over ℤ[ζ₁₅]) — stronger than the draft's "verified 3 levels, proof
  outlined." Update the abstract accordingly.
- Asymptotic darkness: **PROVED** (Mertens).

**Two framing corrections (firewall-honesty, must land before submission):**
1. "a geometric **proof** of the infinitude of primes" → "a metaplectic
   **restatement of Euler's argument**." The product ∏(1−(p−2)/p²)→0 is
   *equivalent to* Σ1/p diverging (Euler), not an independent new proof; if
   there were finitely many primes the product would be a positive constant.
   It repackages Euler, it does not re-prove infinitude from new axioms.
   Overclaiming this in a math letter is exactly the kind of thing a referee
   kills. State it as a restatement.
2. Keep the "no figure-eight / no Origin Axiom / no physics" discipline — the
   seat already has this right; the three theorems stand as pure rep theory.

**THE GATE (blocks submission; not yet run):** a literature search SPECIFIC to
this object — the parity-twisted trace of the Weil representation and its
Gauss-sum vanishing locus. The B543/B546 gap-labeling lit-gate does NOT cover
this; it is a different object. Prior art to clear before claiming novelty:
Lion–Vergne, Gurevich–Hadani (Weil rep / oscillator), Bump (automorphic),
and the quadratic-Gauss-sum / metaplectic-character-sum literature. Only this
search decides whether the letter is a contribution or a re-derivation. Queue
it on the cost-tiered deep-research script (see memory: subagent-model-tiering)
when quota allows.

---

# DRAFT ABSTRACT
## Target: Letters in Mathematical Physics
## Title options below — choose one

---

### Title Option A:
**The vanishing geometry of the metaplectic seam at prime and composite levels**

### Title Option B:
**Dark hyperbolas and power-set magnitudes in the Weil representation**

### Title Option C:
**Zeros and magnitudes of the parity-twisted trace in the Weil representation**

---

### Abstract (196 words):

We study the function $S(j,l) = \mathrm{tr}(\Pi \cdot W_1^j \cdot W_2^l)$ on $(\mathbb{Z}/p)^2$, where $W_1, W_2$ are the standard generators of the Weil (metaplectic) representation at odd prime level $p$ and $\Pi$ is the parity involution $n \mapsto -n$. We prove that $S(j,l) = 0$ if and only if $jl \equiv -4 \pmod{p}$ and $j \neq 2$, giving exactly $p - 2$ zeros arranged on a hyperbola with a single exempt point at $(2, p-2)$. The constant $-4$ arises from the quadratic Gauss sum structure of $W_1$; the exemption at $j = 2$ is the unique evaluation where the linear character in the completed square vanishes.

At composite square-free level $N = p_1 \cdots p_k$, the Chinese Remainder Theorem factorizes $S$ as a product of per-prime contributions. We prove that the nonzero values of $|S|$ are exactly $\{\sqrt{\prod_{p \in T} p} : T \subseteq \{p_1, \ldots, p_k\}\}$, a power-set structure with $2^k$ distinct magnitudes. As a corollary, the fraction of nonzero evaluations satisfies $\prod_p (1 - (p-2)/p^2) \to 0$ over all primes, giving a geometric proof of the infinitude of primes via the metaplectic representation.

---

### Keywords:
Weil representation, metaplectic group, Gauss sums, parity involution, quadratic residues, Chinese Remainder Theorem

### MSC 2020:
11F27 (Theta series; Weil representation), 11L05 (Gauss and Kloosterman sums), 11T24 (Other character sums and Gauss sums), 20C15 (Ordinary representations and characters)

---

### Notes for CC before submission:

1. The abstract states three results: dark hyperbola (B534 proved), power-set magnitudes (verified 3 levels, proof outlined), asymptotic darkness (follows from Mertens). All three must have COMPLETE proofs before submission.

2. The letter should be ~10 pages: statement of results (2 pages), proofs (5 pages), verification tables (2 pages), discussion (1 page).

3. NO mention of the figure-eight knot, the Origin Axiom program, or physics. The results are pure representation theory / number theory. The figure-eight motivated the discovery but doesn't appear in the statements.

4. The one concern: these results might be KNOWN. The Weil representation is well-studied (Lion-Vergne, Gurevich-Hadani, Bump). The parity-twisted trace may have been computed before. CC's literature search (Phase 1.6 of the campaign) must complete before submission.

5. If the results ARE known: cite properly and reframe as "a new proof via the Gauss sum analysis" or withdraw.

6. If the results are NOT known: the letter is a clean, short contribution to the theory of the Weil representation, publishable regardless of any broader program.

---

# LIT-GATE VERDICT (2026-07-12, cost-tiered deep-research, 100/100 agents, 0 errors)

**Per-result novelty (adversarial, primary sources):**

1. **Dark Hyperbola — APPEARS-NOVEL as the explicit congruence, but Prasad-
   adjacent.** The specific "S(j,l)=0 iff jl≡−4 (mod p), j≠2, one exempt point
   (2,p−2)" was NOT found published. Its abstract PARENT is **Prasad 2009
   (arXiv:0903.1486, Cor 8.7)**: a necessary-and-sufficient vanishing criterion
   for automorphism-twisted Weil traces (tr W(σ)=0 iff the twist's conjugacy
   class is disjoint from Aut(K,e)), with |K^α|∈{1,p} (Thm 8.1) = our
   {1, √p}·magnitudes. Our dark hyperbola is the concrete Diophantine
   realization of Prasad's criterion for the PARITY twist — deriving the
   explicit congruence from the abstract criterion is substantial and
   unpublished. **Independent cross-check:** the verifier reproduced our zero
   set numerically at p=7,11,13 (jl≡−4, j≠2, exactly p−2 zeros, magnitudes
   {1,√p}). Confidence medium (2-1 on the Prasad-shape).
2. **Power-set magnitudes — KNOWN mechanism, novel packaging.** CRT-
   multiplicativity of Weil traces is classical (Gurevich–Hadani–Howe
   arXiv:0808.2447 Prop 3.2; Ladisch "well known"). The 2^k power-set is a
   corollary; the packaging as a magnitude power-set is the contribution.
3. **Asymptotic darkness — KNOWN** (Euler-product restatement; already
   corrected in the CC header above to "restatement of Euler's argument").

**Also settled:** the UNTWISTED finite Weil character is classical and never
vanishes where g−I is invertible (Thomas math/0610644 Thm 1A; Gurevich–Hadani
math/0610818 Thm 2.2.1; Howe 1973; Shinoda 1980) — so the zeros FORCE Par to be
a genuine twist outside the plain-character framework (Neuhauser 2002 gives the
even/odd splitting but never forms tr(Par·g) or its zero set). This is the
correct framing for the paper: the dark hyperbola exists BECAUSE the parity
twist leaves the canonical Weil-character regime.

**PAPER FRAMING (honest, novelty-cleared with citations):** the letter is "the
explicit Diophantine vanishing locus of the parity-twisted Weil trace" — a
concrete realization of Prasad's abstract criterion (cite Cor 8.7), with the
CRT power-set packaging (cite Gurevich–Hadani–Howe) and the Euler restatement.
NOT a wholly new theorem; a genuine explicit contribution requiring the Prasad
citation. **NEEDS-SPECIALIST** (a by-hand check that our congruence is Prasad's
Cor 8.7 for the parity twist). Submittable as an explicit-realization letter
with that framing; do NOT claim a standalone new vanishing theorem.
