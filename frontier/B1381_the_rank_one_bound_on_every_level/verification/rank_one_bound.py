#!/usr/bin/env python3
"""B1381 -- THE RANK-ONE BOUND ON EVERY LEVEL.  Main's B1427 (2026-09-18) found h^1 = 2 on no component of any cyclic cover
M_n of m004 for n = 2..7 (exactly, over the whole character group) and named the mechanism: with 3 generators and 2 relators
h^1 = 2 needs the whole Fox Jacobian to vanish.  This proves it never vanishes, for every n.

pi_1(M_n) = < a, b, t | t a t^-1 = phi^n(a), t b t^-1 = phi^n(b) >, phi = m004's monodromy on F(a, b) (here sigma^2 of B1380:
a -> aba, b -> ab, abelianization M = [[2,1],[1,1]]).  For a character chi = (x, y, s) = (chi(a), chi(b), chi(t)):
  * the t-column of the Fox Jacobian is (1 - x, 1 - y), so J = 0 forces x = y = 1;
  * at x = y = 1 the (a, b)-block is s*I - N_n with N_n the exponent-sum matrix of phi^n, i.e. M^n up to transpose;
  * M^n has distinct eigenvalues phi^(2n), phi^(-2n), so it is never scalar and J never vanishes.
Hence h^1(M_n; C_chi) = 2 - rank J <= 1 for every chi != 1 (and = b_1 = 1 at chi = 1), for every n >= 1.

Sections (each asserts; the run log is rank_one_bound_run.txt):
  S1 the Fox Jacobian of M_n symbolically in (x, y, s), n = 1..8: the t-column and the fibre block at x = y = 1
  S2 the block is never zero: M^n = [[F(2n+1), F(2n)], [F(2n), F(2n-1)]], off-diagonal F(2n) != 0, n = 1..40
  S3 instrument control that MUST fire: the hyperelliptic involution a -> a^-1, b -> b^-1 (abelianization -I) gives J = 0
     at the non-trivial character (1, 1, -1), i.e. h^1 = 2 there
  S4 h^1 by direct rank at sample characters (roots of unity and the golden loci s = phi^(+-2n) at x = y = 1), n = 1..6
Usage: python3 rank_one_bound.py"""
import sympy as sp

A, B = 1, 2
x, y, s = sp.symbols("x y s")
CHI = {A: x, B: y}


def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return out


def inv(w):
    return [-g for g in reversed(w)]


def apply(phi, w):
    out = []
    for g in w:
        out += phi[g] if g > 0 else inv(phi[-g])
    return red(out)


def power(phi, n):
    res = {A: [A], B: [B]}
    for _ in range(n):
        res = {g: apply(phi, res[g]) for g in (A, B)}
    return res


def ev(word, chi):
    """chi(word) for a word in the fibre generators (t does not occur)."""
    v = sp.Integer(1)
    for g in word:
        v *= chi[abs(g)] ** (1 if g > 0 else -1)
    return v


def fox(word, gen, chi):
    """Fox derivative d(word)/d(gen) evaluated under the abelian character chi (fibre letters only)."""
    total, prefix = sp.Integer(0), sp.Integer(1)
    for g in word:
        if g == gen:
            total += prefix
        if g == -gen:
            total -= prefix * chi[gen] ** -1
        prefix *= chi[abs(g)] ** (1 if g > 0 else -1)
    return sp.simplify(total)


def jacobian(phi_n, chi=None, t_val=s):
    """Rows r_a = t a t^-1 w_a^-1, r_b = t b t^-1 w_b^-1; columns a, b, t.  d r_g/d t = 1 - chi(g);
    d r_g/d h = t*[g == h] - chi(t g t^-1 w_g^-1) * d w_g/d h, and chi(t g t^-1 w_g^-1) = chi(g)/chi(w_g)."""
    chi = chi or CHI
    rows = []
    for g in (A, B):
        w = phi_n[g]
        c = chi[g] / ev(w, chi)
        row = [(t_val if g == h else 0) - c * fox(w, h, chi) for h in (A, B)] + [1 - chi[g]]
        rows.append([sp.simplify(e) for e in row])
    return sp.Matrix(rows)


SIGMA2 = {A: [A, B, A], B: [A, B]}          # m004's monodromy (B1380: sigma^2), abelianization [[2,1],[1,1]]
M = sp.Matrix([[2, 1], [1, 1]])


def s1_jacobian(nmax=8):
    out = []
    for n in range(1, nmax + 1):
        pn = power(SIGMA2, n)
        J = jacobian(pn)
        tcol = [sp.simplify(J[0, 2]), sp.simplify(J[1, 2])]
        assert tcol == [1 - x, 1 - y]
        block = J[:, :2].subs({x: 1, y: 1})
        N = sp.Matrix([[sum(1 for g in pn[A] if g == A) - sum(1 for g in pn[A] if g == -A),
                        sum(1 for g in pn[B] if g == A) - sum(1 for g in pn[B] if g == -A)],
                       [sum(1 for g in pn[A] if g == B) - sum(1 for g in pn[A] if g == -B),
                        sum(1 for g in pn[B] if g == B) - sum(1 for g in pn[B] if g == -B)]])
        assert N == M ** n
        assert sp.simplify(block - (s * sp.eye(2) - N.T)) == sp.zeros(2)
        out.append((n, len(pn[A]) + len(pn[B]), N.tolist()))
    return out


def s2_never_scalar(nmax=40):
    fib = [0, 1]
    while len(fib) < 2 * nmax + 3:
        fib.append(fib[-1] + fib[-2])
    for n in range(1, nmax + 1):
        Mn = M ** n
        assert Mn == sp.Matrix([[fib[2 * n + 1], fib[2 * n]], [fib[2 * n], fib[2 * n - 1]]])
        assert Mn[0, 1] != 0 and Mn[1, 0] != 0
    lam = sp.Matrix(M).eigenvals()
    assert len(lam) == 2
    return nmax, sorted(float(v) for v in lam)


def s3_control():
    """The hyperelliptic involution iota: a -> a^-1, b -> b^-1 (abelianization -I; mapping torus Seifert-fibred).
    At chi = (1, 1, -1) the whole Jacobian vanishes: h^1 = 2 at a non-trivial character. The criterion can fire."""
    iota = {A: [-A], B: [-B]}
    J = jacobian(iota)
    J0 = J.subs({x: 1, y: 1, s: -1})
    assert J0 == sp.zeros(2, 3)
    J1 = jacobian(SIGMA2).subs({x: 1, y: 1, s: -1})
    assert J1 != sp.zeros(2, 3)
    return J.tolist(), J0.rank(), J1.rank()


def h1(J, chi_is_trivial):
    return 3 - J.rank() - (0 if chi_is_trivial else 1)


def s4_samples(nmax=6):
    rows = []
    phi_golden = (1 + sp.sqrt(5)) / 2
    for n in range(1, nmax + 1):
        pn = power(SIGMA2, n)
        J = jacobian(pn)
        samples = []
        for (xv, yv, sv) in [(1, 1, 1), (1, 1, -1), (-1, 1, 1), (1, -1, -1), (sp.I, -sp.I, 1)]:
            Jv = sp.simplify(J.subs({x: xv, y: yv, s: sv}))
            triv = (xv, yv, sv) == (1, 1, 1)
            samples.append(h1(Jv, triv))
        for sv in (phi_golden ** (2 * n), phi_golden ** (-2 * n)):
            Jv = sp.simplify(J.subs({x: 1, y: 1, s: sv}))
            samples.append(h1(Jv, False))
        assert max(samples) <= 1 and samples[0] == 1
        rows.append((n, samples))
    return rows


if __name__ == "__main__":
    for n, length, N in s1_jacobian():
        print("S1  n = %d: t-column (1-x, 1-y); fibre block at x=y=1 is s*I - (M^n)^T, M^n = %s (word length %d)" % (n, N, length))
    nmax, ev_ = s2_never_scalar()
    print("S2  M^n = [[F(2n+1), F(2n)], [F(2n), F(2n-1)]] with F(2n) != 0 for n = 1..%d; eigenvalues of M %s -- never scalar"
          % (nmax, [round(v, 6) for v in ev_]))
    J, r0, r1 = s3_control()
    print("S3  control: hyperelliptic involution, J =", J, "| rank at (1,1,-1):", r0, "(h1 = 2 -- the criterion fires);",
          "m004's monodromy at the same character: rank", r1)
    for n, sm in s4_samples():
        print("S4  n = %d: h1 at (1,1,1), (1,1,-1), (-1,1,1), (1,-1,-1), (i,-i,1), golden s = phi^(+-2n):" % n, sm)
    print("DONE")
