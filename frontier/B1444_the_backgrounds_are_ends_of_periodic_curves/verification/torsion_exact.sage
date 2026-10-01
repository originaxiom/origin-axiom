# Exact sector torsion on the twisted period-3 curve of the root.  PSL(2) curve = the u-line; X = u - 1, Y = -Z,
# Z^2 = 1 + 1/u^2.  Explicit matrices need q with q + 1/q = Z; the meridian needs c with c^2 det T = 1.
import itertools, json
K.<u> = FunctionField(QQ); Rt.<t> = K[]
L.<Z> = K.extension(t^2 - 1 - 1/u^2); Rq.<s> = L[]
M.<q> = L.extension(s^2 - Z*s + 1)
X = M(u - 1); Y = -M(Z)
rx = matrix(M, [[X, -1], [1, 0]]); ry = matrix(M, [[0, q], [-1/q, Y]])
PX, PY = "xyxyxxyxyxxyxxyxyxxyx", "yxxyxxyxyxxyx"; SX, SY = 1, -1
def wordmat(w, gx, gy):
    r = identity_matrix(gx.base_ring(), 2)
    for ch in w: r = r * (gx if ch == "x" else gy)
    return r
Px, Py = wordmat(PX, rx, ry), wordmat(PY, rx, ry)
rows = []
for g, P, sg in ((rx, Px, SX), (ry, Py, SY)):
    for i in range(2):
        for j in range(2):
            row = [M(0)] * 4
            for a in range(2):
                for b in range(2):
                    if a == i: row[2*a + b] += g[b, j]
                    if b == j: row[2*a + b] -= sg * P[i, a]
            rows.append(row)
ker = matrix(M, rows).right_kernel(); assert ker.dimension() == 1
v = ker.basis()[0]; T = matrix(M, [[v[0], v[1]], [v[2], v[3]]]); dT = T.det(); trT = T.trace()
print("tr^2 T / det T =", trT^2/dT)
# cyclotomic twist: a = (zeta8^i, zeta8^j); work over M(zeta8) by hand: elements A + B*z with z^4 = -1 ... use a number field base instead
C.<z> = CyclotomicField(8)
KC.<uu> = FunctionField(C); RtC.<tt> = KC[]
LC.<ZZ_> = KC.extension(tt^2 - 1 - 1/uu^2); RqC.<ss> = LC[]
MC.<qq> = LC.extension(ss^2 - ZZ_*ss + 1)
def lift(e):
    # M -> MC
    co = e.list()   # coefficients in q over L
    out = MC(0)
    for k, ck in enumerate(co):
        cz = ck.list(); val = LC(0)
        for m_, cm in enumerate(cz):
            val += KC(cm.numerator().change_ring(C)(uu) / cm.denominator().change_ring(C)(uu)) * ZZ_^m_
        out += MC(val) * qq^k
    return out
rxC = rx.apply_map(lift); ryC = ry.apply_map(lift); TC = T.apply_map(lift); dTC = lift(dT); trTC = lift(trT)
def fox(w, gx, gy):
    dx = zero_matrix(MC, 2); dy = zero_matrix(MC, 2); pre = identity_matrix(MC, 2)
    for ch in w:
        if ch == "x": dx += pre; pre = pre * gx
        else: dy += pre; pre = pre * gy
    return dx, dy
res = {}
Rc.<c> = MC[]
for (i, j) in itertools.product((0, 2, 4, 6), (1, 3, 5, 7)):
    gx, gy = z^i * rxC, z^j * ryC
    xx, xy = fox(PX, gx, gy); yx, yy = fox(PY, gx, gy)
    Vt = c * TC.change_ring(Rc)
    D = block_matrix(Rc, [[Vt - xx.change_ring(Rc), -xy.change_ring(Rc)], [-yx.change_ring(Rc), Vt - yy.change_ring(Rc)]])
    N = D.det()                       # polynomial in c, degree 4;  reduce with c^2 = 1/dT
    co = N.list() + [MC(0)] * 5
    A = co[0] + co[2]/dTC + co[4]/dTC^2; B = co[1] + co[3]/dTC          # N = A + B c
    # denominator det(cT - 1) = c^2 dT - c trT + 1 = 2 - c trT
    # tau = (A + B c)/(2 - c trT) ;  conjugate c -> -c
    nrm = (A^2 - B^2/dTC) / (4 - trTC^2/dTC)
    tra = ((A + B*c)*(2 + c*trTC) + (A - B*c)*(2 - c*trTC))    # numerator of tau + tau' over (4 - c^2 trT^2)
    tra = (2*2*A + 2*B*trTC/dTC) / (4 - trTC^2/dTC)
    res[(i, j)] = (nrm, tra)
    print("a = (%d,%d)\n   tau*tau' = %s\n   tau+tau' = %s" % (i, j, nrm, tra)); sys.stdout.flush()
