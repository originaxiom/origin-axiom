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
- **SCAN — MB6: "reproduction is not interpretation" — run the control, not just the reproduce-check** (B133, the
  `K-H` field-fusion artifact, a correction to merged B132/K015). A cross-session handoff (or your own prior result) can
  verify at the **computation** level — the numbers reproduce exactly — yet be wrong at the **interpretation** level:
  the causal/structural claim attached to the numbers. The "chirality shifts the eigenvalue arithmetic" claim survived
  **three** times because it is numerically real and interpretively false (it passes every "does it reproduce" test).
  **The guard:** for any claim of the form "property X causes effect Y," run the **CONTROL that varies X while holding
  the confounds fixed** (here: achiral-vs-chiral words at fixed quantum-group inputs / fixed R,L multiset — which showed
  achiral words alone span all three fields, so the field tracks word-composition, not chirality). Banking on
  reproduction alone, without the control, is the lazy-revival failure mode at one remove.
- **SCAN — MB7: filter the REDUCIBLE locus before counting character-variety "escapes"** (B137, the m=2 sealing
  false-alarm). In an off-sublocus character-variety search testing whether traces stay in a field `K` (e.g. the S031
  sealing), the **reducible** locus (algebra generated by A,B has dim < n²) carries degenerate fixed points whose
  commutator trace `κ` is **not** constrained to `K` — they fake "escapes" (well-converged, residual ~1e-15, but
  `trA` a root of unity, `|eig|=1`). They nearly read as "the sealing is false." **Guard:** count an escape only among
  **genuine irreducible** points (algebra = `M_n`, dim n²); classify by algebra rank first. (B129's m=1 search missed
  this only because its reducibles happened to be rational ∈ ℚ(√−3); m=2's reducibles have messy non-ℚ(i) `κ`.) Sibling
  of MB2 / K-G / K-H — a surprising "escape" that is a degenerate artifact.
- **SCAN — MB8: a generic / necessary feature is not a discriminating / sufficient one — check the null case**
  (CHAT-1 LEADS REGISTER §E). When a feature is observed on the object of interest and read as *evidence for* a
  property, ask whether the feature is **generic** — present on the null/control object too. A *necessary*
  condition that everything satisfies discriminates nothing; only a feature that **separates** the positive case
  from the null case is evidence. (This is the structural sibling of MB6 "reproduction≠interpretation" — there the
  miss is the missing *control*; here the miss is the missing *null case*. Both are "right object, wrong level":
  run the case where the property is **absent** and confirm the feature disappears.) *(Numbering note: the CHAT-1
  doc labelled this "MB7"; that collides with the repo's MB7 above, so it is banked here as **MB8**. A further
  level-confusion guard — "a non-abelian symmetry **group** is not non-abelian **gauge** content" — is queued in a
  later handoff and will be **MB9**.)*
- **SCAN — MB10: structure-group invariants are not gauge-group rank (the dimensional form of MB9)** (B142, the
  "Borromean/SU(3)" over-reach). The **dimension** of an **SL(2,ℂ)** character variety does **not** establish **SU(N)**
  gauge content; matching "char-variety dim = rank(SU(N))" conflates the structure group with a would-be gauge group.
  SU(N) gauge content in the 3d-3d correspondence comes from **SL(N,ℂ)** Chern–Simons (`T_N[M]`), not a numerical
  dim/rank coincidence on the SL(2,ℂ) side. **Guard:** before reading any "dim k = rank G" as gauge enhancement, (a)
  recall Thurston — a k-cusped hyperbolic 3-manifold's SL(2,ℂ) character variety has complex dim **= #cusps** at the
  geometric rep (so the number is the cusp count, generic — run the **null control** across manifolds of differing
  symmetry, `MB8`); (b) check the **level** — SU(N) needs the SL(N,ℂ) variety (dim ≈ (N−1)·#cusps), not SL(2,ℂ); (c)
  a cusp-symmetry restated as `κ_i=κ_j` equalities is **automatic**, not independent evidence. Extends `MB9`
  (group ≠ gauge) from groups to invariants. Cluster: `MB6`/`MB8`/`MB9`/`MB10` = "right object, wrong level."
- **SCAN — MB11: state every result twice — bare math theorem + labeled (POSTULATED) physics reading — and never let
  the second contaminate the first** (B143, the strategic synthesis; the constructive form of `MB6` and of the
  firewall). The recurring drift is not in the *computations* but in the *prose*: a math fact (a character-variety
  dimension, a cusp count, a discrete intersection) gets written with a physics name (a gauge rank, a coupling, a
  "vacuum selection") and the borrowed reading silently becomes load-bearing. It crept into the project's own best
  strategic reflection, which is the tell that it needs an explicit rule. **Guard:** for any result, write (a) the bare
  mathematical statement, then (b) — separately and explicitly tagged POSTULATED — any physics reading, which cites (a)
  one-way and is never cited back. The 3d-3d / `T[M]` cusp↔gauge dictionary is *borrowed* (`../knowledge/K006`), so all
  cusp/gauge language is layer (b). Sibling of `MB10` (structure ≠ gauge) and the whole tombstone wall: "right object,
  wrong level," here as "right fact, wrong tier."
- **SCAN — MB9: a non-abelian symmetry GROUP is not non-abelian GAUGE content** (B139, the "SM through
  multiplicity" cartography). Before reading "the construction generates a non-abelian / free group" as "non-abelian
  physics / the firewall cracked," **check the level**: the firewall is stated on the **trace-ring / `T[M]` /
  fixed-locus** (abelian × discrete), **not** on the monodromy *group* (which is non-abelian for any hyperbolic
  object — every knot group is). Generating a free subgroup of SL(2,ℤ) (e.g. two seeds → 161 elements by length 4)
  is **generic and firewall-neutral**. The guard cluster: **MB6** reproduction≠interpretation (missing control) ·
  **MB8** generic≠discriminating (missing null case) · **MB9** group-level≠gauge-level — the "right object, wrong
  level" family, each defeated by naming the level the claim lives on. *(The B139 handoff labelled this "MB8"; that
  number was taken by the CHAT-1 §E guard, so it is banked here as **MB9**.)*
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
