"""B1517 -- the first sweep under SEE THE REPO FIRST, THEN THE LITERATURE, applied to GENESIS v1.0's census line.

GENESIS v1.0 section 3 counts 758 states to word length 12 (signed primitive words in L and R with both letters, up to rotation
and the L<->R swap; main's B1434/B1439 convention, re-derived by B1516 C4) and says each is realised as a once-punctured-torus
bundle. This script checks what those 758 realise.

  C1  the word states, as B1516 C4 and main count them: 758, i.e. twice OEIS A000048 summed over lengths 2..12
  C2  the same words up to rotation, swap AND reversal: 536, twice OEIS A000046; every class has one or two states; a pair is
      always a word and its reverse; the first pair is at length 7
  C3  SnapPy: isometry signatures of all 758 bundles give exactly 536 manifolds, and the partition is C2's
  C4  orientation: on every pair the reverse is orientation-preservingly isometric (a cusp map of determinant +1; equal
      Chern-Simons mod 1/2) and the swap is the mirror (an isometry of determinant -1; negated Chern-Simons)
  C5  main's B1439 firing list (quoted in main_B1439_firing_own_states.json) read by manifold: no pair is split, and the rate
      per manifold, with the split by reversal-closed and paired states at each length 7..12 (descriptive, not a test)
  C6  the identity underneath, exact over the integers: reverse(w) = (PJ) w^-1 (PJ)^-1 for every word to length 12, with
      det(PJ) = -1 (J = [[0,1],[-1,0]] gives w^T = J w^-1 J^-1; P = [[0,1],[1,0]] gives L^T = PLP = R)

    python3 census_by_manifold.py            # C1, C2, C5, C6 (pure integers, about a second)
    python3 census_by_manifold.py --snappy   # adds C3 and C4 (about a minute)
    python3 census_by_manifold.py --snappy --write   # and writes census_by_manifold_run.json
"""
import itertools
import json
import pathlib
import sys
import warnings

HERE = pathlib.Path(__file__).resolve().parent
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
P, J, I2 = ((0, 1), (1, 0)), ((0, 1), (-1, 0)), ((1, 0), (0, 1))
SW = str.maketrans("LR", "RL")
OEIS_A000048 = {2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 9, 8: 16, 9: 28, 10: 51, 11: 93, 12: 170}   # oeis.org/A000048, read 2026-10-02
OEIS_A000046 = {2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8, 8: 14, 9: 21, 10: 39, 11: 62, 12: 112}   # oeis.org/A000046, read 2026-10-02


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def word(w):
    M = I2
    for c in w:
        M = mul(M, L if c == "L" else R)
    return M


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):                                    # exact inverse of a matrix with determinant +-1
    d = det(A)
    return ((A[1][1] * d, -A[0][1] * d), (-A[1][0] * d, A[0][0] * d))


def primitive(w):
    n = len(w)
    return not any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n))


def rots(w):
    return [w[i:] + w[:i] for i in range(len(w))]


def canon_state(w):                            # B1516 C4's and main's convention: rotation and the swap
    return min(min(rots(x)) for x in (w, w.translate(SW)))


def canon_manifold(w):                         # rotation, swap and reversal
    xs = [w, w.translate(SW)]
    xs += [x[::-1] for x in xs]
    return min(min(rots(x)) for x in xs)


def mobius(n):
    m, k, res = n, 2, 1
    while k * k <= m:
        if m % k == 0:
            m //= k
            if m % k == 0:
                return 0
            res = -res
        k += 1
    return -res if m > 1 else res


def a000048(n):                                # own formula: (1/2n) sum over odd d | n of mu(d) 2^(n/d)
    return sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1, 2) if n % d == 0) // (2 * n)


def census(maxlen=12):
    per_len, states = {}, []
    for n in range(2, maxlen + 1):
        seen = set()
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if "L" in w and "R" in w and primitive(w):
                seen.add(canon_state(w))
        per_len[n] = len(seen)
        states += [s + w for w in sorted(seen) for s in "+-"]
    return per_len, states


def checks(with_snappy=False):
    rec = {}
    per_len, states = census()
    rec["C1 word states"] = len(states)
    rec["C1 per length (unsigned)"] = [per_len[n] for n in range(2, 13)]
    rec["C1 equals twice OEIS A000048, and the own Moebius formula agrees"] = (
        all(per_len[n] == OEIS_A000048[n] == a000048(n) for n in range(2, 13)) and len(states) == 2 * sum(OEIS_A000048.values()))
    classes = {}
    for s in states:
        classes.setdefault((s[0], canon_manifold(s[1:])), []).append(s)
    pairs = [v for v in classes.values() if len(v) == 2]
    m_len = {}
    for (sg, w) in classes:
        m_len[len(w)] = m_len.get(len(w), 0) + (sg == "+")
    rec["C2 classes under rotation, swap and reversal"] = len(classes)
    rec["C2 per length (unsigned)"] = [m_len[n] for n in range(2, 13)]
    rec["C2 equals twice OEIS A000046"] = (all(m_len[n] == OEIS_A000046[n] for n in range(2, 13))
                                          and len(classes) == 2 * sum(OEIS_A000046.values()))
    rec["C2 class sizes"] = sorted({len(v) for v in classes.values()})
    rec["C2 reversal pairs"] = len(pairs)
    rec["C2 every pair is a word and its reverse"] = all(
        canon_state(a[1:][::-1]) == b[1:] and a[0] == b[0] for a, b in pairs)
    rec["C2 first pair"] = min(pairs, key=lambda v: (len(v[0]), v))
    # C6: the identity, exact
    PJ = mul(P, J)
    tot = ok = 0
    for n in range(1, 13):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            tot += 1
            ok += word(w[::-1]) == mul(mul(PJ, inv(word(w))), inv(PJ))
    rec["C6 words checked"] = tot
    rec["C6 reverse(w) = (PJ) w^-1 (PJ)^-1 on every word"] = ok == tot
    rec["C6 det(PJ)"] = det(PJ)
    rec["C6 transpose identity L^T = PLP = R"] = (((1, 0), (1, 1)) == mul(mul(P, L), P) == R)
    # C5: main's firing list, read by manifold
    main = json.loads((HERE / "main_B1439_firing_own_states.json").read_text(encoding="utf-8"))
    fire = {e[0] for e in main["firing_own_states"]}
    rec["C5 main's firing own-level states (lengths 7-12), quoted"] = len(fire)
    rec["C5 every firing state is a census state"] = fire <= set(states)
    rec["C5 pairs split by main's census (one member fires, the other not)"] = [v for v in pairs if (v[0] in fire) != (v[1] in fire)]
    fire_cls = {(f[0], canon_manifold(f[1:])) for f in fire}
    rec["C5 firing manifolds (lengths 7-12)"] = len(fire_cls)
    rec["C5 rate per word state (with main B1434's two at lengths 2-6)"] = [len(fire) + 2, len(states)]
    rec["C5 rate per manifold (with main B1434's two at lengths 2-6)"] = [len(fire_cls) + 2, len(classes)]
    split = []
    for n in range(7, 13):
        ws = sorted({s[1:] for s in states if len(s) == n + 1})
        closed = [w for w in ws if canon_state(w[::-1]) == w]
        paired = [w for w in ws if canon_state(w[::-1]) != w]
        for sg in "+-":
            split.append({"length": n, "sign": sg, "reversal-closed states": len(closed),
                          "firing": sum(sg + w in fire for w in closed), "paired states": len(paired),
                          "firing ": sum(sg + w in fire for w in paired)})
    rec["C5 split by length and sign (descriptive; not a test)"] = split
    c_tot = sum(r["reversal-closed states"] for r in split)
    c_f = sum(r["firing"] for r in split)
    p_tot = sum(r["paired states"] for r in split)
    p_f = sum(r["firing "] for r in split)
    rec["C5 lengths 7-12: reversal-closed firing / states, paired firing / states"] = [c_f, c_tot, p_f, p_tot]
    if with_snappy:
        warnings.filterwarnings("ignore")
        import snappy

        def man(s):
            return snappy.Manifold(("b++" if s[0] == "+" else "b+-") + s[1:])
        sig, fails = {}, []
        for s in states:
            try:
                sig[s] = man(s).isometry_signature()
            except Exception:
                fails.append(s)
        by = {}
        for k, v in sig.items():
            by.setdefault(v, []).append(k)
        rec["C3 snappy"] = snappy.__version__
        rec["C3 signature failures"] = fails
        rec["C3 distinct manifolds by isometry signature"] = len(by)
        rec["C3 partition equals C2's"] = (sorted(sorted(v) for v in by.values())
                                         == sorted(sorted(v) for v in classes.values()))

        def dets(a, b):
            isos = man(a).is_isometric_to(man(b), return_isometries=True)
            return sorted({int(round(float(m.det()))) for i in isos for m in i.cusp_maps()})

        def cs_close(x, y):
            d = abs(x - y) % 0.5
            return min(d, 0.5 - d) < 1e-8
        rev_pres = swap_rev = swap_only_rev = cs_rev = cs_swap = 0
        for a, _ in pairs:
            sg, w = a[0], a[1:]
            r, q = sg + w[::-1], sg + w.translate(SW)
            rev_pres += 1 in dets(a, r)
            d = dets(a, q)
            swap_rev += -1 in d
            swap_only_rev += d == [-1]
            ca, cr, cq = (float(man(x).chern_simons()) for x in (a, r, q))
            cs_rev += cs_close(ca, cr)
            cs_swap += cs_close(ca, -cq)
        rec["C4 pairs"] = len(pairs)
        rec["C4 reverse orientation-preservingly isometric (cusp map det +1)"] = rev_pres
        rec["C4 Chern-Simons equal for the reverse (mod 1/2)"] = cs_rev
        rec["C4 swap has an orientation-reversing isometry (det -1)"] = swap_rev
        rec["C4 swap has only orientation-reversing isometries"] = swap_only_rev
        rec["C4 Chern-Simons negated for the swap (mod 1/2)"] = cs_swap
    passed = (rec["C1 word states"] == 758 and rec["C1 equals twice OEIS A000048, and the own Moebius formula agrees"]
              and rec["C2 classes under rotation, swap and reversal"] == 536 and rec["C2 equals twice OEIS A000046"]
              and rec["C2 class sizes"] == [1, 2] and rec["C2 reversal pairs"] == 222
              and rec["C2 every pair is a word and its reverse"] and rec["C6 reverse(w) = (PJ) w^-1 (PJ)^-1 on every word"]
              and rec["C6 det(PJ)"] == -1 and rec["C5 every firing state is a census state"]
              and rec["C5 pairs split by main's census (one member fires, the other not)"] == [])
    if with_snappy:
        passed = passed and (rec["C3 signature failures"] == [] and rec["C3 distinct manifolds by isometry signature"] == 536
                             and rec["C3 partition equals C2's"] and rec["C4 reverse orientation-preservingly isometric "
                                                                         "(cusp map det +1)"] == 222
                             and rec["C4 Chern-Simons equal for the reverse (mod 1/2)"] == 222
                             and rec["C4 swap has an orientation-reversing isometry (det -1)"] == 222
                             and rec["C4 Chern-Simons negated for the swap (mod 1/2)"] == 222)
    rec["passed"] = passed
    return rec


if __name__ == "__main__":
    rec = checks(with_snappy="--snappy" in sys.argv)
    text = json.dumps(rec, indent=1, ensure_ascii=False)
    print(text)
    if "--write" in sys.argv:
        (HERE / "census_by_manifold_run.json").write_text(text + "\n", encoding="utf-8")
    sys.exit(0 if rec["passed"] else 1)
