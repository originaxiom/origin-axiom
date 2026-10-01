#!/usr/bin/env python3
"""B1434 -- THE ARCHITECTURE CENSUS: the complete Standard-Model-frame doublet census (lifted and non-lifted
backgrounds) on the generated state space, not on m004's tower alone.

STATES.  A state is a signed cyclic word  s = (eps, w),  eps = +1 or -1,  w a word in L, R with both letters, taken up
to cyclic rotation and the swap L <-> R.  Its carrier is the once-punctured-torus bundle with monodromy eps * A(w),
A(L) = [[1,1],[0,1]], A(R) = [[1,0],[1,1]].  m004 = (+, LR), m003 = (-, LR), m009 = (+, LLR), m010 = (-, LLR).
LEVELS.  Level k of a state is the k-fold cyclic cover dual to the fibre, the bundle with monodromy (eps A)^k.

PRESENTATION.  F = <x, y> the fibre group.  tau_x: x -> x, y -> y x  and  tau_y: x -> x y, y -> y  both fix the
commutator [x, y] = x y x^-1 y^-1 exactly and act on H_1 by L and R.  iota: x -> c x^-1 c^-1, y -> c y^-1 c^-1 with
c = y x fixes [x, y] exactly and acts by -I.  phi = (iota if eps = -1) o (product of tau's along w), and level k uses
phi^k.  pi_1 = <x, y, t | t x t^-1 = phi^k(x), t y t^-1 = phi^k(y)>, peripheral pair  mu = t,  lambda = [x, y]
(phi fixes lambda, so t commutes with it; lambda is primitive on the cusp and t maps to the base generator).
THE DECK of level k over the state is  x -> phi(x), y -> phi(y), t -> t.

The census itself is B1432's: characters of pi_1 trivial on mu with values in mu_N, N the torsion exponent; every
candidate module (lambda, alpha); index by main's B1427 code; three primes, the firing modules re-checked at the
other two; backgrounds from (theta, psi_Y, W) with lambda = theta^2 / W, counted once by their six sector modules.
"""
import sys, json, time, itertools, math, pathlib
from collections import Counter, defaultdict
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1432_the_three_fold_cover_fires_off_the_lift" / "verification"))
import cover_census as cc                      # (inserts B1427's verification dir on sys.path itself)
from myindex import index

X, Y, T = 1, 2, 3                              # generator numbers; negative = inverse

def inv(w): return [-g for g in reversed(w)]
def reduce(w):
    out = []
    for g in w:
        if out and out[-1] == -g: out.pop()
        else: out.append(g)
    return out
def apply(aut, w):                             # aut: dict {X: word, Y: word}
    out = []
    for g in w: out += aut[g] if g > 0 else inv(aut[-g])
    return reduce(out)
def compose(a, b):                             # (a o b)(g) = a(b(g))
    return {X: apply(a, b[X]), Y: apply(a, b[Y])}

TAU = {"L": {X: [X], Y: [Y, X]}, "R": {X: [X, Y], Y: [Y]}}
C = [Y, X]
IOTA = {X: reduce(C + [-X] + inv(C)), Y: reduce(C + [-Y] + inv(C))}
IDENT = {X: [X], Y: [Y]}
COMM = [X, Y, -X, -Y]

def monodromy(eps, word):
    phi = IDENT
    for ch in word: phi = compose(phi, TAU[ch])
    if eps < 0: phi = compose(IOTA, phi)
    assert apply(phi, COMM) == COMM, "phi must fix the commutator exactly"
    return phi

def hmat(phi):
    def ex(w): return [sum(1 if g == X else -1 if g == -X else 0 for g in w), sum(1 if g == Y else -1 if g == -Y else 0 for g in w)]
    a, b = ex(phi[X]), ex(phi[Y])
    return [[a[0], b[0]], [a[1], b[1]]]        # columns = images of x, y

def level(eps, word, k):
    phi = monodromy(eps, word); P = IDENT
    for _ in range(k): P = compose(phi, P)
    rels = [reduce([T, X, -T] + inv(P[X])), reduce([T, Y, -T] + inv(P[Y]))]
    tau = {X: phi[X], Y: phi[Y], T: [T]}
    A = hmat(P); tors = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    return 3, rels, [T], COMM, tau, A, tors

def torsion_exponent(A):
    g = math.gcd(math.gcd(A[0][0] - 1, A[1][1] - 1), math.gcd(A[0][1], A[1][0]))
    d = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    return d // g if g else 0                  # invariant factors (g, d/g); exponent d/g

def census(eps, word, k, pstart=3000, nprimes=3):
    """the B1432 census on level k of the state (eps, word); returns the summary dict"""
    ng, rels, mu, lam, tau, A, tors = level(eps, word, k)
    if tors == 0: return dict(state=("+" if eps > 0 else "-") + word, k=k, torsion=0, skipped="b1 > 1")
    N = max(1, torsion_exponent(A))
    saved = cc.cover
    cc.cover = lambda _n: (ng, rels, mu, lam, tau)
    try:
        o, bgs, I, chars, _ = cc.census(k, N, pstart, nprimes=nprimes, verbose=False)
    finally:
        cc.cover = saved
    assert o["characters"] == tors, (o["characters"], tors)
    o.update(state=("+" if eps > 0 else "-") + word, k=k, trace=A[0][0] + A[1][1], torsion=tors, exponent=N)
    for key in ("tau", "seconds", "n"): o.pop(key, None)
    return o

def cyc_min(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def primitive(w): return all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
def states(maxlen):
    seen = set(); out = []
    for n in range(2, maxlen + 1):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if len(set(w)) < 2 or not primitive(w): continue
            key = min(cyc_min(w), cyc_min(swap(w)))
            if key in seen: continue
            seen.add(key); out.append(key)
    return out

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "control":                      # C1: m004's tower, levels 1..5 (level 6 with --six)
        res = [census(+1, "LR", k) for k in range(1, 7 if "--six" in sys.argv else 6)]
        for o in res: print(o["k"], o["torsion"], o["loci"], o["loci_nonsquare"], o["candidates"], o["firing"], o["generation_backgrounds"], o["lifted"], o["backgrounds_by_orbit_size"], flush=True)
        json.dump(res, open(HERE / "control_m004_tower.json", "w"), indent=1)
    elif mode == "run":
        maxlen, tmax = int(sys.argv[2]), int(sys.argv[3]); kmax = int(sys.argv[4]); res = []
        for w in states(maxlen):
            for eps in (+1, -1):
                for k in range(1, kmax + 1):
                    ng, rels, mu, lam, tau, A, tors = level(eps, w, k)
                    if tors == 0 or tors > tmax: continue
                    t0 = time.time(); o = census(eps, w, k); o["seconds"] = round(time.time() - t0, 1); res.append(o)
                    print(o["state"], k, "tr", o["trace"], "tors", o["torsion"], "loci", o["loci"], "nonsq", o["loci_nonsquare"], "fire", o["firing"],
                          "gen", o["generation_backgrounds"], "lifted", o["lifted"], "orbits", o["backgrounds_by_orbit_size"], "absI", o["abs_counts"],
                          "signs", o["signs"], "h1", o["h1_multiset"], "differ", o["differing_at_other_primes"], flush=True)
                    json.dump(res, open(HERE / f"architecture_census_len{maxlen}_t{tmax}.json", "w"), indent=1)
