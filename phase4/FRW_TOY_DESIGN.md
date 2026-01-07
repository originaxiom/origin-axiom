# Phase 4 FRW-like toy diagnostics (design note)

Status: **DRAFT / non-binding**

This note sketches a minimal, FRW-inspired *toy* diagnostic that can be
driven by the Phase 4 scalar
\(E_{\mathrm{vac}}(\theta) = \alpha \, A(\theta)^{\beta}\) produced by
the F1 mapping family. It is **not** a cosmological model, does not
attempt to fit parameters, and does not make any physical claims about
the real universe.

The design goal is narrower:

> Given a scalar \(E_{\mathrm{vac}}(\theta)\) that is strictly positive
> and reasonably smooth, define simple, auditable diagnostics that
> check whether it can be embedded in an FRW-like module without
> producing obviously pathological behaviour.

## 1. Inputs and assumptions

We assume as inputs:

- A fixed Phase 3 vacuum configuration (e.g. `baseline_v1`);
- The corresponding F1 scalar
  \(E_{\mathrm{vac}}(\theta) = \alpha \, A(\theta)^{\beta}\)
  evaluated on a uniform grid of \(\theta \in [0, 2\pi)\);
- A toy corridor mask, such as the one defined in
  `phase4/src/phase4/run_f1_shape_diagnostics.py`, which marks
  "low-energy" regions where
  \[
    E_{\mathrm{vac}}(\theta) \leq E_{\mathrm{vac},\min} +
    k_\sigma \sigma, \quad k_\sigma = 1.
  \]

No physical units are assigned to \(E_{\mathrm{vac}}\); it is treated as
a dimensionless, positive scalar that can be rescaled.

## 2. Toy FRW-like module (design only)

We consider a one-dimensional, dimensionless toy module:

- A scale factor \(a(\tau)\) evolving in a dimensionless "time"
  \(\tau\);
- A toy Hubble-like quantity \(H(\tau)\) related to
  \(E_{\mathrm{vac}}(\theta)\).

The minimal structure we intend to test is:

1. A monotonic scale factor:
   \[
     \frac{da}{d\tau} = H(\tau), \quad a(\tau) > 0, \ H(\tau) \ge 0.
   \]

2. A simple mapping from \(E_{\mathrm{vac}}(\theta)\) to \(H(\tau)\),
   for example
   \[
     H(\tau)^2 = C \, E_{\mathrm{vac}}(\theta(\tau)),
   \]
   where \(C > 0\) is a dimensionless scaling parameter and
   \(\theta(\tau)\) is a prescribed trajectory through the
   \(\theta\)-space (e.g. uniform sweep).

At this design stage we do **not** fix \(C\) or the detailed
\(\theta(\tau)\), but we require:

- \(H^2 \ge 0\) for all sampled points;
- no blow-ups or discontinuities in \(H(\tau)\) over the sampled
  interval;
- the ability to integrate \(a(\tau)\) numerically with stable
  behaviour for reasonable step sizes.

## 3. Planned diagnostics

Once implemented, the toy FRW module should report:

1. **Range checks**:
   - \(\min H\), \(\max H\), and whether the ratio
     \(\max H / \min H\) stays within a configurable bound.

2. **Smoothness checks**:
   - discrete derivatives of \(H(\tau)\) and a measure of whether they
     exhibit spikes or sharp discontinuities;
   - optional second-derivative diagnostics.

3. **Corridor compatibility**:
   - behaviour of \(H(\tau)\) restricted to the toy
     \(\theta\)-corridor defined by the F1 shape mask;
   - whether the corridor region yields a "tamer" or more regular
     evolution of \(H(\tau)\) and \(a(\tau)\) than the complement.

These diagnostics are intended to be summarised in a small JSON file
and optionally visualised in figures. They remain *non-binding* unless
and until a later rung promotes a particular corridor and mapping to a
candidate Phase 4 \(\theta\)-filter.

## 4. Non-claims

This FRW-like toy module will **not** claim:

- a realistic FRW or \(\Lambda\)CDM model;
- any fit to observed cosmological data;
- a unique or physically preferred mapping from the Phase 3 mechanism
  to cosmology.

Its sole purpose is to test whether the Phase 3 global-amplitude
mechanism, as wired through the F1 mapping, admits even a toy-level
FRW-style embedding that is numerically sane and structurally
non-pathological.

If all reasonable choices of scaling and trajectories yield clearly
pathological behaviour, Phase 4 will treat this as a *negative*
diagnostic, to be reported alongside other corridor results.

## Baseline Rung-7 outcome (toy, non-binding)

Using the F1 sanity curve and the default toy parameters
(\Omega_m = 0.3, \Omega_r = 0, \langle \Omega_\Lambda \rangle \approx 0.7)
together with a bounded-variation criterion on H^2(a; \theta), the
script `phase4/src/phase4/run_f1_frw_toy_diagnostics.py` produced:

- a diagnostics file
  `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json`, and
- a per-theta mask
  `phase4/outputs/tables/phase4_F1_frw_toy_mask.csv`.

In this baseline configuration the FRW-sanity fraction is effectively
zero (`frac_sane ≈ 0`), i.e. the mask is empty. This is interpreted
as a **local, toy-level negative result** for this particular choice
of normalisation and sanity criterion, not as a failure of Phase 4 as
a whole. It is not used as a θ-filter and remains strictly
non-binding, serving only to demonstrate how empty-corridor outcomes
are recorded and inspected.

## Late-time FRW toy tweak (Rung 9, non-binding)

Following the initial Rung-7 configuration, which used a scale-factor
grid a ∈ [0.1, 1] and produced an effectively empty FRW-sanity mask,
we switched to a *late-time* window a ∈ [0.5, 1] while keeping the
same basic sanity criterion (positivity of H^2 and a bound on
max(H^2)/min(H^2) per θ).

The script `phase4/src/phase4/run_f1_frw_toy_diagnostics.py` now:

- uses this late-time window for its toy FRW check;
- records the resulting sanity fraction `frac_sane` in
  `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json`; and
- writes a per-theta FRW-sanity mask to
  `phase4/outputs/tables/phase4_F1_frw_toy_mask.csv`.

This remains a toy diagnostic only. Whether `frac_sane` is close to 0
or appreciably non-zero, the outcome is logged as a structured
positive/negative result, not elevated to a Phase 4 θ-filter.
