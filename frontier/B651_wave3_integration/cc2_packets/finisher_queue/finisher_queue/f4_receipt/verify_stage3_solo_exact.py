#!/usr/bin/env python3
"""
F4 track-S verify: INDEPENDENT exact recompute of B649 stage 3a's SOLO
headline dimensions (h0(M_silver;27)=1, h1(M_silver;27)=3) -- the number
that reproduces the fig-8's solo h1=3, the "3" in the 3/5/1 grammar.

Fully in-reach from the persisted, hash-verified letters27_L.json alone
(no weld/lift reconstruction needed for the solo case -- only the
3-generator, 2-relator presentation acting on the 27-dim rep).

Own code: a fresh exact quotient-ring class for L = Q(s,i)/(s^4-8s^2-16)
(written from the field definition in the sealed preregs, not copied from
b649_stage3a.py), a fresh Fox-calculus row builder, and a fresh
fraction-free-pivot Gaussian elimination routine for the rank/nullity
(not cc's Span/L_nullspace_dim classes).
"""
import json
import time
from fractions import Fraction as Fr

SRC = "<seat-workdir>/origin-axiom/frontier/B649_silver_holonomy"

# ---------------------------------------------------------------------------
# L = Q(s,i), s^4 = 8 s^2 + 16.  Element: (re: 4-tuple, im: 4-tuple) over Q,
# basis {1,s,s^2,s^3} each.  Written independently (own convolution + own
# reduction step), no reuse of b649_stage3a.py code.
# ---------------------------------------------------------------------------
_RED = (Fr(16), Fr(0), Fr(8), Fr(0))  # s^4 -> 16 + 0 s + 8 s^2 + 0 s^3


def _conv_reduce(p, q):
    """multiply two degree<=3 poly's in s (4-tuples), reduce mod s^4-8s^2-16."""
    acc = [Fr(0)] * 7
    for i, pi in enumerate(p):
        if pi:
            for j, qj in enumerate(q):
                if qj:
                    acc[i + j] += pi * qj
    for deg in (6, 5, 4):
        c = acc[deg]
        if c:
            acc[deg] = Fr(0)
            shift = deg - 4
            for t, rc in enumerate(_RED):
                acc[shift + t] += c * rc
    return tuple(acc[:4])


class Lelt:
    __slots__ = ("re", "im")

    def __init__(self, re=(Fr(0),) * 4, im=(Fr(0),) * 4):
        self.re = tuple(re)
        self.im = tuple(im)

    def __add__(self, o):
        return Lelt(tuple(a + b for a, b in zip(self.re, o.re)),
                    tuple(a + b for a, b in zip(self.im, o.im)))

    def __sub__(self, o):
        return Lelt(tuple(a - b for a, b in zip(self.re, o.re)),
                    tuple(a - b for a, b in zip(self.im, o.im)))

    def __neg__(self):
        return Lelt(tuple(-a for a in self.re), tuple(-a for a in self.im))

    def __mul__(self, o):
        rr = _conv_reduce(self.re, o.re)
        ii = _conv_reduce(self.im, o.im)
        ri = _conv_reduce(self.re, o.im)
        ir = _conv_reduce(self.im, o.re)
        return Lelt(tuple(a - b for a, b in zip(rr, ii)),
                    tuple(a + b for a, b in zip(ri, ir)))

    def iszero(self):
        return not any(self.re) and not any(self.im)

    def conj(self):
        return Lelt(self.re, tuple(-a for a in self.im))

    def vec8(self):
        return self.re + self.im

    def inv(self):
        """own general field-inverse: solve (this * w) = 1 as an 8x8
        rational linear system, own pivoting (partial, first-nonzero)."""
        BAS = [Lelt((Fr(1), Fr(0), Fr(0), Fr(0)), (Fr(0),) * 4)]
        BAS += [Lelt((Fr(0), Fr(1), Fr(0), Fr(0)), (Fr(0),) * 4)]
        BAS += [Lelt((Fr(0), Fr(0), Fr(1), Fr(0)), (Fr(0),) * 4)]
        BAS += [Lelt((Fr(0), Fr(0), Fr(0), Fr(1)), (Fr(0),) * 4)]
        BAS += [Lelt((Fr(0),) * 4, (Fr(1), Fr(0), Fr(0), Fr(0)))]
        BAS += [Lelt((Fr(0),) * 4, (Fr(0), Fr(1), Fr(0), Fr(0)))]
        BAS += [Lelt((Fr(0),) * 4, (Fr(0), Fr(0), Fr(1), Fr(0)))]
        BAS += [Lelt((Fr(0),) * 4, (Fr(0), Fr(0), Fr(0), Fr(1)))]
        cols = [(self * b).vec8() for b in BAS]
        n = 8
        rows = [[cols[c][r] for c in range(n)] + [Fr(1) if r == 0 else Fr(0)]
                for r in range(n)]
        for piv in range(n):
            pr = next(r for r in range(piv, n) if rows[r][piv] != 0)
            rows[piv], rows[pr] = rows[pr], rows[piv]
            pv = rows[piv][piv]
            rows[piv] = [x / pv for x in rows[piv]]
            for r in range(n):
                if r != piv and rows[r][piv] != 0:
                    f = rows[r][piv]
                    rows[r] = [x - f * y for x, y in zip(rows[r], rows[piv])]
        sol = [rows[r][n] for r in range(n)]
        return Lelt(tuple(sol[:4]), tuple(sol[4:]))


ZERO = Lelt()
ONE = Lelt((Fr(1), Fr(0), Fr(0), Fr(0)))


def elt_from_json(vec8):
    return Lelt(tuple(Fr(x) for x in vec8[:4]), tuple(Fr(x) for x in vec8[4:]))


# ---------------------------------------------------------------------------
# load the persisted, hash-verified letters27_L.json (S1 side only -- the
# solo dimension needs nothing else)
# ---------------------------------------------------------------------------
d27 = json.load(open(f"{SRC}/letters27_L.json"))


def mat27(nm):
    return [[elt_from_json(d27[nm][i][j]) for j in range(27)] for i in range(27)]


t0 = time.time()
S1 = {nm: mat27(nm) for nm in "abcABC"}
print(f"loaded 6 letters (own Lelt class) in {time.time()-t0:.1f}s")


def mmul27(A, B):
    n = 27
    Bt = list(zip(*B))
    out = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nz = [(k, Ai[k]) for k in range(n) if not Ai[k].iszero()]
        for j in range(n):
            col = Bt[j]
            acc = ZERO
            for k, a in nz:
                b = col[k]
                if not b.iszero():
                    acc = acc + a * b
            out[i][j] = acc
    return out


# own sanity re-check of S2b-G1 on this fresh backend
for rel in ("aBAbcc", "aaCbcB"):
    t0 = time.time()
    M = None
    for ch in rel:
        M = S1[ch] if M is None else mmul27(M, S1[ch])
    ok = all((M[i][j] - (ONE if i == j else ZERO)).iszero() for i in range(27) for j in range(27))
    print(f"  own-backend recheck {rel} = I27 exactly: {ok}  ({time.time()-t0:.1f}s)")

# ---------------------------------------------------------------------------
# Fox-calculus rows for the SOLO presentation (own construction), + own
# fraction-free-ish Gaussian elimination over L for rank/nullity.
# ---------------------------------------------------------------------------
GENS = "abc"
RELATORS = ["aBAbcc", "aaCbcB"]


def fox_rows_solo():
    rows = []
    for w in RELATORS:
        blocks = {g: [[ZERO] * 27 for _ in range(27)] for g in GENS}
        P = [[ONE if i == j else ZERO for j in range(27)] for i in range(27)]
        for ch in w:
            g = ch.lower()
            if ch.islower():
                term = P
            else:
                PM = mmul27(P, S1[ch])
                term = [[ZERO - x for x in row] for row in PM]
            blocks[g] = [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(blocks[g], term)]
            P = mmul27(P, S1[ch])
        for i in range(27):
            rows.append([blocks[g][i][j] for g in GENS for j in range(27)])
    return rows


t0 = time.time()
rows = fox_rows_solo()
print(f"built {len(rows)} Fox rows x {len(rows[0])} cols in {time.time()-t0:.1f}s")


def rank_over_L(rows, ncols):
    """own Gaussian elimination over L, first-nonzero pivoting."""
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    for c in range(ncols):
        piv = None
        for k in range(r, m):
            if not A[k][c].iszero():
                piv = k
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv_pv = A[r][c].inv()
        A[r] = [x * inv_pv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].iszero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        r += 1
        if r == m:
            break
    return r  # rank


t0 = time.time()
rk_rows = rank_over_L(rows, 81)
z1 = 81 - rk_rows
print(f"rank(Fox rows) = {rk_rows}; dim Z1 = {z1}  ({time.time()-t0:.1f}s)")

# coboundary map: 27 columns (basis vectors), 81 rows (3 gens x 27)
cob = []
for j in range(27):
    v = [ONE if t == j else ZERO for t in range(27)]
    col_entry = []
    for g in GENS:
        gv = [sum((S1[g][i][k] * v[k] for k in range(27) if not v[k].iszero()), ZERO)
              for i in range(27)]
        col_entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(col_entry)
# cob currently: 27 "columns" each an 81-vector; transpose to rows x cols=27
cob_rows = [[cob[j][i] for j in range(27)] for i in range(81)]
t0 = time.time()
rk_cob = rank_over_L(cob_rows, 27)
print(f"rank(coboundary) = {rk_cob}  ({time.time()-t0:.1f}s)")

h0 = 27 - rk_cob
h1 = z1 - rk_cob
print(f"\nINDEPENDENT SOLO RESULT (own Lelt class + own elimination): "
      f"h0(M;27) = {h0}, h1(M;27) = {h1}")
print(f"CLAIMED (cc, FINDINGS.md stage 3a table): h0 = 1, h1 = 3")
print(f"MATCH: {h0 == 1 and h1 == 3}")

import json as _json
with open("<seat-workdir>/seat-work/finisher_queue/f4_receipt/stage3_solo_exact_results.json", "w") as f:
    _json.dump({"rank_fox_rows": rk_rows, "z1": z1, "rank_coboundary": rk_cob,
                "h0": h0, "h1": h1, "match_claimed": (h0 == 1 and h1 == 3)}, f, indent=2)
print("Wrote stage3_solo_exact_results.json")
