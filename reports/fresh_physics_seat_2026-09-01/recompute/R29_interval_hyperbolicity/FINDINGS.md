# R29 — interval + exact certification of the 112-member ℚ(√−3) family (R3 §3 items 8 / 23)

**Verdict: CERTIFIED (three layers, all 112/112; the R23 carrier set and the seven R24 members
included). What stays uncertified without Sage is listed in §4 in one sentence.**

R3 §3 item 8 said: *"no verified interval arithmetic anywhere"* behind the SnapPy-dependent results
(R21, R23, R24, B1088, B1186, B1163). SnapPy's own `verify_hyperbolicity()`, `isometry_signature(verified=True)`
and `canonical_retriangulation(verified=True)` all raise `SageNotAvailable` on this box, so the certificate
below is an independent implementation, written and run by this seat, of the standard argument, plus two
exact layers that the banked arcs never had.

## 1. What was computed (three scripts, ~6 s total)

| layer | script | statement certified | result |
|---|---|---|---|
| (a) interval | `r29_krawczyk.py` → `r29_results.json`, `r29_run.txt` | the numerical shapes of the census triangulation are within 10⁻⁴⁰ of a **unique** zero of the log-form gluing equations, all edge/meridian/longitude rows hold exactly there, and Im z > 0 on the whole box ⇒ the triangulation is geometric and the zero is the **complete hyperbolic structure** | **114/114** (112 R23 members + m015, m016 controls; R24's s118, o10_150700, t12840, s955 are members) |
| (b) exact shapes | `r29_exact_shapes.py` → `r29_exact_shapes.json/.txt` | the fitted candidates wᵢ = aᵢ + bᵢ√−3 satisfy **every** multiplicative gluing equation **exactly** (Fraction arithmetic in ℚ(√−3)) and lie inside the layer-(a) box (distance to the 212-bit shapes ≤ 3.9 × 10⁻⁵⁸ ≪ 10⁻⁴⁰) ⇒ by uniqueness the true shapes **are** the candidates: **shapes ∈ ℚ(√−3) is now a theorem for all 112, not a 10⁻⁴⁰ fit** | **112/112**; max denominator 98 (t06829), 79 members have denominator 2 |
| (c) exact cusp shapes | `r29_exact_cusp_shapes.py` → `r29_exact_cusp_shapes.json/.txt` | cusp modulus τ of every cusp from the exact shapes by Neumann–Zagier linear algebra over ℚ(√−3) (edge Jacobian kernel, meridian normalised, longitude read off); compared **strictly** (same complex number, 10⁻⁹) with `cusp_info()['shape']`; then SL(2,ℤ)-reduced **exactly** | all **183 cusps** agree with SnapPy; 0 moved under reduction; reduced τ = 2√3i on exactly **7 cusps**: m004[0], t12840[1], o9_41001[0], o9_41009[0], o10_150684[1], o10_150685[2], o10_150693[0] |

Mechanics of (a), so a reader can refute it: mpmath `iv` at 300 bits; branch integers kⱼ read off the
212-bit solution (residual gate 10⁻⁵⁰); square subsystem = edge rows to rational rank n − c plus the c
meridian rows (Neumann–Zagier); Krawczyk operator K(X) = z₀ − Y F(z₀) + (I − Y J(X))(X − z₀) strictly
inside X ⇒ exactly one zero; the dropped edge rows are exact ℚ-combinations of the retained ones (the
combination's F/(πi) is computed as an exact rational and must be even — it was 0 on all 185 dropped
rows, with lcm-denominators D ∈ {1, 2}), and every dropped row is additionally evaluated on K(X)
(contains 0, diameter < 2π/D). Longitude rows are not linear consequences; they follow geometrically
(a similarity commuting with a translation is a translation) and are interval-checked on K(X) as a
cross-check. Family sizes: 2–10 tetrahedra, 1–5 cusps.

**Negative controls** (`r29_controls.py` → `r29_controls.txt`): the torus-knot complements 3_1, 5_1, 7_1
(non-hyperbolic; SnapPy: "contains flat tetrahedra") pass Krawczyk — the flat solution *is* a zero of the
log form — and are correctly **refused** at the Im z > 0 gate; a 10⁻³⁰ perturbation of m004's shapes is
refused at the residual gate (1.7 × 10⁻³⁰ vs 10⁻⁵⁰); m015/m016 (cubic shape field) are refused by layer (b)
(fit candidates fail the exact equations, distance 5 × 10⁻⁵ from the box). So the certificate can fail.

Convention note (c): SnapPy's `'rect'` cusp rows give the derivative ratio v/u = conj(τ) relative to the
orientation of `cusp_info()['shape']`; the conjugate is taken once, globally, and then agreement is strict on
all 183 cusps including the non-real moduli (m003: ½ + ½√−3). 2√3i is fixed by every convention anyway.

## 2. What this changes in the banked ledger

- **B1186 / R23 claim (i)** ("all shapes in ℚ(√−3), denominator ≤ 256") — upgraded from *fitted at 10⁻⁴⁰*
  (R23) and *double precision, tol 10⁻⁹* (the banked instrument) to **exact**. The family census of 112 is
  the double-precision *pre-filter*'s output; layer (b) certifies the 112 positives exactly. It does **not**
  certify that no other census manifold was missed by the pre-filter (a member with shapes in ℚ(√−3) but
  denominator > 256, or a numerical near-miss, would not be in the 112) — that negative half was and
  remains a numerical sweep (R23, 212,641 manifolds, tol 10⁻⁹).
- **B1186 / R23 claim (ii)** (six carriers of 2√3i besides m004) — now **exact**: the seven cusps above,
  name-for-name and cusp-index-for-cusp-index with R23 and the bank. The *instrument* B1186 used (raw
  double-precision `cusp_info`, tol 10⁻⁶, no reduction) happened to give the right answer; the exact
  reduction shows why (no cusp modulus in the family moves under SL(2,ℤ) reduction).
- **B1186 / R23 claim (iii)** (quine) — the cusp-shape leg is exact; the volume leg (ratios 1, 2, 3, 4, 5 to
  Vol(m004) at 220 bits) is **still numerical**. Exact volume ratios need Bloch-group / dilogarithm
  identities, not shapes; not attempted.
- **R3 §3 item 8** ("no verified interval arithmetic anywhere") — no longer true for the *hyperbolic
  structure* leg. Still true for the legs named in §4.
- **R24's seven members** — their complete structures and shape fields are certified; their **amphichirality
  verdicts are not** (see §4). The R24 DISCREPANCY (s118, o10_150700 chiral) therefore stands on the same
  footing as before: SnapPy's unverified `is_isometric_to`/`symmetry_group` plus the CS ∈ {0, ¼} consistency
  check, plus (for o10_150700) R30's `symmetry_group()` order 2.

## 3. Physics content

None is added. Everything here is 3-manifold arithmetic (shapes in ℚ(√−3), cusp moduli, a uniqueness
certificate). It hardens the *object* the thesis names (m004 and its ℚ(√−3) census family) — it says nothing
about whether that object determines an observable. In the seat's words of record: **no observable content**
is created or removed by R29.

## 4. Not certified here (Sage-only) — relay item for cc's bench

Chern–Simons values, symmetry groups, isometry classes and amphichirality (`isometry_signature(verified=True)`,
`canonical_retriangulation(verified=True)`, `verify_hyperbolicity()`) need Sage. A cc seat with Sage can run
them on the 112 in minutes; until then every amphichirality row in R20/R24 (the 38/112 split) is SnapPy-unverified
numerics, as R3 already said.

## 5. Reproduce

```
cd reports/fresh_physics_seat_2026-09-01/recompute/R29_interval_hyperbolicity
python3 r29_krawczyk.py            # 114 manifolds, ~6 s  -> r29_results.json, stdout as r29_run.txt
python3 r29_exact_shapes.py        # 112                  -> r29_exact_shapes.json / .txt
python3 r29_exact_cusp_shapes.py   # 112, 183 cusps       -> r29_exact_cusp_shapes.json / .txt
python3 r29_controls.py            # negative controls    -> r29_controls.txt
```
Inputs: SnapPy's `OrientableCuspedCensus` triangulations (via `Manifold(name)`) and R23's
`sweep_candidates.json` (the 112 names). mpmath 300-bit interval arithmetic; sympy for the exact ℚ-rank
bookkeeping in (a); Python `Fraction` pairs for (b) and (c).
