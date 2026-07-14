"""B599-ALG — the algebraic face of the selection rule (OA_SLOW lock ~12 min).

L0 (not dot-symmetric), nilpotency orders, the L1 parity zeros, the m=8/b2
t^2 witness and the weld-only twist-twist identity. See
frontier/B599_selection_rule/FINDINGS.md (B599-ALG).
"""
import os
import sys
from fractions import Fraction as Fr

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B599-ALG lock requires OA_SLOW=1 (the exact B575 build)",
                allow_module_level=True)

_ROOT = os.path.join(os.path.dirname(__file__), "..")
src = open(os.path.join(_ROOT, "frontier", "B575_bridge_obstruction",
                        "l51_obstruction.py")).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']
meye = ns['meye']; mexp_nil = ns['mexp_nil']; nullspace = ns['nullspace']
A27 = ns['A27']; B27 = ns['B27']; A27i = ns['A27i']; B27i = ns['B27i']
e_pr = ns['e_pr']; f_pr = ns['f_pr']; h_pr = ns['h_pr']; BLOCKS = ns['BLOCKS']
K0 = ns['K0']; K1 = ns['K1']

kc = lambda x: K(x.a, -x.b)
mconj = lambda M: [[kc(x) for x in r] for r in M]
matvec = lambda M, v: [sum((M[i][j] * v[j] for j in range(27)
                            if not v[j].is_zero()), K0) for i in range(27)]
dot = lambda u, v: sum((u[i] * v[i] for i in range(27)
                        if not (u[i].is_zero() or v[i].is_zero())), K0)

Om = madd(madd(mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
          mscale(K(Fr(1, 2)), mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]
VM = {m: BLOCKS[m][0] for m in (4, 8)}


def test_l0_not_dot_symmetric():
    assert not all((Om[i][j] - Om[j][i]).is_zero()
                   for i in range(27) for j in range(27))


def test_nilpotency_orders():
    for m, expected in ((4, 5), (8, 3)):
        P = VM[m]
        k = 1
        while True:
            P = mmul(P, VM[m])
            k += 1
            if all(all(x.is_zero() for x in r) for r in P):
                break
        assert k == expected


def test_l1_parity_zeros():
    for m in (4, 8):
        assert dot(matvec(VM[m], v0), v0).is_zero()


def test_t2_witness_and_weld_identity_m8():
    def letters(t):
        c = mexp_nil(mscale(K(t), VM[8]))
        ci = mexp_nil(mscale(K(-t), VM[8]))
        b2 = mmul(mmul(c, mconj(B27)), ci)
        return c, b2

    D = 22
    pts = [Fr(j) for j in range(D + 1)]
    vals = []
    for t in pts:
        c, b2 = letters(t)
        vals.append(dot(matvec(c, v0), matvec(b2, v0)))
    # Lagrange -> coefficients of the b-part (the sqrt(-3) coefficient)
    coB = [Fr(0)] * (D + 1)
    for i, (xi, vi) in enumerate(zip(pts, vals)):
        num = [Fr(1)]
        den = Fr(1)
        for j, xj in enumerate(pts):
            if j == i:
                continue
            new = [Fr(0)] * (len(num) + 1)
            for k in range(len(num)):
                new[k + 1] += num[k]
                new[k] -= xj * num[k]
            num = new
            den *= (xi - xj)
        for k in range(len(num)):
            coB[k] += vi.b * num[k] / den
    assert coB[0] == 0 and coB[1] == 0                 # Im starts at t^2
    assert coB[2] == Fr(-536481792000)                 # the witness
    c, b2 = letters(Fr(1))
    val = dot(v0, matvec(b2, v0))
    assert val.b == Fr(-536481792000)                  # weld = t^2 (twist-twist)
