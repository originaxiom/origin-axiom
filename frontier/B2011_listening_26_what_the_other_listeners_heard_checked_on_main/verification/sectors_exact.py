"""B2011 (main, 2026-11-26; data-free): exact sector polynomials of the six-move covariant unfolding W on the orbit of
(3,3,3) mod N, by characteristic polynomials over GF(p) for primes p = 1 mod 3 and the Chinese remainder theorem, run until
the product of the primes exceeds twice a bound on every coefficient.

- The orbit and the six moves are B2002's (`leaf`): L, R and their conjugates by C, C^-1. W pushes e_v to the sum of e_m(v).
- The neutral sector: W on the C-orbit classes, Q[orbit of m(v)][o] += 1 from a representative v (B2002's Q; its
  characteristic polynomial is W's on the C-invariant functions).
- The charged sector q = 1: on the size-3 C-orbits, basis b_o = sum_j w^-j e_{C^j v}; the entry [o'][o] is the sum over j and
  over the moves m with m(C^j v) = v' (the representative of o') of w^-j. Over GF(p), w is a primitive cube root of 1.
- The bound: ||W|| <= 6, so each coefficient of a sector polynomial of degree d is at most binomial(d, k) 6^k <= 7^d.
Imported by the B2011 scripts; prints nothing itself."""
import flint
from sympy import nextprime


def leaf(N, start=(3, 3, 3)):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    C = lambda v: (v[1], v[2], v[0]); Ci = lambda v: (v[2], v[0], v[1])
    s = tuple(c % N for c in start)
    seen, todo = {s}, [s]
    while todo:
        v = todo.pop()
        for g in (L, R, Li, Ri):
            u = g(v)
            if u not in seen:
                seen.add(u); todo.append(u)
    pts = sorted(seen)
    moves = [L, R, lambda v: C(L(Ci(v))), lambda v: C(R(Ci(v))), lambda v: Ci(L(C(v))), lambda v: Ci(R(C(v)))]
    return pts, moves, C


def sector_data(N, start=(3, 3, 3)):
    """Integer neutral matrix and the charged entries as (a, b) for a + b w, plus counts."""
    pts, moves, C = leaf(N, start)
    idx = {v: i for i, v in enumerate(pts)}
    fixed, c_orbs, orb_of = [], [], {}
    for v in pts:
        if v in orb_of:
            continue
        if C(v) == v:
            orb_of[v] = (len(fixed) + len(c_orbs), 0); fixed.append(v)
        else:
            o = len(fixed) + len(c_orbs)
            u = v
            for j in range(3):
                orb_of[u] = (o, j); u = C(u)
            c_orbs.append(v)
    # renumber: neutral classes in order of discovery
    reps = {}
    for v, (o, j) in orb_of.items():
        if j == 0:
            reps[o] = v
    d0 = len(reps)
    Q = [[0] * d0 for _ in range(d0)]
    for o, v in reps.items():
        for m in moves:
            Q[orb_of[m(v)][0]][o] += 1
    # charged: index size-3 orbits
    ch_index = {}
    for v in c_orbs:
        ch_index[orb_of[v][0]] = len(ch_index)
    d1 = len(ch_index)
    Ca = [dict() for _ in range(d1)]   # Ca[row][col] = [a, b] for a + b w
    pw = ((1, 0), (0, 1), (-1, -1))    # w^0, w^1, w^2 = -1 - w
    for v in c_orbs:
        col = ch_index[orb_of[v][0]]
        u = v
        for j in range(3):
            ph = pw[(3 - j) % 3]       # w^-j
            for m in moves:
                t = m(u)
                o2, jt = orb_of[t]
                if o2 in ch_index and jt == 0:
                    row = ch_index[o2]
                    e = Ca[row].setdefault(col, [0, 0]); e[0] += ph[0]; e[1] += ph[1]
            u = C(u)
    return dict(n=len(pts), fixed=len(fixed), d0=d0, d1=d1, Q=Q, Ca=Ca)


def _primes_1mod3(start_bits=61):
    p = int(nextprime(1 << start_bits))
    while True:
        if p % 3 == 1:
            g = 2
            while True:
                w = pow(g, (p - 1) // 3, p)
                if w != 1:
                    break
                g += 1
            yield p, w
        p = int(nextprime(p))


def exact_charpolys(data, log=None):
    """Exact integer characteristic polynomials (coefficients constant first) of the neutral and the q = 1 charged sector."""
    out = {}
    for name, d in (("neutral", data["d0"]), ("charged", data["d1"])):
        bound = 2 * 7 ** d + 1
        M = 1; res = None; nprimes = 0
        for p, w in _primes_1mod3():
            if name == "neutral":
                A = flint.nmod_mat(data["Q"], p)
            else:
                rows = [[0] * d for _ in range(d)]
                for r, dct in enumerate(data["Ca"]):
                    for c, (a, b) in dct.items():
                        rows[r][c] = (a + b * w) % p
                A = flint.nmod_mat(rows, p)
            cp = [int(c) for c in A.charpoly().coeffs()]
            if res is None:
                res = cp; M = p
            else:
                # CRT combine res (mod M) with cp (mod p)
                inv = pow(M, -1, p)
                res = [r + M * (((c - r) * inv) % p) for r, c in zip(res, cp)]
                M *= p
            nprimes += 1
            if M > bound:
                break
        coeffs = [r if r <= M // 2 else r - M for r in res]
        out[name] = flint.fmpz_poly(coeffs)
        if log:
            log("    %s sector: degree %d, %d primes of 62 bits (product > 2 * 7^d)" % (name, d, nprimes))
    return out["neutral"], out["charged"]


def halved_monic(f):
    """f(2x) / 2^deg f, for f monic: monic with integer coefficients."""
    cs = [int(c) for c in f.coeffs()]
    d = len(cs) - 1
    g = [c * 2 ** i for i, c in enumerate(cs)]
    assert all(c % 2 ** d == 0 for c in g)
    return flint.fmpz_poly([c // 2 ** d for c in g])
