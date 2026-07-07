#!/usr/bin/env python3
"""B446 (Thermodynamic Campaign D1) — the tower moment law + the twisted SFF.

Independent rebuild per PREREGISTRATION.md (the 2026-07-06 review pilot is NOT trusted;
every number is re-derived here from scratch).

Pipeline:
  1. Weil-formula quantization U(B) at odd N  (gcd(B[0,1], N) = 1).
  2. Hecke desymmetrization: norm-one units aI + bA of Z[A]/N, joint-diagonalized
     with parity via a random-Hermitian-combination split.
  3. Moments of the matrix elements of f = cos(2*pi*x) over the Hecke eigenbasis.
  4. Gates (prime N): Kurlberg-Rudnick N*Var -> 1.00 (the arithmetically-enhanced,
     parity-coherent constant; generic/RMT would give 1/2), m4/m2^2 -> 2.00 (SU(2)).
  5. The tower N = 15*3^k: measure N*Var and kurtosis; test the CRT product law
     N*Var = C3 * S5 against the independently measured pure-3-power constant C3
     (N = 243, 729) and the exact 5-dim factor S5 (N = 5, closed form).
  6. Same-class control: the silver cat map A2 = R^2 L^2 = [[5,2],[2,1]].
  7. SFF: untwisted (pre-registered launder-control: the Pisano/P59 degeneracy law
     ord(A mod N) = pi(N)/2 forces non-RMT spikes) and parity-resolved.

Run:  python3 pipeline.py           (~10-20 min; results printed + results.json)
"""
import json
import math
import time
import numpy as np

rng = np.random.default_rng(20260706)

A_GOLD = np.array([[2, 1], [1, 1]])     # R L,   trace 3 = 1^2 + 2
A_SILV = np.array([[5, 2], [2, 1]])     # R^2L^2, trace 6 = 2^2 + 2

TOL_PHASE = 1e-6      # eigenphase clustering (documented trap: LAPACK splits ~3e-8)
TOL_DIAG = 1e-7       # off-diagonality residual per commuting operator


def modinv(a, n):
    return pow(int(a) % n, -1, n)


def U_weil(B, N):
    """U(B)_{jk} = N^{-1/2} e_N( inv(2b) (a k^2 - 2jk + d j^2) ), odd N, gcd(b,N)=1."""
    a, b = int(B[0, 0]), int(B[0, 1])
    d = int(B[1, 1])
    if math.gcd(b, N) != 1:
        raise ValueError(f"b={b} not invertible mod N={N}")
    ib2 = modinv(2 * b, N)
    j = np.arange(N).reshape(-1, 1)
    k = np.arange(N).reshape(1, -1)
    expo = (ib2 * (a * k * k - 2 * j * k + d * j * j)) % N
    return np.exp(2j * np.pi * expo / N) / np.sqrt(N)


def hecke_units(A, N, count=4):
    """Norm-one units alpha*I + beta*A of Z[A]/N with invertible (0,1)-entry.

    det(aI + bA) = a^2 + t*ab + b^2  (t = tr A, det A = 1).
    Returns list of 2x2 integer matrices mod N, excluding scalar +/-I,
    preferring units that are NOT powers of A (checked by matrix power scan).
    Also returns the commutant order (#solutions) as a gate datum.
    """
    t = int(np.trace(A))
    a = np.arange(N).reshape(-1, 1)
    b = np.arange(N).reshape(1, -1)
    norm = (a * a + t * a * b + b * b) % N
    sols = np.argwhere(norm == 1 % N)
    order = len(sols)
    # powers of A mod N (to exclude, so the Hecke set adds information)
    powsA = set()
    P = np.eye(2, dtype=np.int64) % N
    Amod = A % N
    for _ in range(6 * N):
        key = tuple(P.flatten() % N)
        if key in powsA:
            break
        powsA.add(key)
        P = (P @ Amod) % N
    picked = []
    entry01 = int(A[0, 1])
    idx = rng.permutation(len(sols))
    for i in idx:
        aa, bb = int(sols[i][0]), int(sols[i][1])
        if bb == 0:                      # scalar (+/-I): skip
            continue
        if math.gcd((bb * entry01) % N, N) != 1:
            continue
        Bm = (aa * np.eye(2, dtype=np.int64) + bb * np.array(A, dtype=np.int64)) % N
        if tuple(Bm.flatten()) in powsA:
            continue
        picked.append(Bm)
        if len(picked) >= count:
            break
    return picked, order


def parity(N):
    P = np.zeros((N, N))
    for j in range(N):
        P[(-j) % N, j] = 1.0
    return P


def joint_eigenbasis(ops, N):
    """Joint eigenbasis of a commuting normal family via a random Hermitian combination.

    Returns (V, resid, mult_max): columns of V = basis; resid = max off-diagonal
    residual of each op in that basis; mult_max = max joint multiplicity
    (cluster size over the tuple of eigenvalues of all ops).
    """
    K = np.zeros((N, N), dtype=complex)
    for M in ops:
        g = rng.normal() + 1j * rng.normal()
        K += g * M + np.conj(g) * M.conj().T
    # K is Hermitian by construction
    K = (K + K.conj().T) / 2
    _, V = np.linalg.eigh(K)
    resid = 0.0
    diags = []
    for M in ops:
        Md = V.conj().T @ M @ V
        off = Md - np.diag(np.diag(Md))
        resid = max(resid, float(np.max(np.abs(off))))
        diags.append(np.diag(Md))
    # joint multiplicity: cluster the tuple of eigenvalues
    key = np.round(np.array(diags).T / TOL_PHASE) * TOL_PHASE
    _, counts = np.unique(np.round(key, 5), axis=0, return_counts=True)
    return V, resid, int(counts.max())


def moments_f(V, N):
    """Matrix-element moments of f = cos(2 pi x) over the eigenbasis columns of V."""
    fdiag = np.cos(2 * np.pi * np.arange(N) / N)
    X = np.einsum('jn,j,jn->n', V.conj(), fdiag, V).real
    m2 = float(np.mean(X ** 2))
    m4 = float(np.mean(X ** 4))
    return N * m2, (m4 / m2 ** 2 if m2 > 0 else float('nan')), X


def run_level(A, N, n_hecke=4, want_sff=False):
    """Full pipeline at one level. Returns a result dict."""
    t0 = time.time()
    U = U_weil(A % N, N)
    # gate: unitarity
    unit_err = float(np.max(np.abs(U @ U.conj().T - np.eye(N))))
    H, comm_order = hecke_units(A, N, count=n_hecke)
    P = parity(N)
    comm_err = 0.0
    for M in H + [P]:
        Mq = U_weil(M, N) if M.shape == (2, 2) else M
    # quantize hecke units
    HQ = [U_weil(M, N) for M in H]
    for M in HQ + [P]:
        comm_err = max(comm_err, float(np.max(np.abs(U @ M - M @ U))))
    ops = [U] + HQ + [P.astype(complex)]
    V, resid, mult = joint_eigenbasis(ops, N)
    nvar, kurt, X = moments_f(V, N)
    out = dict(N=N, trace=int(np.trace(A)), unitarity_err=unit_err,
               commutant_order=comm_order, commutator_err=comm_err,
               joint_diag_resid=resid, max_joint_mult=mult,
               NVar=nvar, kurtosis=kurt, seconds=round(time.time() - t0, 1))
    if want_sff:
        theta = np.angle(np.diag(V.conj().T @ U @ V))
        # eigenphase degeneracy profile (the Pisano launder-control)
        th_sorted = np.sort(np.mod(theta, 2 * np.pi))
        clusters = np.split(th_sorted, np.where(np.diff(th_sorted) > TOL_PHASE)[0] + 1)
        degs = sorted((len(c) for c in clusters), reverse=True)
        # ord(A mod N)
        Amod = A % N
        Pm = np.array(Amod)
        o = 1
        while not np.array_equal(Pm % N, np.eye(2, dtype=np.int64) % N):
            Pm = (Pm @ Amod) % N
            o += 1
            if o > 12 * N:
                o = -1
                break
        # SFF at integer times, untwisted + parity-resolved
        par = np.einsum('jn,j,jn->n', V.conj(), np.diag(parity(N)) * 0 + 1.0, V).real  # placeholder
        pdiag = np.diag(V.conj().T @ parity(N).astype(complex) @ V).real
        ts = list(range(1, min(3 * (o if o > 0 else N), 400) + 1))
        sff_u, sff_tw = [], []
        for t in ts:
            z = np.exp(1j * t * theta)
            sff_u.append(float(np.abs(z.sum()) ** 2) / N)
            sff_tw.append(float(np.abs((pdiag * z).sum()) ** 2) / N)
        out.update(ord_A_mod_N=o, top_degeneracies=degs[:6],
                   sff_t=ts, sff_untwisted=sff_u, sff_twisted=sff_tw,
                   parity_expect_minmax=[float(pdiag.min()), float(pdiag.max())])
    return out, X


def five_factor_exact():
    """The 5-dim factor: matrix elements of M5^u over the N=5 Hecke eigenbasis, all u.

    Returns the multiset E|Y|^2-average per unit u and the S5 constant
    S5 = 5 * mean_over_basis |<psi| (M5^u + M5^-u)/2 |psi>|^2  (Galois-checked over u).
    """
    N = 5
    U = U_weil(A_GOLD % N, N)
    H, order = hecke_units(A_GOLD, N, count=3)
    HQ = [U_weil(M, N) for M in H]
    P = parity(N).astype(complex)
    V, resid, mult = joint_eigenbasis([U] + HQ + [P], N)
    vals = {}
    for u in range(1, 5):
        fd = np.cos(2 * np.pi * u * np.arange(N) / N)
        X = np.einsum('jn,j,jn->n', V.conj(), fd, V).real
        vals[u] = dict(X=[round(float(x), 10) for x in X],
                       S5=float(5 * np.mean(X ** 2)),
                       K5=float(np.mean(X ** 4) / np.mean(X ** 2) ** 2))
    return vals, resid, mult


def main():
    results = dict(meta=dict(date="2026-07-07", probe="B446",
                             prereg="PREREGISTRATION.md", pilot_trusted=False))

    print("=" * 72)
    print("B446 D1 — GATES (prime N; KR targets N*Var -> 1.00, m4/m2^2 -> 2.00)")
    print("=" * 72)
    gates = []
    for N in [241, 1201, 2003]:
        r, _ = run_level(A_GOLD, N)
        gates.append(r)
        print(f"  N={N:5d}: N*Var={r['NVar']:.4f} kurt={r['kurtosis']:.3f} "
              f"unit={r['unitarity_err']:.1e} comm={r['commutator_err']:.1e} "
              f"resid={r['joint_diag_resid']:.1e} mult={r['max_joint_mult']} "
              f"#commutant={r['commutant_order']} ({r['seconds']}s)")
    results['gates_prime_gold'] = gates

    print("\n" + "=" * 72)
    print("B446 D1 — THE 5-DIM FACTOR (exact anchor for the product law)")
    print("=" * 72)
    five, resid5, mult5 = five_factor_exact()
    for u, d in five.items():
        print(f"  u={u}: X={d['X']}  S5={d['S5']:.6f}  K5={d['K5']:.4f}")
    results['five_factor'] = five

    print("\n" + "=" * 72)
    print("B446 D1 — PURE 3-POWER CONSTANT C3")
    print("=" * 72)
    c3 = []
    for N in [243, 729]:
        r, _ = run_level(A_GOLD, N)
        c3.append(r)
        print(f"  N={N:5d}: N*Var={r['NVar']:.4f} kurt={r['kurtosis']:.3f} "
              f"mult={r['max_joint_mult']} ({r['seconds']}s)")
    results['pure3_gold'] = c3

    print("\n" + "=" * 72)
    print("B446 D1 — THE TOWER N = 15*3^k (with SFF at 45/135/405)")
    print("=" * 72)
    tower = []
    for N in [15, 45, 135, 405, 1215]:
        r, _ = run_level(A_GOLD, N, want_sff=(N in (45, 135, 405)))
        tower.append(r)
        extra = ""
        if 'ord_A_mod_N' in r:
            extra = f" ord(A)={r['ord_A_mod_N']} degs={r['top_degeneracies']}"
        print(f"  N={N:5d}: N*Var={r['NVar']:.4f} kurt={r['kurtosis']:.3f} "
              f"mult={r['max_joint_mult']}{extra} ({r['seconds']}s)")
    results['tower_gold'] = tower

    print("\n" + "=" * 72)
    print("B446 D1 — SILVER CONTROL A2=[[5,2],[2,1]] (primes + 3-power tower)")
    print("=" * 72)
    silver = []
    for N in [241, 1201, 45, 135, 405]:
        r, _ = run_level(A_SILV, N)
        silver.append(r)
        print(f"  N={N:5d}: N*Var={r['NVar']:.4f} kurt={r['kurtosis']:.3f} "
              f"mult={r['max_joint_mult']} ({r['seconds']}s)")
    results['silver'] = silver

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=1)
    print("\n[results.json written]")


if __name__ == '__main__':
    main()
