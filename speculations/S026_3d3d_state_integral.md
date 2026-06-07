# S026 — does the SL(n) tower organize the `T[4₁]` state-integral, at fixed knot / varying rank?

**Status: `DORMANT`.** Firewalled; not a claim. Phase 3 of the physics-bridge sweep (a HEAVY/deferred fork,
mapped + obstruction stated). Nothing promotes to `../CLAIMS.md`; the physics chapter stays CLOSED.

**[MATH] (the citable anchor).** The figure-eight complement defines a 3d N=2 SCFT `T[4₁]`; its partition functions
on `S³_b` (squashed sphere), `D²×S¹`, and lens spaces are **state-integrals** built from the quantum dilogarithm
(Andersen–Kashaev; Dimofte–Gaiotto–Gukov), whose **saddle points are the flat connections = the character-variety
points** (`M_SUSY(T[M]) ≅ M_flat(M;G_C)`, K006/B107). The classical limit is the **A-polynomial**; the repo has the
SL(n) A-variety `L=(−1)ⁿ⁻¹Mⁿ` (B71/B83) and the geometric saddle (`vol(4₁)=2.0299`, B96/B82). The Kashaev sum (the
`N`-th colored Jones at the root of unity) is a cheap finite computation whose asymptotic recovers the volume
(feasibility shown, `kashaev_feasibility.py`).

**[LEAP] (kept separate).** Raising the **rank `n`** (at fixed knot 4₁) builds a tower of "higher" 3d theories /
higher complex-CS levels, and the SL(n) tower (the Sym two-sequence) **organizes** the saddle structure / the
holomorphic-block decomposition of the partition function.

**[HOOK] (the concrete computation + its obstruction).** Reproduce the known **SL(2)/4₁** Andersen–Kashaev
state-integral (one quantum-dilogarithm integral; its saddles are the two geometric flat connections), then attempt
**SL(3)** and test whether the saddle multiset / block decomposition is indexed by the tower. **Obstruction (why it
is DORMANT):** the state-integral needs the **quantum dilogarithm** machinery and a careful contour/saddle analysis
— research-level, not a bounded probe; the SL(n≥3) state-integral is at the frontier of the field. Only the
**moduli/classical** level (the A-variety + the saddle = volume) is in-house and citable; the **quantum** partition
function at higher rank is the heavy, deferred part.

**Negative beside the leap (the ceiling).** This is the partition function of a **specific 3d N=2 theory** `T[4₁]`,
not the Standard Model. The bridge is "our SL(n) A-variety is its classical limit and the rank-tower may index its
saddles," not "our object is the SM." The continuous **family-in-m** is DEAD as a moduli family (no Coulomb branch,
forced j=1728; Gate 1/2) — so vary the **rank `n`**, not the seed `m`. Citable chain stops at class-S / N=4 SYM
(K006).

Related: `K006` (the 3d-3d anchor), B71/B83 (the SL(n) A-variety), B82/B96 (the volume), `kashaev_feasibility.py`
(the in-house feasibility witness), `S027` (the modular/cocycle sibling), `PHYSICS_BRIDGE_MAP.md`.
