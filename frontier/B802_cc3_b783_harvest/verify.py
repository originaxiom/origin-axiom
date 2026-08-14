#!/usr/bin/env python3
"""B802 — independent verification of cc3's B783 (observer ground-zero) before harvest.

Standing rule (integrate-don't-merge): cherry-pick cc3 deliverables under a NEW number, verify
independently, never merge the branch. This verifies what is computable from scratch.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2


def fib_word(n):
    """Fibonacci word S_n under sigma: a->ab, b->a."""
    s = "a"
    for _ in range(n):
        s = "".join("ab" if c == "a" else "a" for c in s)
    return s


def freqs(w):
    return sp.Rational(w.count("a"), len(w)), sp.Rational(w.count("b"), len(w))


def main():
    print("=" * 76)
    print("B802 — verifying cc3's B783 claims independently")
    print("=" * 76)
    w = fib_word(24)
    fa, fb = freqs(w)
    print(f"  |S| = {len(w)}   d(a) = {fa}   d(b) = {fb}")
    print(f"  d(a) -> 1/phi  ? limit check: {float(fa):.10f} vs {float(1/phi):.10f}")
    print(f"  d(b) -> 1/phi^2? limit check: {float(fb):.10f} vs {float(1/phi**2):.10f}")
    print(f"  d(a)+d(b) = 1 : {fa + fb == 1}")

    # CLAIM 1 -- reversal preserves letter frequencies
    rev = w[::-1]
    ra, rb = freqs(rev)
    c1 = (ra, rb) == (fa, fb)
    print(f"\n  [1] reversal preserves frequencies                 : {c1}   {(ra,rb)==(fa,fb)}")

    # CLAIM 2 -- complement (a<->b) SWAPS them
    comp = w.translate(str.maketrans("ab", "ba"))
    ca, cb = freqs(comp)
    c2 = (ca, cb) == (fb, fa)
    print(f"  [2] complement swaps frequencies                   : {c2}")

    # CLAIM 3 -- therefore reversal != complement as operations on frequencies
    c3 = (ra, rb) != (ca, cb)
    print(f"  [3] reversal and complement differ on frequencies  : {c3}")

    # CLAIM 4 -- both reading directions have the same growth rate phi
    ratios = [sp.Rational(len(fib_word(n + 1)), len(fib_word(n))) for n in range(14, 18)]
    conv = all(abs(float(r) - float(phi)) < 1e-3 for r in ratios)
    print(f"  [4] growth rate -> phi (direction-independent)     : {conv}"
          f"   (last ratio {float(ratios[-1]):.8f} vs phi {float(phi):.8f})")

    # CLAIM 5 -- the load-bearing NEGATIVE: gamma5 cannot be reading direction.
    # gamma5 sends sqrt5 -> -sqrt5, hence phi -> phibar = 1-phi = -1/phi, so it MOVES any
    # quantity built from phi. Reversal provably does NOT move the frequencies. Therefore
    # gamma5 != reversal. This is the argument that carries cc3's headline negative.
    phibar = 1 - phi
    moves = sp.simplify(1 / phibar - 1 / phi) != 0
    print(f"\n  [5] gamma5 moves phi-built quantities (1/phi != 1/phibar): {moves}")
    print(f"      reversal does NOT move them (claim 1)                : {c1}")
    print(f"      => gamma5 is NOT reading direction                   : {bool(moves and c1)}")

    # SCOPE NOTE -- what is NOT verified here
    print("\n  NOT verified in-sandbox (needs cc3's tracking-map definition, not reproduced):")
    print("    - parent(sigma) = child(sigma_mirror) with zero mismatches to F_18")
    print("    - the per-prediction 1/5 scoring of proposal #16")
    print("    - the K-theory positive-cone identity")
    return {"rev_preserves": c1, "comp_swaps": c2, "differ": c3, "growth": conv,
            "gamma5_moves": bool(moves), "gamma5_not_direction": bool(moves and c1)}


if __name__ == "__main__":
    main()
