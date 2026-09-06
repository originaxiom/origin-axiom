#!/usr/bin/env python3
"""THE SEATS VERIFIED (2026-09-07): the other seats' chirality results, re-derived with this branch's own code.

Fetched: origin/main @ 506c591f (B1267 deciding, B1290 index formula, B1291 parity theorem, B1292 m202, B1293 harvest,
B1294 the chirality bit), origin/claude/physics-seat-evaluation @ 659487bb (fc R56-R72), origin/codex/seat-r001 @ f7a49536
(R040).  Their own scripts were re-run on this bench in detached worktrees (the table is recorded in the FINDINGS); this
script re-derives the load-bearing statements independently:

  A. B1291's parity arithmetic: |Fix| = |det(A - I)| for the eight affine cusp maps of m004 (B1279's table) is
     [0,0,0,0,0,0,4,4]; over all finite-order classes of GL(2,Z), |det(A - I)| in {0,1,2,3,4}, 3 only from the
     order-3 rotation; one cusp => even.
  B. B1294's Lefschetz numbers: L(g) = 1 - s_mu in {0, 2} (H_1(m004) = Z<mu>, H_2 = 0); the inversions' two arcs
     (chi = 2, four corners) are the L = 2 cases; on a closed QHS closing L(g) = 1 - deg g.
  C. fc R72's two lifts of the inversion to E_6: inner Ad(exp(pi i rho^v)) fixes 32 roots, algebra dim 38 = A_5 + A_1;
     the order-3 inner lift fixes 18 roots, dim 24 = A_2^3; the outer lift theta_D fixes f_4 (dim 52 from the
     sigma-split of the roots).  Plus B1280's resolution on the geometric germ: off the F_4 locus the lift is the
     OUTER one (iota^* rho = theta rho, so an inner lift would need iota^* rho = rho).
  D. fc R71's region-swap theorem: for g o sigma = -g (sigma = -1 on the torus) with transverse zeros,
     chi({g > 0}) = chi({g < 0}) = 0 -- checked on random odd trigonometric fields with a cubical Euler
     characteristic, with an even control field whose positive region is a disc (chi = 1) so the test can fail.
     This makes B1277-addendum's theta-odd 'no' exact and voids its c_(+-2,0) caveat.
  E. m202 (SnapPy, if available): two cusps, volume 4 v_tet = 2 vol(m004), hexagonal cusp shapes, |Sym| = 12,
     chiral; m004: rectangular cusp, |Sym| = 8, amphicheiral -- B1292's and R72's frame.
"""
from __future__ import annotations
import itertools, math
import numpy as np

# --------------------------------------------------------------------------------------------- A. parity
def part_a():
    maps = [(1, 1, 'identity'), (1, 1, 'period-2 swap'), (-1, -1, 'inversion theta'), (-1, -1, 'theta T'),
            (-1, 1, 'rotoreflection'), (-1, 1, 'rotoreflection'), (1, -1, 'glide'), (1, -1, 'glide')]
    fix = [abs((s - 1) * (t - 1)) for s, t, _ in maps]
    # finite-order classes of GL(2,Z): (det, tr) with |tr| <= 2 for det 1 (orders 1..6) and tr = 0 for det -1 (reflections/glides)
    classes = sorted({(1, tr) for tr in (-2, -1, 0, 1, 2)} | {(-1, 0)})
    table = {(d, tr): abs(d - tr + 1) for d, tr in classes}
    return fix, table


# --------------------------------------------------------------------------------------------- B. Lefschetz
def part_b():
    maps = [(1, 1), (1, 1), (-1, -1), (-1, -1), (-1, 1), (-1, 1), (1, -1), (1, -1)]
    L = [1 - s for s, t in maps]                     # H_0 = Z (trace 1), H_1 = Z<mu> (trace s_mu), H_2 = H_3 = 0
    return L


# --------------------------------------------------------------------------------------------- C. lifts
C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0], [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])


def e6_positive_roots():
    simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
    roots, fr = set(simple), list(simple)
    while fr:
        new = []
        for r in fr:
            rv = np.array(r)
            for i in range(6):
                t = tuple(int(x) for x in rv - (rv @ C6[:, i]) * np.array(simple[i]))
                if t not in roots and all(x >= 0 for x in t) and any(t):
                    roots.add(t); new.append(t)
        fr = new
    return sorted(roots)


def dynkin_components(rs):
    """the simple roots of a closed root subsystem given by its positive roots, and the sizes of the connected components."""
    S = set(rs)
    simp = [r for r in rs if not any(tuple(a + b for a, b in zip(x, y)) == r for x in rs for y in rs)]
    n = len(simp)
    adj = {i: [j for j in range(n) if j != i and (np.array(simp[i]) @ C6 @ np.array(simp[j])) != 0] for i in range(n)}
    seen, comps = set(), []
    for i in range(n):
        if i in seen:
            continue
        stack, comp = [i], []
        while stack:
            k = stack.pop()
            if k in seen:
                continue
            seen.add(k); comp.append(k); stack += adj[k]
        comps.append(len(comp))
    return sorted(comps, reverse=True)


def part_c():
    pos = e6_positive_roots(); assert len(pos) == 36
    ht = [sum(r) for r in pos]
    even = [r for r, h in zip(pos, ht) if h % 2 == 0]
    mod3 = [r for r, h in zip(pos, ht) if h % 3 == 0]
    sigma = lambda r: (r[5], r[1], r[4], r[3], r[2], r[0])
    fixed_sigma = [r for r in pos if sigma(r) == r]
    pairs = (len(pos) - len(fixed_sigma)) // 2
    f4_dim = 4 + 2 * len(fixed_sigma) + 2 * pairs        # Cartan 4 + the sigma-fixed root spaces + one combination per pair
    return dict(inner2=(2 * len(even), 2 * len(even) + 6, dynkin_components(even)),
                inner3=(2 * len(mod3), 2 * len(mod3) + 6, dynkin_components(mod3)),
                outer=(len(fixed_sigma) * 2, pairs, f4_dim))


# --------------------------------------------------------------------------------------------- D. region swap
def cubical_euler(mask):
    """Euler characteristic of the union of the closed grid squares marked True, on the torus (periodic grid)."""
    n, m = mask.shape
    F = int(mask.sum())
    # edges: horizontal edge between rows i and i+1 at column j belongs to the union if either adjacent square is in
    Eh = int(np.sum(mask | np.roll(mask, 1, axis=0)))     # edge on the top side of square (i,j): shared with square (i-1,j)
    Ev = int(np.sum(mask | np.roll(mask, 1, axis=1)))
    # vertices: the corner (i,j) belongs if any of the four squares touching it is in
    V = int(np.sum(mask | np.roll(mask, 1, axis=0) | np.roll(mask, 1, axis=1) | np.roll(np.roll(mask, 1, axis=0), 1, axis=1)))
    return V - (Eh + Ev) + F


def part_d(n_fields=6, N=400, seed=3):
    rng = np.random.default_rng(seed)
    x = (np.arange(N) + 0.5) / N; X, Y = np.meshgrid(x, x, indexing='ij')
    results = []
    for _ in range(n_fields):
        g = np.zeros_like(X)
        for (k, l) in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 0), (0, 2), (3, 1), (2, 3)]:
            c = rng.standard_normal(); d = rng.standard_normal()
            g += c * np.sin(2 * math.pi * (k * X + l * Y)) + d * np.sin(2 * math.pi * (k * X - l * Y))   # odd under (x,y) -> (-x,-y)
        results.append((cubical_euler(g > 0), cubical_euler(g < 0)))
    control = cubical_euler((np.cos(2 * math.pi * X) + np.cos(2 * math.pi * Y) - 1.5) > 0)       # a disc
    torus = cubical_euler(np.ones_like(X, dtype=bool))
    return results, control, torus


# --------------------------------------------------------------------------------------------- E. m202
def part_e():
    try:
        import warnings; warnings.filterwarnings("ignore")
        import snappy
    except Exception:
        return None
    out = {}
    for name in ("m004", "m202"):
        M = snappy.Manifold(name)
        vtet = 1.0149416064096536
        shapes = [complex(z) for z in M.cusp_info('shape')]
        G = M.symmetry_group()
        out[name] = dict(cusps=M.num_cusps(), vol_over_vtet=float(M.volume()) / vtet, shapes=shapes,
                         sym_order=G.order(), amphicheiral=bool(G.is_amphicheiral()))
    return out


def main():
    fix, table = part_a()
    print("A. |Fix| = |det(A - I)| for the eight cusp maps of m004:", fix, "-> values", sorted(set(fix)), "(even, one cusp)")
    print("   finite-order GL(2,Z) classes (det, tr) -> |det(A - I)|:", table, "-> 3 only from (det 1, tr -1), the order-3 rotation")
    L = part_b()
    print("B. Lefschetz numbers L(g) = 1 - s_mu over the eight isometries:", L, "-> {0, 2}; the inversions' two arcs have chi = 2")
    c = part_c()
    print(f"C. inner lift of order 2: fixed roots {c['inner2'][0]} of 72, algebra dim {c['inner2'][1]}, components {c['inner2'][2]} (A5 + A1)")
    print(f"   inner lift of order 3: fixed roots {c['inner3'][0]} of 72, algebra dim {c['inner3'][1]}, components {c['inner3'][2]} (A2^3)")
    print(f"   outer lift theta_D: sigma-fixed roots {c['outer'][0]}, root pairs {c['outer'][1]}, fixed algebra dim {c['outer'][2]} (f4)")
    print("   B1280 on the geometric germ: iota^* rho = theta rho for every deformation, so off the F_4 locus the lift is the OUTER one")
    res, control, torus = part_d()
    print(f"D. region swap: chi(g>0), chi(g<0) for random theta-odd fields: {res}; control (a disc): {control}; whole torus: {torus}")
    e = part_e()
    if e is None:
        print("E. SnapPy not available: m202 data not recomputed here")
    else:
        for k, v in e.items():
            print(f"E. {k}: cusps {v['cusps']}, vol/v_tet = {v['vol_over_vtet']:.6f}, shapes {[f'{z:.4f}' for z in v['shapes']]}, |Sym| = {v['sym_order']}, amphicheiral {v['amphicheiral']}")
    ok = (sorted(fix) == [0] * 6 + [4, 4] and set(table.values()) == {0, 1, 2, 3, 4} and table[(1, -1)] == 3
          and sorted(set(L)) == [0, 2] and c['inner2'][1:] == (38, [5, 1]) and c['inner3'][1:] == (24, [2, 2, 2]) and c['outer'][2] == 52
          and all(r == (0, 0) for r in res) and control == 1 and torus == 0)
    if e is not None:
        ok = ok and e['m202']['cusps'] == 2 and abs(e['m202']['vol_over_vtet'] - 4) < 1e-6 and e['m202']['sym_order'] == 12 and not e['m202']['amphicheiral'] \
            and e['m004']['cusps'] == 1 and e['m004']['sym_order'] == 8 and e['m004']['amphicheiral'] \
            and all(abs(z - complex(0.5, math.sqrt(3) / 2)) < 1e-6 or abs(z - complex(0.5, -math.sqrt(3) / 2)) < 1e-6 or abs(abs(z) - 1) < 1e-6 for z in e['m202']['shapes'])
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    return dict(fix=fix, table=table, L=L, lifts=c, region=(res, control, torus), snappy=e, ok=ok)


if __name__ == "__main__":
    out = main()
    raise SystemExit(0 if out['ok'] else 1)
