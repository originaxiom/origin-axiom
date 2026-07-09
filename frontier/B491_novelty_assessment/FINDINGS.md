# B491 — the positive question: adversarial novelty assessment of three candidate results
**Owner directive (2026-07-09): "ask the positive question — is this new mathematics?" Ran the
deep-research adversarial prior-art harness (104 agents, 21 primary sources, 25 claims verified 21-4)
on the three strongest candidate results. Assume-known, hunt hard. Result: TWO of three survive as
APPEARS-NOVEL / NEEDS-SPECIALIST; one is classical. This is the honest terminal state per the
compute-before-deferring directive — the computation is exhausted, the specialist question is named.
Firewall: this is a mathematics-novelty record, nothing to CLAIMS.md.**

## R1 — the held-breath torsion law (= P3 Theorem F7, B479): PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST
Claim: on the one-holed-torus SL(2,ℂ) character variety, the finite-order mapping class σ_m (a↔b)
fixes (⊇) the order-d torsion characters for divisors d≥3 of m (d≠4). **[Field CORRECTED, round-2
re-panel:** d=3 gives ℚ(√−7) (minpoly z²−z+2); **d=5 gives a DEGREE-4 field over ℚ(√5)** (minpoly
z⁴−3z³+7z²−4z+4, disc 5²·41) — NOT ℚ(√41); the "41" was a discriminant factor. The novelty VERDICT
below is unchanged — the divisor-indexed fixed-character phenomenon is what is not-found, independent
of the field's degree.**
- **Framework classical:** Goldman, *The modular group action on real SL(2)-characters of a one-holed
  torus*, Geom. Topol. 7 (2003) 443–486 (arXiv:math/0305096) — the exact Markoff-cubic κ=x²+y²+z²−xyz−2
  setup and Γ≅PGL(2,ℤ)⋉(ℤ/2)². But Goldman's theorems are the ERGODIC dichotomy; he does NOT compute
  torsion fixed-characters, has no divisor indexing, no τ²(τ²−8) field (full-text grep: 0 hits).
- **Closest prior art for the MECHANISM — Cantat (2009):** *Bers and Hénon, Painlevé and Schrödinger*,
  Duke 149 (2009). He computes the fixed points of Ψ=[[2,1],[1,1]] (= our A₁, the figure-eight
  monodromy) on the character surface via the fixed curve (x, x/(x−1), x): four points solving
  x⁴−3x³+x²+4x−2=0, factoring over **ℚ(√17)**. This is the SAME fixed-curve→quartic→quadratic-field
  technique — but for the pseudo-Anosov Ψ at commutator-order-4 (ℚ(√17)), NOT the finite-order σ_m
  at the cusp κ=−2 (ℚ(√−7) at d=3, a degree-4 field over ℚ(√5) at d=5, divisor-indexed). **This is a
  gift: it validates the mechanism
  independently and hands the specialist the exact tool.**
- **Structural direction known:** Biswas–Gupta–Mj–Whang, Geom. Topol. 26 (2022) (arXiv:1707.00071) —
  finite genus-1 MCG orbits = finite/special-dihedral (once-punctured torus in Appendix A). But they
  classify finite orbits of the FULL MCG, not fixed points of one σ_m; no field formula.
- **Verdict:** the object, the modular action, and the fixed-curve→field mechanism are all in the
  literature; **no source states the divisor-indexing or the τ²(τ²−8)-norm fields.** APPEARS-NOVEL,
  NEEDS-SPECIALIST. Specialist question: is the τ²(τ²−8) field an easy corollary of Cantat's method,
  or genuinely new? (Four sibling over-claims — BGMW "exact setting", Dubrovin–Mazzocco, Tykhyy,
  Cantat–Loray field-formula — were adversarially REFUTED 0-3, which SHARPENS the verdict.)

## R2 — the seam broken-lattice selection rule (= P1, B459): PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST
Claim: the cross-map seam s(a,b)=tr(Par·P_a·Q_b) at level 15 lands in ℚ(√5,√−3) and its Galois
channels vanish in exactly the subfield lattice minus the ℚ(√−15) node plus a zero stratum.
- **Building blocks standard:** Kurlberg–Rudnick (Duke 103, 2000, arXiv:chao-dyn/9901031) — Hecke
  operators from the real-quadratic eigenvalue field, CRT prime-power factorization at composite N;
  Ladisch (arXiv:2303.09676, 2023) + Strömberg (arXiv:1108.0202) — explicit Weil character-value
  formulas at odd composite level; Dong–Lin–Ng (Alg. Number Th. 9, 2015, arXiv:1201.6644) — Galois
  symmetry of modular data.
- **The decisive gap:** standard Galois-equivariance of modular data is a **signed permutation**
  G_σ=σ(s)s⁻¹ (Dong–Lin–Ng) — it shuffles entries with signs and **can never send a nonzero value to
  zero.** So the seam's *systematic vanishing* of the √−15 channel is NOT an instance of the known
  Galois mechanism. No source constructs a cross-map seam matrix coefficient between two distinct
  Anosov quantizations, or a one-node-absent vanishing rule (grep: seam=0, biquadratic=0, N=15=0).
- **Verdict:** every ingredient standard; the specific object and its selection rule not found, and
  the natural candidate explanation (Galois-equivariance) provably cannot produce the vanishing.
  APPEARS-NOVEL, NEEDS-SPECIALIST. Question: does a CRT/Galois-descent argument explain the √−15
  absence, or is it genuinely new?

## R3 — the cover-tower torsion |L(2n)−2| (= B489): KNOWN / CLASSICAL
|H₁| of the n-fold cyclic cover = |det(A₁ⁿ−I)| = |L(2n)−2| = Res(Δ, tⁿ−1) is a textbook special
case of **Fox's formula** (cyclic-cover homology = cyclic resultant of the Alexander polynomial; see
Porti arXiv:math/0306181; Gordon 1972 on periodic homology). Confirms B489's own self-assessment.
Only the verbatim Lucas closed form |L(2n)−2| may be folklore-uncited — trivial to derive.

## Net (the honest positive answer)
The program has **two genuinely novel-looking mathematical cores** — the held-breath torsion field law
(R1) and the seam broken-subfield-lattice (R2) — that survive an adversarial prior-art hunt as
APPEARS-NOVEL/NEEDS-SPECIALIST, with classical frameworks but specific cores absent from the canonical
literature, and (for R2) a proof that the natural known mechanism cannot explain it. The third (R3) is
classical. This is the terminal state of the compute-before-defer directive: the computation is
exhausted and the specialist question is precisely posed for each. **These belong to number theory /
low-dimensional topology on their own terms — not because they are the SM (they are not, B490), but
because they may be true and new.** Directly upgrades the novelty gates of Papers P1 (seam) and P3
(held-breath) from "pending" to "APPEARS-NOVEL, specialist-gated," with the Cantat/Goldman/KR/Ladisch
citations to fold in. Caveat (stated): these are NEGATIVE-EXISTENCE verdicts over canonical references;
less-indexed literature (theses, proceedings, Markoff-dynamics preprints) not exhaustively mined.

Reproducer: deep-research run wf_bfe715db-e53 (this session). Sources: Goldman math/0305096; Cantat
Duke 149 (2009); BGMW 1707.00071; Kurlberg–Rudnick chao-dyn/9901031; Ladisch 2303.09676; Dong–Lin–Ng
1201.6644; Porti math/0306181.
