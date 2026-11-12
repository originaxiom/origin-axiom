#!/usr/bin/env python3
"""WP-1.5, first step; harvest row 916 on main: what the parities carry at the tick where the weave separates them.

THE STATEMENT (the SM seat's W7, at its commit; read as a statement, none of its code run)
  Every state to word length 6 (24 of them) is read at its resolving tick: 3 at odd trace, 2 where the act is an
  involution modulo 2, 1 where it is the identity modulo 2.  The characters read are those of the tick whose restriction
  to the fibre is a parity, with the value kappa on the stable letter a twelfth root of unity.  A member has n > 0.
  Found by the seat: no member on any odd-trace state; on +-LLR and +-LLLLR members on exactly two of the three non-zero
  parities, with (h1, r1, n) = (2, 1, 1), and none on the third; none on +-LLLRR and +-LLRLR; on +-LLRR members on two
  parities and none on the third; none on +-LLLLRR; no member at the zero parity anywhere.
WHAT MAIN COMPUTES, with its own instrument (kernel_site.py: the tick is the kernel of eps modulo n, built from the
base's own presentation; the reading is B1492's)
  The characters with fibre restriction of order at most 2 are exactly sigma * kappa^eps', sigma a sign character of the
  tick and eps' the tick's map to Z; two of them coincide when sigma differs by (-1)^eps' and kappa by -1.  So there are
  4 x 12 = 48, in four classes: the zero parity (sigma trivial on the fibre) and three others.  Which of the three is
  which is not labelled here; what is compared is the pattern over the three.  kappa's sign depends on the stable
  letter chosen within a class, so "at kappa = 1" in the seat's table is compared as "at one value of kappa".
HOW IT COULD FAIL: the tick must have b1 = 1; the classes must be four of twelve characters each; the planted case reads
the trivial character, which must give h1 = 1 on the end and no member (Lemma V)."""
import sys, json, time, pathlib, collections, itertools
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1602_the_forced_cover_on_every_thread" / "verification"))
import snappy
import kernel_site as KS
import forced_every as FE

WORDS = ["LR", "LLR", "LLLR", "LLRR", "LLLLR", "LLLRR", "LLRLR", "LLLLLR", "LLLLRR", "LLLRLR", "LLLRRR", "LLRLRR"]
TICK = {3: 3, 1: 2, 0: 1}                                    # FE.parity_class: 3 a 3-cycle, 1 fixes one parity, 0 fixes all
OUT = HERE / "the_parity_sectors_on_main.jsonl"


def state(name):
    M = snappy.Manifold(name); G = M.high_precision().fundamental_group(); eps = FE.z_map(G)
    n = TICK[FE.parity_class(name[3:])]
    q = {g: eps[g] % n for g in G.generators()}
    K = KS.Kernel(M, q, lambda a, b: (a + b) % n, lambda a: (-a) % n, 0, label=name)
    epsK = [sum((1 if c.islower() else -1) * eps[c.lower()] for c in w) for w in K.gen_words]
    assert all(v % n == 0 for v in epsK); epsK = [v // n for v in epsK]
    assert all(sum(epsK[k] * s for k, s in r) == 0 for r in K.rels), "eps' is not a map of the tick"
    return K, n, epsK


def characters(K, epsK):
    """{exponent vector mod 24: (class, k)}: sigma * kappa^eps', kappa = zeta_12^k; the class is sigma modulo (-1)^eps'"""
    signs = K.characters(2); par = tuple(v % 2 for v in epsK)
    cls = {}
    for s in signs:
        key = min(s, tuple((a + b) % 2 for a, b in zip(s, par)))
        cls.setdefault(key, len(cls))
    assert len(signs) == 8 and len(cls) == 4, ("the tick has not eight sign characters in four classes", len(signs), len(cls))
    zero = min(tuple([0] * K.n), par); out = {}
    for s in signs:
        c = min(s, tuple((a + b) % 2 for a, b in zip(s, par)))
        for k in range(12):
            e = tuple((12 * a + 2 * k * b) % 24 for a, b in zip(s, epsK))
            out.setdefault(e, ("zero" if c == zero else "parity %d" % cls[c], s, k))
    assert len(out) == 48, len(out)
    return out


if __name__ == "__main__":
    names = sys.argv[1:] or ["b+%s%s" % (s, w) for w in WORDS for s in "+-"]
    done = {}
    if OUT.exists():
        for l in OUT.read_text().split("\n"):
            if l.strip():
                r = json.loads(l); done[(r["state"], tuple(r["e"]))] = r
    with open(OUT, "a") as fh:
        for name in names:
            t0 = time.time(); K, n, epsK = state(name); chars = characters(K, epsK); new = 0
            for e, (c, s, k) in sorted(chars.items(), key=lambda kv: (kv[1][0], kv[1][2])):
                if (name, e) in done: continue
                r = K.counts_mp(e, 24)
                row = {"state": name, "tick": n, "class": c, "k": k, "sigma": list(s), "e": list(e), "a1": r["a1"], "r1": r["r1"], "n": r["n"], "t0": r["t0"]}
                fh.write(json.dumps(row) + "\n"); fh.flush(); done[(name, e)] = row; new += 1
            mine = [r for (st, _), r in done.items() if st == name]
            mem = collections.defaultdict(list)
            for r in mine:
                if r["n"] > 0: mem[r["class"]].append((r["k"], (r["a1"], r["r1"], r["n"])))
            print("%-12s tick %d, %d generators, %d cusps; members by class: %s  (%d read now, %.0fs)" % (name, n, K.n, len(K.cusps), {c: sorted(v) for c, v in sorted(mem.items())} or "none", new, time.time() - t0), flush=True)
