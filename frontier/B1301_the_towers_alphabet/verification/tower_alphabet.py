#!/usr/bin/env python3
"""THE TOWER'S ALPHABET (B1301): the h^1 support of the closings Y_3, Y_4, Y_6, Y_9, Y_12 (the n-fold cyclic branched
covers of the object -- the Fibonacci manifolds), the deck action on it, the pullback structure between levels, and the
Standard-Model Wilson lines and the triplet's protection on the first closing whose alphabet has a 2-part beyond the
family group.

(a) For each n: H_1(Y_n) by Smith form (Fox's product |prod Delta(zeta)| as check), the deck transformation t (the shift
    x_k -> x_{k+1} of the Schreier generators; the filled meridian z = a^n is trivial), the deck orbits of the characters,
    h^1(Y_n; psi) on one representative per orbit (Fox calculus, 40 digits; deck invariance of h^1 checked on random
    full orbits), every positive confirmed exactly over Q(zeta_order(psi)).
(b) The deck-eigen structure of the support: psi with t.psi = psi^lambda; on Y_9 the odd support is exactly the set of
    eigencharacters (lambda = 6, 16, the roots of Delta = t^2 - 3t + 1 modulo 19, primitive 9th roots of unity); on Y_4,
    Y_6 the order-5 eigencharacters (lambda = -1, not a primitive n-th root) have h^1 = 0; on Y_12 the odd part has no
    support at all (Delta has no root mod 3; -1 is not a primitive 12th root mod 5).
(c) Pullbacks Y_d -> Y_n (d | n): x_k -> x_{k mod d}; the support of Y_d pulls back into the support of Y_n (transfer);
    the NEW support at each level.
(d) The alphabet K3 of each closing, the lines (psi_Q, psi_u, psi_L) in K3^3 with every multiplet's multiplicity
    (lines_from_support.py, the weight table of B1300), B1278's classes, and the triplet's protection test.
Support files support_Y{n}.json (the positives, the family characters, H_1) are written next to this script.
"""
from __future__ import annotations
import sys, math, time, json, collections, pathlib
import numpy as np, sympy as sp, mpmath as mp
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for arc in ("B1267_spectrum_law_rebuilt", "B1268_cusped_net_chirality_bound", "B1269_transport_computed",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles", "B1275_the_cubic_made_explicit",
            "B1276_the_relations_the_chain_forces", "B1277_the_vacuum_manifold_of_the_closing", "B1278_the_six_fold_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))
sys.path.insert(0, str(HERE))
import six_fold_closing as SF
import lines_from_support as LS
TW = SF.TW


def deck(a, n):
    """the deck transformation on a character a = (a_z, a_0, ..., a_{n-1}): conjugation by a shifts x_k -> x_{k+1}."""
    return (a[0],) + (a[n],) + tuple(a[1:n])


def order_of(a, m):
    return max([m // math.gcd(x, m) for x in a] + [1])


_G = {}


def _init(gens, rels, m, dps):
    mp.mp.dps = dps
    _G.update(gens=gens, rels=rels, m=m)


def _h1(a):
    h, h0, lo, hi = SF.h1_numeric(_G['gens'], _G['rels'], a, _G['m'])
    return a, h, lo, hi


def eigenvalues(A, B, m):
    """for rows a (A) and t.a (B): the lambda in Z/m with B = lambda A, or -1."""
    lam = -np.ones(len(A), dtype=np.int64)
    for l in range(m):
        ok = np.all((l * A - B) % m == 0, axis=1)
        lam[ok & (lam < 0)] = l
    return lam


def level(n, dps=40, workers=3, control_orbits=30, exact_max_order=None, out_dir=None):
    t0 = time.time()
    gens, rels = TW.presentation(n, branched=True)
    Rm = SF.relation_matrix(gens, rels)
    D, U, V = SF.smith_with_transforms(Rm)
    inv = [int(D[j, j]) for j in range(min(D.shape))]
    tors = sorted(d for d in inv if d not in (0, 1))
    free = len(gens) - sum(1 for d in inv if d != 0)
    m = 1
    for d in tors:
        m = m * d // math.gcd(m, d)
    order = int(np.prod(tors)) if tors else 1
    fox = SF.alexander_order(n)
    assert free == 0 and order == fox
    chars, coords, moduli = SF.characters(D, V, m, with_coords=True)
    assert len(chars) == order == len(set(chars))
    print(f"\n=== Y_{n}: H_1 = {' + '.join(f'Z/{d}' for d in tors)}, order {order} = Fox's product {fox}, exponent {m}; {len(gens)} generators ===", flush=True)
    S = set(chars); reps = {}; orbit_of = {}
    for a in chars:
        if a in orbit_of:
            continue
        orb = [a]; b = deck(a, n)
        while b != a:
            orb.append(b); b = deck(b, n)
        for x in orb:
            orbit_of[x] = a
        reps[a] = orb
    assert all(deck(a, n) in S for a in chars)
    sizes = collections.Counter(len(o) for o in reps.values())
    print(f"  the deck transformation permutes the characters: {len(reps)} orbits, sizes {dict(sorted(sizes.items()))}", flush=True)
    t1 = time.time()
    with Pool(workers, initializer=_init, initargs=(gens, rels, m, dps)) as pool:
        res = pool.map(_h1, list(reps.keys()), chunksize=16)
    h1 = {}; lo_all, hi_all = 1.0, 0.0
    for a, h, lo, hi in res:
        for x in reps[a]:
            h1[x] = h
        lo_all = min(lo_all, lo); hi_all = max(hi_all, hi)
    dist = dict(sorted(collections.Counter(h1.values()).items()))
    print(f"  h^1(Y_{n}; psi) on one representative per orbit ({len(reps)} Fox computations, {dps} digits, {time.time() - t1:.0f} s): distribution over all {order} characters {dist}; smallest accepted singular value {lo_all:.3e}, largest rejected {hi_all:.3e}", flush=True)
    # deck invariance of h^1: recompute on every element of random full orbits
    rng = np.random.default_rng(1)
    sample = [a for a in reps if len(reps[a]) > 1]
    idx = rng.choice(len(sample), size=min(control_orbits, len(sample)), replace=False)
    mp.mp.dps = dps
    bad = sum(SF.h1_numeric(gens, rels, x, m)[0] != h1[x] for i in idx for x in reps[sample[i]])
    print(f"  deck-invariance control: h^1 recomputed on every element of {len(idx)} full orbits, mismatches {bad}", flush=True)
    assert bad == 0
    pos = [a for a in chars if h1[a] > 0]
    # exact confirmation of every positive over Q(zeta_order): the character takes values in the order-th roots of unity
    t2 = time.time(); ok = True; skipped = 0
    for a in pos:
        o = order_of(a, m); step = m // o
        assert all(x % step == 0 for x in a)
        if exact_max_order is not None and o > exact_max_order:
            skipped += 1; continue
        ok &= (SF.h1_exact(gens, rels, tuple(x // step for x in a), o) == h1[a])
    zeros = [a for a in chars if h1[a] == 0 and a != tuple([0] * len(gens))][:3]
    for a in zeros:
        o = order_of(a, m); step = m // o
        ok &= (SF.h1_exact(gens, rels, tuple(x // step for x in a), o) == 0)
    print(f"  exact confirmation over Q(zeta_order(psi)) of all {len(pos) - skipped} positives{' (' + str(skipped) + ' of order > ' + str(exact_max_order) + ' skipped)' if skipped else ''} and {len(zeros)} zero controls: {ok} ({time.time() - t2:.0f} s)", flush=True)
    assert ok
    chis = SF.family_characters(n, gens, m) if n % 3 == 0 else None
    if chis:
        perm = [chis.index(deck(c, n)) for c in chis]
        print(f"  family characters: h^1 = {[h1[c] for c in chis]}; the deck permutes them as {perm} (a 3-cycle: Delta = t^2 + t + 1 mod 2)", flush=True)
    byord = dict(sorted(collections.Counter(order_of(a, m) for a in pos).items()))
    print(f"  support: {len(pos)} characters, by order {byord}", flush=True)
    # (b) eigen-structure
    A = np.array(chars, dtype=np.int64); B = np.array([deck(a, n) for a in chars], dtype=np.int64)
    lam = eigenvalues(A, B, m)
    H = np.array([h1[a] for a in chars]); ords = np.array([order_of(a, m) for a in chars])
    eig = collections.Counter()
    for i in np.where(lam >= 0)[0]:
        eig[(int(ords[i]), int(lam[i] % ords[i]) if ords[i] > 1 else 0, int(H[i]))] += 1
    print(f"  deck eigencharacters t.psi = psi^lambda, (order, lambda mod order, h^1) -> count: {dict(sorted(eig.items()))}", flush=True)
    sup_eig = collections.Counter()
    for a in pos:
        i = chars.index(a); o = order_of(a, m)
        sup_eig[(o, int(lam[i] % o) if lam[i] >= 0 else None)] += 1
    print(f"  the support's eigen-structure (order, lambda mod order or None) -> count: {dict(sorted(sup_eig.items(), key=str))}", flush=True)
    print(f"  ({time.time() - t0:.0f} s)", flush=True)
    data = dict(n=n, tors=tors, m=m, gens=len(gens), order=order, dist=dist, positives=[list(a) for a in pos],
                chis=[list(c) for c in chis] if chis else None, eig=[[k[0], k[1], k[2], v] for k, v in sorted(eig.items())],
                lo=lo_all, hi=hi_all)
    ((pathlib.Path(out_dir) if out_dir else HERE) / f"support_Y{n}.json").write_text(json.dumps(data))
    return dict(n=n, gens=gens, rels=rels, m=m, tors=tors, chars=chars, h1=h1, chis=chis, pos=pos, dist=dist, eig=eig, sup_eig=sup_eig)


def pullback(low, high):
    nl, nh, ml, mh = low['n'], high['n'], low['m'], high['m']
    assert nh % nl == 0 and mh % ml == 0
    return {a: tuple((x * (mh // ml)) % mh for x in (0,) + tuple(a[1 + (k % nl)] for k in range(nh))) for a in low['chars']}


def main(levels=(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), workers=3):
    t0 = time.time()
    L = {n: level(n, workers=workers) for n in levels}
    out = {n: dict(tors=L[n]['tors'], dist=L[n]['dist'], support=len(L[n]['pos'])) for n in levels}
    print("\n=== (c) pullbacks between levels ===", flush=True)
    for hi in levels:
        Hh = L[hi]; old = set()
        for lo in levels:
            if lo < hi and hi % lo == 0:
                pb = pullback(L[lo], Hh)
                land = all(pb[a] in set(Hh['chars']) for a in L[lo]['chars'])
                sup_ok = all(Hh['h1'][pb[a]] >= 1 for a in L[lo]['pos'])
                pulled = {pb[a] for a in L[lo]['pos']}; old |= pulled
                print(f"  Y_{lo} -> Y_{hi}: pulled-back characters are characters: {land}; the support of Y_{lo} lands in the support of Y_{hi}: {sup_ok} ({len(pulled)} characters)", flush=True)
                out[hi][f'pullback_{lo}'] = dict(land=land, sup_ok=sup_ok, n=len(pulled))
                assert land and sup_ok
        new = [a for a in Hh['pos'] if a not in old]
        byord = dict(sorted(collections.Counter(order_of(a, Hh['m']) for a in new).items()))
        print(f"  Y_{hi}: support {len(Hh['pos'])} = {len(set(Hh['pos']) & old)} pulled back from lower levels + {len(new)} NEW, the new by order {byord}", flush=True)
        out[hi]['new'] = len(new); out[hi]['new_by_order'] = byord
    print("\n=== (d) the alphabet, the lines and the triplet's protection on each closing with family characters ===", flush=True)
    for n in levels:
        if n % 3:
            continue
        r = LS.run(HERE / f"support_Y{n}.json", n, roots=HERE / "e6_roots_qul.json")
        out[n]['lines'] = r
    print(f"\n  ({time.time() - t0:.0f} s)", flush=True)
    return out


if __name__ == "__main__":
    out = main()
    ok = (out[9]['lines']['counts'] == dict(three_gen=758593, su5_broken=737568, sm_vacua=706464, full=568656)
          and out[9]['support'] == 147 and out[6]['support'] == 27 and out[4]['support'] == 0 and out[3]['support'] == 3
          and out[2]['support'] == 0 and out[5]['support'] == 20 and out[7]['support'] == 56 and out[8]['support'] == 0
          and out[10]['support'] == 20 and out[10]['new'] == 0 and out[12]['support'] == 123 and out[12]['new'] == 96
          and out[12]['lines']['n_split'] == 0 and out[12]['lines']['d_totals'] == [1, 3])
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
