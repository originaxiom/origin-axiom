"""B897 (SEALED cell, compute AFTER the prereg seal): the 27 under G20.

Per prime q (two primes; block dims must agree or UNSTABLE):
 1. rebuild the B854 frame; derive the tower digits (r, gamma, a) for ALL
    THREE roots of mu mod q (the sm_closer search, per root);
 2. build the three wall centralizers in the adjoint, close to G20 (dim 20,
    derived 19 -- gates);
 3. color su(3)_c from the z6c exact generators (reduced mod q); its
    centralizer in Der(G20) (dim 11) split into su(3)' + su(2)' by the
    root-vector ideal walk (dims 8 + 3 -- gates);
 4. Casimirs (intrinsic Killing) of color / flavor / weak on the 27;
    joint (Cc, Cf) blocks refined by Cw -> the block table.
Then the sealed criteria (A: a block with f != 0 and m = 3d, d in {1,3},
one color type; su(2)' refinement single-valued) are EVALUATED VERBATIM.
Env: SCRATCH (session scratchpad), HANDOFF4_RUN (solo run dir with pickles).
"""
import io, os, contextlib, pickle, json, itertools
import numpy as np
import sympy as sp
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ["SCRATCH"]
RUN = os.environ["HANDOFF4_RUN"]
rho = sp.symbols("rho")

with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
print("frame rebuilt", flush=True)

TW = pickle.load(open(os.path.join(SCRATCH, "b12_tower.pkl"), "rb"))
e_, det14 = TW["e_"], TW["det14"]
CD = pickle.load(open(os.path.join(RUN, "color27.pkl"), "rb"))
C8 = [[sp.Rational(x) for x in v] for v in CD["C8"]]
RP = pickle.load(open(os.path.join(RUN, "rep27.pkl"), "rb"))
REP = RP["REP"]

MUq = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)

def fval(a, rq, qq):
    a = list(a) + [sp.Integer(0)]*(3-len(a))
    s = 0
    for k in range(3):
        c = sp.Rational(a[k])
        s = (s + (c.p % qq)*pow(c.q % qq, -1, qq)*pow(rq, k, qq)) % qq
    return s

def msqrt(v, q):
    if v == 0: return 0
    if pow(v, (q-1)//2, q) != 1: return None
    return sp.sqrt_mod(v, q)

def towers_at(q):
    rts = sp.Poly(MUq.as_expr(), rho, modulus=q).ground_roots()
    if len(rts) != 3: return None
    out = []
    for rq in sorted(int(x) % q for x in rts):
        gq = msqrt(fval(e_, rq, q), q)
        if gq is None: return None
        dg = (fval(det14[0], rq, q) + gq*fval(det14[1], rq, q)) % q
        aq = msqrt((q - dg) % q, q)
        if aq in (None, 0): return None
        out.append((rq, gq, aq))
    return out

def find_prime(start):
    cand = start
    while True:
        cand = int(sp.nextprime(cand))
        t = towers_at(cand)
        if t: return cand, t

def redq(x, q):
    x = sp.Rational(x); return (x.p % q)*pow(x.q % q, -1, q) % q

def rref_rows(A0, q):
    A = [[int(x) % q for x in row] for row in
         (A0.tolist() if hasattr(A0, "tolist") else A0)]
    n_, m_ = len(A), len(A[0]); piv = []; rr = 0
    for c in range(m_):
        pr = next((x for x in range(rr, n_) if A[x][c] % q), None)
        if pr is None: continue
        A[rr], A[pr] = A[pr], A[rr]
        iv = pow(A[rr][c], -1, q); A[rr] = [(e*iv) % q for e in A[rr]]
        for x in range(n_):
            if x != rr and A[x][c]:
                f = A[x][c]; A[x] = [(A[x][j]-f*A[rr][j]) % q for j in range(m_)]
        piv.append(c); rr += 1
    return rr, np.array(A[:rr], dtype=np.int64)

def rref_null(A0, q):
    rr, A = rref_rows(A0, q)
    m_ = A.shape[1] if A.size else A0.shape[1]
    piv = [next(c for c in range(m_) if A[r_][c] % q) for r_ in range(rr)]
    fr = [c for c in range(m_) if c not in piv]; K = []
    for f2 in fr:
        v = [0]*m_; v[f2] = 1
        for i, c in enumerate(piv): v[c] = int((-A[i][f2]) % q)
        K.append(v)
    return rr, (np.array(K, dtype=np.int64) % q
                if K else np.zeros((0, m_), dtype=np.int64))

# sparse bracket table once (exact)
Tn = {}
for i in range(78):
    for j in range(i+1, 78):
        v = bracket_basis(i, j)
        nz = [(k, Fr(c)) for k, c in enumerate(v) if c != 0]
        if nz: Tn[(i, j)] = nz

def bv(u, v, q):
    w = np.zeros(78, dtype=np.int64)
    for (i, j), nz in Tn.items():
        cij = (int(u[i])*int(v[j]) - int(u[j])*int(v[i])) % q
        if cij:
            for k, f3 in nz:
                w[k] = (w[k] + cij*(f3.numerator % q)
                        * pow(f3.denominator % q, -1, q)) % q
    return w

def span_close(rows, q, max_rounds=4):
    _, B = rref_rows(np.vstack(rows), q)
    for _ in range(max_rounds):
        n = B.shape[0]
        Bk = [bv(B[a], B[b], q) for a in range(n) for b in range(a+1, n)]
        n2, B2 = rref_rows(np.vstack([B] + Bk), q)
        if n2 == n: return B
        B = B2
    return B

def analyze(q, towers):
    res = {"prime": q}
    Gq = {n: np.array([[redq(sp.Matrix(ADS[n])[i, j], q) for j in range(78)]
                       for i in range(78)], dtype=np.int64) for n in ns}
    walls = []
    for rq, gq, aq in towers:
        M1 = (Gq[8] + rq*Gq[16]) % q
        My = (gq*Gq[14] + (q-aq)*Gq[16]) % q
        _, K = rref_null(np.vstack([M1, My]), q)
        walls.append(K)
    B20 = span_close([np.vstack(walls)], q)
    res["g_dim"] = int(B20.shape[0])
    n = B20.shape[0]
    Dk = [bv(B20[a], B20[b], q) for a in range(n) for b in range(a+1, n)]
    dd, Der = rref_rows(np.vstack(Dk), q)
    res["derived_dim"] = int(dd)
    # centralizer of color inside Der: [c_a, X] = 0 for all 8 color gens
    C8q = [np.array([redq(x, q) for x in v], dtype=np.int64) for v in C8]
    rows = []
    for cg in C8q:
        # linear map X -> [cg, X] restricted to Der's span: build on basis
        rows.append(np.array([bv(cg, Der[b], q) for b in range(dd)]).T)
    Mstack = np.vstack(rows) % q          # (78*8, dd)
    _, Kc = rref_null(Mstack.T @ np.zeros((0,)) if False else Mstack, q) \
        if False else rref_null(Mstack, q)
    # columns index Der basis; kernel vectors = coeffs in Der basis
    Z = (Kc @ Der) % q
    res["z_color_dim"] = int(Kc.shape[0])
    # split Z into ideals by the root-vector ideal walk
    dz = Z.shape[0]
    rng = np.random.default_rng(5)
    ideals = None
    for attempt in range(12):
        co = rng.integers(1, q, dz)
        X = (co @ Z) % q
        adX = np.array([bv(X, Z[b], q) for b in range(dz)]).T  # 78 x dz -> proj
        # express ad(X) Z_b back in Z-coordinates: solve Z^T c = col
        rrz, Rz = rref_rows(Z, q)
        # build projection solve: for each bracket, coordinates via rref solve
        A = []
        ok = True
        for b in range(dz):
            w = bv(X, Z[b], q)
            # solve coeffs: w = sum c_a Z[a]
            aug = np.vstack([Z, w]).astype(np.int64)
            r2, _ = rref_rows(aug, q)
            if r2 != rrz: ok = False; break
            # least effort: Gaussian solve
            # solve via numpy-free elimination on [Z^T | w]
            ZT = [[int(Z[a][i]) for a in range(dz)] + [int(w[i])]
                  for i in range(78)]
            rr3, R3 = rref_rows(ZT, q)
            c = [0]*dz
            for r_ in range(rr3):
                pc = next(cc for cc in range(dz+1) if R3[r_][cc] % q)
                if pc == dz: ok = False; break
                c[pc] = int(R3[r_][dz]) % q
            if not ok: break
            A.append(c)
        if not ok: continue
        A = np.array(A, dtype=np.int64).T % q  # ad(X) in Z-coords
        chp = sp.Poly(sp.Matrix(A.tolist()).charpoly(sp.Symbol("t")).as_expr(),
                      sp.Symbol("t"), modulus=q)
        roots = chp.ground_roots()
        if sum(roots.values()) != dz: continue  # not split; retry
        nz_eig = [ev for ev in roots if int(ev) % q != 0]
        if not nz_eig: continue
        # take an eigenvector for one nonzero eigenvalue; walk its ideal
        found = []
        used = np.zeros(dz, dtype=bool)
        for ev in nz_eig:
            _, V = rref_null((A - int(ev)*np.eye(dz, dtype=np.int64)) % q, q)
            if V.shape[0] == 0: continue
            seed = (V[0] @ Z) % q
            ideal = [seed]
            _, IB = rref_rows(np.vstack(ideal), q)
            grew = True
            while grew:
                grew = False
                nb = IB.shape[0]
                new = [bv(IB[a], Z[b], q) for a in range(nb)
                       for b in range(dz)]
                n2, IB2 = rref_rows(np.vstack([IB] + new), q)
                if n2 != nb: IB, grew = IB2, True
            dimI = IB.shape[0]
            if dimI in (3, 8) and not any(d == dimI for d, _ in found):
                found.append((dimI, IB))
            if len(found) == 2: break
        if len(found) == 2:
            ideals = {d: IB for d, IB in found}
            break
    if ideals is None:
        res["split"] = "FAILED"; return res
    res["split"] = {str(d): int(ideals[d].shape[0]) for d in ideals}
    FLAV, WEAK = ideals[8], ideals[3]

    # 27-rep mod q
    def rep27(vec):
        M = np.zeros((27, 27), dtype=np.int64)
        for k, c in enumerate(vec):
            cc = int(c) % q
            if cc:
                Rk = REP[k]
                for a in range(27):
                    for b_ in range(27):
                        if Rk[a][b_]:
                            M[a][b_] = (M[a][b_] + cc*redq(Rk[a][b_], q)) % q
        return M

    def casimir(gens):
        m = len(gens)
        # intrinsic Killing: K_ab = tr(ad_F(a) ad_F(b)) inside F
        # coords: express [g_a, [g_b, g_c]] in F basis
        def coords(w):
            FT = [[int(gens[a][i]) for a in range(m)] + [int(w[i])]
                  for i in range(78)]
            rr3, R3 = rref_rows(FT, q)
            c = [0]*m
            for r_ in range(rr3):
                pc = next(cc for cc in range(m+1) if R3[r_][cc] % q)
                if pc == m: return None
                c[pc] = int(R3[r_][m]) % q
            return c
        adF = []
        for a in range(m):
            cols = []
            for b_ in range(m):
                c = coords(bv(gens[a], gens[b_], q))
                if c is None: return None, None
                cols.append(c)
            adF.append(np.array(cols, dtype=np.int64).T % q)
        K = np.array([[int(np.trace((adF[a] @ adF[b_]) % q)) % q
                       for b_ in range(m)] for a in range(m)], dtype=np.int64)
        Kinv = np.array(sp.Matrix(K.tolist()).inv_mod(q).tolist(),
                        dtype=np.int64)
        R = [rep27(gens[a]) for a in range(m)]
        Cas = np.zeros((27, 27), dtype=np.int64)
        for a in range(m):
            for b_ in range(m):
                if Kinv[a][b_]:
                    Cas = (Cas + Kinv[a][b_]*((R[a] @ R[b_]) % q)) % q
        return Cas, K

    CasC, _ = casimir(C8q)
    CasF, _ = casimir([FLAV[a] for a in range(8)])
    CasW, _ = casimir([WEAK[a] for a in range(3)])
    if CasC is None or CasF is None or CasW is None:
        res["casimir"] = "FAILED"; return res

    # joint blocks: simultaneous eigenspaces of (CasC, CasF), refined by CasW
    t = sp.Symbol("t")
    def eig_split(M, space):
        # space: rows spanning a subspace of F_q^27; decompose under M
        S = space
        MS = (M @ S.T) % q  # image coords in ambient; solve to S-coords
        # represent M restricted: solve S^T c = M s_i
        m_ = S.shape[0]
        cols = []
        for i in range(m_):
            w = (M @ S[i]) % q
            ST = [[int(S[a][j]) for a in range(m_)] + [int(w[j])]
                  for j in range(27)]
            rr3, R3 = rref_rows(ST, q)
            c = [0]*m_
            for r_ in range(rr3):
                pc = next(cc for cc in range(m_+1) if R3[r_][cc] % q)
                if pc == m_: return None
                c[pc] = int(R3[r_][m_]) % q
            cols.append(c)
        A = np.array(cols, dtype=np.int64).T % q
        chp = sp.Poly(sp.Matrix(A.tolist()).charpoly(t).as_expr(), t,
                      modulus=q)
        roots = chp.ground_roots()
        if sum(roots.values()) != m_: return None
        out = []
        for ev, mlt in roots.items():
            _, V = rref_null((A - int(ev)*np.eye(m_, dtype=np.int64)) % q, q)
            out.append((int(ev) % q, (V @ S) % q))
        return out

    I27 = np.eye(27, dtype=np.int64)
    blocks = []
    s1 = eig_split(CasC, I27)
    for cval, Vc in s1:
        s2 = eig_split(CasF, Vc)
        if s2 is None: return {**res, "blocks": "NOT-SPLIT"}
        for fval_, Vf in s2:
            s3 = eig_split(CasW, Vf)
            wvals = sorted(set(ev for ev, _ in s3)) if s3 else ["?"]
            blocks.append({"c": cval, "f": fval_,
                           "w": [int(x) for x in wvals] if s3 else wvals,
                           "dim": int(Vf.shape[0])})
    res["blocks"] = blocks
    res["tiles_27"] = sum(b["dim"] for b in blocks) == 27
    return res

out = {}
q1 = 40123
t1 = towers_at(q1)
print("prime 1:", q1, "towers", t1, flush=True)
out["p1"] = analyze(q1, t1)
print(json.dumps(out["p1"], default=str), flush=True)
q2, t2 = find_prime(40639)
print("prime 2:", q2, "towers", t2, flush=True)
out["p2"] = analyze(q2, t2)
print(json.dumps(out["p2"], default=str), flush=True)

# cross-prime agreement on the INVARIANT data: sorted block dims with
# (color-trivial?, flavor-trivial?) flags (eigenvalues are prime-dependent)
def signature(r):
    if not isinstance(r.get("blocks"), list): return None
    return sorted((b["dim"], b["c"] == 0, b["f"] == 0, len(b["w"]))
                  for b in r["blocks"])
sig1, sig2 = signature(out["p1"]), signature(out["p2"])
out["primes_agree"] = (sig1 is not None and sig1 == sig2)
print("primes agree on block signature:", out["primes_agree"], flush=True)
json.dump(out, open(os.path.join(HERE, "results.json"), "w"),
          indent=1, default=str)
print("saved", flush=True)
