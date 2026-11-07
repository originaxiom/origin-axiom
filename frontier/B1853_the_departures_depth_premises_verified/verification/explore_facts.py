"""B1853 -- the explore seat's two relays of 2026-11-07 (least volume; the level premise as a conservation law),
re-derived with main's own code (data-free: integer matrices, residues, SnapPy volumes; nothing compared with data).
Definitions as the relays state them: a defect replaces m golden runs by runs S = (r1..rm), first and last >= 2;
E = D_S D_g^-1 with D the alternating product L^r1 R^r2 ...; its word is S's letters (+ R if m is odd) + (LR)^k; excess
volume = vol(b++word) - (k + (m+1)//2) vol(m004); excess length = 2 acosh(tr W/2) - 2 acosh(tr G/2) at k = 20.
Premises: charge at N = E = +-I mod N; symmetry at 5 = E commutes with LR mod 5. Range R1: m <= 6 with runs <= 6,
m = 7, 8 with runs <= 3; R2 adds m = 1..3 with runs <= 64, m = 4 with runs <= 24, m = 5 with runs <= 10."""
import itertools, math, time, warnings
warnings.filterwarnings("ignore")
import mpmath as mp
mp.mp.dps = 40

def mul(A, B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def pw(A, n):
    X = ((1, 0), (0, 1))
    for _ in range(n): X = mul(X, A)
    return X
def mod(A, n): return tuple(tuple(x % n for x in r) for r in A)
L, R, I = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1)); LR = mul(L, R)
def D(runs):
    M = I
    for i, r in enumerate(runs): M = mul(M, pw(L if i % 2 == 0 else R, r))
    return M
def E(runs): return mul(D(runs), inv(D([1] * len(runs))))
def pmI(A, n): return mod(A, n) in (mod(I, n), mod(((-1, 0), (0, -1)), n))
def commutes5(A): return mod(mul(A, LR), 5) == mod(mul(LR, A), 5)
def R1():
    for m in range(1, 9):
        top = 6 if m <= 6 else 3
        for r in itertools.product(range(1, top + 1), repeat=m):
            if r[0] >= 2 and r[-1] >= 2: yield r
def R2():
    for m, top in ((1, 64), (2, 64), (3, 64), (4, 24), (5, 10)):
        for r in itertools.product(range(1, top + 1), repeat=m):
            if r[0] >= 2 and r[-1] >= 2: yield r
def excess_len(runs, k=20):
    m = len(runs); X = R if m % 2 else I
    W = mul(mul(D(runs), X), pw(LR, k)); G = mul(mul(D([1] * m), X), pw(LR, k))
    t = lambda A: mp.mpf(A[0][0] + A[1][1])
    return 2 * mp.acosh(t(W) / 2) - 2 * mp.acosh(t(G) / 2)
out = []
# --- the defect space and HV1's set
r1 = list(R1()); rung = [r for r in r1 if pmI(E(r), 5)]
out.append("R1: %d defects, %d rung-invisible (E = +-I mod 5)" % (len(r1), len(rung)))
# --- HL1: the centraliser of LR in SL(2, F5)
G5 = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]
cent = {A for A in G5 if mod(mul(A, LR), 5) == mod(mul(LR, A), 5)}
gen = set(); P = I
for _ in range(20): gen.add(mod(P, 5)); P = mul(P, LR)
out.append("HL1: |SL(2,F5)| = %d; |C5(LR)| = %d; C5(LR) = <LR> (which contains -I): %s" % (len(G5), len(cent), cent == gen))
assert len(G5) == 120 and cent == gen and len(cent) == 10 and mod(((-1, 0), (0, -1)), 5) in gen
# --- HL2: which E conserve the (+-)conjugacy class of every golden background, N = 2..5
hl2 = []
for n in (2, 3, 4, 5):
    G = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(n), repeat=4) if (a * d - b * c) % n == 1 % n]
    def cls(W): return {mod(mul(mul(g, W), inv(g)), n) for g in G}
    backs = set(); P = I
    for _ in range(30): backs.add(mod(P, n)); P = mul(P, LR)
    C = {W: cls(W) | cls(mod(((-W[0][0], -W[0][1]), (-W[1][0], -W[1][1])), n)) for W in backs}
    keep = {A for A in G if all(mod(mul(A, W), n) in C[W] for W in backs)}
    pm = {mod(I, n), mod(((-1, 0), (0, -1)), n)}
    hl2.append(keep == pm)
out.append("HL2: only +-I conserve every golden background's class at N = 2, 3, 4, 5: %s" % hl2)
assert all(hl2)
# --- HL3: the least-length departure under each premise, over R1 u R2
space = list(dict.fromkeys(itertools.chain(R1(), R2())))
prem = {"none": lambda A: True, "symmetry at 5": commutes5, "charge at 5": lambda A: pmI(A, 5),
        "charge at 4, 5": lambda A: pmI(A, 4) and pmI(A, 5), "charge at 2, 3, 4, 5": lambda A: all(pmI(A, n) for n in (2, 3, 4, 5))}
EM = {r: E(r) for r in space}
for name, f in prem.items():
    cands = sorted(((excess_len(r), r) for r in space if f(EM[r])), key=lambda t: t[0])
    (l0, s0), (l1, s1) = cands[0], cands[1]
    out.append("HL3 %-22s least length %s (%.6f); next %s (+%.4f)" % (name + ":", s0, float(l0), s1, float(l1 - l0)))
# --- the apex law for single runs: max over shifts of (x+ - x-)/2 for the cyclic quotients (n, 1, 1, ...)
for n in (2, 6, 21, 61):
    xp = n + 1 / mp.phi; xm = -1 / mp.phi
    assert abs((xp - xm) / 2 - ((n - 1) / mp.mpf(2) + mp.sqrt(5) / 2)) < mp.mpf(10) ** -30
out.append("apex law: the single run (n) in the golden background has apex (n - 1)/2 + sqrt5/2 (n = 2, 6, 21, 61: exact)")
# --- the post hoc: LR's fixed points on P^1(Z/N)
def P1(n):
    pts = set()
    for a, b in itertools.product(range(n), repeat=2):
        if math.gcd(math.gcd(a, b), n) != 1: continue
        orb = frozenset(((u * a) % n, (u * b) % n) for u in range(n) if math.gcd(u, n) == 1); pts.add(orb)
    return pts
fixed = {}
for n in (2, 3, 4, 5):
    fx = [sorted(p)[0] for p in P1(n) if frozenset((((LR[0][0] * a + LR[0][1] * b) * u) % n, ((LR[1][0] * a + LR[1][1] * b) * u) % n) for (a, b) in [sorted(p)[0]] for u in range(n) if math.gcd(u, n) == 1) & p]
    fixed[n] = fx
out.append("LR's fixed points on P^1(Z/N): %s" % {n: fixed[n] for n in fixed})
# --- HV1: least excess volume among the rung-invisible defects (SnapPy, k = 10)
import snappy
V4 = float(snappy.Manifold("m004").volume()); K = 10
def word(r, k=K): return "".join(("L" if i % 2 == 0 else "R") * x for i, x in enumerate(r)) + ("R" if len(r) % 2 else "") + "LR" * k
t0 = time.time(); vols = []; bad = 0
for r in rung:
    M = snappy.Manifold("b++" + word(r))
    if M.solution_type() != "all tetrahedra positively oriented": bad += 1; continue
    vols.append((float(M.volume()) - (K + (len(r) + 1) // 2) * V4, r))
vols.sort()
out.append("HV1: %d volumes (%d non-geometric skipped, %.0f s); least %s at %.10f; next %s %.10f and %s %.10f; gap %.4f"
           % (len(vols), bad, time.time() - t0, vols[0][1], vols[0][0], vols[1][1], vols[1][0], vols[2][1], vols[2][0], vols[1][0] - vols[0][0]))
d11 = float(snappy.Manifold("b++" + word((11,))).volume()) - (K + 1) * V4
out.append("HV3: (dV(11) - dV(6))/dV(6) = %.3f" % ((d11 - vols[0][0]) / vols[0][0]))
print("\n".join(out))
# --- HV2: least excess volume among the line-invisible (= symmetry at 5, by HL1) defects of R1; and (2,2,2) directly
line = [r for r in r1 if commutes5(E(r))]
lv = []
for r in line:
    M = snappy.Manifold("b++" + word(r))
    if M.solution_type() == "all tetrahedra positively oriented":
        lv.append((float(M.volume()) - (K + (len(r) + 1) // 2) * V4, r))
lv.sort()
d222 = float(snappy.Manifold("b++" + word((2, 2, 2))).volume()) - (K + 2) * V4
print("HV2: %d line-invisible defects; least excess volume %s (%.6f), next %s (+%.4f); dV(2,2,2) = %.4f (not rung-invisible)"
      % (len(lv), lv[0][1], lv[0][0], lv[1][1], lv[1][0] - lv[0][0], d222))
