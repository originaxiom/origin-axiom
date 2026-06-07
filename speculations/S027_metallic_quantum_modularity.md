# S027 — the metallic Kashaev invariants as a family of quantum modular forms (the GL(2,ℤ) cocycle)

**Status: `DORMANT`.** Firewalled; not a claim. Phase 3 of the physics-bridge sweep (a HEAVY/deferred fork, mapped
+ **feasibility shown in-house**). Nothing promotes to `../CLAIMS.md`; the physics chapter stays CLOSED.

> **⚠ SCOPE (the genuinely-new content is `m≥2`).** The golden case (`4₁`, m=2 in the knot convention) — `J_N(4₁) →
> vol(4₁)` — is **textbook** (the standard volume-conjecture example, ~1995, and Zagier's prototype quantum modular
> form). It is recorded here only as the **in-house feasibility witness**, not as new content. The new content of
> this fork is the **`m≥2` metallic family** (the silver/bronze knots/links): their colored-Jones at roots of unity,
> and whether the quantum-modular **cocycle** varies with `m` through the field `ℚ(√(m²+4))` (tying to S023). Do not
> re-derive the golden case as if it were the result.

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

**[HOOK — the sharpest, decidable form (the phase-structure comparison).** The one computation that would actually
*decide* whether there is metallic-specific content: compute the **specific quantum phases and their degeneracies at
each `k`** for the figure-eight, and compare to **(a)** other knots and **(b)** the metallic family at `m≥2`. A
clear **yes/no** discriminator:
- **YES** — if the phase structure / degeneracy pattern **distinguishes** the metallic family from generic knots,
  that is genuine metallic-specific content (a real fingerprint in the quantum data);
- **NO** — if the metallic family is just "generic knots with a particular trace field," there is no bridge here.

Currently **UNKNOWN — not computed.** This is the right form of "something may be hiding": not a feeling, a specific
computable comparison with a clean verdict. **Tooling gate (do NOT brute-force):** this — and the cocycle extraction
above — need **SnapPy / Magma / custom state-integral code**, not numpy+sympy; beyond the present environment. Bank
as a DORMANT, tooling-gated pointer; do not attempt in a numpy+sympy session.

**Negative beside the leap.** Quantum modularity of the knot invariant is real, established mathematics
(Zagier–Garoufalidis); our contribution would be the **systematic metallic family + the field-dependence of the
cocycle / the phase-structure discriminator** — not a new physical prediction. Bank it as arithmetic, firewalled.
The "something is hiding" instinct is **relocated** here: not in the generic quantum-classical transition (standard
semiclassics; see `TOMBSTONES`), not in fundamental physics (dead), but in *whether the metallic structure
specifically* fingerprints the quantum data — an honest, unanswered, tooling-gated question.

Related: `S023` (the same `ℚ(√(m²+4))` arithmetic, on the spectral side), `S026` (the state-integral sibling),
B82/V37–V38 (the Kashaev / A-polynomial computations), `kashaev_feasibility.py` (the in-house witness),
`PHYSICS_BRIDGE_MAP.md`.
