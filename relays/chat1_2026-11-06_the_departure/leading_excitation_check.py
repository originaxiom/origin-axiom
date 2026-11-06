"""The web seat, 2026-11-06: THE PRINCIPLE'S LEADING EXCITATION (PREREGISTRATION_LEADING_EXCITATION.md). Data-free
arithmetic on the principle's own measure (P-441's golden end). No coupling, scale ratio or held-out quantity.

  D_n = (n - 1) * 2 log phi - dS_n, dS_n = 2 log((n - 1 + sqrt5)/sqrt5): the length a run of n loses at fixed moves.
  P1: D_n for n = 2..60 and its monotonicity; P2: the leading departure overall and in the line sector (n = 1 mod 5);
  P3: the run of 6's share of the sector at |s| = 0.25, 0.5, 1, 2; P4: the departures per golden position
  sum_{n >= 2} e^(-|s| D_n), the |s| where it falls below 0.1, and the run of 6's fraction of all departures there.

    python3 leading_excitation_check.py
"""
import mpmath as mp

mp.mp.dps = 40
SQ5 = mp.sqrt(5)
PHI = (1 + SQ5) / 2
N_MAX = 60
S_VALUES = (mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf(1), mp.mpf(2))


def D(n):
    return (n - 1) * 2 * mp.log(PHI) - 2 * mp.log((n - 1 + SQ5) / SQ5)


def per_position(s):
    return mp.nsum(lambda n: mp.e ** (-s * D(n)), [2, mp.inf])


if __name__ == "__main__":
    print("THE PRINCIPLE'S LEADING EXCITATION -- data-free check (the web seat, 2026-11-06)")
    vals = {n: D(n) for n in range(2, N_MAX + 1)}
    for n in (2, 3, 4, 5, 6, 7, 11, 16, 21, 26):
        print("  D_%d = %s" % (n, mp.nstr(vals[n], 10)))
    print("  D_n positive for 2 <= n <= %d: %s; increasing: %s" % (
        N_MAX, all(v > 0 for v in vals.values()), all(vals[n + 1] > vals[n] for n in range(2, N_MAX))))
    lead_all = min(vals, key=lambda n: vals[n])
    lead_sec = min((n for n in vals if n % 5 == 1 and n >= 6), key=lambda n: vals[n])
    print("  the leading departure overall: run %d; in the line sector: run %d" % (lead_all, lead_sec))
    for s in S_VALUES:
        sec = mp.nsum(lambda m: mp.e ** (-s * D(5 * m + 1)), [1, mp.inf])
        print("  |s| = %s: the run of 6's share of the sector %s" % (mp.nstr(s, 3), mp.nstr(mp.e ** (-s * D(6)) / sec, 8)))
    s_star = mp.findroot(lambda s: per_position(s) - mp.mpf("0.1"), 10)
    frac6 = mp.e ** (-s_star * D(6)) / per_position(s_star)
    print("  departures per golden position fall to 0.1 at |s| = %s; there the run of 6 is %s of all departures" % (
        mp.nstr(s_star, 8), mp.nstr(frac6, 6)))
    print("leading_excitation_check exit 0")
