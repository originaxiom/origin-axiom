#!/usr/bin/env python3
"""WP-1.5, first step; harvest row 918 on main: the frame at the weave's common point reads rank-one lines, and no line
on a once-punctured-torus bundle is interior (the SM seat's W8 and its Lemma V).

THE STATEMENTS (the seat's, at its commit; read as statements, none of its code run)
  LEMMA V.  nu a character of a hyperbolic once-punctured-torus bundle, of finite order when it is trivial on the fibre.
  Then h1(nu) <= 1; and when h1(nu) = 1, nu is trivial on the cusp and the class restricts to it injectively, so n = 0.
  THE CENSUS.  On each of the 24 states to length 6, at its resolving tick: each of the three non-zero parities carries
  exactly one line (h1 = 1 at one of kappa = +-1), 72 lines, none interior; of the 768 characters of order dividing 4
  none has n > 0.
MAIN'S READING OF THE PROOF (in its own words; found right).  Trivial on the fibre: the Wang sequence gives
h1 = [kappa = 1] + [1/kappa is an eigenvalue of the act on H1 of the fibre]; the act is hyperbolic, its eigenvalues are
not roots of unity, so h1 = 1 only for the trivial character, whose class is the fibration's and is not zero on the
cusp.  Not trivial on the fibre: H0 of the fibre vanishes, so H1 of the bundle injects into H1 of the fibre, which is
one-dimensional (Euler characteristic -1); that class restricts isomorphically to the puncture loop, because the next
term of the pair's sequence is H0 of the fibre again; the loop lies on the cusp torus, and a character that is not
trivial on the torus has no H1 there; so the character is trivial on the cusp and the class is not zero on it.
WHAT MAIN COMPUTES, exactly (Gaussian integers; the tick built by kernel_site.py from the base's own presentation):
for every character of order dividing 4 of every tick: h1, whether it is trivial on the cusp, the rank of the
restriction to the cusp, and n.
HOW IT COULD FAIL: h1 = 2 anywhere; a class that dies on the cusp; a count of characters that is not the seat's; the
planted case, a "bundle" whose relators are dropped (a free group), must show h1 > 1."""
import sys, json, pathlib, collections
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parity_sectors_on_main as PS

POW = [sp.Integer(1), sp.I, sp.Integer(-1), -sp.I]


def line(K, e, rels=None, cusps=None):
    """(h1, trivial on the cusp, rank of the restriction, n) of the rank-one module with exponents e mod 4, exactly"""
    rels = K.rels if rels is None else rels; cusps = K.cusps if cusps is None else cusps
    val = lambda ex: POW[sum(a * b for a, b in zip(ex, e)) % 4]
    def fox(t):
        row = [sp.Integer(0)] * K.n; ex = [0] * K.n
        for k, s in t:
            if s > 0: row[k] += val(ex); ex[k] += 1
            else: ex[k] -= 1; row[k] -= val(ex)
        return row, val(ex)
    d0 = sp.Matrix([[POW[e[k] % 4] - 1] for k in range(K.n)]); r0 = d0.rank()
    d1 = sp.Matrix([fox(t)[0] for t in rels]) if rels else sp.zeros(0, K.n); rd1 = d1.rank() if rels else 0
    a1 = K.n - rd1 - r0
    block_rows, rB, triv = [], 0, True
    for (a, b) in cusps:
        ra, va = fox(a); rb, vb = fox(b)
        B = sp.Matrix([[va - 1], [vb - 1]]); rB += B.rank(); triv &= (va == 1 and vb == 1)
        block_rows += [ra + [va - 1], rb + [vb - 1]]
    block = sp.Matrix([list(r) + [0] for r in (d1.tolist() if rels else [])] + block_rows)
    r1 = block.rank() - rd1 - rB
    return int(a1), bool(triv), int(r1), int(a1 - r1)


if __name__ == "__main__":
    names = sys.argv[1:] or ["b+%s%s" % (s, w) for w in PS.WORDS for s in "+-"]
    CHECKS, rows, total = [], {}, 0
    def check(name, ok, detail=""):
        CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""), flush=True)
    worst_h1, interior, dead, parity_lines, lines_total = 0, 0, 0, 0, 0
    for name in names:
        K, n, epsK = PS.state(name); ch = K.characters(4); total += len(ch)
        par = tuple(v % 2 for v in epsK); got = collections.Counter(); per_class = collections.Counter()
        for e in ch:
            h1, triv, r1, nn = line(K, e)
            worst_h1 = max(worst_h1, h1); interior += (nn > 0); got[(h1, triv, r1, nn)] += 1
            if h1 >= 1:
                lines_total += 1
                if not (triv and r1 == h1): dead += 1
                if all(x in (0, 2) for x in e):                               # a sign character: which class
                    s = tuple(x // 2 for x in e); key = min(s, tuple((a + b) % 2 for a, b in zip(s, par)))
                    if key != min(tuple([0] * K.n), par): per_class[key] += 1
        parity_lines += sum(per_class.values())
        rows[name] = {"tick": n, "characters of order dividing 4": len(ch), "by (h1, trivial on the cusp, rank of the restriction, n)": {str(k): v for k, v in got.items()},
                      "lines on each non-zero parity": sorted(per_class.values())}
        print("%-12s tick %d: %3d characters; %s; lines on the three parities: %s" % (name, n, len(ch), dict(got), sorted(per_class.values())), flush=True)
    check("the characters of order dividing 4 on the 24 ticks number 768, the seat's count", total == 768 or len(names) < 24, total)
    check("LEMMA V on every one of them: h1 is 0 or 1", worst_h1 <= 1, "the largest h1: %d" % worst_h1)
    check("and where h1 = 1 the character is trivial on the cusp and the class restricts to it injectively", dead == 0, "%d lines; %d that fail" % (lines_total, dead))
    check("so none is interior: n = 0 for every character", interior == 0)
    check("each of the three non-zero parities carries exactly one line among the sign characters, on every state: 72 lines", all(r["lines on each non-zero parity"] == [1, 1, 1] for r in rows.values()) and (parity_lines == 72 or len(names) < 24), parity_lines)
    # planted: the same generators with every relator dropped is a free group, where a line has h1 = (generators - 1) > 1
    K, n, epsK = PS.state("b++LLR")
    h1, triv, r1, nn = line(K, tuple([2] + [0] * (K.n - 1)), rels=[], cusps=[])
    check("planted: with the relators dropped (a free group) a line has h1 above 1, so the instrument can see it", h1 > 1, "h1 = %d on %d generators" % (h1, K.n))
    json.dump({"rows": rows, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "the_common_point_on_main.json", "w"), indent=1)
    print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
