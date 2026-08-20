# B1098 — THE HATCH OPENS: the object's own holonomy, taken non-abelianly, breaks E₆ to the trinification remnant su(3)⊕su(3) ⊇ SM at rank exactly 4

**Date:** 2026-08-20 · **Verdict: PROVED (the sl₂-factored stratum decided; the hatch OPENS with two named landings; the pre-registered outcome grammar's positive branch)**
**The cell:** W1 of the closing campaign — THE RANK WALL's single live hatch (B1094:
non-abelian holonomy), first stratum: holonomies factoring π₁(M) → SL(2,ℂ) → E₆.

## 1. The stratum, completely enumerated (saturation 20/20)

Every such holonomy lands in an sl₂ conjugacy class = a nonzero nilpotent orbit of e₆.
The enumeration was CONSTRUCTIVE (Levi regular nilpotents over all 31 simple-root
subsets + a saturation-gated random search inside the big Levis for the distinguished
non-regular orbits), deduped by fast invariants with every BANKED number exact
(sympy over ℚ on the corpus-verified Chevalley e₆; the B1087-pattern JM solver, triple
relations verified exactly per class; centralizers as exact 234×78 nullspaces).
**Twenty classes found — saturating the CITED count (Bala–Carter) — and every
centralizer (dim, rank, type) matches the standard table** (a₅ 35/5; b₃+u(1) 22/4;
a₂⊕a₂ 16/4; g₂ 14/2; a₂+a₁ 11/3; b₂+u(1) 11/3; a₂+u(1) 9/3; a₂ 8/2; a₁+u(1) 4/2 ×3;
a₁ 3/1 ×2; u(1)² 2/2; u(1) 1/1 ×3; 0 ×3) — the class naming is by invariant match,
with node adjacency inferred self-consistently from the computation itself.

## 2. THE LEMMA that makes the table physical (density)

The object's hyperbolic ρ: π₁ → SL(2,ℂ) is irreducible and non-elementary (banked:
tr[A,B] = 3/2 + (√3/2)i ≠ 2, the B1086-record verification), hence its image is
Zariski-dense in SL(2,ℂ) (CITED-standard). Therefore for ANY algebraic φ: SL(2) → E₆,
the centralizer of the composed holonomy (φ∘ρ)(π₁) equals the centralizer of φ(SL(2))
= the sl₂-triple centralizer. **The table's rows ARE the unbroken gauge algebras of
the object's own composed holonomies.**

## 3. THE VERDICT — the hatch opens, twice

| class | unbroken algebra | rank | SM verdict |
|---|---|---|---|
| **A2** | **su(3) ⊕ su(3)** | **4** | **SM-COMPATIBLE AT RANK EXACTLY 4**: color in one factor, su(2)×u(1) inside the other — zero extra u(1)s |
| A1 (minimal) | su(6) | 5 | SM-compatible with ONE extra u(1) (the (3,2) embedding su(6) ⊃ su(3)⊕su(2)⊕u(1)) |
| 2A1 | so(7) ⊕ u(1) | 4 | **excluded**: no su(2) commutes with any su(3) inside so(7) (su(3) ⊂ g₂ or ⊂ su(4)≅so(6) has commutant ≤ u(1); rank budget exhausted) |
| the other 17 | — | ≤ 3 | below the SM rank |

**THE TRINIFICATION READING.** e₆ ⊃ su(3)³, and the A2-class sl₂ is the principal sl₂
of one su(3) factor; the exact dimension equality 16 = 8 + 8 proves the sl₂-triple's
centralizer EQUALS the full factor's centralizer — **the object's own geometry, taken
through the 3-dimensional representation, eats exactly one trinification factor and
leaves su(3) ⊕ su(3).** The wall's holonomy face, closed twice over for abelian
holonomy (B1094), is OPEN at the first non-abelian stratum — and not by an exotic
choice: by the smallest faithful representation of the object's own fundamental group.

## 4. The honest fences (each one load-bearing)

1. **The class is a priced choice, not a derivation**: φ's class is 1 of 20 (log₂20 ≈
   4.3 bits; 2 of 20 land; the exact-rank landing is 1 of 20 ≈ 4.3 bits spent) — the
   freedom ledger carries it. No dynamical mechanism selecting A2 is claimed.
2. **Hypercharge not yet matched**: whether B970's banked Y direction sits correctly
   inside the second su(3) is THE FOLLOW-ON CELL (B1100: the 27's branching under
   sl₂^{A2} ⊕ su(3) ⊕ su(3), the broken matter content, the charge-table match).
3. **Chirality untouched**: the four-language wall stands — this is rank/gauge
   structure, not a chirality mechanism. EWSB remains outside.
4. **Prior-art adjacencies declared**: B854 (the FINITE 2T-centralizer u(1)⁴ — rank 4
   abelian; the sl₂ stratum shows what CONTINUOUS holonomy buys at the same rank:
   non-abelian su(3)²); B932 (finite-order measurement walls; its GUT-chain grammar
   row concerned a different door — the B1079 scope addendum already bounds it; this
   arc's trinification lane enters by holonomy, which B932 never swept).

## 5. Verification

Independent own-code agent re-derivation COMPLETE, all claims PASS, cross-validated
THREE ways (native bracket; exact DomainMatrix; a from-scratch pure-Python modular
engine over three large primes): the three sl₂-triples exact; all nine dim/rank/center
numbers (35/5/0, 22/4/1, 16/4/0); **the a₂⊕a₂ split EXHIBITED** (two commuting simple
8-dim rank-2 ideals — by a primary-decomposition method the verifier pre-validated on
synthetic sl₃⊕sl₃ data with known ground truth, catching its own first-version bug
before touching the real algebra); **the su(2)×u(1) inside the second factor
EXHIBITED concretely** (an explicit intrinsic sl₂-triple in I₂ with 1-dimensional
centralizer, commuting with the entire first ideal — the SM chain's electroweak seat
constructed, not asserted); the 2A1 semisimple part confirmed SIMPLE (dim 21, rank 3).
Verifier's honest caveat, adopted: dim+rank+simplicity alone cannot distinguish b₃
from its dual c₃ for that row — **and the exclusion survives either reading** (sp(6)'s
su(3) also has commutant ≤ u(1): no 4-dim symplectic su(3)-rep exists, so no su(3)
fits inside an sp(4) factor and the diagonal embedding exhausts the rank), so the
2A1 exclusion is type-label-independent. **Locks:** tests/test_b1098_nonabelian_hatch.py (the three
rows' dims/ranks from stored + a live A2 recomputation; the saturation count).

## 6. What this does to THE RANK WALL's sentence

Old: one slot, pair-space, purity-conditioned, arithmetically unobstructed; open =
the counter + the non-abelian hatch. **New: the non-abelian hatch is OPEN at its
first stratum — the object's own holonomy reaches su(3)⊕su(3) ⊇ SM at rank exactly
4. The wall's remaining questions: the matter content at the landing (B1100), the
class-choice's price, and Route A's frontier counter (B1099).**

## ADDENDUM 2026-08-20 — the relation to B959, stated (the audit seat's flag; one day later, computed)

B959 ("every route to rank 4 makes the 27 real; no centralizer construction whatsoever
— measurement, holonomy, or finite image — can deliver chiral matter at the SM's
rank") is PRIOR ART this arc's stratum sits OUTSIDE, twice over: B959's §4 mechanism
is Steinberg torality on SEMISIMPLE elements of the object's FINITE images (A₄, D₅,
S₅; simply connected form; its own §5 names its boundary), while this arc's holonomy
is CONTINUOUS (the Zariski-dense hyperbolic ρ — no finite quotient) and
NILPOTENT-generated (su(3)⊕su(3) contains no maximal torus; the torality machinery
never engages — the B1074/B8074 nilpotent gap). B1100 then computed what B959's
sentence asserts cannot happen: **the 27 is COMPLEX at this landing, exact, witnessed**
— falsifying the headline BEYOND its toral scope while leaving its proof untouched on
its own ground. The re-scope addendum sits beside B959; the audit seat's
state-the-relation flag is credited as the trigger.

