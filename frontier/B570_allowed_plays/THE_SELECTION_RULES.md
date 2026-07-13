# B570-AP6 — THE SELECTION-RULES THEOREM

**Cell:** AP6 (synthesis). **Date:** 2026-07-13 run (prereg 2026-07-14 entry, `frontier/B570_allowed_plays/PREREGISTRATION.md`). **Inputs:** verified cells AP1–AP5, C1–C4, C5QC, QA (all adversarially re-verified; verdicts and defects folded in below). **Fresh in-sandbox facts for this cell:** `scratchpad/ap6_controls.py` (cast arithmetic, minimal-stratum recovery, Ising and (ℤ/3, 2a²/3) monodromy, seven-level clock table — all reproduced exactly).

**Firewall (governs everything below):** this theorem classifies the *stage's* admissible structures. The SM appears only as a clause-by-clause audit subject; no SM numeric is matched, banked, or claimed; nothing here goes to CLAIMS.md. Epistemic tiers are stated per clause: **THEOREM** (closed-form proof, machine-verified), **COMPUTED** (exhaustive/2-method finite computation), **STRUCTURAL** (prior banked campaign result), **CONJECTURE/HINT**, **OPEN**.

---

## 1. The theorem

> **THE SELECTION-RULES THEOREM.** A play P = (M, T, S, D, Λ) is admissible on the stage **iff** all five clauses hold:
>
> **(M) M ∈ 𝒞, the cast monoid.** 𝒞 = { m ∈ ℤ⁴≥0 : Σ mᵢχᵢ ≡ 0 and Σ mᵢχᵢ³ ≡ 0 (mod 11) }, with χ = (1,3,6,7) — the object's own left-fixed M₄-eigenvector charge (B552), χ³ = (1,5,7,2) mod 11. 𝒞 is a finitely generated monoid with a **35-element Hilbert basis** (generator totals spanning {7,10,…,19}; completeness verified by independent DP-reachability against brute force to total 80, zero mismatches). Achievable totals = {0,7} ∪ [10,∞): exactly 8 forbidden totals {1–6, 8, 9}. The base cast (1,1,1,1) is **not** in 𝒞 (lin=6, cub=4 — the banked B565 T2 arithmetic).
> *Tier: THEOREM for the Hilbert basis and the stratum structure (finite, 2-method); the co-finiteness of the totals semigroup is COMPUTED (to 80, extended to 500 by the verifier) + the standard numerical-semigroup argument — bank as computed-with-standard-closure, not as an unqualified infinite theorem.* [AP1, CONFIRMED, holds]
>
> **(T) T ∈ sighted consistent theaters.** T must pass the consistency gates FIRST (S unitary, S⁴=I, (ST)³=S², Verlinde integrality, Gauss–Milgram) and then be SIGHTED for the monodromy ρ(A₁) = [T,S]. Content: for **every** one of the 243 consistent abelian (ℤ/N, q) theaters, N ≤ 24, **Tr ρ(A₁) = +1 exactly** — a short closed-form theorem from the Gauss–Milgram identity, q-independent; 249/250 tested theaters are sighted (only the empty N=1 theory is blind); Z is always real; the nonabelian additions are {0, −1/φ, 1/φ²}. The commutator word makes ρ(A₁) **algebraically independent of the c mod 24 phase** (the T-phase cancels identically in any commutator) — the prereg's "c mod 24" clause is falsified, cleanly.
> *Tier: THEOREM for abelian Tr=+1 and for the c-independence; COMPUTED for the nonabelian table. Known defect (verified benign): the DFib Gauss–Milgram gate was hardcoded in the cell's code, not computed — the verifier computed it independently (G = 2+φ = D_tot exactly, c=0) and it is true; fix the code before locking.* [AP2 CONFIRMED (prereg pattern-conjecture holds=false: Z is not confined to {0,±1}); AP3 CONFIRMED]
>
> **(S) S ∈ reachable chiral selectors.** Two-part clause. (i) *The branching table* (exact weight arithmetic, two routes each): 27|_H is **complex/chiral** for Spin(10)×U(1), SU(3)³, SU(6)×SU(2), G₂×SU(3); **self-dual/vector-like** for F₄ and Sp(8). (ii) *Reachability:* the play's holonomy Zariski-closure inside E₆(ℂ) must land in a chiral row. For the object's own holonomy (B565 construction, principal SL(2,ℂ) ⊂ E₆(ℂ), 27 = Sym¹⁶⊕Sym⁸⊕Sym⁰): every SL(2,ℂ) rep is self-dual, the principal SL(2) is θ-stable, so the closure sees a **reducible, vector-like 27 — for ANY E₆-embedding of the rank-1 holonomy**. The preregistered falsifier fired: **the chirality wall holds even complexified — the FIFTH WALL.**
> *Tier: table rows THEOREM (exact); reachability THEOREM modulo one patch (Zariski density should be cited via Borel density for the lattice, not inferred from bare irreducibility — the conclusion is true and standard). The cell's "self-dual iff H ⊆ F₄ or Sp(8)" biconditional is DOWNGRADED to CONJECTURE (only 6 subgroups checked; the converse is unproven — verifier-caught overclaim). The fifth wall does not depend on it.* [AP4 CONFIRMED, falsifier fired (holds=false)]
>
> **(D) D passes the order obstruction.** One-line test: a dynamical play at level N must have every frequency in (2π/ord_N)·ℤ, where **ord_N = ord(A₁ mod N) = π(N)/gcd(π(N),2)** (π = Pisano period) — proved for all N (elementary group theory on ord(F²); verified 2 methods, 0 mismatches, N ≤ 1000). Program-levels table: ord = {3:4, 5:10, 11:5, 15:20, 30:60, 165:20, 1155:40} (reproduced fresh in this cell). In consistent abelian theaters the operator order **equals** (not just divides) the arithmetic order at all tested odd N. The stage ticks at Fibonacci–Pisano frequencies; the c mod 24 phase plays no role (see T).
> *Tier: THEOREM (arithmetic identity) + COMPUTED (theater equality). Retro-kills verified computed, not asserted: six π/3-spaced levels need 6 | ord, and 6 ∤ 20, 6 ∤ 40 — the B567 handoff's claim stays dead.* [AP5, AP3 CONFIRMED, hold]
>
> **(Λ) Λ is relational.** The stage carries **no absolute scale** — the one structurally missing slot (prior bank; the prereg's own table row). Any play whose content requires an absolute unit fails outright.
> *Tier: STRUCTURAL (standing banked fact of the program; not re-derived in B570).*

**Chirality rider (Lane C, folded into clause S).** The object *has* a chirality, and the theorem now says where it lives: **the c-column, not the θ-column.** (i) C2 (THEOREM, verified biconditional at SL(2,ℂ)): all-traces-real ⟺ ρ̄ ≅ ρ ⟺ real form — all three fail on the object on the single fact tr(ab) = 5/2 − (√3/2)i; the compactness gap and c-chirality are **formally equivalent, both directions**. (ii) QA (CONFIRMED, exact arithmetic in ℚ(√−3)): θ fixes the geometric component pointwise (the principal sl₂ lies in F₄ = E₆^θ), c moves it — the trichotomy resolves to the third branch, **c ≠ θ and c is not inner**; the c=θ reframe is refuted. (iii) C1 (NULL, sign-free): no cusp-sign propagates to the θ-odd exponent lines — the J²=+1 result is a forced tautology on 1-dim lines, correctly banked as a null. (iv) C4 (holds=false): every cyclic cover of 4₁, n=2..12, branched and unbranched, is amphichiral — the handoff's "chiral covers correlate with {4,8}" row is refuted outright. Consequence for clause S: the θ-slot chirality a play would need (27 vs 27̄) is exactly the slot in which the object is symmetric; the chirality the object actually possesses (c: orientation / √−3 Galois) is not a selector in the AP4 table at all.

---

## 2. The SM run through the clauses — ONCE (the definitive gap-spec)

| Clause | Verdict for the SM | The exact fact |
|---|---|---|
| **M** | **NOT EVALUABLE** (fails for want of a dictionary) | The SM has no canonical 4-letter multiplicity vector; all sixteen σ→SM chains were killed retail — each was a failed dictionary. The clause now constrains any *future* dictionary wholesale: it must land in the 35-generator monoid; totals 1–6, 8, 9 are forbidden; the base cast (1,1,1,1) is excluded (lin=6, cub=4). |
| **T** | **PASSES — the one live channel** | Sighted theaters exist wholesale (249/250). The live channel is C3 (BANKED): E₆ level 2, the θ-odd 3-space carries a **non-scalar order-4 SU(3) monodromy**, eigenvalues {1, +i, −i} — chirality above the fold is *dynamical*, the first positive chirality-sector signal in seventeen campaigns. Whether any play can couple to it is open (see §5); the theater door itself is not the SM's obstruction. |
| **S** | **FAILS — the fifth wall** | Chiral rows exist (Spin(10)×U(1), SU(3)³, SU(6)×SU(2), G₂×SU(3)) but none is reachable: the object's holonomy closure factors through the θ-stable principal SL(2,ℂ), under which 27 is self-dual/vector-like — embedding-independently for the rank-1 holonomy. Folded with the rider: the SM's slot is θ-chirality; the object's chirality is c and is C2-dual to the compactness gap — **you cannot close the gap without losing the object's chirality, and neither is in the SM's slot.** |
| **D** | **FAILS at every tested level** | SM-like spectra need frequency patterns the clock forbids: ord = {3:4, 5:10, 11:5, 15:20, 30:60, 165:20, 1155:40}; six π/3-spaced levels require 6 \| ord and 6 divides neither 20 nor 40 (computed). B567's level-15 kill is now a wholesale criterion, not a retail adjudication. |
| **Λ** | **FAILS structurally** | Every dimensionful SM number requires an absolute unit; the stage has none. This clause no play with absolute scale can ever pass; it is the standing structural wall. |

**Gap-spec in one sentence:** the SM fails S and Λ structurally, fails D at every tested level, is unevaluable at M pending a dictionary that must now land in an explicitly presented 35-generator monoid — and has exactly **one** live positive channel, clause T, where C3's order-4 θ-odd rotation shows the stage's measurement face is chirality-sighted even though its algebra face (S) is chirality-blind. This is sharper than the sixteen retail kills combined: any future σ→SM play is now checked against five decidable clauses in minutes.

---

## 3. Two controls — the rules discriminate (all facts computed fresh in this cell)

**Control 1 — a random anomaly-free toy.** Cast m = (3,3,2,6) (= generator (0,1,1,5) + generator (3,2,1,1), total 14; AF verified: lin ≡ cub ≡ 0 mod 11). Theater (ℤ/3, q = 2a²/3): gates pass at 1e-15, Z = +1, ord(ρ(A₁)) = 4 = ord(A₁ mod 3) — sighted. Dynamics on the level-3 clock: frequencies in (π/2)·ℤ — passes D. Relational — passes Λ. Selector: F₄. **Verdict: passes M, T, D, Λ; fails S alone** (F₄ is a self-dual row, THEOREM tier). A play can score 4/5 and die on one clause — the clauses are independent, and S is doing real work.

**Control 2 — the Ising world.** Gates pass at 1e-16. Z = Tr ρ(A₁) = 0 (sighted, matching AP2), ord(ρ(A₁)) = 3, spectrum in (2π/3)·ℤ — it has a perfectly good clock of its own. But **S² = I exactly** (computed): charge conjugation is trivial, every object is self-dual — the Ising world fails S not by selector *choice* (as the toy does) but by theater-level *incapacity*: it contains no complex object that could ever carry chirality. And it fails M: no 4-letter cast map exists. **Two different failure signatures** (toy: reachability-of-choice; Ising: structural incapacity; SM: fifth wall + scale) — the clauses discriminate between worlds, they do not rubber-stamp or blanket-kill.

---

## 4. The ground state — B568-SQ recovered

Enumerated fresh: totals 1–6, 8, 9 contain **zero** anomaly-free casts; total 7 contains **exactly three**: (0,1,1,5), (1,5,1,0), (3,2,1,1) — byte-identical to the banked B568-SQ minimal casts (locked in `tests/test_b568_minimal_play.py`). The minimal play is therefore not an isolated find but the **bottom nonzero stratum of the cast monoid 𝒞** — the theorem's ground state: the least total at which clause M is satisfiable at all, sitting below the 8-gap Frobenius desert before the semigroup turns co-finite at total 10.

---

## 5. The honest open list

1. **The AP4 biconditional converse.** "27|_H self-dual ⟹ H ⊆ F₄ or Sp(8)" is unproven (6 subgroups checked). Prove over the full subgroup lattice or cite; until then the clause-S table is a verified 6-row table plus a conjecture. (The fifth wall does not depend on it.)
2. **The Zariski-density patch.** Replace "irreducible ⟹ dense" with the Borel-density argument for the lattice in the AP4 writeup before locking.
3. **The AP2 DFib gate.** Compute the Gauss–Milgram magnitude in code (verified true out-of-band: G = 2+φ = D_tot, c = 0) instead of the hardcoded `mag_ok = True`.
4. **AP1 co-finiteness.** Formalize {0,7} ∪ [10,∞) via the standard numerical-semigroup lemma (10 consecutive achievable totals + coprime 7); currently computed-to-500.
5. **AP3 even-N gap.** The q(x) = x²/N U(1) family is Gauss–Milgram-consistent only for odd N — normalization-specific; the even-N theater story is open (the group-theoretic order is unaffected).
6. **Q-C is NOT closed.** C5QC's headline discriminating fact is an algebraic tautology (mirror ≡ entrywise conjugate for any unitary data and real basis) computed on the wrong object (WZW level-2 modular data, not the geometric holonomy). **Quarantine its conclusion**; the c-column verdict stands on QA + C2 instead. The actual transport question — does the σ/σ̄ arrow fix the holonomy's sign choice — remains OPEN.
7. **A live inconsistency in the banked record** (C1's verifier): `docs/THEOREM_REGISTRY.md` T-θTANGENT (B501/B521: "amphichiral involution IS θ") vs B353 (hyperelliptic = θ, gauge-certified to 1e-102). The amphichiral map is antilinear; θ is ℂ-linear — they cannot both be θ. Adjudicate before anything further leans on T-θTANGENT.
8. **C4 phrasing fix before verbatim banking:** "two independent SnapPy methods on every n" is true only for the unbranched family; the branched rows had one SnapPy method (9/11), the lens-space criterion (n=2), or the lifting theorem alone (n=3,4). The census verdict itself stands.
9. **The M(2,7) HINT** (C3): S_odd moduli = (2/√7)·sin(kπ/7) — flagged, unmatched against exact M(2,7) data; do not cite as identification.
10. **The real next question:** can any play couple to the live channel — C3's order-4 θ-odd rotation at level 2? And separately: can the object's *c*-chirality (the one it actually has, dual to the gap by C2) be spent by any selector at all — c is outside the AP4 table's scope by construction.

**Discipline note:** no repo writes and no git were performed by this cell; the fresh control computations live in `scratchpad/ap6_controls.py`. Cells C5QC (conclusion), AP4 (biconditional sentence), and C4 (methods sentence) should not be banked verbatim — bank them with the corrections above. Everything else in §1–§4 is bankable as stated, at the tiers stated.