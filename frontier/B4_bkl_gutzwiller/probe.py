"""
Frontier probe B4 — the BKL billiard, Gutzwiller weighting, and golden Kasner.

  SPECULATIVE FRONTIER WORK. Outputs are *logged observations*, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

Question:
  A = LR is a periodic orbit of the modular billiard, which models the BKL
  dynamics of a cosmology near a singularity. Is the figure-eight orbit the
  shortest such orbit, how does a Gutzwiller periodic-orbit sum weight it, and
  what Kasner exponents does its BKL parameter u = phi correspond to?

Run:  python frontier/B4_bkl_gutzwiller/probe.py
"""

from itertools import product as iprod

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
L = np.array([[1, 1], [0, 1]])
R = np.array([[1, 0], [1, 1]])


def word_matrix(w):
    M = np.eye(2, dtype=int)
    for c in w:
        M = M @ (L if c == "L" else R)
    return M


def is_primitive(w):
    for p in range(1, len(w)):
        if len(w) % p == 0 and w[:p] * (len(w) // p) == w:
            return False
    return True


def canonical(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def gutzwiller_sum(max_len=10):
    """Enumerate primitive periodic {L,R}-orbits; weight each by exp(-length)."""
    orbits = {}
    for wl in range(2, max_len + 1):
        for bits in iprod("LR", repeat=wl):
            w = "".join(bits)
            if len(set(w)) == 1 or not is_primitive(w):
                continue
            c = canonical(w)
            if c != w or canonical(w[::-1]) < c:
                continue
            T = abs(int(np.trace(word_matrix(w))))
            if T <= 2:
                continue
            orbits.setdefault(T, []).append(w)
    total = fig8 = 0.0
    rows = []
    for T in sorted(orbits)[:15]:
        length = 2 * np.arccosh(T / 2)
        contribution = len(orbits[T]) * np.exp(-length) / np.sqrt(T * T - 4)
        total += contribution
        if T == 3:
            fig8 = contribution
        rows.append((T, length, len(orbits[T]), contribution))
    return rows, fig8, total


def kasner_at(u):
    """Standard Kasner exponents for BKL parameter u (hold for any u)."""
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


def main():
    print("=" * 72)
    print("Frontier probe B4 -- BKL billiard, Gutzwiller weighting, golden Kasner")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    rows, fig8, total = gutzwiller_sum()
    print("\n[1] Primitive periodic orbits of the modular billiard")
    for T, length, n, _c in rows:
        tag = "  <-- figure-eight orbit (A = LR)" if T == 3 else ""
        print(f"    trace {T:>2}   length {length:.4f}   count {n}{tag}")
    print(f"\n    The figure-eight orbit (trace 3) is the SHORTEST primitive orbit.")
    print(f"    Gutzwiller weight 4*log(phi)/sqrt5 = {4 * np.log(PHI) / np.sqrt(5):.6f}")
    print(f"    Figure-eight share of the orbit sum  = {fig8 / total * 100:.1f}%")

    p1, p2, p3 = kasner_at(PHI)
    print("\n[2] Kasner exponents at BKL parameter u = phi")
    print(f"    p1, p2, p3 = {p1:.6f}, {p2:.6f}, {p3:.6f}")
    print(f"    sum = {p1 + p2 + p3:.6f},  sum of squares = {p1**2 + p2**2 + p3**2:.6f}")
    print(f"    ratios  p3/p2 = {p3 / p2:.6f},  p2/|p1| = {p2 / abs(p1):.6f}")
    print(f"    => at u = phi the three exponents form a geometric progression")
    print(f"       (common ratio phi). This is the ONE exact phi-specific fact:")
    print(f"       the Kasner conditions sum=1, sum-sq=1 hold for EVERY u.")

    print("\n[verdict]  See README.md. Bounded result: the figure-eight orbit is")
    print("the shortest primitive billiard orbit (exact), the leading Gutzwiller")
    print("term (37.8% -- modest, not dominant), and at u = phi the Kasner")
    print("exponents are in golden geometric progression. 'Leading' is not")
    print("'selected'; BKL describes only the near-singularity regime; this is")
    print("one Kasner solution among infinitely many. No claim promoted.")


if __name__ == "__main__":
    main()
