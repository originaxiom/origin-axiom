"""High-precision certificate that SL5 o=5 m=1 has [A,B]=mu^2 (k=2), mu=A^-1 t.
Stable damped Gauss-Newton (qr_solve LS step + accept-if-better) so the polish REFINES the
float64 seed instead of jumping to another component. Prints relation-residual AND ||[A,B]-mu^k||
each step so they must track. Verify-don't-trust: a certificate must converge, not just exist."""
import numpy as np, mpmath as mp, sys
mp.mp.dps = 60
sys.path.insert(0, '.')
from gauge_newton import make_A, newton_t, irred, exponent

def to_mp(M):
    return mp.matrix([[mp.mpc(complex(M[i, j])) for j in range(M.shape[1])] for i in range(M.shape[0])])

def resid_mp(t, A, Ai, Ai2, n, gfix):
    R = t*Ai2*t*A - Ai*t*A*t
    rows = [R[i, j] for i in range(n) for j in range(n)]
    rows.append(mp.det(t) - 1)
    for i in gfix:
        rows.append(t[i, i+1] - 1)
    return mp.matrix(rows)

def commstuff(t, A, Ai, Ai2):
    B = Ai2*t*A*(t**-1)
    comm = A*B*Ai*(B**-1)
    mu = Ai*t
    return comm, mu

n, o, exps = 5, 5, [0, 1, 2, 3, 4]
Af, Aif, Ai2f = make_A(o, exps)
gfix = list(range(n-1))
best = None  # (err, t, relresid)
for rs in range(30):
    rng = np.random.default_rng(rs)
    for s in range(150):
        t, r = newton_t(Af, Aif, Ai2f, n, gfix, rng)
        if t is not None and r < 1e-10 and abs(np.linalg.det(t)) > 1e-3 and np.linalg.cond(t) < 1e5:
            B = Ai2f@t@Af@np.linalg.inv(t)
            if irred(Af, B, n) == n*n and np.max(np.abs(Aif@t - t)) > 1e-3:
                sgn, k, err = exponent(Af, B, t)
                if (sgn, k) == (1, 2) and (best is None or err < best[0]):
                    best = (err, t.copy(), r)
    if best is not None and best[0] < 1e-9:
        break
assert best is not None, "no float seed with (s,k)=(1,2)"
t0 = best[1]
print("float64 seed: ||[A,B]-mu^2||=%.2e  relresid=%.2e  ||mu-t||=%.3f" %
      (best[0], best[2], np.max(np.abs(Aif@t0 - t0))))

z = mp.exp(2j*mp.pi/o); d = [z**e for e in exps]
A = mp.diag(d); Ai = mp.diag([1/x for x in d]); Ai2 = mp.diag([1/x**2 for x in d])
N = n*n
t = to_mp(t0)

def flat(t): return [t[i, j] for i in range(n) for j in range(n)]
def unflat(f): return mp.matrix([[f[i*n+j] for j in range(n)] for i in range(n)])

g = resid_mp(t, A, Ai, Ai2, n, gfix)
cur = mp.norm(g, mp.inf)
for it in range(80):
    if cur < mp.mpf(10)**(-50):
        break
    h = mp.mpf(10)**(-30)
    f0 = flat(t)
    J = mp.zeros(g.rows, N)
    for kk in range(N):
        fp = f0[:]; fp[kk] += h
        gp = resid_mp(unflat(fp), A, Ai, Ai2, n, gfix)
        for r_ in range(g.rows):
            J[r_, kk] = (gp[r_] - g[r_]) / h
    JhJ = J.H * J
    dx = mp.lu_solve(JhJ + (mp.mpf(10)**(-45))*mp.eye(N), J.H * g)  # LM-damped normal eqs
    lam = mp.mpf(1)
    accepted = False
    for _ in range(40):
        fn = [f0[kk] - lam*dx[kk] for kk in range(N)]
        tn = unflat(fn)
        gn = resid_mp(tn, A, Ai, Ai2, n, gfix)
        if mp.norm(gn, mp.inf) < cur:
            t = tn; g = gn; cur = mp.norm(gn, mp.inf); accepted = True
            break
        lam /= 2
    comm, mu = commstuff(t, A, Ai, Ai2)
    err2 = mp.norm(comm - mu**2, mp.inf)
    if it % 5 == 0:
        print("iter %2d: relresid=%s  ||[A,B]-mu^2||=%s  ||mu-t||=%s" %
              (it, mp.nstr(cur, 4), mp.nstr(err2, 4), mp.nstr(mp.norm(mu-t, mp.inf), 4)))
    if not accepted:
        print("  (no decrease; stop)"); break

comm, mu = commstuff(t, A, Ai, Ai2)
print("\n=== FINAL CERTIFICATE (dps=%d) ===" % mp.mp.dps)
print("relation residual         :", mp.nstr(mp.norm(resid_mp(t, A, Ai, Ai2, n, gfix), mp.inf), 5))
print("||mu - t|| (nondegeneracy):", mp.nstr(mp.norm(mu-t, mp.inf), 5))
for k in (1, 2, 3):
    print("||[A,B] - mu^%d||          : %s" % (k, mp.nstr(mp.norm(comm-mu**k, mp.inf), 5)))
c = (comm * (mu**-2))
print("[A,B]*mu^-2 diag (=c):", [mp.nstr(c[i, i], 6) for i in range(n)])
print("[A,B]*mu^-2 max offdiag:", mp.nstr(max(abs(c[i, j]) for i in range(n) for j in range(n) if i != j), 5))
