"""B1957: agy-exp's X-FOUNDATION campaign, the statements main can decide by its own computation (2026-11-18; data-free).
The seat's notes are read; none of its code is run or imported.
 F1  the 240 roots of E8 by the charge Q = (2/3)(e0 + e1 + e2): how many are neutral, of charge +-1, and of fractional
     charge; the least k > 0 with exp(2 pi i k Q) = 1 on every root; Q on the roots orthogonal to the colour roots.
 F2  the punctured-torus bundle with monodromy M = [[2, 1], [1, 1]]: ker(M - 1) on the fibre's first homology (the
     second homology of the bundle) and det(M - 1); the traces of M^1..M^4; det(M^4 - 1) and its Smith form.
 F3  2 sin(pi/5) and 2 sin(2 pi/5); the least and greatest distance among any three distinct fifth roots of unity.
 F4  frame C on main's own frame code (B1945's determinant_law, B1940's frame): at each of the 24 points of order 5,
     det Y(tau + 5, w)/det Y(tau, w) and the same at tau + 25, divided by its value at a reference point.  The same
     representatives (i/5, j/5) on both sides, as in B1945's plain-sum test.
 F5  frame D1's residue at the pole (main's rebuild in web_wb2_d1.py: v_x(-h) v_y(-h)^T / theta_1'(0), h = c q_H w), point by
     point, for c = 0, +-1, +-2, 5, 7 and the three sectors: each entry at tau + 5 and at tau + 25 over the same entry at
     tau, divided by the same ratio at a reference point.  The four entries must agree (the change is one scalar per
     point), and the scalar is compared with zeta^(E (5a)^2), E = q_L^2 + q_R^2 + c q_H^2 mod 5.  A plain sum of these
     residues is not used: they carry no metric and differ in size by many orders between points.
 F6  the tension on a parabola y = c u(1 - u) with the induced factor K = 1 + c^2 (1 - 2u)^2, at b = 2 and c = 3/5 (the
     two inputs read from the text of the seat's checker): 2 sqrt(b) int u(1 - u) sqrt(K) du, sqrt(b)/3,
     sqrt(b + c^2)/3 and the two ratios, against the four figures of its committed output file."""
import sys, pathlib, itertools, functools, math, cmath
from fractions import Fraction as Fr
import numpy as np, sympy as sp
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))

# F1
roots = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=8):
    if sum(1 for s in signs if s < 0) % 2 == 0: roots.append(tuple(Fr(s, 2) for s in signs))
assert len(roots) == 240
Q = lambda r: Fr(2, 3) * (r[0] + r[1] + r[2])
neutral = sum(1 for r in roots if Q(r) == 0); unit = sum(1 for r in roots if abs(Q(r)) == 1); frac = sum(1 for r in roots if Q(r).denominator == 3)
least = next(k for k in range(1, 10) if all((k * Q(r)).denominator == 1 for r in roots))
colour = [r for r in roots if all(r[i] == 0 for i in range(3, 8)) and sum(r[:3]) == 0]
cent = [r for r in roots if all(sum(x * y for x, y in zip(r, c)) == 0 for c in colour)]
print("F1: roots 240; neutral %d, charge +-1 %d, fractional charge %d (values %s); least k with exp(2 pi i k Q) = 1 on all roots: %d; colour roots %d; roots orthogonal to them %d, their charges %s"
      % (neutral, unit, frac, sorted({str(Q(r)) for r in roots if Q(r).denominator == 3}, key=lambda s: Fr(s)), least, len(colour), len(cent), sorted({str(Q(r)) for r in cent}, key=lambda s: Fr(s))))
# F2
M = sp.Matrix([[2, 1], [1, 1]]); one = sp.eye(2)
from sympy.matrices.normalforms import smith_normal_form
print("F2: ker(M - 1) has dimension %d and det(M - 1) = %d, so the bundle's second homology is 0 and its first is Z; traces of M^1..4: %s; det(M^4 - 1) = %d; Smith form of M^4 - 1: %s"
      % (len((M - one).nullspace()), (M - one).det(), [(M ** k).trace() for k in (1, 2, 3, 4)], (M ** 4 - one).det(), [abs(x) for x in smith_normal_form(M ** 4 - one, domain=sp.ZZ).diagonal()]))
# F3
z = [cmath.exp(2j * math.pi * k / 5) for k in range(5)]; mins, maxs = set(), set()
for tri in itertools.combinations(range(5), 3):
    d = [abs(z[a] - z[b]) for a, b in itertools.combinations(tri, 2)]; mins.add(round(min(d), 6)); maxs.add(round(max(d), 6))
print("F3: 2 sin(pi/5) = %.6f; 2 sin(2 pi/5) = %.6f; among any three distinct fifth roots the least distance is %s and the greatest %s" % (2 * math.sin(math.pi / 5), 2 * math.sin(2 * math.pi / 5), sorted(mins), sorted(maxs)))
# F4
import determinant_law as DL
mp = DL.mp
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
def fifth(r):
    k = float(mp.arg(r)) * 5 / (2 * math.pi); return int(round(k)) % 5, abs(k - round(k)), abs(float(abs(r)) - 1)
for sec in ("up", "down"):
    for rd in ("S", "St"):
        d0 = {}; skipped = 0
        for p in PTS:
            dets = [mp.det(DL.parts(tx, 1.7, p[0], p[1], sec)[2][rd]) for tx in ("0.13", "5.13", "25.13")]
            if abs(dets[0]) == 0: skipped += 1; continue
            d0[p] = (dets[1] / dets[0], dets[2] / dets[0])
        ref = d0[(Fr(0), Fr(1, 5))]; res5, res25, off = {}, {}, 0.0
        for p, (r5, r25) in d0.items():
            k5, e5, m5 = fifth(r5 / ref[0]); k25, e25, m25 = fifth(r25 / ref[1]); off = max(off, e5, m5, e25, m25)
            res5.setdefault(k5, set()).add(int(p[0] * 5)); res25.setdefault(k25, set()).add(int(p[0] * 5))
        print("F4 %-4s %-2s: points with det = 0: %d; under tau + 5 the determinant's phase over the reference is zeta^k with k -> rows 5a: %s; under tau + 25: %s; worst distance from a fifth root %.1e"
              % (sec, rd, skipped, {k: sorted(v) for k, v in sorted(res5.items())}, {k: sorted(v) for k, v in sorted(res25.items())}, off))
# F5
import web_wb2_d1 as D
ZERO = (Fr(0), Fr(1, 5))
def resid(tx, a, b, sec, c):
    t = mp.mpc(tx, "1.7"); ql, qr, qh = D.SEC[sec]; h = c * qh * (D.f2m(a) * t + D.f2m(b))
    return D.vvec(D.chars(ql, a, b), -h, t) * D.vvec(D.chars(qr, a, b), -h, t).T / D.t1p(t)
closes = {}
for c in (0, 1, -1, 2, -2, 5, 7):
    row = []
    for sec in ("up", "down", "lepton"):
        ql, qr, qh = D.SEC[sec]; E = (ql * ql + qr * qr + c * qh * qh) % 5; worst = 0.0; ks = {5: {}, 25: {}}; sg = {5: {}, 25: {}}
        base = {p: resid("0.13", p[0], p[1], sec, c) for p in PTS}
        for shift, tx in ((5, "5.13"), (25, "25.13")):
            rat = {p: [resid(tx, p[0], p[1], sec, c)[m, n] / base[p][m, n] for m in range(2) for n in range(2)] for p in PTS}
            for p in PTS:
                rho = [x / y for x, y in zip(rat[p], rat[ZERO])]; k, e, m_ = fifth(rho[0]); rel = [r / rho[0] for r in rho[1:]]
                signs = tuple(int(round(float(r.real))) for r in rel); worst = max(worst, e, m_, max(float(abs(r - sg_)) for r, sg_ in zip(rel, signs)))
                assert set(signs) <= {1, -1}
                ks[shift].setdefault(int(p[0] * 5), set()).add(k); sg[shift].setdefault(int(p[0] * 5), set()).add(signs)
        assert all(len(v) == 1 for sh in ks.values() for v in sh.values()) and all(len(v) == 1 for sh in sg.values() for v in sh.values())
        k5 = {i: next(iter(v)) for i, v in sorted(ks[5].items())}; k25 = {i: next(iter(v)) for i, v in sorted(ks[25].items())}
        law = all(k5[i] == (E * i * i) % 5 for i in k5); assert set(k25.values()) == {0}
        scalar = {sh: all(next(iter(v)) == (1, 1, 1) for v in sg[sh].values()) for sh in (5, 25)}
        odd = {sh: all(next(iter(v)) == ((1, 1, 1) if (i % 2 == 0) else (-1, -1, 1)) for i, v in sg[sh].items()) for sh in (5, 25)}
        closes[(c, sec)] = (set(k5.values()) == {0}) and scalar[5]
        row.append("%s E = %d, k by row %s (= E (5a)^2: %s), one scalar per point at +5 and +25: %s and %s%s, worst %.0e"
                   % (sec, E, list(k5.values()), law, scalar[5], scalar[25], "" if scalar[5] and scalar[25] else " (the two off-diagonal entries carry (-1)^(5a): %s and %s)" % (odd[5], odd[25]), worst))
    print("F5 c = %+d: under tau + 5 the first entry's phase over the reference is zeta^k, k by the row 5a = 0..4; E = q_L^2 + q_R^2 + c q_H^2 mod 5; the first entry's phase is 1 at every point under tau + 25: %s" % (c, "; ".join(row)))
print("F5: sectors whose residue is unchanged up to one constant under tau + 5, by c: %s; a c with both up and down: %s; residues c mod 5 with 2 + 4c = 0 and 4c = 0 mod 5: %s"
      % ({c: [s for s in ("up", "down", "lepton") if closes[(c, s)]] for c in (0, 1, -1, 2, -2, 5, 7)}, [c for c in (0, 1, -1, 2, -2, 5, 7) if closes[(c, "up")] and closes[(c, "down")]], [c for c in range(5) if (2 + 4 * c) % 5 == 0 and (4 * c) % 5 == 0]))
# F6
import mpmath as mq
b_, c_ = mq.mpf(2), mq.mpf(3) / 5
true = 2 * mq.sqrt(b_) * mq.quad(lambda u: u * (1 - u) * mq.sqrt(1 + c_ * c_ * (1 - 2 * u) ** 2), [0, mq.mpf(1) / 2, 1])
unc, straight = mq.sqrt(b_) / 3, mq.sqrt(b_ + c_ * c_) / 3
COMMITTED = {"true": 0.48777795855930306, "uncurved": 0.47140452079103173, "ratio": 0.9525492183792764, "old ratio": 0.9205746178983234}
mine = {"true": true, "uncurved": unc, "ratio": true / straight, "old ratio": mq.sqrt(b_) / mq.sqrt(b_ + c_ * c_)}
print("F6: the tension with the induced factor %s, without it %s, their ratio to the straight path's %s and %s; |y''| = 2c = %s; greatest difference from the seat's four committed figures: %.1e"
      % (mq.nstr(true, 10), mq.nstr(unc, 10), mq.nstr(mine["ratio"], 10), mq.nstr(mine["old ratio"], 10), mq.nstr(2 * c_, 3), max(abs(float(mine[k]) - v) for k, v in COMMITTED.items())))
