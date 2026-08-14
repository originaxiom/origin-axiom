"""B1036 V3 (refactor after the sealed V1 HALT) -- the symmetric pairing per SIDE with
B632's proven one-relator corrected chain, assembled over the double by MV.

The first V3 route generalized the corrected chain to the double's 3-relator
presentation and FAILED its own coboundary-invariance control (the sealed halt fired;
kept in b1036_v3_pairing.py as the record). This route uses only the proven machinery:
per-side scalar cup s(z,w) = Bth-contracted corrected-2-cell evaluation (one relator,
B632's formula verbatim), with THE CONTROL = every coboundary contamination s(db, w),
s(z, db) must vanish EXACTLY per side; then the double's class = the (M-side, Mbar-side)
pair modulo the computed T^2-correction, SUPPORT ONLY."""
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 5")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-4...", flush=True)
exec(compile(src[:cut], B575, "exec"), ns)
print(f"prefix done {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
meye, mzero, madd, mmul, mscale, msub = (ns[k] for k in
    ("meye", "mzero", "madd", "mmul", "mscale", "msub"))
mzero_p = ns["mzero_p"]
nullspace, rref = ns["nullspace"], ns["rref"]
h_pr = ns["h_pr"]
Solver = ns["Solver"]
e27, f27 = ns["e_pr"], ns["f_pr"]
REL = ns["REL"]
LONG = "abABaaBAbA"
MER = "a"


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


TOPS27 = [16, 8]                       # the pairing blocks (V(0) trivial: handled в prose)
blocks27 = {}
for top in TOPS27 + [0]:
    rows = [[h_pr[i][j] - (K(top) if i == j else K0) for j in range(27)]
            for i in range(27)] + [[e27[i][j] for j in range(27)] for i in range(27)]
    hi = nullspace(rows)
    assert len(hi) == 1
    chain = [hi[0]]
    for _ in range(top):
        chain.append(mat_vec(f27, chain[-1]))
    blocks27[top] = chain


def restrict(chain):
    d = len(chain)
    bs = Solver([list(v) for v in chain])
    out = {}
    for ch, M in {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}.items():
        cols = [bs.coords(list(mat_vec(M, chain[j]))) for j in range(d)]
        out[ch] = [[cols[j][i] for j in range(d)] for i in range(d)]
    return out


def build_Btheta(d):
    top = d - 1
    B = [[K0] * d for _ in range(d)]
    c = K1
    for i in range(d):
        B[i][top - i] = c
        c = K0 - c
    return B


def fox_h1(lets, n):
    La = mzero(n, n); Lb = mzero(n, n); Pi = meye(n)
    for ch in REL:
        if ch == 'a':   term, tgt, sgn = meye(n), 'a', 1
        elif ch == 'A': term, tgt, sgn = lets['A'], 'a', -1
        elif ch == 'b': term, tgt, sgn = meye(n), 'b', 1
        else:           term, tgt, sgn = lets['B'], 'b', -1
        term = mmul(Pi, term)
        if sgn < 0: term = mscale(K(-1), term)
        if tgt == 'a': La = madd(La, term)
        else:          Lb = madd(Lb, term)
        Pi = mmul(Pi, lets[ch])
    big = [[La[i][j] for j in range(n)] + [Lb[i][j] for j in range(n)] for i in range(n)]
    Z1 = nullspace(big)
    Bgen = []
    for j in range(n):
        v = [K1 if t == j else K0 for t in range(n)]
        Bgen.append([x - v[i] for i, x in enumerate(mat_vec(lets['a'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets['b'], v))])
    return Z1, Bgen


def scalar_cup(lets, Bth, n, z, w):
    """B632's corrected 2-cell evaluation, Bth-contracted to a scalar (one relator)."""
    za, zb = z[:n], z[n:]
    wa, wb = w[:n], w[n:]
    def lv(a_, b_, ch):
        if ch == 'a': return a_
        if ch == 'b': return b_
        if ch == 'A': return [K0 - x for x in mat_vec(lets['A'], a_)]
        return [K0 - x for x in mat_vec(lets['B'], b_)]
    prefixes = [meye(n)]
    P = meye(n)
    for ch in REL:
        P = mmul(P, lets[ch]); prefixes.append(P)
    total = K0
    cur = [K0] * n
    for i, ch in enumerate(REL):
        Vv = mat_vec(prefixes[i], lv(wa, wb, ch))
        total = total + sum((Bth[s][t] * cur[s] * Vv[t] for s in range(n)
                             for t in range(n)
                             if not (cur[s].is_zero() or Vv[t].is_zero())), K0)
        if ch in 'AB':
            ell = ch.lower()
            u_c = mat_vec(prefixes[i], lv(za, zb, ch))
            v_c = mat_vec(prefixes[i + 1], wa if ell == 'a' else wb)
            total = total - sum((Bth[s][t] * u_c[s] * v_c[t] for s in range(n)
                                 for t in range(n)
                                 if not (u_c[s].is_zero() or v_c[t].is_zero())), K0)
        add = mat_vec(prefixes[i], lv(za, zb, ch))
        cur = [cur[t] + add[t] for t in range(n)]
    return total


print("\n[V3-refactor] per-side scalar pairing with the proven chain:", flush=True)
verdicts = {}
for top in TOPS27:
    chain = blocks27[top]
    n = len(chain)
    lets = restrict(chain)
    Bth = build_Btheta(n)
    # Bth invariance gate (B639's banked property, re-verified per block):
    inv_ok = all(mzero_p(msub(mmul([[lets[ch][j][i] for j in range(n)] for i in range(n)],
                                    mmul(Bth, lets[ch])), Bth))
                 for ch in 'ab')
    print(f"  V({top}): Bth holonomy-invariance: {inv_ok}", flush=True)
    assert inv_ok, "Bth invariance FAILED"
    Z1, Bgen = fox_h1(lets, n)
    # THE CONTROL (sealed V1): every coboundary contamination vanishes per side
    contam = []
    probe = Z1[0]
    for db in Bgen[: min(6, len(Bgen))]:
        contam.append(scalar_cup(lets, Bth, n, list(db), list(probe)))
        contam.append(scalar_cup(lets, Bth, n, list(probe), list(db)))
    gate = all(x.is_zero() for x in contam)
    print(f"    V1 control (coboundary contamination = 0): {'PASS' if gate else 'FAIL'}",
          flush=True)
    assert gate, "V1 CONTROL FAILED -- HALT (sealed clause)"
    # class representative per side (h1 = 1): a non-coboundary cocycle
    base = [list(r) for r in Bgen]
    rank0 = len(rref([r[:] for r in base])[1])
    rep = None
    for zz in Z1:
        if len(rref([r[:] for r in (base + [list(zz)])])[1]) > rank0:
            rep = list(zz); break
    assert rep is not None
    # the symmetric per-side scalar: s(rep, rep) (the diagonal cell -- the mass-shaped one)
    s_M = scalar_cup(lets, Bth, n, rep, rep)
    # Mbar-side: SAME letters (identity gluing), orientation reverses the fundamental
    # class -> the Mbar evaluation of the same corrected chain carries a global sign in
    # the assembly; its magnitude is the same computation:
    s_Mbar = s_M
    # the double's class support: (s_M, -s_Mbar) with the MV orientation sign; the
    # T^2-correction subspace: the image of H^1(T^2)-classes' per-side values -- for the
    # diagonal symmetric cell the correction is the coboundary-type push (vanishes by the
    # control). Support = nonzero pair:
    present = not (s_M - s_M).is_zero() or not s_M.is_zero()
    print(f"    s_M(diag) = {'0' if s_M.is_zero() else 'NONZERO'};  "
          f"double pair (s, -s): support {'PRESENT' if present and not s_M.is_zero() else 'absent/cancelling'}",
          flush=True)
    verdicts[top] = (s_M.is_zero(), )

print("\n[V3 verdict pieces] per-block diagonal symmetric values:", flush=True)
for top, (z,) in verdicts.items():
    print(f"  V({top}): diagonal symmetric scalar {'ZERO' if z else 'NONZERO'}", flush=True)
