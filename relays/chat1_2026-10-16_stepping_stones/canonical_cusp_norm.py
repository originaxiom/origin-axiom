"""Is there a canonical, scale-free, POSITIVE reading of the cusp for the frame's mode norms? (chat1; no data)

W72's surface frame left the three generations' modes without a normalisation: each unit has a principal part
(q^-7/8, q^-1/8 or q^-5/8, coefficient 1) that grows at the cusp, so every Petersson norm diverges, and W73 used the
cusp's own pairing of the units (K = diag(1, 2, 2), "H-end", chosen post hoc). This asks whether the cusp has a
canonical reading that keeps the norms finite without a cutoff, and whether it is a norm.

The canonical candidate. Truncate the fundamental domain at y <= T. For y >= 1 the x-integral keeps, per component l
(weight w_l: 1 on e_i, 2 on v+-, the invariant Hermitian form of tlow2's (i, j, k) basis), the terms with equal
exponents p, each times I(p) = int_1^T e^{-4 pi p y} y^m dy with m = k - 2 (dmu = dx dy / y^2). For p > 0 this
converges. For p < 0 it grows like e^{a T} T^m (a = -4 pi p); its constant term in T (the Hadamard finite part,
with the growing series median-resummed) is the real part of the analytic continuation of the convergent formula,
FP = Re[(-a)^(-m-1) Gamma(m+1, -a)], the same for both lateral continuations (they differ by a pure imaginary
constant). There is no log T term for these weights (m = -1/2, -5/2, 3/2), so FP does not depend on the scale of T:
it is scale-free. The region y < 1 of the fundamental domain is integrated directly (Gauss-Legendre in x and y).
K_reg = FP of the truncated pairing, for the three norm cells K32 (weight 3/2), KM12 (-1/2) and K72 (7/2, with
fser). It is the regularised inner product of Bringmann, Diamantis and Ehlen (2017), whose growing terms are continued
and their real part taken. Checks: FP against two independent formulas; the quadrature at two node counts; the series
at two truncations.

The height family. The principal parts are orthogonal to every other term after the x-integral, so every
regularisation of this kind differs from K_reg only in the three growing modes' diagonal entries:
K(c) = K_reg - diag(w FP int_c^infinity e^{a y} y^m dy). Cutting at c = 1, the edge of SL(2, Z)'s standard maximal
cusp neighbourhood (y > 1; other heights, such as sqrt(3)/2, are also distinguished), is positive by construction (the integral over F below 1 plus that of |A - principal part|^2 above);
the script reports K(1)'s eigenvalues and the threshold c* above which K(c) is positive definite.
Usage: python3 -B canonical_cusp_norm.py <forms.pkl> > canonical_cusp_norm_run.txt
"""
import hashlib, math, pickle, sys
import numpy as np
import mpmath as mp

mp.mp.dps = 40
P = pickle.load(open(sys.argv[1], "rb"))
FORMS_SHA = hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest()
W = {"e_i": 1.0, "v+": 2.0, "v-": 2.0}


def series(s, nmax8=None):
    out = {}
    for (l, n8), a in s.items():
        if nmax8 is None or n8 <= nmax8:
            out.setdefault(l, {})[n8] = complex(mp.mpc(a))
    return out


def I_tail(p, m):
    """int_1^infinity e^{-4 pi p y} y^m dy for p > 0; its median finite part for p < 0"""
    b = 4 * mp.pi * p
    if p > 0:
        return mp.gammainc(m + 1, b) / b ** (m + 1)
    a = -b
    return mp.re(mp.power(mp.mpc(-a, 0), -m - 1) * mp.gammainc(m + 1, mp.mpc(-a, 0)))


def I_tail_check(p, m):
    """the same finite part by a different route: -int_0^1 e^{a y} y^m dy + Gamma(m+1) a^(-m-1) cos(pi (m+1)) for
    m > -1, and integration by parts downward for m < -1"""
    a = -4 * mp.pi * p
    if m > -1:
        return -mp.quad(lambda y: mp.e ** (a * y) * y ** m, [0, 1]) + mp.gamma(m + 1) * a ** (-m - 1) * mp.cos(mp.pi * (m + 1))
    return -mp.e ** a / (m + 1) - a / (m + 1) * I_tail_check(p, m + 1)


def lower_region(forms, m, nx, ny):
    """int over |x| <= 1/2, sqrt(1 - x^2) <= y <= 1 of sum_l w_l A_l conj(B_l) y^m dx dy, for every pair"""
    gx, wx = np.polynomial.legendre.leggauss(nx)
    gy, wy = np.polynomial.legendre.leggauss(ny)
    X = 0.5 * gx; WX = 0.5 * wx
    K = np.zeros((len(forms), len(forms)), dtype=complex)
    for x, wxi in zip(X, WX):
        y0 = math.sqrt(1 - x * x)
        Y = y0 + (1 - y0) * (gy + 1) / 2; WY = wy * (1 - y0) / 2
        tau = x + 1j * Y
        vals = []
        for f in forms:
            comp = {}
            for l, coeffs in f.items():
                n8 = np.array(sorted(coeffs)); c = np.array([coeffs[n] for n in sorted(coeffs)])
                comp[l] = (np.exp(2j * np.pi * np.outer(tau, n8) / 8) * c).sum(axis=1)
            vals.append(comp)
        for i in range(len(forms)):
            for j in range(len(forms)):
                tot = 0
                for l in W:
                    if l in vals[i] and l in vals[j]:
                        tot = tot + W[l] * vals[i][l] * np.conj(vals[j][l])
                K[i, j] += wxi * np.sum(WY * tot * Y ** m)
    return K


def upper_region(forms, m):
    K = np.zeros((len(forms), len(forms)), dtype=complex)
    fp_terms = []
    for i in range(len(forms)):
        for j in range(len(forms)):
            tot = mp.mpc(0)
            for l in W:
                if l not in forms[i] or l not in forms[j]:
                    continue
                for n8, a in forms[i][l].items():
                    b = forms[j][l].get(n8)
                    if b is None:
                        continue
                    term = W[l] * a * b.conjugate() * I_tail(mp.mpf(n8) / 8, m)
                    tot += term
                    if n8 < 0 and i == j:
                        fp_terms.append((i, l, n8, complex(term)))
            K[i, j] = complex(tot)
    return K, fp_terms


def gram(name, raw, k, nmax8=None, nx=48, ny=48):
    forms = [series(s, nmax8) for s in raw]
    m = k - 2
    Ku, fp = upper_region(forms, m)
    Kl = lower_region(forms, m, nx, ny)
    return Ku + Kl, Ku, Kl, fp


if __name__ == "__main__":
    print(f"forms.pkl sha256 {FORMS_SHA} (W72's units, from m003_exploration/instrument/build_forms.py, as in the seals)")
    print("finite-part checks (two formulas):")
    for p, m in ((-7 / 8, -0.5), (-1 / 8, -0.5), (-5 / 8, -0.5), (-7 / 8, 1.5), (-5 / 8, -2.5), (-1 / 8, -2.5)):
        print(f"  p = {p:+.3f}, m = {m:+.1f}: FP = {mp.nstr(I_tail(mp.mpf(p), m), 15)}; check {mp.nstr(I_tail_check(mp.mpf(p), m), 15)}")
    cells = {"K32 (weight 3/2: F_i, F+, F-)": (P["F32"], 1.5),
             "KM12 (weight -1/2: the three -1/2 sections; R is the second)": (P["FM12"], -0.5),
             "K72 (weight 7/2: E4 times the -1/2 sections, and fser)": (P["E4F"] + [P["fser"]], 3.5)}
    for name, (raw, k) in cells.items():
        K, Ku, Kl, fp = gram(name, raw, k)
        K2, _, _, _ = gram(name, raw, k, nmax8=160, nx=72, ny=72)
        dev = np.max(np.abs(K - K2)) / np.max(np.abs(K))
        H = (K + K.conj().T) / 2
        ev = np.linalg.eigvalsh(H)
        print(f"\n{name}")
        print(f"  the principal parts' finite parts (diagonal): " + "; ".join(
            f"unit {i} {l} q^{n8}/8: {t.real:+.6g}" for i, l, n8, t in fp))
        print(f"  diagonal: y >= 1 part {np.round(np.real(np.diag(Ku)), 4)}, y < 1 part {np.round(np.real(np.diag(Kl)), 4)}")
        print(f"  K_reg diagonal {np.round(np.real(np.diag(K)), 4)}; Hermitian defect {np.max(np.abs(K - K.conj().T)):.1e}; "
              f"stability (series and nodes) {dev:.1e}")
        w_, v_ = np.linalg.eigh(H)
        print(f"  eigenvalues of K_reg: {', '.join(f'{x:.6e}' for x in ev)}  ->  {'POSITIVE DEFINITE' if ev.min() > 0 else 'NOT POSITIVE'}")
        print(f"  the most negative eigenvalue's direction (moduli on the units): {np.round(np.abs(v_[:, 0]), 4)}")
        m = k - 2
        def Kc(c):
            Kc_ = K.copy()
            for i, l, n8, t in fp:
                a = -4 * mp.pi * mp.mpf(n8) / 8
                tail_c = mp.re(mp.power(mp.mpc(-a, 0), -m - 1) * mp.gammainc(m + 1, mp.mpc(-a * c, 0)))  # FP of int_c^inf
                Kc_[i, i] -= W[l] * float(tail_c)
            return Kc_
        e1 = np.linalg.eigvalsh((Kc(1.0) + Kc(1.0).conj().T) / 2)
        lo, hi = 0.0, 1.0
        for _ in range(50):
            mid = (lo + hi) / 2
            if np.linalg.eigvalsh((Kc(mid) + Kc(mid).conj().T) / 2).min() > 0: hi = mid
            else: lo = mid
        print(f"  K(c = 1), principal parts cut at the standard maximal cusp: eigenvalues {', '.join(f'{x:.6g}' for x in e1)}; "
              f"K(c) positive definite for c > c* = {hi:.4f}")
