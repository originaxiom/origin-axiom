# B548 — The un-hideability census: prediction REFUTED (the property is generic)

Tests whether "un-hideable ⟺ self-priored / Pisot" (the conjecture the
Hoffman + Barrett pointers sharpened). Census over small substitutions:
enumerate the incidence matrix's Parikh-lifts, filter by grammar + length-6
language, count distinct surviving languages. UN-HIDEABLE := collapse to one
conjugacy class.

| substitution | #lifts | distinct langs | verdict | class |
|---|---|---|---|---|
| Fibonacci a→ab, b→a | 2 | 1 | UN-HIDEABLE | Pisot β=φ |
| Thue–Morse a→ab, b→ba | 4 | 1 | UN-HIDEABLE | Pisot β=2 |
| period-doubling a→ab, b→aa | 2 | 1 | UN-HIDEABLE | **non-Pisot** β=2 |
| tribonacci | 4 | 1 | UN-HIDEABLE | Pisot β=1.839 |
| 3-bonacci variant a→ab,b→c,c→a | 2 | 1 | UN-HIDEABLE | Pisot β=1.466 |
| reducible a→aa, b→ab | 2 | 1 | UN-HIDEABLE | **non-Pisot, reducible** β=2 |
| σ (4-letter object) | 17280 | 2 | UN-HIDEABLE | Pisot β=3.676 (B535, locked) |

**Prediction 2 REFUTED (falsifier partially fired):** un-hideability does NOT
track the Pisot / irreducible-charpoly property. Even the non-Pisot
period-doubling AND the reducible a→aa,b→ab are un-hideable. Every small
substitution tested is un-hideable — the property is GENERIC at small
alphabet size, not discriminating.

**Honest consequence for the Hoffman/Barrett framing:** "the object is
un-hideable" is TRUE (B535) but it is NOT special to this object — most small
substitutions are self-priored. Un-hideability is the generic case; a
HIDEABLE substitution (many surviving languages, needing an external prior)
is the thing to hunt, and it did not appear in this small census. The
"faithful ⟺ self-priored" reading survives as a definition but loses its
force as a DISCRIMINATOR until a hideable example is exhibited (larger
alphabets, or high image-permutation-freedom, where σ's own 17280→2 shows the
first non-trivial collapse). Filed as an honest deflation, not a hit.

Methodology note: the σ row's fast recompute disagreed with B535's locked
value (my quick language filter is not identical to the tested B535 C2
machinery); σ defers to B535's 2. The small rows (tiny lift counts) are
exact. Locks: tests/test_b548.py (small cases only).
