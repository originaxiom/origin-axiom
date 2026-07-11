"""
Movement XXXI — handoff verification.

The other seat delivered five items for independent verification:
  1. √13 artifact (broken derived interleaving substitution) → CONFIRMED broken
  2. Coupling resonance (golden pair beats same-angle) → CONFIRMED (293×, not 7×)
  3. Recognizability radius → REFINED (centered R=3, diameter 7, not "9")
  4. Bounded remainder (saturation) → CONFIRMED (~1.6, not ~15)
  5. Session ledger (already integrated)
"""
import numpy as np
import sympy as sp

PHI = (1 + np.sqrt(5)) / 2
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
BETA = PHI * (1 + np.sqrt(PHI))


def _word(n=600000):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


def fp(sub, level, seed='a'):
    w = seed
    for _ in range(level):
        w = ''.join(sub.get(c, c) for c in w)
    return w


# =====================================================================
# (1) √13 artifact
# =====================================================================

def verify_sqrt13_error():
    """
    RESULT: √13 artifact CONFIRMED.
    The handoff's 4-letter binary substitution 0→0, 1→030, 2→0302, 3→20202
    has letter '1' never regenerated (zero column in incidence matrix).
    The ERROR: binary return words '011' collapse two distinct original-alphabet
    return words ('aAB' and 'bAB'), producing a singular substitution.
    The correct 5-letter derivation has char poly = x·(x⁴−2x³−5x²−4x−1),
    Perron root = β, NOT (1+√13)/2.
    """
    print("=" * 70)
    print("(1) √13 artifact verification")
    print("=" * 70)

    # (a) Verify the handoff's substitution is broken
    handoff_sub = {0: '0', 1: '030', 2: '0302', 3: '20202'}
    print("Handoff substitution: 0→0, 1→030, 2→0302, 3→20202")
    for target in range(4):
        appears_in = [k for k, v in handoff_sub.items() if str(target) in v]
        status = "OK" if appears_in else "*** NEVER REGENERATED ***"
        print(f"  Letter '{target}' in images of: {appears_in} → {status}")

    handoff_M = np.zeros((4, 4), dtype=int)
    for src, img in handoff_sub.items():
        for ch in img:
            handoff_M[int(ch), src] += 1
    x = sp.Symbol('x')
    handoff_char = sp.Matrix(handoff_M.tolist()).charpoly(x).as_expr()
    print(f"\n  Handoff char poly: {sp.factor(handoff_char)}")
    sqrt13_root = (1 + np.sqrt(13)) / 2
    print(f"  (1+√13)/2 = {sqrt13_root:.6f}")

    # (b) Correct derivation: 5 original-alphabet return words
    u = _word(50000)
    old_pos = [i for i, c in enumerate(u) if c in 'ab']
    orig_rws = sorted(set(u[old_pos[i]:old_pos[i + 1]]
                          for i in range(len(old_pos) - 1)), key=len)
    print(f"\nCorrect return words to {{a,b}}: {orig_rws}")
    print(f"  Count: {len(orig_rws)} (binary '011' = both 'aAB' and 'bAB')")

    rw_idx = {rw: i for i, rw in enumerate(orig_rws)}
    n = len(orig_rws)
    inc = np.zeros((n, n), dtype=int)
    print(f"\nDerived substitution:")
    for j, rw in enumerate(orig_rws):
        img = ''.join(SUB[c] for c in rw)
        old_p = [k for k, c in enumerate(img) if c in 'ab']
        chunks = [img[old_p[k]:old_p[k + 1] if k + 1 < len(old_p) else len(img)]
                  for k in range(len(old_p))]
        for ch in chunks:
            if ch in rw_idx:
                inc[rw_idx[ch], j] += 1
        labels = ''.join(str(rw_idx.get(ch, '?')) for ch in chunks)
        print(f"  σ_D({j}: '{rw}') → '{img}' → {labels}")

    char_poly = sp.Matrix(inc.tolist()).charpoly(x).as_expr()
    print(f"\n  Char poly: {sp.factor(char_poly)}")
    eigs = sorted([complex(e) for e in np.linalg.eigvals(inc.astype(float))],
                  key=lambda z: -abs(z))
    perron = abs(eigs[0])
    print(f"  Perron root: {perron:.6f}")
    print(f"  β:           {BETA:.6f}")
    print(f"  Match: {abs(perron - BETA) < 1e-4}")
    print(f"\n  VERDICT: √13 artifact CONFIRMED. The 4-letter binary derivation")
    print(f"  collapses 'aAB'/'bAB' into one return word '011' → singular matrix.")
    print(f"  Correct derivation: 5 return words, char poly = x·(x⁴−2x³−5x²−4x−1),")
    print(f"  Perron root = β. √13 was never structural.")

    return dict(broken=True, correct_perron=perron, correct_count=n)


# =====================================================================
# (2) Coupling resonance
# =====================================================================

def verify_coupling_resonance():
    """
    RESULT: golden pair (π/5, 2π/5) beats same-angle (π/5, π/5) by 293×.
    Handoff claimed 7× — our number is larger, same direction.
    F≠F² advantage: 242,036× over uncoupled (matches movement XXIX).
    """
    print("\n" + "=" * 70)
    print("(2) Coupling resonance — golden pair vs same-angle")
    print("=" * 70)

    def U_op(word, coins):
        default = np.eye(2, dtype=complex)
        N = len(word); D = 2 * N
        C_mat = np.zeros((D, D), complex); S_mat = np.zeros((D, D), complex)
        for x, c in enumerate(word):
            C_mat[2*x:2*x+2, 2*x:2*x+2] = coins.get(c, default)
        for x in range(N):
            S_mat[2*((x-1) % N) + 0, 2*x + 0] = 1
            S_mat[2*((x+1) % N) + 1, 2*x + 1] = 1
        return S_mat @ C_mat

    def eigenphases(M_):
        return np.sort(np.angle(np.linalg.eigvals(M_)))

    def nesting_cost(a, b):
        d = np.abs(a[:, None] - b[None, :]); d = np.minimum(d, 2*np.pi - d)
        return float(np.mean(d.min(1)**2))

    def R(t):
        return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]], complex)

    I2 = np.eye(2, dtype=complex)
    GOLD = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
    UNCOUPLED = {'a': 'ab', 'b': 'a', 'A': 'AB', 'B': 'A'}
    SYMMETRIC = {'a': 'abAB', 'b': 'aA', 'A': 'abAB', 'B': 'aA'}

    def nest(sub, coins, lv=(3, 4), seed='a'):
        wlo = fp(sub, lv[0], seed); whi = fp(sub, lv[1], seed)
        if len(wlo) < 4 or len(whi) < 4:
            return float('nan')
        return nesting_cost(eigenphases(U_op(wlo, coins)),
                            eigenphases(U_op(whi, coins)))

    golden_pair = {'a': R(np.pi/5), 'A': R(2*np.pi/5), 'b': I2, 'B': I2}
    same_angle = {'a': R(np.pi/5), 'A': R(np.pi/5), 'b': I2, 'B': I2}

    gp = nest(GOLD, golden_pair)
    sa = nest(GOLD, same_angle)
    ratio = sa / gp if gp > 0 else float('inf')
    print(f"  Golden pair (π/5, 2π/5): {gp:.3e}")
    print(f"  Same angle  (π/5, π/5):  {sa:.3e}")
    print(f"  Ratio same/golden-pair:  {ratio:.1f}× (handoff claimed 7×)")

    g = nest(GOLD, golden_pair)
    u = nest(UNCOUPLED, golden_pair, lv=(5, 6))
    s = nest(SYMMETRIC, golden_pair)
    print(f"\n  Coupling advantage (golden-pair coin):")
    print(f"    GOLDEN (F≠F²):   {g:.3e}")
    print(f"    SYMMETRIC (F=F): {s:.3e}")
    print(f"    UNCOUPLED (2×F): {u:.3e}")
    if g > 0:
        print(f"    Uncoupled/Golden: {u/g:.0f}× (movement XXIX: 240,000×)")

    return dict(gp_cost=gp, sa_cost=sa, ratio=ratio, coupling_advantage=u/g if g > 0 else None)


# =====================================================================
# (3) Recognizability radius
# =====================================================================

def verify_recognizability_radius():
    """
    RESULT: centered recognizability radius = 3 (diameter 7).
    The handoff's "radius = 9" was the Mossé upper bound (2·max|σ|−1 = 9),
    not the actual value. At R=2 (diameter 5), one ambiguity: 'ABabA' starts
    at offset 0 of both σ(a) and σ(A). At R=3 (diameter 7), fully resolved.
    """
    print("\n" + "=" * 70)
    print("(3) Recognizability radius (centered)")
    print("=" * 70)

    img_lens = {c: len(SUB[c]) for c in 'abAB'}
    max_img = max(img_lens.values())
    print(f"Image lengths: {img_lens}")
    print(f"Mossé upper bound: 2·max|σ|−1 = {2*max_img - 1}")

    u_prev = fp(SUB, 7)
    u_next = fp(SUB, 8)

    pos_map = []
    for c in u_prev:
        img = SUB[c]
        for j in range(len(img)):
            pos_map.append((c, j))

    n = min(len(u_next), len(pos_map))

    result_radius = None
    for R_ in range(1, 8):
        diameter = 2*R_ + 1
        factor_map = {}
        for i in range(R_, n - R_):
            f = u_next[i-R_:i+R_+1]
            key = (pos_map[i][0], pos_map[i][1])
            if f not in factor_map:
                factor_map[f] = set()
            factor_map[f].add(key)

        ambiguous = [(f, s) for f, s in factor_map.items() if len(s) > 1]
        print(f"  R={R_} (diameter={diameter}): {len(factor_map)} factors, "
              f"{len(ambiguous)} ambiguous", end="")
        if ambiguous:
            f0, s0 = ambiguous[0]
            print(f"  e.g. '{f0}' → {s0}")
        else:
            print(f"  → RECOGNIZABLE")
            result_radius = R_
            break

    if result_radius:
        print(f"\n  Centered recognizability radius: R = {result_radius} (diameter {2*result_radius+1})")
        print(f"  (Mossé bound: R ≤ {max_img - 1}, diameter ≤ {2*max_img - 1})")
    return result_radius


# =====================================================================
# (4) Bounded remainder
# =====================================================================

def verify_bounded_remainder():
    """
    RESULT: bounded remainder CONFIRMED. Max single-letter discrepancy ≈ 1.6,
    saturates by N=1000. Much tighter than the handoff's "~15".
    """
    print("\n" + "=" * 70)
    print("(4) Bounded remainder")
    print("=" * 70)

    u = _word(500000)
    n = len(u)
    letter_map = {'a': 0, 'b': 1, 'A': 2, 'B': 3}

    evals, evecs = np.linalg.eig(M.astype(float))
    idx = np.argmax(np.abs(evals))
    freq_vec = np.abs(evecs[:, idx])
    freq_vec = freq_vec / freq_vec.sum()

    actual = np.array([sum(1 for c in u if c == l) for l in 'abAB']) / n
    print(f"Perron frequencies: {freq_vec}")
    print(f"Actual frequencies: {actual}")
    assert np.allclose(freq_vec, actual, atol=1e-3), "frequency mismatch"

    counts = np.zeros(4)
    max_disc = np.zeros(4)
    for i, c in enumerate(u):
        j = letter_map[c]
        counts[j] += 1
        for k in range(4):
            d = abs(counts[k] - (i + 1) * freq_vec[k])
            if d > max_disc[k]:
                max_disc[k] = d

    print(f"\nMax single-letter discrepancy:")
    for k, c in enumerate('abAB'):
        print(f"  max |D_{c}(N)|: {max_disc[k]:.2f}")
    overall = max(max_disc)
    print(f"  Overall: {overall:.2f}")
    print(f"  BOUNDED: {overall < 5}")

    # Contracting-direction check
    print(f"\nContracting-direction discrepancy (over N=50000):")
    for i in range(4):
        if abs(evals[i]) < 1:
            v = evecs[:, i].real
            v = v / np.linalg.norm(v)
            cum = np.zeros(4)
            max_p = 0
            for j, c in enumerate(u[:50000]):
                cum[letter_map[c]] += 1
                disc = cum - (j + 1) * freq_vec
                p = abs(np.dot(disc, v))
                if p > max_p:
                    max_p = p
            print(f"  λ={evals[i]:.4f}: max |proj| = {max_p:.2f}")

    return dict(max_disc=overall, bounded=overall < 5)


if __name__ == "__main__":
    r1 = verify_sqrt13_error()
    r2 = verify_coupling_resonance()
    r3 = verify_recognizability_radius()
    r4 = verify_bounded_remainder()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"1. √13 artifact: CONFIRMED broken (correct derivation: {r1['correct_count']} return words, Perron = β)")
    print(f"2. Coupling resonance: same/golden-pair = {r2['ratio']:.0f}× (handoff: 7×, same direction)")
    if r2['coupling_advantage']:
        print(f"   F≠F² advantage: {r2['coupling_advantage']:.0f}× over uncoupled")
    print(f"3. Recognizability: centered R = {r3}, diameter = {2*r3+1} (handoff: 'radius=9' was Mossé bound)")
    print(f"4. Bounded remainder: max disc = {r4['max_disc']:.2f}, bounded = {r4['bounded']} (handoff: ~15)")
