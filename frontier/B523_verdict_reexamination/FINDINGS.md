# B523 — The wrong-leap re-examination: was any negative a premature leap?

**Owner's ask (2026-07-11): "inspect the math and where we missed the step and took the wrong leap to
negative conclusion."** This node treats the program's own negative verdict as the thing to *break*. Each
key "generic / laundered / no-crossing" call is recomputed and classified into exactly one terminal state:
**CONFIRMED-GENERIC** (the control ran, the negative holds — no wrong leap) · **PREMATURE** (a wrong leap;
reopen) · **UNTESTED-RESIDUAL** (existence-negative right, but an object-specific control never run — run it).
Firewalled; nothing to `CLAIMS.md`. The independent audit ([[B521]]) already corroborates the negative;
this pass looks for a leap the corroboration might hide.

## The classification table
| cell | negative call | terminal | why |
|---|---|---|---|
| 1 | the (3,1) Lorentzian signature is generic | **CONFIRMED-GENERIC** (C3 run) | trace-form + Lyapunov both generic (splitting-type / C1); **C3/Malament now run** — only the evolution verb gives a proper cone; the monoid shares none (below) |
| 2 | B518 mixed-chain = "just gap-labeling" | **CONFIRMED** (correct decline) | the composite IS additive Bellissard gap-labeling (a known theorem); declining to call it a crossing is right, not a wrong kill |
| 3 | wild-census S₄-generic | **CONFIRMED-GENERIC** | the census used field-isomorphism (not disc-match) against the Bhargava base rate (D0 gates); S₄-genericity is a proper base-rate statement, not a laundering |
| 4 | seam ℚ(√−15) generic (h=2) | **CONFIRMED** | the *value* question is generic (h=2, 14 fields); the object-specific structure (A1 "product un-taken") is already banked as STRUCTURE (B519), not a physics value |
| 5 | B519 "no crossing" | **CONFIRMED** | corroborated by the independent audit ([[B521]]/CLOSURE_2026-07-11) — two seats, same negative |

**Verdict: NO wrong leap found.** The one genuine UNTESTED-RESIDUAL (C3) was run and it *confirms* the
negative. The negative now stands on firmer ground than before the re-examination.

## Cell 1 (the substantive computation): C3 / Malament — does the four-verb monoid preserve ONE causal cone?
The (3,1) signature's *existence* is generic (trace-form control + C1/tetranacci, both banked). The handoff's
**C3** was the one control never run: Malament's theorem gives a canonical conformal structure only if the
*whole* causal automorphism group preserves *one* cone. Computed here (`c3_malament.py`) — the four banked
verbs (B497), each in the bootstrap coupling `M_v = [[v,v],[v²,v]]`, against M*'s timelike (expanding) cone:

> **CORRECTION (B525 'Are You Sure' audit).** The original write-up carried a "preserves M*'s cone"
> column with percentages (1.000/0.96/1.000/—) computed by a buggy `lyap()` whose sign convention sent
> genuine ZERO eigenvalues to 'spacelike' (|0|<1 → +1), so the det-0 TM verb printed "(3,1) proper,
> preserves 1.000" — a *proxy-for-object* error (a magnitude count substituted for the Lorentzian
> signature). That column is **struck**. The discriminator is the **signature** (# expanding directions,
> with degeneracy flagged), recomputed correctly below (`c3_malament.py`, fixed). The conclusion is
> unchanged and rests only on the signatures.

| verb | det(M_v) | causal type (recomputed, degeneracy-flagged) |
|---|---|---|
| **evolution** F=[[1,1],[1,0]] | −1 | **(1,3) proper** — one timelike direction |
| decimation [[2,0],[0,2]] | +16 | **(2,2)** — two timelike directions |
| decimation [[1,2],[1,0]] | −8 | **(3,1) inverted** — three timelike directions |
| TM/erasure [[1,1],[1,1]] | 0 | **DEGENERATE** — det 0, non-invertible |

The four verbs carry **four different causal types**: only the unimodular **evolution** verb yields a
proper single-timelike (1,3) Lorentzian cone; decimation gives (2,2) or an inverted (3,1) with multiple
timelike directions; TM/erasure (det 0) are non-invertible — not causal automorphisms at all.

**⟹ the Level-1 four-verb monoid does NOT preserve a single causal cone.** Malament does not apply to the
monoid (its premise needs a causal automorphism preserving one cone); there is **no single object-specific
causal structure**. The proper single-timelike cone belongs to the **evolution sub-dynamics alone**, and
there it is generic to any 2-real-1-complex quartic Pisot (C1). **C3 CONFIRMS the negative — on the
signature grounds, which the audit verified survive the bug.**

### Structural note (banked as STRUCTURE, firewalled — not a crossing; audit-narrowed)
Among the four verbs, a proper single-timelike (1,3) Lorentzian signature arises **only for the unimodular
evolution verb**; decimation gives extra timelike directions and TM/erasure are degenerate. That is a
signature fact and is close to a restatement of "det = ±1 / measure-preserving." *(The stronger phrasing
"causal structure ⟺ the evolution verb", tied to the struck cone-preservation percentages, is retracted —
the audit showed those percentages did not discriminate.)* Firewalled: the (1,3) is generic, no physics.

## Bearing on cell 1: the incoming Level-1 free-product / genus-2 "spacetime" handoff (verified, 2026-07-12)
A cross-seat handoff proposed upgrading Level 1 from the direct product F₂×F₂ to the **free product
F₂*F₂ = F₄**, claiming its substitution `φ: a→abAB, b→aA, A→abaAB, B→aA` is an automorphism (det = −1) whose
mapping torus is a genus-2 fibered hyperbolic 3-manifold (a "Level-1 spacetime"). Verified
(`verify_handoff_L1.py`):
- **SOUND:** the *direct-product obstruction* is real — every 2-dim SL(2,ℂ) irrep of F₂×F₂ tensor-factors
  (Schur), so cross-coupling (κ(a,A)≠2) needs the free product. The conceptual point ("independence =
  freeness, not commutativity") is correct. And **|γ| = 1/√φ exactly** (|γ|² = 1/φ² + (√5−2) = 1/φ ✓) — a
  genuine golden-nesting fact.
- **BROKEN:** the stated φ is **NOT an automorphism.** `φ(b) = φ(B) = aA` (both map to the same word) ⟹ φ
  is **non-injective**; its abelianization matrix has two identical columns and **det = 0, not −1.** The
  genus-2 fibered-hyperbolic-3-manifold construction — and every downstream claim (χ=−3, vol ≥ 3·log β, the
  trace field, the 9d cross-coupled character variety *with this monodromy*) — **does not follow**, because
  Thurston's theorem needs φ to be a pseudo-Anosov *automorphism*.
- **Terminal:** the Level-1 upgrade is **NOT a new door as stated** (the specific map is broken). The idea is
  *possibly* salvageable with a genuine Σ_{2,1} pseudo-Anosov automorphism carrying Perron β=φ(1+√φ), but
  that map has not been exhibited; and even an abelianization-det-±1 endomorphism of a *free* group need not
  be an automorphism. Recorded as a corrected-cross-seat-claim (cf. the β-function handoff): the verify pass
  caught the over-claim before banking. B515–B517 (substitution, Rauzy, Pisot β) are untouched — they live
  at the word level, below the group structure, as the handoff itself notes.

## Addendum (2026-07-12): the CORRECTED train-track handoff — the fix is real, the iwip claim isn't (yet)
A follow-up handoff supplied the corrected substitution **φ: a→abAAB, b→aAB, A→abAB, B→aA** (on F₄ = ⟨a,b,A,B⟩,
positive letters) and retracted the false genus-2 mapping-class claim (matching this node's finding). Verified
(`verify_traintrack.py`):
- **The fix is real and nice.** φ is **injective** (φ(b)=aAB ≠ φ(B)=aA — the prior collapse is gone), and its
  abelianization is **conjugate over ℚ to the bootstrap matrix M\* = [[F,F],[F²,F]]**: same char poly
  **x⁴−2x³−5x²−4x−1**, det **−1**, primitive ((I+M)³>0), unique Perron **β ≈ 3.676 = φ(1+√φ)**. So the Level-1
  free-group substitution and B517's bootstrap carry the *same* β — a genuine consistency. It is a train-track
  map on the rose R₄ with primitive transition matrix. **[MATH, VERIFIED]**
- **φ ∈ Aut(F₄) — VERIFIED (independently, 2026-07-12).** Not via the abelianization (det = −1 is necessary,
  *not* sufficient for free groups) and not on chat3's authority, but by a cleaner route: **F₄ is Hopfian, so a
  surjective endomorphism is an automorphism**, and φ is surjective — all four generators are explicit reduced
  words in the images (`verify_auto.py`): a = βα⁻¹γβ⁻¹δ, B = δ⁻¹β, A = a⁻¹δ, b = a⁻¹(γβ⁻¹)a
  (α,β,γ,δ = φ(a),φ(b),φ(A),φ(B); each free-reduces to its generator). So **im(φ) = F₄ ⟹ φ ∈ Aut(F₄).** This
  corrects an earlier under-statement here (it had lumped Aut-status with iwip). Chat1's attribution: chat3 had
  already built the explicit inverse; this trunk now confirms it independently.
- **But "φ is iwip / word-hyperbolic" is STILL open — not established by the five tests.** All five (primitivity,
  M^k-primitivity, no permutation-block-triangular, irreducible char poly, Perron) are **abelianization-level
  properties** — *necessary for* and *consistent with* iwip, but not a certificate: there exist non-iwip free
  automorphisms with primitive, irreducible-char-poly abelianizations (e.g. one fixing a proper free factor up
  to conjugacy). The iwip certificate needs **Bestvina–Handel** (build the train-track representative, tighten,
  check for periodic Nielsen paths) — a genuine algorithm, not a matrix check; **not run.** **The word-hyperbolic
  / atoroidal / CAT(0) / Menger-boundary consequences follow ONLY IF iwip holds — so they are CONDITIONAL, not
  banked.** Terminal: **iwip = NEEDS-CERTIFICATE (Bestvina–Handel)** — the one genuinely open group-theoretic
  question; the abelianization-as-proxy was the subtler over-claim the verify pass caught.
- **T[4₁] / DGG bridge — cited correctly, but it is the already-CLOSED route, not a new one.** The handoff
  presents T[4₁] (DGG 3d–3d) as an external bridge giving gauge group **U(1)** + 2 chirals + a dilog
  superpotential. That U(1) is *exactly* the abelian gauge group **T-NOGO-DGG (B490)** already characterized as
  U(1)^{N−c} and used to CLOSE the 3d–3d route (SM gauge is nonabelian). "Gauge from the triangulation" still
  yields abelian U(1) — **no route to SM gauge**; the handoff's own "NOT a firewall crossing" is right, and it
  does not reopen B490. External established math, correctly firewalled.
- **The two owned bugs (volume, Kashaev) are correctly self-caught:** vol(4₁)=2.02988… (Bloch–Wigner branch
  error), and the volume-conjecture asymptotic is (2π log|⟨4₁⟩_N|)/N not (2π/N)·log (the Kashaev values
  ⟨4₁⟩₂=5, ⟨4₁⟩₃=13 are right). No bank affected.

**Net:** the corrected substitution is a real fix, abelianizes to the bootstrap β, and **φ ∈ Aut(F₄) is
verified** (surjective + Hopfian) — all banked as MATH. The **iwip** property (hence word-hyperbolic /
atoroidal / "spacetime") is the one open group-theoretic question → **NEEDS-CERTIFICATE (Bestvina–Handel)**.
T[4₁] is the already-closed abelian route (B490). Method note: abelianization (H₁ = ℤ⁴) properties are
necessary-not-sufficient proxies for F₄-level properties — the session's sharpest verification lesson. Lock
extended in `tests/test_b523.py`.

## Terminal state
DOOR B523 — **CLOSED (re-examination complete): NO wrong leap to negative.** Five cells re-checked; the one
UNTESTED-RESIDUAL (C3/Malament) run and CONFIRMS the negative; the proposed Level-1 genus-2 upgrade is built
on a non-automorphism and opens no door as stated. One structural nugget banked (causal ⟺ evolution verb),
firewalled. Lock: `tests/test_b523.py`. Cross-refs: [[B517]] (SIGNATURE_HUNT / C1), [[B497]] (the four
verbs), [[B521]] (audit corroboration), [[K025]] (the value-free theorem), P015/P016 (the reading).
