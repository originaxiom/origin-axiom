#!/usr/bin/env python3
"""B1869 -- the founding principle read as a selection rule: the advisor seat's sealed enumeration, re-derived by main.

The seat's reading (its words): a departure from the background that some counted level can detect is undone; what remains is
the least departure that no counted level detects.  Its run is exhaustive to 20 letters.  Main ran none of its code.  This
file is main's own enumeration, on B1853's definitions (main's), with exact integers and no modulus until the test:

  background   (L^b R^b)^k: b = 1 golden, 2 silver, 3 bronze
  departure    m consecutive runs of the background replaced by runs S = (r_1, ..., r_m), every r_i >= 1, r_1 != b, r_m != b
  E(S)         D(S) D(b, ..., b)^-1, D the alternating product L^r1 R^r2 ...
  letters      r_1 + ... + r_m;   extra letters: that less b m
  not detected at a level N, in three senses:
      whole level, sign +    E = +1 mod N
      whole level, any sign  E = +1 or -1 mod N   (for several levels: the sign may differ by level, or be one for all)
      the line               E commutes with the period L^b R^b mod N

    python3 -B frontier/B1869_the_principle_as_a_selection_rule_verified/verification/nc_on_main.py [B]      (B = 20 by default)
"""
import sys

B = 20                                                                  # the bound on letters; main() reads another from the command line
say = print
I = (1, 0, 0, 1)
def mul(X, Y): return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3], X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])
def inv(X): return (X[3], -X[1], -X[2], X[0])
def Lp(r): return (1, r, 0, 1)
def Rp(r): return (1, 0, r, 1)
def is_one(E, N, sign): return (E[0] - sign) % N == 0 and E[1] % N == 0 and E[2] % N == 0 and (E[3] - sign) % N == 0
def commutes(E, A, N):
    X, Y = mul(E, A), mul(A, E)
    return all((x - y) % N == 0 for x, y in zip(X, Y))


def departures(b, bound):
    """every departure with at most `bound` letters on the background b, with its E as exact integers (depth-first, in order of runs)"""
    stack = [((), I, I, 0)]
    while stack:
        S, DS, Dg, n = stack.pop()
        i = len(S)
        X = Lp if i % 2 == 0 else Rp
        for r in range(1, bound - n + 1):
            if i == 0 and r == b:
                continue
            S2, DS2, Dg2 = S + (r,), mul(DS, X(r)), mul(Dg, X(b))
            if r != b:
                yield S2, mul(DS2, inv(Dg2))
            if n + r < bound:
                stack.append((S2, DS2, Dg2, n + r))


READINGS = ("whole level, sign +", "whole level, any sign by level", "whole level, one sign for all", "the line")
def passes(E, A, Ns):
    plus = all(is_one(E, N, 1) for N in Ns)
    minus = all(is_one(E, N, -1) for N in Ns)
    each = all(is_one(E, N, 1) or is_one(E, N, -1) for N in Ns)
    line = all(commutes(E, A, N) for N in Ns)
    return {"whole level, sign +": plus, "whole level, any sign by level": each, "whole level, one sign for all": plus or minus, "the line": line}


def run(b, level_sets, bound):
    A = mul(Lp(b), Rp(b))
    hits = {(rd, name): [] for rd in READINGS for name in level_sets}
    count = 0
    for S, E in departures(b, bound):
        count += 1
        for name, Ns in level_sets.items():
            p = passes(E, A, Ns)
            for rd in READINGS:
                if p[rd]:
                    hits[(rd, name)].append((sum(S), sum(S) - b * len(S), S))
    return hits, count


def least(rows, key):
    if not rows: return None, [], None
    vals = sorted({r[key] for r in rows})
    best = [r[2] for r in rows if r[key] == vals[0]]
    return vals[0], sorted(best), (vals[1] if len(vals) > 1 else None)


def show(rows, key=0, cap=6):
    v, best, nxt = least(rows, key)
    if v is None: return "none with at most %d letters" % B
    return "%d: %d departure%s %s%s; next %s" % (v, len(best), "" if len(best) == 1 else "s", " ".join(str(s).replace(" ", "") for s in best[:cap]), " ..." if len(best) > cap else "", nxt)


def main():
    global B
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        B = int(sys.argv[1])
    names = {1: "golden", 2: "silver", 3: "bronze"}
    say("the period is minus a unipotent mod N exactly when N divides b^2 + 4: golden %s, silver %s, bronze %s" % tuple([N for N in range(2, 40) if (b * b + 4) % N == 0] for b in (1, 2, 3)))
    # the period L^b R^b has trace b^2 + 2 and determinant 1, so its characteristic polynomial is (t + 1)^2 mod N exactly when N divides
    # its trace plus two, which is b^2 + 4: an identity, checked here on the matrices themselves
    for b in (1, 2, 3):
        A = mul(Lp(b), Rp(b))
        assert A[0] + A[3] + 2 == b * b + 4 and A[0] * A[3] - A[1] * A[2] == 1
    # controls with known answers (the seat's four, recomputed here): (6) is +1 at level 5; (3,4,3) is -1; (2,1,1,1,2) commutes and is not +-1; (2) does not commute
    ctrl = {S: E for S, E in departures(1, 10) if S in ((6,), (3, 4, 3), (2, 1, 1, 1, 2), (2,))}
    A1 = mul(Lp(1), Rp(1))
    assert is_one(ctrl[(6,)], 5, 1) and is_one(ctrl[(3, 4, 3)], 5, -1) and commutes(ctrl[(2, 1, 1, 1, 2)], A1, 5) and not is_one(ctrl[(2, 1, 1, 1, 2)], 5, 1) and not is_one(ctrl[(2, 1, 1, 1, 2)], 5, -1) and not commutes(ctrl[(2,)], A1, 5)
    say("controls: (6) is +1 at level 5; (3,4,3) is -1; (2,1,1,1,2) commutes with the period and is neither; (2) does not commute -- all four as known")

    GOLD = {"5": [5], "2": [2], "3": [3], "4": [4], "7": [7], "11": [11], "4 and 5": [4, 5], "2, 3, 4, 5": [2, 3, 4, 5]}
    hits, count = run(1, GOLD, B)
    say("")
    say("GOLDEN: %d departures with at most %d letters" % (count, B))
    say("  the own level, 5 -- least by letters:")
    for rd in ("whole level, sign +", "whole level, any sign by level", "the line"):
        say("    %-32s %s" % (rd, show(hits[(rd, "5")])))
    minus5 = [r for r in hits[("whole level, any sign by level", "5")] if r not in hits[("whole level, sign +", "5")]]
    say("    %-32s %s" % ("sign - only", show(minus5)))
    say("  the own level, 5 -- least by extra letters:")
    for rd in ("whole level, sign +", "whole level, any sign by level", "the line"):
        v, best, nxt = least(hits[(rd, "5")], 1)
        say("    %-32s least %s, shared by %d departures (within %d letters)" % (rd, v, len(best), B))
    fam = sorted(S for (n, ex, S) in hits[("the line", "5")] if ex == least(hits[("the line", "5")], 1)[0])
    say("    the line's least by extra letters: %s" % " ".join(str(s).replace(" ", "") for s in fam))
    say("  one level alone, sign + -- least by letters:  " + ";  ".join("level %s: %s" % (nm, show(hits[("whole level, sign +", nm)], cap=2)) for nm in ("2", "3", "4", "7", "11")))
    for nm in ("4 and 5", "2, 3, 4, 5"):
        say("  levels %s -- least by letters:" % nm)
        for rd in READINGS:
            say("    %-32s %s" % (rd, show(hits[(rd, nm)], cap=4)))
    upto12 = lambda rows: [r for r in rows if r[0] <= 12]
    p12 = upto12(hits[("whole level, sign +", "5")]); a12 = upto12(hits[("whole level, any sign by level", "5")]); l12 = upto12(hits[("the line", "5")])
    say("  to 12 letters at level 5: %d with E = +1, %d with E = -1, %d more that fix the line only" % (len(p12), len(a12) - len(p12), len(l12) - len(a12)))
    single = lambda N: (N + 1,)
    say("  the single run of N + 1 is +1 at level N for N = 2, 3, 4, 5, 7, 11: %s; under the ladder it needs %d letters" % (
        all(is_one(mul(Lp(N + 1), inv(Lp(1))), N, 1) for N in (2, 3, 4, 5, 7, 11)), 60 + 1))

    for b, own in ((2, 8), (3, 13)):
        hb, cb = run(b, {"own": [own]}, B)
        say("")
        say("%s (b = %d): %d departures with at most %d letters; its own level %d -- least by letters:" % (names[b].upper(), b, cb, B, own))
        for rd in ("whole level, sign +", "whole level, any sign by level", "the line"):
            say("    %-32s %s" % (rd, show(hb[(rd, "own")])))
        sr = (b + own,)
        say("    the single run %s has %d letters and is +1 at level %d: %s" % (sr, b + own, own, is_one(mul(Lp(b + own), inv(Lp(b))), own, 1)))


if __name__ == "__main__":
    main()
