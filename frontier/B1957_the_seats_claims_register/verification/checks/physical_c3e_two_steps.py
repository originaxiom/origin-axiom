"""B1957: the physical lane's P-C3e, the nonlinear part (CUSP_GAUGE_INVERSE..., sections 3 to 5, equations (4) to (9);
BALANCED_FORM_TANGENTS..., equations (2), (3), (4), (7)): the algebra and the two implicit-function steps, tested by main
in a finite-dimensional model with the same structure.  Data-free.

WHAT THIS IS AND IS NOT.  The lane's argument is: a raw family that satisfies the holomorphic equations exactly; a
complexified gauge transformation exp(-psi), psi orthogonal to the one unbroken generator Q, solves the moment equation
off Q (first implicit-function step, by the inverse of P_v = 2 k^dagger k off Q); the one remaining moment, along Q, is
t^2 e_Q (1 - rho^2) + higher, and is solved by the relative amplitude rho (second step).  Here the same scheme is run
where every hypothesis holds trivially: gauge group SU(2) x U(1)_B x U(1)_Q on six doublets; a background of four doublets neutral under Q
(e1 and e2 with B = +1 and -1, and (e1 +- e2)/sqrt 2 with B = 0) has zero moment, breaks SU(2) x U(1)_B completely and
keeps Q; two charged directions p (Q = +1, B = 2) and r (Q = -1, B = -1), deliberately unlike each other.  It tests the
signs, the orders in the amplitude, the coefficients and the independence of the auxiliary projection.  It does NOT
test the lane's analysis on the cusp (its equation (3), the weighted spaces, analyticity there): that stays conditional.
 T1  mu2 = -i[a_x, a_y] = [a, a^dagger]/2 for a = a_x + i a_y (random Hermitian parts).
 T2  d mu (I k psi) = -P_v psi with P_v = 2 k^dagger k at the background, and its kernel is Q alone.
 T3  the first step: psi(t, rho) solves the SU(2) moment; psi = O(t^2); its second coefficient is P_v^-1 of the source.
 T4  the second step: h/t^2 -> e_Q (1 - rho^2); d/d rho at rho = 1 is -2 e_Q; rho(t) -> 1.
 T5  the final point has zero moment, and is the same (up to a real gauge rotation) for two different auxiliary
     projections ('bumps'); the Q vector's mass is 4 e_Q^2 t^2 + O(t^3).
 T6  the second-order correction beta = I k P^-1(source) cancels the quadratic moment off Q; the Q moment is\n     e_Q eps^2 (|P|^2 - |R|^2), zero only when the two norms balance."""
import functools, warnings
import numpy as np
from scipy.linalg import expm
from scipy.optimize import root, brentq
warnings.simplefilter("ignore")
print = functools.partial(print, flush=True)
rng = np.random.default_rng(1957); SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
herm = lambda c: sum(ci * s for ci, s in zip(c[:3], SIG))                  # the SU(2) part of a parameter (3 reals); c[3] is the U(1)_B part
e1, e2 = np.array([1, 0], complex), np.array([0, 1], complex); BCH = (1, -1, 0, 0, 2, -1); QCH = (0, 0, 0, 0, 1, -1); EQ = 1.0
unit = lambda v: v / np.linalg.norm(v); p = unit(rng.normal(size=2) + 1j * rng.normal(size=2)); r = unit(rng.normal(size=2) + 1j * rng.normal(size=2))
X0 = [e1, e2, (e1 + e2) / np.sqrt(2), (e1 - e2) / np.sqrt(2), 0 * p, 0 * r]


def moment(X):
    """(the SU(2) x U(1)_B moment as 4 reals, the Q moment) of six doublets X"""
    M = sum(np.outer(f, f.conj()) for f in X); return np.array([np.trace(M @ s).real for s in SIG] + [sum(b * np.vdot(f, f).real for b, f in zip(BCH, X))]), EQ * sum(q * np.vdot(f, f).real for q, f in zip(QCH, X))


def act(c, X): return [expm(-(herm(c) + c[3] * b * np.eye(2))) @ f for b, f in zip(BCH, X)]
raw = lambda t, rho: X0[:4] + [t * p, t * rho * r]


def first_step(t, rho, w=np.zeros(4)):
    """psi orthogonal to Q with (Pi m) = 0, Pi f = f - phi <v_Q, f>, phi = v_Q + w (w off Q: the 'bump')"""
    return root(lambda c: (lambda m4, mq: m4 - w * mq)(*moment(act(c, raw(t, rho)))), np.zeros(4), tol=1e-14).x


def h(t, rho, w=np.zeros(4)): return moment(act(first_step(t, rho, w), raw(t, rho)))[1]


if __name__ == "__main__":
    ax, ay = (lambda A: (A + A.conj().T) / 2)(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))), (lambda A: (A + A.conj().T) / 2)(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))); a = ax + 1j * ay
    print("T1: |(-i[a_x, a_y]) - [a, a^dagger]/2| = %.1e" % np.abs(-1j * (ax @ ay - ay @ ax) - (a @ a.conj().T - a.conj().T @ a) / 2).max())
    eps = 1e-6; J = np.zeros((4, 4)); gen = lambda j, f, b: (1j * SIG[j] @ f) if j < 3 else 1j * b * f
    for j in range(4):
        d = np.zeros(4); d[j] = eps; J[:, j] = (moment(act(d, X0))[0] - moment(act(-d, X0))[0]) / (2 * eps)
    kk = np.array([[sum(np.vdot(gen(i, f, b), gen(j, f, b)).real for b, f in zip(BCH, X0)) for j in range(4)] for i in range(4)])
    print("T2: at the background, d mu(I k psi) = -P psi: |P - 2 k^dagger k| = %.1e (P by numerical derivative; its eigenvalues %s, all positive: nothing off Q is unbroken); |k_Q|^2 = %.1f, so Q is the whole kernel" % (np.abs(-J - 2 * kk).max(), np.round(np.linalg.eigvalsh((-J - J.T) / 2), 4).tolist(), sum(q * q * np.vdot(f, f).real for q, f in zip(QCH, X0))))
    ts = [0.2, 0.1, 0.05, 0.025]; ps = [np.linalg.norm(first_step(t, 1.0)) for t in ts]; src = moment(raw(1.0, 1.0))[0] - moment(X0)[0]; pred = np.linalg.solve(-J, src)
    print("T3: |psi(t, 1)| at t = %s: %s; ratios %s (4 means O(t^2)); psi/t^2 against P^-1 of the quadratic source: %.1e at t = 0.025, %.1e at t = 0.0125 (falling as t^2)" % (ts, ["%.2e" % x for x in ps], ["%.3f" % (ps[i] / ps[i + 1]) for i in range(3)], np.linalg.norm(first_step(0.025, 1.0) / 0.025 ** 2 - pred), np.linalg.norm(first_step(0.0125, 1.0) / 0.0125 ** 2 - pred)))
    for rho in (0.7, 1.0, 1.3):
        print("T4: rho = %.1f: h/t^2 at t = 0.1, 0.05, 0.025: %.6f, %.6f, %.6f; e_Q (1 - rho^2) = %.6f" % (rho, h(0.1, rho) / 0.01, h(0.05, rho) / 0.05 ** 2, h(0.025, rho) / 0.025 ** 2, EQ * (1 - rho * rho)))
    t = 0.01; dh = (h(t, 1 + 1e-4) - h(t, 1 - 1e-4)) / (2e-4 * t * t); print("T4: d(h/t^2)/d rho at rho = 1, t = 0.01: %.5f (the lane: -2 e_Q = %.1f)" % (dh, -2 * EQ))
    out = {}
    for name, w in (("the plain projection", np.zeros(4)), ("a skew projection", np.array([0.7, -0.4, 0.5, 0.3]))):
        for t in (0.2, 0.1, 0.05):
            rho = brentq(lambda x: h(t, x, w), 0.5, 1.5, xtol=1e-15); X = act(first_step(t, rho, w), raw(t, rho)); m4, mq = moment(X)
            inv = sorted(np.linalg.svd(np.column_stack(X), compute_uv=False).tolist()) + [np.vdot(f, f).real for f in X]                      # unchanged by a real gauge rotation
            out[(name, t)] = (rho, np.abs(m4).max(), abs(mq), inv, 2 * EQ ** 2 * (np.vdot(X[4], X[4]).real + np.vdot(X[5], X[5]).real))
    for (name, t), (rho, a4, aq, inv, mass) in out.items(): print("T5: %s, t = %.2f: rho(t) = %.6f, (rho - 1)/t^2 = %+.4f; moments left %.1e and %.1e; the Q vector's mass^2/(4 e_Q^2 t^2) = %.5f" % (name, t, rho, (rho - 1) / t ** 2, a4, aq, mass / (4 * EQ ** 2 * t * t)))
    print("T5: the two projections give the same final point up to a real gauge rotation: invariants differ by %s" % ", ".join("%.1e (t = %.2f)" % (np.abs(np.array(out[("the plain projection", t)][3]) - np.array(out[("a skew projection", t)][3])).max(), t) for t in (0.2, 0.1, 0.05)))
    for lab, rr in (("balanced, |P| = |R|", 1.0), ("unbalanced, |R| = 0.6 |P|", 0.6)):
        res = []
        for e in (0.1, 0.05, 0.025):
            s4 = moment(X0[:4] + [p, rr * r])[0] - moment(X0)[0]; psi = np.linalg.solve(2 * kk, s4); beta = [-(herm(psi) + psi[3] * b * np.eye(2)) @ f for b, f in zip(BCH, X0)]             # beta = I k psi, the second-order correction
            X = [x0 + e * a1 + e * e * bb for x0, a1, bb in zip(X0, [0 * e1] * 4 + [p, rr * r], beta)]; m4, mq = moment(X); res.append((np.abs(m4).max(), abs(mq)))
        print("T6: %s: after the second-order correction beta = I k P^-1(source), the moment off Q at eps = 0.1, 0.05, 0.025: %s (the quadratic moment is cancelled; in this model the later terms vanish too, by the SU(2) structure, so this shows the cancellation and not the lane's order eps^3); the Q moment: %s (e_Q eps^2 (|P|^2 - |R|^2) = %.2e at eps = 0.025)" % (lab, ["%.1e" % x[0] for x in res], ["%.1e" % x[1] for x in res], EQ * 0.025 ** 2 * (1 - rr * rr)))
