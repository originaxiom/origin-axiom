"""B666 cell 1 (L105) — the silver stage scan + exact tone certificates.

PART 1 of the sealed cell: the silver's gate under the banked κ-gating
law (B621): torsion base t^2 - 4 = 3^v * m, reflection-coset content
iff m | κ. Silver RRLL: t = 6, base = 32 = 3^0 * 32, so the law's
literal gate is 32 | κ. BUT the silver is the first object whose base
is NOT (3-part)*(squarefree): 32 = 2^2 * 8 = f^2 * disc Q(sqrt2) —
the order Z[2 sqrt2] vs the maximal order Z[sqrt2]. The field
alternative would gate at 8 | κ (the conductor of the quadratic
character of Q(sqrt2), the modulus of the B644-style ear).

FIELD LEMMA (abstract, checked here): the odd hearing trace at stage κ
lives in Q(zeta_{3κ}); sqrt2 ∈ Q(zeta_n) iff 8 | n; 8 | 3κ iff 8 | κ.
So sqrt2 content is POSSIBLE only at 8 | κ — every off-grid level is
field-forced silent. The scan then decides which multiples of 8
actually bear (gate 8 vs 16 vs 32).

PART 3: exact tone arithmetic. At each κ in {8,16,24,32,40,48} the
trace tr B_odd(RRLL; κ) is computed EXACTLY in Z[zeta_{3κ}]-arithmetic
(integer coefficient vectors mod x^n - 1, reduced mod Phi_n, the
Kac-Peterson normalizer handled exactly via S^{-1} = S^dagger so the
scalar r = (Sigma Sigma^dagger)_00 is the only division), then
decomposed over {1, sqrt2, i, i*sqrt2} with rational coefficients —
the decisive "lands in Q(sqrt2)" fact, exact.

DISCOVERY LAYER (floats, B618's banked pattern verbatim): the κ = 4..48
scan with the a + b*sqrt2 rational-fit detector; golden (RL, sqrt5 at
5|κ — banked B601/B618) and tr-5 (R^3L, sqrt21 at κ=14 — banked B618)
as positive controls of the detector.
"""
import importlib.util
import math
import os
import sys
from fractions import Fraction
from itertools import permutations

import numpy as np
from sympy import cyclotomic_poly, Symbol

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "..", "B238_su32_levelrank",
                         "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


# ---------------------------------------------------------------- floats
def odd_trace(level, word):
    """B618's observable, verbatim pattern."""
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    W = np.eye(n, dtype=complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    return np.trace(-(U.T @ W @ U))


def fit_sqrt(x, root, den_max=24, tol=1e-9):
    """x ~ a + b*sqrt(root), a,b rational, denominators <= den_max."""
    s = math.sqrt(root)
    best = None
    for db in range(1, den_max + 1):
        for nb in range(-6 * db, 6 * db + 1):
            b = Fraction(nb, db)
            a = x - float(b) * s
            fa = Fraction(a).limit_denominator(den_max)
            if abs(float(fa) + float(b) * s - x) < tol:
                cand = (fa, b)
                if best is None or (cand[1] != 0 and best[1] == 0):
                    best = cand
                if cand[1] != 0:
                    return cand
    return best


# ------------------------------------------------------- exact machinery
def su3_exact_data(kap):
    """weights, Sigma (unnormalized KP numerator matrix) as dict of
    monomials {index: coeff} per entry, T-exponent list, n = 3*kap."""
    k = kap - 3
    n = 3 * kap
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    perms = list(permutations(range(3)))
    sgn = {p: (-1) ** sum(p[i] > p[j] for i in range(3)
                          for j in range(i + 1, 3)) for p in perms}

    def Lvec(w):
        return (Fraction(w[0] + w[1] + 2), Fraction(w[1] + 1),
                Fraction(0))

    def ip(u, v):
        su, sv = sum(u), sum(v)
        return (u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
                - su * sv / 3)

    m = len(weights)
    Ls = [Lvec(w) for w in weights]
    # Sigma[i][j] = list of (index, sign)
    Sig = [[None] * m for _ in range(m)]
    for i in range(m):
        Li = Ls[i]
        for j in range(m):
            Lj = Ls[j]
            terms = []
            for p in perms:
                Lp = (Li[p[0]], Li[p[1]], Li[p[2]])
                e = -3 * ip(Lp, Lj)          # exponent * n / (2 pi i):
                assert e.denominator == 1    # e = -ip/kap * n = -3 ip
                terms.append((int(e) % n, sgn[p]))
            Sig[i][j] = terms
    # T exponents: (h - c/24)*n = a^2+ab+b^2 + 3(a+b) - k
    Texp = [((a * a + a * b + b * b) + 3 * (a + b) - k) % n
            for (a, b) in weights]
    return weights, Sig, Texp, n


def entry_M(Sig, Texp2neg, x, y, n, m):
    """M_xy = sum_z conj(Sig[z][x]) * tbar2_z * Sig[z][y] as int vector."""
    v = [0] * n
    for z in range(m):
        sh = Texp2neg[z]
        for (e1, s1) in Sig[z][x]:
            base = (-e1 + sh) % n
            for (e2, s2) in Sig[z][y]:
                v[(base + e2) % n] += s1 * s2
    return v


def poly_mod_phi(vec, phi):
    """reduce integer/Fraction coefficient vector mod Phi_n (monic int
    poly, given low->high). Returns Fraction list of length deg(phi)."""
    d = len(phi) - 1
    v = [Fraction(c) for c in vec]
    for i in range(len(v) - 1, d - 1, -1):
        c = v[i]
        if c == 0:
            continue
        for j in range(d + 1):
            v[i - d + j] -= c * phi[j]
    return v[:d]


def solve_membership(vred, basis_vecs):
    """exact: is vred a Q-combination of basis_vecs? Gaussian elim."""
    rows = len(vred)
    cols = len(basis_vecs)
    A = [[basis_vecs[c][r] for c in range(cols)] + [vred[r]]
         for r in range(rows)]
    piv = []
    r0 = 0
    for c in range(cols):
        pr = None
        for r in range(r0, rows):
            if A[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        A[r0], A[pr] = A[pr], A[r0]
        pv = A[r0][c]
        A[r0] = [x / pv for x in A[r0]]
        for r in range(rows):
            if r != r0 and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[r0])]
        piv.append(c)
        r0 += 1
    # consistency: rows beyond pivots must be 0 = 0
    for r in range(r0, rows):
        if A[r][cols] != 0:
            return None
    sol = [Fraction(0)] * cols
    r = 0
    for c in piv:
        sol[c] = A[r][cols]
        r += 1
    return sol


def exact_tone(kap, word="RRLL", verify_float=True):
    """exact tr B_odd(word; kap); decompose over {1, i} and
    {1, sqrt2, i, i sqrt2} (the latter only if 8 | 3*kap)."""
    weights, Sig, Texp, n = su3_exact_data(kap)
    m = len(weights)
    assert word == "RRLL"
    Texp2 = [(2 * t) % n for t in Texp]
    Texp2neg = [(-2 * t) % n for t in Texp]

    # r = (Sigma Sigma^dagger)_00 (exact scalar of unitarity)
    def gram(x, y):
        v = [0] * n
        for z in range(m):
            for (e1, s1) in Sig[z][x]:
                for (e2, s2) in Sig[z][y]:
                    v[(e2 - e1) % n] += s1 * s2
        return v

    phi = [int(c) for c in reversed(
        cyclotomic_poly(n, Symbol("x")).all_coeffs())]
    r_vec = poly_mod_phi(gram(0, 0), phi)
    r_rat = r_vec[0]
    assert all(c == 0 for c in r_vec[1:]), "r not rational!"
    # unitarity spot-gates (exact): a few diagonal + off-diagonal
    import random
    random.seed(1)
    for _ in range(4):
        i0 = random.randrange(m)
        v = poly_mod_phi(gram(i0, i0), phi)
        assert v[0] == r_rat and all(c == 0 for c in v[1:]), \
            f"diag gram fail at {i0}"
    for _ in range(6):
        i0, j0 = random.randrange(m), random.randrange(m)
        if i0 == j0:
            continue
        v = poly_mod_phi(gram(i0, j0), phi)
        assert all(c == 0 for c in v), f"offdiag gram fail {i0},{j0}"

    idx = {w: i for i, w in enumerate(weights)}
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in weights
                  if a != b})
    acc = [Fraction(0)] * n
    for (a, b) in prs:
        p, q = idx[(a, b)], idx[(b, a)]
        for (x, y, sgn_) in ((p, p, 1), (p, q, -1), (q, p, -1),
                             (q, q, 1)):
            Mv = entry_M(Sig, Texp2neg, x, y, n, m)
            sh = Texp2[x]
            for e in range(n):
                if Mv[e]:
                    acc[(e + sh) % n] += sgn_ * Mv[e]
    # tr B_odd = -(1/2) * acc / r
    acc = [-(c / (2 * r_rat)) for c in acc]
    vred = poly_mod_phi(acc, phi)
    d = len(vred)

    def vec_of_power(j):
        v = [0] * n
        v[j % n] = 1
        return poly_mod_phi(v, phi)

    one = [Fraction(1)] + [Fraction(0)] * (d - 1)
    i4 = vec_of_power(n // 4)
    out = {"kappa": kap, "n": n, "r": r_rat}
    sol_qi = solve_membership(vred, [one, i4])
    out["in_Q(i)"] = sol_qi
    if n % 8 == 0:
        s2 = [x + y for x, y in zip(vec_of_power(n // 8),
                                    vec_of_power(7 * n // 8))]
        is2v = [0] * n
        is2v[(n // 4 + n // 8) % n] = 1
        is2v[(n // 4 + 7 * n // 8) % n] = 1
        is2 = poly_mod_phi(is2v, phi)
        sol = solve_membership(vred, [one, s2, i4, is2])
        out["decomp_1_s2_i_is2"] = sol
    else:
        out["decomp_1_s2_i_is2"] = None
    if verify_float:
        # float cross-check of the exact value
        z = np.exp(2j * np.pi / n)
        val = sum(float(c) * z ** j for j, c in enumerate(vred))
        fl = odd_trace(kap - 3, word)
        out["float_delta"] = abs(val - fl)
    return out


def main():
    print("B666 cell 1 — the silver stage: gate + exact tones")
    print("=" * 70)
    print("\nTHE GATE FROM THE LAW (B621): t=6, base t^2-4 = 32 = 3^0*32")
    print("  -> literal law gate: 32 | kappa.  Field alternative: "
          "8 | kappa")
    print("  (32 = 2^2 * 8 = f^2 * disc Q(sqrt2); first non-maximal-"
          "order base).")
    print("\nFIELD LEMMA: value ∈ Q(zeta_3k); sqrt2 ∈ Q(zeta_n) iff 8|n;"
          " 8|3k iff 8|k.")
    print("  -> sqrt2 content impossible unless 8 | kappa "
          "(off-grid silence is field-forced).")

    # ---- controls for the float detector
    print("\n[controls] golden RL, sqrt5 fit (banked: bearing at 5|kappa):")
    for kap in range(4, 16):
        tr = odd_trace(kap - 3, "RL")
        hits = []
        for part, val in (("Re", tr.real), ("Im", tr.imag)):
            if abs(val) < 1e-9:
                continue
            f = fit_sqrt(val, 5)
            if f and f[1] != 0:
                hits.append(f"{part}={f[0]}+{f[1]}*sqrt5")
        print(f"    kappa={kap:>2}: {tr.real:+.6f}{tr.imag:+.6f}j"
              f"{'  <-- ' + '; '.join(hits) if hits else ''}")
    tr14 = odd_trace(11, "RRRL")
    f14 = [fit_sqrt(v, 21) for v in (tr14.real, tr14.imag)
           if abs(v) > 1e-9]
    print(f"    tr-5 control kappa=14 (banked sqrt21-bearing): "
          f"{tr14:.6f} fits {f14}")

    # ---- the silver scan
    print("\n[scan] RRLL odd trace, kappa = 4..48, sqrt2 fit "
          "(floats, discovery):")
    bearing = []
    for kap in range(4, 49):
        tr = odd_trace(kap - 3, "RRLL")
        hits = []
        for part, val in (("Re", tr.real), ("Im", tr.imag)):
            if abs(val) < 1e-9:
                continue
            f = fit_sqrt(val, 2)
            if f and f[1] != 0:
                hits.append(f"{part} = {f[0]} + {f[1]}*sqrt2")
        if hits:
            bearing.append(kap)
        print(f"    kappa={kap:>2}: tr = {tr.real:+.9f}"
              f"{tr.imag:+.9f}j"
              f"{'  <-- sqrt2-BEARING: ' + '; '.join(hits) if hits else ''}",
              flush=True)
    print(f"\n  sqrt2-bearing levels (float detector): {bearing}")
    print(f"  multiples of 8 in range: {[k for k in range(4, 49) if k % 8 == 0]}")
    print(f"  multiples of 32 in range: {[k for k in range(4, 49) if k % 32 == 0]}")

    # ---- exact certificates
    print("\n[exact] certificates at kappa in {8,16,24,32,40,48} "
          "(Z[zeta_3k] arithmetic, mod Phi_n, decomposition over "
          "{1, sqrt2, i, i*sqrt2}):", flush=True)
    for kap in (8, 16, 24, 32, 40, 48):
        res = exact_tone(kap)
        sol = res["decomp_1_s2_i_is2"]
        qi = res["in_Q(i)"]
        line = f"    kappa={kap:>2} (n={res['n']}, r={res['r']}): "
        if sol is not None:
            a, b, c, dd = sol
            line += (f"tr = ({a}) + ({b})*sqrt2 + i*[({c}) + "
                     f"({dd})*sqrt2]")
            line += f"   sqrt2-BEARING: {b != 0 or dd != 0}"
        else:
            line += "NOT in Q(sqrt2, i) — larger field (vector kept)"
        if qi is not None:
            line += f"   [also in Q(i): a={qi[0]}, c={qi[1]}]"
        line += f"   [float delta {res['float_delta']:.2e}]"
        print(line, flush=True)

    print("\nDONE", flush=True)


if __name__ == "__main__":
    main()
