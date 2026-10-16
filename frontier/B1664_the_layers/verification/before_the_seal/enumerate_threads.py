"""Every primitive thread (a cyclic class of forward words in L, R with both letters) with trace <= T, one Lyndon
representative each: depth-first over words, pruned by trace (appending a letter never lowers the trace of a forward
matrix). Checks: the layer sizes 1, 2, 2, 3 at t = 3..6 (the web seat's count)."""
import sys
def lyndon_ok(w):
    n = len(w)
    return "L" in w and "R" in w and all(w < w[i:] + w[:i] for i in range(1, n))
def threads_upto(T):
    out = []
    stack = [("L", (1, 1, 0, 1)), ("R", (1, 0, 1, 1))]
    while stack:
        w, (a, b, c, d) = stack.pop()
        if a + d > T or len(w) > T: continue          # a pure run L^n keeps trace 2: L^n R has trace n + 2, so n <= T - 2
        if lyndon_ok(w): out.append((w, a + d))
        stack.append((w + "L", (a, a + b, c, c + d)))
        stack.append((w + "R", (a + b, b, c + d, d)))
    return out
if __name__ == "__main__":
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    th = threads_upto(T); from collections import Counter
    cnt = Counter(t for _, t in th)
    print("layer sizes t=3..12:", [cnt.get(t, 0) for t in range(3, 13)], " total", len(th), "to trace", T)
