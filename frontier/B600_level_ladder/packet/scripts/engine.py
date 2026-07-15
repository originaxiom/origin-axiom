"""CC2-LL engine — generic-level E6 modular data + figure-eight monodromy readouts.

Conventions locked verbatim to the banked pipeline (B570-C3 / B578-D7):
  - PRIM enumeration order = lexicographic nested loops over Dynkin labels
    (tests/test_b578_level3.py::enumerate_level_weights);
  - rho(A1) = T^2 S T, two-word gate vs T S T^-1 S^-1 (the B569 lesson);
  - theta = diagram flip (1<->6, 3<->5); odd basis (e_a - e_b)/sqrt(2) over
    theta-pairs in first-appearance order;
  - S normalized S/sqrt((S S^dag)_00), sign fixed S_00 > 0.

Two pipelines, cross-gated:
  FLOAT : the banked einsum build (complex128).
  EXACT : unnormalized U_ab = sum_w eps(w) zeta_{6K}^{e(w,a,b)} with INTEGER
          exponents e = (-2/3)(W P_a, C P_b) mod 6K (integrality asserted),
          stored as integer count vectors of length 6K. All downstream
          precision (float64, mpmath dps>=50) is EVALUATED FROM THE COUNTS,
          so every readout carries an exact-integer certificate behind it.

Usage:
  engine.py gates    -> P0: validate k=1,2,3 against banked values (hard stop on mismatch)
  engine.py level4   -> P2: run k=4 blind, bank outputs/level4_readouts.json (no comparison)
"""
import json
import sys
from fractions import Fraction

import mpmath as mp
import numpy as np

C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
MARKS = [1, 2, 2, 3, 2, 1]          # comarks of E6 (simply-laced)
HVEE = 12
DIMG = 78
Cinv3 = np.rint(3 * np.linalg.inv(C6)).astype(np.int64)   # 3 * C^-1 is integral for E6
assert np.array_equal(Cinv3 @ C6, 3 * np.eye(6, dtype=np.int64))
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])


def enumerate_level_weights(level):
    weights = []
    bounds = [level // m + 1 for m in MARKS]
    for l0 in range(bounds[0]):
        for l1 in range(bounds[1]):
            for l2 in range(bounds[2]):
                for l3 in range(bounds[3]):
                    for l4 in range(bounds[4]):
                        for l5 in range(bounds[5]):
                            lab = (l0, l1, l2, l3, l4, l5)
                            if sum(m * x for m, x in zip(MARKS, lab)) <= level:
                                weights.append(lab)
    return weights


def weyl_group():
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes()}
    mats, signs = [I], [1]
    frontier = [(I, 1)]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs, dtype=np.int64)


def positive_roots():
    """All 72 roots of E6 in the root basis via reflection closure; 36 positive."""
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    roots = {tuple(r) for r in np.eye(6, dtype=np.int64)}
    frontier = list(roots)
    while frontier:
        new = []
        for r in frontier:
            for g in gens:
                rr = tuple(np.array(r) @ g.T)
                if rr not in roots:
                    roots.add(rr)
                    new.append(rr)
        frontier = new
    assert len(roots) == 72
    pos = [np.array(r) for r in roots if all(x >= 0 for x in r)]
    assert len(pos) == 36
    return pos


def theta_split(PRIM):
    fixed_idx = [i for i, p in enumerate(PRIM) if theta(p) == p]
    pairs, used = [], set()
    for i, p in enumerate(PRIM):
        if i in used or theta(p) == p:
            continue
        j = PRIM.index(theta(p))
        pairs.append((i, j)); used.add(i); used.add(j)
    return fixed_idx, pairs


class Level:
    """E6 level-k modular data, exact-counts pipeline + float cross-check."""

    def __init__(self, level, W, eps):
        self.k = level
        self.K = level + HVEE
        self.M6 = 6 * self.K                       # zeta order for S
        self.PRIM = enumerate_level_weights(level)
        self.N = len(self.PRIM)
        self.fixed_idx, self.pairs = theta_split(self.PRIM)
        self.W, self.eps = W, eps

        # --- EXACT S: integer exponent counts over zeta_{6K} ---
        P = (Cinv3 @ (np.array(self.PRIM, dtype=np.int64) + 1).T).T   # 3*(lambda+rho), int
        WP = np.einsum('wij,aj->wai', self.W, P)                      # 3*w(lambda+rho)
        CP = C6 @ P.T                                                 # 6 x N
        counts = np.zeros((self.N, self.N, self.M6), dtype=np.int64)
        for a in range(self.N):
            Q = WP[:, a, :] @ CP                                      # (|W|, N) integer
            assert (Q % 3 == 0).all(), "exponent integrality failed"
            E = (-2 * (Q // 3)) % self.M6
            for b in range(a, self.N):
                cp = np.bincount(E[self.eps > 0, b], minlength=self.M6)
                cm = np.bincount(E[self.eps < 0, b], minlength=self.M6)
                counts[a, b] = counts[b, a] = cp - cm
        self.counts = counts

        # --- T: exact integer exponents over zeta_{12K} ---
        # h_a = (lam, lam+2rho)/(2K) = r_a/(6K) with r_a = 3*(lam, lam+2rho) integer;
        # T_a = zeta_{12K}^(2 r_a - 117 k)  [c/24 = 13k/(4K) = 117k/(12K)... x12K = 39k*... ]
        lam3 = (Cinv3 @ np.array(self.PRIM, dtype=np.int64).T).T      # 3*lambda
        rho3 = Cinv3 @ np.ones(6, dtype=np.int64)                     # 3*rho
        r = np.array([int((la @ C6 @ (la + 2 * rho3))) for la in lam3])
        assert (r % 3 == 0).all()
        self.r = r // 3                                               # 3*(lam,lam+2rho)
        ck_num = 39 * self.k                                          # 12K * c/24 = 39k/... checked below
        # c/24 = k*78/(24K) = 13k/(4K); *12K = 39k  -> integer exponent
        self.T_expo = (2 * self.r - ck_num) % (12 * self.K)           # zeta_{12K} exponents

    # ---------- evaluation from exact counts ----------
    def S_float(self):
        z = np.exp(2j * np.pi * np.arange(self.M6) / self.M6)
        U = self.counts @ z
        norm = np.sqrt((U @ U.conj().T)[0, 0].real)
        S = U / norm
        if S[0, 0].real < 0:
            S = -S
        return S

    def S_banked_style(self):
        """The banked float einsum build (independent of the counts) — cross-gate."""
        Cf = C6.astype(float)
        rho_w = np.linalg.inv(Cf) @ np.ones(6)
        shifted = [np.linalg.inv(Cf) @ np.array(p, dtype=float) + rho_w for p in self.PRIM]
        S = np.zeros((self.N, self.N), dtype=complex)
        Wl = np.einsum('wij,lj->wli', self.W.astype(float), np.array(shifted))
        for a in range(self.N):
            for b in range(a, self.N):
                ips = Wl[:, a, :] @ (Cf @ shifted[b])
                S[a, b] = S[b, a] = np.sum(self.eps * np.exp(-2j * np.pi * ips / self.K))
        norm = np.sqrt((S @ S.conj().T)[0, 0].real)
        S = S / norm
        if S[0, 0].real < 0:
            S = -S
        return S

    def T_float(self):
        return np.diag(np.exp(2j * np.pi * self.T_expo / (12 * self.K)))

    def S_mp(self, dps=50):
        mp.mp.dps = dps
        zpow = [mp.e ** (2j * mp.pi * j / self.M6) for j in range(self.M6)]
        U = mp.matrix(self.N, self.N)
        for a in range(self.N):
            for b in range(self.N):
                U[a, b] = mp.fsum(int(c) * zpow[j] for j, c in enumerate(self.counts[a, b]) if c)
        n2 = mp.fsum((U[0, b] * mp.conj(U[0, b])).real for b in range(self.N))
        norm = mp.sqrt(n2)
        S = U / norm
        if mp.re(S[0, 0]) < 0:
            S = -S
        return S

    def T_mp(self, dps=50):
        mp.mp.dps = dps
        return mp.diag([mp.e ** (2j * mp.pi * int(e) / (12 * self.K)) for e in self.T_expo])

    # ---------- gates ----------
    def run_gates(self, tol=1e-8):
        S, T = self.S_float(), self.T_float()
        N = self.N
        rep = {}
        rep['float_vs_exactcounts'] = float(np.linalg.norm(S - self.S_banked_style()))
        rep['unitary'] = float(np.linalg.norm(S @ S.conj().T - np.eye(N)))
        rep['symmetric'] = float(np.linalg.norm(S - S.T))
        C2 = S @ S
        rep['(ST)^3=S^2'] = float(np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2))
        rep['S^4=I'] = float(np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(N)))
        # S^2 must be the theta-flip permutation
        expect = np.zeros((N, N))
        for i, p in enumerate(self.PRIM):
            expect[self.PRIM.index(theta(p)), i] = 1
        rep['S^2=theta-perm'] = float(np.linalg.norm(C2 - expect))
        # Verlinde integrality
        d0 = S[0]
        Nv = np.einsum('am,bm,cm->abc', S, S, S.conj() / d0)
        rep['verlinde_int_dev'] = float(np.max(np.abs(Nv - np.rint(Nv.real))))
        rep['verlinde_min'] = float(np.min(np.rint(Nv.real)))
        # q-dim independent cross-check
        pos = positive_roots()
        Cf = C6.astype(float)
        rho_w = np.linalg.inv(Cf) @ np.ones(6)
        qd = []
        for p in self.PRIM:
            lam = np.linalg.inv(Cf) @ np.array(p, dtype=float)
            num = den = 1.0
            for al in pos:
                alf = al.astype(float)
                num *= np.sin(np.pi * float((lam + rho_w) @ Cf @ alf) / self.K)
                den *= np.sin(np.pi * float(rho_w @ Cf @ alf) / self.K)
            qd.append(num / den)
        rep['qdim_dev'] = float(np.max(np.abs(np.array(qd) - (S[0] / S[0, 0]).real)))
        # two-word monodromy
        w1 = T @ T @ S @ T
        w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
        rep['two_word'] = float(np.linalg.norm(w1 - w2))
        rep['rho_unitary'] = float(np.linalg.norm(w1 @ w1.conj().T - np.eye(N)))
        ok = all(v < tol for k_, v in rep.items() if k_ not in ('verlinde_min',)) and rep['verlinde_min'] >= 0
        return rep, ok, S, T, w1

    # ---------- readouts ----------
    def readouts(self, S, rho):
        n_odd = len(self.pairs)
        odd = np.zeros((self.N, n_odd))
        for j, (a, b) in enumerate(self.pairs):
            odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        S_odd = odd.T @ S @ odd
        B_odd = odd.T @ rho @ odd
        out = {}
        out['N'] = self.N
        out['n_theta_fixed'] = len(self.fixed_idx)
        out['dim_odd'] = n_odd
        Z = np.trace(rho)
        out['Z'] = [float(Z.real), float(Z.imag)]
        out['tr_odd'] = [float(np.trace(B_odd).real), float(np.trace(B_odd).imag)]
        out['off_block_norm'] = float(np.linalg.norm(rho - (odd @ B_odd @ odd.T +
                                     (np.eye(self.N) - odd @ odd.T) @ rho @ (np.eye(self.N) - odd @ odd.T))))
        out['S_odd_sq_plus_I'] = float(np.linalg.norm(S_odd @ S_odd + np.eye(n_odd)))
        out['B_odd_nonscalar'] = float(np.linalg.norm(B_odd - B_odd[0, 0] * np.eye(n_odd)))
        # order by matrix powers (float scan, generous ceiling)
        order = None
        P = np.eye(n_odd, dtype=complex)
        for m in range(1, 20001):
            P = P @ B_odd
            if np.linalg.norm(P - np.eye(n_odd)) < 1e-6:
                order = m
                break
        out['order_float'] = order
        # distinct |S_odd| magnitudes, banked-style dedupe, scaled by 2K
        mags = np.abs(S_odd)
        vals = sorted(set(round(v, 8) for row in mags for v in row if v > 1e-6))
        out['n_distinct_mags'] = len(vals)
        out['ws_2K'] = [2 * self.K * v ** 2 for v in vals]
        return out, S_odd, B_odd


def mp_odd_blocks(L, dps=50):
    """S_odd and B_odd at dps digits, evaluated FROM THE EXACT COUNTS."""
    mp.mp.dps = dps
    S = L.S_mp(dps)
    T = L.T_mp(dps)
    rho = T * T * S * T
    n_odd = len(L.pairs)
    odd = mp.matrix(L.N, n_odd)
    s2 = 1 / mp.sqrt(2)
    for j, (a, b) in enumerate(L.pairs):
        odd[a, j], odd[b, j] = s2, -s2
    S_odd = odd.T * S * odd
    B_odd = odd.T * rho * odd
    return S_odd, B_odd, rho


def mp_magnitude_poly(L, S_odd, dps=50, max_scale_pow3=8):
    """Distinct |S_odd| magnitudes at dps digits -> ws = 2K*|.|^2 -> the exact
    integer polynomial D * prod(w - w_i), with D the minimal power of 3."""
    mp.mp.dps = dps
    n = S_odd.rows
    vals = []
    for i in range(n):
        for j in range(n):
            m = mp.sqrt((S_odd[i, j] * mp.conj(S_odd[i, j])).real)
            if m > mp.mpf('1e-30'):
                if not any(abs(m - v) < mp.mpf('1e-30') for v in vals):
                    vals.append(m)
    ws = sorted(2 * L.K * v ** 2 for v in vals)
    coeffs = [mp.mpf(1)]
    for wv in ws:
        new = [mp.mpf(0)] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            new[i] += c
            new[i + 1] -= c * wv
        coeffs = new
    for p3 in range(max_scale_pow3 + 1):
        D = 3 ** p3
        ints = [mp.nint(D * c) for c in coeffs]
        if all(abs(D * c - iv) < mp.mpf('1e-25') for c, iv in zip(coeffs, ints)):
            return [int(iv) for iv in ints], D, [str(w) for w in ws]
    return None, None, [str(w) for w in ws]


def mp_certify_order(B_odd, order, dps=50):
    """Certify ord(B_odd) = order at dps digits: ||B^order - I|| < 1e-(dps-10),
    and ||B^d - I|| >> 0 for every maximal proper divisor d."""
    mp.mp.dps = dps
    n = B_odd.rows
    I = mp.eye(n)

    def matpow(M, e):
        R = mp.eye(n)
        base = M.copy()
        while e:
            if e & 1:
                R = R * base
            base = base * base
            e >>= 1
        return R

    def dev(M):
        return max(abs(M[i, j] - I[i, j]) for i in range(n) for j in range(n))

    d_ord = dev(matpow(B_odd, order))
    proper = []
    for p in set(factorint_small(order)):
        proper.append(order // p)
    d_props = {d: float(dev(matpow(B_odd, d))) for d in proper}
    return float(d_ord), d_props


def factorint_small(n):
    fs, d = [], 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d); n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'gates'
    print("building W(E6)...", flush=True)
    W, eps = weyl_group()
    assert len(W) == 51840
    print("|W(E6)| = 51840 (exact)")

    if mode == 'gates':
        # ---- banked targets: k=1 (B569), k=2 (B570-C3), k=3 (B578-D7) ----
        expected = {
            1: dict(N=3, dim_odd=1, order=1, Z=1.0),
            2: dict(N=9, dim_odd=3, order=4, Z=1.0,
                    eig_odd={1: 1, 1j: 1, -1j: 1}),
            3: dict(N=20, dim_odd=8, order=60, Z=1.0,
                    octic=[81, -2430, 29160, -181800, 640800, -1296000,
                           1448000, -800000, 160000]),
        }
        for k in (1, 2, 3):
            print(f"\n===== LEVEL {k} (K = {k+HVEE}) =====")
            L = Level(k, W, eps)
            rep, ok, S, T, rho = L.run_gates()
            for kk, v in rep.items():
                print(f"  gate {kk}: {v:.3e}" if isinstance(v, float) else f"  gate {kk}: {v}")
            assert ok, f"GATE FAILURE at level {k} — HARD STOP (B569 lesson)"
            out, S_odd, B_odd = L.readouts(S, rho)
            e = expected[k]
            assert out['N'] == e['N'] and out['dim_odd'] == e['dim_odd'], (out, e)
            assert abs(out['Z'][0] - e['Z']) < 1e-8 and abs(out['Z'][1]) < 1e-8
            assert (out['order_float'] or 1) == e['order'], out['order_float']
            print(f"  N={out['N']}, dim_odd={out['dim_odd']}, Z={out['Z'][0]:+.10f}, "
                  f"order(B_odd)={out['order_float']}, tr_odd={out['tr_odd'][0]:+.6f}")
            if k == 3:
                assert out['n_distinct_mags'] == 8
                S_odd_mp, B_odd_mp, _ = mp_odd_blocks(L, dps=50)
                ints, D, ws50 = mp_magnitude_poly(L, S_odd_mp, dps=50)
                print(f"  octic gate (dps50 from exact counts): D = {D}, poly = {ints}")
                assert ints == e['octic'], "OCTIC MISMATCH — HARD STOP"
                d_ord, d_props = mp_certify_order(B_odd_mp, 60, dps=50)
                print(f"  order-60 certificate: ||B^60-I|| = {d_ord:.1e}; "
                      f"proper divisors dev = { {d: f'{v:.2e}' for d, v in d_props.items()} }")
                assert d_ord < 1e-40 and all(v > 1e-3 for v in d_props.values())
        print("\nALL P0 GATES GREEN — the engine reproduces the banked ladder exactly.")

    elif mode == 'level4':
        k = 4
        print(f"\n===== LEVEL {k} (K = 16) — BLIND RUN, banking to outputs/ =====")
        L = Level(k, W, eps)
        rep, ok, S, T, rho = L.run_gates()
        for kk, v in rep.items():
            print(f"  gate {kk}: {v:.3e}" if isinstance(v, float) else f"  gate {kk}: {v}")
        assert ok, "GATE FAILURE at level 4 — HARD STOP"
        out, S_odd, B_odd = L.readouts(S, rho)
        np.savez('outputs/level4_blocks.npz', S_odd=S_odd, B_odd=B_odd,
                 counts=L.counts, T_expo=L.T_expo)
        with open('outputs/level4_readouts.json', 'w') as f:
            json.dump(out, f, indent=1)
        print(json.dumps(out, indent=1))
        print("BANKED to outputs/level4_readouts.json — comparison to P1 happens in a separate step.")


if __name__ == '__main__':
    main()
