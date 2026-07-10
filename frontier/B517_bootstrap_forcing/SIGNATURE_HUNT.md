# B517 Phase C — the Lorentzian-signature hunt: (3,1) is REAL but GENERIC (control-filtered)
**Computed 2026-07-11. The control ran BEFORE any physics reading (the B513 lesson applied
pre-emptively). Firewalled; no T-SIG claim.**

## Method (the proper form, not an ad hoc one)
The canonical bilinear form on ℚ(β) is the **trace form** Tr(xy); its signature is a theorem:
(r₁+r₂, r₂) for r₁ real embeddings, r₂ complex-conjugate pairs. It lives on the Minkowski embedding =
the 1 expanding + 3 contracting eigendirections of the substitution (the "spacetime"). This passes the
legitimacy test B513's Hessian failed (natural on the spacetime, not the parameter space).

## Result + control (the filter)
| field | (r₁,r₂) | trace-form signature |
|---|---|---|
| **golden β=φ(1+√φ)** | (2,1) | **(3,1)** Lorentzian |
| silver canonical coupling | (2,1) | (3,1) |
| bronze canonical coupling | (2,1) | (3,1) |
| tetranacci (control) | (2,1) | (3,1) |
| child field x⁴−x−1, d_K=−283 (control) | (2,1) | (3,1) |
| totally-real x⁴−4x²+1 (control) | (4,0) | (4,0) Euclidean |
| totally-complex x⁴+1 (control) | (0,2) | (2,2) |

**(3,1) is GENERIC to any quartic with one complex place** — β, silver, bronze, tetranacci, and the
child field all give it; totally-real quartics give (4,0), two-complex-pair give (2,2). So the Lorentzian signature is
NOT golden-specific and NOT object-forced — it is the generic arithmetic of "2-real-1-complex" number
fields. **T-SIG via the canonical form FAILS the control gate.** Verdict: the Lorentzian signature is
real but laundered (generic); firewalled, not a physics signal.

## Honest structural note (recorded, not promoted)
The single timelike direction is the **imaginary part of the contracting complex pair** (trace form =
+β² + (−0.44)² + Re² − Im²), NOT the expanding β direction. If it meant anything, "time" would be the
phase/rotation of the contracting dynamics, not the expansion — but this too is generic across (3,1)
quartics.

## The prep gap (what a MEANINGFUL hunt would need)
A form tied to the substitution DYNAMICS (not just the field), (3,1) for the object AND control-
distinguishing. The trace form only sees the generic splitting type. No canonical dynamical Lorentzian
form is in hand; candidates (coupling-asymmetry form; Rauzy-boundary geometry) must each clear
"natural, not ad hoc" first — the B513 trap. TERMINAL for this pass: T-SIG via the canonical arithmetic
form = generic/laundered; the dynamical-form hunt is NEEDS-A-CANONICAL-CANDIDATE, not run.

---
## Addendum (2026-07-12): the Lyapunov (3,1) [cross-seat, chat1] + control C1 — ALSO generic
Chat1 built the DYNAMICAL form I flagged as the prep gap: the Lyapunov (expanding/contracting) form of
the substitution M*, NOT the field trace form. Verified: M* eigen-exponents {+1.302, −0.241, −0.241,
−0.821} ⟹ signature **(1,3) = Lorentzian (3,1)**, a genuinely DIFFERENT object from the trace form (its
timelike direction is the Perron eigenvector (φ,1,φ√φ,√φ), orthogonal to the trace-form's imaginary
direction). Chat1's new content — the phase diagram ((3,1)→(2,2) transition at p(M*)≈0.3–0.5), the
(2+1) spatial anisotropy (the complex pair gives two equal contracting exponents), the det(M*)=−1
orientation reversal — all verified.

**Control C1 (run this session — the decisive test chat1 named as needed): the Lyapunov content is
GENERIC.** Running the identical computation on controls:
| quartic Pisot | Lyapunov signature | (2+1) anisotropy |
|---|---|---|
| golden M* | (1,3)=(3,1) | yes |
| **tetranacci** (x⁴−x³−x²−x−1, NON-golden) | **(1,3)=(3,1)** | **yes** |
| child-type x⁴−x−1 | (1,3) Stein [CORRECTED: 3 unstable+1 stable, NOT (2,2)] | — |

Tetranacci — a completely non-golden quartic Pisot — gives the IDENTICAL (3,1) + (2+1) structure. So
the Lyapunov form's existence AND its (2+1) anisotropy are generic to the **(2-real,1-complex) splitting
type** — the SAME genericity that killed the trace form. The signature is determined by the splitting
type (child-type = 2 complex pairs → (2,2)), not by anything golden. Object-specific remainder: det=−1
and the φ/√φ Perron nesting — both "golden because golden," not Lorentzian-forced. The phase-transition
*point* differs between Pisot numbers only trivially (different eigenvalues → different crossings), not
as meaningful structure.

**Integrated verdict: BOTH (3,1) structures (trace-form + Lyapunov) exist, are different objects, and
are BOTH GENERIC.** T-SIG fails via both the arithmetic and the dynamical canonical form. **D6 stays
CLOSED** — chat1's own C1 control, now executed, confirms it. Chat1's dynamical form was the right kind
of object and its honest framing was correct; the control delivers the verdict it anticipated. (Chat1's
C3/Malament — does the FULL Level-1 monoid preserve one cone — remains the one un-run distinguisher, but
it too would need to beat the same splitting-type genericity.)


---
## Addendum 2 (2026-07-12): the EXACT rational Stein form [cross-seat GPT-5.6, re-derived] + a correction
**Chat3/GPT-5.6 supplied the exact rational Lyapunov/Stein representative of the (1+3) split; verified
here by independent recomputation (no files ingested).** For the golden Rauzy incidence M∗, the discrete
Stein equation **MᵀGM − G = −I₄** has the unique symmetric solution
```
G = (1/11) [[12,−8,−5,−4],[−8,20,−4,−1],[−5,−4,14,−13],[−4,−1,−13,27]]
```
Verified EXACT: symmetric; residual MᵀGM−G+I = 0; det G = −9/11; leading minors 12/11, 16/11, 12/11,
−9/11; **signature (3,1)**; the Perron vector is TIMELIKE (q<0); positive on the 3d contracting/Rauzy
space. **Strict cone identity: q(Mx) = q(x) − |x|²** — so M is a *dissipative* Lorentzian map (the
future cone is strictly preserved, not isometrically). This upgrades the qualitative Lyapunov (1+3)
split to an exact rational metric.

**CORRECTION (owned): my Lyapunov control listed x⁴−x−1 as "(2 complex pairs) → (2,2)". WRONG** — x⁴−x−1
has 2 real + 1 complex pair, and its Stein inertia (stable,unstable) is **(1,3)** (3 unstable, 1 stable).
Corrected. Controls (Stein inertia = the stable/unstable split): golden (3,1), tetranacci (3,1) [both
Pisot: exactly 1 unstable], silver (2,2) [not Pisot: 2 unstable], x⁴−x−1 (1,3) [not Pisot: 3 unstable].
So the **(3,1) Stein signature IS the Pisot condition** (1 expanding direction) — generic to Pisot
quartics; tetranacci shares it. **Genericity verdict UNCHANGED; D6 STAYS CLOSED.**

**The remaining canonicity gap (honest):** M alone does NOT fix a unique metric — for every W≻0,
MᵀG_W M − G_W = −W has a unique causal form, and W=I (atomic) vs invariant-frequency weighting give
non-proportional G's. The open question: does the Origin object force a unique positive one-step form W
(up to scale + substitution equivalences: relabeling, copy-exchange, reordering, state-splitting, strong
shift equivalence, conjugacy)? Un-run.

**Claim boundary (KNOWN-THEOREM APPLICATION — the discrete Stein/Lyapunov inertia theorem, W≻0):** SAFE
— the exact rational Stein solution, uniqueness for the chosen W, Lorentzian inertia, strict future-cone
preservation, positive metric on the Rauzy stable space, the controls. NOT CLAIMED — physical spacetime,
Lorentz-invariant dynamics, a 4-manifold, GR, object-unique (3,1), or reopening D6. The evolution is
dissipative (q(Mx)−q(x) = −xᵀWx). Firewalled.
