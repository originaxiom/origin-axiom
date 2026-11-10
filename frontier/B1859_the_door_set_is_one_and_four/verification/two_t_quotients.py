"""B1859 (data-free; exact): which metallic bundles have a quotient onto the binary tetrahedral group 2T = SL(2, 3).

- **Why.** The structural frame enters at E6 through pi_1 -> 2T (the root's trace field has one ramified prime). The
  own-conductor door (door_set.py) is a property of the grammar's letters, not a quotient of pi_1. A cascade needs both.
- **Method 1, by hand.** pi_1 of the bundle of R^m L^m is <a, b, t | t a t^-1 = phi(a), t b t^-1 = phi(b)>, with
  phi = lambda^m rho^m for the two Dehn twists lambda: (a, b) -> (a, ba) and rho: (a, b) -> (ab, b). Under a
  homomorphism with images (A, B, T) the relations read T A T^-1 = A (B A^m)^m and T B T^-1 = B A^m. On homology phi
  is [[1 + m^2, m], [m, 1]], of trace m^2 + 2, the trace of L^m R^m.
- **Method 2, SnapPy's presentation** of the bundle 'b++' + 'R'*m + 'L'*m, where SnapPy is installed.
- **The count.** Surjections, and their classes under the 24 automorphisms of SL(2, 3), which act freely on them.
- **The control:** m = 1 is the figure-eight complement, with 48 surjections in 2 classes (B266, B993).
- **The aside.** pi_1 of the root has no surjection onto SL(2, 5): the E8 door is not a quotient of pi_1."""
from itertools import product


def group(p):
    els = [(a, b, c, d) for a, b, c, d in product(range(p), repeat=4) if (a * d - b * c) % p == 1]
    return els


def mul(A, B, p):
    return ((A[0] * B[0] + A[1] * B[2]) % p, (A[0] * B[1] + A[1] * B[3]) % p,
            (A[2] * B[0] + A[3] * B[2]) % p, (A[2] * B[1] + A[3] * B[3]) % p)


def inv(A, p):
    return (A[3] % p, (-A[1]) % p, (-A[2]) % p, A[0] % p)


def power(A, k, p):
    X = (1, 0, 0, 1)
    for _ in range(k):
        X = mul(X, A, p)
    return X


def generated(gens, p, full):
    I = (1, 0, 0, 1)
    seen, frontier = {I}, [I]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h, p)
                if x not in seen:
                    seen.add(x); nxt.append(x)
        frontier = nxt
    return len(seen) == full


def surjections_by_hand(m, p):
    G = group(p); n = len(G); count = 0
    for A in G:
        for B in G:
            BAm = mul(B, power(A, m, p), p)
            phia = mul(A, power(BAm, m, p), p)
            for T in G:
                Ti = inv(T, p)
                if mul(mul(T, A, p), Ti, p) == phia and mul(mul(T, B, p), Ti, p) == BAm and generated([A, B, T], p, n):
                    count += 1
    return count


def surjections_by_snappy(m, p):
    try:
        import snappy
    except Exception:
        return None
    M = snappy.Manifold("b++" + "R" * m + "L" * m)
    F = M.fundamental_group()
    gens, rels = F.generators(), F.relators()
    G = group(p); n = len(G); count = 0
    for imgs in product(G, repeat=len(gens)):
        img = dict(zip(gens, imgs))
        ok = True
        for r in rels:
            X = (1, 0, 0, 1)
            for ch in r:
                g = img[ch.lower()]
                X = mul(X, g if ch.islower() else inv(g, p), p)
            if X != (1, 0, 0, 1):
                ok = False; break
        if ok and generated(list(imgs), p, n):
            count += 1
    return count


rows, hand = [], {}
for m in (1, 2, 3, 4, 5, 6):
    h = surjections_by_hand(m, 3); hand[m] = h
    s = surjections_by_snappy(m, 3) if m <= 4 else None
    assert s is None or s == h, (m, h, s)
    rows.append("m = %d   surjections onto SL(2, 3): %3d = %2d classes   [by hand%s]" % (m, h, h // 24, "; SnapPy's presentation agrees" if s is not None else ""))
print("\n".join(rows))
assert hand[1] == 48 and hand[2] == 0 and hand[3] == 240 and hand[4] == 0
e8 = surjections_by_hand(1, 5)
print("the root (m = 1): surjections onto SL(2, 5): %d" % e8)
assert e8 == 0
print("=> m = 1 has the own-conductor door and a 2T quotient; m = 4 has the door and no 2T quotient; m = 3 has 2T quotients and no door")
print("=> the E8 door is a shadow of the grammar's letters, not a quotient of pi_1")
