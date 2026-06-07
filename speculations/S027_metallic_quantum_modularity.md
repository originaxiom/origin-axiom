# S027 — the metallic Kashaev invariants as a family of quantum modular forms (the GL(2,ℤ) cocycle)

**Status: `DORMANT`.** Firewalled; not a claim. Phase 3 of the physics-bridge sweep (a HEAVY/deferred fork, mapped
+ **feasibility shown in-house**). Nothing promotes to `../CLAIMS.md`; the physics chapter stays CLOSED.

**[MATH] (the citable anchor + the in-house feasibility).** The figure-eight Kashaev invariant `J_N(4₁) =
Σ_{k=0}^{N−1} |(q)_k|²` (`q=e^{2πi/N}`) is Zagier's prototype **quantum modular form** — a function on `ℚ` whose
failure to be modular under `GL(2,ℤ)` is a smooth "cocycle" (the Zagier–Garoufalidis "strange identity"), and whose
asymptotics are the complex-Chern–Simons / volume-conjecture data. **Feasibility is in-house**
(`kashaev_feasibility.py`): the Kashaev sum is a cheap finite computation and `(2π/N) log J_N(4₁) → vol(4₁)=2.0299`
(monotone, from above). So the SL(2)/4₁ side is computable here today.

**[LEAP] (kept separate).** The **metallic family** of knots/links (the `M_m` monodromies) gives a **family of
quantum modular forms**, and the `GL(2,ℤ)` (modular-group) structure of the seed `M_m` is reflected in the
**modular cocycle** of `J_N`. The seed *is* a modular-group element; its quantum modularity should be readable from
the arithmetic of `ℚ(√(m²+4))` (the same field that distinguishes the metallic quasicrystals, S023).

**[HOOK] (the concrete computation + its obstruction).** Compute `J_N` for the metallic knots/links beyond 4₁ and
extract the **quantum-modular cocycle** (the period function under the `GL(2,ℤ)` action); test whether it varies
with `m` through the field `ℚ(√(m²+4))` — tying S027 to S023's arithmetic distinctness. **Obstruction (why it is
DORMANT):** identifying the metallic knots/links for general `m`, computing their colored-Jones at roots of unity,
and extracting the cocycle is a substantial number-theory/quantum-topology computation. **Crucial scoping:** the
continuous **family-in-m is DEAD** as a moduli family (genus locked, forced j=1728; Gate 1/2, V32–34) — so this
fork targets the **arithmetic / the per-knot cocycle**, NOT a moduli family. The bridge is to **number theory /
quantum modularity** (physics-adjacent: CS asymptotics), citable as such — not new fundamental physics.

**Negative beside the leap.** Quantum modularity of the knot invariant is real, established mathematics
(Zagier–Garoufalidis); our contribution would be the **systematic metallic family + the field-dependence of the
cocycle** — not a new physical prediction. Bank it as arithmetic, firewalled.

Related: `S023` (the same `ℚ(√(m²+4))` arithmetic, on the spectral side), `S026` (the state-integral sibling),
B82/V37–V38 (the Kashaev / A-polynomial computations), `kashaev_feasibility.py` (the in-house witness),
`PHYSICS_BRIDGE_MAP.md`.
