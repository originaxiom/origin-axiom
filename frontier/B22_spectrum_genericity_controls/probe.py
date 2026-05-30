"""B22 -- spectrum genericity controls."""

from __future__ import annotations

from collections import Counter
import sympy as sp


def sym2_charpoly(M: sp.Matrix, t: sp.Symbol) -> sp.Expr:
    tr = M.trace()
    det = M.det()
    return sp.factor((t - det) * (t**2 - (tr**2 - 2 * det) * t + det**2))


def main() -> None:
    print("=" * 72)
    print("B22 -- Spectrum genericity controls")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    t = sp.symbols("t")
    counts: Counter[tuple[int, int, int]] = Counter()
    a_sector = []
    orientation_reversing = 0
    for a in range(-5, 6):
        for b in range(-5, 6):
            for c in range(-5, 6):
                for d in range(-5, 6):
                    M = sp.Matrix([[a, b], [c, d]])
                    if M.det() not in (-1, 1):
                        continue
                    det = int(M.det())
                    tr = int(M.trace())
                    cp = sym2_charpoly(M, t)
                    if det == -1:
                        orientation_reversing += 1
                        assert sp.rem(cp, t + 1, domain=sp.QQ) == 0
                    if sp.rem(cp, t**2 - 3 * t + 1, domain=sp.QQ) == 0:
                        a_sector.append((det, tr, M))
                    counts[(det, abs(tr), tr * tr - 4 * det)] += 1

    assert orientation_reversing > 0
    assert all(det == -1 and abs(tr) == 1 for det, tr, _ in a_sector)
    print(f"    orientation-reversing samples with generic -1 sector: {orientation_reversing}")
    print(f"    A-sector samples all satisfy det=-1, |tr|=1: {len(a_sector)}")
    print("    -1 is generic; t^2-3t+1 is the selective sector")

    print("\nVerdict: STALLED")
    print("Parity alone is generic; the half-step A-sector is special.")


if __name__ == "__main__":
    main()
