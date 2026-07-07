#!/usr/bin/env python3
"""B467 F3 — the wall transfer function child(p), per prereg.

GATE (verified before this table was built): 4_1(5,1) ISOMETRIC to 5_2(5,1)
(SnapPy certificate; vol 0.9813688289, H1 = Z/5; identified as m003(-2,3) —
a filling of the fig-8's SISTER). Chat-1's two-parents-one-child premise VERIFIED.

The table: child invariants vs slope p for both parents, +/- slopes.
CS convention per the R1/B460 lesson: prime the cusped manifold's CS first, then fill.
Banked anchor: CS(4_1(5,1)) = +-0.07703818 (B434) must reproduce.
Lit-frame: smoothness/asymptotics of vol(p), CS(p) are Neumann-Zagier (cited, known).
"""
import sys

import snappy


def child_row(knot, p):
    C = snappy.Manifold(knot)
    try:
        C.chern_simons()          # prime on the cusped manifold
    except Exception:
        pass
    C.dehn_fill((p, 1))
    try:
        vol = float(C.volume())
    except Exception:
        vol = float('nan')
    try:
        cs = float(C.chern_simons())
    except Exception:
        cs = None
    hom = str(C.homology())
    try:
        geo = float(C.length_spectrum(0.7)[0].length.real) if C.length_spectrum(0.7) else None
    except Exception:
        geo = None
    return vol, cs, hom, geo


def main():
    print("== the transfer function child(p) ==")
    print(f"{'p':>4} | {'vol(4_1(p,1))':>14} {'CS':>10} {'H1':>8} | {'vol(5_2(p,1))':>14} {'CS':>10} {'H1':>8} | same?")
    coincidences = []
    for p in list(range(-8, 0)) + list(range(1, 9)):
        v1, c1, h1, _ = child_row('4_1', p)
        v2, c2, h2, _ = child_row('5_2', p)
        A = snappy.Manifold(f'4_1({p},1)')
        B = snappy.Manifold(f'5_2({p},1)')
        try:
            same = A.is_isometric_to(B)
        except RuntimeError:
            same = abs(v1 - v2) < 1e-9   # volume proxy when undecided
        if same:
            coincidences.append(p)
        c1s = f"{c1:+.6f}" if c1 is not None else "   n/a  "
        c2s = f"{c2:+.6f}" if c2 is not None else "   n/a  "
        print(f"{p:>4} | {v1:>14.9f} {c1s:>10} {h1:>8} | {v2:>14.9f} {c2s:>10} {h2:>8} | {same}")
    print(f"\nslopes where the two parents give the SAME child: {coincidences}")
    # banked anchor
    _, cs5, _, _ = child_row('4_1', 5)
    anchor = cs5 is not None and abs(abs(cs5) - 0.07703818) < 1e-6
    print(f"banked anchor CS(4_1(5,1)) = +-0.07703818: {'PASS' if anchor else 'FAIL'} (got {cs5})")
    sys.exit(0 if anchor else 1)


if __name__ == '__main__':
    main()
