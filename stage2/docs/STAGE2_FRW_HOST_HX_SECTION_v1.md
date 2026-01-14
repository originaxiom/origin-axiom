
---

## H5: External-cosmo host age–corridor kernel (summary)

Using the external-cosmo host background grid and the Stage2 joint θ-grid, we extracted the triple-overlap

\[
\text{HOST\_AGE\_ANCHOR} \wedge \text{FRW\_VIABLE} \wedge \text{TOY\_CORRIDOR},
\]

where:
- HOST\_AGE\_ANCHOR is defined by a host FRW age window of \([13.3, 14.3]\) Gyr,
- FRW\_VIABLE refers to the θ-grid points that pass the FRW viability cuts in the Phase 4 toy,
- TOY\_CORRIDOR is the original FRW corridor flag from the Phase 4 F1 probe.

The resulting kernel has the following properties (from
`stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`):

- Size: \(n = 12\) points out of 2048 (≈0.6% of the grid).
- θ-range: two disjoint arcs,
  - θ ≈ 0.64–0.66,
  - θ ≈ 3.30–3.32.
- Repo toy sector:
  - \(\omega_\Lambda^{\text{repo}} \in [0.6892, 0.7230]\),
  - toy FRW ages: \(\langle t_0^{\text{toy}} \rangle \approx 13.45~\text{Gyr}\) with σ ≈ 0.03 Gyr.
- External-cosmo host sector:
  - host FRW ages: \(\langle t_0^{\text{host}} \rangle \approx 13.55~\text{Gyr}\) with σ ≈ 0.14 Gyr,
  - all 12 points lie inside the observational age window by construction.
- Mechanism:
  - `mech_baseline_A0` (and its floor/binding variants) occupy a narrow band
    \(\sim 0.0461\)–\(0.0467\),
  - the corresponding `*_bound` flags are zero throughout the kernel.

This 12-point kernel is not yet a claim about the real Universe, but it is a compact region of the θ-grid where:

1. the Phase 4 FRW toy is FRW-viable and lies inside its corridor,
2. an external flat-ΛCDM background (with fixed \(H_0\)) assigns ages in the observational window,
3. the Stage 2 mechanism behaves in a controlled, non-pathological way.

As such, it provides a concrete, inspectable object for Phase 5 discussions (“first real contact” panels) and a useful stress test of the FRW + mechanism + external-cosmo host chain.

