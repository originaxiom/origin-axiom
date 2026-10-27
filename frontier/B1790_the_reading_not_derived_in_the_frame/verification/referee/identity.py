"""Attack 2: conj(av_k(tau)) = av_k(-conj tau) for I, J and -av_K(-conj tau) for K.
(i) structural: the q-series coefficients of te.B[1] (DR) are real (I, J) / purely imaginary (K), and x(-conj tau) = conj x(tau);
(ii) numerical at 3 points; (iii) independent: DR rebuilt from mpmath jtheta + E2 + numerical d/dtau, compared with te.ev;
(iv) eps X* eps^T = X for X in {QI, QJ, QK} (so S~ = S with conjugated components)."""
import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import common as C, numpy as np, mpmath as mp
from fractions import Fraction as F
te = C.te
mp.mp.dps = 30
for name, c in zip("IJK", te.B[1]):
    re_only = all(b == 0 for (a, b) in c.d.values()); im_only = all(a == 0 for (a, b) in c.d.values())
    print("DR_%s: %d coefficients; all real %s; all imaginary %s; integer keys %s" % (name, len(c.d), re_only, im_only, all(isinstance(k, int) for k in c.d)))
def R_mp(t):
    q = mp.exp(1j * mp.pi * t)
    t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    d = t2 * t3 * t4
    return [-(t2 ** 2) / d, -(t4 ** 2) / d, 1j * t3 ** 2 / d]
def E2_mp(t):
    q = mp.exp(2j * mp.pi * t)
    return 1 - 24 * mp.nsum(lambda n: n * q ** n / (1 - q ** n), [1, mp.inf])
def DR_mp(t):
    # Serre derivative at weight -1/2: D f = q df/dq - (k/12) E2 f = (1/(2 pi i)) df/dtau + (1/24) E2 f
    e2 = E2_mp(t)
    return [mp.diff(lambda z: R_mp(z)[i], t) / (2j * mp.pi) + e2 * R_mp(t)[i] / 24 for i in range(3)]
pts = [mp.mpc(0.3, 3.0), mp.mpc(0.27, 3.04), mp.mpc(-0.41, 1.7)]
for t in pts:
    tm = -mp.conj(t)
    a = [te.ev(c, t) for c in te.B[1]]; am = [te.ev(c, tm) for c in te.B[1]]
    devs = [abs(mp.conj(a[0]) - am[0]) / abs(a[0]), abs(mp.conj(a[1]) - am[1]) / abs(a[1]), abs(mp.conj(a[2]) + am[2]) / abs(a[2])]
    devK_plus = abs(mp.conj(a[2]) - am[2]) / abs(a[2])
    ind = DR_mp(t)
    dind = max(abs(ind[i] - a[i]) / abs(a[i]) for i in range(3))
    indm = DR_mp(tm)
    dind_id = max(abs(mp.conj(ind[0]) - indm[0]) / abs(ind[0]), abs(mp.conj(ind[1]) - indm[1]) / abs(ind[1]), abs(mp.conj(ind[2]) + indm[2]) / abs(ind[2]))
    print("tau", mp.nstr(t, 4), "| identity rel dev (I, J, K-negated):", [mp.nstr(d, 3) for d in devs], "| K without negation:", mp.nstr(devK_plus, 3),
          "| te.ev vs independent jtheta DR:", mp.nstr(dind, 3), "| identity on independent DR:", mp.nstr(dind_id, 3))
for nm, X in (("QI", C.QI), ("QJ", C.QJ), ("QK", C.QK)):
    print("eps %s* eps^T - %s: %.1e" % (nm, nm, np.max(np.abs(C.EPS @ np.conj(X) @ C.EPS.T - X))))
# K negation as a rotation: diag(1,1,-1) = -(rotation by pi about K); check -QK S QK^-1 negates only K
a = np.array([0.3 + 0.2j, -1.1 + 0.5j, 0.7 - 0.4j]); S = C.quat(a)
lam = C.quat(np.array([a[0], a[1], -a[2]])); rot = -(C.QK @ S @ np.linalg.inv(C.QK))
print("S with K negated == -(QK S QK^-1):", np.max(np.abs(lam - rot)))
