# Probe B4 — BKL billiard, Gutzwiller weighting, golden Kasner

> **Speculative frontier work.** Logged observations, not claims
> (`../../GOVERNANCE.md` §5). Nothing here is promoted to `CLAIMS.md`.

## The question

`A = LR` is a periodic orbit of the modular billiard — the dynamical system that
models BKL (Belinsky–Khalatnikov–Lifshitz) cosmology near a singularity. Is the
figure-eight orbit the shortest such orbit? How does a Gutzwiller periodic-orbit
sum weight it? What Kasner exponents does its BKL parameter `u = φ` give?

## Findings (`probe.py`)

**Exact:**

- The figure-eight orbit (trace 3, word `LR`) is the **shortest primitive
  periodic orbit** of the modular billiard — length `4·log φ ≈ 1.925`.
- Its Gutzwiller weight is `4·log(φ)/√5 ≈ 0.8608` exactly (uses `sinh(2logφ)=√5/2`).
- At BKL parameter `u = φ`, the three Kasner exponents are
  `p₁ = −1/(2φ)`, `p₂ = 1/2`, `p₃ = φ/2`, and they form a **geometric
  progression with common ratio φ**. (`u = φ` is the *unique* `u` for which the
  Kasner exponents are in geometric progression.)

**Numerical:**

- In a Gutzwiller periodic-orbit sum over orbits up to trace 17, the figure-eight
  orbit contributes **37.8%** of the total.

## Honest verdict — bounded; this is the project's most-caveated material

Every caveat below is load-bearing. This material was the **most walked-back
content in the project's history** (see `legacy/`), and the discipline is to
keep it that way:

- **"Leading" is not "selected."** 37.8% is the largest single share, but the
  ratio to the next orbit is only ~1.13 — *first among equals*, not dominant.
- **BKL describes the near-singularity regime only** — the very early universe,
  a regime that ended billions of years ago. It says nothing about the present,
  isotropic universe.
- **Every Kasner solution satisfies Einstein's vacuum equations** — that is what
  Kasner solutions *are*. The golden orbit gives *one* solution among infinitely
  many; nothing here selects it as physical.
- **The Kasner conditions `Σp=1, Σp²=1` hold for every `u`.** The only
  `φ`-specific fact is the geometric-progression property.
- **"Dominated by the shortest orbit" is semiclassical** (Gutzwiller trace
  formula), not exact quantum gravity.

So B4 is a bounded observation: the figure-eight orbit *is* the shortest
primitive modular-billiard orbit and the leading Gutzwiller term, and `u = φ`
gives golden Kasner exponents — all exact or cleanly computed. But none of it
derives a physical selection principle. **No claim promoted; O1–O5 remain `open`.**
