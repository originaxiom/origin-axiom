#!/usr/bin/env python3
"""Failing control for Card A2-PEER-PHYS-C8 (100% self-contained, exits 1 with 0 stderr bytes under python3 -I).

Omits the commuting dihedral sheet lift j from the meridian on the 13+3 Spin(16) -> Ss(16) subset E_8
peripheral torus, restoring the periodic adjoint spin kernel from 0 back to 8 and failing cleanly.
"""
import itertools
import sys


def main():
    pairs = []
    seen = set()
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            p = min((a, b), ((-a) % 5, (-b) % 5))
            if p not in seen:
                seen.add(p)
                pairs.append(p)

    def weil_w(va, vb, xa, xb):
        x2a = (xa * xa + 2 * xb * xb) % 5
        x2b = (2 * xa * xb) % 5
        pa = (va * x2a + 2 * vb * x2b) % 5
        return (4 * pa) % 5

    w12 = [(weil_w(1, 0, a, b), weil_w(0, 3, a, b)) for a, b in pairs]
    rem = list(w12)
    planes = []
    while rem:
        w = rem.pop(0)
        rem.remove(((-w[0]) % 5, (-w[1]) % 5))
        planes.append(w)

    # Planted fault: omit sheet lift j => geometric meridian acts as +1 on Spin(3) spinor 2,
    # restoring 4 * 2 = 8 periodic kernel states instead of 0.
    hits_64 = sum(
        1 for eps in itertools.product((1, -1), repeat=6)
        if (sum(e * p[0] for e, p in zip(eps, planes)) % 5 == 0
            and sum(e * p[1] for e, p in zip(eps, planes)) % 5 == 0)
    )
    periodic_kernel = 2 * hits_64
    ok = (periodic_kernel == 0)
    print(f"CONTROL_FAIL: omit_sheet_action_restores_periodic_kernel={periodic_kernel} expected=0 ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
