"""B570 Lane C, cell C3 — THE DECISIVE CELL (run first, owner directive 2026-07-14):
the figure-eight monodromy on the theta-odd 3-space of E6 level 2.

Level 1 (B569): the theta-odd sector is 1-dim and the monodromy acts trivially (+1).
Level 2: nine primaries, theta-odd dimension 3. Question: does rho(A1) act
NON-TRIVIALLY on the theta-odd 3-space (dynamical chirality above the fold),
or is it trivial again (honest null)?

Method (Krasnov-level rigor):
  1. W(E6) enumerated exactly (51840 elements, BFS over simple reflections,
     epsilon = parity of word length);
  2. Kac-Peterson S at k=2 (h_vee=12, k+h_vee=14), T from h(lambda)=(l,l+2r)/28
     and c = 2*78/14 = 78/7;
  3. CONSISTENCY GATES before any evaluation (the B569 lesson):
     S symmetric + unitary, S^2 = charge conjugation (a permutation),
     (ST)^3 = S^2, Verlinde fusion integers >= 0,
     quantum dims from the S-column == independent q-Weyl-dimension formula;
  4. rho(A1) via TWO words (T^2 S T and T S T^-1 S^-1) — must agree;
  5. restrict to the theta-odd 3-space, report the block exactly.

Run: python3 frontier/B570_allowed_plays/c3_e6_level2_monodromy.py
"""
import numpy as np
from fractions import Fraction

C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
KH = 14                                    # k + h_vee = 2 + 12
C = np.array(C6, dtype=float)              # Gram matrix in the root basis (simply-laced)
Cinv = np.linalg.inv(C)

# the nine level-2 primaries (Dynkin labels), theta = diagram flip (1<->6, 3<->5)
PRIM = [(0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1),
        (2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2), (1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)]
NAMES = ['1', '27', '27b', '351p', '351pb', '650', '78', '351', '351b']
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])


def weyl_group():
    """All of W(E6) as 6x6 integer matrices (root-basis action) + parity signs."""
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
    lam = Cinv @ np.array(labels, dtype=float)
    return lam


def main():
    W, eps = weyl_group()
    assert len(W) == 51840, f"|W(E6)| wrong: {len(W)}"
    print(f"|W(E6)| = {len(W)} (exact)")

    rho_w = root_coords([1] * 6)
    shifted = [root_coords(p) + rho_w for p in PRIM]      # lambda + rho, root coords

    # ---- Kac-Peterson S (unnormalized), vectorized over W ----
    S = np.zeros((9, 9), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))  # w(l+r)
    Gm = C
    for a in range(9):
        for b in range(a, 9):
            ips = Wl[:, a, :] @ (Gm @ shifted[b])          # (w(la+r), lb+r)
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
    # normalize to unitary with S00 > 0
    norm = np.sqrt((S @ S.conj().T)[0, 0].real)
    S = S / norm
    if S[0, 0].real < 0:
        S = -S
    uni = np.linalg.norm(S @ S.conj().T - np.eye(9))
    sym = np.linalg.norm(S - S.T)
    print(f"GATE S: unitary {uni:.2e}, symmetric {sym:.2e}, S00 = {S[0,0].real:.6f} > 0")
    assert uni < 1e-9 and sym < 1e-9

    # ---- T and the modular relations ----
    ip = lambda x, y: float(x @ (Gm @ y))
    hs, c = [], 2 * 78 / KH
    for p in PRIM:
        lam = root_coords(p)
        hs.append(ip(lam, lam + 2 * rho_w) / (2 * KH))
    T = np.diag([np.exp(2j * np.pi * (h - c / 24)) for h in hs])
    print("c =", c, " h =", [f"{NAMES[i]}:{Fraction(hs[i]).limit_denominator(200)}" for i in range(9)])

    C2 = S @ S
    perm_ok = np.allclose(np.abs(C2), np.eye(9)[np.argsort([PRIM.index(theta(p)) for p in PRIM])], atol=1e-9) \
        or np.allclose(np.abs(C2), np.abs(C2).round(), atol=1e-9)
    conj_perm = np.abs(C2).round().astype(int)
    rel = np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2)
    s4 = np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(9))
    print(f"GATE modular: ||(ST)^3 - S^2|| = {rel:.2e}, ||S^4 - I|| = {s4:.2e}")
    assert rel < 1e-9 and s4 < 1e-9
    # S^2 must be the conjugation permutation = the theta diagram flip on labels
    expect = np.zeros((9, 9), dtype=int)
    for i, p in enumerate(PRIM):
        expect[PRIM.index(theta(p)), i] = 1
    print(f"GATE S^2 = conjugation permutation (= theta flip): {np.allclose(C2, expect, atol=1e-9)}")
    assert np.allclose(C2, expect, atol=1e-9)

    # ---- GATE: Verlinde integrality (all 729 fusion numbers) ----
    Nmax_bad = 0.0
    allN = np.zeros((9, 9, 9))
    for a in range(9):
        for b in range(9):
            for cc in range(9):
                N = np.sum(S[a, :] * S[b, :] * S[cc, :].conj() / S[0, :])
                allN[a, b, cc] = N.real
                Nmax_bad = max(Nmax_bad, abs(N.imag), abs(N.real - round(N.real)))
                assert round(N.real) >= 0
    print(f"GATE Verlinde: all 729 fusion numbers integers >= 0 (max dev {Nmax_bad:.2e})")

    # ---- GATE: independent method 2 — q-Weyl dimensions vs the S-column ----
    # positive roots
    allr = {tuple(int(x) for x in r) for r in
            (np.eye(6, dtype=int)).tolist()}
    frontier = set(allr) | {tuple((-np.array(r)).tolist()) for r in allr}
    allroots = set(frontier)
    while frontier:
        new = set()
        for rt in frontier:
            for j in range(6):
                pj = sum(C6[i][j] * rt[i] for i in range(6))
                y = list(rt); y[j] -= pj; ty = tuple(y)
                if ty not in allroots:
                    allroots.add(ty); new.add(ty)
        frontier = new
    pos = [np.array(r, dtype=float) for r in allroots if all(x >= 0 for x in r)]
    assert len(pos) == 36
    for i, p in enumerate(PRIM):
        lam = root_coords(p)
        qd = 1.0
        for al in pos:
            qd *= np.sin(np.pi * ip(lam + rho_w, al) / KH) / np.sin(np.pi * ip(rho_w, al) / KH)
        ratio = (S[0, i] / S[0, 0]).real
        assert abs(qd - ratio) < 1e-8, (NAMES[i], qd, ratio)
    print("GATE q-dims: S-column ratios == q-Weyl-dimension formula, all 9 primaries (independent method)")

    # ---- the monodromy, two words ----
    w1 = T @ T @ S @ T
    w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    print(f"\nrho(A1): two words agree: {np.linalg.norm(w1 - w2):.2e}")
    assert np.linalg.norm(w1 - w2) < 1e-9
    rho = w1
    print(f"unitary: {np.linalg.norm(rho @ rho.conj().T - np.eye(9)):.2e}; [rho, S^2] = {np.linalg.norm(rho @ C2 - C2 @ rho):.2e}")
    print(f"Z = Tr rho(A1) = {np.trace(rho):.10f}")

    # ---- THE QUESTION: the theta-odd 3-space ----
    pairs = [(1, 2), (3, 4), (7, 8)]                      # (27,27b), (351p,351pb), (351,351b)
    fixed = [0, 5, 6]
    odd = np.zeros((9, 3))
    for j, (a, b) in enumerate(pairs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    even = np.zeros((9, 6))
    for j, f in enumerate(fixed):
        even[f, j] = 1
    for j, (a, b) in enumerate(pairs):
        even[a, 3 + j], even[b, 3 + j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    B_odd = odd.T @ rho @ odd
    B_even = even.T @ rho @ even
    off = np.linalg.norm(even.T @ rho @ odd) + np.linalg.norm(odd.T @ rho @ even)
    print(f"\nblock-diagonal in the theta-split: off-block norm = {off:.2e}")
    print("\nTHE THETA-ODD 3x3 BLOCK:")
    for row in B_odd:
        print("  ", np.round(row, 6))
    ev = np.linalg.eigvals(B_odd)
    print("theta-odd eigenvalues:", np.round(sorted(ev, key=lambda z: (round(z.real, 6), round(z.imag, 6))), 8))
    scal = np.linalg.norm(B_odd - B_odd[0, 0] * np.eye(3))
    print(f"scalar? ||B - B00*I|| = {scal:.6f}  -> {'TRIVIAL (scalar)' if scal < 1e-9 else 'NON-TRIVIAL'}")
    for k in range(1, 200):
        if np.linalg.norm(np.linalg.matrix_power(B_odd, k) - np.eye(3)) < 1e-8:
            print(f"order of the theta-odd block: {k}")
            break
    else:
        print("order of the theta-odd block: > 200 (or infinite)")
    print(f"\ntheta-even 6x6 block eigenvalues:", np.round(sorted(np.linalg.eigvals(B_even), key=lambda z: (round(z.real, 6), round(z.imag, 6))), 8))
    print(f"Tr(odd block) = {np.trace(B_odd):.8f};  Tr(even block) = {np.trace(B_even):.8f}")


if __name__ == '__main__':
    main()
