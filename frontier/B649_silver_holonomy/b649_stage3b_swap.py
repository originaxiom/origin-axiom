"""B649 stage 3b-i — the silver swap structure (prereg 3d0d45f7).

Reuses the stage-3a code path verbatim for the L-class, letters, weld,
and Fox rows (exec of the shared header section), then: Z1 basis
extraction, H1 representatives, sigma* with side exchange, gates G1-G4.
"""
import json
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- shared header: execute stage 3a's definitions up to the Fox part ---------
src = open(os.path.join(HERE, "b649_stage3a.py")).read()
head = src[:src.index("print(f\"  weld solution space")]
ns = {"__name__": "b649_shared", "__file__": os.path.join(HERE, "b649_stage3a.py")}
exec(compile(head, "b649_stage3a_head.py", "exec"), ns)

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
mconj27 = ns["mconj27"]
lift_sl2 = ns["lift_sl2"]
S1 = ns["S1"]
G2m = ns["G2"]
mm2, adj2 = ns["mm2"], ns["adj2"]
word2 = ns["word2"]

MU2 = ns["MU2"]
LAM2 = ns["LAM2"]
null = ns["null"]
u = None
for v in null:
    cand = [[L(list(map(Fr, v[8 * (2 * i + j): 8 * (2 * i + j) + 4])),
               list(map(Fr, v[8 * (2 * i + j) + 4: 8 * (2 * i + j) + 8])))
             for j in range(2)] for i in range(2)]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        break
assert u is not None
U27 = lift_sl2(u)
U27i = lift_sl2(adj2(u))
print("weld reconstructed", flush=True)

S2 = {nm: mmul(mmul(U27, mconj27(S1[nm])), U27i) for nm in "abcABC"}
LETS = {"a": S1["a"], "b": S1["b"], "c": S1["c"],
        "A": S1["A"], "B": S1["B"], "C": S1["C"],
        "d": S2["a"], "e": S2["b"], "f": S2["c"],
        "D": S2["A"], "E": S2["B"], "F": S2["C"]}
RELATORS = ["aBAbcc", "aaCbcB", "dEDeff", "ddFefE", "CCBeff", "caCAfdFD"]
GENS = "abcdef"
prim = {g: g for g in GENS}
for g in GENS:
    prim[g.upper()] = g

print("== G1: J^2 ==", flush=True)
JJ = mmul(U27, mconj27(U27))
c = JJ[0][0]
isscalar = all((JJ[i][j] - (c if i == j else L0)).is_zero()
               for i in range(27) for j in range(27))
c2 = c * c
print(f"  U27 conj(U27) scalar: {isscalar}; c^2 = 1: "
      f"{(c2 - L1).is_zero()}; c = {c.re}, {c.im}", flush=True)

# ---- Fox rows + Z1 basis -------------------------------------------------------
t0 = time.time()
rows27 = []
for w in RELATORS:
    Lb = {g: [[L0] * 27 for _ in range(27)] for g in GENS}
    P = meye(27)
    for ch in w:
        g = prim[ch]
        if ch.islower():
            term = P
        else:
            term = mscale(Lc(-1), mmul(P, LETS[ch]))
        Lb[g] = madd(Lb[g], term)
        P = mmul(P, LETS[ch])
    for i in range(27):
        rows27.append([Lb[g][i][j] for g in GENS for j in range(27)])
print(f"rows built ({time.time()-t0:.0f}s)", flush=True)


def L_nullspace_basis(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    r = 0
    pivs = []
    for cidx in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][cidx].is_zero()),
                   None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][cidx].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][cidx].is_zero():
                f = A[k][cidx]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(cidx)
        r += 1
        if r == m:
            break
    free = [cx for cx in range(ncols) if cx not in pivs]
    basis = []
    for fc in free:
        v = [L0] * ncols
        v[fc] = L1
        for rr, pc in enumerate(pivs):
            v[pc] = L0 - A[rr][fc]
        basis.append(v)
    return basis


t0 = time.time()
Z1 = L_nullspace_basis(rows27, 162)
print(f"dim Z1 = {len(Z1)} ({time.time()-t0:.0f}s)", flush=True)

cob = []
for j in range(27):
    v = [L1 if t == j else L0 for t in range(27)]
    entry = []
    for g in GENS:
        gv = [sum((LETS[g][i][k] * v[k] for k in range(27)
                   if not v[k].is_zero()), L0) for i in range(27)]
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(entry)


class Span:
    """incremental echelon store for membership + coords."""

    def __init__(self, ncols):
        self.rows = []          # (pivcol, vector-normalized, tag)
        self.n = ncols

    def reduce(self, v):
        v = v[:]
        coeffs = []
        for (pc, w, tag) in self.rows:
            f = v[pc]
            if not f.is_zero():
                v = [x - f * y for x, y in zip(v, w)]
                coeffs.append((tag, f))
        return v, coeffs

    def add(self, v, tag):
        v, _ = self.reduce(v)
        pc = next((i for i in range(self.n) if not v[i].is_zero()), None)
        if pc is None:
            return False
        inv = v[pc].inv()
        v = [x * inv for x in v]
        self.rows.append((pc, v, tag))
        return True


span = Span(162)
nc = 0
for k, cv in enumerate(cob):
    if span.add(cv, ("cob", k)):
        nc += 1
print(f"independent coboundaries: {nc}", flush=True)

reps = []
for z in Z1:
    if span.add(z, ("rep", len(reps))):
        reps.append(z)
    if len(reps) == 5:
        break
print(f"H1 representatives: {len(reps)}", flush=True)

# ---- sigma* ---------------------------------------------------------------------
def Jvec(v27):
    cv = [x.conj() for x in v27]
    return [sum((U27[i][k] * cv[k] for k in range(27)
                 if not cv[k].is_zero()), L0) for i in range(27)]


def sigma_star(z):
    # slots: a,b,c (0..80), d,e,f (81..161); sigma* exchanges with J
    out = [L0] * 162
    for gi, g in enumerate("abc"):
        src = z[81 + 27 * gi: 81 + 27 * (gi + 1)]
        img = Jvec(src)
        out[27 * gi: 27 * (gi + 1)] = img
    for gi in range(3):
        src = z[27 * gi: 27 * (gi + 1)]
        img = Jvec(src)
        out[81 + 27 * gi: 81 + 27 * (gi + 1)] = img
    return out


def is_cocycle(z):
    for row in rows27:
        s_ = L0
        for t in range(162):
            if not z[t].is_zero() and not row[t].is_zero():
                s_ = s_ + row[t] * z[t]
        if not s_.is_zero():
            return False
    return True


print("\n== G2: sigma* maps the representatives to cocycles ==", flush=True)
imgs = [sigma_star(r) for r in reps]
oks = [is_cocycle(v) for v in imgs]
print(f"  cocycle: {oks}", flush=True)

print("\n== G3: sigma*^2 = id mod B1 ==", flush=True)
ok3 = []
for r in reps:
    d = [a - b for a, b in zip(sigma_star(sigma_star(r)), r)]
    red, _ = Span(162), None
    # membership in coboundary span:
    sp = Span(162)
    for k, cv in enumerate(cob):
        sp.add(cv, ("cob", k))
    dd, _ = sp.reduce(d)
    ok3.append(all(x.is_zero() for x in dd))
print(f"  {ok3}", flush=True)

print("\n== G4: the sigma*-matrix (run 2: honest coordinate solve —", flush=True)
print("   run 1's echelon-coefficient shortcut was frame-mangled; its", flush=True)
print("   diagonal violated the G3-proven constraint |d|=1, the tell) ==", flush=True)
cobsp = Span(162)
for k, cv in enumerate(cob):
    cobsp.add(cv, ("cob", k))
red_reps = [cobsp.reduce(r)[0] for r in reps]
red_imgs = [cobsp.reduce(v)[0] for v in imgs]
# solve c_i . R = img_i in the quotient: build echelon of red_reps with tags
rsp = Span(162)
for idx, rr in enumerate(red_reps):
    ok = rsp.add(rr, ("rep", idx))
    assert ok
Mrows = []
for v in red_imgs:
    resid, coeffs = rsp.reduce(v)
    assert all(x.is_zero() for x in resid), "image not in rep-span mod cob"
    # rsp rows are normalized/reduced; recover TRUE coords by back-solve:
    # build the 5x5 change T: red_reps[i] reduces through rsp rows too.
    Mrows.append(coeffs)
# The coeffs are still in the rsp echelon frame. Convert: express each
# echelon row in terms of the true reps by solving T explicitly.
# T[i] = coords of red_reps[i] in echelon frame:
T = []
for rr in red_reps:
    resid, cf = rsp.reduce(rr)
    row = [L0] * 5
    for (tag, f) in cf:
        row[tag[1]] = row[tag[1]] + f
    T.append(row)
# true matrix C with img = C . reps satisfies: img_ech = C . T (both in
# echelon frame, rows = images): C = img_ech . T^{-1}
def solve5(Trows, target):
    # solve x . T = target  (x, target row-vectors of L, T 5x5)
    A = [[Trows[r][c] for r in range(5)] for c in range(5)]  # A = T^T
    b = target[:]
    # gaussian solve A x^T = b^T? We need x with sum_r x_r T[r][c] = target[c]
    # i.e. (T^T) x = target as column. A = T^T as built.
    n = 5
    Aug = [A[r][:] + [b[r]] for r in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if not Aug[r][c].is_zero())
        Aug[c], Aug[piv] = Aug[piv], Aug[c]
        pinv = Aug[c][c].inv()
        Aug[c] = [x * pinv for x in Aug[c]]
        for r in range(n):
            if r != c and not Aug[r][c].is_zero():
                f = Aug[r][c]
                Aug[r] = [x - f * y for x, y in zip(Aug[r], Aug[c])]
    return [Aug[r][n] for r in range(n)]

img_ech = []
for v in red_imgs:
    resid, cf = rsp.reduce(v)
    row = [L0] * 5
    for (tag, f) in cf:
        row[tag[1]] = row[tag[1]] + f
    img_ech.append(row)
C = [solve5(T, ie) for ie in img_ech]
def lstr(x):
    return f"({x.re}|{x.im})"
for i, row in enumerate(C):
    print("  C[" + str(i) + "] = " + "  ;  ".join(
        "0" if x.is_zero() else lstr(x) for x in row), flush=True)
# verify the antilinear involution constraint: C . conj(C) = I (5x5, exact)
CC = [[sum((C[i][k] * C[k][j].conj() for k in range(5)), L0)
       for j in range(5)] for i in range(5)]
okI = all((CC[i][j] - (L1 if i == j else L0)).is_zero()
          for i in range(5) for j in range(5))
print(f"  C . conj(C) = I exactly: {okI}", flush=True)
# s-content: does C live in Q(i) (all s-coefficients zero)?
sfree = all(all(x.re[k] == 0 and x.im[k] == 0 for k in (1, 2, 3))
            for row in C for x in row)
print(f"  C is s-free (lives in Q(i)): {sfree}", flush=True)
import json as _json
_json.dump([[[str(f) for f in (x.re + x.im)] for x in row] for row in C],
           open(os.path.join(HERE, "sigma_matrix_L.json"), "w"))
print("sigma_matrix_L.json written (honest coordinates)", flush=True)

print("\nB649 stage 3b-i DONE", flush=True)
