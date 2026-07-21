# B749 — MEASUREMENTS (fixed before seal; each must distinguish ROBUST from FRAGILE)

Per fork: the sibling construction, the discriminating measurements, and what each verdict
looks like concretely (MB12: both outcomes stated, both reachable). The anatomy yardstick
throughout = the banked V₄ interface: being (trace field ℚ(√−3)), hearing (the golden/ℚ(√5)
side), the cusp/interface, arithmeticity — plus knot-ness (H₁ = ℤ) where applicable.

**F2 — periodicity allowed.** Sibling: mapping tori of finite-order/reducible monodromies
(periodic words ⇒ |trace| ≤ 2 abelianization). Measure: Thurston trichotomy class (pA vs
finite-order/reducible — computed from the trace), existence of a hyperbolic structure,
carried faces. ROBUST = no pA, no hyperbolic carrier, zero faces (compute the geometry it
does get). FRAGILE = any periodic-word carrier admitting hyperbolic structure.

**F3 — the silver slope.** Sibling: the m=2 once-punctured-torus bundle (monodromy
[[2,1],[1,0]]², trace 6). Measure in-sandbox: (a) volume + hyperbolicity (snappy); (b) trace
field (exact minpoly of tr γ, algdep-verified with residual guard per cc2's lindep lesson —
coefficient-size-aware thresholds, exact factornf confirmation); (c) arithmeticity
(Maclachlan–Reid criteria; B125 predicted YES — verify, don't cite); (d) H₁ (knot-ness: m004
has ℤ; silver expected NOT a knot complement — compute coker); (e) which V₄ faces survive.
ROBUST = silver lacks ≥2 of {knot-ness, being-field analogue's special prime, interface
structure}. FRAGILE = silver carries a comparable full interface (then m=1's selection rests
entirely on K009/B313's soft selectors, and the chain says so).

**F4 — shadow-rule variants.** Siblings: σ_inert (a→ab, b→b), σ_rev (a→ab, b→ba), plus the
swap (a→b, b→ab). Measure: primitivity (does every letter eventually generate both),
aperiodicity, abelianization determinant (mapping-class realizability requires det = ±1).
ROBUST = each variant fails a structural requirement (state which: σ_inert non-primitive →
eventually periodic; σ_rev det 0 → no mapping class; the swap = Fibonacci conjugate — if so,
NOT a distinct sibling, record as identification not failure). FRAGILE = a variant yields a
primitive aperiodic invertible class inequivalent to Fibonacci.

**F5 — det −1 (the orientability fork).** Sibling: the once-punctured-torus bundle with
orientation-reversing monodromy [[1,1],[1,0]]. Build via snappy's bundle census; measure:
(a) identify the manifold (expected: the Gieseking — verify by volume 1.0149… AND by the
orientation double cover being isometric to m004, snappy is_isometric_to — the double-cover
check is the verdict-bearing fact, cheaply re-executable); (b) its invariant trace field;
(c) cusp structure; (d) which faces exist unoriented. FRAGILE (per the sealed prior) = the
sibling is m004's own parent (the double cover IS m004): the discarded choice re-enters the
chain as ancestry, and A6's price is "orientation = passing to the child". ROBUST = the
double cover is NOT m004 (prior falsified — a finding).

**F6 — no puncture (Sol).** Sibling: the closed torus bundle of [[2,1],[1,1]]. Measure:
geometry type (Anosov closed bundle ⇒ Sol — verify via the trichotomy, not citation);
hyperbolicity NO; H₁ = ℤ ⊕ coker(A−I) (compute exactly); trace field NONE; every V₄ face
present/absent explicitly. ROBUST = total face-loss (B747/B748's interface-only prediction
confirmed at the origin: no interface, no faces). FRAGILE = any face survives closure.

**F7 — the Sturmian strata control (corrected per §16 review 1 — the sealed v1 sentence
"quadratic = exactly the metallic family" was FALSE; witness √3−1 = [0;1,2,1,2,…]: quadratic,
self-similar, non-metallic).** Three strata, each measured:
  F7a (non-quadratic slope): by Lagrange, NO self-similar generator — verified on a concrete
  transcendental-slope witness via CF non-periodicity. ROBUST = no self-map exists (the
  self-similarity locus is exactly the QUADRATIC class, not the metallic family).
  F7b (quadratic NON-metallic — the stratum v1 missed): the √3−1 word's composite
  substitution (CF period (1,2)) and its carrier bundle — compute the mapping-torus, its
  hyperbolicity, volume, trace field, faces. This is a genuine sibling CLASS: metallicity is
  the all-equal-digits subfamily selected only by T4's extremality, and F7b measures what the
  in-between stratum carries. ROBUST = F7b carriers lack the anatomy (metallic selection
  survives); FRAGILE = an F7b carrier matches the interface (T4's extremality is then the
  load-bearing selector and the chain prices it).
  F7c = the metallic stratum itself (covered by F3; cross-reference only).

**F8 — the non-geometric carriers (no prior; genuinely open).** Siblings: the Fibonacci
substitution tiling hull and its AF/C*-algebra. Measure: the dimension group (direct limit of
ℤ² under the substitution matrix — compute the ordered K₀ with its φ-cone), gap-labeling
data, and THE question: which V₄ faces are recoverable from the combinatorial carrier alone?
Expected computables: the hearing/golden face (φ, ℚ(√5)) lives in K-theory; test whether ANY
route to the being face (ℚ(√−3)) exists without the geometric realization. Verdict language
for F8 (declared): GEOMETRY-NECESSARY = the being face is absent from every combinatorial
invariant computed (A5 is then the load-bearing bridge to the being side, priced exactly);
GEOMETRY-REDUNDANT = the combinatorial carrier already sees ℚ(√−3) (the chain simplifies).

**Cross-fork instrument rules:** every exact field claim double-checked (numeric relation +
exact factornf — cc2's lindep lesson is binding); every snappy identification confirmed by
two independent invariants (volume + isometry check, never volume alone); all scripts
deterministic with printed check-lines for cc's re-execution gate; verdicts journal-only.
Executor warnings from §16 review 1 (binding): snappy bundle strings verified live —
'b++RL' = m004, m000 = the Gieseking (vol 1.0149416064, orientation_cover ≅ m004); but
'b-+RL'/'b--RL' are a DIFFERENT non-orientable manifold (vol 2·Catalan) — F5 must verify its
construction string by volume + cover, never assume notation. F2's trichotomy carries the
det=−1 scope caveat as recorded in the review.
