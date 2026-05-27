"""
E11 -- Entropic emergence: does counting alone force departure from the void?

  SPECULATIVE FRONTIER WORK. Outputs are logged observations, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

n-cell binary lattice; compute the multiplicity of each occupancy class and
the exponential suppression of the empty configuration. Save a log-scale plot
of multiplicities for n = 64 to entropy_multiplicity.png.

Run:  python paths/E11_entropic_emergence/probe.py
"""

from math import comb, log

import matplotlib

matplotlib.use("Agg")  # no display required
import matplotlib.pyplot as plt


def total_microstates(n: int) -> int:
    return 2 ** n


def occupancy_multiplicity(n: int, k: int) -> int:
    return comb(n, k)


def peak_multiplicity(n: int) -> int:
    return max(occupancy_multiplicity(n, k) for k in range(n + 1))


def empty_probability_uniform(n: int) -> float:
    return 1.0 / total_microstates(n)


def entropic_pull_from_empty(n: int) -> float:
    """log( peak / 1 ) -- the Boltzmann pull, in units of k_B T, from empty to peak."""
    return log(peak_multiplicity(n))


def save_multiplicity_plot(n: int, path: str) -> None:
    ks = list(range(n + 1))
    mults = [occupancy_multiplicity(n, k) for k in ks]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.semilogy(ks, mults, marker="o", markersize=4, linewidth=1)
    ax.axhline(1.0, color="red", linewidth=1, linestyle="--", label="empty (k=0): 1 microstate")
    ax.set_xlabel("occupancy k (number of occupied cells)")
    ax.set_ylabel("multiplicity  C(n, k)   [log scale]")
    ax.set_title(f"Microstate multiplicity vs occupancy, n = {n}")
    ax.legend(loc="lower center")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    print("=" * 72)
    print("E11 -- entropic emergence probe")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    print(
        "\n  n  |     P(empty)     |  peak multiplicity   | entropic pull  (log)"
    )
    print(
        "  ---+------------------+----------------------+---------------------"
    )
    for n in (2, 4, 8, 16, 32, 64, 128):
        ep = empty_probability_uniform(n)
        pm = peak_multiplicity(n)
        pull = entropic_pull_from_empty(n)
        print(f"  {n:3d}|   {ep:.4e}   |   {pm:.4e}     |   {pull:>8.4f}")

    plot_path = "paths/E11_entropic_emergence/entropy_multiplicity.png"
    save_multiplicity_plot(64, plot_path)
    print(f"\n  saved plot: {plot_path}  (n = 64, log-scale multiplicity)")

    print(
        "\nObservations:\n"
        "  - P(empty) under uniform-over-microstates falls as 2^-n -- exponentially.\n"
        "  - Peak multiplicity at half-filling scales as 2^n / sqrt(n).\n"
        "  - The entropic 'pull' log(peak/empty) grows ~ n*log 2 - (1/2)log(n*pi/2);\n"
        "    linear in n at leading order.\n"
        "  - All three are elementary combinatorics, no free parameters.\n"
    )

    print("[verdict]  See FINDINGS.md. Counting works as a selection INSIDE a")
    print("phase space; it does not construct the phase space itself.")


if __name__ == "__main__":
    main()
