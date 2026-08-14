# B953 — E₆ vs E₄, AND THE TWO SEEDS: we are on the achiral one, and switching is not a fix

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Directive:** *"lets figure out e6 vs e4, and is it possible there are plus and minus
seeds and we're at the wrong one, where matter is absent by construction."*

---

## 1. E₆ vs E₄ — the series, and why the skip matters

"E₄" is a real object: the **E_n series** (del Pezzo / M-theory convention) continues below
E₆ as

| | | rank |
|---|---|---|
| E₆ | E₆ | 6 |
| **E₅** | **D₅ = SO(10)** | 5 |
| **E₄** | **A₄ = SU(5)** | **4 ← the rank of the Standard Model** |
| E₃ | A₂×A₁ = SU(3)×SU(2) | 3 |

**E₄ = SU(5) is exactly the rank-4 member.** Now the rank bookkeeping of the standard
descent:

| step | rank | what is shed |
|---|---|---|
| E₆ | 6 | — |
| → SO(10) = E₅ | 5 | **U(1)_ψ** |
| → SU(5) = E₄ | 4 | **U(1)_χ** |
| → SM | 4 | **nothing — RANK-PRESERVING** (adjoint VEV) |

Two facts follow immediately, and together they explain B952's obstruction:

1. **SU(5) → SM is rank-preserving**, so a centralizer *can* perform that last step. The
   cascade is not incapable in general.
2. **The rank reduction lives entirely in E₆ → SO(10) → SU(5)** — and B892's own headline
   is that the second measurement **skips SU(5)**.

> **Skipping SU(5) IS skipping the rank reduction.** The two units of rank the cascade
> cannot shed are precisely **U(1)_ψ and U(1)_χ** — the standard E₆ extra abelian
> directions. That is almost certainly what the object's u(1)³ is:
> **u(1)_Y ⊕ u(1)_χ ⊕ u(1)_ψ.** (Testable; it is exactly what L132's scouting panel is
> sent to establish.)

## 2. The ± seeds — the hypothesis is CONFIRMED, and it is already banked

There are two branches, and the record named them a month ago. **B576:**

> *"Any integrable deformation with nonzero θ-odd component has Zariski closure all of E₆
> and is chiral; θ-even deformations stay F₄-stable and vector-like."*
> *"**The geometric point sits on the F₄-stable (achiral) stratum.**"*

**So yes: there are plus and minus seeds, and we are on the one where chiral matter is
absent by construction.** That is not a new suspicion — it is banked, in those words.

Supporting: **B714** (the object authors a **vector-like** E₆ skeleton), **B713**
(chirality is not in the amphichiral object), **B582** (chiral matter *was* constructed —
but on the θ-odd twisted mirror-double, i.e. the other branch).

## 3. THE NEW PART — the rank reading, and why switching does not help

θ is the outer involution of E₆, and its split is exact:

> dim E₆ = 78 = **52 (θ-even = F₄)** + **26 (θ-odd)**, and **rank F₄ = 4**.

**rank F₄ = 4 = rank of the Standard Model.** Moreover F₄ ⊃ SU(3)×SU(3) ⊃
SU(3)×(SU(2)×U(1)) = the SM gauge algebra, **all at rank 4**. And every F₄ representation
is **real** — which is precisely why the θ-even branch is vector-like.

So the two seeds have **exactly complementary defects**:

| branch | algebra | rank | rank OK? | chiral? | verdict |
|---|---|---|---|---|---|
| **θ-even** | **F₄** | **4** | **✅ right rank** | ❌ all reps real | **matter absent by construction** |
| **θ-odd** | **E₆** | 6 | ❌ B952's obstruction | ✅ the 27 is complex | **right matter, wrong rank** |

> **You cannot fix this by changing seeds.** The branch we are on has the *right rank* and
> no chirality. The other branch has *chirality* and rank 6 — which is exactly the
> obstruction B952 proved. **Each branch is missing precisely what the other has.**

That is the sharpest statement the programme can currently make about its own position,
and it is worse news than the hypothesis it answers: the "wrong seed" reading suggests a
fix by relocation, and there is none.

## 4. What this makes precise — the requirement, stated exactly

Combining §1 and §3, what is needed is now a single sentence:

> **A rank-reducing mechanism that is NOT the θ-projection.**

θ-projection reduces rank 6 → 4 and kills chirality (it lands in F₄). The GUT chain reduces
rank 6 → 4 and *keeps* chirality (it lands in SU(5) with a complex 27) — but it does so by
**Higgs VEVs**, i.e. requirement #11 of the GUT ledger, which the object does not supply.

**L133 is sharpened accordingly:** the question is not merely "does the object supply any
rank-reducing structure" but "**does it supply one that is not θ, and that preserves the
27's complexity?**" A Wilson line / Hosotani flux is the candidate worth checking first,
because the object has a fundamental group and a cusp, and the banked literature map
records centralizer-of-holonomy as one of the forced mechanisms for the unbroken subgroup.

## 5. Honest limits

1. **The u(1)³ = u(1)_Y ⊕ u(1)_χ ⊕ u(1)_ψ identification is INFERRED from the rank
   bookkeeping, not computed.** It is the natural reading and it is testable; it is not
   established here. L132's panel is scouting the literature for how that identification is
   conventionally made.
2. The F₄ facts used (rank 4; 78 = 52 + 26; SU(3)×SU(3) ⊂ F₄; all F₄ reps real) are
   **standard Lie theory, cited not re-derived**. The arithmetic is checked in
   `results.json`; the representation-theoretic facts are not re-proved.
3. **This does not refute anything.** B576, B714, B582, B892, B952 all stand unchanged.
   What is new is the *rank* reading of the θ-split and the resulting complementarity.
4. Whether some third structure evades the dichotomy (a subgroup that is neither F₄ nor all
   of E₆, at rank 4, with complex reps) is **not excluded here** — SU(5) itself is such a
   thing. The point is that the *object's own operations* do not reach it.

---

**Verdict: the hypothesis is confirmed and sharpened into worse news.** There are two
seeds; the geometric point sits on the achiral one (banked, B576); **but the seeds have
complementary defects — F₄ gives rank 4 without chirality, E₆ gives chirality without
rank 4 — so switching seeds is not a fix.** What is required is a rank-reducing mechanism
that is not θ and that preserves the 27's complexity. E₄ = SU(5) is exactly the rank-4
waypoint the cascade skips, and skipping it is skipping the rank reduction.
