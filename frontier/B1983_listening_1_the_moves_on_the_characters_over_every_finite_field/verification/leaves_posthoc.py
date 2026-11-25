"""B1983, POST HOC (labelled; written after listen1_run.txt was read): from the committed listen1_run.json, for each prime p,
the leaves kappa in F_p on which the moves L, R leave exactly one orbit of size > 1 (the whole connects the leaf), and the
leaves connected at every prime 5 <= p <= 47, written as integers -2..2 where they are; plus the number of nontrivial orbits
per leaf at the largest prime.
    python3 -B leaves_posthoc.py > leaves_posthoc_run.txt"""
import json, pathlib
R = json.loads(pathlib.Path(__file__).with_name("listen1_run.json").read_text())
P = sorted(int(k.split("|")[1]) for k in R if k.startswith("L, R|"))
conn = {}
for p in P:
    by = R["L, R|%d" % p]["orbits_by_kappa"]
    conn[p] = sorted(int(k) for k, v in by.items() if sum(1 for s in v if s > 1) == 1)
    print("p = %2d: connected leaves (one orbit of size > 1) %s; leaves with no orbit of size > 1: %s" % (
        p, conn[p], sorted(int(k) for k, v in by.items() if all(s == 1 for s in v))))
def as_int(k, p): return k - p if k > p // 2 else k
for c in (-2, -1, 0, 1, 2):
    print("the leaf kappa = %2d is connected at the primes: %s" % (c, [p for p in P if p >= 5 and (c % p) in conn[p]]))
always = [c for c in range(-3, 4) if all((c % p) in conn[p] for p in P if p >= 5)]
print("SUMMARY: integer leaves kappa in -3..3 connected at every prime 5 <= p <= 47: %s" % always)
wide = [c for c in range(-40, 41) if all((c % p) in conn[p] for p in P if p >= 5)]
print("SUMMARY (wider): integer leaves kappa in -40..40 connected at every prime 5 <= p <= 47: %s" % wide)
print("   and connected at every prime 11 <= p <= 47: %s" % [c for c in range(-40, 41) if all((c % p) in conn[p] for p in P if p >= 11)])
p = P[-1]; by = R["L, R|%d" % p]["orbits_by_kappa"]
print("at p = %d, nontrivial orbits per leaf (kappa as an integer -p/2..p/2): %s" % (p, sorted((as_int(int(k), p), sum(1 for s in v if s > 1)) for k, v in by.items())))
