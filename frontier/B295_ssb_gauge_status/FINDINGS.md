# B295 — The SSB / gauge status of the CP sign (Chat-2 adjudicated)

**Status: banked (frontier). The computable kernel is verified; the physics is firewalled; two stop-gates named.
Nothing to `CLAIMS.md`.** B289 banked that the closing forces a CP sign *law* but the *sign itself* is external.
Chat-2 argued the externality is **not** a Curie wall but (a) an **SSB** loophole and (b) **gauge** redundancy
(`τ` gauged ⟹ sign pure gauge). Verify-don't-trust: this tests the computable pieces and gates the rest.

## The adjudication
1. **Curie is not a hard wall — Chat-2 is right (correction to P011/B286).** Curie's principle has the famous
   **spontaneous-symmetry-breaking** loophole: a symmetric system *does* select an asymmetric outcome when a running
   control parameter destabilizes the symmetric point. So "Curie forbids the sign — theorem not preference" (P011)
   was the **wrong argument**.
2. **But the SSB "τ-symmetric double-well potential" is ABSENT (computed NEGATIVE).** The program's gradient potential
   `V(τ) = κ(τ³/3 − τ²/2 − τ)` (P15/P16) is the **wrong object** on three counts:
   - its `τ` is the **modular** parameter on ℍ (`A` acts by `τ→(2τ+1)/(τ+1)`), **not** the amphichiral involution;
   - its critical points are **golden** `φ = (1+√5)/2` (min), `−1/φ = (1−√5)/2` (max) in `ℚ(√5)` — **disjoint** from
     the **Eisenstein** `±π/6` vacua `ω, ω² ∈ ℚ(√−3)` (verified disjoint, sympy);
   - it is a **cubic with exactly one minimum** (`φ`) and one maximum (`−1/φ`), unbounded below — so it **cannot** be
     the degenerate **double-well** SSB requires (a cubic rules out SSB regardless of which `τ`, which only sharpens
     the point).
   The conflation of the two `τ`'s is the trap. **SSB-availability is not demonstrated.** (The degenerate `±π/6`
   vacua themselves *do* exist — the two conjugate Riley roots of the real polynomial `u²+u+1`, swapped by complex
   conjugation = `τ` — but they are inert without a potential.)
3. **"τ is gauged" is a STOP-GATE.** Chat-2's "sign is pure gauge" reads B279's topological **FIX** bit as `τ`
   gauged — the parity-anomaly/η-invariant link B279's own status flags as **unverified**. NEEDS-SPECIALIST. The
   gauge reframe stays **conditional**.

## Net (sharper than both CC's and Chat-2's framings)
B289 **stands**: the sign is **external** because the object is **CP-symmetric** (delivers `±π/6` symmetrically). But
the **reason is open** — **not** "Curie forbids it" (refuted), and **not** an established "pure gauge" (`τ`-gauged
unverified). The honest statement: *the sign is not object-derivable because the object is CP-symmetric, and no
symmetry-breaking mechanism (SSB or gauge-fixing) is established in-sandbox.* This is, if anything, a **sharper
firewall** — the externality is real, its mechanism is genuinely open.

## The live frontier (Chat-2's genuinely-new question)
Does the **running de Sitter clock** (`k`, via `T_dS ~ 1/√k`) **dynamically gauge-fix** the `τ`-sign (→
matter-over-antimatter internal, fixed by *when* on the clock), or is it truly pure gauge (→ external)? The structure
is computable (the peripheral symplectic, B293); the **trajectory** is specialist-gated. This is the shared frontier
of B293 + B295.

## Firewall
SSB / gauge / baryon physics is **HELD/[LEAP]** in `speculations/S038` (updated). The two stop-gates ("τ is gauged",
"does running k gauge-fix the sign") are surfaced, not ground. Nothing to `CLAIMS.md`.

`ssb_gauge.py` (pyenv sympy: the ±π/6 vacua, V(τ) critical points, the disjointness catch) · `verdict.py` ·
`tests/test_b295_ssb_gauge_status.py`. Related: `B289` (the CP sign law), `B285` (±π/6), `B286` (the seam),
`B279` (the spin-structure FIX bit — the gauge premise), `P011`/`P15`/`P16`, `S038` (firewalled), `S043`/`S044`.
