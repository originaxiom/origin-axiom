"""B33 -- SL(n) trace tower.

Explains the known SL(2)/SL(3) spectra by symmetric-power sectors and stops
before claiming a full SL(n) trace-coordinate theorem.
"""

from __future__ import annotations

import sympy as sp


def sym_power_charpoly(power: int, t: sp.Symbol) -> sp.Expr:
    """Exact reduced sector polynomials for the low-rank checks.

    The roots are powers of the half-step eigenvalues `phi` and `-1/phi`.
    Writing the reduced polynomials directly avoids depending on Sympy's
    simplification of `GoldenRatio` powers.
    """

    if power == 2:
        return sp.factor((t + 1) * (t**2 - 3 * t + 1))
    if power == 3:
        return sp.factor((t**2 - 4 * t - 1) * (t**2 + t - 1))
    if power == 4:
        return sp.factor((t - 1) * (t**2 + 3 * t + 1) * (t**2 - 7 * t + 1))
    raise ValueError("only low-rank sector controls are implemented")


def main() -> None:
    print("=" * 72)
    print("B33 -- SL(n) trace tower")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    t = sp.symbols("t")
    sym2 = sym_power_charpoly(2, t)
    sym3 = sym_power_charpoly(3, t)
    known_sl2 = sp.factor((t + 1) * (t**2 - 3 * t + 1))
    known_sl3 = sp.factor((t - 1) * (t + 1) * (t**2 - 4 * t - 1) * (t**2 - 3 * t + 1) * (t**2 + t - 1))

    print("\n[1] SL(2) sector")
    print(f"    Sym^2(F) = {sym2}")
    print(f"    known SL(2) trace-map char = {known_sl2}")
    assert sp.factor(sym2 - known_sl2) == 0

    print("\n[2] SL(3) sector decomposition")
    decomposition = sp.factor(sym3 * sym2 * (t - 1))
    print(f"    Sym^3(F) = {sym3}")
    print(f"    Sym^3(F)*Sym^2(F)*(t-1) = {decomposition}")
    print(f"    known SL(3) char = {known_sl3}")
    assert sp.factor(decomposition - known_sl3) == 0

    print("\n[3] extrapolation target, not a theorem")
    sym4 = sym_power_charpoly(4, t)
    print(f"    Sym^4(F) candidate sector = {sym4}")
    assert sp.degree(sym4, t) == 5

    print("\nVerdict: STALLED")
    print("Ranks 2 and 3 fit a symmetric-power tower, but the full SL(n)")
    print("trace-coordinate lift has not been constructed.")


if __name__ == "__main__":
    main()
