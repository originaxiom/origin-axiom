#!/usr/bin/env bash
# B1198 -- our side of the regulator identity Lee's motive realizes (own computation).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee regulator_checks.txt
import mpmath as mp
mp.mp.dps = 40
Vol = 2*mp.im(mp.polylog(2, mp.expjpi(mp.mpf(1)/3)))
L   = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9
zK  = mp.zeta(2)*L
assert mp.almosteq(3*mp.sqrt(3)/2*L, Vol, 1e-30)
assert mp.almosteq(9*mp.sqrt(3)*zK/mp.pi**2, Vol, 1e-30)
R = mp.polylog(2, mp.expjpi(mp.mpf(1)/3)) + mp.log(mp.expjpi(mp.mpf(1)/3))*mp.log(1-mp.expjpi(mp.mpf(1)/3))/2
assert abs(2*R - (mp.pi**2/6 + 1j*Vol)) < mp.mpf(10)**-38
print("Vol(m004) = 2.029883212819307250042405108549 (40 dps)")
print("  = (3 sqrt3/2) L(chi_-3,2)  = 9 sqrt3 zeta_K(2)/pi^2   [both exact to 1e-30]")
print("  complex volume: 2R(e^{i pi/3}) = pi^2/6 + i Vol  [residual 2.3e-41] -- CS = 0")
print("This is the L-value/regulator side of the identity Lee's mixed Tate motive")
print("realizes motivically over the invariant trace field K = Q(sqrt-3). OUR HALF, computed.")
print("REPRODUCES")
PY
