#!/usr/bin/env python3
"""SM-R384 (register row P-384): does a principle in B1934's terms single out the line class (2/5, odd/10)?
Exact enumeration over the lines (points of (Q/Z)^2 up to sign) of order <= 12, the record's 266 (B1749, B1753), and
over orders 15, 20, 25 and 30 for the reach of each rule.
Card relays/cards/SM_R384_a-principle-for-the-two-fifths-class.md, written before this script is run on the real case.
Data-free: no measured number is read, loaded or printed.
The act's line comes from B1943's own module, the charges and the Legendre table from B1934's.
    python3 -B run.py MAIN_CHECKOUT > r384_run.txt          # the real case, p = 5 (phase 2 only)
    python3 -B run.py MAIN_CHECKOUT --smoke                  # the same code at p = 7, prints only SMOKE OK"""
import json
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd, lcm

MAIN = pathlib.Path(sys.argv[1]).resolve()
SMOKE = "--smoke" in sys.argv[2:]
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1943_*")) / "verification"))
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1934_*")) / "verification"))
import fixed_lines as FL              # noqa: E402  (B1943; its checks run only under __main__)
import level_five_structure as LF     # noqa: E402  (B1934; its checks run only under __main__)

P = 7 if SMOKE else 5                 # the level; the smoke run uses 7, outside the test population
Q = 2                                 # the second prime of the class's order
H = 3                                 # the Higgs's 6Y in SU(5)'s 5: (-2, -2, -2, 3, 3) (B1934)
NMAX = max(12, 2 * P)
REACH = (3 * P, 4 * P, 5 * P, 6 * P)  # orders 15, 20, 25, 30 at p = 5


def red(x): return x - (x.numerator // x.denominator)
def order(v): return lcm(v[0].denominator, v[1].denominator)
def neg(v): return (red(-v[0]), red(-v[1]))
def canon(v): return min(v, neg(v))
def scale(u, v): return (red(u * v[0]), red(u * v[1]))


def lines_of_order(N):
    return sorted({canon((Fr(i, N), Fr(j, N))) for i in range(N) for j in range(N) if gcd(gcd(i, j), N) == 1})


def part(v, p):
    """The p-primary part of v by CRT: e v with e = 1 mod p^r, 0 mod the rest of the order."""
    N = order(v); pr = 1
    while N % (pr * p) == 0:
        pr *= p
    m = N // pr
    if pr == 1:
        return (Fr(0), Fr(0))
    e = m * pow(m, -1, pr)
    return scale(e, v)


def legendre(x, p):
    x %= p
    if x == 0:
        return 0
    if p == 5:
        return LF.LEG[x]             # B1934's table: the golden field's quadratic character
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


LR = FL.mul(FL.L, FL.R)
ACT_LINE = {v for v, s in FL.fixed_up_to_sign(LR, P).get(P, set())}            # B1943: the act's fixed line mod p
MARK = (Fr(1, P), Fr(2, P))                                                     # B1934 § 2's mark
COPY = LF.transposed_orders(Nmax=60)                                            # B1934 § 3: orders where L, e copy Q, d
MINLEVEL = min(N for N in range(P, 61, P) if N not in COPY)                     # least multiple of p where it breaks


def twist_unit(v):          # the Higgs's twist H a is a unit generator +-1/p of the centre Z/p, nothing else
    t = red(H * v[0]); return t in (Fr(1, P), Fr(P - 1, P))


def twist_nonzero(v):       # its Galois-invariant form: H a is a non-zero element of (1/p)Z/Z
    t = red(H * v[0]); return t != 0 and (t * P).denominator == 1


def a_p(v): return part((v[0], Fr(0)), P)[0]
def a_q(v): return part((v[0], Fr(0)), Q)[0]
def chi_a(v):               # the golden character of 5 a_5 when a's 5-part has order 5; 0 otherwise
    x = a_p(v) * P; return legendre(int(x), P) if x.denominator == 1 else 0


RULES = {
    # plants and simple order rules (B1753's referee)
    "div5 (plant: the five-ality rule)": lambda v: order(v) % P == 0,
    "div2": lambda v: order(v) % Q == 0,
    "order 10": lambda v: order(v) == P * Q,
    "order 5": lambda v: order(v) == P,
    # B1943: the act's line
    "5-part on the act's line": lambda v: order(v) % P == 0 and part(v, P) in ACT_LINE | {neg(w) for w in ACT_LINE},
    "order 10, 5-part on the act's line": lambda v: order(v) == P * Q and part(v, P) in
    ACT_LINE | {neg(w) for w in ACT_LINE},
    "5-part is +-the mark": lambda v: part(v, P) in (MARK, neg(MARK)),
    "5-part is +-2 x the mark": lambda v: part(v, P) in (scale(2, MARK), neg(scale(2, MARK))),
    # SM-C24: the cusp sees the 5-part (a has a p-part)
    "cusp sees the 5-part": lambda v: a_p(v) != 0,
    "order 10, cusp sees the 5-part": lambda v: order(v) == P * Q and a_p(v) != 0,
    "order 10, cusp sees the 5-part, not the 2-part": lambda v: order(v) == P * Q and a_p(v) != 0 and a_q(v) == 0,
    # B1934: the golden character on the cusp's coordinate
    "chi(5a_5) = -1": lambda v: chi_a(v) == -1,
    "chi(5a_5) = +1": lambda v: chi_a(v) == 1,
    # B1934 § 3: hypercharge mod 5 is SU(5)'s centre; the Higgs's twist
    "unit twist (3a = +-1/5)": twist_unit,
    "nonzero twist (Galois-invariant)": twist_nonzero,
    "least level breaking the copy": lambda v: order(v) == MINLEVEL,
    # the candidate principle and its Galois-invariant shadow
    "PI: least level breaking the copy, unit twist": lambda v: order(v) == MINLEVEL and twist_unit(v),
    "PI_inv: least level breaking the copy, nonzero twist": lambda v: order(v) == MINLEVEL and twist_nonzero(v),
    # plant: the principle with the wrong charge (h = 1 in place of the Higgs's 3)
    "PI with h = 1 (plant)": lambda v: order(v) == MINLEVEL and red(v[0]) in (Fr(1, P), Fr(P - 1, P)),
    # positive control: the description itself must select exactly the class
    "DESCRIPTION (control): order 10, a = +-2/5": lambda v: order(v) == P * Q and red(v[0]) in (Fr(2, P), Fr(P - 2, P)),
}


def units(N): return [u for u in range(1, N) if gcd(u, N) == 1]


def unit_invariant(S):
    return all(canon(scale(u, v)) in S for v in S for u in units(order(v)))


def tinf_orbit(v):
    """Orbit under <T, -I> in the row convention (a, b) -> (a, b - a) (B1733): a cusp of the level."""
    seen, w = set(), v
    while canon(w) not in seen:
        seen.add(canon(w)); w = (w[0], red(w[1] - w[0]))
    return frozenset(seen)


def fs(v): return "(%s, %s)" % v


def main():
    U = [v for N in range(1, NMAX + 1) for v in lines_of_order(N)]
    Uset = set(U)
    K = {canon((Fr(2, P), Fr(k, P * Q))) for k in range(1, P * Q, 2)}
    K = {v for v in K if order(v) == P * Q}
    carriers = {canon((Fr(2, P), Fr(1, P * Q))), canon((Fr(2, P), Fr(1, Q)))}
    out = {"p": P, "universe": len(U), "order_p": len(lines_of_order(P)), "order_pq": len(lines_of_order(P * Q)),
           "class": sorted(fs(v) for v in K), "carriers_in_class": carriers <= K, "class_in_universe": K <= Uset,
           "act_line": sorted(fs(v) for v in ACT_LINE), "copy_orders": COPY, "least_level": MINLEVEL}
    closure = {canon(scale(u, v)) for v in K for u in units(P * Q)}
    out["class_unit_invariant"] = unit_invariant(K)
    out["class_unit_closure"] = sorted(fs(v) for v in closure)
    orbits = {tinf_orbit(v) for v in lines_of_order(P * Q)}
    out["cusps_at_order_pq"] = [{"a": str(min(v[0] for v in o)), "size": len(o), "is_class": set(o) == K,
                                 "sees_p_part": a_p(next(iter(o))) != 0} for o in sorted(orbits, key=lambda o: min(o))]
    rows = {}
    for name, f in RULES.items():
        S = {v for v in U if f(v)}
        rows[name] = {"selected": len(S), "in_class": len(S & K), "outside_class": len(S - K),
                      "carriers_in": len(S & carriers), "exactly_class": S == K, "unit_invariant": unit_invariant(S),
                      "order_pq_selected": sorted(fs(v) for v in S if order(v) == P * Q)}
        rows[name]["reach"] = {}
        for N in REACH:
            SN = [v for v in lines_of_order(N) if f(v)]
            rows[name]["reach"][N] = {"lines": len(SN), "a": sorted({str(min(v[0], red(-v[0]))) for v in SN},
                                                                     key=Fr)}
    out["rules"] = rows
    return out


if __name__ == "__main__":
    res = main()
    if SMOKE:
        assert res["universe"] > 0 and res["rules"]
        print("SMOKE OK")
        sys.exit(0)
    print("SM-R384: the line class (2/5, odd/10) against rules in B1934's terms (exact enumeration)")
    for k in ("p", "universe", "order_p", "order_pq", "class", "carriers_in_class", "class_in_universe", "act_line",
              "copy_orders", "least_level", "class_unit_invariant", "class_unit_closure"):
        print("%-22s %s" % (k, res[k]))
    print("cusps (<T, -I>-orbits) of the order-10 lines:")
    for c in res["cusps_at_order_pq"]:
        print("   ", c)
    print("%-56s %4s %4s %4s %4s %6s %6s" % ("rule", "sel", "inK", "out", "carr", "exact", "unitinv"))
    for name, r in res["rules"].items():
        print("%-56s %4d %4d %4d %4d %6s %6s" % (name, r["selected"], r["in_class"], r["outside_class"],
                                                r["carriers_in"], r["exactly_class"], r["unit_invariant"]))
    print("order-10 selections and reach at orders %s:" % (REACH,))
    for name, r in res["rules"].items():
        print("  %s\n     order 10: %s\n     reach: %s" % (name, r["order_pq_selected"], r["reach"]))
    (pathlib.Path(__file__).resolve().parent / "r384_results.json").write_text(json.dumps(res, indent=1, default=str))
