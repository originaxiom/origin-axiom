#!/usr/bin/env python3
"""B1602 -- THE FORCED COVER ON EVERY THREAD: the common point's cover on every thread to length eight, read at every
sign character of the four.  W3 gives every thread a finite quotient from the quaternion point: A4 for odd trace (the
image 2T mod +-1), D4 when the act fixes one parity (Q16 mod +-1), V4 when it fixes all three (Q8 mod +-1).  The forced
covers of a thread are the kernels of the surjections q: pi_1(M) -> A4 / D4 / V4 whose restriction to the fibre
F = ker(eps: pi_1 -> Z) is the parity map -- onto V4 (the fibre's image lies in a Klein four-subgroup for D4; equals V4 for
V4; for A4 the composite to A4/V4 = Z/3 is eps mod 3).  Every such kernel is read (the sign and choice variants are
among them); the four at every sign character by B1492's stacked instrument (40 digits); a member is n > 0.

    python3 forced_every.py b++LR b+-LR ...        -> forced_<name>.json beside this file, one summary line per thread
    python3 forced_every.py threads 8              -> the signed thread names to length 8 (SnapPy's b+<sign>w)
    python3 forced_every.py census 8               -> every signed thread to length 8, summaries to census_8.jsonl"""
import sys, json, itertools, pathlib, time
import snappy
import sympy as sp
from sympy.combinatorics import Permutation
from mpmath import mpc
HERE = pathlib.Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    raise RuntimeError("repository root not found")


ROOT = _root()
sys.path.insert(0, str(ROOT / "frontier" / "B1492_the_three_ended_companion_read" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1493_the_room_on_the_companions" / "verification"))
import multicusp as MC          # noqa: E402
import room as RM               # noqa: E402

E = (0, 1, 2, 3)
mul = lambda p, q: tuple(p[q[i]] for i in range(4))
inv = lambda p: tuple(sorted(range(4), key=lambda i: p[i]))


def closure(gens):
    G = {E}; fr = [E]
    while fr:
        p = fr.pop()
        for g in gens:
            q = mul(p, g)
            if q not in G:
                G.add(q); fr.append(q)
    return G


A4 = sorted(p for p in itertools.permutations(range(4)) if Permutation(list(p)).is_even)
r, s = (1, 2, 3, 0), (0, 3, 2, 1)
D4 = sorted(closure([r, s]))
KLEINS = [frozenset(closure([mul(r, r), s])), frozenset(closure([mul(r, r), mul(r, s)]))]
V4 = sorted(closure([mul(r, r), s]))
PAIRINGS = [frozenset([frozenset([0, 1]), frozenset([2, 3])]), frozenset([frozenset([0, 2]), frozenset([1, 3])]), frozenset([frozenset([0, 3]), frozenset([1, 2])])]
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}


def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]
        A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]


def parity_class(w):
    """how the act permutes the three non-zero parities: 3 (a 3-cycle), 1 (fixes one), 0 (fixes all)"""
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]
        A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 2 for j in range(2)) for i in range(2))
    par = [(1, 0), (0, 1), (1, 1)]
    fixed = sum(1 for v in par if tuple((A[i][0] * v[0] + A[i][1] * v[1]) % 2 for i in range(2)) == v)
    return {0: 3, 1: 1, 3: 0}[fixed]


def words(nmax):
    seen, out = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
                continue
            ex = w.translate(str.maketrans("LR", "RL"))
            c = min(min(v[i:] + v[:i] for i in range(n)) for v in (w, ex))
            if c not in seen:
                seen.add(c); out.append(c)
    return out


def threads(nmax):
    return [f"b+{sg}{w}" for w in words(nmax) for sg in "+-"]


def to_z3(p):
    img = [PAIRINGS.index(frozenset(frozenset(p[i] for i in pair) for pair in P)) for P in PAIRINGS]
    return 0 if img == [0, 1, 2] else (1 if img == [1, 2, 0] else 2)


def word_image(w, img):
    p = E
    for ch in w:
        p = mul(p, img[ch] if ch.islower() else inv(img[ch.lower()]))
    return p


def z_map(G):
    gens, rels = G.generators(), G.relators()
    A = sp.Matrix([[sum((1 if ch == g else -1 if ch == g.upper() else 0) for ch in rr) for g in gens] for rr in rels])
    ns = A.nullspace(); assert len(ns) == 1, ("b1 != 1", A)
    v = ns[0]; v = v * sp.ilcm(*[sp.fraction(c)[1] for c in v]); g = sp.igcd(*[int(c) for c in v])
    return {gg: int(c) // g for gg, c in zip(gens, v)}


def surjections(G, group, size):
    gens, rels = G.generators(), G.relators(); out = []
    for imgs in itertools.product(group, repeat=len(gens)):
        img = dict(zip(gens, imgs))
        if all(word_image(rr, img) == E for rr in rels) and len(closure(list(imgs))) == size:
            out.append(img)
    return out


def fibre_image(G, img, eps):
    """the image of the fibre ker(eps): the normal closure in the image group of the images of g t^{-eps(g)}"""
    gens = G.generators()
    t0 = next((g for g in gens if eps[g] == 1), None) or next(g.upper() for g in gens if eps[g] == -1)
    T = word_image(t0, img); base = []
    for g in gens:
        Tk = E
        for _ in range(abs(eps[g])):
            Tk = mul(Tk, T if eps[g] > 0 else inv(T))
        base.append(mul(word_image(g, img), inv(Tk)))
    grp = closure([img[g] for g in gens])
    return frozenset(closure(base + [mul(mul(x, b), inv(x)) for x in grp for b in base]))


def kernel_key(G, img):
    """a fingerprint of the kernel: the words to length five that map to the identity"""
    gens = G.generators(); letters = list(gens) + [g.upper() for g in gens]
    return frozenset(w for n in range(1, 6) for w in ("".join(t) for t in itertools.product(letters, repeat=n)) if word_image(w, img) == E)


def forced(M):
    G = M.fundamental_group(); eps = z_map(G); w = M.name()[3:]; pc = parity_class(w)
    if pc == 3:
        group, label = A4, "A4"
        good = [img for img in surjections(G, A4, 12) if any(all(to_z3(img[g]) == (sg * eps[g]) % 3 for g in G.generators()) for sg in (1, -1))]
    elif pc == 1:
        group, label = D4, "D4"
        good = [img for img in surjections(G, D4, 8) if fibre_image(G, img, eps) in KLEINS]
    else:
        group, label = V4, "V4"
        good = [img for img in surjections(G, V4, 4) if fibre_image(G, img, eps) == frozenset(V4)]
    ks = {}
    for img in good:
        ks.setdefault(kernel_key(G, img), img)
    return G, eps, label, group, good, list(ks.values())


def site_of(N):
    H = N.high_precision(); S = RM.Room.__new__(RM.Room); S.name = N.name(); S.M = H; Gh = H.fundamental_group()
    S.gens = Gh.generators(); S.rels = Gh.relators(); S.cusps = Gh.peripheral_curves()
    S.rho = {g: MC.matrix([[mpc(MC.num(Gh.SL2C(g)[i, j].real()), MC.num(Gh.SL2C(g)[i, j].imag())) for j in range(2)] for i in range(2)]) for g in S.gens}
    S.m = len(S.cusps); return S


def read(N):
    S = site_of(N); rows = []
    for vals, nu in RM.sign_characters(S):
        c = S.counts(S.four(nu)); rows.append({"nu": list(vals), "h1": c["a1"], "r1": c["r1"], "n": c["n"]})
    return rows


def run(name):
    t0 = time.time(); M = snappy.Manifold(name)
    G, eps, label, group, good, ks = forced(M)
    out = {"thread": name, "word": name[3:], "trace": (1 if name[2] == "+" else -1) * trace(name[3:]), "orientable": M.is_orientable(),
           "homology": str(M.homology()), "deck": label, "forced_surjections": len(good), "kernels": len(ks), "covers": []}
    for img in ks:
        perms = [[group.index(mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()]
        N = M.cover(perms); rows = read(N); members = [x for x in rows if x["n"] > 0]
        out["covers"].append({"cover_homology": str(N.homology()), "cusps": N.num_cusps(), "volume_ratio": round(float(N.volume() / M.volume()), 9),
                              "sign_characters": len(rows), "members": len(members),
                              "member_structures": sorted({(x["h1"], x["r1"], x["n"]) for x in members}),
                              "trivial": next(x for x in rows if all(v == 1 for v in x["nu"])), "rows": rows})
    out["any_member"] = any(c["members"] for c in out["covers"]); out["s"] = round(time.time() - t0, 1)
    (HERE / f"forced_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps({k: (v if k != "covers" else [{kk: vv for kk, vv in c.items() if kk != "rows"} for c in v]) for k, v in out.items()}, default=str), flush=True)
    return out


if __name__ == "__main__":
    if sys.argv[1] == "threads":
        print(" ".join(threads(int(sys.argv[2]))))
    elif sys.argv[1] == "census":
        with open(HERE / f"census_{sys.argv[2]}.jsonl", "a") as fh:
            done = {json.loads(l)["thread"] for l in open(HERE / f"census_{sys.argv[2]}.jsonl") if l.strip()} if (HERE / f"census_{sys.argv[2]}.jsonl").exists() else set()
            for n in threads(int(sys.argv[2])):
                if n in done:
                    continue
                o = run(n); fh.write(json.dumps({k: (v if k != "covers" else [{kk: vv for kk, vv in c.items() if kk != "rows"} for c in v]) for k, v in o.items()}, default=str) + "\n"); fh.flush()
    else:
        for n in sys.argv[1:]:
            run(n)
