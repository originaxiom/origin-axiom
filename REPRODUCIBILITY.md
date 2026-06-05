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
