#!/usr/bin/env python3
"""B1396 -- the capped Eisenstein cusp: per rotated cusp of an order-3 rotation g, the lift's weights at g's three fixed points on the
cusp torus (B1394's arc weights, read at the arcs' ends) against the character's restriction to that torus, computed separately from
the cusp's link.

The statements checked (FINDINGS.md):
  (A) the cusp's Hopf trace: the three weights at a rotated cusp c are balanced (1, w, w^2) when chi is non-trivial on T_c, and all
      equal (the lift's constant) when chi is trivial on T_c;
  (B) half lives, half dies: h^1(M; chi) >= t(chi), the number of cusps on which chi is trivial, so an acyclic chi is non-trivial on
      every cusp;
  (C) a flux cap of degree n whose charged sector carries the arc weights has n = 0 mod 3, and zero-mode content (n/3) Reg exactly
      when the weights are balanced; the multiplicities come from the holomorphic Lefschetz formula,
      m_j = [n + w^-j chi(R) + w^-2j chi(R^2)] / 3,  chi(R) = S kappa,  chi(R^2) = S' conj(kappa),  kappa = 1/(1 - w^-1)
      (one sense of rotation; balance does not depend on it);
  (E) the arc weights of B1394 are the half-sum of the cusp weights: 2 counts(arcs) = sum over rotated cusps of counts(c).
Reuses B1394's instrument (regular_three.py) unchanged.
Usage: python3 capped_cusp.py [identity|census]"""
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1394_the_regular_three" / "verification"))
import regular_three as R3                                           # noqa: E402

W = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2                        # omega = e^{2 pi i / 3}
VB, FACES = R3.VB, R3.FACES


# ------------------------------------------------------------------ (C) the theorem's arithmetic, exact in Q(omega)
def multiplicities(weights, n):
    """m_0, m_1, m_2 for fixed-point weights (exponents mod 3) and flux degree n"""
    lam = [W ** (w % 3) for w in weights]
    S = sp.expand(sum(lam))
    S2 = sp.expand(sum(x ** 2 for x in lam))
    kappa = 1 / (1 - W ** 2)                                          # 1/(1 - omega^{-1})
    chiR, chiR2 = S * kappa, S2 * sp.conjugate(kappa)
    return [sp.nsimplify(sp.simplify(sp.expand((n + W ** (-j % 3) * chiR + W ** (-2 * j % 3) * chiR2) / 3))) for j in range(3)]


def arithmetic():
    """the banked identity's first half: which n are integral for each weight pattern, and the multiplicities there"""
    out = {}
    for ws in ((0, 1, 2), (0, 0, 0), (0, 0, 1), (1, 1, 1), (0, 1, 1)):
        integral, mult = [], {}
        for n in range(-3, 7):
            m = multiplicities(ws, n)
            if all(x.is_integer for x in m):
                integral.append(n)
                mult[n] = [int(x) for x in m]
        out[ws] = (integral, mult)
    return out


# ------------------------------------------------------------------ the character on a cusp torus, from the cusp's link
def cusp_trivial(M, z, c):
    """is the character (face cocycle z mod 3) trivial on the cusp torus T_c?  The link of c is triangulated by the corners (t, v) at
    c; crossing a face f of t that contains v changes the holonomy by sgn * z[f].  Every loop of the link graph is a loop on T_c and
    its loops generate pi_1(T_c) (the small loops around the link's vertices are the edges of M, where z sums to 0).  So chi|T_c is
    trivial iff z restricted to the link graph is a coboundary."""
    FM = M.FM
    nodes = [(t.Index, j) for t in FM.tets for j in range(4) if FM.cusp_idx[t.Index][j] == c]
    psi = {nodes[0]: 0}
    stack = [nodes[0]]
    ok = True
    while stack:
        ti, j = stack.pop()
        t = FM.tets[ti]
        for F in FACES:
            if not F & VB[j]:
                continue
            fi, sgn = FM.face_index[(ti, F)]
            t2 = t.Neighbor[F]
            j2 = VB.index(t.Gluing[F].image(VB[j]))
            val = (psi[(ti, j)] + sgn * z[fi]) % 3
            key = (t2.Index, j2)
            if key in psi:
                ok = ok and psi[key] == val
            else:
                psi[key] = val
                stack.append(key)
    assert len(psi) == len(nodes), "the link of cusp %d is not connected" % c
    return ok


# ------------------------------------------------------------------ the weights at the arcs' ends
def arc_weights(M, a, comps, z, phi):
    """the lift's weight on each arc, in component order (B1394's rule, arc by arc)"""
    out = []
    for comp in comps:
        ts = [y[1] for y in comp if y[0] == "T"]
        if ts:
            out.append(phi[ts[0]])
            continue
        e = [y[1] for y in comp if y[0] == "E"][0]
        walk = M.walks[e]
        t0, ed0 = walk[0][0], walk[0][1]
        s, pp = a[t0]
        target = (s, M.img_bits(pp, ed0))
        pos = [j for j, (t, ed, fi, sg) in enumerate(walk) if (t, ed) == target][0]
        S = 0
        for j in range(pos):
            S = (S + walk[j][3] * z[walk[j][2]]) % 3
        out.append((phi[t0] + S) % 3)
    return out


def per_member(M, label):
    """rows: one per (rotation subgroup, invariant character, rotated cusp); pairs: one per (subgroup, character); failures"""
    FM = M.FM
    rows, pairs, failures = [], [], []
    seen = set()
    sub = 0
    for a_obj in FM.auts:
        if FM.aut_sign(a_obj) != {0}:
            continue
        a = M.aut_tuple(a_obj)
        if M.order(a) != 3:
            continue
        key = frozenset([a, M.compose(a, a)])
        if key in seen:
            continue
        seen.add(key)
        comps, anomalies = M.fixed_components(a)
        if anomalies:
            failures.append(("V0 the fixed set is arcs (B1390)", label, anomalies))
            continue
        if not comps:
            continue                                                  # a free order-3 symmetry: no rotated cusp
        sub += 1
        ends = [[y[1] for y in comp if y[0] == "end"] for comp in comps]
        G1T = M.G1T(a_obj)
        reps, d = M.invariant_characters(G1T)
        for idx, z in enumerate(reps):
            hs = [M.twisted(z, p, w) for (p, w) in R3.PRIMES]
            assert hs[0] == hs[1], ("primes disagree", label, hs)
            h = hs[0]
            acyclic = h == (0, 0, 0)
            lamc, phi = M.weights(a, comps, z, G1T)
            aw = arc_weights(M, a, comps, z, phi)
            assert Counter(aw) == lamc, "arc weights disagree with B1394's instrument"
            at_cusp = defaultdict(list)
            for w, (c1, c2) in zip(aw, ends):
                at_cusp[c1].append(w)
                at_cusp[c2].append(w)
            triv = {c: cusp_trivial(M, z, c) for c in range(FM.num_cusps)}
            where = dict(member=label, sub=sub, chi=idx, trivial_chi=(idx == 0), h=list(h))
            total = [0, 0, 0]
            for c, ws in sorted(at_cusp.items()):
                cnt = [ws.count(j) for j in range(3)]
                total = [x + y for x, y in zip(total, cnt)]
                balanced, equal = cnt == [1, 1, 1], max(cnt) == 3
                self_arcs = sum(1 for (c1, c2) in ends if c1 == c2 == c)
                rows.append(dict(where, cusp=c, weights=sorted(ws), counts=cnt, balanced=balanced, all_equal=equal,
                                 chi_trivial_on_cusp=triv[c], self_arcs=self_arcs, acyclic=acyclic))
                if len(ws) != 3:
                    failures.append(("V1 three ends per rotated cusp", where, c, ws))
                if not (balanced or equal):
                    failures.append(("V2 all equal or balanced (A)", where, c, ws))
                if balanced == triv[c]:
                    failures.append(("V3 balanced iff chi non-trivial on the cusp (A)", where, c, ws, triv[c]))
            if acyclic and any(triv.values()):
                failures.append(("V4 acyclic => non-trivial on every cusp (B)", where, triv))
            if h[1] < sum(triv.values()):
                failures.append(("V6 h1 >= the number of cusps where chi is trivial (B)", where, h, triv))
            arc_counts = [lamc.get(j, 0) for j in range(3)]
            if [2 * x for x in arc_counts] != total:
                failures.append(("V5 2 counts(arcs) = sum of cusp counts (E)", where, arc_counts, total))
            pairs.append(dict(where, acyclic=acyclic, k=len(comps), arc_counts=arc_counts,
                              rotated_cusps=len(at_cusp), trivial_rotated=[c for c in sorted(at_cusp) if triv[c]],
                              trivial_cusps_all=[c for c in range(FM.num_cusps) if triv[c]]))
    return rows, pairs, failures


def identity():
    """the banked identity: the arithmetic of (C), and m202 (the lane's R32 case) -- both rotated cusps balanced at the two
    non-trivial invariant characters, all equal at the trivial one, no arc returning to its own cusp.  Returns the failures."""
    bad = []
    ar = arithmetic()
    if ar[(0, 1, 2)][0] != [-3, 0, 3, 6] or any(m != [n // 3] * 3 for n, m in ar[(0, 1, 2)][1].items()):
        bad.append(("balanced: n = 0 mod 3 and (n/3) Reg", ar[(0, 1, 2)]))
    if ar[(0, 0, 0)][0] != [-3, 0, 3, 6] or any(m != [n // 3 + 1, n // 3 - 1, n // 3] for n, m in ar[(0, 0, 0)][1].items()):
        bad.append(("all equal: n = 0 mod 3 and (n/3 + 1, n/3 - 1, n/3)", ar[(0, 0, 0)]))
    if ar[(0, 0, 1)][0] != [-2, 1, 4]:
        bad.append(("(1, 1, w): n = 1 mod 3", ar[(0, 0, 1)]))
    M = R3.member_from("m202", "m202")
    rows, pairs, failures = per_member(M, "m202")
    bad += failures
    nontriv = [r for r in rows if not r["trivial_chi"]]
    if not (len(pairs) == 3 and len(nontriv) == 4 and all(r["balanced"] and not r["chi_trivial_on_cusp"] for r in nontriv)):
        bad.append(("m202: two non-trivial characters, both rotated cusps balanced", nontriv))
    if any(r["self_arcs"] for r in rows):
        bad.append(("m202: no self-arc", rows))
    if not all(r["all_equal"] and r["chi_trivial_on_cusp"] for r in rows if r["trivial_chi"]):
        bad.append(("m202: the trivial character all equal", rows))
    return bad, ar, rows


def census(out_json=None):
    t0 = time.time()
    arith = R3.census_members()
    RP = R3._load("b1386_the_open_cusp", "frontier/B1386_the_open_eisenstein_cusp/verification/the_open_cusp.py")
    todo = [(n, n) for n in arith] + [("cube~3.24", RP.member())]
    rows, pairs, failures = [], [], []
    for i, (label, src) in enumerate(todo):
        t1 = time.time()
        r, p, f = per_member(R3.member_from(src, label), label)
        rows += r
        pairs += p
        failures += f
        if p:
            print("member %3d/%d %-12s pairs %3d  cusp rows %4d  %.1f s" % (i + 1, len(todo), label, len(p), len(r), time.time() - t1),
                  file=sys.stderr, flush=True)
    nontriv_pairs = [p for p in pairs if not p["trivial_chi"]]
    cusp_triv_nontriv = [p for p in nontriv_pairs if p["trivial_rotated"]]
    summary = dict(
        members=len(todo), members_with_rotations=len({p["member"] for p in pairs}), pairs=len(pairs),
        nontrivial_pairs=len(nontriv_pairs), acyclic_nontrivial=sum(1 for p in nontriv_pairs if p["acyclic"]),
        cusp_rows=len(rows), cusp_rows_nontrivial_chi=sum(1 for r in rows if not r["trivial_chi"]),
        balanced_rows=sum(1 for r in rows if r["balanced"]), all_equal_rows=sum(1 for r in rows if r["all_equal"]),
        failures=len(failures),
        acyclic_with_unbalanced_cusp=sum(1 for p in nontriv_pairs if p["acyclic"] and p["trivial_rotated"]),
        nontrivial_chi_trivial_on_a_rotated_cusp=len(cusp_triv_nontriv),
        members_where=sorted({p["member"] for p in cusp_triv_nontriv}),
        self_arc_rows=sum(1 for r in rows if r["self_arcs"]),
        h1_equals_trivial_cusps=sum(1 for p in pairs if p["h"][1] == len(p["trivial_cusps_all"])),
        unbalanced_arc_pairs_nontrivial=sum(1 for p in nontriv_pairs if len(set(p["arc_counts"])) > 1),
        seconds=round(time.time() - t0))
    if out_json:
        json.dump(dict(summary=summary, failures=failures, pairs=pairs, rows=rows), open(out_json, "w"), indent=1)
    return summary, failures, pairs, rows


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "identity"
    t0 = time.time()
    bad, ar, rows = identity()
    print("## the banked identity: the arithmetic of (C) and m202")
    for ws, (integral, mult) in ar.items():
        print("weights %s: integral n in [-3, 6] = %s; multiplicities %s" % (ws, integral, mult))
    for r in rows:
        print("m202", {k: r[k] for k in ("sub", "chi", "cusp", "weights", "balanced", "chi_trivial_on_cusp", "self_arcs", "acyclic")})
    print("identity failures:", bad)
    if bad:
        sys.exit("the banked identity failed; nothing below is read")
    if mode == "census":
        summary, failures, pairs, rows = census(out_json=str(HERE / "capped_census.json"))
        for k, v in summary.items():
            print("%-42s %s" % (k, v))
        print("failures:", failures[:10])
        print("non-trivial characters trivial on a rotated cusp:")
        for p in pairs:
            if not p["trivial_chi"] and p["trivial_rotated"]:
                print("   ", p)
    print("(%.0f s)" % (time.time() - t0))
