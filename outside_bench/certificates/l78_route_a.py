"""OUTSIDE BENCH -- L78 ROUTE A: the level-2 filling span, and the non-vacuum reach.

Seal: outside_bench/seals/L78_ROUTE_A_PREREG.md
      sha256 bff5ed36d85880c5a667c54086aa28f88d0fd182f8ef2a9e517c59a2bf355edf

Everything below is rebuilt on this bench from the E6 Cartan matrix.  No modular
data is imported from any arc.  The stage's own consistency gates run BEFORE any
cell is computed, and no cell is read until the MB12 transversality control (C3)
shows the instrument can report a non-zero.

CELL 1  does B583 X3's level-2 rank reproduce?
CELL 2  could L78 Route A's positive outcome fire at all?
CELL 3  the theta-odd reach of a non-vacuum observer seed.   [NEW]

Run: python3 outside_bench/certificates/l78_route_a.py
"""
import numpy as np

# ---------------------------------------------------------------- E6, Bourbaki
C6 = np.array([[2, 0, -1, 0, 0, 0],
               [0, 2, 0, -1, 0, 0],
               [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0],
               [0, 0, 0, -1, 2, -1],
               [0, 0, 0, 0, -1, 2]], dtype=np.int64)   # node 2 = the branch node
MARKS = np.array([1, 2, 2, 3, 2, 1], dtype=np.int64)    # theta = sum a_i alpha_i
H_VEE = 12
DIM_E6 = 78
DETC = 3                                                # det(Cartan(E6)) = 3
CI3 = np.rint(np.linalg.inv(C6.astype(float)) * DETC).astype(np.int64)
assert np.array_equal(CI3 @ C6, DETC * np.eye(6, dtype=np.int64)), "Cinv*3 is not integral"


def weyl_group():
    """W(E6) as 6x6 integer matrices acting on ROOT coordinates, with signs."""
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]                 # s_j: alpha_i -> alpha_i - <alpha_i,alpha_j^v> alpha_j
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes(): 1}
    layer = [(I, 1)]
    mats, signs = [I], [1]
    while layer:
        nxt = []
        for M, s in layer:
            for g in gens:
                Mg = g @ M
                k = Mg.tobytes()
                if k not in seen:
                    seen[k] = -s
                    nxt.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        layer = nxt
    return np.array(mats), np.array(signs, dtype=np.int64)


def positive_roots(W):
    """The 36 positive roots of E6, in root coordinates, from the W-orbit of the simples."""
    simples = np.eye(6, dtype=np.int64)
    seen = set()
    for w in W:
        for j in range(6):
            r = w @ simples[j]
            seen.add(tuple(int(x) for x in r))
    pos = [np.array(r, dtype=np.int64) for r in sorted(seen) if all(x >= 0 for x in r)]
    return pos


def weyl_dim(labels, pos):
    """Classical dim of the E6 irrep with these Dynkin labels (Weyl's formula, exact)."""
    from fractions import Fraction
    lam = np.array(labels, dtype=np.int64) + 1                  # lambda + rho, Dynkin coords
    rho = np.ones(6, dtype=np.int64)
    num = den = 1
    # simply-laced with alpha^2 = 2: (omega_i, alpha_j) = delta_ij, so (mu, alpha) = mu . a
    for a in pos:
        num *= int(lam @ a)
        den *= int(rho @ a)                                     # = height(alpha), never zero
    d = Fraction(num, den)
    assert d.denominator == 1, "Weyl dimension is not an integer"
    return int(d)


def primaries(k):
    """Level-k integrable highest weights as Dynkin label tuples."""
    out = []
    def rec(i, rem, acc):
        if i == 6:
            out.append(tuple(acc)); return
        for v in range(rem // MARKS[i] + 1):
            rec(i + 1, rem - v * MARKS[i], acc + [v])
    rec(0, k, [])
    return sorted(out, key=lambda t: (sum(t), t))


def modular_data(k, W, eps):
    """Kac-Peterson S and T at level k, built from integer arithmetic only."""
    KH = k + H_VEE
    PRIM = primaries(k)
    N = len(PRIM)
    rho = np.ones(6, dtype=np.int64)
    A = np.array([np.array(p, dtype=np.int64) + rho for p in PRIM])     # lambda+rho, Dynkin
    X = (CI3 @ A.T).T                    # 3*(lambda+rho) in ROOT coords, integral
    # (w(l+r), m+r) = (1/9) (W @ X_l)^T C (X_m);  exponent = -2 pi i * n / (9*KH)
    MOD = 9 * KH
    Y = C6 @ X.T                                         # (6, N)
    zeta = np.exp(-2j * np.pi * np.arange(MOD) / MOD)
    epsc = eps.astype(np.complex128)
    Su = np.empty((N, N), dtype=complex)
    for l in range(N):                                   # one l at a time: bounded memory
        WXl = W @ X[l]                                   # (|W|, 6)
        nl = (WXl @ Y) % MOD                             # (|W|, N) int64
        Su[l] = epsc @ zeta[nl]
    # normalisation: S^2 must be a 0/1 permutation matrix (charge conjugation)
    S2u = Su @ Su
    beta = S2u[np.unravel_index(np.argmax(np.abs(S2u)), S2u.shape)]
    S0 = Su / np.sqrt(beta)
    # T
    c = k * DIM_E6 / KH
    h = np.array([float(np.array(pp) @ (CI3 / DETC) @ (np.array(pp) + 2 * rho)) / (2 * KH)
                  for pp in PRIM])
    T = np.diag(np.exp(2j * np.pi * (h - c / 24)))
    # the sign of the square root is fixed by the SL(2,Z) relation, not by taste
    cand = [(sg, float(np.abs(np.linalg.matrix_power(sg * S0 @ T, 3) - (S0 @ S0)).max()))
            for sg in (1.0, -1.0)]
    sg, err = min(cand, key=lambda t: t[1])
    print(f"    level {k}: (ST)^3 = S^2 residual  sign +1 -> {cand[0][1]:.3e}, "
          f"sign -1 -> {cand[1][1]:.3e}   (taken: {sg:+.0f})")
    S = sg * S0
    return PRIM, S, T, h, c


def gates(PRIM, S, T, tag):
    N = len(PRIM)
    out = {}
    out['symmetric'] = float(np.abs(S - S.T).max())
    out['unitary'] = float(np.abs(S @ S.conj().T - np.eye(N)).max())
    Cperm = S @ S
    out['S2_is_permutation'] = float(np.abs(Cperm - np.rint(Cperm.real)).max())
    P = np.rint(Cperm.real).astype(int)
    out['S2_perm_ok'] = bool((P.sum(0) == 1).all() and (P.sum(1) == 1).all()
                             and set(np.unique(P)) <= {0, 1})
    out['ST3_eq_S2'] = float(np.abs(np.linalg.matrix_power(S @ T, 3) - Cperm).max())
    d = (S[0, :] / S[0, 0]).real
    out['qdim_min'] = float(d.min())
    Nv = np.einsum('il,jl,kl,l->ijk', S, S, S.conj(), 1.0 / S[0, :])
    out['verlinde_int'] = float(np.abs(Nv - np.rint(Nv.real)).max())
    out['verlinde_nonneg'] = float(np.rint(Nv.real).min())
    print(f"  [{tag}] gates: " + "  ".join(f"{k}={v}" for k, v in out.items()))
    return Cperm, P, d, out


# ---------------------------------------------------------------- SL(2,Z) words
def sl2_reduction(p, q):
    """Ops applied (in order) to the column (p,q) to reach (+-1, 0).
    Each op is ('T', k) meaning t^{-k}, or ('S',) meaning s = [[0,-1],[1,0]]."""
    a, b, ops = p, q, []
    while b != 0:
        k = a // b
        a = a - k * b
        ops.append(('T', k))
        a, b = -b, a
        ops.append(('S',))
    return ops, a


def rho_filling(p, q, S, T, Tinv, Sinv):
    """rho(g) for g in SL(2,Z) with first column (p,q), plus the 2x2 check."""
    ops, a = sl2_reduction(p, q)
    s2 = np.array([[0, -1], [1, 0]], dtype=np.int64)
    M2 = np.eye(2, dtype=np.int64)
    R = np.eye(S.shape[0], dtype=complex)
    # g = (applied[0])^-1 ... (applied[-1])^-1 * (a*I)
    for op in ops:
        if op[0] == 'T':
            M2 = M2 @ np.array([[1, op[1]], [0, 1]], dtype=np.int64)   # (t^{-k})^{-1} = t^{k}
            R = R @ np.linalg.matrix_power(T, op[1]) if op[1] >= 0 else \
                R @ np.linalg.matrix_power(Tinv, -op[1])
        else:
            M2 = M2 @ np.array([[0, 1], [-1, 0]], dtype=np.int64)      # s^{-1}
            R = R @ Sinv
    if a < 0:
        M2 = M2 @ (-np.eye(2, dtype=np.int64))
        R = R @ (S @ S)                                                # rho(-I) = S^2
    assert M2[0, 0] == p and M2[1, 0] == q, f"word does not carry ({p},{q}): {M2}"
    return R


def slopes(Q):
    from math import gcd
    out = []
    for q in range(1, Q + 1):
        for p in range(-Q, Q + 1):
            if gcd(abs(p), q) == 1:
                out.append((p, q))
    return out


def span_rank(rows, tol=1e-9):
    if len(rows) == 0:
        return 0, np.zeros(0)
    M = np.array(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    return int((sv > tol * max(1.0, sv[0])).sum()), sv


def main():
    print("=" * 78)
    print("L78 ROUTE A -- outside bench")
    print("seal sha256 bff5ed36d85880c5a667c54086aa28f88d0fd182f8ef2a9e517c59a2bf355edf")
    print("=" * 78)

    W, eps = weyl_group()
    assert len(W) == 51840, f"|W(E6)| = {len(W)}, expected 51840"
    print(f"\nC2 (stage gates) -- |W(E6)| = {len(W)} EXACT")

    stages = {}
    for k in (1, 2):
        PRIM, S, T, h, c = modular_data(k, W, eps)
        print(f"\n  level {k}: {len(PRIM)} primaries, c = {c:.6f}, h = {np.round(h,6)}")
        Cperm, P, d, g = gates(PRIM, S, T, f"level {k}")
        assert g['symmetric'] < 1e-8 and g['unitary'] < 1e-8, "S not symmetric/unitary"
        assert g['S2_is_permutation'] < 1e-8 and g['S2_perm_ok'], "S^2 is not a permutation"
        assert g['ST3_eq_S2'] < 1e-7, "(ST)^3 != S^2"
        assert g['verlinde_int'] < 1e-6 and g['verlinde_nonneg'] >= 0, "Verlinde fails"
        assert g['qdim_min'] > 0, "a quantum dimension is non-positive"
        stages[k] = (PRIM, S, T, Cperm, P, d)
    print("\n  ALL STAGE GATES PASS.")

    # --- the C-eigenspace split at each level
    for k in (1, 2):
        PRIM, S, T, Cperm, P, d = stages[k]
        ev, V = np.linalg.eigh(Cperm.real)
        even = V[:, ev > 0.5]
        odd = V[:, ev < -0.5]
        print(f"\n  level {k}: dim(theta-even) = {even.shape[1]}, "
              f"dim(theta-odd) = {odd.shape[1]}  (C = S^2 eigenvalues "
              f"{np.round(np.sort(ev),6)})")
        stages[k] = (PRIM, S, T, Cperm, P, d, even, odd)

    # ============================================================ CELL 1 + C1 + C4
    print("\n" + "=" * 78)
    print("CELL 1 -- the vacuum-seeded filling span")
    print("=" * 78)
    results = {}
    for k in (1, 2):
        PRIM, S, T, Cperm, P, d, even, odd = stages[k]
        Sinv = np.linalg.inv(S); Tinv = np.linalg.inv(T)
        N = len(PRIM)
        e0 = np.zeros(N, dtype=complex); e0[0] = 1.0
        for Q in (5, 15, 30):                                   # C4: nested slope sets
            sl = slopes(Q)
            rows = [e0 @ rho_filling(p, q, S, T, Tinv, Sinv) for (p, q) in sl]
            r, sv = span_rank(rows)
            oddproj = max(abs(np.array(rows) @ odd).max(), 0.0) if odd.shape[1] else 0.0
            print(f"  level {k}  Q={Q:2d}  slopes={len(sl):5d}  rank={r}  "
                  f"dim(even)={even.shape[1]}  max|theta-odd proj|={oddproj:.3e}")
            results[(k, Q)] = (r, even.shape[1], oddproj)

    # ============================================================ CELL 2
    print("\n" + "=" * 78)
    print("CELL 2 -- is the positive outcome excluded a priori?")
    print("=" * 78)
    for k in (1, 2):
        PRIM, S, T, Cperm, P, d, even, odd = stages[k]
        N = len(PRIM)
        e0 = np.zeros(N, dtype=complex); e0[0] = 1.0
        a = float(np.abs(e0 @ Cperm - e0).max())
        b = float(np.abs(Cperm @ S - S @ Cperm).max())
        cc = float(np.abs(Cperm @ T - T @ Cperm).max())
        Sinv = np.linalg.inv(S); Tinv = np.linalg.inv(T)
        worst = 0.0
        for (p, q) in slopes(8):
            v = e0 @ rho_filling(p, q, S, T, Tinv, Sinv)
            worst = max(worst, float(np.abs(v @ Cperm - v).max()))
        print(f"  level {k}: |e0.C - e0| = {a:.3e}   |[C,S]| = {b:.3e}   "
              f"|[C,T]| = {cc:.3e}   worst |v.C - v| over the sweep = {worst:.3e}")

    # ============================================================ C3 + CELL 3
    print("\n" + "=" * 78)
    print("C3 (MB12 transversality) and CELL 3 -- the non-vacuum reach, level 2")
    print("=" * 78)
    PRIM, S, T, Cperm, P, d, even, odd = stages[2]
    Sinv = np.linalg.inv(S); Tinv = np.linalg.inv(T)
    N = len(PRIM)
    POS = positive_roots(W)
    assert len(POS) == 36, f"E6 has 36 positive roots, found {len(POS)}"
    NAMES = [f"{weyl_dim(p, POS)}[{''.join(str(x) for x in p)}]" for p in PRIM]
    print("  36 positive roots confirmed; the nine level-2 primaries, "
          "classical dim by Weyl's formula:")
    for i, pp in enumerate(PRIM):
        print(f"    [{i}] Dynkin {pp}   dim = {weyl_dim(pp, POS):5d}")
    perm = [int(np.argmax(P[i])) for i in range(N)]
    print(f"\n  charge conjugation C = S^2 as a permutation: {perm}")
    print("  " + ", ".join(f"{NAMES[i]}->{NAMES[perm[i]]}" for i in range(N)))
    # GATE: C must BE the E6 diagram flip (1<->6, 3<->5) on the labels -- computed, not assumed
    flip = lambda t: (t[5], t[1], t[4], t[3], t[2], t[0])
    idx = {p: i for i, p in enumerate(PRIM)}
    dflip = [idx[flip(p)] for p in PRIM]
    print(f"  the E6 diagram flip as a permutation:     {dflip}")
    assert dflip == perm, "C = S^2 is NOT the diagram flip -- the stage is misbuilt"
    print("  GATE PASSED: C = S^2 IS the diagram flip, computed independently.")

    sl = slopes(30)
    RHO = {(p, q): rho_filling(p, q, S, T, Tinv, Sinv) for (p, q) in sl}

    def reach(seed):
        rows = np.array([seed @ RHO[s] for s in sl])
        r, _ = span_rank(rows)
        proj = rows @ odd
        ro, _ = span_rank(proj)
        return r, ro, float(np.abs(proj).max())

    # C3: a seed placed INSIDE the theta-odd space must report a non-zero reach
    print("\n  C3 -- seeds placed inside the theta-odd 3-space:")
    c3_fired = False
    for j in range(odd.shape[1]):
        seed = odd[:, j].astype(complex)
        r, ro, mx = reach(seed)
        print(f"    odd basis vector {j}: span rank {r}, theta-odd reach {ro}, "
              f"max|proj| {mx:.3e}")
        if ro >= 1:
            c3_fired = True
    print(f"  C3 verdict: instrument CAN report a non-zero theta-odd reach = {c3_fired}")
    if not c3_fired:
        print("  *** C3 FAILED -- no cell may be read (memo 164). Stopping.")
        return

    print("\n  CELL 3 -- per-seed reach (nine primary seeds):")
    for i in range(N):
        seed = np.zeros(N, dtype=complex); seed[i] = 1.0
        r, ro, mx = reach(seed)
        print(f"    e[{NAMES[i]:5s}]  span rank {r}  theta-odd reach {ro}  "
              f"max|theta-odd proj| {mx:.3e}")

    print("\n  CELL 3 -- C-antisymmetric seeds (e_i - e_C(i))/sqrt2:")
    done = set()
    for i in range(N):
        j = perm[i]
        if i == j or (j, i) in done:
            continue
        done.add((i, j))
        seed = np.zeros(N, dtype=complex); seed[i] = 1.0; seed[j] = -1.0
        seed /= np.sqrt(2)
        r, ro, mx = reach(seed)
        print(f"    (e[{NAMES[i]}] - e[{NAMES[j]}])/sqrt2  span rank {r}  "
              f"theta-odd reach {ro}  max|proj| {mx:.3e}")

    print("\n  CELL 3 -- the union over all C-antisymmetric seeds:")
    allrows = []
    for (i, j) in done:
        seed = np.zeros(N, dtype=complex); seed[i] = 1.0; seed[j] = -1.0
        allrows += [seed @ RHO[s] for s in sl]
    A = np.array(allrows)
    proj = A @ odd
    ru, sv = span_rank(proj)
    print(f"    joint theta-odd reach = {ru} of {odd.shape[1]}   "
          f"singular values {np.round(sv[:4], 8)}")
    # is the C-antisymmetric span ENTIRELY inside the theta-odd space?
    tot = float((np.abs(A) ** 2).sum())
    cap = float((np.abs(proj) ** 2).sum())
    pred = 2.0 * len(done) * len(sl)          # each unnormalised seed has norm^2 = 2; rho unitary
    print(f"    Frobenius^2 of the full span = {tot:.6f}   captured by theta-odd = {cap:.6f}"
          f"   predicted if the span is entirely theta-odd = {pred:.6f}")
    print(f"    leakage into theta-even = {tot - cap:.3e}")

    print("\n" + "=" * 78)
    print("DONE -- outcomes above; interpretation lives in the memo, not here.")
    print("=" * 78)


if __name__ == '__main__':
    main()
