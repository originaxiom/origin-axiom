"""
E5 -- Vilenkin tunneling from nothing: does the mainstream answer work?

  SPECULATIVE FRONTIER WORK. Outputs are logged observations, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

Minisuperspace Wheeler-DeWitt equation for closed FRW + Lambda:

    [-d^2/da^2 + V(a)] psi(a) = 0,    V(a) = a^2 - (Lambda/3) a^4

Barrier: 0 < a < a_max = sqrt(3 / Lambda).  Compute the WKB tunneling
exponent B(Lambda) = integral_0^{a_max} sqrt(V(a)) da both analytically and
numerically, and the tunneling-amplitude suppression exp(-2 B).

Saves two plots:
  vilenkin_barrier.png  -- V(a) for several Lambda
  vilenkin_psi.png      -- WKB |psi(a)| for Lambda = 1, across and beyond barrier

Run:  python paths/E5_vilenkin_tunneling/probe.py
"""

from math import exp, sqrt

import numpy as np
import matplotlib

matplotlib.use("Agg")  # no display required
import matplotlib.pyplot as plt
from scipy.integrate import quad


def V(a: float, Lam: float) -> float:
    """Minisuperspace potential for closed FRW + cosmological constant."""
    return a * a - (Lam / 3.0) * a ** 4


def a_max(Lam: float) -> float:
    """Outer classical turning point: V(a_max) = 0."""
    return sqrt(3.0 / Lam)


def B_analytic(Lam: float) -> float:
    """Closed-form WKB barrier integral B(Lambda) = 1 / Lambda.

    Derivation: B = integral_0^{a_max} a sqrt(1 - (Lambda/3) a^2) da.
    Substitute u = (Lambda/3) a^2, du = (2 Lambda/3) a da:
        B = (3 / (2 Lambda)) * integral_0^1 sqrt(1 - u) du
          = (3 / (2 Lambda)) * (2/3)
          = 1 / Lambda
    """
    return 1.0 / Lam


def B_numeric(Lam: float) -> float:
    """Cross-check by numerical quadrature."""
    amax = a_max(Lam)
    integrand = lambda a: sqrt(max(V(a, Lam), 0.0))
    val, _err = quad(integrand, 0.0, amax)
    return val


def wkb_psi_under_barrier(a: float, Lam: float) -> float:
    """WKB amplitude under the barrier: exp(-integral_a^{a_max} sqrt(V) da').

    Normalized so psi(a_max) = 1.  Strictly the prefactor V^{-1/4} also
    appears; we omit it here -- this routine is for visualisation only.
    """
    amax = a_max(Lam)
    if a >= amax:
        return 1.0
    integrand = lambda ap: sqrt(max(V(ap, Lam), 0.0))
    val, _ = quad(integrand, a, amax)
    return exp(-val)


def save_barrier_plot(path: str) -> None:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    a_grid = np.linspace(0.0, 6.0, 600)
    for Lam in (0.1, 0.3, 1.0, 3.0):
        ax.plot(a_grid, [V(a, Lam) for a in a_grid], label=f"Lambda = {Lam}")
        amax = a_max(Lam)
        ax.axvline(amax, linestyle=":", linewidth=0.8, alpha=0.5)
    ax.axhline(0.0, color="black", linewidth=0.6)
    ax.set_xlabel("scale factor  a")
    ax.set_ylabel("V(a) = a^2 - (Lambda/3) a^4")
    ax.set_title("Wheeler-DeWitt barrier (closed FRW + Lambda)")
    ax.set_ylim(-3.0, 3.0)
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_psi_plot(path: str, Lam: float = 1.0) -> None:
    amax = a_max(Lam)
    a_grid = np.linspace(0.0, 1.6 * amax, 400)
    psi = np.array([wkb_psi_under_barrier(a, Lam) for a in a_grid])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(a_grid, psi, label="|psi(a)|  (WKB, prefactor dropped)")
    ax.axvline(amax, color="red", linestyle="--", linewidth=1, label=f"a_max = sqrt(3/Lambda) = {amax:.3f}")
    ax.axhline(exp(-B_analytic(Lam)), color="gray", linestyle=":", linewidth=1,
               label=f"|psi(0)| ~ exp(-B) = exp(-1/Lambda) = {exp(-B_analytic(Lam)):.3f}")
    ax.set_xlabel("scale factor  a")
    ax.set_ylabel("|psi(a)|  (under-barrier WKB)")
    ax.set_title(f"Vilenkin tunneling wavefunction, Lambda = {Lam}")
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    print("=" * 72)
    print("E5 -- Vilenkin tunneling from nothing")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    print(
        "\n  Lambda  |  a_max = sqrt(3/Lambda) |  B_analytic = 1/Lambda |  B_numeric  |  exp(-2B)"
    )
    print(
        "  --------+-------------------------+------------------------+-------------+-----------------"
    )
    for Lam in (0.1, 0.3, 1.0, 3.0, 10.0):
        amax = a_max(Lam)
        Ba = B_analytic(Lam)
        Bn = B_numeric(Lam)
        suppression = exp(-2.0 * Ba)
        print(
            f"   {Lam:5.2f} |        {amax:7.4f}          |        {Ba:7.4f}         |  {Bn:7.4f}    |  {suppression:.4e}"
        )

    # Cross-check: analytic vs numeric should agree to quadrature tolerance.
    max_err = max(
        abs(B_analytic(Lam) - B_numeric(Lam)) for Lam in (0.1, 0.3, 1.0, 3.0, 10.0)
    )
    print(f"\n  max |B_analytic - B_numeric| = {max_err:.3e}  (quadrature noise)")

    save_barrier_plot("paths/E5_vilenkin_tunneling/vilenkin_barrier.png")
    save_psi_plot("paths/E5_vilenkin_tunneling/vilenkin_psi.png", Lam=1.0)
    print("\n  saved  paths/E5_vilenkin_tunneling/vilenkin_barrier.png")
    print("  saved  paths/E5_vilenkin_tunneling/vilenkin_psi.png   (Lambda = 1)")

    print(
        "\nObservations:\n"
        "  - B(Lambda) = 1/Lambda exactly (natural units; dimensionful conventions\n"
        "    multiply by O(1) factors like 3 pi /(2 G), depending on ordering).\n"
        "  - The tunneling amplitude exp(-2 B) is non-zero for any Lambda > 0.\n"
        "  - For small Lambda (large universe) the suppression is severe;\n"
        "    for large Lambda (small universe) the barrier almost vanishes.\n"
        "  - The Lambda dependence is the only free knob in this minisuperspace.\n"
    )

    print("[verdict]  See FINDINGS.md. The amplitude is non-zero, but 'nothing'")
    print("in this setup is the a=0 boundary of a Hilbert space that already")
    print("encodes FRW cosmology, the minisuperspace truncation, and Lambda.")


if __name__ == "__main__":
    main()
