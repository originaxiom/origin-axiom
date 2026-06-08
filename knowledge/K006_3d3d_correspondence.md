# K006 — The 3d-3d correspondence (the citable physics, and its firewall)

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). This is the **one** place the project touches real physics literature;
> everything here is **citable background**, nothing promotes to `../CLAIMS.md`, and the firewall (below) is the
> point. Never a premise in a proof.

## The correspondence

The **3d-3d correspondence** (Dimofte–Gaiotto–Gukov, 2011; arXiv:1108.4389, 1112.5179) assigns to a 3-manifold `M` a
3-dimensional `N=2` superconformal theory `T[M]`, obtained by compactifying the 6d `(2,0)` theory on `M`. Its
defining dictionary is an isomorphism of moduli spaces:
```
   M_SUSY( T[M] )   ≅   M_flat( M ; G_ℂ ) ,
```
the supersymmetric vacuum moduli space of `T[M]` equals the moduli space of **flat `G_ℂ`-connections** on `M` — i.e.
the **character variety** (`K001`). For `M` a knot complement and `G_ℂ = SL(n,ℂ)`, the right-hand side is exactly the
object this project computes. Flat connections ↔ SUSY vacua; the **three branches** of the character variety map to
three branches of the vacuum structure.

## What this licenses (and what the project actually cites)

It licenses calling the character variety a **moduli space with a physics name** and citing the dictionary
`M_SUSY ≅ M_flat`, the three-branch ↔ three-fixed-point-class map (the trivial / geometric / Dehn-filling classes,
`K004`, B106), and the Chern–Simons / complex-CS data (volume, torsion) as the asymptotic content (GKLP 1305.0937 for
the higher-rank A-polynomial side). `B101` uses it to recognize the geometric component `V0` as the **Fuchsian locus
of the `SL(3,ℝ)` Hitchin / Fock–Goncharov component**; `B107` (V94, POSTULATED/firewalled) audits the full
physics-connection map and records what survives.

## The firewall — what is NOT licensed

This is the load-bearing part. The 3d-3d correspondence is a statement about **moduli spaces**, and the project keeps
two lines uncrossed (`GOVERNANCE.md`):

1. **No spectral identification.** Tower eigenvalues are **moduli-space monodromy** (`±φ^k`, a single golden scale),
   **not** a mass spectrum or a fluctuation Hessian (`S015`, killed by B107). The KKT/Fibonacci reading (`K007`)
   confirms the trace map is a *quasicrystal* trace map, not a particle spectrum.
2. **No spacetime.** The character variety's metric is **Riemannian**, not Lorentzian (B96/B101); there is no "tower
   of spacetimes" up the ranks (S016–S018, dead). "Time" in "trace-map flow" is iteration-count of a monodromy, not
   physical time (the two-headed-time reading is fenced, `../philosophy/P006`).
3. **Ceiling stated.** The Hitchin → Langlands → `N=4` SYM / class-`S` chain is real and citable, but its **ceiling is
   `N=4` SYM / class-`S`**, *not* the Standard Model, gravity, or cosmology (`S024`, POSTULATED). Every reachable
   physics anchor is special to `n=2` / `m=1`, and the systematic physics-paths sweep is **robustly negative**; the
   physics chapter is **CLOSED**.

## How the project uses it

`K006` is why the project can honestly say its object is "a SUSY moduli space" without claiming any physics result:
the dictionary is borrowed, the firewalled readings live in `../speculations/` (S024 Hitchin, S025/S026/S027 the
heavy forks, all DORMANT or POSTULATED), and **nothing crosses into `../CLAIMS.md`**. The standing prize is purely
mathematical (the functorial `Sym(W) → trace-ring` construction, `K008`).

**Anchors:** B101/V85 (the Hitchin-component reframing), B107/V94 (the physics-connection audit, POSTULATED), B96
(the Riemannian signature). External: Dimofte–Gaiotto–Gukov (3d-3d, 1108.4389 / 1112.5179); Gang–Kim–Lee–Park
(1305.0937, higher-rank); Gaiotto (class-`S`). Firewalled readings: `../speculations/S024`, `S025`–`S027`,
`PHYSICS_BRIDGE_MAP.md`.
