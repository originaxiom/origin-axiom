# Memo 221 — MEMO 210's TWO QUESTIONS ANSWERED: the linear coefficient is exact, and the constant is not a constant

**Certificate:** `outside_bench/certificates/mueller_answers_memo210.py` ·
**Output:** `outside_bench/outputs/mueller_answers_memo210.txt`
**No seal** — verification of a banked computation against statements **read verbatim** from
two papers the owner supplied on 2026-09-13, both previously `EGRESS_BLOCKED` (memo 219):

- **[Mül]** W. Müller, *"The asymptotics of the Ray-Singer analytic torsion of hyperbolic
  3-manifolds"*, **arXiv:1003.5168v1**, 26 Mar 2010.
- **[MFP]** P. Menal-Ferrer, J. Porti, *"Higher-dimensional Reidemeister torsion invariants
  for cusped hyperbolic 3-manifolds"*, **arXiv:1110.3718v2**, 16 Apr 2013.

---

## 1. What memo 210 left open

On B581's six **exact** torsions it fitted `log|τ_m| = A·m² + B·m + C` and measured
`A/(Vol/π) = 1.000781734`, `B/(Vol/π) = 0.9861960956`, then asked: **is the linear
coefficient exactly Vol/π, and what is C?** It explicitly declined to identify C, on the
grounds that four significant figures cannot support an identification.

## 2. Q1 — the combination is `m(m+1)`, exactly, and it is a theorem

**[Mül]'s Corollary 1.2**, verbatim — *"−log τ_X(τ_m) = (vol(X)/4π)·m² + O(m)"* — gives only
`O(m)` and does **not** pin the linear coefficient. But his **own sharp formula at the end
of §8** does, and here his `τ_{2m} = Sym^{2m}`, so **his m is our m**:

> **`log T_X(τ_{2m}) = log T_X(τ₄) + Σ_{k=3}^{m} log |R_{2k}(k)| − (1/π)·vol(Γ\H³)·(m(m+1) − 6)`**

**[MFP] eq. (2)** quotes the same and adds that the sum is *"uniformly bounded on k."*

> **The combination is `m(m+1)`, exactly.** Memo 210 *fitted* it at `B/(Vol/π) = 0.9861960956`.
> The theorem makes it **1**.

## 3. The scope, which is the part that matters

**[Mül] Theorem 1.1: *"Let X be a CLOSED, oriented hyperbolic 3-manifold."*** And [MFP],
who do the cusped case, prove the **leading term only**:

> *"lim_{k→∞} log|T_{2k+1}(M)| / (2k+1)² = − Vol(M)/4π"*

**The figure-eight complement is cusped.** So the `m(m+1)` refinement is **not established
for our object** by either paper.

> **INTERPRETIVE.** That makes memo 210's measurement better than a citation would have
> been: **six exact integers on a cusped manifold obey a closed-manifold refinement to a
> spread of 0.0123** — evidence for an extension nobody in these two papers proves, and a
> precisely stated target for someone who could.

## 4. Q2 — C is not a constant, and that is why it would not identify

[Mül]'s formula names it: `log T(τ₄) + 6·Vol/π + Σ_k log|R_{2k}(k)|` — a **bounded**,
**decaying** Ruelle sum (his Lemma 8.1: `log|R(k,σ_{2k})| ≤ C`, with the bound
`≤ C₁ ΣΣ e^{−3nℓ(γ)}/n`).

**So memo 210's residual was never going to be a constant** — and the drift it measured and
flagged as unexplained is that sum converging. **Consecutive exponents extract the Ruelle
terms directly:**

| step | increment | the Ruelle term |
|---|---|---|
| m = 4 → 5 | `R₅ − R₄ = −0.0104577255` | **`log\|R₁₀(5)\| = +0.0104577255`** |
| m = 7 → 8 | `R₈ − R₇ = +0.0002468702556` | **`log\|R₁₆(8)\| = −0.0002468702556`** |

> **The decay rate is the Ruelle rate.** Ratio of magnitudes across three steps:
> **42.361**, against `e^{3ℓ₀} = 26.081` and `e^{3.5ℓ₀} = 44.914` at the systole
> `ℓ₀ = 1.087070144995739` (SnapPy). Between `e^{−ℓ₀}` and `e^{−1.3ℓ₀}` per step.
>
> **And the sign flips** — `−0.01046` then `+0.0002469`. The geodesics carry imaginary parts
> (`±1.7228i` at the systole), so the terms oscillate. **A constant cannot change sign; a
> Ruelle sum must.**

## 5. What this says about memo 210's discipline

Memo 210 wrote: *"THE CONSTANT IS NOT IDENTIFIED, AND NO IDENTIFICATION IS ATTEMPTED … four
figures cannot support an identification, and this bench has a banked precedent for exactly
that overreach (B583's X2, a PSLQ-null overclaim)."*

> **The refusal was right for a better reason than it knew.** There is no constant to
> identify. Any PSLQ hit on `−0.4636` would have been a numerical coincidence fitted to the
> partial sum of a convergent series — the exact failure mode B583's X2 was retracted for.

## 6. Filed

| memo 210 asked | answer | scope |
|---|---|---|
| is the linear coefficient exactly `Vol/π`? | **YES** | proved by [Mül] **for closed** manifolds; **unproved for the cusped 4₁**, where the bench's six exact integers obey it to 0.0123 |
| what is the constant `C`? | **there is no constant** | `log T(τ₄) + 6Vol/π + Σ log\|R_{2k}(k)\|`, bounded and decaying; the measured drift is that sum |

**Memo 210 is corrected by addendum, not rewritten:** its cells, numbers and outcomes stand;
its two "successors registered, neither claimed" are now answered, one with a scope caveat
that makes the bench's own measurement the live contribution.
