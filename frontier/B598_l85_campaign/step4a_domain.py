"""B598 step 4a — the typed DOMAIN of the P2 map (failure-enforcing).

Per block m in {1,4,5,7,8,11} (V_m the adjoint block of dim d):
  (i)   re-certify dim H1(pi_K; V_m) = 1 (Fox relator cocycles mod
        coboundaries; B575-G4 / P1's gate, recomputed here);
  (ii)  the peripheral module: W_mu = acts['a'], W_lam = the CERTIFIED
        longitude word 'abABaaBAbA'; compute dim H0(T^2; V_m),
        dim Z1(T^2), dim B1(T^2), dim H1(T^2) exactly, and the Euler
        gate dim H1 = dim H0 + dim H2 (chi(T^2) = 0; H2 = coinvariants);
  (iii) res: H1(pi_K) -> H1(T^2): evaluate the solved knot-group cocycle
        on (mu, lambda), certify it lies in Z1(T^2) and is NONZERO mod
        B1(T^2)  =>  res is injective on each of the six lines;
  (iv)  the polarization face: report whether the class has nonzero
        mu-component mod B1 (the mu-line convention of slot 8).

Exits nonzero on any gate failure. Run: OA_SLOW=1 python3 step4a_domain.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; meye = ns['meye']
nullspace = ns['nullspace']; rref = ns['rref']
BLOCK_DATA = ns['BLOCK_DATA']
REL = ns['REL']

LONGITUDE = "abABaaBAbA"          # the certified true longitude (P1 erratum)


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def word_action(acts, word):
    d = len(acts['a'])
    W = meye(d)
    for ch in word:
        W = mmul(W, acts[ch])
    return W


def fox_pair(acts, d):
    I = meye(d)
    Da = [[K0] * d for _ in range(d)]
    Db = [[K0] * d for _ in range(d)]
    P = I
    for ch in REL:
        if ch == 'a':
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] + P[i][j]
        elif ch == 'A':
            PA = mmul(P, acts['A'])
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] - PA[i][j]
        elif ch == 'b':
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] + P[i][j]
        else:
            PB = mmul(P, acts['B'])
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] - PB[i][j]
        P = mmul(P, acts[ch])
    return Da, Db


def cocycle_eval(acts, xa, xb, word):
    d = len(xa)
    val = [K0] * d
    P = meye(d)
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
        P = mmul(P, acts[ch])
    return val


def matrix_rank(rows):
    live = [list(r) for r in rows if any(not x.is_zero() for x in r)]
    if not live:
        return 0
    _, piv = rref(live)
    return len(piv)


allok = True
print("STEP 4a: the typed domain (six blocks; the certified longitude)")
for m in sorted(BLOCK_DATA):
    D = BLOCK_DATA[m]
    d, acts = D['d'], D['acts']

    # (i) H1(pi_K; V_m) via Fox calculus on the relator
    Da, Db = fox_pair(acts, d)
    rows = [[Da[i][j] for j in range(d)] + [Db[i][j] for j in range(d)]
            for i in range(d)]
    sols = nullspace(rows)                      # Z1(pi_K) as (xa, xb) pairs
    cob = []                                    # coboundaries: v -> ((a-1)v,(b-1)v)
    Ia = acts['a']; Ib = acts['b']
    for j in range(d):
        e = [K1 if t == j else K0 for t in range(d)]
        cob.append([x - y for x, y in zip(mat_vec(Ia, e), e)] +
                   [x - y for x, y in zip(mat_vec(Ib, e), e)])
    rk_cob = matrix_rank(cob)
    dimH1K = len(sols) - rk_cob
    g1 = dimH1K == 1
    allok &= g1

    # pick the H1 generator: a Z1 element independent of coboundaries
    gen = None
    for s in sols:
        if matrix_rank(cob + [s]) > rk_cob:
            gen = s
            break
    allok &= gen is not None
    xa, xb = gen[:d], gen[d:]

    # (ii) the peripheral T^2 module
    Wmu = acts['a']
    Wlam = word_action(acts, LONGITUDE)
    comm = mmul(Wmu, Wlam)
    comm2 = mmul(Wlam, Wmu)
    gcomm = all((comm[i][j] - comm2[i][j]).is_zero()
                for i in range(d) for j in range(d))
    allok &= gcomm                              # peripheral subgroup abelian

    Mmu = [[Wmu[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
    Mlam = [[Wlam[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
    # H0 = fix(Wmu) cap fix(Wlam)
    h0 = len(nullspace(Mmu + Mlam))
    # Z1(T^2): (Wmu-1) x_lam = (Wlam-1) x_mu   on pairs (x_mu, x_lam)
    zrows = [[K0 - Mlam[i][j] for j in range(d)] + [Mmu[i][j] for j in range(d)]
             for i in range(d)]
    z1 = len(nullspace(zrows))
    # B1(T^2): v -> ((Wmu-1)v, (Wlam-1)v)
    bgen = []
    for j in range(d):
        e = [K1 if t == j else K0 for t in range(d)]
        bgen.append(mat_vec(Mmu, e) + mat_vec(Mlam, e))
    b1 = matrix_rank(bgen)
    h1 = z1 - b1
    # H2(T^2; V_m): the CW cochain complex of T^2 has delta^1 = zrows, so
    # h2 = d - rank(delta^1) = d - (2d - z1) = z1 - d identically; the Euler
    # identity h1 = h0 + h2 is then automatic (rank-nullity) — NOT a gate
    # (MB12: it cannot fail). Report the duality comparison h0 vs h2 instead.
    h2 = z1 - d

    # (iii) res of the H1(pi_K) generator
    xi_mu = cocycle_eval(acts, xa, xb, "a")
    xi_lam = cocycle_eval(acts, xa, xb, LONGITUDE)
    pair = xi_mu + xi_lam
    # in Z1(T^2)?
    lhs = mat_vec(Mmu, xi_lam)
    rhs = mat_vec(Mlam, xi_mu)
    gz = all((lhs[i] - rhs[i]).is_zero() for i in range(d))
    allok &= gz
    # nonzero mod B1?
    ginj = matrix_rank(bgen + [pair]) > b1
    allok &= ginj

    # (iv) the mu-polarization face: xi_mu nonzero mod (Wmu-1)V + is the class
    # detected by its mu-leg alone?  report (not a gate)
    mu_leg = matrix_rank([mat_vec(Mmu, [K1 if t == j else K0 for t in range(d)])
                          for j in range(d)] + [xi_mu])
    mu_only = matrix_rank([mat_vec(Mmu, [K1 if t == j else K0 for t in range(d)])
                           for j in range(d)])
    print(f"  block m={m:2d} (dim {d:2d}): dim H1(pi_K)={dimH1K} [{g1}];  "
          f"T^2: h0={h0} z1={z1} b1={b1} h1={h1} h2={h2} duality(h0=h2): {h0 == h2}  "
          f"[mu,lam]=1[{gcomm}];  res in Z1[{gz}] nonzero mod B1[{ginj}];  "
          f"mu-leg detects: {mu_leg > mu_only}")

print()
assert allok, "STEP 4a FAILED"
print("STEP 4a: the domain is TYPED — six lines, res injective at every block. DONE")
