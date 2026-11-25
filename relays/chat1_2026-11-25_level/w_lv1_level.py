#!/usr/bin/env python3
"""W-LV1 (chat1, 2026-11-25; data-free): which levels does the matter content tie under frame C's own lens rule, and
does that arithmetic single out level 30 (P-845)?

CONDITION, written before the run. Disclosure: the seat's hand arithmetic in conversation the same morning anticipated
parts of the table (below, "anticipated"), so the reading rule is not blind to it. Nothing is compared with data.

Inputs: frame C's sector charge pairs from main's module (B.SIXY, B.SECTORS) in a checkout of main at be8c83d4f, passed
as the argument (any other commit is refused), and B1976's unit rule (sectors tied by a unit k of Z/N, directly or with
the two charges swapped), restated in tied() below with one change: a sector against itself counts only swapped (the
unswapped k p = p is a symmetry of the level, not a tie). In frame C the Higgs triplet is common to all sectors and
carries no point, so its charge does not enter the lens (determinant_law.parts, B1945).

Two readings of a tie, both computed:
  whole level: tied by any unit k. Then Y_t(w) and Y_s(k w) are built from the same characteristics up to integer
      shifts, so over all the points of order N sector t plays sector s's couplings in another order.
  pointwise: k = 1 (the same point) or k = -1 (the point negated; B1949: the rates ignore that sign).

T1  for N = 2..420, every sector pair (up, down, lep, and each against itself swapped), whole level and pointwise.
T2  the levels with a tie; the primes p with a tie at some power of p up to 420; the primes dividing the differences of
    the five multiplets' charges 6Y (Q 1, u -4, d 2, L -3, e 6).
T3  three candidate principles for the level, each read off exactly:
      P1  the product of the primes p with a whole-level tie at some power of p;
      P2  the product of the primes dividing a difference of two multiplets' charges (where charges coincide);
      P3  the least tie-free level (whole level) that is a multiple of 5 (the act's line fixes the 5-part, B1943).
    For information only: the least tie-free level N >= 2 of any kind.
C1  controls on frame C's own coupling (determinant_law.parts, column 0.13, height 6, reading S): normalised singular
    values of Y_t(w) against Y_s(k w) for ties of T1 -- N = 5 (down, lep swapped, k = 1: B1976's E2), N = 6 (up, down,
    k = 1: B1976's E1), N = 7 (up, lep swapped, k = 6 = -1) and N = 15 (up against itself swapped, k = 11) -- at two
    points of order N each; a negative control: (down, lep) at the same point, at two points of order 30 on the act's
    line, (11/30, 2/5) and (8/15, 9/10).

READING RULE.
  R1  If P1 = P2 = P3 = 30: the content's arithmetic singles out 30; P-845 gets a candidate principle, counted and post
      hoc to B1976.
  R2  If they differ: the tie arithmetic does not single out 30. The card reports which principle gives which level and
      what else would have to select 30 (B1976's alignment, carried by the 6-part, is the candidate); P-845 stays open.
  R3  A positive control of C1 differing by more than 1e-12 at either point means the unit rule does not describe frame
      C's couplings for that kind of tie, and the T1 rows of that kind are void and say so. The negative control passes
      if at least one of its two points differs by more than 1e-3; if both agree, the controls cannot tell, and say so.
Anticipated by hand (not blind): whole-level ties at N in {2, 3, 4, 5, 6, 7, 9, 15} and nowhere else; the differences'
primes {2, 3, 5}; P1 = 210, P2 = 30, P3 = 10; hence R2.

    python3 -B w_lv1_level.py <a checkout of main at be8c83d4f>     # writes w_lv1_level.json next to this file
"""
import sys, json, pathlib, subprocess
from fractions import Fraction as Fr
from math import gcd, prod

PIN = "be8c83d4f"
SECS = ("up", "down", "lep")
PAIRS = [("up", "down"), ("up", "lep"), ("down", "lep"), ("up", "up"), ("down", "down"), ("lep", "lep")]


def load(main_dir):
    head = subprocess.run(["git", "-C", main_dir, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if not head.startswith(PIN):
        sys.exit("refused: the checkout is at %s, not %s" % (head[:9] or "?", PIN))
    root = pathlib.Path(main_dir).resolve()
    sys.path.insert(0, str(next((root / "frontier").glob("B1945_*")) / "verification"))
    import determinant_law as DL
    return DL


def primes_of(n):
    n, out, p = abs(n), set(), 2
    while p * p <= n:
        while n % p == 0:
            out.add(p); n //= p
        p += 1
    if n > 1:
        out.add(n)
    return out


def tied(N, p, q, self_pair, ks=None):
    """B1976's rule: a unit k of Z/N with k p = q (mod N), or k p = q swapped. Self pairs count only swapped."""
    units = [k for k in range(1, N + 1) if gcd(k, N) == 1] if ks is None else sorted({k % N for k in ks})
    hits = []
    for k in units:
        if gcd(k, N) != 1:
            continue
        a = ((k * p[0]) % N, (k * p[1]) % N)
        if not self_pair and a == (q[0] % N, q[1] % N):
            hits.append((k % N, False))
        if a == (q[1] % N, q[0] % N):
            hits.append((k % N, True))
    return hits


def table(charges, NMAX=420):
    T = {}
    for N in range(2, NMAX + 1):
        row = {}
        for s, t in PAIRS:
            w = tied(N, charges[s], charges[t], s == t)
            pt = tied(N, charges[s], charges[t], s == t, ks=(1, -1))
            if w or pt:
                row["%s~%s" % (s, t)] = {"whole": w, "pointwise": pt}
        T[N] = row
    return T


def svn(DL, a, b, sec, ty=6.0):
    RD, Mw, Ys, u, cs, ds = DL.parts("0.13", ty, a, b, sec)
    sv = sorted(abs(x) for x in DL.mp.svd_c(Ys["S"], compute_uv=False))
    top = sv[-1] if sv[-1] != 0 else DL.mp.mpf(1)
    return [x / top for x in sv]


def diff(DL, A, B):
    return max(abs(x - y) for x, y in zip(A, B))


def main():
    DL = load(sys.argv[1])
    B = DL.B
    charges = {s: (B.SIXY[B.SECTORS[s][0]], B.SIXY[B.SECTORS[s][1]]) for s in SECS}
    mult = {m: B.SIXY[m] for m in ("Q", "u", "d", "L", "e")}
    print("inputs: sector charge pairs %s; multiplets %s; the Higgs's 6Y = %s does not enter frame C's lens" % (
        charges, mult, B.SIXY.get("H")))
    T = table(charges)
    tie_levels = [N for N, row in T.items() if any(v["whole"] for v in row.values())]
    pt_levels = [N for N, row in T.items() if any(v["pointwise"] for v in row.values())]
    print("T1 whole-level ties, N = 2..420 (k, swapped):")
    for N in tie_levels:
        print("  N = %3d: %s" % (N, {k: v["whole"] for k, v in T[N].items() if v["whole"]}))
    print("T1 pointwise ties (k = 1 or -1), N = 2..420:")
    for N in pt_levels:
        print("  N = %3d: %s" % (N, {k: v["pointwise"] for k, v in T[N].items() if v["pointwise"]}))
    tie_primes = sorted({p for N in tie_levels for p in primes_of(N) if all(q == p for q in primes_of(N))})
    level_primes = sorted({p for N in tie_levels for p in primes_of(N)})
    vals = list(mult.values())
    diffs = sorted({abs(x - y) for i, x in enumerate(vals) for y in vals[i + 1:]})
    diff_primes = sorted({p for d in diffs for p in primes_of(d)})
    print("T2 levels with a whole-level tie: %s" % tie_levels)
    print("T2 levels with a pointwise tie: %s" % pt_levels)
    print("T2 primes with a tie at some power: %s; primes of the tie levels: %s" % (tie_primes, level_primes))
    print("T2 multiplet charge differences: %s; their primes: %s" % (diffs, diff_primes))
    P1, P2 = prod(tie_primes), prod(diff_primes)
    P3 = next(N for N in range(5, 421, 5) if N not in tie_levels)
    least = next(N for N in range(2, 421) if N not in tie_levels)
    print("T3 P1 = %d, P2 = %d, P3 = %d; for information, the least tie-free level >= 2 is %d" % (P1, P2, P3, least))

    print("C1 controls on frame C's coupling (column 0.13, height 6, reading S):")
    cases = [(5, "down", "lep", 1, [(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))]),
             (6, "up", "down", 1, [(Fr(1, 6), Fr(1, 3)), (Fr(1, 2), Fr(1, 3))]),
             (7, "up", "lep", 6, [(Fr(1, 7), Fr(2, 7)), (Fr(3, 7), Fr(1, 7))]),
             (15, "up", "up", 11, [(Fr(1, 15), Fr(2, 15)), (Fr(2, 5), Fr(1, 3))])]
    C1 = []
    for N, s, t, k, pts in cases:
        found = tied(N, charges[s], charges[t], s == t, ks=(k,))
        ds = []
        for (a, b) in pts:
            ka, kb = (k * a) % 1, (k * b) % 1
            ds.append(diff(DL, svn(DL, a, b, t), svn(DL, ka, kb, s)))
        ok = bool(found) and all(d < 1e-12 for d in ds)
        C1.append(dict(N=N, s=s, t=t, k=k, rule_finds=found, diffs=[float(d) for d in ds], holds=ok))
        print("  N = %2d: Y_%s(w) against Y_%s(%d w): the rule finds %s; differences %s -> %s" % (
            N, t, s, k, found, ["%.1e" % d for d in ds], "holds" if ok else "FAILS (R3)"), flush=True)
    neg = []
    for (a, b) in [(Fr(11, 30), Fr(2, 5)), (Fr(8, 15), Fr(9, 10))]:
        neg.append(float(diff(DL, svn(DL, a, b, "down"), svn(DL, a, b, "lep"))))
    neg_ok = any(d > 1e-3 for d in neg)
    print("  negative control, (down, lep) at the same point of order 30: differences %s -> %s" % (
        ["%.1e" % d for d in neg], "passes" if neg_ok else "cannot tell (R3)"))

    if not all(c["holds"] for c in C1) or not neg_ok:
        verdict = "R3 in part: see C1"
    elif P1 == P2 == P3 == 30:
        verdict = "R1"
    else:
        verdict = "R2"
    print("READING: %s (P1 = %d, P2 = %d, P3 = %d)" % (verdict, P1, P2, P3))
    out = dict(pin=PIN, charges=charges, multiplets=mult, tie_levels=tie_levels, pointwise_levels=pt_levels,
               table={str(N): T[N] for N in tie_levels}, tie_primes=tie_primes, level_primes=level_primes,
               diffs=diffs, diff_primes=diff_primes, P1=P1, P2=P2, P3=P3, least_tie_free=least, C1=C1,
               negative_control=neg, verdict=verdict)
    pathlib.Path(__file__).with_name("w_lv1_level.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
