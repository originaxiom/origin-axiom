# B1107 — independent verification of the one-loop chain (B8100 → B8104 → B8112 → B8113)

Verification bench, run against `origin/paper/structure-genesis-first` on the audit seat's
checkout, before harvest to `main`. Own code throughout (`b1107_verify.py`); none of the audit
seat's scripts were imported or executed. Full run: 119.2s, all checks PASS. Results:
`b1107_results.json`.

---

## 1. THE ALGEBRAIC IDENTITY — the unwind, in 5 lines

Claim: for the 1-dim rep `σ_k` of `M = SO(2)` with highest weight `k`, `R(k,σ_k) = ∏_γ(1−q_γ^k)`.

1. `M = SO₂(ℝ)` is abelian, so **every** irreducible representation of `M` is 1-dimensional
   (textbook: irreps of a connected compact abelian Lie group are exactly its characters).
2. `σ_k`, the character of weight `k`, therefore sends the rotation `m_γ ∈ M` (parametrized by
   angle `θ_γ`) to the scalar `e^{ikθ_γ}` — this is what "highest weight `k·e₂`" *means* for a
   1-dim rep of a circle group.
3. Pfaff's `R(s,σ) := ∏_{[γ] prime} det(Id − σ(m_γ)e^{−sℓ(γ)})` (his eq. 3.4) has a 1×1 "det" for
   any 1-dim `σ`, i.e. it's just the scalar factor: `1 − σ(m_γ)e^{−sℓ(γ)}`.
4. Substitute `σ = σ_k`, `s = k`: the factor is `1 − e^{ikθ_γ}e^{−kℓ_γ} = 1 − (e^{−ℓ_γ+iθ_γ})^k`.
5. Define `q_γ := e^{−ℓ_γ+iθ_γ}` (packaging the real length and the `M`-rotation angle of one
   geodesic into one complex number — exactly SnapPy's own `complex(g.length)` convention). Then
   the factor is `1 − q_γ^k`, and `R(k,σ_k) = ∏_γ(1−q_γ^k)` — the GMY nome/factor, exactly.

**No physics content enters this step** — it is a substitution of `s=k` into a definition, given
that `σ_k` is 1-dimensional. The identity is real; what B8112 actually contributes on top is
noticing that the *infinite* graviton product `∏_{n≥2}|R(n,σ_n)|^{-2}` therefore cannot equal any
single *finite* `ρ(m)` torsion (a dimension-counting argument, not part of the unwind itself).

### Independent numeric check (not just restating the algebra)

Rather than trust the hand derivation alone, `b1107_verify.py` rebuilds `σ_k(m_γ)` from an actual
2×2 `SO(2)` rotation matrix `R(θ)=[[cosθ,−sinθ],[sinθ,cosθ]]`, diagonalizes it over `ℂ`
(`numpy.linalg.eig`), picks the eigenvalue continuously connected to `e^{+iθ}`, raises it to the
`k`-th power, and only then compares `1 − σ_k(m_γ)e^{−kℓ}` against `1 − q^k`. This exercises actual
linear algebra rather than typing in `e^{ikθ}` by fiat.

- 500 random synthetic `(ℓ,θ,k)` triples, `ℓ∈[0.05,6]`, `θ∈[−π,π]`, `k∈{2,…,12}`:
  **max |lhs−rhs| = 1.19×10⁻¹⁵** (machine precision).
- The same check on m004's own 50 geodesic classes below `ℓ=3.5`, `n=2..8`:
  **max |lhs−rhs| = 2.22×10⁻¹⁶**.

**CLAIM 1: CONFIRMED.**

### Primary-source check on the definitions (went further than "read their FINDINGS")

Fetched arXiv:1206.0228 (Pfaff) directly — abstract page plus the HTML rendering
(`arxiv.org/html/1206.0228v1`) — rather than trusting B8112's transcription. Verbatim matches:

| B8112's claim | Paper (verbatim, live-fetched 2026-08-21) |
|---|---|
| `M = SO₂(ℝ)` | *"Let `P₀:=MAN`... Then we have `M=SO₂(ℝ)`."* |
| every `σ_k` is 1-dimensional | *"every representation in `M̂` is one-dimensional and the elements of `M̂` will be parametrized as `σⱼ`, `j∈½ℤ`. Here `σⱼ` denotes the representation of `M` with highest weight `je₂`."* |
| `R(s,σ):=∏_{[γ] prime}det(Id−σ(m_γ)e^{−sℓ(γ)})` | *"`R(s,σ):=∏_{[γ]∈C(Γ)_s−[1], [γ] prime} det(Id−σ(m_γ)e^{−sℓ(γ)})`"* (their eq. 3.4) |
| absolutely convergent for `Re(s) > 2` | *"The infinite product in (3.4) converges absolutely for `Re(s)>2`"* |
| `ρ(m)` = 2m-th symmetric power of the standard `SL₂(ℂ)` rep | *"For `m∈½ℕ` we let `ρ(m)` denote the 2m-th symmetric power of the standard representation of `SL₂(ℂ)` over `V_ρ(m):=Sym^{2m}ℂ²`."* |
| Theorem 1.2, `m≥3` | *"`T_X(ρ(m))/T_X(ρ(2))=(c(m)/c(2))^{κ(X)}exp(−(1/π)vol(X)(m(m+1)−6))∏_{k=3}^m|R(k,σ_k)|`"* |
| `γ` decomposes as `exp(ℓ(γ)H₁)m_γ`, `m_γ∈M` | *"there exists a unique `ℓ(γ)>0` and a `m_γ∈M`... such that `γ` is conjugate to `exp(ℓ(γ)H₁)m_γ`"* |

Every definitional ingredient B8112 used is transcribed correctly. **No misquote found.**

---

## 2. THE NUMBERS — independent reproduction

All computed fresh from SnapPy (`Manifold('m004').length_spectrum(cutoff)`, `full_rigor=True`,
the library default — confirmed via `help()`, not assumed). Own `R(n,·)` implementation, own two
summation orders, own mpmath cross-check. Full ladder run: cutoffs 2.0–5.0 fetch in <6s total;
cutoff 5.5 (the audit seat's own headline cutoff) took 95.6s — reproducible, not a one-off (timed
independently three times during development, always 95–100s, always the same class/geodesic
counts).

### 2a. `log Z_geod`

| cutoff | mine | | cutoff | mine |
|---|---|---|---|---|
| 2.0 | −0.338894158892 | | 4.0 | −0.266081757054 |
| 2.5 | −0.313154801832 | | 4.5 | −0.274094490477 |
| 3.0 | −0.292104095975 | | 5.0 | −0.271015115395 |
| 3.5 | −0.279182286527 | | **5.5** | **−0.272977170838** |

At the top cutoff (5.5, matching their headline): **mine = −0.27297717083840395**, banked value
**−0.2729771708384004** → **agreement 3.6×10⁻¹⁵ (14–15 significant digits)**.

**Summation-order check** (own two independent algorithms: "n outer, complex product over γ
inner, then `−2log|·|`" vs "`−2log|1−q^n|` summed in real arithmetic per γ, then weighted by
multiplicity and summed over γ" — these are different floating-point *algorithms*, not just a
reordered loop):

- float64: `n-outer = −0.2729771708384856`, `gamma-outer = −0.27297717083840395`,
  **|diff| = 8.166×10⁻¹⁴** — matches their claimed **8.2×10⁻¹⁴** almost on the nose.
- **mpmath cross-check (50 decimal digits, independent library):** the same two orderings agree
  to **1.16×10⁻⁴⁰**. This confirms the 8×10⁻¹⁴ float64 discrepancy is *pure floating-point
  roundoff from two different summation algorithms*, not a hidden mathematical inconsistency — a
  strictly stronger check than re-running their code once more in float64 would have given.
  Float64 vs. the mpmath "true" value differ by 1.29×10⁻¹³, which is unremarkable accumulated
  roundoff over ~2800 geodesic-weighted terms and does not affect any claim (the physically
  quoted uncertainty is the cutoff error, 2×10⁻³, six orders larger).

**CLAIM 2a: CONFIRMED.** Cutoff used: 5.5 (matches the audit seat's own headline; fetch + compute
took 95.6s, well inside budget). Agreement with their banked value: 15 significant digits.

### 2b. Cutoff-instability table (n=2 term vs. n≥3 tail)

| cutoff | n=2 term (mine) | target | n≥3 tail (mine) | target |
|---|---|---|---|---|
| 4.0 | −0.346991558 | −0.346991558 | +0.080909800 | +0.080909800 |
| 4.5 | −0.354912150 | −0.354912150 | +0.080817660 | +0.080817660 |
| 5.0 | −0.351949899 | −0.351949899 | +0.080934784 | +0.080934784 |
| 5.5 (bonus) | −0.353902280 | — | +0.080925110 | — |

Matches to <5×10⁻⁷ at every targeted cutoff (float print rounding only). Last-step
(5.0→5.5) instability ratio: **201.8×** (theirs: "202×"). **CONFIRMED.**

### 2c. S(2), S(3) Dirichlet-type sums (B8113)

| cutoff | S(2) mine | target | S(3) mine | target |
|---|---|---|---|---|
| 4.0 | 0.746569 | 0.746569 | 0.133744 | 0.133744 |
| 4.5 | 0.796785 (step +0.050216) | 0.796785 (+0.050216) | 0.134429 (step +0.00068469) | 0.134429 (+0.00068469) |
| 5.0 (extension) | 0.847228 (step +0.050443) | — | 0.134867 (step +0.00043881) | — |
| 5.5 (extension) | 0.891968 (step +0.044741) | — | 0.135112 (step +0.00024472) | — |

Extended two steps beyond the requested range (5.0 and 5.5, not just one). At 5.5 the `S(2)`
step (+0.0447) has *dropped* below the 4.5→5.0 step (+0.0504) for the first time — i.e. with one
more cutoff step of data, `S(2)`'s increments are no longer flat, they've started falling. This
doesn't contradict B8113 (which explicitly disclaims proving divergence and calls the n=2 factor
"at best conditionally convergent" — a falling-but-not-yet-decaying-like-S(3) increment is
consistent with slow conditional convergence or continued oscillation), but it is worth the next
seat's attention: the "flat to 0.45%" observation at cutoffs 4.5→5.0 does not extend cleanly to
5.0→5.5, so the descriptive claim should be scoped to the cutoffs it was measured at (which
B8113's own FINDINGS already does — it never claims the flatness persists indefinitely). **Not a
discrepancy in what was claimed; a note for whoever extends this next.**

**CLAIM 2c: CONFIRMED** at the requested cutoffs; extension flagged above for context.

---

## 3. SCOPE FACTS — quote-check

**(i) Pfaff's `R(s,σ)` absolute convergence for `Re(s)>2`.** Appears in B8112's FINDINGS.md
verbatim: `` `R(s,σ) := ∏_{[γ] prime} det(Id − σ(m_γ)e^{−sℓ(γ)})`, absolutely convergent for
**Re(s) > 2** `` — and is exactly what B8113 uses to identify "residue 3" (the `n=2` factor sits
at the boundary of, not inside, this region). **Independently confirmed against the actual paper**
(§1 above): *"The infinite product in (3.4) converges absolutely for `Re(s)>2`."* Exact match.
**CONFIRMED.**

**(ii) B8112's own scope note.** FINDINGS.md, "What this does NOT establish": *"Not the one-loop
partition function. The cusp's continuous spectrum is still absent; B739's scattering determinant
(verified in B8101) remains the missing half. Not that analytic torsion is the graviton
determinant. Pfaff computes Ray–Singer analytic torsion. What is identified here is the Ruelle
factors, exactly and by definition. The torsion-to-determinant step is a further identification
and is not claimed."* Also in the SCOPE blockquote at the top of the same file and in
`results.json`'s `"scope"` field, word-for-word consistent across all three locations.
**CONFIRMED** — the statement is present, and present consistently (not just in one place that
could be stale relative to another).

---

## 4. Something that smelled wrong (not covered by the three claims, found while gathering data)

**B8100's class/geodesic count at cutoff 5.5 is not reproducible — the figure quoted is actually
the cutoff-5.0 count.**

`B8100/arc_verdict.json` and `B8100/FINDINGS.md` both state: *"cutoff pushed to length 5.5 (134
classes, 1221 geodesics with multiplicity)."*

Independently fetching `m004.length_spectrum(5.5)` (three separate runs during this verification,
including the final clean run inside `b1107_verify.py`) consistently gives **214 classes, 2819
geodesics with multiplicity** at cutoff 5.5. The numbers **134 classes, 1221 geodesics** are
exactly what this bench (and B8112's and B8113's own re-derivations) get at cutoff **5.0**, not
5.5 — see `class_geodesic_counts_by_cutoff` in `b1107_results.json`:

```
"5.0": {"classes": 134, "geodesics_with_multiplicity": 1221}
"5.5": {"classes": 214, "geodesics_with_multiplicity": 2819}
```

Cross-checked both manifold names (`m004` and `4_1`, B8100's own name for the object) — identical
counts at every cutoff 2.0 through 5.0, confirming this isn't a triangulation artifact.

**This does not appear to affect any computed result.** `oneloop.py`'s `logZ()` function calls
`M.length_spectrum(cut)` fresh inside the loop for every cutoff in its list (which does include
5.5), and its `results.json`'s `logZ_by_cutoff[-1] = -0.2729771708384004` **is** the correct
cutoff-5.5 value — reproduced here to 15 digits (§2a). So the actual numerics used the real
cutoff-5.5 spectrum; only the **prose class-count** in the verdict/FINDINGS is wrong, most likely
transcribed from an earlier interactive check at cutoff 5.0 and never re-checked after the cutoff
list was extended to 5.5. **Classification: a documentation/prose defect in B8100, not a
computational defect** — same shape as the E2 "control ran on different data than the headline"
defect B8112 already found and fixed in B8100's conjugate-pairs control, but this instance was not
caught by that fix and is a distinct occurrence (a class-count claim, not a control gate). Worth a
one-line correction in B8100's FINDINGS/verdict at harvest time; does not block the harvest and
does not touch any of the four numeric claims this bench was asked to verify, all of which
reproduce independently regardless.

---

## 5. Artifacts

- `b1107_verify.py` — standalone, no absolute paths, ~119s runtime, all internal gates PASS.
- `b1107_results.json` — full numeric output (every value quoted above).
- This file.
