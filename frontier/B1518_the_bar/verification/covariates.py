"""B1518 -- the covariates of the generated word states: cheap invariants of each monodromy, computed before any outcome.

For every signed word state s = (eps, w) to length 12 (GENESIS v1.1 section 3; 758 states, 536 manifolds):
  length, sign, signed trace t, the fibre torsion group G = coker(eps A(w) - I) with its Smith invariant factors (d1 | d2),
  |G| = abs(2 - t) (the number of fibre characters the monodromy fixes), its exponent, its p-ranks for p = 2, 3, 5, 7,
  the reversal class (closed or paired; palindromic or antipalindromic when closed), the manifold key (rotation, swap and
  reversal; B1517), and, with --snappy, volume, symmetry-group order and amphichirality.

These are not outcomes: nothing here reads any frame's firing. The control `main_torsion_agrees` compares |G| with the
torsion main's B1439 lists for each state it reports (a banked identity this code must reproduce).

    python3 covariates.py            # integers only
    python3 covariates.py --snappy   # adds volume and symmetry (about a minute)
    python3 covariates.py --snappy --write   # writes covariates.json
"""
import itertools
import json
import math
import pathlib
import sys
import warnings

HERE = pathlib.Path(__file__).resolve().parent
L, R, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
SW = str.maketrans("LR", "RL")


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def word(w):
    M = I2
    for c in w:
        M = mul(M, L if c == "L" else R)
    return M


def primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n))


def rots(w):
    return [w[i:] + w[:i] for i in range(len(w))]


def canon_state(w):
    return min(min(rots(x)) for x in (w, w.translate(SW)))


def canon_manifold(w):
    xs = [w, w.translate(SW)]
    xs += [x[::-1] for x in xs]
    return min(min(rots(x)) for x in xs)


def smith_2x2(M):
    """Invariant factors (d1, d2) of a nonsingular integer 2x2 matrix: d1 = gcd of entries, d1*d2 = |det|."""
    d1 = math.gcd(math.gcd(M[0][0], M[0][1]), math.gcd(M[1][0], M[1][1]))
    det = abs(M[0][0] * M[1][1] - M[0][1] * M[1][0])
    assert det and d1 and det % d1 == 0 and (det // d1) % d1 == 0, (M, d1, det)
    return d1, det // d1


def p_rank(d1, d2, p):
    return (d1 % p == 0) + (d2 % p == 0)


def census(maxlen=12):
    out = []
    for n in range(2, maxlen + 1):
        seen = set()
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if "L" in w and "R" in w and primitive(w):
                seen.add(canon_state(w))
        out += [(s, w) for w in sorted(seen) for s in "+-"]
    return out


def row(s, w):
    eps = 1 if s == "+" else -1
    A = word(w)
    t = eps * (A[0][0] + A[1][1])
    M = ((eps * A[0][0] - 1, eps * A[0][1]), (eps * A[1][0], eps * A[1][1] - 1))
    d1, d2 = smith_2x2(M)
    rev = canon_state(w[::-1])
    closed = rev == w
    pal = closed and (min(rots(w[::-1])) == min(rots(w)))
    anti = closed and (min(rots(w[::-1])) == min(rots(w.translate(SW))))
    return {"state": s + w, "sign": s, "word": w, "length": len(w), "trace": t, "torsion": abs(2 - t),
            "d1": d1, "d2": d2, "noncyclic": d1 > 1, "exponent": d2,
            "rank2": p_rank(d1, d2, 2), "rank3": p_rank(d1, d2, 3), "rank5": p_rank(d1, d2, 5), "rank7": p_rank(d1, d2, 7),
            "reversal_closed": closed, "palindromic": pal, "antipalindromic": anti,
            "manifold": s + canon_manifold(w)}


def table(with_snappy=False):
    rows = [row(s, w) for s, w in census()]
    if with_snappy:
        warnings.filterwarnings("ignore")
        import snappy
        for r in rows:
            M = snappy.Manifold(("b++" if r["sign"] == "+" else "b+-") + r["word"])
            r["volume"] = round(float(M.volume()), 9)
            G = M.symmetry_group()
            r["symmetry_order"] = G.order()
            r["amphichiral"] = bool(G.is_amphicheiral())
    return rows


def controls(rows):
    """Banked identities this table must reproduce before it is used."""
    by = {r["state"]: r for r in rows}
    main = json.loads((HERE / "main_B1439_firing_own_states.json").read_text(encoding="utf-8"))
    agree = all(by[e[0]]["torsion"] == e[1] for e in main["firing_own_states"])
    c = {"states": len(rows), "manifolds": len({r["manifold"] for r in rows}),
         "main_torsion_agrees (93 listed states)": agree,
         "m369 = -LLRLR has G = Z/12": (by["-LLRLR"]["d1"], by["-LLRLR"]["d2"]) == (1, 12),
         "s639 = -LLLRLR has G = Z/15": (by["-LLLRLR"]["d1"], by["-LLLRLR"]["d2"]) == (1, 15),
         "m004 = +LR has trivial G": (by["+LR"]["d1"], by["+LR"]["d2"]) == (1, 1),
         "m003 = -LR has G = Z/5": (by["-LR"]["d1"], by["-LR"]["d2"]) == (1, 5)}
    c["passed"] = (c["states"] == 758 and c["manifolds"] == 536 and all(v for k, v in c.items()
                                                                     if k not in ("states", "manifolds")))
    return c


if __name__ == "__main__":
    rows = table(with_snappy="--snappy" in sys.argv)
    c = controls(rows)
    print(json.dumps(c, indent=1))
    if "--write" in sys.argv:
        (HERE / "covariates.json").write_text(json.dumps({"controls": c, "rows": rows}, indent=0) + "\n", encoding="utf-8")
    sys.exit(0 if c["passed"] else 1)
