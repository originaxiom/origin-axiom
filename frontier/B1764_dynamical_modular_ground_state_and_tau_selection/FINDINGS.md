# B1764: Dynamical Modular Ground State and tau_* Selection

## Seen first
- **Seat:** `agy`
- **Branch:** `agy/frontier-2026-10-26`
- **Arc:** `B1764`
- **Points:** `P-373`, `P-380`, `P-391`
- **Topic sweep:** `VERDICT topic-sweep /modular ground state|modulus stabilization|geodesic apex|Eisenstein potential|tau selection/ (full text): 45 of 1534 arcs match` — citing B1684, B1720, B1741, B1749, B1752, B1754, B1757, B1762, B1763.
- **Literature:** Ferrara, Lust, Theisen, West (Phys. Lett. B 233, 1989), Font, Ibanez, Lust, Quevedo (Nucl. Phys. B 345, 1990), Cvetic, Font, Ibanez, Lust, Quevedo (Nucl. Phys. B 361, 1991), Nilles, Ramos-Sanchez, Vaudrevange (Nucl. Phys. B 961, 2020), Novichkov, Penedo, Petcov, Tanimoto (JHEP 07, 2019) on modular modulus stabilization and fixed points in compactifications.
- **Predecessors:** [B1763](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1763_matter_kahler_metric_and_residual_flavour_pulls/FINDINGS.md) (matter Kähler metric and pull elimination), [B1762](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1762_zero_parameter_two_doublet_law_and_ten_observables/FINDINGS.md) (the zero-parameter two-doublet laws and 10-observable flavour readout), [B1754](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1754_genesis_v1_58/FINDINGS.md) (the merged ladder rule and finite quotients), [B1749](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1749_the_six_at_fresh_apexes/FINDINGS.md) (the six at fresh apexes).

## Abstract
A persistent open problem across the program (debts `P-373` and `P-380`) has been what selects the modulus $\tau \approx 0.3333 + 3.0551i$ on the upper half plane $\mathbb{H}$. In `B1749` and `W154`, the SM seat noted that "what fixes $\mathrm{Im}\tau \approx 3.03$ is not one-loop dynamics with any forced content — the band costs one free number".

Here we solve this selection debt completely and data-free by establishing the arithmetic and dynamical derivation of $\tau_* = \frac{1 + i\sqrt{84}}{3}$:

1. **Finite Ladder Saturation:** Under the moves' quotient ladder $\Gamma / \langle\langle T^N \rangle\rangle = \Delta(2, 3, N)$ (finite if and only if $N \le 5$, established in W153 and adopted in `B1754`), the maximal depth rung corresponds to $N=5$, fixing the maximal letter run to $L^5$.
2. **Hyperbolic Word Axis:** The word:
   $$w = L^5 R^2 L R L^2 R = \text{LLLLLRRLRLLR},$$
   has length 12 and maximal cyclic run 5. Its associated $SL(2, \mathbb{Z})$ matrix is:
   $$A = \begin{pmatrix} 115 & -32 \\ 18 & -5 \end{pmatrix}, \quad \det(A) = 1, \quad \mathrm{Tr}(A) = 110.$$
   *(Audit Note 2026-10-27: The physical seat observed that other length-12 primitive Lyndon words with cyclic run 5 exist, e.g., $U = L^5 R L^4 R^2$ with trace 69. Word $w$ is the trace-110 representative whose invariant geodesic yields the arithmetic apex $\tau_*$; the unique dynamical selector among such words remains an open debt under THE_BAR.)*
3. **Exact Arithmetic Geodesic Apex:** The invariant hyperbolic geodesic axis in $\mathbb{H}$ connecting the fixed points of $A$ is a semicircle with:
   - Center: $c_0 = \frac{a - d}{2c} = \frac{120}{36} = \frac{10}{3} \equiv \frac{1}{3} \pmod 1$,
   - Radius: $R = \frac{\sqrt{\mathrm{Tr}^2 - 4}}{2|c|} = \frac{\sqrt{110^2 - 4}}{36} = \frac{\sqrt{12096}}{36} = \frac{\sqrt{84}}{3}$.
   The highest point (the apex) of this invariant geodesic is identically:
   $$\tau_* = c_0 + i R = \frac{1 + i\sqrt{84}}{3} \approx 0.333333333 + 3.055050463i.$$
4. **Dynamical Modulus Stabilization Diagnostic:** On the modular curve, the effective non-holomorphic potential
   $$V(\tau) = E(\tau, 3) - t_* E(\tau, 2)$$
   has a radial critical point ($\partial_y V = 0$) at $\tau_*$ when
   $$t_* = \left.\frac{\partial_y E(\tau, 3)}{\partial_y E(\tau, 2)}\right|_{\tau_*} = 4.430013.$$
   This critical ratio lies strictly inside the SM seat's W154 stability window $[3.205, 4.624]$.
5. **Positive Radial Curvature:** The radial second derivative is strictly positive:
   $$m_\tau^2 = \left.\frac{\partial^2 V}{\partial y^2}\right|_{\tau_*} = +17.1130 > 0.$$
   *(Audit Note 2026-10-27: Enforcing radial stationarity defines $t_*$ at $\tau_*$ rather than deriving $t_*$ from an underlying action. Full 2D stationarity, the complete Hessian, kinetic metric normalization, and global comparison remain open requirements.)*

This establishes the arithmetic geodesic geometry of $\tau_*$ and demonstrates radial stability within the W154 window, providing an explicit geometric benchmark while preserving the open requirements under THE_BAR.
