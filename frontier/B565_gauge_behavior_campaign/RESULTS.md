# B565 — Gauge-Behavior Campaign RESULTS (2026-07-13/14)

44 agents, 0 errors; 18 cells + a 123-item false-kill exhumation; every numeric verdict
adversarially verified (2 framing rejections, corrected below). Locks:
`tests/test_b565_campaign.py`. Full per-cell evidence: the campaign journal
(`wf_1529ebff-6c0`). Firewalled throughout; nothing to CLAIMS.md.

## THE HEADLINE LEDGER

| cell | verdict | the fact |
|---|---|---|
| **T1** ℤ/11 't Hooft anomaly | **CLOSED BY DECOUPLING** | the ℤ/11 charge **does not descend** to the golden-anyon chain: 11 (prime) divides NO IR invertible-symmetry order (Inv(Fib)=1, Inv(Z(Fib))=1, sectors=2, TCI ℤ/2) ⇒ only the trivial hom. UV: on-site linear grading ⇒ H³ class **0** (gaugeable). IR: **vacuous**. The charge is real UV arithmetic on a *different floor* from the emergent CFT — not a force. Complements 2d (gauge-anomaly also fails) |
| **T3** chiral index | **≡ 0 — the 4th mechanism-level wall** | exact chiral symmetry of the species chain (±E defect ~1e-14 at N up to 8000, 2 word-sets + random controls); sublattice imbalance 0; **amphichiral label pairing σ+(1−σ)=1 EXACT for all 6 B546 labels**; the one nonzero-looking winding was a closed-gap artifact (cond 1e16) and a routine that failed SSH calibration was discarded. **The object is gauge-vector-like; SM matter is chiral (Nielsen–Ninomiya-rigid)** |
| **T4** trace-map β-sign | LIVE (medium) | the flow is **SCREENING-like**, never AF: γ ~ g^p with p saturating ≈0.86–0.93 (σ₄ word, depths 3–9, 2 grids × 2 seeds), d γ/d g > 0 throughout |
| **T5** ℤ/11 loop observables | LIVE (medium) | first loop observable on the object: closed strings decay pure-exponentially (a_C=−0.1800±0.0007), open strings **faster** (a_O−a_C = −0.0545, 7.5σ), FM ratio decreasing — a **confining-like signature** for the charge strings on the free-fermion floor (1D caveats explicit; NB T1: this is the letter floor, not the anyon floor) |
| **T2** centralizer stratification | CONFIRMED | SL(2) Fix(T₁²): ONE irreducible component (rational curve); z=1 (scalar) at generic + discrete-faithful points; z=2 (Cartan) at the 4 fiber-reducible ζ₅ points, broken back to 1 by the monodromy t; the ideal point (2,2,2) is NOT realized by any actual rep (exact singular-system proof). The object's breaking chain is **scalar-almost-everywhere** |
| **T8** B71 vs HMP | **CORROBORATED** | B71's SL(3) character variety matches Heusener–Muñoz–Porti (Illinois J. Math. 60) — external corroboration |
| **T6** Jordan/octonion residue | **REFUTED (the 5th door closed, with teeth)** | computed the octavian arithmetic: \|Aut\| = **G₂(2), order 12096 = 2⁶·3³·7 — element orders {1,2,3,4,6,7,8,12}, NO order 11** (and 11 divides none of the relevant orders up the chain); the Eisenstein axes (28) and unit axes (63) are **disjoint** strata; no object structure selects the Baez–Schwahn nested pair. The ℤ/11 charge cannot even act on the octonion arithmetic |
| **H1-krasnov** | **CONFIRMED by computation** | built Cl(9) on ℝ¹⁶ from scratch: dim so(9)=36 exact, J²=−I exact, **centralizer of J = 12-dim, center 1 + semisimple 11 = u(1)⊕su(2)⊕su(3)** — Krasnov's theorem verified, not cited |
| **H1-realform** | **THE HONEST HEADLINE: compactness is the gap** | the geometric holonomy lands in **F₄(ℂ)/E₆(ℂ) as real groups — in NO real form**: (i) non-real adjoint traces (tr Ad_{𝔢₆}ρ(a) = 37437270+38799960√3·i, exact in ℚ(√−3), two witnesses, two code paths) kill ALL real forms; (ii) the regular-unipotent meridian (Jordan {3,9,11,15,17,23}) independently kills the compact forms (compact ⇒ semisimple). TDV transfers as the **complexified** statement (H₁ℂ∩H₂ℂ = 𝔰𝔩(3,ℂ)⊕𝔰𝔩(2,ℂ)⊕ℂ on our F₄(ℂ)); the **compact slice — what makes it a gauge group — is extra structure the hyperbolic geometry does not provide** |
| **H1-triality** | **MATCH (100%)** | B299's (θ,φ) ℤ₃×ℤ₃ **IS** Boyle's SO(8) triality at the weight level: both generators 3-cycle the SU(3)³ factors identically; on the 27, 9/9 free orbits of size 3 hit each trinification block exactly once — the cyclic-triality signature exact. **The first live structural generations connection** (firewalled: a structure match, not a generations claim) |
| **R1** (B85, earned this time) | **TOMBSTONE + a positive law** | the Sym→trace-ring functor provably cannot reach the multiplicity-2 sector before n=5: **mult(char(M^h)) at height 2 = ⌈(n−2)/2⌉** (orbit-enumeration verified n=3..15; θ-fixed index exists iff n odd; n=5 is the first with dim 2). B85's wall now has its mechanism |
| **R2** (sealing) | PARTIAL — **leak evidence** | calibration PASSED (76-digit SnapPy match for b++RRLL, K=ℚ(x₀), x⁴−4x²+8, D₄); SL(3) off-sublocus: **50/50 irreducible fixed points fail K-membership** (validated separator) — evidence the sealing is metallic-specific; but the fixed loci are positive-dimensional (local dim 10 ≠ the expected 4), so the final verdict needs the dimension question resolved first |
| **R3** (Cell-3 Bézout) | PARTIAL | real bounds computed: best multihomogeneous Bézout = **7,099,436 characters** (vs 253 recovered) — far from tight; completeness stays open (BKK/numerical-AG = specialist) |
| **R4** (ρₙ) | verifier-REJECTED framing | the necklace/peel computation is right, but the "CH-cutoff corroborates the n=5 wall" claim was **contradicted by the cell's own unreported rank data** (no rank drop anywhere in range) — corrected: SPECIALIST, with the false corroboration struck |
| **R5** (L38 Higgs/scale, earned this time) | **TOMBSTONE — earned** | computed: the PVI time has **ℂ\* weight 0** (dimensionless modulus, exact); the only ℂ\*-fixed base point is h=0 (nilpotent); dilation is NOT isomonodromic (verified numerically both ways); ℏ-compensation exact. **No intrinsic scale on the Hitchin side.** The do-or-die dies with its fact computed |
| **H2-F2** | CONFIRMED | rung-3 K₀ = ℤ/18845089 **cyclic**, [1] coprime ⇒ **O_{M₁₆} ≅ O_{18845090}** (Kirchberg–Phillips chain extends) |
| **H2-F4** | CONFIRMED **with correction** | at composite e₄: the Σχ criterion fails at 3 of 4 prime factors under the unique-line reading, **but at p=11 the fixed space is 2-dim and CONTAINS a zero-sum class** — the anomaly-incompatibility is **NOT uniform up the tower** (the verifier caught the "uniform" overclaim; the honest statement is rung-1/2 incompatibility + partial rung-4) |
| **H2-F3** | **CONJECTURE REFUTED + exact identification** | rung-1 group = **D₄ (4T3)**, rung-2 = **8T15 = SmallGroup(32,43) = C8⋊(C2×C2)** (sage/PARI-exact; census matches theoretical class fractions to 0.006); **\|Gₙ\| = 2^{2n+1} is REFUTED at rung 3**: predicted 128 ⇒ expect 87.9 identity-hits in 11255 primes; observed **1** (P ≈ 5.8×10⁻³⁷). Data consistent with \|G₃\| ≳ 2048 — the tower grows FASTER than conjectured (still a 2-group; the PCF frame stands, the formula falls) |
| **H2-litgate** | CONFIRMED | Ibanez–Ross conventions verified from the sources: for N odd, η=0 and r=r′=0 — no mod-2N subtlety; 2d's verdict robust on the LINEAR condition alone (Σχ=6≠0). KP hypotheses + Raeburn gauge-action citations confirmed |

## THE FALSE-KILL EXHUMATION (Batch E — owner-directed)

**123 banked negatives audited: 113 SOUND, 9 SUSPECT, 1 CRACKED-COMPONENT.** The
discipline has improved sharply since B525 (3/10 cracked): the post-B525, prereg-era
negatives audit clean; the weak items are all early (pre-discipline) entries.

- **CRACKED-COMPONENT — S014's "~60% null" clause.** The Λ = Λ_Pl·φ^{−2N} death has two
  legs: circularity (sound, definitional, sufficient) and "~60% of random constants
  match as well" — which was **never computed in-repo** (git-archaeology: enters in a
  docs-only commit) **and does not reproduce**: an honest from-scratch attempt gives
  ~10.6%, with φ's fit (0.049 dex) *better* than the random-base median (0.34 dex).
  S014 stays DEAD on circularity alone; **the epitaph must be corrected** (done in
  TOMBSTONES.md). Numerology-grade either way; firewalled.
- 9 SUSPECTS = citation/scope-precision issues (e.g. VAL-CS4), none reversing a verdict;
  registered as a low-priority hygiene queue. One prior gap (K-O class count, no
  in-repo reproducer) was **recomputed from scratch this pass and reproduces exactly**
  — upgraded to SOUND.

## What the campaign settles (the one-paragraph reading)

The gauge question is now closed at the *behavior* level, not just the group level: the
object's charge is **non-anomalous, non-descending, screening, confining-on-its-own-floor
UV bookkeeping** (T1/T4/T5 + 2d); its matter is **exactly vector-like** (T3 — the fourth
mechanism-level wall, the sharpest yet); its centralizer chain is scalar almost
everywhere (T2); the octonion route has **no order-11 anywhere** (T6); and the TDV bridge
resolves honestly — the folding is ours and forced, the complexified SM-algebra
intersection transfers, and **compactness is exactly what the object does not supply**
(H1). Two genuine positives came out: the **triality match** (B299 ≡ Boyle, the first
live structural generations thread) and the corrected tower arithmetic (8T15 exact;
2^{2n+1} refuted — the Galois tower is *bigger* than conjectured). The kills that were
owed honest facts got them (B85 with its ⌈(n−2)/2⌉ law; L38 with its weight-0 theorem);
and the exhumation shows the ledger is 92% sound with one epitaph corrected.
