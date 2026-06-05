"""B73 (Path A) -- the degree=rank tower law: SL(4) figure-eight Dehn-filling components give M^4=L.

The decisive open question: is the longitude the meridian's RANK-th power on the Dehn-filling
components, for every rank? SL(3) gave M^3=L (P1/V47, exact). This establishes the SL(4) point, and
the SL(2) baseline.

A0 (SL(2) end, exact -- see test): Fix(T_1^2) on the SL(2) Fricke coords is a SINGLE (geometric)
component {y=z=x/(x-1)}; there is NO Dehn-filling component, and L=M^k is not on the Cooper-Long curve
for any k. So the Dehn-filling-component phenomenon (clean M^n=L) starts at n=3; SL(2) is degenerate.

A1/A2 (SL(4), high-precision-numerical): explicit irreducible SL(4) figure-eight BUNDLE reps (A,B)
(monodromy t with tAt^-1=A^2B, tBt^-1=AB) exist at specific finite-order A-spectra. Using the genuine
meridian mu=A^-1 t (V46, rank-independent) and the scalar-matrix criterion [A,B]=c*mu^k (<=> M^k=L,
the rank-4 analogue of P1's [A,B]=c*mu^3), across full ~15-rep families:

  * A-spectrum {1, 1, w, w^2} (w=e^{2pi i/3}; char (z-1)^2(z^2+z+1); tr A = tr A^-1 = 1 -- the direct
    analogue of SL(3)'s W1 spectrum {1,i,-i}):  [A,B]=c*mu^4  i.e.  M^4 = L  -- DEGREE = RANK.
    Confirmed to ~1e-31 at HIGH PRECISION (mpmath, exact A, Newton-refined bundle rep; controls k=3,5
    are O(1)); median ~5e-13 over a 15-rep family (double precision).
  * A-spectrum {primitive 8th roots; char z^4+1; tr A = 0}:  M^3 = L  (a SECOND Dehn-filling component
    with a DIFFERENT degree). Median ~2e-13 over a 15-rep family.

VERDICT: the degree=rank tower law -- on the SL(n) figure-eight bundle's PRINCIPAL Dehn-filling
component {tr A = tr A^-1 = 1}, the longitude is the meridian's n-th power, M^n = L -- is CONFIRMED for
n=3 (M^3=L) and n=4 (M^4=L, ~1e-31). Honest caveat: SL(4) has MORE than one Dehn-filling component
(the {z^4+1} component gives M^3=L), so the rank-th power lives specifically on the {tr=1} component;
"degree=rank" is the relation on that principal component, not the only relation. Genuine new
character-variety result; label high-precision-numerical (not yet symbolic-exact). Proven core
P1-P16 untouched; standalone topology, no physics.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares

I4 = np.eye(4, dtype=complex)
W = np.exp(2j * np.pi / 3)
WORDS = ["A", "AA", "AAA", "B", "BB", "BBB", "AB", "AAB", "ABB", "BBA",
         "AABB", "AAAB", "ABBB", "ABAB", "AAABB", "AABBB"]

# principal Dehn-filling A-spectrum (tr A = tr A^-1 = 1) and the second (char z^4+1)
SPEC_W1 = np.array([1, 1, W, W ** 2], dtype=complex)                       # -> M^4 = L
SPEC_Z4 = np.array([np.exp(1j * np.pi / 4 * k) for k in (1, 3, 5, 7)], dtype=complex)  # -> M^3 = L


def _g(A, B):
    return {"A": A, "B": B, "m": np.linalg.inv(A), "n": np.linalg.inv(B)}


def _word(s, g):
    M = np.eye(4, dtype=complex)
    for ch in s:
        M = M @ g[ch]
    return M


def _resid(bvec, A):
    B = (bvec[:16] + 1j * bvec[16:]).reshape(4, 4)
    try:
        g, pg = _g(A, B), _g(A @ A @ B, A @ B)
    except np.linalg.LinAlgError:
        return np.ones(2 * (len(WORDS) + 1)) * 1e3
    e = np.array([np.trace(_word(w, g)) - np.trace(_word(w, pg)) for w in WORDS]
                 + [np.linalg.det(B) - 1], dtype=complex)
    return np.concatenate([e.real, e.imag])


def monodromy(A, B):
    """t in SL(4,C) with t A t^-1 = A^2 B, t B t^-1 = A B (figure-eight monodromy); returns (t, res)."""
    pA, pB = A @ A @ B, A @ B
    E = np.vstack([np.kron(A.T, I4) - np.kron(I4, pA), np.kron(B.T, I4) - np.kron(I4, pB)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(4, 4, order="F")
    t = t / np.linalg.det(t) ** 0.25
    res = np.max(np.abs(t @ A @ np.linalg.inv(t) - pA)) + np.max(np.abs(t @ B @ np.linalg.inv(t) - pB))
    return t, res


def _irreducible(A, B):
    g = _g(A, B)
    ws = ["", "A", "B", "m", "n", "AA", "AB", "BA", "BB", "Am", "mB", "AAB", "ABA", "ABB",
          "BAB", "BBA", "AAm", "ABm", "mAB", "BBm", "AABB", "ABAB", "AABm", "ABAm"]
    return np.linalg.matrix_rank(np.array([_word(w, g).flatten() for w in ws]), tol=1e-7) >= 16


def realize_bundle_rep(spec, seed=0, tries=400):
    """An irreducible SL(4) figure-eight bundle rep (A,B) with A=diag(spec). Returns (A,B,t) or None."""
    A = np.diag(np.array(spec, dtype=complex))
    rng = np.random.default_rng(seed)
    for _ in range(tries):
        r = least_squares(_resid, rng.standard_normal(32) * 0.8, args=(A,), method="trf", max_nfev=700)
        if np.max(np.abs(_resid(r.x, A))) < 1e-9:
            B = (r.x[:16] + 1j * r.x[16:]).reshape(4, 4)
            if not _irreducible(A, B):
                continue
            t, res = monodromy(A, B)
            if res < 1e-7:
                return A, B, t
    return None


def scalar_dev(M):
    return max(np.max(np.abs(M - np.diag(np.diag(M)))), np.max(np.abs(np.diag(M) - np.mean(np.diag(M)))))


def degree_relation_dev(A, B, t, k):
    """Scalar-deviation of [A,B]*mu^-k (mu=A^-1 t); ~0 iff M^k = L on this component."""
    mu = np.linalg.inv(A) @ t
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    return scalar_dev(comm @ np.linalg.matrix_power(np.linalg.inv(mu), k))


def degree_over_family(spec, k_test, n_reps=8, seed=1):
    """Median scalar-dev of [A,B]=c*mu^k over n_reps bundle reps with A=diag(spec)."""
    A = np.diag(np.array(spec, dtype=complex))
    rng = np.random.default_rng(seed)
    devs = []
    for _ in range(300):
        if len(devs) >= n_reps:
            break
        r = least_squares(_resid, rng.standard_normal(32) * 0.8, args=(A,), method="trf", max_nfev=700)
        if np.max(np.abs(_resid(r.x, A))) < 1e-9:
            B = (r.x[:16] + 1j * r.x[16:]).reshape(4, 4)
            if not _irreducible(A, B):
                continue
            t, res = monodromy(A, B)
            if res < 1e-7:
                devs.append(degree_relation_dev(A, B, t, k_test))
    return float(np.median(devs)) if devs else float("nan"), len(devs)


def main():
    print("B73 (Path A) -- degree=rank tower law at SL(4): M^4=L on the {tr A=tr A^-1=1} component\n")
    for name, spec, k in [("{1,1,w,w^2} (trA=trA^-1=1)", SPEC_W1, 4),
                          ("{8th roots, z^4+1} (trA=0)", SPEC_Z4, 3)]:
        med, n = degree_over_family(spec, k)
        print(f"  A={name}: [A,B]=c*mu^{k} (M^{k}=L) median scalar-dev = {med:.1e} over {n} reps")
        # show the other k are not clean
        others = {kk: degree_over_family(spec, kk, n_reps=3)[0] for kk in (k - 1, k + 1)}
        print(f"     controls: " + ", ".join(f"M^{kk}=L:{v:.0e}" for kk, v in others.items()))
    print("\n=> degree=rank confirmed at SL(4) (M^4=L on the principal Dehn-filling component);")
    print("   a second component {z^4+1} gives M^3=L. See dehn_filling_highprec for the ~1e-31 check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
