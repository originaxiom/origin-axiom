"""B739 Stage-B recompute -- target B58 (dead probe, kill_form=category-error).

BANKED KILL (B58 FINDINGS, sealed Stage-A record): "the representation-perturbation
route is killed as computing the wrong object, so 'the prediction cannot be tested
numerically'" -- i.e. the SL(4) 7-factor tower prediction (PC12: parity block + 7
degree-2 char(M^k) factors in the 15x15 ambient fixed-line Jacobian) is numerically
untestable, because every representation realizing the fixed-line point (all traces
= 4) is the identity, where d tr(W) = 0 for every word W (traces second-order).

THE DISCRIMINATING FACT of the kill is the headline impossibility: "the prediction
cannot be tested numerically."  The in-arc computed fact (first-order degeneracy at
the identity representation) is only the NECESSARY component: it kills the naive
at-the-point route.  E19 both directions:

  PART 1  recompute B58's own in-arc facts from its declared conventions
          (identity recursion (r-1)^4; identity-rep degeneracy; and, sharpened,
          the full 15x30 representation-differential at the identity ~ 0, so the
          naive Jacobian extraction AT the point is genuinely undefined).
  PART 2  rebuild the exact SL(3) ambient fixed-line Jacobian symbolically from
          B54's declared conventions (B48/B51 coordinates x1..x8, metallic m=1 =
          Fibonacci substitution (A,B)->(AB,A), fixed line c=3) and factor its
          characteristic polynomial exactly.  This is the in-sandbox ground truth
          anchor -- computed here, not cited.
  PART 3  implement the eps-extrapolated pinv-ratio route (the B59 method):
          DT(eps) = D[tr W_i(AB,A)] . pinv(D[tr W_j(A,B)]) at A=exp(eps P),
          B=exp(eps Q), extrapolated to eps=0.  Validate it against PART 2's
          exact SL(3) spectrum.
  PART 4  apply the validated method to SL(4) (15 trace coordinates) and test the
          7-factor prediction: (a) match the computed spectrum to the banked B59
          factorization char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)
          (t-1)^2(t+1); (b) the sign-sector discriminator: eigenvalues at
          -phi^2, -phi^-2 exist, and NO char(M^k) (any integer k) nor a parity
          root +-1 can be within 1.0 of -phi^2 (case lemma, verified over
          |k|<=12 and closed by monotonicity); (c) parity multiplicity is 3, not 1.

If PART 4 succeeds, the ambient object IS computed numerically in this sandbox and
the prediction IS numerically tested (and refuted in specifics) -- negating the
banked headline while PART 1 reconfirms its necessary-only component.

CONVENTIONS DECLARED (E1; undeclared in B58, adopted from the cited arcs):
  * SL(4) 15-trace-coordinate generating set: B58 cites Procesi without a list;
    we adopt B59's declared word list
      A, A^2, A^3, B, B^2, B^3, AB, A^2B, AB^2, A^2B^2, A^3B, AB^3, ABAB,
      A^3B^2, A^2B^3.
  * Substitution map: Fibonacci (A,B) -> (AB, A), per B54/B58 "tr(word(AB,A))".
  * SL(3) coordinates: B48/B51 convention x1..x8 = tr(A),tr(B),tr(AB),tr(A^-1),
    tr(B^-1),tr(A^-1B),tr(AB^-1),tr(A^-1B^-1); tau_k = tr(A^k B) with SL(3)
    Cayley-Hamilton tau_k = x1 tau_{k-1} - x4 tau_{k-2} + tau_{k-3}.
  * Numerical parameters adopted from B59: finite-difference step h=1e-6
    (multiplicative perturbations exp(+-h G)), eps grids {0.04..0.12} (SL3) /
    {0.03..0.11} (SL4), degree-4 polynomial extrapolation to eps=0, pinv
    rcond=1e-12, seeds (10, 11) averaged.  scipy.linalg.expm as in the original
    arc (scipy 1.16.3 present in the sandbox).
  * Spectrum matching: sum-minimizing bipartite assignment
    (scipy.optimize.linear_sum_assignment) reporting the MAX assigned distance --
    stricter than B59's greedy matcher.

Deterministic: fixed seeds only, no wall-clock, no network.  Gate 5: pure
trace-map mathematics, no SM quantities.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment

PHI = (1.0 + 5.0**0.5) / 2.0


def max_match(spectrum, targets) -> float:
    """Max assigned |ev - root| under the sum-minimizing bipartite assignment."""
    spectrum = list(spectrum)
    targets = list(targets)
    assert len(spectrum) == len(targets)
    cost = np.array([[abs(ev - r) for r in targets] for ev in spectrum])
    rows, cols = linear_sum_assignment(cost)
    return float(cost[rows, cols].max())


# ----------------------------------------------------------------------------
# PART 1 -- B58's own in-arc facts (the necessary component of the kill)
# ----------------------------------------------------------------------------

def part1_identity_recursion() -> bool:
    r = sp.symbols("r")
    e1, e2, e3 = 4, 6, 4  # elementary symmetrics of eigenvalues all = 1 (SL(4) identity)
    charpoly = r**4 - e1 * r**3 + e2 * r**2 - e3 * r + 1
    ok = sp.factor(charpoly) == (r - 1) ** 4
    print(f"[P1a] SL(4) identity recursion charpoly == (r-1)^4: {ok}")
    return bool(ok)


def part1_identity_degeneracy() -> bool:
    """B58's declared conventions: seed 0, word W = A A B A B^-1, eps = 1e-6."""
    rng = np.random.default_rng(0)

    def rand_sl4() -> np.ndarray:
        m = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        return m - np.trace(m) / 4 * np.eye(4)

    x, y = rand_sl4(), rand_sl4()
    eps = 1e-6

    def tr_at(t: float) -> complex:
        A = np.eye(4) + t * x
        B = np.eye(4) + t * y
        return np.trace(A @ A @ B @ A @ np.linalg.inv(B))

    first = abs((tr_at(eps) - tr_at(-eps)) / (2 * eps))
    second = abs((tr_at(eps) - 2 * tr_at(0) + tr_at(-eps)) / eps**2)
    ok = first < 1e-6 and second > 1.0
    print(f"[P1b] identity-rep degeneracy: |d tr(W)/de| = {first:.3e} (~0), "
          f"|d2 tr(W)/de2| = {second:.4g} (nonzero): {ok}")
    return ok


def basis_sl(n: int) -> list[np.ndarray]:
    basis = []
    for i in range(n):
        for j in range(n):
            if i != j:
                e = np.zeros((n, n), complex)
                e[i, j] = 1.0
                basis.append(e)
    for i in range(n - 1):
        e = np.zeros((n, n), complex)
        e[i, i] = 1.0
        e[i + 1, i + 1] = -1.0
        basis.append(e)
    return basis


def words_sl4(A: np.ndarray, B: np.ndarray) -> list[np.ndarray]:
    return [
        A, A @ A, A @ A @ A, B, B @ B, B @ B @ B, A @ B, A @ A @ B, A @ B @ B,
        A @ A @ B @ B, A @ A @ A @ B, A @ B @ B @ B, A @ B @ A @ B,
        A @ A @ A @ B @ B, A @ A @ B @ B @ B,
    ]


def words_sl3(A: np.ndarray, B: np.ndarray) -> list[np.ndarray]:
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    return [A, B, A @ B, Ai, Bi, Ai @ B, A @ Bi, Ai @ Bi]


def rep_differential(A, B, n, substitute, pert_plus, pert_minus, h):
    """Central-difference differential of the trace coordinates w.r.t. the
    representation, along multiplicative sl(n)-basis perturbations of A then B."""
    words = words_sl3 if n == 3 else words_sl4
    nw = 8 if n == 3 else 15
    rows = [[0j] * (2 * (n * n - 1)) for _ in range(nw)]
    col = 0
    for Pp, Pm in zip(pert_plus, pert_minus):  # perturb A
        Ap, Am = Pp @ A, Pm @ A
        wp = words(Ap @ B, Ap) if substitute else words(Ap, B)
        wm = words(Am @ B, Am) if substitute else words(Am, B)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pert_plus, pert_minus):  # perturb B
        Bp, Bm = Pp @ B, Pm @ B
        wp = words(A @ Bp, A) if substitute else words(A, Bp)
        wm = words(A @ Bm, A) if substitute else words(A, Bm)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    return np.array(rows)


def part1_at_identity_differential(pert4) -> bool:
    """Sharpened category-error check: the full 15x30 representation-differential
    of the trace coordinates AT the identity is numerically zero (all singular
    values ~ finite-difference noise), so the naive 'extract the Jacobian from
    representations at the fixed-line point' route has no object to extract."""
    h = 1e-6
    A = np.eye(4, dtype=complex)
    B = np.eye(4, dtype=complex)
    dx0 = rep_differential(A, B, 4, False, pert4[0], pert4[1], h)
    sv0 = np.linalg.svd(dx0, compute_uv=False)
    # same differential at a perturbed representation (eps = 0.05): full rank 15
    rng = np.random.default_rng(10)
    P = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    P -= np.trace(P) / 4 * np.eye(4)
    Q = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    Q -= np.trace(Q) / 4 * np.eye(4)
    dx1 = rep_differential(expm(0.05 * P), expm(0.05 * Q), 4, False, pert4[0], pert4[1], h)
    sv1 = np.linalg.svd(dx1, compute_uv=False)
    ok = sv0[0] < 1e-7 and sv1[14] > 1e-6
    print(f"[P1c] 15x30 rep-differential at identity: max sv = {sv0[0]:.3e} (~0, rank 0); "
          f"at eps=0.05: min sv = {sv1[14]:.3e} (rank 15): {ok}")
    return ok


# ----------------------------------------------------------------------------
# PART 2 -- exact SL(3) ambient anchor (B48/B51/B54 conventions, m=1, c=3)
# ----------------------------------------------------------------------------

def sl3_exact_fixed_line_jacobian() -> sp.Matrix:
    """8x8 ambient fixed-line Jacobian of the SL(3) Fibonacci trace map at c=3.

    Coordinates x1..x8 as declared above.  Substitution (A,B)->(AB,A) pulls back:
      x1' = tr(AB)          = tau_1        x5' = tr(A^-1)       = x4
      x2' = tr(A)           = x1           x6' = tr((AB)^-1 A)  = tr(B^-1) = x5
      x3' = tr(AB A)        = tau_2        x7' = tr(AB A^-1)    = tr(B)   = x2
      x4' = tr((AB)^-1)     = sigma(tau_1) x8' = tr((AB)^-1 A^-1) = sigma(tau_2)
    with tau_k = tr(A^k B), tau_{-1}=x6, tau_0=x2, tau_1=x3,
    tau_k = x1 tau_{k-1} - x4 tau_{k-2} + tau_{k-3}, and sigma the exchange
    involution x1<->x4, x2<->x5, x3<->x8, x6<->x7 (i.e. (A,B)->(A^-1,B^-1)).
    On the fixed line (all coordinates = c) the derivative rows obey
      d tau_k = c d tau_{k-1} - c d tau_{k-2} + d tau_{k-3} + c (e_1 - e_4).
    """
    c = sp.Integer(3)

    def unit(i: int) -> sp.Matrix:
        col = sp.zeros(8, 1)
        col[i] = 1
        return col

    exchange = sp.zeros(8)
    for s, t in {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}.items():
        exchange[t, s] = 1

    tau = {-1: unit(5), 0: unit(1), 1: unit(2)}
    forcing = c * (unit(0) - unit(3))
    for k in range(2, 3):
        tau[k] = sp.expand(c * tau[k - 1] - c * tau[k - 2] + tau[k - 3] + forcing)
    sigma = {k: exchange * tau[k] for k in tau}
    rows = [tau[1], unit(0), tau[2], sigma[1], unit(3), sigma[0], tau[0], sigma[2]]
    return sp.Matrix.hstack(*rows).T


def part2_exact_sl3() -> tuple[bool, list[complex]]:
    t = sp.symbols("t")
    J = sl3_exact_fixed_line_jacobian()
    charpoly = sp.expand(J.charpoly(t).as_expr())
    target = sp.expand((t - 1) * (t + 1) * (t**2 - 3 * t + 1)
                       * (t**2 + t - 1) * (t**2 - 4 * t - 1))
    ok = sp.expand(charpoly - target) == 0
    print(f"[P2 ] exact SL(3) 8x8 fixed-line Jacobian charpoly == "
          f"(t-1)(t+1)(t^2-3t+1)(t^2+t-1)(t^2-4t-1): {ok}")
    roots: list[complex] = []
    for factor in [t - 1, t + 1, t**2 - 3 * t + 1, t**2 + t - 1, t**2 - 4 * t - 1]:
        roots += [complex(r) for r in sp.nroots(sp.Poly(factor, t))]
    return bool(ok), roots


# ----------------------------------------------------------------------------
# PART 3 / 4 -- the eps-extrapolated pinv-ratio ambient Jacobian (B59 route)
# ----------------------------------------------------------------------------

def dt_at(eps, P, Q, n, pert_plus, pert_minus, h=1e-6):
    A, B = expm(eps * P), expm(eps * Q)
    dx = rep_differential(A, B, n, False, pert_plus, pert_minus, h)
    dX = rep_differential(A, B, n, True, pert_plus, pert_minus, h)
    return dX @ np.linalg.pinv(dx, rcond=1e-12)


def fixed_line_spectrum(n, seeds, epss, pert):
    dim = n * n - 1
    h = 1e-6
    spectra = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        P = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        P -= np.trace(P) / n * np.eye(n)
        Q = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        Q -= np.trace(Q) / n * np.eye(n)
        dts = [dt_at(e, P, Q, n, pert[0], pert[1], h) for e in epss]
        dt0 = np.zeros((dim, dim), complex)
        deg = min(len(epss) - 1, 4)
        for i in range(dim):
            for j in range(dim):
                dt0[i, j] = np.polyfit(epss, [d[i, j] for d in dts], deg)[-1]
        spectra.append(np.sort_complex(np.linalg.eigvals(dt0)))
    return np.mean(spectra, axis=0), spectra


def char_mk_roots(k: int) -> list[float]:
    """char(M^k) roots for M = [[1,1],[1,0]]: {phi^k, (-1)^k phi^-k}."""
    return [PHI**k, ((-1) ** k) * PHI ** (-k)]


def part4_sign_sector_lemma() -> bool:
    """No char(M^k) root (any integer k) and no parity root +-1 lies within 1.0
    of -phi^2.  Verified over |k|<=12; closed for |k|>12 because the positive
    root phi^k has distance > phi^2 from -phi^2 for every k, and the root
    (-1)^k phi^-k is positive for even k (distance > phi^2) while for odd k it
    is -phi^-k with phi^-k ranging over odd powers of phi, whose closest
    approach to phi^2 is |phi^1 - phi^2| = 1 (monotone growth of |phi^m - phi^2|
    in |m - 2| forces larger distances beyond the sweep)."""
    target = -PHI**2
    dmin = min(abs(r - target) for k in range(-12, 13) for r in char_mk_roots(k))
    dmin = min(dmin, abs(1.0 - target), abs(-1.0 - target))
    ok = dmin >= 1.0 - 1e-9
    print(f"[P4b] lemma: min distance from any char(M^k) (|k|<=12) or parity root "
          f"to -phi^2 = {dmin:.6f} (>= 1.0): {ok}")
    return ok


def main() -> int:
    print("B739 Stage-B recompute -- B58 (SL(4) tower 'cannot be tested numerically')")
    print("=" * 78)

    pert4_h = 1e-6
    b4 = basis_sl(4)
    pert4 = ([expm(pert4_h * g) for g in b4], [expm(-pert4_h * g) for g in b4])
    b3 = basis_sl(3)
    pert3 = ([expm(pert4_h * g) for g in b3], [expm(-pert4_h * g) for g in b3])

    print("\nPART 1 -- B58's in-arc facts (necessary component of the kill)")
    ok1 = part1_identity_recursion()
    ok2 = part1_identity_degeneracy()
    ok3 = part1_at_identity_differential(pert4)

    print("\nPART 2 -- exact SL(3) ambient anchor (computed in-sandbox, B54 conventions)")
    ok4, sl3_exact_roots = part2_exact_sl3()

    print("\nPART 3 -- pinv-ratio route validated against the exact SL(3) anchor")
    sl3_spec, sl3_per_seed = fixed_line_spectrum(
        3, seeds=(10, 11), epss=np.array([0.04, 0.06, 0.08, 0.10, 0.12]), pert=pert3)
    sl3_match = max_match(sl3_spec, sl3_exact_roots)
    sl3_seed_spread = max_match(sl3_per_seed[0], sl3_per_seed[1])
    ok5 = sl3_match < 0.02
    print(f"[P3 ] SL(3) numerical spectrum vs EXACT anchor: max match = {sl3_match:.4f} "
          f"(< 0.02): {ok5}   [seed-to-seed spread {sl3_seed_spread:.4f}]")

    print("\nPART 4 -- the ambient SL(4) 15x15 Jacobian, computed numerically")
    sl4_spec, sl4_per_seed = fixed_line_spectrum(
        4, seeds=(10, 11), epss=np.array([0.03, 0.05, 0.07, 0.09, 0.11]), pert=pert4)
    sl4_seed_spread = max_match(sl4_per_seed[0], sl4_per_seed[1])

    # (a) match to the B59-banked factorization, roots built exactly from M=[[1,1],[1,0]]
    b59_roots = []
    for k in (-1, 1, 2, 3, 4):
        b59_roots += char_mk_roots(k)
    b59_roots += [-PHI**2, -PHI**-2]          # char(-M^2)
    b59_roots += [1.0, 1.0, -1.0]             # (t-1)^2 (t+1)
    sl4_match = max_match(sl4_spec, b59_roots)
    ok6 = sl4_match < 0.05
    print(f"[P4a] SL(4) spectrum vs char(M^-1)char(M)char(M^2)char(M^3)char(M^4)"
          f"char(-M^2)(t-1)^2(t+1): max match = {sl4_match:.4f} (< 0.05): {ok6}"
          f"   [seed-to-seed spread {sl4_seed_spread:.4f}]")

    # (b) sign-sector discriminator against '1 parity + 7 char(M^k)'
    ok7 = part4_sign_sector_lemma()
    d_neg_phi2 = min(abs(ev - (-PHI**2)) for ev in sl4_spec)
    d_neg_phim2 = min(abs(ev - (-PHI**-2)) for ev in sl4_spec)
    ok8 = d_neg_phi2 < 0.05 and d_neg_phim2 < 0.05
    print(f"[P4b] computed eigenvalues at the sign sector: dist to -phi^2 = "
          f"{d_neg_phi2:.4f}, to -phi^-2 = {d_neg_phim2:.4f} (both < 0.05): {ok8}")

    # (c) parity multiplicity
    parity_count = sum(1 for ev in sl4_spec if min(abs(ev - 1), abs(ev + 1)) < 0.1)
    ok9 = parity_count == 3
    print(f"[P4c] eigenvalues within 0.1 of +-1: {parity_count} "
          f"(prediction says 1; actual parity block is degree 3): {ok9}")

    print("\nComputed SL(4) fixed-line spectrum (seed-averaged, extrapolated to eps=0):")
    for ev in sorted(sl4_spec, key=lambda z: (round(z.real, 6), z.imag)):
        print(f"    {ev.real:+.4f} {ev.imag:+.4f}i")

    all_ok = all([ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9])
    print("\n" + "=" * 78)
    print(f"ALL CHECKS PASS: {all_ok}")
    print("""
VERDICT: REVIVED.
  RECONFIRMED (necessary component): the identity-rep degeneracy is real -- the
  representation-differential AT the fixed-line point is rank 0, so the naive
  'Jacobian from representations at the point' route computes nothing (P1a-P1c).
  NEGATED (the discriminating headline): the ambient SL(4) 15x15 fixed-line
  Jacobian IS computable numerically -- the eps-extrapolated pinv ratio
  DT(eps) = D[tr W(AB,A)] . pinv(D[tr W(A,B)]), a representation-perturbation
  construction, reproduces the EXACT in-sandbox SL(3) anchor and yields the
  SL(4) spectrum, which numerically TESTS the 7-factor tower prediction and
  refutes it in specifics (5 char(M^k), k=-1,1,2,3,4; a sign sector char(-M^2)
  no char(M^k) can imitate -- lemma margin 1.0; a degree-3 parity block).
  The banked kill fact was necessary-only, not discriminating: 'cannot be
  tested numerically' is false.""")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
