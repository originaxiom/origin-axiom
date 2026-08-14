# B798 — THE ALGEBRAICITY FALSIFIER'S POWER BOX (R32-4/R32-5), computed and sealed

Discharges Review 32 action items **R32-4** (seal the (d, H) box) and **R32-5** (correct the cost).
Prompted by Chat-1's review. Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## Why this exists

The B796 campaign falsifier reads: *"if the deep-precision algebraicity test (50+ digits) returns
negative **with adequate power**, the BC/CM route cannot be completed."* **"Adequate power" was
unspecified.** An unspecified power criterion is repairable after the fact by pleading higher
degree — and a falsifier that can be repaired after the fact is not a falsifier (**E32**).

## The power box (computed)

PSLQ at N digits excludes degree-d integer relations of height ≤ H only when
**N ≳ 1.43 · d · log₁₀H** (calibrated off Booker–Strömbergsson–Venkatesh, who used d ≤ 10,
H ≤ 10⁷ at ~100 digits).

| digits N | d=2 | d=4 | d=8 | d=10 |
|---|---|---|---|---|
| **8** (the certified run) | H ≤ 10^2.8 | 10^1.4 | 10^0.7 | 10^0.6 |
| 20 | 10^7.0 | 10^3.5 | 10^1.7 | 10^1.4 |
| **50** | 10^17.5 | 10^8.7 | 10^4.4 | **10^3.5** |
| **100** | 10^35.0 | 10^17.5 | 10^8.7 | **10^7.0** |

**Two consequences, and the second was not anticipated:**

1. **At 8 digits there is no power at all** — d=2 reaches only H ≤ 10^2.8. cc3 was right to refuse
   a verdict in either direction, and B797's "open and untested in both directions" is exact.
2. **"50+ digits" is under-specified.** At 50 digits the d ≤ 10 exclusion reaches only
   **H ≤ 10^3.5**. **BSV parity (d ≤ 10, H ≤ 10⁷) requires N ≥ 1.43·10·7 = 100 digits.** The
   falsifier as written would fire on a much weaker exclusion than the literature standard it is
   implicitly measured against.

## Sealed criterion (proposed for the Cell 9 prereg)

> **The (d, H) box is declared BEFORE the run and is not amendable after it.** Cell 9 targets
> **d ≤ 10, H ≤ 10⁷**, requiring **N ≥ 100 certified digits**. A negative excludes *exactly that
> box* and is reported as such — never as "not algebraic". If the achieved precision is N < 100,
> the verdict states the box actually excluded (from the table above) and the falsifier **does not
> fire**; it is not repaired by widening d after seeing the result.

## The cost (R32-5) — the report's "cheap" was wrong-adjacent

cc's session report called the §16 factual review cheap; the sentence sat next to the computation
and read as if the computation were cheap too. It is not.

| target | modes | dense solve | ×10 overhead | ×100 overhead |
|---|---|---|---|---|
| 50 digits | 900 → 5 625 | 244× | 10^3.4 | 10^4.4 |
| **100 digits** | 900 → 11 250 | **1 953×** | **10^4.3** | **10^5.3** |

Modes scale ~linearly with precision; the dense solve is cubic; arbitrary-precision arithmetic
adds 10–100×. So the run that would actually discharge the falsifier at BSV parity is **4–5 orders
of magnitude** beyond the certified run, **on a different numerical stack** (arb/mpmath Bessel, mp
linear algebra) from the one that produced the 17 eigenvalues. **It is a new instrument, not a
refinement of the existing one** — and the existing one's validation (two heights, mode-count
certification) does not transfer to it.

*(Chat-1 estimated 10⁴–10⁵× for the 50-digit target; cc computes 10^3.4–10^4.4 there and
10^4.3–10^5.3 at 100. The estimates agree to within the overhead assumption, and the operative
point is identical.)*

## Consequence for sequencing

Cell 9 is not a cheap keystone. Before it is scheduled:
- seal the (d, H) box as above;
- state that the 100-digit stack requires **its own** two-height + mode-count certification, since
  the 8-digit instrument's validation does not carry over;
- run the **§16 factual review** on the sealed design (that part *is* cheap — GOVERNANCE §16
  permits a spawned subagent given the design verbatim).

— cc, 2026-07-29
