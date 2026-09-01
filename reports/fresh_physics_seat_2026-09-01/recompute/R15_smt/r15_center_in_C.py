"""Verify (mod p, both primes) that the 3-dim center of the wall centralizer lies
inside the charge torus C = span(g8,g14,g16,g22) — the B992-compatible fact."""
HERE = __file__.rsplit("/", 1)[0]
src = open(HERE + '/r15_types_modp.py').read().split("# ---------------- run at banked prime")[0]
src = src.replace('__file__.rsplit("/", 1)[0]', repr(HERE))
exec(src)
from flint import nmod_mat
for p in (40123, 40039):
    rs, _ = poly_roots_modp(MU, p)
    s2, _ = poly_roots_modp(SEXT2, p)
    hit = None
    for r in rs:
        for s in s2:
            nul, Mat = joint_nullity(p, r, s)
            if nul == 14:
                hit = (r, s, Mat); break
        if hit: break
    r, s, Mat = hit
    X, k = Mat.nullspace()
    Z = [[int(X[i, j]) for i in range(DIM)] for j in range(k)][:k]
    # center vectors: v = sum c_i Z_i with [v, Z_b] = 0 for all b
    colmat = []
    for cix in range(len(Z)):
        col = []
        for b in range(len(Z)):
            col += brk_modp(Z[cix], Z[b], p)
        colmat.append(col)
    Cm = nmod_mat(colmat, p).transpose()
    Xc, kc = Cm.nullspace()
    print(f"p={p}: center dim = {kc if kc<=3 else 'check'}", end=" ")
    # center vectors in ambient coords
    cvs = []
    for j in range(kc):
        v = [0]*DIM
        for i in range(len(Z)):
            ci = int(Xc[i, j])
            for t in range(DIM):
                v[t] = (v[t] + ci*Z[i][t]) % p
        cvs.append(v)
    # span test: rank of [charges; center vectors] == 4?
    ch = []
    for n in (8, 14, 16, 22):
        v = [0]*DIM
        for kk, c in charges[n].items():
            v[kk] = c % p
        ch.append(v)
    r4 = nmod_mat(ch, p).rank()
    rall = nmod_mat(ch + cvs, p).rank()
    print(f"rank(C)={r4}, rank(C + center)={rall} -> center subset of C: {rall == r4}")
