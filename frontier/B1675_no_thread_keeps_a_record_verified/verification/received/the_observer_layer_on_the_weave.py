"""W34: the observer layer on the weave (the rule, W34_RULE.md, was committed before this file existed).

The record's four observer-layer probes (Gate 5-Q) were computed on m004 at its geometric representation. This script
takes their structural content to every thread and to the weave's common point.

  Q1  B761's private states on every thread. Per block Sym^{2k} (k = 1, 2, 3) at the thread's geometric representation:
      dim H^1, the rank of the restriction to the cusp torus, and their difference. GENESIS's 758 states to length 12
      (SnapPy 3.3.2, b++w and b+-w, 60 digits).
  Q2  the private states at the common point (a -> i, b -> j), exact over the Gaussian rationals: H^1 of the fibre's
      free group, the restriction to the puncture [a, b], the private part, and what the moves keep, jointly and
      thread by thread.
  Q3  the self-name among the threads: the volume and the cusp shape up to GL(2, Z) and the mirror, compared at 30
      digits, against the reversal pairs (a word and its reverse are one manifold).
  Q4  the self-sign on the weave: assembled from the record, no computation.
  Q5  the register: the four founding rules as automorphisms, their outer classes, their lifts at the common point and
      their action on H^1; the two hands.

Run: python3 the_observer_layer_on_the_weave.py  ->  the_observer_layer_on_the_weave.json beside it.
     python3 the_observer_layer_on_the_weave.py --selftest checks the machinery only (no cell).
"""
import json
import sys
import time
import traceback
import warnings
from collections import Counter
from pathlib import Path

import mpmath as mp
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402  (the moves as automorphisms of F_2, composition, inner automorphisms)
import the_weaves_laws as TL  # noqa: E402  (GENESIS's states to length 12)

warnings.filterwarnings("ignore")
OUT = HERE / "the_observer_layer_on_the_weave.json"
KS = (1, 2, 3)
mp.mp.dps = 60
TOL_ZERO, TOL_NONZERO = mp.mpf(10) ** -40, mp.mpf(10) ** -25
NAME_TOL = mp.mpf(10) ** -30

# ================================================================================================ exact: Q(i) matrices
Z0, Z1, ZI = QQ_I(0, 0), QQ_I(1, 0), QQ_I(0, 1)


def q(c):
    return QQ_I(int(c), 0)


def mmul(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), Z0) for j in range(len(B[0]))] for i in range(len(A))]


def madd(A, B, s=Z1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(A, c):
    return [[c * x for x in row] for row in A]


def eye(d):
    return [[Z1 if i == j else Z0 for j in range(d)] for i in range(d)]


def zeros(r, c):
    return [[Z0] * c for _ in range(r)]


def vstack(*Ms):
    out = []
    for M in Ms:
        out += [list(r) for r in M]
    return out


def hstack(*Ms):
    return [sum((list(M[i]) for M in Ms), []) for i in range(len(Ms[0]))]


def rank(A):
    if not A or not A[0]:
        return 0
    return DomainMatrix(A, (len(A), len(A[0])), QQ_I).rank()


def left_null(B):
    """rows n with n B = 0"""
    N = DomainMatrix(B, (len(B), len(B[0])), QQ_I).transpose().nullspace()
    return N.to_list() if N.shape[0] else []


def key(M):
    return tuple(str(x) for row in M for x in row)


def det2(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def adj2(g):
    return [[g[1][1], -g[0][1]], [-g[1][0], g[0][0]]]


def sym(g, n):
    """Sym^n(g) on x^(n-j) y^j with (x, y) -> (x, y) g, a homomorphism"""
    a, b, c, d = g[0][0], g[0][1], g[1][0], g[1][1]
    cols = []
    for j in range(n + 1):
        p = [Z1]
        for _ in range(n - j):
            p = [(p[i] if i < len(p) else Z0) * a + (p[i - 1] if i >= 1 else Z0) * c for i in range(len(p) + 1)]
        for _ in range(j):
            p = [(p[i] if i < len(p) else Z0) * b + (p[i - 1] if i >= 1 else Z0) * d for i in range(len(p) + 1)]
        cols.append(p)
    return [[cols[j][i] for j in range(n + 1)] for i in range(n + 1)]


def S_even(g, k):
    """Sym^{2k}(g) / det(g)^k: the even block's image of the projective class of g"""
    dt = det2(g)
    return mscale(sym(g, 2 * k), Z1 / dt ** k)


# ---- the common point: a -> i, b -> j (the_spin_room's QM) ----
E2 = eye(2)
QI = [[ZI, Z0], [Z0, -ZI]]
QJ = [[Z0, Z1], [-Z1, Z0]]
QK = mmul(QI, QJ)
RHO = {1: QI, 2: QJ, -1: mscale(QI, -Z1), -2: mscale(QJ, -Z1)}
UNITS = {"1": E2, "-1": mscale(E2, -Z1), "i": QI, "-i": mscale(QI, -Z1), "j": QJ, "-j": mscale(QJ, -Z1),
         "k": QK, "-k": mscale(QK, -Z1)}
UNIT_OF = {key(M): u for u, M in UNITS.items()}
PUNCTURE = [1, 2, -1, -2]


def rho_word(w):
    M = E2
    for x in w:
        M = mmul(M, RHO[x])
    return M


SYMQ = {}


def sym_unit(u, n):
    if (u, n) not in SYMQ:
        SYMQ[(u, n)] = sym(UNITS[u], n)
    return SYMQ[(u, n)]


FOX_COUNTS = {}


def fox_counts(w):
    """the Fox derivatives of w as integer combinations of the units of Q8 (the common point's values)"""
    t = tuple(w)
    if t not in FOX_COUNTS:
        cnt = {1: Counter(), 2: Counter()}
        pre = "1"
        for x in w:
            g = abs(x)
            if x > 0:
                cnt[g][pre] += 1
                pre = UNIT_OF[key(mmul(UNITS[pre], RHO[x]))]
            else:
                pre = UNIT_OF[key(mmul(UNITS[pre], RHO[x]))]
                cnt[g][pre] -= 1
        FOX_COUNTS[t] = cnt
    return FOX_COUNTS[t]


def fox(w, n):
    """the Fox derivatives of the word w (letters +-1, +-2) evaluated in Sym^n rho_Q: {1: d x d, 2: d x d}"""
    cnt = fox_counts(w)
    d = n + 1
    out = {}
    for g in (1, 2):
        M = zeros(d, d)
        for u, c in cnt[g].items():
            if c:
                M = madd(M, sym_unit(u, n), q(c))
        out[g] = M
    return out


def lift(phi):
    """g, unique up to a scalar, with g rho(x) g^-1 = rho(phi(x)) for x = a, b"""
    rows = []
    for x in (1, 2):
        A, B = RHO[x], rho_word(phi[x])
        for r in range(2):
            for s in range(2):
                row = [Z0] * 4
                for t in range(2):
                    row[2 * r + t] += A[t][s]          # (g A)_rs
                    row[2 * t + s] -= B[r][t]          # (B g)_rs
                rows.append(row)
    N = DomainMatrix(rows, (8, 4), QQ_I).nullspace()
    assert N.shape[0] == 1, "the intertwiner is not unique"
    v = N.to_list()[0]
    g = [[v[0], v[1]], [v[2], v[3]]]
    for x in (1, 2):
        assert mmul(g, RHO[x]) == mmul(rho_word(phi[x]), g)
    assert det2(g) != Z0
    return g


class Block:
    """H^1(F_2; Sym^{2k} rho_Q): cocycles z = (z_a, z_b) in V^2, coboundaries, the restriction to the puncture"""

    def __init__(self, k):
        self.k, self.n, self.d = k, 2 * k, 2 * k + 1
        d = self.d
        Sa, Sb = S_even(QI, k), S_even(QJ, k)
        self.B = vstack(madd(Sa, eye(d), -Z1), madd(Sb, eye(d), -Z1))           # 2d x d, columns span B^1
        self.rB = rank(self.B)
        self.NB = left_null(self.B)                                             # rows killing B^1
        F = fox(PUNCTURE, self.n)
        self.R = hstack(F[1], F[2])                                             # z -> z(c)
        assert rank(mmul(self.R, self.B)) == 0, "the puncture does not kill coboundaries"
        self.h1 = 2 * d - self.rB
        self.rank_res = rank(self.R)
        self.private = self.h1 - self.rank_res

    def action(self, phi, g=None):
        """(phi* z)(x) = S(g)^-1 z(phi(x)), as a 2d x 2d matrix on (z_a, z_b)"""
        g = lift(phi) if g is None else g
        Sinv = S_even(adj2(g), self.k)
        Fa, Fb = fox(phi[1], self.n), fox(phi[2], self.n)
        A = vstack(hstack(mmul(Sinv, Fa[1]), mmul(Sinv, Fa[2])), hstack(mmul(Sinv, Fb[1]), mmul(Sinv, Fb[2])))
        if self.NB:
            assert rank(mmul(self.NB, mmul(A, self.B))) == 0, "the action does not keep the coboundaries"
        return A

    def kept(self, actions):
        """(dim of H^1 kept by every action, dim of the private part kept by every action)"""
        d2 = 2 * self.d
        rows = []
        for A in actions:
            if self.NB:
                rows += mmul(self.NB, madd(A, eye(d2), -Z1))
        h1 = d2 - rank(rows) - self.rB if rows else self.h1
        priv = d2 - rank(rows + [list(r) for r in self.R]) - self.rB
        return h1, priv


def abel(phi):
    """the matrix of phi on the records (columns: the images of a and b)"""
    col = {x: (sum(1 if y == 1 else -1 if y == -1 else 0 for y in phi[x]),
               sum(1 if y == 2 else -1 if y == -2 else 0 for y in phi[x])) for x in (1, 2)}
    return ((col[1][0], col[2][0]), (col[1][1], col[2][1]))


PAR = [(1, 0), (0, 1), (1, 1)]


def parity_perm(M):
    return [PAR.index(((M[0][0] * p[0] + M[0][1] * p[1]) % 2, (M[1][0] * p[0] + M[1][1] * p[1]) % 2)) for p in PAR]


def axis_perm(g):
    """the permutation the lift induces on the axes i, j, k (conjugation, up to sign)"""
    ginv = mscale(adj2(g), Z1 / det2(g))
    out = []
    for u in ("i", "j", "k"):
        v = UNIT_OF[key(mmul(mmul(g, UNITS[u]), ginv))].lstrip("-")
        out.append("ijk".index(v))
    return out


def proportional(A, B):
    return rank([[x for row in A for x in row], [x for row in B for x in row]]) == 1


# ================================================================================================ numerical: SnapPy
def to_mp(x):
    return mp.mpc(str(x.real()).replace(" ", ""), str(x.imag()).replace(" ", ""))


def sym_mp(g, n):
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    out = mp.matrix(n + 1, n + 1)
    for j in range(n + 1):
        p = [mp.mpc(1)]
        for _ in range(n - j):
            p = [(p[i] if i < len(p) else 0) * a + (p[i - 1] if i >= 1 else 0) * c for i in range(len(p) + 1)]
        for _ in range(j):
            p = [(p[i] if i < len(p) else 0) * b + (p[i - 1] if i >= 1 else 0) * d for i in range(len(p) + 1)]
        for i in range(n + 1):
            out[i, j] = p[i]
    return out


def fox_mp(word, gens, rho, d):
    blocks = {g: mp.zeros(d, d) for g in gens}
    pre = mp.eye(d)
    for ch in word:
        g = ch.lower()
        if ch == g:
            blocks[g] += pre
            pre = pre * rho[g]
        else:
            pre = pre * rho[g.upper()]
            blocks[g] -= pre
    return blocks, pre


def rank_mp(M):
    """(rank or None if undecided, smallest non-zero ratio, largest zero ratio)"""
    if M.rows == 0 or M.cols == 0:
        return 0, None, None
    s = sorted([abs(x) for x in mp.svd_c(M, compute_uv=False)], reverse=True)
    top = s[0] if s[0] > 0 else mp.mpf(1)
    nz = [x / top for x in s if x / top > TOL_NONZERO]
    z = [x / top for x in s if x / top < TOL_ZERO]
    r = len(nz) if len(nz) + len(z) == len(s) else None
    return r, (min(nz) if nz else None), (max(z) if z else None)


def kernel_mp(M, dim):
    """an orthonormal basis of the null space: the full V (mpmath's thin V drops the null directions when the matrix
    is wide, and an out-of-range row of an mpmath matrix reads as zeros), each vector checked to be null"""
    U, S, V = mp.svd_c(M, full_matrices=True)
    assert V.rows == M.cols
    s = [abs(S[i]) for i in range(len(S))]
    order = sorted(range(M.cols), key=lambda i: s[i] if i < len(s) else mp.mpf(0))
    out = [V[i, :].H for i in order[:dim]]
    scale = max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))
    for v in out:
        assert abs(mp.norm(v) - 1) < mp.mpf(10) ** -40
        assert mp.norm(M * v) < TOL_ZERO * scale * M.cols
    return out


def thread_block(G, k):
    n, d = 2 * k, 2 * k + 1
    gens = G.generators()
    rho = {}
    for g in gens:
        A = G.SL2C(g)
        m = mp.matrix([[to_mp(A[0, 0]), to_mp(A[0, 1])], [to_mp(A[1, 0]), to_mp(A[1, 1])]])
        rho[g] = sym_mp(m, n)
        rho[g.upper()] = mp.inverse(rho[g])
    rels = G.relators()
    F = mp.matrix(len(rels) * d, len(gens) * d)
    for r_i, r in enumerate(rels):
        bl, _ = fox_mp(r, gens, rho, d)
        for g_i, g in enumerate(gens):
            for i in range(d):
                for j in range(d):
                    F[r_i * d + i, g_i * d + j] = bl[g][i, j]
    Bm = mp.matrix(len(gens) * d, d)
    for g_i, g in enumerate(gens):
        D = rho[g] - mp.eye(d)
        for i in range(d):
            for j in range(d):
                Bm[g_i * d + i, j] = D[i, j]
    mer, lon = G.peripheral_curves()[0]
    Rm, BT = mp.matrix(2 * d, len(gens) * d), mp.matrix(2 * d, d)
    for p_i, w in enumerate((mer, lon)):
        bl, P = fox_mp(w, gens, rho, d)
        for g_i, g in enumerate(gens):
            for i in range(d):
                for j in range(d):
                    Rm[p_i * d + i, g_i * d + j] = bl[g][i, j]
        D = P - mp.eye(d)
        for i in range(d):
            for j in range(d):
                BT[p_i * d + i, j] = D[i, j]
    ranks, nzs, zs = [], [], []
    rF, a, b = rank_mp(F)
    ranks.append(rF), nzs.append(a), zs.append(b)
    rB, a, b = rank_mp(Bm)
    ranks.append(rB), nzs.append(a), zs.append(b)
    if rF is None or rB is None:
        return {"undecided": True, "nz": nzs, "z": zs}
    dimZ = len(gens) * d - rF
    Zb = kernel_mp(F, dimZ)
    C = mp.matrix(2 * d, dimZ + d)
    for c, zv in enumerate(Zb):
        v = Rm * zv
        for i in range(2 * d):
            C[i, c] = v[i]
    for j in range(d):
        for i in range(2 * d):
            C[i, dimZ + j] = BT[i, j]
    rC, a, b = rank_mp(C)
    nzs.append(a), zs.append(b)
    rT, a, b = rank_mp(BT)
    nzs.append(a), zs.append(b)
    if rC is None or rT is None:
        return {"undecided": True, "nz": nzs, "z": zs}
    h1, res = dimZ - rB, rC - rT
    return {"undecided": False, "H1": h1, "res": res, "private": h1 - res, "nz": nzs, "z": zs}


def name_of(M):
    vol = mp.mpf(str(M.volume()).replace(" ", ""))
    tau = M.cusp_info()[0]["shape"]
    tau = to_mp(tau)
    if tau.imag < 0:
        tau = mp.conj(tau)                    # the mirror
    for _ in range(10000):
        tau = tau - mp.nint(tau.real)
        if abs(tau) < 1 - mp.mpf(10) ** -45:
            tau = -1 / tau
        else:
            break
    return (vol, abs(tau.real), tau.imag)


def canon(w):
    n = len(w)
    sw = w.translate(str.maketrans("LR", "RL"))
    return min([w[i:] + w[:i] for i in range(n)] + [sw[i:] + sw[:i] for i in range(n)])


def short(x, digits=12):
    return None if x is None else mp.nstr(x, digits)


# ================================================================================================ the cells
def q1_q3(states):
    import snappy
    rows, names, errors = [], {}, []
    t0 = time.time()
    for w, sign in states:
        name = ("b++" if sign > 0 else "b+-") + w
        row = {"word": w, "sign": "+" if sign > 0 else "-"}
        try:
            M = snappy.ManifoldHP(name)
            row["solution"] = M.solution_type()
            G = M.fundamental_group()
            blocks = [thread_block(G, k) for k in KS]
            row["blocks"] = [{"H1": b.get("H1"), "res": b.get("res"), "private": b.get("private"),
                              "undecided": b["undecided"]} for b in blocks]
            nz = [x for b in blocks for x in b["nz"] if x is not None]
            zz = [x for b in blocks for x in b["z"] if x is not None]
            row["smallest non-zero ratio"] = short(min(nz)) if nz else None
            row["largest zero ratio"] = short(max(zz)) if zz else None
            names[(w, sign)] = name_of(M)
            row["volume"] = mp.nstr(names[(w, sign)][0], 25)
            row["cusp shape (|Re|, Im), reduced"] = [mp.nstr(names[(w, sign)][1], 20), mp.nstr(names[(w, sign)][2], 20)]
        except Exception as e:  # noqa: BLE001
            row["error"] = "%s: %s" % (type(e).__name__, e)
            errors.append(name)
        rows.append(row)
    seconds = time.time() - t0

    ok_rows = [r for r in rows if "error" not in r]
    decided = [r for r in ok_rows if not any(b["undecided"] for b in r["blocks"])]
    fiber = Counter(tuple(sum(b["private"] for b in r["blocks"][:n - 1]) for n in (2, 3, 4)) for r in decided)
    per_block = Counter(tuple((b["H1"], b["res"], b["private"]) for b in r["blocks"]) for r in decided)
    m004 = next(r for r in rows if r["word"] == "LR" and r["sign"] == "+")
    m004_blocks = [(b["H1"], b["res"], b["private"]) for b in m004.get("blocks", [])]
    q1 = {
        "the states": len(rows),
        "errors": errors,
        "undecided (a rank between 1e-40 and 1e-25 relative)": [(r["word"], r["sign"]) for r in ok_rows
                                                                  if any(b["undecided"] for b in r["blocks"])],
        "solution types": dict(Counter(r.get("solution") for r in ok_rows)),
        "per block (H1, rank, private) for k = 1, 2, 3 -> states": {str(k): v for k, v in per_block.items()},
        "fiber_dim(n) for n = 2, 3, 4 -> states": {str(k): v for k, v in fiber.items()},
        "the control m004 (b++LR): B761's (1, 1, 0) in each block": m004_blocks == [(1, 1, 0)] * 3,
        "smallest non-zero singular ratio over the census": min((mp.mpf(r["smallest non-zero ratio"]) for r in decided
                                                                  if r["smallest non-zero ratio"]), default=None),
        "largest zero singular ratio over the census": max((mp.mpf(r["largest zero ratio"]) for r in decided
                                                             if r["largest zero ratio"]), default=None),
        "seconds": round(seconds, 1),
    }
    q1["smallest non-zero singular ratio over the census"] = short(q1["smallest non-zero singular ratio over the census"])
    q1["largest zero singular ratio over the census"] = short(q1["largest zero singular ratio over the census"])
    q1["prediction (every decided state (1, 1, 0) in every block, none undecided, no error)"] = (
        not errors and len(decided) == len(rows) and set(per_block) == {((1, 1, 0),) * 3})

    # ---- Q3: the names against the reversal pairs ----
    keys = [k for k in names]
    clusters = []
    for kk in keys:
        v = names[kk]
        for cl in clusters:
            u = names[cl[0]]
            if all(abs(v[i] - u[i]) < NAME_TOL * max(1, abs(u[i])) for i in range(3)):
                cl.append(kk)
                break
        else:
            clusters.append([kk])
    partner = {}
    for (w, sign) in keys:
        r = canon(w[::-1])
        partner[(w, sign)] = (r, sign)
    rev_pairs = sorted({tuple(sorted([k, partner[k]])) for k in keys if partner[k] != k})
    expected = []
    seen = set()
    for k in keys:
        if k in seen:
            continue
        grp = {k, partner[k]}
        seen |= grp
        expected.append(frozenset(grp))
    found = [frozenset(cl) for cl in clusters]
    unexpected = [sorted(cl) for cl in found if cl not in set(expected)]
    import snappy
    iso_checks = {}
    for cl in unexpected:
        for i in range(1, len(cl)):
            a, b = cl[0], cl[i]
            Ma = snappy.Manifold(("b++" if a[1] > 0 else "b+-") + a[0])
            Mb = snappy.Manifold(("b++" if b[1] > 0 else "b+-") + b[0])
            try:
                iso = bool(Ma.is_isometric_to(Mb))
            except Exception as e:  # noqa: BLE001
                iso = "error: %s" % e
            iso_checks["%s%s ~ %s%s" % ("+" if a[1] > 0 else "-", a[0], "+" if b[1] > 0 else "-", b[0])] = iso
    rev_iso = {}
    for a, b in rev_pairs:
        Ma = snappy.Manifold(("b++" if a[1] > 0 else "b+-") + a[0])
        Mb = snappy.Manifold(("b++" if b[1] > 0 else "b+-") + b[0])
        try:
            rev_iso["%s%s ~ %s%s" % ("+" if a[1] > 0 else "-", a[0], "+" if b[1] > 0 else "-", b[0])] = bool(
                Ma.is_isometric_to(Mb))
        except Exception as e:  # noqa: BLE001
            rev_iso["%s ~ %s" % (a, b)] = "error: %s" % e
    pm_separated = all(
        not any((w, 1) in cl and (w, -1) in cl for cl in found) for (w, s) in keys if s > 0)
    q3 = {
        "the states named": len(keys),
        "distinct names": len(clusters),
        "reversal pairs (a word and its reverse, same sign, different states)": len(rev_pairs),
        "the reversal pairs": ["%s%s ~ %s%s" % ("+" if a[1] > 0 else "-", a[0], "+" if b[1] > 0 else "-", b[0])
                               for a, b in rev_pairs],
        "SnapPy: each reversal pair is one manifold": rev_iso,
        "every reversal pair shares its name": all(any(set(p) <= cl for cl in found) for p in rev_pairs),
        "shared names that are not reversal pairs": [["%s%s" % ("+" if s > 0 else "-", w) for w, s in cl]
                                                     for cl in unexpected],
        "SnapPy on those": iso_checks,
        "every + state is separated from its - state": pm_separated,
        "the names m004 and m003": {"m004 (+LR)": [mp.nstr(x, 15) for x in names.get(("LR", 1), ())],
                                    "m003 (-LR)": [mp.nstr(x, 15) for x in names.get(("LR", -1), ())]},
    }
    q3["prediction (names coincide exactly for the reversal pairs)"] = (
        not unexpected and q3["every reversal pair shares its name"] and pm_separated)
    return q1, q3, rows


def q2(states):
    moves = {m: CP.AUT[m] for m in ("L", "R", "P", "-I")}
    out = {"the common point's invariants (Gate 5-Q, Q3)": {
        "tr a, tr b, tr ab": [str(sum((rho_word(w)[i][i] for i in range(2)), Z0)) for w in ([1], [2], [1, 2])],
        "tr [a, b]": str(sum((rho_word(PUNCTURE)[i][i] for i in range(2)), Z0)),
        "rho([a, b])": UNIT_OF[key(rho_word(PUNCTURE))]}}
    blocks, table = {}, {}
    chars = {"chi0": (1, 1), "chi1": (-1, 1), "chi2": (1, -1), "chi3": (-1, -1)}   # (chi(a), chi(b))
    unit_char = {"1": (0, 0), "-1": (0, 0), "i": (1, 0), "-i": (1, 0), "j": (0, 1), "-j": (0, 1), "k": (1, 1), "-k": (1, 1)}
    for k in KS:
        b = Block(k)
        blocks[k] = b
        mult = {}
        for c, (ca, cb) in chars.items():
            tot = Z0
            for u in UNITS:
                ea, eb = unit_char[u]
                tot += q((ca ** ea) * (cb ** eb)) * sum((sym_unit(u, 2 * k)[i][i] for i in range(2 * k + 1)), Z0)
            mult[c] = str(tot / q(8))
        single = {m: b.kept([b.action(moves[m])]) for m in moves}
        joint = {}
        for name, ms in (("L, R", ("L", "R")), ("L, R, -I", ("L", "R", "-I")), ("L, R, P", ("L", "R", "P")),
                         ("L, R, P, -I", ("L", "R", "P", "-I"))):
            joint[name] = b.kept([b.action(moves[m]) for m in ms])
        table[k] = {"dim V": b.d, "multiplicities (chi0, chi1, chi2, chi3)": mult, "dim H1": b.h1,
                    "rank of the restriction to the puncture": b.rank_res, "private": b.private,
                    "kept by one move (H1, private)": single, "kept by the joint action (H1, private)": joint}
    out["per block k (Sym^{2k})"] = {str(k): v for k, v in table.items()}
    out["fiber_dim(n) at the common point, n = 2, 3, 4"] = [sum(blocks[k].private for k in KS[:n - 1]) for n in (2, 3, 4)]
    pred = {1: (3, 3, 0), 2: (7, 3, 4), 3: (8, 6, 2)}
    out["the table as predicted (H1, rank, private) = (3,3,0), (7,3,4), (8,6,2)"] = all(
        (blocks[k].h1, blocks[k].rank_res, blocks[k].private) == pred[k] for k in KS)
    out["the joint action keeps nothing (every set containing L and R, H1 and private)"] = all(
        v == (0, 0) for k in KS for v in table[k]["kept by the joint action (H1, private)"].values())

    # ---- thread by thread ----
    rows, bad_private, odd_rows = [], [], []
    t0 = time.time()
    for w, sign in states:
        phi = CP.word_aut(w, sign)
        g = lift(phi)
        M = abel(phi)
        tr = M[0][0] + M[1][1]
        kept = [blocks[k].kept([blocks[k].action(phi, g)]) for k in KS]
        row = {"word": w, "sign": "+" if sign > 0 else "-", "trace": tr,
               "kept (H1, private) for k = 1, 2, 3": kept}
        rows.append(row)
        if any(p for _, p in kept):
            bad_private.append((w, sign))
        if tr % 2:
            odd_rows.append(tuple(h for h, _ in kept))
    dist = Counter(("odd trace" if r["trace"] % 2 else "even trace", tuple(h for h, _ in r["kept (H1, private) for k = 1, 2, 3"]))
                   for r in rows)
    out["thread by thread"] = {
        "the states": len(rows),
        "states keeping a private state (predicted none)": bad_private,
        "kept H1 for k = 1, 2, 3 -> states": {"%s %s" % kk: v for kk, v in sorted(dist.items())},
        "every odd-trace state keeps (1, 1, 2) (predicted)": all(t == (1, 1, 2) for t in odd_rows),
        "the odd-trace states": len(odd_rows),
        "seconds": round(time.time() - t0, 1),
    }
    out["prediction (the table, the joint zeros, no thread keeps a private state)"] = (
        out["the table as predicted (H1, rank, private) = (3,3,0), (7,3,4), (8,6,2)"]
        and out["the joint action keeps nothing (every set containing L and R, H1 and private)"] and not bad_private)
    return out, rows


def q5(blocks):
    sigma = {1: [1, 2], 2: [1]}
    rev = {1: [2, 1], 2: [1]}
    csig = {1: [2], 2: [2, 1]}
    crev = {1: [2], 2: [1, 2]}
    rules = {"sigma": sigma, "C(sigma)": csig, "rev(sigma)": rev, "C(rev sigma)": crev}
    out = {"sigma = L o P (as automorphisms)": CP.compose(CP.AUT["L"], CP.AUT["P"]) == sigma,
           "rev(sigma) = i_{a^-1} o sigma": CP.compose(CP.inner([-1]), sigma) == rev,
           "C(rev sigma) = i_{b^-1} o C(sigma)": CP.compose(CP.inner([-2]), csig) == crev,
           "C(sigma) = P o sigma o P": CP.compose(CP.AUT["P"], CP.compose(sigma, CP.AUT["P"])) == csig}
    lifts = {n: lift(r) for n, r in rules.items()}
    out["the matrices"] = {n: abel(r) for n, r in rules.items()}
    out["the determinants (the records' hand)"] = {n: abel(r)[0][0] * abel(r)[1][1] - abel(r)[0][1] * abel(r)[1][0]
                                                   for n, r in rules.items()}
    out["the parity permutation (the cyclic order of the three)"] = {n: parity_perm(abel(r)) for n, r in rules.items()}
    out["the lift's permutation of the axes i, j, k (its class mod Q8: the McKay hand)"] = {
        n: axis_perm(g) for n, g in lifts.items()}
    out["the lift of rev(sigma) is rho(a)^-1 times the lift of sigma"] = proportional(lifts["rev(sigma)"],
                                                                                       mmul(RHO[-1], lifts["sigma"]))
    out["the lift of C(rev sigma) is rho(b)^-1 times the lift of C(sigma)"] = proportional(
        lifts["C(rev sigma)"], mmul(RHO[-2], lifts["C(sigma)"]))
    same = {}
    for k in KS:
        b = blocks[k]
        A1, A2 = b.action(sigma, lifts["sigma"]), b.action(rev, lifts["rev(sigma)"])
        C1, C2 = b.action(csig, lifts["C(sigma)"]), b.action(crev, lifts["C(rev sigma)"])
        diff = madd(A1, A2, -Z1)
        diffc = madd(C1, C2, -Z1)
        same[str(k)] = {"sigma and rev(sigma) act identically on H1": (rank(mmul(b.NB, diff)) == 0) if b.NB else True,
                        "C(sigma) and C(rev sigma) act identically on H1":
                            (rank(mmul(b.NB, diffc)) == 0) if b.NB else True,
                        "sigma and C(sigma) act identically on H1 (control, expected not)":
                            (rank(mmul(b.NB, madd(A1, C1, -Z1))) == 0) if b.NB else True}
    out["on H1(F_2; Sym^{2k} rho_Q)"] = same
    pp = out["the parity permutation (the cyclic order of the three)"]
    ap = out["the lift's permutation of the axes i, j, k (its class mod Q8: the McKay hand)"]
    dets = out["the determinants (the records' hand)"]
    out["the control: C flips the cyclic order (the McKay hand)"] = (pp["sigma"] != pp["C(sigma)"]
                                                                    and ap["sigma"] != ap["C(sigma)"])
    out["the register keeps both hands"] = (pp["sigma"] == pp["rev(sigma)"] and ap["sigma"] == ap["rev(sigma)"]
                                            and dets["sigma"] == dets["rev(sigma)"]
                                            and pp["C(sigma)"] == pp["C(rev sigma)"]
                                            and ap["C(sigma)"] == ap["C(rev sigma)"])
    out["prediction (the identities; the register in no hand; the same action on H1; the control fails as it should)"] = (
        out["sigma = L o P (as automorphisms)"] and out["rev(sigma) = i_{a^-1} o sigma"]
        and out["C(rev sigma) = i_{b^-1} o C(sigma)"]
        and out["the lift of rev(sigma) is rho(a)^-1 times the lift of sigma"]
        and out["the register keeps both hands"] and out["the control: C flips the cyclic order (the McKay hand)"]
        and all(v["sigma and rev(sigma) act identically on H1"] and v["C(sigma) and C(rev sigma) act identically on H1"]
                for v in same.values()))
    return out


Q4 = {
    "status": "assembled from the record; no computation",
    "W26 N1-N2": "the weave is closed under the mirror; every orientation-odd invariant a thread carries has its "
                 "conjugate on the mirror thread",
    "main's B1607, B1609, B1610": "the three's hand is the records' orientation, the sheet of the orientation double "
                                  "cover, which the rule itself exchanges; the McKay hand is the founding torsor's swap "
                                  "bit, a naming",
    "main's B1183": "on m004 the self-sign obstruction and the orientation are one class",
    "so": "the weave cannot sign itself, and on the weave the self-sign is exactly the hand: one bit, the choice at "
          "GENESIS SE2 and GM5c",
    "thread against weave": "m004 is amphichiral and cannot tell its two orientations apart; a chiral thread can, but "
                            "its mirror is a thread",
}


def selftest():
    """the machinery only: no cell is computed"""
    import random
    random.seed(34)
    for _ in range(5):
        g = [[QQ_I(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(2)] for _ in range(2)]
        h = [[QQ_I(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(2)] for _ in range(2)]
        for n in (2, 4, 6):
            assert sym(mmul(g, h), n) == mmul(sym(g, n), sym(h, n))
    # Fox derivatives against the cocycle rule, on arbitrary cocycles (F_2 is free: any z_a, z_b)
    for n in (2, 4, 6):
        d = n + 1
        za = [[QQ_I(random.randint(-5, 5), random.randint(-5, 5))] for _ in range(d)]
        zb = [[QQ_I(random.randint(-5, 5), random.randint(-5, 5))] for _ in range(d)]
        for w in ([1, 2, -1, -2], [2, 2, -1, 2, 1, 1, -2], [-1, -2, -2, 1]):
            z, pre = zeros(d, 1), E2
            for x in w:
                if x > 0:
                    z = madd(z, mmul(sym(pre, n), za if x == 1 else zb))
                    pre = mmul(pre, RHO[x])
                else:
                    pre = mmul(pre, RHO[x])
                    z = madd(z, mmul(sym(pre, n), za if x == -1 else zb), -Z1)
            F = fox(w, n)
            assert z == madd(mmul(F[1], za), mmul(F[2], zb))
    gL = lift(CP.AUT["L"])
    assert proportional(gL, madd(E2, QI)), "L's lift is 1 + i"
    import snappy
    G = snappy.ManifoldHP("b++LR").fundamental_group()
    assert [(b["H1"], b["res"], b["private"]) for b in (thread_block(G, k) for k in KS)] == [(1, 1, 0)] * 3
    nm = name_of(snappy.ManifoldHP("b++LR"))
    assert abs(nm[1]) < mp.mpf(10) ** -40 and abs(nm[2] - 2 * mp.sqrt(3)) < mp.mpf(10) ** -40, nm
    print("selftest: the machinery passes (sym, Fox, L's lift, the m004 control, m004's cusp shape 2 sqrt 3 i)")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    t0 = time.time()
    import snappy
    states = [(w, s) for w in TL.states(12) for s in (1, -1)]
    res = {"rule": "W34_RULE.md, committed first (1915fe92)",
           "versions": {"snappy": snappy.__version__, "mpmath dps": mp.mp.dps},
           "the states": {"count": len(states), "words": len(set(w for w, _ in states)),
                          "longest word": max(len(w) for w, _ in states)}}
    try:
        res["Q2 the private states at the common point (exact)"], q2rows = q2(states)
    except Exception:  # noqa: BLE001
        res["Q2 the private states at the common point (exact)"] = {"error": traceback.format_exc()}
        q2rows = []
    try:
        res["Q5 the register and the hands (exact)"] = q5({k: Block(k) for k in KS})
    except Exception:  # noqa: BLE001
        res["Q5 the register and the hands (exact)"] = {"error": traceback.format_exc()}
    try:
        q1, q3, q1rows = q1_q3(states)
        res["Q1 the private states on every thread (B761's quantity)"] = q1
        res["Q3 the self-name among the threads"] = q3
    except Exception:  # noqa: BLE001
        res["Q1 the private states on every thread (B761's quantity)"] = {"error": traceback.format_exc()}
        res["Q3 the self-name among the threads"] = {"error": "Q1's loop failed"}
        q1rows = []
    res["Q4 the self-sign on the weave (assembled)"] = Q4
    p = {}
    for cell, k in (("Q1", "Q1 the private states on every thread (B761's quantity)"),
                    ("Q2", "Q2 the private states at the common point (exact)"),
                    ("Q3", "Q3 the self-name among the threads"),
                    ("Q5", "Q5 the register and the hands (exact)")):
        v = res[k]
        p[cell] = next((vv for kk, vv in v.items() if kk.startswith("prediction")), None) if isinstance(v, dict) else None
    res["Q6 the verdict"] = {
        "each cell as predicted": p,
        "all as predicted": all(v is True for v in p.values()),
        "the reading if all hold": "the observer layer's negatives are properties of the class of threads, not of "
                                   "m004; at the common point the private states are kept by no thread and not by "
                                   "the weave; every thread is named among the threads up to its reversal; the weave "
                                   "cannot sign itself, and the self-sign is the hand; the register carries neither "
                                   "hand. No ingredient for the hand (GENESIS SE2, GM5c) or the count (GENESIS FK11).",
    }
    res["seconds"] = round(time.time() - t0, 1)
    res["per state, Q1 and Q3"] = q1rows
    res["per state, Q2"] = q2rows
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if not k.startswith("per state")}, indent=1, ensure_ascii=False,
                     default=str)[:20000])


if __name__ == "__main__":
    main()
