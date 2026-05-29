"""B46 -- rank stability controls."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B46 -- rank stability controls")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    t = sp.symbols("t")
    sl3_char = sp.factor((t - 1) * (t + 1) * (t**2 - 4 * t - 1) * (t**2 - 3 * t + 1) * (t**2 + t - 1))
    selected = t**2 - 3 * t + 1
    nearby = t**2 - 4 * t + 1

    print("\n[1] selected sector divisibility")
    quotient_selected, remainder_selected = sp.div(sl3_char, selected, domain=sp.QQ)
    print(f"    quotient = {sp.factor(quotient_selected)}")
    print(f"    remainder = {remainder_selected}")
    assert remainder_selected == 0

    print("\n[2] nearby sector control")
    _, remainder_nearby = sp.div(sl3_char, nearby, domain=sp.QQ)
    print(f"    remainder for t^2-4t+1 = {remainder_nearby}")
    assert remainder_nearby != 0

    print("\nVerdict: STALLED")
    print("The selected A-sector is stable in the known SL(3) lift, but higher")
    print("rank consistency does not derive the selector.")


if __name__ == "__main__":
    main()
