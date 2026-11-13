# B1912 — The golden state is the lowest twin-odd state on the level-5 curve, and it is simple (P-783; P-776's condition R3)

**Verdict: PROVED** (numerically, by a scan with two independent heights and a positive control; over the spectral range
0.02 ≤ R ≤ 3.40, which contains the state; the exceptional range λ < 1/4 is not scanned). cc (main), 2026-11-13 (S306p).
Main's own code; no seat's code run. No data; no value of the modulus on record is read, and no point is compared with
anything. **0 of 19.**

## 1. The answer first

- **The question (P-783):** Maass's construction gives the golden state (B1885) at the spectral parameter R₀ = π/(2 ln φ) =
  3.2642513026, not its rank. The twin-odd states are the Maass cusp forms on Γ₀(5) with the quadratic character
  χ(d) = (d/5), and they fall in four classes, by parity under the mirror z ↦ −z̄ (sine or cosine series) and sign under the
  Fricke involution W₅: z ↦ −1/(5z). The golden state is in the class (sine, −1). Is any twin-odd state lower, and is the
  golden state's eigenvalue simple?
- **The answer:** for 0.02 ≤ R ≤ 3.40, in all four classes, **the only eigenvalue is R₀, in the golden state's own class, and it
  is simple there and absent from the other three.** So the golden state is the lowest twin-odd state, and simple, over that
  range. For the read-out on the whole (P-776) this is condition R3, existence and uniqueness first, met within the range.
- **What is not covered:** R < 0.02 (λ between 1/4 and 0.2504), and exceptional eigenvalues λ < 1/4, which this code cannot
  see. Whether Selberg's bound is known for this group with this character is not checked here.

## 1a. Seen first

`VERDICT topic-sweep /P-783|lowest twin|golden state|Hejhal|Maass/: 19 of 1650 arcs on main match (NEGATIVE 4, OPEN 2,
PROVED 13); 5 register rows match (QUEUED 5)`. B1885 (the golden state verified on main, its rank not), P-783, P-776; the
record's earlier Maass forms are those of the figure-eight complement (B790 to B797, B922). The web seat's referee has a scan
in double precision that finds no state below it in part of the range (P-783's row); it was not read for this arc.
**Literature:** Hejhal's method for Maass cusp forms (Hejhal 1992; Strömberg's variants for groups with characters); Maass
1949 for the dihedral forms of a real quadratic field.

## 2. How it was done (`verification/`)

- **The ansatz:** f(z) = Σ_{n ≤ M} c(n) √y K_{iR}(2πny) cs(2πnx), cs = sin or cos. Points on a horocycle y = Y are pulled back to
  the fundamental domain of PSL₂(ℤ) and through the six cosets of Γ₀(5) (I and S T^k); the automorphy factor is χ(d) of the
  Γ₀(5) part; a point the coset sends toward the cusp 0 is brought back up by W₅ with the factor ε. The relation between f on
  the horocycle and f at the pulled-back points, transformed over the half period, is a linear system V(R) c = 0; an
  eigenvalue makes V(R) singular.
- **K_{iR}(x)** by its integral ∫₀^∞ e^{−x cosh t} cos(Rt) dt, against mpmath: 5.3 × 10⁻¹² relative.
- **An eigenvalue is a minimum of the least singular value that falls to rounding at two heights** (Y = 0.12 with M = 34, and
  Y = 0.10 with M = 40). A single height gives false minima where K_{iR}(2πnY) vanishes for some n: at Y = 0.12 the first scan
  found eight, one of them (R = 2.558385) in all four classes, the signature of such a zero: K_{iR}(2π · 0.12) = 1.4 × 10⁻⁸
  there. Each vanishes at the other height.
- **The control in the golden state's class:** at R₀ the least singular value is 2.4 × 10⁻¹² (one height) and 3.3 × 10⁻¹³,
  2.6 × 10⁻¹² (both), against ~10⁻⁴ at R₀ ± 0.01; the other three classes give 0.1 to 0.2 at R₀.
- **The control in a mirror-even class,** where the continuous spectrum lives: the dihedral form with no sign of the norm in
  its character, at 2R₀ = 6.5285026, is found in the class (cosine, +1) at both heights (2.4 × 10⁻¹⁴, 1.8 × 10⁻⁹). A cusp-form
  ansatz has no constant term, so the continuous spectrum gives no false minimum.
- **Simplicity:** the next singular value at R₀ is 1.1 × 10⁻² to 0.47, far from rounding.

| range | step | classes | eigenvalues found at both heights |
|---|---|---|---|
| 0.25 ≤ R < 3.40 (detected at Y = 0.12, then at Y = 0.10) | 0.004 | four | R₀ = 3.2642513026 in (sine, −1); none elsewhere |
| 0.02 ≤ R < 0.26 | 0.002 | four | none: the least value shared by both heights is 0.66 to 0.81 |
| 2R₀ ± 0.06 (the control) | 0.003 | four | 6.5285026 in (cosine, +1) |

## 3. What is not shown

- R < 0.02 and λ < 1/4 (exceptional eigenvalues).
- Two eigenvalues closer than the step would show as one minimum; the second singular value rules out a repeat at R₀ itself,
  not a pair closer than 0.002–0.004 elsewhere.
- That the twin-odd states are exactly the forms with the quadratic character is the identification B1885 and P-776 use
  (the character's sign is the exchange of the twins); it is taken from them, not re-derived here.

## Files

- `verification/hejhal_level5.py` (the method, the Bessel check and the control at R₀) → `hejhal_level5_run.txt`.
- `verification/scan.py`, `scan2.py`, `scan3.py` → `.json`, `_run.txt`.
- The lock: `verification/test_b1912_the_golden_state_is_lowest.py`.

## Reproduce

```
cd frontier/B1912_the_golden_state_is_the_lowest_twin_odd_state_and_simple/verification
python3 -B hejhal_level5.py; python3 -B scan2.py; python3 -B scan3.py     # minutes each; scan.py is the first pass
```

## Dated note, 2026-11-13 (B1923)

A second computation exists and agrees: the web seat's sealed scan on the golden state (harvest row 1713), its own code, expectations committed first: the state is the lowest in all four classes and simple, over its range. It was not read when this arc was written; it is the independent second computation the rule of 2026-11-13 asks of an absence.
