"""B637 repair — the FORMAL chain check: the S-expansion's cells must
satisfy delta S = omega as a formal identity (cells identified by
GROUP-element equality via exact SL(2) fingerprints). The nonzero
residual multiset names the bug exactly. No 27-dim evaluation needed.
"""
import heapq
from fractions import Fraction as Fr

REL = "abABaBAbaB"
RELI = REL[::-1].swapcase()
LONG = "abABaaBAbA"


def freduce(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase():
            out.pop()
        else:
            out.append(ch)
    return "".join(out)


def inv(w):
    return w[::-1].swapcase()


# exact SL(2,Q(sqrt-3)) fingerprints: entries (a, b) as Fractions, w = a+b*s
class Q3:
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0):
        s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): return Q3(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Q3(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return Q3(s.a * o.a - 3 * s.b * o.b,
                                 s.a * o.b + s.b * o.a)
    def key(s): return (s.a, s.b)


OM = Q3(Fr(1, 2), Fr(1, 2))
M_a = [[Q3(1), Q3(1)], [Q3(0), Q3(1)]]
M_b = [[Q3(1), Q3(0)], [OM, Q3(1)]]
M_A = [[Q3(1), Q3(-1)], [Q3(0), Q3(1)]]
M_B = [[Q3(1), Q3(0)], [Q3(0) - OM, Q3(1)]]
GEN = {'a': M_a, 'b': M_b, 'A': M_A, 'B': M_B}
FP_CACHE = {}


def fp(w):
    w = freduce(w)
    if w not in FP_CACHE:
        M = [[Q3(1), Q3(0)], [Q3(0), Q3(1)]]
        for ch in w:
            g = GEN[ch]
            M = [[M[i][0] * g[0][j] + M[i][1] * g[1][j] for j in range(2)]
                 for i in range(2)]
        FP_CACHE[w] = tuple(M[i][j].key() for i in range(2) for j in range(2))
    return FP_CACHE[w]


ID_FP = fp("")


def cellkey(x, y, z):
    fx, fy, fz = fp(x), fp(y), fp(z)
    if fx == ID_FP or fy == ID_FP or fz == ID_FP:
        return None                       # identity slot: omega = 0, drop
    return (fx, fy, fz)


CERT_CACHE = {}


def certify(word):
    w0 = freduce(word)
    if w0 == "":
        return []
    if w0 in CERT_CACHE:
        return CERT_CACHE[w0]
    seen = {w0: (None, None, None)}
    beam = [(len(w0), w0)]
    for depth in range(1, 18):
        cand = {}
        for _, w in beam:
            for ins, sgn in ((REL, +1), (RELI, -1)):
                for i in range(len(w) + 1):
                    nw = freduce(w[:i] + ins + w[i:])
                    if nw not in seen and nw not in cand:
                        cand[nw] = (w, i, sgn)
        seen.update(cand)
        if "" in cand:
            break
        beam = heapq.nsmallest(600, ((len(nw), nw) for nw in cand))
    chain = []
    node = ""
    while seen[node][0] is not None:
        parent, i, sgn = seen[node]
        chain.append((parent, i, sgn))
        node = parent
    chain.reverse()
    cert = []
    w = w0
    for (parent, i, sgn) in chain:
        cert.append((w[:i], -sgn))
        w = freduce(w[:i] + (REL if sgn > 0 else RELI) + w[i:])
    prod = ""
    for (u, e) in cert:
        prod += u + (REL if e > 0 else RELI) + inv(u)
    assert freduce(prod) == w0
    CERT_CACHE[w0] = cert
    return cert


def rel_chain():
    cells = []
    pre = ""
    for ch in REL:
        cells.append(("", pre, ch, +1))
        if ch in 'AB':
            nxt = freduce(pre + ch)
            cells.append((nxt, ch, ch.lower(), -1))
        pre = freduce(pre + ch)
    return cells


RELCHAIN = rel_chain()


def fox_positions(w):
    out = []
    for i, ch in enumerate(w):
        pre = w[:i]
        if ch.islower():
            out.append((pre, ch, +1))
        else:
            out.append((freduce(pre + ch), ch.lower(), -1))
    return out


def S_cells(g, h, gh):
    """the exact cell list of my S_eval, as (x, y, z, coeff)."""
    cells = []
    cells.append(("", g, h, +1))                     # s([g|h])
    for (u, e) in certify(g + h + inv(gh)):
        for (cw, s1, s2, sgn) in RELCHAIN:
            cells.append((freduce(u + cw), s1, s2, -e * sgn))
    # - s(g H1[h]) -> -[g|1|h] + sum sgn [g|pre|x]
    cells.append((g, "", h, -1))
    for (pre, ch, sgn) in fox_positions(h):
        cells.append((g, pre, ch, sgn))
    # + s(H1[gh]) -> +[1|1|gh] - sum sgn [1|pre|x]
    cells.append(("", "", gh, +1))
    for (pre, ch, sgn) in fox_positions(gh):
        cells.append(("", pre, ch, -sgn))
    # - s(H1[g]) -> -[1|1|g] + sum sgn [1|pre|x]
    cells.append(("", "", g, -1))
    for (pre, ch, sgn) in fox_positions(g):
        cells.append(("", pre, ch, sgn))
    return cells


def accumulate(target, cells, mult):
    for (x, y, z, c) in cells:
        k = cellkey(x, y, z)
        if k is None:
            continue
        target[k] = target.get(k, 0) + mult * c
        if target[k] == 0:
            del target[k]


def check_cell(g, h, k, gh, hk, ghk, label):
    tot = {}
    accumulate(tot, S_cells(h, k, hk), +1)
    accumulate(tot, S_cells(gh, k, ghk), -1)
    accumulate(tot, S_cells(g, hk, ghk), +1)
    accumulate(tot, S_cells(g, h, gh), -1)
    kk = cellkey(g, h, k)
    if kk is not None:
        tot[kk] = tot.get(kk, 0) - 1
        if tot[kk] == 0:
            del tot[kk]
    print(f"[{label}] residual cells: {len(tot)}", flush=True)
    if tot:
        # decode fingerprints back to a witness word where possible
        for kres, c in list(tot.items())[:12]:
            print(f"    coeff {c:+d} at fp-cell (words unknown; "
                  f"fp hash {hash(kres) & 0xffffffff:08x})", flush=True)
    return tot


MU, LAM = "a", LONG
PROD = freduce("a" + LONG)
GHK = freduce("a" + LONG + "a")
print("formal delta S = omega check:", flush=True)
r1 = check_cell(MU, LAM, MU, PROD, PROD, GHK, "mu|lam|mu")
r2 = check_cell("a", "b", "a", "ab", "ba", "aba", "a|b|a")
r3 = check_cell(LAM, MU, LAM, PROD, PROD, freduce(LONG + "a" + LONG),
                "lam|mu|lam")

if not (r1 or r2 or r3):
    print("\nALL FORMAL CHECKS CANCEL — the S-expansion is exact; the bug "
          "must be in the 27-dim evaluation layer, not the cell algebra.",
          flush=True)
else:
    print("\nRESIDUALS FOUND — the cell algebra itself deviates; the bug is "
          "in the S-expansion.", flush=True)
print("formal check DONE", flush=True)
