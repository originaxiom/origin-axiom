"""Check 4: is the lines tally's flatness in N an identity?  Burnside: SL(2, Z/N) acts transitively on the vectors of
exact order N in (Z/N)^2, so the mean over the group of #{v : v M = v} is 1, and of #{v : v M = -v} is 1 (M -> -M is a
bijection of the group).  The two sets meet only when 2v = 0, i.e. N = 2.  Hence the group mean of B1733's count
(both signs) is exactly 2 for N >= 3 and 1 for N = 2, for ANY family equidistributed mod N.  Computed exhaustively for
N = 2..12; then the draft's tally divided by its 2536 threads; then the same tally on words of length exactly 18
(uniform sample), to show the approach to 2."""
import itertools, math, sys, os, json, random
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from refcore import lyndon, mat

def group_mean(N):
    vecs = np.array([(a, b) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1])
    tot = 0; cnt = 0
    for a, b, c, d in itertools.product(range(N), repeat=4):
        if (a * d - b * c) % N != 1: continue
        v0 = (vecs[:, 0] * a + vecs[:, 1] * c) % N; v1 = (vecs[:, 0] * b + vecs[:, 1] * d) % N
        plus = (v0 == vecs[:, 0]) & (v1 == vecs[:, 1]); minus = (v0 == (-vecs[:, 0]) % N) & (v1 == (-vecs[:, 1]) % N)
        tot += int((plus | minus).sum()); cnt += 1
    return tot / cnt, cnt

def count(M, N):
    k = 0
    for a, b in itertools.product(range(N), repeat=2):
        if math.gcd(math.gcd(a, b), N) != 1: continue
        v = ((a * M[0][0] + b * M[1][0]) % N, (a * M[0][1] + b * M[1][1]) % N)
        k += v == (a, b) or v == ((-a) % N, (-b) % N)
    return k

out = {"group mean (exhaustive)": {}}
for N in range(2, 13):
    m, g = group_mean(N); out["group mean (exhaustive)"][N] = [m, g]; print("N=%d |SL2(Z/N)|=%d mean=%.6f" % (N, g, m), flush=True)
draft = json.load(open(__import__("pathlib").Path(__file__).resolve().parents[1] / "stage1_threads_measure.json"))["lines fixed, by order N (summed over threads)"]
out["draft tally / 2536"] = {N: round(draft[N] / 2536, 3) for N in sorted(draft, key=int)}
print("draft tally per thread:", out["draft tally / 2536"])
rng = random.Random(1813); ws = ["".join(rng.choice("LR") for _ in range(18)) for _ in range(3000)]
ws = [w for w in ws if "L" in w and "R" in w]
out["mean per word, length 18 (3000 uniform words)"] = {N: round(sum(count(mat(w), N) for w in ws) / len(ws), 3) for N in (2, 3, 4, 5, 6, 7, 12, 23, 28, 30)}
print("length-18 mean:", out["mean per word, length 18 (3000 uniform words)"])
json.dump(out, open(os.path.join(os.path.dirname(__file__), "check4_lines_burnside.json"), "w"), indent=1)
