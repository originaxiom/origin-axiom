# B290 — The core-geodesic scale ladder, and why the filling n is not the level k

**Status: banked. The ladder is verified two methods; the n=k identity is a clean negative; the G·Λ link is HELD.
Nothing to `CLAIMS.md`.** Phase III of the seam arc (wall #5, scale). B286 found scale generated at the seam (core
geodesic `~ 2π/n`). B290 makes the asymptotic precise and tests whether the filling integer `n` is the program's WRT
level `k`.

## 1. The ladder (POSITIVE — math)
The **complex** core length of the `(1,n)` filling is
```
    ℓ_ℂ(1,n) = 2πi/n + (π/√3)/n² + O(1/n³),
```
so `|ℓ_ℂ| ~ 2π/n` (confirming B286). The `1/n²` correction coefficient is **`π/√3 = 2π/|τ_cusp|`**, with the cusp
shape `τ_cusp = 2√3·i` — i.e. the ladder is the **Neumann–Zagier** core-geodesic ladder, **controlled by the cusp
shape**. (The `1/n³` imaginary term is `π/6`, a geometric NZ coefficient.)

**Two methods:** (1) SnapPy `core_length` directly; (2) the correction coefficient **predicted independently** from
the separately-computed cusp shape (`2π/|τ_cusp| = π/√3`) — matches the measured `Re(ℓ_ℂ)·n² → 1.81379` to 5 digits.

**Caveat (red-team, Arc II — m004-specificity).** The NZ correction is genuinely the *complex* coefficient
`2πi/τ`; it lands as a *clean real* `π/√3` only because m004's cusp shape `τ=2√3·i` is **purely imaginary**. On a
manifold with a non-imaginary cusp shape (e.g. m003, `τ=½+0.866i`) the correction splits into a real `1/n²` part plus
a separate `~−π/n` imaginary term. So the tidy real-coefficient form is figure-eight-specific (the claim is scoped to
m004 and labels it the NZ ladder); the *generic* statement is "`ℓ_ℂ = 2πi/n + (2πi/τ)/n² + …`."

## 2. The filling `n` is NOT the level `k` (NEGATIVE)
- The filling coefficient `n` is a **topological** Dehn-surgery integer.
- The WRT level `k` (B204) is a **quantum** root-of-unity parameter, `q = e^{2πi/(k+2)}` (B204's own shifted level is
  `k+2`, a *different* integer again).
- They are **independent axes**: one can evaluate the WRT invariant at *any* level `k` of the `(1,n)`-surgered
  manifold. So **"filling `n` = level `k`" is a formal substitution, not an identity.** The scale ladder is a
  geometric `1/n` ladder; the level is a quantum parameter. The seam *generates* scale, but it does not *identify*
  the filling with the level.

## 3. The G·Λ link (HELD — firewalled)
Under the formal substitution `k = n`, the firewalled relation `G·Λ = 6π/k` (S043/B259) gives
`core = 2π/n = (G·Λ)/3` — a numerical coincidence carrying the **122-order gap**. **HELD, not banked**: there is no
derivation that the core length *is* the cosmological length, and the value-match would need a null-hypothesis test.

## Where this lands (the scale axis of selection)
B290 shows the seam **generates** a clean, NZ-controlled scale ladder (math), but the ladder does **not** by itself
distinguish a closing or identify the level — consistent with the seam reframe (scale is born at the boundary, its
*value* is gapped). The next probe (B291) asks whether any closing is *scale-extremal* (a different scale-selection
axis); B294 tabulates.

## The fence
The ladder and its NZ correction are pure geometry. The `n=k` identity is **refuted** as an identity (independent
axes). The `G·Λ` link is **HELD** with the 122-order gap. Nothing to `CLAIMS.md`.

`core_scale_ladder.py` (sage-python: SnapPy core_length + cusp-shape prediction) · `verdict.py` (pyenv; recomputes
`2π/|τ|`) · `tests/test_b290_core_scale_ladder.py`. Related: `B286` (the seam, `2π/n`), `B204` (the WRT level/period),
`B263` (the NZ frame), `S043`/`S044` (G·Λ, the 122-order gap), `B250` (volume/geometry), `B291` (scale-extremal).
