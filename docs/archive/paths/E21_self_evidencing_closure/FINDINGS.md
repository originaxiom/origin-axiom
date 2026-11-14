# E21 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

(a) **The exact fact is real.** On `I = c² − 1`, the half-return Jacobian's
restricted characteristic polynomial is `t² − (4c² − 2)t + 1`, equal to
`char(M²)` exactly at `I = m²/4` (`λ = m`). Verified symbolically.

(b) **The exact fact is trivial.** It is the single linear identity
`4c² − 2 = m² + 2`. The "self-model discrepancy" `D(I) = (4I − m²)²` is the
squared residual of that identity; the "action-matching" and Fisher-information
statements are the same identity re-expressed through eigenvalues. One equation,
several costumes.

(c) **The framing is analogy, not derivation.** Mapping `D(I)` to Friston's
variational free energy is a structural parallel (`D(I)` is a coefficient
residual, not a divergence between distributions); the parallels to SSB and
einselection are likewise nomenclature. The originating write-up concedes the
non-derivation explicitly. No observable is predicted.

## Why it is quarantined here and not in PC12

This is the project's documented failure mode — exact algebra re-narrated as a
grand unifying principle (here the Free Energy Principle). Per
`../../docs/atlas/FAILURE_ATLAS.md`, the missing object is an **observable with a
comparison target** (and, for the FEP reading, a stochastic/quantum framework in
which `D(I)` is genuinely a free energy). The exact algebra belongs to the
standalone trace-map mathematics (`frontier/B51`, `frontier/B54`, PC12); the
self-evidencing/free-energy interpretation does not, and is kept out of PC12.

## Further controls (2026-06-02)

(d) **Fisher information = Weil–Petersson coefficient (exact, but elementary).**
The Fisher information of `D(I)` is
`F(m) = 16/(m²(m²+4)) = 16/disc(char(M²)) = 16·g_WP(m²+2) = (4/Δ_eig)²`, where
`g_WP(α) = 1/(α²−4)` is the Goldman/Weil–Petersson metric coefficient and
`Δ_eig = m√(m²+4)` the eigenvalue gap of `M²`. The identity is exact (verified
symbolically) but follows from the chain rule on `LE(I)=arccosh(2I+1)` plus the
elementary `disc(t²−αt+1)=α²−4=1/g_WP(α)`. The originating session itself flags
the geometric reading as possibly "just calculus"; the "Teichmüller geometry
controls self-evidencing sharpness" framing is **recorded, not promoted**.

(e) **Aubry self-duality at `λ=m` is dead (no metal–insulator observable).** The
duality map `λ → m²/λ` has `λ=m` as its trivial fixed point, so "self-dual at
`λ=m`" is vacuous. The off-diagonal m-metallic model has **no** genuine Aubry
self-duality at `λ=m` for `m≥2` (session IPR test: `IPR(λ) ≠ IPR(m²/λ)` off the
fixed point); for `m=1` the known `λ→1/λ` duality is already literature. This
removes a tempting physical reading of `λ=m`. Recorded in
`../../docs/atlas/FAILURE_ATLAS.md`.

Both controls **strengthen** the verdict: one is an exact-but-elementary identity
dressed in geometry, the other kills a physical reading. Neither produces an
observable.

## Verdict

`STALLED`

The exact algebra (one identity) is real; the self-evidencing / variational
free-energy reading supplies framing, not force, and predicts no observable.
This instantiates E18 (self-consistency / bootstrap) without supplying E18's
missing ingredient: a consistency condition that forces a *physical* selection.
Not promoted; no Origin-core claim changes; nothing here enters PC12.
