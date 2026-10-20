# B1672 — THE WORDINGS-WEAVE CLAIMS OF 18 OCTOBER, VERIFIED: the four shears generate Aut⁺(F₂) and the lifts cohere after an odd η-twist, but no postulate is discharged — L₆ is reducible under the moves, the index theorem is asserted, and the E₈ steps are classical branching plus identifications

**Verdict: NEGATIVE (a verification arc; what the arc claimed, that the triplet, index, boundary-domain and
hypercharge postulates are discharged, does not hold).** cc (main), 2026-10-20. POINT_REGISTER P-198. 0 of 19.
- **What this arc is.** On 18 October a separate session, working with the owner in main's working tree while main was
  away, wrote an arc under this number. It claimed, as PROVED and law-creating, that "the wordings weave" discharges
  the triplet postulate, the index postulate, the extreme boundary domain, the hypercharge dictionary and Gate 12, and
  that 4D spacetime emerges as M₁,₂. It also edited the paper's Table 1, §6 and §7 to say so. The arc was never sealed
  and never committed. Main verified it claim by claim, and banks the verification under the same number.
- **The received files** are in `verification/as_received/`, with their sha256 as received in
  `SHA256_AS_RECEIVED.txt`. One line of the received script was redacted on main: an absolute local path, replaced by
  a relative one. Its hash is the received one. `p9_edits_2026-10-18_19.patch` is the paper diff of both separate
  arcs, B1672 and B1673. **It did not enter the paper.**

## 0. Seen first

`VERDICT topic-sweep /Nielsen|Aut\+?\(F_?2\)|wordings weave|puncture module|L_6|Gate 12|E_?8|E6 x SU\(3\)|Dolbeault/: 75 of 1445 arcs on main match (NEGATIVE 6, OPEN 6, PROVED 63)`
— chiefly B1600 (W10's order-96 group on V = T ⊕ T̄), B1606 (the index formula and its domains, W22; P4), B1641 (M₁,₂'s
point-pushes act on the triplet by parity signs), and the paper's Proposition 24 (L₆ = V₂ ⊕ V₄ under 2O, irreducible
only under the parity-graded group of order 192). **Literature:** Nielsen's generators of Aut(F₂); Aut⁺(F₂) as the
mapping class group of the twice-punctured torus (Birman); the E₈ branchings (Slansky 1981).

## 0b. Disclosed

- **A verification, not a sealed test.** Nothing here was predicted blind.
- **Who checked.** One reading pass for main recomputed every claim with its own code (`verification/main_check/`,
  v1–v8). Main re-ran the decisive one, the irreducibility, itself.

## 1. What was claimed, and what holds

| claim (as received) | result on main |
|---|---|
| The four shears L_ab, L_ba, R_ab, R_ba generate Aut⁺(F₂) ≅ Mod(M₁,₂); the wording discrepancies are inner | **Holds, up to notation.** L_ab⁻¹∘L_ba = conj(a⁻¹) and R_ba⁻¹∘R_ab = conj(b⁻¹). The shears have determinant +1, give SL(2, ℤ) and generate Inn(F₂), so they generate SAut(F₂) = Aut⁺(F₂). The isomorphism should read "the mapping class group of the twice-punctured torus" (the orbifold fundamental group of M₁,₂), not "Mod(M₁,₂)" |
| T1: L₆ ≅ (χ_η³ρ_T) ⊗ V₂, with a puncture exact sequence matched by the level-2 theta doublet at weight ½ | **Holds, and it is new (scoped).** Hom dimension 2 at weight 3. The doublet (θ₃(2τ), −iθ₂(2τ)) has T = diag(1, i), with an S-fit residual of 10⁻³¹. But the module is still 2 + 4 under Mp₂(ℤ), and the sequence is pointwise exact for any non-zero Θ, so **no invariant domain Λ₊ follows** |
| T2: 4D spacetime is M₁,₂; a 4D Dolbeault–Dirac operator there has index ±3n, with Leray degeneration | **Asserted, not computed.** The received script sets the degeneration to true by hand; it is automatic over a base of dimension one. No Dirac operator and no Riemann–Roch on M₁,₂ is computed. What is computed is the modular-form count n(dim Λ₊ − 3), which is B1606's W22. "H²(M̄₁,₂, ℤ) = ℤ" is false: the rank is 2. Reading M₁,₂ as spacetime is an identification |
| T3: the moves generate G₉₆ ⊇ P_a, P_b; L₆ is irreducible under the moves, so ∣Λ₊∣ ∈ {0, 6} is forced and the domain choice discharged | **Refuted.** On W10's V the words RL²R and LR²L are P_a and P_b exactly, and ⟨M_L, M_R⟩ has order 96. That much holds, a small addition to B1600 and B1641. But that module is reducible (T is invariant; commutant dimension 2). **On L₆, where the index lives, the moves generate 2O (order 48; commutant dimension 2), and RL²R acts as diag(i, −i, …), not as P_a.** Irreducibility (order 192, commutant 1) appears only when P_a and P_b are added by hand: that is the paper's Proposition 24 and its priced requirement. The received arc mixed the two modules |
| T4: twisting by the spin bundle K^½ = χ_η³ makes Δ⁴ = +I, so the lifts cohere on Aut⁺(F₂) (Gate 12, P-074) | **Holds at a stated scope, with a choice.** Δ⁴ = −I₃ on T and χ_η³(Δ⁴) = −1, so the twisted Δ⁴ = +I. Over every word in the eight shear letters to length 7 (67 284 distinct automorphisms), the untwisted lift has 2 950 conflicts and the twisted lift none. **Gate 12 closes to that length.** Any odd η-power works; k = 3 and the reading "= K^½" are choices. A theorem needs a presentation of Aut⁺(F₂) |
| T5–T6: (E₆ × SU(3)_T)/ℤ₃ ⊂ E₈ places left-handed matter in (27, 3_T), discharging the triplet postulate; a polarisation of V₂ gives the SM hypercharges | **Classical branching plus identifications.** 248 = (78,1) + (1,8) + (27,3) + (27̄,3̄) is textbook. The central element is trivial in E₈, so "su(2) stays unbroken" is empty. T5 and T6 read the SU(3) factor once as colour and once as family. The hypercharge diag(1/6, 1/6, 1/6, −1/2, 1/2, −1/2) is typed in, not obtained from a polarisation that is never computed; on the 27 it gives the SM's 16 plus the usual 10 + 1, textbook E₆. Matter in (27, 3_T) is the triplet postulate restated, not discharged |
| T7: non-Sturmian wordings mix T and T̄ | **Not as stated.** 16 of the 55 determinant-one pairs to length 4 are not bases: they are endomorphisms, not automorphisms. T is invariant under all four shears |

## 2. What it says

- **No postulate of Table 1 is discharged.** The triplet postulate, the one cusp unit, the extreme boundary domain,
  the index as the generation count, the hypercharge dictionary and the index formula stay priced as they were. The
  paper's Table 1, §6 and §7 are unchanged; the edits are declined.
- **What it adds to the record, scoped:**
  - the four elementary shears of the words generate Aut⁺(F₂), the inner part coming from the two wording
    discrepancies;
  - RL²R and LR²L lift to the parity matrices on W10's V;
  - L₆ ≅ (χ_η³ρ_T) ⊗ V₂ as an Mp₂(ℤ) module, with the level-2 theta doublet's bundle sequence (no invariant domain
    follows);
  - **Gate 12 (P-074) closes to word length 7**: after an odd η-twist, the lifts are well defined on Aut⁺(F₂) over
    67 284 automorphisms.
- **The foundations question it raises** is the right one, even though the claims fail. A weave of words (Aut⁺(F₂))
  is larger than a weave of records (SL(2, ℤ)), and the difference is the inner automorphisms. That is the owner's
  question of 2026-10-20 (P-200), and it is the start of the foundations quest.

## 3. Files

- `verification/as_received/`: the received FINDINGS, verdict, script, output and lock, the paper patch, and
  `SHA256_AS_RECEIVED.txt`.
- `verification/main_check/`: the reading pass's report and scripts v1–v8, with their runs.
- The lock: `tests/test_b1672_discharging_triplet_index_gauge_frontier.py`. It replaces the received lock, which
  tested hand-typed matrices.
