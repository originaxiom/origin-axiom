#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C1, FINDING E7: WHAT THE FREEDOM LEDGER'S WALK COMPUTES, READ BY THIS SEAT'S OWN ROUTE.
The web seat (chat1), 2026-11-11.  Run on main's checkout at 2f3984d27, read-only.  Prints booleans, counts and arc
names, and no claim line.

The seat had read the finding (row E7: "a sum of eleven typed zeros ... The check is a substring match"), its acceptance
row ("The verdict is not PROVED; the unpriced row and the embedding choice are in the claim line; one endpoint is credited
and named"), main's corrected claim line of B1028 through the mask, the walk b1028_walk.py and main's lock
tests/test_b1028_freedom_ledger.py, before writing this.  It has not read the advisor seat's re-audit 7.

THE ROUTE (the seat's own code; the lock counts the string "price=0.0", this parses the walk)
  Y1  The walk's syntax tree: in links(), the dict(...) calls with a keyword price; how many, and whether each value is the
      float literal 0.0; that verdict() sums r["price"] over links() and asserts that the sum is 0.0.
  Y2  B997's verdict file: its verdict, and whether its claim line holds both phrases the walk matches ("UNIQUE METALLIC
      GRAMMAR", "INFINITE FAMILY") and the correction ("the door set is {1, 4}").
  Y3  The walk run as a script (main's code, in main's checkout): whether what it prints says "outcome: COMPRESSION" and
      "0.000 retroactive designer bits", and whether it prints the correction's words.
  Y4  For each of the ten arcs the links cite: its verdict, whether its claim line begins "CORRECTED", and whether the
      phrases the walk matches are present.  Reported, not predicted, except for B997.
  Y5  The endpoint's dimension: su(3) + su(2) + u(1)^3 against su(3) + su(2) + u(1), from dim su(n) = n^2 - 1.

EXPECTATIONS (written before the run)
  Y1  eleven price keywords, all the literal 0.0; the sum is over them alone, and the zero is asserted.
  Y2  B997 is PROVED, and its line holds both phrases and the correction: the check passes on a corrected line.
  Y3  the walk prints COMPRESSION and the zero, and not the correction's words (a remaining item, if it holds).
  Y5  14 and 12.
"""
import ast
import json
import pathlib
import subprocess
import sys

MAIN = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('.')
ARC = MAIN / 'frontier' / 'B1028_freedom_ledger'
MARK = "the freedom ledger's zero is not a computed quantity"


def y1():
    tree = ast.parse((ARC / 'b1028_walk.py').read_text(encoding='utf-8'))
    links = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'links')
    prices = []
    for n in ast.walk(links):
        if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'dict':
            for kw in n.keywords:
                if kw.arg == 'price':
                    prices.append(kw.value)
    literal = [isinstance(v, ast.Constant) and isinstance(v.value, float) and v.value == 0.0 for v in prices]
    verdict = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'verdict')
    src = ast.get_source_segment((ARC / 'b1028_walk.py').read_text(encoding='utf-8'), verdict)
    sums_links = 'bits_in = sum(r["price"] for r in L)' in src and 'L, I, O = links(), inputs(), outputs()' in src
    asserts_zero = 'assert bits_in == 0.0' in src
    print('Y1  price keywords in links(): %d; all the literal 0.0: %s; verdict() sums them alone: %s; asserts the zero: %s'
          % (len(prices), all(literal), sums_links, asserts_zero))
    return len(prices) == 11 and all(literal) and sums_links and asserts_zero


def y2():
    v = json.loads((MAIN / 'frontier' / 'B997_golden_conductor_uniqueness' / 'arc_verdict.json').read_text(encoding='utf-8'))
    c = v['claim_one_line']
    a, b, k = 'UNIQUE METALLIC GRAMMAR' in c, 'INFINITE FAMILY' in c, 'the door set is {1, 4}' in c
    print('Y2  B997: verdict %s; holds "UNIQUE METALLIC GRAMMAR": %s; "INFINITE FAMILY": %s; the correction: %s; begins "CORRECTED": %s'
          % (v['verdict'], a, b, k, c.startswith('CORRECTED')))
    return v['verdict'] == 'PROVED' and a and b and k


def y3():
    r = subprocess.run([sys.executable, '-I', str(ARC / 'b1028_walk.py')], capture_output=True, text=True, cwd=str(MAIN))
    out = r.stdout
    comp = 'outcome: COMPRESSION' in out
    zero = '0.000 retroactive designer bits' in out
    corr = MARK.lower() in out.lower() or 'CORRECTED' in out or 'NOT PRICED' in out
    print('Y3  the walk run as a script: exit %d; prints "outcome: COMPRESSION": %s; prints "0.000 retroactive designer bits": %s; prints the correction: %s'
          % (r.returncode, comp, zero, corr))
    return r.returncode == 0 and comp and zero and not corr


def y4():
    tree = ast.parse((ARC / 'b1028_walk.py').read_text(encoding='utf-8'))
    links = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'links')
    cites = []
    for n in ast.walk(links):
        if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == '_cite':
            args = [a.value for a in n.args if isinstance(a, ast.Constant)]
            cites.append((args[0], args[1:]))
    print('Y4  the arcs the links cite (%d calls):' % len(cites))
    for arc, phrases in cites:
        v = json.loads((MAIN / 'frontier' / arc / 'arc_verdict.json').read_text(encoding='utf-8'))
        c = v['claim_one_line']
        print('    %-40s verdict %-8s begins CORRECTED: %-5s phrases present: %s'
              % (arc.split('_')[0], v['verdict'], c.startswith('CORRECTED'), all(p in c for p in phrases)))
    return True


def y5():
    su = lambda n: n * n - 1
    ep = su(3) + su(2) + 3
    sm = su(3) + su(2) + 1
    print('Y5  dim su(3) + su(2) + u(1)^3 = %d; dim su(3) + su(2) + u(1) = %d; difference %d' % (ep, sm, ep - sm))
    return ep == 14 and sm == 12


def main():
    print('W-C1, E7: the freedom ledger\'s walk, read by the seat\'s own route (main at %s)' % MAIN)
    res = [('Y1', y1()), ('Y2', y2()), ('Y3', y3())]
    y4()
    res.append(('Y5', y5()))
    print()
    for n, ok in res:
        print('%s: %s' % (n, 'HOLDS' if ok else 'FAILS'))
    print('EXPECTATIONS: %d of %d hold' % (sum(ok for _, ok in res), len(res)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
