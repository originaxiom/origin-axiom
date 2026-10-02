"""B1518 -- post-run checks (run after `bar_run.py --write`; not sealed, labelled as post-run in FINDINGS).

Q1  The mixed (G, sign) strata of the sealed run (P1's witnesses), listed with their words and main's background counts.
Q2  An independent route to main's own-level census (the owner's rule NO NEGATIVE FROM A BUG): P1 rests on main's records,
    so every manifold in a mixed (G, sign) stratum is recomputed here with code that shares nothing with main's but the
    definitions:
      - the bundle: main's automorphisms (B1434 architecture_census.py:31-60; tau_L, tau_R, and iota fixing [x, y] exactly,
        so that mu = t and lambda = [x, y] are a peripheral pair) -- a definition, re-implemented here;
      - the characters: every (i, j) in (Z/N)^2 fixed by the monodromy, by brute force (main: Smith form);
      - the slope s(chi) = u(mu) / u(lambda) for u in H^1(G; chi): here the full Fox-calculus cocycle system of both
        relators is solved mod p and the coboundaries removed (main: one relator in a fixed gauge, B1438 slope_census.py);
        two primes = 1 mod N above 3 * 10^9 (main's are above 2 * 10^9);
      - the index I(l, a) = [s(a) = s(l)] - [s(1/b) = s(l)], b = a / l, and 0 when l, a or b is trivial (main's frame,
        B1438 Theorem A and slope_census.py's docstring);
      - the backgrounds: every (theta, psi_Y, W) in the character group cubed, enumerated directly (main: solved through the
        fifth-power map), l = theta^2 / W, a_s = theta psi_Y^{s_Y} W^{(s_g - 1)/2} for B1374's sectors
        Q(1,3), u^c(-4,3), e^c(6,3), d^c(2,1), L(-3,1), nu^c(0,-5) (main B1439 PREREGISTRATION and B1434's frame);
        generation-shaped when the five charged sectors have equal non-zero index; counted once by (l, a_Q, ..., a_nu).
    Banked identities first: m004 = +LR has none (B1434 (a)), m369 = -LLRLR has 8 and s639 = -LLLRLR has 16 (B1434 (a)).
Q3  The smallest witness pair, identified with SnapPy.
Q4  T3 inside the strata that hold both reversal classes, descriptively.
Q5  The bar (PREREGISTRATION section 3) applied to the record's positives with the run's numbers.

    python3 post_run_checks.py --write    # writes post_run_checks.json
"""
import json
import math
import pathlib
import sys
from collections import defaultdict

import sympy

HERE = pathlib.Path(__file__).resolve().parent
X, Y, T = 1, 2, 3
SECT = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]


# ----------------------------------------------------------------------------- the bundle (definitions)
def inv(w):
    return [-g for g in reversed(w)]


def reduce(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return out


def apply(aut, w):
    out = []
    for g in w:
        out += aut[g] if g > 0 else inv(aut[-g])
    return reduce(out)


def compose(a, b):
    return {X: apply(a, b[X]), Y: apply(a, b[Y])}


TAU = {"L": {X: [X], Y: [Y, X]}, "R": {X: [X, Y], Y: [Y]}}
C = [Y, X]
IOTA = {X: reduce(C + [-X] + inv(C)), Y: reduce(C + [-Y] + inv(C))}
COMM = [X, Y, -X, -Y]


def monodromy(state):
    phi = {X: [X], Y: [Y]}
    for ch in state[1:]:
        phi = compose(phi, TAU[ch])
    if state[0] == "-":
        phi = compose(IOTA, phi)
    assert apply(phi, COMM) == COMM
    return phi


def exps(w):
    return (sum((g == X) - (g == -X) for g in w), sum((g == Y) - (g == -Y) for g in w))


# ----------------------------------------------------------------------------- characters and slopes
def characters(phi):
    (a, c), (b, d) = exps(phi[X]), exps(phi[Y])           # columns: images of x and y
    det = abs((a - 1) * (d - 1) - b * c)
    g = math.gcd(math.gcd(a - 1, b), math.gcd(c, d - 1))
    N = det // g
    chars = [(i, j) for i in range(N) for j in range(N)
             if ((a - 1) * i + c * j) % N == 0 and (b * i + (d - 1) * j) % N == 0]
    assert len(chars) == det, (len(chars), det)
    return N, chars


def primes_1_mod(N, start=3 * 10 ** 9, count=2):
    out, q = [], start - (start % N) + 1
    while len(out) < count:
        q += N
        if sympy.isprime(q):
            out.append(q)
    return out


def fox_row(w, val, p):
    """The linear form u(w) in (u_x, u_y, u_t) for the cocycle rule u(ab) = u(a) + chi(a) u(b)."""
    row = [0, 0, 0]
    pre = 1
    for g in w:
        if g > 0:
            row[g - 1] = (row[g - 1] + pre) % p
            pre = pre * val[g] % p
        else:
            pre = pre * pow(val[-g], p - 2, p) % p            # chi(prefix * g^-1)
            row[-g - 1] = (row[-g - 1] - pre) % p             # u(g^-1) = -chi(g)^-1 u(g), carried by the new prefix
    return row


def nullspace_mod_p(rows, n, p):
    M = [r[:] for r in rows]
    piv, r = [], 0
    for col in range(n):
        k = next((i for i in range(r, len(M)) if M[i][col] % p), None)
        if k is None:
            continue
        M[r], M[k] = M[k], M[r]
        iv = pow(M[r][col], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv.append(col)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][f]) % p
        basis.append(v)
    return basis


def slope(phi, chi, N, p):
    zeta = pow(sympy.primitive_root(p), (p - 1) // N, p)
    val = {X: pow(zeta, chi[0], p), Y: pow(zeta, chi[1], p), T: 1}
    rels = [reduce([T, X, -T] + inv(phi[X])), reduce([T, Y, -T] + inv(phi[Y]))]
    Z = nullspace_mod_p([fox_row(r, val, p) for r in rels], 3, p)
    assert len(Z) == 2, ("dim Z^1", len(Z))                   # H^1 is a line (B1438) plus the coboundary line
    lam = fox_row(COMM, val, p)
    ratios = set()
    for z in Z:
        ul = sum(a * b for a, b in zip(lam, z)) % p
        if ul:
            ratios.add(z[2] * pow(ul, p - 2, p) % p)
    assert len(ratios) == 1, ratios                           # coboundaries vanish on mu and lambda
    return ratios.pop()


def own_level_census(state):
    phi = monodromy(state)
    N, chars = characters(phi)
    ps = primes_1_mod(N)
    S = {c: tuple(slope(phi, c, N, p) for p in ps) for c in chars if c != (0, 0)}
    one_prime = sum(1 for a in S for b in S if a < b and (S[a][0] == S[b][0]) != (S[a][1] == S[b][1]))
    add = lambda u, v: ((u[0] + v[0]) % N, (u[1] + v[1]) % N)
    mul = lambda u, m: ((m * u[0]) % N, (m * u[1]) % N)
    triv = (0, 0)

    def index(l, a):
        b = add(a, mul(l, -1))
        if triv in (l, a, b):
            return 0
        return int(S[a] == S[l]) - int(S[mul(b, -1)] == S[l])

    bgs = set()
    for th in chars:
        for py in chars:
            for W in chars:
                l = add(mul(th, 2), mul(W, -1))
                if l == triv:
                    continue
                a_s = tuple(add(add(th, mul(py, sy)), mul(W, (sg - 1) // 2)) for _, sy, sg in SECT)
                c0 = index(l, a_s[0])
                if c0 and all(index(l, a) == c0 for a in a_s[1:5]):
                    bgs.add((l,) + a_s)
    return {"state": state, "N": N, "characters": len(chars), "primes": ps, "slope_classes": len(set(S.values())),
            "coincidences_at_one_prime_only": one_prime, "generation_backgrounds": len(bgs)}


# ----------------------------------------------------------------------------- the checks
def main():
    run = json.loads((HERE / "bar_run.json").read_text(encoding="utf-8"))
    cov = json.loads((HERE / "covariates.json").read_text(encoding="utf-8"))["rows"]
    lev = {(r["state"], r["k"]): r for r in json.loads((HERE / "main_B1439_levels.json").read_text(
        encoding="utf-8"))["records"]}
    out = {}
    # banked identities first
    banked = {"+LR": 0, "-LLRLR": 8, "-LLLRLR": 16}
    bi = {s: own_level_census(s) for s in banked}
    out["Q2 banked identities (B1434 (a)): own route against the banked count"] = {
        s: [bi[s]["generation_backgrounds"], banked[s]] for s in banked}
    ok_banked = all(bi[s]["generation_backgrounds"] == banked[s] for s in banked)
    out["Q2 banked identities pass"] = ok_banked
    if not ok_banked:
        out["stopped"] = "the independent route fails a banked identity; no witness is read"
        return out
    # Q1: the mixed S2 strata, with every manifold's states
    by_m = defaultdict(list)
    for r in cov:
        by_m[r["manifold"]].append(r)
    strata = defaultdict(list)
    for m, rs in by_m.items():
        r = rs[0]
        strata[(r["d1"], r["d2"], r["sign"])].append(m)
    mixed = {}
    for key, ms in sorted(strata.items()):
        hits = {m: lev[(by_m[m][0]["state"], 1)]["generation_backgrounds"] for m in ms}
        if 0 < sum(1 for v in hits.values() if v) < len(ms):
            mixed[key] = hits
    out["Q1 mixed (d1, d2, sign) strata"] = len(mixed)
    out["Q1 manifolds in them"] = sum(len(v) for v in mixed.values())
    # Q2: every manifold of every mixed stratum, recomputed (one state per manifold; its reverse is the same manifold)
    rows, agree = [], True
    for key, hits in mixed.items():
        for m, main_count in sorted(hits.items()):
            st = by_m[m][0]["state"]
            mine = own_level_census(st)
            same = mine["generation_backgrounds"] == main_count and mine["coincidences_at_one_prime_only"] == 0
            agree &= same
            rows.append([list(key), st, main_count, mine["generation_backgrounds"], same])
    out["Q2 every manifold of the mixed strata: [stratum, state, main, own route, agree]"] = rows
    out["Q2 the own route agrees with main on every one"] = agree
    smallest = min(mixed, key=lambda k: (k[0] * k[1], k[2]))
    out["Q2 the smallest witness stratum"] = {"stratum": list(smallest), "manifolds": {
        by_m[m][0]["state"]: c for m, c in sorted(mixed[smallest].items())}}
    # Q3: the smallest witness pair, identified (SnapPy 3.3.2); both words have trace |G| - 2 for sign -
    import warnings
    warnings.filterwarnings("ignore")
    import snappy
    out["Q3 the witness pair, identified"] = {
        st: {"identify": [str(x) for x in snappy.Manifold("b+-" + st[1:]).identify()],
             "homology": str(snappy.Manifold("b+-" + st[1:]).homology()),
             "trace of A": sum(word_matrix(st[1:])[i][i] for i in range(2))}
        for st in out["Q2 the smallest witness stratum"]["manifolds"]}
    # Q4: T3 inside the 32 informative (G, sign) strata, descriptively (the sealed test read NO at the gate)
    rc = {"closed": [0, 0], "paired": [0, 0]}
    for key, ms in strata.items():
        cls = {by_m[m][0]["reversal_closed"] for m in ms}
        if len(cls) < 2:
            continue
        for m in ms:
            h = lev[(by_m[m][0]["state"], 1)]["generation_backgrounds"] > 0
            k = "closed" if by_m[m][0]["reversal_closed"] else "paired"
            rc[k][0] += h
            rc[k][1] += 1
    out["Q4 inside the strata holding both reversal classes (hits, manifolds)"] = rc
    # Q5: the bar applied to the record's positives (PREREGISTRATION section 3; the run's numbers)
    from null_model import clopper_pearson
    r_P = run["readings"]["R1 base rate, manifolds"]["rate"]
    q5 = {"m369 and s639 (B1434; found by scanning 24 manifolds)": {
        "p = 1 - (1 - r_P)^24": round(1 - (1 - r_P) ** 24, 4), "grade if claimed": "FITTED"}}
    tower = run["decided"]["D3 the root's tower against the other level-manifolds at the same k"]
    for k, v in tower.items():
        if v["root_hit"] and v["others"]:
            r = clopper_pearson(v["others_hit"], v["others"])[1]
            q5[f"the root's level {k} (chosen by T-ROOT)"] = {"others firing": [v["others_hit"], v["others"]],
                                                              "p = r (upper exact 95% limit)": round(r, 4),
                                                              "grade": "DERIVED" if r < 0.01 else "REPRODUCED"}
        elif v["root_hit"]:
            q5[f"the root's level {k} (chosen by T-ROOT)"] = {"others firing": [0, 0], "p = r": 1.0,
                                                              "grade": "no credit (no comparable object: r = 1)"}
    out["Q5 the bar applied to the record's positives"] = q5
    out["predictions read by the sealed run (unchanged)"] = run["predictions"]
    return out


def word_matrix(w):
    M = ((1, 0), (0, 1))
    for ch in w:
        B = ((1, 1), (0, 1)) if ch == "L" else ((1, 0), (1, 1))
        M = ((M[0][0] * B[0][0] + M[0][1] * B[1][0], M[0][0] * B[0][1] + M[0][1] * B[1][1]),
             (M[1][0] * B[0][0] + M[1][1] * B[1][0], M[1][0] * B[0][1] + M[1][1] * B[1][1]))
    return M


if __name__ == "__main__":
    res = main()
    text = json.dumps(res, indent=1, default=str)
    print(text)
    if "--write" in sys.argv:
        (HERE / "post_run_checks.json").write_text(text + "\n", encoding="utf-8")
