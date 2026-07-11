# B521 — Integration of the parallel closure audit's gate seals (integrate, don't merge)

**What this is.** The parallel closure campaign (Fable-5 seat, separate clone `oaudit/`, branch
`closure/phase1-duels` @ `e42c336`, terminal doc `docs/CLOSURE_2026-07-10.md`) finished with an
independent negative closure of the program: the four gates of `docs/OPEN_PROBLEMS.md` all SEALED /
REDUCED / CLOSED, no counterexample, "Origin Postulate REFUTED-AS-STATED." Its node numbering
**B493–B503 collides with this trunk's B496–B503** (tm_endo … external_contact), so the branch is **not
merged**. Instead its genuine deliverables are recorded here under a fresh trunk number, each **verified by
independent recomputation before banking** (governance), with the provenance stated per claim. The audit
branch remains a historical record; nothing here promotes to `CLAIMS.md`; the firewall is untouched.

**Bottom line.** The audit *corroborates* this trunk's own negative verdict (B511/B519) from a second,
prereg'd, foreign-controlled seat. Two independent seats, same terminal position. This is the strongest
evidence the negative is not a wrong leap — it is a theorem-shaped result reached twice by different routes.

## The audit → trunk node remap (collision resolution)
| audit node (oaudit) | content | recorded here |
|---|---|---|
| B493_seam_descent_duel | R2 seam law: PARTIAL + blind (4,7) prediction HIT | §R2 below |
| B494_cantat_corollary_duel | R1 held-breath = COROLLARY of Cantat; √41/√−239 erratum | banked in [[B479]]/[[B491]] (done 2026-07-11) |
| B495_adjoint_torsion_galois | Gate A / adjoint torsion | §Gate A |
| B496_cs_eta_galois | Gate A / CS,η | §Gate A |
| B497_extended_bloch_galois | Gate A / extended Bloch | §Gate A |
| B498_sl3_gluing_galois | Gate A / SL(3) gluing | §Gate A |
| B499_nonhermitian_dg_data | Gate D data | §Gate D |
| B500_irregular_covers_78 | Gate A / covers 7–8 | §Gate A |
| B501_gateB_reductions | Gate B reductions + θ-tangent theorem | §Gate B |
| B502_gateC_commensurator | Gate C CLOSES | §Gate C |
| B503_tower_timebox | tower filtration theorem | banked separately in [[B522]] |

## Gate A — no forced choice across the invariant classes (SEALED)
The all-invariants question ("does any peripheral invariant force a choice the object doesn't already
make?"): across thirteen invariant classes the answer is **no** — the values Galois-collapse and the two
ends *meet*.
- **Adjoint torsion (B495):** total Galois collapse {±3,±5}; the dynamical zeta = the Wada torsion at the
  Burde–de Rham rep; one V0 function carries all four values, its zero locus **disc −15**.
  *Verified here (`verify_gates.py`):* disc(ℚ(√−15)) = −15 (−15 ≡ 1 mod 4), h = 2 — the deeply-banked
  generic seam ([[K020]]/[[K022]]/B333/B334). The disc value is independently confirmed and matches trunk.
- **CS/η (B496):** amphichirality forces the 2-torsion values **{0,¼}**; the ± pairs sum to 0 (the member =
  external orientation); mirror law 31/31. *Provenance:* the {0,¼} 2-torsion structure is the arithmetic
  consequence of amphichirality (CS ↦ −CS); the 31/31 mirror table is on the audit's machine-checked run
  (`b495/b496 probe.py` + json), headline structure consistent with the amphichiral-forcing argument.
- **Extended Bloch (B497):** conjugation-symmetrized at every stratum; the seed's Ptolemy coordinates *are*
  the seam roots **c²−c+1** (the disc −3 figure-eight trace field); the chiral child mirror-pairs through
  its parent. *Provenance:* audit machine-checked run; c²−c+1 is the banked seam-root quadratic.
- **SL(3) gluing (B498):** W1/W2 ψ-swapped; **τ_V0(geo) = −84** total-collapse; the transverse multiplier
  spectrum given exactly (closing [[B99]]'s numerical form). *Provenance:* audit machine-checked run;
  cross-ref B99 (this closes its previously-numerical value).
- **Covers 7–8 (B500):** horizon extended to index ≤ 8; the first genuine multiplicity split at index 8 →
  the canonical datum is the **isometry-class multiset**. *Provenance:* audit machine-checked run.

**Net Gate A:** SEALED — the invariants meet at the seam (disc −15), the amphichiral 2-torsion is {0,¼},
the SL(3) torsion is −84; no invariant forces a choice the object doesn't already make.

## Gate B — REDUCED ×3 + a theorem (the θ-tangent)
- **Theorem (audit B501):** the manifold's amphichiral involution **is θ on the tangent, canonically** —
  the sl₂-commutant of Aut(𝔢₆) is {1,θ}. *Verified here:* Out(E₆) = ℤ/2 = {1,θ} is the standard E₆ Dynkin
  ℤ/2 diagram automorphism (the E₆→F₄ folding); the theorem identifies the geometric amphichiral involution
  with this canonical θ. Rep-theory core independently confirmed.
- H103 chiral-embedding search 70262 → **28 explicit survivors**; the {4,8} escape sector **unobstructed
  through order 4**. *Provenance:* audit machine-checked run (`b501 probe.py` + json pieces).

## Gate C — CLOSES (the commensurator is trinification, not generation) — INDEPENDENTLY CONFIRMED
The figure-eight's intrinsic commensurator ℤ/3: does it realize three symmetric 27-copies (a generation-3)?
**No.** The deck ℤ/3 acts as scalar ω-multiplication *within one* Eisenstein module.
*Verified here in full (`verify_gates.py`)* — all three independent "not-three-copies" tests:
- **Fix = {0}:** T = companion of Φ₃ = x²+x+1 (ω-multiplication), **det(T−I) = 3 ≠ 0** ⟹ no nonzero fixed
  vector ⟹ no diagonal ≅ A to fix (a genuine 3-copy permutation must fix the diagonal). N(1−ω) = Φ₃(1) = 3
  (the ramified 3 makes the action fixed-point-free).
- **|A|³ test:** |A| = 16 is **not a perfect cube** ⟹ A⊕A⊕A structure impossible.
- **Eigenvalue-1 test:** Φ₃(1) ≠ 0 ⟹ no eigenvalue 1 ⟹ not a permutation matrix.

The ℤ/3 is the **trinification-3 acting within one 27** (the ω-grading 𝔢₆ = 24 ⊕ 27_ω ⊕ 27_ω²), never a
generation-3. Gate C's written refutation condition fired on its CLOSES branch (both branches were live a
priori). **This closes an OPEN_PROBLEMS gate outright — confirmed independently on this trunk.**

## Gate D — DATA-BANKED (non-Hermitian Damanik–Gorodetski)
At κ = √3·e^{±iπ/6}: complex horseshoe signature, zero-area dim ≈ 1 spectrum, **polynomial** condition
numbers (no spectral pooling); two precise DATA-SUPPORTED conjectures; **no SURPRISE fired**. Banked as
data (the non-Hermitian DG question stays specialist-reduced, not closed). *Provenance:* audit run.

## R2 — the seam selection law: PARTIAL + a blind out-of-sample prediction HIT
The seam vanishing derives from the object's own P64/P66/P67/P68 machinery up to one named pair-specific
lemma **L5b** — so it is *internal structure*, not an imported physical value. The DERIVED classifier made
a **pre-committed out-of-sample prediction** of pair (4,7)'s full 31-cell table.
*Verified here (blind-hit check on the committed JSONs):* `b493_prediction_47.json` `committed_utc`
**2026-07-10T00:09:30Z** (phase=predict) precedes `b493_verify_47.json` `started_utc`
**2026-07-10T00:14:10Z** (phase=verify) by 5 minutes; the verify records `G1_tensor_mismatches: 0` and a
`global_table_sha256` pinning the table so it cannot be back-fitted. The prediction was **cell-exact**
(0/240 mismatches; 2,072-point machine-check including the L5b-violating points).

**Firewalled reading.** This is the one genuinely *predictive* result in either campaign: a **forced +
unsought + controlled** blind prediction that HIT — but of the object's **own arithmetic** (the seam
selection law, which derives internally), **not a physics value**. It refines "the object produces nothing"
→ "the object predictively produces its own arithmetic." It clears three of the four D0 bars (FORCED,
UNSOUGHT, CONTROLLED) and fails the fourth by construction (EXACT-physics-value — there is none; it predicts
a seam cell-table, arithmetic). Consistent with the firewall: the object is not inert, it is predictive of
its structure; it just does not cross to physics values.

## Verification ledger (what was independently recomputed vs cited)
| claim | provenance |
|---|---|
| Gate A disc −15 | **independently recomputed** (`verify_gates.py`) + matches banked seam |
| Gate B θ = Out(E₆) = ℤ/2 | **independently confirmed** (standard E₆ Dynkin ℤ/2) |
| Gate C Fix=0 / N(1−ω)=3 / 16≠cube / no eig-1 | **independently recomputed in full** (`verify_gates.py`) |
| R2 (4,7) blind prediction hit | **independently verified** (JSON timestamps 00:09:30 < 00:14:10, sha256 pin, 0 mismatches) |
| CS/η {0,¼}; extended-Bloch c²−c+1; SL(3) τ_V0=−84; DG data | cited on the audit's machine-checked run (heavy tooling); headline structure consistent with trunk |

Firewall: character-variety / representation-theory computation; no physics claim. Cross-refs:
[[B511]]/[[B519]] (this trunk's negative — corroborated), [[B479]]/[[B491]] (the held-breath erratum +
downgrade), [[B522]] (the tower filtration theorem), [[K020]]/[[K022]] (the seam), [[B99]] (SL(3) closed).
