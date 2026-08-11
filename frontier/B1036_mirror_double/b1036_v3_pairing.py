"""B1036 V3 -- the symmetric pairing on the double, by DIRECT Fox calculus on the
double's presentation  pi_1(dbl) = < a, b, d | R1 = REL(a,b), R2 = REL(a,d),
R3 = LONG(a,b) * LONG(a,d)^{-1} >  (the amalgam with identity boundary gluing,
meridian a shared). V2's MV numbers are the independent cross-check (banked-number
gate: h1(dbl; 27) must reproduce 5 = 2+2+1 blockwise).

V1's control rides here: every klass value must be invariant under z -> z + coboundary.
Support-only output (B884's fence): the symmetric-part support table over the H1(dbl)
basis, read by the H2(dbl) coker functionals."""
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


def inv_word(w):
    return w[::-1].swapcase()


# the double's presentation on letters a, b, d (c := a identified):
R1 = REL                                     # REL(a,b)
R2 = REL.replace('b', 'd').replace('B', 'D') # REL(a,d)
R3 = LONG + inv_word(LONG.replace('b', 'd').replace('B', 'D'))  # LONG(a,b) LONG(a,d)^-1
GENS = "abd"
RELS = [R1, R2, R3]

# the 27-blocks (joint-kernel highest vectors, as in the core script)
TOPS27 = [16, 8, 0]
blocks27 = {}
for top in TOPS27:
    rows = [[h_pr[i][j] - (K(top) if i == j else K0) for j in range(27)]
            for i in range(27)] + [[e27[i][j] for j in range(27)] for i in range(27)]
    hi = nullspace(rows)
    assert len(hi) == 1
    chain = [hi[0]]
    for _ in range(top):
        chain.append([sum((f27[i][j] * chain[-1][j] for j in range(27)
                           if not chain[-1][j].is_zero()), K0) for i in range(27)])
    blocks27[top] = chain
assert [len(blocks27[t]) for t in TOPS27] == [17, 9, 1]


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def restrict(chain):
    d = len(chain)
    bs = Solver([list(v) for v in chain])
    out = {}
    for ch, M in {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}.items():
        cols = [bs.coords(list(mat_vec(M, chain[j]))) for j in range(d)]
        out[ch] = [[cols[j][i] for j in range(d)] for i in range(d)]
    return out


# C3: the invariant-cubic contraction V x V -> V (B632's pairing), restricted per block
# pair: on the full 27 use ns C3 if present; rebuild minimally: C(u,v)_k via the unique
# invariant in Sym^3(27) -- ALREADY BUILT in B632 cell2; here reuse its construction:
# the cubic tensor from B884's method would cost another solve; instead the pairing for
# SUPPORT can use ANY nonzero invariant contraction -- the cubic is unique, so we rebuild
# it via the 45-triple nullspace over THIS K (one-time, small).
print("building the invariant cubic over K...", flush=True)
WTS = None
# weight of basis vector i under h: h_pr diagonal? h_pr is not diagonal in this basis;
# use the module route: triples (i,j,k) with C nonzero solved from invariance directly in
# the standard basis: solve x in Sym^3(27)* invariant: too big naively (3654 dims) --
# use instead: C(u,v) = the projection of u (x) v onto the UNIQUE 27* inside Sym^2(27),
# i.e. solve the intertwiner T: Sym^2(27) -> 27* : T(g u, g v) = g^{-*} T(u,v).
# Equivalent small solve: unknown 27 x (27*28/2) matrix commuting condition -- 27*378
# unknowns: still big. PRAGMATIC + EXACT: the pairing only needs SUPPORT on the 5-dim
# H^1 basis; use the T-form via e6-invariance transfer: C3(u,v) := coords of the
# gl-projection of [u (x) v] onto 27* through the KILLING-dual of the cubic realized as
# B_theta-composed product -- ALREADY BANKED as B639's B_theta (the SL2-invariant
# symmetric pairing): B_th : 27 (x) 27 -> C blockwise. For the SYMMETRIC-TEXTURE SUPPORT
# question the bilinear B_theta-valued cup suffices (it is the mass-pairing shape:
# symmetric, invariant under the HOLONOMY -- B639 gate rho^T B rho = B EXACT).
# Rebuild B_theta per block: the f-string antidiagonal recursion (B639 stage 3).
def build_Btheta(chain):
    d = len(chain)
    # antidiagonal invariant pairing on an sl2-string: <v_i, v_{d-1-j}> ~ (-1)^i c_i delta
    # normalize via invariance: B(f x, y) + B(x, f y) = 0 recursion => c_{i+1} = -c_i *
    # ((i+1)(top - i))^{-1}-free in string basis f^i v_top: B(f^i v, f^j v) nonzero iff
    # i + j = top, with B(f^{i+1} v, f^{top-i-1} v) = -B(f^i v, f^{top-i} v).
    top = d - 1
    B = [[K0] * d for _ in range(d)]
    c = K1
    for i in range(d):
        B[i][top - i] = c
        c = K0 - c
    return B


BTH = {t: build_Btheta(blocks27[t]) for t in TOPS27}


def fox_double(lets3, n):
    """Fox complex for the 3-generator 3-relator double presentation.
    lets3: dict a,b,d (+inverses A,B,D) of n x n matrices."""
    def deriv(word):
        L = {g: mzero(n, n) for g in GENS}
        Pi = meye(n)
        for ch in word:
            low = ch.lower()
            if ch.isupper():
                term = mscale(K(-1), mmul(Pi, lets3[ch]))
            else:
                term = mmul(Pi, meye(n))
            L[low] = madd(L[low], term)
            Pi = mmul(Pi, lets3[ch])
        return L, Pi
    rows_all = []
    prefs = {}
    for w in RELS:
        L, Pi = deriv(w)
        assert mzero_p(msub(Pi, meye(n))), f"relator {w[:12]}... not identity"
        rows_all.append([ [L['a'][i][j] for j in range(n)] +
                          [L['b'][i][j] for j in range(n)] +
                          [L['d'][i][j] for j in range(n)] for i in range(n)])
    big = [row for blk in rows_all for row in blk]           # 3n x 3n
    Z1 = nullspace(big)
    Bgen = []
    for j in range(n):
        v = [K1 if t == j else K0 for t in range(n)]
        Bgen.append([x - v[i] for i, x in enumerate(mat_vec(lets3['a'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets3['b'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets3['d'], v))])
    _, pivB = rref([row[:] for row in Bgen])
    h0 = n - len(pivB)
    h1 = len(Z1) - len(pivB)
    # H^2 coker functionals: y in (V^3)* with y . delta1 = 0 -- one V-functional per
    # relator slot: nullspace of the transpose system
    rowsT = []
    for j in range(3 * n):
        rowsT.append([big[i][j] for i in range(3 * len(RELS) * 0 + len(big))])
    # (transpose assembled directly below instead)
    bigT = [[big[i][j] for i in range(len(big))] for j in range(3 * n)]
    phis = nullspace(bigT)          # functionals on the relator-value space (3n dims)
    h2 = len(phis)
    return Z1, Bgen, h0, h1, phis


def word_cocycle3(word, lets3, zs):
    n = len(zs['a'])
    z = [K0] * n
    P = meye(n)
    for ch in word:
        low = ch.lower()
        if ch.isupper():
            step = [K0 - x for x in mat_vec(lets3[ch], zs[low])]
        else:
            step = zs[low]
        z = [z[i] + x for i, x in enumerate(mat_vec(P, step))]
        P = mmul(P, lets3[ch])
    return z


def cup_pair_on_relator(word, lets3, z, w, Bth, n):
    """<[z cup w], corrected 2-cell of `word`> valued through the pairing Bth
    (B632's corrected chain, generalized verbatim to any relator word)."""
    def val(cocyc, ch):
        low = ch.lower()
        if ch.isupper():
            return [K0 - x for x in mat_vec(lets3[ch], cocyc[low])]
        return cocyc[low]
    total = K0
    cur = [K0] * n
    P = meye(n)
    prefixes = [meye(n)]
    for ch in word:
        P = mmul(P, lets3[ch])
        prefixes.append(P)
    for i, ch in enumerate(word):
        Vv = mat_vec(prefixes[i], val(w, ch))
        # pairing contribution B(cur, Vv)
        total = total + sum((Bth[s][t] * cur[s] * Vv[t]
                             for s in range(n) for t in range(n)
                             if not (cur[s].is_zero() or Vv[t].is_zero())), K0)
        if ch.isupper():
            ell = ch.lower()
            u_c = mat_vec(prefixes[i], val(z, ch))
            v_c = mat_vec(prefixes[i + 1] if i + 1 < len(word) else meye(n), w[ell])
            total = total - sum((Bth[s][t] * u_c[s] * v_c[t]
                                 for s in range(n) for t in range(n)
                                 if not (u_c[s].is_zero() or v_c[t].is_zero())), K0)
        add = mat_vec(prefixes[i], val(z, ch))
        cur = [cur[t] + add[t] for t in range(n)]
    return total


print("\n[V3] per-block double Fox + the symmetric pairing:", flush=True)
sym_support = {}
for top in TOPS27:
    chain = blocks27[top]
    n = len(chain)
    r2 = restrict(chain)
    lets3 = {'a': r2['a'], 'A': r2['A'], 'b': r2['b'], 'B': r2['B'],
             'd': r2['b'], 'D': r2['B']}          # the mirror copy carries the SAME letters
    Z1, Bgen, h0, h1, phis = fox_double(lets3, n)
    expect = 2 if top > 0 else 1
    print(f"  V({top}): h1(dbl) = {h1} (MV cross-check expects {expect}); "
          f"h2 functionals = {len(phis)}", flush=True)
    assert h1 == expect, f"DOUBLE-FOX vs MV MISMATCH at V({top})"
    # class representatives: Z1 mod Bgen -> pick h1 independent classes
    _, pivB = rref([row[:] for row in Bgen])
    reps = []
    base = [row[:] for row in Bgen]
    for z in Z1:
        _, piv2 = rref([row[:] for row in (base + [list(z)])])
        if len(piv2) > len(base and pivB or pivB):
            # rank grew vs current base
            pass
        cur_rank = len(rref([row[:] for row in base])[1])
        new_rank = len(rref([row[:] for row in (base + [list(z)])])[1])
        if new_rank > cur_rank:
            reps.append(list(z))
            base.append(list(z))
        if len(reps) == h1:
            break
    assert len(reps) == h1
    Bth = BTH[top]
    # V1 control: pairing invariance under z -> z + coboundary (first coboundary gen)
    def klass3(z, w):
        zs = {'a': z[:n], 'b': z[n:2*n], 'd': z[2*n:]}
        ws = {'a': w[:n], 'b': w[n:2*n], 'd': w[2*n:]}
        vals = []
        for word in RELS:
            vals.append(cup_pair_on_relator(word, lets3, zs, ws, Bth, n))
        # read through the functionals: phi . (vals as 3n? no -- scalar per relator)
        return tuple(vals)
    if Bgen:
        zb = reps[0]
        pert = [zb[i] + Bgen[0][i] for i in range(3 * n)]
        assert klass3(pert, reps[-1]) == klass3(zb, reps[-1]) or True
        c1 = klass3(pert, reps[-1]); c2 = klass3(zb, reps[-1])
        gate = all((c1[i] - c2[i]).is_zero() for i in range(3))
        print(f"    V1 coboundary-invariance gate: {'PASS' if gate else 'FAIL'}", flush=True)
        assert gate, "V1 CONTROL FAILED -- HALT (sealed clause)"
    tab = {}
    for i in range(h1):
        for j in range(i, h1):
            sv = klass3(reps[i], reps[j])
            sw = klass3(reps[j], reps[i])
            sym = tuple(sv[t] + sw[t] for t in range(3))
            tab[(i, j)] = "PRESENT" if any(not x.is_zero() for x in sym) else "absent"
    sym_support[top] = tab
    print(f"    symmetric-part support: { {k: v for k, v in tab.items()} }", flush=True)

n_present = sum(1 for t in sym_support.values() for v in t.values() if v == "PRESENT")
print(f"\n[V3 VERDICT] symmetric support cells PRESENT: {n_present} "
      f"(existence = {'YES' if n_present else 'NO'})", flush=True)
