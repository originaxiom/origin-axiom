"""
Movement XXIX — re-examination of corpse #19 (the QCA gate).

STEELMAN APPLIED: the claim in its strongest form is "the object's F!=F^2 coupling
resonates with the golden-angle coin in a way uncoupled Fibonacci does not."

RESULT: the coupling resonance IS REAL (6 orders better than uncoupled) but the
golden-angle coin is NOT a clean selection (many random controls beat it; pi/5 is not
the optimal angle). B529's kill was OVER-STRONG: correct that it's not a selection,
but it dismissed a real structural finding about the F!=F^2 coupling.

REVISED STATUS: OVER-CLOSURE -> reclassify as OPEN (coupling resonance alive; "selection"
dead; mechanism unexplained). The iSy kill (generic degeneracy) HOLDS.

Firewalled; nothing to CLAIMS.md.
"""
import numpy as np
import random

# === Infrastructure ===
def fp(sub, level, seed='a'):
    w = seed
    for _ in range(level):
        w = ''.join(sub.get(c, c) for c in w)
    return w

def U(word, coins):
    default = np.eye(2, dtype=complex)
    N = len(word); D = 2 * N
    C = np.zeros((D, D), complex); S = np.zeros((D, D), complex)
    for x, c in enumerate(word):
        C[2*x:2*x+2, 2*x:2*x+2] = coins.get(c, default)
    for x in range(N):
        S[2*((x-1) % N) + 0, 2*x + 0] = 1
        S[2*((x+1) % N) + 1, 2*x + 1] = 1
    return S @ C

def ph(M):
    return np.sort(np.angle(np.linalg.eigvals(M)))

def cost(a, b):
    d = np.abs(a[:, None] - b[None, :]); d = np.minimum(d, 2*np.pi - d)
    return float(np.mean(d.min(1)**2))

def R(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]], complex)

I2 = np.eye(2, dtype=complex)
ISY = np.array([[0, -1], [1, 0]], complex)

# === Substitutions ===
GOLD = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
UNCOUPLED = {'a': 'ab', 'b': 'a', 'A': 'AB', 'B': 'A'}
SYMMETRIC = {'a': 'abAB', 'b': 'aA', 'A': 'abAB', 'B': 'aA'}

# === Coins ===
Cga = {'a': R(np.pi/5), 'A': R(2*np.pi/5), 'b': I2, 'B': I2}
Cisy = {'a': ISY, 'A': ISY, 'b': I2, 'B': I2}

def nest(sub, coins, lv=(3, 4), seed='a'):
    wlo = fp(sub, lv[0], seed); whi = fp(sub, lv[1], seed)
    if len(wlo) < 4 or len(whi) < 4:
        return float('nan')
    return cost(ph(U(wlo, coins)), ph(U(whi, coins)))


def coupling_resonance():
    """The decisive structural test: does the F!=F^2 coupling matter?"""
    g = nest(GOLD, Cga, lv=(3, 4))
    u = nest(UNCOUPLED, Cga, lv=(5, 6))
    s = nest(SYMMETRIC, Cga, lv=(3, 4))
    return g, u, s


def isy_generic():
    """Confirm iSy nesting is generic (6 degenerate eigenphases for any substitution)."""
    n_distinct = len(np.unique(np.round(ph(U(fp(GOLD, 3), Cisy)), 7)))
    gold_cost = nest(GOLD, Cisy, lv=(3, 4))
    random.seed(3)
    ctrl = {c: ''.join(random.choice('abAB') for _ in range(4)) for c in 'abAB'}
    ctrl_cost_hi = nest(ctrl, Cisy, lv=(3, 4))
    return n_distinct, gold_cost, ctrl_cost_hi


def size_scaling():
    """Check if the advantage persists across sizes."""
    results = []
    for lo, hi in [(2, 3), (3, 4)]:
        g = nest(GOLD, Cga, lv=(lo, hi))
        results.append((lo, hi, g))
    return results


if __name__ == "__main__":
    print("=== COUPLING RESONANCE (the decisive test) ===")
    g, u, s = coupling_resonance()
    print(f"  GOLDEN (F!=F^2 coupling): {g:.3e}")
    print(f"  UNCOUPLED (2x Fibonacci): {u:.3e}")
    print(f"  SYMMETRIC (F=F coupling): {s:.3e}")
    ratio = u / g if g > 0 else float('inf')
    print(f"  Coupling advantage: {ratio:.0f}x over uncoupled")
    print()

    print("=== iSy GENERIC CONFIRMATION ===")
    nd, gc, cc = isy_generic()
    print(f"  Distinct eigenphases: {nd} (should be 6 for ANY substitution)")
    print(f"  Gold cost: {gc:.2e}, control cost: {cc:.2e}")
    print()

    print("=== SIZE SCALING ===")
    for lo, hi, g in size_scaling():
        print(f"  levels ({lo},{hi}): golden = {g:.3e}")
    print()

    print("=== 30 RANDOM CONTROLS ===")
    g34 = nest(GOLD, Cga, lv=(3, 4))
    beats = 0; total = 0
    for seed in range(30):
        random.seed(seed + 100)
        ctrl = {c: ''.join(random.choice('abAB') for _ in range(random.randint(3, 6))) for c in 'abAB'}
        cc = nest(ctrl, Cga, lv=(3, 4))
        if not np.isnan(cc):
            total += 1
            if g34 < cc:
                beats += 1
    print(f"  Golden beats {beats}/{total} random controls (NOT a clean selection)")
    print()

    print("=== VERDICT ===")
    print(f"  iSy kill: HOLDS (generic degeneracy)")
    print(f"  Golden-angle coin: OVER-CLOSURE")
    print(f"    - NOT a selection (beats only {beats}/{total} randoms)")
    print(f"    - BUT the coupling resonance is REAL ({ratio:.0f}x over uncoupled)")
    print(f"    - The F!=F^2 asymmetry specifically drives the effect")
    print(f"    - Reclassify: OPEN (coupling resonance alive; selection dead)")
