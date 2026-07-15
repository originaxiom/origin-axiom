"""B637 repair — the LITERAL chain machine: formal ZG-chains, s, d, Phi,
Psi implemented as chain operations; H1, H2 by the recursion; the
homotopy identity verified FORMALLY before any omega evaluation.

Chains: dict key -> [int coeff, witness], key = (fp(coeffword),
fp(w1), ..., fp(wn)) with Gamma-fingerprints (exact parabolic SL(2)),
witness = (coeffword, w1, ..., wn) for later evaluation.
The section SIGMA is a GLOBAL function element-fp -> word.
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


class Q3:
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0):
        s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): return Q3(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Q3(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return Q3(s.a * o.a - 3 * s.b * o.b,
                                 s.a * o.b + s.b * o.a)
    def key(s): return (s.a, s.b)


OMq = Q3(Fr(1, 2), Fr(1, 2))
GENQ = {'a': [[Q3(1), Q3(1)], [Q3(0), Q3(1)]],
        'b': [[Q3(1), Q3(0)], [OMq, Q3(1)]],
        'A': [[Q3(1), Q3(-1)], [Q3(0), Q3(1)]],
        'B': [[Q3(1), Q3(0)], [Q3(0) - OMq, Q3(1)]]}
FPC = {}


def fp(w):
    w = freduce(w)
    if w not in FPC:
        M = [[Q3(1), Q3(0)], [Q3(0), Q3(1)]]
        for ch in w:
            g = GENQ[ch]
            M = [[M[i][0] * g[0][j] + M[i][1] * g[1][j] for j in range(2)]
                 for i in range(2)]
        FPC[w] = tuple(M[i][j].key() for i in range(2) for j in range(2))
    return FPC[w]


SIGMA = {}


def sigma(w):
    """the GLOBAL section: element -> canonical word (first spelling seen)."""
    f = fp(w)
    if f not in SIGMA:
        SIGMA[f] = freduce(w)
    return SIGMA[f]


def sig_set(w, word):
    f = fp(w)
    assert f not in SIGMA or SIGMA[f] == freduce(word), "section conflict"
    SIGMA[f] = freduce(word)


class Chain:
    """formal sum of coeffword*[w1|...|wn]."""
    def __init__(self):
        self.d = {}
    def add(self, coeffw, cells, c=1):
        coeffw = freduce(coeffw)
        cells = tuple(freduce(x) for x in cells)
        # NORMALIZED bar complex: degenerate cells (identity in any slot) die
        if any(fp(x) == fp("") for x in cells):
            return
        key = (fp(coeffw),) + tuple(fp(x) for x in cells)
        if key in self.d:
            self.d[key][0] += c
            if self.d[key][0] == 0:
                del self.d[key]
        else:
            self.d[key] = [c, (coeffw,) + cells]
    def madd(self, other, mult=1):
        for key, (c, wit) in other.d.items():
            if key in self.d:
                self.d[key][0] += mult * c
                if self.d[key][0] == 0:
                    del self.d[key]
            else:
                self.d[key] = [mult * c, wit]
    def translate(self, g):
        out = Chain()
        for key, (c, wit) in self.d.items():
            out.add(freduce(g + wit[0]), wit[1:], c)
        return out
    def is_zero(self):
        return not self.d
    def terms(self):
        return [(c, wit) for (c, wit) in
                ((v[0], v[1]) for v in self.d.values())]


def boundary(ch_):
    """the bar boundary of an n-chain (n = len(cells))."""
    out = Chain()
    for (c, wit) in ch_.terms():
        k = wit[0]
        cells = wit[1:]
        n = len(cells)
        # d(k[g1|...|gn]) = kg1[g2|..] + sum (-1)^i k[..|gigi+1|..]
        #                 + (-1)^n k[g1|..|gn-1]
        out.add(freduce(k + cells[0]), cells[1:], c)
        for i in range(1, n):
            merged = cells[:i - 1] + (freduce(cells[i - 1] + cells[i]),) \
                     + cells[i + 1:]
            out.add(k, merged, c * (-1) ** i)
        out.add(k, cells[:-1], c * (-1) ** n)
    return out


def scontract(ch_):
    """s(k[g1|..|gn]) = [k|g1|..|gn] (Z-linear)."""
    out = Chain()
    for (c, wit) in ch_.terms():
        out.add("", (wit[0],) + wit[1:], c)
    return out


def fox_positions(w):
    out = []
    for i, ch in enumerate(w):
        pre = w[:i]
        if ch.islower():
            out.append((pre, ch, +1))
        else:
            out.append((freduce(pre + ch), ch.lower(), -1))
    return out


def Phi1Psi1(coeffw, w):
    """Phi1 Psi1 of coeffw*[w] as a 1-chain (uses the GLOBAL section)."""
    out = Chain()
    sw = sigma(w)
    for (pre, ch, sgn) in fox_positions(sw):
        out.add(freduce(coeffw + pre), (ch,), sgn)
    return out


CERT_CACHE = {}


def certify(word):
    w0 = freduce(word)
    if w0 == "":
        return []
    if w0 in CERT_CACHE:
        return CERT_CACHE[w0]
    seen = {w0: (None, None, None)}
    beam = [(len(w0), w0)]
    for depth in range(1, 20):
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
        beam = heapq.nsmallest(800, ((len(nw), nw) for nw in cand))
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


def Phi2_fr(coeffw, mult=1):
    """coeffw * Phi2(f_r): the corrected bar 2-chain of the relator."""
    out = Chain()
    pre = ""
    for ch in REL:
        out.add(coeffw, (pre, ch), mult)
        if ch in 'AB':
            # correction: - p_{i-1} [l^-1 | l]  (prefix BEFORE the letter;
            # the p_i transcription error was THE part-2b bug)
            out.add(freduce(coeffw + pre), (ch, ch.lower()), -mult)
        pre = freduce(pre + ch)
    return out


def Phi2Psi2(coeffw, g, h, mult=1):
    """Phi2 Psi2 of coeffw*[g|h] (global section; certificate)."""
    out = Chain()
    sg, sh, sgh = sigma(g), sigma(h), sigma(freduce(g + h))
    defect = freduce(sg + sh + inv(sgh))
    for (u, e) in certify(defect):
        out.madd(Phi2_fr(freduce(coeffw + u)), mult * e)
    return out


def H1(ch1):
    """H1: defined on GENERATORS [w] as s([w] - Phi1Psi1[w]), then extended
    ZG-LINEARLY: H1(k[w]) = k * H1([w]) — the coefficient stays OUTSIDE
    (early folding was the machine's second bug)."""
    out = Chain()
    for (c, wit) in ch1.terms():
        k, (w,) = wit[0], wit[1:]
        if freduce(w) == "":
            continue
        x = Chain()
        x.add("", (w,), 1)
        x.madd(Phi1Psi1("", w), -1)
        base = scontract(x)                 # coefficient-1 generator chain
        out.madd(base.translate(k), c)      # equivariant extension
    return out


def H2_cell(g, h):
    """H2([g|h]) literally: s([g|h] - Phi2Psi2([g|h]) - H1(d2[g|h]))."""
    y = Chain()
    y.add("", (g, h), 1)
    y.madd(Phi2Psi2("", g, h), -1)
    d2 = Chain()
    d2.add(g, (h,), 1)
    d2.add("", (freduce(g + h),), -1)
    d2.add("", (g,), 1)
    y.madd(H1(d2), -1)
    return scontract(y), y


def homotopy_check(g, h):
    """verify d3 H2([g|h]) == y  (the homotopy identity, formally)."""
    H2c, y = H2_cell(g, h)
    lhs = boundary(H2c)
    lhs.madd(y, -1)
    return lhs.is_zero(), H2c


print("== the literal chain machine: formal homotopy checks ==", flush=True)
# fix the global section on the peripheral elements FIRST (canonical words)
sig_set("a", "a")
sig_set(LONG, LONG)
sig_set(freduce("a" + LONG), freduce("a" + LONG))
sig_set(freduce("a" + LONG + "a"), freduce("a" + LONG + "a"))
sig_set(freduce(LONG + "a" + LONG), freduce(LONG + "a" + LONG))

for (g, h) in (("a", "b"), ("a", LONG), (LONG, "a"),
               (freduce("a" + LONG), "a"), ("a", freduce("a" + LONG))):
    ok, _ = homotopy_check(g, h)
    print(f"  d3 H2 = id - Phi2Psi2 - H1 d2 on [{g[:6]}..|{h[:6]}..]: {ok}",
          flush=True)

# the formal deltaS = omega residual with the literal H2:
def S_chain(g, h):
    H2c, _ = H2_cell(g, h)
    return H2c


def formal_deltaS_minus_omega(g, h, k):
    tot = Chain()
    tot.madd(S_chain(h, k), +1)
    tot.madd(S_chain(freduce(g + h), k), -1)
    tot.madd(S_chain(g, freduce(h + k)), +1)
    tot.madd(S_chain(g, h), -1)
    om = Chain()
    om.add("", (g, h, k), 1)
    tot.madd(om, -1)
    # drop identity-slot cells (omega vanishes there) and coefficient-fold:
    # NOTE: cells here have a leading coeff slot from scontract("") = "";
    # evaluation folds coeffword into slot 1 ALREADY via scontract, so all
    # coeff words are "" and cells are genuine [x|y|z]; drop identity slots.
    resid = {}
    for (c, wit) in tot.terms():
        cw = wit[0]
        cells = wit[1:]
        assert cw == "" or fp(cw) == fp(""), "unfolded coefficient?"
        if any(fp(x) == fp("") for x in cells):
            continue
        key = tuple(fp(x) for x in cells)
        resid[key] = resid.get(key, 0) + c
        if resid[key] == 0:
            del resid[key]
    return resid


MU, LAM = "a", LONG
r1 = formal_deltaS_minus_omega(MU, LAM, MU)
print(f"\nformal (deltaS - omega) residual on [mu|lam|mu]: {len(r1)} cells",
      flush=True)
r2 = formal_deltaS_minus_omega("a", "b", "a")
print(f"formal (deltaS - omega) residual on [a|b|a]: {len(r2)} cells",
      flush=True)
r3 = formal_deltaS_minus_omega(LAM, MU, LAM)
print(f"formal (deltaS - omega) residual on [lam|mu|lam]: {len(r3)} cells",
      flush=True)
if not (r1 or r2 or r3):
    print("\nTHE LITERAL MACHINE IS EXACT: deltaS = omega holds FORMALLY — "
          "ready to re-evaluate the 3-form with it.", flush=True)
print("chain machine check DONE", flush=True)
