"""S301 verifier B, check T42 (value-free group theory, first principles; no lane code run).

Inputs are the torus data Theorem 42 states in clear (docstring l. 7834, l. 8063, T46 l. 8741-8746):
  x = (1/4, 0, -1/4, -1/2, -3/4), p = -H_5/4 = (1, 1/2, 0, -1/2, -1), c = (1/2)^5 on the D5 torus,
  h = exp(3 pi i Q_em / 4) with Q_em = (1, -1/3, -1/3, -1/3) on the 4 of SU(4) = Spin(6)  (=> Q_em|A3 = (2/3)(e1+e2+e3)).
E8 roots in the D8 basis (first 3 coordinates A3 = D3, last 5 D5).  Checked:
 (1) 2x - p = -c;  on the 32 spinor: A^2 = C^-1 P, A^4 = -I, P^2 = I, C = +-i by chirality;
 (2) h^2 = C_{A3} on the 4; C_{A3} C_{D5} acts trivially on all 240 root spaces (so h^2 = C_{A3} = C_{D5}^-1 in E8);
 (3) tilde_A = A h: tilde_A^2 = K_pi := zeta P (zeta = C_{D5}^2) and tilde_A^4 = I on all 240 roots; K_pi^2 = I, K_pi != I;
 (4) the presentation <a, d | a^8, d^4, a d a^-1 = d^-1> with <a> cap <d> = 1: order 32 = C4 x| C8, its invariants;
     and the same with a^4 = 1 (the 10_v image): order 16 = C4 x| C4 = main's Z4 x| Z4 (SmallGroup(16,4)) invariants.
D itself (Theorem 42's d_spin) is built from constants the mask withholds; its relations are not re-run here.
"""
import itertools
from fractions import Fraction as F
from collections import Counter

x = [F(1, 4), F(0), F(-1, 4), F(-1, 2), F(-3, 4)]
p = [F(1), F(1, 2), F(0), F(-1, 2), F(-1)]
c = [F(1, 2)] * 5
print("(1) 2x - p + c =", [2 * a - b + cc for a, b, cc in zip(x, p, c)])

def frac(z): return z - (z.numerator // z.denominator)
spin_w = [tuple(F(s, 2) for s in sg) for sg in itertools.product((-1, 1), repeat=5)]
dot = lambda u, v: sum(a * b for a, b in zip(u, v))
ok_A2 = all(frac(2 * dot(x, w) - (dot(p, w) - dot(c, w))) == 0 for w in spin_w)
A4 = set(frac(4 * dot(x, w)) for w in spin_w)
P2 = set(frac(2 * dot(p, w)) for w in spin_w)
Cv = Counter((sum(1 for s in w if s < 0) % 2, frac(dot(c, w))) for w in spin_w)
print("    A^2 = C^-1 P on all 32 weights:", ok_A2, "; phases of A^4 (as fractions of 2 pi):", A4, "(1/2 => -I)",
      "; phases of P^2:", P2, "; C's phase by chirality parity:", dict(Cv))

roots = []
for i, j in itertools.combinations(range(8), 2):
    for s1, s2 in itertools.product((-1, 1), repeat=2):
        r = [F(0)] * 8; r[i], r[j] = F(s1), F(s2); roots.append(r)
for sg in itertools.product((-1, 1), repeat=8):
    if sum(1 for s in sg if s < 0) % 2 == 0: roots.append([F(s, 2) for s in sg])
print("\n    E8 roots:", len(roots), "+ 8 Cartan =", len(roots) + 8)

cA3 = [F(1, 2)] * 3 + [F(0)] * 5
cD5 = [F(0)] * 3 + [F(1, 2)] * 5
hT = [F(1, 4)] * 3 + [F(0)] * 5                        # (3/8) * (2/3)(1,1,1)
for par, nm in ((0, "4 (even # of minus signs)"), (1, "4bar (odd)")):
    ws3 = [tuple(F(s, 2) for s in s3) for s3 in itertools.product((-1, 1), repeat=3) if sum(1 for s in s3 if s < 0) % 2 == par]
    Q4 = sorted(dot([F(2, 3)] * 3, w) for w in ws3)
    print("(2) Q_em on the %s with Q = (2/3)(e1+e2+e3):" % nm, [str(q) for q in Q4],
          "; h^2 phase (fractions of 2 pi):", set(str(frac(2 * F(3, 8) * q)) for q in Q4), "(3/4 => -i, 1/4 => +i)")
print("    h^2 has torus log 2h = cA3:", [2 * a for a in hT] == cA3)
print("    C_A3 C_D5 trivial on all 240 roots:", all(frac(dot(r, [a + b for a, b in zip(cA3, cD5)])) == 0 for r in roots))
xE = [F(0)] * 3 + x; pE = [F(0)] * 3 + p
zeta = [2 * a for a in cD5]
kpi = [a + b for a, b in zip(pE, zeta)]
tx = [a + b for a, b in zip(xE, hT)]
print("(3) tilde_A^2 = K_pi on all roots:", all(frac(dot(r, [2 * a - b for a, b in zip(tx, kpi)])) == 0 for r in roots),
      "; tilde_A^4 = I:", all(frac(dot(r, [4 * a for a in tx])) == 0 for r in roots),
      "; K_pi^2 = I:", all(frac(dot(r, [2 * a for a in kpi])) == 0 for r in roots),
      "; roots where K_pi != 1:", sum(1 for r in roots if frac(dot(r, kpi)) != 0))
# note: without h, A^2 = K_pi fails (h is what makes the A3 part work)
print("    control: A (no h) satisfies A^2 = K_pi on all roots:", all(frac(dot(r, [2 * a - b for a, b in zip(xE, kpi)])) == 0 for r in roots))

def semidirect(n_a, n_d):
    # elements (i, j) = a^i d^j, a d a^-1 = d^-1;  (a^i d^j)(a^k d^l) = a^(i+k) d^((-1)^k j + l)
    els = [(i, j) for i in range(n_a) for j in range(n_d)]
    mul = lambda u, v: ((u[0] + v[0]) % n_a, ((-1) ** v[0] * u[1] + v[1]) % n_d)
    e = (0, 0)
    def order(g):
        k, h = 1, g
        while h != e: h = mul(h, g); k += 1
        return k
    center = [g for g in els if all(mul(g, h) == mul(h, g) for h in els)]
    comm = set()
    inv = {g: next(h for h in els if mul(g, h) == e) for g in els}
    for g in els:
        for h in els: comm.add(mul(mul(g, h), mul(inv[g], inv[h])))
    return len(els), dict(Counter(order(g) for g in els)), len(center), len(comm)
print("\n(4) <a, d | a^8, d^4, ada^-1 = d^-1>: order, element orders, |center|, |[G,G]| =", semidirect(8, 4))
print("    <a, d | a^4, d^4, ada^-1 = d^-1>  : order, element orders, |center|, |[G,G]| =", semidirect(4, 4),
      " (main's c4 for <K_i, K_j>: orders {1:1, 2:3, 4:12}, |center| 4)")
