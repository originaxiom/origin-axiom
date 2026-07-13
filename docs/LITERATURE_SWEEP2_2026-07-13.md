# Literature sweep 2 (sharpened search image) — what we're missing, what to borrow, where we collide

*Second model-tiered sweep (6 angles, citation-checked, 2026-07-13), run AFTER the gauge
arc fixed the search image: the object's gauge story = Connes-abelian U(1)-ladder, Cuntz
gauge algebras, torsion charges, 2-group Galois tower, RG-selected. Companion to
`docs/LITERATURE_GAUGE_SM_2026-07-13.md`. Firewall-clean; nothing to CLAIMS.md.
Locks for the two in-session verified facts: `tests/test_sweep2_facts.py`.*

## The three verdicts

**1. NOT scooped where it matters.** No literature computes an H³ anomaly class for any
order-11 symmetry of the golden chain / M(4,5) (T1 stays novel). **No gap-label work
above quadratic fields exists anywhere** — even Jagannathan's 2026 unified metallic-mean
treatment (arXiv:2602.09769) stays rank-2; a degree-4 measurement would be a genuine
first (PC23's novelty REINFORCED). The exact |Gₙ|=2^{2n+1} tower formula appears nowhere.

**2. Two framings are 30+ years old — cite as precedent, not as new.**
- *Torsion-as-charge* is Kellendonk's integer group of coinvariants (CMP 187, 1997) +
  the Bellissard gap-labelling theorem (rigorous 1-D: **Bellissard–Bovier–Ghez**, Rev.
  Math. Phys. 4 (1992) — the sweep's own mis-attribution corrected by the verifier);
  physics reading of integer-matrix entries as tile-bound charge: PRX 11, 041051 (2021).
- *The Cuntz–Krieger K-theory identification* (K₀=coker(I−Mᵀ), K₁=ker) is textbook
  (Cuntz–Krieger 1980; Anderson–Putnam 1998). What remains OURS: the specific tower of
  Cuntz algebras with RG-selected charges and the **anomaly-incompatibility theorem**.
- *The tower's qualitative Galois collapse* (sub-full, widening gap) is a proven PCF
  theorem (Pink arXiv:1307.5678; Benedetto–Ghioca–Juul–Tucker arXiv:2411.06745 — BGJT
  authorship corrected by the verifier). Only the exact formula is our claim.

**3. Five nearly-free computations** (two already verified in-session):
- **lk₂(11, 809) = 1 — VERIFIED (locked).** The object's two leading charge primes are
  **nontrivially linked in Spec ℤ** (Morishita: linking = Legendre; (809/11) = (−11/809)
  = −1; 809≡1 mod 4). The first arithmetic-topology fact about the charge tower.
- **The arboreal identification — VERIFIED (locked).** The doubling step λ→λ(1±√λ) is a
  PCF quadratic correspondence; our tower matches **full** Aut(binary tree) at depths
  1–2 (2, 8=D₄) and the order-32 census at depth 3 is **index 4** — the PCF collapse
  signature, exactly where Pink/BGJT predict sub-fullness. The 2^{2n+1} conjecture =
  "full at depths 1–2, then ×4 per level" vs the tree's squaring.
- **βₙ = log λ_PF(Mₙ) — the forced KMS temperature ladder** (Exel arXiv:math/0110183):
  every O_{Mₙ} carries a UNIQUE KMS state at inverse temperature log(Perron), state =
  the PF eigenvectors. A free thermodynamic invariant on matrices already in hand; via
  the 3/2 law, βₙ₊₁/βₙ → 3/2 — the growth law IS a temperature law. (Honest boundary:
  primitive finite matrices give ONE temperature per rung — no Bost–Connes transition.)
- **Pink's closed-form |M_{1,n}|** vs 2^{2n+1} at rung 3 — the discriminating fact for
  the tower conjecture (proof or kill, replacing 2-point extrapolation); Stoll/BGJT
  field-degree criterion ([ℚ(ζ₈,√D₁):ℚ]=8?) can promote the rung-1 D₄ census to a theorem.
- **e_n mod 5/7 exclusion — WITH A CAVEAT the sweep missed:** the Ward/Lucas period
  protocol assumes eventual periodicity of eₙ mod p, automatic for LINEAR recurrences
  but NOT obvious for our doubling tower (field degree grows). Needs an
  eventual-periodicity lemma first; registered as such, not overclaimed.

## Borrowable recipes (exact sources)
Rédei triple symbols (Ishida–Kuramoto–Zheng arXiv:2403.17957; **caveat: 11≡3 mod 4
breaks the vanilla precondition — needs the twisted Rédei–Reichardt form**) · the
Kim-school arithmetic-CS template (Chung–Kim–Kim–Park–Yoo arXiv:1609.03012 Thm 5.13:
CS = ½ ⟺ (t/809) = −1 — mechanical once t is chosen from the disc −400 data) ·
Cheng–Williamson relative-anomaly recipe (arXiv:2002.02984) as an INDEPENDENT extraction
of the ℤ/11 class from M(4,5) modular data — cross-checks B565-T1 · Aasen–Fendley–Mong
(arXiv:2008.08598) explicit MPO/defect construction · Seiberg–Seifnashri–Shao LSM
strategy (arXiv:2401.12281) — if the ℤ/11 class is nontrivial, gapless-or-degenerate
follows · Baboux et al. (arXiv:1607.03813) polariton winding-measurement protocol — the
experimental FORM for PC23's degree-4 prediction (Rechtsman 2-phason design as apparatus;
Jagannathan's rank-2 formula as the boundary it must reduce to) · Anderson–Putnam
collared-tile complex — the border-forcing check on σ₄ (does naive coker miss K₁
torsion? a correctness check on our K-theory) · Markoff-mod-p algorithmics
(arXiv:2401.00630; BGS arXiv:1505.06411; W. Chen, Annals 199 (2024)) as the
strong-approximation genre for the orbit-selection law.

## New targets (registered; two-outcome)
N1 eₙ mod 5/7 periodicity lemma + exclusion · N2 the KMS ladder βₙ (+ consistency with
the PF eigenvectors already computed) · N3 BGJT field-degree criterion (rung-1 D₄ →
theorem) · N4 Pink |M_{1,n}| vs 2^{2n+1} at rung 3 (THE discriminating fact) · N5 Pink
universality vs our multi-seed census (a mismatch falsifies the arboreal identification)
· N6 arithmetic-CS at p=809 (+ the twisted Rédei gap for 11) · N7 B565-T1 cross-check via
Cheng–Williamson + the FDLUC-vs-MPO regime check + Liang's φ² benchmarks
(arXiv:2607.01151) · N8 Anderson–Putnam border-forcing on σ₄ · N9 PC23 restated in
Baboux winding form · N10 quarantined-until-verified: the Spin(7)₁×Fib̄ SymTFT claim
(arXiv:2310.16878) — check against M(4,5) modular data in-sandbox before any use.

## Reading list
Exel math/0110183 · Kellendonk CMP 187 (1997) + RMP 7 (1995) · Anderson–Putnam ETDS 18
(1998) · R. Jones arXiv:1402.6018 (arboreal survey) · Pink arXiv:1307.5678 · BGJT
arXiv:2411.06745 (+2507.08347) · Morishita arXiv:0904.3399 (+ Knots and Primes, 2012) ·
CKKPY arXiv:1609.03012 (+1706.03336) · IKZ arXiv:2403.17957 · Cheng–Williamson
arXiv:2002.02984 · SSS arXiv:2401.12281 (+AFM 2008.08598, Liang 2607.01151) ·
Bilu–Hanrot–Voutier Crelle 539 (2001) + W. Chen Annals 199 (2024) · Baboux
arXiv:1607.03813 + Jagannathan arXiv:2602.09769.

## The structural echo (firewalled, hint-grade)
Three independent literatures each hand the object an intrinsic layer it already forces:
its matrices force a **thermodynamics** (KMS temperature = growth rate), its recursion
forces an **arboreal Galois tower**, and its charge primes are **arithmetically linked**
— the object carries its own interaction grammar on every mathematical side it touches,
consistent with the observer-coupling reorientation.
