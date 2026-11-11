#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
THE INTEGRITY SCAN OF THE AGY LANE'S LOOP, kept for the record.  The web seat (chat1), 2026-11-11.  POST HOC as a
committed file: the seat ran this scan before its first check and did not commit it; it is committed now, after
the referee's first read of the relay, and run again on the same extracted copy of the lane's branch at 2cc5bf4e5.

It prints no content of the lane's files.  For each of the three phases it prints: whether the sha256 of the
pre-registration file is the hash in the seal file; the top-level modules the referee script imports, and whether
any of them is the lane's own engine package; the number of source lines of that engine; the names of its output
files.  It is a scan of import statements: it does not show that a referee script reads no output of the engine.

Usage: integrity_scan.py <path to the lane's self_consistent_loop directory>
"""
import ast
import hashlib
import os
import re
import sys


def main():
    root = sys.argv[1]
    phases = [('phase 1', 'self_consistent_loop_phi'), ('phase 2', 'cusped_3d_loop_phase2'), ('phase 3', 'relational_yukawa_phase3')]
    for name, d in phases:
        p = os.path.join(root, d)
        seal = open(os.path.join(p, 'SEAL_SHA256.txt')).read()
        hashes = set(re.findall(r'\b[0-9a-f]{64}\b', seal))
        pre = [f for f in os.listdir(p) if f.upper().startswith('PREREG')]
        ok = []
        for f in pre:
            h = hashlib.sha256(open(os.path.join(p, f), 'rb').read()).hexdigest()
            ok.append((f, h in hashes))
        print(name, '| hashes in the seal file:', len(hashes), '| pre-registration files and whether their sha256 is in the seal:', ok)
        prod = set(x for x in os.listdir(os.path.join(p, 'src')) if os.path.isdir(os.path.join(p, 'src', x)))
        for f in sorted(os.listdir(os.path.join(p, 'scripts'))):
            if not f.endswith('.py'):
                continue
            tree = ast.parse(open(os.path.join(p, 'scripts', f)).read())
            mods = set()
            for n in ast.walk(tree):
                if isinstance(n, ast.Import):
                    mods.update(a.name.split('.')[0] for a in n.names)
                elif isinstance(n, ast.ImportFrom) and n.module:
                    mods.add(n.module.split('.')[0])
            print('   script', f, '| imports:', sorted(mods), '| imports the engine package', sorted(prod), ':', bool(mods & prod))
        nsrc = sum(len(open(os.path.join(dp, f)).read().splitlines()) for dp, _, fs in os.walk(os.path.join(p, 'src')) for f in fs if f.endswith('.py'))
        print('   engine source lines:', nsrc, '| output files:', sorted(os.listdir(os.path.join(p, 'outputs'))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
