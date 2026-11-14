"""B1928's H2 and H3, numerically (written before the run): the length per letter of a random word concentrates (its
spread falling like 1/sqrt(n): the Lyapunov exponent), and the longest run of one letter, which is how deep the thread
goes into the cusp, grows only like log2(n), so the return time r (logarithmic in a run's length) is uniformly
integrable under the uniform measures on words. Printed: means and shares only."""
import math, random
import numpy as np


def ell(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        if ch == "L":
            a, b, c, d = a, a + b, c, c + d
        else:
            a, b, c, d = a + b, b, c + d, d
    tr = a + d
    return 2 * math.log((tr + math.sqrt(tr * tr - 4)) / 2)


if __name__ == "__main__":
    rng = random.Random(23)
    for n in (20, 50, 100, 200):
        ls, runs = [], []
        for _ in range(2000):
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" not in w or "R" not in w:
                continue
            ls.append(ell(w) / n)
            runs.append(max(max(len(s) for s in w.split("R") if s), max(len(s) for s in w.split("L") if s)))
        ls, runs = np.array(ls), np.array(runs)
        print("n = %3d: length per letter mean %.4f, sd %.4f; longest run mean %.1f; share with a run >= 2 log2(n) + 4: %.4f"
              % (n, ls.mean(), ls.std(), runs.mean(), np.mean(runs >= 2 * math.log2(n) + 4)))
