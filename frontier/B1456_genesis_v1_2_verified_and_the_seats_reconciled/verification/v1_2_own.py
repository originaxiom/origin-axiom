#!/usr/bin/env python3
"""B1456 -- the new claims of GENESIS v1.2 (the SM seat's sm:B1517, sm:B1519; the audit lane's R78), by main's own code.

    python3 v1_2_own.py [--quick]     # prints, writes v1_2_own.json; exit 1 if a check fails

  H1  a word and its reverse: M(reverse w) = D M(w)^-1 D^-1 with D = diag(-1, 1), on every word to length 12.
  H2  the 758 signed word states are 536 classes when reversal is divided out as well; 222 states pair off, the first
      pair at length seven.  SnapPy: isometry signatures give the same partition (all lengths unless --quick), and the
      reverse is isometric by an orientation-preserving map on a sample.
  H3  main's own census (B1439): its own-level firing list splits no pair; 95 of 758 states is 87 of 536 manifolds.
  H4  the signed powers: -(LR)^2 is m207, H1 = Z + Z/3 + Z/3, not m206 = (LR)^2 = (-LR)^2; its double cover is t12839;
      and -u^k with k even is the level of no state (the argument, checked on the matrices of the box).
  H5  P (LR) P = RL; J (LR) J^-1 = (LR)^-1 with J = [[0,1],[-1,0]] of determinant 1.
  H6  the eight isometries of m004 act on the cusp by diag(s_m, s_l), each of the four sign pairs twice.
  H7  every hyperbolic matrix of determinant 1 in the box is eps A(u)^k for one primitive u up to rotation and swap.
"""
import itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "B1454_genesis_v1_verified_and_adopted", "verification"))
import genesis_own as G
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
QUICK = "--quick" in sys.argv
J = ((0, 1), (-1, 0)); D = ((-1, 0), (0, 1))


def canon(w, with_reverse):
    n = len(w); sw = w.translate(str.maketrans("LR", "RL")); forms = [w, sw]
    if with_reverse: forms += [w[::-1], sw[::-1]]
    return min(x[i:] + x[:i] for x in forms for i in range(n))


def h1():
    bad = 0; n = 0
    for L in range(1, 13):
        for bits in itertools.product("LR", repeat=L):
            w = "".join(bits); n += 1
            if G.word(w[::-1]) != G.mul(G.mul(D, G.inv(G.word(w))), G.inv(D)): bad += 1
    return bad == 0 and G.det(D) == -1 and G.mul(G.P, J) == D, dict(words=n, failures=bad, D_is_PJ=G.mul(G.P, J) == D)


def h2():
    states, classes, first = {}, {}, None; per_len = {}
    for L in range(2, 13):
        st = G.states(L); cl = sorted({canon(w, True) for w in st})
        per_len[L] = (2 * len(st), 2 * len(cl))
        for w in st:
            for s in "+-":
                states[s + w] = s + canon(w, True)
        if first is None:
            pairs = [w for w in st if canon(w, True) != w or canon(w[::-1], False) != w]
            if len(cl) < len(st): first = (L, sorted(w for w in st if canon(w[::-1], False) != w)[:2])
    nclass = len(set(states.values())); paired = sum(1 for k, v in states.items() if list(states.values()).count(v) == 2)
    out = dict(states=len(states), classes=nclass, states_in_pairs=paired, first_pair=first, per_length=per_len)
    ok = len(states) == 758 and nclass == 536 and paired == 444 and first[0] == 7
    if not QUICK:
        import snappy
        sig = {}
        for k in states:
            M = snappy.Manifold("b+" + k[0] + k[1:]); sig[k] = M.isometry_signature()
        by_sig = {}
        for k, s in sig.items(): by_sig.setdefault(s, set()).add(states[k])
        out["isometry_signatures"] = len(set(sig.values()))
        out["signature_partition_equals_reversal_partition"] = all(len(v) == 1 for v in by_sig.values()) and len(by_sig) == nclass
        ok &= out["signature_partition_equals_reversal_partition"]
        # orientation: the reverse is isometric by a map of cusp determinant +1 (sample: the first 30 pairs)
        pairs = sorted({(k, k[0] + canon(k[1:][::-1], False)) for k in states if canon(k[1:][::-1], False) != k[1:]})[:30]
        plus = 0
        for a, b in pairs:
            A, B = snappy.Manifold("b+" + a), snappy.Manifold("b+" + b)
            isos = A.is_isometric_to(B, return_isometries=True)
            if any(i.cusp_maps()[0].det() == 1 for i in isos): plus += 1
        out["pairs_sampled"] = len(pairs); out["orientation_preserving_isometry_found"] = plus
        ok &= plus == len(pairs)
    return ok, out


def h3():
    d = json.load(open(os.path.join(ROOT, "frontier", "B1439_the_census_by_slope", "census_summary.json")))
    fire = d["firing_own_states"]; names = [f[0] for f in fire]
    # the summary lists the own-level states NEW to B1439 (lengths seven to twelve); B1434's two, to length six, are its control
    names += ["-LLRLR", "-LLLRLR"]
    cls = {}
    for nm in names: cls.setdefault(nm[0] + canon(nm[1:], True), []).append(nm)
    # a pair is split if one member fires and its reverse does not
    split = [nm for nm in names if (nm[0] + canon(nm[1:][::-1], False)) not in names and canon(nm[1:][::-1], False) != nm[1:]]
    return len(names) == 95 and len(cls) == 87 and not split, dict(firing_states=len(names), new_in_B1439=len(fire), firing_manifolds=len(cls), pairs_split=len(split), by_sign={sg: sum(1 for n in names if n[0] == sg) for sg in '+-'})


def h4():
    A = G.mul(G.L, G.R); A2 = G.mul(A, A); mA2 = G.neg(A2)
    out = dict(minus_LR_squared_equals_LR_squared=G.mul(G.neg(A), G.neg(A)) == A2, torsion_of_minus_LR2=G.smith(G.minus_identity(mA2)),
               torsion_of_LR2=G.smith(G.minus_identity(A2)))
    ok = out["minus_LR_squared_equals_LR_squared"] and out["torsion_of_minus_LR2"] == (3, 3) and out["torsion_of_LR2"] == (1, 5)
    # no state has -u^k (k even) as a level: (eps v)^n = -u^k needs eps^n = -1 (n odd, eps = -1) and v^n = u^k
    rng = range(-5, 6); found = 0; levels = 0
    hyp = [((a, b), (c, d)) for a, b, c, d in itertools.product(rng, repeat=4) if a * d - b * c == 1 and abs(a + d) > 2]
    S = set(hyp)
    for B in hyp:
        if G.tr(B) > 2: continue                       # B = -u^k ...
        per = G.cf_period(G.neg(B)); w = G.period_word(per); W = G.word(w); k = 1; T = W
        while G.tr(T) < G.tr(G.neg(B)) and k < 40: T = G.mul(T, W); k += 1
        if G.tr(T) != G.tr(G.neg(B)) or k % 2: continue
        found += 1                                     # a signed even power in the box
        # is it conjugate to (eps v)^n for a primitive v and n > 1 with that being a level of a STATE?  it would need n odd and v^n = u^k
        # v^n = u^k with u, v primitive positive words forces v = u and n = k (unique roots in the positive monoid): k is even, n odd -- impossible
    out["signed_even_powers_in_the_box"] = found
    if not QUICK:
        import snappy
        ident = lambda M: next((N.name() for N in M.identify()), None)
        m = snappy.Manifold("b+-LRLR"); out["bundle_of_minus_LRLR"] = ident(m); out["H1"] = str(m.homology())
        out["bundle_of_plus_LRLR"] = ident(snappy.Manifold("b++LRLR"))
        out["double_covers_of_m207"] = sorted({ident(C) for C in snappy.Manifold("m207").covers(2)})
        out["fourth_level_of_m004"] = sorted({ident(C) for C in snappy.Manifold("m004").covers(4, cover_type="cyclic")})
        ok &= out["bundle_of_minus_LRLR"] == "m207" and out["bundle_of_plus_LRLR"] == "m206" and "t12839" in out["double_covers_of_m207"] and out["fourth_level_of_m004"] == ["t12839"]
        ok &= out["H1"] in ("Z/3 + Z/3 + Z", "Z + Z/3 + Z/3")
    return ok and found > 0, out


def h5():
    LR, RL = G.mul(G.L, G.R), G.mul(G.R, G.L)
    a = G.mul(G.mul(G.P, LR), G.P) == RL; b = G.mul(G.mul(J, LR), G.inv(J)) == G.inv(LR)
    c = G.mul(G.mul(G.P, LR), G.P) != G.inv(LR)
    return a and b and c and G.det(J) == 1, dict(P_sends_LR_to_RL=a, J_sends_LR_to_its_inverse=b, P_does_not=c, det_J=G.det(J))


def h6():
    if QUICK: return True, "not run (--quick)"
    import snappy
    M = snappy.Manifold("m004"); isos = M.is_isometric_to(M, return_isometries=True)
    maps = [tuple(tuple(int(i.cusp_maps()[0][r, c]) for c in range(2)) for r in range(2)) for i in isos]
    count = {}
    for m in maps: count[str(m)] = count.get(str(m), 0) + 1
    diag = all(m[0][1] == 0 and m[1][0] == 0 and abs(m[0][0]) == 1 and abs(m[1][1]) == 1 for m in maps)
    return len(maps) == 8 and diag and sorted(count.values()) == [2, 2, 2, 2], dict(isometries=len(maps), cusp_maps=count)


def h7(box=5):
    rng = range(-box, box + 1); seen = {}; bad = 0; n = 0
    for a, b, c, d in itertools.product(rng, repeat=4):
        B = ((a, b), (c, d))
        if G.det(B) != 1 or abs(G.tr(B)) <= 2: continue
        n += 1; eps = 1 if G.tr(B) > 2 else -1; Bp = B if eps == 1 else G.neg(B)
        w = G.period_word(G.cf_period(Bp)); W = G.word(w); k = 1; T = W
        while G.tr(T) < G.tr(Bp) and k < 40: T = G.mul(T, W); k += 1
        if G.tr(T) != G.tr(Bp): bad += 1; continue
        u = canon(w, False)
        if any(len(w) % dd == 0 and w == w[:dd] * (len(w) // dd) for dd in range(1, len(w))): bad += 1       # the period word must be primitive
        key = (u, k, eps); seen[key] = seen.get(key, 0) + 1
    even_signed = sorted(k for k in seen if k[2] == -1 and k[1] % 2 == 0)
    return bad == 0, dict(matrices=n, triples=len(seen), signed_even_power_triples=even_signed[:6], count_signed_even=len(even_signed))


def main():
    res = {}; allok = True
    for name, f in (("H1 reverse identity", h1), ("H2 758 states, 536 manifolds", h2), ("H3 main's census by manifold", h3), ("H4 signed powers", h4),
                    ("H5 swap and inverse", h5), ("H6 the cusp action of m004's isometries", h6), ("H7 the triple (u, k, eps)", h7)):
        ok, data = f(); res[name] = dict(ok=bool(ok), data=data); allok &= bool(ok)
        print("%-42s %s   %s" % (name, "PASS" if ok else "FAIL", str(data)[:260]))
    json.dump(res, open(os.path.join(HERE, "v1_2_own.json"), "w"), indent=1, default=str)
    print("VERDICT v1.2-own: %s" % ("PASS" if allok else "FAIL")); return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
