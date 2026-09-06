# B1294 — THE CHIRALITY BIT: the object counts 2 at every fixed locus, and on a closed closing the 2 costs the chirality

*Seat harvest 2026-09-06 (sm:B1277-addendum, sm:B1278, sm:B1279; fc:R69, fc:R70), every load-bearing number
re-run or re-derived on this bench, plus the one statement none of the seats made. Verification:
`verification/harvest_chirality_bit.py` (prints `SELFTEST: PASS`, writes `chirality_bit.json`). Lock
`tests/test_b1294_the_chirality_bit.py`. Phase 0 of the approved MASTERPLAN v3 (`docs/MAIN_GOAL.md`).*

## The sentence

> **The object counts 2 at every fixed locus.** On m004, every isometry `g` has Lefschetz number
> `L(g) = 1 − s_μ(g) ∈ {0, 2}` — because `H₁(m004) = ℤ⟨μ⟩` and the longitude is null-homologous — so
> `χ(Fix g) ∈ {0, 2}` for all eight, never 1, never 3. On a closed rational-homology-sphere closing,
> `L(g) = 1 − deg g ∈ {0, 2}`, and **the 2 needs an orientation-reversing isometry, i.e. an amphicheiral
> closing — the very closings whose spectra the SM seat found mirror-paired.** Three appears only through
> the ℤ/3 descent (`3 | n`), and the descent is vector-like (sm:B1278/B1279).

## The seats' results, first (their priority, plainly)

- **sm:B1278 — Y₉ carries the Standard-Model group AND three generations.** 706,464 SM lines (three generations
  of Q, uᶜ, dᶜ, L, eᶜ with ⟨N⟩, ⟨νᶜ⟩, H_u, H_d available, SU(5) broken); **sm:B1279:** they fall into **19,624
  inequivalent vacua** under the group of order 72 (deck ℤ/9 × the eight lifts), in mirror pairs, all vector-like:
  *"the chiral closing … needs to supply only the chirality bit."* Y₆ has **no** three-generation SM vacuum
  (control Y₃ fires).
- **sm:B1277 addendum — ∂⁺M is annular.** The eight isometries as affine maps of the cusp torus; the b₁ Higgs
  field's leading symmetry-allowed radial mode is the orbit `(±2, 0)`; its sign partition of the torus is two
  annuli each, `χ(∂⁺M) = 0`. Stated caveat: the **coefficient `c₍±2,0₎` is not computed** (a symmetry-allowed
  direction of dimension 1, not the harmonic form's actual value); if it vanishes, `(±2, ±1)` leads and `χ = ±4`.
- **fc:R69 — Fix(θ) as a charge locus gives net ±2 or 0**, and *"the cusp is what keeps the endpoints; every
  closing removes them"*: on every filling the two arcs close into one loop or two, `χ = 0`.
- **fc:R70 — what the two are two of:** every θ-even Cartan direction gives `2(R ⊕ R̄)`, vector-like; the only
  chiral abelian direction, `ω₁^∨` (SO(10)×U(1), `1 + 16 + 10`), is not θ-even, so under θ-equivariance its
  count is zero. Scope gap fc states: PW §3.1 non-abelian spectral covers **not examined**.

## Re-computed here (sections of the script)

**A. m004's eight isometries (SnapPy, independent of the seats' Riley/horoball route).** `Isom = D₄`, amphicheiral;
all eight cusp maps diagonal `±1`; orders `{1:1, 2:5, 4:2}` from `multiply_elements`; `H₁ = ℤ` from the
presentation `⟨a,b | aaabABBAb⟩` with the meridian `ab` generating and the longitude `aBAbABab` null-homologous.
Hence `L(g) = 1 − s_μ`:

| `(s_μ, s_λ)` | orientation | order | `L = χ(Fix)` | Fix |
|---|---|---|---|---|
| `(+,+)` id | preserving | 1 | 0 | all of M |
| `(+,+)` | preserving | 2 | 0 | one closed geodesic (the period-2 axis) |
| `(+,−)` ×2 | reversing | 2 | 0 | **empty** (Gieseking-type glides, free) |
| `(−,−)` ×2 | preserving | 2 | 2 | **two arcs**, four corners on the cusp (the strong inversions) |
| `(−,+)` ×2 | reversing | **4** | 2 | **exactly two isolated interior points** on the period-2 axis |

The last row is new: the SM addendum's "GLIDE along λ, order 4, no fixed points" is true *on the cusp torus*;
in the interior each order-4 element fixes exactly two points (`g² =` the period-2 rotation, so
`Fix g ⊂` its axis; `L = 2` and no fixed circle is possible since `g|axis = id` would give `χ = 0`). The seats'
classification is otherwise reproduced line by line (order-4 ⇔ `(−,+)`; order-2 glides ⇔ `(+,−)`; four corners
per inversion). **Which fillings each extends to:** `A(p,q) = ±(p,q)` forces `pq = 0` for the four
orientation-reversing elements — **only the orientation-preserving V₄ extends to any non-trivial QHS filling**
(110 slopes tested), the V₄ of B1182.

**B. fc R69 as a Lefschetz statement, and the loop count derived without fc's pairing.** On m004 the 2 of the
two arcs is `1 − tr(θ*|H₁) = 1 − (−1)`; a filling with `p ≠ 0` kills `b₁` and with it the term — that *is*
"the cusp keeps the endpoints". On the filled manifold, `M(p/q)` is the double branched cover of `S³` along
`Fix(θ)/θ` (Montesinos), a double branched cover along a `c`-component link has `dim H₁(−;𝔽₂) = c − 1`, and
`H₁(M(p/q)) = ℤ/p`; so **the number of loops is `1 + [p even]`**, independently of any arc-pairing. fc's
pairing (`0↔τ/2`, `½↔½+τ/2`) reproduces exactly this on every slope; the only alternative pairing contradicts it
on odd slopes — so fc's geometric pairing is confirmed from homology alone. `χ = 0` for either.

**C. `H₁(Y_n)` from the Alexander companion matrix** `C` of `t² − 3t + 1`: SNF of `Cⁿ − I`, `n = 2..12`, each
order checked against `Res(Δ, tⁿ − 1)`. Seat values reproduced: `Y₃: (ℤ/4)²`, `Y₆: ℤ/8 ⊕ ℤ/40`, `Y₉: (ℤ/76)²`.
The golden form of the whole table: **odd `n`: `(ℤ/L_n)²`; even `n`: `ℤ/F_n ⊕ ℤ/5F_n`** (Lucas, Fibonacci —
`Δ`'s roots are `φ^{±2}`); the **19 of the three-generation closing is `L₉/L₃ = L₆ + 1 = 19`.**

**D. The deck action on the 19-torsion of Y₉:** roots of `t² − 3t + 1` mod 19 are `{6, 16} = φ^{±2}` (`φ ≡ 5, 15`);
two eigenlines × 18 generators = the seat's 36 "family" classes among the 360 elements of order 19.

**E. E₆ coweight spectra on the 27 (Bourbaki, B1293's own machinery).** `ω₁^∨: 1₍₄⁄₃₎ + 16₍₁⁄₃₎ + 10₍₋₂⁄₃₎`
(fc's `2/3, 1/6, −1/3` is the half normalisation); `ω₆^∨` is its negative; `ω₂^∨: 15₀ + 6_{±1}`;
`ω₁^∨+ω₆^∨: 9₀ + 8_{±1} + 1_{±2}` — fc's table reproduced. Every θ-even direction has a `q → −q` symmetric
spectrum (forced: θ-even `u`, θ: 27 → 27̄); `ω₁^∨`'s is not symmetric — the one chiral abelian direction.
**Sharpened:** under the diagram automorphism `ω₁^∨ ↦ ω₆^∨`, so `ω₁^∨` is **mixed, not θ-odd** (even part
`½(ω₁^∨+ω₆^∨)`, the D₄ ⊕ u(1)² direction, vector-like; odd part `½(ω₁^∨−ω₆^∨)`). fc's conclusion stands
unchanged — it is not an admissible θ-even direction — the eigenvector wording does not.

**F. The seat scripts re-run on this bench** (their machinery, sm:B1267–B1276, is not on main; detached worktrees):
`arcs_and_corners.py` rc 0 (leading orbit `(±2,0)`, `χ(∂⁺M) = 0`); `symmetries_on_the_lines.py` rc 0, 261 s
(8 outer classes, group order 72 on Y₉, deck on the eigenlines `(6, 16)`, 706,464 lines → 19,624 orbits;
average orbit 36 = average stabiliser 2); `six_fold_closing.py 3 6` rc 0 (Y₃ control True, Y₆: 0 three-generation
SM lines); `six_fold_closing.py 9` rc 0 — **Y₉ reproduced to the number: `H₁ = (ℤ/76)²` (5776, Fox = SNF here), `h¹` distribution
`{0: 5629, 1: 147}` (147 = 3 family + 108 of order 38 + 36 of order 19), three-generation alphabet 145, SU(5)-breaking
three-generation lines 737,568, SM vacua 706,464, full-spectrum 568,656, 16 distinct spectra**; fc `r69`, `r70`, `r70b` rc 0 (`ω₁^∨` half-charges
`{−1/3: 10, 1/6: 16, 2/3: 1}`; θ_F₄ fixed Cartan dim 4; conjugation fixed dim 1).

## The theorem this adds (registered: `T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING`)

For a closed rational-homology-sphere closing `N` and any isometry `g`: `L(g) = 1 − deg g`, so
`χ(Fix g) = 0` if `g` preserves orientation and `2` if it reverses it (Lefschetz; `H₁(N;ℚ) = H₂(N;ℚ) = 0`).
An orientation-reversing isometry exists iff `N` is amphicheiral (Mostow), and then `CS(N) ∈ {0, ½}`.
**Hence every closing that is chiral in B432's sense (`CS ∉ {0, ½}`) has `χ(Fix g) = 0` for every isometry;
the fixed-locus 2 and manifold chirality are mutually exclusive on closed closings.** On m004 itself the 2 is
`1 − s_μ`, carried by the cusp's `b₁ = 1`, and the orientation-reversing isometries extend to no QHS filling.
This is why the closings on which the SM seat found a count — Y₃, Y₆, Y₉, amphicheiral — found it mirror-paired,
and why a filling that "chiralizes" (B432/B434, 31/31) has no locus to count on. The two-chiralities crux
(c vs θ) in one line: **on a closed closing you may have the 2 or the c-breaking, not both.** Not claimed: any
identification of a fixed-locus count with a generation count (that is I-26, UNEARNED).

## The two named assumptions (not theorems — every door below is about one of them)

1. **θ-equivariance of the vacuum** (fc's modelling choice; derived nowhere on main — swept). Dropping it is
   door **D1** (B1296): expected first chiral spectrum with count **2**, priced as an identification row.
2. **`c₍±2,0₎ ≠ 0`** (the SM seat's caveat). Computing it is door **D4** (B1295), with the closed-manifold census
   check of the theorem above on Y₃/Y₉ (isolated-point counts of the orientation-reversing lifts) and the
   degree-≤10 cover scan (87 covers, `|det(A−I)| ∈ {0, 4}`, run on this bench 2026-09-06, unbanked until B1295).

**Door D2** (B1297+): PW §3.1 spectral covers via B298's cusped 3-fold cyclic cover — the one route no negative
closes; the count there must be a different index (degree × chirality bit), not a fixed locus. Prior ~30 %.

## Not verified here, fenced as harvest
sm:B1278's enumeration internals and sm:B1279's orbit computation (re-run only, not re-derived); fc's icosian
identification of quaternion conjugation with `−s_β`, `β = φ⁻¹`; fc's PW charge count itself (its combinatorial
half is re-derived in B, its charge half re-run). No identification-ledger row moves. Number collision recorded:
main's `B1277_leak_closure` vs the seat's `B1277_the_vacuum_manifold_of_the_closing` — cite seat arcs as
`sm:Bnnnn` / `fc:Rnn`; seat branches never merge.
