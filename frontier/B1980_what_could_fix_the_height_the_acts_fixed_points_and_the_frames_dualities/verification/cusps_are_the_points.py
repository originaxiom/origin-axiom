"""B1980, post hoc (labelled; written after act_level30_run.txt was read; exact): are the cusps of X(30) fixed by M^12 exactly
B1976's 96 points of order 30 on the act's line, up to sign? And the act's orbits on the cusps against B1978's orbits.
    python3 -B cusps_are_the_points.py > cusps_are_the_points_run.txt"""
import json, pathlib
from fractions import Fraction as Fr
from math import gcd
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
N = 30
P96 = {(int(Fr(r["a"]) * N), int(Fr(r["b"]) * N)) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text())}
def sgn(v): return min(v, ((-v[0]) % N, (-v[1]) % N))
def mul(A, B): return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N, (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)
M = (2, 1, 1, 1); P = (1, 0, 0, 1)
for _ in range(12): P = mul(P, M)
cusps = {sgn((a, c)) for a in range(N) for c in range(N) if N // gcd(gcd(a, c), N) == N}
fixed = {v for v in cusps if sgn(((P[0] * v[0] + P[1] * v[1]) % N, (P[2] * v[0] + P[3] * v[1]) % N)) == v}
print("M^12 mod 30 = %s" % (P,))
print("cusps fixed by M^12: %d; B1976's points up to sign: %d; the same set: %s" % (len(fixed), len({sgn(v) for v in P96}), fixed == {sgn(v) for v in P96}))
print("is -p among the 96 whenever p is: %s; does M^12 fix each of the 96 points (not only up to sign): %s" % (
    all(((-a) % N, (-b) % N) in P96 for (a, b) in P96), all(((P[0] * a + P[1] * b) % N, (P[2] * a + P[3] * b) % N) == (a, b) for (a, b) in P96)))
print("SUMMARY: the cusps of X(30) fixed by a power of the act are exactly B1976's 96 points up to sign: %s" % (fixed == {sgn(v) for v in P96}))
