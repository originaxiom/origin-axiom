"""agy-002's older files taken into the register under P-876 (lane agy-002-verify, harvest row 1966): the facts of its reviews
that main settles by computation.  Nothing of the seat's is run.
 A1  (REVIEW_79B line 85; REVIEW_80 line 99) 5^2 + 5^4 + 5^6 ordered sequences and their cyclic orbits by Burnside.
 A2  (REVIEW_82 lines 126, 127) the square roots of 1 modulo N = m^2 + 4 at m = 9, 11, 13.
 A3  (REVIEW_82 line 133) hyperbolic matrices of SL(2, Z) with entries in [-7, 7], and those of positive trace.
 A4  (REVIEW_82 lines 66 to 68) B1927's corner ratio as its own run prints it, against the 1.79 of its table."""
import glob, itertools, math, re
def necklaces(n, k=5): return sum(k ** math.gcd(i, n) for i in range(n)) // n
print("A1: ordered %d; cyclic orbits %s, total %d" % (sum(5 ** n for n in (2, 4, 6)), [necklaces(n) for n in (2, 4, 6)], sum(necklaces(n) for n in (2, 4, 6))))
print("A2: " + "; ".join("m = %d, N = %d: %s" % (m, m * m + 4, [x for x in range(m * m + 4) if (x * x) % (m * m + 4) == 1]) for m in (9, 11, 13)))
R = range(-7, 8); hyp = [(a, b, c, d) for a, b, c, d in itertools.product(R, R, R, R) if a * d - b * c == 1 and abs(a + d) > 2]
print("A3: hyperbolic matrices with entries in [-7, 7]: %d; of positive trace %d" % (len(hyp), sum(1 for a, b, c, d in hyp if a + d > 0)))
F = open(glob.glob("frontier/B1927_*/FINDINGS.md")[0]).read(); runs = sorted(glob.glob("frontier/B1927_*/verification/arc_corner_run.txt"))
r = open(runs[0]).read().split("\n") if runs else []
print("A4: B1927's table gives 1.79: %s; its arc_corner_run.txt lines 1 and 3: %s" % ("**1.79**" in F, [l[:120] for l in (r[0:1] + r[2:3])]))
import subprocess
d = glob.glob("frontier/B1927_*")[0]; old = subprocess.run(["git", "show", "86930f574:%s/FINDINGS.md" % d], capture_output=True, text=True).stdout
print("A4: at 86930f574, the commit the seat read, B1927's table gives 1.79: %s" % ("**1.79**" in old))
