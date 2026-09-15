"""Main's check of B1352's two locus points (read from the seat's fixed_locus_points.json, 60-digit 27x27 matrices):
(i) the figure-eight relator residual under a -> '1', b -> '2' (SnapPy's presentation aaabABBAb), (ii) h^1(27) and h^1(27bar)
by main's Fox calculus, N = h^1(27) - h^1(27bar), (iii) the joint fixed space of the peripheral images (cusp-fixed weights)."""
import json, mpmath as mp, snappy
mp.mp.dps = 70
d = json.load(open("<sm worktree @ 1703c0d8>/frontier/B1352_the_fixed_vector_locus_along_v10/verification/fixed_locus_points.json"))
rel = "abABaBAbaB"; per = ("a", "bABaaBAb")   # the seat's presentation (spectrum_law.py): a w = w b, w = bABa; meridian a; longitude w w*
print("presentation (seat's): relator", rel, "meridian/longitude", per)
def tomat(rows): return mp.matrix([[mp.mpc(mp.mpf(x[0].replace(" ","")), mp.mpf(x[1].replace(" ",""))) for x in r] for r in rows])
def word(w, A, B):
    D = {'a': A, 'b': B, 'A': A**-1, 'B': B**-1}; M = mp.eye(A.rows)
    for ch in w: M = M*D[ch]
    return M
def rank(Mx, tol):
    H = Mx.H*Mx; ev = [mp.re(e) for e in mp.eig(H)[0]]; mx = max(abs(e) for e in ev) or mp.mpf(1)
    return sum(1 for e in ev if abs(e) > tol*mx) if mx > tol else 0
def fox_h1(A, B):
    n = A.rows; I = mp.eye(n); D = {'a': A, 'b': B, 'A': A**-1, 'B': B**-1}
    val = I; dd = {'a': mp.zeros(n,n), 'b': mp.zeros(n,n)}
    for ch in rel:
        g = ch.lower(); X = D[ch]
        if ch.islower(): dd[g] = dd[g] + val
        else: dd[g] = dd[g] - val*X
        val = val*X
    d0 = mp.zeros(2*n, n); d1 = mp.zeros(n, 2*n)
    for i in range(n):
        for j in range(n):
            d0[i,j]=(A-I)[i,j]; d0[n+i,j]=(B-I)[i,j]; d1[i,j]=dd['a'][i,j]; d1[i,n+j]=dd['b'][i,j]
    r0, r1 = rank(d0, mp.mpf(10)**-40), rank(d1, mp.mpf(10)**-40)
    return (2*n - r1) - r0, n - r0
for name, v in d.items():
    A = tomat(v['1']); B = tomat(v['2'])
    resid = max(abs(x) for x in (word(rel, A, B) - mp.eye(27)))
    print(f"\n== {name}: seat's residual {v['residual']}, self_dual {v['self_dual']}")
    print(f"   relator residual (a->1, b->2): {mp.nstr(resid, 3)}")
    if resid > mp.mpf(10)**-30:
        A, B = B, A; resid = max(abs(x) for x in (word(rel, A, B) - mp.eye(27))); print(f"   swapped generators: residual {mp.nstr(resid,3)}")
    h1, h0 = fox_h1(A, B); h1d, h0d = fox_h1((A**-1).T, (B**-1).T)
    print(f"   h^0(27) = {h0}, h^1(27) = {h1};  h^0(27bar) = {h0d}, h^1(27bar) = {h1d};  N = h^1(27) - h^1(27bar) = {h1 - h1d}   [seat: h1(27) = h1(27bar) = 3, N = 0]")
    Mm = word(per[0], A, B); Ml = word(per[1], A, B)
    stacked = mp.matrix(54, 27)
    for i in range(27):
        for j in range(27): stacked[i,j] = (Mm - mp.eye(27))[i,j]; stacked[27+i,j] = (Ml - mp.eye(27))[i,j]
    fixed = 27 - rank(stacked, mp.mpf(10)**-40)
    print(f"   joint fixed space of the peripheral images on the 27: dim {fixed}   [seat: exactly three cusp-fixed weights]")
    print(f"   self-duality check: |tr A - tr A^-1| = {mp.nstr(abs(sum(A[i,i] for i in range(27)) - sum((A**-1)[i,i] for i in range(27))), 3)}")
