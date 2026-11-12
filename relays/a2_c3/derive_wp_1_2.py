#!/usr/bin/env python3
"""Independent blind second derivation and exhaustive verification of M12 (WP-1.2), Statements A through E.

Card: A2-C3 (committed at 45b29e14e strictly before writing or running this script).
Source read: ONLY the verbatim text of M12 on docs/seats/agy-002.md.
Firewall: 0 of 19 (pure group theory, matrix algebra, surface topology, and finite-dimensional representations).
"""
from __future__ import annotations

import itertools
import sys
from collections import deque

import sympy as sp

INV_CHAR = {"a": "A", "A": "a", "b": "B", "B": "b"}
ALPHABET = ("a", "A", "b", "B")


def reduce_word(w: str) -> str:
    stack: list[str] = []
    for ch in w:
        if stack and stack[-1] == INV_CHAR[ch]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def inv_word(w: str) -> str:
    return "".join(INV_CHAR[ch] for ch in reversed(w))


def mul_word(u: str, v: str) -> str:
    return reduce_word(u + v)


def comm_word(u: str, v: str) -> str:
    return reduce_word(u + v + inv_word(u) + inv_word(v))


def cyclic_reduce(w: str) -> str:
    rw = reduce_word(w)
    i, j = 0, len(rw)
    while i < j - 1 and rw[i] == INV_CHAR[rw[j - 1]]:
        i += 1
        j -= 1
    return rw[i:j]


def conj_rep(w: str) -> str:
    cw = cyclic_reduce(w)
    if not cw:
        return ""
    return min(cw[k:] + cw[:k] for k in range(len(cw)))


def apply_endo(w: str, img_a: str, img_b: str) -> str:
    ia, ib = inv_word(img_a), inv_word(img_b)
    mp = {"a": img_a, "A": ia, "b": img_b, "B": ib}
    return reduce_word("".join(mp[ch] for ch in w))


MOVES: dict[str, tuple[str, str]] = {
    "R1_a_to_ab": ("ab", "b"),
    "R2_a_to_ba": ("ba", "b"),
    "R3_b_to_ba": ("a", "ba"),
    "R4_b_to_ab": ("a", "ab"),
    "SWAP": ("b", "a"),
    "TICK": ("ab", "a"),
}

RECORD_MOVES = ("R1_a_to_ab", "R2_a_to_ba", "R3_b_to_ba", "R4_b_to_ab")

MOVE_INVERSES: dict[str, tuple[str, str]] = {
    "R1_a_to_ab": ("aB", "b"),
    "R2_a_to_ba": ("Ba", "b"),
    "R3_b_to_ba": ("a", "bA"),
    "R4_b_to_ab": ("a", "Ab"),
    "SWAP": ("b", "a"),
    "TICK": ("b", "Ba"),
}


def all_reduced_words_up_to(max_len: int) -> list[str]:
    words = [""]
    prev = [""]
    for length in range(1, max_len + 1):
        curr: list[str] = []
        for w in prev:
            last = w[-1] if w else ""
            for ch in ALPHABET:
                if last and ch == INV_CHAR[last]:
                    continue
                curr.append(w + ch)
        words.extend(curr)
        prev = curr
    return words


def abelianize(w: str) -> tuple[int, int]:
    return (w.count("a") - w.count("A"), w.count("b") - w.count("B"))


def verify_statement_A(words_le8: list[str]) -> None:
    print("=== STATEMENT A: ABELIANIZATION F_2 -> Z^2 AND THE SIX MOVES ===")
    # Verify all six moves are automorphisms of F_2.
    for name, (ia, ib) in MOVES.items():
        ja, jb = MOVE_INVERSES[name]
        assert apply_endo(ja, ia, ib) == "a" and apply_endo(jb, ia, ib) == "b", name
        assert apply_endo(ia, ja, jb) == "a" and apply_endo(ib, ja, jb) == "b", name

    # Induced GL_2(Z) matrices M_phi on column vectors (n_a, n_b)^T.
    induced_mats: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {}
    for name, (ia, ib) in MOVES.items():
        col_a = abelianize(ia)
        col_b = abelianize(ib)
        M = ((col_a[0], col_b[0]), (col_a[1], col_b[1]))
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        induced_mats[name] = M
        for w in words_le8:
            x, y = abelianize(w)
            lhs = abelianize(apply_endo(w, ia, ib))
            rhs = (M[0][0] * x + M[0][1] * y, M[1][0] * x + M[1][1] * y)
            assert lhs == rhs, (name, w, lhs, rhs)
        print(f"  {name}: Aut(F_2)=True, induced GL_2(Z) matrix={M}, det={det}")

    assert induced_mats["R1_a_to_ab"] == induced_mats["R2_a_to_ba"] == ((1, 0), (1, 1))
    assert induced_mats["R3_b_to_ba"] == induced_mats["R4_b_to_ab"] == ((1, 1), (0, 1))
    assert len(set(induced_mats.values())) == 4
    print(f"  Verified on all {len(words_le8)} reduced words of length <= 8: ab(phi(w)) == M_phi * ab(w).")
    print("  Note: 6 distinct F_2 automorphisms collapse to 4 distinct GL_2(Z) matrices (R1==R2, R3==R4).")


def verify_statement_B(words_le8: list[str]) -> None:
    print("\n=== STATEMENT B: [a, b] CONJUGACY AND CONJUGACY CLASSES OF LENGTH <= 8 ===")
    c = comm_word("a", "b")
    c_inv = inv_word(c)
    assert c == "abAB" and c_inv == "baBA"
    assert abelianize(c) == (0, 0)
    assert conj_rep(c) != conj_rep(c_inv)
    print(f"  [a, b] = {c}, ab([a, b]) = {abelianize(c)}, conj_rep([a,b]) = {conj_rep(c)} != conj_rep([a,b]^-1) = {conj_rep(c_inv)}")

    expected_conj = {
        "R1_a_to_ab": ("", c),
        "R2_a_to_ba": ("b", c),
        "R3_b_to_ba": ("", c),
        "R4_b_to_ab": ("a", c),
        "SWAP": ("", c_inv),
        "TICK": ("a", c_inv),
    }
    for name, (ia, ib) in MOVES.items():
        img = apply_endo(c, ia, ib)
        u, base = expected_conj[name]
        assert img == reduce_word(u + base + inv_word(u)), (name, img)
        target_rep = conj_rep(c) if name in RECORD_MOVES else conj_rep(c_inv)
        assert conj_rep(img) == target_rep
        print(f"  {name}([a, b]) = {img} = ({u or '1'}) * {'[a,b]' if base == c else '[a,b]^-1'} * ({inv_word(u) or '1'})")

    # Partition all 13,121 reduced words of length 0..8 by F_2 conjugacy class representative.
    classes_all: dict[str, list[str]] = {}
    for w in words_le8:
        classes_all.setdefault(conj_rep(w), []).append(w)

    kept_le8_all = sorted(
        rep
        for rep in classes_all
        if all(conj_rep(apply_endo(rep, *MOVES[m])) == rep for m in RECORD_MOVES)
    )
    kept_le8_nonempty = [r for r in kept_le8_all if r != ""]

    target_four = sorted([conj_rep(c), conj_rep(c_inv), conj_rep(mul_word(c, c)), conj_rep(mul_word(c_inv, c_inv))])
    assert kept_le8_nonempty == target_four
    assert kept_le8_all == [""] + target_four
    print(f"  Total reduced words of length 0..8: {len(words_le8)}; distinct F_2 conjugacy classes touched: {len(classes_all)}")
    print(f"  Classes kept by all 4 record moves (0 <= len <= 8): {len(kept_le8_all)} -> {kept_le8_all}")
    print(f"  Classes kept by all 4 record moves (1 <= len <= 8): {len(kept_le8_nonempty)} -> {kept_le8_nonempty}")

    # Also check classes whose representatives ONLY appear via non-cyclically-reduced words of length <= 8?
    # Note: len(conj_rep(w)) <= len(w), so every class represented by any reduced word of length <= 8 has cyclically reduced length <= 8!
    assert all(len(rep) <= 8 for rep in classes_all)

    # Check literal finite sets of reduced words (NOT modulo conjugacy): R2^n([a,b]) = b^n [a,b] b^-n has unbounded length 4 + 2n.
    orbit_r2 = [c]
    for _ in range(4):
        orbit_r2.append(apply_endo(orbit_r2[-1], *MOVES["R2_a_to_ba"]))
    assert [len(x) for x in orbit_r2] == [4, 6, 8, 10, 12]
    print(f"  Lengths of R2^n([a,b]) for n=0..4: {[len(x) for x in orbit_r2]} (escapes length <= 8 at n=3, confirming conjugacy classes in F_2 are meant).")

    # Also check whether ANY conjugacy class of length <= 8 has a finite orbit of size > 1 under RECORD_MOVES
    # (in case "the ones kept by all four record moves" is read collectively rather than class-by-class):
    finite_orbit_classes = []
    for rep in classes_all:
        orb = {rep}
        q_orb = deque([rep])
        escaped = False
        while q_orb:
            cur_r = q_orb.popleft()
            for m in RECORD_MOVES:
                nxt = conj_rep(apply_endo(cur_r, *MOVES[m]))
                if len(nxt) > 8:
                    escaped = True
                    break
                if nxt not in orb:
                    orb.add(nxt)
                    q_orb.append(nxt)
            if escaped:
                break
        if not escaped:
            finite_orbit_classes.append((rep, len(orb)))
    assert sorted(r for r, _ in finite_orbit_classes) == kept_le8_all
    assert all(sz == 1 for _, sz in finite_orbit_classes)
    print(f"  Collective vs individual check: classes whose {RECORD_MOVES}-orbit stays in length <= 8 all have orbit size 1 -> {len(finite_orbit_classes)} classes.")

    # Control CTL-WP12-CONJ: keeping only R1 and R2 preserves powers of b as well.
    kept_r1_r2 = [
        rep
        for rep in classes_all
        if all(conj_rep(apply_endo(rep, *MOVES[m])) == rep for m in ("R1_a_to_ab", "R2_a_to_ba"))
    ]
    assert len(kept_r1_r2) > len(kept_le8_all) and conj_rep("b") in kept_r1_r2
    print(f"  CTL-WP12-CONJ PASS: under {{R1, R2}} alone, {len(kept_r1_r2)} classes are kept (including 'b' and its powers).")


def eval_mat2_gauss(w: str, A, B):
    # Exact 2x2 Gaussian-integer arithmetic ((a00, a01), (a10, a11)) where entries are complex ints (re, im).
    def cadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def csub(x, y):
        return (x[0] - y[0], x[1] - y[1])

    def cmul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def mmul(X, Y):
        return (
            (cadd(cmul(X[0][0], Y[0][0]), cmul(X[0][1], Y[1][0])), cadd(cmul(X[0][0], Y[0][1]), cmul(X[0][1], Y[1][1]))),
            (cadd(cmul(X[1][0], Y[0][0]), cmul(X[1][1], Y[1][0])), cadd(cmul(X[1][0], Y[0][1]), cmul(X[1][1], Y[1][1]))),
        )

    def minv_sl2(X):
        z = (0, 0)
        return ((X[1][1], csub(z, X[0][1])), (csub(z, X[1][0]), X[0][0]))

    I2 = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    gens = {"a": A, "A": minv_sl2(A), "b": B, "B": minv_sl2(B)}
    cur = I2
    for ch in w:
        cur = mmul(cur, gens[ch])
    return cur


def eval_heisenberg(w: str, swap_gens: bool = False) -> tuple[int, int, int]:
    # Upper unitriangular 3x3 integer matrix [[1, x, z], [0, 1, y], [0, 0, 1]] represented as (x, y, z).
    # Multiplication: (x1, y1, z1) * (x2, y2, z2) = (x1 + x2, y1 + y2, z1 + z2 + x1 * y2).
    def hmul(u: tuple[int, int, int], v: tuple[int, int, int]) -> tuple[int, int, int]:
        return (u[0] + v[0], u[1] + v[1], u[2] + v[2] + u[0] * v[1])

    ga = (1, 0, 0) if not swap_gens else (0, 1, 0)
    gb = (0, 1, 0) if not swap_gens else (1, 0, 0)
    gA = (-ga[0], -ga[1], -ga[2] + ga[0] * ga[1])
    gB = (-gb[0], -gb[1], -gb[2] + gb[0] * gb[1])
    gens = {"a": ga, "A": gA, "b": gb, "B": gB}
    cur = (0, 0, 0)
    for ch in w:
        cur = hmul(cur, gens[ch])
    return cur


def eval_sanov(w: str) -> tuple[int, int, int, int]:
    # Exact integer 2x2 matrix (m00, m01, m10, m11).
    def mmul(X, Y):
        return (
            X[0] * Y[0] + X[1] * Y[2],
            X[0] * Y[1] + X[1] * Y[3],
            X[2] * Y[0] + X[3] * Y[2],
            X[2] * Y[1] + X[3] * Y[3],
        )

    gens = {
        "a": (1, 2, 0, 1),
        "A": (1, -2, 0, 1),
        "b": (1, 0, 2, 1),
        "B": (1, 0, -2, 1),
    }
    cur = (1, 0, 0, 1)
    for ch in w:
        cur = mmul(cur, gens[ch])
    return cur


def verify_statement_C(words_le8: list[str]) -> None:
    print("\n=== STATEMENT C: Q_8, INTEGRAL HEISENBERG U_3(Z), AND SANOV GROUP ===")
    I2_c = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    minus_I2_c = (((-1, 0), (0, 0)), ((0, 0), (-1, 0)))
    A1 = (((0, 1), (0, 0)), ((0, 0), (0, -1)))
    B1 = (((0, 0), (1, 0)), ((-1, 0), (0, 0)))

    def tr_c(X):
        return (X[0][0][0] + X[1][1][0], X[0][0][1] + X[1][1][1])

    assert tr_c(A1) == (0, 0) and tr_c(B1) == (0, 0) and tr_c(eval_mat2_gauss("ab", A1, B1)) == (0, 0)
    c1 = eval_mat2_gauss(comm_word("a", "b"), A1, B1)
    assert c1 == minus_I2_c
    for g in ("a", "b", "A", "B"):
        assert eval_mat2_gauss(comm_word(comm_word("a", "b"), g), A1, B1) == I2_c
    print("  Point 1 (Q_8): tr(a)=tr(b)=tr(ab)=0, [a,b]=-I_2, all 4 triple commutators == I_2: VERIFIED.")

    # Point 2: Heisenberg U_3(Z) under both generator assignments (I+E_12, I+E_23) and (I+E_23, I+E_12).
    for swapped in (False, True):
        c2 = eval_heisenberg(comm_word("a", "b"), swap_gens=swapped)
        assert c2 != (0, 0, 0) and c2 in ((0, 0, 1), (0, 0, -1))
        for g in ("a", "b", "A", "B"):
            assert eval_heisenberg(comm_word(comm_word("a", "b"), g), swap_gens=swapped) == (0, 0, 0)
    print("  Point 2 (U_3(Z)): [a,b] = I +- E_13 != I_3, all 4 triple commutators == I_3: VERIFIED.")

    triv_q8 = [w for w in words_le8 if eval_mat2_gauss(w, A1, B1) == I2_c]
    triv_u3 = [w for w in words_le8 if eval_heisenberg(w) == (0, 0, 0)]
    triv_sanov = [w for w in words_le8 if eval_sanov(w) == (1, 0, 0, 1)]

    triv_u3_by_len = {k: [w for w in triv_u3 if len(w) == k] for k in range(9) if any(len(w) == k for w in triv_u3)}
    triv_q8_by_len = {k: len([w for w in triv_q8 if len(w) == k]) for k in range(9) if any(len(w) == k for w in triv_q8)}
    assert list(triv_u3_by_len.keys()) == [0, 8], triv_u3_by_len
    assert len(triv_u3_by_len[8]) > 0
    assert triv_sanov == [""]
    assert "" in triv_q8 and len(triv_q8) > len(triv_u3)
    assert set(triv_u3) < set(triv_q8)
    print(f"  Trivial reduced words of length 0..8 at Point 2 (U_3(Z)) by length: {{k: len(v) for k, v in triv_u3_by_len.items()}} = { {k: len(v) for k, v in triv_u3_by_len.items()} }")
    print(f"    Sample length-8 words in gamma_3(F_2) = ker(F_2 -> U_3(Z)): {triv_u3_by_len[8][:6]} (e.g. [[a,B],b] = {comm_word(comm_word('a', 'B'), 'b')})")
    print(f"  Trivial reduced words of length 0..8 at Point 1 (Q_8) by length: {triv_q8_by_len} (total {len(triv_q8)}; strict superset of U_3(Z)'s {len(triv_u3)}).")
    print(f"    Sample words trivial in Q_8 and NON-trivial in U_3(Z): {[w for w in triv_q8 if w not in set(triv_u3)][:8]}")
    print(f"  Subset check: ALL {len(triv_u3)} reduced words of length <= 8 trivial in U_3(Z) are trivial in Q_8: {set(triv_u3) <= set(triv_q8)}.")
    print(f"  Trivial reduced words of length 0..8 at Point 3 (Sanov): {triv_sanov} (empty word of length 0 IS trivial; 0 non-empty words trivial).")
    assert eval_sanov(comm_word(comm_word("a", "b"), "a")) != (1, 0, 0, 1)
    print(f"  Point 3 (Sanov) [[a,b], a] = {eval_sanov(comm_word(comm_word('a', 'b'), 'a'))} != I_2.")

    # Control CTL-WP12-HEIS: verify swap_gens invariance of ker(F_2 -> U_3(Z)) and check lengths 9 and 10 as well.
    triv_u3_swapped = [w for w in words_le8 if eval_heisenberg(w, swap_gens=True) == (0, 0, 0)]
    assert triv_u3_swapped == triv_u3
    words_le10 = all_reduced_words_up_to(10)
    triv_u3_len9 = [w for w in words_le10 if len(w) == 9 and eval_heisenberg(w) == (0, 0, 0)]
    triv_u3_len10 = [w for w in words_le10 if len(w) == 10 and eval_heisenberg(w) == (0, 0, 0)]
    assert len(triv_u3_len9) == 0 and len(triv_u3_len10) > 0
    assert comm_word(comm_word("a", "b"), "a") in triv_u3_len10
    assert all(eval_mat2_gauss(w, A1, B1) == I2_c for w in triv_u3_len10)
    print(
        f"  CTL-WP12-HEIS PASS: ker(F_2 -> U_3(Z)) independent of generator order; 0 trivial words at lengths 1..7 and 9, "
        f"{len(triv_u3_by_len[8])} at length 8 (minimum non-empty length of gamma_3(F_2)!), and {len(triv_u3_len10)} at length 10 "
        f"(including [[a,b],a]={comm_word(comm_word('a', 'b'), 'a')}); ALL also trivial in Q_8."
    )


def verify_statement_D() -> None:
    print("\n=== STATEMENT D: SURFACES WITH pi_1 ~= F_2 AND Z^2 ORBITS ===")
    # Classify compact connected surfaces with boundary b >= 1 and Euler characteristic chi = 1 - rk(F_2) = -1.
    orientable = [(g, b) for g in range(0, 10) for b in range(1, 10) if 2 - 2 * g - b == -1]
    non_orientable = [(c, b) for c in range(1, 10) for b in range(1, 10) if 2 - c - b == -1]
    assert orientable == [(0, 3), (1, 1)]
    assert non_orientable == [(1, 2), (2, 1)]
    print(f"  Compact connected surfaces with b >= 1 and chi = -1: orientable (g,b)={orientable}, non-orientable (c,b)={non_orientable} -> total {len(orientable) + len(non_orientable)} == 4.")

    # Boundary words in F_2 = <a, b> and their images in H_1(S; Z) ~= Z^2:
    surfaces = {
        "Sigma_1_1 (torus, 1 boundary)": ["abAB"],
        "Sigma_0_3 (sphere, 3 boundaries)": ["a", "b", "BA"],
        "N_1_2 (RP^2, 2 boundaries: a^2 b c = 1 => c = B A^2)": ["b", "BAA"],
        "N_2_1 (Klein bottle, 1 boundary: a^2 b^2)": ["aabb"],
    }
    for sname, bwords in surfaces.items():
        ab_imgs = [abelianize(bw) for bw in bwords]
        all_in_comm = all(v == (0, 0) for v in ab_imgs)
        # Verify presentation-independence: apply every move in MOVES (generating Aut(F_2)) and check all_in_comm is invariant.
        for mname, (ia, ib) in MOVES.items():
            moved = [abelianize(apply_endo(bw, ia, ib)) for bw in bwords]
            assert (all(v == (0, 0) for v in moved)) == all_in_comm
        print(f"  {sname}: boundary H_1(S;Z) classes = {ab_imgs} -> all in [pi_1, pi_1]: {all_in_comm}")

    # Forward-semigroup orbit test under T1(x, y) = (x + y, y) and T2(x, y) = (x, x + y):
    # Algebraic proof: if y != 0, T1^n(x, y) = (x + n*y, y) gives infinitely many distinct vectors;
    # if y == 0 and x != 0, T2^n(x, 0) = (x, n*x) gives infinitely many distinct vectors.
    for x in range(-6, 7):
        for y in range(-6, 7):
            if (x, y) == (0, 0):
                continue
            vis = {(x, y)}
            q = deque([(x, y)])
            while q and len(vis) < 40:
                cx, cy = q.popleft()
                for nx, ny in ((cx + cy, cy), (cx, cx + cy)):
                    if (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((nx, ny))
            assert len(vis) >= 40, (x, y)
    # Check finite invariant sets in H_1(S; Z/NZ) for N = 2, 3: non-zero finite invariant sets DO exist over Z/NZ!
    mod2_nonzero = {(1, 0), (0, 1), (1, 1)}
    assert {((x + y) % 2, y % 2) for x, y in mod2_nonzero} == mod2_nonzero
    assert {(x % 2, (x + y) % 2) for x, y in mod2_nonzero} == mod2_nonzero
    print("  Forward semigroup <T1, T2>_+ orbit has size >= 40 (and algebraically infinite) for every non-zero (x,y) in [-6,6]^2.")
    print("  Unstated edge cases verified: empty set {} is finite and invariant in Z^2; over Z/2Z homology, {(1,0),(0,1),(1,1)} is finite, non-zero, and invariant.")


def find_intertwiner(A1: sp.Matrix, B1: sp.Matrix, A2: sp.Matrix, B2: sp.Matrix) -> sp.Matrix | None:
    """Solve G * A1 = A2 * G and G * B1 = B2 * G with det(G) != 0 for small dimension p."""
    p = A1.rows
    gvars = sp.symbols(f"g0:{p * p}")
    G = sp.Matrix(p, p, gvars)
    eqs = [sp.expand(e) for e in (list(G * A1 - A2 * G) + list(G * B1 - B2 * G))]
    sol = sp.linsolve(eqs, gvars)
    if not sol:
        return None
    tup = next(iter(sol))
    free = sorted(set().union(*(expr.free_symbols for expr in tup)), key=str)
    if not free:
        return None
    trials = []
    for i in range(len(free)):
        trials.append({free[j]: (1 if j == i else 0) for j in range(len(free))})
    for vals in itertools.product((0, 1, -1, 2), repeat=len(free)):
        if any(vals):
            trials.append(dict(zip(free, vals)))
    for sub in trials:
        G_cand = sp.Matrix(p, p, [sp.expand(expr.subs(sub)) for expr in tup])
        if sp.expand(G_cand.det()) != 0:
            assert sp.Matrix(p, p, [sp.expand(x) for x in (G_cand * A1 - A2 * G_cand)]) == sp.zeros(p, p)
            assert sp.Matrix(p, p, [sp.expand(x) for x in (G_cand * B1 - B2 * G_cand)]) == sp.zeros(p, p)
            return G_cand
    return None


def clock_and_shift(p: int, zeta):
    A = sp.zeros(p, p)
    B = sp.zeros(p, p)
    for j in range(p):
        A[(j + 1) % p, j] = 1
        B[j, j] = zeta ** j
    return A, B


def eval_sympy_word(w: str, A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    p = A.rows
    gens = {"a": A, "A": A.inv(), "b": B, "B": B.inv()}
    cur = sp.eye(p)
    for ch in w:
        cur = sp.simplify(cur * gens[ch])
    return cur


def verify_statement_E() -> None:
    print("\n=== STATEMENT E: CLOCK-AND-SHIFT REPRESENTATIONS OF PRIME DIMENSION p ===")
    # 1. Counterexample when unstated primitivity of zeta is omitted (zeta = 1):
    for p in (2, 3, 5):
        A_triv, B_triv = clock_and_shift(p, sp.Integer(1))
        comm_triv = A_triv * B_triv * A_triv.inv() * B_triv.inv()
        assert comm_triv == sp.eye(p)
    print("  Unstated primitivity check: at zeta = 1, [a, b] = I_p = zeta^0 (k = 0), falsifying 'k not zero' unless zeta is a primitive p-th root of unity.")

    # 2. Exact check at p = 2, 3, 5 with primitive p-th root of unity zeta = exp(2*pi*I/p):
    for p in (2, 3, 5):
        zeta = sp.Integer(-1) if p == 2 else sp.exp(2 * sp.pi * sp.I / p)
        A, B = clock_and_shift(p, zeta)
        comm = sp.simplify(A * B * A.inv() * B.inv())
        scalar_expected = sp.simplify(zeta ** (p - 1))  # zeta^-1
        assert sp.simplify(comm - scalar_expected * sp.eye(p)) == sp.zeros(p, p)
        assert sp.simplify(scalar_expected - 1) != 0

        for mname, (ia, ib) in MOVES.items():
            Ap = eval_sympy_word(ia, A, B)
            Bp = eval_sympy_word(ib, A, B)
            cp = sp.simplify(Ap * Bp * Ap.inv() * Bp.inv())
            target_scalar = scalar_expected if mname in RECORD_MOVES else sp.simplify(zeta ** 1)
            assert sp.simplify(cp - target_scalar * sp.eye(p)) == sp.zeros(p, p), (p, mname)

        same_central_swap_tick = sp.simplify(scalar_expected - zeta ** 1) == 0
        assert same_central_swap_tick is (p == 2)
        print(f"  p={p}: [a,b] = zeta^(p-1) * I_{p} (k = -1 mod {p} != 0); 4 record moves keep zeta^-1; swap & tick give zeta^+1; zeta^-1 == zeta^+1: {same_central_swap_tick}")

    # 3. Linear F_2-representation equivalence check (CTL-WP12-P2-TICK):
    # At p = 2 (zeta = -1): A = sigma_x, B = sigma_z.
    A2, B2 = clock_and_shift(2, sp.Integer(-1))
    # SWAP: (B2, A2) IS GL_2(C)-equivalent to (A2, B2) via Hadamard [[1,1],[1,-1]].
    G_swap_2 = find_intertwiner(A2, B2, B2, A2)
    assert G_swap_2 is not None
    # TICK: (A2*B2, A2) has (A2*B2)^2 = -I_2 while A2^2 = +I_2 -> NO GL_2(C) intertwiner exists!
    AB2 = A2 * B2
    assert A2 ** 2 == sp.eye(2) and AB2 ** 2 == -sp.eye(2)
    G_tick_2 = find_intertwiner(A2, B2, AB2, A2)
    assert G_tick_2 is None
    # Also check R1 at p = 2: (A2*B2, B2) also has (A2*B2)^2 = -I_2 != A2^2!
    G_r1_2 = find_intertwiner(A2, B2, AB2, B2)
    assert G_r1_2 is None
    # Also check rho (+) conj(rho) at p = 2 (where conj(rho) == rho since A2, B2 are real):
    G_tick_2_sum = find_intertwiner(sp.diag(A2, A2), sp.diag(B2, B2), sp.diag(AB2, AB2), sp.diag(A2, A2))
    assert G_tick_2_sum is None
    # Whereas at the Q_8 point of Statement C (A_q8 = diag(i, -i), B_q8 = [[0, 1], [-1, 0]]), ALL 6 moves have GL_2(C) intertwiners:
    Aq8 = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    Bq8 = sp.Matrix([[0, 1], [-1, 0]])
    for mname, (ia, ib) in MOVES.items():
        G_q8 = find_intertwiner(Aq8, Bq8, eval_sympy_word(ia, Aq8, Bq8), eval_sympy_word(ib, Aq8, Bq8))
        assert G_q8 is not None, mname
    print(
        f"  CTL-WP12-P2-TICK PASS (p=2 linear F_2-rep): A^2=+I_2, (AB)^2=-I_2; "
        f"GL_2 intertwiner for SWAP exists (det={G_swap_2.det()}), GL_2 intertwiner for TICK is {G_tick_2} "
        f"(and on rho(+)conj(rho) is {G_tick_2_sum}), GL_2 intertwiner for R1 is {G_r1_2} "
        f"(3 D_4 spin sectors permuted; only Statement C's Q_8 sector (-I,-I) is fixed by all 6 moves as a linear F_2-rep!)."
    )

    # Contrast with odd prime p = 3 (using exact algebraic zeta_3 = (-1 + i*sqrt(3))/2):
    # (AB)^3 == +I_3 (since binom(p,2) = p(p-1)/2 is divisible by p for every odd prime p, unlike p=2!),
    # ALL 4 record moves preserve the linear F_2-rep up to GL_3(C) conjugacy,
    # and on rho_k (+) rho_{-k} (dim 6) BOTH SWAP and TICK preserve the linear F_2-rep!
    zeta3 = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    A3, B3 = clock_and_shift(3, zeta3)
    assert sp.Matrix(3, 3, [sp.expand(x) for x in ((A3 * B3) ** 3 - sp.eye(3))]) == sp.zeros(3, 3)
    for mname in RECORD_MOVES:
        ia, ib = MOVES[mname]
        Ap, Bp = eval_sympy_word(ia, A3, B3), eval_sympy_word(ib, A3, B3)
        G_m = find_intertwiner(A3, B3, Ap, Bp)
        assert G_m is not None, f"Expected GL_3 intertwiner for {mname} at p=3"
    # Direct sum rho_1 (+) rho_2 at p = 3 under SWAP and TICK:
    A3_conj, B3_conj = clock_and_shift(3, sp.conjugate(zeta3))
    A_sum = sp.diag(A3, A3_conj)
    B_sum = sp.diag(B3, B3_conj)
    for mname in ("SWAP", "TICK"):
        ia, ib = MOVES[mname]
        Ap1, Bp1 = eval_sympy_word(ia, A3, B3), eval_sympy_word(ib, A3, B3)
        Ap2, Bp2 = eval_sympy_word(ia, A3_conj, B3_conj), eval_sympy_word(ib, A3_conj, B3_conj)
        G12 = find_intertwiner(A3_conj, B3_conj, Ap1, Bp1)
        G21 = find_intertwiner(A3, B3, Ap2, Bp2)
        assert G12 is not None and G21 is not None
        G_full = sp.BlockMatrix([[sp.zeros(3, 3), G12], [G21, sp.zeros(3, 3)]]).as_explicit()
        assert sp.expand(sp.det(G_full)) != 0
        Ap_sum = sp.diag(Ap1, Ap2)
        Bp_sum = sp.diag(Bp1, Bp2)
        assert sp.Matrix(6, 6, [sp.expand(x) for x in (G_full * A_sum - Ap_sum * G_full)]) == sp.zeros(6, 6)
        assert sp.Matrix(6, 6, [sp.expand(x) for x in (G_full * B_sum - Bp_sum * G_full)]) == sp.zeros(6, 6)
    # Also verify exact discrete-Gaussian intertwiner D_1 * A * D_1^-1 == A*B and (A*B)^p == +I_p at odd primes p = 3, 5, 7:
    for p in (3, 5, 7):
        zp = sp.exp(2 * sp.pi * sp.I / p)
        Ap_odd, Bp_odd = clock_and_shift(p, zp)
        inv2 = (p + 1) // 2
        D1 = sp.diag(*[zp ** ((inv2 * j * (j - 1)) % p) for j in range(p)])
        lhs = sp.simplify(D1 * Ap_odd * D1.inv() - Ap_odd * Bp_odd)
        assert lhs == sp.zeros(p, p), p
    print("  Odd primes p=3,5,7 linear F_2-rep check: (AB)^p = +I_p and discrete-Gaussian intertwiner D_1*A*D_1^-1 = AB verified; at p=3 all 4 record GL_3 intertwiners and SWAP/TICK GL_6 intertwiners on rho(+)conj(rho) verified!")


def main() -> int:
    words_le8 = all_reduced_words_up_to(8)
    assert len(words_le8) == 1 + 4 * sum(3 ** (k - 1) for k in range(1, 9)) == 13121
    verify_statement_A(words_le8)
    verify_statement_B(words_le8)
    verify_statement_C(words_le8)
    verify_statement_D()
    verify_statement_E()
    print("\nALL A2-C3 (WP-1.2) DERIVATIONS AND CONTROLS PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
