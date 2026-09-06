#!/usr/bin/env python3
"""JOIN 1 q1 on the CUSPED object in the theta-odd frame -- high precision (python-flint ball
arithmetic at 400 bits for the Newton search, mpmath at 60 digits for the ranks).

The 27 of the geometric holonomy is numerically hostile in double precision (Sym^16 of a
loxodromic-free but non-unitary holonomy: intermediate products span ~1e11), so every rank here
is decided at 60 digits with a printed pivot gap.

THE BOUND (theorem): with the lemma N(V) = rank(res_V) - h0(dM;V) and rank(res_V) + rank(res_V*)
= h1(dM;V) (Poincare-Lefschetz complementarity),   -h0(dM;V) <= N(V) <= h0(dM;V*).
Near the geometric point h1(M;27_s) <= 3 by semicontinuity, so N(27_s) <= min(3 - h0, h0) <= 1.

THE COMPUTATION:
  (0) the geometric point, exact: h1 = 3 = 3, rank(res) = 3 = h0(dM): N = 0 (self-dual);
  (a) an exact cocycle class in H1(M; V8) (the hv8 slot's block, the theta-odd direction),
      a Newton search from rho_0 twisted by it, converging to a genuine E6(C) representation
      rho_s of pi_1(m004) (relator residual < 1e-60), NOT self-dual (tr rho(g) != tr rho(g^-1)),
      and its 27 / 27bar cohomology, cusp data, restriction ranks and N;
  (b) the fixed-vector locus: an augmented Newton search for a nearby theta-odd representation
      whose cusp holonomy keeps a common fixed vector (mu v = lambda v = v), and N there.
"""
from __future__ import annotations
import os, sys, time
from fractions import Fraction as F
import numpy as np
import mpmath as mp
try:
    from flint import acb_mat, acb, arb, fmpq, ctx        # python-flint (ball arithmetic); pip install python-flint
except ImportError as _ex:                                # the exact stage (cusped_bound.py) needs no flint
    raise SystemExit("this stage needs python-flint: pip install python-flint  (%s)" % _ex)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1265_spectrum_law_rebuilt', 'verification'))
import e6_instrument as E
import spectrum_law as S

ctx.prec = 600
mp.mp.dps = 60
Qw = E.Qw
OMEGA_ACB = (acb(-1) + acb(0, 1) * acb(3).sqrt()) / 2
U_ACB = 1 + OMEGA_ACB


# ---------------------------------------------------------------- conversions
def q2acb(x):
    if isinstance(x, Qw):
        return acb(fmpq(x.x.numerator, x.x.denominator)) + acb(fmpq(x.y.numerator, x.y.denominator)) * OMEGA_ACB
    x = F(x)
    return acb(fmpq(x.numerator, x.denominator))


def to_acb(M):
    return acb_mat([[q2acb(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])])


def acb2mp(z):
    return mp.mpc(mp.mpf(z.real.mid().str(70, radius=False)), mp.mpf(z.imag.mid().str(70, radius=False)))


def mat2mp(M):
    return mp.matrix([[acb2mp(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())])


def eye(n):
    return acb_mat(n, n, 1)


def frob(M):
    s = arb(0)
    for i in range(M.nrows()):
        for j in range(M.ncols()):
            a = abs(M[i, j])
            s += a * a
    return s.sqrt()


def hstack(*Ms):
    n = Ms[0].nrows()
    rows = []
    for i in range(n):
        row = []
        for M in Ms:
            row += [M[i, j] for j in range(M.ncols())]
        rows.append(row)
    return acb_mat(rows)


def vstack(*Ms):
    rows = []
    for M in Ms:
        rows += [[M[i, j] for j in range(M.ncols())] for i in range(M.nrows())]
    return acb_mat(rows)


def flat(M):
    return [M[i, j] for i in range(M.nrows()) for j in range(M.ncols())]


def hermitian(M):
    return M.transpose().conjugate()


# ---------------------------------------------------------------- words
REL, LONG = S.REL, S.LONG


def ev(mats, invs, word, n):
    out = eye(n)
    for L in word:
        out = out * (mats[L] if L > 0 else invs[-L])
    return out


def fox(mats, invs, word, g, n):
    acc = acb_mat(n, n)
    cur = eye(n)
    for L in word:
        if L > 0:
            if L == g:
                acc = acc + cur
            cur = cur * mats[L]
        else:
            cur = cur * invs[-L]
            if -L == g:
                acc = acc - cur
    return acc


def adfox_apply(mats, invs, word, g, Y, n):
    """sum over occurrences of x_g in `word` of (sign) P Y P^-1  -- the derivative of the word
    under x_g -> exp(eps Y) x_g, divided on the right by the word's value."""
    acc = acb_mat(n, n)
    cur = eye(n)
    curinv = eye(n)
    for L in word:
        if L > 0:
            if L == g:
                acc = acc + cur * Y * curinv
            cur = cur * mats[L]
            curinv = invs[L] * curinv
        else:
            cur = cur * invs[-L]
            curinv = mats[-L] * curinv
            if -L == g:
                acc = acc - cur * Y * curinv
    return acc


def cocycle_value(mats, invs, word, fa, fb, n):
    val = acb_mat(n, 1)
    cur = eye(n)
    fdict = {1: fa, 2: fb}
    for L in word:
        if L > 0:
            val = val + cur * fdict[L]
            cur = cur * mats[L]
        else:
            cur = cur * invs[-L]
            val = val - cur * fdict[-L]
    return val


# ---------------------------------------------------------------- mp ranks / nullspaces
def mp_rank(M, tol=mp.mpf('1e-30'), name=""):
    """Rank of an mp matrix by pivoted elimination; prints the pivot gap."""
    A = M.copy()
    n, m = A.rows, A.cols
    scale = max([abs(A[i, j]) for i in range(n) for j in range(m)] + [mp.mpf(1)])
    r = 0
    pivots = []
    rejected = mp.mpf(0)
    for c in range(m):
        piv, best = None, mp.mpf(0)
        for i in range(r, n):
            if abs(A[i, c]) > best:
                best, piv = abs(A[i, c]), i
        if piv is None or best <= tol * scale:
            rejected = max(rejected, best / scale)
            continue
        pivots.append(best / scale)
        if piv != r:
            for j in range(m):
                A[r, j], A[piv, j] = A[piv, j], A[r, j]
        pv = A[r, c]
        for j in range(m):
            A[r, j] = A[r, j] / pv
        for i in range(n):
            if i != r and A[i, c] != 0:
                fct = A[i, c]
                for j in range(m):
                    A[i, j] = A[i, j] - fct * A[r, j]
        r += 1
        if r == n:
            break
    if name:
        smallest = min(pivots) if pivots else None
        print(f"      [{name}] rank {r} of ({n}x{m}); smallest accepted pivot/scale = {mp.nstr(smallest, 3) if smallest else '-'}; largest rejected = {mp.nstr(rejected, 3)}")
    return r


def mp_nullspace(M, tol=mp.mpf('1e-30')):
    """Basis of the (right) nullspace of an mp matrix by RREF with thresholding."""
    A = M.copy()
    n, m = A.rows, A.cols
    scale = max([abs(A[i, j]) for i in range(n) for j in range(m)] + [mp.mpf(1)])
    r = 0
    pivcols = []
    for c in range(m):
        piv, best = None, mp.mpf(0)
        for i in range(r, n):
            if abs(A[i, c]) > best:
                best, piv = abs(A[i, c]), i
        if piv is None or best <= tol * scale:
            continue
        if piv != r:
            for j in range(m):
                A[r, j], A[piv, j] = A[piv, j], A[r, j]
        pv = A[r, c]
        for j in range(m):
            A[r, j] = A[r, j] / pv
        for i in range(n):
            if i != r and A[i, c] != 0:
                fct = A[i, c]
                for j in range(m):
                    A[i, j] = A[i, j] - fct * A[r, j]
        pivcols.append(c)
        r += 1
        if r == n:
            break
    free = [c for c in range(m) if c not in pivcols]
    basis = []
    for fcol in free:
        v = mp.matrix(m, 1)
        v[fcol] = 1
        for i, pc in enumerate(pivcols):
            v[pc] = -A[i, fcol]
        basis.append(v)
    return basis


def cohomology_report(mats, invs, n, label):
    """h0, h1 of M; h0(dM), h1(dM); rank(res); N-lemma value.  All ranks at 60 digits."""
    I = eye(n)
    d0 = mat2mp(vstack(mats[1] - I, mats[2] - I))
    d1 = mat2mp(hstack(fox(mats, invs, REL, 1, n), fox(mats, invs, REL, 2, n)))
    r0 = mp_rank(d0, name=f"{label} d0")
    r1 = mp_rank(d1, name=f"{label} d1")
    h0, h1 = n - r0, (2 * n - r1) - r0
    mu, lam = mats[1], ev(mats, invs, LONG, n)
    comm = frob(mu * lam - lam * mu)
    fixed = mat2mp(vstack(mu - I, lam - I))
    h0t = n - mp_rank(fixed, name=f"{label} cusp fixed")
    Zt = mat2mp(hstack(lam - I, -(mu - I)))
    Bt = mat2mp(vstack(mu - I, lam - I))
    rZ = mp_rank(Zt, name=f"{label} Z1(T2)")
    rB = mp_rank(Bt, name=f"{label} B1(T2)")
    h1t = (2 * n - rZ) - rB
    kern = mp_nullspace(d1)
    cols = []
    for v in kern:
        fa = acb_mat([[acb(arb(str(v[i].real)), arb(str(v[i].imag)))] for i in range(n)])
        fb = acb_mat([[acb(arb(str(v[n + i].real)), arb(str(v[n + i].imag)))] for i in range(n)])
        val = vstack(cocycle_value(mats, invs, [1], fa, fb, n), cocycle_value(mats, invs, LONG, fa, fb, n))
        cols.append([acb2mp(val[i, 0]) for i in range(2 * n)])
    R = mp.matrix(cols).T if cols else mp.matrix(2 * n, 0)
    RB = mp.matrix(2 * n, R.cols + Bt.cols)
    for i in range(2 * n):
        for j in range(R.cols):
            RB[i, j] = R[i, j]
        for j in range(Bt.cols):
            RB[i, R.cols + j] = Bt[i, j]
    rank_res = mp_rank(RB, name=f"{label} res+B") - rB
    N = rank_res - h0t
    print(f"    {label}: h0(M) = {h0}, h1(M) = {h1}, h0(dM) = {h0t}, h1(dM) = {h1t}, rank(res) = {rank_res}, [mu,lambda] = {float(frob(mu*lam-lam*mu).mid()):.1e}  =>  N = rank(res) - h0(dM) = {N}")
    return dict(h0=h0, h1=h1, h0t=h0t, h1t=h1t, rank_res=rank_res, N=N)


def dual_of(mats, invs):
    return {g: invs[g].transpose() for g in mats}, {g: mats[g].transpose() for g in mats}


def trace(M):
    return sum((M[i, i] for i in range(M.nrows())), acb(0))


def selfduality_trace_test(mats, invs, n):
    """tr rho(w) - tr rho(w^-1) for a few words: any nonzero => NOT self-dual."""
    out = []
    for word in ([1], [2], [1, 2], [1, 1, 2], [1, 2, -1, -2], [2, 1, 1]):
        M = ev(mats, invs, word, n)
        Mi = ev(mats, invs, [-x for x in reversed(word)], n)
        out.append(abs(trace(M) - trace(Mi)))
    return out


# ---------------------------------------------------------------- setup: the geometric point, exact
e, h, f = E.principal_sl2()
HV = E.hw_vectors(e)
# The Chevalley basis is badly scaled for floating point (the principal f carries the coefficients
# of 2 rho^vee, up to 42): rescale every 27x27 matrix by the exact similarity D = diag(5^{h/2}),
# which sends e -> 5 e and f -> f/5.  A similarity changes nothing below; it tames exp().
_HD = [int(E.rho(h)[i, i]) // 2 for i in range(27)]


def rescale(M):
    out = M.copy()
    for i in range(27):
        for j in range(27):
            k = _HD[i] - _HD[j]
            out[i, j] = M[i, j] * (F(5) ** k)
    return out


REPA = [to_acb(rescale(E.REP[k])) for k in range(78)]
rep0 = S.build_rep(e, f)
A0, B0, A0i, B0i = (to_acb(rescale(rep0.M[1])), to_acb(rescale(rep0.M[2])),
                    to_acb(rescale(rep0.I[1])), to_acb(rescale(rep0.I[2])))
M0, M0i = {1: A0, 2: B0}, {1: A0i, 2: B0i}
print(f"    [rescaled 27: |A0| = {frob(A0).str(3)}, |B0| = {frob(B0).str(3)}]")


def _gram_schmidt(mats):
    """Orthonormalize (Frobenius inner product) a list of acb_mat -- an e6 basis on which the
    Newton unknowns are well scaled."""
    out = []
    for M in mats:
        V = M
        for Q in out:
            ip = sum((Q[i, j].conjugate() * V[i, j] for i in range(27) for j in range(27)), acb(0))
            V = V - Q * ip
        nv = frob(V)
        out.append(V * (1 / nv))
    return out


REPA_ON = _gram_schmidt(REPA)          # 78 orthonormal matrices spanning e6 in gl(27)


def e6_matrix(coeffs):
    """sum_k c_k REPA[k] for acb coefficients."""
    out = acb_mat(27, 27)
    for k, c in enumerate(coeffs):
        if c != 0:
            out = out + REPA[k] * c
    return out


# ---------------------------------------------------------------- the exact V8 cocycle class
def block_cocycle_exact(m=4):
    """An exact cocycle (Z_a, Z_b) in Z^1(M; V_{2m}) not a coboundary, as e6 coefficient vectors
    (over Q(omega)).  V_{2m} = span{ad(f)^k hv_{2m}}; Ad(rho0(a)) = exp(ad e), Ad(rho0(b)) = exp(u ad f)."""
    # block basis in e6 coordinates (exact rationals)
    v = HV[2 * m]
    basis = [v]
    for k in range(2 * m):
        v = E.br(f, v)
        basis.append(v)
    d = len(basis)
    import sympy as sp
    Bm = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in b] for b in basis]).T   # 78 x d
    # ad e, ad f restricted to the block: solve Bm X = ad(y) Bm
    def restrict(y):
        img = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in E.br(y, b)] for b in basis]).T
        X = sp.zeros(d, d)
        sol = Bm.gauss_jordan_solve(img)[0]
        return sol
    ade = restrict(e)
    adf = restrict(f)
    # exact exponentials over Q(omega) as Qw matrices
    def qwm(M, c):
        out = E.qw_zeros(d)
        for i in range(d):
            for j in range(d):
                x = sp.Rational(M[i, j])
                out[i, j] = Qw(F(int(x.p), int(x.q))) * c
        return out
    Aa = E.qw_expm_nilpotent(qwm(ade, E.ONE))
    Aai = E.qw_expm_nilpotent(qwm(ade, Qw(-1)))
    Bb = E.qw_expm_nilpotent(qwm(adf, E.U_RILEY))
    Bbi = E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))
    R = S.Rep({1: Aa, 2: Bb}, {1: Aai, 2: Bbi})
    S.check_rep(R, [1, 2], [REL])
    d1 = np.hstack([R.fox(REL, 1), R.fox(REL, 2)])          # d x 2d over Q(omega)
    # exact nullspace over Q(omega) by elimination
    A = [[d1[i, j] for j in range(2 * d)] for i in range(d)]
    n, mm = d, 2 * d
    r = 0
    pivcols = []
    for c in range(mm):
        piv = next((i for i in range(r, n) if not A[i][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                fct = A[i][c]
                A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        pivcols.append(c)
        r += 1
    free = [c for c in range(mm) if c not in pivcols]
    kern = []
    for fc in free:
        vct = [E.ZERO] * mm
        vct[fc] = E.ONE
        for i, pc in enumerate(pivcols):
            vct[pc] = -A[i][fc]
        kern.append(vct)
    # coboundaries ((Aa-1)w, (Bb-1)w)
    I = E.qw_eye(d)
    cob = np.vstack([Aa - I, Bb - I])                         # 2d x d
    rB = S.exact_rank_qw(cob)
    print(f"    block V{2*m}: dim Z1 = {len(kern)}, dim B1 = {rB}, h1 = {len(kern) - rB}")
    # pick a kernel vector not in the coboundary span: rank test
    for vct in kern:
        test = np.hstack([cob, np.array([[x] for x in vct], dtype=object)])
        if S.exact_rank_qw(test) > rB:
            za, zb = vct[:d], vct[d:]
            break
    Za = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * za[i] for i in range(d)), E.ZERO) for k in range(78)]
    Zb = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * zb[i] for i in range(d)), E.ZERO) for k in range(78)]
    return Za, Zb


# ---------------------------------------------------------------- Newton (multiplicative updates)
def newton(mats, invs, extra=None, iters=40, mu=None, verbose=True, target=mp.mpf('1e-60')):
    """Gauss-Newton with left-multiplicative updates rho(x) <- exp(Y_x) rho(x), Y_x in e6.
    Residual: relator - I (729) [+ extra equations].  Jacobian analytic (the adjoint Fox operator)."""
    n = 27
    mats = dict(mats)
    invs = dict(invs)
    v = None if extra is None else extra["v0"]
    for it in range(iters):
        Rm = ev(mats, invs, REL, n)
        r = flat(Rm - eye(n))
        if extra is not None:
            r += extra["resid"](mats, invs, v)
        nr = float(sum((abs(x) * abs(x) for x in r), arb(0)).sqrt().mid())
        if verbose:
            print(f"      newton it {it}: |res| = {nr:.2e}")
        if nr < float(target):
            break
        cols = []
        for g in (1, 2):
            for k in range(78):
                col = flat(adfox_apply(mats, invs, REL, g, REPA_ON[k], n) * Rm)
                if extra is not None:
                    col += extra["jac_Y"](mats, invs, v, g, REPA_ON[k])
                cols.append(col)
        if extra is not None:
            for k in range(n):
                cols.append([acb(0)] * (n * n) + extra["jac_v"](mats, invs, v, k))
        J = acb_mat(cols).transpose()             # rows = equations
        JH = hermitian(J)
        rhs = JH * acb_mat([[-x] for x in r])
        G = JH * J
        gmax = max(abs(G[i, i]) for i in range(G.nrows()))
        reg = gmax * arb(mu if mu is not None else "1e-24")
        for i in range(G.nrows()):
            G[i, i] = G[i, i] + reg
        # solve the regularized normal equations in mpmath (ball LU refuses ill-conditioned systems)
        with mp.workdps(90):
            Gm = mat2mp(G)
            bm = mat2mp(rhs)
            ym = mp.lu_solve(Gm, bm)
        y = acb_mat([[acb(arb(mp.nstr(ym[i].real, 85)), arb(mp.nstr(ym[i].imag, 85)))] for i in range(Gm.rows)])
        # damped update with backtracking on the residual
        damp = acb(1)
        for _ in range(12):
            Ya = sum((REPA_ON[k] * (y[k, 0] * damp) for k in range(78)), acb_mat(n, n))
            Yb = sum((REPA_ON[k] * (y[78 + k, 0] * damp) for k in range(78)), acb_mat(n, n))
            m_try = {1: Ya.exp() * mats[1], 2: Yb.exp() * mats[2]}
            i_try = {1: invs[1] * (-Ya).exp(), 2: invs[2] * (-Yb).exp()}
            v_try = None if extra is None else v + acb_mat([[y[156 + k, 0] * damp] for k in range(n)])
            r_try = flat(ev(m_try, i_try, REL, n) - eye(n))
            if extra is not None:
                r_try += extra["resid"](m_try, i_try, v_try)
            nr_try = float(sum((abs(x) * abs(x) for x in r_try), arb(0)).sqrt().mid())
            if nr_try < nr:
                mats, invs, v = m_try, i_try, v_try
                break
            damp = damp / 2
        else:
            print("      newton: no descent direction found; stopping")
            break
    return mats, invs, v, nr


def main():
    t0 = time.time()
    print("=== (0) the geometric point, principal 27 (exact input, 60-digit ranks) ===")
    print("    trace test |tr rho(w) - tr rho(w^-1)|:", [x.str(2) for x in selfduality_trace_test(M0, M0i, 27)])
    rep0r = cohomology_report(M0, M0i, 27, "27 at s=0")

    print("\n=== (a) the exact theta-odd cocycle class (V8 block) and the Newton search ===")
    Za, Zb = block_cocycle_exact(4)
    Ya1 = e6_matrix([q2acb(z) for z in Za])
    Yb1 = e6_matrix([q2acb(z) for z in Zb])
    znorm = max(float(frob(Ya1).mid()), float(frob(Yb1).mid()))
    print(f"    |Z_a|, |Z_b| on the rescaled 27: {frob(Ya1).str(3)}, {frob(Yb1).str(3)}")
    for eps_f in (0.02 / znorm,):
        eps = F(eps_f).limit_denominator(10**6)
        Ya = Ya1 * acb(fmpq(eps.numerator, eps.denominator))
        Yb = Yb1 * acb(fmpq(eps.numerator, eps.denominator))
        mats = {1: Ya.exp() * A0, 2: Yb.exp() * B0}
        invs = {1: A0i * (-Ya).exp(), 2: B0i * (-Yb).exp()}
        print(f"    start eps = {eps}: relator residual {frob(ev(mats, invs, REL, 27) - eye(27)).str(3)}")
        mats, invs, _, nr = newton(mats, invs)
        print(f"    converged: residual {nr:.1e}")
        tt = selfduality_trace_test(mats, invs, 27)
        print("    trace test |tr rho(w) - tr rho(w^-1)|:", [x.str(3) for x in tt], " -> NOT self-dual (theta-odd)" if max(float(x.mid()) for x in tt) > 1e-20 else " -> self-dual")
        print(f"    tr_27 rho(a) = {trace(mats[1]).str(12)}   (27 at s = 0)")
        rep = cohomology_report(mats, invs, 27, f"27 at eps={eps}")
        dm, di = dual_of(mats, invs)
        repd = cohomology_report(dm, di, 27, f"27bar at eps={eps}")
        print(f"    ==> N(27) = h1(27) - h1(27bar) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}")

    print("\n=== (b) the fixed-vector locus: mu v = v, lambda v = v, theta-odd ===")
    # start from the converged theta-odd point; v0 = the fixed vector of the unipotent mu_0
    n = 27
    # fixed vector of A0: solve (A0 - I) v = 0 exactly is 3-dim; take the highest-weight-type vector:
    # the kernel of the exact (A0 - I) restricted... use mp nullspace
    K = mp_nullspace(mat2mp(A0 - eye(n)))
    # choose the kernel vector also fixed by lambda_0 with the largest projection on the Sym^16 block
    lam0 = ev(M0, M0i, LONG, n)
    Kl = mp_nullspace(mat2mp(vstack(A0 - eye(n), lam0 - eye(n))))
    v0mp = Kl[0]
    v0 = acb_mat([[acb(arb(str(v0mp[i].real)), arb(str(v0mp[i].imag)))] for i in range(n)])
    v0h = hermitian(v0)

    def resid(mats, invs, v):
        lam = ev(mats, invs, LONG, n)
        r1 = (mats[1] - eye(n)) * v
        r2 = (lam - eye(n)) * v
        r3 = v0h * v - acb_mat([[acb(1)]])
        return flat(r1) + flat(r2) + flat(r3)

    def jac_Y(mats, invs, v, g, Y):
        lam = ev(mats, invs, LONG, n)
        dmu = (Y * mats[1]) * v if g == 1 else acb_mat(n, 1)
        dlam = (adfox_apply(mats, invs, LONG, g, Y, n) * lam) * v
        return flat(dmu) + flat(dlam) + [acb(0)]

    def jac_v(mats, invs, v, k):
        lam = ev(mats, invs, LONG, n)
        ek = acb_mat(n, 1)
        ek[k, 0] = acb(1)
        return flat((mats[1] - eye(n)) * ek) + flat((lam - eye(n)) * ek) + flat(v0h * ek)

    extra = dict(v0=v0, resid=resid, jac_Y=jac_Y, jac_v=jac_v)
    mats2, invs2, v, nr = newton(mats, invs, extra=extra, iters=60)
    print(f"    converged: residual {nr:.1e}")
    tt = selfduality_trace_test(mats2, invs2, n)
    print("    trace test |tr rho(w) - tr rho(w^-1)|:", [x.str(3) for x in tt], " -> NOT self-dual (theta-odd)" if max(float(x.mid()) for x in tt) > 1e-20 else " -> SELF-DUAL")
    print(f"    tr_27 rho(a) = {trace(mats2[1]).str(12)}")
    rep = cohomology_report(mats2, invs2, n, "27 on the fixed-vector locus")
    dm, di = dual_of(mats2, invs2)
    repd = cohomology_report(dm, di, n, "27bar on the fixed-vector locus")
    print(f"    ==> N(27) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
