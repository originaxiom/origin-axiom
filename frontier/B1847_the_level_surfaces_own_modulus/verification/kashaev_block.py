"""Data-free, for main's ruling on B1012 (S306d): the figure-eight's single holomorphic block at q = e^{2 pi i/N} -- the
Kashaev invariant <4_1>_N = sum_{m<N} prod_{j<=m} |1 - q^j|^2 -- against the leading exponential exp(N Vol/2pi) and the
proven asymptotic 3^(-1/4) N^(3/2) exp(N Vol/2pi) (Andersen-Hansen; named, not re-derived). Knot invariants only: no
scale, coupling or ratio is computed."""
import mpmath as mp
mp.mp.dps = 30
VOL = mp.mpf("2.029883212819307250042405108549")


def kashaev(N):
    q = mp.e ** (2j * mp.pi / N); s = mp.mpf(0); prod = mp.mpf(1)
    for m in range(N):
        if m > 0:
            prod *= abs(1 - q ** m) ** 2
        s += prod
    return s


if __name__ == "__main__":
    print(" N   exact            exp(N Vol/2pi)   full asymptotic    exact/full")
    for N in (3, 5, 10, 20, 40, 80):
        ex = kashaev(N); lead = mp.e ** (N * VOL / (2 * mp.pi)); full = 3 ** mp.mpf(-0.25) * N ** 1.5 * lead
        print(f"{N:3d}  {mp.nstr(ex, 12):>16s}  {mp.nstr(lead, 10):>14s}  {mp.nstr(full, 12):>16s}   {mp.nstr(ex / full, 8)}")
    print("N = 5: 46 + 2 sqrt5 =", mp.nstr(46 + 2 * mp.sqrt(5), 15))
