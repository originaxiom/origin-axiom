"""cc2 INDEPENDENT recompute of B645's two headline numbers, from raw
text values transcribed by hand (via Read, byte-checked) out of the
B637 source tables -- NOT via B645's own parser (re.compile + sympy)
and NOT via the test file's parser (also sympy). Pure stdlib
fractions.Fraction, hand-rolled Q(sqrt(-3)) arithmetic: elements are
(a, b) meaning a + b*r with r = sqrt(-3), so r*r = -3.

Row 1 -- the unit cross-ratio law on a 024-SILENT double (the unbent
weld table, B637/stage3_output.txt lines 64-74):
  (Y[023]*Y[134]) / (Y[034]*Y[123]) should be exactly 1.

Row 2 -- one row of the 13-dial table on a 024-LIT double
(D_bent(M; m=1), B637/part2b_stage2_fixed_output.txt lines 25-35):
  inv1 = (Y[023]*Y[124]) / (Y[024]*Y[123]) claimed = 1 + 13/3696 (real)
  inv2 = (Y[023]*Y[134]) / (Y[034]*Y[123]) claimed
       = 1 + 13*(6613 + 13*sqrt(-3))/21866138
"""
from fractions import Fraction as Fr


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def qmul(x, y):
    a, b = x
    c, d = y
    return (a * c - 3 * b * d, a * d + b * c)


def qinv(x):
    a, b = x
    den = a * a + 3 * b * b
    return (a / den, -b / den)


def qdiv(x, y):
    return qmul(x, qinv(y))


def qshow(x):
    a, b = x
    if b == 0:
        return str(a)
    return f"{a} + {b}*r"


# ---- Row 1: the unbent weld table (024-silent) ------------------------------
# transcribed by hand from stage3_output.txt:64-74 (Read tool, byte-checked)
Y023_w = (Fr(-7983360, 13), Fr(2661120, 13))
Y024_w = (Fr(0), Fr(0))
Y034_w = (Fr(0), Fr(2, 3))
Y123_w = (Fr(0), Fr(221760, 13))
Y124_w = (Fr(0), Fr(2, 3))
Y134_w = (Fr(1, 24), Fr(1, 72))

assert Y024_w == (Fr(0), Fr(0)), "024 must be silent for the cross-ratio law"

num_w = qmul(Y023_w, Y134_w)
den_w = qmul(Y034_w, Y123_w)
cr_w = qdiv(num_w, den_w)
print("== Row 1: unit cross-ratio law (unbent weld, 024-silent) ==")
print(f"  Y023 = {qshow(Y023_w)}")
print(f"  Y134 = {qshow(Y134_w)}")
print(f"  Y034 = {qshow(Y034_w)}")
print(f"  Y123 = {qshow(Y123_w)}")
print(f"  (Y023*Y134)/(Y034*Y123) = {qshow(cr_w)}")
print(f"  == 1 exactly: {cr_w == (Fr(1), Fr(0))}")

# ---- Row 2: D_bent(M; m=1) (024-lit) ----------------------------------------
# transcribed by hand from part2b_stage2_fixed_output.txt:25-35
Y023_b = (Fr(-7983360, 13), Fr(2661120, 13))
Y024_b = (Fr(-88704, 13), Fr(29568, 13))
Y034_b = (Fr(-3300, 13), Fr(3326, 39))
Y123_b = (Fr(0), Fr(221760, 13))
Y124_b = (Fr(0), Fr(7418, 39))
Y134_b = (Fr(1, 24), Fr(2213, 312))

print("\n== Row 2: the 13-dial, D_bent(M; m=1) (024-lit) ==")
inv1 = qdiv(qmul(Y023_b, Y124_b), qmul(Y024_b, Y123_b))
print(f"  inv1 = (Y023*Y124)/(Y024*Y123) = {qshow(inv1)}")
claim1 = (Fr(1) + Fr(13, 3696), Fr(0))
print(f"  claimed 1 + 13/3696 = {qshow(claim1)}  match: {inv1 == claim1}")
dev1 = qsub(inv1, (Fr(1), Fr(0)))
if dev1[0] != 0:
    n, d = dev1[0].numerator, dev1[0].denominator
    print(f"  deviation (real part) = {dev1[0]} = {n}/{d}; "
          f"13 | numerator: {n % 13 == 0}; 13 does not divide denom: {d % 13 != 0}")

inv2 = qdiv(qmul(Y023_b, Y134_b), qmul(Y034_b, Y123_b))
print(f"\n  inv2 = (Y023*Y134)/(Y034*Y123) = {qshow(inv2)}")
# claimed form: 1 + 13*(6613 + 13r)/21866138
claim2 = qadd((Fr(1), Fr(0)),
              qmul((Fr(13), Fr(0)),
                   (Fr(6613, 21866138), Fr(13, 21866138))))
print(f"  claimed 1 + 13*(6613+13r)/21866138 = {qshow(claim2)}  "
      f"match: {inv2 == claim2}")
dev2 = qsub(inv2, (Fr(1), Fr(0)))
for label, comp in (("real", dev2[0]), ("r-coeff", dev2[1])):
    if comp != 0:
        n, d = comp.numerator, comp.denominator
        print(f"  deviation {label} part = {comp} = {n}/{d}; "
              f"13 | numerator: {n % 13 == 0}; 13 does not divide denom: {d % 13 != 0}")

print("\nDONE (pure-Fraction independent path; no sympy, no repo parser reused)")
