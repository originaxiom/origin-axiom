"""The web seat, 2026-11-06: THE CLOCK AND THE LINE SECTOR (PREREGISTRATION_CLOCK.md). Data-free arithmetic on weights
of histories. No coupling, scale ratio or held-out quantity is computed; the weights' parameters are generic. Volumes
are not recomputed (P-476 has them).

For the line sector's departures (runs n = 1 mod 5, n >= 6): the share of the run of 6, and the sector's share of all
departures (n >= 2), under the move clock's fair-coin law, the length clock's single-departure weights at s = 1 and 2,
and the Liouville (Gauss-Kuzmin) run law.

    python3 clock_check.py
"""
import mpmath as mp

mp.mp.dps = 40
SQ5 = mp.sqrt(5)


def laws():
    return {
        "moves (fair coin, 2^-(n-1))": lambda n: mp.mpf(2) ** (-(n - 1)),
        "length, s = 1 (e^(-dS_n))": lambda n: ((n - 1 + SQ5) / SQ5) ** (-2),
        "length, s = 2 (e^(-2 dS_n))": lambda n: ((n - 1 + SQ5) / SQ5) ** (-4),
        "Gauss-Kuzmin (Liouville)": lambda n: mp.log(1 + mp.mpf(1) / (n * (n + 2)), 2),
    }


if __name__ == "__main__":
    print("THE CLOCK AND THE LINE SECTOR -- data-free check (the web seat, 2026-11-06)")
    for name, w in laws().items():
        sector = mp.nsum(lambda m: w(5 * m + 1), [1, mp.inf])
        alldep = mp.nsum(lambda n: w(n), [2, mp.inf])
        print("  %-30s share of the run of 6 in the sector %s; the sector's share of all departures %s" % (
            name, mp.nstr(w(6) / sector, 8), mp.nstr(sector / alldep, 6)))
        print("  %-30s next sector members: run 11 %s, run 16 %s" % (
            "", mp.nstr(w(11) / sector, 6), mp.nstr(w(16) / sector, 6)))
    print("  exact check: moves share = 31/32 = %s" % mp.nstr(mp.mpf(31) / 32, 8))
    print("clock_check exit 0")
