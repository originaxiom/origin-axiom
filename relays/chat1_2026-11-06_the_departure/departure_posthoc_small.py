"""The web seat, 2026-11-06: POST HOC to departure_check.py (b79bb6d95 -> 6c284645b), written after reading its output,
committed before its run. Data-free (SL(2, Z) arithmetic only; no frame value, no data, no held-out quantity).

Question (for P-717's ask 1, "one departure"): can "one departure" be replaced by "the lowest excursion that returns,
in the line's own curve, to the golden lift it left"? A defect word D inserted into the golden path (... G G D G G ...,
G = LR) leaves the lift G and returns to D G D^-1; the line's pair returns unchanged iff D fixes each of +-v, +-2v (mod
5) -- B1733's own lines of G, in G's marking.
  (1) the single-run defects L^n R: fix the pair iff n = 1 mod 5 (departure_check.py, part E, in another form);
  (2) five run-2 defects, each L^2 R (LR)^4 = L (LR)^5 (one extra L, then four golden periods): each alone moves the
      pair; together the five extra L's give L^5 = I mod 5, since (LR)^5 = -I mod 5;
  (3) the highest apex of the periodic histories D (LR)^k, k = 0..12, by continued fractions over the run sequence
      and by the matrix orbit with S-conjugates; against the single run-6 value (5 + sqrt5)/2 and phi.

    python3 departure_posthoc_small.py
"""
import importlib.util
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("departure_check", HERE / "departure_check.py")
D0 = importlib.util.module_from_spec(sp)
sys.modules["departure_check"] = D0
sp.loader.exec_module(D0)
L, R, LR, mul, pw, prod, own, act, pm, inv, mod5, fl = D0.L, D0.R, D0.LR, D0.mul, D0.pw, D0.prod, D0.own, D0.act, D0.pm, D0.inv, D0.mod5, D0.fl


def fixes_each(D, pair):
    """D fixes each line of the pair up to sign: w D^-1 = +-w"""
    Di = inv(D)
    return all(pm(act(w, Di)) == w for w in pair)


def runs(letters):
    """cyclic run lengths of a word in L, R, starting at a run boundary"""
    s = ["L" if x == L else "R" for x in letters]
    i = next(j for j in range(len(s)) if s[j] != s[j - 1])
    s = s[i:] + s[:i]
    out, c = [], 1
    for j in range(1, len(s)):
        if s[j] == s[j - 1]:
            c += 1
        else:
            out.append(c); c = 1
    out.append(c)
    return out


if __name__ == "__main__":
    pair = own(LR)
    print("POST HOC: departures that return the line only together (the web seat, 2026-11-06)")
    print("  G = LR; its own order-5 pair in G's marking: %s" % fl(pair))
    print("(1) single-run defects L^n R: fixes the pair iff n = 1 mod 5")
    print("    " + ", ".join("n=%d %s" % (n, fixes_each(prod([L] * n + [R]), pair)) for n in range(1, 13)))
    block = [L, L, R] + [L, R] * 4
    print("(2) the block L^2 R (LR)^4: mod 5 %s; = L (LR)^5: %s; (LR)^5 mod 5 %s; fixes the pair alone: %s" % (
        mod5(prod(block)), mod5(prod(block)) == mod5(mul(L, pw(LR, 5))), mod5(pw(LR, 5)), fixes_each(prod(block), pair)))
    for m in range(1, 6):
        print("    %d blocks: fixes the pair %s" % (m, fixes_each(prod(block * m), pair)))
    five = block * 5
    print("(3) the periodic history (five blocks)(LR)^k, its highest apex | single run 6 (5 + sqrt5)/2 = %s | phi = %s" % (
        mp.nstr((5 + mp.sqrt(5)) / 2, 12), mp.nstr(D0.PHI, 12)))
    for k in range(0, 13, 2):
        w = five + [L, R] * k
        rr = runs(w)
        ri, cr = D0.highest_cf(rr, reps=20)
        c, r, A = D0.highest_matrix(w)
        print("    k = %2d: runs %s...; max run %d; Im %s (cf) | %s (matrix); fixes the pair %s" % (
            k, rr[:8], max(rr), mp.nstr(ri, 12), mp.nstr(r, 12), fixes_each(prod(w), pair)))
    print("departure_posthoc_small exit 0")
