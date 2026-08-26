#!/usr/bin/env python3
"""Dependency-free reproduction and scope audit of the B1153 C4 statistic.

The certificate uses only the Python standard library.  It reproduces the
Kolmogorov distances for the single Wigner surmise and for the product of two
Wigner-surmise renewal gap functions.  It deliberately does not rename that
approximation as the exact GUE point-process spacing law.
"""

from math import erf, erfc, exp, log, pi, sqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"


def read_zeros(name):
    return sorted(float(line) for line in (DATA / name).read_text().splitlines() if line.strip())


def unfold_factor(values, conductor):
    spacings = []
    for left, right in zip(values, values[1:]):
        midpoint = (left + right) / 2
        density = log(conductor * midpoint / (2*pi)) / (2*pi)
        if density > 0:
            spacings.append((right-left) * density)
    return spacings


def gue_wigner_cdf(value):
    return erf(2*value/sqrt(pi)) - (4*value/pi)*exp(-4*value*value/pi)


def ks_distance(sample, cdf):
    ordered = sorted(sample)
    size = len(ordered)
    d_plus = max((index+1)/size - cdf(value) for index, value in enumerate(ordered))
    d_minus = max(cdf(value) - index/size for index, value in enumerate(ordered))
    return max(d_plus, d_minus)


def nominal_ks_p_asymptotic(distance, size):
    """Two-sided iid asymptotic KS p-value; diagnostic, not a validity claim."""
    lam = (sqrt(size) + 0.12 + 0.11/sqrt(size)) * distance
    total = 0.0
    for k in range(1, 100):
        term = 2 * (-1 if k % 2 == 0 else 1) * exp(-2*k*k*lam*lam)
        total += term
        if abs(term) < 1e-16:
            break
    return max(0.0, min(1.0, total))


zeta = read_zeros("c4_zeros_zeta.txt")
lchi = read_zeros("c4_zeros_L.txt")
assert len(zeta) == 2469 and len(lchi) == 2991

uz = unfold_factor(zeta, 1)
ul = unfold_factor(lchi, 3)
Dz = ks_distance(uz, gue_wigner_cdf)
Dl = ks_distance(ul, gue_wigner_cdf)

merged = sorted(zeta + lchi)
um = []
for left, right in zip(merged, merged[1:]):
    midpoint = (left + right) / 2
    density = (
        log(midpoint/(2*pi)) + log(3*midpoint/(2*pi))
    ) / (2*pi)
    if density > 0:
        um.append((right-left) * density)

Dm = ks_distance(um, gue_wigner_cdf)
f1 = len(zeta)/(len(zeta)+len(lchi))
f2 = 1-f1


def gap(value):
    return exp(-4*value*value/pi) - value*erfc(2*value/sqrt(pi))


def gap_prime(value):
    return -erfc(2*value/sqrt(pi)) - (4*value/pi)*exp(-4*value*value/pi)


def superposition_cdf(value):
    if value <= 0:
        return 0.0
    return 1 + (
        f1*gap_prime(f1*value)*gap(f2*value)
        + f2*gap(f1*value)*gap_prime(f2*value)
    )


Ds = ks_distance(um, superposition_cdf)
Dzs = ks_distance(uz, superposition_cdf)
Dls = ks_distance(ul, superposition_cdf)
p_nominal = nominal_ks_p_asymptotic(Ds, len(um))

assert abs(Dz-0.0401) < 1e-3
assert abs(Dl-0.0487) < 1e-3
assert abs(Dm-0.13359) < 1e-4
assert abs(Ds-0.02400) < 1e-4
assert abs(Dzs-0.1802) < 1e-4
assert abs(Dls-0.1914) < 1e-4
assert Ds < 0.06 and Ds < Dm/2
assert Dzs > Dz and Dls > Dl
assert p_nominal < 0.01

print(f"data counts: zeta={len(zeta)} Lchi={len(lchi)} merged={len(merged)}")
print(f"single-factor Wigner distances: zeta={Dz:.5f} Lchi={Dl:.5f}")
print(f"merged versus single Wigner: D={Dm:.5f}")
print(f"density fractions: f_zeta={f1:.6f} f_Lchi={f2:.6f}")
print(f"merged versus two-renewal superposition: D={Ds:.5f}")
print(f"factor controls versus superposition: zeta={Dzs:.5f} Lchi={Dls:.5f}")
print(f"nominal iid asymptotic KS p for superposition: {p_nominal:.6g}")
print("VERDICT: RELATIVE D-GATE PASSES; EXACT GUE/INDEPENDENCE CLAIM DOES NOT FOLLOW")
