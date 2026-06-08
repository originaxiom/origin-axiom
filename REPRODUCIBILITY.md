# Reproducibility

Every `proven` claim in `CLAIMS.md` must be reproducible from this repository by a third
party. This file is the entry point. Governed by `GOVERNANCE.md` §9.

---

## Environment

- **Python** ≥ 3.11
- **Core dependencies:** `numpy`, `scipy`, `sympy`, `matplotlib` (see `requirements.txt`).
- **Topology dependency:** `snappy` (SnapPy) — required for the figure-eight / sister
  manifold data (claims P9, P10). Heavier to install; the verified constants are also
  hard-coded and tested, so the algebra/statistics tests run without SnapPy.

Setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# optional, for topology tests:
pip install snappy
```

*(`requirements.txt` and the `src/` package are created in Phase A — see `ROADMAP.md`.)*

### Tooling availability (recorded for the arithmetic / low-dim-topology probes)

- **SnapPy + cypari are installable and usable in-sandbox** (`pip install snappy --break-system-packages` brings
  SnapPy 3.3.2 + cypari 2.5.6). This **lifts the gate** on items previously parked as "SnapPy/MAGMA-gated" — most
  were only *SnapPy*-gated. Used by **B125** (the metallic invariant-trace-field / arithmeticity computation).
- **MAGMA is NOT installable** (closed, license-gated). Genuinely MAGMA-only work (heavy Galois / class-field
  computation) stays parked — parked for *no tool*, not handed to anyone as a "prove it."
- **SnapPy 3.3.2 gotchas** (documented so they are not re-derived): the high-level `invariant_trace_field()` /
  `.find_field()` are **Sage-gated** (use shapes + `cypari.algdep` instead — the shape field *is* the invariant
  trace field, Neumann–Reid); `polished_holonomy(bits_prec=…)` is **broken** (use
  `ManifoldHP(...).fundamental_group().SL2C(word)` for high precision); `algdep` works in **method form** and the
  degree search must **start at 2** (`algdep(x,1)` on a non-rational raises a domain error); build pari complex
  numbers from `str(z.real())/str(z.imag())` to preserve precision; the `SL₂` *generator*-trace field can be **2×**
  the shape field (lift-dependent sign) — use traces of **squares** for the commensurability invariant.
- **SCAN — chirality / amphichirality MUST use `symmetry_group().is_amphicheiral()`** (B128). Naive
  `M.is_isometric_to(M_mirror)` is **orientation-blind** and gives **false positives** — it returns `True` for the
  known-chiral census knots m015/m016/m009 (it admits the orientation-**reversing** mirror isometry). Raw Chern–Simons
  **sign** is also unsafe (CS carries a period/modulus; an achiral manifold can read CS = π²/2 as for m003, and a
  *small* CS can still be genuinely chiral). The correct test is `M.symmetry_group().is_amphicheiral()`, **gated on**
  `M.symmetry_group().is_full_group() == True`. Validated controls: m004/m003 amphichiral; m015/m016/m009 chiral.
  (Build punctured-torus bundles from `R/L` words as `snappy.Manifold("b++" + word)`.)
- **SCAN — "is this number in ℚ(√−3)?" needs a small-height detector** (B129, bug B1). Test rationality of `Re(z)`
  **and** of `Im(z)/√3` directly, and accept **pure rationals** (`1 = 1 + 0·√−3` *is* in ℚ(√−3) — a naive
  `a + b√−3` grid rejects them and fakes "escapes"). Use a **small** `Fraction.limit_denominator` bound (≈100, the
  genuine traces have small height): `limit_denominator(10000)` is too permissive — by Dirichlet it approximates almost
  any real to <1e-8, so it would accept genuine escapes (√2, π) too. Tuned: `maxden=100`, `tol≈1e-6`.
- **SCAN — fixed points of a hyperbolic trace map are SADDLES; root-find, don't iterate** (B129, bug B2). Forward
  iteration *flees* saddles (the KKT/metallic trace map is a horseshoe, `knowledge/K010`). A solver stopping at
  residual ~1e-7 lands on **degenerate** trivial/central fixed points with slightly-off traces (`0.99998` vs `1`) that
  fake an "escape" at the residual floor. The figure-eight rep is **unipotent** (`|eig|=1`), so eigenvalue-modulus does
  **not** separate genuine content from trivial reps. Robust escape test: **polished distance** — re-solve from the
  candidate (`ftol≈1e-15`), then measure deviation from ℚ(√−3) with a threshold (≈1e-4) set ~100× above the artifact
  band (observed max 1.2e-6 over 427 points) and ~10× below any real escape. The escape count is then stable (no
  0-vs-1 flicker). *(Both B1 and B2 produced false firewall "reopenings" / a near-false-refutation before being caught.)*
- **SCAN — "discrete vs continuous fixed-locus value?" use the elimination ideal, not `sp.solve` branch-counting**
  (B130, the `K-G` revival false-positive). To decide whether an invariant `f` takes finitely many values on a fixed
  locus (a genuine discrete choice) or varies continuously, **adjoin `k=f` and eliminate the coordinates** (lex Gröbner):
  an **empty** `k`-only elimination ideal ⟹ `f` is unconstrained ⟹ continuous ⟹ no choice. `sp.solve` on the fixed
  equations **mislabels degeneracies of a continuous curve as isolated 0-dimensional points** (tell: a returned "point"
  still carries a free symbol, e.g. `κ = z²−2`). Confirm 0-dimensionality by **Jacobian rank** (rank = #coords), not by
  `solve`'s branch split. *(This is the revival failure mode — a too-eager "yes" — sibling of bug B2's kill mode.)*
- Tests that need SnapPy **skip** (via `pytest.importorskip`) when it is absent, so the suite stays green without it;
  the verified constants are also recorded in-probe and tested unconditionally.

---

## Running the tests

From the repository root:

```bash
python -m pytest tests/ -v
```

Every test corresponds to a numbered claim in `CLAIMS.md`. A failing test means a `proven`
claim has regressed — that is a stop-the-line event, not a number to update.

---

## Freeze tags

Stable states of the repository are git-tagged so any past result can be checked out
exactly:

| Tag | Meaning |
|---|---|
| `phaseA-foundation-freeze` | Phase A complete: all P-claims locked behind passing tests (Phase 0 governance and the legacy consolidation are included in the same milestone). |
| `session3-synthesis-freeze` | Session-3 synthesis freeze: P15/P16 and the conditional uniqueness theorem are locked and public. |
| `atlas-paper-integration-v1` | First atlas/paper integration checkpoint after consolidation of reviewer and paper-candidate navigation. |
| `trace-map-spectrum-checkpoint-v1` | Trace-map/spectrum checkpoint: B13-B25 plus public documentation harmonization; no new claim promotion. |
| `trace-selector-c5-freeze` | Trace selector C5 freeze: B13-B47, C5/T1 conditional theorem, and PC02/PC11 external-review packets. |

To reproduce a result as of a freeze:

```bash
git checkout <tag>
python -m pytest tests/ -v
```

---

## Determinism

All computations in the `proven` core are exact (integer/symbolic) or deterministic
floating-point with fixed inputs. No result in the proven core depends on a random seed.
Any stochastic exploration belongs in `frontier/` and must pin and record its seed.

## Frontier probes

Frontier probes are not part of the proven core, but many are executable:

```bash
python frontier/B25_fibonacci_spectrum_anchor/probe.py
python frontier/B26_lambda1_derivation_attempt/probe.py
python frontier/B38_tangent_return_arithmetic_filter/probe.py
python frontier/B40_filter_reuse_audit/probe.py
python frontier/B47_s1_verdict_ledger/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B49_sl3_certificate_proof_hardening/probe.py
python frontier/B51_sl3_symbolic_m_factorization/probe.py
python frontier/B52_multichannel_fibonacci_bridge_control/probe.py
```

Probe outputs are observations with bounded verdicts. A passing frontier probe
does not promote a claim unless the governance gate is explicitly run and logged.

## Portability

No test or probe may hardcode an absolute machine path (e.g. `/Users/...`, `/home/...`); sibling imports
resolve via `Path(__file__)`-relative paths — for a `frontier/<name>/probe.py`, the `frontier/` directory
is `pathlib.Path(__file__).resolve().parents[1]`, and a sibling module is loaded from
`parents[1] / "<sibling>" / "probe.py"` (use `importlib.util.spec_from_file_location` when the module name
`probe` would collide). This is locked by `tests/test_no_hardcoded_paths.py` (it scans active `*.py` for
absolute-path prefixes; `legacy/` and vendored virtualenvs are excluded).
