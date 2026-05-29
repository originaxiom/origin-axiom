"""B24 -- anyon / quantum bridge controls."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B24 -- Anyon / quantum bridge")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    k = sp.symbols("k", integer=True, nonnegative=True)
    phi = (1 + sp.sqrt(5)) / 2
    matches = []
    for kv in range(1, 11):
        dim = sp.simplify(2 * sp.cos(sp.pi / (kv + 2)))
        if sp.simplify(dim - phi) == 0:
            matches.append(kv)
    assert matches == [3]
    print("    2*cos(pi/(k+2))=phi only at k=3 for k=1..10")

    discriminant = 5
    assert matches[0] + 2 == discriminant
    print("    k+2=5 matches the discriminant/index number")
    print("    no rule deriving the +2 shift is supplied")

    print("\nVerdict: STALLED")
    print("k=3 is compatible, not derived.")


if __name__ == "__main__":
    main()
