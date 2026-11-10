#!/usr/bin/env python3
"""The non-cancellation reading as a selection rule: an exact, exhaustive enumeration (data-free; integers only).

Definitions (B1853's, extended to the metallic backgrounds):
  background  the metallic word (L^b R^b)^k, b = 1 golden, 2 silver, 3 bronze; its runs are all b
  defect      m consecutive background runs replaced by runs S = (r_1 .. r_m), r_i >= 1, r_1 != b, r_m != b
  E(S)        D_S * D_bg(m)^-1, with D the alternating product L^r1 R^r2 ...
  letters     sum(S) -- the size of the departure as a word; the grammar's own count, no metric
  extra       sum(S) - b*m
Visibility at a level N:
  charge+     E = +I mod N              charge+-   E = +-I mod N
  line        E commutes with the background's period A_b = L^b R^b mod N
The enumeration is exhaustive over every defect with letters <= B, so 'least' is exact below B.
    python3 relays/advisor_2026-11-10_audit/non_cancellation/nc_enumerate.py [B]"""
import sys, math, json, os, collections
B = int(sys.argv[1]) if len(sys.argv) > 1 else 20
MOD = 2 * 3 * 4 * 5 * 8 * 13 * 7 * 11                      # every level tested divides this
I2 = (1, 0, 0, 1)
def mul(A, C, M=MOD): return ((A[0]*C[0]+A[1]*C[2]) % M, (A[0]*C[1]+A[1]*C[3]) % M, (A[2]*C[0]+A[3]*C[2]) % M, (A[2]*C[1]+A[3]*C[3]) % M)
def inv(A): return (A[3] % MOD, (-A[1]) % MOD, (-A[2]) % MOD, A[0] % MOD)
def Lp(r): return (1, r % MOD, 0, 1)
def Rp(r): return (1, 0, r % MOD, 1)
def red(A, N): return tuple(x % N for x in A)

def facts():
    out = []
    for b in (1, 2, 3):
        t = b * b + 2
        own = [N for N in range(2, 200) if (b * b + 4) % N == 0]
        out.append("background b=%d: A = L^%dR^%d, tr %d; A = -(unipotent) mod N exactly for N | b^2+4 = %d: %s" % (b, b, b, t, b*b+4, own))
    return out

def search(b, levels, B):
    """every defect with letters <= B on background b; returns {(premise, level-set): sorted list of (letters, extra, S)}"""
    A = mul(Lp(b), Rp(b))
    hits = collections.defaultdict(list); count = 0
    def test(S, DS, Dg):
        nonlocal count
        count += 1
        E = mul(DS, inv(Dg)); n = sum(S); ex = n - b * len(S)
        for name, Ns in levels.items():
            Em = [red(E, N) for N in Ns]
            if all(e == red(I2, N) for e, N in zip(Em, Ns)): hits[("charge+", name)].append((n, ex, S))
            if all(e in (red(I2, N), tuple((-x) % N for x in red(I2, N))) for e, N in zip(Em, Ns)): hits[("charge+-", name)].append((n, ex, S))
            if all(red(mul(E, A), N) == red(mul(A, E), N) for N in Ns): hits[("line", name)].append((n, ex, S))
    def rec(S, DS, Dg, n):
        i = len(S)
        X = Lp if i % 2 == 0 else Rp
        for r in range(1, B - n + 1):
            if i == 0 and r == b: continue
            S2 = S + (r,); DS2 = mul(DS, X(r)); Dg2 = mul(Dg, X(b))
            if r != b: test(S2, DS2, Dg2)
            if n + r < B: rec(S2, DS2, Dg2, n + r)
    rec((), I2, I2, 0)
    for k in hits: hits[k].sort()
    return hits, count

def report(b, levels, B):
    hits, count = search(b, levels, B)
    lines = ["", "background b=%d: %d defects with letters <= %d" % (b, count, B)]
    res = {}
    for name in levels:
        for prem in ("charge+", "charge+-", "line"):
            h = hits.get((prem, name), [])
            if not h:
                lines.append("  %-9s at %-12s none with letters <= %d" % (prem, name, B)); res["%s|%s" % (prem, name)] = None; continue
            n0 = h[0][0]; least = [x for x in h if x[0] == n0]
            nxt = next((x for x in h if x[0] > n0), None)
            exmin = min(x[1] for x in h); least_ex = [x for x in h if x[1] == exmin]
            lines.append("  %-9s at %-12s by letters: least %d, %d defect(s): %s%s | next %s | by extra letters: least %d, %d defect(s) below the bound%s" % (
                prem, name, n0, len(least), [x[2] for x in least[:6]], " ..." if len(least) > 6 else "",
                (nxt[0], nxt[2]) if nxt else "none below the bound", exmin, len(least_ex),
                ": " + str([x[2] for x in least_ex[:4]]) + (" ..." if len(least_ex) > 4 else "")))
            res["%s|%s" % (prem, name)] = dict(least_letters=n0, least=[x[2] for x in least], next=(list(nxt) if nxt else None),
                                               least_extra=exmin, n_least_extra=len(least_ex), least_extra_examples=[x[2] for x in least_ex[:8]])
    return lines, res

if __name__ == "__main__":
    out = ["non-cancellation enumeration, exhaustive to B = %d letters" % B] + facts()
    allres = {}
    gold = {"5": (5,), "2": (2,), "3": (3,), "4": (4,), "4,5": (4, 5), "2,3,4,5": (2, 3, 4, 5), "11": (11,), "7": (7,)}
    l, r = report(1, gold, B); out += l; allres["golden"] = r
    l, r = report(2, {"8": (8,), "4": (4,), "2": (2,), "5": (5,)}, B); out += l; allres["silver"] = r
    l, r = report(3, {"13": (13,), "5": (5,)}, B); out += l; allres["bronze"] = r
    print("\n".join(out))
    json.dump(allres, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nc_enumerate_B%d.json" % B), "w"), indent=1)
