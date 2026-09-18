# xB024 ADDENDUM 3 (2026-09-18) — MEYERHOFF–NEUMANN OBTAINED: L194's machinery is in hand, and their worked example is at our object's volume

**Beyond the seal.** `PREREGISTRATION.md` untouched (`9880dc01…`). The owner supplied the PDF from
ETH's E-Periodica after this seat declined to automate past the archive's bot challenge.

**R. Meyerhoff and W. D. Neumann, *An asymptotic formula for the eta invariants of hyperbolic
3-manifolds*, Comment. Math. Helv. 67 (1992) 28–46**, DOI `10.5169/seals-51082`.
**Grade: UNREAD → READ-AT-SOURCE.**

---

## 1. WHAT THE PAPER SAYS

**The setting, verbatim:** *"Let M be an oriented complete finite-volume hyperbolic 3-manifold with
one cusp. Suppose that an oriented basis `l, m` for the first homology at the cusp has been
chosen…"* — **the cusp-basis dependence CGHN pointed at, now in its own source.**

**THEOREM 1, its hypothesis quoted exactly:**

> *"Suppose that the basis `m, l` at the cusp is chosen so that `l` is a **"longitude"**, that is, it
> is **null-homologous in M**. Then, with ingredients to be described below, for `p² + q²`
> sufficiently large:"*

and the identity has the shape

`−(2/π)·Vol(M(p,q)) + 3η(M(p,q)) = f(u(p,q)) − (1/π)·λ(γ(p,q)) − I(p,q)`

**FENCE ON THE TRANSCRIPTION:** the scan's OCR mangles the coefficients (it renders `π` as `Tt`,
`η` as `rj`/`ri`, and drops operators). **The hypothesis, the named ingredients and the integrality
of `I(p,q)` are quoted with confidence; the exact numerical coefficients are NOT, and nothing here
rests on them.**

The ingredients: `f(u)` is the analytic function of Thurston's Dehn-surgery parameter from
Yoshida/Neumann–Zagier; `λ(γ) = length(γ) + i·torsion(γ)` is the complex length of the core geodesic;
and — the part that matters — **`I(p,q)` is an explicit INTEGER depending only on `p` and `q`**,
given by the **Hirzebruch defect**, with recurrences the paper derives from **the reciprocity formula
for Dedekind sums** ([H-Z] §5.1).

## 2. THE CONVERGENCE WITH OUR OWN CENSUS — FLAGGED, NOT IDENTIFIED

**Theorem 1's hypothesis is a null-homologous peripheral curve.** Our own record reports exactly that
condition, per level:

- **B1375's census prints `mu null-homologous: True/False` for every tower level** (False at Y₂/Y₃,
  True at Y₄/Y₅/Y₆), and xB027 reproduced the field.
- **B1374 names it the structural reason generations fire:** *"a generation needs χ² = 1 on the cusp,
  which the tower's **null-homologous lifted longitude** grants at every locus and the siblings'
  meridians deny."*

> **The same condition governs both.** **This is recorded as a CONVERGENCE and explicitly NOT as an
> identification** — no map is exhibited between Meyerhoff–Neumann's `l` and the census's lifted
> longitude, and two conditions sharing a name is precisely what B1223 forbids as evidence. What is
> worth a later arc is the narrow question: *is the census's null-homologous curve Theorem 1's `l`?*
> **Unanswered here.**

## 3. THE PAPER'S OWN REMARK ON ORIENTATION REVERSAL — L194's STEP, IN THE LITERATURE

Verbatim, from their numerical section:

> *"In many cases one expects **rational eta invariant for geometric reasons (some cover has an
> orientation reversing self-homeomorphism)**, and the computation bears this out."*

**That is L194's step, stated by the authors of the cusped η machinery.** It is a *remark*, not a
theorem, and is graded as such — but it is the first literature support the record has for the
orientation-reversal → rational-η direction in the **cusped** setting.

## 4. AND THEIR WORKED EXAMPLE IS AT OUR OBJECT'S VOLUME

Verbatim: *"for `N = W(3, −2; 6, −1)` the formula gives `Vol(N) + 3πi·2η(N) ≈
1.01494160640965362502120255427452028594168930753029979 + 0i`. Note that its volume is that of a
regular ideal tetrahedron — **half that of the figure-eight knot complement**; `N` is presumably
**arithmetic over ℚ(√−3)**."*

**Verified on this bench to 40 digits** (`verification/` of this arc is not re-run; the check is
one line and is recorded here):

```
MN's printed Vol(N) = 1.014941606409653625021203
vol(m000)           = 1.014941606409653625021203     |difference| = 0.0
vol(m004)/2         = 1.014941606409653625021203
```

> **Meyerhoff–Neumann's own worked example sits at the Gieseking volume — exactly `vol(m004)/2` —
> and they place it over `ℚ(√−3)`.** That is the object's own field and the object's own half-volume.
> **And the printed value has zero imaginary part, so `η(N) = 0`** for it.

**Two fences.** The exact coefficient in `Vol + 3πi·2η` is OCR-uncertain (§1), but **any reading
makes the imaginary part proportional to `η`, so `η(N) = 0` follows from "+ 0i" on any of them.**
And **a volume coincidence is not an identification** — `N` is not claimed to be m000 or any cover of
it. What is verified is the **number**.

## 5. WHAT THIS DOES AND DOES NOT DO FOR L194

**Does:** supplies the cusped-η machinery the register listed as the blocker; gives the cusp-basis
condition in its own source; gives an explicit **integer** `I(p,q)` (Hirzebruch defect / Dedekind
sums) as the arithmetic carrier; and supplies a literature remark tying orientation-reversing
self-homeomorphisms to rational η in the cusped case.

**Does NOT:** close L194. The open half needs the **transformation law of η under the
orientation-reversing isometry acting on the invariant cusp** — how the chosen basis `l, m` is
carried by `τ`, and what that does to `I(p,q)`. **That is Meyerhoff–Ouyang 1997's content and MO
remains UNREAD.** This arc cites it for nothing.

**The route it opens, stated so it can be taken or refused:** `τ` acts on the cusp by `A ∈ GL(2,ℤ)`
with `det A = −1`, so it maps the filling `M(p,q)` to `M(A(p,q))`. Theorem 1 applied to both, with
`η` odd under orientation reversal, yields a **functional equation in the explicit integer
`I(p,q)`** — and `I` is a Dedekind-sum object whose behaviour under `GL(2,ℤ)` is classical.
**That is computable on this bench.** It is **not** attempted here.

**Register updated. No value. Gate 5 absolute. Nothing to `CLAIMS.md`.**
