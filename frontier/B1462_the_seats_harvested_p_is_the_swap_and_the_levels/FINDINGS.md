# B1462 — THE SEATS HARVESTED: P IS THE SWAP, THE MIRROR BREAKS ON THE LEVELS WHERE THE TWIST IS SINGLE-SHEET, AND GENESIS v1.7

**Verdict: PROVED** (a harvest arc with three re-derivations of its own; scope: F-HE on m004's harmonic family and its
levels M₁…M₆, reach *class* for the level computation, *single* for P's identification on m004; the adoption of GENESIS
v1.6 and of the bar's null contract frame-independent). cc (main), 2026-10-03. Pays L242 (b); registers L242 (e);
corrects one sentence of B1455's addendum and one of GENESIS FK12 (ii).

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "P is the swap|period-2 (symmetry|involution)|strong inversion|count-odd|golden
  (sheet|reflection|eigenline)|cyclic cover|Fox calculus|null contract|Bonferroni|Sidak|Šidák"`: *VERDICT topic-sweep: 28
  of 1334 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 21)*. Read where they bear: B1297 (P written as a ↦ a⁻¹, b ↦ a³b,
  "the rotational period-2 symmetry, axis disjoint from the knot", verified as −1 on Tors H₁(C₃) by Reidemeister–Schreier
  and by Fox calculus over ℤ[ℤ/3] — the instrument this arc generalises; its §8 cites the SM seat's identification of P
  with the hyperelliptic involution as "cited, not verified"), B1455 and its addenda (the symmetries of Ballas' family;
  the sentence corrected here), B1459 (ι̃ = −id on the fibre), B1518/B1458 (the bar as adopted). The SM seat's lane read
  at `48f6af3b`: sm:B1521–B1526 and its ten unrowed relays, all rowed (HARVEST_LEDGER 826–831; RELAY_LEDGER). The audit
  lane's reply of 2026-10-03, read (B1460). **Literature:** none new; Ballas' presentation and generators as in B1455.

## 1. P is the swap (sm:B1521 C1, re-derived; `verification/p_is_the_swap.py`)

SnapPy's ⟨a, b | aaabABBAb⟩ holonomy sends the relator to −I; a has exponent sum 1 in it, so a ↦ −a is a genuine
SL(2, ℂ) lift. With m = ab and n = aabA Ballas' relator holds and a = MnmN, b = nMNmm. B1297's P (a ↦ a⁻¹, b ↦ a³b)
becomes P(m) = a²b = MnmNm and P(n) = aba = nmN, and both equal conjugation by nM of the *swapped* generators:
**P = conj(nM) ∘ (m ↔ n).** Control: P(m) ≠ m with the same trace. So P fixes ρ_q (B1455's table has ρ_q∘swap ≅ ρ_q),
and the dualising symmetry of Ballas' family is the strong inversion ι: m ↦ m⁻¹, n ↦ n⁻¹. B1455's addendum of
2026-10-02 had identified ι with P; **addendum 3 corrects it**. B1459 is untouched: its ι̃ is −id on the fibre,
meridian-preserving, which *is* P, and it carries V to V*⊗ε by inverting the fibre character while fixing each SL(2)
factor's class — exactly what "P fixes ρ_q" says. GENESIS FK12 (ii)'s "P followed by dualising reverses the order"
(main's since v1.3) is withdrawn in v1.7: P alone reverses it; followed by dualising it fixes the module.

## 2. The levels (sm:B1522, re-derived on M₁…M₆; `verification/levels_count_odd.py`)

**Own route.** The eight symmetry classes of π₁(m004) in Ballas' presentation, found by search over maps m ↦ u, n ↦ v
(reduced words to length 4) that send the relator to the identity in the SL(2) holonomy and, exactly, in Ballas' SL(4, ℚ)
representation at q = 2, with the degenerate endomorphisms dropped by their character; classified by orientation (the
probe character kept or conjugated), the meridian sign ε, the longitude (kept or inverted under ρ₂ — inverted means
dualising, B1455) and the action on T₂ = ℤ/5. They are D4 as they should be: identity (+1 on T₂), P (−1), two strong
inversions (ε = −1, longitude inverted, T₂ ±1 — the dualising orientation-preserving classes), and four
orientation-reversing classes of order four (T₂ ×2, ×3), two with the longitude kept and two inverted. Transport to
SnapPy's generators (checked in the holonomy); H₁(M_n) = ker d₁/im d₂ of the Fox complex over ℤ[ℤ/n] (Shapiro; φ: a ↦ 0,
b ↦ 1 — the relator's exponent sums are a: 1, b: 0 — no Reidemeister–Schreier), with the induced map of each symmetry
semilinear by t ↦ t^ε and the deck lifts by conjugation with b; the kernel in Smith coordinates y = Vᵀx. **A twist ν_F of
T_n with λ generic off the circle is fixed by a count-odd map iff some lift β of a strong inversion satisfies ν_F∘β_* =
ν_F⁻¹ on T_n and ν_F(τ_β) = 1, β_*(z) = −z + τ_β** (for ε = +1 the free part forces |λ| = 1, and so does conjugating the
twist; coordinate-free, so no choice of z enters). Controls: T_n's invariant factors equal coker(Φⁿ − 1)'s; d₁d₂ = 0;
every induced map preserves ker d₁ and im d₂; the transported identity acts as the identity on H₁ (this control caught
the one real bug — the Smith coordinates had been read as V⁻¹x; before the fix the identity moved z by a torsion
element, which no inner automorphism can do).

**Result:** unfixed twists off the circle **0, 0, 0, 0, 20, 96 on M₁…M₆**, invariant factors 5; 4,4; 3,15; 11,11; 8,40 —
the SM seat's table exactly. **On M₅ the 20 are exactly the single-sheet twists**: the deck generator acts on T₅ = 𝔽₁₁²
with eigenvalues 5 and 9 (= φ², φ̄² mod 11, 11 split), and the unfixed characters are the eigenvectors of its action on
the dual, ten on each eigenline; no mixed twist is unfixed. This is sm:B1522's Lemma C with Lemma G in the M₅ case, by a
route sharing nothing with its two. M₇–M₁₂, Lemma F's closed counts and the 196 firing members' flags are read, not
re-derived. **L242 (b) is paid:** the count-odd mirror breaks on the levels, first on M₅, where the twist chooses a
golden sheet; and (the seat's P8, read) it breaks only where nothing chiral has been found.

## 3. The bar's null contract (sm:B1524; `verification/bar_contract_checks.py`)

Two of its numbers re-derived: the scan law 1 − C(N−K, n)/C(N, n) exceeds B1518's 1 − (1 − K/N)ⁿ for every n ≥ 2 (and
equals it at n = 1), so the binomial understated p (m369's scan: 0.98714 exact against 0.98575); and the Šidák
counterexample at the gate — two picks in a stratum of 399 with two carriers have exact size 0.0100125 > 0.01, Šidák's
0.00999 passes, Bonferroni's 0.01003 does not. The conservativeness of r under the census's own law and the size bound
are read. **Adopted into `docs/THE_BAR.md` as received** (sha `851e4754…`), under main's header; the top grade is PASSED, a
rarity screen; no grade on the record changed. This answers the audit lane's request of 2026-10-03.

## 4. GENESIS v1.7

sm:B1526's v1.6 was built on main's v1.5 as asked, additive, each item marked. Received (`received/GENESIS_v1_6_sm.md`,
sha `59ef40a6…`) and adopted by `adoption/amend.py` with four changes: the version line and intro; **FK12 (ii) corrected**
against B1459; the v1.7 log line (what was re-derived — P; the levels; two bar numbers — and what was read: sm:B1523's
Lemma R and T, the rest of sm:B1524, sm:B1525's items, sm:B1526's C2–C5).

## 5. Read, not verified, and what is owed

sm:B1523 (every word state's projective family; 262 mirror-broken manifolds) is registered, not re-derived; its ask —
a blind second-route run of main's class index on ±LLRLRR / ±L³RLR² after the seat seals — is **L242 (e)**. sm:B1521's
AR3–AR6 (B37, B130, B723) reached GENESIS through the seat's text; L243 (a) stays open on main. The SM seat's pin moves
to `48f6af3b`; ten of its relays rowed.

## 6. Errors in this arc

One, caught by its control before any number was read: the Smith-coordinate basis (V⁻¹x for Vᵀx). And the harvest came
a day after the seat's relays, behind three arcs of main's own.
