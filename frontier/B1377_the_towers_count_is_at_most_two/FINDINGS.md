# B1377 — THE TOWER'S COUNT IS AT MOST TWO IN ONE BACKGROUND, AND IS ONE: on every level of the tower where every rank-one character has h¹ ≤ 1 — verified here on the complete character groups of Y₂–Y₆ (57 564 characters, h¹ ∈ {0, 1} on all, 509 with h¹ = 1) — the extension sequence bounds the doublet module's a₁ by 2 and the one-cusped index by |I| ≤ 2, so three generations in one background are impossible there; and every firing doublet module on levels two, four, five and six (16, 976, 4 400, 10 816 of them) has (a₁, r₁) = (1, 0) on one side and (2, 2) on the other, which is why B1375's count is exactly one

> **Harvested from main (2026-09-26, main @ `987c0c8f`): the instrument limit below is closed on main.** Main's B1427 (2026-09-18)
> solved h¹ ≥ 1 and h¹ = 2 exactly over the whole of Hom(H₁, ℂ*) — gcd of the Fox Jacobian's 2×2 minors and entries over ℚ(ζ_e) —
> for n = 2…7: **h¹ = 2 occurs on no component of any level, including M₇**, and not only on finite-order characters. So this
> arc's bound (|I| ≤ 2 in one doublet sector, and |I| = 1 on every firing module) holds on every rank-one character through
> level seven, the two non-torsion loci per level included; main's qualification (2) to B1375 states exactly this arc's bound.
> Cited, not re-derived here.

> **Notation correction (2026-09-26, B1379; E72).** Y₂–Y₆ below are the **cusped** covers of m004 — now **M₂–M₆** — not B1301's closed branched Yₙ. The bound and the dimension pattern stand, on Mₙ.

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the bound on the levels computed; the dimension pattern) · **Fence:** as B1374/B1375 — main's index on a non-semisimple background, no physics reading · **Price: unchanged** · **Numbering:** B1377 (sL-2 (ii), the reason behind the one-per-background law).

## 0. Seen from above

B1375 found that every generation-shaped background on Y₄, Y₅, Y₆ carries exactly one net generation. This arc says why, and how far the
"why" reaches. A firing doublet sector is V = ρ_χ ⊗ ψ, an extension 0 → χψ → V → χ⁻¹ψ → 0 of rank-one modules; the long exact sequence
gives a₁(V) ≤ a₁(χψ) + a₁(χ⁻¹ψ), and n(V) = a₁ − r₁ ≤ a₁, n(V*) ≥ 0, so I = n(V) − n(V*) ≤ a₁(V), and symmetrically −I ≤ a₁(V*). If
every rank-one character of the level has h¹ ≤ 1, then |I| ≤ 2 on every doublet sector of every background — a count of three in one
background is impossible. The hypothesis is checked here on the complete character groups Hom(H₁, μ_N), N = lcm(12, torsion exponent),
of Y₂–Y₆: 300 + 192 + 2 700 + 15 972 + 38 400 = 57 564 characters, h¹ = 0 or 1 on every one (5 + 16 + 45 + 123 + 320 with h¹ = 1; every
non-zero value re-checked over two more primes, the four "differences" on Y₅ being spurious ranks of the smallest prime 661, absent on
1321 and 1453). And the actual firing modules do better than the bound: on every firing doublet module of Y₂, Y₄, Y₅, Y₆ the dimensions
are (a₁, r₁) = (1, 0) for V and (2, 2) for V*, or the reverse — one interior class on one side and none on the other — so |I| = 1 exactly,
which is B1375's law. Beyond level six the bound needs h¹ ≤ 1 on that level's characters, which B1301–B1303 computed on the eigencharacters
of the levels they swept and which the same instrument decides in seconds per level.

## 1. Computed

`verification/rank_one_bound.py` (record `rank_one_bound_run.txt`); the firing dimensions from B1375's `tower_generations.py`
(`tower_generations_run.txt`, the "firing modules' (a_1, r_1, a_1*, r_1*)" field).

| level | characters into μ_N | h¹ = 0 | h¹ = 1 | h¹ ≥ 2 | re-checked (two more primes) | firing doublet modules: (a₁, r₁, a₁*, r₁*) |
|---|---|---|---|---|---|---|
| Y₂ (N = 60) | 300 | 295 | 5 | 0 | 5, 0 differing | 16: (1,0,2,2) × 8, (2,2,1,0) × 8 |
| Y₃ (N = 12) | 192 | 176 | 16 | 0 | 16, 0 | none fires |
| Y₄ (N = 60) | 2 700 | 2 655 | 45 | 0 | 45, 0 | 976: 488 + 488 |
| Y₅ (N = 132) | 15 972 | 15 849 | 123 | 0 | 123, 4 differing (spurious rank drops on the prime 661; 0 on 1321, 1453) | 4 400: 2 200 + 2 200 |
| Y₆ (N = 120) | 38 400 | 38 080 | 320 | 0 | 320, 0 | 10 816: 5 408 + 5 408 |

## 2. The bound

**Lemma.** Let V be an extension 0 → L₁ → V → L₂ → 0 of rank-one local systems on a one-cusped M. Then a₁(V) ≤ a₁(L₁) + a₁(L₂), and
I(V) = n(V) − n(V*) satisfies −a₁(V*) ≤ I(V) ≤ a₁(V). *Proof.* H¹(M; L₁) → H¹(M; V) → H¹(M; L₂) is exact; n = a₁ − r₁ ≤ a₁ and n ≥ 0.

**Corollary.** On a level where every rank-one character has h¹ ≤ 1, every doublet sector has |I| ≤ 2, and a background's net count of any
Standard-Model representation is at most two in absolute value. On Y₂–Y₆ the hypothesis holds on the complete torsion character groups.

**Observation.** The firing modules realise (a₁, r₁) = (1, 0) against (2, 2): the side with two classes restricts injectively to the cusp
(r₁ = 2 = t₁ − r₁* with r₁* = 0), the side with one class is interior. |I| = 1 on all of them. Whether (2, 0) against (·, ·) — a count of
two — can occur on a higher level is not excluded by the lemma and not seen.

## 3. What it means

1. **Three generations never in one background on the tower's computed levels** — by a theorem whose only input is h¹ ≤ 1 for rank-one
   characters, which is what the tower's cyclic Alexander module makes plausible everywhere (B1301–B1303 on the eigencharacters of every
   level swept) and what is verified here on the full character groups of Y₂–Y₆.
2. **One is the observed law, two the bound.** If the programme's three is to come from this mechanism, it must come from three
   backgrounds or from outside the tower; the class's one-cusped siblings gave no generation at all (B1374).
3. **What would extend it.** The same rank-one sweep on Y₇–Y₁₂ (seconds to minutes each) turns the corollary into a statement about
   those levels; a proof of h¹ ≤ 1 from the cyclic Alexander module would make it a theorem for the whole tower.

## 4. Caveats

Prime fields with the same discipline as B1374–B1375 (three primes; a rank can only drop, so h¹ can only rise modulo p; the maximum over
the two larger primes is the value reported). The lemma is elementary; the corollary's hypothesis is verified, not proved, on the levels
listed.

## Verification

`verification/rank_one_bound.py [n ...]`. Lock: `tests/test_b1377_the_towers_count_is_at_most_two.py` (fast: Y₂, Y₃, Y₄; slow: Y₅, Y₆).

**Sources.** B1375 (the count and the firing dimensions), B1374 (the sectors and T5), B1301–B1303 (the tower's rank-one cohomology),
main's B1297 (the index).
