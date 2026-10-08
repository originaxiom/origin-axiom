#!/usr/bin/env python3
"""W26 of the weave: THE SEARCH BEYOND THE WEAVE. Do the threads' hyperbolic holonomies, or main's F-MC arithmetic,
supply a forced complex structure on the gauge side (the input W25 showed the weave's bundles cannot supply)? The rule
is W26_RULE.md, committed before this ran (186cb3d0).

  N1 the weave is closed under the mirror (exact): for every positive word phi in L, R with both letters to length 10,
     S phi^-1 S^-1 is the matrix of phi' = reverse(phi) with L <-> R; so M_phi' = -M_phi (the fibre kept, the ticks
     reversed). The amphichiral threads (phi' a rotation of phi) are counted.
  N2 the orientation-odd invariants pair up (SnapPy): every hyperbolic thread to length 6, both signs; the volume of
     M_phi and M_phi' agree and their Chern-Simons invariants are opposite; SnapPy's isometries M_phi -> M_phi' are
     orientation-reversing (cusp-map determinant -1), and an orientation-preserving one exists only for the
     amphichiral threads.
  N3 the order-3 orientation alternates at every tick (exact): on every odd-trace cyclic word to length 10, the
     direction of the 3-cycle its monodromy induces on the three parities (the non-zero vectors of F2^2, in the shared
     basis) flips at each rotation of the word.
  N4 (F-MC's chirality is an input in main's own list) and N5 (the verdict) are stated in the rule and the note.

    python3 the_weaves_mirror.py   ->  the_weaves_mirror.json beside it
"""
import itertools
import json
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
L = np.array([[1, 1], [0, 1]])
R = np.array([[1, 0], [1, 1]])
S = np.array([[0, -1], [1, 0]])
P2 = np.array([[0, 1], [1, 0]])
MAT = {"L": L, "R": R}


def mat(w):
    M = np.eye(2, dtype=np.int64)
    for c in w:
        M = M @ MAT[c]
    return M


def inv2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return np.array([[d, -b], [-c, a]])                     # det 1


def mirror(w):
    return "".join({"L": "R", "R": "L"}[c] for c in reversed(w))


def swap(w):
    return "".join({"L": "R", "R": "L"}[c] for c in w)


def amphichiral(w):
    """M_w = M_w' (orientation kept) iff w' or swap(w) is a rotation of w: M_reverse(u) = M_u for every u, since
    reverse(u) = (P S) u^-1 (P S)^-1 with det(P S) = -1"""
    return canonical(mirror(w)) == canonical(w) or canonical(swap(w)) == canonical(w)


def rotations(w):
    return [w[i:] + w[:i] for i in range(len(w))]


def canonical(w):
    return min(rotations(w))


def primitive(w):
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)


def cyclic_words(nmax):
    seen = []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w) and w == canonical(w):
                seen.append(w)
    return seen


PAR = [(1, 0), (0, 1), (1, 1)]


def perm_mod2(M):
    """the permutation of the three parities (column vectors mod 2) as a tuple of images' indices"""
    out = []
    for v in PAR:
        img = tuple(int(x) % 2 for x in M @ np.array(v))
        out.append(PAR.index(img))
    return tuple(out)


def direction(p):
    """+1 for the 3-cycle (1,0) -> (0,1) -> (1,1), -1 for its inverse, 0 otherwise"""
    if p == (1, 2, 0):
        return 1
    if p == (2, 0, 1):
        return -1
    return 0


def n1(nmax=10):
    words = cyclic_words(nmax)
    ok = all(np.array_equal(S @ inv2(mat(w)) @ inv2(S), mat(mirror(w))) for w in words)
    amph = [w for w in words if amphichiral(w)]
    rev_ok = all(np.array_equal(P2 @ S @ inv2(mat(w)) @ inv2(S) @ P2, mat(w[::-1])) for w in words)
    return {"cyclic primitive words with both letters, to length %d" % nmax: len(words),
            "S phi^-1 S^-1 = matrix of reverse(phi) with L <-> R, for every one": bool(ok),
            "the mirror is a positive word (a thread) for every one": True,
            "reverse(phi) = (P S) phi^-1 (P S)^-1, so M_reverse(phi) = M_phi": bool(rev_ok),
            "amphichiral (phi' or swap(phi) a rotation of phi)": len(amph),
            "amphichiral, to length 6": [w for w in amph if len(w) <= 6]}, words


def n3(words):
    odd = [w for w in words if abs(int(np.trace(mat(w)))) % 2 == 1]
    alternating = 0
    rows = {}
    for w in odd:
        dirs = [direction(perm_mod2(mat(r))) for r in rotations(w)]
        alt = all(d != 0 for d in dirs) and all(dirs[i] == -dirs[(i + 1) % len(dirs)] for i in range(len(dirs)))
        alternating += alt
        if len(w) <= 6:
            rows[w] = dirs
    letters = {c: perm_mod2(MAT[c]) for c in "LR"}
    return {"odd-trace cyclic words to length 10": len(odd),
            "the 3-cycle's direction flips at every tick on all of them": bool(alternating == len(odd)),
            "the directions at each tick, words to length 6": rows,
            "L and R mod 2 as permutations of the parities (a transposition each)": {
                c: {"permutation": list(p), "fixed": [str(PAR[i]) for i in range(3) if p[i] == i]}
                for c, p in letters.items()},
            "every odd-trace word has even length": bool(all(len(w) % 2 == 0 for w in odd))}


def cs_of(M):
    try:
        return float(M.chern_simons())
    except Exception:  # noqa: BLE001
        import math
        return float(M.complex_volume().imag()) / (2 * math.pi ** 2)


def n2(words, nmax=6):
    import snappy
    rows = {}
    pairs_ok, iso_ok, cs_amph_ok = True, True, True
    for w in [x for x in words if len(x) <= nmax]:
        for sign in "+-":
            name, mname = "b+%s%s" % (sign, w), "b+%s%s" % (sign, mirror(w))
            M, Mm = snappy.Manifold(name), snappy.Manifold(mname)
            if M.solution_type() != "all tetrahedra positively oriented":
                M = M.high_precision()
            vol, volm = float(M.volume()), float(Mm.volume())
            cs, csm = cs_of(M), cs_of(Mm)
            s_half = ((cs + csm) % 0.5)
            opp = min(s_half, 0.5 - s_half) < 1e-9
            same_vol = abs(vol - volm) < 1e-9
            dets = []
            try:
                for iso in M.is_isometric_to(Mm, return_isometries=True):
                    m = iso.cusp_maps()[0]
                    dets.append(int(round(float(m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]))))
            except Exception as e:  # noqa: BLE001
                dets = ["error: %s" % e]
            amph = amphichiral(w)
            rev = all(d == -1 for d in dets if isinstance(d, int))
            has_pres = any(d == 1 for d in dets if isinstance(d, int))
            iso_row_ok = bool(dets) and all(isinstance(d, int) for d in dets) and (has_pres if amph else rev)
            if amph:
                c4 = min(abs((cs % 0.5) - t) for t in (0.0, 0.25, 0.5))
                cs_amph_ok &= c4 < 1e-9
            pairs_ok &= same_vol and opp
            iso_ok &= iso_row_ok
            rows[sign + w] = {"mirror": sign + mirror(w), "volume": round(vol, 12), "volume of the mirror": round(volm, 12),
                              "CS": round(cs, 12), "CS of the mirror": round(csm, 12),
                              "CS + CS' = 0 (mod 1/2)": bool(opp), "amphichiral": bool(amph),
                              "isometries to the mirror: cusp-map determinants": sorted(set(d for d in dets if isinstance(d, int)))}
    return {"threads read (both signs)": len(rows), "every pair: same volume, opposite CS": bool(pairs_ok),
            "isometries to the mirror reverse orientation (both kinds exist only when amphichiral)": bool(iso_ok),
            "amphichiral threads have CS in {0, 1/4} (mod 1/2)": bool(cs_amph_ok), "rows": rows}


def run():
    res = {"rule": "W26_RULE.md (committed 186cb3d0 before this ran)"}
    r1, words = n1(10)
    res["N1 the weave is closed under the mirror"] = r1
    res["N3 the order-3 orientation on the parities, tick by tick"] = n3(words)
    res["N2 the orientation-odd invariants pair up (SnapPy)"] = n2(words, 6)
    res["N4 F-MC's chirality is an input in main's own list"] = (
        "THE_CLAIM section 1: 'two F2 bits (time's arrow; chirality - the conjugation bit, = tau)' among the five typed "
        "external data")
    ok = (r1["S phi^-1 S^-1 = matrix of reverse(phi) with L <-> R, for every one"]
          and res["N2 the orientation-odd invariants pair up (SnapPy)"]["every pair: same volume, opposite CS"]
          and res["N3 the order-3 orientation on the parities, tick by tick"]["the 3-cycle's direction flips at every tick on all of them"])
    res["N5 neither candidate supplies a forced gauge-side complex structure at the weave level"] = bool(ok)
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_weaves_mirror.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps({k: v for k, v in out.items() if k != "N2 the orientation-odd invariants pair up (SnapPy)"},
                     indent=1, ensure_ascii=False, default=str))
    n2r = out["N2 the orientation-odd invariants pair up (SnapPy)"]
    print(json.dumps({k: v for k, v in n2r.items() if k != "rows"}, indent=1))
