# B1959: the weighted inverse on a finite-area cusp, with the constant asymptote adjoined

**Verdict: PROVED** (a theorem of analysis about a class of operators; main, 2026-11-18). It is the first of the six
deciding calculations the physical lane ranks on its status page, its equation (3) in
`fixed_sector_light_system_2026_11_16/CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH.md` (read at `8d5c91032`). Main
said on that seat's page (M8) that it would either give an independent argument for the stated map or name the lemma
that fails. This is the independent argument. No lemma fails.

**What this is not.** It banks nothing of the lane's model. The theorem is about any operator of the form below. That
the lane's gauge operator on its background has this form is three structural hypotheses (H1 to H3), and they stay the
lane's own statements about its fields. Inputs removed: zero. Nothing is compared with data. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /cusp.*invers|bounded inverse|weighted H.lder|maximum principle|Fredholm|finite.area cusp|essential spectrum|Laplace.type/ (full text): 17 of 1700 arcs on main match (OPEN 2, PROVED 15); 5 register rows match (DONE 2, QUEUED 3)`.
- **What the record already holds:**
  - **B1911, B1954:** the physical lane's elliptic complex and its work of 2026-11-15 to 17, held on main as algebra.
    Neither holds an inverse on the cusp.
  - **B1957** (records physical-c3e, physical-ns-01): the finite algebra of the lane's package P-C3e, with its
    analytic estimate marked as not recomputed. This arc is that estimate.
  - **Register row P-061:** another lane's analytic work on a Fredholm problem at a puncture, queued for a
    specialist's review and never read by main. It is a different operator and end; nothing of it is used here.
  - The other matching arcs are harvests that use the word Fredholm for seats' index counts. None proves an inverse.
- **The literature** (searched on 2026-11-18; the papers themselves were not read for this arc):
  - The nearest standard frame is the weighted theory of elliptic operators on manifolds with cylindrical ends
    (Lockhart and McOwen, *Elliptic differential operators on noncompact manifolds*, Ann. Scuola Norm. Sup. Pisa, 1985):
    such an operator is Fredholm between weighted spaces exactly when the weight is not an indicial root, and the index
    changes only across those roots. *[Corrected 2026-11-19 at Review 85, finding B1: the cusp is not a cylindrical end.
    Its circle shrinks, and the nonzero frequencies see e^(2t) D_x². Only the zero-frequency part has that form, and its
    exponents −β and 1 + β are indicial roots in that sense. The frame is cited for orientation; the proof does not use
    it, and the papers were not read.]*
  - That the essential spectrum of the Laplacian on a surface with a hyperbolic cusp starts at 1/4 is classical
    (spectral theory of manifolds with cusps; W. Müller, Math. Nachr. 111, 1983).
  - **No novelty is claimed.** The statement is of a known kind. What this arc adds is a self-contained proof for the
    stated class, with the constant asymptote adjoined, by a route that does not use the lane's own argument.
- **What is new to the record:** the theorem as stated in § 2, its proof, and seven numerical checks with controls.

## 1. The setting

A surface Σ is a compact piece K joined to one cusp C = [T₀, ∞) × S¹ with the metric ℓ²(dt² + e^(−2t) dx²), where x
has period L. Its area form on the cusp is ℓ² e^(−t) dt dx, so the cusp has finite area and its circle shrinks.

E is a real vector bundle of finite rank over Σ with a metric and a metric connection D. M is a symmetric nonnegative
endomorphism of E. The operator is

    P = D*D + M        (on the cusp: ℓ⁻²(−∂ₜ² + ∂ₜ − e^(2t) D_x²) + M).

- **H1 (the cusp is homogeneous).** Over the cusp, in a parallel orthonormal frame, E ⊗ ℂ splits into lines L_j. On
  L_j the connection is d + i (w_j/2) e^(−t) dx, sections are periodic up to the phase e^(2πi ν_j), and M is a constant
  μ_j ≥ 0. So on L_j a section of angular frequency m (m in (2π/L)(ℤ + ν_j)) sees the ordinary operator

      ℓ⁻²(−∂ₜ² + ∂ₜ + V_m),   V_m(t) = (m e^t + w_j/2)² + ℓ²μ_j.

  At m = 0 this is the lane's (1) with c_j = μ_j + w_j²/(4ℓ²).
- **H2 (one neutral channel).** Exactly one zero-frequency channel has c_j = 0. It is spanned by a global parallel
  section Q with MQ = 0.
- **H3 (the kernel).** P is nonnegative and its bounded kernel is ℝQ.

Let β_j = (√(1 + 4ℓ²c_j) − 1)/2 for the zero-frequency channels with c_j > 0, and fix 0 < δ < min β_j, k ≥ 0 and
0 < α < 1. C_δ^(k,α) is the space of sections whose C^(k,α) norms on balls of fixed radius in the universal cover of
the cusp, multiplied by e^(δt), are bounded (ordinary C^(k,α) on K). Then, with χ a cutoff equal to 1 far out the cusp,

    X_δ = { aχQ + ψ : a real, ψ in C_δ^(k+2,α) },      Y_δ,0 = { f in C_δ^(k,α) : ⟨Q, f⟩ = 0 }.

## 2. The theorem

**Under H1 to H3, P maps X_δ ∩ Q^⊥ onto Y_δ,0, one to one, with a bounded inverse.** The constant a is determined by f.
It is not a free datum at the end.

## 3. The proof

**Step 1: P maps X_δ into Y_δ,0, continuously.** P(aχQ) = a[P, χ]Q has compact support, since PQ = 0. On a ball of
the universal cover, in the half-plane coordinates (x, y = e^t), the operator is the same on every ball: the metric
ℓ²(dx² + dy²)/y², the connection form (w/2) dx/y and the constants μ_j are all unchanged by x → λx + b, y → λy. So P is
bounded from C_δ^(k+2,α) to C_δ^(k,α). Green's identity with Q on {t ≤ T} leaves a boundary term
∮⟨Q, ∂ₜψ⟩ e^(−T) dx, which tends to zero. Hence ⟨Q, Pψ⟩ = 0.

**Step 2: one to one.** If Pu = 0 with u in X_δ, then u is bounded with decaying derivatives, so the same integration
by parts gives ‖Du‖² + ⟨u, Mu⟩ = 0. By H3, u is a multiple of Q, and it is orthogonal to Q, so it is zero.

**Step 3: a solution in the square-integrable sense.** With u = e^(t/2) v, −u″ + u′ = e^(t/2)(−v″ + v/4), and the norm
of u against e^(−t) dt is the plain norm of v. So a zero-frequency channel is −d²/dt² + 1/4 + ℓ²c_j, and its quadratic
form is at least (1/4 + ℓ²c_j)‖u‖² for sections supported in the cusp, which are the ones Persson's formula uses *[added
2026-11-19 at Review 85, finding B3: with v = e^(−t/2)u the form is ∫|v′|² + (1/4 + ℓ²c_j)‖v‖² − v(T₀)²/2, so a section
that does not vanish at the cut can lie below; K2's eigenvalue 0.9031 under the threshold 1.15, with the cut's own
boundary condition, is such a state, and it is discrete]*. A channel of nonzero frequency has V_m → ∞. By Persson's formula the essential
spectrum of P starts at or above 1/(4ℓ²). Zero is therefore an isolated eigenvalue, of eigenspace ℝQ (H3). For f in
Y_δ,0 there is a unique square-integrable u orthogonal to Q with Pu = f, and ‖u‖ ≤ ‖f‖/λ₁, where λ₁ > 0 is the gap.
It is smooth by interior regularity, and on a collar {T ≤ t ≤ T + 1} its values are bounded by a constant times the
norm of f.

**Step 4: decay on the cusp, channel by channel.** Write u = e^(−δt) W. Then

    −u″ + u′ + V u = e^(−δt) [ −W″ + (1 + 2δ) W′ + (V − δ − δ²) W ].                         (∗)

- *Zero frequency, c_j > 0.* Here V = ℓ²c_j, and V > δ + δ² exactly when δ < β_j, because β_j² + β_j = ℓ²c_j. The
  solutions of the homogeneous equation are e^(−β_j t) and e^((1+β_j)t). The second is not square-integrable against
  e^(−t) dt, so u is a decaying particular solution plus a multiple of e^(−β_j t). At an interior maximum of |W|,
  (∗) gives (V − δ − δ²)|W| ≤ ℓ² e^(δt)|f|. *[Added 2026-11-19 at Review 85, finding B4: the supremum could be
  approached at infinity, and the step as first written did not exclude that. The repair: u is bounded, being a decaying
  particular solution plus a multiple of e^(−β_j t), so |W| grows at most like e^(δt). For γ in (δ, 1 + β_j + δ) the
  operator of (∗) maps e^(γt) to a positive multiple of itself, since its exponents are δ − β_j and 1 + β_j + δ. So the
  maximum principle compares |W| with M + ε e^(γt), where M is the right side below, and ε → 0 gives |W| ≤ M.]* So

      sup e^(δt)|u| ≤ max( e^(δT)|u(T)| , ℓ² sup e^(δt)|f| / (ℓ²c_j − δ − δ²) ).

- *Zero frequency, c = 0 (the channel of Q).* −u″ + u′ = ℓ²f. The growing solution e^t is excluded as before. So
  u′(t) = ℓ² e^t ∫ₜ^∞ e^(−s) f(s) ds and u(t) = a − ∫ₜ^∞ u′. With |f| ≤ F e^(−δt):
  |u′| ≤ ℓ²F e^(−δt)/(1 + δ) and |u − a| ≤ ℓ²F e^(−δt)/(δ(1 + δ)). This is where the constant a comes from.
- *Nonzero frequencies, all at once.* Let N(t) be the norm over the circle of the part of u with nonzero frequency,
  and F(t) the same for f. Summing the channel equations,

      (N²)″ − (N²)′ = 2 Σ|u_m′|² + 2 Σ V_m |u_m|² − 2ℓ² Re Σ ū_m f_m,

  and (N′)² ≤ Σ|u_m′|² by Cauchy–Schwarz. With K(t) the least of the V_m, this gives −N″ + N′ + K N ≤ ℓ²F wherever
  N > 0. Let m₀ > 0 be the least nonzero |m|. Beyond T₁ = log(max|w_j|/m₀), K(t) ≥ m₀² e^(2t)/4, and K is increasing there, since each V_m is when |m|e^t > |w_j|/2 *[the reason corrected 2026-11-19 at Review 85, finding B5: the line gave the bound's growth as the reason]*.
  Take T₁ larger if needed so that K₁ = K(T₁) > δ + δ². Compare N with

      Z(t) = N(T₁) e^(−β₁(t − T₁)) + ℓ² F₀ e^(−δt)/(K₁ − δ − δ²),   β₁ = (√(1 + 4K₁) − 1)/2 > δ,

  where F ≤ F₀ e^(−δt). N − Z − ε e^((1+β₁)t) is a subsolution of −d²/dt² + d/dt + K₁, it is negative at T₁, and it is
  negative along a sequence tending to infinity because N is square-integrable against e^(−t) dt. The maximum
  principle makes it negative between, and ε → 0 gives N ≤ Z.

**Step 5: from the circle norm to pointwise and Hölder bounds.** A ball of fixed radius in the universal cover at
height t covers the circle about e^t times, and the area of the annulus it covers is about e^(−t). So the
square-integrable norm of the nonzero-frequency part over the ball is bounded by the supremum of N over |s − t| ≤ r.
The interior estimate on the ball, whose constant does not depend on the ball (Step 1), then bounds the supremum of
that part at height t by a constant times e^(−δt) times the norm of f. The zero-frequency parts are functions of t
alone and are bounded in Step 4. Schauder's interior estimate on the same balls, applied to u − aQ, gives the two
further derivatives.

**Step 6.** So u = aχQ + ψ with ψ in C_δ^(k+2,α): u lies in X_δ ∩ Q^⊥ and Pu = f. With Steps 1 and 2, P is a
continuous bijection of Banach spaces, and its inverse is bounded. ∎

**Used and not proved here** (standard): the essential self-adjointness of a Laplace-type operator with a
bounded-below potential on a complete surface; Persson's formula for the bottom of the essential spectrum; interior
elliptic and Schauder estimates.

## 4. What is computed (`verification/cusp_inverse.py`)

The proof's formulas, each checked. K4 and K7 carry a control that breaks them here, and the lock adds controls for K1, K3 and K4; K2, K5 and K6 have none, and K5 and K6 are not in the lock *[corrected 2026-11-19 at Review 85, finding B6: the line said each had the change that breaks it; owed, R85-3]*. The numerics do not prove the theorem.
They test its steps on examples.

| | what | result |
|---|---|---|
| K1 | the channel potential is the perfect square (m e^t + w/2)², equal to w²/4 at m = 0 | exact (sympy) |
| K2 | the conjugation by e^(t/2); the count of eigenvalues below 1/4 + ℓ²c with the cut at 30 and at 60 | exact; 1 and 1 |
| K3 | the identity (∗); β² + β = ℓ²c | exact |
| K4 | zero frequency, c > 0, 40 sources: sup e^(δt)\|u\| against the bound | 1.727 against 4.412 |
| | control: a weight δ = 0.8 beyond β = 0.572 | e^(δt)\|u\| grows: 11, 110, 1074 at t = 10, 20, 30 |
| K5 | c = 0, 20 sources: the two bounds | 1.411 ≤ 1.731 and 2.025 ≤ 5.769 |
| K6 | four nonzero frequencies, 12 sources: the inequality for N, and N against Z | never positive (to the grid); N/Z ≤ 0.557 |
| K7 | a whole surface (a cap closed onto the cusp), the channel of Q, 16 sources orthogonal to the constants | a between −0.866 and 0.422; decaying part 1.081 against 2.564 |
| | control: a source orthogonal to the constants that does not decay | u grows by 1.94 to 2.02 over ten units: no constant tail |

K7 shows why the constant must be adjoined: for decaying sources orthogonal to Q the solution has a ≠ 0, so the
decaying space alone does not reach them.

## 5. What it gives the physical lane, and what it does not

- **Its equation (3) follows for its operator if H1 to H3 hold for its fields.** The proof above is independent of the
  lane's: it uses a maximum principle on the weighted function and a convexity inequality for the circle norm, where
  the lane argues by variation of constants and the bounded inverse theorem. The two agree on every point they share:
  the exponents −β and 1 + β, the exclusion of the growing solution by the measure e^(−t) dt, the constant only in
  the channel of Q, and the condition δ < min β.
- **One hypothesis of the lane's is not needed.** It takes δ < min(1, β_c). Nothing in the proof uses δ < 1.
- **H2's algebra is already on main.** The joint weights of the two principal triples on E6 contain one trivial
  summand, the one at Q = 0 (record physical-ns-01 of B1957, `checks/physical_neutral_source.py`). So their common
  centraliser in E6 is Q.
- **H1 and H3 are not checked by main.** That the lane's background is parallel on the whole cusp end with this
  connection and a constant potential, and that its global gauge operator is nonnegative with kernel exactly Q, are
  statements about its actual fields (its packages P-C3b and P-C3e). They are its model's facts, conditional as before.
  *[Added 2026-11-18: the lane answered this the same day (its reply at 6f074b770; B1957, record physical-m10r-01,
  `checks/physical_m10_reply.py`). With the connection it states, A_x = −H/(4y), the operator on the cusp is exactly
  the channel of H1 with μ = m², the drift included (main's symbolic check). Its bounded kernel is ℝQ by the roster
  of E₆ under the two principal triples (one trivial summand, rebuilt by main) and a cutoff argument main checked by
  hand. What stays a premise of its model: that its background is this parallel pair on the whole cusp, and that the
  global gluing preserves Q. The lane also found main's own indicial check of its package short by a factor ℓ²
  (corrected in B1957); this page's statement had the factor right.]*
- **Its two nonlinear steps.** Their algebra was checked on a finite model (record physical-c3e-04). With the theorem,
  the linear hypothesis of its first implicit-function step holds under H1 to H3. That the moment is a real-analytic
  map between these spaces is the lane's argument (products and exponentials in weighted Hölder spaces, the constant
  tail acting through Q, which commutes with the background). Main finds no fault in it and has not written it out.
- **So the lane's local family of stationary backgrounds stands as a conditional result in its supplied model.** It
  removes no input, selects no amplitude or direction, and is not a join.

## Not claimed

- That the lane's operator satisfies H1 or H3.
- Anything about the lane's physical reading of the family, or about three families.
- An explicit value of the gap λ₁ or of the inverse's norm for the lane's surface.
