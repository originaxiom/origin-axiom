"""B1970 (P-295, P-847; main, 2026-11-20; data-free): the record's dictionary supplies two Higgs doublets of opposite
hypercharge, one per sector type, and the frame's holomorphic coupling then reads S in every sector.

 D1  the 10 of the record's 27 (B1253's dictionary: hypercharge from B1252's derived direction, main's code imported
     unchanged): its states and hypercharges; expected two SU(2) doublets at Y = +1/2 and -1/2 and a colour-triplet pair.
 D2  the dictionary's Yukawa terms 10 . 16 . 16 (B1253's cubic triples): for each Standard Model operator, the
     hypercharge of the 10-state it uses (Q u^c, Q d^c, L e^c, L nu^c), by hypercharge alone; and whether the up
     operator and the down and lepton operators use the same state or two distinct ones.
 D3  the frame's sector charges (B1656's SIXY, 6Y: Q 1, u^c -4, d^c 2, L -3, e^c 6): the Higgs charge each sector's
     coupling needs, q_H = -(q_L + q_R), against D2.
 D4  holomorphy in tau: the frame's Higgs coefficients (DR's three components, frame C's te.ev of B[1]) and a matter
     residue (kap theta[cs] theta[ds] / (2 pi eta^3) at a fixed line point) satisfy d/d(conj tau) = 0 (finite
     differences); the conjugate reading's coefficients conj(c_k(tau)) do not (they satisfy d/d tau = 0 instead).
     Also: a twist of either sign of characteristic is holomorphic (theta[+a, b] and theta[-a, -b] both), which is
     agy-exp's F3 point and is not what D4 tests.
 D5  frame C with every sector reading S: the cusp mixing at three points of order 5, height 30 (B1946's measure).
    python3 -B two_doublets.py > two_doublets_run.txt"""
import sys, pathlib, itertools, collections
from fractions import Fraction as F
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1253_*")) / "verification"))
import sm_sector as SM

Y, (one, ten, sixteen), wts = SM.hypercharges()
print("D1: the 10's hypercharges:", sorted(collections.Counter(Y[i] for i in ten).items()))
print("    the 16's hypercharges:", sorted(collections.Counter(Y[i] for i in sixteen).items()), "; the 1:", [Y[i] for i in one])
lab16 = {F(1, 6): "Q", F(-2, 3): "u^c", F(1, 3): "d^c", F(-1, 2): "L", F(1): "e^c", F(0): "nu^c"}
trip = SM.cubic_triples(wts)
yuk = []
for t in trip:
    a = [i for i in t if i in ten]; b = [i for i in t if i in sixteen]
    if len(a) == 1 and len(b) == 2: yuk.append((a[0], b[0], b[1]))
print("D2: Yukawa-type triples 10.16.16:", len(yuk))
ops = collections.defaultdict(set)
for h, i, j in yuk:
    pair = tuple(sorted((lab16[Y[i]], lab16[Y[j]])))
    ops[pair].add((h, Y[h]))
for pair in (("Q", "u^c"), ("Q", "d^c"), ("L", "e^c"), ("L", "nu^c")):
    hs = ops.get(tuple(sorted(pair)), set())
    print("    %-10s uses 10-states with Y = %s (states %s)" % (" ".join(pair), sorted({y for _, y in hs}), sorted({h for h, _ in hs})))
up_states = {h for h, _ in ops[tuple(sorted(("Q", "u^c")))]}; dn_states = {h for h, _ in ops[tuple(sorted(("Q", "d^c")))]}; le_states = {h for h, _ in ops[tuple(sorted(("L", "e^c")))]}
print("    the up operator's 10-states and the down operator's are disjoint: %s; the down and lepton operators share theirs: %s" % (not (up_states & dn_states), dn_states == le_states))
print("    every Yukawa triple conserves Y: %s" % all(Y[h] + Y[i] + Y[j] == 0 for h, i, j in yuk))

SIXY = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6}
for sec, (l, r), op in (("up", ("Q", "u^c"), ("Q", "u^c")), ("down", ("Q", "d^c"), ("Q", "d^c")), ("lepton", ("L", "e^c"), ("L", "e^c"))):
    qH = -(SIXY[l] + SIXY[r]); need = F(qH, 6)
    have = sorted({y for _, y in ops[tuple(sorted(op))]})
    print("D3: the frame's %-6s sector needs a Higgs of 6Y = %+d, Y = %s; the dictionary's %s operator uses Y = %s: %s" % (sec, qH, need, " ".join(op), have, have == [need]))

sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp; te = DL.FM.te; B = DL.FM.B
mp.mp.dps = 40
def dbar(fn, t, h=mp.mpf(10) ** -12):
    return (fn(t + h) - fn(t - h)) / (4 * h) + 1j * (fn(t + 1j * h) - fn(t - 1j * h)) / (4 * h)   # (d_x + i d_y)/2
def dhol(fn, t, h=mp.mpf(10) ** -12):
    return (fn(t + h) - fn(t - h)) / (4 * h) - 1j * (fn(t + 1j * h) - fn(t - 1j * h)) / (4 * h)   # (d_x - i d_y)/2
for t in (mp.mpc(0.13, 1.4), mp.mpc(-0.31, 2.2)):
    for k in range(3):
        c = lambda z, k=k: te.ev(te.B[1][k], z)
        cb = lambda z, k=k: mp.conj(te.ev(te.B[1][k], z))
        print("D4: tau %s, Higgs component %d: |d c/d conj tau| / |d c/d tau| = %.1e; for conj(c): |d/d tau| / |d/d conj tau| = %.1e" % (
            mp.nstr(t, 3), k, float(abs(dbar(c, t)) / abs(dhol(c, t))), float(abs(dhol(cb, t)) / abs(dbar(cb, t)))))
    th = lambda z: B.thc_mp(mp.mpf(3) / 10, mp.mpf(7) / 10, 0, z) * B.thc_mp(mp.mpf(1) / 10, mp.mpf(9) / 10, 0, z)
    thm = lambda z: B.thc_mp(-mp.mpf(3) / 10, -mp.mpf(7) / 10, 0, z) * B.thc_mp(-mp.mpf(1) / 10, -mp.mpf(9) / 10, 0, z)
    print("D4: tau %s, a matter residue's theta product: |d/d conj tau| / |d/d tau| = %.1e; with both characteristics negated (F3's case) %.1e" % (
        mp.nstr(t, 3), float(abs(dbar(th, t)) / abs(dhol(th, t))), float(abs(dbar(thm, t)) / abs(dhol(thm, t)))))

sys.path.insert(0, str(next((ROOT / "frontier").glob("B1946_*")) / "verification"))
import same_reading as SR
r = SR.pair_stats(30.0, [(F(1, 5), F(2, 5)), (F(2, 5), F(4, 5)), (F(0), F(3, 5))])
d, o = min(x[0] for x in r[("S", "S")]), max(x[1] for x in r[("S", "S")])
print("D5: every sector reading S, height 30, three points of order 5: smallest diagonal |V| %.6f, largest off-diagonal %.2e" % (d, o))
