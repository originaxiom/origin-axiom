# B1738 — W139 ON MAIN (P-338): UNDER E₆'S CUBIC NO VEV OF THE FAMILIES' 27s SPLITS THE CHARGED LEPTONS FROM THE DOWN QUARKS — THEIR EXTENDED MASS MATRICES HAVE THE SAME SINGULAR VALUES, SO D ≡ 1 AND THE LEPTON FACTOR 3 CANNOT COME FROM THE 27s

**Verdict: PROVED** (computed on main's own code from the invariance and the charges alone; no data). cc (main),
2026-10-23. **0 of 19.**

## 0. Why

P-338 (relay 229): after E₆ breaks, d^c mixes with the 27's exotic D^c and L with the Higgs-like doublets; can that
split the charged leptons from the down quarks, and so supply the lepton factor that B1726's two ingredients put in by
hand (P-294)? The SM seat's W139 (rule 488495863, script 4116b434f before its one run, output 0b9b31bd5 unread,
recorded c6c057d13; relay 233; HARVEST_LEDGER row 1333) answers no: under E₆'s cubic the extended lepton matrix is the
extended down-quark matrix transposed and rotated, for every symmetric coupling and every colour- and charge-keeping
vev. This arc checks it on main without the seat's code.

## Seen first

`VERDICT topic-sweep /M_e ?= ?M_d|m_e ?= ?m_d|down.quark matrix transposed|trinification|E6'?s cubic|det Q \+ det L|Georgi.Jarlskog|lepton factor/ (full text): 75 of 1510 arcs on main match (NEGATIVE 17, OPEN 6, PROVED 52)`.

Bearing on it: B1726 and B1735 (the lepton factor by hand), B1729 (the leptons' coarser line gives no Georgi–Jarlskog
shift), B884 (E₆'s cubic and the Yukawa-support table), B1734 (D = 9 on order-5 lines). **Literature:** the
trinification form of E₆'s cubic and the relation m_e = m_dᵀ for 27-Higgs Yukawas are standard (e.g. the E₆ and
trinification reviews; from memory, not fetched).

## Disclosed

- W139's record was read before this arc; its script was not run or imported here.

## 1. The check (`verification/e6_down_equals_lepton.py`)

- **The cubic.** N = det Q + det L + det Q^c − tr(Q L Q^c) on Q ∈ (3_C, 3̄_L), L ∈ (3_L, 3̄_R), Q^c ∈ (3_R, 3̄_C):
  invariant under random SU(3)_C × SU(3)_L × SU(3)_R to 8 × 10⁻¹⁶ (relative).
- **The charges.** Q_em = T₃ + T₈/√3 on each SU(3) gives L **five neutral components**, and per colour **two charge
  +1/3 entries of Q against two charge −1/3 entries of Q^c** (d, D against d^c, D^c), and **two charge −1 against two
  charge +1 entries of L** (the charged leptons with the doublets' partners).
- **The mass matrices** are the Hessian of the polarised cubic with a symmetric family coupling λ_abc (complex,
  random) and complex vevs in the five neutral components of each family's L (random): 6 × 6 for the down type and for
  the leptons.
- **Result:** at eight random points, **the six singular values of the two matrices agree to 6 × 10⁻¹⁶ (relative).**
- **Control:** with det L's coefficient doubled (the symmetry broken) the leptons double and the singular values
  differ by a factor 2 (relative difference 1.0).

## 2. What it means

- **D ≡ 1 in the joint E₆ frame for every 27 vev:** the down-quark and charged-lepton spectra are identical, so the
  data's D = 10.58 ± 0.11 (P-094) is out of reach and **the lepton factor 3 cannot come from the 27s' cubic**. P-338 is
  answered: no.
- **P-294 sharpens:** the factor must come from outside the 27s (a representation that carries Georgi–Jarlskog's 45
  of SU(5) — E₆'s 351′ contains SO(10)'s 126, which contains it; from memory, not fetched — or from the frame itself, not
  its E₆ dress). B1729 closed the leptons' coarser
  line; this closes E₆ breaking by 27s.

## Files

- `verification/e6_down_equals_lepton.py` → `e6_down_equals_lepton.json`, `e6_down_equals_lepton_run.txt`.
- The lock: `tests/test_b1738_w139_on_main.py`.
