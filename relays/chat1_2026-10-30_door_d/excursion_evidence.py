"""Door D (P-474), the web seat's data-free check: how much a history's excursions can tell the move clock from area.

A history's runs of one letter are the continued-fraction digits a of its endpoint; a run of a letters reaches height
about a/2 (B1813). Under the move clock (fair-coin letters; Minkowski's measure) the digits are i.i.d.
Geometric(1/2): p_M(a) = 2^-a (B1815). Under area, with the start drawn from the stationary (Gauss) measure, every digit
has the Gauss-Kuzmin law p_G(a) = -log2(1 - 1/(a+1)^2) (P-438: Gauss-Kuzmin runs, with infinite mean); from a
Lebesgue start this holds only asymptotically (the first digit is 1/(a(a+1))). Area's digits are weakly dependent;
part (3) gives the size of that approximation. Both clocks enter as the record's two dynamics models. Standard
library only; no measured value is read. The strip's depth (Im tau about 3, so a about 5-6) is the one data-derived
input, used as the record states it (P-373).

Throughout, the runs are read at positions fixed independently of their lengths; part (5) shows what a placement by
depth would change.

It prints:
 (1) the evidence one run of length a carries, ln(p_G(a)/p_M(a)) in nats (positive favours area);
 (2) the expected evidence per run: KL(M||G) for a move-clock world (uncapped), and KL(G||M) for an area world,
     which diverges like ln A; it is given with the digit capped at A in two ways: both laws conditioned on a <= A
     and renormalised, and runs deeper than A lumped into one cell; also an area world's median run;
 (3) three runs at given depths: the likelihood ratio in bits with the runs independent, and for three consecutive
     runs the exact Gauss-measure cylinder;
 (4) THE_BAR's gate (p < 0.01 after Bonferroni over m = 53 looks, 12.4 bits, as THE FINAL ACT'S BAR states it) used
     only as a yardstick, in three readings: as a likelihood ratio; as the Sellke-Bayarri-Berger bound on the Bayes
     factor at that p (P-479 converts p-values so); as the p-value of the likelihood-ratio statistic with the move
     clock as the null;
 (5) a placement by depth, as illustration: the deepest of N runs.
"""
import math

LN2 = math.log(2)
AMAX = 60  # digits above 60 carry move-clock mass below 2^-60


def pM(a): return 2.0 ** -a
def pG(a): return -math.log2(1 - 1 / (a + 1) ** 2)
def ev(a): return math.log(pG(a) / pM(a))
def TM(a): return 2.0 ** -a                          # move clock: P(run > a)
def TG(a): return math.log2((a + 2) / (a + 1))       # Gauss-Kuzmin: P(run > a)
def FM(a): return 1 - TM(a)                          # P(run <= a)
def FG(a): return 1 - TG(a)


print("(1) evidence per run, ln(p_G/p_M) in nats (positive favours area)")
for a in (1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 20, 25):
    print(f"   a = {a:2d}  height about {a / 2:4.1f}   {ev(a):+.3f}")

print("(2) expected evidence per run (nats)")
kl_mg = sum(pM(a) * math.log(pM(a) / pG(a)) for a in range(1, 400))
print(f"   a move-clock world, uncapped: KL(M||G) = {kl_mg:.4f} (favours the move clock; {-kl_mg:+.4f} in (1)'s sign)")
print("   an area world: KL(G||M) diverges like ln A (the Gauss-Kuzmin tail); capped at A:")


def kl_gm_renormalised(A):
    g = [pG(a) for a in range(1, A + 1)]; m = [pM(a) for a in range(1, A + 1)]
    sg, sm = sum(g), sum(m)
    return sum((x / sg) * math.log((x / sg) / (y / sm)) for x, y in zip(g, m))


def kl_gm_lumped(A):
    body = sum(pG(a) * math.log(pG(a) / pM(a)) for a in range(1, A + 1))
    tg, tm = TG(A), TM(A)
    return body + tg * math.log(tg / tm)


for A in (6, 10, 20, 50, 200, 1000):
    print(f"   A = {A:5d}   conditioned on a <= A, renormalised: {kl_gm_renormalised(A):.4f}"
          f"   deeper runs lumped into one cell: {kl_gm_lumped(A):.4f}")
print(f"   an area world's median run: P_G(a <= 2) = {FG(2):.4f}; a run of 2 carries {ev(2):+.3f} nats")

print("(3) three runs at given depths: bits of likelihood ratio (positive favours area)")
for trip in ((4, 4, 4), (5, 5, 5), (6, 6, 6), (6, 5, 4), (9, 9, 9), (10, 10, 10), (11, 11, 11)):
    print(f"   runs {trip}, independent: {sum(ev(a) for a in trip) / LN2:6.2f} bits")


def gauss_cylinder(digits):
    """Gauss measure of the set of x in (0,1) whose first continued-fraction digits are `digits` (by the measure's
    shift invariance, also the probability that any given consecutive digits are these)."""
    p0, q0, p1, q1 = 1, 0, 0, 1  # p_{-1}, q_{-1}, p_0, q_0
    for a in digits:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
    x1, x2 = p1 / q1, (p1 + p0) / (q1 + q0)
    return abs(math.log2((1 + x1) / (1 + x2)))


for trip in ((6, 6, 6), (9, 9, 9), (11, 11, 11)):
    lr = gauss_cylinder(trip) / 2.0 ** -sum(trip)
    print(f"   runs {trip}, consecutive, the exact Gauss-measure cylinder: {math.log2(lr):6.2f} bits")

print("(4) THE_BAR's gate used as a yardstick")
p_gate = 0.01 / 53
bits_lr = -math.log2(p_gate)
sbb = 1 / (-math.e * p_gate * math.log(p_gate))
print(f"   the gate: p < 0.01/53 = {p_gate:.3e}, that is {bits_lr:.3f} bits (stated as 12.4)")
print(f"   (a) as a likelihood ratio of {bits_lr:.2f} bits;"
      f" (b) the SBB bound at that p, 1/(-e p ln p) = {sbb:.1f} = {math.log2(sbb):.2f} bits")
first_a = next(a for a in range(1, 40) if 3 * ev(a) / LN2 >= bits_lr)
first_b = next(a for a in range(1, 40) if 3 * ev(a) / LN2 >= math.log2(sbb))
print(f"   three equal runs first reach (a) at a = {first_a} ({3 * ev(first_a) / LN2:.2f} bits),"
      f" (b) at a = {first_b} ({3 * ev(first_b) / LN2:.2f} bits)")
lv = {a: ev(a) for a in range(1, AMAX + 1)}
wv = {a: pM(a) for a in range(1, AMAX + 1)}


def p_value_three(t):
    """P_M(l(a1) + l(a2) + l(a3) >= t), three i.i.d. runs on the move clock (digits above AMAX dropped)."""
    tot = 0.0
    for a1 in range(1, AMAX + 1):
        for a2 in range(1, AMAX + 1):
            r = t - lv[a1] - lv[a2]; w12 = wv[a1] * wv[a2]
            tot += w12 * sum(wv[a3] for a3 in range(1, AMAX + 1) if lv[a3] >= r - 1e-12)
    return tot


for a in (6, 8, 9):
    pv = p_value_three(3 * ev(a))
    print(f"   (c) three runs of a = {a}: p = {pv:.3e} ({-math.log2(pv):.2f} bits); passes the gate: {pv < p_gate}")

print("(5) a placement by depth, as illustration: the deepest of N runs equals a")
for N, a in ((64, 6), (64, 9)):
    PMx = FM(a) ** N - FM(a - 1) ** N; PGx = FG(a) ** N - FG(a - 1) ** N
    print(f"   N = {N}, deepest = {a}: P_M = {PMx:.4g}, P_G = {PGx:.4g},"
          f" {math.log2(PMx / PGx):+.2f} bits for the move clock")
