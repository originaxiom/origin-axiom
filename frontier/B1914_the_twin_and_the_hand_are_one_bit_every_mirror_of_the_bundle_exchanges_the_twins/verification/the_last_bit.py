"""B1914: the line's last bit. Can a history, or a symmetry of the object, choose between the line's two twins?

Convention (the record's, B1867 section 4): L = [[1,1],[0,1]], R = [[1,0],[1,1]], the golden ground LR = [[2,1],[1,1]],
matrices acting on column vectors of (Z/N)^2; a line of order N is a primitive vector up to sign; a word W fixes a line v
with sign s when W v = s v mod N, s = +1 or -1.

Main's reading, written before the run ((b) relabelled after it, on reading B1872's correction):
 (a) The ground fixes lines only at order 5, exactly +-(1,2) and +-(2,4), with sign -1 (seen first: B1867 section 4).
 (b) An IDENTITY, not a finding (B1872's correction of 2026-11-11): (2,4) = 2 (1,2) is the first point's twin, and a
     matrix that keeps +-v keeps +-2v by linearity, so no history separates the twins. It is computed below only so the
     census is whole, and the lock shows the checker separates two points that are not twins.
 (c) The symmetries of the golden bundle are the integer matrices X with X A X^-1 = A or A^-1 (A = LR). X preserves the
     bundle's orientation iff det X times that exponent is +1. On A's eigenline mod 5, X acts as a scalar; main expects
     +-1 for every orientation-preserving X and +-2 for every orientation-reversing X: the twins are kept by the first
     and exchanged by the second (the tick's case is on record: B1871, B1879, B1881).
 (d) So of the four placements (the hand, the twin), the object's symmetries leave two classes.
A plant: with L and R swapped in the departure test only, the run of 6 must stop fixing the record's line.
No data; no value of the modulus on record is read; nothing is compared with anything measured."""
import itertools, json, pathlib
from math import gcd

HERE = pathlib.Path(__file__).resolve().parent
L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); I2 = ((1, 0), (0, 1))


def mul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def word(s, Lm=L, Rm=R):
    M = I2
    for ch in s:
        M = mul(M, Lm if ch == "L" else Rm)
    return M


def det(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def inv(X):
    d = det(X)
    assert d in (1, -1)
    return ((X[1][1] * d, -X[0][1] * d), (-X[1][0] * d, X[0][0] * d))


def act(X, v, N):
    return ((X[0][0] * v[0] + X[0][1] * v[1]) % N, (X[1][0] * v[0] + X[1][1] * v[1]) % N)


def lines(N):
    out = set()
    for a in range(N):
        for b in range(N):
            if gcd(gcd(a, b), N) == 1:
                w = ((-a) % N, (-b) % N)
                out.add(min((a, b), w))
    return sorted(out)


def fixed(X, N):
    """{line: sign} for the lines X fixes up to sign at order N"""
    res = {}
    for v in lines(N):
        Xv = act(X, v, N)
        if Xv == v:
            res[v] = +1
        elif Xv == ((-v[0]) % N, (-v[1]) % N):
            res[v] = -1
    return res


def scalar_on(X, v, N):
    """lam with X v = lam v mod N, or None"""
    Xv = act(X, v, N)
    for lam in range(N):
        if Xv == ((lam * v[0]) % N, (lam * v[1]) % N):
            return lam
    return None


def run():
    A = word("LR")
    out = {"A": A}
    # (a) the census over orders
    orders = {N: fixed(A, N) for N in range(2, 61)}
    out["a_orders_with_a_fixed_line"] = [N for N, f in orders.items() if f]
    out["a_at_5"] = {f"{v[0]},{v[1]}": s for v, s in orders[5].items()}
    # (b) no element of SL2(Z/5) (all 120) separates v from 2v
    v1, v2 = (1, 2), (2, 4)
    sl = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]
    sep = []
    for X in sl:
        f = fixed(X, 5)
        if f.get(v1) != f.get(v2):
            sep.append(X)
    out["b_SL2_F5_size"] = len(sl)
    out["b_elements_separating_the_two_points"] = len(sep)
    out["b_elements_fixing_the_pair"] = sum(1 for X in sl if v1 in fixed(X, 5))
    # (b') every positive word of length <= 14: fixes v1 iff fixes v2, with the same sign
    nw = agree = fixes = 0
    for n in range(1, 15):
        for t in itertools.product("LR", repeat=n):
            W = word(t)
            f = fixed(W, 5)
            nw += 1
            agree += f.get(v1) == f.get(v2)
            fixes += v1 in f
    out["b_words_up_to_14"] = nw
    out["b_words_agreeing"] = agree
    out["b_words_fixing_the_pair"] = fixes
    # the departure family L^a R: fixes the pair iff a = 1 mod 5
    out["b_LaR_fixing"] = [a for a in range(1, 31) if v1 in fixed(word("L" * a + "R"), 5)]
    out["b_run6_periods_signs"] = [fixed(word("L" * 6 + "R" + "LR" * k), 5).get(v1) for k in (1, 2, 3)]
    # (e) a history alone does not force the order: the orders N <= 60 at which each history fixes some line
    out["e_histories"] = {}
    for name, dep in (("run of 6", "L" * 6 + "R"), ("L^2 R", "LLR"), ("L R^2", "LRR"), ("L^3 R", "LLLR")):
        for k in (1, 2, 3):
            W = word(dep + "LR" * k)
            out["e_histories"][f"{name} + {k}"] = {"orders": [N for N in range(2, 61) if fixed(W, N)],
                                                   "fixes the pair": v1 in fixed(W, 5)}
    out["plant_swapped_run6_fixes_v1"] = v1 in fixed(word("L" * 6 + "R" + "LR", Lm=R, Rm=L), 5)
    # (c) the symmetries of the bundle: X A X^-1 = A^e. A full search over |entries| <= 12, then the two solution
    # families of the linear equations (X A = A X: X = [[a, b], [b, a - b]]; X A = A^-1 X: X = [[a, b], [-a - b, -a]])
    # over |a|, |b| <= 300, checked against the full search where they overlap.
    Ainv = inv(A)
    def classify(X):
        XA = mul(X, A)
        if XA == mul(A, X):
            return 1
        if XA == mul(Ainv, X):
            return -1
        return None
    full = set()
    for a, b, c, d in itertools.product(range(-12, 13), repeat=4):
        X = ((a, b), (c, d))
        if det(X) in (1, -1) and classify(X) is not None:
            full.add(X)
    fam = set()
    for a in range(-300, 301):
        for b in range(-300, 301):
            for X in (((a, b), (b, a - b)), ((a, b), (-a - b, -a))):
                if det(X) in (1, -1) and classify(X) is not None:
                    fam.add(X)
    small = {X for X in fam if max(abs(x) for r in X for x in r) <= 12}
    out["c_full_search_equals_families_within_12"] = full == small
    syms = []
    for X in sorted(fam):
        dX = det(X); e = classify(X)
        orient = dX * e
        lam = scalar_on(X, v1, 5)
        lam2 = scalar_on(X, v2, 5)
        syms.append({"X": X, "det": dX, "e": e, "orientation": orient, "lam_on_eigenline": lam, "lam2": lam2})
    out["c_symmetries_found"] = len(syms)
    out["c_preserving_scalars"] = sorted({s["lam_on_eigenline"] for s in syms if s["orientation"] == 1})
    out["c_reversing_scalars"] = sorted({s["lam_on_eigenline"] for s in syms if s["orientation"] == -1})
    out["c_every_symmetry_keeps_the_eigenline"] = all(s["lam_on_eigenline"] is not None for s in syms)
    J = ((1, 1), (1, 0)); K = ((0, 1), (-1, 0))
    out["c_J"] = {"J^2 == A": mul(J, J) == A, "det": det(J), "commutes": mul(J, A) == mul(A, J),
                  "lam": scalar_on(J, v1, 5)}
    out["c_K"] = {"K A K^-1 == A^-1": mul(mul(K, A), inv(K)) == Ainv, "det": det(K), "lam": scalar_on(K, v1, 5)}
    # every symmetry found is +-J^n or +-J^n K (the normaliser's generators)
    gens = set()
    P = I2
    pw = [I2]
    for _ in range(30):
        P = mul(P, J); pw.append(P)
    P = I2
    for _ in range(30):
        P = mul(P, inv(J)); pw.append(P)
    for M in pw:
        for s in (1, -1):
            Ms = tuple(tuple(s * x for x in r) for r in M)
            gens.add(Ms); gens.add(mul(Ms, K))
    out["c_all_found_are_pm_Jn_or_pm_JnK"] = all(s["X"] in gens for s in syms)
    # modulo the flow (powers of A, isotopic to the identity on the bundle): the classes and their orientations
    Apow = [I2]
    P = I2
    for _ in range(20):
        P = mul(P, A); Apow.append(P)
    P = I2
    for _ in range(20):
        P = mul(P, Ainv); Apow.append(P)
    reps = []
    for s0 in syms:
        if not any(mul(s0["X"], inv(r["X"])) in Apow for r in reps):
            reps.append(s0)
    out["c_classes_modulo_A"] = len(reps)
    out["c_classes_reversing"] = sum(1 for r in reps if r["orientation"] == -1)
    try:
        import snappy
        G = snappy.Manifold("4_1").symmetry_group()
        out["c_snappy_4_1"] = {"order": G.order(), "amphicheiral": bool(G.is_amphicheiral()), "group": str(G)}
    except Exception as ex:                                             # SnapPy absent: the cross-check is skipped, said so
        out["c_snappy_4_1"] = {"skipped": type(ex).__name__}
    # (d) orbits of the four placements (hand o, point v) under the symmetries: X sends (o, v) to (o * orient, X v)
    pts = {v1: "v", v2: "2v"}
    def cls(v):
        for p in pts:
            if v == p or v == ((-p[0]) % 5, (-p[1]) % 5):
                return pts[p]
        return None
    place = [(o, p) for o in (1, -1) for p in ("v", "2v")]
    vec = {"v": v1, "2v": v2}
    adj = {x: {x} for x in place}
    for s in syms:
        for (o, p) in place:
            img = act(s["X"], vec[p], 5)
            q = cls(img)
            adj[(o, p)].add((o * s["orientation"], q))
    orbits = []
    seen = set()
    for x in place:
        if x in seen:
            continue
        comp, stack = set(), [x]
        while stack:
            y = stack.pop()
            if y in comp:
                continue
            comp.add(y); stack.extend(adj[y])
        seen |= comp
        orbits.append(sorted(comp))
    out["d_orbits"] = [[f"{'+' if o == 1 else '-'} hand, {p}" for o, p in orb] for orb in orbits]
    return out


if __name__ == "__main__":
    r = run()
    lines_out = [
        f"A = LR = {r['A']}",
        f"(a) orders N <= 60 at which the ground fixes a line: {r['a_orders_with_a_fixed_line']}; at 5: {r['a_at_5']}",
        f"(b) SL2(F5): {r['b_SL2_F5_size']} elements; fixing the pair: {r['b_elements_fixing_the_pair']}; "
        f"separating the two points: {r['b_elements_separating_the_two_points']}",
        f"(b) positive words of length 1..14: {r['b_words_up_to_14']}; the two points agree in all but "
        f"{r['b_words_up_to_14'] - r['b_words_agreeing']}; words fixing the pair: {r['b_words_fixing_the_pair']}",
        f"(b) L^a R fixes the pair for a in 1..30: {r['b_LaR_fixing']}",
        f"(b) the run of 6 with 1, 2, 3 golden periods: signs {r['b_run6_periods_signs']}",
        "(e) orders N <= 60 at which a history fixes some line, and whether it fixes the pair: " + "; ".join(
            f"{h}: {v['orders'][:6]}{'...' if len(v['orders']) > 6 else ''} {v['fixes the pair']}" for h, v in r["e_histories"].items()),
        f"plant (L and R swapped in the run of 6): fixes the record's line: {r['plant_swapped_run6_fixes_v1']}",
        f"(c) symmetries X A X^-1 = A^(+-1), |a|, |b| <= 300 in the two families: {r['c_symmetries_found']} "
        f"(the full search within 12 agrees: {r['c_full_search_equals_families_within_12']}); all keep the eigenline: "
        f"{r['c_every_symmetry_keeps_the_eigenline']}; all are +-J^n or +-J^n K: {r['c_all_found_are_pm_Jn_or_pm_JnK']}",
        f"(c) scalar on the eigenline mod 5: orientation-preserving {r['c_preserving_scalars']}, "
        f"orientation-reversing {r['c_reversing_scalars']}",
        f"(c) J = [[1,1],[1,0]]: {r['c_J']}; K = [[0,1],[-1,0]]: {r['c_K']}",
        f"(c) modulo the powers of A: {r['c_classes_modulo_A']} classes, {r['c_classes_reversing']} reversing the "
        f"orientation; SnapPy's symmetry group of the figure-eight complement: {r['c_snappy_4_1']}",
        f"(d) the four placements (hand, point) fall in {len(r['d_orbits'])} classes: {r['d_orbits']}",
    ]
    print("\n".join(lines_out))
    (HERE / "the_last_bit.json").write_text(json.dumps({k: (str(v) if not isinstance(v, (int, float, list, dict, bool, str)) else v)
                                                         for k, v in r.items()}, indent=1, default=str))
    (HERE / "the_last_bit_run.txt").write_text("\n".join(lines_out) + "\n")
