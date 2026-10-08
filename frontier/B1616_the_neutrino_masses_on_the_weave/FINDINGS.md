# B1616 — THE NEUTRINO MASSES ON THE WEAVE: TM1's own neutrino-side symmetry admits no Majorana vacuum, and every other residual-aligned Majorana vacuum gives a rigid, degenerate spectrum the two measured splittings exclude — the weave's group fixes no neutrino mass

**Verdict: NEGATIVE as sealed** (N1 holds; N2 fails; N3 holds only on rigid degenerate points; N4's numbers are artifacts;
D1 void). cc (main), 2026-10-08. Sealed `08b7f328f` before the run and before any cosmological datum was read. Results
carry "given Λ" (the owner's FK11 ruling as relayed). Outside the nineteen. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /neutrino mass|Majorana|sum rule|Sigma m|cosmolog|DESI|Takagi|seesaw/: 91 of 1387 arcs on main match (NEGATIVE 12, OPEN 13, PROVED 66)`
— B1615, B1612–B1613, B1611, the falsifier register's P4 and P5; the SM seat's lane at `0471ce849` (W36, W37, the owner's
rulings as relayed). **Literature:** Takagi factorisation; neutrino mass sum rules in flavour models (cited).

## 1. The computation (`neutrino_masses_on_the_weave.py`; `neutrino_masses_on_the_weave.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **N1** | Sym² T = 1 + 2 + 3; Λ² T irreducible | 70% | **HOLDS** |
| **N2** | along RRL some irreducible of Sym² T has a fixed space | 80% | **FAILS** — along RRL, TM1's neutrino-side symmetry, no irreducible of Sym² T has a fixed vacuum |
| **N3** | some residual-aligned family obeys an exact sum rule | 50% | **HOLDS only on rigid points**: the singlet along RL gives (1, 1, 1); the triplet along RL gives (½, ½, 1) and along L or R (0, 1, 1); each satisfies m₁ + m₂ = m₃ or 2m₂ = m₁ + m₃ trivially, through an exact degeneracy; the doublet has no fixed vacuum along any of the four |
| **N4** | if m₁ + m₂ = m₃: Σm ≈ 0.115 eV at NO | 80% (cond.) | **The printed numbers (0.1149 eV NO, 0.0997 eV IO) are artifacts**: the solver imposed the sum rule alone and ignored the rigid ratios, which already fix (½, ½, 1) or (0, 1, 1) — spectra with m₁ = m₂ or m₂ = m₃, incompatible with Δm²₂₁ ≠ 0 and |Δm²₃₁| ≠ Δm²₂₁. Not predictions |
| **D1** | any predicted Σm above DESI DR2's 95% bound | 70% (cond.) | **VOID** — no residual-aligned spectrum survives the oscillation splittings, so there is no Σm to compare; no cosmological datum was read |

## 2. What it says

The weave's residual-vacuum reading of the neutrino masses fails on oscillation data alone: TM1's own neutrino-side
symmetry admits no Majorana vacuum, and every other residual vacuum gives exact degeneracies the two measured splittings
rule out. So the TM1 reading (P10) can live for the mixing, but not with residual-aligned neutrino masses. With B1611
(the phase), B1612 (the angles) and B1615 (the charged-fermion masses), the weave's group fixes no value in the flavour
sector, quark, lepton or neutrino. Values need a forced modulus, dynamics, or end data (the seat's W36: a chiral count
needs end data or an object of dimension four or more).

## 3. Disclosed

- N4's solver was written to impose a sum rule and did not impose the rigid ratios; its outputs are recorded and are not
  predictions (the instrument is sealed and unchanged).
- The instrument's inverted-ordering formula was repaired before the seal (disclosed there).

## 4. Files

`verification/neutrino_masses_on_the_weave.py` (sealed, unchanged), `neutrino_masses_on_the_weave.json`,
`neutrino_run.txt`; `adoption/amend.py` (GENESIS v1.33: the owner's rulings as relayed; this arc),
`received/GENESIS_v1_32_main.md`. Test: `tests/test_b1616_the_neutrino_masses_on_the_weave.py`. Kill-graph entry B1616.
