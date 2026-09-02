#!/usr/bin/env python3
"""R48(f): the B511/D3 trace-map dynamics at two precisions (mpmath dps=15 ~ double, and dps=60).
If the 'classicalization' (kappa -> 2 exactly) is a floating-point absorbing state, it must shrink with precision;
if it is dynamics, it must not.  Moves as committed: F (AB,A), M (AB,BA), D (A^2,B^2), on traces (x,y,z)."""
import mpmath as mp, random, sys
def run(dps, mix, n=300, steps=3000, seed=11):
    mp.mp.dps = dps; rnd = random.Random(seed); out = []
    K = lambda x, y, z: x*x + y*y + z*z - x*y*z - 2
    for h in range(n):
        # Haar SU(2) pair via random unit quaternions -> traces; build from angles: tr = 2 cos(theta)
        import math
        def haar():
            a = [rnd.gauss(0, 1) for _ in range(4)]; s = math.sqrt(sum(v*v for v in a)); a = [v/s for v in a]
            return a
        qa, qb = haar(), haar()
        # quaternion product for AB: (a0,a) (b0,b) = (a0 b0 - a.b, ...); tr = 2*real part
        def qmul(p, q): return [p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3], p[0]*q[1]+p[1]*q[0]+p[2]*q[3]-p[3]*q[2], p[0]*q[2]-p[1]*q[3]+p[2]*q[0]+p[3]*q[1], p[0]*q[3]+p[1]*q[2]-p[2]*q[1]+p[3]*q[0]]
        x, y, z = mp.mpf(2*qa[0]), mp.mpf(2*qb[0]), mp.mpf(2*qmul(qa, qb)[0]); k0 = K(x, y, z)
        absorbed = False; escaped = False
        for t in range(steps):
            r = rnd.random()
            if r < mix[0]:   w = x*y*z - x*x - y*y + 2; x, y, z = z, z, w
            elif r < mix[0] + mix[1]: w = x*y*z - x*x - y*y + 2; x, y, z = x*x - 2, y*y - 2, w
            else: x, y, z = z, x, x*z - y
            if abs(x) > 2 + mp.mpf(10)**(-dps+3) or abs(y) > 2 + mp.mpf(10)**(-dps+3): escaped = True; break
        k = K(x, y, z) if not escaped else mp.nan
        out.append((k, escaped, k0))
    fin = [o for o in out if not o[1]]
    cl = sum(1 for k, _, _ in fin if abs(k - 2) < mp.mpf('0.05')); wild = sum(1 for k, _, _ in fin if abs(k - 2) > mp.mpf('0.5') and -2 <= k <= 2)
    dk = max((abs(k - k0) for k, _, k0 in fin), default=mp.nan) if mix == (0.0, 0.0) else None
    return dict(escaped=sum(o[1] for o in out)/n, classical=cl/max(len(fin), 1), wild=wild/max(len(fin), 1), n_fin=len(fin), dk=dk)
for dps in (15, 60):
    for mix, name in [((0.10, 0.10), 'M10/D10/F80'), ((0.0, 0.20), 'D20/F80'), ((0.20, 0.0), 'M20/F80'), ((0.0, 0.0), 'F100 control')]:
        r = run(dps, mix); print('dps=%2d %-13s escaped=%.3f  over %3d finite: P(classical)=%.3f P(wild)=%.3f%s' % (dps, name, r['escaped'], r['n_fin'], r['classical'], r['wild'], ('  max|kappa-kappa0|=%s' % mp.nstr(r['dk'], 3)) if r['dk'] is not None else ''), flush=True)
