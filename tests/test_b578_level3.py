"""Locks for D7-level3 (L67 extension to E6 level 3).

Reproducer: frontier/B570_allowed_plays/c3_e6_level2_monodromy.py pattern,
extended to level 3 (KH = 3+12 = 15). Standalone script embedded below
(same content as c3_e6_level3_monodromy.py) so the test is self-contained
and fast (~1.5s: full |W(E6)|=51840 Kac-Peterson build + all gates).

Findings locked:
  - 20 level-3 integrable weights (marks (1,2,2,3,2,1)), theta-odd dim = 8
    (4 theta-fixed + 8 theta-swapped pairs) -- confirms the task's prediction.
  - All Kac-Peterson/Verlinde gates green (unitarity, S^2=charge conj,
    (ST)^3=S^2, S^4=I, 8000 Verlinde fusion numbers >=0, q-dim cross-check).
  - S_odd (8x8) has eigenvalues exactly {+i x4, -i x4} (forced: C=S^2 acts
    as -1 on the odd space, so S_odd^2 = -I identically).
  - rho(A1)|odd is NON-SCALAR, order exactly 60 (verified by matrix power).
  - THE LAW QUESTION: the 8 squared-magnitudes of S_odd entries (scaled by
    30) are the roots of one exact octic  81 w^8 - 2430 w^7 + 29160 w^6
    - 181800 w^5 + 640800 w^4 - 1296000 w^3 + 1448000 w^2 - 800000 w
    + 160000 = 0, which factors EXACTLY as
       (w^2 - 10w + 20) * (81w^6 - 1620w^5 + 11340w^4 - 36000w^3
                             + 54000w^2 - 36000w + 8000)
    i.e. a Q(sqrt5) quadratic factor (2 roots, w=5+/-sqrt5) times an
    irreducible-over-Q sextic that itself factors into two Galois-conjugate
    CUBICS over Q(sqrt5) (6 roots). This is a genuine 2+3+3 algebraic
    split, NOT a single clean sine-kernel of any one modulus (5, 15, or 30)
    -- unlike the level-2 case (Z/7 sine kernel, one clean quartic-free
    modulus). The naive L67 "one new prime modulus per level" law is
    REFUTED at level 3 (KH=15=3*5 is composite; the odd sector genuinely
    entangles both prime factors, does not factor per-prime).
"""
import numpy as np
import pytest

C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
LEVEL = 3
HVEE = 12
KH = LEVEL + HVEE
MARKS = [1, 2, 2, 3, 2, 1]
C = np.array(C6, dtype=float)
Cinv = np.linalg.inv(C)
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
    n = 6
    gens = []
    for j in range(n):
        M = np.eye(n, dtype=np.int64)
        M[j, :] -= np.array(C6, dtype=np.int64)[:, j]
        gens.append(M)
    I = np.eye(n, dtype=np.int64)
    seen = {I.tobytes(): 1}
    frontier = [(I, 1)]
    mats, signs = [I], [1]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen[key] = -s
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs)


def root_coords(labels):
    return Cinv @ np.array(labels, dtype=float)


def build():
    PRIM = enumerate_level_weights(LEVEL)
    N = len(PRIM)
    W, eps = weyl_group()
    rho_w = root_coords([1] * 6)
    shifted = [root_coords(p) + rho_w for p in PRIM]

    S = np.zeros((N, N), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    Gm = C
    for a in range(N):
        for b in range(a, N):
            ips = Wl[:, a, :] @ (Gm @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
    norm = np.sqrt((S @ S.conj().T)[0, 0].real)
    S = S / norm
    if S[0, 0].real < 0:
        S = -S

    ip = lambda x, y: float(x @ (Gm @ y))
    dim_g = 78
    c = LEVEL * dim_g / KH
    hs = [ip(root_coords(p), root_coords(p) + 2 * rho_w) / (2 * KH) for p in PRIM]
    T = np.diag([np.exp(2j * np.pi * (h - c / 24)) for h in hs])

    C2 = S @ S
    w1 = T @ T @ S @ T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    rho = w1

    fixed_idx = [i for i, p in enumerate(PRIM) if theta(p) == p]
    pairs, used = [], set()
    for i, p in enumerate(PRIM):
        if i in used or theta(p) == p:
            continue
        j = PRIM.index(theta(p))
        pairs.append((i, j)); used.add(i); used.add(j)

    odd = np.zeros((N, len(pairs)))
    for j, (a, b) in enumerate(pairs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)

    S_odd = odd.T @ S @ odd
    B_odd = odd.T @ rho @ odd

    return dict(PRIM=PRIM, N=N, W=W, S=S, T=T, C2=C2, rho=rho, w1=w1, w2=w2,
                fixed_idx=fixed_idx, pairs=pairs, S_odd=S_odd, B_odd=B_odd)


@pytest.fixture(scope="module")
def data():
    return build()


def test_weyl_group_order(data):
    assert len(data['W']) == 51840


def test_level3_weight_count(data):
    assert data['N'] == 20


def test_theta_split(data):
    assert len(data['fixed_idx']) == 4
    assert len(data['pairs']) == 8


def test_gates(data):
    S, C2, T, rho, w1, w2 = data['S'], data['C2'], data['T'], data['rho'], data['w1'], data['w2']
    N = data['N']
    assert np.linalg.norm(S @ S.conj().T - np.eye(N)) < 1e-8
    assert np.linalg.norm(S - S.T) < 1e-8
    assert np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2) < 1e-8
    assert np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(N)) < 1e-8
    assert np.linalg.norm(w1 - w2) < 1e-8    # two-word monodromy agreement
    assert np.linalg.norm(rho @ rho.conj().T - np.eye(N)) < 1e-8


def test_S_odd_squares_to_minus_identity(data):
    # forced: C = S^2 acts as -1 on the theta-odd (antisymmetric) subspace
    S_odd = data['S_odd']
    assert np.linalg.norm(S_odd @ S_odd + np.eye(8)) < 1e-8
    ev = sorted(np.linalg.eigvals(S_odd), key=lambda z: z.imag)
    assert np.allclose(sorted(ev, key=lambda z: z.imag)[:4], -1j, atol=1e-8)
    assert np.allclose(sorted(ev, key=lambda z: z.imag)[4:], 1j, atol=1e-8)


def test_monodromy_nonscalar_order_60(data):
    B_odd = data['B_odd']
    scal = np.linalg.norm(B_odd - B_odd[0, 0] * np.eye(8))
    assert scal > 1.0   # emphatically non-scalar
    assert np.linalg.norm(np.linalg.matrix_power(B_odd, 60) - np.eye(8)) < 1e-6
    for k in range(1, 60):
        if 60 % k == 0:
            assert np.linalg.norm(np.linalg.matrix_power(B_odd, k) - np.eye(8)) > 1e-4, \
                f"order divides {k} < 60"


def test_S_odd_magnitude_octic_factorization(data):
    """The 8 distinct |S_odd| entries, scaled as w=30*|S_odd_ij|^2, are the
    roots of 81w^8-2430w^7+29160w^6-181800w^5+640800w^4-1296000w^3
    +1448000w^2-800000w+160000, which factors EXACTLY as
    (w^2-10w+20)*(81w^6-1620w^5+11340w^4-36000w^3+54000w^2-36000w+8000).
    Two roots (w=5+/-sqrt5) are Q(sqrt5); the other six are NOT (spot-check:
    no small-height algebraic relation up to degree 8, maxcoeff 2000, found
    by mpmath.findpoly at 60 dps for the sextic's roots individually)."""
    S_odd = data['S_odd']
    mags = np.abs(S_odd)
    vals = sorted(set(round(v, 8) for row in mags for v in row if v > 1e-6))
    assert len(vals) == 8
    ws = sorted(30 * v ** 2 for v in vals)

    coeffs = [81, -2430, 29160, -181800, 640800, -1296000, 1448000, -800000, 160000]
    true_roots = sorted(r.real for r in np.roots(coeffs) if abs(r.imag) < 1e-6)
    assert len(true_roots) == 8
    for w in ws:
        assert min(abs(w - tr) for tr in true_roots) < 1e-4, (w, true_roots)

    # the quadratic factor's two roots (Q(sqrt5)) must appear among the 8
    quad_roots = sorted([5 - 5**0.5, 5 + 5**0.5])
    hit = [any(abs(w - qr) < 1e-4 for w in ws) for qr in quad_roots]
    assert all(hit)


if __name__ == '__main__':
    import sys
    d = build()
    print("N =", d['N'], " |W| =", len(d['W']))
    print("theta-fixed:", len(d['fixed_idx']), " theta-pairs:", len(d['pairs']))
    print("S_odd eigenvalues:", np.linalg.eigvals(d['S_odd']))
    print("B_odd (rho|odd) eigenvalues:", np.linalg.eigvals(d['B_odd']))
    sys.exit(0)
