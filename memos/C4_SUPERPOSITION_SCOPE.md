# C4 superposition: the finite-data result is positive; the exactness headline is not

## Reproduced result

The B1153/Memo-55 data and formulas reproduce without NumPy or SciPy:

- each factor versus the single Wigner surmise: \(D=0.0401,0.0487\);
- the merged sequence versus the single Wigner surmise: \(D=0.13359\);
- the merged sequence versus the fixed-fraction product of two
  Wigner-surmise renewal gap functions: \(D=0.02400\);
- applying that two-component model to either factor alone is much worse:
  \(D=0.1802,0.1914\).

Thus the preregistered relative-distance gate passes decisively.  The result is
real finite-sample evidence that the merge deviation has the expected
two-component shape.

## Hostile scope correction

The tested CDF is

\[
E(s)=E_W(f_1s)E_W(f_2s),
\]

where \(E_W\) is built from the Wigner surmise under a renewal approximation.
It is **not** the exact nearest-neighbour distribution of a superposition of
two GUE point processes.  Nor can a deterministic finite zero list establish
statistical independence of the two spectra.  In addition, the nominal iid KS
value for the superposition fit is about \(0.0037\), below \(0.01\); adjacent
spacings are dependent, so that number is diagnostic rather than a calibrated
test here, but it plainly cannot support an “exact fit” headline.

The defensible answer is therefore:

> On the committed \(T=3000\) data, the merged spacings are substantially more
> compatible with the fixed-fraction two-component Wigner-surmise renewal model
> than with a single Wigner surmise, and factor-only controls discriminate the
> direction.  This is empirical compatibility with the expected product-spectrum
> mechanism—not a proof of independence, exact GUE superposition, or
> object-specific universality.

OA-C1077's original single-GUE proposition is `REFUTED`.  The replacement
two-component result belongs in a separate `EMPIRICAL` row.

## Reproducibility

`certificates/r009_c4_superposition/superposition_stdlib.py` uses only the
Python standard library and file-relative vendored data.  The data SHA-256
digests are:

- zeta: `fd65ad71d2a5c56a749150bbe049eda9df6fe44d620afdacee2ac97856dca0e2`;
- L(chi_-3): `ffad4dee2741e705a15481853c92babf60bf589563440d8f9511c8d4bebff716`.
