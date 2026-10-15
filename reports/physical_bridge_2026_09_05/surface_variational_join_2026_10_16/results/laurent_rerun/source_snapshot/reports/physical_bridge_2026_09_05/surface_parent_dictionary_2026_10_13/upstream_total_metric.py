"""Exact metric-to-spin reconstruction. No global spectral inference."""
from functools import lru_cache
import json
import sympy as s

x, y, u, v = s.symbols('x y u v', real=True)
l, A = s.symbols('ell A', positive=True)
# y is positive in every formula; rebind before building the metric.
y = s.Symbol('y', positive=True)
n = s.Symbol('n', real=True)
coords = (x, y, u, v)
I = s.eye(4)
Z = s.zeros(4)


def simp(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def zero(a):
    b = simp(a)
    return b == s.zeros(*b.shape) if isinstance(b, s.MatrixBase) else b == 0


def gammas():
    p1 = s.Matrix([[0, 1], [1, 0]])
    p2 = s.Matrix([[0, -s.I], [s.I, 0]])
    p3 = s.diag(1, -1)
    return [s.I*s.kronecker_product(p1, s.eye(2)),
            s.I*s.kronecker_product(p2, s.eye(2)),
            s.I*s.kronecker_product(p3, p1),
            s.I*s.kronecker_product(p3, p2)]


def coordinate_connection(g):
    gi = simp(g.inv())
    G = [[[simp(sum(gi[k, d]*(s.diff(g[d, b], coords[a])
                 +s.diff(g[d, a], coords[b])-s.diff(g[a, b], coords[d]))
                 for d in range(4))/2) for b in range(4)]
                 for a in range(4)] for k in range(4)]
    return gi, G


def scalar_curvature(gi, G):
    ric = s.zeros(4)
    for a in range(4):
        for b in range(4):
            ric[a, b] = simp(sum(s.diff(G[c][a][b], coords[c])
                -s.diff(G[c][c][b], coords[a])
                +sum(G[c][c][d]*G[d][a][b]-G[c][a][d]*G[d][c][b]
                     for d in range(4)) for c in range(4)))
    return simp(sum(gi[a, b]*ric[a, b] for a in range(4) for b in range(4)))


@lru_cache(None)
def geometry():
    g = s.diag(l*l/y**2, l*l/y**2, A/y, A*(x*x/y+y))
    g[2, 3] = g[3, 2] = A*x/y
    co = s.Matrix([[l/y, 0, 0, 0], [0, l/y, 0, 0],
                   [0, 0, s.sqrt(A/y), x*s.sqrt(A/y)],
                   [0, 0, 0, s.sqrt(A*y)]])
    E = simp(co.inv().T)  # row i is Ei in coordinate components
    gi, G = coordinate_connection(g)
    C = [[[simp(sum(co[k, a]*sum(E[i, b]*s.diff(E[j, a], coords[b])
             -E[j, b]*s.diff(E[i, a], coords[b]) for b in range(4))
             for a in range(4))) for k in range(4)] for j in range(4)] for i in range(4)]
    GK = [[[simp((C[i][j][k]-C[j][k][i]+C[k][i][j])/2)
            for k in range(4)] for j in range(4)] for i in range(4)]
    GC = [[[simp(sum(co[k, a]*(sum(E[i, b]*s.diff(E[j, a], coords[b]) for b in range(4))
             +sum(G[a][b][c]*E[i, b]*E[j, c] for b in range(4) for c in range(4)))
             for a in range(4))) for k in range(4)] for j in range(4)] for i in range(4)]
    cs = gammas()
    omega = [simp(sum((GK[i][j][k]*cs[j]*cs[k]/4 for j in range(4)
                      for k in range(4)), Z)) for i in range(4)]
    wc = [simp(sum((co[i, a]*omega[i] for i in range(4)), Z)) for a in range(4)]
    M = [simp(sum((cs[i]*E[i, a] for i in range(4)), Z)) for a in range(4)]
    K = simp(sum((cs[i]*omega[i] for i in range(4)), Z))
    return g, co, E, gi, G, C, GK, GC, cs, omega, wc, M, K


def lichnerowicz_residual(K, wc, R, twist_curvature=Z):
    g, co, E, gi, G, C, GK, GC, cs, omega, unused, M, _ = geometry()
    rows = []
    for a in range(4):
        for b in range(a, 4):
            factor = 1 if a == b else 2
            square = M[a]*M[b] if a == b else M[a]*M[b]+M[b]*M[a]
            rows.append(simp(square+factor*gi[a, b]*I))
    for b in range(4):
        dsq = sum((M[a]*M[b].diff(coords[a]) for a in range(4)), Z)+K*M[b]+M[b]*K
        lap = -2*sum((gi[a, b]*wc[a] for a in range(4)), Z)
        lap += sum(gi[a, c]*G[b][a][c] for a in range(4) for c in range(4))*I
        rows.append(simp(dsq-lap))
    dsq = sum((M[a]*K.diff(coords[a]) for a in range(4)), Z)+K*K
    lap = -sum((gi[a, b]*(wc[b].diff(coords[a])+wc[a]*wc[b]
              -sum((G[c][a][b]*wc[c] for c in range(4)), Z))
              for a in range(4) for b in range(4)), Z)
    rows.append(simp(dsq-lap-R*I/4-twist_curvature))
    return rows


@lru_cache(None)
def checks():
    out = {}
    def ck(label, condition):
        out[label] = bool(condition)
        if not out[label]:
            raise AssertionError(label)
    g, co, E, gi, G, C, GK, GC, cs, omega, wc, M, K = geometry()
    ck('metric_from_coframe', zero(co.T*co-g))
    ck('dual_frame', zero(co*E.T-I))
    ck('volume', zero(g.det()-l**4*A**2/y**4))
    expected = {(0, 1, 0): -1/l, (1, 2, 2): 1/(2*l),
                (0, 3, 2): -1/l, (1, 3, 3): -1/(2*l)}
    expected.update({(j, i, k): -a for (i, j, k), a in list(expected.items())})
    for i in range(4):
        for j in range(4):
            ck(f'clifford_{i}_{j}', zero(cs[i]*cs[j]+cs[j]*cs[i]+(2*I if i == j else Z)))
            for k in range(4):
                ck(f'bracket_{i}_{j}_{k}', zero(C[i][j][k]-expected.get((i, j, k), 0)))
                ck(f'connection_{i}_{j}_{k}', zero(GK[i][j][k]-GC[i][j][k]))
                ck(f'metric_compatibility_{i}_{j}_{k}', zero(GK[i][j][k]+GK[i][k][j]))
                ck(f'torsion_{i}_{j}_{k}', zero(GK[i][j][k]-GK[j][i][k]-C[i][j][k]))
            ck(f'spin_compatibility_{i}_{j}', zero(omega[i]*cs[j]-cs[j]*omega[i]
                -sum((GK[i][j][k]*cs[k] for k in range(4)), Z)))
        ck(f'skew_clifford_{i}', zero(cs[i].H+cs[i]))
    mixed = cs[0]*cs[2]*cs[3]/(4*l)
    ck('full_spin_term', zero(K+cs[1]/(2*l)-mixed))
    rho = l*l*A/y**2
    div = [simp(sum(s.diff(rho*E[i, a], coords[a]) for a in range(4))/rho) for i in range(4)]
    ck('density_divergence', div == [0, -1/l, 0, 0])
    ck('formal_adjoint', zero(sum((cs[i]*div[i] for i in range(4)), Z)+K.H-K))
    ck('missing_density_rejected', not zero(sum((cs[i]*div[i] for i in range(4)), Z)+mixed.H-mixed))
    chir = -cs[0]*cs[1]*cs[2]*cs[3]
    ck('chirality_square', zero(chir*chir-I))
    ck('chirality_zeroth', zero(chir*K+K*chir))
    for a in range(4):
        ck(f'chirality_symbol_{a}', zero(chir*M[a]+M[a]*chir))
    R = scalar_curvature(gi, G)
    ck('scalar_curvature', zero(R+3/l**2))
    for j, residual in enumerate(lichnerowicz_residual(K, wc, R)):
        ck(f'lichnerowicz_{j}', zero(residual))
    for name, wrong in [('omitted', K-mixed), ('reversed', K-2*mixed)]:
        ck(f'{name}_mixed_rejected', any(not zero(r) for r in lichnerowicz_residual(wrong, wc, R)))
    wn = list(wc)
    wn[0] = wn[0]-6*s.I*n*I/y
    Kn = K-6*s.I*n*cs[0]/l
    for j, residual in enumerate(lichnerowicz_residual(Kn, wn, R, -6*s.I*n*cs[0]*cs[1]/l**2)):
        ck(f'twisted_lichnerowicz_{j}', zero(residual))
    deck = s.Matrix([x+1, y, u-v, v])
    ck('cusp_deck_coframe', zero(co.subs(dict(zip(coords, deck)), simultaneous=True)*deck.jacobian(coords)-co))
    # U=y^-1/2 up to a positive constant. U D U^-1 adds c2/(2l).
    density_correction = sum((M[a]*s.diff(s.sqrt(y), coords[a])/s.sqrt(y) for a in range(4)), Z)
    ck('unitary_radial_term', zero(K+density_correction-mixed))
    ck('radial_density', zero(rho*y*(y/(l*l*A))-1))
    fg, fG = coordinate_connection(s.eye(4))
    ck('flat_control_connection', all(zero(fG[k][i][j]) for i in range(4) for j in range(4) for k in range(4)))
    ck('flat_control_curvature', zero(scalar_curvature(fg, fG)))
    return out


if __name__ == '__main__':
    rows = checks()
    print(json.dumps({'checks': rows, 'passed': len(rows), 'scope': 'differential expression, not global domain or physical spectrum'}, indent=2))
