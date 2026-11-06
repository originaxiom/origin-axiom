#!/usr/bin/env python3
"""
verify_agy29/check_algebra.py -- algebra and circularity checks for agy Stage 29 (claims 5c, 9a, 10, 11).

PRE-REGISTERED: header written before any run; sha256 recorded in prereg_sha256.txt before the first run.
DATA-FREE, VALUE-FREE: every input is a random number or a 2x2 integer matrix. No volume, level, coupling, scale ratio,
CKM or CP quantity of any manifold or frame is evaluated; agy's code is not imported or run.

PREDICTIONS AND PASS RULES
A1 (9a, B1012's split). With c+ = i(V + iC), c- = conj(c+), t = k + i s, t~ = k - i s, V, C, k, s random reals:
   S := (t/2) c+ + (t~/2) c-.  Pass rule: S == -k*C - s*V iff max relative error < 1e-12 over 10^4 draws.
   Per hand: the k-coefficient of hand + is c+/2, of hand - is c-/2. Report: their imaginary parts (+-V/2) cancel for
   every (V, C); their real parts (-C/2 each) ADD to -C.  Prediction: S == -kC - sV; k drops iff C = 0.
A2 (9a, agy's docstring form, toe_closure.py 27842-27843 and 27875: c- = -i(V - i C-), with C- = -C+).
   S' := (t/2) c+ + (t~/2) c-'.  Pass rule: S' is k-independent for every C iff max |S'(k1) - S'(k2)| < 1e-12;
   S' == S iff |S' - S| < 1e-12.  Prediction: c-' = -c+ identically, so S' = -sV - i s C is k-independent for ANY C,
   and S' != S unless C = 0 (the docstring's form builds the k-cancellation in; it cannot test amphichirality).
A3 (11). L^n mod 5 for n = 1..10 in GENESIS's convention L = [[1,1],[0,1]] and in the transposed [[1,0],[1,1]].
   Prediction: L^n == I (mod 5) iff 5 | n; L^6 == L (mod 5) != I. The ledger's 'L^6 == I (mod 5)' is FALSE.
A4 (5c, Theorem 156's 50-digit 'independent countercheck', toe_closure.py 28561-28566). For 2000 random complex z:
   L := 2 asinh(1/sqrt(z - 1)) (negated if Re L < 0); err := |coth^2(L/2) - z| / max(1, |z|).
   Pass rule: the check is a TAUTOLOGY iff err < 1e-9 for every random z (it cannot fail for any z).
   Prediction: tautology.
A5 (5c, Theorem 154's Haar check, toe_closure.py 28196-28216). For 2000 random complex L and random unitary U:
   M := [[cosh(L/2), sinh(L/2)], [sinh(L/2), cosh(L/2)]], M' := U M U^dagger; err := |tr^2/(tr^2 - 4 det) - coth^2(L/2)|.
   Pass rule: TAUTOLOGY iff err / max(1, |coth^2|) < 1e-9 for every draw.  Prediction: tautology.
"""
import cmath
import json
import os
import random

import numpy as np

random.seed(20261106)
rng = np.random.default_rng(20261106)
OUT = {}
HERE = os.path.dirname(os.path.abspath(__file__))

# A1, A2
max_rel = 0.0
max_kdep_prime = 0.0
min_diff_when_C_nonzero = float('inf')
vol_parts_cancel = 0.0
cs_parts_sum_err = 0.0
for _ in range(10000):
    V = random.uniform(0.1, 20.0)
    C = random.uniform(-0.5, 0.5)
    k = random.uniform(-10, 10)
    s = random.uniform(-10, 10)
    cp = 1j * (V + 1j * C)
    cm = cp.conjugate()
    t = complex(k, s)
    tt = complex(k, -s)
    S = (t / 2) * cp + (tt / 2) * cm
    ref = -k * C - s * V
    max_rel = max(max_rel, abs(S - ref) / max(1.0, abs(ref)))
    # per-hand k coefficients
    vol_parts_cancel = max(vol_parts_cancel, abs((cp / 2).imag + (cm / 2).imag))
    cs_parts_sum_err = max(cs_parts_sum_err, abs((cp / 2).real + (cm / 2).real - (-C)))
    # agy docstring variant
    Cm = -C
    cm_prime = -1j * (V - 1j * Cm)
    def S_prime(kk):
        return (complex(kk, s) / 2) * cp + (complex(kk, -s) / 2) * cm_prime
    max_kdep_prime = max(max_kdep_prime, abs(S_prime(k) - S_prime(k + 3.7)) / max(1.0, abs(S_prime(k))))
    if abs(C) > 1e-3:
        min_diff_when_C_nonzero = min(min_diff_when_C_nonzero, abs(S_prime(k) - S))
OUT['A1'] = dict(max_rel_err_S_vs_minus_kC_minus_sV=max_rel, identity_holds=max_rel < 1e-12,
                 per_hand_volume_parts_cancel_max=vol_parts_cancel, per_hand_cs_parts_add_to_minus_C_err=cs_parts_sum_err)
OUT['A2'] = dict(docstring_form_k_dependence_max=max_kdep_prime, k_independent_for_any_C=max_kdep_prime < 1e-12,
                 min_abs_Sprime_minus_S_when_absC_gt_1em3=min_diff_when_C_nonzero,
                 cminus_prime_equals_minus_cplus=all(abs(-1j * (v - 1j * (-c)) + 1j * (v + 1j * c)) < 1e-12
                                                     for v, c in ((1.3, 0.2), (7.0, -0.4), (2.0, 0.0))))

# A3
def matpow_mod(A, n, m):
    R = [[1, 0], [0, 1]]
    for _ in range(n):
        R = [[(R[0][0] * A[0][0] + R[0][1] * A[1][0]) % m, (R[0][0] * A[0][1] + R[0][1] * A[1][1]) % m],
             [(R[1][0] * A[0][0] + R[1][1] * A[1][0]) % m, (R[1][0] * A[0][1] + R[1][1] * A[1][1]) % m]]
    return R
a3 = {}
for label, Lm in (('GENESIS L=[[1,1],[0,1]]', [[1, 1], [0, 1]]), ('transposed [[1,0],[1,1]]', [[1, 0], [1, 1]])):
    powers = {n: matpow_mod(Lm, n, 5) for n in range(1, 11)}
    a3[label] = dict(identity_at=[n for n, P in powers.items() if P == [[1, 0], [0, 1]]],
                     L6_mod5=powers[6], L6_equals_L=powers[6] == [[x % 5 for x in r] for r in Lm],
                     L6_equals_I=powers[6] == [[1, 0], [0, 1]])
OUT['A3'] = a3

# A4
worst = 0.0
for _ in range(2000):
    z = complex(random.uniform(-50, 50), random.uniform(-50, 50))
    if abs(z - 1) < 1e-3:
        continue
    L = 2 * cmath.asinh(1 / cmath.sqrt(z - 1))
    if L.real < 0:
        L = -L
    c2 = (cmath.cosh(L / 2) / cmath.sinh(L / 2)) ** 2
    worst = max(worst, abs(c2 - z) / max(1.0, abs(z)))
OUT['A4'] = dict(max_rel_err_over_random_z=worst, tautology=worst < 1e-9)

# A5
worst5 = 0.0
for _ in range(2000):
    L = complex(random.uniform(0.01, 3.0), random.uniform(-3.1, 3.1))
    M = np.array([[cmath.cosh(L / 2), cmath.sinh(L / 2)], [cmath.sinh(L / 2), cmath.cosh(L / 2)]], dtype=complex)
    Z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    Q, R = np.linalg.qr(Z)
    U = Q * (np.diag(R) / np.abs(np.diag(R)))[np.newaxis, :]
    Mp = U @ M @ U.conj().T
    tr = complex(np.trace(Mp))
    det = complex(np.linalg.det(Mp))
    c2 = (cmath.cosh(L / 2) / cmath.sinh(L / 2)) ** 2
    worst5 = max(worst5, abs(tr ** 2 / (tr ** 2 - 4 * det) - c2) / max(1.0, abs(c2)))
OUT['A5'] = dict(max_rel_err=worst5, tautology=worst5 < 1e-9)

print(json.dumps(OUT, indent=1, default=str))
with open(os.path.join(HERE, 'check_algebra_out.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
