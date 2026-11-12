"""Roots of x^2 - x - 1 modulo N (B1884's row P2 counts lines kept as sets by these), N = 2..200, and at 209 and 25."""
from collections import Counter
cnt = {N: sum(1 for x in range(N) if (x * x - x - 1) % N == 0) for N in range(2, 201)}
by = Counter(cnt.values())
print("N in 2..200 by number of roots:", dict(sorted(by.items())))
print("levels with 0 roots, first ten:", [N for N in cnt if cnt[N] == 0][:10])
print("levels with 1 root:", [N for N in cnt if cnt[N] == 1])
print("levels with 2 roots, first twelve:", [N for N in cnt if cnt[N] == 2][:12])
print("roots at 209:", [x for x in range(209) if (x * x - x - 1) % 209 == 0], " at 25:", [x for x in range(25) if (x * x - x - 1) % 25 == 0])
