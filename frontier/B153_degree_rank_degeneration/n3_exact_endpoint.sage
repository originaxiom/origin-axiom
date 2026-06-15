#!/usr/bin/env sage
# B153 n=3 endpoint, EXACT over F_p (needs Sage; p = 1 mod 4 so i = sqrt(-1) exists).
#
# A = diag{1,i,-i} (order 4); bundle reps (A,t), B = A^-2 t A t^-1; (*) : t A^-2 t A = A^-1 t A t.
# The det-t-saturated (*)-ideal has TWO components in t-space (dims 3, 5 -- also seen over Q(i)). For each,
# we exhibit an F_p point and compute, EXACTLY over F_p, the full-variety A-free Zariski tangent
# (F1=tA-A^2 B t, F2=tB-A B t, with A,B,t free, 27 vars), whether tr A can move in SL x SL, the
# degree=rank relation [A,B] = +mu^3/det t (n=3 sign (-1)^{n-1}=+), and Burnside irreducibility.
#
# RESULT (3 primes, consistent): the dim-5 component is the genuine geometric one -- RIGID (tr A fixed),
# IRREDUCIBLE (Burnside rank 9), carries L=+M^3 (matrix identity); the dim-3 component is a REDUCIBLE
# SLICE (tr A moves, Burnside rank 5, no relation). This upgrades the n=3 endpoint from numerical to
# exact, and CORRECTS the earlier numerical "slice-piece tangent 14" (exact value 10, and it is reducible).
#
# The tangent function is validated against the known n=4 case (A-free tangent 19; audit/lab).
# Run:  sage frontier/B153_degree_rank_degeneration/n3_exact_endpoint.sage
n = 3
PRIMES = [1000037, 1000253, 1000273]   # all = 1 mod 4

def afree_tangent(F, A, A2i, t0):
    B0 = A2i * t0 * A * t0.inverse()
    def dF(dA, dB, dt):
        dF1 = dt*A + t0*dA - (dA*A*B0*t0 + A*dA*B0*t0 + A*A*dB*t0 + A*A*B0*dt)
        dF2 = dt*B0 + t0*dB - (dA*B0*t0 + A*dB*t0 + A*B0*dt)
        return list(dF1.list()) + list(dF2.list())
    Z = zero_matrix(F, n, n); cols = []
    for which in range(3):
        for a in range(n):
            for b in range(n):
                E = zero_matrix(F, n, n); E[a, b] = 1
                cols.append(dF(E if which == 0 else Z, E if which == 1 else Z, E if which == 2 else Z))
    J = matrix(F, cols).transpose(); rk = J.rank()
    Kb = J.right_kernel().basis_matrix()
    A0i = A.inverse(); t0i = t0.inverse()
    c_trA  = lambda v: sum(v[k*n+k] for k in range(n))
    c_detA = lambda v: sum(A0i[b,a]*v[a*n+b] for a in range(n) for b in range(n))
    c_dett = lambda v: sum(t0i[b,a]*v[2*n*n+a*n+b] for a in range(n) for b in range(n))
    sl = matrix(F, [[c_detA(Kb.row(r)), c_dett(Kb.row(r))] for r in range(Kb.nrows())]) if Kb.nrows() else matrix(F,0,2)
    al = matrix(F, [[c_detA(Kb.row(r)), c_dett(Kb.row(r)), c_trA(Kb.row(r))] for r in range(Kb.nrows())]) if Kb.nrows() else matrix(F,0,3)
    return 3*n*n - rk, bool(al.rank() > sl.rank())

def relation_and_irr(F, A, A2i, t0):
    B0 = A2i * t0 * A * t0.inverse()
    mu = A.inverse() * t0
    comm = A * B0 * A.inverse() * B0.inverse()
    rel = (comm == (mu**3) / t0.det())                  # L = (-1)^{n-1} M^n / det t, n=3 -> +
    gens = [A, B0, A.inverse(), B0.inverse()]
    fr = [identity_matrix(F, n)]; allm = [identity_matrix(F, n)]
    for _ in range(5):
        fr = [g*m for m in fr for g in gens]; allm += fr
    return bool(rel), int(matrix(F, [m.list() for m in allm]).rank())

def point_on(R, tg, P, F):
    d = P.dimension()
    seeds = [[1,2,3,4,5,6,7,8,9],[9,1,8,2,7,3,6,4,5],[2,3,5,7,11,13,17,19,23],
             [1,4,1,5,9,2,6,5,3],[3,1,4,1,5,9,2,6,5],[7,2,9,1,4,8,3,6,2]]
    for attempt in range(len(seeds)-d+1):
        cuts = [sum(F(seeds[(attempt+r) % len(seeds)][k])*tg[k] for k in range(n*n)) - F(r+2) for r in range(d)]
        Jz = R.ideal(list(P.gens()) + cuts)
        if Jz.dimension() != 0:
            continue
        V = Jz.variety(F)
        if V:
            return V[0]
    return None

def main():
    print("=== B153 n=3 endpoint, EXACT over F_p (A=diag{1,i,-i}) ===")
    rigid_ok = True
    for p in PRIMES:
        F = GF(p); i = F(-1).sqrt()
        A = matrix(F, [[1,0,0],[0,i,0],[0,0,-i]]); A2i = (A*A).inverse(); Ai = A.inverse()
        R = PolynomialRing(F, ['t%d%d'%(a,b) for a in range(n) for b in range(n)], order='degrevlex')
        tg = R.gens(); t = matrix(R, n, n, tg)
        star = t*A2i*t*A - Ai*t*A*t
        Isat = R.ideal([star[a,b] for a in range(n) for b in range(n)]).saturation(R.ideal(t.det()))[0]
        comps = Isat.minimal_associated_primes()
        print("p=%d:" % p)
        for P in sorted(comps, key=lambda Q: Q.dimension()):
            d = P.dimension(); pt = point_on(R, tg, P, F)
            if pt is None:
                print("   t-comp dim %d: (no F_p point)" % d); continue
            t0 = matrix(F, n, n, [pt[g] for g in tg])
            tang, moves = afree_tangent(F, A, A2i, t0)
            rel, brank = relation_and_irr(F, A, A2i, t0)
            kind = "SLICE" if moves else "RIGID"
            print("   t-comp dim %d:  A-free tangent=%2d  %-5s  L=+M^3:%-5s  Burnside=%d  %s"
                  % (d, tang, kind, rel, brank, "(irreducible)" if brank == n*n else "(reducible)"))
            if d == 5:   # the geometric component
                rigid_ok = rigid_ok and (not moves) and rel and brank == n*n and tang == 11
    print("\nn=3 geometric (dim-5) component: RIGID + L=+M^3 + irreducible, tangent 11 --",
          "PASS" if rigid_ok else "FAIL")
    return rigid_ok

# sage runs .sage files with __name__ != "__main__", so call directly:
main()
