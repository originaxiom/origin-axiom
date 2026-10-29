"""Referee check 3b: own Duval enumeration of primitive necklaces (Lyndon words over L<R, both letters) up to length 18;
share with #L - #R = 0 mod 4 among lengths <= N, for even and odd N.  (Classes up to rotation only; B1814's canon may
also identify the L<->R swap, which preserves #L - #R = 0 mod 4 up to sign, so the share is the same up to swap-fixed words.)"""
import collections
def lyndon(nmax):
    w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        if m <= nmax: yield w[:]
        while len(w) < nmax: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()
by = collections.Counter(); hit = collections.Counter()
for w in lyndon(18):
    n = len(w); r = sum(w)
    if r == 0 or r == n: continue
    by[n] += 1
    if ((n - r) - r) % 4 == 0: hit[n] += 1
for N in range(10, 19):
    print("length <= %2d: %6d classes, share %.4f  | exactly %2d: share %.4f" % (N, sum(by[k] for k in by if k <= N), sum(hit[k] for k in hit if k <= N) / sum(by[k] for k in by if k <= N), N, hit[N] / by[N]))
