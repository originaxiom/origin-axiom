#!/usr/bin/env python3
"""R29c — EXACT cusp shapes of the 112 members from the exact Q(sqrt-3) tetrahedron shapes (R29b).

Neumann–Zagier: at the complete structure the deformation variety is smooth of dimension c (= #cusps);
writing u_i = log H(meridian_i), v_i = log H(longitude_i), one has  v_i = tau_i u_i + O(u^2)  with tau_i
the cusp modulus (longitude/meridian translation ratio).  With snappy's 'rect' cusp rows the derivative
ratio comes out as conj(tau) relative to snappy's `cusp_info()['shape']` orientation; the conjugate is
taken and the result is compared STRICTLY (same complex number, 1e-9) with snappy's numerical value.

So tau_k is exact linear algebra over Q(sqrt-3):  solve  J_edge . dz = 0,  J_{m_i} . dz = delta_{ik}
for dz (the Jacobian rows of the log gluing equations, entries a_i/w_i - b_i/(1-w_i), are in Q(sqrt-3)
because the shapes w_i are), then  tau_k = J_{l_k} . dz.   Everything is done on Fraction pairs; the
numerical snappy cusp shape is printed alongside as a convention cross-check only.
Output: r29_exact_cusp_shapes.json / .txt
"""
import json, os, sys, warnings
warnings.filterwarnings('ignore')
from fractions import Fraction
import snappy, mpmath as mp
import r29_krawczyk as r
from r29_exact_shapes import qmul, qinv, fit, as_mpc, S3

HERE = os.path.dirname(os.path.abspath(__file__))
ZERO, ONE = (Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))

def qsub(x, y): return (x[0] - y[0], x[1] - y[1])
def qadd(x, y): return (x[0] + y[0], x[1] + y[1])
def qscal(s, x): return (s * x[0], s * x[1])

def solve(A, rhs):
    """Gaussian elimination over Q(sqrt-3) for A dz = rhs (A may be tall; consistent system assumed).
    Returns dz or raises if the system is inconsistent / singular."""
    m, n = len(A), len(A[0])
    M = [row[:] + [b] for row, b in zip(A, rhs)]
    piv_cols, rrow = [], 0
    for col in range(n):
        p = next((i for i in range(rrow, m) if M[i][col] != ZERO), None)
        if p is None: continue
        M[rrow], M[p] = M[p], M[rrow]
        inv = qinv(M[rrow][col])
        M[rrow] = [qmul(inv, x) for x in M[rrow]]
        for i in range(m):
            if i != rrow and M[i][col] != ZERO:
                f = M[i][col]
                M[i] = [qsub(x, qmul(f, y)) for x, y in zip(M[i], M[rrow])]
        piv_cols.append(col); rrow += 1
        if rrow == m: break
    for i in range(rrow, m):
        if M[i][n] != ZERO: raise ValueError('inconsistent')
    if len(piv_cols) != n: raise ValueError('singular: rank %d < %d' % (len(piv_cols), n))
    return [M[i][n] for i in range(n)]

def cusp_shapes_exact(name):
    M = snappy.Manifold(name)
    H = M.high_precision()
    z0 = [mp.mpc(str(s.real()).replace(' ', ''), str(s.imag()).replace(' ', '')) for s in H.tetrahedra_shapes('rect')]
    W = [fit(z) for z in z0]
    rows = r.logform_rows(M)
    n, nc = M.num_tetrahedra(), M.num_cusps()
    n_edge = len(rows) - 2 * nc
    def jrow(row):
        a, b, _ = row
        out = []
        for ai, bi, w in zip(a, b, W):
            t = ZERO
            if ai: t = qadd(t, qscal(Fraction(ai), qinv(w)))
            if bi: t = qsub(t, qscal(Fraction(bi), qinv((1 - w[0], -w[1]))))
            out.append(t)
        return out
    J_edge = [jrow(rows[j]) for j in range(n_edge)]
    J_m = [jrow(rows[n_edge + 2 * i]) for i in range(nc)]
    J_l = [jrow(rows[n_edge + 2 * i + 1]) for i in range(nc)]
    taus = []
    for k in range(nc):
        A = J_edge + J_m
        rhs = [ZERO] * n_edge + [ONE if i == k else ZERO for i in range(nc)]
        dz = solve(A, rhs)
        tau = ZERO
        for c, d in zip(J_l[k], dz): tau = qadd(tau, qmul(c, d))
        # the 'rect' cusp rows give v/u = conj(tau) for snappy's cusp orientation (checked on every cusp of
        # the family, including the non-real ones like m003's 1/2 + (1/2)sqrt(-3)); take the conjugate
        taus.append((tau[0], -tau[1]))
    num = [complex(ci['shape']) for ci in M.cusp_info()]
    return W, taus, num

if __name__ == '__main__':
    names = sys.argv[1:] or json.load(open(HERE + '/../R23_carriers_quine/sweep_candidates.json'))['candidates']
    out, carriers = [], []
    for nm in names:
        try:
            W, taus, num = cusp_shapes_exact(nm)
            info = []
            for k, (t, z) in enumerate(zip(taus, num)):
                tv = complex(as_mpc(t))
                agree = abs(tv - z) < 1e-9     # strict: same complex number as snappy's cusp_info shape
                is_carrier = (t == (Fraction(0), Fraction(2)))
                if is_carrier: carriers.append((nm, k))
                info.append(dict(cusp=k, tau_exact=[str(t[0]), str(t[1])], tau_snappy=str(z), convention_agrees=bool(agree), is_2sqrt3i=is_carrier))
            o = dict(name=nm, cusps=info, all_conventions_agree=all(c['convention_agrees'] for c in info))
        except Exception as e:
            o = dict(name=nm, error='EXC %s: %s' % (type(e).__name__, str(e)[:200]))
        out.append(o)
        print(nm, ' '.join('[%d] tau=%s+%s*sqrt(-3) num=%s ok=%s%s' % (c['cusp'], c['tau_exact'][0], c['tau_exact'][1], c['tau_snappy'][:22], c['convention_agrees'], ' <== 2sqrt3i' if c['is_2sqrt3i'] else '') for c in o.get('cusps', [])) or o.get('error'), flush=True)
    json.dump(dict(rows=out, carriers=carriers), open(HERE + '/r29_exact_cusp_shapes.json', 'w'), indent=1)
    print('== exact 2sqrt(3)i carriers (name, cusp): %s ==' % carriers)
    print('== all snappy conventions agree: %s ==' % all(o.get('all_conventions_agree') for o in out))
