#!/usr/bin/env python3
"""B1871 -- one tick or two acts: the advisor seat's sealed run, re-derived by main (data-free: integers and SnapPy).

The record's grammar has two acts, L and R.  The owner's founding rule (a -> ab, b -> a; B1323, B1607) is one act, the TICK:
add, and the two sides change roles.  As matrices the tick is F = L P with P the exchange, and F F = L R.

  a two-act history   a cyclic word in L and R with both letters, not a repetition of a shorter word
  a tick history      a cyclic sequence of run lengths (r_1, ..., r_m), not a repetition: the monodromy is (L^r1 P)(L^r2 P)...(L^rm P).
                      With m even it is the two-act history L^r1 R^r2 ... ; with m odd it reverses orientation, and done twice it
                      is the two-act history of the doubled sequence.

The seat's code was read and not run.  Everything below is main's own.

    python3 -B frontier/B1871_one_tick_or_two_acts_verified/verification/tick_on_main.py
"""
import itertools
import warnings
from fractions import Fraction

warnings.filterwarnings("ignore")
say = print
SW = str.maketrans("LR", "RL")


def necklace(w): return min(w[s:] + w[:s] for s in range(len(w)))
def primitive(seq): return not any(len(seq) % d == 0 and seq == seq[:d] * (len(seq) // d) for d in range(1, len(seq)))
def cyc(seq): return min(seq[s:] + seq[:s] for s in range(len(seq)))


def compositions(n):
    for cuts in itertools.product((0, 1), repeat=n - 1):
        out, run = [], 1
        for c in cuts:
            if c: out.append(run); run = 1
            else: run += 1
        out.append(run)
        yield tuple(out)


def word_of(runs):
    """the two-act word of a run sequence of even length, or of an odd one done twice"""
    seq = runs if len(runs) % 2 == 0 else runs + runs
    return "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(seq))


# ------------------------------------------------------------------ T1: what exists
two_act, tick_only = {}, {}
for n in range(1, 13):
    words = {necklace("".join(t)) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}
    two_act[n] = sorted(w for w in words if primitive(w))
    odd = {cyc(c) for c in compositions(n) if len(c) % 2 == 1}
    tick_only[n] = sorted(c for c in odd if primitive(c))
say("T1. histories with n letters, n = 1 .. 12")
say("  two-act histories:                       %s" % " ".join(str(len(two_act[n])) for n in range(1, 13)))
say("  added by the tick (an odd number of runs): %s" % " ".join(str(len(tick_only[n])) for n in range(1, 13)))
assert [len(two_act[n]) for n in range(1, 13)] == [0, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335]
assert [len(tick_only[n]) for n in range(1, 13)] == [1, 1, 1, 2, 3, 5, 9, 16, 28, 51, 93, 170]
# a cross-check that does not use the definition of a word: the even run sequences, counted as run sequences, are the two-act
# histories up to the exchange of the letters (a rotation of the runs by one place is the swap)
even_runs = {n: {cyc(c) for c in compositions(n) if len(c) % 2 == 0} for n in range(2, 13)}
classes = {n: {min(w, necklace(w.translate(SW))) for w in {necklace("".join(t)) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}} for n in range(2, 13)}
ok_even = all(len(even_runs[n]) == len(classes[n]) for n in range(2, 13))
say("  cross-check: run sequences with an even number of runs = two-act words up to the exchange of the letters, for every n: %s" % ok_even)
assert ok_even
tot2, tott = sum(len(two_act[n]) for n in range(1, 13)), sum(len(tick_only[n]) for n in range(1, 13))
say("  to 12 letters: %d two-act histories and %d added by the tick, a ratio of %.3f" % (tot2, tott, tott / tot2))

# ------------------------------------------------------------------ T2: handedness of the two-act histories, by the law of B1867
def stab(w):
    out = []
    for rev in (0, 1):
        for sw in (0, 1):
            u = w[::-1] if rev else w
            u = u.translate(SW) if sw else u
            out += [(s, rev, sw) for s in range(len(w)) if u[s:] + u[:s] == w]
    return out
H8 = [w for n in range(2, 9) for w in two_act[n]]
own = [w for w in H8 if any(sw for (_, _, sw) in stab(w))]
doubles = sorted({necklace(word_of(c)) for n in range(1, 5) for c in tick_only[n]})                 # tick histories of 1 to 4 letters, done twice
by_rot = [w for w in own if any(sw and not rev for (_, rev, sw) in stab(w))]                         # its own mirror by an odd rotation of the runs
by_ref = [w for w in own if w not in by_rot]
partners = {frozenset((w, necklace(w.translate(SW)))) for w in H8 if w not in own}
say("T2. the %d two-act histories with at most 8 letters, by the law (a history is its own mirror exactly when its stabiliser holds the swap):" % len(H8))
say("  its own mirror: %d -- %d by a rotation with the swap (they are the tick histories done twice: %s), %d by a reflection with the swap: %s" % (
    len(own), len(by_rot), sorted(by_rot) == doubles, len(by_ref), " ".join(sorted(by_ref))))
say("  with a distinct mirror partner: %d histories in %d pairs; the shortest pair: %s" % (len(H8) - len(own), len(partners), " and ".join(sorted(min(partners, key=lambda p: (len(min(p)), sorted(p)))))))
assert (len(H8), len(own), len(by_rot), len(by_ref), len(partners)) == (69, 11, 5, 6, 29) and sorted(by_rot) == doubles

# ------------------------------------------------------------------ T3: the exchange at the levels (integers)
def mul(A, B, N): return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N, (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)
def group(gens, N):
    one = (1 % N, 0, 0, 1 % N); seen = {one}; fr = [one]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = mul(a, g, N)
                if x not in seen: seen.add(x); nx.append(x)
        fr = nx
    return seen
Lm, Rm, Pm = (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 0)
rowsT3 = []
for N in (2, 3, 4, 5, 7, 8):
    g2 = group([tuple(x % N for x in Lm), tuple(x % N for x in Rm)], N)
    g3 = group([tuple(x % N for x in Lm), tuple(x % N for x in Pm)], N)
    rowsT3.append((N, len(g2), len(g3), tuple(x % N for x in Pm) in g2))
say("T3. level N: the group of the two acts, the group with the exchange, the exchange already inside: %s" % "; ".join("%d: %d, %d, %s" % (N, a, b, "yes" if c else "no") for N, a, b, c in rowsT3))
assert rowsT3 == [(2, 6, 6, True), (3, 24, 48, False), (4, 48, 96, False), (5, 120, 240, False), (7, 336, 672, False), (8, 384, 768, False)]
F = mul(Lm, Pm, 10 ** 9)                                                   # the tick, as integers
assert mul(F, F, 10 ** 9) == mul(Lm, Rm, 10 ** 9)                          # two ticks are LR
tr, det = F[0] + F[3], F[0] * F[3] - F[1] * F[2]
say("  the tick F = L P = %s: trace %d, determinant %d; F F = L R: True; its characteristic polynomial t^2 - t - 1 is (t - 3)^2 mod 5: %s" % (
    F, tr, det, (9 - 3 - 1) % 5 == 0 and (2 * 3 - 1) % 5 == 0))
v = (1, 2); orbit = [v]
for _ in range(4):
    v = ((F[0] * v[0] + F[1] * v[1]) % 5, (F[2] * v[0] + F[3] * v[1]) % 5); orbit.append(v)
say("  on the golden line at level 5 the tick acts by: %s  (multiplication by %d; up to sign it exchanges (1,2) and (2,4))" % (" -> ".join(str(x).replace(" ", "") for x in orbit), next(c for c in range(5) if ((c * 1) % 5, (c * 2) % 5) == orbit[1])))
fixed1, inv1 = abs((F[0] - 1) * (F[3] - 1) - F[1] * F[2]), abs((F[0] + 1) * (F[3] + 1) - F[1] * F[2])
F2 = mul(F, F, 10 ** 9)
fixed2, inv2 = abs((F2[0] - 1) * (F2[3] - 1) - F2[1] * F2[2]), abs((F2[0] + 1) * (F2[3] + 1) - F2[1] * F2[2])
say("  fibre characters fixed and inverted: by one tick %d and %d (the trivial one only); by two ticks %d and %d" % (fixed1, inv1, fixed2, inv2))
assert orbit == [(1, 2), (3, 1), (4, 3), (2, 4), (1, 2)] and (fixed1, inv1, fixed2, inv2) == (1, 1, 1, 5)

# ------------------------------------------------------------------ T4: a single act alone
def fixed_directions(M):
    """the discriminant of the fixed directions of a 2x2 integer matrix acting on lines: a square means rational directions"""
    a, b, c, d = M
    disc = (a - d) ** 2 + 4 * b * c
    r = int(abs(disc) ** 0.5)
    return disc, disc >= 0 and r * r == disc
t4 = {name: fixed_directions(M) for name, M in (("L", Lm), ("R", Rm), ("the bare exchange", Pm), ("the tick", (1, 1, 1, 0)))}
say("T4. a single act alone: its fixed directions are rational for %s, and irrational for %s (discriminant %d: the golden direction)" % (
    ", ".join(k for k, (dsc, rat) in t4.items() if rat), ", ".join(k for k, (dsc, rat) in t4.items() if not rat), t4["the tick"][0]))
assert [rat for _, rat in t4.values()] == [True, True, True, False] and t4["the tick"][0] == 5
Pp = mul(Pm, Pm, 10 ** 9)
say("  the bare exchange done twice is the identity: %s -- by the principle's first clause it is not an act by itself" % (Pp == (1, 0, 0, 1)))

# ------------------------------------------------------------------ SnapPy: T2 against the manifolds, and T2b
try:
    import snappy
except ImportError:
    snappy = None
if snappy is None:
    say("SnapPy is not installed here: the comparison with the manifolds (T2, T2b) is skipped")
else:
    g = snappy.Manifold("b-+L")
    assert g.is_isometric_to(snappy.Manifold("m000")) and not g.is_orientable() and g.orientation_cover().is_isometric_to(snappy.Manifold("m004"))
    say("SnapPy control: b-+L is m000, non-orientable, and its orientation cover is m004")
    agree = sum(1 for w in H8 if bool(snappy.Manifold("b++" + w).symmetry_group().is_amphicheiral()) == (w in own))
    say("T2 against SnapPy: the law's 'its own mirror' agrees with SnapPy on %d of %d histories" % (agree, len(H8)))
    assert agree == len(H8)
    odd_h = [c for n in range(1, 8) for c in tick_only[n]]
    nonor = cover = 0
    for c in odd_h:
        wd = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(c))             # the run sequence as an alternating word, closed by the exchange
        M = snappy.Manifold("b-+" + wd)
        if not M.is_orientable(): nonor += 1
        if M.orientation_cover().is_isometric_to(snappy.Manifold("b++" + word_of(c))): cover += 1
    say("T2b. the %d tick histories with at most 7 letters and an odd number of runs: non-orientable %d of %d; orientation cover = the same history done twice: %d of %d" % (
        len(odd_h), nonor, len(odd_h), cover, len(odd_h)))
    assert nonor == len(odd_h) == cover

# ------------------------------------------------------------------ main's addition: the tick on the weave's own six-dimensional space
# B1610's module (main's): the moves L, R and the exchange P as 6 x 6 unitary matrices on V = T + conj T, the weave's triplet and its conjugate.
import importlib.util
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("hands_for_b1871", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
Hm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Hm)
ML6, MR6, MP6 = Hm.W.ML, Hm.W.MR, Hm.W.MP
Tb, Tc = Hm.PIECES["T"], Hm.PIECES["Tbar"]
proj = lambda Bm: Bm @ np.linalg.pinv(Bm)
into = lambda M, src, dst: bool(np.allclose(proj(dst) @ (M @ src), M @ src, atol=1e-9))
def grp(gens, cap=5000):
    key = lambda M: tuple(np.round(M.flatten(), 6).view(float))
    one = np.eye(gens[0].shape[0], dtype=complex); seen = {key(one): one}; fr = [one]
    while fr:
        nx = []
        for a in fr:
            for g_ in gens:
                x = a @ g_
                k = key(x)
                if k not in seen:
                    seen[k] = x; nx.append(x)
                    assert len(seen) < cap
        fr = nx
    return list(seen.values())
def commutant_dim(gens):
    n = gens[0].shape[0]
    rows = [np.kron(np.eye(n), g_) - np.kron(g_.T, np.eye(n)) for g_ in gens]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-8))
G2, G3 = grp([ML6, MR6]), grp([ML6, MP6])
tick6 = ML6 @ MP6
say("On the weave's six-dimensional space (B1610's matrices, main's): the two acts keep the triplet: %s, %s; the exchange carries it into its conjugate: %s, and the conjugate into it: %s" % (
    into(ML6, Tb, Tb), into(MR6, Tb, Tb), into(MP6, Tb, Tc), into(MP6, Tc, Tb)))
keyM = lambda M: tuple(np.round(M.flatten(), 6).view(float))
in_G2 = lambda M: keyM(M) in {keyM(g_) for g_ in G2}
# the exchange enters with a lift, fixed only up to the two acts' group; what does not depend on that lift is stated
say("  the exchange normalises the two acts' group (it carries L and R to elements of it: %s, %s), and the tick done twice lies in that group: %s" % (
    in_G2(MP6 @ ML6 @ np.linalg.inv(MP6)), in_G2(MP6 @ MR6 @ np.linalg.inv(MP6)), in_G2(tick6 @ tick6)))
assert in_G2(MP6 @ ML6 @ np.linalg.inv(MP6)) and in_G2(MP6 @ MR6 @ np.linalg.inv(MP6)) and in_G2(tick6 @ tick6) and not in_G2(MP6) and not in_G2(tick6)
say("  the group of the two acts on it has %d elements and commutant of dimension %d (two pieces, the triplet and its conjugate); with the exchange: %d elements, commutant of dimension %d (one piece)" % (
    len(G2), commutant_dim([ML6, MR6]), len(G3), commutant_dim([ML6, MP6])))
assert into(MP6, Tb, Tc) and into(MP6, Tc, Tb) and not into(MP6, Tb, Tb) and len(G2) == 96 and commutant_dim([ML6, MR6]) == 2 and commutant_dim([ML6, MP6]) == 1
say("  so with the tick as an act the triplet and its conjugate are one object: the tick gives the three no hand, it joins the two hands.")

