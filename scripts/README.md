# scripts/ — Session-3 synthesis verification scripts

These are the original verification scripts from the Session-3 synthesis
(2026-05-27). They are kept as the handoff artifacts; the *authoritative* locks
for the proven results are the tests in `../tests/`, and the frontier readings
live under `../frontier/`. This table maps each script to where its content is
governed.

| Script | What it computes | Governed by |
|---|---|---|
| `mobius_vector_field.py` | `v(τ)=−κ(τ²−τ−1)` and `V(τ)` from `log(A)`; fixed points. | **P15, P16** — `tests/test_mobius_vector_field.py`, `tests/test_derived_potential.py` |
| `six_faces.py` | `τ²−τ−1` in six contexts; each verified from its own setting. | CLAIMS.md note on P15/P16; audit in `PROGRESS_LOG.md` 2026-05-27 |
| `fisher_kpp.py` | Reaction–diffusion creation wave `τ=0→φ`. | **frontier B7** — `frontier/B7_fisher_kpp_creation/` |
| `mobius_lattice.py` | Coupled-lattice convergence to `φ` from noise. | **frontier B7** (supplement) |
| `particle_spectrum.py` | `mass²=κ√5`, coupling `κ`, and the **non-exact** `m/g≈φ` near-miss. | **frontier B8** — `frontier/B8_particle_spectrum/` |

The conceptual narrative is in `../docs/SESSION3_SYNTHESIS.md`. Run any script with
`python scripts/<name>.py` from the repo root.

> Note: `mobius_vector_field.py` uses `scipy.linalg.logm` (numerical) for `log(A)`;
> the proven-core tests use exact `sympy` algebra. Both agree (the numerical
> match to `~1e-15` is checked in the synthesis). One known cosmetic discrepancy:
> the synthesis's prose test-table line `V_at_phi = -1.515028` omits the `κ`
> factor; with `V(τ)=κ(τ³/3−τ²/2−τ)` the correct value is `-1.304163`, which the
> script prints and the P16 test asserts.
