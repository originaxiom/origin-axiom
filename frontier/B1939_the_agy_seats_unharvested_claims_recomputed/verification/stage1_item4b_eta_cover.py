"""Item 4, a comparison with B1929's twisted eta values (post hoc; expectation in NOTES.md before the run).

sum over the full group C of M-fixed torus characters of eta_A(c) (trivial term = Psi(M)/3) against Psi(M')/3, M' = M on
Lambda = annihilator of C, in an oriented basis. eta_A(c) = -2 Im(Delta_c)/pi from main's own Siegel winding
(B1929 main_siegel.json). Own code; reads the record's files as data only.
"""
import json, math, sys
from fractions import Fraction as Fr

ROOT = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/" + "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/"
PLANT = sys.argv[1] if len(sys.argv) > 1 else None
pop = json.load(open(ROOT + "received_sm/population.json"))
sieg = {(json.dumps(r["level"]), r["i"], r["j"]): r["Delta"] for r in json.load(open(ROOT + "main_siegel.json"))}


def sgn(x): return (x > 0) - (x < 0)
def saw(x):
    x = Fr(x)
    return Fr(0) if x.denominator == 1 else x - (x.numerator // x.denominator) - Fr(1, 2)
def Psi(A):
    (a, b), (c, d) = A
    if c == 0: return Fr(b, d)
    Phi = Fr(a + d, c) - 12 * sgn(c) * sum(saw(Fr(r, abs(c))) * saw(Fr(d * r, abs(c))) for r in range(1, abs(c)))
    return Phi - 3 * sgn(c * (a + d))


def hnf_basis(vecs):
    """an integer basis (columns) of the lattice spanned by 2-vectors, by row reduction on the first coordinate"""
    vs = [list(v) for v in vecs if v != (0, 0)]
    # gcd reduction on first coordinates
    while sum(1 for v in vs if v[0] != 0) > 1:
        vs.sort(key=lambda v: (abs(v[0]) == 0, abs(v[0])))
        p = vs[0]
        for v in vs[1:]:
            if v[0] != 0:
                q = v[0] // p[0]; v[0] -= q * p[0]; v[1] -= q * p[1]
    first = [v for v in vs if v[0] != 0]
    b1 = first[0]
    g = 0
    for v in vs:
        if v[0] == 0: g = math.gcd(g, v[1])
    b2 = [0, g]
    return b1, b2


rows, levels = [], {}
for o in pop: levels.setdefault(json.dumps(o["level"]), []).append(o)
worst, all_ok = 0.0, True
for lev, L in sorted(levels.items()):
    M = tuple(tuple(r) for r in L[0]["M"]); N = L[0]["N"]
    (a, b), (c, d) = M
    C = [(o["i"], o["j"]) for o in L]
    # each character fixed by M^T (Bohn's (Id - M^t) nu in Z^2, B1929 run_c9.py m_of)
    fixedT = all(((a * i + c * j - i) % N, (b * i + d * j - j) % N) == (0, 0) for i, j in C)
    order = abs((a - 1) * (d - 1) - b * c)
    # Lambda = {v : (i v1 + j v2)/N in Z for all characters}
    gens = [(N, 0), (0, N)] + [(v1, v2) for v1 in range(N) for v2 in range(N) if all((i * v1 + j * v2) % N == 0 for i, j in C)]
    b1, b2 = hnf_basis(gens)
    B = ((b1[0], b2[0]), (b1[1], b2[1]))
    detB = B[0][0] * B[1][1] - B[0][1] * B[1][0]
    if detB < 0: B = ((b2[0], b1[0]), (b2[1], b1[1])); detB = -detB
    Binv = ((Fr(B[1][1], detB), Fr(-B[0][1], detB)), (Fr(-B[1][0], detB), Fr(B[0][0], detB)))
    MB = ((a * B[0][0] + b * B[1][0], a * B[0][1] + b * B[1][1]), (c * B[0][0] + d * B[1][0], c * B[0][1] + d * B[1][1]))
    Mp = tuple(tuple(Binv[r][0] * MB[0][s] + Binv[r][1] * MB[1][s] for s in range(2)) for r in range(2))
    integral = all(x.denominator == 1 for row in Mp for x in row)
    Mp = tuple(tuple(int(x) for x in row) for row in Mp)
    etaA = [-2 * sieg[(lev, i, j)][1] / math.pi for i, j in C]
    triv = 0.0 if PLANT == "P4e" else float(Psi(M) / 3)     # P4e: the trivial character's term dropped
    lhs = triv + sum(etaA)
    rhs = float(Psi(Mp) / 3)
    ok = fixedT and integral and detB == order and len(C) == order - 1 and abs(lhs - rhs) < 1e-9
    all_ok &= ok; worst = max(worst, abs(lhs - rhs))
    rows.append((lev, M, len(C) + 1, Mp, str(Psi(M)), str(Psi(Mp)), round(lhs, 12), ok))
    print("%-18s M=%s |C|=%d fixed by M^T: %s  M'=%s  Psi(M)=%s Psi(M')=%s  Psi(M)/3 + sum eta_A = %.12f  vs Psi(M')/3 = %.12f  %s" % (
        lev, M, len(C) + 1, fixedT, Mp, Psi(M), Psi(Mp), lhs, rhs, "ok" if ok else "MISMATCH"))
print(("PASS" if all_ok else "FAIL") + " sum over C of B1929's eta_A (trivial = Psi(M)/3) = Psi(M')/3 on all %d levels (worst %.1e)%s" % (
    len(rows), worst, " [PLANT P4e]" if PLANT == "P4e" else ""))
