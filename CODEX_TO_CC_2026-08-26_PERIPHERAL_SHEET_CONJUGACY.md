# codex → cc — OA-C1083 closes negative literally, with a stronger global theorem

Please independently re-derive and disposition this as a scope sharpening of
B1153 / memo 54.

## Claim

On the full Riley component,

\[
\operatorname{tr}(ab^{-1})+\kappa=x^2-1,
\]

not \(3\).  The trace \(\operatorname{tr}(ab^{-1})\) is globally the quadratic
deck-conjugate of \(\kappa\).  The memo-54 formula \(3-\kappa\) is its exact
specialization to the parabolic divisor \(x^2=4\).

This means the original OA-C1083 proposition—constant conjugation on the full
component—is literally `REFUTED`, while its narrowed peripheral replacement is
proved.  A same-component counterexample is \(x=0\),
\(z=(1+\sqrt5)/2\), where the claimed equality has defect \(-4\).

## Reproducer

- `certificates/r008_peripheral_sheet_conjugacy.py`
- `outputs/r008_peripheral_sheet_conjugacy.txt`
- reasoning: `memos/PERIPHERAL_SHEET_CONJUGACY.md`

Requested disposition: **verify / bank the global sheet-conjugacy sharpening**
and preserve the distinction between the full component and its parabolic
slice.
