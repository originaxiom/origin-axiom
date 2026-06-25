# B211 — the metallic family's three faces: geometric limit, chirality spectrum, and the arithmetic of the variety itself

**Date:** 2026-06-25. **Status:** the six remaining *computable* leads from the `OPEN_LEADS` catalog (L29–L34),
run properly and verified. Each claim is **computed, not asserted**, with its load-bearing step locked in a test.
The headline is **L34** (a genuinely new arithmetic face). Firewall-clean low-dimensional topology / arithmetic
geometry / quantum topology; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V211**.

---

## L34 — the arithmetic of the character variety itself (the new face) ★★★

Every prior arithmetic statement about these bundles was about a *number field*: the **monodromy** field
`ℚ(√(m²+4))` (B148…) or the **hyperbolic trace** field `ℚ(√−3)` (B210). L34 asks the never-touched question —
**what is the arithmetic of the character *variety* as a scheme over `𝔽_p`** (its point-counts / Weil zeta)?

**Derivation (not assertion).** The figure-eight (`m=1`) is the 2-bridge knot `b(5,3)`; in the Riley
parametrization `A=[[s,1],[0,1/s]]`, `B=[[s,0],[−u,1/s]]` with relator `a w = w b`, `w = b a⁻¹ b⁻¹ a`, the
non-abelian locus is
```
  R(x,u) = u² + 3u + 3 − (x²−2)(u+1) = 0,      x = tr(meridian).
```
**Verified** against the known complete hyperbolic structure: at the parabolic point `x=2`, `R(2,u)=u²+u+1`, whose
roots are the **cube roots of unity `ω`** — exactly the corrected figure-eight Riley parameter (B210). In trace
coordinates `z = tr(AB) = (x²−2) − u`, the character variety is the plane curve
```
  Φ(x,z) = z² − (x²+1) z + (2x²−1) = 0.
```
It is quadratic in `z` with **`z`-discriminant `(x²−1)(x²−5)`** — a double cover of the `x`-line branched at the
four points `x=±1, ±√5`, hence an **irreducible genus-1 curve**.

**The result (verified for all good primes `p ≤ 97`, 23 primes, exactly — no exceptions):**
```
  #X^{na}(𝔽_p)  =  p − 1 − a_p(E),       E :  y² = x(x−1)(x−5)  =  Cremona 40a1.
```
So the figure-eight's non-abelian `SL(2,ℂ)` character variety is **birational to the elliptic curve `40a1`**:
conductor `40 = 2³·5`, `j = 148176/25`, **non-CM**, rank 0, torsion `ℤ/4`. Its Weil zeta is the L-function of a
**weight-2 newform of level 40** — *not* governed by the trace field `ℚ(√−3)` (which lives only at the single
complete-structure point `x=2`). The two prime sets even differ: the variety's bad primes are `{2,5}`, the trace
field's ramified prime is `3`. **The arithmetic of the object and the arithmetic of its distinguished point are
different objects.**

**Novelty — UNCHECKED, conservative.** The character-variety polynomial `z²−(x²+1)z+(2x²−1)` is **classical**
(figure-eight char varieties are textbook). That it is genus 1 is likely **observed** somewhere. The specific
identification as the non-CM curve **`40a1`** and the **"Weil zeta of the character variety"** framing
*appear* new in this corner but **prior art was not run** — do **not** claim. (The metallic `m≥2` bundles are not
2-bridge knots, so the clean Riley route is figure-eight-specific; their character-variety zeta is a natural
follow-on, not done here.)

## L31 — volume → Borromean: the geometric limit identified ★★

B207 found the metallic bundle volumes converge to `2·v_oct = 7.32772475…` (two regular ideal octahedra). **Why?**
Drilling the (effectively two) short core geodesics of `RᵐLᵐ` returns — **`m`-independently** — a 3-cusped
manifold that SnapPy identifies as the **Borromean rings complement** (`6³₂ = L6a4 = t12067`, two ideal octahedra,
vol exactly `2·v_oct`). Confirmed `m=8, 10` (clean; `m=12` hit a known Dirichlet-domain numerical failure — the
`m=8,10` agreement already exhibits `m`-independence). **So the metallic bundles are the large-twist Dehn fillings
of one fixed 2-octahedron parent (the Borromean complement); the volume ceiling is forced.** Novelty UNCHECKED —
once-punctured-torus bundles as fillings of the Borromean/magic complement is plausibly **folklore** (chain-link
literature); do not claim.

*(In-place correction of B207: the volume growth was first misread as linear; canonical retriangulation showed
geometric convergence to `2·v_oct`, and the "→ Borromean" was unearned until this drilling. Now earned.)*

## L32 — the Chern–Simons / chirality spectrum ★

Every metallic bundle `RᵐLᵐ` (`m=1..6`) is **amphichiral** — *isometric to its orientation-reversal* (SnapPy
`is_isometric_to(reverse_orientation)` = `True`) — hence **`CS = 0`** (computed `|CS| < 1e-15` for all `m`). This
unifies the chirality work (B128–147) with the volume work (B207): the family is **uniformly amphichiral**, so the
candidate scale-carrier (`CS`) vanishes for *all* `m`, not only the figure-eight — the firewall (L15: no invariant
of the unit carries a scale) holds **across the whole family**. Characterization, not new mathematics
(amphichirality of `RᵐLᵐ` follows from the palindromic word / B128–147 machinery).

## L33 — the WRT level-period is a Pisano period ★★

B204 derived the WRT level-period `P_WRT(m) = m(m²+4)/gcd(m²+4,4)` via Gauss sums. It is also **elementary number
theory**: the **Pisano period** of the metallic Fibonacci recurrence `x_{n+1} = m·x_n + x_{n−1}` (the order of
`M_m=[[m,1],[1,0]]`) modulo the discriminant satisfies
```
  π(m, m²+4) = 4·Q(m),   Q(m) = (m²+4)/gcd(m²+4,4),    and    P_WRT(m) = (m/4)·π(m, m²+4).
```
Verified `m=1..12`. So B204's period is a Pisano period of the metallic recurrence — a number-theoretic reading,
complementary to the Gauss-sum proof. Novelty UNCHECKED (Pisano periods of `x_{n+1}=mx_n+x_{n-1}` are standard; the
WRT bridge is the framing).

## L29 — the congruence-tower order ★

The monodromy reduces to a finite group `SL(2,𝔽_{m²+4})`; its order there is
`ord(RᵐLᵐ mod (m²+4)) = 2·Q(m)` (`m=1..12`), an elementary consequence of L33. The shadows are generically
`SL(2,𝔽_p)` (only golden McKay-exceptional, B206); the order tracks the core `Q(m)`, no new invariant beyond it.

## L30 — the skein quotient at `q=e^{2πi/5}` is not `2I` (resolved-negative) ★★

The finite quotient of the B205 skein algebra at the golden root `q=e^{2πi/5}` is the **`SU(2)₃` Verlinde algebra**
(rank `k+1 = 4`). The `2I = SL(2,𝔽₅)` representation ring has rank **9** (its 9 conjugacy classes, B206).
`4 ≠ 9` ⇒ the skein quotient is **not** the `2I` rep ring — it is the *bigger* object (matching B210's WRT image of
order **2880**). Confirms: the WRT/skein ↔ congruence-shadow link is **arithmetic** (`det(γ+I)=m²+4`, B208), not a
representation-ring identity.

---

## Honest status & tiers
- **L34** — `[exact]` for the count relation `#X = p−1−a_p(40a1)` (23 primes, plus the curve identification via
  Sage: conductor 40, non-CM, label `40a1`); novelty **UNCHECKED** (the new framing; do not claim).
- **L31** — `[num, SnapPy]` Borromean identification, `m`-independent (`m=8,10`); novelty **UNCHECKED** (likely folklore).
- **L32** — `[num, SnapPy]` uniform amphichirality / `CS=0` (`m=1..6`); a characterization, not new math.
- **L33/L29** — `[exact]` elementary identities (`m=1..12`); the WRT-Pisano bridge is a framing, novelty UNCHECKED.
- **L30** — `[exact]` rank mismatch (resolved-negative), consistent with B210.

**Firewall:** standalone low-dim topology / arithmetic geometry / quantum topology. No Λ/scale/spectral-mass;
McKay/`2I` references are representation-theoretic. **Nothing to `CLAIMS.md`.**

## Reproduction
- `python charvar_zeta.py` — derive Φ, verify at the complete structure, point-count, the `40a1` relation. (pyenv)
- `python metallic_numbertheory.py` — L33 (Pisano), L29 (order), L30 (rank). (pyenv)
- `sage-python geometric_limit_sage.py` — L31 (drill → Borromean) + L32 (CS / amphichirality). (Sage/SnapPy gated)
- `sage-python` one-liner for the curve: `EllipticCurve([0,-6,0,5,0]).conductor()` → 40, `.has_cm()` → False,
  `.label()` → `40a1`.
- `tests/test_b211_metallic_faces.py` — 7 locks (the L34 Weil-zeta relation is the load-bearing one). All pass.
