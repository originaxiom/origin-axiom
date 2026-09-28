# B1395 — THE FREE CUSP IS CHARGE-BLIND AT FINITE ENERGY: in 7d SYM only the Higgs field and gauge flux can tell charge q from −q. At a free cusp the Higgs field decays. A Higgs class alive on the cusp torus has logarithmically divergent norm, so it is fixed boundary data, not a dynamical field. A gauge flux through a hyperbolic cusp torus has quadratically divergent energy. And a boundary condition uniform over the torus adds −χ(T²) = 0. So every finite-energy, normalizable datum at a free cusp is charge-blind except the decaying Higgs tail, which B1388–B1393 showed is not a physical count. A completion that yields normalizable chiral matter must cap the cusp and carry a flux on its torus, or bring non-normalizable sources.

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's question after B1393, "what physical
ingredient at a free cusp knows the sign of the charge?" · **Status:**
- PROVED: the elimination, elementary.
- COMPUTED: the cusp integrals, exact in sympy, and one free mode by quadrature.

**Fence:** the seat's frame; the hyperbolic cusp metric; classical energies and norms, no quantum completion. · **Price:** unchanged,
0 of 19 · **Numbering:** B1395.

## 0. Seen from above

B1393 showed that a count needs end data that flip with the charge. This arc asks which data at a free cusp can do that, and finds
that no finite-energy field there can.
- **What flips.** In 7d super-Yang–Mills only two things change under q → −q: the Higgs field, which enters as qφ, and gauge flux,
  which enters as qF. Flat unitary Wilson lines cannot: charge −q is the complex conjugate of charge q.
- **The Higgs field.**
  - A Higgs class alive on a cusp torus (a sealed cusp) has L² norm growing like log(height).
  - It is therefore not a normalizable four-dimensional modulus but fixed boundary data.
  - A dynamical Higgs vev is cuspidal: its field decays at every cusp.
- **Gauge flux.** A flux through a hyperbolic cusp torus has energy growing like height². The torus shrinks and the field strength is
  squeezed into it.
- **Uniform conditions.** A boundary condition uniform over the torus, of relative or absolute type in each sector, adds −χ(T²) = 0,
  whichever sector gets which.
  - This covers orbifold (parity) walls, with or without a charge-conjugating twist.
  - The only charge-odd integers a torus end can carry are the Euler characteristic of a sign partition and the degree of a line
    bundle (Riemann–Roch on T²: index = degree).

## 1. The statements

Let c be a cusp with coordinates (x, y, h), metric (dx² + dy² + dh²)/h² and coordinate torus area A.

**(a) Sealed Higgs classes are non-normalizable.**
- For ω = a dx + b dy (a class alive on the torus, B1392's sealed case): |ω|² = h²(a² + b²).
- ∫_{h₀}^{H} |ω|² dvol = A(a² + b²) log(H/h₀), which diverges.
- Consequence: the Higgs vevs that are normalizable four-dimensional moduli are cuspidal, and every cusp is free for them. Sealed
  classes are fixed boundary data.

**(b) Free cusps are finite.**
- The modes of a cuspidal class at a free cusp are d(c h K₁(2π|k|h) e^{2πik·x}) (B1387). Their norm converges: the density decays
  like e^{−4π|k|h}.
- One mode computed: norm 2.84·10⁻⁶ on [1, ∞).

**(c) Flux through a cusp torus has infinite energy.**
- For F = φ dx∧dy, the flux Aφ is the same through every horospherical torus, since dF = 0. Then |F|² = φ²h⁴.
- ∫_{h₀}^{H} |F|² dvol = Aφ²(H² − h₀²)/2, which diverges.
- So no finite-energy gauge field carries flux through a hyperbolic cusp. This holds whatever sources the flux: a commutator
  [φ, φ] of a non-commuting (T-brane) Higgs field, or a monopole.

**(d) Uniform conditions add nothing.**
- A condition uniform over T_c, of relative or absolute type in each charge sector, contributes −χ(T_c) = 0 to the frame's count
  (B1351 (ii), whole-torus convention). The whole-torus flip is included: relative for q, absolute for −q.
- Non-zero contributions need either a partition of T_c with χ(∂⁺) ≠ 0 (the frame's disc patterns) or a line bundle on T_c of
  degree n. For the latter, the Dirac index on T² is n (Riemann–Roch in genus one), and a charge-q sector sees qn.

**(e) The menu.** Combining (a)–(d) with B1388–B1393:
- The finite-energy, normalizable data at a free cusp are charge-blind, except the decaying Higgs tail.
  - That tail's partition moves with the cut inside the embedded region (B1388).
  - Its modes are not normalizable on the complete manifold (B1392, B1393's remark).
- A completion that gives normalizable four-dimensional chiral matter must therefore do one of two things:
  - cap the cusp and carry a flux on its torus, where capping makes (c)'s energy finite; or
  - bring non-normalizable sources, whose strengths are fixed data (the lane's R28).
- In both cases the charge-odd integer is an input of the completion. It does not come out of the dynamics.

## 2. Computed (`verification/cusp_ends.py`; record `cusp_ends_run.txt`)

| quantity | result |
|---|---|
| \|a dx + b dy\|² | h²(a² + b²) |
| its L² norm to height H | A(a² + b²) log(H/h₀) → ∞ |
| one free mode, k = 1: its L² norm on [1, ∞) | 2.8420894·10⁻⁶ |
| that mode's density × e^{2πh} at h = 10, 20, 40 | 5.1·10⁻²⁷, 2.6·10⁻⁵⁴, 7.0·10⁻¹⁰⁹ |
| \|φ dx∧dy\|² | h⁴φ² |
| its energy to height H | Aφ²(H² − h₀²)/2 → ∞ |
| χ(T²); the Riemann–Roch index for degrees −2 … 3 | 0; −2, −1, 0, 1, 2, 3 |

## 3. What this settles, and what it does not

**Settled.** The answer to the owner's question inside the frame: no finite-energy field at a free cusp knows the sign of the
charge. The datum must be supplied by the completion, as a flux on a capped cusp torus or as a non-normalizable source.

**Not settled.** Which completion physics chooses. Two are named for sealed tests; neither is chosen here:
- **A capped cusp with flux (B1396).**
  - At an Eisenstein cusp that respects the order-3 rotation, the flux degree is fixed mod 3 by the lift's weights at the rotation's
    three fixed points. These are the endpoints of B1390's fixed arcs, whose weights B1394 computes.
  - An M-theory reading of the cap, speculative: a Hořava–Witten E₈ wall. At a cut its worldvolume ℝ^{3,1} × T_c × ℂ²/Γ is ten
    dimensional, its orbifold conditions are uniform on T_c (so (d) gives 0), and its E₈ bundle can carry the flux.
- **Sources (the lane's R15/R24).** These are non-normalizable (R28).

0 of 19.

## 4. Fences

- **The frame's.** Classical norms and energies on the fixed hyperbolic cusp. A changed metric near the cusp, as in the lane's
  canonical-cusp work, needs its own calculation.
- **(d)** covers conditions of relative/absolute type uniform on the torus. General couplings between sectors are not classified.
- **The Hořava–Witten reading** is a speculation, recorded for a sealed test, not a result.

## 5. Prior art (swept before banking)

Both branches and the audit lane were swept for "log-divergent", "infinite energy", "non-normalizable", "kinetic norm" and "flux
through".
- **The audit lane.**
  - R28 (main's B1413): source residues and through-flux parameters have divergent kinetic norm; they are non-normalizable
    four-dimensional moduli.
  - Its canonical-cusp report: an infinite Higgs norm and a non-normalizable q variation on the fixed hyperbolic base, and
    non-normalizable cusp periods.
  - These are the lane's versions, in its setting, of (a) and (c). This arc states them for the seat's frame and adds (d) and the
    menu.
- **This branch.**
  - B1392 (sealed and free cusps; the continuum);
  - B1393 (the flip lemma);
  - B1351 (ii) (the torus conventions).
- **The literature.** The Riemann–Roch index on T² is standard; Hořava–Witten (Nucl. Phys. B460 (1996) 506) for the wall reading.
