"""R72 (part 4) -- the SM seat's D2 (B916/B1250/B1265) in this bench's frame.

B1250: D2(w) = (-1)^(<w13, w> + 1) on the 27's weights, w13 itself one of the 27 and itself flipped ("the 11-flip").
B1265: D2 is conjugation by a torus element, fixed algebra so(10) + u(1) (dim 46), signature -14: INNER.
Checked here in Bourbaki Dynkin labels with the invariant form scaled by 3 (integral on the 27: values 4, 1, -2):
  for w13 = any weight of the 27, D(w) = (-1)^(3<w13,w> + 1) flips exactly 11 weights (w13 and the 10 with pairing -2)
  and fixes 16; on the roots D(alpha) = (-1)^(3<w13,alpha>) fixes exactly 40 = the D5 orthogonal to w13, so the fixed
  algebra is D5 + T^1 = so(10) + u(1); the coweight dual to w13 has centraliser D5 + T^1 -- the SO(10) direction, the
  Weyl class of omega_1^vee.  D2 is a torus element: it fixes every u in h and acts innerly on every C(u), so R72's
  untwisted count S_n(u) is the count under the record's own D2.
"""
import io, contextlib, collections
from fractions import Fraction as Fr
import sympy as sp
_src = open('r71_theta_even_pairing.py').read().split('print("\\n== all other theta-even directions')[0]
with contextlib.redirect_stdout(io.StringIO()): exec(_src)
def form(l, m):   # invariant form in Dynkin labels: l^T C^-1 m
    v = (sp.Matrix(list(l)).T * Cinv * sp.Matrix(list(m)))[0]; return Fr(int(v.p), int(v.q))
results = collections.Counter()
for w13 in W27:
    pair = {w: 3*form(w13, w) for w in W27}
    assert all(p.denominator == 1 for p in pair.values()) and set(int(p) for p in pair.values()) == {4, 1, -2}
    D = {w: (-1)**(int(pair[w]) + 1) for w in W27}
    flipped = [w for w in W27 if D[w] == -1]
    rootsign = {a: (-1)**int(3*form(w13, a)) for a in ROOTS}
    fixed_roots = [a for a in ROOTS if rootsign[a] == 1]
    pos_, simple_ = cu_simple(fixed_roots); typ = '+'.join(sorted(t for t, _ in factors(simple_)))
    # the coweight dual to w13: u = C^-1 w13 in coweight coordinates has <lambda, u> = 3 form(w13, lambda)/3 ... use c = Dynkin labels of w13 as coweight coefficients? no: <l, sum c_k omega_k^vee> = c . rootcoords(l); choose c with c . rc(l) = form(w13, l): c = Dynkin labels of w13 (since form(w13,l) = w13^T C^-1 l = w13 . rc(l))
    c = tuple(Fr(x) for x in w13)
    cu = [a for a in ROOTS if dot(c, RC[a]) == 0]; pos2, simple2 = cu_simple(cu); typ_u = '+'.join(sorted(t for t, _ in factors(simple2)))
    results[(len(flipped), D[w13], len(fixed_roots), typ, len(cu), typ_u)] += 1
print("over all 27 choices of w13: (flipped weights, D(w13), fixed roots, fixed type, |roots of C(u_w13)|, type):", dict(results))
assert results == collections.Counter({(11, -1, 40, 'D5', 40, 'D5'): 27})
print("D2 flips 11 = w13 + the 10, fixes the 16; fixed algebra so(10)+u(1) (dim 46, rank 6: INNER, a torus element); u_w13 has C(u) = D5+T1: the SO(10) direction.")
# and the count under D2: identical to the untwisted count (D2 fixes h pointwise)
print("under D2 every direction u in h is even and the twist on C(u) is inner: S_n(u) = n (+)_{q>0} 27_q (+) n (+)_{q<0} conj(27_q) -- R72 (c).")
print("SELFTEST: PASS")
