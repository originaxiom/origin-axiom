"""The weave's laws, the two new ones checked: the parity trichotomy along the wave, and the triplet's group.

(1) The trichotomy (WEAVE and WAVE). A monodromy phi in GL(2, Z) acts on the three non-zero parities of the records
    through phi mod 2, an element of GL(2, F_2) = S_3. It has order 3 exactly when tr phi is odd, order 2 when tr phi is
    even and phi is not the identity mod 2, and order 1 when phi is the identity mod 2. At tick n (the level, monodromy
    phi^n) the order is that of (phi mod 2)^n. So the parity triplet is one orbit (A_4, 2T) at the ticks 3 does not
    divide on an odd-trace thread, and three lines (V_4, Q_8) at every third tick; a line and a pair (D_4, Q_16), then
    three lines, on an even-trace thread of order 2; three lines at every tick when phi is the identity mod 2. Checked on
    every state of GENESIS to word length 12 (758, both signs) and on every integer matrix of determinant +-1 with entries
    of size at most 6.

(2) The triplet's group (W4, recomputed from the matrices banked in the_common_point.json). L, R and the fibre's
    translations generate a group of order 24 with reflections and without -1: T_d, which is S_4. The sign -I acts on the
    triplet as the fibre translation by ab, so it adds nothing; the swap P doubles the group to O_h (order 48). Every
    element of the weave's group is conjugate to its inverse, so all its characters are real. One odd-trace thread with
    the fibre generates A_4 (order 12), whose elements of order 3 are not conjugate to their inverses; and conjugating
    the monodromy by L (the change of marking LR -> RL) carries it to the other class.

Run: python3 the_weaves_laws.py  ->  the_weaves_laws.json beside it.
"""
import json
import os
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))

L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
I2 = ((1, 0), (0, 1))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))


def mod2(A):
    return tuple(tuple(x % 2 for x in row) for row in A)


def order_mod2(A):
    a, P = mod2(A), mod2(A)
    for k in range(1, 7):
        if P == I2:
            return k
        P = mod2(mul(P, a))
    raise AssertionError("GL(2, F_2) has exponent 6")


def kind(A):
    return {1: "identity mod 2: three lines", 2: "an involution mod 2: a line and a pair", 3: "a 3-cycle mod 2: one orbit"}[
        order_mod2(A)]


# ---------- (1) the states of GENESIS to length 12 ----------

def states(nmax=12):
    """signed cyclic words: primitive, both letters, up to rotation and the L<->R swap (GENESIS section 3)"""
    out = []
    for n in range(2, nmax + 1):
        seen = set()
        for bits in product("LR", repeat=n):
            w = "".join(bits)
            if "L" not in w or "R" not in w:
                continue
            rots = [w[i:] + w[:i] for i in range(n)]
            if len(set(rots)) < n:
                continue                                   # not primitive
            sw = w.translate(str.maketrans("LR", "RL"))
            canon = min(rots + [sw[i:] + sw[:i] for i in range(n)])
            if canon in seen:
                continue
            seen.add(canon)
            out.append(canon)
    return out


def matrix(w):
    M = I2
    for c in w:
        M = mul(M, L if c == "L" else R)
    return M


def part1():
    words = states()
    rows, by_kind, by_len = [], {}, {}
    for w in words:
        for eps in (1, -1):
            M = matrix(w)
            M = tuple(tuple(eps * x for x in r) for r in M)
            tr = M[0][0] + M[1][1]
            k = order_mod2(M)
            assert (k == 3) == (tr % 2 == 1)
            ticks = []
            P = I2
            for n in range(1, 7):
                P = mul(P, M)
                ticks.append(order_mod2(P))
            # the order at tick n is that of (phi mod 2)^n
            assert ticks == [k // __import__("math").gcd(k, n) for n in range(1, 7)]
            by_kind[kind(M)] = by_kind.get(kind(M), 0) + 1
            by_len.setdefault(len(w), {}).setdefault(kind(M), 0)
            by_len[len(w)][kind(M)] += 1
            if len(w) <= 6:
                rows.append({"state": ("+" if eps > 0 else "-") + w, "trace": tr, "order mod 2": k,
                             "orders at ticks 1-6": ticks})
    total = sum(by_kind.values())
    assert total == 758, total
    # every determinant +-1 matrix with small entries
    checked = 0
    for a, b, c, d in product(range(-6, 7), repeat=4):
        if a * d - b * c in (1, -1):
            A = ((a, b), (c, d))
            k = order_mod2(A)
            assert (k == 3) == ((a + d) % 2 == 1)
            assert (k == 1) == (mod2(A) == I2)
            checked += 1
    return {"states of GENESIS to length 12 (both signs)": total,
            "by kind": by_kind,
            "by word length": {str(n): v for n, v in sorted(by_len.items())},
            "the states to length 6": rows,
            "order 3 exactly at odd trace, order 1 exactly at the identity mod 2: matrices of det +-1, entries <= 6": checked,
            "the order at tick n is that of (phi mod 2)^n, so a 3-cycle thread has one orbit at ticks 1, 2, 4, 5 and three lines at 3, 6": True}


# ---------- (2) the triplet's group ----------

def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


ID3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
NEG3 = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))


def closure(gens):
    G, fr = {ID3}, [ID3]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = mmul(A, g)
                if B not in G:
                    G.add(B)
                    nx.append(B)
        fr = nx
    return G


def inv(A, G):
    for B in G:
        if mmul(A, B) == ID3:
            return B
    raise AssertionError


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def order(A):
    P, k = A, 1
    while P != ID3:
        P, k = mmul(P, A), k + 1
    return k


def real(G):
    """every element conjugate to its inverse (the characters are all real)"""
    Gl = list(G)
    return all(any(mmul(mmul(inv(g, G), x), g) == inv(x, G) for g in Gl) for x in Gl)


def part2():
    banked = json.load(open(os.path.join(HERE, "the_common_point.json")))["(3) the triplet"][
        "the matrices (columns: the lines trivial on a, on b, on ab)"]
    M = {n: tuple(tuple(r) for r in m) for n, m in banked.items()}
    a, b = M["inner by a"], M["inner by b"]
    G0 = closure([M["L"], M["R"], a, b])
    Gs = closure([M["L"], M["R"], a, b, M["-I"]])
    G = closure([M["L"], M["R"], a, b, M["-I"], M["P"]])
    LR, RL = mmul(M["L"], M["R"]), mmul(M["R"], M["L"])
    T = closure([LR, a, b])
    T2 = closure([RL, a, b])
    Linv = inv(M["L"], G)

    def cls(x, H):
        return frozenset(mmul(mmul(inv(g, H), x), g) for g in H)
    out = {
        "L, R and the fibre's translations": {
            "order": len(G0), "contains -1": NEG3 in G0,
            "reflections (det -1, order 2)": sum(1 for A in G0 if det3(A) == -1 and order(A) == 2),
            "element orders": {str(k): sum(1 for A in G0 if order(A) == k) for k in sorted({order(A) for A in G0})},
            "every element conjugate to its inverse (all characters real)": real(G0)},
        "the sign -I acts as the translation by ab": M["-I"] == mmul(a, b),
        "with the sign": {"order": len(Gs), "the same group": Gs == G0},
        "with the sign and the swap P": {"order": len(G), "contains -1": NEG3 in G,
                                         "all characters real": real(G)},
        "one odd-trace thread with the fibre (LR)": {
            "order": len(T), "every element conjugate to its inverse": real(T),
            "LR and RL generate the same group with the fibre": T == T2,
            "RL = L^-1 (LR) L on the triplet": RL == mmul(mmul(Linv, LR), M["L"]),
            "LR and RL lie in different classes of that group": cls(LR, T) != cls(RL, T),
            "RL lies in the class of LR's inverse": RL in cls(inv(LR, T), T)},
    }
    assert out["L, R and the fibre's translations"]["order"] == 24 and not out["L, R and the fibre's translations"][
        "contains -1"]
    assert out["the sign -I acts as the translation by ab"] and out["with the sign"]["the same group"]
    assert out["with the sign and the swap P"]["order"] == 48
    return out


# ---------- (3) no state has its three parities separate and carried into one another ----------

def isqrt_exact(n):
    if n < 0:
        return None
    r = int(n ** 0.5)
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r if r * r == n else None


def normalizer_mod2(M, bound=60):
    """the images mod 2 of the elements g of GL(2, Z) with g M g^-1 = M or M^-1, found with a bounded parameter.
    Commuting g are d I + (m/g0)(M - s I) with det +-1 (a Pell equation in d, m); reversing g are [[a, b], [c, -a]] with
    a(p - s) + b r + c q = 0 and -a^2 - b c = +-1, so g^2 = +-I."""
    (p, q), (r, s) = M
    g0 = __import__("math").gcd(__import__("math").gcd(q, r), p - s)
    imgs = set()
    for m in range(-bound, bound + 1):
        if m == 0:
            continue
        if (q * m) % g0 or (r * m) % g0 or ((p - s) * m) % g0:
            continue
        B, C, D = q * m // g0, r * m // g0, (p - s) * m // g0
        for e in (1, -1):
            # d^2 + D d - (B C + e) = 0
            disc = D * D + 4 * (B * C + e)
            sq = isqrt_exact(disc)
            if sq is None:
                continue
            for num in (-D + sq, -D - sq):
                if num % 2 == 0:
                    d = num // 2
                    g = ((d + D, B), (C, d))
                    assert g[0][0] * g[1][1] - g[0][1] * g[1][0] == e
                    assert mul(g, M) == mul(M, g)
                    imgs.add(mod2(g))
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            # c q = -a (p - s) - b r
            if q == 0:
                continue
            num = -a * (p - s) - b * r
            if num % q:
                continue
            c = num // q
            if -a * a - b * c in (1, -1):
                g = ((a, b), (c, -a))
                Minv = ((s, -q), (-r, p)) if p * s - q * r == 1 else ((-s, q), (r, -p))
                assert mul(g, M) == mul(Minv, g)
                imgs.add(mod2(g))
    # the group the images generate in GL(2, F_2)
    G, fr = {I2}, [I2]
    while fr:
        nx = []
        for A in fr:
            for g in imgs:
                Bm = mod2(mul(A, g))
                if Bm not in G:
                    G.add(Bm)
                    nx.append(Bm)
        fr = nx
    return G


def orbits_on_parities(G):
    vecs = [(1, 0), (0, 1), (1, 1)]
    act = lambda g, v: ((g[0][0] * v[0] + g[0][1] * v[1]) % 2, (g[1][0] * v[0] + g[1][1] * v[1]) % 2)
    seen, sizes = set(), []
    for v in vecs:
        if v in seen:
            continue
        orb = {act(g, v) for g in G}
        seen |= orb
        sizes.append(len(orb))
    return sorted(sizes)


def part3(nmax=12):
    rows, tally = [], {}
    for w in states(nmax):
        for eps in (1, -1):
            M = tuple(tuple(eps * x for x in r) for r in matrix(w))
            if mod2(M) != I2:
                continue
            G = normalizer_mod2(M)
            assert len(G) <= 2
            key = "+".join(str(x) for x in orbits_on_parities(G))
            tally[key] = tally.get(key, 0) + 1
            if len(w) <= 8:
                rows.append({"state": ("+" if eps > 0 else "-") + w, "trace": M[0][0] + M[1][1],
                             "its isometries on the three parities: group order": len(G),
                             "orbits": key})
    return {"the states with phi = I mod 2 (three separate parities at their own tick), to length 12": sum(tally.values()),
            "orbits of their isometries on the three parities": tally,
            "never one orbit of three (the group has order at most 2)": "3" not in tally,
            "to length 8": rows}


if __name__ == "__main__":
    res = {"(1) the parity trichotomy, along the wave": part1(), "(2) the triplet's group": part2(),
           "(3) no state has its three parities separate and alike at its own tick": part3()}
    with open(os.path.join(HERE, "the_weaves_laws.json"), "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    for k, v in res.items():
        print(k)
        for kk, vv in v.items():
            if kk not in ("the states to length 6", "to length 8"):
                print("  ", kk, ":", json.dumps(vv, ensure_ascii=False)[:300])
