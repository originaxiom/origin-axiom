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
```

Probe outputs are observations with bounded verdicts. A passing frontier probe
does not promote a claim unless the governance gate is explicitly run and logged.
