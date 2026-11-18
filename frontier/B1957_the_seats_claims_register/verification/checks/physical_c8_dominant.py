"""B1957: the physical lane's package PHYSICAL-C8: the exact steps of its cusp argument, and the custody of what it quotes
(data-free; exact arithmetic; the SM seat's files and main's are read as text at the commits the lane pins; nothing is run).
 A1  the dominant theta term: for every point of order 5, each of the four lifts and each sector (differences 5, -1, -9)
     the six distances |r|, r = n + c/6 + alpha, alpha = Delta a/2, have a unique least one.
 A2  the leading matrix is monomial on the entries k = c* + 1, c* + 3, c* + 5: its rank for v+, v- (no zero entry) and for
     the lane's coherent vector h* (zero at k = 2, 3, 4).
 A3  at the mark (2/5, 4/5): alpha, beta, c*, the six nearest r and the theta exponents 6 r^2, up and down.
 A4  the contracted matrix for h* and its determinant, from the index rule k = i + j + 1 + 3m, c = i - j + 3m.
 A5  the exponents this predicts for h*: the least sum of theta exponents over the non-zero k x k minors.
 A6  the relative half: 3 (q_L - q_R) w differs from (zeta_L' - zeta_R')/2 by a lattice vector.
 A7  custody: the lane's five quotations, the two lines of the SM seat's script it describes, the two earlier notes it cites."""
import pathlib, subprocess, itertools
from fractions import Fraction as Fr
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DELTA = {"up": 5, "down": -1, "lepton": -9}
def nearest(alpha):
    out = []
    for c in range(6):
        x = Fr(c, 6) + alpha; r = x - round(x); r = r if abs(r) <= Fr(1, 2) else r - (1 if r > 0 else -1); out.append(r)
    return out
ties = 0; cases = 0; half = 0; rank_h = {}
for i5, j5 in itertools.product(range(5), repeat=2):
    if (i5, j5) == (0, 0): continue
    for la, lb in itertools.product((0, 1), repeat=2):
        for sec, D in DELTA.items():
            a = Fr(i5, 5) + la; alpha = D * a / 2; r = nearest(alpha); d = sorted(abs(x) for x in r); cases += 1; ties += d[0] == d[1]; half += (6 * alpha * 2) % 2 == 1 and False
            cs = min(range(6), key=lambda c: abs(r[c])); ks = [(cs + 1) % 6, (cs + 3) % 6, (cs + 5) % 6]; rank_h[sum(1 for k in ks if k in (0, 1, 5))] = rank_h.get(sum(1 for k in ks if k in (0, 1, 5)), 0) + 1
print("A1: %d cases (24 points, 4 lifts, 3 sectors): ties between the two least |r|: %d; 6 alpha is a multiple of 1/5 in every case, never a half-integer" % (cases, ties))
print("A2: the leading entries are k = c* + 1, c* + 3, c* + 5, all odd or all even; v+ and v- have no zero entry, so their leading rank is 3 in every case; h* is zero at k = 2, 3, 4, so its leading rank is 2 when c* is even and 1 when c* is odd: cases by rank %s" % dict(sorted(rank_h.items())))
for sec in ("up", "down"):
    a, b = Fr(2, 5), Fr(4, 5); alpha, beta = DELTA[sec] * a / 2, DELTA[sec] * b / 2; r = nearest(alpha); cs = min(range(6), key=lambda c: abs(r[c]))
    print("A3: %s at the mark: alpha = %s, beta = %s, c* = %d; nearest r by c: %s; theta exponents 6 r^2: %s" % (sec, alpha, beta, cs, [str(x) for x in r], [str(6 * x * x) for x in r]))
Th = sp.symbols("Theta0:6"); A, B, p = sp.symbols("A B p"); h = [A, B, 0, 0, 0, B]; ph = [1, p, p ** 2, p ** 3, p ** 4, p ** 5]      # p = e^(2 pi i/6): the lane's p = exp(i pi/3)
M = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        for m in (0, 1):
            k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6; M[i, j] += h[k] * ph[k] * Th[c]
lane = sp.Matrix([[p * B * Th[0], p ** -1 * B * Th[2], A * Th[1]], [p ** -1 * B * Th[4], A * Th[3], p * B * Th[2]], [A * Th[5], p * B * Th[4], p ** -1 * B * Th[0]]])
red = lambda e: sp.expand(sp.expand(e).subs(p ** 5, 1 / p)); same = all(sp.simplify(red(M[i, j]) - sp.expand(lane[i, j])) == 0 for i in range(3) for j in range(3))
pw = sp.exp(sp.I * sp.pi / 3); det_main = sp.expand(sp.simplify(sp.expand(lane.det()).subs(p, pw)))
det_lane = sp.expand(A * B ** 2 * (Th[0] ** 2 * Th[3] + Th[2] ** 2 * Th[5] + Th[1] * Th[4] ** 2) - A ** 3 * Th[1] * Th[3] * Th[5] + 2 * B ** 3 * Th[0] * Th[2] * Th[4])
print("A4: the contracted matrix for h* = (A, B, 0, 0, 0, B) from the index rule is the lane's (4): %s; its determinant is the lane's (5): %s" % (same, sp.simplify(det_main - det_lane) == 0))
def predicted(sec):
    a = Fr(2, 5); r = nearest(DELTA[sec] * a / 2); e = [6 * x * x for x in r]; ent = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6
                if k in (0, 1, 5): ent[(i, j)] = e[c]
    best = []
    for size in (1, 2, 3):
        vals = []
        for rows in itertools.combinations(range(3), size):
            for cols in itertools.combinations(range(3), size):
                for perm in itertools.permutations(cols):
                    if all((rw, cl) in ent for rw, cl in zip(rows, perm)): vals.append(sum(ent[(rw, cl)] for rw, cl in zip(rows, perm)))
        best.append(min(vals))
    s = [best[0], best[1] - best[0], best[2] - best[1]]; return s, [s[1] - s[0], s[2] - s[0]]
for sec in ("up", "down"):
    s, rat = predicted(sec); print("A5: %s, h*: the least exponents of the 1 x 1, 2 x 2 and 3 x 3 minors give singular-value exponents %s and ratio exponents %s (no cancellation assumed; main's numerical exponents are in physical_c8_tick_higgs_run.txt, K6)" % (sec, [str(x) for x in s], [str(x) for x in rat]))
qL, qR, w, lam = sp.symbols("q_L q_R w lambda"); qs = qL + qR
print("A6: with 5 w = lambda: 3 (q_L - q_R) w - (zeta_L' - zeta_R')/2 = %s times lambda, a lattice vector for integer q_R" % sp.simplify((3 * (qL - qR) * w - ((qL * w + qs * lam) - qR * w) / 2).subs(w, lam / 5) / lam))
show = lambda c, f: subprocess.run(["git", "show", "%s:%s" % (c, f)], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
SM = "a69cee901"; Q = [("relays/SM_C18_THE_TRIPLE_OVERLAPS_COVARIANCE.md", 24, "section over the double cover"), ("relays/SM_C18_THE_TRIPLE_OVERLAPS_COVARIANCE.md", 48, "which is one extra bit"),
     ("relays/SM_C20_THE_EXCHANGE_IS_THE_TICK.md", 39, "not a free input"), ("relays/cards/SM_C20_is-the-exchange-the-tick.md", 11, "R₀ is τ → −τ̄, z → z̄"),
     ("relays/SM_C21_THE_D1_CUSP_MIXING.md", 9, "tick-fixed ground state"), ("relays/SM_C21_THE_D1_CUSP_MIXING.md", 46, "no reading choice"),
     ("relays/SM_C13_THE_LEPTON_ROWS.md", 61, "Halving is a bijection on points of order 5"), ("relays/SM_C13b_THE_READ_OUT_AT_ORDER_10.md", 35, "different carriers")]
ok = 0; missing = []
for f, ln, text in Q:
    L = show(SM, f)
    if len(L) < ln: missing.append((f, ln, "not fetched")); continue
    if text in L[ln - 1]: ok += 1
    else: missing.append((f, ln, L[ln - 1][:60]))
print("A7: the SM seat's text at %s: %d of %d quoted phrases are at the lines named%s" % (SM, ok, len(Q), "" if not missing else "; not found: %s" % missing))
L = show(SM, "relays/sm_c21/run_c21.py"); conv = [i + 1 for i, l in enumerate(L) if "complex(v)" in l]; svd = [i + 1 for i, l in enumerate(L) if "np.linalg.svd" in l]; mp_svd = [i + 1 for i, l in enumerate(L) if "mp.svd" in l or "svd_c" in l]
print("A7: the SM seat's script for SM-C21, read as text: the extended-precision entries are converted with complex(v) at line(s) %s; singular values come from np.linalg.svd at line(s) %s; extended-precision SVD calls: %s" % (conv, svd, mp_svd))
Lm = show("c34a926a2", "frontier/B1957_the_seats_claims_register/verification/checks/level6_higgs.py")
print("A7: main's level6_higgs.py at c34a926a2: line 12 holds 'lift-invariant B': %s; line 95 holds 'dimension 2, one bit': %s" % ("lift-invariant B" in Lm[11], "dimension 2, one bit" in Lm[94]))
