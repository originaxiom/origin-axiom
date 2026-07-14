"""B598-P1 — THE CUSP TABLE: the six H1 representatives restricted to the
peripheral subgroup (see CAMPAIGN.md).

Per block m in {1,4,5,7,8,11}: solve the Fox cocycle condition
    (dr/da) xi_a + (dr/db) xi_b = 0   in V_m  (exact, over the B575 model),
mod coboundaries (H0 = 0 gate; dim H1 = 1 gate = B575-G4), then evaluate
  xi(meridian = a)  and  xi(lambda = [b,a] = the fiber boundary, B67 convention)
exactly. Also the meridian's nilpotent Jordan gate (regular unipotent: one
block of size 2m+1). The table is the classical domain data for P2.

Run: OA_SLOW=1 python3 p1_cusp_table.py (~10 min: the B575 exact build).
Nothing to CLAIMS.md.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
L51 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")

print("loading the B575 exact machinery (~6 min)...")
spec = importlib.util.spec_from_file_location("l51mod", L51)
m5 = importlib.util.module_from_spec(spec)
_argv = sys.argv
sys.argv = [L51]
try:
    spec.loader.exec_module(m5)
finally:
    sys.argv = _argv
print("machinery loaded")

K, K0, K1 = m5.K, m5.K0, m5.K1
REL = m5.REL                                     # "abABaBAbaB"
rref, nullspace = m5.rref, m5.nullspace


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def mat_mul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    out = [[K0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            x = X[i][k]
            if x.is_zero():
                continue
            Yk = Y[k]
            oi = out[i]
            for j in range(p):
                y = Yk[j]
                if not y.is_zero():
                    oi[j] = oi[j] + x * y
    return out


def fox_pair(acts, d):
    """The Fox matrices D_a = dr/da, D_b = dr/db (block rep, exact)."""
    I = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    Da = [[K0] * d for _ in range(d)]
    Db = [[K0] * d for _ in range(d)]
    P = I
    for ch in REL:
        if ch == 'a':
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] + P[i][j]
        elif ch == 'A':
            PA = mat_mul(P, acts['A'])
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] - PA[i][j]
        elif ch == 'b':
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] + P[i][j]
        elif ch == 'B':
            PB = mat_mul(P, acts['B'])
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] - PB[i][j]
        P = mat_mul(P, acts[ch])
    return Da, Db


def cocycle_eval(acts, xa, xb, word):
    """xi(word) from xi(a)=xa, xi(b)=xb via xi(uv) = xi(u) + u.xi(v)."""
    d = len(xa)
    val = [K0] * d
    P = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    for ch in word:
        if ch == 'a':
            inc = xa
        elif ch == 'b':
            inc = xb
        elif ch == 'A':
            inc = [K0 - v for v in mat_vec(acts['A'], xa)]
        else:
            inc = [K0 - v for v in mat_vec(acts['B'], xb)]
        val = [val[i] + v for i, v in enumerate(mat_vec(P, inc))]
        P = mat_mul(P, acts[ch])
    return val


def matrix_rank(rows):
    if not rows:
        return 0
    _, piv = rref([list(r) for r in rows])
    return len(piv)


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}w)"      # w = sqrt(-3)


print("\nTHE CUSP TABLE (exact over Q(sqrt-3); w = sqrt(-3)); lambda = [b,a] = 'baBA':")
for mexp in sorted(m5.BLOCK_DATA.keys()):
    D = m5.BLOCK_DATA[mexp]
    d, acts = D['d'], D['acts']
    Da, Db = fox_pair(acts, d)
    # cocycles: [Da | Db] (xa; xb) = 0
    big = [[Da[i][j] for j in range(d)] + [Db[i][j] for j in range(d)] for i in range(d)]
    sols = nullspace(big)
    # coboundaries: v -> ((1 - a)v, (1 - b)v)
    cobs = []
    for j in range(d):
        e = [K1 if i == j else K0 for i in range(d)]
        ca = [e[i] - v for i, v in enumerate(mat_vec(acts['a'], e))]
        cb = [e[i] - v for i, v in enumerate(mat_vec(acts['b'], e))]
        cobs.append(ca + cb)
    # H0 gate: joint fixed vectors of a and b = kernel of the coboundary map
    rank_cob = len(cobs) - len(nullspace([list(r) for r in zip(*cobs)])) if cobs else 0
    # dim H1
    dimH1 = len(sols) - rank_cob
    # pick a representative NOT in the coboundary span
    span = [list(c) for c in cobs]
    rep = None
    for s in sols:
        test = span + [list(s)]
        # rank test via rref on the transpose-free matrix
        r_before = matrix_rank(span)
        r_after = matrix_rank(test)
        if r_after > r_before:
            rep = s
            break
    assert rep is not None, f"no non-coboundary cocycle at m={mexp}"
    xa, xb = list(rep[:d]), list(rep[d:])
    # normalize: first nonzero coordinate of xi(a) = 1
    piv = next((i for i, v in enumerate(xa) if not v.is_zero()), None)
    if piv is None:
        piv = next(i for i, v in enumerate(xb) if not v.is_zero())
        scale = xb[piv].inv()
    else:
        scale = xa[piv].inv()
    xa = [scale * v for v in xa]
    xb = [scale * v for v in xb]
    xi_mu = xa
    xi_lam = cocycle_eval(acts, xa, xb, "baBA")
    # the meridian nilpotent gate: (rho(a) - 1)^(2m) != 0, ^(2m+1) = 0 handled by
    # regular-unipotency (banked adjoint Jordan type); here: rank(rho(a)-1) = d-1
    Am1 = [[acts['a'][i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
    rk = matrix_rank(Am1)
    print(f"\n  block m={mexp} (dim {d}): dim H1 = {dimH1} (gate 1: {dimH1 == 1}); "
          f"rank(rho(a)-1) = {rk} = d-1: {rk == d - 1}")
    print(f"    xi(mu = a)      = [{', '.join(fmt(v) for v in xi_mu)}]")
    print(f"    xi(lambda=[b,a])= [{', '.join(fmt(v) for v in xi_lam)}]")

print("\nDONE — the cusp table banked (the classical domain data for P2)")
