#!/usr/bin/env python3
"""Main's own recomputation of the SM seat's census "the line's room on every companion" (harvest row 908).

WHAT IS RECOMPUTED.  For every word state in L and R of length 2 to 8 (both letters, primitive, up to rotation and the
swap, either sign) whose fixed-point companion N has at most 12 ends, and for EVERY sign character chi of pi_1(N):

    h1   = dim H^1(N; chi)
    r1   = rank of the restriction H^1(N; chi) -> sum over the ends on which chi is trivial of H^1(T^2)
    n    = h1 - r1                 (the room of the line)
    m_A  = the number of ends on which chi is trivial

WHOSE CODE.  Main's.  The states are enumerated by main's B1434; the companion is built as main's B1494 builds it (the
regular cover with deck group H_1(M) / <the peripheral subgroup>); the cohomology is read here by Fox calculus on
SnapPy's presentation of pi_1(N), in exact arithmetic modulo two primes that are not the seat's.  No line of the seat's
census script, and none of any other session's verifier, is imported or run.  The seat's committed OUTPUT is read, as
data, only to be compared with (compare_with_the_seat).

HOW IT COULD FAIL.  (1) a character that is not a homomorphism is refused (every relator must evaluate to 1); (2) at
the trivial character h1 must be the number of ends and the room 0 (main's B1494, a theorem); (3) the companions of
+LLLR and -LR must be the manifolds main's B1493 read by name; (4) a planted fault (the restriction left out; one end
left out) must change the table, or the comparison could not have failed.

    python3 room_census_on_main.py            # the census, written beside this file
    python3 room_census_on_main.py --planted  # the same with each planted fault, on four states
"""
import sys, json, itertools, math, pathlib, collections
import numpy as np
import snappy, sympy
from sympy.matrices.normalforms import smith_normal_decomp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1434_the_architecture_census" / "verification"))
import architecture_census as ac          # main's enumerator of states

PRIMES = (1000000007, 2147483647)         # not the seat's two
MAXLEN, MAXENDS = 8, 12


def bundle_name(state):
    return "b+" + ("+" if state[0] == "+" else "-") + state[1:]


def exp_vec(w, gens):
    return [sum((1 if ch.islower() else -1) for ch in w if ch.lower() == g) for g in gens]


def deck_map(M):
    """generators -> T = H_1(M) / <peripheral subgroup>, as main's B1494 reads it (Smith normal form)"""
    G = M.fundamental_group(); gens = G.generators()
    rows = [exp_vec(r, gens) for r in G.relators()] + [exp_vec(w, gens) for ml in G.peripheral_curves() for w in ml]
    S, U, V = smith_normal_decomp(sympy.Matrix(rows), sympy.ZZ)
    n = len(gens); d = [int(S[i, i]) if i < min(S.shape) else 0 for i in range(n)]
    imgs = [tuple((int(V[j, i]) % d[i]) if d[i] else int(V[j, i]) for i in range(n)) for j in range(n)]
    tors = [i for i in range(n) if d[i] > 1]
    assert not [i for i in range(n) if d[i] == 0], "the quotient by the peripheral subgroup has a free part"
    return [d[i] for i in tors], [tuple(im[i] for i in tors) for im in imgs]


def companion(state):
    M = snappy.Manifold(bundle_name(state))
    assert M.is_orientable()
    ds, imgs = deck_map(M); T = math.prod(ds) if ds else 1
    if T == 1:
        return M, T
    elems = list(itertools.product(*[range(x) for x in ds])); idx = {e: i for i, e in enumerate(elems)}
    perms = [[idx[tuple((e[i] + im[i]) % ds[i] for i in range(len(ds)))] for e in elems] for im in imgs]
    return M.cover(perms), T


def ends_of(state):
    """|det(eps M - 1)| for the state's monodromy: the number of ends its companion must have"""
    L = sympy.Matrix([[1, 1], [0, 1]]); R = sympy.Matrix([[1, 0], [1, 1]]); m = sympy.eye(2)
    for ch in state[1:]:
        m = m * (L if ch == "L" else R)
    eps = 1 if state[0] == "+" else -1
    return abs(int((eps * m - sympy.eye(2)).det()))


# ------------------------------------------------------------------------------------------------ the cohomology
def word_letters(w, index):
    return [(index[ch.lower()], 1 if ch.islower() else -1) for ch in w]


def fox_row(letters, s, n):
    """the row of c(w) = sum_j row[j] c(g_j) for a cocycle c of the line chi, chi(g_j) = s[j] = +-1:
    c(ab) = c(a) + chi(a) c(b), c(g^-1) = -chi(g)^-1 c(g).  Returns (row, chi(w))."""
    row = [0] * n; pre = 1
    for j, e in letters:
        if e == 1:
            row[j] += pre; pre *= s[j]
        else:
            pre *= s[j]; row[j] -= pre          # chi(g^-1) = s[j] for a sign
    return row, pre


def rank_mod(A, p):
    A = np.array(A, dtype=np.int64) % p
    if A.size == 0:
        return 0
    rows, cols = A.shape; r = 0
    for c in range(cols):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        piv = r + int(nz[0])
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        others = np.nonzero(A[:, c])[0]; others = others[others != r]
        if len(others):
            A[others] = (A[others] - (A[others, c][:, None] * A[r][None, :]) % p) % p
        r += 1
        if r == rows:
            break
    return r


def sign_characters(rel_exp, n):
    """every s in {+1, -1}^n with every relator evaluating to 1: the null space over GF(2) of the relators' exponent sums"""
    rows = [[x % 2 for x in r] for r in rel_exp]; piv = []; r = 0
    rows = [row[:] for row in rows]
    for c in range(n):
        k = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if k is None:
            continue
        rows[r], rows[k] = rows[k], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[r])]
        piv.append(c); r += 1
    free = [c for c in range(n) if c not in piv]
    for bits in itertools.product((0, 1), repeat=len(free)):
        e = [0] * n
        for c, b in zip(free, bits):
            e[c] = b
        for i, c in enumerate(piv):
            e[c] = sum(rows[i][f] * e[f] for f in free) % 2
        yield tuple(-1 if x else 1 for x in e)


def read_state(state, planted=None):
    N, T = companion(state)
    G = N.fundamental_group(); gens = G.generators(); n = len(gens); index = {g: j for j, g in enumerate(gens)}
    rels = [word_letters(r, index) for r in G.relators()]
    cusps = [(word_letters(mu, index), word_letters(lam, index)) for mu, lam in G.peripheral_curves()]
    assert N.num_cusps() == len(cusps) == T == ends_of(state), (state, N.num_cusps(), T, ends_of(state))
    rel_exp = [exp_vec(r, gens) for r in G.relators()]
    cells = collections.Counter(); n_chars = 0; n_at_trivial = None
    for s in sign_characters(rel_exp, n):
        n_chars += 1
        J = []
        for r in rels:
            row, val = fox_row(r, s, n)
            assert val == 1, "not a homomorphism"                      # control (1)
            J.append(row)
        trivial = all(x == 1 for x in s)
        res, m_A = [], 0
        for k, (mu, lam) in enumerate(cusps):
            rm, vm = fox_row(mu, s, n); rl, vl = fox_row(lam, s, n)
            if vm == 1 and vl == 1:
                m_A += 1
                if planted == "one end left out" and k == 0:
                    continue
                res += [rm, rl]
        if planted == "the restriction left out":
            res = []
        out = []
        for p in PRIMES:
            rj = rank_mod(J, p)
            h1 = (n - rj) - (0 if trivial else 1)
            r1 = (rank_mod(J + res, p) - rj) if res else 0
            out.append((h1, r1))
        assert out[0] == out[1], ("the two primes disagree", state, s, out)
        h1, r1 = out[0]
        cells[(m_A, h1, r1, h1 - r1)] += 1
        if trivial:
            n_at_trivial = h1 - r1
            if planted is None:
                assert h1 == T, ("b_1 of the companion is not its number of ends", state, h1, T)     # control (2)
    hist = collections.Counter()
    for (m_A, h1, r1, room), k in cells.items():
        hist[room] += k
    return {"state": state, "ends": T, "generators": n, "relators": len(rels), "sign characters": n_chars, "n(1)": n_at_trivial,
            "room histogram": {str(k): hist[k] for k in sorted(hist)},
            "(m_A, h1, r1, n): characters": {str(list(k)): cells[k] for k in sorted(cells)},
            "largest min(n, m_A)": max(min(room, m_A) for (m_A, h1, r1, room) in cells),
            "largest room": max(hist),
            "largest m_A at a room of three or more": max([m_A for (m_A, h1, r1, room) in cells if room >= 3], default=None),
            "largest room at three or more trivial ends": max([room for (m_A, h1, r1, room) in cells if m_A >= 3], default=None)}


def the_states():
    out = []
    for w in ac.states(MAXLEN):
        for eps in "+-":
            if ends_of(eps + w) <= MAXENDS:
                out.append(eps + w)
    return out


if __name__ == "__main__":
    if "--planted" in sys.argv:
        res = {}
        for st in ("+LLLR", "-LR", "-LLRR", "-LLRLR"):
            clean = read_state(st)
            for fault in ("the restriction left out", "one end left out"):
                bad = read_state(st, planted=fault)
                res["%s | %s" % (st, fault)] = {"table changed": bad["(m_A, h1, r1, n): characters"] != clean["(m_A, h1, r1, n): characters"],
                                               "room histogram, clean": clean["room histogram"], "room histogram, planted": bad["room histogram"]}
                print("%-8s %-26s table changed: %s" % (st, fault, res["%s | %s" % (st, fault)]["table changed"]), flush=True)
        (HERE / "room_census_on_main_planted.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
        sys.exit(0)
    states = the_states()
    print("states with at most %d ends: %d" % (MAXENDS, len(states)), flush=True)
    out = []
    for st in states:
        r = read_state(st); out.append(r)
        print("%-10s ends %2d  characters %5d  n(1) %s  rooms %s  largest min(n, m_A) %d" % (st, r["ends"], r["sign characters"], r["n(1)"], r["room histogram"], r["largest min(n, m_A)"]), flush=True)
    # control (3): two companions by name
    names = {}
    for st, name in (("+LLLR", "L8a15"), ("-LR", "o10_150729")):
        N, T = companion(st)
        names[st] = bool(N.is_isometric_to(snappy.Manifold(name)))
        print("the companion of %s is %s: %s" % (st, name, names[st]), flush=True)
    total = sum(r["sign characters"] for r in out)
    res = {"primes": list(PRIMES), "states": out, "sign characters in all": total, "companions by name": names,
           "n(1) = 0 on every companion": all(r["n(1)"] == 0 for r in out),
           "every character with a room of three or more is trivial on at most one end": all((r["largest m_A at a room of three or more"] or 0) <= 1 for r in out),
           "every character trivial on three or more ends has a room of at most two": all((r["largest room at three or more trivial ends"] or 0) <= 2 for r in out),
           "largest room on any companion": max(r["largest room"] for r in out)}
    (HERE / "room_census_on_main.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print("sign characters in all: %d | n(1) = 0 everywhere: %s | largest room: %d" % (total, res["n(1) = 0 on every companion"], res["largest room on any companion"]))
    print("room of three or more only with at most one trivial end: %s | three or more trivial ends only with room at most two: %s"
          % (res["every character with a room of three or more is trivial on at most one end"], res["every character trivial on three or more ends has a room of at most two"]))
