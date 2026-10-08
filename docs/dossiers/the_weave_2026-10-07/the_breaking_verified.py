"""W42 (the rule: W42_RULE.md, committed before this script). Main's B1620 verified from this seat's normal form, and the
threads' own zero modes (main's ask 2 of relay THE_BREAKING_THE_WEAVE_ALLOWS).

Part A, a VERIFICATION, not blind (B1620's FINDINGS and the definition in its post_seal_tensors.py read first; its code
is not run and its group is not used):
  - the group G on the matter triplet T from W21's construction (W38), in W38's normal form c(g) S(g), encoded exactly
    as (k mod 24, S) with c = exp(2 pi i k/24); compared with G' = {z S : z^8 = 1, z^4 = sgn S} built by hand (A0);
  - every subgroup and its conjugacy class (A1);
  - viability under T-bar (x) T, T (x) T and Sym^2 T (B1620's definition: the singular values of a generic invariant M
    are three, distinct and non-zero), by two routes: exact (orbit vectors of the monomial action, a generic member at
    random Gaussian-integer points, det M and the discriminant of M M^dagger's characteristic polynomial in Z[zeta_24])
    and the character criterion by hand (A2, A3);
  - K, the inner automorphisms' lifts with c = 1, from W40's construction, and the subgroups containing it (A4).
Part B, a census of every thread (each Lyndon word in L and R of length 2 to 12, read as in
the_mixing_patterns_verified.word): the fixed space on T of its monodromy for both extensions +-g, which by the Wang
sequence (H^0(F; W) = 0) is the T part of the thread's own H^1 (B1 to B3); the general extension's line types (B4);
main's B1621 tick as the zero-mode projector of the thread RL (B5).

Run: python3 the_breaking_verified.py  ->  the_breaking_verified.json beside it.
"""
import itertools
import json
import random
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_couplings_exact as CE  # noqa: E402  (W38's normal form)
import the_couplings_verified as CV  # noqa: E402  (W38: the group on T from W21's construction)
import the_mixing_patterns_verified as MV  # noqa: E402  (W35: T, its basis, word())

OUT = HERE / "the_breaking_verified.json"
CP, CT, H = MV.CP, MV.CT, MV.H
TENSORS = ("T-bar (x) T", "T (x) T", "Sym^2 T")

# ---------------------------------------------------------------- Z[zeta_24], exactly: Phi_24 = x^8 - x^4 + 1

def zmul(a, b):
    r = [0] * 15
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] += x * y
    for d in range(14, 7, -1):                  # x^d = x^(d-4) - x^(d-8)
        c = r[d]
        if c:
            r[d] = 0
            r[d - 4] += c
            r[d - 8] -= c
    return tuple(r[:8])


def zadd(*xs):
    return tuple(sum(c) for c in zip(*xs))


def zneg(a):
    return tuple(-x for x in a)


def zscale(a, n):
    return tuple(n * x for x in a)


ZERO = (0,) * 8
POW = [(1,) + (0,) * 7]
for _ in range(47):
    POW.append(zmul(POW[-1], (0, 1) + (0,) * 6))


def zconj(a):
    return zadd(ZERO, *[zscale(POW[(24 - j) % 24], x) for j, x in enumerate(a) if x])


def gauss(x, y):
    """x + i y, with i = zeta_24^6"""
    return zadd(zscale(POW[0], x), zscale(POW[6], y))


def mmul(A, B):
    return [[zadd(ZERO, *[zmul(A[i][k], B[k][j]) for k in range(3)]) for j in range(3)] for i in range(3)]


def dagger(A):
    return [[zconj(A[j][i]) for j in range(3)] for i in range(3)]


def det3(A):
    t = ZERO
    for p in itertools.permutations(range(3)):
        s = 1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 == 0 else -1
        t = zadd(t, zscale(zmul(zmul(A[0][p[0]], A[1][p[1]]), A[2][p[2]]), s))
    return t


def trace(A):
    return zadd(A[0][0], A[1][1], A[2][2])


def four_discriminant(X):
    """4 Delta for lambda^3 + a lambda^2 + b lambda + c = det(lambda - X), with B = 2b:
    4 Delta = a^2 B^2 - 2 B^3 - 16 a^3 c - 108 c^2 + 36 a B c"""
    a = zneg(trace(X))
    tX2 = trace(mmul(X, X))
    B = zadd(zmul(trace(X), trace(X)), zneg(tX2))
    c = zneg(det3(X))
    a2 = zmul(a, a)
    return zadd(zmul(a2, zmul(B, B)), zscale(zmul(B, zmul(B, B)), -2), zscale(zmul(zmul(a2, a), c), -16),
                zscale(zmul(c, c), -108), zscale(zmul(zmul(a, B), c), 36))


# ---------------------------------------------------------------- the group, exactly

def perm_of(S):
    """pi with S e_i = s_i e_pi(i)"""
    return tuple(int(np.argmax(np.abs(np.array(S)[:, i]))) for i in range(3))


def parity(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2


def stype(S):
    S = np.array(S)
    p, tr = perm_of(S), int(np.trace(S))
    if p == (0, 1, 2):
        return "identity" if tr == 3 else "face half-turn"
    if parity(p) == 0:
        return "3-cycle"
    return "quarter-turn" if tr == 1 else "edge half-turn"


def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            S = np.zeros((3, 3), dtype=int)
            for i in range(3):
                S[p[i], i] = s[i]
            if round(np.linalg.det(S)) == 1:
                out.append(tuple(map(tuple, S.tolist())))
    return out


def the_group_exact():
    GT, _, el = CV.the_group()
    _, _, _, (B, data) = CE.normal_form(GT, el)
    enc = {(CE.root_of_unity(z), tuple(map(tuple, S.tolist()))) for _, z, S in data}

    def encode(g):
        M = B.conj().T @ g @ B
        nz = np.argwhere(abs(M) > 1e-6)
        z = M[tuple(nz[0])]
        S = np.round((M / z).real).astype(int)
        if round(np.linalg.det(S)) == -1:
            S, z = -S, -z
        assert np.allclose(M, z * S, atol=1e-8)
        return (CE.root_of_unity(z), tuple(map(tuple, S.tolist())))

    named = {w: encode(el[w]) for w in ("L", "R", "RL", "RRL")}
    return sorted(enc), B, encode, named


def emul(x, y):
    return ((x[0] + y[0]) % 24, tuple(map(tuple, (np.array(x[1]) @ np.array(y[1])).tolist())))


# ---------------------------------------------------------------- the tensors: monomial actions on matrix positions

def positions(tensor):
    if tensor == "Sym^2 T":
        return [(i, j) for i in range(3) for j in range(i, 3)]
    return [(i, j) for i in range(3) for j in range(3)]


def act(x, pos, tensor):
    """x = (k, S) on the matrix unit at pos: (phase exponent mod 24, new pos)"""
    k, S = x
    p = perm_of(S)
    s = [S[p[i]][i] for i in range(3)]
    i, j = pos
    ph = (0 if s[i] * s[j] == 1 else 12) + (0 if tensor == "T-bar (x) T" else 2 * k)
    q = (p[i], p[j])
    if tensor == "Sym^2 T":
        q = tuple(sorted(q))
    return ph % 24, q


def fixed_basis(Hel, tensor):
    """the Reynolds images of the matrix units, one per orbit whose stabiliser acts with phase 1 (exact)"""
    seen, basis = set(), []
    for x0 in positions(tensor):
        if x0 in seen:
            continue
        v = {}
        for h in Hel:
            ph, y = act(h, x0, tensor)
            v[y] = zadd(v.get(y, ZERO), POW[ph])
            seen.add(y)
        v = {y: c for y, c in v.items() if c != ZERO}
        if v:
            basis.append(v)
    return basis


def member(basis, coeffs, tensor):
    M = [[ZERO] * 3 for _ in range(3)]
    for v, t in zip(basis, coeffs):
        for (i, j), c in v.items():
            M[i][j] = zadd(M[i][j], zmul(c, t))
            if tensor == "Sym^2 T" and i != j:
                M[j][i] = zadd(M[j][i], zmul(c, t))
    return M


def viable_exact(basis, tensor, rng, points=3, bound=10 ** 6):
    """three distinct non-zero singular values at a random Gaussian-integer point: det M != 0 and disc(M M^dagger) != 0"""
    if not basis:
        return 0
    passed = 0
    for _ in range(points):
        coeffs = [gauss(rng.randint(-bound, bound), rng.randint(-bound, bound)) for _ in basis]
        M = member(basis, coeffs, tensor)
        if det3(M) != ZERO and four_discriminant(mmul(M, dagger(M))) != ZERO:
            passed += 1
    return passed


# ---------------------------------------------------------------- Part A

def part_A(G, named, encode):
    N = len(G)
    idx = {x: i for i, x in enumerate(G)}
    MUL = [[idx[emul(x, y)] for y in G] for x in G]
    E = idx[(0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))]
    INV = [next(j for j in range(N) if MUL[i][j] == E) for i in range(N)]

    def closure(gens):
        S, fr = {E}, [E]
        while fr:
            nx = []
            for x in fr:
                for g in gens:
                    y = MUL[x][g]
                    if y not in S:
                        S.add(y)
                        nx.append(y)
            fr = nx
        return frozenset(S)

    subs = {}
    for g in range(N):
        subs.setdefault(closure([g]), [g])
    queue = list(subs.items())
    while queue:
        Hs, gens = queue.pop()
        for g in range(N):
            if g not in Hs:
                J = closure(gens + [g])
                if J not in subs:
                    subs[J] = gens + [g]
                    queue.append((J, gens + [g]))
    subs = sorted(subs, key=lambda s: (len(s), sorted(s)))

    def conj(Hs, x):
        return frozenset(MUL[MUL[x][h]][INV[x]] for h in Hs)

    cls_of, classes = {}, []
    for Hs in subs:
        if Hs in cls_of:
            continue
        orbit = {conj(Hs, x) for x in range(N)}
        for J in orbit:
            cls_of[J] = len(classes)
        classes.append(sorted(orbit, key=lambda s: sorted(s)))

    def abelian(Hs):
        return all(MUL[a][b] == MUL[b][a] for a in Hs for b in Hs)

    def real_character(Hs):
        return all(int(np.trace(np.array(G[h][1]))) == 0 or G[h][0] % 12 == 0 for h in Hs)

    def involutive(Hs):
        return all(MUL[h][h] == E for h in Hs)

    criterion = {"T-bar (x) T": abelian, "T (x) T": lambda s: abelian(s) and real_character(s), "Sym^2 T": involutive}
    rng = random.Random(20261008)
    table, agree, passes = [], True, {}
    for Hs in subs:
        Hel = [G[h] for h in Hs]
        row = {"order": len(Hs), "class": cls_of[Hs], "abelian": bool(abelian(Hs)),
               "its image in the rotations": len({G[h][1] for h in Hs}),
               "its scalars": sum(1 for h in Hs if G[h][1] == ((1, 0, 0), (0, 1, 0), (0, 0, 1)))}
        for t in TENSORS:
            basis = fixed_basis(Hel, t)
            passed = viable_exact(basis, t, rng)
            exact = passed > 0
            by_hand = bool(criterion[t](Hs))
            agree &= exact == by_hand
            passes[passed] = passes.get(passed, 0) + 1
            row[t] = {"invariant dimension": len(basis), "viable (exact)": bool(exact), "points passed of 3": passed,
                      "viable (the criterion by hand)": by_hand}
        table.append((Hs, row))

    # A3: the elements of order 3, and Sym^2 T along each
    order3 = [h for h in range(N) if h != E and MUL[MUL[h][h]][h] == E]
    a3_each = []
    for h in order3:
        Hs = closure([h])
        basis = fixed_basis([G[x] for x in Hs], "Sym^2 T")
        a3_each.append({"c = 1": G[h][0] == 0, "a 3-cycle": stype(G[h][1]) == "3-cycle",
                        "Sym^2 T fixed dimension": len(basis),
                        "points passed of 3": viable_exact(basis, "Sym^2 T", rng)})

    # A4: K from W40's construction (the inner automorphisms, every lift, on T)
    named_T, _ = H.triplets()
    C = named_T["T"]
    G0 = H.gram_V()
    Qt = C.conj().T @ G0 @ C
    Kc = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T
    inner = {"inner by a": CP.inner([1]), "inner by b": CP.inner([2])}
    lifts = {n: [encode(MV.on_T(C, Kc, CT.on_V(phi, g))) for g in CP.extend(phi)] for n, phi in inner.items()}
    diag_signs = all(perm_of(x[1]) == (0, 1, 2) for v in lifts.values() for x in v)
    K = closure([idx[x] for v in lifts.values() for x in v if x[0] == 0])
    Eall = closure([idx[x] for v in lifts.values() for x in v])
    over_K = [(Hs, row) for Hs, row in table if K <= Hs]
    diagonal_ok = True
    for Hs, row in over_K:
        for t in TENSORS:
            if row[t]["viable (exact)"]:
                for v in fixed_basis([G[x] for x in Hs], t):
                    diagonal_ok &= all(i == j for (i, j) in v)
    # every pair of viable subgroups containing K: generic members, the mixing moduli (a permutation matrix)
    perm_ok = True
    nrng = np.random.default_rng(7)
    for t in TENSORS:
        vs = [Hs for Hs, row in over_K if row[t]["viable (exact)"]]
        for Hu, Hd in itertools.product(vs, vs):
            Ws = []
            for Hs in (Hu, Hd):
                basis = fixed_basis([G[x] for x in Hs], t)
                coeffs = [complex(*nrng.normal(size=2)) for _ in basis]
                M = np.zeros((3, 3), complex)
                for v, c in zip(basis, coeffs):
                    for (i, j), z in v.items():
                        val = c * sum(z[m] * np.exp(2j * np.pi * m / 24) for m in range(8))
                        M[i, j] += val
                        if t == "Sym^2 T" and i != j:
                            M[j, i] += val
                Ws.append(np.linalg.eigh(M @ M.conj().T)[1])
            A = np.abs(Ws[0].conj().T @ Ws[1])
            perm_ok &= bool(np.allclose(np.sort(A, axis=1), [[0, 0, 1]] * 3, atol=1e-9)
                            and np.allclose(np.sort(A, axis=0), [[0] * 3, [0] * 3, [1] * 3], atol=1e-9))

    def tally(t):
        vs = [row for _, row in table if row[t]["viable (exact)"]]
        return {"viable subgroups": len(vs), "their orders": sorted({r["order"] for r in vs}),
                "viable classes": len({r["class"] for r in vs}), "all abelian": all(r["abelian"] for r in vs)}

    abel = [row for _, row in table if row["abelian"]]
    nonab = [row for _, row in table if not row["abelian"]]
    orders_abelian = {}
    for r in abel:
        orders_abelian[r["order"]] = orders_abelian.get(r["order"], 0) + 1
    out = {
        "A1: the subgroup lattice": {
            "subgroups": len(subs), "conjugacy classes": len(classes),
            "abelian subgroups": len(abel), "abelian classes": len({r["class"] for r in abel}),
            "non-abelian subgroups": len(nonab), "non-abelian classes": len({r["class"] for r in nonab}),
            "abelian subgroups by order": {str(k): v for k, v in sorted(orders_abelian.items())},
            "non-abelian (order, image in the rotations, scalars)": sorted(
                [r["order"], r["its image in the rotations"], r["its scalars"]] for r in nonab)},
        "A2: viable under each tensor (exact; B1620's definition)": {t: tally(t) for t in TENSORS},
        "A2: the exact route and the criterion by hand agree on every subgroup and tensor": bool(agree),
        "A2: sectors by the number of random points passed (of 3)": {str(k): v for k, v in sorted(passes.items())},
        "A3: the elements of order 3": {
            "how many": len(order3),
            "all have c = 1 and are 3-cycles": all(r["c = 1"] and r["a 3-cycle"] for r in a3_each),
            "Sym^2 T fixed dimension along each": sorted({r["Sym^2 T fixed dimension"] for r in a3_each}),
            "none viable under Sym^2 T": all(r["points passed of 3"] == 0 for r in a3_each),
            "no viable subgroup under Sym^2 T has order divisible by 3": all(
                not (row["Sym^2 T"]["viable (exact)"] and row["order"] % 3 == 0) for _, row in table)},
        "A4: K and the subgroups containing it": {
            "the inner automorphisms' lifts in normal form": {n: [{"k": x[0], "S": [list(r) for r in x[1]]} for x in v]
                                                              for n, v in lifts.items()},
            "they act as diagonal signs (the parity grading)": bool(diag_signs),
            "K (the lifts with c = 1): order": len(K),
            "K = V4 of diagonal signs": sorted(G[x][1] for x in K) == sorted(
                [((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
                 ((-1, 0, 0), (0, 1, 0), (0, 0, -1)), ((-1, 0, 0), (0, -1, 0), (0, 0, 1))]) and all(G[x][0] == 0 for x in K),
            "all four lifts generate a group of order": len(Eall),
            "subgroups containing K": len(over_K),
            "their orders": sorted(row["order"] for _, row in over_K),
            "viable orders among them": {t: sorted(row["order"] for _, row in over_K if row[t]["viable (exact)"])
                                         for t in TENSORS},
            "every invariant matrix of every viable one is diagonal in the parity basis": bool(diagonal_ok),
            "every pair of them gives a permutation (numerical illustration)": bool(perm_ok)},
        "the class table": [],
    }
    for c, orbit in enumerate(classes):
        row = next(r for Hs, r in table if r["class"] == c)
        out["the class table"].append({"class": c, "size": len(orbit), "order": row["order"], "abelian": row["abelian"],
                                       "image in the rotations": row["its image in the rotations"],
                                       "scalars": row["its scalars"],
                                       "conjugates containing K": sum(1 for J in orbit if K <= J),
                                       **{t: row[t]["viable (exact)"] for t in TENSORS}})
    return out, idx


# ---------------------------------------------------------------- Part B

def lyndon(n):
    out = []
    for w in itertools.product("LR", repeat=n):
        s = "".join(w)
        if all(s < s[i:] + s[:i] for i in range(1, n)):
            out.append(s)
    return out


def cycles_of(p):
    out, seen = [], set()
    for i in range(3):
        if i not in seen:
            cyc, j = [], i
            while j not in seen:
                seen.add(j)
                cyc.append(j)
                j = p[j]
            out.append(cyc)
    return out


def zero_modes(x):
    """the fixed space of x = zeta_24^k S on T, exactly. x e_i = zeta^k s_i e_pi(i), so on each cycle C of pi the
    eigenvalues are the |C|-th roots of the cycle product zeta^(k |C|) prod s_i; the eigenvalue 1 occurs once exactly
    when that product is 1, with the orbit sum of e_i0 as its vector. Returns (dimension, type)."""
    k, S = x
    p = perm_of(S)
    s = [S[p[i]][i] for i in range(3)]
    vecs = []
    for cyc in cycles_of(p):
        if (k * len(cyc) + 12 * sum(1 for i in cyc if s[i] == -1)) % 24 == 0:
            v, i, ph = {}, cyc[0], 0
            for _ in cyc:
                v[i] = ph
                ph = (ph + k + (0 if s[i] == 1 else 12)) % 24
                i = p[i]
            vecs.append(v)
    d = len(vecs)
    if d == 0:
        return 0, "none"
    if d == 3:
        return 3, "all of T"
    if all(len(v) == 1 for v in vecs):
        return d, "parity line" if d == 1 else "plane of two parity lines"
    if d == 1 and len(vecs[0]) == 3:
        return 1, "body diagonal" if all(e in (0, 12) for e in vecs[0].values()) else "trimaximal line with phases"
    if d == 1 and len(vecs[0]) == 2:
        return 1, "bimaximal line"
    return d, "other"


def part_B(G, named, encode, B):
    gL, gR = named["L"], named["R"]
    (_, lL, lR) = H.lift_choices()[0]
    lifts_V = {"L": CT.on_V(CP.AUT["L"], lL), "R": CT.on_V(CP.AUT["R"], lR)}
    named_T, _ = H.triplets()
    C = named_T["T"]
    G0 = H.gram_V()
    Qt = C.conj().T @ G0 @ C
    Kc = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T

    def exact_word(w):
        x = (0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
        for ch in w:
            x = emul(x, gL if ch == "L" else gR)
        return x

    cache, rows, float_ok, b1_ok, b2_ok, rot_ok = {}, [], True, True, True, True
    by_len = {}
    for n in range(2, 13):
        for w in lyndon(n):
            x = exact_word(w)
            Y = B.conj().T @ MV.on_T(C, Kc, MV.word(lifts_V, w)) @ B
            float_ok &= bool(np.allclose(Y, np.exp(2j * np.pi * x[0] / 24) * np.array(x[1]), atol=1e-8))
            r, l = w.count("R"), w.count("L")
            b1_ok &= x[0] == (3 * (r - l)) % 24
            modes = {}
            for eps, dk in (("+g", 0), ("-g", 12)):
                y = ((x[0] + dk) % 24, x[1])
                if y not in cache:
                    cache[y] = zero_modes(y)
                modes[eps] = cache[y]
                for i in range(1, n):                        # every rotation of the word: the same type
                    z = exact_word(w[i:] + w[:i])
                    z = ((z[0] + dk) % 24, z[1])
                    if z not in cache:
                        cache[z] = zero_modes(z)
                    rot_ok &= cache[z] == cache[y]
            st = stype(x[1])
            has = any(m[0] > 0 for m in modes.values())
            b2_ok &= has == ((r - l) % 4 == 0)
            if (r - l) % 4 == 0:
                c_sign = 1 if x[0] == 0 else (-1 if x[0] == 12 else None)
                b2_ok &= c_sign is not None
                if c_sign is not None:
                    unit = modes["+g"] if c_sign == 1 else modes["-g"]    # the extension with eps c = 1
                    other = modes["-g"] if c_sign == 1 else modes["+g"]
                    expect_unit = {"face half-turn": "parity line", "3-cycle": "body diagonal", "identity": "all of T"}
                    expect_other = {"face half-turn": "plane of two parity lines", "3-cycle": "none", "identity": "none"}
                    b2_ok &= unit[1] == expect_unit.get(st) and other[1] == expect_other.get(st)
            rows.append({"word": w, "r - l": r - l, "k": x[0], "rotation": st,
                         "+g": list(modes["+g"]), "-g": list(modes["-g"])})
            t = by_len.setdefault(n, {"threads": 0, "with zero modes": 0, "with a body-diagonal zero mode": 0})
            t["threads"] += 1
            t["with zero modes"] += int(has)
            t["with a body-diagonal zero mode"] += int(any(m[1] == "body diagonal" for m in modes.values()))
    types = {}
    for r_ in rows:
        for e in ("+g", "-g"):
            types[r_[e][1]] = types.get(r_[e][1], 0) + 1
    b3_ok = set(types) <= {"none", "parity line", "plane of two parity lines", "all of T", "body diagonal"}

    # B4: the general extension diag(lambda) c S, a zero mode forced on one cycle of S's axis permutation (numerical)
    rng = np.random.default_rng(42)
    b4 = {}
    for S in rotations():
        S_ = np.array(S)
        p = perm_of(S)
        cycles = cycles_of(p)
        for cyc in cycles:
            for _ in range(3):
                lam = np.exp(2j * np.pi * rng.random(3))
                c = np.exp(2j * np.pi * rng.random())
                A = np.diag(lam) @ (c * S_)
                prod = np.prod([A[p[i], i] for i in cyc])
                lam[p[cyc[0]]] /= prod                       # make the cycle's product 1
                A = np.diag(lam) @ (c * S_)
                w_, V = np.linalg.eig(A)
                one = [i for i in range(3) if abs(w_[i] - 1) < 1e-9]
                ok = len(one) == 1
                if ok:
                    v = V[:, one[0]] / np.linalg.norm(V[:, one[0]])
                    m = np.abs(v) ** 2
                    ok = bool(np.allclose(m[cyc], 1 / len(cyc), atol=1e-9) and
                              np.allclose(np.delete(m, cyc), 0, atol=1e-9))
                key = "%s, a cycle of length %d" % (stype(S), len(cyc))
                b4[key] = b4.get(key, True) and ok

    # B5: the thread RL (Lyndon word LR): the Cesaro mean of g's powers is the zero-mode projector, every entry 1/3
    x = exact_word("LR")
    S = sp.Matrix(x[1])
    P = (sp.eye(3) + S + S * S) / 3
    v = sp.Matrix(S - sp.eye(3)).nullspace()[0]
    proj = v * v.T / (v.T * v)[0]
    b5 = {"k (c = exp(2 pi i k/24))": x[0], "rotation": stype(x[1]),
          "the mean (1 + g + g^2)/3 is the projector onto the fixed line": bool(x[0] == 0 and P == proj
                                                                                 and P * P == P and P.rank() == 1),
          "every entry has modulus 1/3": all(sp.Abs(e) == sp.Rational(1, 3) for e in P),
          "the fixed line": [int(e) for e in v]}

    examples = [r_ for r_ in rows if len(r_["word"]) <= 6]
    return {
        "the threads": "every Lyndon word in L and R of length 2 to 12 (each thread once, no covers), read as in "
                       "the_mixing_patterns_verified.word; both extensions +-g of the record's lifts",
        "how many": len(rows),
        "B1: c(w) = exp(i pi (r - l)/4) on every thread": bool(b1_ok),
        "B1: the exact product matches the float route on every thread": bool(float_ok),
        "B2: zero modes exactly when r = l mod 4, of the predicted type": bool(b2_ok),
        "B3: zero-mode spaces by type (threads x extensions)": dict(sorted(types.items())),
        "B3: every one is spanned by parity lines or is a body diagonal": bool(b3_ok),
        "B3: the type is the same for every rotation of the word": bool(rot_ok),
        "by length": {str(k): v for k, v in by_len.items()},
        "B4: the general extension's zero-mode line, by rotation and cycle (equal moduli on the cycle)": b4,
        "B5: the thread RL and main's B1621 tick": b5,
        "the threads to length 6": examples,
    }


def ring_selftest():
    i = POW[6]
    assert POW[24] == POW[0] and POW[12] == zneg(POW[0]) and zmul(i, i) == zneg(POW[0])
    assert zmul(POW[5], POW[7]) == POW[12] and zconj(POW[5]) == POW[19] and zmul(POW[5], zconj(POW[5])) == POW[0]
    z = gauss(3, -4)
    assert zmul(z, zconj(z)) == zscale(POW[0], 25)
    rt2 = zadd(POW[3], POW[21])                                   # zeta_8 + zeta_8^-1 = sqrt 2
    assert zmul(rt2, rt2) == zscale(POW[0], 2)


def main():
    ring_selftest()
    G, B, encode, named = the_group_exact()
    rot = rotations()
    Gp = sorted((k, S) for S in rot for k in range(0, 24, 3)
                if (4 * k) % 24 == (0 if parity(perm_of(S)) == 0 else 12))
    a0 = {"elements": len(G), "every k a multiple of 3 (c an eighth root of unity)": all(k % 3 == 0 for k, _ in G),
          "G equals G' = {z S : z^8 = 1, z^4 = sgn S}": G == Gp,
          "the named elements (k, rotation)": {w: [x[0], stype(x[1])] for w, x in named.items()}}
    A, idx = part_A(G, named, encode)
    Bres = part_B(G, named, encode, B)
    checks = {
        "A0: G = G'": a0["G equals G' = {z S : z^8 = 1, z^4 = sgn S}"] and a0[
            "every k a multiple of 3 (c an eighth root of unity)"],
        "A1: 68 subgroups in 26 classes; 57 abelian in 20; 11 non-abelian in 6": (
            A["A1: the subgroup lattice"]["subgroups"], A["A1: the subgroup lattice"]["conjugacy classes"],
            A["A1: the subgroup lattice"]["abelian subgroups"], A["A1: the subgroup lattice"]["abelian classes"],
            A["A1: the subgroup lattice"]["non-abelian subgroups"],
            A["A1: the subgroup lattice"]["non-abelian classes"]) == (68, 26, 57, 20, 11, 6),
        "A1: the abelian orders 1, 2, 3, 4, 6, 8, 12, 16 with 1, 7, 4, 11, 4, 19, 4, 7":
            A["A1: the subgroup lattice"]["abelian subgroups by order"] == {"1": 1, "2": 7, "3": 4, "4": 11, "6": 4,
                                                                            "8": 19, "12": 4, "16": 7},
        "A1: the non-abelian ones as predicted": A["A1: the subgroup lattice"][
            "non-abelian (order, image in the rotations, scalars)"] == sorted(
            [[12, 12, 1], [24, 12, 2], [48, 12, 4]] + [[24, 6, 4]] * 4 + [[32, 8, 4]] * 3 + [[96, 24, 4]]),
        "A2: 57 / 24 / 16 viable, all abelian": [A["A2: viable under each tensor (exact; B1620's definition)"][t][
            "viable subgroups"] for t in TENSORS] == [57, 24, 16] and all(
            A["A2: viable under each tensor (exact; B1620's definition)"][t]["all abelian"] for t in TENSORS),
        "A2: the orders as predicted": [A["A2: viable under each tensor (exact; B1620's definition)"][t][
            "their orders"] for t in TENSORS] == [[1, 2, 3, 4, 6, 8, 12, 16], [1, 2, 3, 4, 6, 8], [1, 2, 4, 8]],
        "A2: the two routes agree": A["A2: the exact route and the criterion by hand agree on every subgroup and tensor"],
        "A3: no order-3 residual under Sym^2 T": A["A3: the elements of order 3"]["how many"] == 8 and A[
            "A3: the elements of order 3"]["all have c = 1 and are 3-cycles"] and A["A3: the elements of order 3"][
            "none viable under Sym^2 T"] and A["A3: the elements of order 3"][
            "no viable subgroup under Sym^2 T has order divisible by 3"] and A["A3: the elements of order 3"][
            "Sym^2 T fixed dimension along each"] == [2],
        "A4: K = V4, 10 subgroups contain it, viable orders as predicted, every pattern a permutation": (
            A["A4: K and the subgroups containing it"]["they act as diagonal signs (the parity grading)"]
            and A["A4: K and the subgroups containing it"]["K = V4 of diagonal signs"]
            and A["A4: K and the subgroups containing it"]["all four lifts generate a group of order"] == 8
            and A["A4: K and the subgroups containing it"]["subgroups containing K"] == 10
            and A["A4: K and the subgroups containing it"]["their orders"] == [4, 8, 12, 16, 24, 32, 32, 32, 48, 96]
            and A["A4: K and the subgroups containing it"]["viable orders among them"] == {
                "T-bar (x) T": [4, 8, 16], "T (x) T": [4, 8], "Sym^2 T": [4, 8]}
            and A["A4: K and the subgroups containing it"][
                "every invariant matrix of every viable one is diagonal in the parity basis"]
            and A["A4: K and the subgroups containing it"]["every pair of them gives a permutation (numerical illustration)"]),
        "B1": Bres["B1: c(w) = exp(i pi (r - l)/4) on every thread"] and Bres[
            "B1: the exact product matches the float route on every thread"] and Bres["how many"] == 745,
        "B2": Bres["B2: zero modes exactly when r = l mod 4, of the predicted type"],
        "B3": Bres["B3: every one is spanned by parity lines or is a body diagonal"] and Bres[
            "B3: the type is the same for every rotation of the word"],
        "B4": all(Bres["B4: the general extension's zero-mode line, by rotation and cycle (equal moduli on the cycle)"]
                  .values()),
        "B5": Bres["B5: the thread RL and main's B1621 tick"][
            "the mean (1 + g + g^2)/3 is the projector onto the fixed line"] and Bres[
            "B5: the thread RL and main's B1621 tick"]["every entry has modulus 1/3"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    out = {"status": "W42: Part A a VERIFICATION of main's B1620 (read first), from this seat's construction; Part B a "
                     "census of every thread to length 12 (main's ask 2)",
           "A0: the group": a0, **A, "Part B: the threads' own zero modes": Bres, "checks": checks,
           "every check holds": all(checks.values())}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=1))
    print("every check holds:", all(checks.values()))


if __name__ == "__main__":
    main()
